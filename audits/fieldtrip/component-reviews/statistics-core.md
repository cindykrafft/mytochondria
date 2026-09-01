# FieldTrip statistics core — adversarial review notes

Scope: the code paths behind the inferences the 42 cohort papers report —
`ft_statistics_montecarlo` and its helpers (`clusterstat`, `findcluster`,
`resampledesign`, the `ft_statfun_*` family), plus the connectivity and
spectral estimators the connectivity/time-frequency papers depend on.
FieldTrip `master` at commit 2e14f72 (Aug 2026). Line numbers refer to that
commit. All "[verified]" items were reproduced by running FieldTrip's own
code under GNU Octave 8.4 (`../verify/`).

Legend: **[verified]** reproduced on the shipped code; **[code-read]**
mechanism unambiguous from the source; **[design note]** intentional
behaviour worth knowing; **[exonerated]** checked and found correct.

---

## FT1 — Permutation p-values exclude ties (strict `>` / `<`) [verified]

`private/clusterstat.m` compares each observed cluster statistic with the
randomization distribution using strict inequalities (lines 414, 433/435,
447/449 for positive clusters; 494, 513/515, 527/529 for negative), and
`ft_statistics_montecarlo.m` does the same for the uncorrected and
max-statistic paths (lines 378-379, 384-385):

```matlab
prob(j) = sum(posdistribution>stat(j))/Nrand;              % numrandomization='all'
prob(j) = (sum(posdistribution>stat(j)) + 1)/(Nrand + 1);  % random subset
```

The permutation p-value is defined as the proportion of randomizations *at
least as extreme* as the observed statistic (Maris & Oostenveld 2007;
Phipson & Smyth 2010) — `>=`, not `>`. The strict form matters in two
situations:

**(a) `cfg.numrandomization = 'all'`.** The enumerated set contains the
identity permutation (`resampledesign.m` line 221-225 emits the all-zeros flip
pattern; `perms(1:N)` contains the identity), which reproduces the observed
statistic exactly. It is a tie, is excluded, and on this path no `+1` is
added — so every p-value is short by exactly `1/Nperm`, and an observed
statistic that is the most extreme of the whole enumeration is reported as
**p = 0**. Verified with `ft_statfun_depsamplesT`, 10 paired subjects
(1024 sign flips), `correctm='no'`, `tail=1`:

```
observed t = 6.294
FieldTrip prob (numrandomization=all, tail=1) = 0.000000
exact one-sided permutation p should be 1/1024 = 0.000977

weaker effect: observed t = -0.762
FieldTrip prob                          = 0.764648  (= #{T >  tobs}/1024 = 783/1024)
standard exact p = #{T >= tobs}/1024    = 0.765625  (784/1024)
```

The exhaustive test is the one FieldTrip itself recommends for small paired
designs (`resampledesign.m` lines 236-240 warn users towards `'all'` when the
requested number of randomizations approaches the number of unique
permutations), so this is the path small-N MEG/EEG studies are steered onto.

**(b) integer-valued cluster statistics.** With `cfg.clusterstatistic =
'maxsize'` ties between the observed cluster size and the largest
randomization cluster are frequent; each tie is excluded, so cluster
p-values are systematically too small.
`../verify/ft1b_cluster_ties.m` quantifies this on null data (single channel,
60 samples, 12 paired subjects, 500 randomizations, 200 datasets):

<!-- FT1B_RESULTS -->
*(simulation running at the time of this commit; numbers follow in the next
commit)*

For the default `'maxsum'` on continuous t-values, ties are measure-zero
and the two definitions agree — recorded as an exoneration in the same run.

Fix (`upstream/0001-Count-ties-...patch`): `>=`/`<=` throughout both files,
consistent with the existing `+1/(N+1)` convention for random subsets. The
strict comparisons date from the 2012 commit that introduced the `+1`
(bug 783, "smallest possible p-value should not be 0"), which addressed the
random-subset path but not the enumerated one.

Cohort exposure: 32/42 papers report Monte Carlo / permutation statistics;
one describes an exhaustive enumeration explicitly; `maxsize` is not named
by any (the default `maxsum` is unaffected for continuous statistics), and
most papers do not state the cluster statistic at all.

