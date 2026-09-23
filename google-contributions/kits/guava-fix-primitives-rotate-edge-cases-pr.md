**Title:** Fix primitive `rotate` methods for `Integer.MIN_VALUE` distances and empty ranges

The `rotate(array, distance)` and `rotate(array, distance, fromIndex, toIndex)` methods in `Booleans`, `Bytes`, `Chars`, `Doubles`, `Floats`, `Ints`, `Longs` and `Shorts` have two edge-case bugs. The Javadoc says each method is equivalent to `Collections.rotate` on the `asList` view (or its `subList`), but it isn't in these cases.

### Repro

```java
int[] a = {1, 2, 3};
Ints.rotate(a, Integer.MIN_VALUE);
List<Integer> ref = new ArrayList<>(List.of(1, 2, 3));
Collections.rotate(ref, Integer.MIN_VALUE);

double[] d = {1, 2, 3, 4, 5};
Doubles.rotate(d, Integer.MIN_VALUE);

int[] e = {1, 2, 3};
Ints.rotate(e, 1, 1, 1); // empty range
```

Before (33.7.0-jre and current master):

```
Ints.rotate({1,2,3}, MIN_VALUE)        = [2, 3, 1]
Collections.rotate([1,2,3], MIN_VALUE) = [3, 1, 2]
Doubles.rotate({1..5}, MIN_VALUE)      = [3.0, 4.0, 5.0, 1.0, 2.0]   (Collections.rotate: [4.0, 5.0, 1.0, 2.0, 3.0])
Ints.rotate({1,2,3}, 1, 1, 1)          -> java.lang.ArithmeticException: / by zero
```

After:

```
Ints.rotate({1,2,3}, MIN_VALUE)        = [3, 1, 2]
Collections.rotate([1,2,3], MIN_VALUE) = [3, 1, 2]
Doubles.rotate({1..5}, MIN_VALUE)      = [4.0, 5.0, 1.0, 2.0, 3.0]
Ints.rotate({1,2,3}, 1, 1, 1)          -> no-op, array unchanged
```

### Root cause

1. The shift is computed as `int m = -distance % length;`. For `distance == Integer.MIN_VALUE`, `-distance` overflows back to `Integer.MIN_VALUE`, so the array is rotated the wrong way whenever the range length is not a power of two. `Integer.MIN_VALUE + 1` and `Integer.MAX_VALUE` already worked.
2. The early return checks `array.length <= 1`, not the length of the range being rotated. An empty range (`fromIndex == toIndex`) inside an array of length 2 or more reaches `% 0` and throws `ArithmeticException`. The Javadoc documents only `IndexOutOfBoundsException`, and `Collections.rotate` on an empty `subList` does nothing.

### Fix

The same change in all eight classes:

- Compute `length = toIndex - fromIndex` right after the existing `checkNotNull`/`checkPositionIndexes` calls and return early when `length <= 1`. Index validation still runs first, so invalid indices still throw `IndexOutOfBoundsException`.
- Compute `m = -(distance % length)` instead of `-distance % length`. `distance % length` lies in `(-length, length)`, so negating it can't overflow. The existing `m < 0 ? m + length : m` normalization is unchanged.

The one-argument overload calls the four-argument one, so it gets both fixes.

### Tests

The existing `testRotate` and `testRotateIndexed` in each of `BooleansTest`, `BytesTest`, `CharsTest`, `DoublesTest`, `FloatsTest`, `IntsTest`, `LongsTest` and `ShortsTest` now also cover:

- `Integer.MIN_VALUE`, `Integer.MIN_VALUE + 1` and `Integer.MAX_VALUE` on arrays of length 3 and 5, and on sub-ranges of length 3 and 5 inside a 7-element array. The expected values are what `Collections.rotate` produces.
- Empty ranges (`fromIndex == toIndex` at 0, 3 and 7) inside a 7-element array are a no-op.

`./mvnw -B -pl guava,guava-testlib,guava-tests test -Dtest.include="com/google/common/primitives/**"`: 13948 tests, 0 failures. With the main-code change reverted, the new assertions fail in all 8 test classes: 8 failures (wrong rotation for `Integer.MIN_VALUE`) and 8 errors (`ArithmeticException: / by zero`).

I couldn't find an existing issue or PR for either problem.
