**Title:** Fix out-of-bounds read in Base64Unescape for non-ASCII input

`WhenBase64Unescaped` (via `internal::Base64Unescape` in `gmock-internal-utils.cc`) iterates over the input string as `int`. Where `char` is signed, bytes 0x80–0xFF become negative values. Two things then go wrong:

- They are passed to `std::isspace`, which is undefined behavior for negative values other than `EOF`.
- They are converted with `static_cast<size_t>` to huge indices into `kUnBase64` (a `std::array<char, 256>`), so the lookup reads memory before the table.

In practice:

- AddressSanitizer reports a `global-buffer-overflow` in `Base64Unescape` for input such as `"h\xC3\xA9llo"`.
- With `_GLIBCXX_ASSERTIONS`, `std::array::operator[]` asserts (`__n < this->size()`).
- In an uninstrumented build, the result depends on the bytes that happen to precede the table. In one build, 64 of the 128 possible non-ASCII bytes, repeated four times, were accepted as valid base64 and "decoded". So a test like `EXPECT_THAT(payload, Not(WhenBase64Unescaped(_)))` can give the wrong answer.

This change iterates as `unsigned char`, which keeps every index in range and makes the `std::isspace` call well-defined. Non-ASCII bytes map to the table's "invalid" entries and are rejected, as intended.

Added `Base64Unescape.NonAsciiCharactersAreInvalid` to `gmock-internal-utils_test.cc`. It checks that every byte 0x80–0xFF is rejected, as is a valid prefix followed by UTF-8 text. It trips the `std::array` bounds assertion without the fix (under `-D_GLIBCXX_ASSERTIONS`) and passes with it. The full test suite passes.
