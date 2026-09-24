**Title:** matc: array parameter types misparsed (whitespace, float[0], huge sizes)

**Describe the bug**
matc handles some array parameter types in `parameters` unexpectedly. All of these are in `libs/filament-matp`:
1. If there is whitespace between `]` and the next token, the whitespace stays in the type string. This happens with `{ name : arr, type : float[4] }` and with `{ type : float[4] , name : arr }`. The material is rejected with `the type 'float[4] ' ... is neither a valid uniform type nor a valid sampler type`. `{ type : float[4], name : arr }` compiles.
2. `float[0]` is accepted and becomes a scalar `float`.
3. `float[4294967297]` is accepted and becomes `float a[1]` in the generated GLSL.
4. `float[99999999999999999999]` makes matc abort with an uncaught `std::out_of_range` from `stoul`.

**To Reproduce**
Each case uses this template, with `<TYPE>` and `<USE>` filled in as listed below:
```
material {
    name : <file name>,
    shadingModel : unlit,
    parameters : [ { type : <TYPE>, name : arr } ]
}
fragment {
    void material(inout MaterialInputs material) {
        prepareMaterial(material);
        material.baseColor = vec4(materialParams.arr<USE>);
    }
}
```
| file | `<TYPE>` | `<USE>` |
|---|---|---|
| c4.mat | `float[4]` | `[0]` |
| c0.mat | `float[0]` | `[0]` |
| c0s.mat | `float[0]` | (empty) |
| cbig.mat | `float[4294967297]` | `[0]` |
| cbigs.mat | `float[4294967297]` | (empty) |
| bhuge.mat | `float[99999999999999999999]` | (empty; `baseColor` line removed) |

For case 1, `a4.mat` is the same as c4.mat but with the keys swapped, `{ name : arr, type : float[4] }`, and without the `baseColor` line.

`run.sh`:
```sh
M=out/cmake-debug/tools/matc/matc
I=out/cmake-debug/tools/matinfo/matinfo
$M -p desktop -a opengl -o a4.filamat a4.mat
for f in c4 c0 cbig c0s cbigs; do $M -p desktop -a opengl -o $f.filamat $f.mat && $I -g 1 $f.filamat | sed -n 15,18p; done
$M -p desktop -a opengl -o bhuge.filamat bhuge.mat
```
(`matinfo -g 1` prints the first desktop fragment shader. Lines 15-18 are the `MaterialParams` block. The shader minifies `arr` to `a`.)

Desktop debug build at a5e4a836 (`./build.sh -p desktop debug`, clang 18, libc++).

**Expected behavior**
- Whitespace after the type doesn't matter, as for other values.
- `float[0]`, and sizes that don't fit the builder's size type, are rejected with an error rather than changed.
- An out-of-range size gives a matc error message instead of an abort.

**Screenshots**
N/A

