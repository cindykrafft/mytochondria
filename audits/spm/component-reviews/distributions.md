# Component review: statistical distribution & p-value functions

Scope: `spm_*cdf`/`spm_*pdf`, `spm_inv*cdf`, noncentral variants, `spm_t2z`,
`spm_z2p`, `spm_u`, `spm_lg_gamma`, `spm_betaln`, random-variate helpers.
Method: every file read in full; each candidate transcribed faithfully to
Python and compared with scipy.stats before being marked CONFIRMED.

## Confirmed

1. **`spm_lg_gamma.m:25`** — the generalised (multivariate) gamma sums
   *ascending* arguments `gammaln(b+0.5*(alpha-1))`; the definition (Muirhead
   p.62, Box & Tiao p.427 — the references the header cites) descends,
   `Γ(b)·Γ(b−1/2)·…`. The guard `b <= (p-1)/2` only makes sense for the
   descending form. `spm_lg_gamma(2,2)` = 0.8570 vs scipy `multigammaln` 0.4516;
   `(3,4)` = 9.1406 vs 5.4030. Correct only for p = 1. Callers with dim ≥ 2
   silently corrupted: `spm_kl_wishart`, `toolbox/mixture/spm_mix`,
   `toolbox/spectral/spm_mar`, `toolbox/mlm/spm_mlm_bayes`. **High.**
2. **`spm_ncFcdf.m:71-73`** — the noncentral-F series breaks when the *first*
   term is < 1e-12, but the Poisson weights grow until i≈δ/2; for δ ≳ 62 the
   loop exits at i=1. `spm_ncFcdf(5,[5,10],100)` = 1.90e-22 vs scipy 2.995e-4.
   (`spm_ncFpdf` starts its running term at the central pdf and is safe —
   verified.) **High.**
3. **`spm_ncTcdf.m:72`** — `exp(-δ²/2)` underflows for |δ| ≳ 39; every series
   term is 0 and the function silently returns 0/1. `spm_ncTcdf(39,10,39)` = 0
   vs 0.4411; accurate at δ=38. Propagates into `spm_ncTpdf`. **Medium.**
4. **`spm_Gcdf.m:99,106`** (hence `spm_Xcdf.m:62`) — `'upper'` tail leaves
   x ≤ 0 at the initialisation 0 where P(X>x) = 1. **Medium.**
5. **`spm_invIcdf.m:87-94`** — vectorised counting loop has no per-element
   `tr < n` guard; an element with F=1 (or above its roundoff pdf sum) keeps
   incrementing while any other element keeps the loop alive, returning r > n.
   `spm_invIcdf([1 .999999999999],[2 200],[.3 .5])` → r(1)=200 vs 2. **Medium.**
6. **`spm_Pcdf.m:100`** — non-integer x not floored (contrast `spm_Icdf:113`);
   `spm_Pcdf(2.5,3)` = 0.5397 vs 0.4232. **Medium.**
7. **`spm_Fpdf.m:105`** — x = 0 left at 0; correct pdf is Inf (v<2) or 1 (v=2).
   **Low.**
8. **`spm_Bpdf.m:80-84`** — boundary v==1 at x=0 (pdf = w) and w==1 at x=1
   (pdf = v) fall through to 0. **Low.**
9. **`spm_invTcdf.m:102-103`** — the Cauchy branch mask does not exclude
   F∈{0,1}, overwriting ±Inf with `tan(±π/2)` = ±1.63e16. **Low.**
10. **`spm_z2p.m:22`** — `nargin < 2` should be `< 3`; two-argument calls error
    (loud). **Low.**

## Verified correct

`spm_Tcdf`, `spm_Tpdf`, `spm_Fcdf`, `spm_Ncdf`, `spm_Npdf`, `spm_Ncdf_jdw`,
`spm_Gpdf` (incl. explicit x=0 cases), `spm_Bcdf`, `spm_Icdf`, `spm_Ipdf`,
`spm_Ppdf`, `spm_Xpdf`, `spm_Dpdf`, `spm_invBcdf`, `spm_invFcdf`,
`spm_invGcdf`, `spm_invNcdf`, `spm_invPcdf`, `spm_invXcdf`, `spm_ncFpdf`,
`spm_ncTpdf`, `spm_mvNpdf`, `spm_t2z` (direct branch numerically vs scipy to
~1e-10), `spm_u`, `spm_nCr`, `spm_betaln`, `spm_gamrnd` wrapper,
`spm_normrnd`, `spm_multrnd`, `spm_percentile`.
