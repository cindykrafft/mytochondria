**Title:** Don't cache adapter placeholders for failed nested `getAdapter` calls

### Purpose

Suppose a `TypeAdapterFactory` calls `gson.getAdapter(...)` for another type inside `create()`, catches the resulting exception (for example "declares multiple JSON fields named 'a'"), and carries on. Then the unresolved `FutureTypeAdapter` placeholder for the failed type is published to the `Gson` instance's adapter cache when the outer request succeeds.

From then on, every `gson.getAdapter(ThatType)` returns the placeholder. Using it throws the misleading

```
IllegalStateException: Adapter for type with cyclic dependency has been used before dependency has been resolved
```

instead of re-running adapter creation and reporting the real problem. This lasts for the lifetime of the `Gson` instance.

### Description

The cause is that the `finally` block of `getAdapter` only cleans up the thread-local `threadCalls` map for the initial request. When a nested request fails, its placeholder stays in the map, and `typeTokenCache.putAll(threadCalls)` later copies it into the cache.

The fix: when a nested request fails (a factory threw, or no factory supports the type), remove its placeholder from `threadCalls`. Also remove every entry added after it. Those entries were created during the failed request and might hold a reference to the unresolved placeholder. For example, the reflective adapter for a field type is created before the duplicate field name is detected. `threadCalls` is now a `LinkedHashMap` so that insertion order identifies those entries.

Why this is safe:

- **Order identifies the failed request's work.** `getAdapter` only adds entries with `put`, and replacing a placeholder with the real adapter keeps its position (`LinkedHashMap` Javadoc: "encounter order is not affected if a key is *re-inserted* into the map"). So entries after the failed type were created during the failed request.
- **Earlier entries are left alone.** They belong to requests further up the call chain, or to earlier siblings that completed. As far as I can tell they could not have received the failed placeholder.
- **The initial request's failure handling is unchanged.** The success path's only change is `HashMap` becoming `LinkedHashMap`.

The removed types are simply created again the next time they are requested.

A regression test is added to `GsonTest` (`testGetAdapter_NestedFailureNotCached`). It covers the failed type itself, and a type created during the failed request which references it. The test fails without the fix. A variant that removes only the failed type's own entry fails at the `DuplicateFields.Child` check.

### Checklist

- [x] New code follows the Google Java Style Guide (`mvn spotless:check`)
- [ ] ~~New public API validates arguments / has Javadoc~~ (no new API)
- [x] New unit tests have been added
  - [x] Assertions use Truth
  - [x] No JUnit 3 features are used
  - [x] The new test fails without the fix and passes with it
- [x] `mvn clean verify` passes for the `gson` module
