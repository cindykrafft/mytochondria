Thanks for taking a look, and you're right about the comment: it doesn't say "without a lookup". That was my wording, and it overstated things. I agree that `300.1.1.1` and `zz:1` aren't valid host names, so resolving them will fail.

What I had in mind is that `getByName` still hands these strings to the system resolver before failing. With a normal resolver configuration that means a DNS query (or several, with search domains) per value, which I understood was what #3075 set out to avoid. The `hosts` file was just a way to show that the lookup happens.

Thanks for the offer. I've sent #PR_NUMBER, which keeps the change small. IPv4 parts are limited to 0–255, with leading zeros still accepted because `getByName` accepts them. A candidate with a colon must start with a hex digit, `:` or `[`. Those are exactly the strings `getByName` parses as literals, rejecting the invalid ones without a lookup. It's a change to the pattern plus tests.
