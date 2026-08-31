# FSL bug analysis against 114 published papers (2021–2026)

_Companion to `../freesurfer-analysis/`. Generated 2026-08-31._

## What this is

The six-journal survey found **114 papers** in *Nature*, *Science*, PNAS and *Cell*
(2021–2026) that used FSL. Each paper's full text was re-mined for **which FSL tools it
ran** (`fsl_papers.tsv`), and the corresponding component repositories from Oxford WIN's
GitLab (`git.fmrib.ox.ac.uk/fsl/*`, current master with git history consulted for
version dating) were read adversarially for bugs that change published numbers.
Seven component reviews with file:line evidence live in `component-reviews/`;
per-paper exposure is joined in `fsl_paper_exposure.tsv`.

**Epistemic status.** Code-level findings. Several were verified beyond reading: the
reviewers compiled routines verbatim and checked them against 400-digit arithmetic and
scipy (f2z, t2z, GRF Infer, the smoothness LUT), ported suspect estimators to Python
against grid-search ground truth (FLAME), and ran a 9,000-repetition simulation of the
FILM pipeline (Tukey taper). Two reviewers independently derived the same f2z defect.
None has yet been reproduced by running FSL binaries on imaging data. "Exposed" means a
paper used the affected feature/version — not that its conclusions are wrong.

## How the papers use FSL

| Feature | Papers |
|---|---|
| Task fMRI GLM (FEAT/FILM) | 25 |
| Distortion correction (topup/eddy) | 24 |
| Linear registration (FLIRT) | 19 |
| Brain extraction (BET) | 16 |
| Permutation inference (randomise/TFCE) | 10 |
| Group mixed effects (FLAME) | 9 |
| MCFLIRT / dtifit-bedpostx | 9 / 9 |
| FNIRT / GRF cluster correction | 7 / 7 |

Versions named: 5.0.9 (11), 6.0.x (scattered), most unstated. PNAS 92, Nature 19.

## Findings, ranked by (severity × exposure)

### Tier 1 — statistical inference

**FS1. A misplaced parenthesis in the F→z conversion understates F-test z-statistics by
up to several z-units — in every FSL version from the origins through current master.**
CONFIRMED, **independently by two reviewers** (one compiled the routine verbatim against
400-digit mpmath; the other re-derived the series and ported to Python vs scipy).
`miscmaths/f2z.cc:48` multiplies the log-Beta normalization by `d1/2`; the error is
exactly zero for 2-row contrasts (why it survived ~25 years) and grows with both dofs:
d1=4, d2=200, F=20 reports z=6.05 (true 7.39); d1=6, d2=500, F=20 reports **4.97 (true
9.33)**. Engages above z≈4.8 — precisely the headline-peak regime. Worse, the output is
**non-monotone in F**, and a fallthrough writes **+inf voxels** into zfstat maps. Every
producer of zfstats inherits it: FILM (first level), FLAME (all run modes), randomise.
Related (FS1b): 1-row F-tests never use the asymptotic and saturate at z≈8.2 / +inf.
Direction: conservative below the cliff, garbage above it; rank order of peaks distorted.
Exposure: any of the 29 FEAT/FLAME papers that reports F-contrast z-statistics.
A one-parenthesis fix reproduces the true log-sf to 4 decimals.

**FS2. FLAME1+2 F-test dof collapses to ≈3 for any design with ≥2 EVs.** CONFIRMED.
`multitfit` (`flameo/gsmanager.cc:471`) applies the univariate t moment-matching formula
`v = 2/(1−φ/cosi)` to a P-dimensional fit (needs `cosi/P`). Verified by faithful port:
P=1 recovers true dof; P≥2 returns ~2.3–2.9 regardless of truth — even for Gaussian
samples. F=10 at d1=2: z=3.04 at the correct dof 18 vs z=1.67 at dof 3. Massively
deflates flame12 F statistics; t contrasts unaffected.

**FS3. The FILM Tukey taper is off by one lag — lag 0 is tapered — inflating every
default first-level t/z by ~1–1.5%.** CONFIRMED by a 9,000-rep simulation of the full
pipeline (AR(1) φ=0.35, N=180, default M): variance understated 2.6% from the taper
shift alone. Deterministic, in every default FEAT first-level analysis, not reduced by
spatial ACF smoothing. Small per-voxel, but it is a bias on ~all 25 FEAT papers'
statistics, plus a further ~0.5–3% from a σ² divisor (N−p) inconsistent with the
reported dof (N−p−1).

**FS4. GRF cluster machinery: three coding defects on top of the known assumption
gap.** CONFIRMED (verified by compiling the code under test):
(a) *2D images get 3D constants* — `setD(2)` arrives after `Infer`'s constructor froze
the 3D Euler density; single-slice cluster p-values are **100–12,000× too small**
(anticonservative). Whole-brain 3D is unaffected by this one.
(b) *The dof-correction LUT interpolation is broken* (slope anchored at the lower node,
added to the upper node's value): smoothness overestimated at small n — a cluster at
true p=0.05 reported as p=0.077 at dof 5 (conservative; bites small-n FLAME groups).
(c) A (2π) exponent sign error in the |t|≥8 branch (conservative, practical impact nil,
but a p-discontinuity at t=8). Meanwhile the 3D GRF formulas themselves were verified
as a faithful Friston/Worsley implementation — the Eklund-type anticonservativeness at
z=2.3 is the theory's assumptions (hard-wired 26-connectivity vs connectivity-free
theory; squared-exponential ACF), faithfully implemented.

