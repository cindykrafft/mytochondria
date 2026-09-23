# gson bug hunt: unreported bugs (2026-09-23)

Tested against google/gson HEAD `854c825` (plus a Javadoc-only commit), built as 2.14.1-SNAPSHOT.
Every finding below was reproduced by running code. Each was searched for in gson's issues and PRs (open and closed) and no existing report was found.
Repro sources: `scratchpad/hunt-{stream,adapters,reflect,tree}/`.

## 1. The InetAddress "no DNS" guard can be bypassed. Security-adjacent: report it privately.
- Since #3075, `InetAddress` deserialization accepts only IP literals unless `gson.allowDnsInetAddress=true`.
- The guard is the regex `.*:.*|[0-9]+(\.[0-9]+){3}` (TypeAdapters.java ~767). The code comment assumes that anything it lets through which is not a valid IP fails without a lookup. It does not.
- `"300.1.1.1"`, `"999.999.999.999"` and `"zz:1"` all pass the regex, and `InetAddress.getByName` then sends them to the system resolver.
- Proof:
  - With a custom hosts file, `"300.1.1.1"` resolves to `300.1.1.1/10.9.9.9`.
  - Without one, it fails with `UnknownHostException: Name or service not known`, which means a real lookup was attempted.
- **Impact:** untrusted JSON can still trigger blocking DNS lookups (latency or DoS), which is exactly what #3075 set out to prevent.
- **Fix:** validate strictly without resolving: IPv4 octets 0–255, a proper IPv6 literal check, or `InetAddress.ofLiteral` on JDK 22+.

## 2. `skipValue()` skips STRICT-mode string checks (JsonReader)
- `skipQuotedValue` (JsonReader.java ~1343–1366) does not have two checks that `nextQuotedValue` has:
  - the rejection of unescaped control characters (~1222);
  - unpaired-surrogate validation (`validateString`, ~1265, added in #3116).
- `strict.fromJson("{\"a\":1,\"junk\":\"x\u0001y\"}", Pojo.class)` succeeds. The same document parsed into `JsonObject` throws `MalformedJsonException`.
- **Fix:** when strict, validate while skipping (or delegate to `nextQuotedValue`). Add tests next to the existing strict-mode tests.

## 3. A failed nested `getAdapter` poisons the adapter cache (Gson.getAdapter)
- Suppose a factory calls `gson.getAdapter(Bad.class)`, catches the exception, and the outer request succeeds.
- The unresolved `FutureTypeAdapter` for `Bad` is then copied into `typeTokenCache` (Gson.java ~364–397).
- From then on, every `getAdapter(Bad.class)` throws a misleading "cyclic dependency has been used before dependency has been resolved" `IllegalStateException` instead of the real error.
- **Fix:** remove the `threadCalls` entry when `create` throws.

## 4. `JsonTreeReader.nextInt/nextLong` reject quoted `"1.0"` / `"1e2"`, which `JsonReader` accepts
- `fromJson(String)` gives `count=100`, but `fromJson(JsonElement)` throws `JsonSyntaxException` for the same JSON.
- The same applies to `Map<Long,…>` keys like `"1.0"`.
- **Root cause:** JsonTreeReader.java ~276/300 goes through `JsonPrimitive.getAsInt/Long` (`Integer.parseInt`), which has no exact-double fallback.
- This is the mirror image of #2817, and it is not covered by PRs #3029 or #3094.

## 5. The java.time adapters let raw exceptions escape
- `{"year":2020,"month":13,"day":1}` as LocalDate throws `DateTimeException`.
- An unknown zone ID throws `ZoneRulesException`.
- An out-of-range year throws `ArithmeticException`.
- `{"id":"Europe/Paris"}` read as `ZoneOffset` throws `ClassCastException`.
- `{}` behaves inconsistently: LocalTime returns `00:00`, LocalDate throws `DateTimeException`, and LocalDateTime throws `JsonSyntaxException`.
- **Fix:** wrap these in `JsonSyntaxException` with the path (IntegerFieldsTypeAdapter.read, ZONE_ID).

## 6. `TypeToken.getParameterized` drops the owner type for static nested classes
- `getParameterized(Outer.Box.class, String.class)` is not equal to `new TypeToken<Outer.Box<String>>(){}` (owner `null` vs `Outer`).
- As a result, an adapter registered with the `getParameterized` type is silently ignored for fields declared as `Outer.Box<String>`.
- **Root cause:** TypeToken.java ~443 passes a null owner. A TODO in TypeTokenTest ~163 acknowledges the difference, but no issue has been filed.

## 7. Outer-class type variables are not resolved in inner-class fields
- `class Page<T> { class Entry { T item; } List<Entry> entries; }` deserialized as `Page<Item>` stores a `LinkedHashMap` in `item`, which leads to a `ClassCastException`.
- **Root cause:** `GsonTypes.resolveTypeVariable` only walks supertypes, never `getOwnerType()`.
- Lower priority: the UserGuide already discourages non-static inner classes.

## Minor
- **Locale round-trip loses data:**
  - `_US` comes back as language `us`;
  - scripts are lost (`sr_RS_#Latn`);
  - `en__POSIX` shifts the variant into the country field.
  - Cause: `StringTokenizer` drops empty fields. Changing this has compatibility implications.
- **`EnumSet<? extends E>` / `EnumMap<? extends K, V>` fields throw** "Invalid EnumSet type" (ConstructorConstructor ~186/204).
- **Raw `NumberFormatException` escapes** from `LongSerializationPolicy.STRING` (LONG_AS_STRING) and from the BitSet adapter on non-numeric strings.
