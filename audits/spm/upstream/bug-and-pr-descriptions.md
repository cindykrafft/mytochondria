# SPM high-priority correctness fixes — bug reports & PR descriptions

Five independent fixes, prepared as one commit each on branch
`fix/high-priority-correctness` (based on upstream `spm/spm@530ec52`).
Each can be submitted as its own PR/issue, or combined into a single PR
with five commits. Numeric claims were verified offline (NumPy/SciPy) or
by internal-consistency argument; none have been run inside a live MATLAB
install, so please regression-test before merging.

---

## 1 — Chi-squared EC densities use the wrong power of t (dimensions 2 & 3)

**File:** `spm_ECdensity.m` (STAT=='X' branch) · **Severity:** high (invalid inference on χ² SPMs) · **Reach:** χ² statistic images only

### Bug report

The chi-squared Euler-characteristic density branch builds a single leading
factor `b = t.^(1/2*(v-1)) .* exp(-t/2-gammaln(v/2))/2^((v-2)/2)` and reuses
it for the 1-, 2- and 3-dimensional EC densities:

```matlab
EC(2,:) = a^(1/2)*b;
EC(3,:) = a*b.*(t-(v-1));
EC(4,:) = a^(3/2)*b.*(t.^2-(2*v-1)*t+(v-1)*(v-2));
```

Worsley's χ² EC densities require the power of `t` to **decrease with
dimension**: `t^((v-1)/2)`, `t^((v-2)/2)`, `t^((v-3)/2)` for the 1D/2D/3D
densities respectively. (The F-field branch a few lines below does exactly
this — it decrements the exponent for each order.) As shipped:

- `EC(3,:)` is too large by a factor of **√t**
- `EC(4,:)` is too large by a factor of **t**

**Impact.** For χ² statistic images this corrupts every RFT p-value: peak
FWE-corrected p-values come out far too conservative, while cluster-extent
p-values (which divide by the expected EC) are grossly **anticonservative**.
T- and F-fields are unaffected. Reached via `spm_P_RF` / `spm_P` / `spm_uc*`
whenever `STAT=='X'`.

**Reproduction (offline).** Compare `spm_ECdensity('X',t,[1 v])` against the
F-field limit χ²_v = v·F(v,∞): the corrected densities agree to the finite-df
reference tolerance, while the old EC(3)/EC(4) reproduce the exact √t and t
discrepancies (e.g. at t = 8, 15, 25 the buggy EC(3)/reference ratios are
2.83, 3.87, 5.00 = √t and EC(4) ratios 8, 15, 25 = t).

### PR description

**Fix chi-squared EC densities (wrong power of t at dimensions 2 and 3)**

The `STAT=='X'` branch of `spm_ECdensity` reused a single `t^((v-1)/2)`
leading factor across EC densities of all dimensions. Worsley's χ² EC
densities need `t^((v-d)/2)` for the d-th density, so the shipped `EC(3,:)`
was inflated by √t and `EC(4,:)` by t. This makes RFT inference on χ²
statistic images wrong (conservative peak FWE, anticonservative cluster
extent).

This factors the common terms out of `b` and applies the correct
`t^((v-1)/2)`, `t^((v-2)/2)`, `t^((v-3)/2)` power to EC(2)/EC(3)/EC(4).
`EC(2,:)` is unchanged. Verified numerically against the F-field limit
(χ²_v = v·F(v,∞)); T- and F-field densities are untouched.

---

## 2 — Free-energy log-det term overcounted by a factor of nq (`spm_nlsi_GN`)

**File:** `spm_nlsi_GN.m:500` · **Severity:** high (wrong model evidence) · **Reach:** models with >1 error-covariance block (DCM-ERP / induced)

### Bug report

The E-step log-evidence term is:

```matlab
L(1) = spm_logdet(iS)*nq/2 - real(e'*iS*e)/2 - ny*log(8*atan(1))/2;
```

At this point `iS` has already been Kronecker-expanded to the full ny×ny
precision (`iS = kron(speye(nq),iS)` earlier in the M-step), so
`spm_logdet(iS)` already equals `nq·logdet(iS_small)`. Multiplying by an
additional `nq/2` scales the log-det term by **nq²/2** instead of the
correct **nq/2** — an overcount of factor nq.

