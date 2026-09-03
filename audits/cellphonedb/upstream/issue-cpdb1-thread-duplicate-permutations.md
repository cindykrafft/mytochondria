Title: The permutation workers draw identical shuffles, so `iterations` is effectively divided by `threads`

<!-- ventolab/CellphoneDB has no issue template; this follows the structure of a minimal
     complete verifiable example. -->

**Version:** 5.0.1 (PyPI wheel and `master` @ `dc8abd15`, byte-identical). Linux, Python 3.12,
`multiprocessing` start method `fork`.

### Summary

`shuffled_analysis` sends the iterations to a `Pool(processes=threads)`
(`cpdb_statistical_analysis_helper.py:494-506`) and each task shuffles with the **global** numpy
RNG (`shuffle_meta`, line 96: `np.random.shuffle(meta_copy['cell_type'].values)`). On a fork
platform every worker inherits the parent's RNG state at fork and then advances its own private
copy, so worker *k*'s *j*-th shuffle is the same permutation as worker *l*'s *j*-th shuffle. With
T workers the null distribution ends up containing roughly `iterations / T` distinct permutations,
each counted T times.

`threads` defaults to 4, and the tutorial notebooks pass 5 (`T1_Method1`, `T1_Method2`) and 25
(`T1_Method3`), so a user who asks for the default 1,000 iterations on 25 threads is getting a
null built from about 40 distinct label shuffles.

### Minimal reproduction

The package's own `shuffle_meta` is wrapped so that every permutation it returns is recorded, and
the analysis is then run normally. The dataset is 30 cells in three cell types of ten, i.e.
30!/(10!)³ = 5.55e12 distinct label assignments, so repeated draws cannot arise by chance.

```python
import os, glob, collections, tempfile
import numpy as np, pandas as pd
from cellphonedb.utils import db_utils
from cellphonedb.src.core.methods import cpdb_statistical_analysis_helper as helper
from cellphonedb.src.core.methods import cpdb_statistical_analysis_method

d = tempfile.mkdtemp()
open(d + "/gene_input.csv", "w").write(
    "gene_name,uniprot,hgnc_symbol,ensembl\n"
    "LIG1,P00001,LIG1,ENSG00000000001\nREC1,P00002,REC1,ENSG00000000002\n"
    "SUB1,P00003,SUB1,ENSG00000000003\nSUB2,P00004,SUB2,ENSG00000000004\n"
    "LIG2,P00005,LIG2,ENSG00000000005\n")
open(d + "/protein_input.csv", "w").write(
    "uniprot,protein_name,transmembrane,peripheral,secreted,secreted_desc,secreted_highlight,"
    "receptor,receptor_desc,integrin,other,other_desc,tags,tags_reason,tags_description\n"
    "P00001,LIG1_HUMAN,False,False,True,,True,False,,False,False,,,,\n"
    "P00002,REC1_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
    "P00003,SUB1_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
    "P00004,SUB2_HUMAN,True,False,False,,False,True,,False,False,,,,\n"
    "P00005,LIG2_HUMAN,False,False,True,,True,False,,False,False,,,,\n")
open(d + "/complex_input.csv", "w").write(
    "complex_name,uniprot_1,uniprot_2,uniprot_3,uniprot_4,transmembrane,peripheral,secreted,"
    "secreted_desc,secreted_highlight,receptor,receptor_desc,integrin,other,other_desc,pdb_id,"
    "pdb_structure,stoichiometry,comments_complex\n"
    "RECCPLX,P00003,P00004,,,True,False,False,,False,True,,False,False,,,,,\n"
    "BIGCPLX,P00002,P00003,P00004,P00005,True,False,False,,False,True,,False,False,,,,,\n")
open(d + "/interaction_input.csv", "w").write(
    "partner_a,partner_b,protein_name_a,protein_name_b,annotation_strategy,source\n"
    "P00001,P00002,LIG1_HUMAN,REC1_HUMAN,curated,test\n"
    "P00001,RECCPLX,LIG1_HUMAN,,curated,test\n")
db_utils.create_db(d)
db = glob.glob(d + "/cellphonedb_*.zip")[0]

rng = np.random.default_rng(11)
cells = ["c%02d" % i for i in range(30)]
pd.DataFrame(np.round(rng.random((5, 30)) * 4 + 0.5, 6),
             index=["ENSG0000000000%d" % i for i in (1, 2, 3, 4, 5)],
             columns=cells).rename_axis("Gene").to_csv(d + "/counts.txt", sep="\t")
pd.DataFrame({"Cell": cells, "cell_type": ["CTA"] * 10 + ["CTB"] * 10 + ["CTC"] * 10}).to_csv(
    d + "/meta.txt", sep="\t", index=False)

orig = helper.shuffle_meta                       # record what the package actually draws
def recording(m):
    out = orig(m)
    open(os.path.join(d, "perm_%d.txt" % os.getpid()), "a").write(
        "".join(s[-1] for s in out["cell_type"]) + "\n")
    return out
helper.shuffle_meta = recording

for threads in (1, 4):
    for f in [x for x in os.listdir(d) if x.startswith("perm_")]:
        os.remove(os.path.join(d, f))
    cpdb_statistical_analysis_method.call(
        cpdb_file_path=db, meta_file_path=d + "/meta.txt", counts_file_path=d + "/counts.txt",
        counts_data="ensembl", output_path=d + "/out", iterations=1000, threshold=0.1,
        threads=threads, debug_seed=-1, result_precision=3, pvalue=0.05, separator="|",
        output_suffix="t%d" % threads)
    perms = []
    for f in sorted(x for x in os.listdir(d) if x.startswith("perm_")):
        perms += open(os.path.join(d, f)).read().split()
    c = collections.Counter(perms)
    print("threads=%d: %d shuffles drawn, %d DISTINCT, multiplicities %s"
          % (threads, len(perms), len(c), sorted(collections.Counter(c.values()).items())))
```

