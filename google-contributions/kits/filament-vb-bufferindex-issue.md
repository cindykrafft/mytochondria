**Title:** VertexBuffer::Builder accepts an attribute bufferIndex >= bufferCount

**Describe the bug**
`VertexBuffer::Builder::attribute()` documents that `bufferIndex` "Must be between 0 and bufferCount() - 1" and that the call "is a no-op if the \p bufferIndex is out of bounds". As far as I can tell, `bufferIndex` is only checked against `MAX_VERTEX_ATTRIBUTE_COUNT` (16), not against `bufferCount()`. `build()` then only compares how many distinct buffer slots are used with `bufferCount`, so `bufferCount(2)` with attributes on slots 0 and 5 passes.

What happens next depends on the build and on `enableBufferObjects()`:
- With `enableBufferObjects(true)`, `build()` succeeds in a debug build.
- Without it, a debug build stops at `assert_invariant(slot < mBufferCount)` in the `FVertexBuffer` constructor. With `NDEBUG` that assert compiles out. I have not run a release build, so I haven't checked what happens after that.

**To Reproduce**
`vb_bufferindex.cpp`:
```cpp
#include <filament/Engine.h>
#include <filament/VertexBuffer.h>
#include <utils/Panic.h>
#include <cstdio>
#include <cstring>
using namespace filament;

int main(int argc, char** argv) {
    bool const bufferObjects = argc > 1 && !strcmp(argv[1], "bo");
    Engine* engine = Engine::create(Engine::Backend::NOOP);
    try {
        VertexBuffer* vb = VertexBuffer::Builder()
                .vertexCount(3)
                .bufferCount(2)
                .enableBufferObjects(bufferObjects)
                .attribute(VertexAttribute::POSITION, 0, VertexBuffer::AttributeType::FLOAT3)
                .attribute(VertexAttribute::UV0, 5, VertexBuffer::AttributeType::FLOAT2)
                .build(*engine);
        printf("build() succeeded (bufferCount=2, UV0 at bufferIndex 5)\n");
        engine->destroy(vb);
    } catch (utils::PreconditionPanic const& e) {
        printf("build() rejected: %s\n", e.what());
    }
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
  vb_bufferindex.cpp -o vb_bufferindex \
  -Wl,--start-group $B/filament/libfilament.a $B/filament/backend/libbackend.a \
    $B/libs/bluegl/libbluegl.a $B/libs/bluevk/libbluevk.a \
    $B/libs/filaflat/libfilaflat.a $B/libs/filabridge/libfilabridge.a \
    $B/libs/math/libmath.a $B/libs/utils/libutils.a \
    $B/third_party/smol-v/tnt/libsmol-v.a $B/third_party/zstd/tnt/libzstd.a \
    $B/shaders/libshaders.a \
  -Wl,--end-group -ldl -lpthread
./vb_bufferindex bo   # enableBufferObjects(true)
./vb_bufferindex      # enableBufferObjects(false)
```

**Expected behavior**
Going by the header, I'd expect `build()` to reject the builder with a precondition failure, or `attribute(UV0, 5, ...)` to be ignored, since 5 is not below `bufferCount()`.

**Screenshots**
N/A

**Logs**
`./vb_bufferindex bo`:
```
Using 'soft' CircularBuffer (12288 KiB)
FEngine (64 bits) created at 0x55ebca088b40 (threading is enabled)
FEngine resolved backend: Noop
Backend feature level: 1
FEngine feature level: 1
build() succeeded (bufferCount=2, UV0 at bufferIndex 5)
CircularBuffer: High watermark 0 KiB (0%)
FEngine::mHeapAllocator arena: High watermark 1428 bytes
```
`./vb_bufferindex` (debug build, so the process aborts):
```
Using 'soft' CircularBuffer (12288 KiB)
FEngine (64 bits) created at 0x55b51beffb40 (threading is enabled)
FEngine resolved backend: Noop
Backend feature level: 1
FEngine feature level: 1
PanicLog
in void utils::panic(const char *, const char *, int, const char *):26
in file /home/user/google/filament/libs/utils/src/debug.cpp
reason: /home/user/google/filament/filament/src/details/VertexBuffer.cpp:334: failed assertion 'slot < mBufferCount'
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; the repro uses the Noop backend)
 - Backend: Noop

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
The header ([VertexBuffer.h#L120-L121](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/include/filament/VertexBuffer.h#L120-L121) and [#L137-L138](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/include/filament/VertexBuffer.h#L137-L138)):
```cpp
 * @param bufferIndex  The index of the buffer containing the data for this attribute. Must
 *                     be between 0 and bufferCount() - 1.
...
 * This is a no-op if the \p attribute is an invalid enum.
 * This is a no-op if the \p bufferIndex is out of bounds.
```
`attribute()` checks against the attribute limit ([VertexBuffer.cpp#L114-L115](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/VertexBuffer.cpp#L114-L115)):
```cpp
if (size_t(attribute) < MAX_VERTEX_ATTRIBUTE_COUNT &&
        size_t(bufferIndex) < MAX_VERTEX_ATTRIBUTE_COUNT) {
```
`build()` compares only the number of distinct slots ([VertexBuffer.cpp#L242-L243](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/VertexBuffer.cpp#L242-L243)):
```cpp
FILAMENT_CHECK_PRECONDITION(attributedBuffers.count() == mImpl->mBufferCount)
        << "At least one buffer slot was never assigned to an attribute.";
```
The only range check I found is the debug-only [`assert_invariant(slot < mBufferCount)` at L334](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/VertexBuffer.cpp#L334). `setBufferAt()` / `setBufferObjectAt()` do check `bufferIndex < mBufferCount`, so as far as I can tell, data can never be supplied for slot 5 in this configuration.

One possible fix is a precondition in `build()` that every declared attribute's `buffer` is `< mImpl->mBufferCount`, e.g. in the loop that already does `attributedBuffers.set(attributes[j].buffer)` ([L239](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/VertexBuffer.cpp#L239)). Alternatively, `attribute()` could be made a no-op as documented, but it doesn't know the final `bufferCount` because the builder calls can come in any order, so `build()` seems like the simpler place. I'm not sure which you'd prefer.

I'd be happy to send a PR if this is something you'd like fixed.
