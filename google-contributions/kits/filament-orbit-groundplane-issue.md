**Title:** camutils ORBIT: default ground plane is wrong when target isn't at origin

**Describe the bug**
When an ORBIT manipulator is built without `groundPlane()`, `OrbitManipulator::setProperties()` builds a default plane "so that it aligns with the targetPosition position". It uses `-length(targetPosition)` as the plane's `w`. `raycastPlane()` treats `w` as the distance along the normal (`p0 = n * plane[3]`), so the plane only passes through the target when the target is at the origin.

In the repro, with target `(0,0,10)` and home `(0,0,20)`, a raycast through the viewport centre hits `z = -10` instead of `z = 10`. Panning 40 px moves the camera by 2.79 units, versus 0.93 units for the same camera setup with the target at the origin.

**To Reproduce**
`orbit_repro.cpp`:
```cpp
#include <camutils/Manipulator.h>
#include <cstdio>
#include <initializer_list>

using namespace filament::math;
using namespace filament::camutils;
using M = Manipulator<float>;

int main() {
    float3 eye, target, up, hit;

    // 1. ORBIT with no explicit groundPlane(): raycast through the viewport centre.
    for (float3 t : { float3{0, 0, 10}, float3{3, 4, 0} }) {
        M* m = M::Builder()
                .viewport(256, 256)
                .targetPosition(t.x, t.y, t.z)
                .orbitHomePosition(t.x, t.y, t.z + 10)
                .build(Mode::ORBIT);
        bool ok = m->raycast(128, 128, &hit);
        printf("target (%g, %g, %g): raycast ok=%d hit=(%g, %g, %g)\n",
                t.x, t.y, t.z, ok, hit.x, hit.y, hit.z);
        delete m;
    }

    // 2. Same camera/target distance (10), same 40 px pan, target at z=0 vs z=10.
    for (float tz : { 0.0f, 10.0f }) {
        M* m = M::Builder()
                .viewport(256, 256)
                .targetPosition(0, 0, tz)
                .orbitHomePosition(0, 0, tz + 10)
                .build(Mode::ORBIT);
        m->grabBegin(128, 128, true);   // strafe = pan
        m->grabUpdate(168, 128);
        m->grabEnd();
        m->getLookAt(&eye, &target, &up);
        printf("target z=%g: 40 px pan moved the eye by x=%g\n", tz, eye.x);
        delete m;
    }

    // 3. MAP with no groundPlane().
    M* m = M::Builder().viewport(256, 256).build(Mode::MAP);
    m->getLookAt(&eye, &target, &up);
    printf("MAP default: eye=(%g, %g, %g) target=(%g, %g, %g) up=(%g, %g, %g)\n",
            eye.x, eye.y, eye.z, target.x, target.y, target.z, up.x, up.y, up.z);
    delete m;
}
```
Built against a desktop debug build (`./build.sh -p desktop debug`, clang 18, libc++) at a5e4a836:
```sh
F=/path/to/filament
B=$F/out/cmake-debug
clang++ -std=c++17 -stdlib=libc++ -g \
  -I$F/libs/camutils/include -I$F/libs/utils/include -I$F/libs/math/include \
  orbit_repro.cpp -o orbit_repro \
  $B/libs/camutils/libcamutils.a $B/libs/utils/libutils.a $B/libs/math/libmath.a -lpthread -ldl
./orbit_repro
```

**Expected behavior**
- The centre raycast hits (about) the target: `z = 10` in the first case and `z = 0` in the second.
- The 40 px pan moves the eye by the same amount whether the target is at z = 0 or z = 10, since the eye-to-target distance is the same.

**Screenshots**
N/A

**Logs**
```
target (0, 0, 10): raycast ok=1 hit=(0.0347125, 0.0347125, -10)
target (3, 4, 0): raycast ok=1 hit=(3.01736, 4.01736, -5)
target z=0: 40 px pan moved the eye by x=-0.927522
target z=10: 40 px pan moved the eye by x=-2.79376
MAP default: eye=(0, 0, 0) target=(0, 0, 0) up=(-nan, -nan, -nan)
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; the repro doesn't render)
 - Backend: N/A

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
[OrbitManipulator.h#L60-L66](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/camutils/src/OrbitManipulator.h#L60-L66):
```cpp
        // By default, place the ground plane so that it aligns with the targetPosition position.
        // This is used only when PANNING.
        if (resolved.groundPlane == vec4(0)) {
            const FLOAT d = length(resolved.targetPosition);
            const vec3 n = normalize(resolved.orbitHomePosition - resolved.targetPosition);
            resolved.groundPlane = vec4(n, -d);
        }
```
[Manipulator.cpp#L220-L227](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/camutils/src/Manipulator.cpp#L220-L227) (`raycastPlane`):
```cpp
    const vec4 plane = props->groundPlane;
    const vec3 n = vec3(plane[0], plane[1], plane[2]);
    const vec3 p0 = n * plane[3];
    const FLOAT denom = -dot(n, dir);
    if (denom > 1e-6) {
        const vec3 p0l0 = p0 - origin;
        *t = dot(p0l0, n) / -denom;
        return *t >= 0;
```
With `p0 = n * w`, the plane is `dot(n, p) = w`. For it to contain the target, `w` would be `dot(n, targetPosition)`. For target `(0,0,10)` and `n = (0,0,1)`, the current code gives `w = -10`, which matches the `z = -10` hit above. In the pan case, I think the 3x comes from the grab point being 30 units from the eye instead of 10, but I haven't traced the pan math in detail.

One possible fix is `resolved.groundPlane = vec4(n, dot(n, resolved.targetPosition));`.

Related (last line of the log): a MAP manipulator built without `groundPlane()` ends up with `eye == target` and a NaN up vector. `MapManipulator` uses `groundPlane.xyz` as the target-to-eye direction ([MapManipulator.h#L41-L46](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/camutils/src/MapManipulator.h#L41-L46)), and nothing gives it a default the way ORBIT does. I'm not sure whether MAP is meant to require `groundPlane()`. If it is, a precondition or a note in the Builder docs might help. I can split this into its own issue if you prefer.

I'd be happy to send a PR if this is something you'd like fixed.
