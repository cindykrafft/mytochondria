Thanks! In case it helps with your testing, I looked for public code that might depend on this. I used Sourcegraph's public code search, which covers a large part of public GitHub but not all of it, and of course nothing internal.

I collected the Java files that call `filterKeys(`, `filterValues(` or `filterEntries(`. After dropping copies of Guava that came to about 1,500 files in about 490 repositories, some of them calling other libraries' methods with the same names. I searched those files for `firstEntry`, `lastEntry`, `floorEntry`, `ceilingEntry`, `higherEntry`, `lowerEntry`, `pollFirstEntry` and `pollLastEntry`, and read every file that had one of those calls or mentioned `NavigableMap`.

- One project calls a navigation method on a filtered `NavigableMap`: Consensys/teku, in [`Eth1DataCache.java` line 129](https://github.com/Consensys/teku/blob/524c297a5b0111fc3d3145a2d53b4ee9fe1dfa6a/beacon/validator/src/main/java/tech/pegasys/teku/validator/coordinator/Eth1DataCache.java#L129). It calls `lastEntry().getValue()` right away, so as far as I can tell it would behave the same with this change.
- Four other projects use the `NavigableMap` overload but only iterate the result.
- I didn't find any `setValue`, cast or `==` comparison on entries from these methods, or any `pollFirstEntry`/`pollLastEntry` call on a filtered map.

One limit: the search only looked for navigation calls in the same file as the filter call, plus files that mention `NavigableMap`. It could miss a filtered map that is passed around and navigated elsewhere.
