**Title:** Document that `FluentIterable.toSortedList` is stable

`FluentIterable.toSortedList(Comparator)` delegates to `Ordering.from(comparator).immutableSortedCopy(...)`, which delegates to `ImmutableList.sortedCopyOf(Comparator, Iterable)`. Both of those methods document that the sort is stable, but `toSortedList` did not. This adds a paragraph to its Javadoc, using the same wording as `ImmutableList.sortedCopyOf`:

> The sorting algorithm used is stable, so elements that compare as equal will stay in the order in which they appear in this fluent iterable.

This is a Javadoc-only change. `toSortedSet` is not changed: it removes duplicates, so stability does not apply to it in the same way, and the issue covers only `toSortedList`.

Fixes #2884

Testing:
- `./mvnw -pl guava,guava-testlib,guava-tests test -Dtest.include="**/FluentIterableTest.java"`: 105 tests, 0 failures, 0 errors.
- `./mvnw -pl guava javadoc:javadoc`: BUILD SUCCESS, and the new sentence appears in the generated `FluentIterable.html`.
