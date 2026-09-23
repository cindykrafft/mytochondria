# guava bug hunt: open issues and unreported bugs (2026-09-23)

Tested against google/guava HEAD `7915234` (2026-09-23). guava was built with its official toolchain: `./mvnw install`, Temurin 26 with error-prone for compilation, and Temurin 21 as the test JDK. Every repro was run on JDK 26 and JDK 21, and the output was identical on both.

Every finding below was reproduced by running code, and each was searched for in guava's issues and PRs (open and closed); none has been reported.
Repro sources are in `scratchpad/gh-{collect,base,io,concurrent}/` and `scratchpad/guava-triage/`.

## Unreported bugs

### 1. Filtered NavigableMap views return wrong or live entries. Medium-high.
Affects `Maps.filterKeys`, `filterValues` and `filterEntries` on a `NavigableMap`.

**Symptom A.** `pollFirstEntry()`/`pollLastEntry()` remove the right key but return the wrong entry.
- With `filterKeys(TreeMap{1,2,3}, k -> k != 1)`, `pollFirstEntry()` returns `3=three` instead of `2=two`.
- Draining an odd-keys filter returns `[2, 4, 6, 7, 9]`, and the even keys among those are ones the filter excludes.
- Root cause: Maps.java:3297 and 3302 use `Iterables.removeFirstMatching`, which returns the live `TreeMap` entry after `iterator.remove()`. `TreeMap` copies the successor's mapping into a deleted two-child node, so the returned entry now shows the successor.

**Symptom B.** `firstEntry`, `lastEntry`, `ceilingEntry`, `floorEntry`, `higherEntry` and `lowerEntry` return live backing entries.
- Their `setValue` works, and it bypasses the `filterValues` predicate.
- The Javadoc says `setValue` throws IAE for a value that fails the predicate, and `TreeMap.firstEntry().setValue` throws UOE.

**Fix:** return snapshots (`Maps.immutableEntry`), taken before `remove()` in the poll methods.

### 2. Stats / StatsAccumulator return a wrong-signed infinite mean for finite inputs. Medium-high.
- `Stats.of(Double.MAX_VALUE, -Double.MAX_VALUE).mean()` is `-Infinity`; the exact mean is 0.
- `Stats.of(1e308, -1e308, 5).mean()` is `-Infinity`.
- `acc.add(MAX); acc.add(-MAX); acc.add(+Inf)` gives `mean()` = NaN, although the `mean()` Javadoc promises +Infinity.
- The merge path, `meanOf`, and `PairedStats` are affected the same way.

**Root cause:** the Welford `delta = value - mean` overflows (StatsAccumulator.java:66–68, 207–209; Stats.java:497, 521). Existing tests only cover same-sign large values.

**Fix:** use an overflow-safe update when `delta` is non-finite.

### 3. `Ints/Longs/…/Booleans.rotate` are wrong for `Integer.MIN_VALUE` and throw on an empty sub-range. Medium.
- `Ints.rotate({1,2,3}, Integer.MIN_VALUE)` gives `[2,3,1]`, but `Collections.rotate` gives `[3,1,2]`. The Javadoc says the two are equivalent.
- `Ints.rotate(arr, 1, 1, 1)` throws `ArithmeticException: / by zero`; only IOOBE is documented.
- All 8 primitive classes are affected.

**Root cause:** `int m = -distance % length` (Ints.java:597, and likewise in the other classes), plus an early return that checks `array.length` instead of the range length.

**Fix:** return early for a range length of 1 or less, and use `Math.floorMod`.

### 4. `BloomFilter.create` throws for valid small or high-fpp settings. Medium-low.
- `BloomFilter.create(funnel, 1, 0.75)` throws "Could not create BloomFilter of 0 bits".
- The same happens for `(0, 0.75)` and `(2, 0.8)`.

**Root cause:** `optimalNumOfBits` truncates to 0 (BloomFilter.java:585).

**Fix:** clamp the bit count to at least 1.

### 5. `ByteSource.slice(a, MAX).slice(b, n)` overflows. Low.
- A second slice with offsets that sum past `Long.MAX_VALUE` throws "offset (-9223372036854775807) may not be negative". Per the Javadoc it should return an empty source, as `ByteSource.wrap` does.

**Root cause:** ByteSource.java:536 uses `this.offset + offset`.

**Fix:** `LongMath.saturatedAdd`.

### 6. `InetAddresses` accepts an empty IPv6 zone ID. Low.
- `isInetAddress("fe80::1%")` returns true, and `forString` builds scope 0.
- The JDK and RFC 4007 reject an empty zone ID.

**Root cause:** InetAddresses.java:233 and 383.

### 7. `UnsignedInts.parseUnsignedInt("-0")`, `decode("0x-0")` and `decode("#+5")` are accepted. Low.
- `UnsignedLongs`, the JDK, and guava's own `UnsignedIntsTest` reject signs.

**Root cause:** UnsignedInts.java:362 delegates to `Long.parseLong`.

### Minor
- `TypeToken.toString()` prints `Outer$Inner<>` for `Outer<String>.Inner`. The JDK prints `Outer<java.lang.String>$Inner`. See Types.java:287–297.

## Open issues with an obvious fix (maintainer-labelled, 0 comments, no PR)
- **#2884:** document that `FluentIterable.toSortedList` is stable. It delegates to `Ordering.immutableSortedCopy`, which documents stability. Labels: type=api-docs, status=triaged.
- **#2690:** document that an exception thrown by the function passed to `Futures.transform` / `transformAsync` (and the `FluentFuture` equivalents) fails the output future. Verified behaviour. Labels: type=api-docs, status=triaged.
- **#2237:** note the performance effect of argument order in `Multisets.intersection` / `union`. Labels: type=api-docs, status=triaged. The benchmark claim needs re-checking before the wording is written.
- Borderline: **#1924**, `DoubleMath.fuzzyEquals` should reject a tolerance of -0.0. It still reproduces, but it would change behaviour and its comments couldn't be read.

## Already reported (ruled out)
- `Range.greaterThan(MAX_VALUE).canonical(integers())` throws AssertionError: #1767.
- `RateLimiter` with a warmup of zero never limits: #2730 / #6475, PR #8586.
- EventBus generic subscriber bridge methods: #1235.
- Items that already have PRs: #7985, #5284, #6076, #4010. Items already fixed at HEAD: #1792, #1480, #2862.
