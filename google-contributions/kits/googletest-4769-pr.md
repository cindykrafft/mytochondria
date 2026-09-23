**Title:** Update docs: assertions are thread-safe on desktop Windows

Fixes #4769

The primer's "Known Limitations" section says it is unsafe to use assertions from two threads concurrently on systems without pthreads "(e.g. Windows)". `docs/advanced.md` has two similar notes ("Assertions from multiple threads are currently not supported on Windows."), one after the `{ASSERT|EXPECT}_NO_FATAL_FAILURE` example and one after the `EXPECT_{NON}FATAL_FAILURE_ON_ALL_THREADS` macros.

These statements are outdated:

- `gtest-port.h` defines `GTEST_IS_THREADSAFE` for desktop Windows. The condition includes `defined(GTEST_OS_WINDOWS) && !defined(GTEST_OS_WINDOWS_PHONE) && !defined(GTEST_OS_WINDOWS_RT)`.
- `gtest-port.cc` provides Windows implementations of `Mutex`, `ThreadLocal` and `ThreadWithParam`.
- The tests that exercise assertions from multiple threads are guarded by `GTEST_IS_THREADSAFE`, so they are also built on desktop Windows. Examples are `ExpectFailureWithThreadsTest` and the concurrent `SCOPED_TRACE` test in `googletest-output-test_.cc`, and the threading tests in `gtest_stress_test.cc` and `googletest-port-test.cc`.

This PR changes documentation only:

- The primer now says the implementation is thread-safe where pthreads is available and on desktop Windows, and unsafe on other systems.
- The two Windows-specific notes are removed from `advanced.md`.
