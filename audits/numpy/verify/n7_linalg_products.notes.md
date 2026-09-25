# n7_linalg_products — notes

Harness: `audits/numpy/verify/n7_linalg_products.py`. Outputs: `n7_linalg_products.out` (numpy 2.4.6),
`n7_linalg_products.v1.23.5.out`, `.v1.24.4.out`, `.v1.26.4.out`. Runtime about 1 s per build.
Truths: mpmath at 50 digits (`eig`, `eigsy`, `eighe`, `qr`, `cholesky`, `svd_r`, `svd_c`, `lu_solve`, `inverse`, `det`,
`mnorm`), `fractions.Fraction` (determinants, integer products), closed forms, and explicit Python loops
(einsum, tensordot, dot/matmul/inner/kron/cross). No scipy anywhere.

## Counts

| build | ok | FAIL |
|---|---|---|
| numpy 2.4.6 | 308 | 0 |
| numpy 1.26.4 | 285 | 0 |
| numpy 1.24.4 | 285 | 0 |
| numpy 1.23.5 | 285 | 0 |

(2.x-only checks: cholesky `upper=`, `svdvals`, pinv/matrix_rank `rtol`, `vecdot`/`matvec`/`vecmat`,
`matrix_transpose`/`.mT`, the `np.linalg` array-API aliases, `matrix_norm`/`vector_norm`, the cross 2-D
DeprecationWarning, the 2.0 `solve` stacking rule. The 1.x builds instead check the pre-2.0 rules.)

## FAIL lines

None in any build. Every expectation that initially failed turned out to be a harness error and was
re-derived: (a) `pinv(rtol=None)` on `diag(1, 1e-3, 3e-16)` — the NumPy default `rcond=1e-15` *also* cuts
3e-16, so the value that distinguishes the two cut-offs is one between 3·eps = 6.7e-16 and 1e-15 (8e-16 is
used now); (b) `cond(p=None)` of the exactly singular `[[1,2],[2,4]]` is 4.8e16, not inf, because `gesdd`
returns a rounding-level smallest singular value (the documentation only says "May be infinite"; the inverse
based orders give inf as the source converts the nans); (c) `einsum_path` returns a *tuple*
`(path, string_repr)`; (d) `einsum 'ij,ji->'` truth had the wrong loop range; (e) `eigvalsh` of complex64
input correctly returns float32 (the harness listed it among the complex-valued outputs).

## Version-dependent behaviour encoded (all documented or in release notes; none judged a bug)

* `solve(a (3,4,4), b (4,))`: 2.x treats a 1-D b as the column vector (documented `versionchanged 2.0`);
  1.x raises `ValueError` because the vector path required `b.ndim == a.ndim - 1`, and `(4,1)` also fails
  (interpreted as a stack of four length-1 vectors); the 1.x way is `b[None, :, None]` or broadcasting b
  to `(3,4)`. `solve(a (3,3,3), b (3,3))`: 2.x solves each `a[i]` against the *matrix* b; 1.x solves
  `a[i]` against the *vector* `b[i]`. Both interpretations verified against mpmath.
* `lstsq` default `rcond`: 2.x = `rcond=None` = eps·max(M,N) (rank 2 on the (1, 1e-3, 3e-16) test);
  1.x emits the documented `FutureWarning` and uses -1 = machine precision (rank 3). Explicit
  `rcond=None` gives the new rule on every build (`linalg.py: if rcond is None: rcond = finfo(t).eps * max(n, m)`).
* `LinAlgError`: `class LinAlgError(Exception)` in 1.23.5 / 1.24.4, `class LinAlgError(ValueError)` from
  1.25 (1.26.4, 2.4.6). Code that writes `except ValueError` around `inv`/`solve` behaves differently
  across those builds.
* `norm` of empty matrices with `ord=2`, `inf`, `'nuc'`, and of an empty vector with `ord=inf`: 1.x raises
  `ValueError: zero-size array to reduction operation maximum which has no identity`; 2.x returns 0.0
  (`_linalg.py`: `abs(x).max(axis=axis, keepdims=keepdims, initial=0)`, `_multi_svd_norm(..., amax, 0)`).
  `ord=-2` / `-inf` on empty input still raise on every build. Not mentioned in the docstring
  (documentation gap, minor).
* `np.cross` with 2-D vectors: 2.x emits `DeprecationWarning: Arrays of 2-dimensional vectors are deprecated
  ... (deprecated in NumPy 2.0)`; 1.x silent. Both return the scalar z-component. `np.linalg.cross` (2.x)
  raises `ValueError` for 2-vectors outright.
