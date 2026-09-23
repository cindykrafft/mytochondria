**Title:** Clarify when `JsonSyntaxException` is thrown

### Purpose

Closes #1138

### Description

The Javadoc of `JsonSyntaxException` says it is raised when Gson "attempts to read (or write) a malformed JSON element". In practice it is also thrown for well-formed JSON which does not match the expected type, which is how the `@throws JsonSyntaxException` clauses of the `Gson.fromJson` methods already describe it ("if json is not a valid representation for an object of type ..."):

```java
new Gson().fromJson("\"s\"", int[].class);
// JsonSyntaxException: java.lang.IllegalStateException: Expected BEGIN_ARRAY but was STRING at line 1 column 2 path $

new Gson().fromJson("{\"foo\":10000000000}", C.class); // C has an `int foo` field
// JsonSyntaxException: java.lang.NumberFormatException: Expected an int but was 10000000000 at line 1 column 19 path $.foo
```

This PR only updates the class Javadoc to describe both cases, using these two situations as examples. It also drops "(or write)", since none of the places which throw `JsonSyntaxException` are on the serialization side.

No behavior is changed. The question raised in #2816 of whether a different exception type should be thrown is intentionally left out of scope.

### Checklist

- [x] New code follows the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) (`mvn spotless:check` passes)
- [ ] ~~If necessary, new public API validates arguments~~ (no new API)
- [ ] ~~New public API has Javadoc~~ (no new API)
- [ ] ~~If necessary, new unit tests have been added~~ (Javadoc-only change)
- [x] `mvn clean verify` passes for the `gson` module
