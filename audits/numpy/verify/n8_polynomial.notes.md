# n8_polynomial — notes

Harness: `audits/numpy/verify/n8_polynomial.py`. Outputs: `n8_polynomial.out` (numpy 2.4.6),
`n8_polynomial.v1.23.5.out`, `.v1.24.4.out`, `.v1.26.4.out`. Runtime about 1 s per build.
Truths: mpmath at 50 digits (the five basis recurrences evaluated directly, `polyroots` of the exact
power-form polynomial, closed-form moments of the five weight functions, an mpmath Vandermonde-moment solve
for quadrature weights) and `fractions.Fraction` (exact polynomial algebra in the power basis with an exact
change of basis to each series kind by leading-coefficient elimination, exact weighted normal-equation least
squares, Faddeev-LeVerrier characteristic polynomial). No scipy anywhere (the 1.x builds have none).

## Counts

| build | ok | FAIL |
|---|---|---|
| numpy 2.4.6 | 397 | 8 |
| numpy 1.26.4 | 397 | 8 |
| numpy 1.24.4 | 397 | 8 |
| numpy 1.23.5 | 396 | 8 |

The same eight FAIL lines appear in every build; all are documentation-level findings (none is a numerical
error). The 1.23.5 build has one check fewer because the `symbol=` keyword arrived in 1.24.

## FAIL lines

### 1–5. `chebweight` / `legweight` / `hermweight` / `hermeweight` / `lagweight` reject a plain Python list (all builds)

Measured: each `*weight([x0, x1, ...])` with a Python list raises `TypeError`; an ndarray or a scalar works
and gives the documented weight (checked to 1e-14 against `1/sqrt(1-x^2)`, `1`, `exp(-x^2)`, `exp(-x^2/2)`,
`exp(-x)` in mpmath). Library: none of the five converts its argument. `numpy/polynomial/chebyshev.py`
`chebweight`: `w = 1. / (np.sqrt(1. + x) * np.sqrt(1. - x))` (`1. + list` fails); `legendre.py` `legweight`:
`w = x * 0.0 + 1.0`; `hermite.py` `hermweight`: `w = np.exp(-x**2)`; `hermite_e.py` `hermeweight`:
`w = np.exp(-.5 * x**2)`; `laguerre.py` `lagweight`: `w = np.exp(-x)` (unary minus on a list). Documentation:
every docstring says `x : array_like  Values at which the weight function will be computed`, and array_like
elsewhere in the package means lists are accepted (`chebval`, `chebvander`, `chebfit` all convert). Verdict:
documentation gap / minor API inconsistency (a one-line `x = np.asarray(x)` would make the docstring true).
Not a numerical problem.

### 6. `ABCPolyBase.integ()` with `lbnd` omitted does not equal `integ(lbnd=0)` on a shifted domain (all builds)

Measured: `p = Polynomial([1, 2, 3], domain=[0, 10])`; `p.integ()` evaluates to -5 at x = 0 and to 0 at x = 5,
whereas `p.integ(lbnd=0)` evaluates to 0 at x = 0. So the omitted lower bound is the *window* origin (which is
the domain mid-point x = 5 here), while an explicit lower bound is taken in *domain* coordinates.
Library (`numpy/polynomial/_polybase.py`, `integ`, lines 870–875 of the main source and 823–827 in 1.23.5):
```
off, scl = self.mapparms()
if lbnd is None:
    lbnd = 0
else:
    lbnd = off + scl * lbnd
coef = self._int(self.coef, m, k, lbnd, 1. / scl)
```
The default 0 is passed straight to `_int`, i.e. in the window variable, while a user-supplied `lbnd` is mapped.
Documentation: the class docstring says only `lbnd : Scalar  The lower bound of the definite integral.` with
no default and no statement of the coordinate system; the module functions (`polyint` etc.) document
`lbnd : scalar, optional  The lower bound of the integral. (Default: 0)`. Everything else about `integ` holds up
exactly: with an explicit `lbnd` the result is the antiderivative with respect to x (chain rule `1/scl`
applied, verified against exact Fraction composition), the value at `lbnd` is `k[0]`, the second constant is
the value of the second integral, and `integ().deriv()` round-trips. Verdict: bug or at least a documentation
gap — the two code paths use different coordinate systems, so `integ()` and `integ(lbnd=0)` differ on any
series whose window origin is not the domain origin (the default domain [-1, 1] hides it, which is why it is
rarely noticed; `Polynomial.fit` always produces such a shifted domain). Present identically in all four builds.

### 7. `np.polyder(sequence, m > degree)` returns an empty array, not the zero polynomial (all builds)

Measured: `np.polyder([1, 2, 3, 4], 4)` returns `array([], dtype=int64)`; `np.polyder(np.poly1d([1, 2, 3, 4]), 4)`
returns `poly1d([0])`. Library (`numpy/lib/_polynomial_impl.py`, `polyder`, lines 443–452): the recursion
`y = p[:-1] * NX.arange(n, 0, -1)` produces an empty array once `p` has a single element, and only the
`truepoly` branch wraps it as `poly1d(val)`, whose constructor turns an empty coefficient array into `[0]`.
Documentation: "The fourth-order derivative of a 3rd-order polynomial is zero: `np.polyder(p, 4)` →
`poly1d([0])`" — the example only uses a poly1d input. The empty array still evaluates to 0 through
`np.polyval`, so it is functionally a zero polynomial, but `len`, `np.roots` or printing differ. Verdict:
documentation gap / minor inconsistency between the two input types.

