**Title:** math::fast::qadd/qsub give wrong results on AArch64 (signed intrinsics)

**Describe the bug**
`filament::math::fast::qadd()` and `qsub()` in `libs/math/include/math/fast.h` are under a comment that says "unsigned saturated arithmetic". On AArch64 with NEON they use the signed saturating intrinsics `vuqadd*_s*` (SUQADD) and `vqsub*_s*` (SQSUB). In my testing under qemu-aarch64 the results are wrong for inputs at or above the signed midpoint, and for any subtraction that goes below zero. For example, `qadd(uint8_t(200), uint8_t(100))` returns 44 and `qsub(uint8_t(10), uint8_t(20))` returns 246. The same source built for x86-64, which takes the generic branch, returns 255 and 0.

**To Reproduce**
`qadd_arm64.cpp`, which uses filament's own header:
```cpp
#include <math/fast.h>
#include <cstdio>
#include <cstdint>

using namespace filament::math;

int main() {
    // volatile so the compiler can't constant-fold the calls
    volatile uint8_t  a8 = 200, b8 = 100, c8 = 10, d8 = 20;
    volatile uint16_t a16 = 60000, b16 = 10000;
    volatile uint32_t a32 = 0x80000000u;

    printf("qadd(uint8_t 200, 100)          = %u (expected 255)\n", fast::qadd(uint8_t(a8), uint8_t(b8)));
    printf("qadd(uint8_t 100, 100)          = %u (expected 200)\n", fast::qadd(uint8_t(b8), uint8_t(b8)));
    printf("qsub(uint8_t 200, 100)          = %u (expected 100)\n", fast::qsub(uint8_t(a8), uint8_t(b8)));
    printf("qsub(uint8_t 10, 20)            = %u (expected 0)\n",   fast::qsub(uint8_t(c8), uint8_t(d8)));
    printf("qadd(uint16_t 60000, 10000)     = %u (expected 65535)\n", fast::qadd(uint16_t(a16), uint16_t(b16)));
    printf("qadd(uint32_t 2^31, 2^31)       = %u (expected 4294967295)\n", fast::qadd(uint32_t(a32), uint32_t(a32)));
}
```
I don't have AArch64 hardware, so I cross-compiled on x86-64 Linux and ran it under qemu user-mode emulation. Compiled with clang 18 targeting aarch64 (Ubuntu's `libc++` headers, `aarch64-linux-gnu` sysroot), linked statically with the GNU cross toolchain:
```sh
F=/path/to/filament
clang++ --target=aarch64-linux-gnu --sysroot=/usr/aarch64-linux-gnu -std=c++17 -O2 -stdlib=libc++ \
    -I$F/libs/math/include -c qadd_arm64.cpp -o qadd_arm64.o
aarch64-linux-gnu-gcc -static qadd_arm64.o -o qadd_arm64     # gcc 13.3.0
qemu-aarch64 ./qadd_arm64                                     # qemu 8.2.2

# same file, native x86-64 (generic branch of fast.h)
clang++ -std=c++17 -O2 -I$F/libs/math/include qadd_arm64.cpp -o qadd_x86 && ./qadd_x86
```

**Expected behavior**
Unsigned saturating results on AArch64, matching the generic branch: 255, 200, 100, 0, 65535, 4294967295.

**Screenshots**
N/A

**Logs**
AArch64 (qemu-aarch64):
```
qadd(uint8_t 200, 100)          = 44 (expected 255)
qadd(uint8_t 100, 100)          = 127 (expected 200)
qsub(uint8_t 200, 100)          = 128 (expected 100)
qsub(uint8_t 10, 20)            = 246 (expected 0)
qadd(uint16_t 60000, 10000)     = 4464 (expected 65535)
qadd(uint32_t 2^31, 2^31)       = 0 (expected 4294967295)
```
x86-64 (native):
```
qadd(uint8_t 200, 100)          = 255 (expected 255)
qadd(uint8_t 100, 100)          = 200 (expected 200)
qsub(uint8_t 200, 100)          = 100 (expected 100)
qsub(uint8_t 10, 20)            = 0 (expected 0)
qadd(uint16_t 60000, 10000)     = 65535 (expected 65535)
qadd(uint32_t 2^31, 2^31)       = 4294967295 (expected 4294967295)
```
Saturating instructions in the AArch64 object (`aarch64-linux-gnu-objdump -d qadd_arm64.o | grep -E "suqadd|sqsub|uqadd|uqsub"`):
```
  54:	0e203820 	suqadd	v0.8b, v1.8b
  70:	0e203820 	suqadd	v0.8b, v1.8b
  8c:	0e212c00 	sqsub	v0.8b, v0.8b, v1.8b
  a8:	0e212c00 	sqsub	v0.8b, v0.8b, v1.8b
  c4:	0e603820 	suqadd	v0.4h, v1.4h
  e8:	5ea03820 	suqadd	s0, s1
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64), AArch64 binary run under qemu-aarch64 8.2.2 user-mode emulation
 - GPU: N/A (header-only math code, no rendering)
 - Backend: N/A

**Smartphone (please complete the following information):**
 - Device: N/A (not tested on a device)
 - OS: N/A

**Additional context**
[fast.h#L126-L137](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/math/include/math/fast.h#L126-L137):
```cpp
/*
 * unsigned saturated arithmetic
 */

#if defined(__ARM_NEON) && defined(__aarch64__)
inline uint8_t  MATH_PURE qadd(uint8_t a,  uint8_t b)  noexcept { return vuqaddb_s8(a, b);  }
inline uint16_t MATH_PURE qadd(uint16_t a, uint16_t b) noexcept { return vuqaddh_s16(a, b); }
inline uint32_t MATH_PURE qadd(uint32_t a, uint32_t b) noexcept { return vuqadds_s32(a, b); }

inline uint8_t  MATH_PURE qsub(uint8_t a,  uint8_t b)  noexcept { return vqsubb_s8(a, b);  }
inline uint16_t MATH_PURE qsub(uint16_t a, uint16_t b) noexcept { return vqsubh_s16(a, b); }
inline uint32_t MATH_PURE qsub(uint32_t a, uint32_t b) noexcept { return vqsubs_s32(a, b); }
```
The outputs above match treating `a` as signed and saturating to the signed range. For example, 200 as `int8_t` is -56, and -56 + 100 = 44. 100 + 100 saturates to 127. -56 - 100 saturates to -128, which reads back as 128.

One possible fix is to use the unsigned saturating intrinsics: `vqaddb_u8` / `vqaddh_u16` / `vqadds_u32` and `vqsubb_u8` / `vqsubh_u16` / `vqsubs_u32`. I checked those with the same toolchain under qemu. On the inputs above they return 255, 200, 100, 0, 65535 and 4294967295 (plus `vqsubh_u16(10000, 60000)` = 0 and `vqsubs_u32(1, 2^31)` = 0). A small test comparing both branches might also help, if that fits how libmath is tested.

As far as I can tell from grepping the tree, nothing in filament calls `qadd`/`qsub` (or `qinc`/`qdec`, which wrap them) outside `fast.h`, so I've only seen this through the public header.

I'd be happy to send a PR if this is something you'd like fixed.
