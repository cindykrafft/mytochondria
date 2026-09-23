**Title:** InetAddress numeric-only check lets some non-IP strings through to name resolution

# Gson version
`main` at 854c825 (2.14.1-SNAPSHOT), which includes #3075

# Java / Android version
OpenJDK 21.0.10

# Used tools
- [ ] Maven; version:
- [ ] Gradle; version:
- [ ] ProGuard (attach the configuration file please); version:
- [x] None, plain `javac` / `java`

# Description
#3075 made `InetAddress` deserialization reject host names, unless `gson.allowDnsInetAddress` is set, so that deserialization does not perform host-name resolution. The check is a regex pre-filter, `.*:.*|[0-9]+(\.[0-9]+){3}`, followed by `InetAddress.getByName(s)`. The code comment assumes that any string the regex lets through which is not a valid IP literal is rejected by `getByName` without a lookup.

That does not hold. `InetAddress.getByName` treats the string as a literal only if it is a valid IPv4 literal, or if it starts with a hex digit, `:` or `[`. Everything else goes to the name service. The regex lets through two such kinds of string:

- IPv4-shaped strings with out-of-range parts, such as `"300.1.1.1"` or `"999.999.999.999"`.
- Strings that contain `:` but don't start with a hex digit, `:` or `[`, such as `"zz:1"`.

## Expected behavior
These strings are rejected with `JsonSyntaxException`, without any name lookup, like `"evil.example.com"` is.

## Actual behavior
They are resolved through the system name service. With the default resolver the lookup fails with `UnknownHostException: 300.1.1.1: Name or service not known`, after a real resolver query. With a hosts file that maps them, they resolve successfully:

```
inet evil.example.com -> JsonSyntaxException: Failed parsing 'evil.example.com' as InetAddress; at path $; to allow DNS addresses, set system property gson.allowDnsInetAddress to "true"
inet 300.1.1.1 => 300.1.1.1/10.9.9.9
inet zz:1 => zz:1/10.8.8.8
```

# Reproduction steps
```java
Gson gson = new Gson();
gson.fromJson("\"300.1.1.1\"", InetAddress.class);
gson.fromJson("\"zz:1\"", InetAddress.class);
```

Run with `-Djdk.net.hosts.file=hosts`, where `hosts` contains:

```
10.9.9.9 300.1.1.1
10.8.8.8 zz:1
```

This shows that the name service is consulted.

Possible fixes:
- Tighten the IPv4 branch to octets 0–255, and require the IPv6 branch to start with a hex digit, `:` or `[`. `getByName` then parses these strings as literals, and throws `UnknownHostException("invalid IPv6 address literal")` without a lookup for invalid ones.
- On JDK 22+, use `InetAddress.ofLiteral`.

# Exception stack trace
Not applicable. No exception is thrown when resolution succeeds.
