**Title:** Fix "With diff" output for strings ending in a newline

When an `EXPECT_EQ` / `EXPECT_STREQ` failure between multi-line strings prints a diff, `SplitEscapedString` splits the escaped values on `\n`. Its loop condition `i + 1 < end` never looks at the last character before the closing quote. So an escaped `\n` at the very end of the string is not treated as a line break.

For strings with a trailing newline, which is common for file contents and generated text, the diff is misleading:

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

The fix changes the loop condition to `i < end`. A printed string cannot end in a lone backslash, so looking at the last character is safe.

Added `AssertionTest.EqFailureWithDiffAndTrailingNewline` next to the existing `EqFailureWithDiff` test. It fails without the change and passes with it. The full test suite passes.
