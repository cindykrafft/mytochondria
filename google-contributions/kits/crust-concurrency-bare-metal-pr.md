**Title:** Fix notes in the concurrency and bare-metal material

Small corrections to speaker notes and comments. I ran the concurrency samples, and cross-compiled the bare-metal projects with `--locked`, to check that they match the text. None of these touch bare-metal/microcontrollers.md, which #3286 changes.

- **bare-metal/alloc.md:** "The const parameter of `LockedHeap` is the max order of the allocator; i.e. in this case it can allocate regions of up to 2**32 bytes." The buddy_system_allocator version in Cargo.lock (0.13.0) documents: "The max order of the buddy system is `ORDER - 1`. For example, to create a heap with a maximum block size of 2^32 bytes, you should define the heap with `ORDER = 33`." So `LockedHeap::<32>` gives up to 2**31 bytes. I reworded the note rather than changing the code.
- **bare-metal/microcontrollers/other-projects.md:** "NVIC (Nested Virtual Interrupt Controller)". Arm's Cortex-M documentation calls it the [Nested Vectored Interrupt Controller](https://developer.arm.com/documentation/dui0553/latest/Cortex-M4-Peripherals/Nested-Vectored-Interrupt-Controller).
- **concurrency/shared-state/example.md:** the notes say "Blocks are introduced to narrow the scope of the `LockGuard` as much as possible." The solution on the page has no block (it looks like #2737 changed it), and the std type is `MutexGuard`. I reworded it to say the guard is held until the end of the closure, and that a block could release it earlier.
- **concurrency/async/state-machine.md:** the notes describe "`main` contains a naïve executor, which just busy-loops until the future is ready" and say "every future is ready immediately". The page's code blocks have no `main`, executor or `roll_d10` definition, so I removed those two sentences.
- **concurrency/shared-state/arc.md:** the comment says "Sleep for 0-500ms", but `500 - i * 100` with `i` in `0..5` gives 100–500ms.
- Typos: `BtreeMap` → `BTreeMap` (bare-metal/no_std.md), "indrection" and "an a new state" (state-machine.md), "happed" → "happened" (aarch64-rt/exceptions.md).

`mdbook test` and `dprint check` pass.
