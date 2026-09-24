# filament: open issues and unreported bugs (2026-09-23)

Tested against google/filament HEAD `a5e4a836`, desktop debug build via `./build.sh -p desktop debug` (clang 18, libc++).

**Baseline tests.** All suites pass except two:
- `RenderingTest.*` needs a Vulkan/X display this container doesn't have.
- `JobSystem.JobPoolExhaustionNullJobRun` fails. That failure is finding 6 below.

**Checks.** Every finding was reproduced by running code, and none turned up in searches of filament's open and closed issues and PRs.

**Repros.** `scratchpad/fh-{core,mat,img,utils}/`.

**Policy.** filament accepts AI-assisted contributions that follow `AGENTS.md` and `skills/`: its verification pipeline, header ordering, and 50/72 commit messages. CONTRIBUTING asks for an issue before a PR. Outside PRs that touch `.github/` or `libs/gltfio/` are auto-closed.

## Engine core

### 1. `Texture::setImage` bounds checks bypassed by uint32 wraparound. Medium.
`setImage(engine, 0, xoffset=0xFFFFFFFF, 0, 0, width=2, ...)` is accepted on a 4×4 texture, and the out-of-range region goes to the backend.
- Root cause: Texture.cpp:476/481/510 check `xoffset + width <= W` on uint32.
- VertexBuffer, IndexBuffer and BufferObject already use the wrap-safe form, with the comment "so that a large byteOffset cannot wrap around". Texture was missed.
- Fix: `width <= W && xoffset <= W - width`.

### 2. `VertexBuffer::Builder` accepts an attribute `bufferIndex >= bufferCount`. Low–medium.
`bufferCount(2)` with `attribute(UV0, 5, ...)` builds without an error when `enableBufferObjects(true)` is set; without it, the debug build aborts at the `assert_invariant` (VertexBuffer.cpp:334). (Corrected 2026-09-24.)
- The only guard is `assert_invariant(slot < mBufferCount)` (VertexBuffer.cpp:334).
- With assertions off, UV0 reads a buffer that can never be set.
- The header says bufferIndex "must be between 0 and bufferCount() - 1" and that the call is "a no-op" otherwise.
- Root cause: `attribute()` checks against 16 (VertexBuffer.cpp:114), and `build()` compares only the popcount (:242).

## Material toolchain (matc / filament-matp / filabridge)

### 3. Uniform arrays over 65,535 floats wrap the `uint16_t` offset. Medium: silent corruption.
`parameters: [{type: float4[16384], name: arr}, {type: float, name: g}]` compiles. The resulting UBO is 16 bytes, and `g` sits at offset 0 on top of `arr[0]`. MaterialInstance sizes its CPU buffer from this, so writes to `arr[i]` would go out of bounds.
- Root cause: BufferInterfaceBlock.cpp:126.
- Fix: a 32-bit offset, and reject UBOs over a size limit.

### 4. Unquoted values that are prefixes of `true`, `false` or `null` become booleans or null. Medium.
- `doubleSided : tru` (or `t`) compiles as **true**. matinfo shows "Double sided: true".
- A parameter can't be named `f` or `n` unquoted: it fails with "name value must be STRING".
- Root cause: JsonishLexer.cpp:32–37 and JsonishParser.cpp:293 use `strncmp` with the lexeme's length.

### 5. Array parameter sizes are mishandled. Medium.
- Any whitespace between an array type's `]` and the next token (for example before `}` or before `,`) is kept in the type string, and the type is rejected (JsonishParser.cpp:262). (Corrected 2026-09-24; the first version said only the last key before `}`.)
- `float[0]` silently becomes a scalar `float`. `float[4294967297]` is narrowed to `uint32_t` (MaterialBuilder.cpp:681) and becomes `float a[1]` in the generated GLSL. (Corrected 2026-09-24; the first version said it became a scalar.)
- `float[99999999999999999999]` aborts matc with an uncaught `std::out_of_range`.
- Root cause: `extractArraySize` in ParametersProcessor.cpp:118–146.
- Related: `matc -PmaskThreshold=abc` aborts with an uncaught `std::invalid_argument` (ParametersProcessor.cpp:1482).
- Doc drift: Materials.md says values are not case-sensitive, but `shadingModel : UNLIT` and `doubleSided : TRUE` are rejected.

