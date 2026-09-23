# googletest bug hunt: unreported bugs (2026-09-23)

Tested against google/googletest HEAD `4267679` (2026-09-17), built with g++ 13 at C++17. Some checks were also run at C++20, with clang, and with ASan/UBSan.
Every finding below was reproduced by running code. Each was searched for in googletest's issues and PRs (open and closed) and no existing report was found.
Repro sources: `scratchpad/gt-hunt-{assert,runner,gmock,struct}/`.

## 1. Death tests can falsely pass when a test name contains `:` `-` `*` or `?`. Medium-high.
- In "threadsafe" style (always on Windows and Fuchsia), the parent re-runs the binary with `--gtest_filter=<suite>.<name>`, and the name is not escaped (gtest-death-test.cc:1372, 778, 972).
- A typed-test name generator returning `"std::string"` (legal and unvalidated), or a `RegisterTest` name containing those characters, makes the child's filter match nothing. The child then runs no tests and exits 0.
- The parent reads no status byte and treats that as `DIED` (gtest-death-test.cc:482).
- Result: `EXPECT_EXIT({ /* doesn't die */ }, ExitedWithCode(0), "")` **passes without running the statement**. `EXPECT_EXIT(_exit(1), ExitedWithCode(1), "")` fails with "Exited with exit status 0". The `TT/int` versions of the same tests behave correctly.
- **Fix:** have the child select its test by exact name instead of through filter syntax, and/or treat "child exited without reaching the statement" as an error.

## 2. `WhenBase64Unescaped` reads out of bounds on non-ASCII input. Medium, memory safety.
- `Base64Unescape` (gmock-internal-utils.cc:235–239) iterates the string as `int`. Bytes of 0x80 and above are negative, so `kUnBase64[static_cast<size_t>(src)]` reads before the table, and `isspace(negative)` is undefined behaviour.
- ASan reports a global-buffer-overflow at line 239.
- In a normal build, 64 of the 128 non-ASCII bytes (repeated four times) are **accepted as valid base64**.
- **Fix:** `for (unsigned char src : encoded)`.

## 3. `testing::Range()` wraps around for narrow types or near the type's maximum. Medium.
- `RangeGenerator::CalculateEndIndex` (gtest-param-util.h:279) and `Advance` (241) add `step` without checking for overflow. Results:
  - `Range<unsigned char>(250, 255, 3)` registers 87 tests (250, 253, 0, 3, …) instead of 2.
  - `Range<uint8_t>(0, 255, 2)` hangs forever at registration.
  - `Range(INT_MAX-10, INT_MAX, 7)` hangs and is signed overflow (UBSan).
- This contradicts docs/reference/testing.md:108.
- **Fix:** stop when `end - i <= step`, or when the next value would not increase.

## 4. `--gtest_fail_if_no_test_selected` skips writing the XML/JSON report. Medium.
- The early `return false` in `UnitTestImpl::RunAllTests` (gtest.cc:6113–6126) skips `OnTestIterationEnd`, which is where the report is written. It also skips `OnTestProgramEnd` and environment teardown.
- Without the flag, an empty run writes a report. With the flag, the file is missing, which CI report collectors don't expect.
- **Fix:** mark the run failed and fall through to the normal end-of-iteration path.

## 5. String diffs are wrong when strings end with `\n`. Low, misleading output.
- `SplitEscapedString` (gtest.cc:1631) loops `i + 1 < end`, so an escaped `\n` at the very end is never treated as a line break.
- `EXPECT_EQ("alpha\nbeta\ngamma\n", "alpha\nbeta\ndelta\n")` shows `-gamma\n` / `+delta\n`.
- `"a\n"` vs `"a\n\n"` reports line `a` as changed.
- Wide strings also leave the `L"` prefix and closing quote inside the diff lines.
- **Fix:** `i < end`, and strip string prefixes.

## 6. `volatile` pointers print as `1`. Low-medium, misleading output.
- `PointerPrinter` (gtest-printers.h:221–233) streams `volatile T*` directly. Before C++23 that converts to `bool`, so two different pointers both print "Which is: 1".
- The smart-pointer path already avoids this with `VoidifyPointer`.
- **Fix:** voidify volatile pointers.

## 7. `--gtest_list_tests` with XML/JSON output ignores the filter. Low-medium.
- `PrintXmlTestsList` / `PrintJsonTestList` total `total_test_count()` and emit every suite. With `--gtest_filter=A.One` the report says `tests="4"` and includes an empty `<testsuite name="B" tests="0">`.
- Run mode uses `reportable_test_count()` and skips empty suites.

## 8. `IsSubsetOf` failure explanation reports the wrong count. Low.
- gmock-matchers.cc:452–458: "the closest match is 2 of 5 matchers" should be "2 of 3 elements" (copied from the Superset branch).

## Minor
- **`CodePointToUtf8` range check:** it accepts U+110000..U+1FFFFF (it checks against 0x1FFFFF, not 0x10FFFF), producing invalid UTF-8 in failure messages and reports (gtest.cc:2058, 2077).
- **JSON `time` precision:** it's printed with 6 significant digits, so over ~1000s it loses milliseconds, and past ~11 days it becomes `7e+06s`, which isn't a valid Duration (gtest.cc:4667).
- **JSON property keys:** `RecordProperty` keys aren't JSON-escaped, so a key with `"` or `\` produces invalid JSON. Docs say keys must be valid XML names, so this is borderline.
- **`EXPECT_NEAR` hint:** it says the double spacing is "inf" when a value is ±DBL_MAX (gtest.cc:1732).

## Already reported (ruled out)
- Invalid UTF-8 breaks the XML/JSON reports: #2953, #2932.
- No `skipped` count on `<testsuites>`: #3836.
- Global-environment errors missing from the report: #4911.
- Duplicate INSTANTIATE prefix runs tests twice: #3209.
- `GTEST_SKIP` in `Environment::SetUp` reports PASSED: #4653.
- Also #4073, #5089, #5086, #4785 and the rest from the earlier issue triage.
