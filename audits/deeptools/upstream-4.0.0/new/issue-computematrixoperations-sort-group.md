Title: computeMatrixOperations sort cannot sort a single-BED matrix from the 4.0.0 computeMatrix unless the BED is called genes.bed

<!-- deeptools/deepTools .github/ISSUE_TEMPLATE.md checklist -->

- [x] Search whether this issue (or a similar issue) has been solved before: no prior report found (nearest: #1037 "computeMatrixOperations dataRange - additional features", #1200 "IndexError: list index out of range with computeMatrix"; #1423 is the gzipped-BED crash in the same function).
- [x] deepTools version: 4.0.0, `master` @ `4db9d816` ("4.0.0 cleanup (#1450)"), Python 3.12.3; not present in 3.5.6 / `computeMatrix_old`
- [x] Full command producing the issue: `computeMatrix reference-point -S signal.bw -R regions.bed -o m.mat.gz -a 300 -b 300 -bs 100` then `computeMatrixOperations sort -m m.mat.gz -R order.bed -o sorted.mat.gz` (script below builds the inputs)
- [x] Output printed: `The computeMatrix output is missing the 'genes' region group. It has {'regions'} but the specified regions have dict_keys(['genes']).` (exit 1)

**What happens.** The Rust `computeMatrix` names the region group of a BED file without group labels after the file stem (`src/computematrix.rs`, lines 152–160: `Path::new(bed).file_stem()`), so a matrix from `regions.bed` carries `"group_labels": ["regions"]`. `computeMatrixOperations.sortMatrix` (`pydeeptools/deeptools/computeMatrixOperations.py`, lines 698–700) still assumes what the Python `computeMatrix` wrote for a single file — `defaultGroup = "genes"` — labels the regions of the single sort file `genes`, and exits at the sanity check (line 733) because the matrix has no such group. The only way through is a BED literally named `genes.bed`. Multi-file matrices are unaffected (both sides use the file stems), and `computeMatrix_old` output (`genes`) sorts as before.

**Minimal script** (a 100-bp-step bigWig via pyBigWig, four regions in `regions.bed`, the wanted order in `order.bed`; both `computeMatrix` and `computeMatrix_old` are run for comparison):

```python
import gzip, json, os, subprocess, sys, tempfile
import pyBigWig

BIN = os.path.dirname(sys.executable)
d = tempfile.mkdtemp()
bw = os.path.join(d, "signal.bw")
b = pyBigWig.open(bw, "w")
b.addHeader([("chr1", 10000)])
b.addEntries(["chr1"] * 100, list(range(0, 10000, 100)), ends=list(range(100, 10001, 100)), values=[float(i) for i in range(100)])
b.close()
bed = os.path.join(d, "regions.bed")
with open(bed, "w") as fh:
    for name, s in [("geneA", 1000), ("geneB", 3000), ("geneC", 5000), ("geneD", 7000)]:
        fh.write("chr1\t%d\t%d\t%s\t0\t+\n" % (s, s + 500, name))
sort_bed = os.path.join(d, "order.bed")
with open(sort_bed, "w") as fh:            # the order we want: D, B, A, C
    for name, s in [("geneD", 7000), ("geneB", 3000), ("geneA", 1000), ("geneC", 5000)]:
        fh.write("chr1\t%d\t%d\t%s\t0\t+\n" % (s, s + 500, name))

def group_labels(mat):
    return json.loads(gzip.open(mat).readline().decode()[1:])["group_labels"]

def regions(mat):
    return [l.split("\t")[3] for l in gzip.open(mat).read().decode().splitlines()[1:]]

for tool in ["computeMatrix", "computeMatrix_old"]:
    mat = os.path.join(d, tool + ".mat.gz")
    subprocess.run([os.path.join(BIN, tool), "reference-point", "-S", bw, "-R", bed, "-o", mat, "-a", "300", "-b", "300", "-bs", "100", "-p", "1"],
                   check=True, capture_output=True)
    print("%-18s group_labels %-12s regions %s" % (tool, group_labels(mat), regions(mat)))
    out = os.path.join(d, tool + ".sorted.mat.gz")
    r = subprocess.run([os.path.join(BIN, "computeMatrixOperations"), "sort", "-m", mat, "-R", sort_bed, "-o", out], capture_output=True, text=True)
    if r.returncode == 0:
        print("   sort with order.bed: regions %s" % regions(out))
    else:
        print("   sort with order.bed: exit %d: %s" % (r.returncode, (r.stderr or r.stdout).strip().splitlines()[-1]))
    if tool == "computeMatrix":
        assert r.returncode == 0, "computeMatrixOperations sort cannot sort the matrix computeMatrix wrote from regions.bed"
```

**Output** (4.0.0 @ `4db9d816`):

```
computeMatrix      group_labels ['regions']  regions ['geneA', 'geneB', 'geneC', 'geneD']
   sort with order.bed: exit 1: The computeMatrix output is missing the 'genes' region group. It has {'regions'} but the specified regions have dict_keys(['genes']).
AssertionError: computeMatrixOperations sort cannot sort the matrix computeMatrix wrote from regions.bed
```

(`computeMatrix_old` on the same inputs: `group_labels ['genes']`, and the sort returns `['geneD', 'geneB', 'geneA', 'geneC']`.)

**Fix.** In `sortMatrix`, when one sort file is given and the matrix has exactly one group, use that group's label as the default group instead of the literal `genes` (five lines; the `genes` fallback stays for matrices from `computeMatrix_old`). This also lets the sort file carry a different name from the BED the matrix was built from, which it usually does. Alternatively the Rust side could keep calling a single unlabelled group `genes`, but the file-stem label is the more useful one on the heatmap. A PR with the fix and a test that sorts a Rust-`computeMatrix` matrix built from the shipped `input_computeMatrix_regions1.bed` with a reordered copy follows.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/deeptools)

---
_Generated by [Claude Code](https://claude.ai/code)_
