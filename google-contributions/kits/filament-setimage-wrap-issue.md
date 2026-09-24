**Title:** Texture::setImage offset + size bounds checks can wrap around in uint32_t

**Describe the bug**
`FTexture::setImageCommon()` checks the upload region with `xoffset + width <= ...`, `yoffset + height <= ...` and `zoffset + depth <= ...`, all in `uint32_t`. When the offset is close to `UINT32_MAX` the sum wraps to a small number and the check passes. On a 4x4 texture, `setImage(..., xoffset = 0xFFFFFFFF, ..., width = 2, ...)` is accepted, while `xoffset = 5, width = 1` is rejected as expected.

**To Reproduce**
`setimage_wrap.cpp`:
```cpp
#include <filament/Engine.h>
#include <filament/Texture.h>
#include <utils/Panic.h>
#include <cstdio>
#include <cstdlib>
using namespace filament;

static void tryUpload(Engine& engine, Texture* tex, uint32_t x, uint32_t y,
        uint32_t w, uint32_t h, const char* label) {
    size_t const size = 4 * 4 * 4;
    try {
        tex->setImage(engine, 0, x, y, 0, w, h, 1,
                Texture::PixelBufferDescriptor(malloc(size), size,
                        Texture::Format::RGBA, Texture::Type::UBYTE,
                        [](void* buffer, size_t, void*) { free(buffer); }));
        printf("%s: accepted\n", label);
    } catch (utils::PreconditionPanic const& e) {
        printf("%s: rejected\n", label);
    }
}

int main() {
    Engine* engine = Engine::create(Engine::Backend::NOOP);
    Texture* tex = Texture::Builder().width(4).height(4).levels(1)
            .format(Texture::InternalFormat::RGBA8).build(*engine);
    tryUpload(*engine, tex, 5, 0, 1, 1, "xoffset=5, width=1");
    tryUpload(*engine, tex, 0xFFFFFFFFu, 0, 2, 1, "xoffset=0xFFFFFFFF, width=2");
    tryUpload(*engine, tex, 0, 0xFFFFFFFEu, 1, 3, "yoffset=0xFFFFFFFE, height=3");
    engine->destroy(tex);
    Engine::destroy(&engine);
}
```
Built against a desktop debug build (`./build.sh -p desktop debug`, clang 18, libc++) at a5e4a836:
```sh
F=/path/to/filament
B=$F/out/cmake-debug
clang++ -std=c++20 -stdlib=libc++ -g \
  -I$F/filament/include -I$F/filament/backend/include \
  -I$F/libs/filabridge/include -I$F/libs/utils/include -I$F/libs/math/include \
  setimage_wrap.cpp -o setimage_wrap \
  -Wl,--start-group $B/filament/libfilament.a $B/filament/backend/libbackend.a \
    $B/libs/bluegl/libbluegl.a $B/libs/bluevk/libbluevk.a \
    $B/libs/filaflat/libfilaflat.a $B/libs/filabridge/libfilabridge.a \
    $B/libs/math/libmath.a $B/libs/utils/libutils.a \
    $B/third_party/smol-v/tnt/libsmol-v.a $B/third_party/zstd/tnt/libzstd.a \
    $B/shaders/libshaders.a \
  -Wl,--end-group -ldl -lpthread
./setimage_wrap
```

**Expected behavior**
The second and third calls should fail the precondition check, as the first one does.

**Screenshots**
N/A

**Logs**
```
Using 'soft' CircularBuffer (12288 KiB)
FEngine (64 bits) created at 0x561109bb6b40 (threading is enabled)
FEngine resolved backend: Noop
Backend feature level: 1
FEngine feature level: 1
xoffset=5, width=1: rejected
xoffset=0xFFFFFFFF, width=2: accepted
yoffset=0xFFFFFFFE, height=3: accepted
CircularBuffer: High watermark 0 KiB (0%)
FEngine::mHeapAllocator arena: High watermark 1216 bytes
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; the repro uses the Noop backend)
 - Backend: Noop

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
The checks are in [`filament/src/details/Texture.cpp#L476`](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/Texture.cpp#L476), [`#L481`](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/Texture.cpp#L481) and [`#L510`](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/Texture.cpp#L510), with `uint32_t` parameters:
```cpp
FILAMENT_CHECK_PRECONDITION(xoffset + width <= valueForLevel(level, mWidth))
...
FILAMENT_CHECK_PRECONDITION(yoffset + height <= valueForLevel(level, mHeight))
...
FILAMENT_CHECK_PRECONDITION(zoffset + depth <= effectiveTextureDepthOrLayers)
```
After these checks, `setImage()` passes the same offsets to `update3DImage()` ([Texture.cpp#L569](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/Texture.cpp#L569)). I only ran this on the Noop backend, so I haven't looked at what a real backend does with those values.

`VertexBuffer::setBufferAt()` already uses a wrap-safe form, with this comment ([VertexBuffer.cpp#L451-L455](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/VertexBuffer.cpp#L451-L455)):
```cpp
// Written as two comparisons rather than `byteOffset + buffer.size <= capacity` so that a
// large byteOffset cannot wrap around and defeat the check.
uint32_t const capacity = mBufferSizes[bufferIndex];
FILAMENT_CHECK_PRECONDITION(
        buffer.size <= capacity && byteOffset <= capacity - buffer.size)
```
IndexBuffer.cpp has the same comment at [L172-L173](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/IndexBuffer.cpp#L172-L173).

One possible fix is to use the same form in the three Texture checks, e.g. `width <= w && xoffset <= w - width` with `w = valueForLevel(level, mWidth)`.

I'd be happy to send a PR if this is something you'd like fixed.
