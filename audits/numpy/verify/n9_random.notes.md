# n9_random: numpy.random, deeper pass (notes)

Harness: `n9_random.py`. Output files: `n9_random.out` (numpy 2.4.6), `n9_random.v1.23.5.out`,
`n9_random.v1.24.4.out`, `n9_random.v1.26.4.out`. Wall time: about 60 s on 2.4.6 and 80-90 s on the 1.x
builds, most of it in the choice / shuffle loops and the 10 s subprocess hang checks.

Counts (ok / FAIL): 2.4.6: 920 / 18; 1.26.4: 917 / 21; 1.24.4: 914 / 22; 1.23.5: 914 / 22. No tracebacks.

FAILs by build:

| FAIL | 2.4.6 | 1.26.4 | 1.24.4 | 1.23.5 |
|---|---|---|---|---|
| zipf(1.001) and zipf(1.1), both APIs (4 lines) | yes | yes | yes | yes |
| RandomState.dirichlet((0.001, 0.001)) | yes | yes | yes | yes |
| RandomState.negative_binomial(1, p=0) | yes | yes | yes | yes |
| RandomState.wald(1e9, 2.25) | yes | yes | yes | yes |
| Generator.wald(1e9, 2.25) | - | yes | yes | yes |
| RandomState.geometric(1e-17) and (1e-300) (2 lines) | yes | yes | yes | yes |
| Generator.geometric(1e-300) | - | - | yes | yes |
| RandomState.negative_binomial(1e10, 1e-10) | yes | yes | yes | yes |
| Generator.choice(2-D a, size=()) | - | yes | yes | yes |
| RandomState.zipf(2000) hang | yes | yes | yes | yes |
| Generator.zipf(2000) hang | - | yes | yes | yes |
| Philox.advance documentation | yes | yes | yes | yes |
| MT19937.jumped (4 lines) | yes | yes | yes | yes |
| set_state / state pos out of range (2 lines) | yes | yes | yes | yes |