## FT7 — `ft_statfun_correlationT` critical value uses n−1 df [verified]

`statfun/ft_statfun_correlationT.m` line 71 sets `df = nrepl - 1`, while the
statistic (line 81) is `t = r*sqrt(n-2)/sqrt(1-r^2)`, which has n−2 degrees
of freedom. The parametric critical value that becomes the cluster-forming
threshold (and the optional parametric `prob`) is therefore computed with
one df too many — a slightly liberal threshold, worst for small samples:

```
n= 8: FieldTrip df=7 critval=2.3646 | correct df=6 critval=2.4469 | ratio 0.966
n=12: FieldTrip df=11 critval=2.2010 | correct df=10 critval=2.2281 | ratio 0.988
n=20: FieldTrip df=19 critval=2.0930 | correct df=18 critval=2.1009 | ratio 0.996
n=40: FieldTrip df=39 critval=2.0227 | correct df=38 critval=2.0244 | ratio 0.999
```

Both lines come from the same Oct 2015 "overhaul" commit (2a54f12). The
final cluster-level p is still a valid permutation p for whatever threshold
was used, so this shifts cluster *formation* (sensitivity/specificity of
which samples enter clusters) rather than invalidating the inference. Eight
cohort papers describe correlation-based cluster tests. One-line fix in
`upstream/`.

## FT11 — Phase slope index: top frequency bins contaminated, −Inf when normalized [verified]

