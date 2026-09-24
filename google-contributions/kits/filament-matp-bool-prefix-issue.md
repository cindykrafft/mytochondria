**Title:** matc: unquoted prefixes of true/false/null (t, tru, f, n) parse as bool/null

**Describe the bug**
The Jsonish lexer used by matc (`libs/filament-matp`) decides whether an unquoted identifier is `true`, `false` or `null` with `strncmp(keyword, lexeme, lexemeSize)`, where the length is the lexeme's. So any prefix of those words matches:
- `doubleSided : tru` and `doubleSided : t` compile as `true`, and `doubleSided : fal` compiles as `false`. `doubleSided : yes` is rejected, as I'd expect.
- A parameter can't be named `f` or `n` unquoted. It fails with `parameters: name value must be STRING.` because `f` lexes as a boolean and `n` as null. `name : fo` and `name : "f"` work.

**To Reproduce**
`ds_tru.mat` (and the same with `t`, `fal`, `yes` in place of `tru`):
```
material {
    name : ds_tru,
    shadingModel : unlit,
    doubleSided : tru
}
fragment {
    void material(inout MaterialInputs material) {
        prepareMaterial(material);
    }
}
```
`pn_f.mat` (and the same with `n`, `fo`, and quoted `"f"`):
```
material {
    name : pn_f,
    shadingModel : unlit,
    parameters : [ { type : float, name : f } ]
}
fragment {
    void material(inout MaterialInputs material) {
        prepareMaterial(material);
        material.baseColor = vec4(materialParams.f);
    }
}
```
```sh
M=out/cmake-debug/tools/matc/matc
I=out/cmake-debug/tools/matinfo/matinfo
$M -p desktop -a opengl -o ds_tru.filamat ds_tru.mat; echo "matc exit=$?"; $I ds_tru.filamat | grep "Double sided"
$M -p desktop -a opengl -o pn_f.filamat pn_f.mat; echo "matc exit=$?"
```
Desktop debug build at a5e4a836 (`./build.sh -p desktop debug`, clang 18, libc++).

**Expected behavior**
Only the exact words `true`, `false` and `null` are keywords. `doubleSided : tru` is rejected like `doubleSided : yes`, and `name : f` is accepted as the string `"f"`.

**Screenshots**
N/A

**Logs**
(The `==` lines are labels printed by the shell loop I ran the commands in.)
```
== doubleSided : tru
matc exit=0
    Double sided:              true
== doubleSided : t
matc exit=0
    Double sided:              true
== doubleSided : fal
matc exit=0
    Double sided:              false
== doubleSided : yes
Value for key:"doubleSided" is not what was expected.
Got :"STRING" but expected 'BOOL'
matc exit=1
```
```
== parameter name : f
Error while processing material json, key:"parameters"
Error message: parameters: name value must be STRING.
parameters: name value must be STRING.
matc exit=1
== parameter name : n
Error while processing material json, key:"parameters"
Error message: parameters: name value must be STRING.
parameters: name value must be STRING.
matc exit=1
== parameter name : fo
matc exit=0
== parameter name : "f"
matc exit=0
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64)
 - GPU: none (CPU-only; offline material compilation only)
 - Backend: N/A (matc run with `-a opengl`)

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
[JsonishLexer.cpp#L30-L38](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filament-matp/src/JsonishLexer.cpp#L30-L38):
```cpp
    size_t lexemeSize = mCursor - lexemeStart;

    // Check what kind of keyword we got here.
    if (strncmp("true", lexemeStart, lexemeSize) == 0) {
        return BOOLEAN;
    } else if (strncmp("false", lexemeStart, lexemeSize) == 0) {
        return BOOLEAN;
    } else if (strncmp("null", lexemeStart, lexemeSize) == 0) {
        return NUll;
```
The parser then takes the value the same way ([JsonishParser.cpp#L291-L293](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/filament-matp/src/JsonishParser.cpp#L291-L293)):
```cpp
        case BOOLEAN:
            consumeLexeme(BOOLEAN);
            return new JsonishBool(!strncmp(next->getStart(), "true", next->getSize()));
```

One possible fix is to also compare the length, e.g. `lexemeSize == 4 && strncmp("true", lexemeStart, 4) == 0` (or compare against a `std::string_view`), in both places. This would turn materials that currently rely on `t` / `tru` / `fal` into errors. I don't know whether any exist, so I'm not sure how you'd want to handle that.

I'd be happy to send a PR if this is something you'd like fixed.