**Logs**
Output of the three commands above, in order:
```
Error while processing material json, key:"parameters"
Error message: parameters: the type 'float[4] ' for parameter with name 'arr' is neither a valid uniform type nor a valid sampler type.
parameters: the type 'float[4] ' for parameter with name 'arr' is neither a valid uniform type nor a valid sampler type.
layout(std140) uniform MaterialParams
{
float a[4];
} materialParams;
ERROR: surface_shading_parameters.fs:9: 'expression' :  left of '[' is not of type array, matrix, or vector  
ERROR: surface_shading_parameters.fs:9: '' : compilation terminated 
ERROR: 2 compilation errors.  No code generated.

Could not compile material c0.mat
layout(std140) uniform MaterialParams
{
float a[1];
} materialParams;
layout(std140) uniform MaterialParams
{
float a;
} materialParams;
ERROR: surface_shading_parameters.fs:9: 'constructor' : constructing non-array constituent from array argument 
ERROR: surface_shading_parameters.fs:9: 'assign' :  cannot convert from ' const float' to ' global mediump 4-component vector of float'
ERROR: surface_shading_parameters.fs:9: '' : compilation terminated 
ERROR: 3 compilation errors.  No code generated.

Could not compile material cbigs.mat
libc++abi: terminating due to uncaught exception of type std::out_of_range: stoul: out of range
run.sh: line 5:  1481 Aborted                 $M -p desktop -a opengl -o bhuge.filamat bhuge.mat
```
Reading that in order: `a4` is rejected with the trailing space in the type. `c4` gives `float a[4]`. `c0` fails GLSL compilation because `arr` is not an array. `cbig` gives `float a[1]`. `c0s` gives the scalar `float a`. `cbigs` fails because `arr` is an array. `bhuge` aborts (exit status 134).

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; offline material compilation only)
 - Backend: N/A (matc run with `-a opengl`)

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
Case 1: after an array type, `parseString()` takes everything up to the start of the next token, including any whitespace in between ([JsonishParser.cpp#L257-L263](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filament-matp/src/JsonishParser.cpp#L257-L263)):
```cpp
        const JsonLexeme* next = peekNextLexemeType();
        ...
        size_t length = next->getStart() - strLexeme->getStart();
        tmp = std::string(strLexeme->getStart(), length);
```
Then `extractArraySize()` requires `]` to be the last character ([ParametersProcessor.cpp#L124-L128](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filament-matp/src/ParametersProcessor.cpp#L124-L128)), so the trailing space makes it return 0 and leave the type unchanged. The type then fails validation.

Cases 2-4: [`extractArraySize()`, ParametersProcessor.cpp#L117-L146](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filament-matp/src/ParametersProcessor.cpp#L117-L146) ends with:
```cpp
    // Remove the [...] bit
    type.erase(start);

    // handle an empty size array: []
    if (end - start == 1) {
        return -1;
    }

    // Return the size (we already validated this part of the string contains only digits)
    return (ssize_t)std::stoul(type.c_str() + start + 1, nullptr);
```
- A return of 0 means "not an array" to the caller, which then adds a scalar ([L256-L257](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filament-matp/src/ParametersProcessor.cpp#L256-L257)). So `[0]` becomes a scalar.
- For 4294967297, `MaterialBuilder` narrows the size with `uint32_t(param.size == 1u ? 0u : param.size)` ([MaterialBuilder.cpp#L681](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filamat/src/MaterialBuilder.cpp#L681)), which gives 1. That matches the `float a[1]` above.
- `stoul` throws for values that don't fit in `unsigned long`, and nothing catches it.

Separately, as far as I can tell, `stoul` reads from `type.c_str() + start + 1` after `type.erase(start)`. That is one past the new terminator, so it relies on the erased digits still being in the string's buffer. It gives the right number in my build, but it seemed worth mentioning since it's in the same lines.

One possible fix is to parse the digits before erasing (e.g. `std::from_chars` on the substring, which reports overflow without throwing), trim trailing whitespace from the type string, and have `processParameter` return `Status::invalidArgument` for a size of 0 or one above some maximum.

Related, and smaller: `matc -PmaskThreshold=abc` also aborts, with `std::invalid_argument`, from `std::stof(value)` at [ParametersProcessor.cpp#L1482](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filament-matp/src/ParametersProcessor.cpp#L1482):
```
$ $M -PmaskThreshold=abc -p desktop -a opengl -o p.filamat p.mat; echo "matc exit=$?"
libc++abi: terminating due to uncaught exception of type std::invalid_argument: stof: no conversion
/bin/bash: line 8:  1062 Aborted                 $M -PmaskThreshold=abc -p desktop -a opengl -o p.filamat p.mat
matc exit=134
```
(`p.mat` is `material { name : x, shadingModel : unlit, blending : masked }` plus an empty `fragment` block. `-PmaskThreshold=0.3` works.) I can file that separately if you prefer.

I'd be happy to send a PR if this is something you'd like fixed.