**FS5. randomise: historical F-TFCE statistic change and a border-voxel exclusion.**
CONFIRMED. Pre-5.0.7 (fixed 2014), F-contrast TFCE enhanced the *raw F map* — a
different statistic; p-values don't reproduce across the 5.0.6/5.0.7 boundary and can
cross 0.05 either way. And in **all** versions, the fast TFCE excludes the outermost
voxel shell: border voxels can never reach significance (tight-FOV/subject-space
analyses; padded MNI152 unaffected). Also: `--uncorrp` cluster p images are written all
zero; the 6.0.6 RNG change breaks `--seed` reproducibility across versions (expected,
documented — not a bug). The core p-value convention (exact Phipson–Smyth, identity
included) and Freedman–Lane confound handling were verified correct.

### Tier 2 — measurement bias

**FS6. dtifit: a 1%-of-S0 signal floor caps measurable diffusivity at 4.6/b (CSF MD
underestimated ~2× at b=3000), and unclamped negative eigenvalues let FA>1 and negative
MD reach output files** (ROI FA inflated near mask edges/CSF). CONFIRMED; both hit the
same low-signal voxels. Single-shell b=1000 in-brain largely unaffected.

**FS7. BET2 brain volumes are biased upward by a partial one-voxel boundary shell
(~1–2% at 1 mm, grows with voxel size), plus a subject-dependent smoothing fallback.**
CONFIRMED. Consistent across subjects, so group contrasts mostly survive; absolute
volumes and cross-resolution comparisons are biased.

**FS8. FAST4 bias-field smoothing doesn't match its documentation (σ=0.51·`-l`, ~20%
smoother than the stated FWHM; `kernalsize` argument ignored) and single- vs
multi-channel modes use dimensionally different rules.** CONFIRMED; tissue volumes not
comparable across modes at the same `-l`.

### Tier 3 — environment/invocation traps

**FS9. Threaded sinc interpolation has a data race**: shared mutable kernel scratch
buffers written by a `const` method while `raw_general_transform` parallelizes over
rows. `applywarp --interp sinc` with `FSL_NUM_THREADS>1` produces plausible-looking but
wrong, nondeterministic voxel values. CONFIRMED from code; trilinear and spline safe.

**FS10. `flirt -usesqform` applies the basescale conversion twice** — and basescale≠1
auto-enables for sub-0.75 mm voxels (7T/HCP structurals): init translations inflated
×2–2.8, capable of pushing the search out of its basin on exactly the data the flag
targets. CONFIRMED.

**FS11. Fieldmap-BBR extrapolation direction is a transformed homogeneous *point***
(translation contaminates the "PE direction"; PE axis hard-coded to y): `epi_reg
--fmap` transforms biased at fieldmap-mask edges. CONFIRMED.

**FS12. eddy/topup: core geometry exonerated**, with narrow exceptions: applytopup
`--method=jac` uses xdim for the y-scale in its plain-fieldmap branch (anisotropic
in-plane voxels only); rotated bvecs may ignore the x-flip convention for
neurological-stored NIfTIs (PLAUSIBLE, ~2× subject rotation); `--repol` slices can be
part-original at FOV edges. Bvec rotation direction, field units/signs, and
single-application Jacobian modulation all verified correct.

## What held up

- **t→z conversion**: exact to ~1e-4 z over dof 3–1000, t to 50 — published t-based
  zstat maps are numerically sound arbitrarily far into the tail (two reviewers).
- **FLAME t-contrast paths** (OLS/FE/FLAME1 — the overwhelmingly common higher-level
  configs) and the OLS/GLS variance algebra.
- **randomise's p-value convention** (exact, p ≥ 1/nPerms, ties against H0), genuine
  Freedman–Lane, and TFCE core numerics (fixed dh, connectivity tables).
- **3D GRF formulas** (exact Friston/Worsley), smoothest core algebra, FEAT wiring of
  dof/DLH/RESELS/VOLUME.
- **eddy's bvec rotation ↔ resampling consistency**, topup field units end to end.
- **MCFLIRT** (motion applied exactly once, exact RMS), MI/NMI/CR histogram machinery,
  spline interpolation, premat/warp/postmat composition.
- **dtifit linear chain** (b-matrix, FA/MO formulas), bedpostx model math, BET2
  evolution equations.

## Files

| File | Contents |
|---|---|
| `fsl_papers.tsv` | 114 papers × versions × commands × features |
| `fsl_paper_exposure.tsv` | per-paper applicable findings (conditions in parentheses) |
| `component-reviews/*.md` | the seven full reviews with file:line evidence |
| `fsl_profile.py` | the script that mined FSL usage from paper full texts |

Exposure counts: FS1 candidates 29 (F-test reporting to be checked per paper), FS3 25
(universal small inflation), FS4b 26 (small-n condition), FS7 16, FS6 9, FS2 9, FS9-11
environment/invocation-dependent.

## Filing route (differs from FreeSurfer)

FSL's GitLab has issues enabled but external signup appears closed; the sanctioned
outside channel is the **FSL JISCMail mailing list**, monitored by the developers.

The filing material itself — JISCMail-ready report per finding, `git format-patch`
fixes for six of them (FS1 one-line; FS2, FS3, FS4b, FS10, FS12a small), verification
harnesses, and the intro post — lives in its own dedicated repository, deliberately
outside this one: **github.com/cindykrafft/fsl-bug-reports**. This directory keeps
only the analysis (reviews, paper exposure); nothing here is sent upstream.