**Internal-consistency confirmation.** The M-step Fisher gradient uses
`ny/2` (= nq·ny_small/2) for the log-det derivative (the `nh==1`
simplification, and `trace(PS{i})*nq/2` generally). That is the derivative
of the *corrected* term ½·logdet(iS_full), not of the shipped
(nq/2)·logdet(iS_full). So the objective and the gradient that optimises it
are currently inconsistent.

**Impact.** Confined to `nq > 1`, i.e. multiple error-covariance components
— e.g. **DCM for evoked/induced responses** (channels × trials). The
hyperparameter-dependent part of the free energy is inflated nq-fold, which
distorts free-energy differences and hence **Bayesian model comparison**.
Parameter estimates are unaffected; fMRI DCM (nq == 1) is unaffected.

### PR description

**Fix free-energy log-det term overcounted by factor nq in `spm_nlsi_GN`**

`L(1)` computed the log-evidence log-det as `spm_logdet(iS)*nq/2`, but `iS`
is already the Kronecker-expanded ny×ny precision at that point, so
`spm_logdet(iS)` already carries the nq factor. The term was therefore
scaled by nq² rather than nq. This is corrected to `spm_logdet(iS)/2`, which
matches the M-step gradient (`ny/2`) that ascends this objective.

Only affects models with more than one error-covariance component (nq > 1,
e.g. DCM-ERP/induced), where it changes the free energy and thus model
comparison; nq == 1 (fMRI DCM) is unchanged.

---

## 3 — Baseline double-counted mapping artefact events to samples (`badsamples`)

**File:** `@meeg/badsamples.m:39-40` · **Severity:** high (silent, epoched M/EEG) · **Reach:** automatic artefact rejection on epoched data with a baseline

### Bug report

`badsamples` converts artefact-event times to sample indices with:

```matlab
samples = find((trialonset(this,trialind(i))+time(this))>=ev(k).time & ...
               (trialonset(this,trialind(i))+time(this))<=(ev(k).time+ev(k).duration));
```

`time(this)` returns the peristimulus axis **including** the baseline offset
(`time = timeOnset + (0:n-1)/fs`). But artefact-event times are written by
the detectors **relative to trial onset, excluding** `timeOnset` — e.g.
`spm_eeg_artefact_jump`:

```matlab
res(end).time = D.time(onsets(k)+1) - D.time(1) + D.trialonset(i);
%             = trialonset + onsets(k)/fs   (the timeOnset terms cancel)
```

So `timeOnset` is added on the reader side but not present on the writer
side, and every bad-sample window is shifted by **timeOnset·fs samples** —
the whole baseline. Example: 100 ms baseline at 250 Hz (`timeOnset = -0.1`)
shifts the mask by 25 samples on every epoch.

**Impact.** Corrupts anything that maps artefact events to samples on
epoched data: `spm_eeg_artefact` bad-channel/segment classification,
`spm_eeg_average`/`_TF` `removebad` masking, `spm_eeg_cfc` weighting, and
DAiSS robust covariance.

**Note (out of scope for this fix).** There is a separate, one-sample
inconsistency between detector families (`jump/threshchan/flat/nans/zscore`
write `onset/fs`; `eyeblink/saccade/heartbeat` write `(onset-1)/fs`). This
patch does not attempt to unify that; it only removes the baseline-length
error.

### PR description

**Fix baseline double-counting when mapping artefact events to samples**

`badsamples` added `trialonset + time(this)`, but `time(this)` already
includes the peristimulus `timeOnset`, whereas detector event times are
stored relative to trial onset without it. The onset offset was thus counted
twice, shifting every bad-sample window by the baseline length
(`timeOnset·fs` samples) on epoched data.

Uses the trial-relative offset `(0:nsamples-1)/fsample` instead of
`time(this)`. Behaviour is identical when `timeOnset == 0` (continuous data,
or epochs with no baseline); the spurious shift is removed otherwise.

---

## 4 — Downsampled dataset stamped with requested, not achieved, rate

**File:** `spm_eeg_downsample.m:115` · **Severity:** high (silent time-axis error) · **Reach:** downsampling with a non-integer ratio

### Bug report

The output object is stamped with the **requested** rate:

```matlab
Dnew = fsample(Dnew, S.fsample_new);
```

But `ft_preproc_resample` uses a **rounded integer** decimation factor, so
the achieved rate can differ from the request. The achieved rate is already
computed a few lines above and used for the printed "Resampling frequency":

