**Title:** Material uniform block offsets wrap past 65535 words (uint16_t offset)

**Describe the bug**
`BufferInterfaceBlock` stores each field's offset as a `uint16_t` count of 32-bit words. When the fields before a member add up to 65536 words or more, the running offset wraps. matc accepts this material without an error:
```
parameters : [
    { type : float4[16384], name : arr },
    { type : float, name : g }
]
```
In std140, `float4[16384]` is 16384 × 4 = 65536 words. After it, the offset is back to 0. `g` is placed at byte offset 0, on top of `arr[0]`, and the block's `getSize()` is 16 bytes.

**To Reproduce**
1. `big.mat`:
```
material {
    name : big,
    shadingModel : unlit,
    parameters : [
        { type : float4[16384], name : arr },
        { type : float, name : g }
    ]
}
fragment {
    void material(inout MaterialInputs material) {
        prepareMaterial(material);
        material.baseColor = materialParams.arr[5] + vec4(materialParams.g);
    }
}
```
```sh
out/cmake-debug/tools/matc/matc -p desktop -a opengl -o big.filamat big.mat; echo "matc exit=$?"
```
2. To see the resulting layout, this builds the same two fields directly with `BufferInterfaceBlock::Builder`, which is what `MaterialBuilder` uses for parameters ([MaterialBuilder.cpp#L659](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filamat/src/MaterialBuilder.cpp#L659)) (`uib_repro.cpp`):
```cpp
#include <private/filament/BufferInterfaceBlock.h>
#include <cstdio>

using namespace filament;

int main() {
    // Same layout matc builds for: parameters : [ { type : float4[16384], name : arr },
    //                                              { type : float,         name : g   } ]
    BufferInterfaceBlock uib = BufferInterfaceBlock::Builder()
            .name("MaterialParams")
            .add({ { "arr", 16384, BufferInterfaceBlock::Type::FLOAT4 },
                   { "g",   0,     BufferInterfaceBlock::Type::FLOAT  } })
            .build();
    printf("getSize() = %zu bytes\n", uib.getSize());
    printf("offset(arr[0]) = %zd, offset(arr[1]) = %zd, offset(g) = %zd\n",
            uib.getFieldOffset("arr", 0), uib.getFieldOffset("arr", 1), uib.getFieldOffset("g", 0));
}
```
```sh
F=/path/to/filament
B=$F/out/cmake-debug
clang++ -std=c++20 -stdlib=libc++ -g \
  -I$F/libs/filabridge/include -I$F/filament/backend/include -I$F/libs/utils/include \
  -I$F/libs/math/include -I$F/third_party/robin-map/include \
  uib_repro.cpp -o uib_repro \
  $B/libs/filabridge/libfilabridge.a $B/libs/utils/libutils.a $B/libs/math/libmath.a -lpthread -ldl
./uib_repro
```
Both use a desktop debug build at a5e4a836 (`./build.sh -p desktop debug`, clang 18, libc++).

**Expected behavior**
Either the block is laid out with `g` after `arr` (byte offset 262144) and a matching size, or matc rejects the material with an error saying the uniform block is too large.

**Screenshots**
N/A

**Logs**
```
matc exit=0
```
```
getSize() = 16 bytes
offset(arr[0]) = 0, offset(arr[1]) = 16, offset(g) = 0
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; the repro doesn't render)
 - Backend: N/A

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
[BufferInterfaceBlock.h#L83](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filabridge/include/private/filament/BufferInterfaceBlock.h#L83):
```cpp
        uint16_t offset;            // offset in "uint32_t" of this field in the buffer
```
[BufferInterfaceBlock.cpp#L126](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filabridge/src/BufferInterfaceBlock.cpp#L126), [#L152](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filabridge/src/BufferInterfaceBlock.cpp#L152) and [#L157](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filabridge/src/BufferInterfaceBlock.cpp#L157):
```cpp
    uint16_t offset = 0;
    ...
        offset += stride * std::max(1u, e.size);
    ...
    mSize = sizeof(uint32_t) * ((offset + 3) & ~3);
```
`FMaterialInstance` sizes its CPU-side uniform buffer from this value ([MaterialInstance.cpp#L83-L84](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/filament/src/details/MaterialInstance.cpp#L83-L84)):
```cpp
    size_t const uboSize = std::max(size_t(16), material->getUniformInterfaceBlock().getSize());
    mUniforms = UniformBuffer(uboSize);
```
So I think setting `arr` on a `MaterialInstance` of this material would write past a 16-byte buffer. I haven't run that path, so this is from reading the code only. I also haven't checked what size GPUs in practice accept for a UBO this large. The main point is that the layout silently disagrees with the shader.

One possible fix is to accumulate the offset in a wider type (`uint32_t`/`size_t`) and have `Builder::build()` (or matc) reject a block whose size doesn't fit in the stored offset type, or that goes past some chosen size limit. Which limit to use seems like your call.

I'd be happy to send a PR if this is something you'd like fixed.
