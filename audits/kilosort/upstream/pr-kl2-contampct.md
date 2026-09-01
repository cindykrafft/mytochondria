# PR: Report unevaluable clusters as fully contaminated, not ContamPct 0

**Target:** `MouseLand/Kilosort`, base `main`
**Head branch:** `fix/refract-contam-default` (patch: `0001-Report-unevaluable-clusters-not-fully-contaminated-no.patch` — actual filename `0001-Report-unevaluable-clusters-as-fully-contaminated-no.patch`)
**Fixes:** the KL2 issue (file it first; reference its number here)

## Title

```
Report unevaluable clusters as fully contaminated, not ContamPct 0
```

## Body

```markdown
Fixes #<issue-number>.

`CCG.refract` initialized `R12` (est_contam_rate) to zeros and only computed
it for clusters with more than 10 spikes and a nonzero time span, so such
clusters were exported by `io.save_to_phy` with ContamPct = 0.0 — the best
possible score. Downstream selections of the form "ContamPct < x" without a
minimum-spike-count criterion silently admit every such cluster.

This PR initializes `R12` to ones so unevaluable clusters export as
ContamPct = 100, matching the Kilosort 2.5/3 convention (`set_cutoff.m`
defaulted `est_contam_rate` to 1). `is_refractory` is unchanged (these
clusters were already labeled `mua`).

Verification on 4.1.7 + this patch: a 5000-spike uniform-Poisson unit
exports ContamPct 93.9 (unchanged), an 8-spike junk cluster exports 100.0
(previously 0.0). If you would rather export NaN for "not evaluated", I am
happy to change the default — the important part is that it not be 0.
```

---

*After pasting, append the PR attribution footer required by your workflow.*
