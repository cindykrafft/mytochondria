**Title:** Tighten the `InetAddress` check to IP literals

### Purpose

Fixes #3128

### Description

Following the discussion in #3128, this tightens the pattern that decides whether a string is passed to `InetAddress.getByName`. It does two things.

- **IPv4:** each of the four parts must be 0–255 and at most three digits long. Leading zeros such as `001` are still accepted, because `getByName` parses them (in my testing on JDK 21 and 26, `001.002.003.004` gives `1.2.3.4`). The three-digit limit keeps a match within the 15 characters that JDK 21's `IPAddressUtil.textToNumericFormatV4` parses. A longer string like `00000000001.2.3.4` is rejected by default, but it is looked up when `jdk.net.allowAmbiguousIPAddressLiterals=true`.
- **IPv6:** a string containing a colon must now also start with a hex digit, `:` or `[`. In JDK 21's `InetAddress.getAllByName` (`InetAddress.java` lines 1623–1688), literal parsing is only tried for strings starting with a hex digit or `:`, after stripping `[...]`. Within that branch, a string containing a colon is either parsed or rejected with "invalid IPv6 address literal". A string like `zz:1` never enters it and goes to `getAllByName0`, the name lookup.

With this change `256.1.1.1`, `300.1.1.1`, `0001.2.3.4` and `zz:1` get the same "Failed parsing ... as InetAddress" `JsonSyntaxException` as `localhost`. The comment above the pattern is updated to match.

To check the IPv4 part, I generated 200,000 random strings matching the new IPv4 pattern (random values with random leading zeros) and passed them to `getByName` with an empty `jdk.net.hosts.file`, on JDK 21. All of them parsed as IPv4 literals, with `jdk.net.allowAmbiguousIPAddressLiterals` both unset and set to `true`.

Tests added to `DefaultInetAddressTypeAdapterTest`:

- `testInetAddressDeserializeIpLikeNonIpAddress`: `256.1.1.1`, `300.1.1.1`, `1.2.3.999`, `0001.2.3.4`, `zz:1` and `g::1` are rejected. This test fails without the change.
- `testInetAddressDeserializeIpAddressForms`: `0.0.0.0`, `255.255.255.255`, `01.2.3.4`, `001.002.003.004`, `::1`, `[::1]`, `::ffff:1.2.3.4` and `fe80::1%1` are still accepted, and give the same result as `InetAddress.getByName`.

The expected values in the second test come from `InetAddress.getByName` itself. I ran the tests on JDK 21.

### Checklist

- [x] New code follows the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) (`mvn spotless:check` passes)
- [ ] ~~New public API validates arguments / has Javadoc~~ (no new API)
- [x] New unit tests have been added
  - [x] Assertions use Truth
  - [x] The new test fails without the fix and passes with it
- [x] `mvn clean verify` passes for the `gson` module (4675 tests)
