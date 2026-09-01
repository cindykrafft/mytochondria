# SPM upstream submission kit

Five independent fixes, each staged as a single-commit branch on your fork
(`cindykrafft/spm`), ready to submit to `spm/spm`. SPM's CONTRIBUTING.md asks
for: bugs as GitHub issues with expected vs. actual behaviour and reproduction
code; PRs from external contributors are welcome. There is no issue/PR
template and no CLA.

**Suggested flow per fix:** (1) search existing issues first (CONTRIBUTING
asks this — try the function name, e.g. "ECdensity"); (2) open the issue;
(3) open the PR from the compare link, replacing `#NNN` in the PR body with
the real issue number.

**Before submitting anything**, see the pre-flight checklist at the bottom.

---

## 1 — spm_ECdensity (chi-squared EC densities)

**Branch:** `fix/ecdensity-chi2` (fix + new unit test)
**Open PR:** https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/ecdensity-chi2?expand=1
**Open issue:** https://github.com/spm/spm/issues/new

### Issue title
`spm_ECdensity: chi-squared EC densities use the wrong power of t at dimensions 2 and 3`

### Issue body
```markdown
**Summary.** In the `STAT=='X'` branch of `spm_ECdensity.m` (lines 48-53), a
single leading factor `b ∝ t^((v-1)/2)` is reused for the EC densities of all
dimensions. Worsley's chi-squared EC densities require the power of t to
decrease with dimension: `t^((v-1)/2)`, `t^((v-2)/2)`, `t^((v-3)/2)` for the
1D/2D/3D densities (compare the F-field branch below it, which decrements the
exponent per order). As shipped, `EC(3,:)` is too large by a factor of
`sqrt(t)` and `EC(4,:)` by a factor of `t`.

**Impact.** RFT inference on chi-squared statistic images: peak FWE-corrected
p-values far too conservative, cluster-extent p-values strongly
anticonservative, via `spm_P_RF`/`spm_P`/`spm_uc*` with `STAT=='X'`. T- and
F-fields are unaffected.

**Reproduction** (uses the identity chi²_v = v·F(v,∞), relying only on the
F branch):

```matlab
t = 15; v = 10;
EC_X = spm_ECdensity('X', t,   [1 v]);
EC_F = spm_ECdensity('F', t/v, [v 1e8]);
EC_X(3)/EC_F(3)   % expected: ~1     actual: 3.873 (= sqrt(15))
EC_X(4)/EC_F(4)   % expected: ~1     actual: 15.0  (= t)
```

The same discrepancy shows against the identity chi²_1 = Z²
(`spm_ECdensity('X',t,[1 1])` vs `2*spm_ECdensity('Z',sqrt(t),[])`), and
against direct simulation of smooth chi-squared fields.

**Environment:** platform-independent (pure MATLAB code path; present in
current `main`).

A pull request with the one-line-per-density fix and a new unit test
(`tests/test_spm_ECdensity.m`) follows.
```

### PR title
`Fix chi-squared EC densities (wrong power of t at dimensions 2 and 3)`

### PR body
```markdown
Fixes #NNN.

The `STAT=='X'` branch of `spm_ECdensity` reused a single `t^((v-1)/2)`
leading factor across EC densities of all dimensions. Worsley's chi-squared
EC densities need `t^((v-d)/2)` for the d-th density, so the shipped
`EC(3,:)` was inflated by `sqrt(t)` and `EC(4,:)` by `t`, corrupting RFT
inference on chi-squared statistic images (conservative peak FWE,
anticonservative cluster extent).

This PR factors the common terms out of `b` and applies the correct
`t^((v-1)/2)`, `t^((v-2)/2)`, `t^((v-3)/2)` powers to EC(2)/EC(3)/EC(4).
`EC(2,:)` is unchanged, as are the Z/T/F branches (verified bit-identical).

It also adds `tests/test_spm_ECdensity.m` (the file previously had no test
coverage), which checks the densities against closed-form reference values,
the chi²_1 = Z² identity, and the chi²_v = v·F(v,∞) limit, plus a
T-vs-Gaussian large-df guard. The test fails on the pre-fix code (12/23
assertions) and passes on the fixed code (verified by executing the
assertions; the matlab.unittest wrapper follows the pattern of
tests/test_spm_Ncdf.m).
```

