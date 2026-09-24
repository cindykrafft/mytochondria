# google/guava#8692: cross-file follow-up survey (filtered NavigableMap created in one place, navigated elsewhere)

Date: 2026-09-24. Research only; nothing posted, nothing pushed.

Follow-up to `guava-8692-usage-survey.md`, which only looked for a navigation call **in the same
file** as the `filterKeys`/`filterValues`/`filterEntries` call. cpovirk's question on #8692 was
"whether we can find someone who is relying upon some part of it (like maybe to call `setValue`,
hopefully with values that are valid!)".

What the PR changes (from the diff at `64248f2`, `Maps.java` ~3236-3334): on
`Maps.FilteredEntryNavigableMap` only, `entryIterator()` and `descendingEntryIterator()` now yield
`immutableEntry` copies, and `pollFirstEntry()`/`pollLastEntry()` return a copy taken before
removal. `AbstractNavigableMap` uses those two iterators for `firstEntry()`, `lastEntry()`,
`pollFirstEntry()`, `pollLastEntry()` (AbstractNavigableMap.java L46-61), and
`floor/ceiling/higher/lowerEntry` go through filtered `headMap`/`tailMap` views. `entrySet()`
(overridden to `filteredDelegate.entrySet()`), `values()`, `navigableKeySet()` and the
`entrySet()` of `descendingMap()/headMap/tailMap/subMap` (which are again filtered navigable maps)
are unchanged. So code is affected only if it (a) gets a map through the `NavigableMap` overload,
(b) calls one of the eight `*Entry` navigation/poll methods on it or on one of its navigable
sub-views, and (c) calls `setValue` on the result, casts it to a concrete entry class, compares it
with `==`, holds on to it expecting later map changes to show, or depends on the old poll result.

## Method

Tool: Sourcegraph public search stream API (no token), plus local grep over downloaded files.
Raw files came from `raw.githubusercontent.com` (or `sourcegraph.com/<repo>@<commit>/-/raw/`) at
the commit Sourcegraph had indexed.

### A. Outflow from creation sites

I did not re-run the collection queries. I reused the 2,482 files that the first survey had
already downloaded (the union of its Q1-Q6, same commits, same day). As in that survey, I
excluded files in `*.common.collect` packages and Guava copies, which leaves 1,495 Java files in
494 repos. I also skipped the generated CodeQL taint-test stubs (`github/codeql` and a copy in
`whitesquirrell/C0deVari4nt`), which call every overload with a `NavigableMap in` and pass the
result to `sink(...)`.

Local passes over these files (scripts in the session scratchpad, not in the repo):

1. **Argument type.** For every `filter(Keys|Values|Entries)(` call I pulled out the first
   argument and flagged the call if the argument is a variable declared in the file as
   `NavigableMap`/`TreeMap`/`ConcurrentSkipListMap`/`ConcurrentNavigableMap`/`ImmutableSortedMap`,
   an expression containing `descendingMap`/`headMap`/`tailMap`/`subMap`/`navigableKeySet`/`new
   TreeMap`/`unmodifiableNavigableMap` etc., or a call to a method declared in the file with one
   of those return types. I also listed every identifier argument in a file that mentions one of
   those types, printed its declarations, and checked each one by hand (117 calls).
2. **Result used as NavigableMap.** Every filter call whose statement mentions `Navigable`, or
   that is `return`ed from a method whose declared return type mentions `Navigable`.
3. **Assignment.** Every `x = ...filter*(` where `x` is declared in the file with a navigable
   type, or declared with `var` (13 `var` sites, each read).
4. **Filter call used as an argument** (`foo(..., Maps.filterKeys(...))`), 582 sites. I dropped
   the ones where the outer call copies the map (`copyOf`, `putAll`, `new HashMap<>`, etc.) or
   where the argument's declared type is plain `Map`, and read the rest by hand (about 110).

For each flow where the filtered map leaves the method, I followed it inside the repo (Sourcegraph
`repo:`-scoped searches for the method/field name, then read the consumers). For consumers in
other repos I searched Sourcegraph for the method name.