`connectivity/ft_connectivity_psi.m`, subfunction `phaseslope` (lines 91-107,
unchanged since the file's first commit in July 2010):

```matlab
x(1:end-1,:,:,:,:) = conj(x(1:end-1,:,:,:,:)).*x(2:end,:,:,:,:);
...
y(k,:,:,:,:) = imag(nansum(x(begindx:endindx,:,:,:,:),1));  % window k-n..k+n
```

`x(1:end-1)` becomes the products `conj(C(f))·C(f+δf)`, but `x(end)` is left
as the raw coherency at the highest frequency. Every window that reaches the
top bin — the last `nbin+1` output bins — therefore adds `imag(C(fmax))` to
the PSI. Verified against the Nolte et al. (2008) definition with a 20-bin
synthetic coherency and `nbin=3`:

```
bin   FieldTrip    reference   difference   imag(C(fmax))=-0.0007
 16      0.8354      0.8354      0.0000
 17      0.5206      0.5214     -0.0007
 18      0.6281      0.6288     -0.0007
 19      0.4100      0.4107     -0.0007
 20      0.4212      0.4220     -0.0007
```

With `cfg.normalize = 'yes'` it is worse: `coh(end)` is never set (stays 0),
so `x(end)./coh(end)` is infinite and **the last `nbin+1` bins are ±Inf**:

```
normalize=yes: PSI at bins 16..20 = 0.733345 -Inf -Inf -Inf -Inf
```

Users who inspect the PSI at the top of their frequency range (or run
statistics across all bins) are affected; one cohort paper reports PSI. Fix
in `upstream/`: zero the last element after forming the products and set its
normalizer to 1, so edge windows simply contain one fewer product.

## FTR — `ft_statfun_depsamplesregrT` control-variable branch cannot run [verified]

`statfun/ft_statfun_depsamplesregrT.m` line 98 indexes
`design(cfg.cvar, unitselved)`; the variable is `unitselvec`. Any call with a
non-empty `cfg.cvar` fails:

```
without cvar: ok, stat(1)=-0.334
with cvar: ERROR -> 'unitselved' undefined near line 98, column 42
```

Loud failure (no silent damage); the feature — per-subject regression with
blocking — is simply unusable. Present since at least the July 2017 file
sync. One-character fix in `upstream/`. No cohort paper names this statfun.

## FT2 — Two-sided-without-correction warning only fires at alpha = 0.05 [code-read]

`ft_statistics_montecarlo.m` line 222:

```matlab
if strcmp(cfg.correcttail,'no') && cfg.tail==0 && cfg.alpha==0.05
  ft_warning('Doing a two-sided test without correcting p-values or alpha-level, ...')
```

With `cfg.correcttail='no'` (the default) a two-sided test evaluates each
tail at the full `cfg.alpha`, i.e. the nominal type-I rate is doubled — a
well-known FieldTrip gotcha that this warning exists to catch. But the
condition tests `alpha==0.05` literally: a user with `alpha=0.01` or `0.1` is
in exactly the same situation and gets no warning. Eleven cohort papers
describe two-sided cluster tests at 0.05 (five state 0.025 per tail
explicitly, which is the correct handling). Trivial fix in `upstream/`.

---

## Design notes (not defects, but consequential)

- **`cfg.correctm='fdr'` is Benjamini–Yekutieli, not Benjamini–Hochberg.**
  `private/fdr.m` divides the BH threshold by the harmonic sum `c(V)`
  (≈ ln V + 0.577, about 8× at V=1000), and its header says so ("of which
  the second is currently implemented"), but the `ft_statistics_montecarlo`
  help lists only `'fdr'`. Papers writing "FDR-corrected (FieldTrip)" are
  reporting a far more conservative procedure than readers assume. Ten
  cohort papers mention FDR (not necessarily FieldTrip's).
- **`cfg.correcttail` default `'no'`** — see FT2; documented, warned, and
  still the default.
- **Quality-of-life quirks in `clusterstat.m`** [code-read]: nonparametric
  thresholds index the sorted distribution with `round(alpha/2*Nrand)`,
  which is 0 (an error) for very small `Nrand`; the observed-data `'wcm'`
  branch tests `numel(postailcritval)==numel(posclusrnd)` — the *last
  randomization's* label vector rather than `posclusobs` (same length, so
  it works; undefined if `Nrand=0`).
- **`combineClusters` (mex) vs `combineClusters2` (MATLAB)** are documented
  to differ on isolated single-sample clusters (`combineClusters2.m` header);
  the mex is the default. Not reproducible here (mex not buildable under
  Octave); flagged for maintainers' awareness only.
- **`minnbchan`** counts suprathreshold neighbours using `connmat|connmat'`;
  self is excluded by `ft_prepare_neighbours` (line 434), but a
  user-supplied neighbour structure that lists a channel as its own
  neighbour would inflate the count by one.
- **Unit labels must be 1..N**: `depsamplesregrT`, `actvsblT`,
  `depsamplesFunivariate` use `max(design(uvar,:))` as the unit count and
  the bootstrap path in `resampledesign` uses `find(units==k)`; non-contiguous
  subject codes silently mis-size or error. `depsamplesT` uses `length()`
  and is robust.

## Exonerated (checked, correct)

- `resampledesign` exhaustive enumeration includes the identity permutation
  (correct; it is FT1's counting that is wrong, not the enumeration).
- `findcluster` `minnbchan` pruning iterates to a fixed point; `spm_bwlabel`
  with 6-connectivity on a 2-D freq×time slice is 4-connectivity (the
  documented FieldTrip definition).
- `combineClusters.cpp` union-find merges labels across neighbouring
  channels at the same time/frequency index in both directions.
- `ft_statfun_indepsamplesT` pooled variance; `indepsamplesF` between/within
  mean squares; `depsamplesFunivariate` error df `(N−nunits−(k−1))`.
- `ft_connectivityanalysis` averages the cross-spectrum over trials before
  `ft_connectivity_corr` (coherence is not a mean of per-trial unit-modulus
  values); jackknife path builds leave-one-out averages.
- `ft_connectivity_wpli` (incl. debiased) and `ft_connectivity_ppc` match
  Vinck et al. 2010/2011.
- `ft_inverse_lcmv`/`dics` percentage `lambda` parsing divides by 100
  (checked because the latest upstream commit touched lambda handling).
- `ft_specest_mtmfft` / `mtmconvol` `sqrt(2/N)` scaling and Frobenius taper
  normalization; last Slepian taper dropped by design.
- `ft_freqbaseline` `'db'`, `'relchange'`, per-trial normalization.
- TFCE (`tfcestat.m`, new 2026 exact implementation) was not reviewed in
  depth.