* `np.dot` float32 on 1e6 uniform(0,1) products (truth `math.fsum` of the exact float64 products):
  2.4.6 relative error 1.2e-8, 1.x builds 2.6e-7 (different bundled OpenBLAS `sdot` blocking); float64
  dot 2e-16 / 4e-15. `np.sum(a*b)` in float32 (pairwise) 1.2e-8 / 7.4e-8. Informational.

## Observations recorded as info lines (documented and expected, or documentation gaps)

* `qr` sign convention is undocumented; LAPACK `dgeqrf` returns negative diagonal entries of R where
  mpmath's Householder returns positive ones (printed per matrix). Q columns / R rows agree with mpmath up
  to that per-column sign, |R_ii| agree to 1e-12. `mode='raw'` verified by rebuilding Q from the Householder
  reflectors `prod(I - tau_i v_i v_i^T)` and `triu(h.T)`; it reproduces `mode='complete'` exactly.
* `eig` with NaN input raises `LinAlgError` (`_assert_finite`), while the docstring lists only
  non-convergence under "Raises". Documentation gap.
* `eig` of a real matrix with all-real eigenvalues returns float64, documented ("cast to a real type").
  Eigenvectors are unit 2-norm with the largest component real (LAPACK `geev` convention; only the norm
  is documented). Defective `[[1,1],[0,1]]` returns eigenvectors of rank 1 as documented.
* `eigvalsh`/`eigh` really read only the documented triangle: a non-symmetric input gives the eigenvalues
  of `tril + tril^T` for `'L'` and of `triu + triu^T` for `'U'` (mpmath.eigsy), and the imaginary part
  of the diagonal of a complex input is ignored as documented.
* `cholesky` reads only the lower triangle (garbage in the upper triangle ignored); with `upper=True`
  (2.x) only the upper triangle (garbage in the lower ignored; garbage in the upper makes it fail with
  `LinAlgError`). Source: `gufunc = _umath_linalg.cholesky_up if upper else _umath_linalg.cholesky_lo`.
* `svd(hermitian=True)` on a non-symmetric input silently returns the wrong singular values
  (|eigenvalues| of one triangle); documented as an assumption, no check is performed.
* `inv` of the 12×12 Hilbert matrix (cond 1.6e16) and of `[[1,2],[2,4+1e-15]]` return without any
  warning; only an exactly singular LU pivot raises `LinAlgError('Singular matrix')`. Documented (only
  "singular" raises); users must check `cond` themselves.
* Integer overflow: `matrix_power(Fib, 92)` on int64 wraps silently (exact at n=90, F_91 = 4.66e18);
  `einsum('i,i')`, `np.dot` and `np.matmul` on int8 keep int8 and wrap (30000 -> 48), whereas `np.sum`
  and `np.trace` promote to the platform integer. General NumPy overflow semantics, not mentioned in the
  `matrix_power`/`einsum`/`dot` docstrings.
* `norm` of int8 / int64 arrays is computed after `astype(float)` (source), so no integer overflow
  (sqrt(30000) for int8 `[100,100,100]`, 2^62·sqrt 2 for int64).
* `pinv` default cut-off 1e-15·s_max vs `rtol=None` = max(M,N)·eps: on `diag(1,1e-3,8e-16)` the array-API
  rule keeps 8e-16 (giving 1.25e15) while the NumPy default cuts it; documented in 2.0. The cut-off is
  "less than or equal": `diag(1,1e-3,1e-9)` with `rcond=1e-3` keeps only the 1.
* `cond(p=None)` of an exactly singular matrix is finite (~1e16) (see above); `p=1`/`nuc` give inf.
* `np.linalg.transpose` (an undocumented helper present in every build, `numpy.linalg.linalg` /
  `numpy.linalg._linalg`) swaps only the last two axes, unlike `np.transpose` which reverses all axes.
* `trace` of an int8 matrix is accumulated in the platform int (documented dtype rule).

## What held up (all builds unless marked)