Truths: mpmath at 30 digits (gamma, gammainc, betainc, zeta and Hurwitz zeta, lerchphi, besseli, quad),
closed-form moments, fractions-free exact pmf sums in mpmath, pure-Python reference implementations of
SeedSequence, PCG64 (XSL-RR), PCG64DXSM, MT19937 (and CPython's own MT19937 through `random.Random`),
Philox4x64-10 and SFC64, the C++ seed_seq reference vectors, the CSV vectors shipped in
`numpy/random/tests/data`, and GF(2) polynomial arithmetic for the MT19937 jump. No scipy.

Statistical design. Every distribution is drawn 400,000 times per setting with a fixed seed. The mean
is compared with the exact mean using the exact variance, z = (xbar - mu) / sqrt(var / n). The variance
is compared using the exact fourth central moment, SE = sqrt((mu4 - var^2) / n). That test runs only
where the 8th moment is finite; for lognormal sigma = 1 it is skipped because the kurtosis of x^2 is
about e^16. Continuous CDFs are checked by evaluating the exact CDF at the sample 10/50/90% quantiles:
F(X_(nq)) is a uniform order statistic with mean q and SD sqrt(q(1-q)/n). Discrete CDFs are checked at
exact CDF points. When fewer than about 50 events are expected, the check uses an exact Poisson tail
p-value instead. A FAIL needs |z| > 5, or an exact two-sided p below 5.7e-7.

## FAIL lines

### 1. zipf with a near 1 (a = 1.001 and a = 1.1): Generator and RandomState, all four builds

**Measured.** The test compares the empirical CDF at k = 1, 2, 3, 10, 100, 10^4, 10^6 and 10^15 with
the exact law. That law is pmf k^-a / zeta(a) conditioned on k <= 2^63 (the conditioning is explained
below). All points come out too low: z runs from -2.4 to -88 for a = 1.001 and from -2.3 to -9 for
a = 1.1. At a = 2.5, 4 and 10 the same tests pass.

**Cause.** Zipf draws with a near 1 put too much weight on huge values. The harness prints a
diagnostic: it reruns numpy's rejection step with 4,000,000 proposals and compares the tail mass
P(X > 2^53).

| a     | exact law | numpy Generator | rerun, float64 T | rerun, accurate T |
|-------|-----------|-----------------|------------------|-------------------|
| 1.1   | 0.01214   | 0.0181          | 0.0180           | 0.0122            |
| 1.001 | 0.154     | 0.196           | 0.196            | 0.154             |

The bias comes from the acceptance test in `random_zipf`
(`numpy/random/src/distributions/distributions.c`, lines 1055-1056):

```c
T = pow(1.0 + 1.0 / X, am1);
if (V * X * (T - 1.0) / (b - 1.0) <= T / b)
```

The same code is in `legacy_random_zipf`
(`numpy/random/src/legacy/legacy-distributions.c`, lines 601-602).

For X > 2^53, `1.0 + 1.0 / X` rounds to 1, so T == 1 and the left side is 0: every huge proposal is
accepted. The correct acceptance probability there is about (b-1)/(b(a-1)), roughly 0.7. Below 2^53,
T - 1 loses most of its digits whenever 1/X is near eps. Computing T - 1 as `expm1(am1*log1p(1/X))`
reproduces the exact law. The distribution also stops at 2^63: proposals with X > 2^63 are rejected.
The code comment says so ("models a Zipf distribution truncated to sys.maxint"), but the docstring
does not.

**Documentation.** The docstring gives the pmf k^-a / zeta(a) and says only that a "Must be greater
than 1."

**Verdict.** Bug: floating-point loss in the acceptance ratio, in both the Generator and the legacy
paths, on every build. It matters only when a significant share of the mass lies above about 1e13,
that is for a below about 1.2. The truncation at 2^63 is a documentation gap.

### 2. RandomState.dirichlet((0.001, 0.001)): NaN and inf rows, all builds

**Measured.** 96,917 of 400,000 rows contain NaN, and 113 rows have entries of inf.

**Cause.** In `mtrand.pyx`, `RandomState.dirichlet` sums the gammas and then applies
`invacc = 1/acc; val_data[i + j] = val_data[i + j] * invacc`. Standard gamma(0.001) underflows to 0 in
about 47% of draws. When every gamma in a row is 0, the row becomes 0 * inf = NaN. When the only
non-zero gamma is subnormal, 1/acc is inf.

**Documentation.** The docstring says samples are on the simplex (`x_i > 0`, sum 1) and raises
ValueError only for alpha <= 0.

**Verdict.** Bug in the frozen legacy path. Generator.dirichlet handles this case with stick-breaking
when alpha.max() < 0.1, and its rows are valid on all four builds.

### 3. RandomState.negative_binomial(1, p=0) returns -9223372036854775808, all builds

**Measured.** Every draw is -9223372036854775808.

**Cause.** `legacy_negative_binomial` computes `legacy_gamma(n, (1 - p) / p)`. With p = 0 the scale is
inf, so the gamma draw is inf, and `(int64_t)random_poisson(inf)` gives INT64_MIN. `mtrand.pyx` checks
`p` with `CONS_BOUNDED_0_1`, which lets p = 0 through.

**Documentation.** The legacy docstring says "`p` is in the interval [0, 1]", so p = 0 is documented
as valid. Generator documents 0 < p <= 1 and raises.

**Verdict.** Bug in the legacy API: for the documented value p = 0 it returns a negative count.

### 4. wald(mean=1e9, scale=2.25): negative and zero samples

**Where.** RandomState on all builds. Generator on 1.23.5, 1.24.4 and 1.26.4.

**Measured.** In 100,000 draws, about 190 samples are negative (minimum -212 for RandomState, -424 for
Generator on 1.x) and about 53,000 are exactly 0. The inverse Gaussian has support (0, inf).

**Cause.** `legacy_wald` (`legacy-distributions.c`, lines 149-163) uses
`X = mean + mu_2l * (Y - sqrt(4 * scale * Y + Y * Y))`. When Y is much larger than scale, this
subtracts two nearly equal numbers.

**Fix history.** The Generator fix is in the 2.3.4 release notes ("gh-29926: BUG: fix negative samples
generated by Wald distribution (#29609)"). It computes `X = mean * (1 - 2 / d)` with
`d = 1 + sqrt(1 + 4 * scale / Y)`.

**Verdict.** Bug. It is fixed for Generator in 2.3.4, so it FAILs only on the 1.x Generator builds. It
remains in the frozen legacy path. This is also the Generator stream change listed under "held up".

### 5. geometric with tiny p: negative counts

**Where.**
- RandomState.geometric(1e-17) and geometric(1e-300): all builds, all 20,000 draws are INT64_MIN.
- Generator.geometric(1e-300): 1.23.5 and 1.24.4 only.

**Cause.** `legacy_geometric_inversion` computes
`(long)ceil(npy_log1p(-next_double(bitgen_state)) / log(1 - p))`. For p below about 1.1e-16, `1 - p`
rounds to 1, so `log(1 - p)` is 0. The quotient is -inf, and casting it to long gives INT64_MIN.
Generator uses `npy_log1p(-p)` and, since 1.25.0 ("gh-23691 BUG: random: Don't return negative values
from Generator.geometric"), returns INT64_MAX when the result would not fit (`z >= 9.223372036854776e+18`).
Generator.geometric(1e-17) is fine on every build.

**Documentation.** p is "The probability of success of an individual trial". The support is k >= 1.

**Verdict.** Bug in the legacy path, all builds. In Generator it is fixed in 1.25.

A related check held up: at p = 1e-15, `log(1 - p)` is off by only about 0.08%, and the legacy mean
passes the z-test.

### 6. RandomState.negative_binomial(1e10, 1e-10) returns INT64_MIN, all builds

**Cause.** The mean is 1e20, which is larger than int64 can hold. Casting the huge Poisson draw to int64
overflows.

**Documentation.** Generator documents this limit: the constraint
n(1-p)/p + 10 n sqrt(n)(1-p)/p < 2^63 - 1 - 10 sqrt(2^63 - 1), with a ValueError. The Generator check
passes. The legacy docstring states no limit and no error.

**Verdict.** Bug in the legacy API: it returns an invalid value silently where Generator raises.

### 7. zipf(a=2000) never returns

**Where.** RandomState on all builds. Generator on the 1.x builds.

**Measured.** Run in a subprocess with a 10 s limit; the check reports "no result within 10 s".
RandomState.zipf(1024) returns normally.

**Cause.** In `legacy_random_zipf`, `b = pow(2.0, am1)` overflows to inf once a >= 1025, and so does T.
`V*X*(T-1)/(b-1)` is then inf/inf = NaN, the comparison is always false, and the loop never ends.
Generator short-circuits `if (a >= 1025) return 1`, added in the 2.1.0 changelog ("gh-27046 BUG:
random: prevent zipf from hanging when parameter is large").

**Documentation.** The only constraint is "Must be greater than 1."

**Verdict.** Bug. It is fixed for Generator in 2.1.0 and still present in RandomState.

### 8. Generator.choice(2-D a, size=()) raises ValueError on 1.23.5, 1.24.4 and 1.26.4

**Measured.** The error is "setting an array element with a sequence".

**Documentation.** "the output ndim will be a.ndim - 1 + len(size)", so the result should be one row of
shape (2,).

**Verdict.** Bug, fixed in 2.0.0 (changelog "gh-26544 BUG: Fix handling of size=() in Generator.choice
when a.ndim > 1"). It passes on 2.4.6.

### 9. Philox.advance(delta) advances delta counter blocks, not delta draws, all builds

**Measured.**
- After `Philox(5).advance(1)`, `random_raw(4)` equals raw draws 4..7 of the fresh stream, not draws
  1..4. The pure-Python Philox4x64-10 at counter + 1 gives the same values.
- `jumped()` equals counter + 2^128, which is 2^130 raw 64-bit draws.

**Cause.** In `numpy/random/src/philox/philox.c`, `philox_advance` adds `step` to the 256-bit counter,
and each counter value yields four 64-bit outputs.

**Documentation.** The two docstrings disagree:
- The method docstring says "Advance the underlying RNG as-if delta draws have occurred" and "as-if a
  given number of calls to the underlying RNG have been made".
- The class docstring says "advance can be used to advance the counter for any positive step".
- `jumped` claims "as-if (2**128) * jumps random numbers have been generated".

**Verdict.** Documentation inaccuracy. The method is self-consistent in counter units. The harness
keeps the FAIL because it quotes the method's own docstring.

### 10. MT19937.jumped() does not produce the stream 2^128 ahead, all builds

**Measured.**
1. Berlekamp-Massey on the LSBs of 39,924 MT19937 outputs gives the degree-19937 characteristic
   polynomial P. The harness computes x^(2^128) mod P by 128 squarings over GF(2). Output
   2^128 + t is then the XOR of outputs t + i over the monomials x^i of that residue.
2. The method is checked two ways: x^(2^16) mod P reproduces outputs 2^16 + t exactly, and a scratch
   run confirmed the same for 2^10, 2^15 and 2^17.
3. numpy's `jumped()` agrees with these predictions in 0 of 2,496 outputs in two cases: an MT19937
   seeded by SeedSequence (pos 623, the normal case) and a generator that has drawn 700 values (pos 75).
   `jumped(2)` also agrees in 0 of 2,496.
4. For a legacy-seeded generator at a block boundary (pos 624), 518, 446, 410 and 373 of the successive
   624-output blocks agree, and the agreement decays.
5. In a scratch run from that pos 624 state, the first 35 outputs of the jumped generator matched
   outputs 2^128 - 624 + t.
6. `jumped().jumped() == jumped(2)` holds.

**Cause.** `mt19937_jump_state` (`numpy/random/src/mt19937/mt19937-jump.c`) runs Matsumoto's Horner
jump. That code treats `key`/`pos` as a circular buffer of the last 624 words: `gen_next` overwrites
`key[pos]` and increments pos. Before jumping it only resets `pos >= 624` to 0. numpy's generator reads
the same struct differently. `mt19937_next` returns `key[pos]` directly and, at pos 624, regenerates all
624 words assuming `key[0]` is the oldest. After a jump that leaves pos at 588/589, the state therefore
does not describe the sequence position 2^128 ahead. The generator first returns stale words, then
regenerates a rotated buffer.

numpy's own test (`test_generator_mt19937.py::test_jumped`) compares only the sha256 of the jumped key
and pos with values "produced using the original C implementation". It never compares outputs.

**Documentation.** "The state of the returned bit generator is jumped as-if 2**(128 * jumps) random
numbers have been generated", and the class docstring recommends chained `jumped()` for parallel
streams.

**Verdict.** Bug: the jumped generator is not the documented stream. Separation is still overwhelmingly
likely in practice, because the jumped state is a far-off point of the same period, but the documented
2^128 spacing does not hold. Present in all four builds.

### 11. Out-of-range `pos` in the MT19937 state is accepted, then segfaults, all builds

**Measured.** Two cases, each run in a subprocess:
- `RandomState.set_state(('MT19937', key, 10**7))` is accepted, then `random_sample()` dies with
  SIGSEGV (return code -11).
- `MT19937.state = {..., 'pos': 700}` then `random_raw(10**6)` also ends in SIGSEGV.

**Cause.** The MT19937 state setter (`_mt19937.pyx`) stores `self.rng_state.pos = value['state']['pos']`
without a range check. `mt19937_next` reads `key[pos++]` and regenerates only when pos == 624, so any
pos > 624 walks off the 624-word array. The 1.26.3 / 2.0.0 fix "gh-25466 BUG: avoid seg fault from OOB
access in RandomState.set_state()" added `cython.boundscheck(True)` around the tuple indexing. It does
not validate pos.

**Documentation.** The docstring says only "an integer pos".

**Verdict.** Bug (memory-unsafe input validation). The input is invalid, but a state setter should not
turn it into an out-of-bounds read.

## Observations that are not FAIL lines

- `MT19937(seed)` with a SeedSequence leaves pos = 623, the Cython loop variable after `range(1, 624)`
  (`_mt19937.pyx` line 137: `self.rng_state.pos = i`). The first output is therefore the tempered
  SeedSequence word `key[623]`, not an MT19937 recurrence output. The CSV reference vectors were
  generated with this behavior, so numpy agrees with them. Harmless for randomness.
- `RandomState(np.array([7]))` uses init_genrand(7), because `.squeeze()` turns a 1-element array into
  an index. `RandomState([7])` uses init_by_array([7]). The docstring treats "an array (or other
  sequence) of such integers" as one case. Long-standing legacy behavior.
- `Generator.standard_exponential(method='bogus')` is accepted without error and behaves like 'inv'. The
  docstring says "Either 'inv' or 'zig'".
- `weibull(a=0)` returns 0 on both APIs ("Must be nonnegative"). This is a convention, not a limit of
  the distribution.
- `RandomState.uniform(3, 2)` returns values in (2, 3], which the docstring allows ("officially
  undefined").

## What held up (all four builds unless noted)

- **Distributions.** Every distribution method of Generator and RandomState passes support /
  integrality checks, exact-moment z-tests and exact-CDF tests at 2-5 settings. Covered: beta, binomial,
  chisquare, dirichlet, exponential, f, gamma, geometric, gumbel, hypergeometric, laplace, logistic,
  lognormal, logseries, multinomial, multivariate_hypergeometric (both methods), multivariate_normal
  (svd / cholesky / eigh and legacy), negative_binomial, noncentral_chisquare, noncentral_f, normal,
  pareto, poisson, power, rayleigh, standard_cauchy, standard_exponential (zig / inv, float32),
  standard_gamma (float32), standard_normal (float32), standard_t, triangular, uniform, vonmises, wald,
  weibull, zipf (a >= 2.5), random / rand / randn. The only exceptions are the zipf and dirichlet
  failures above.
- **Edge regimes that passed.**
  - poisson(1e6), poisson(0.01), poisson(9.99) at the PTRS threshold.
  - binomial(1e9, 0.3) (exact CDF by ratio recurrence from an mpmath start value), binomial(10, 1e-6),
    binomial(10, 0.999999), binomial(1e6, 1e-7).
  - geometric(1e-4), geometric(0.999), and 0.35 / 0.4 on the search branch.
  - negative_binomial with n = 0.5 and 1e-3 (non-integer) and p = 0.999.
  - hypergeometric extremes:
    - (1e9-1, 1e9-1, 1000) and (1e9-1, 10, 5), the latter handled by the rare-event exact tail;
    - nsample = total and nsample = total - 10;
    - HRUA (500, 600, 400).
  - logseries(1 - 1e-7), with exact raw moments Li_{1-r}(p)/(-ln(1-p)) and the CDF through the Lerch
    transcendent, plus logseries(1e-6).
  - vonmises kappa 1e-9 (uniform branch), 0.01, 4, 1000 and 1e7 (the Generator wrapped-normal branch;
    the legacy rejection branch is also fine). Wrap-around at mu = 3, -3.1 and 3.14 stays in
    [-pi, pi] with E cos(X - mu) = I1/I0.
  - noncentral_chisquare with df 0.1 and 0.5 (the Poisson-mixture branch) and nonc = 0;
    noncentral_f with dfnum 0.5.
  - weibull(0.5), power(0.3), standard_t with df 1 and 2 (CDF only), lognormal sigma 3 (CDF only).
  - gamma(0.01) and float32 gamma(0.3).
  - uniform at 1e9 and with width 1e-300.
  - triangular with left == mode and mode == right.
  - dirichlet with alpha 0.05, 0.02 and 1e-3 on Generator.
  - multinomial with a zero-probability category and n = 3e9.
- **Docstring pdfs.** The docstring pdfs of beta, gamma, chisquare, gumbel, laplace, logistic, normal,
  pareto (Lomax), power, rayleigh, standard_t, wald and weibull integrate to 1 and reproduce the
  closed-form mean and variance.
- **Boundary values and validation.** All documented boundary values hold and all documented
  ValueErrors are raised. The `dirichlet([0, 1])` expectation follows each build's docstring: 1.x says
  "less than or equal to zero", which raises; 2.x says "less than zero", and the alpha = 0 component
  is 0.
- **Generator.integers and legacy randint.**
  - Full range of every integer dtype and bool, with and without endpoint.
  - Overflow errors, low >= high, float dtype TypeError, high=None, size=None scalar type, size=0.
  - Broadcasting, where every cell covers exactly its range.
  - Chi-square uniformity with exact p-values, including ranges near 2^63 and non-powers of two.
  - randint dtypes and broadcasting; random_integers is inclusive and raises DeprecationWarning;
    tomaxint range.
- **random / out and the raw-to-float mappings.**
  - `random(out=)`, float32 `out`, and the dtype / shape / contiguity errors. The same `out` semantics
    for standard_normal, standard_exponential and standard_gamma.
  - `Generator(PCG64).random() == (raw >> 11) * 2^-53`.
  - float32 `random() == (next_uint32 >> 8) * 2^-24`, low half first.
  - Legacy random_sample equals CPython's `random.random()` (res53) from the same MT state. Legacy
    standard_normal equals the Marsaglia polar method on those doubles, bit for bit.
  - Module-level aliases, and set_bit_generator on 1.24 and later.
- **choice.**
  - The p tolerance is sqrt(eps): 1 + 1e-9 is accepted and 1 + 1e-7 raises.
  - Negative, NaN and 2-D p all raise; zero-p entries are never chosen; "Fewer non-zero entries" raises.
  - Ordered pairs from `replace=False` with p follow successive weighted sampling
    p_i p_j / (1 - p_i) (chi-square, 11 df).
  - Uniform ordered triples.
  - axis handling and output shapes.
  - shuffle=False keeps inclusion probability k/n on both the Floyd and the Fisher-Yates paths.
  - The legacy API rejects 2-D input, as its docstring says.
- **Permutations.** shuffle, permutation and permuted give all 24 permutations with equal
  probability, and their axis semantics match the docs (rows intact, columns whole, independent
  slices for permuted, out=). Views, object arrays and read-only arrays behave as documented.
- **bytes.** Uniform byte values and exact lengths.
- **SeedSequence.**
  - All 10 C++ seed_seq reference vectors match, for 32-bit and 64-bit output.
  - The pure-Python port matches for 8 entropy / spawn_key / pool_size cases.
  - Spawn keys and n_children_spawned behave as documented, and the documented errors are raised.
- **Bit generators.**
  - PCG64, PCG64DXSM, MT19937, Philox and SFC64 match pure-Python references for 2,000 raw draws from
    three seeds and after mixed 32/64-bit consumption. MT19937 also matches CPython.
  - All ten shipped CSV vectors match.
  - The whole seeding chain SeedSequence -> state matches, including PCG64DXSM using the default
    128-bit multiplier for seeding.
  - PCG64 / PCG64DXSM `advance` equals the pure-Python LCG jump-ahead for delta up to 2^128 - 1, and
    `jumped(k)` equals advance(k * 210306068529402873165736369884012333109). That constant is the odd
    integer nearest (phi - 1) 2^128, as documented.
- **State and pickling.** State dict round trips (including a buffered 32-bit half), pickling of every
  bit generator, Generator and RandomState, and legacy get_state / set_state with the cached gaussian.
  The 3-tuple form is accepted.
- **Spawning.** Generator.spawn / BitGenerator.spawn / seed_seq on 1.25 and later, where they are
  absent before as the release notes say. A TypeError is raised for a keyed Philox.
- **Legacy seeding.** init_genrand; init_by_array, including a 700-word key; CPython random.seed
  equivalence; and seed-type errors. The default_rng seed types behave as documented; default_rng of a
  RandomState follows each build's docstring.
- **Docstring examples.** `default_rng(12345).random() == 0.22733602246716966`,
  `integers(0, 10, 3) == [6, 2, 7]`, the seed=42 3x3 array, and the random/index.rst value
  0.5363922081269535. All reproduce on every build.
- **Stream identity.**
  - RandomState: all 61 digests (40-value draws per method and branch) are identical across all four
    builds.
  - Generator: 72 of 75 digests are identical on 1.23.5, 1.24.4 and 1.26.4. The three that differ are
    release-noted:
    - `wald` and `wald_extreme`: new formula in 2.3.4, gh-29926 / gh-29609.
    - `zipf_near_1` (zipf(1.1)): the Umin proposal restriction in 2.1.0, gh-27048.

## What could not be checked, and why

- **Out of range for this machine or budget.** Behavior on platforms where C long is 32-bit (Windows):
  legacy randint / tomaxint / the long casts. Thread-safety and free-threaded builds. ziggurat tables
  bit for bit: normal and exponential are tested statistically, not against a reimplementation.
- **Algorithm-level exactness.** Checked statistically only, not reimplemented:
  - bounded-integer rejection (Lemire / masked);
  - HRUA hypergeometric;
  - BTPE binomial;
  - PTRS poisson.

  With 400,000 draws the tests detect relative distortions of roughly 1e-3 in the bulk, but not rare
  tail defects smaller than about 1e-5 in probability.
- **Stream identity.** The expected digests come from numpy 2.4.6 itself. The checks therefore cover
  cross-build stability, not correctness. Correctness of the raw streams is covered separately by the
  pure-Python references.
- **MT19937 jump range.** The per-block agreement pattern was checked at pos 623, 75 and 624, for
  jumps = 1 and 2 only. The circular-buffer diagnosis rests on reading `mt19937-jump.c`, plus the
  first-35-outputs match seen in a scratch run.
