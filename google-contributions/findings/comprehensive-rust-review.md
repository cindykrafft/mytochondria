# comprehensive-rust: open issues and unreported content errors (2026-09-24)

Reviewed google/comprehensive-rust HEAD `1287785`, using rustc 1.94.1 (edition 2024), Miri (nightly 2026-09-23) and clippy.

**Baseline.** `cargo test --workspace` and `mdbook test` both pass. The tools were installed with `cargo install` at the versions pinned in MODULE.bazel, because `cargo xtask install-tools` needs bazel.

**How each item was checked.**
- Every item was re-checked at HEAD: text by grep, compile claims by rustc, and UB claims by Miri.
- Every item was searched in issues and PRs, open and closed.
- Every item was checked against the heads of all open PRs, including kwy404's #3284–#3286 from today, and none of them changes any of these lines.

**Repros.** `scratchpad/crust-{a,b,c,d}/`.

**Policy.** CLA required. Small content PRs merge in about 4 days. There is no AI policy. Changing English text makes the matching translations fuzzy; that is normal here, and PRs don't edit po files.

## Code that doesn't compile, or doesn't do what the text says

1. **unsafe-deep-dive/pinning/what-a-move-is.md:18.**
   - `pub struct DynamicBuffer { ... };` has a stray `;`, so the sample fails to compile standalone (Play button) with "expected item, found ';'".
   - `mdbook test` passes only because rustdoc wraps the file in its own `fn main` and never runs the sample's `main`.
   - Line 33 says `move_and_expect`, but the function is `move_and_inspect`.
2. **idiomatic/.../dynamic-dispatch/dyn-compatible.md:21.**
   - The comment on `fn takes_self_and_param<T>(&self, input: &T);` says "dyn compatible, but you can't use this method when it's dyn". Using `&dyn` with this trait gives E0038, "not dyn compatible".
   - Lines 46–49 say a dyn-compatible trait has "no associated constants/types". `&dyn Assoc<Item = u8>` compiles; the Reference forbids associated consts and GATs, not plain associated types.
3. **idiomatic/.../naming-conventions/try.md:21.** The sample's `impl TryFrom<i32> for u32` declares `-> Result<i64, TryFromIntError>`. It should be `Result<Self, Self::Error>`.
4. **idiomatic/.../naming-conventions/exercise.md:46.** The answer key gives `get_unchecked_mut(&self, usize) -> &T`. The real signature takes `&mut self` and returns `&mut I::Output`.
5. **idiomatic/.../common-traits/debug.md:71.** `{#?}` is not a valid format spec ("invalid format string"). It should be `{:#?}`.
6. **unsafe-deep-dive/ffi/abs.md:41/63/76/87.**
   - Line 76 says "Attempt to compile to trigger 'error: extern blocks must be unsafe'", but every block already has `unsafe extern "C"`.
   - The "before" and "after" blocks are identical.
   - Plain `extern "C" {}` does give that error in edition 2024.
7. **unsafe-deep-dive/ffi/language-differences/representations.md:14/40.** The speaker-note code passes `u32` to `from_raw_parts` (E0308, expected usize).
8. **unsafe-deep-dive/.../copying-memory/exposed-unsafe.md:35/54.**
   - `main` passes `[114,117,115,116].as_ptr()` with no NUL terminator to a function that loops until `*end != 0`.
   - Miri reports an out-of-bounds read.
   - The notes say "See that the output remains the same".
9. **references/exercise.md:23/31.** `{{#include exercise.rs:magnitude}}` and `:normalize` refer to anchors that exercise.rs doesn't define. They have rendered as blank lines since v2.
10. **running-the-course/course-structure.md:97.**
    - `{{%course outline Unsafe}}` renders as "not found - {{%course outline Unsafe}}" on the live page.
    - The course's name is "Unsafe Deep Dive" (unsafe-deep-dive/welcome.md:2), and mdbook-course matches names exactly.
11. **modules/solution.md.** It has 9 leftover `// ANCHOR:` / `// ANCHOR_END:` lines in plain code blocks, and they show on the live page.
12. **running-the-course.md:62.** It links `github.com/google/comprehensive-rust#building`. The README has no "Building" heading; the setup section is "Setup".

## Statements that are wrong (checked against rustc/std/Reference/crate source)