## utils / math

### 6. The JobSystem job pool holds 16383 jobs, not `MAX_JOB_COUNT` (16384), on glibc. Low–medium.
The pool is sized exactly `MAX_JOB_COUNT * sizeof(Job)`.
- `HeapArea` uses plain `malloc`. glibc returns a 16-aligned pointer for 1 MiB.
- `Job` is `alignas(64)`, so `AtomicFreeList` aligns up and loses one slot.
- This is why the existing test `JobSystem.JobPoolExhaustionNullJobRun` fails on Linux.
- Fix: add `CACHELINE_SIZE` of slack (JobSystem.cpp:186), or make `HeapArea` use an aligned allocation.

### 7. `math::fast::qadd`/`qsub` return wrong results on ARM64. Medium; public libmath API with no in-tree callers.
The AArch64 branch (fast.h:130–137) uses the **signed** saturating intrinsics: `vuqadd*_s*` (SUQADD) and `vqsub*_s*` (SQSUB).

Run under qemu-aarch64:

| Call | Result | Expected |
|---|---|---|
| `qadd(200,100)` | 44 | 255 |
| `qadd(100,100)` | 127 | 200 |
| `qsub(200,100)` | 128 | 100 |
| `qsub(10,20)` | 246 | 0 |
| `qadd(2^31, 2^31)` | 0 | 0xffffffff |

The x86 path is correct. Fix: `vqadd*_u*` / `vqsub*_u*`.

## image / camutils

### 8. `image::compare()` detects only one direction of difference. Medium.
It returns `lexicographical_compare(a, b, x < y - eps)` (ImageOps.cpp:235–246): 1 if a<b, otherwise 0. `ImageDiffer` treats 0 as "match", so a golden-image test passes whenever the result is brighter than the golden. `compare(1.0, 0.0)` returns 0.

### 9. `ImageSampler` ignores `sourceRegion` when choosing source pixels. Medium.
With NEAREST on the right half of an 8-pixel ramp, the result is `0 0 0 7` (expected `4 5 6 7`). The filter bound is also inverted (`domainScale * radius`). See ImageSampler.cpp:136–146.

Related: `computeSingleSample` is biased half a pixel toward the origin. The centre of pixel 4 gives 3.5.

### 10. ORBIT manipulator ground plane is wrong when the target isn't at the origin. Medium.
`groundPlane = vec4(n, -length(target))` (OrbitManipulator.h:62–66) should be `dot(n, target)`. A centre raycast with target (0,0,10) hits z=-10, and pan speed then depends on the target's world position (3× too fast in the repro).

Related: a MAP-mode manipulator built without `groundPlane()` returns eye == target and a NaN up vector.

## Open issues with a fix (no PR yet)
- **#10406 (Metal):** the descriptor-set-layout bindings sort sits inside `#if FILAMENT_METAL_DEBUG_LOG` (MetalDriver.mm:938–957), so release builds never sort. Filed by maintainer poweifeng and assigned to bejado. The fix is a 4-line move, but verifying it needs macOS.
- **#8778:** `interpolation` isn't applied to custom material variables (CodeGenerator.cpp:452–469). A maintainer should decide whether to change the code or the docs.

## Ruled out
- **Has an open PR:** #10200 (PR #10114).
- **Already fixed:** #10391.
- **Restricted `libs/gltfio`:** many recent security reports.
- **Already claimed by its reporter:** #10431.
- **Documented undefined behaviour:** TransformManager re-parenting cycles.