### B, C, D. Reverse searches for code that depends on live navigation entries

| # | Query (all `count:all archived:yes timeout:5m` unless noted) | Result | Limit hit? |
|---|---|---|---|
| B1 | `lang:Java patterntype:regexp \.(first\|last\|floor\|ceiling\|higher\|lower\|pollFirst\|pollLast)Entry\([^;]*\)\s*\.\s*setValue\(` | 22 files / 22 repos, all copies of the JDK test `test/jdk/java/util/SequencedCollection/BasicMap.java` | No (43 s) |
| B2 | `lang:Java patterntype:regexp /\.(first\|...\|pollLast)Entry\(/ and /\.setValue\(/ select:file` | 798 files / 243 repos. After dropping JDK `java/util` copies and Guava copies, 307 files remained and I downloaded all 307. A local grep found 1,461 sites in 88 files where a variable assigned from a navigation/poll call has `.setValue(` called on it within 80 lines. I read the ones not inside an expect-UOE test (`shouldThrow`/`fail(`/`assertThrows`/`UnsupportedOperationException` nearby) | No limit reported, but it took 55.7 s, close to the ~60 s server limit |
| C1 | `lang:Java patterntype:regexp \(\s*[A-Z][\w.]*(<[^>;]*>)?\s*\)\s*\(?[\w.]+\.(first\|...\|pollLast)Entry\(` (cast of a navigation result) | 70 files / 52 repos; after dropping casts to `Map.Entry`/`Entry` I read the rest. Nearly all cast `.getValue()`, not the entry | **Yes: `shard-match-limit`**, 65 s |
| C2 | `lang:Java patterntype:regexp (\.(first\|last\|floor\|ceiling\|higher\|lower)Entry\([^()]*\)\s*[!=]=[^=])\|([!=]=\s*[\w.]+\.(first\|...\|lower)Entry\()` (identity), then dropped `== null` locally | 41 files / 33 repos; 8 non-null lines read | **Yes: `shard-match-limit`**, 61 s |
| D1 | `patterntype:regexp file:\.(kt\|scala\|groovy)$ (first\|...\|pollLast)Entry\([^;]*\)\s*[!?]*\.\s*setValue\(` | 0 | No |
| D2 | `patterntype:regexp file:\.(kt\|scala\|groovy)$ /(first\|...\|pollLast)Entry\(/ and /setValue\(/ select:file` | 11 files / 9 repos, all read | No (54 s) |
| X1 | `lang:Java patterntype:regexp getRows\(.*\)\.(first\|...\|pollLast)Entry\(` (timeout 3m) | 0 | No |
| X2 | `lang:Java patterntype:regexp /import com\.palantir\.atlasdb/ and /\.(first\|...\|pollLast)Entry\(/ select:file` | 6 files, all in palantir/atlasdb itself | No |
| X3 | `lang:Java patterntype:regexp (unmodifiableNavigableMap\|synchronizedNavigableMap\|checkedNavigableMap\|unmodifiableSortedMap\|ForwardingNavigableMap)\(\s*(Maps\.)?filter(Keys\|Values\|Entries)\(` (timeout 3m) | 0 | No |
| repo-scoped | `repo:^github\.com/palantir/atlasdb$` for `rowLoader`, for `ValidatingTransactionScopedCache\.create\|\.(first\|...)Entry\(`, and for `areRowResultsEqual`; `m_specs` (all repos); `stopBundles(`; `(getResetterShadowTypes\|getVisibleShadowTypes\|nonProjectConstraints)\(` | used to follow flows (details in the table) | No |

Kotlin/Scala A-strategy: the first survey's Q9 (`lang:Kotlin Maps\.filter(Keys|Values|Entries)\(`)
found 0 Kotlin files, and Q10 found one Groovy file with no navigation. Kotlin's own
`Map.filterKeys` returns a new `LinkedHashMap`, not a Guava view. So I only ran the reverse
searches (D1, D2) for these languages.

### Coverage caveats

