# google/guava#8692: survey of public code that uses navigation methods on filtered NavigableMaps

Date: 2026-09-24. Research only; nothing posted.

Question (cpovirk on #8692): "the main question is going to be whether we can find someone who is
relying upon some part of it."

What the PR changes (only the `Maps.filterKeys/filterValues/filterEntries(NavigableMap, ...)`
overloads, i.e. `Maps.FilteredEntryNavigableMap`): `first/last/floor/ceiling/higher/lowerEntry`
(also on `descendingMap()/headMap/tailMap/subMap` of the filtered map) return immutable snapshot
entries instead of the backing map's live entries, and `pollFirstEntry/pollLastEntry` return a
snapshot taken before removal. "Relying on it" here means code that (a) gets a filtered map through
one of those overloads, (b) calls one of those methods on it or on its navigable sub-views, and (c)
depends on the returned entry being live (`setValue`, cast to a concrete entry class, `==`,
keeping the entry and expecting later updates to show through, or the old poll result).

## Method

Tool: Sourcegraph public search stream API (`https://sourcegraph.com/.api/search/stream`), no token.

Two steps:

1. **Collect every indexed Java file that calls `filterKeys(` / `filterValues(` / `filterEntries(`**
   (qualified or statically imported), excluding paths under `com/google/common/collect/`.
2. **Download every one of those files** (from `raw.githubusercontent.com` at the commit Sourcegraph
   indexed) **and grep them locally** for `.firstEntry(`, `.lastEntry(`, `.floorEntry(`,
   `.ceilingEntry(`, `.higherEntry(`, `.lowerEntry(`, `.pollFirstEntry(`, `.pollLastEntry(`, and
   separately for any mention of `NavigableMap`. Then read each hit by hand.

I used this local step because Sourcegraph's own `A and B` queries stopped at the ~60 s server limit
and reported `shard-match-limit`, so they could not be trusted to be complete.

### Queries and counts

| # | Query | Files | Repos | Complete? |
|---|---|---|---|---|
| Q1 | `lang:Java patterntype:regexp /Maps\.filter(Keys\|Values\|Entries)/ and /\.(first\|last\|floor\|ceiling\|higher\|lower\|pollFirst\|pollLast)Entry\(/ count:all -repo:^github\.com/google/guava$ select:file` | 10 | 8 | No: `shard-match-limit`, 61 s |
| Q2 | `lang:Java patterntype:regexp /filter(Keys\|Values\|Entries)\(/ and /\.(first\|...\|pollLast)Entry\(/ count:100001000 archived:yes -repo:^github\.com/google/guava$ -file:com/google/common/collect/ select:file timeout:5m` | 16 | 12 | No: `shard-match-limit`, 62 s |
| Q3 | `lang:Java patterntype:literal filterKeys( count:all archived:yes -file:com/google/common/collect/ select:file timeout:5m` | 912 | 303 | Yes (no limit reported, 24 s) |
| Q4 | `lang:Java patterntype:literal filterValues( count:all archived:yes -file:com/google/common/collect/ select:file timeout:5m` | 1310 | 428 | Yes (no limit reported, 22 s) |
| Q5 | `lang:Java patterntype:literal filterEntries( count:all archived:yes -file:com/google/common/collect/ select:file timeout:5m` (run twice) | 407 / 409 | 187 / 189 | No: `shard-match-limit`, 60 s |
| Q6 | `lang:Java patterntype:literal Maps.filterEntries( count:all archived:yes -file:com/google/common/collect/ select:file timeout:5m` | 127 | 80 | Yes (no limit reported, 56 s) |
| Q7 | `lang:Kotlin patterntype:regexp /filter(Keys\|Values\|Entries)\(/ and /\.(first\|...\|pollLast)Entry\(/ count:100001000 archived:yes select:file` | 0 | 0 | Yes (no limit reported) |
| Q8 | `patterntype:regexp /Maps\.filter(Keys\|Values\|Entries)\(/ and /(first\|...\|pollLast)Entry/ -lang:Java count:100001000 archived:yes select:file` | 0 | 0 | Yes (no limit reported) |
| Q9 | Kotlin / Scala / Groovy `Maps\.filter(Keys\|Values\|Entries)\(` (see note below) | KOTLIN_RESULT | | |

Two single-line regex queries (filter call and navigation call on the same line) returned 0 results
but also hit the 60 s limit, so I don't count them as evidence.

Union of Q1 to Q6: **2,482 files**, all downloaded. After dropping 48 files whose `package` is
`*.common.collect` (Guava copies), **1,495 Java files in 494 repositories** contain a
`filterKeys(`/`filterValues(`/`filterEntries(` call. Some of these are other libraries' methods
with the same name (StreamEx, permazen, purefun and others). Of those files:

- **9** also contain a call to one of the eight navigation/poll methods listed above (one of them is
  Azure's vendored Guava copy under a non-`common.collect` package).
- **38** mention `NavigableMap`.

I read every file in both sets (41 distinct files, listed below; some rows group several files).

### Coverage caveats

- Sourcegraph indexes a large but **not complete** set of public repositories. By default it leaves
  out forks: 296 forked repos were skipped for these queries, and I did not include them. Q3, Q4
  and Q6 reported no limit, but Q5 (`filterEntries(` with or without `Maps.`) did hit
  `shard-match-limit`, so some statically imported `filterEntries(` callers may be missing.
- The local grep looks for a navigation call **in the same file** as the filter call. It would miss
  a filtered `NavigableMap` that is returned or stored in a `NavigableMap`-typed member and then
  navigated in **another** file. To narrow that gap I read every file that both calls a filter
  method and mentions `NavigableMap` (the second set above). None of them expose such a map through
  a non-private method or field (details in the table). A filtered map returned as `Map` or
  `SortedMap` can't be navigated without a cast.
- Absence in Sourcegraph's index is not absence in public code, and says nothing about
  Google-internal or other private code.
- Sourcegraph rate-limited me (HTTP 429) after the bulk download step. See the note on Q9.

## Candidates examined

"Overload" means the NavigableMap overload is chosen at the call site (static type of the first
argument is `NavigableMap` or a subtype such as `TreeMap`/`ConcurrentSkipListMap`).

### A. Files with a navigation/poll call (9 from the local grep, plus Guava copies returned by Q1/Q2)

| Repo | File:line | NavigableMap overload? | Navigation method called on the filtered map | Live-entry dependence |
|---|---|---|---|---|
| Consensys/teku (indexed as `Consensys-Incorporated/teku`, same commit as `Consensys/teku` master `524c297`) | [Eth1DataCache.java#L197](https://github.com/Consensys/teku/blob/524c297a5b0111fc3d3145a2d53b4ee9fe1dfa6a/beacon/validator/src/main/java/tech/pegasys/teku/validator/coordinator/Eth1DataCache.java#L197) (filter), [#L129](https://github.com/Consensys/teku/blob/524c297a5b0111fc3d3145a2d53b4ee9fe1dfa6a/beacon/validator/src/main/java/tech/pegasys/teku/validator/coordinator/Eth1DataCache.java#L129) (use) | **Y**: `Maps.filterValues(unfiltered, ...)` where `unfiltered` is a `NavigableMap<UInt64, Eth1Data>` (`Maps.transformValues` of a `ConcurrentSkipListMap.subMap`, L189-196); the result is returned from a `private NavigableMap<...> getVotesToConsider` (L187) | **Y**: `lastEntry()`, at L129: `votesToConsider.isEmpty() ? state.getEth1Data() : votesToConsider.lastEntry().getValue();` | **N**: only `.getValue()` is read, right away |
| gerrit-review/gerrit | [ChangeBundle.java#L330](https://github.com/gerrit-review/gerrit/blob/7d35ff3fbeddc22fd2e0b42ff3f971598bba0c25/java/com/google/gerrit/server/notedb/ChangeBundle.java#L330), filter at L363 | N: `Maps.filterKeys(in, ...)` with `Map<K, V> in` | N: `firstEntry()` is called on the `patchSets` field, not on a filtered map | N |
| apache/pulsar | [ManagedLedgerFactoryImpl.java#L393](https://github.com/apache/pulsar/blob/5e90511526f5b30323a3acb2b57d3c936fe26717/managed-ledger/src/main/java/org/apache/bookkeeper/mledger/impl/ManagedLedgerFactoryImpl.java#L393) | N: filter of a `transformValues` view, returned as `Map` | N: `lastEntry()` at L1350 is on an unrelated `NavigableMap ledgers` parameter | N |
| cdapio/cdap | [InMemoryTableService.java#L308](https://github.com/cdapio/cdap/blob/909aeb353697a41c9dbaa26e966b0af3d63c9229/cdap-data-fabric/src/main/java/io/cdap/cdap/data2/dataset2/lib/table/inmemory/InMemoryTableService.java#L308) | N: argument has static type `SortedMap<Long, Update>` (L306), so the SortedMap overload | N: `lastEntry()` at L133/L154 is on unfiltered `colMap`/`columnMap` | N |
| permazen/permazen | [Transaction.java#L3490](https://github.com/permazen/permazen/blob/17c866b82ed2cbf20356fc0fcaddf2f726fc63ee/permazen-core/src/main/java/io/permazen/core/Transaction.java#L3490) | N: `indexSet.filterKeys(keyRanges)` is permazen's own API, not Guava | N: `pollFirstEntry()` at L3051 is on an unrelated `pending` map | N |
| tonivade/purefun | [ImmutableTreeMap.java#L126](https://github.com/tonivade/purefun/blob/cb9cbbc7db1a22e291a2419d5dae764f7c0f56c0/core/src/main/java/com/github/tonivade/purefun/data/ImmutableTreeMap.java#L126) | N: its own `filterKeys`/`filterValues` methods, not Guava | N | N |
| Scaseco/jena-sparql-api | [TestStateSpaceSearch.java#L533](https://github.com/Scaseco/jena-sparql-api/blob/6138a2e389608a4a755f0e8113b4a91e7a1071d3/jena-sparql-api-cache/src/test/java/org/aksw/jena_sparql_api/cache/tests/TestStateSpaceSearch.java#L533) | N: commented-out `Multimaps.filterEntries` | N: L568 is commented out and uses a different method | N |
| rcore-os/tgoskits | [GuavaCarpet.java#L376](https://github.com/rcore-os/tgoskits/blob/8733618c36a52300d11acbde4c33a0f3fb4c7bd2/apps/starry/java-jse/programs/lib-carpets/GuavaCarpet.java#L376) | N: `left` is `Map<String,Integer>` (an `ImmutableMap`, L367) | N: `firstEntry()` at L222-224 is on a `TreeMultiset` | N |
| Azure/azure-sdk-for-java | `sdk/cosmos/.../implementation/guava25/collect/Maps.java` | n/a (vendored copy of Guava's `Maps`) | n/a | n/a |
| OpenMPDK/SMDK | `.../third_party/java/src/com/google_voltpatches/common/collect/Maps.java` (from Q2) | n/a (vendored Guava copy) | n/a | n/a |
| antlr/codebuff (5 files) | `corpus/java/training/guava/collect/Maps.java`, `output/java_guava/*/Maps.java` (from Q2) | n/a (Guava source used as a corpus) | n/a | n/a |

(The last three rows come from Q1/Q2. The local step either dropped them as `common.collect`
packages or treated them as Guava copies. Q1 also returned several decompiled Guava `Maps.java`
copies, e.g. 7uup/TsojanScan-Plus, Pinball3D/Rabbit-R1, emptybottle-null/Godzilla_null,
tsuzcx/qq_apk. I excluded these as Guava copies too.)

### B. Files that mention `NavigableMap` but make no navigation/poll call (reviewed for overload use, sub-view use and public exposure)

| Repo | File:line | NavigableMap overload? | What is done with the filtered map | Affected by the PR? |
|---|---|---|---|---|
| MartinHaeusler/chronos | [InMemoryCommitMetadataStore.java#L74](https://github.com/MartinHaeusler/chronos/blob/d860bd5092ac2b45356fd9546170fb5a76e03f8e/org.chronos.chronodb.api/src/main/java/org/chronos/chronodb/inmemory/InMemoryCommitMetadataStore.java#L74) (also L131, L169, L199) | **Y**: `NavigableMap<Long, byte[]> subMap = Maps.filterValues(subMap, ...)` | `keySet()/descendingKeySet()` iterators and `entrySet()`. At L201 it is passed to `NavigableMapUtils.entriesAround`, which uses `headMap(..).descendingMap()` / `tailMap(..)` and their `entrySet()` (NavigableMapUtils.java L20-21), with no `*Entry()` navigation calls | N (only iteration, which the PR does not change) |
| OpenMPDK/SMDK (vendored VoltDB) | [ChannelDistributer.java#L667](https://github.com/OpenMPDK/SMDK/blob/4a38421355b84aab298c3c64d10a6c7ec34d2c6c/src/app/voltdb/voltdb_src/src/frontend/org/voltdb/importer/ChannelDistributer.java#L667), L706 | **Y** (result held as `NavigableMap<ChannelSpec,String> pruned`) | `pruned.entrySet()` (L675); `filterValues(specs, ...).navigableKeySet()` (L706) | N |
| OpenMPDK/SMDK (vendored VoltDB) | [ModuleManager.java#L345](https://github.com/OpenMPDK/SMDK/blob/4a38421355b84aab298c3c64d10a6c7ec34d2c6c/src/app/voltdb/voltdb_src/src/frontend/org/voltdb/modular/ModuleManager.java#L345) | **Y** (`NavigableMap<URI,Bundle> stopped`) | `stopped.entrySet()` iteration only | N |
| OpenMPDK/SMDK (vendored VoltDB) | TestFuzzMeshArbiter.java#L444 | held as `Map` | `Map` use only | N |
| tsantalis/RefactoringMiner | 3 copies of VoltDB `ChannelDistributer.java` / `ChannelChangeNotifier.java` under `src/test/resources/oracle/commits/` | same code as VoltDB above | same as above | N |
| palantir/atlasdb | [DbKvsGetRanges.java#L226](https://github.com/palantir/atlasdb/blob/cc7262e5878eef81813dc2494e6d265d9b164910/atlasdb-dbkvs/src/main/java/com/palantir/atlasdb/keyvalue/dbkvs/impl/ranges/DbKvsGetRanges.java#L226) | **Y** (`Maps.filterKeys(request.isReverse() ? cellsByRow.descendingMap() : cellsByRow, ...)` into `NavigableMap cellsForBatch`) | `keySet()`, then `RowResults.viewOfMap(...)`, which uses `map.entrySet()` (RowResults.java L39-41) | N |
| palantir/atlasdb | RowResults.java, ValidatingTransactionScopedCache.java, SerializableTransaction.java, SnapshotTransaction.java | not determined per call; none of these files calls a navigation/poll method | `Map`-style use | N (no navigation call) |
| palantir/gradle-consistent-versions | Dependents.java#L40,47 | not determined | `.values()` / returned as map | N (no navigation call) |
| batfish/batfish | [Configuration.java#L630](https://github.com/batfish/batfish/blob/343bdab16512bc6557992c90c6063e6e7957b2f9/projects/common/src/main/java/org/batfish/datamodel/Configuration.java#L630) | N: `_interfaces` is `Map<String, Interface>` (L261) | returned as `Map` | N |
| github/codeql (+ copy in whitesquirrell/C0deVari4nt) | generated `.../frameworks/guava/generated/collect/Test.java#L5656` | Y (`NavigableMap in`) | taint-flow test stub: `sink(getMapKey(out))` | N |
| jetlinks/jetlinks-community (2 files) | TimescaleDB*QueryOperations.java#L155/L166 | N (`Map` from a query result) | `Map` use | N |
| MangoAutomation/ma-core-public | MockPointValueDao.java#L214 | N: private helper named `filterValues`, not Guava | n/a | N |
| amaembo/streamex (3 files) | EntryStream.java, StreamEx.java, EntryStreamTest.java | N: StreamEx's own `EntryStream.filterKeys/filterValues` | n/a | N |
| apache/causeway | `_Maps.java#L193` | N: own `_Maps.filterKeys` | n/a | N |
| permazen/permazen (8 files) | CoreIndex1-4, IndexMap, AbstractKVNavigableMap/Set, PermazenTransaction | N: permazen's own `filterKeys(KeyFilter)` | n/a | N |
| romainpiel/guava-light | Platform.java | n/a (Guava fork) | n/a | n/a |

## Summary counts

- Java files in Sourcegraph's index that call `filterKeys(`/`filterValues(`/`filterEntries(`
  (non-Guava-copy): 1,495 in 494 repositories (includes same-named non-Guava methods).
- Of these, files that call a navigation/poll method on a map obtained through the NavigableMap
  overload: **1** (Consensys/teku `Eth1DataCache.java`, one `lastEntry()` call).
- Files that depend on a live entry from such a call (`setValue`, cast, `==`, keeping the entry,
  or poll behaviour): **0**.
- Files that get a filtered map through the NavigableMap overload but only iterate it or its
  sub-views (unchanged by the PR): 4 distinct pieces of code (chronos, VoltDB ChannelDistributer and
  ModuleManager, atlasdb DbKvsGetRanges), plus VoltDB copies in SMDK and RefactoringMiner test
  resources.
- Public API that returns a filtered NavigableMap typed as `NavigableMap` (so downstream callers
  could navigate it): none found in these files. teku's `getVotesToConsider` is `private`.
- `pollFirstEntry`/`pollLastEntry` on a filtered map: none found.
- Kotlin/Scala/Groovy: KOTLIN_SUMMARY

## Conclusion

Sourcegraph indexes 1,495 Java files in 494 public repositories that call a method named
`filterKeys`/`filterValues`/`filterEntries`. In those files I found one call to a navigation method
on a map obtained through the `NavigableMap` overload: `lastEntry().getValue()` in Consensys/teku
`Eth1DataCache.java` L129. It reads the value right away, and the PR does not change what that
returns. I found no public code that calls `setValue` on, casts, compares by identity, keeps, or
polls an entry returned by these methods on a filtered `NavigableMap`.

Limits: Sourcegraph does not index all public code, forks were left out, the `filterEntries(` query
hit a result limit, and cross-file uses were checked only as far as described above. This says
nothing about Google-internal or other non-public code.
