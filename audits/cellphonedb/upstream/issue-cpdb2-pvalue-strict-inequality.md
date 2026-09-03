Title: p-values count only permutations strictly greater than the observed mean, so ties are dropped and p = 0 is reported

<!-- ventolab/CellphoneDB has no issue template (no .github/ISSUE_TEMPLATE, no CONTRIBUTING.md);
     this follows the structure of a minimal complete verifiable example. -->

**Version:** 5.0.1 (PyPI wheel and `master` @ `dc8abd15`, which are byte-identical); also
reproduced on v2.1.7, v3.1.0, v4.0.0 and v5.0.0.

### What the documentation says

`docs/RESULTS-DOCUMENTATION.md` states the estimator twice, both times inclusively:

- line 62: "The P value ... is calculated on the basis of the proportion of the means that are
  **as high as or higher** than the actual mean."
- line 104: "By calculating the proportion of the means which are **equal or higher** than the
  actual mean, we obtain a p-value ..."

### What the code does

`cpdb_statistical_analysis_helper.py:537-539` compares strictly:

```python
def shuffled_greater_than_real(shuffled_mean_analysis, real_mean_analysis):
    return np.packbits(shuffled_mean_analysis.values > real_mean_analysis.values, axis=None)
```

and `build_percent_result` (line 613) divides that count by `iterations`. Permutations whose mean
**equals** the observed mean are therefore counted as evidence *for* the interaction rather than
against it, and because the observed labelling is never itself counted, the p-value has no lower
bound: `p = 0` is reported whenever no shuffle strictly exceeds the observed value.

### Minimal reproduction (no database, no RNG)

`build_percent_result` is driven directly with a hand-made null of four draws — none above the
observed mean of 2.0, three exactly equal to it, one below. The documented rule gives 3/4.

```python
import numpy as np, pandas as pd
from cellphonedb.src.core.methods import cpdb_statistical_analysis_helper as helper

IDX, COLS = ['interaction1'], ['ctA|ctB']
real_mean = pd.DataFrame([[2.0]], index=IDX, columns=COLS)
real_pct  = pd.DataFrame([[1]], index=IDX, columns=COLS)
base      = pd.DataFrame(index=IDX, columns=COLS, dtype=float)
interactions = pd.DataFrame({'multidata_1_id': [1], 'multidata_2_id': [2]}, index=IDX)
combos = np.array([['ctA', 'ctB']], dtype=object)

draws = [1.0, 2.0, 2.0, 2.0]          # 0 above, 3 exactly equal, 1 below
stats = [helper.shuffled_greater_than_real(pd.DataFrame([[d]], index=IDX, columns=COLS), real_mean)
         for d in draws]
p = helper.build_percent_result(real_mean, real_pct, stats, interactions, combos, base, '|')

print("documented p ('equal or higher') = 3/4 =", 0.75)
print("reported p                       =", float(p.iloc[0, 0]))
sig = helper.get_significant_means(real_mean, p, 0.05)
print("significant at pvalue=0.05?      =", not np.isnan(float(sig.iloc[0, 0])))
assert float(p.iloc[0, 0]) == 0.75, "expected the documented 'equal or higher' proportion"
```

**Output**

```
[ ][CORE][03/09/26-00:49:00][INFO] Building Pvalues result
documented p ('equal or higher') = 3/4 = 0.75
reported p                       = 0.0
significant at pvalue=0.05?      = True
Traceback (most recent call last):
  File "repro_cpdb2.py", line 19, in <module>
    assert float(p.iloc[0, 0]) == 0.75, "expected the documented 'equal or higher' proportion"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: expected the documented 'equal or higher' proportion
```

**Expected** p = 0.75 and not significant. **Got** p = 0.0 and significant, from a null in which
no permutation exceeded the observed value.

*What shrinking the example revealed:* the data, the database and the RNG are all irrelevant —
the whole effect lives in one comparison operator, which is why the same script reproduces it on
every release from v2.1.7 onward. It also showed that the two symptoms are separable: dropping
ties biases every p-value downward, while never counting the observed configuration is what makes
p = 0 attainable.

### How much of the null is being discarded

Ties are not a measure-zero event here: the statistic is the mean of two cluster means over a
handful of cells, so many permutations reproduce the observed value exactly. On a 9-cell fixture
(three cell types of three) the **entire** null of 9!/(3!)³ = 1680 label assignments can be
enumerated, running each one through `build_clusters`/`mean_analysis` so the arithmetic is the
package's own:

| over the 22 tested entries | value |
|---|---|
| tie mass #(mean == observed)/1680 | min 0.0006, median 0.0345, max 0.2024 |
| entries whose call at `pvalue <= 0.05` changes | **3 of 22** |

All three flips go the same way, e.g. an interaction with documented p = 0.0833 (not significant)
is reported as p = 0.0119. A 20,000-iteration run agrees with the exact strict-inequality value to
0.0040 (2 × binomial se = 0.0141) and differs from the documented value by up to 0.2038, so this
is the estimand, not Monte-Carlo noise.

On real data — the endometrium example shipped in this repository (1,949 cells, 20 cell types)
with the v5.0.0 database and documented defaults (`iterations=1000, threshold=0.1, pvalue=0.05`) —
**16,821 of the 39,444 tested entries (42.6 %) are reported as exactly p = 0**. `ktplotspy` and
`ktplots` dot plots, which this repository recommends, size points by −log10(p); those entries are
infinities.

### Related issues

#179 ("Can Minimum p-value less than 1e-3", closed), #60 ("Precision of pvalues", closed), #155
("Exact p-value output file?", open) and #24 all circle the resolution of the reported p-values,
but I could not find one that raises the strict-vs-inclusive rule or `p = 0` itself. Apologies if
this was already answered in a thread I missed.

### Suggested fix

Two independent one-line decisions, both of which change published numbers, so I have not sent a
patch:

1. `>=` instead of `>` in `shuffled_greater_than_real`, matching the documented rule;
2. reporting `(b + 1) / (iterations + 1)` rather than `b / iterations`, which is the standard
   correction for a sampled permutation test (Phipson & Smyth 2010) and removes p = 0.

One caveat if you take (1): the cluster means are float32 (`counts_preprocessor` casts to
float32 and `numpy_groupies` returns float32), so some mathematically tied permutations already
fall on either side of the comparison through ~1e-7 of rounding — on the fixture above the
exact-arithmetic tie mass has median 0.0458 against 0.0345 as the float32 comparison sees it. A
tolerance, or comparing the sums rather than the means, would make the rule deterministic.

Found in a source-level correctness audit of research software (methods and harnesses, including
the exhaustive enumeration: https://github.com/cindykrafft/research-software-audit/tree/claude/software-package-audit-ablwee/audits/cellphonedb)

---
_Generated by [Claude Code](https://claude.ai/code)_
