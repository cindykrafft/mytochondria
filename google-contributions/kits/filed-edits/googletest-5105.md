# googletest issue #5105: suggested edit to "What happened?"

Posted body matches `kits/googletest-deathtest-issue.json`: WebFetch confirmed the title and eight key sentences verbatim, and the page shows no "edited" marker or human comments. Editing the body in place is fine.

## Why edit

1. **Class A: wrong for `*` and `?`.**
   - Before: "...filter syntax treats `:` as a pattern separator, `-` as the start of negative patterns, and `*` / `?` as wildcards." and "When the name contains one of them, the child's filter matches no test."
   - After: limit the failure to `:` and `-`, and note that `*` and `?` names work.
   - Evidence: I re-ran this on 2026-09-24 against googletest at 4267679 (g++ 13.3, `death_test_style=threadsafe`). The death test is registered through `RegisterTest` under four names, and its statement does not exit:
     ```
     [ RUN      ] S.a*b
         Result: failed to die.
     [  DEATH   ] child ran statement
     [  FAILED  ] S.a*b
     [ RUN      ] S.a?b
         Result: failed to die.
     [  DEATH   ] child ran statement
     [  FAILED  ] S.a?b
     [ RUN      ] S.a-b
     WARNING: filter "S.a-b" did not match any test; no tests were run
     [       OK ] S.a-b
     [ RUN      ] S.a:b
     WARNING: filter "S.a:b" did not match any test; no tests were run
     [       OK ] S.a:b
     ```
     With `*` or `?`, the pattern still matches the name itself, so the child runs the statement. Only `:` (`gtest.cc:831`, `SplitString(filter, ':', ...)`) and `-` (`gtest.cc:872`) cause the problem.
   - A maintainer who tries a `*` name would see the claim fail.

Everything else checks out (class C):
- The `d1` repro output matches the issue.
- The code lines are right: `gtest-death-test.cc:1372/778/972` build `filter=` from `test_suite_name() + "." + name()`, and `:482-483` has `if (bytes_read == 0) set_outcome(DIED)`.
- Typed-test names go through `GenerateNames` with no validation, unlike parameterized names (`IsValidParamName`, `gtest-param-util.h:659`).
- Windows and Fuchsia always create re-exec death tests (`gtest-death-test.cc:1435-1444`). The OS field says this is "by code inspection", which is appropriately hedged.

"Possible fixes" (the `additional` field) needs no change. "Escape the filter's special characters" is still a valid option.

## Revised field: `what-happened` ("What happened?" section). Other fields unchanged.

```markdown
In the "threadsafe" death test style (and always on Windows and Fuchsia), the parent re-executes the test binary and selects the current test with `--gtest_filter=<suite>.<name>`, built from the raw test name (`gtest-death-test.cc`, around lines 1372, 778 and 972). The name is not escaped, but filter syntax treats `:` as a pattern separator and `-` as the start of negative patterns. (`*` and `?` are wildcards too, but in my testing a name containing them still matches itself, so those death tests run normally.)

Test names can legitimately contain these characters. Typed-test name generators aren't restricted (a generator returning `"std::string"` is natural), and neither are names passed to `RegisterTest`.

When the name contains `:` or `-`, the child's filter matches no test. The child prints `WARNING: filter "..." did not match any test; no tests were run` and exits with status 0 without writing a status byte. `DeathTestImpl::ReadAndInterpretStatusByte` then treats the missing byte as `DIED` (around line 482). As a result:

- a death test whose statement does **not** die **passes** without the statement ever running;
- a correct death test such as `EXPECT_EXIT(_exit(1), ExitedWithCode(1), "")` fails with `died but not with expected exit code: Exited with exit status 0`.

The same tests instantiated for a type named `int` behave correctly.

Expected: the death test runs its statement in the child regardless of the characters in the test name. Separately, a child that exits without reaching the death test statement should probably be reported as an error, not as `DIED`.
```
