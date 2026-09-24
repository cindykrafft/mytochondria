**Title:** Tighten the `InetAddress` check to IP literals

### Purpose

Fixes #3128

### Description

As @eamonnmcmanus suggested in #3128, this tightens the pattern that decides whether a string may be passed to `InetAddress.getByName`. It now only lets through strings that `getByName` parses as literals, so it never falls back to a name lookup:

- **IPv4:** each of the four parts must be 0–255. Leading zeros are still accepted, because `getByName` accepts them: `01.2.3.4` parses as `1.2.3.4`.
- **IPv6:** the string must still contain a colon, and must now also start with a hex digit, `:` or `[`. `getByName` only treats a string as an IPv6 literal under that condition. For such strings it either parses the literal or throws `UnknownHostException("... invalid IPv6 address literal")` without a lookup. Any other string containing a colon (for example `zz:1`) is passed to the resolver.

So `256.1.1.1`, `300.1.1.1` and `zz:1` are now rejected with the usual "Failed parsing ... as InetAddress" `JsonSyntaxException`, the same as `localhost`. Every form accepted before that is a real IP literal is still accepted.

I added the part-range limit and the leading-character requirement to the existing comment. The change is two constants in the pattern.

Tests added to `DefaultInetAddressTypeAdapterTest`:

- `testInetAddressDeserializeIpLikeNonIpAddress`: `256.1.1.1`, `300.1.1.1`, `1.2.3.999`, `zz:1` and `g::1` are rejected. This test fails without the change.
- `testInetAddressDeserializeIpAddressForms`: `0.0.0.0`, `255.255.255.255`, `01.2.3.4`, `::1`, `[::1]`, `::ffff:1.2.3.4` and `fe80::1%1` are still accepted, and give the same result as `InetAddress.getByName`.

I checked `getByName`'s behaviour for all of these inputs on JDK 21 and JDK 26.

### Checklist

- [x] New code follows the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html) (`mvn spotless:check` passes)
- [ ] ~~New public API validates arguments / has Javadoc~~ (no new API)
- [x] New unit tests have been added
  - [x] Assertions use Truth
  - [x] The new test fails without the fix and passes with it
- [x] `mvn clean verify` passes for the `gson` module (4675 tests)
