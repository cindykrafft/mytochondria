**Title:** Validate strings skipped by `skipValue()` in strict mode

### Purpose

In `Strictness.STRICT`, `JsonReader` rejects unescaped control characters (U+0000–U+001F) and unpaired surrogates (the latter added in #3116) in strings and names read with `nextString()` / `nextName()`. `skipValue()` goes through `skipQuotedValue`, which does neither check, so in my testing the same invalid document is rejected or accepted depending on whether the string is read or skipped:

```java
Gson strict = new GsonBuilder().setStrictness(Strictness.STRICT).create();
class Pojo { int a; }

strict.fromJson("{\"a\":1,\"junk\":\"x\u0001y\"}", Pojo.class);      // accepted: "junk" is skipped
strict.fromJson("{\"a\":1,\"junk\":\"x\u0001y\"}", JsonObject.class); // JsonSyntaxException (cause: MalformedJsonException)
strict.fromJson("{\"a\":1,\"junk\":\"\\uD800\"}", Pojo.class);        // accepted
```

This seems inconsistent with the `JsonReader.setStrictness` Javadoc, which says "In strict mode, only input compliant with RFC 8259 is accepted." ([JsonReader.java:368](https://github.com/google/gson/blob/854c8255b625cf1e13c701a83ea9ccb4caaa576a/gson/src/main/java/com/google/gson/stream/JsonReader.java#L368)). Is skipping meant to be covered by that too?

### Description

In strict mode, `skipQuotedValue` now delegates to `nextQuotedValue`, so skipped strings and names go through the same checks as ones that are read. In the repro above, the skipped and the read case now report the same message and location (`at line 1 column 16 path $.junk`). The allocation-free skipping path is unchanged for `LENIENT` and `LEGACY_STRICT`.

The cost, in strict mode only, is that each skipped string is built as a `String` (plus a `StringBuilder` when it contains escapes or spans a buffer refill), as for `nextString()`. I preferred this over duplicating the control-character and surrogate checks in the skip loop: duplicating them would be more code, and could diverge from the read path, for example for surrogate pairs split across buffer refills.

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
  - [x] The two `...Rejects...` tests fail without the fix; all four pass with it
- [x] `mvn clean verify` passes for the `gson` module (4677 tests, 0 failures)
