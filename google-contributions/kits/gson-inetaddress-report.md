# Draft report: gson InetAddress "numeric only" check can be bypassed, so name resolution still happens

(This text works for a private submission at bughunters.google.com, where the product is the "Open Source" google/gson project, or for a public GitHub issue. See the notes at the end.)

## Summary

PR #3075 ("Only deserialize `InetAddress` from numeric IP addresses", merged 2026-07-29) makes Gson reject host names when deserializing `InetAddress`. This avoids expensive host-name resolution unless the system property `gson.allowDnsInetAddress` is set.

The check is a regex pre-filter (`TypeAdapters.INET_ADDRESS`, `TypeAdapters.java` ~line 767):

```java
// A pattern that matches every IP address and no DNS address. It matches plenty of things
// that aren't either of those, which is fine. ...
private final Pattern ipAddressPattern = Pattern.compile(".*:.*|[0-9]+(\\.[0-9]+){3}");
```

The value is then passed to `InetAddress.getByName(s)`. The comment assumes that any string the pattern lets through which is not a valid IP literal is rejected by `getByName` without a lookup. That assumption does not hold. The JDK only parses a string as a literal if it is a valid IPv4 literal, or if its first character is a hex digit, `:` or `[`. Anything else is sent to the configured name service. That covers:

- IPv4-shaped strings with out-of-range parts, e.g. `"300.1.1.1"` and `"999.999.999.999"`.
- Strings containing `:` that don't start with a hex digit, `:` or `[`, e.g. `"zz:1"` or `"x:anything"`.

## Reproduction (gson main @ 854c825, JDK 21)

```java
Gson gson = new Gson();
gson.fromJson("\"evil.example.com\"", InetAddress.class); // rejected as intended (JsonSyntaxException)
gson.fromJson("\"300.1.1.1\"", InetAddress.class);        // resolved via the name service
gson.fromJson("\"zz:1\"", InetAddress.class);             // resolved via the name service
```

To show the lookup happens, run with `-Djdk.net.hosts.file=hosts`, where `hosts` contains:

```
10.9.9.9 300.1.1.1
10.8.8.8 zz:1
```

Output:

```
inet evil.example.com -> JsonSyntaxException: Failed parsing 'evil.example.com' as InetAddress; at path $; to allow DNS addresses, set system property gson.allowDnsInetAddress to "true"
inet 300.1.1.1 => 300.1.1.1/10.9.9.9
inet zz:1 => zz:1/10.8.8.8
```

With the default resolver the calls fail with `UnknownHostException: ...: Name or service not known`, which confirms that a real resolver query was made.

## Impact

JSON from an untrusted source can still make the application run blocking name-resolution queries during deserialization. That is the cost #3075 set out to remove. The consequences are:

- Latency, and the potential for tying up threads (resolver timeouts can be seconds per value, and arrays of `InetAddress` multiply the effect).
- Queries sent to the network. With search domains configured, the attacker-chosen string is resolved as `<string>.<search-domain>`.

The attacker cannot choose an arbitrary host name, so this is a partial bypass of a hardening measure, not full SSRF.

## Suggested fix

Validate that the value is an IP literal without falling back to resolution. Any of these would work:

- On JDK 22+, use `InetAddress.ofLiteral(s)`, which never resolves.
- Tighten the IPv4 branch to octets 0–255, and for the IPv6 branch require the string to start with a hex digit, `:` or `[`. That makes `getByName` treat it as a literal and throw `UnknownHostException("invalid IPv6 address literal")` without a lookup.
- Or parse IPv4 and IPv6 literals manually and build the address with `InetAddress.getByAddress(byte[])`.

Add tests for `"300.1.1.1"`, `"999.999.999.999"` and `"zz:1"` being rejected with `JsonSyntaxException` when `gson.allowDnsInetAddress` is not set.

## Notes on where to report this

- PR #3075 was not presented as a security fix (no CVE or GHSA). Its stated motivation is avoiding expensive host-name resolution.
- The check is on `main`. I could not confirm whether it has shipped in a release yet.
- If it has not been released, a public issue plus a fix PR is probably appropriate. If it has been released, or you want to be cautious, submit this privately first via https://bughunters.google.com/report (Google OSS VRP) and wait for their answer before posting publicly.