- Sourcegraph indexes a large but **incomplete** set of public repositories. Every query skipped
  forked repositories (283-296 per query, per Sourcegraph's own report), and I did not include
  them. The upstream `VoltDB/voltdb` repo, for example, did not appear; I only saw VoltDB code
  vendored in OpenMPDK/SMDK and in RefactoringMiner test resources.
- C1 and C2 hit `shard-match-limit`, so their results are incomplete. B2 did not report a limit,
  but it ran close to the time limit.
- The A passes are regex heuristics, not type resolution. They can miss a `NavigableMap`-typed
  argument declared in another file (for example a superclass field or another class's getter)
  whose result is then passed straight into a `NavigableMap` parameter or assigned to a field
  declared elsewhere. Pass 4 reduces this gap but does not close it.
- B2 finds only the pattern "entry variable assigned from a navigation call, then `.setValue` on
  it in the same file within 80 lines". An entry passed to another method, or compared or kept in
  a collection, would not be found this way. C1/C2 cover casts and `==` only in the literal forms
  given.
- Sourcegraph returned HTTP 429 during the first survey. In this session, no query returned an
  error or an empty stream that looked like rate limiting. I downloaded raw files from
  `raw.githubusercontent.com`; one download failed with a TLS reset and succeeded on retry.
- This says nothing about Google-internal code or other private code.

## Candidates

Verdicts: **AFFECTED** means behaviour would change under the PR. **NOT AFFECTED** means it would
not, based on the code read. **UNCERTAIN** means something needed for a verdict is unknown.

### A. Filter calls that use the NavigableMap overload, and where their results go

I found 31 such calls in 7 code bases, not counting the CodeQL stubs and the RefactoringMiner
copies of VoltDB (14 more calls): teku 1, chronos 4, VoltDB-in-SMDK 12, atlasdb 6, gradle 4,
robolectric-in-kiwibrowser 2, gradle-consistent-versions 2. The table covers every call whose
result leaves the method it was created in, plus the flows the first survey had missed.

| Code (fixed commit) | Creation | Where the filtered NavigableMap goes | Navigation / live-entry use found | Verdict |
|---|---|---|---|---|
| palantir/atlasdb `ValidatingTransactionScopedCache` | [L157](https://github.com/palantir/atlasdb/blob/cc7262e5878eef81813dc2494e6d265d9b164910/atlasdb-impl-shared/src/main/java/com/palantir/atlasdb/keyvalue/api/cache/ValidatingTransactionScopedCache.java#L142-L160): `return Maps.filterKeys(remoteReads, toReadSorted::contains);` inside the `rowLoader` lambda, where `remoteReads` is a `NavigableMap<byte[], RowResult<byte[]>>` (L142) | The lambda goes to `delegate.getRows(...)`. [TransactionScopedCacheImpl L131-L133](https://github.com/palantir/atlasdb/blob/cc7262e5878eef81813dc2494e6d265d9b164910/atlasdb-impl-shared/src/main/java/com/palantir/atlasdb/keyvalue/api/cache/TransactionScopedCacheImpl.java#L131-L133) returns `rowLoader.apply(rows)` unchanged when `!valueStore.isWatched(tableRef)` (the watched path copies it into a new `TreeMap`, L237-238). The result becomes `cacheReads`, is compared by `ByteArrayUtilities.areRowResultsEqual` (`entrySet()`, `containsKey`, `get`), and is returned (L159-160) to [SnapshotTransaction.getRows L489-L500](https://github.com/palantir/atlasdb/blob/cc7262e5878eef81813dc2494e6d265d9b164910/atlasdb-impl-shared/src/main/java/com/palantir/atlasdb/transaction/impl/SnapshotTransaction.java#L489-L500), which returns it from the public `Transaction.getRows` API. `SerializableTransaction.getRows` (L209-213) passes it on after `ret.values()`. As far as I read, this path is taken only when the column selection is not "all columns", the lock-watch cache exists for the transaction (`CacheStoreImpl` L63-68 always wraps it in `ValidatingTransactionScopedCache`), `random.nextDouble() < validationProbability` (L186-187), and the table is not watched. | In atlasdb, no `*Entry` navigation call on a `getRows` result (repo-scoped search: the 6 navigation sites in atlasdb are on unrelated maps). X1 and X2 found no public code that navigates a `getRows(...)` result or imports atlasdb and calls a navigation method, outside atlasdb itself. | NOT AFFECTED as far as found. This is the only flow I found where a filtered `NavigableMap` can reach callers of a published library's public API as a `NavigableMap`. What callers outside Sourcegraph's index do with it is unknown. |
| palantir/atlasdb `SerializableTransaction` | [L747](https://github.com/palantir/atlasdb/blob/cc7262e5878eef81813dc2494e6d265d9b164910/atlasdb-impl-shared/src/main/java/com/palantir/atlasdb/transaction/impl/SerializableTransaction.java#L729-L749), [L905, L910](https://github.com/palantir/atlasdb/blob/cc7262e5878eef81813dc2494e6d265d9b164910/atlasdb-impl-shared/src/main/java/com/palantir/atlasdb/transaction/impl/SerializableTransaction.java#L895-L913): `reads = Maps.filterKeys(reads, ...)` on `tailMap/headMap` views of a `ConcurrentSkipListMap` (L444-445), returned from two `private NavigableMap` methods | L720 and L783: `Maps.transformValues(..., ByteBuffer::wrap)`, then `.entrySet()` in `isEqual`. L842: `.entrySet().iterator()` | None. Only `entrySet()` iteration | NOT AFFECTED |
| palantir/atlasdb `RowResults.createFilterColumns` | [L72](https://github.com/palantir/atlasdb/blob/cc7262e5878eef81813dc2494e6d265d9b164910/atlasdb-client/src/main/java/com/palantir/atlasdb/keyvalue/impl/RowResults.java#L72): `Maps.filterKeys(row.getColumns(), keepColumn)`, where `RowResult.getColumns()` returns `NavigableMap` (RowResult.java L75) | Passed to `RowResult.create`, which copies it: `ImmutableSortedMap.copyOf(columns, ...)` (RowResult.java L64) | None | NOT AFFECTED |
| palantir/atlasdb `DbKvsGetRanges` | L226 (in first survey) | `RowResults.viewOfMap` → `entrySet()` | None | NOT AFFECTED |
| VoltDB `ChannelDistributer` (vendored in OpenMPDK/SMDK; also 3 copies in tsantalis/RefactoringMiner test resources) | [L1465](https://github.com/OpenMPDK/SMDK/blob/4a38421355b84aab298c3c64d10a6c7ec34d2c6c/src/app/voltdb/voltdb_src/src/frontend/org/voltdb/importer/ChannelDistributer.java#L1463-L1466): `next = Maps.filterEntries(prev, not(inRemoved));`, stored with `m_specs.compareAndSet(prev, next, ...)`. `m_specs` is a package-private `SpecsRef extends AtomicStampedReference<NavigableMap<ChannelSpec,String>>` (L254, L1541). **The first survey missed this flow.** | Readers of `m_specs` (all repos, `m_specs` search): L640 `specs = m_specs.getReference()` → L667 `Maps.filterEntries(specs, ...)` → `.entrySet()`, L706 `.navigableKeySet()`; L1231-1236 re-filter → `.navigableKeySet()` / `putAll` into an `ImmutableSortedMap` builder; TestChannelDistributer [L196-L199](https://github.com/OpenMPDK/SMDK/blob/4a38421355b84aab298c3c64d10a6c7ec34d2c6c/src/app/voltdb/voltdb_src/tests/frontend/org/voltdb/importer/TestChannelDistributer.java#L196-L199) `Maps.filterValues(...m_specs.getReference(), ...).navigableKeySet()`. The other overload calls in the file (L430, L489, L1232, L1235, L1445) are copied into `ImmutableSortedMap` builders. | None. No `*Entry` call in the file or the test | NOT AFFECTED |
| VoltDB `ModuleManager.BundleRef.stopBundles` (SMDK) | [L345](https://github.com/OpenMPDK/SMDK/blob/4a38421355b84aab298c3c64d10a6c7ec34d2c6c/src/app/voltdb/voltdb_src/src/frontend/org/voltdb/modular/ModuleManager.java#L335-L359): `NavigableMap<URI,Bundle> stopped = Maps.filterKeys(expect, in(bundles));`, returned from the package-private `stopBundles` of `static class BundleRef` (L227) | Callers (Sourcegraph `stopBundles(`, all repos): L196 discards the result; L364 `stopBundles(bundles).entrySet()` | None | NOT AFFECTED |
| gradle/gradle `DefaultIncrementalInputProperties.nonIncrementalChanges` | [L46-L47](https://github.com/gradle/gradle/blob/4dc5857f86521be279e983495155f4d3d67399df/platforms/core-execution/execution/src/main/java/org/gradle/internal/execution/history/changes/DefaultIncrementalInputProperties.java#L44-L48): `Maps.filterKeys(previous, ...)`, `Maps.filterKeys(current, ...)` with `ImmutableSortedMap` parameters | Passed to `new DefaultInputFileChanges(SortedMap, SortedMap)` and stored in `SortedMap` fields of `AbstractFingerprintChanges` (L41-47). Used through `get()` and `SortedMapDiffUtil.diff`, which iterates `entrySet()` (SortedMapDiffUtil L28-35). L55-56 copy into `ImmutableSortedMap.copyOfSorted`. | None | NOT AFFECTED |
| robolectric `RobolectricModel` (old copy in kiwibrowser/src; current robolectric/robolectric has a different API) | [L356-L372](https://github.com/kiwibrowser/src/blob/86afd150b847c9dd6f9ad3faddee1a28b8c9b23b/third_party/robolectric/robolectric/processor/src/main/java/org/robolectric/annotation/processing/RobolectricModel.java#L356-L372): `Maps.filterEntries(shadowTypes, ...)` with `TreeMap shadowTypes` (L72), returned from public methods typed `Map` | L268, L276 `.entrySet()`; L375 re-filters through the `Map` overload. No other callers found | None | NOT AFFECTED |
| palantir/gradle-consistent-versions `Dependents` | [L40, L47](https://github.com/palantir/gradle-consistent-versions/blob/253122ec6acf31c12afdb095b0b003c57b1c3dd5/src/main/java/com/palantir/gradle/versions/lockstate/Dependents.java#L39-L48): `Maps.filterKeys(get(), ...)` where `get()` returns `NavigableMap` | L40 `.values().stream()`; L47 returned as `Map` from `nonProjectConstraints()`, whose only caller is LockStates.java L79 `.entrySet().stream()` | None | NOT AFFECTED |
| MartinHaeusler/chronos, Consensys/teku, VoltDB `TestFuzzMeshArbiter` | as in the first survey | chronos L201 passes the map to `NavigableMapUtils.entriesAround` (sub-view `entrySet()`); teku's `private getVotesToConsider` → L129 `lastEntry().getValue()` | teku reads `getValue()` right away | NOT AFFECTED |
| google/libphonenumber `DisjointRangeMap` L143 (and a copy in ric2b/Vivaldi-browser) | The flag was a false positive: the argument is the `SortedMap` constructor parameter (L141), so the `SortedMap` overload is used, and the result is copied with `ImmutableSortedMap.copyOfSorted` | n/a | n/a | NOT AFFECTED (not the NavigableMap overload) |

Other sites read in passes 3 and 4 (`var` locals and filter calls used as arguments) had no
navigable-typed argument or result, or their result is copied or used only as `Map`: NucleoidMC/fantasy,
fuji-fabric/fuji, bazel ×4, camunda, dCache (`Multimaps`), snow-owl, hmftools (its own
`Multimaps.filterEntries`), Spellsource, EDDI (own method), opendaylight/netconf, indeedeng/proctor,
sosy-lab/cpachecker, caffeine tests, presto/trino `TupleDomain.withColumnDomains`, and similar. None
of these files calls a navigation/poll method.

### B/C/D. Code that depends on live navigation entries (any map)

| Code (fixed commit) | Dependent line | Map type that flows in | Can a filtered NavigableMap reach it? | Verdict |
|---|---|---|---|---|
| JDK `test/jdk/java/util/SequencedCollection/BasicMap.java` (openjdk/jdk `ae1a139` and 21 other JDK forks/distributions) | [L532-533, L593-603](https://github.com/openjdk/jdk/blob/ae1a1399be3028b7ccdc6b3642a3019d8cd66345/test/jdk/java/util/SequencedCollection/BasicMap.java#L532-L533): `assertThrows(UOE, () -> { map.firstEntry().setValue(99); });` | JDK maps | No. The test expects `setValue` to throw | NOT AFFECTED |
| analog-garage/dimple `SkipMapTest` | [L82-L88](https://github.com/analog-garage/dimple/blob/d682b34c29471a983cd0de364d011bd07cd8a902/solvers/java/src/test/java/com/analog/lyric/collect/tests/SkipMapTest.java#L82-L88): `firstEntry = map1.firstEntry(); ... firstEntry.setValue("xxx"); assertEquals("xxx", map1.get(map1.firstKey()));` | dimple's own `SkipMap` (L49 `SkipMap.create(...)`) | No | NOT AFFECTED. It does rely on live navigation entries, but of its own map class |
| apache/activemq-apollo `IntervalSet` (Scala) | [Interval.scala L84-L98, L111-L127](https://github.com/apache/activemq-apollo/blob/8e4b134b2a5d3576aa62cd8df9905a9fe2eba2d0/apollo-leveldb/src/main/scala/org/apache/activemq/apollo/broker/store/leveldb/Interval.scala#L84-L127): `var entry = ranges.floorEntry(limit) ... curr.setValue(range.limit(limit))` | `private final val ranges = new TreeMap[N, Interval[N]]` (L68), where `TreeMap` is `org.apache.activemq.apollo.util.TreeMap` (L24), apollo's own class with `entry.previous` | No (private field, own map class) | NOT AFFECTED. Same pattern as dimple: relies on live navigation entries of its own map |
| landawn/abacus-common `MultiClassRegressionATest` | [L329-L336](https://github.com/landawn/abacus-common/blob/56e79edb1f6891386f9329fec025ef46f87d2389/src/test/java/com/landawn/abacus/util/MultiClassRegressionATest.java#L329-L336): `last = CommonUtil.lastEntry(sorted)...; last.setValue(30); assertEquals(30, sorted.get("c"));` | `CommonUtil.lastEntry(Map)` accepts any map. For a `NavigableMap` it returns `descendingMap().entrySet().iterator().next()`, with the comment "Use the entry-set iterator rather than lastEntry(), so maps such as TreeMap retain their supported write-through setValue behavior" (CommonUtil.java L25595-25598) | Yes, any map can be passed in, but the code uses `descendingMap().entrySet()`, which the PR does not change | NOT AFFECTED |
| boonproject/boon `SearchIndexDefault` | [L279](https://github.com/boonproject/boon/blob/9bc6870dbe5dd58c45c18d8edb493e8efc089463/boon/src/main/java/org/boon/datarepo/impl/indexes/SearchIndexDefault.java#L279): `( ( MultiValue ) this.navigableMap.firstEntry() ).getValue()` (casts the entry) | map from `SPIFactory.getMapCreatorFactory().get().createNavigableMap(...)` (L67-68) | Not through the code I read; Guava filter calls don't appear in this path | NOT AFFECTED (a cast of this kind would fail on JDK maps too) |
| omnetpp/omnetpp `EventLog` | [L351, L387](https://github.com/omnetpp/omnetpp/blob/820d04e7bb0ef53acaf6a41858ee7ea29f2754ca/ui/org.omnetpp.common/src/org/omnetpp/eventlog/EventLog.java#L350-L352): `entry == eventNumberToIndexMap.firstEntry()` | `protected TreeMap<Long, ...>` fields (L47, L49) | No (a field typed `TreeMap` cannot hold a Guava view) | NOT AFFECTED |
| Other C1/C2 hits (optaplanner/timefold, RJ/ketama, herddb, qmq, Hive2Hive, forge, ratis, trafficcontrol, etc.) | cast or compare `.getValue()`/`.getKey()`, not the entry | various | n/a | NOT AFFECTED |
| B2's 85 other files | TCK-style tests (jsr166 `TreeMapTest`, `ConcurrentSkipListMapTest`, sub-map tests, SnapTree, mapdb, j2objc, desugar_jdk_libs, AOSP copies, jdereg `ConcurrentNavigableMapNullSafe`/`SealableNavigableMap` tests, VoltDB `TestCOWSortedMap`) that call `setValue` on navigation entries inside an expect-UnsupportedOperationException block | JDK or custom maps | No | NOT AFFECTED |
| D2 others | PubDeer/astro-loop (`setValue` on an iterator entry), GraphScope (`vertex.setValue`), activemq-apollo `LevelDBClient` (iterator/record entries), and map implementations (mapdb `BTreeMap.kt`, kool/littlekt/scala-js/scala-native `TreeMap`) | n/a | No | NOT AFFECTED |

## Summary counts

- Files searched for creation sites: 1,495 Java files in 494 repos (reused from the first survey).
- Filter calls that use the NavigableMap overload: 31 in 7 code bases (plus 14 in RefactoringMiner
  copies of VoltDB and the CodeQL stubs).
- Flows where such a map leaves the creating method: 11 (table A). Of these, 1 flows to a
  published library's public API typed as `NavigableMap` (atlasdb `Transaction.getRows`, under
  the conditions in the table), 2 are stored in or returned through package-private members
  (VoltDB `m_specs`, `stopBundles`), and the rest are private, copied, or exposed only as
  `Map`/`SortedMap`.
- New flow found that the first survey's same-file method missed: VoltDB `ChannelDistributer`
  storing a filtered map in `m_specs`, and the atlasdb cache path. Neither navigates the map.
- Navigation calls on a filtered `NavigableMap` in another file or method: 0 found. The only
  navigation call remains teku L129 `lastEntry().getValue()` from the first survey.
- Public code that calls `setValue` on, casts, `==`-compares, or keeps an entry returned by a
  navigation/poll method: found (dimple `SkipMap`, activemq-apollo's own `TreeMap`, boon's entry
  cast, omnetpp's `==` on `TreeMap` fields, JDK/TCK tests expecting UOE), but in every case the map
  is a JDK or project-specific class, and I found no path by which a Guava filtered
  `NavigableMap` reaches that code.
- AFFECTED: 0. UNCERTAIN: 0 among the code read. The one open point is callers outside the
  index of atlasdb's `Transaction.getRows` in the configuration described above.

## Conclusion

Following filtered `NavigableMap`s beyond the method that creates them in Sourcegraph's index, I
found 11 flows. None of them calls a navigation or poll method on the map. They iterate
`entrySet()`/`navigableKeySet()`/`values()`, copy the map, or re-filter it, and the PR does not
change any of those. Searching the other way, for code that uses `setValue`, casts, or `==` on
entries returned by navigation methods, I found such code only for JDK maps (tests expecting
`UnsupportedOperationException`) or project-specific map classes (dimple `SkipMap`,
activemq-apollo's `TreeMap`). I found no path from a Guava filtered `NavigableMap` into any of it.

The one place where a filtered `NavigableMap` can reach callers of a published library's API is
atlasdb's `Transaction.getRows`. As far as I read, that happens only with lock-watch caching,
validation sampling, an unwatched table and a partial column selection. In the index, I found no
caller that navigates that result.

Limits: Sourcegraph's index is incomplete and forks were excluded; the cast and identity
queries hit `shard-match-limit`; the type checks are regex heuristics and can miss arguments
declared in other files; the reverse searches find only the literal patterns listed. Nothing here
covers Google-internal or other private code.
