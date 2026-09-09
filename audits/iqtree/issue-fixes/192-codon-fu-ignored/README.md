# iqtree/iqtree3 #192 — `+FU{...}` silently ignored for GY-type codon models

Second issue-fix for IQ-TREE 3 (after #203 / PR #207, merged 2026-09-08). **Filed as PR #210 on 2026-09-08; merged 2026-09-09 without discussion, closing #192.** Chosen because it is a
silent wrong-number regression (2.4.0 correct, 3.1.x wrong) reported with a complete table by the
maintainer of another phylogenetics package, open since 2026-07-23 with one unread comment.

## Cause

`model/modelcodon.cpp`, `ModelCodon::init`: after `initCodon()` returns the model's default
frequency type, the code did

    if (freq == FREQ_USER_DEFINED && def_freq != FREQ_USER_DEFINED) // mechanistic model
        freq = def_freq;

`initGY94()` returns `FREQ_EMPIRICAL`, so a `GY{...}+FU{61 values}` request became `GY+F`: the
values were never read (`readStateFreq` is skipped), the report says `GY+F` with 60 free
parameters, and any `+FU` vector gives the same likelihood. The MG family (`initMG94`) needs the
fallback: its frequencies are nucleotide-targeted (`CF_TARGET_NT`) and `+FU` is converted to
`F3X4` there.

## Fix

Branch `fix/issue-192-codon-fu` on `cindykrafft/iqtree3` (one commit, `21ab74e7`, on upstream master `2bbced9a`): the
override applies only when `codon_freq_style == CF_TARGET_NT`. GY-type models then keep
`FREQ_USER_DEFINED`, `readStateFreq(freq_params)` runs and `ModelMarkov::init` reports `+FU`
with no free frequency parameters. MG models are unchanged.

## Verification (`repro.sh`, `repro.before.out`, `repro.after.out`)

4 taxa × 60 codons (`codon.fa`, synthetic), fixed tree (`codon.tree`), `-blfix`, `GY{0.8,1.07}`:

| model | master | branch |
|---|---|---|
| `+FU{skew}` (`codon_freq.txt`) | −648.1018, `GY+F`, 60 free | −674.5579, `GY+FU`, 0 |
| `+FU{uniform}` (`codon_freq_uniform.txt`) | −648.1018, `GY+F`, 60 free | −667.8904, `GY+FU`, 0 |
| `GY+F3X4` / `GY+F` / `MG{0.8}+F3X4` | −665.0301 / −648.1018 / −661.7879 | same |

`gy94_reference_lnl.py` computes the GY94 likelihood independently (numpy, Felsenstein pruning,
IQ-TREE's rate normalisation, the 61 user values read in IQ-TREE's ACGT codon order): −674.55787
and −667.89043, i.e. the branch's values to all printed digits. The reporter's numbers (2.4.0
`GY+FU` 0 free parameters, different values for different vectors) are the same pattern.

## Test added to the PR

`test_iqtree.sh` and `test_iqtree.ps1`: a `GY+FU` run (frequencies from
`test_scripts/test_data/codon_freq.txt`) and a `GY+F3X4` control on `codon.fa`/`codon.tree`;
`expect_ans.txt` rows `codon.gy.fu.iqtree` −674.5579 and `codon.gy.f3x4.iqtree` −665.0301
(threshold 1, like the existing rows). On unmodified master the `+FU` row fails by 26.4.

## Caveats

- The one comment on #192 could not be read from the session; the fix follows the issue text.
- `expected_runtime.tsv` / `expected_memory.tsv` rows for the two new runs are the maintainers'
  to add (they added the #203 rows after merging PR #207); `verify_runtime.sh` falls back when
  a platform column is missing.
- The frequency order convention (61 sense codons in ACGT order) is unchanged by this fix and is
  what the reporter's F3X4-derived vector assumes.

## Files

| file | what |
|---|---|
| `0001-*.patch` | the commit on the branch |
| `repro.sh`, `repro.before.out`, `repro.after.out` | reproduction and outputs |
| `codon.fa`, `codon.tree`, `codon_freq.txt`, `codon_freq_uniform.txt` | the data (same files are added to the PR's test_data) |
| `gy94_reference_lnl.py` | the independent likelihood |
| `pr-body.md`, `comment.md` | PR text (title on the first line) and the issue comment (fill in the PR number) |