13. **borrowing/interior-mutability/refcell.md:50.** The notes say printing a borrowed RefCell shows `"{borrowed}"`. On 1.94.1 it prints `RefCell { value: <borrowed> }`.
14. **modules/encapsulation.md:78.** It says `#[doc_hidden]`; the attribute is `#[doc(hidden)]`. `#[doc_hidden]` gives "cannot find attribute".
15. **idiomatic/.../any-trait.md:40.** "This is an auto trait". `Any` is an ordinary trait with a blanket `impl<T: 'static + ?Sized> Any for T` (core any.rs:116/141).
16. **unsafe-deep-dive/safety-preconditions/common-preconditions.md:39.** "Casting a usize to a raw pointer is no longer allowed." `0x1000usize as *const u8` compiles; std::ptr docs describe these casts as having exposed-provenance semantics.
17. **idiomatic/polymorphism/refresher/default-impls.md:41.** "`Ord`'s `compare`". The method is `cmp`.
18. **bare-metal/alloc.md:24.**
    - "The const parameter of `LockedHeap` is the max order ... up to 2**32 bytes."
    - buddy_system_allocator 0.13.0 (the version pinned in Cargo.lock) documents: "The max order of the buddy system is `ORDER - 1`. For example, to create a heap with a maximum block size of 2^32 bytes, you should define the heap with `ORDER = 33`."
19. **bare-metal/microcontrollers/other-projects.md:28.** "NVIC (Nested Virtual Interrupt Controller)". Arm calls it the Nested *Vectored* Interrupt Controller; quote an Arm page before filing.
20. **concurrency/shared-state/example.md** notes. "Blocks are introduced to narrow the scope of the `LockGuard`". The code has no blocks since #2737, and the type is `MutexGuard`.
21. **concurrency/async/state-machine.md** notes. They describe "`main` contains a naïve executor", but the page has no `main`.
22. **pattern-matching/destructuring-structs.md:39.** The notes say `Movement`; the struct is `Move` (renamed in #3077).
23. **lifetimes/exercise.rs:106.**
    - The comment says "More than 7 bytes is invalid."
    - protobuf.dev says varints take "between one and ten bytes", and that negative `intN` values use all ten.
    - Possibly a deliberate simplification, so the fix is to reword the comment only.
24. **unsafe-rust/unsafe-functions/extern-c.md:10.**
    - It says extern-block functions "must be marked as `safe` or `unsafe`".
    - The Reference says they are "implicitly unsafe unless the safe function qualifier is present", and unqualified declarations compile.
    - Could be a teaching simplification; ask rather than assert.
25. **Weaker ones.** Ask before filing:
    - bare-metal/useful-crates/aarch64-paging.md uses the pre-0.12 API (`IdMap::new(ASID, ..)`, `Attributes::NORMAL`); the snippet is compile_fail/illustrative.
    - branded-01-motivation.md calls an out-of-bounds `get_unchecked` "Panics!"; it's UB, and the debug check isn't guaranteed.
    - rust-pin.md `write()` is UB under Stacked Borrows but not Tree Borrows.
    - `Rc::as_ptr` is shown as a method.
    - mutex-guard.md "no other way" ignores `get_mut`/`into_inner`.
    - drop_option.md refers to a ManuallyDrop example that isn't on the previous slide.
    - unsafe.md cites "Chapter 19.1" of the Book; it is now 20.1, and the old URL redirects.

**Typos.**
- thiserror.md "not the same this"
- helpers.md "know as"
- collect.md "in to"
- pattern-matching/exercise.md "into a the"
- no_std.md `BtreeMap`
- state-machine.md "indrection" / "an a new state"
- exceptions.md "happed"
- extending-foreign-types.md `StringExt`→`StrExt`
- borrow-checker-invariants.md `lock_door`→`close_door`
- common-preconditions.md: two truncated sentences
- documented-safety-preconditions.md `isize:MAX`
- arrays.md `MaybeUninit::<u8>` in a type position
- unsafe-fn.md doc names `p`/`val` for `ptr`
- dyn-trait.md `;;`

## Open issues with an uncontroversial fix and no PR

- **#2997.**
  - modules/filesystem.md:21–23 says "a `garden::vegetables` module can be found at `src/garden/vegetables.rs`" without saying it's declared inside `garden.rs`.
  - Suggested rewording: "declaring `mod vegetables;` inside `src/garden.rs` ...".
  - The issue has a comment we couldn't read, so read it first.
- **#3021 item 6.**
  - unsafe-deep-dive/pinning/self-referential-buffer.md has `{{%segment outline}}` on a nested sub-slide, so it prints the whole Pinning outline.
  - Fix: delete it. PR #3284 covers items 2–4 of the same issue but not this one.

## Ruled out

- **Already in open PRs:** #3285 (Collatz note), #3243 (exclusive-reference note), #3166 (method resolution), #3244 (may_overflow), #3284 (#3021 items 2–4), #3242, #3125, #2914, #3000, #3274.
- **#1330** (async dependencies) needs a setup section the maintainers asked for; it is assigned to 0scvr (stale).
- **Already fixed at HEAD:** #2732, #2955.
- **Need a maintainer decision:** #2733, #2714, #3101, #3155.
- **Checked and correct:** all concurrency samples behave as described, both dining-philosophers solutions are deadlock-free, all bare-metal projects cross-compile, and all Fundamentals exercises pass.
