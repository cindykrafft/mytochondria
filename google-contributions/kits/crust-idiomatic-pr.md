**Title:** idiomatic: fix a few incorrect statements and signatures

Small corrections in the Idiomatic Rust material. I checked each one with rustc 1.94.1 (edition 2024) or against the std source or the Reference.

- **dyn-compatible.md:** the comment on `fn takes_self_and_param<T>(&self, input: &T);` says "dyn compatible, but you can't use this method when it's dyn". Without a bound, using the trait as `&dyn Trait` fails with `error[E0038]: the trait ... is not dyn compatible`. I added `where Self: Sized`, which makes the comment true: the trait is usable as `dyn`, and calling this method on a `dyn` gives "the `takes_self_and_param` method cannot be invoked on a trait object". The notes said "no associated constants/types"; the [Reference](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility) says "It must not have any associated constants" and "It must not have any associated types with generics", and `&dyn Assoc<Item = u8>` compiles, so I changed that to "generic associated types".
- **any-trait.md:** "This is an auto trait: like Send/Sync/Sized". In core, `Any` is declared as `pub trait Any: 'static` and implemented by `impl<T: 'static + ?Sized> Any for T`, so I reworded it to say it comes from a blanket implementation.
- **naming-conventions/exercise.md:** the answer for `slice::get_unchecked_mut` was `(&self /* &[T] */, usize) -> &T`. The real signature is `get_unchecked_mut<I>(&mut self, index: I) -> &mut I::Output`, so the answer is now `(&mut self /* &mut [T] */, usize) -> &mut T`.
- **naming-conventions/try.md:** `impl TryFrom<i32> for u32` returned `Result<i64, TryFromIntError>`. It is now `Result<u32, TryFromIntError>`.
- **debug.md:** `{#?}` → `{:#?}` (`{#?}` is rejected as "invalid format string").
- **default-impls.md:** "`Ord`'s `compare`" → "`Ord`'s `cmp`".
- **extending-foreign-types.md:** the notes say `use ext::StringExt as _`, but the code uses `StrExt`.
- **borrow-checker-invariants.md:** the notes mention `lock_door`, but the function is `close_door`.

`mdbook test` and `dprint check` pass.
