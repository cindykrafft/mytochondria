**Title:** Fix a few statements in the Fundamentals material

Small corrections, each checked with rustc 1.94.1 (edition 2024) or against the linked source. They don't touch the files changed in open PRs (#3243, #3281–#3285).

- **borrowing/interior-mutability/refcell.md:** the notes say printing a borrowed `RefCell` "just shows the message `"{borrowed}"`". With `let c = RefCell::new(5); let _m = c.borrow_mut(); println!("{c:?}");` I get `RefCell { value: <borrowed> }`.
- **modules/encapsulation.md:** `#[doc_hidden]` → `#[doc(hidden)]`. `#[doc_hidden]` gives "cannot find attribute `doc_hidden` in this scope".
- **pattern-matching/destructuring-structs.md:** the notes say "Add a new field to `Movement`", but the struct on the slide is `Move`.
- **lifetimes/exercise.rs:** `parse_varint` read at most 7 bytes, with the comment "More than 7 bytes is invalid". The [protobuf encoding docs](https://protobuf.dev/programming-guides/encoding/) say varints use "between one and ten bytes", and that negative `intN` values use all ten. With the 7-byte limit, a `Person` with `id` = -1 encoded as protobuf does it (`0x10` followed by `ff ff ff ff ff ff ff ff ff 01`) panics with "Too many bytes for varint". I changed the limit to 10. The existing tests pass, and a 10-byte varint for `u64::MAX` now parses. If the 7-byte limit was a deliberate simplification, I can change only the comment instead.
- **unsafe-rust/unsafe-functions/extern-c.md:** "Functions declared in an `extern` block must be marked as `safe` or `unsafe`". The [Reference](https://doc.rust-lang.org/reference/items/external-blocks.html#functions) says "A function declared in an extern block is implicitly unsafe unless the safe function qualifier is present", and an unqualified declaration compiles. I reworded it to "can be marked", and added that unqualified functions are unsafe to call. This may have been a deliberate simplification; please drop it if so.
- **unsafe-rust/unsafe.md:** the Book's Unsafe Rust chapter is now 20.1; the ch19-01 URL redirects to ch20-01.
- Typos: "know as" → "known as" (iterators/helpers.md), "collected in to" → "collected into" (iterators/collect.md), "into a the" → "into the" (pattern-matching/exercise.md).

`cargo test`, `mdbook test` and `dprint check` pass.