**Output**

```
threads=1: 1000 shuffles drawn, 1000 DISTINCT, multiplicities [(1, 1000)]
threads=4: 1000 shuffles drawn, 272 DISTINCT, multiplicities [(1, 3), (2, 21), (3, 37), (4, 211)]
```

**Expected:** 1000 distinct permutations in both cases. **Got:** 272 at `threads=4`, 211 of them
drawn exactly four times. (`imap` hands out tasks dynamically, which is why the multiplicities are
not all exactly 4.) Sweeping the thread count on the same fixture: 1000 distinct at 1 thread, 504
at 2, 279 at 4, 137 at 8.

*What shrinking the example revealed:* the counts, the database and the interactions are
irrelevant — only the number of workers matters, which is what pointed at the inherited RNG state
rather than anything in the statistics. It also showed the effect disappears entirely at
`threads=1`, and (not shown here) under the `spawn` start method, where each worker seeds itself,
so results differ between operating systems as well as between thread counts.

### Consequences measured

- **The estimator has the precision of `iterations/threads` draws.** Over 20 repeats run as
  separate processes, the median per-entry standard deviation of the reported p-value is 0.01275
  at `threads=1` and 0.02764 at `threads=4`; as an effective sample size, p(1−p)/var gives **1068**
  and **270** against a nominal 1,000 iterations.
- **Repeat runs inside one session are not independent replicates.** Nothing in the parent process
  consumes the global RNG when `threads > 1`, so a second `Pool()` forks from the same state as
  the first: two analyses run back to back share 86 % of their distinct permutations
  (258 of 300), where at `threads=1` they share none. Re-running therefore does not average the
  Monte-Carlo error away.

### Suggested fix

Seed each task independently, e.g. draw a `numpy.random.SeedSequence` in `shuffled_analysis` and
either pass one child seed per iteration into `_statistical_analysis` (which already receives the
iteration number, currently unused) or seed each worker once in a `Pool(initializer=...)`. That
makes the result independent of `threads`, and would also let `debug_seed` work in parallel — the
docstring currently has to warn that it only works single-threaded
(`cpdb_statistical_analysis_method.py:59-61`), and the `threads=1` branch exists as a workaround
for issue #102.

I have not sent a patch because the choice of seeding scheme changes results for everyone and is
yours to make; happy to prepare one in whichever form you prefer.

Found in a source-level correctness audit of research software (methods and harnesses:
https://github.com/cindykrafft/research-software-audit/tree/claude/software-package-audit-ablwee/audits/cellphonedb)

---
_Generated by [Claude Code](https://claude.ai/code)_
