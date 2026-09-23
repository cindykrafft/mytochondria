**Title:** Avoid overflow in `Stats` mean computation for large values of opposite sign

`Stats`, `StatsAccumulator` and `PairedStatsAccumulator` return a wrong-signed infinite mean when the data contains finite values of opposite sign and large magnitude, even though the true mean is finite. I did not find an existing issue for this.

### Repro

```java
double M = Double.MAX_VALUE;
Stats s = Stats.of(M, -M);
s.mean(); s.sum(); s.populationVariance();
Stats.meanOf(M, -M);
Stats.of(1e308, 1e308, -1e308).mean();
Stats.of(1e308, -1e308, 5).mean();
StatsAccumulator acc = new StatsAccumulator();
acc.add(M); acc.add(-M); acc.add(Double.POSITIVE_INFINITY);
acc.mean();
StatsAccumulator x = new StatsAccumulator(); x.add(M);
StatsAccumulator y = new StatsAccumulator(); y.add(-M);
x.addAll(y.snapshot()); x.mean();
PairedStatsAccumulator p = new PairedStatsAccumulator();
p.add(M, 1); p.add(-M, 2);
p.xStats().mean(); p.populationCovariance();
```

| Expression | Before | After | Exact |
|---|---|---|---|
| `Stats.of(MAX, -MAX).mean()` | `-Infinity` | `0.0` | `0` |
| `Stats.of(MAX, -MAX).sum()` | `-Infinity` | `0.0` | `0` |
| `Stats.of(MAX, -MAX).populationVariance()` | `0.0` | `Infinity` | `MAX^2` (overflows) |
| `Stats.meanOf(MAX, -MAX)` | `-Infinity` | `0.0` | `0` |
| `Stats.of(1e308, 1e308, -1e308).mean()` | `-Infinity` | `3.3333333333333337E307` | `3.33e307` |
| `Stats.of(1e308, -1e308, 5).mean()` | `-Infinity` | `1.6666666666666667` | `5/3` |
| accumulator `(MAX, -MAX, +Inf)`, `mean()` | `NaN` | `Infinity` | `+Inf` per the `mean()` Javadoc |
| `acc{MAX}.addAll(Stats{-MAX}).mean()` | `-Infinity` | `0.0` | `0` |
| `PairedStatsAccumulator` `(MAX,1), (-MAX,2)`: `xStats().mean()` | `-Infinity` | `0.0` | `0` |
| same, `populationCovariance()` | `Infinity` | `-8.988465674311579E307` | `-MAX/2` |

"Before" is `master` at 7915234; "after" is this branch. Both were built with the project's toolchain (JDK 26 compiler) and run on JDK 21.

### Root cause

The mean is updated incrementally as `mean += (value - mean) / count` (Knuth, TAOCP vol. 2, 4.2.2). When `value` and `mean` are both finite but have opposite signs and large magnitudes, `value - mean` overflows to an infinity, so the mean becomes an infinity. From then on the mean is non-finite, so later values go through `calculateNewMeanNonFinite`. That is why adding `+Infinity` afterwards produces `NaN` (`-Inf` combined with `+Inf`) instead of the documented `+Infinity`. The same thing happens in `StatsAccumulator.merge` (`delta * otherCount / count`), where `delta * otherCount` can also overflow even when `delta` is finite. `Stats.meanOf(Iterator)` and `Stats.meanOf(double...)` have the same update. `meanOf(int...)` and `meanOf(long...)` cannot overflow this way, because int and long magnitudes are far below `Double.MAX_VALUE`.

### Fix

The existing update is kept as the fast path, with the same expression and evaluation order, so results for all inputs that did not overflow are bit-for-bit unchanged. Only when the update overflows:

- `StatsAccumulator.add`, `Stats.meanOf(Iterator)`, `Stats.meanOf(double...)`: `mean += value / count - mean / count`. Each quotient is at most `MAX / count` in magnitude and `count >= 2`, so the difference is finite, and the new mean lies between the old mean and the value.
- `StatsAccumulator.merge`: `mean = mean * (oldCount / count) + otherMean * (otherCount / count)`. This is a convex combination of two finite means, so it cannot overflow. (An increment form `mean + (otherMean - mean) * w` could still overflow when `w > 1/2`.)
- `sumOfSquaresOfDeltas` is set to `POSITIVE_INFINITY` in these branches. When the fast path overflows, the true sum of squares of deltas is at least about `delta^2 / 2` with `|delta| > MAX / count`, which exceeds `Double.MAX_VALUE` for any `long` count. So `+Infinity` is the overflowed true value, and `populationVariance()` and `sampleVariance()` now return `+Infinity`. Before this change, the overflowed sum was `-Infinity` and `ensureNonNegative` clamped the variance to `0.0`, which was wrong. The variance Javadoc only promises `NaN` when the data contain non-finite values, and that is unchanged.

`PairedStatsAccumulator` needs no change of its own. It uses `StatsAccumulator` for the x and y means, and with a finite `xStats().mean()` its covariance update gives the correct result for the repro above. Covariance can still overflow in the intermediate `(y - Y)` term when the y-values themselves differ by more than `MAX`. That separate case is not addressed here.

There are no public API changes. `android/` is not modified, because it is synced from `guava/`.

### Tests

- `StatsTest`: `testMean_largeValuesOfOppositeSigns`, `testSumAndVariance_largeValuesOfOppositeSigns`, `testMeanOf_largeValuesOfOppositeSigns`. These cover the varargs, `Iterable` and `Iterator` overloads and the `±Infinity` after `(MAX, -MAX)` cases.
- `StatsAccumulatorTest`: `testAdd_largeValuesOfOppositeSigns`, `testAddAll_largeValuesOfOppositeSigns`. The second covers merging `Stats` and `StatsAccumulator`, a 1-vs-3 weighted merge, and a merge where only `delta * otherCount` overflows.
- `PairedStatsAccumulatorTest`: `testAdd_largeXValuesOfOppositeSigns`, `testAddAll_largeXValuesOfOppositeSigns`.

`./mvnw -B -pl guava,guava-testlib,guava-tests test -Dtest.include="com/google/common/math/**"`: 498 tests, 0 failures. With the `guava/src` change reverted, all 7 new tests fail and the existing tests still pass.