```matlab
fsample_new = (nsamples_new/D.nsamples)*D.fsample;   % achieved rate (line 52)
...
fprintf(... 'Resampling frequency' ... fsample_new ...);   % displays achieved
...
Dnew = fsample(Dnew, S.fsample_new);   % but STORES requested (line 115)
```

So the stored and displayed rates disagree for non-integer ratios. Example:
requesting 1000 → 180 Hz actually yields ~166.7 Hz, but the file is labelled
180 Hz. Every downstream time axis, latency and filter cutoff derived from
the stored rate is then silently ~8 % wrong. Integer ratios are unaffected.

### PR description

**Stamp downsampled dataset with achieved, not requested, sampling rate**

`spm_eeg_downsample` stored `S.fsample_new` (the requested rate) on the
output object, but `ft_preproc_resample` rounds the decimation factor, so
the achieved rate — already computed as `fsample_new` and used for the
on-screen report — can differ. For non-integer ratios the stored rate was
wrong (e.g. requested 180 Hz, actual ~166.7 Hz), silently biasing all
downstream latencies and filters. Stores the computed `fsample_new` so the
stamped rate matches the data.

---

## 5 — Parametric-modulation contrast padding ignores basis functions

**File:** `spm_design_contrasts.m:63` · **Severity:** high (silently wrong contrasts) · **Reach:** factorial fMRI with a multi-column basis + parametric modulators

### Bug report

When expanding automatic factorial contrasts, each condition block is padded
for parametric modulators by:

```matlab
block = [block, zeros(nr, sum([SPM.Sess(1).U(cc).P.h]))];
```

But in the design matrix, **every** `U.u` column — the main regressor and
each parametric-modulation column — is convolved with all `nbases` basis
functions (see `spm_Volterra`), so a condition occupies
`(1 + sum(h)) * nbases` columns. Padding only `sum(h)` (not `sum(h)*nbases`)
under-pads by `sum(h)*(nbases-1)` columns per modulated condition, sliding
all subsequent conditions' contrast weights onto the wrong regressors. The
final zero-pad to design width (`con(c).c(:,end+1:k)=0`) hides the size
mismatch, so **no error is raised** and the resulting F/T maps are silently
wrong.

**When triggered:** `nbases > 1` (HRF + temporal/dispersion derivatives,
FIR, Fourier) **and** at least one parametric modulator, in a factorial
design — the auto-contrasts created by `spm_run_fmri_est` when `SPM.factor`
is set.

**Worked example.** 2 conditions, `nbases = 2`, one linear modulator on
condition 1. The design has columns
`[c1·bf1, c1·bf2, mod·bf1, mod·bf2, c2·bf1, c2·bf2]` (6). The "main effect"
contrast `[1 -1]` expands to weights on c1 and c2, but with only 1 pad column
the −1 lands on `mod·bf2 / c2·bf1` instead of `c2·bf1 / c2·bf2`.

### PR description

**Account for basis functions when padding parametric-modulation columns**

`spm_design_contrasts` padded automatic factorial contrasts with `sum(h)`
zero columns for parametric modulators, but each modulator column is
convolved with all `nbases` basis functions in the design, so a condition
spans `(1+sum(h))*nbases` columns. The under-padding shifted subsequent
conditions' weights onto the wrong regressors whenever `nbases > 1` and
modulators were present, producing silently wrong F/T maps (the trailing
zero-pad hid the mismatch).

Multiplies the modulation pad width by `nbases`. No change when
`nbases == 1` or when there are no parametric modulators.

---

## Applying these to your own fork

The session that produced these could not fork `spm/spm` (its GitHub access
was scoped to another repo), so the commits are provided as a patch series
and a git bundle. To land them on your own fork:

```bash
# 1. Fork spm/spm on GitHub (web UI or: gh repo fork spm/spm --clone)
git clone https://github.com/<you>/spm && cd spm

# 2a. Apply the patch series (preserves the 5 separate commits + messages)
git checkout -b fix/high-priority-correctness
git am /path/to/patches/*.patch

#     ...or 2b. pull straight from the bundle
git fetch /path/to/spm-high-priority-fixes.bundle \
    fix/high-priority-correctness:fix/high-priority-correctness
git checkout fix/high-priority-correctness

# 3. Regression-test in MATLAB, then push and open PRs
git push -u origin fix/high-priority-correctness
```

The patches are based on `spm/spm@530ec52`; if your fork has moved on,
`git am` may need `-3` (three-way merge) or a quick rebase.