### 8. `np.polyder(sequence)` returns an ndarray although the docstring says `der : poly1d` (all builds)

Measured: `type(np.polyder([1, 2, 3, 4]))` is `ndarray`; a poly1d input returns a poly1d. Library: same
`truepoly` switch as above (`if truepoly: val = poly1d(val)`). Documentation: the Returns section reads
`der : poly1d  A new polynomial representing the derivative.` while the Parameters section accepts
`p : poly1d or sequence`. The sibling `polyint` docstring has no Returns section at all and behaves the same way
(ndarray for a sequence, poly1d for a poly1d; verified). Verdict: documentation gap (the stated return type is
wrong for sequence input); the values are exact in both cases.

## Version-dependent behaviour encoded (informational, all verified against the sources)

* `ABCPolyBase.__call__` with a plain Python *list* argument: 2.x maps through `pu.mapdomain` (which does
  `asanyarray`) and works; 1.23–1.26 compute `off + scl*arg` on the raw argument and raise `TypeError`
  (`can't multiply sequence by non-int of type 'numpy.float64'`). Recorded as informational on 1.x; scalars and
  ndarrays work identically in all builds.
* `Polynomial.fit` with a constant x: 2.x widens the degenerate domain to `[x-1, x+1]` (`_polybase.fit`,
  `if domain[0] == domain[1]`) and returns the mean; 1.x maps through a zero-length domain, produces NaN
  (`RuntimeWarning: divide by zero` in `mapparms`) and `lstsq` raises `LinAlgError: SVD did not converge`.
* Printing: 1.23 documents (and prints) the degree-1 term as `2.0·x¹` / `2.0 x**1`; 1.24+ print `2.0·x` /
  `2.0 x`. `repr` shows `domain=[-1,  1]` (int class arrays) on 1.x and `domain=[-1.,  1.]` on 2.x, and the
  `symbol='x'` field from 1.24. On 2.x `str` of a series with a non-default domain shows the mapped variable
  (2.0 release note); the current `_format_term` prints `'1.0 + 1.0 (-3.0 + 20.0x)'` whereas the 2.0 release
  note's example text reads `'1.0 + 1.0 (-3.0000000000000004 + 20.0 x)'` (scalar rounding and spacing changed
  after 2.0; harmless doc drift, recorded in the detail of the ok line).
* `RankWarning` lives at `np.exceptions.RankWarning` (2.x), `np.RankWarning` (1.x); the harness resolves it.

## Informational measurements (no documented promise, so no expectation)

* Gauss quadrature weights against an mpmath Vandermonde-moment solve at the exact nodes: chebgauss / leggauss
  / hermgauss / hermegauss at n = 5 and 12 agree to 1e-15 – 5e-14 relative; `laggauss(12)` has a relative error
  of 1.3e-10 on its smallest weight (8e-16). All five integrate x^k exactly for k ≤ 2n-1 to 1e-12 relative
  (the doubles summed in mpmath), nodes match mpmath roots of the basis polynomial to 1e-13.
* `chebinterpolate(exp, 10)`: max error 2.7e-11 on [-1, 1], as expected from the size of the T_11 coefficient.
* `np.roots` of the degree-20 Wilkinson polynomial: max absolute root error 8.5e-2 (companion-matrix eigenvalues
  of coefficients up to 20!); `(x-1)^3 (x-3)`: triple root error 9.5e-6 ≈ eps^(1/3), simple root 6e-15.
* `np.polyfit(years 2000–2020, deg=5)`: RankWarning raised in every build, rank 5 of 6 (singular values from
  2.4 down to 8.8e-15 with rcond 4.7e-15); the returned coefficients differ from the exact Fraction least-squares
  coefficients by 97–100 % relative (all six), while the fitted *values* are still within 1e-5 of the data —
  the coefficient vector is simply not determined in double precision. The centred fit `x - 2010` reproduces
  the exact coefficients to 1e-9 (the documented remedy).
* Degree-20 fit of cos(3u), 200 points on the years: `Chebyshev.fit` rank 21, condition 2.9, residual 4e-14;
  `Polynomial.fit` (domain-mapped) rank 21, condition 9e6, residual 4e-14; raw `np.polyfit` rank 6, condition
  7e16–1e17, residual 4.6e-2 with a RankWarning.
* `convert()` round trip through raw-x coefficients of size 1e9 (years fit) loses digits: 4e-10 relative on
  2.x, 7e-9 on 1.x; the well-conditioned round trip on domain [0, 10] is exact to 4e-16 (expectation). Likewise
  evaluating the raw-x Chebyshev series at x ≈ 2000 (T_k(2000) ≈ 1e10) loses to 1e-6 relative — the `convert`
  docstring warns "Conversion between domains and class types can result in numerically ill defined series".
