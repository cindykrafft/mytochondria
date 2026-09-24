**Title:** image::compare() returns 0 when the first image is larger than the second

**Describe the bug**
`image::compare(a, b, epsilon)` in libimage is declared as "Lexicographically compares two images, similar to memcmp." It returns the `bool` result of `std::lexicographical_compare(a, b, x < y - epsilon)`. That is 1 when `a` sorts before `b`, and 0 otherwise. So 0 comes back both when the images match and when the first differing value is larger in `a`. For example, `compare({1,0}, {0,0})` and `compare({0,5}, {0,0})` both return 0.

`image::updateOrCompare()` in libimageio treats 0 as a match:
```cpp
FILAMENT_CHECK_PRECONDITION(compare(limgResult, limgGolden, epsilon) == 0) << "Image mismatch.";
```
As far as I can tell, that means a golden-image comparison passes when the first value (in pixel/channel order) that differs by more than `epsilon` is larger in the result than in the golden.

**To Reproduce**
`compare_repro.cpp`:
```cpp
#include <image/ImageOps.h>
#include <image/LinearImage.h>
#include <cstdio>

using namespace image;

static LinearImage pixels(float p0, float p1) {
    LinearImage img(2, 1, 1);
    img.getPixelRef()[0] = p0;
    img.getPixelRef()[1] = p1;
    return img;
}

int main() {
    printf("compare({0,0}, {0,0})      = %d\n", compare(pixels(0, 0), pixels(0, 0)));
    printf("compare({0,0}, {1,0})      = %d\n", compare(pixels(0, 0), pixels(1, 0)));
    printf("compare({1,0}, {0,0})      = %d\n", compare(pixels(1, 0), pixels(0, 0)));
    printf("compare({0,5}, {0,0})      = %d\n", compare(pixels(0, 5), pixels(0, 0)));
    printf("compare({0.9,0}, {0,0}, 0.1) = %d\n", compare(pixels(0.9f, 0), pixels(0, 0), 0.1f));
}
```
Built against a desktop debug build (`./build.sh -p desktop debug`, clang 18, libc++) at a5e4a836:
```sh
F=/path/to/filament
B=$F/out/cmake-debug
clang++ -std=c++17 -stdlib=libc++ -g \
  -I$F/libs/image/include -I$F/libs/utils/include -I$F/libs/math/include \
  compare_repro.cpp -o compare_repro \
  $B/libs/image/libimage.a $B/libs/utils/libutils.a $B/libs/math/libmath.a -lpthread -ldl
./compare_repro
```

**Expected behavior**
Going by "similar to memcmp", I'd expect a non-zero result whenever the images differ by more than `epsilon`: a negative value when `a < b` and a positive one when `a > b`. The last three lines should not be 0.

**Screenshots**
N/A

**Logs**
```
compare({0,0}, {0,0})      = 0
compare({0,0}, {1,0})      = 1
compare({1,0}, {0,0})      = 0
compare({0,5}, {0,0})      = 0
compare({0.9,0}, {0,0}, 0.1) = 0
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; the repro doesn't render)
 - Backend: N/A

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
Declaration, [ImageOps.h#L60-L61](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/image/include/image/ImageOps.h#L60-L61):
```cpp
// Lexicographically compares two images, similar to memcmp.
UTILS_PUBLIC int compare(const LinearImage& a, const LinearImage& b, float epsilon = 0.0f);
```
Implementation, [ImageOps.cpp#L235-L246](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/image/src/ImageOps.cpp#L235-L246):
```cpp
int compare(const LinearImage& a, const LinearImage& b, float epsilon) {
    ...
    if (b.getWidth() != w || b.getHeight() != h || b.getChannels() != c) {
        return -1;
    }
    ...
    return std::lexicographical_compare(adata, adata + w * h * c, bdata, bdata + w * h * c,
            [epsilon](float x, float y) { return x < y - epsilon; });
}
```
Caller, [ImageDiffer.cpp#L69-L70](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/imageio/src/ImageDiffer.cpp#L69-L70) (`updateOrCompare`, which is used by `libs/image/tests/test_image.cpp` and `tools/cmgen/tests/test_cmgen.cpp`):
```cpp
// Perform a simple comparison of the two images.
FILAMENT_CHECK_PRECONDITION(compare(limgResult, limgGolden, epsilon) == 0) << "Image mismatch.";
```
I haven't checked whether any current golden images in those tests would start failing with a two-sided check.

One possible fix is to walk both buffers and return -1 or +1 at the first element where `x < y - epsilon` or `x > y + epsilon`, and 0 if there is none. That keeps the memcmp-like contract and makes `== 0` mean "equal within epsilon". The size-mismatch case already returns -1, so callers checking `== 0` would still treat it as a mismatch.

I'd be happy to send a PR if this is something you'd like fixed.
