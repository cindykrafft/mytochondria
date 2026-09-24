**Title:** JobSystem job pool holds MAX_JOB_COUNT - 1 jobs on Linux (test fails)

**Describe the bug**
`JobSystem.JobPoolExhaustionNullJobRun` in `libs/utils/test/test_JobSystem.cpp` fails on my Linux desktop build. `createJob()` starts returning `nullptr` after 16383 jobs, not `JobSystem::MAX_JOB_COUNT` (16384).

As far as I can tell, this happens because:
1. The pool is sized to `MAX_JOB_COUNT * sizeof(Job)` bytes, with no room for alignment.
2. That memory comes from `HeapArea`, which calls plain `malloc()`.
3. `Job` is `alignas(CACHELINE_SIZE)` (64 bytes here). When the `malloc()` result isn't 64-byte aligned, `AtomicFreeList` aligns the start up to 64, and the last slot no longer fits.

In my run, a separate `malloc(1048576)` returned an address with `% 64 == 16`. I haven't printed the pool's own base address, so that part is an inference.

**To Reproduce**
With the existing unit test, from a desktop debug build at a5e4a836 (`./build.sh -p desktop debug`, clang 18, libc++):
```sh
out/cmake-debug/libs/utils/test_utils --gtest_filter=JobSystem.JobPoolExhaustionNullJobRun
```
Or with this standalone program, `jobpool_repro.cpp`:
```cpp
#include <utils/JobSystem.h>
#include <cstdint>
#include <cstdio>
#include <cstdlib>

using namespace utils;

int main() {
    size_t const poolBytes = JobSystem::MAX_JOB_COUNT * sizeof(JobSystem::Job);
    void* p = malloc(poolBytes);
    printf("sizeof(Job)=%zu alignof(Job)=%zu, malloc(%zu) %% 64 = %zu\n",
            sizeof(JobSystem::Job), alignof(JobSystem::Job), poolBytes,
            size_t(uintptr_t(p) % 64));
    free(p);

    JobSystem js(JobSystem::SINGLE_THREADED);
    js.adopt();
    size_t n = 0;
    while (js.createJob(nullptr, [](JobSystem&, JobSystem::Job*) {})) {
        n++;
    }
    printf("jobs created before createJob() returned nullptr: %zu (MAX_JOB_COUNT = %zu)\n",
            n, JobSystem::MAX_JOB_COUNT);
    fflush(stdout);
    _Exit(0);  // the held jobs are never run; skip JobSystem teardown
}
```
```sh
F=/path/to/filament
B=$F/out/cmake-debug
clang++ -std=c++17 -stdlib=libc++ -g -I$F/libs/utils/include -I$F/libs/math/include \
  jobpool_repro.cpp -o jobpool_repro $B/libs/utils/libutils.a -lpthread -ldl
./jobpool_repro
```

**Expected behavior**
`MAX_JOB_COUNT` jobs can be created before `createJob()` returns `nullptr`, as the test expects.

**Screenshots**
N/A

**Logs**
```
Note: Google Test filter = JobSystem.JobPoolExhaustionNullJobRun
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from JobSystem
[ RUN      ] JobSystem.JobPoolExhaustionNullJobRun
/home/user/google/filament/libs/utils/test/test_JobSystem.cpp:1331: Failure
Expected equality of these values:
  heldJobs.size()
    Which is: 16383
  JobSystem::MAX_JOB_COUNT
    Which is: 16384

[  FAILED  ] JobSystem.JobPoolExhaustionNullJobRun (3 ms)
[----------] 1 test from JobSystem (3 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (3 ms total)
[  PASSED  ] 0 tests.
[  FAILED  ] 1 test, listed below:
[  FAILED  ] JobSystem.JobPoolExhaustionNullJobRun

 1 FAILED TEST
```
```
sizeof(Job)=64 alignof(Job)=64, malloc(1048576) % 64 = 16
jobs created before createJob() returned nullptr: 16383 (MAX_JOB_COUNT = 16384)
```

**Desktop (please complete the following information):**
 - OS: Ubuntu 24.04 (Linux x86_64), glibc 2.39
 - GPU: none (CPU-only; no rendering involved)
 - Backend: N/A

**Smartphone (please complete the following information):**
 - Device: N/A
 - OS: N/A

**Additional context**
Pool size, [JobSystem.cpp#L186](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/utils/src/JobSystem.cpp#L186):
```cpp
    : mJobPool("JobSystem Job pool", MAX_JOB_COUNT * sizeof(Job)),
```
`HeapArea`, [Allocator.h#L695-L700](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/utils/include/utils/Allocator.h#L695-L700):
```cpp
    explicit HeapArea(size_t const size) {
        if (size) {
            // TODO: policy committing memory
            mBegin = malloc(size);
            mEnd = pointermath::add(mBegin, size);
        }
    }
```
`AtomicFreeList` aligns the start before counting slots, [Allocator.cpp#L131-L132](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/utils/src/Allocator.cpp#L131-L132):
```cpp
    void* const p = pointermath::align(begin, alignment, extra);
    void* const n = pointermath::align(pointermath::add(p, elementSize), alignment, extra);
```
`Job` is declared `class alignas(CACHELINE_SIZE) Job` ([JobSystem.h#L78](https://github.com/google/filament/blob/a5e4a836aa0cfd25bc65ad2a6d64a212236cb271/libs/utils/include/utils/JobSystem.h#L78)).

I've only run this on Linux/glibc. On a platform where `malloc` returns 64-byte-aligned memory for this size, I'd expect the test to pass, but I haven't verified that.

Two possible fixes:
- Add `CACHELINE_SIZE` bytes of slack to the pool size at JobSystem.cpp#L186. That is the smallest change.
- Have `HeapArea` (or this arena) use an aligned allocation, which would also cover other `ObjectPoolAllocator`s of over-aligned types. That is broader, so I'm not sure you'd want it.

I'd be happy to send a PR if this is something you'd like fixed.