* `np.polyint(p, 2, k=[1])` broadcasts a length-1 list to all constants (source `len(k) == 1 and m > 1`); the
  docstring only documents the scalar shortcut for m = 1.

## What held up (exact or to the stated tolerance, every build)

For each of the six kinds (power, Chebyshev, Legendre, Hermite, HermiteE, Laguerre): `*val` at eight points
including -3, 2.5 and 10 (and a complex point) against the recurrence in mpmath (≤ 1e-12 relative), `tensor`
semantics with 2-D coefficients; `*val2d` / `*val3d` / `*grid2d` / `*grid3d` against exact Fraction double and
triple sums; `*vander` / `*vander2d` / `*vander3d` column values and column ordering, and `V @ c.flat == val`;
`*fit` with an integer degree against exact normal equations, `deg=[0, 2, 3]` ("only those terms": the
degree-1 coefficient is exactly 0), weights (w multiplies the unsquared residual, i.e. w² in the normal
equations), 2-D y, `full=True` (`resid` = exact RSS, rank, singular values, `rcond = len(x)*eps`); `*roots` of a
degree-5 series with complex roots against `mpmath.polyroots` (real dtype when all roots are real);
`*companion` eigenvalues = roots, symmetric for the orthogonal kinds; `*fromroots` exact (complex roots →
complex dtype with zero imaginary parts); `*der(m=2, scl=3)` = scl^m times the exact derivative; `*int(m=2,
k, lbnd, scl)` with the documented "multiply by scl, then add the constant so the value at lbnd is k[i]"
semantics; `*add` / `*sub` / `*mul` / `*mulx` / `*div` (quotient and remainder) / `*pow` (incl. `maxpower`
ValueError) exact; `*line`; the ten `poly2cheb` … `lag2poly` conversions exact and mutually inverse; input
trimming. Gauss quadrature as above, weight functions, `chebgauss` closed form, `chebpts1` / `chebpts2`,
`chebinterpolate` exact on polynomials (and `args=`), `Chebyshev.interpolate` on a domain.
`polyutils`: `trimcoef` (tol, all-zero), `trimseq`, `as_series` (by row, dtype, trim, errors), `getdomain`
(real and complex), `mapparms`, `mapdomain` (formula, shape and subtype), `np.vander(increasing=)`.
Classes: `mapparms`, `__call__` domain mapping (exact composition), `deriv` / `integ` with a non-trivial window
(derivative with respect to x, not the mapped variable; explicit `lbnd` in domain coordinates), `roots()` on
mapped domains against mpmath, `fit` default domain / `window=` / `domain=[]` / `full=True` / list of degrees,
`convert().coef` = exact least squares (1e-6 relative on the badly scaled raw-year coefficients, values to
1e-10), `convert(kind=Chebyshev)`, mismatched domain / window / type `TypeError`, exact class arithmetic incl.
`//`, `%`, `divmod`, `**`, scalar operands, composition `p(q)`, `linspace`, `degree` / `trim` / `cutdeg` /
`truncate`, `has_same*`, `copy`, `==` / `!=` semantics, `basis`, `identity` (p(x) == x on any domain),
`fromroots` with domains, `cast`, iteration, unary ops, `set_default_printstyle` documented examples,
`__format__`, basis symbols of all six kinds, `repr`, `symbol=` (1.24+).
Legacy: `poly1d` coefficient order and attributes (`c`, `coef`, `coeffs`, `coefficients`, `order`, `o`, `r`,
`roots`, `variable`), indexing by power and `__setitem__` extension, leading-zero stripping, construction from
roots, `str`/`repr` layout, exact arithmetic incl. `/` → (quotient, remainder), `deriv`, `integ` with the
documented constant order, equality; `np.polyval` bit-identical to a plain Horner loop and composition with a
poly1d; `np.roots` leading zeros / trailing zeros / degree 0 and 1 / dtype; `np.polyder` values; `np.polyint`
k semantics (`P^(j)(0) = k[m-j-1]`) and errors; `np.polymul`, `np.polydiv` (documented example exact, degenerate
cases, 0-d operands), `np.polyadd` / `np.polysub` alignment; `np.poly` from roots (conjugate pairs → real
dtype), from a matrix (characteristic polynomial exact), empty and error cases; `np.polyfit` deg 0 with
`cov=True` (`RSS/(n-1)/n`) and `cov='unscaled'` (`1/n`), the `ValueError` when M ≤ order, `full=True` contents,
RankWarning only when rank < order and `full=False`, centred years, complex y, int y, weights, wrong-length
weights, 2-D y, coefficient order versus `numpy.polynomial.polynomial.polyfit`.

## Not checked and why

* `*fit` with complex x (the docstrings allow complex data; only complex y was checked).
* The `axis=` argument of `*der` / `*int` on multi-dimensional coefficient arrays (only 1-D coefficients).
* `_repr_latex_` output and `poly1d.__str__` for fractional / negative coefficients beyond the documented
  example (formatting only).
* The `RankWarning` on the degree-20 raw fit is LAPACK-dependent; only its presence and the rank were recorded.
