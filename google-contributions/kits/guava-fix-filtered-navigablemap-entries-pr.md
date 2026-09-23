**Title:** Make filtered `NavigableMap` views return snapshot entries from `pollFirstEntry()` etc.

`Maps.filterKeys`, `Maps.filterValues` and `Maps.filterEntries` on a `NavigableMap` (implemented by `Maps.FilteredEntryNavigableMap`) return the backing map's live entry objects from their navigation methods. This causes two problems.

### 1. `pollFirstEntry()` / `pollLastEntry()` can return the wrong mapping

```java
TreeMap<Integer, String> map = new TreeMap<>(Map.of(1, "one", 2, "two", 3, "three"));
System.out.println(Maps.filterKeys(map, k -> k != 1).pollFirstEntry());

TreeMap<Integer, String> digits = new TreeMap<>();
for (int i = 0; i < 10; i++) digits.put(i, "" + i);
NavigableMap<Integer, String> odd = Maps.filterKeys(digits, k -> k % 2 == 1);
List<Integer> polled = new ArrayList<>();
for (Map.Entry<Integer, String> e; (e = odd.pollFirstEntry()) != null; ) polled.add(e.getKey());
System.out.println(polled);
```

Before:
```
3=three
[2, 4, 6, 7, 9]
```
After:
```
2=two
[1, 3, 5, 7, 9]
```

The correct mappings are removed from the backing map. Only the returned entries are wrong.

Root cause: the poll methods used `Iterables.removeFirstMatching(unfiltered.entrySet(), predicate)`, which calls `iterator.remove()` and then returns the same entry object. When `TreeMap` removes a node that has two children, it copies the successor's key and value into that node and unlinks the successor, so the returned entry now shows the successor's mapping.

### 2. `firstEntry()`, `ceilingEntry()` etc. return entries whose `setValue` bypasses the predicate

```java
TreeMap<Integer, String> map = new TreeMap<>(Map.of(1, "one"));
NavigableMap<Integer, String> filtered = Maps.filterValues(map, v -> !v.equals("bad"));
filtered.firstEntry().setValue("bad");
System.out.println(map);
```

Before: prints `{1=bad}`. After: `setValue` throws `UnsupportedOperationException`.

`NavigableMap` specifies that `firstEntry()`, `lastEntry()`, `lowerEntry()`, `floorEntry()`, `ceilingEntry()` and `higherEntry()` return snapshot entries that don't support `setValue`. `TreeMap` follows this, for example. The `filterValues` Javadoc also says that `setValue` on the filtered map's entries throws `IllegalArgumentException` for a value that fails the predicate, but these entries skipped that check. They came from `AbstractNavigableMap`, which reads them from `entryIterator()` / `descendingEntryIterator()`. For the filtered map those iterators were plain `Iterators.filter` over the backing map's entry-set iterator.

### Fix

In `FilteredEntryNavigableMap`:

- `entryIterator()` and `descendingEntryIterator()` now convert each entry to an `immutableEntry(key, value)` snapshot. These iterators only back the navigation methods. `entrySet()` still goes through the `FilteredEntryMap` delegate, so its entries still support `setValue` with the predicate check.
- `pollFirstEntry()` and `pollLastEntry()` use a new private helper that finds the first matching entry, takes an `immutableEntry` snapshot of it, removes it through the iterator and then returns the snapshot.

Nothing else changes. `Iterables.removeFirstMatching` is left as it is. Its other caller (`Sets` filtered navigable sets) returns elements, not mutable entries, so this problem does not affect it.

### Tests

New tests in `MapsTest`:

- `testFilteredNavigableMapPollFirstEntry`: the 1..3 case above, where the first matching key is the `TreeMap` root.
- `testFilteredNavigableMapPollEntriesDrainsInOrder`: drains `filterKeys(0..9, odd)` with `pollFirstEntry()` and then with `pollLastEntry()`.
- `testFilteredNavigableMapNavigationEntriesAreSnapshots`: `setValue` throws `UnsupportedOperationException` on entries from `firstEntry`, `lastEntry`, `ceilingEntry`, `floorEntry`, `higherEntry`, `lowerEntry`, `descendingMap().firstEntry()` and `headMap(..).lastEntry()`. It also checks that `entrySet()` entries still support `setValue` and still enforce the predicate.

All three tests fail without the change to `Maps.java` and pass with it. The full `com.google.common.collect` test package passes (826,073 tests), including `MapsCollectionTest`. The `NavigableMapTestSuiteBuilder` suites that `MapsCollectionTest` applies to filtered navigable maps did not catch this bug. Their sample maps are small, so the polled entry never lands on a two-child `TreeMap` node, and the navigation testers don't call `setValue` on the returned entries.

There is no existing issue for this. Guava's CONTRIBUTING guide says pull requests are fine for bug fixes that don't change the API.