---

## 2 — spm_nlsi_GN (free-energy log-det term)

**Branch:** `fix/nlsi-gn-logdet`
**Open PR:** https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/nlsi-gn-logdet?expand=1

### Issue title
`spm_nlsi_GN: free-energy log-det term overcounted by a factor of nq`

### Issue body
```markdown
**Summary.** In `spm_nlsi_GN.m`, the E-step objective computes

```matlab
L(1) = spm_logdet(iS)*nq/2 - real(e'*iS*e)/2 - ny*log(8*atan(1))/2;
```

but by this point `iS` has already been Kronecker-expanded to the full
ny×ny precision (`iS = kron(speye(nq),iS)` in the M-step, line ~421), so
`spm_logdet(iS)` already equals `nq*logdet(iS_small)`. The extra `*nq`
scales the log-det term by nq²/2 instead of the correct nq/2.

**Internal-consistency check.** The M-step Fisher gradient uses `ny/2`
(and `trace(PS{i})*nq/2` generally) — which is the derivative of the
corrected term `(1/2)*logdet(iS_full)`, not of the shipped one, i.e. the
objective and the gradient ascending it currently disagree.

**Reproduction** (the identity at the heart of it):

```matlab
A  = spm_Q(1/2,8) + speye(8);          % any SPD precision block
nq = 4;
iS = kron(speye(nq), A);
spm_logdet(iS)*nq/2                     % term as computed at spm_nlsi_GN.m:500
spm_logdet(iS)/2                        % correct: (1/2)*logdet of full precision
nq*spm_logdet(A)/2                      % equals the correct value
```

**Impact.** Only models with more than one error-covariance block
(`nq > 1`), e.g. DCM for evoked/induced responses. The
hyperparameter-dependent part of the free energy is inflated nq-fold,
which can distort free-energy differences and hence Bayesian model
comparison. Parameter estimates and fMRI DCM (nq == 1) are unaffected.

**Environment:** platform-independent; present in current `main`.
```

### PR title
`Fix free-energy log-det term overcounted by factor nq in spm_nlsi_GN`

### PR body
```markdown
Fixes #NNN.

`L(1)` computed the log-evidence log-det as `spm_logdet(iS)*nq/2`, but `iS`
is already the Kronecker-expanded ny×ny precision at that point, so
`spm_logdet(iS)` already carries the nq factor and the term was scaled by
nq² rather than nq. Corrected to `spm_logdet(iS)/2`, which matches the
M-step gradient (`ny/2` / `trace(PS)*nq/2`) that ascends this objective.

Only affects models with more than one error-covariance component (nq > 1,
e.g. DCM for ERP/induced responses), where it changes the free energy and
thus model comparison; nq == 1 (fMRI DCM) is unchanged.
```

---

## 3 — @meeg/badsamples (baseline double-counted)

**Branch:** `fix/meeg-badsamples-baseline`
**Open PR:** https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/meeg-badsamples-baseline?expand=1

### Issue title
`@meeg/badsamples: peristimulus timeOnset double-counted when mapping artefact events to samples`

### Issue body
```markdown
**Summary.** `badsamples` converts artefact-event times to sample indices
with `trialonset(this,i) + time(this)`, but `time(this)` already includes
the peristimulus offset (`time = timeOnset + (0:n-1)/fs`), while the
artefact detectors write event times relative to trial onset *without*
timeOnset — e.g. `spm_eeg_artefact_jump.m` (line ~126):

```matlab
res(end).time = D.time(onsets(k)+1) - D.time(1) + D.trialonset(i);
%             = trialonset + onsets(k)/fs   (timeOnset cancels)
```

So timeOnset is added on the read side but absent on the write side, and
every bad-sample window is shifted by `timeOnset*fs` samples — the whole
baseline — on any epoched dataset.

**Expected vs actual.** For a 100 ms baseline at 250 Hz
(`timeOnset = -0.1`), an artefact event written for epoch sample n is
expected to mark samples around n; actually samples around n+25 are marked
(off by the baseline length), so clean data is excluded and part of the
artefact retained.

**Reproduction** (any epoched dataset D with timeOnset < 0):

```matlab
n  = 50;                       % target sample within the epoch
ev = struct('type','artefact_jump','value',char(chanlabels(D,1)), ...
            'time', trialonset(D,1) + n/fsample(D), 'duration', 0);
D  = events(D, 1, [events(D,1,'samples'), ev]);
bad = badsamples(D, ':', ':', 1);
find(any(bad,1), 1)            % expected ~n; actual n + 1 - timeonset(D)*fsample(D)
```

**Impact.** Anything mapping artefact events to samples on epoched data:
`spm_eeg_artefact` bad-channel/segment classification, `removebad` masking
in `spm_eeg_average`/`_TF`, `spm_eeg_cfc`, DAiSS robust covariance.
Continuous data with timeOnset == 0 is unaffected.

**Environment:** platform-independent; present in current `main`.

Note: there is a separate one-sample inconsistency *between* detector
families (jump/threshchan/flat/nans/zscore write `onset/fs`;
eyeblink/saccade/heartbeat write `(onset-1)/fs`). The attached fix does not
attempt to unify that; it only removes the baseline-length error.
```

### PR title
`Fix baseline double-counting when mapping artefact events to samples`

### PR body
```markdown
Fixes #NNN.

`badsamples` added `trialonset + time(this)`, but `time(this)` already
includes the peristimulus `timeOnset`, whereas detector event times are
stored relative to trial onset without it. The onset offset was counted
twice, shifting every bad-sample window by the baseline length
(`timeOnset*fs` samples) on epoched data.

This uses the trial-relative offset `(0:nsamples-1)/fsample` instead of
`time(this)`. Behaviour is identical when `timeOnset == 0` (continuous
data, or epochs with no baseline); the spurious shift is removed otherwise.
```

---

## 4 — spm_eeg_downsample (stored sampling rate)

**Branch:** `fix/meeg-downsample-fsample`
**Open PR:** https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/meeg-downsample-fsample?expand=1

### Issue title
`spm_eeg_downsample: output stamped with requested rather than achieved sampling rate`

### Issue body
```markdown
**Summary.** `spm_eeg_downsample` computes the achieved output rate
(lines ~52-58) and prints it as "Resampling frequency", but then stamps the
output object with the *requested* rate:

```matlab
fsample_new = (nsamples_new/D.nsamples)*D.fsample;   % achieved (printed)
...
Dnew = fsample(Dnew, S.fsample_new);                 % requested (stored)
```

`ft_preproc_resample` with the downsample/decimate methods uses a rounded
integer factor, so for non-integer ratios the achieved rate differs from
the request and the stored rate is wrong.

**Expected vs actual.** Requesting 1000 Hz -> 180 Hz: the data are actually
at ~166.7 Hz (factor round(1000/180) = 6) and the on-screen report says so,
but the file is labelled 180 Hz. All downstream time axes, latencies and
filter cutoffs derived from the stored rate are then silently ~8% wrong.
Integer ratios (e.g. 1000 -> 200) are unaffected.

**Reproduction** (any 1000 Hz dataset):

```matlab
S    = struct('D', D, 'fsample_new', 180);
Dnew = spm_eeg_downsample(S);
fsample(Dnew)                                   % 180 (stored)
nsamples(Dnew)/nsamples(D)*fsample(D)           % ~166.67 (actual)
```

**Environment:** platform-independent; present in current `main`.
```

### PR title
`Stamp downsampled dataset with achieved, not requested, sampling rate`

### PR body
```markdown
Fixes #NNN.

`spm_eeg_downsample` stored `S.fsample_new` (the requested rate) on the
output object, but `ft_preproc_resample` rounds the decimation factor, so
the achieved rate — already computed as `fsample_new` and used for the
on-screen report — can differ. For non-integer ratios the stored rate was
silently wrong (e.g. requested 180 Hz, actual ~166.7 Hz), biasing all
downstream latencies and filters. This stores the computed `fsample_new`
so the stamped rate matches the data.
```

---

## 5 — spm_design_contrasts (modulator padding)

**Branch:** `fix/design-contrasts-nbases`
**Open PR:** https://github.com/spm/spm/compare/main...cindykrafft:spm:fix/design-contrasts-nbases?expand=1

### Issue title
`spm_design_contrasts: parametric-modulation padding ignores basis-function expansion`

### Issue body
```markdown
**Summary.** When expanding automatic factorial contrasts,
`spm_design_contrasts.m` (line ~63) pads each condition block for
parametric modulators with

```matlab
block = [block, zeros(nr, sum([SPM.Sess(1).U(cc).P.h]))];
```

But in the design matrix every `U.u` column — the main regressor *and* each
parametric-modulation column — is convolved with all `nbases` basis
functions (see `spm_Volterra`), so a condition occupies
`(1 + sum(h)) * nbases` columns. Padding only `sum(h)` columns under-pads by
`sum(h)*(nbases-1)` per modulated condition, sliding all subsequent
conditions' contrast weights onto the wrong regressors. The final zero-pad
to design width hides the mismatch, so no error is raised.

**Expected vs actual.** 2 conditions, canonical HRF + temporal derivative
(`nbases = 2`), one linear modulator on condition 1: the design columns are
`[c1·bf1 c1·bf2 mod·bf1 mod·bf2 c2·bf1 c2·bf2]`. The auto-generated main
effect contrast is expected to weight `c2·bf1/c2·bf2`; it actually weights
`mod·bf2/c2·bf1`. The resulting F/T maps are silently wrong.

**Reproduction:** specify a factorial first-level design (`SPM.factor` set)
with time derivatives and a parametric modulator, run
`con = spm_design_contrasts(SPM)`, and compare the nonzero columns of
`con(2).c` against `SPM.xX.name`.

**Triggered when** `nbases > 1` (derivatives/FIR/Fourier) *and* parametric
modulators are present, in the automatic contrasts created when
`SPM.factor` is set. No effect when `nbases == 1` or without modulators.

**Environment:** platform-independent; present in current `main`.
```

### PR title
`Account for basis functions when padding parametric-modulation columns`

### PR body
```markdown
Fixes #NNN.

`spm_design_contrasts` padded automatic factorial contrasts with `sum(h)`
zero columns for parametric modulators, but each modulator column is
convolved with all `nbases` basis functions in the design, so a condition
spans `(1+sum(h))*nbases` columns. The under-padding shifted subsequent
conditions' weights onto the wrong regressors whenever `nbases > 1` and
modulators were present, producing silently wrong F/T maps (the trailing
zero-pad hid the mismatch).

This multiplies the modulation pad width by `nbases`. No change when
`nbases == 1` or when there are no parametric modulators.
```

---

## Pre-flight checklist

1. **Search existing issues first** (CONTRIBUTING asks this): try
   `ECdensity`, `badsamples`, `downsample`, `nlsi_GN`, `design_contrasts`
   at https://github.com/spm/spm/issues?q=
2. **Run a MATLAB regression before submitting.** Fix 1 has been
   machine-verified (its assertions executed against both code versions;
   12/23 fail pre-fix, 0/23 post-fix), but only in GNU Octave — run
   `runtests('tests/test_spm_ECdensity.m')` once in real MATLAB. Fixes 2-5
   were verified by code tracing and offline numerics, not executed in
   MATLAB; ideally run `spm_tests` (or at least exercise the touched
   functions) before opening those PRs, and say in each PR what testing was
   done — maintainers value that honesty.
3. **Submit in impact order** if you stagger them: 1 (ECdensity, has the
   test), 3 (badsamples), 4 (downsample), 2 (nlsi_GN), 5 (design_contrasts).
4. After opening each issue, put its number into the PR body's `Fixes #NNN`.
5. The branches are single-commit and based on `spm/spm@530ec52`; if
   upstream `main` has moved and a PR shows conflicts, rebase that branch
   (`git pull --rebase upstream main` on your clone) — the diffs are tiny
   and should rebase cleanly.
6. Optional context for maintainers: these came out of a systematic
   correctness audit; mention that in the first issue if you like, and be
   transparent about AI assistance if you consider it relevant — several
   projects appreciate knowing.
```
