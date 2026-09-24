**Title:** unsafe-deep-dive: fix samples and notes that don't match

Small fixes in the Unsafe Deep Dive. I checked each with rustc 1.94.1 (edition 2024). None of them touch the files changed in #3284 or #3244.

- **pinning/what-a-move-is.md:** `pub struct DynamicBuffer { ... };` has a `;` after the struct. Compiled on its own (as the playground does), this fails with "expected item, found `;`". `mdbook test` doesn't catch it, I think because rustdoc falls back to wrapping the whole block in its own `fn main`. Without the `;` the sample runs and prints `DynamicBuffer { data: [82, 85, 83, 84], position: 0 }`. The text also refers to `move_and_expect()`; the function is `move_and_inspect()`.
- **ffi/abs.md:** the notes say "Attempt to compile to trigger 'error: extern blocks must be unsafe' error message" and then "Add the unsafe keyword to the block", but the blocks before that step already had `unsafe extern "C"`, so they were identical to the one after it. I removed `unsafe` from the first two blocks and marked them `compile_fail`. In edition 2024 they fail with exactly `error: extern blocks must be unsafe`.
- **ffi/language-differences/representations.md:** the speaker-note code passes `cc_repr.1` (a `u32`) to `std::slice::from_raw_parts`, which gives `E0308: expected usize, found u32`. With `as usize`, the three conversions print "Hello, C", "Hello, C++" and "Hello, Rust".
- **safety-preconditions/common-preconditions.md:** "Casting a `usize` to a raw pointer is no longer allowed." Such casts still compile. The std docs for [`with_exposed_provenance`](https://doc.rust-lang.org/std/ptr/fn.with_exposed_provenance.html) say it "is fully equivalent to `addr as *const T`", so I reworded the note along those lines. Happy to phrase it differently if you had a specific point in mind.
- **pinning/self-referential-buffer.md:** this is a sub-slide of Pinning, so `{{%segment outline}}` there repeats the outline of the whole Pinning segment. I removed it. This is item 6 of #3021.
- Small fixes: `isize:MAX` → `isize::MAX` in a SAFETY comment; the doc comment in introduction/warm-up/unsafe-fn.md referred to `p`/`val`, but the parameter is `ptr`; unpin-trait.md said "when a trait implements `Unpin`", which should be a type.

`mdbook test` and `dprint check` pass.
