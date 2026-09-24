**Title:** Tighten the `InetAddress` check to IP literals

### Purpose

Fixes #3128

### Description

Following the discussion in #3128, this tightens the pattern that decides whether a string is passed to `InetAddress.getByName`:

- **IPv4:** each of the four parts must be 0–255. Leading zeros are still accepted. In my testing on JDK 21 and 26, `getByName("01.2.3.4")` returns `1.2.3.4`, so rejecting them would change behavior for existing inputs.
- **IPv6:** a string containing a colon must now also start with a hex digit, `:` or `[`. In JDK 21's `InetAddress.getAllByName` (`InetAddress.java` lines 1623–1688), only strings starting with one of those characters go through the literal-parsing code. There a string with a colon is either parsed or rejected with "invalid IPv6 address literal". Every other string reaches `getAllByName0`, the name lookup.

With this change `256.1.1.1`, `300.1.1.1` and `zz:1` get the same "Failed parsing ... as InetAddress" `JsonSyntaxException` as `localhost`. The existing comment above the pattern is updated to match.

Tests added to `DefaultInetAddressTypeAdapterTest`:

- `testInetAddressDeserializeIpLikeNonIpAddress`: `256.1.1.1`, `300.1.1.1`, `1.2.3.999`, `zz:1` and `g::1` are rejected. This test fails without the change.
- `testInetAddressDeserializeIpAddressForms`: `0.0.0.0`, `255.255.255.255`, `01.2.3.4`, `::1`, `[::1]`, `::ffff:1.2.3.4` and `fe80::1%1` are still accepted, and give the same result as `InetAddress.getByName`.

The expected values in the second test come from `InetAddress.getByName` itself. I ran the tests on JDK 21.

### Checklist

- [x] New code follows the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) (`mvn spotless:check` passes)
- [ ] ~~New public API validates arguments / has Javadoc~~ (no new API)
- [x] New unit tests have been added
  - [x] Assertions use Truth
  - [x] The new test fails without the fix and passes with it
- [x] `mvn clean verify` passes for the `gson` module (4675 tests)
