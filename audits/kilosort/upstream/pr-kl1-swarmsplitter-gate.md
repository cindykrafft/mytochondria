# PR: Fix disabled refractoriness gate in swarmsplitter.check_CCG

**Target:** `MouseLand/Kilosort`, base `main`
**Head branch:** `fix/swarmsplitter-ccg-guard` (patch: `0001-Fix-disabled-refractoriness-gate-in-swarmsplitter.ch.patch`)
**Fixes:** #1042

---

## Title

```
Fix disabled refractoriness gate in swarmsplitter.check_CCG
```

## Body

```markdown
Fixes #1042.

## What

`swarmsplitter.check_CCG` (since v4.1.5) contains

    K , T = compute_CCG(st1, st2, nbins = nbins, tbin = tbin)
    if len(st1) == 0 or len(st2 == 0) or T == 0:
        return False, False

`st2 == 0` is a boolean array, so `len(st2 == 0)` equals `len(st2)` and is
truthy for every non-empty spike train. The guard therefore fires on all
real inputs and `check_CCG` always returns `(False, False)`. Downstream,
`refractoriness()` can never return 1, so the refractory-CCG veto in
`swarmsplitter.split` ("never split a pair whose cross-correlogram is
refractory") has been dead code in v4.1.5–v4.1.7. Splits are currently
decided by modularity and bimodality alone, which allows oversplitting of
units whose halves remain mutually refractory (bursty, amplitude-varying,
or drifting units) — exactly the case the veto was designed to catch.
v4.0–v4.1.4 applied the veto.

There is a second problem in the same line: the guard sits *after* the
`compute_CCG` call, but `compute_CCG` raises `ValueError` on `.max()` of an
empty array, so the empty-train case the guard tests for crashes before the
guard is reached. Only the `T == 0` clause could ever usefully trigger
(presumably the motivation from the ZeroDivisionError reports, e.g. #1002).

## Fix

- correct `len(st2 == 0)` to `len(st2) == 0`;
- move the empty-train check above the `compute_CCG` call, keeping the
  `T == 0` check after it.

## Verification (kilosort 4.1.7, CPU)

A single simulated refractory neuron (3 ms refractory period, ~10 Hz,
20 min) split randomly in half — the canonical oversplit the veto should
block. Its cross-CCG metrics are `R12 = 0.0000`, `Q12 = 0.0000`
(`cross_refractory = True` under the v4.1.4 logic), yet:

    before: check_CCG(st1, st2) -> (False, False);  refractoriness -> 0  (split allowed)
    after:  check_CCG(st1, st2) -> (True,  True);   refractoriness -> 1  (never split)

Edge cases after the fix:

    check_CCG([1.0, 2.0], [])   -> (False, False)   (previously: ValueError in compute_CCG)
    check_CCG([1.0], [1.0])     -> (False, False)   (T == 0 path, unchanged)
```

---

*After pasting, append the PR attribution footer required by your workflow.*
