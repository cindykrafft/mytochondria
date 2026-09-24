**Title:** Fix "With diff" output for strings ending in a newline

When an `EXPECT_EQ` / `EXPECT_STREQ` failure between multi-line strings prints a diff, `SplitEscapedString` splits the escaped values on `\n`. Its loop condition `i + 1 < end` ([gtest.cc:1631](https://github.com/google/googletest/blob/4267679b6887f349f17b01ccd70c9e3483689b25/googletest/src/gtest.cc#L1631)) stops before the last character before the closing quote. So, as far as I can tell, an escaped `\n` at the very end of the string is not treated as a line break.

For strings with a trailing newline, the last line of the diff then includes a literal `\n`:

```c++
EXPECT_EQ(std::string("alpha\nbeta\ngamma\n"), std::string("alpha\nbeta\ndelta\n"));
```

Before:

```
With diff:
@@ -1,3 +1,3 @@
 alpha
 beta
-gamma\n
+delta\n
```

After:

```
With diff:
@@ -1,4 +1,4 @@
 alpha
 beta
-gamma
+delta
 
```

Similarly, `"a\n"` vs `"a\n\n"` used to report the line `a` as changed (`-a\n` / `+a` / `+\n`). It now shows a single added empty line.

The fix changes the loop condition to `i < end`. `end` is at most `str.size()`, so the extra iteration stays in bounds; if the last character were a backslash, it would only set `escaped` before the loop ends.

Added `AssertionTest.EqFailureWithDiffAndTrailingNewline` next to the existing `EqFailureWithDiff` test. It fails without the change and passes with it. The full test suite passes.