qr reduced/complete/r/raw on tall, wide, square, stacked and complex input (orthonormality, upper R,
Q@R = A, Householder reconstruction, mpmath agreement up to sign, dtype rules, 1-D raises);
cholesky lower / upper (2.x) / triangle read / non-PD raises / stacked / complex Hermitian / dtypes;
eig, eigvals vs mpmath on non-symmetric, complex-pair, symmetric, defective, stacked, float32, complex
matrices; eigh / eigvalsh UPLO, ascending order, orthonormality, Hermitian, imaginary diagonal, stacked,
dtypes; svd full/reduced/compute_uv/hermitian/stacked/complex/rank-deficient/float32 and svdvals (2.x);
tensorinv (ind 1 and 2) and tensorsolve (with axes) vs reshape + mpmath; multi_dot (2, 3, 4 matrices, 1-D
first/last/both, errors); matrix_power (0, 1, 2, 3, 30, 90 exact vs Fibonacci numbers, negative vs mpmath,
60th power of a random matrix vs 60 mpmath multiplications, singular/non-integer/non-square errors,
stacks); cond for all nine orders vs mpmath definitions, non-square, singular, stacked, dtypes; slogdet
(negative, zero, complex, overflowing, stacked) and det of int matrices vs Fraction (5×5 and 10×10),
dtypes; norm for vector orders None/2/1/inf/-inf/0/0.5/3/-1/-2/4.5, zero handling with negative orders,
all eight matrix orders vs mpmath, axis tuples (incl. non-adjacent and negative), keepdims, complex,
float32 dtype, int8/int64 inputs, empty, single element, NaN, invalid orders, matrix_norm/vector_norm (2.x);
lstsq over/under/rank-deficient/square, 1-D and multi-rhs b, residual shapes exactly as documented,
minimum-norm solutions vs mpmath, singular values, rcond thresholds, default-rcond rule per version,
dtypes, complex, errors; solve stacked (all broadcasting forms per version) vs mpmath, singular/non-square/
mismatch errors, dtype rules incl. float16 TypeError; inv vs mpmath, stacks, singular; pinv default/rcond/
rtol/hermitian/stacked/broadcast rcond/zero matrix/complex/dtypes vs mpmath SVD pseudo-inverse;
matrix_rank default/tol/rtol/hermitian/stacked/broadcast tol/1-D; trace/diagonal/diag offsets and axes,
linalg.diagonal/trace last-two-axes semantics (2.x); outer (flattening), kron (block formula, ndim
promotion), cross (3-D, 2-D, mixed, axisa/axisb/axisc/axis, broadcasting, 4-vectors error, deprecation);
tensordot with int axes 0/1/2, tuple-of-lists and pair-of-ints axes vs loops; einsum on 23 subscript
patterns vs loops (trace, diagonal, transpose, sums, matmul, implicit output, batch, ellipsis, outer,
inner, Hadamard, partial diagonals, three operands, chains), optimize=False/True/greedy/optimal/explicit
path identical, einsum_path structure, 0-d scalar rule, int8 overflow, dtype=, out= casting, invalid
subscripts, float32 and float64 vs mpmath; dot vs matmul for 4-D operands against the documented index
formulas, matmul broadcasting, 1-D promotion rules, scalar rejection, @ operator; vdot conjugation and
flattening, inner on N-D, vecdot (axis, broadcasting, conjugation), matvec/vecmat (2.2+) definitions;
array-API aliases equal to the main namespace; transpose vs matrix_transpose/.mT; LinAlgError raised by
17 documented failure paths and not raised by the TypeError/ValueError paths; result-dtype table (int ->
float64, float32 -> float32, complex64 -> complex64 / float32 for real outputs, mixed promotion, float16
and longdouble TypeError, object TypeError); a two-level (2,3,4,4) stack sweep through inv/det/slogdet/
eigvals/eigvalsh/svd/qr/cholesky/pinv/cond/norm/matrix_power/matrix_rank/solve each compared element-wise
with mpmath; empty stacks and the (0,0) determinant convention.

## Not checked, and why

* LAPACK non-convergence paths (`LinAlgError` from `_geev`/`_gesdd` failing): no reproducible input.
* `numpy.matrix` subclass preservation promised by several docstrings (deprecated class; out of scope).
* `out=` arguments of `multi_dot`/`matmul` and the gufunc `axes=` keyword of `matmul`/`vecdot`.
* Object-dtype `matrix_power` (documented fallback to `dot`) — only the TypeError for object input to
  `inv`/`eig` was checked.
* Eigenvector phase/sign conventions of `eig`/`eigh`/`svd` beyond unit norm: not documented, only recorded.
* `einsum` with `casting=` variants other than the default, and `order=`.
* Comparison with scipy (none on the 1.x builds; not required, mpmath was used as the truth throughout).
