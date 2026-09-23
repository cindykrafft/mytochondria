**Title:** Validate strings skipped by `skipValue()` in strict mode

### Purpose

In `Strictness.STRICT`, `JsonReader` rejects unescaped control characters (U+0000–U+001F) and unpaired surrogates (the latter added in #3116 for #3113) in strings and names read with `nextString()` / `nextName()`. `skipValue()` did not apply either check, so the same invalid document was rejected or accepted depending on whether the string was read or skipped:

```java
Gson strict = new GsonBuilder().setStrictness(Strictness.STRICT).create();
class Pojo { int a; }

strict.fromJson("{\"a\":1,\"junk\":\"x\u0001y\"}", Pojo.class);      // accepted: "junk" is skipped
strict.fromJson("{\"a\":1,\"junk\":\"x\u0001y\"}", JsonObject.class); // MalformedJsonException
strict.fromJson("{\"a\":1,\"junk\":\"\\uD800\"}", Pojo.class);        // accepted
```

This contradicts the `setStrictness` documentation, which says only RFC 8259-compliant input is accepted in strict mode.

### Description

In strict mode, `skipQuotedValue` now delegates to `nextQuotedValue`, so skipped strings and names are validated in exactly the same way, with the same error messages and locations, as ones that are read. The allocation-free skipping path is unchanged for `LENIENT` and `LEGACY_STRICT`.

The cost is one string allocation per skipped string, and only in strict mode. I preferred this over duplicating the control-character and surrogate checks in the skip loop: duplicating them would be more code, and could diverge from the read path, for example for surrogate pairs split across buffer refills.

Tests added to `JsonReaderTest`:
- control characters in skipped values and names are rejected;
- unpaired surrogates (escaped and raw) in skipped values and names are rejected;
- valid strings, including surrogate pairs and escaped control characters, are still skipped fine;
- `LEGACY_STRICT` behavior is unchanged.

### Checklist

- [x] New code follows the Google Java Style Guide (`mvn spotless:check`)
- [ ] ~~New public API validates arguments / has Javadoc~~ (no new API)
- [x] New unit tests have been added
  - [x] Assertions use Truth
  - [x] No JUnit 3 features are used
  - [x] The new tests fail without the fix and pass with it
- [x] `mvn clean verify` passes for the `gson` module (4677 tests, 0 failures)
