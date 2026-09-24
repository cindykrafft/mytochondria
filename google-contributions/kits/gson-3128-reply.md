You're right, thanks. The comment doesn't say "without a lookup"; that was my wording and I shouldn't have put it that way. I agree that `300.1.1.1` and `zz:1` are not valid host names.

What I was pointing at is narrower. For those two strings, `InetAddress.getByName` doesn't take the literal-parsing path, because that path only handles strings starting with `[`, a hex digit or `:`. So it ends up in `getAllByName0`, the name lookup, before failing. In JDK 21 that's `InetAddress.java` lines 1623–1688.

Thanks for the offer to take a PR. I've sent #PR_NUMBER. It limits IPv4 parts to 0–255 (still allowing leading zeros, which `getByName` accepts in my testing on JDK 21 and 26). It also requires a string containing a colon to start with a hex digit, `:` or `[`. For strings that match, `getByName` should either parse them or throw without reaching the lookup. It's a change to the pattern plus tests, but happy to adjust or drop it if you'd rather keep things as they are.
