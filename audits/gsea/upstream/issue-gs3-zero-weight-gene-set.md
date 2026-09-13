Title: A gene set whose members all have ranking score 0 is reported with a spurious ES, NES and p-value under the weighted scoring scheme (NaN hit weight)

<!-- GSEA-MSigDB/gsea-desktop has no issue template; CONTRIBUTING.md asks for a title, a clear description and a code sample / executable test case. -->

**Summary**

Under the default `weighted` scheme (and `weighted_p2`, `weighted_p1.5`) the hit weight of a gene-set member is |score|^p / N_R with N_R the sum over the set's members present in the ranked list (`GeneSetScoringTables.Weighted`, `GeneSetScoringTables.java:118-139`). When every present member has score 0, N_R = 0 and `getHitScore` returns 0/0 = NaN. In `KSCore.calculateKSScore_all_modes` the running sum becomes NaN at the first hit (`KSCore.java:175-176`) and every later `Math.abs(ess_maxdev[g]) < Math.abs(runningScores[g])` comparison is false, so the ES that survives is the running sum just before the first hit, −(rank of the first member) / (N − N_H) (`KSCore.java:160-166`): a number that only says where the block of zero-scored genes sits in the list. The permutation null for that set is built from random sets with ordinary weights, so this ES is compared with a proper null: the set gets an NES, a nominal p (0 when the block sits low in the list), an FDR, and appears among the most significant negative sets. Nothing in the log or the report flags it; the "Infinite or NaN value(s)" warning only fires for non-finite ranking scores.

Preranked lists that assign 0 to untested genes (DESeq2/edgeR statistics with NA replaced by 0, often a third of the genome) and a gene set of tissue-specific genes that are all unexpressed produce exactly this input. Reproduced on `master` (`dc35c76`) and on the 4.4.0, 4.3.2 tags; 4.1.0 and 4.0.3 report ES = −1.0 with NES about −2.5 and p = 0 for the same set (their `KSCore` handled the NaN differently).

**Executable test case** (`mcve_gs3_zero_weight_set.sh`; 40 genes — 5 positive scores 3.0..1.0, 15 zeros, 20 negative −0.1..−2.0 — a set `ZEROS` of 12 zero-scored genes and a control set `BOTTOM` of the 5 most negative genes):

```sh
D=$(mktemp -d)
{ for i in $(seq 1 5); do printf 'p%d\t%s\n' $i $(python3 -c "print(3.0 - 0.5*($i-1))"); done
  for i in $(seq 1 15); do printf 'z%d\t0\n' $i; done
  for i in $(seq 1 20); do printf 'n%d\t%s\n' $i $(python3 -c "print(-0.1*$i)"); done; } > $D/list.rnk
{ printf 'ZEROS\tna'; for i in $(seq 1 12); do printf '\tz%d' $i; done; printf '\n'
  printf 'BOTTOM\tna\tn16\tn17\tn18\tn19\tn20\n'; } > $D/sets.gmt
for scheme in weighted classic; do
  gsea-cli.sh GSEAPreranked -rnk $D/list.rnk -gmx $D/sets.gmt -collapse No_Collapse -scoring_scheme $scheme \
      -set_min 5 -set_max 40 -nperm 1000 -rnd_seed 149 -plot_top_x 0 -make_sets false -zip_report false -gui false \
      -out $D -rpt_label $scheme > /dev/null 2>&1
  echo "$scheme:"; cat $D/$scheme.GseaPreranked.*/gsea_report_for_na_*_*.tsv | cut -f1,4,5,6,7,8,10 | grep -v '^NAME'
done
```

Expected for `ZEROS` under `weighted`: no enrichment score (P_hit is 0/0 for every member) — or, if a value has to be reported, the same as under `classic` (equal weights are the limit of |r|^p / N_R when all |r| are equal), here +0.8214 (five misses of 1/28, then twelve hits of 1/12), together with a warning that the set's score depends only on the position of its tied genes. Got on `master`:

```
weighted:
  BOTTOM	5	-1.0	-1.5571214	0.0	0.021764033	6
  ZEROS	12	-0.17857143	-0.35087985	1.0	0.9988545	36
classic:
  BOTTOM	5	-1.0	-2.620524	0.0	0.0	6
  ZEROS	12	0.8214286	3.034824	0.0	0.0	16
```

`ZEROS` is reported with ES = −5/28 = −0.1786 (the running sum after the five misses that precede its first member) and an NES, p and FDR from a null it cannot belong to, while the `classic` run of the same file gives +0.8214. Shrinking the example showed the condition is exactly "every present member has score 0": one member with a non-zero score restores the |r|-weighted computation.

On a synthetic 5,000-gene list with 1,500 zeros (30 %) and 1,000 gene-set permutations, a 40-gene all-zero set near the end of the zero block is reported as ES −0.7056, NES −2.02, p = 0.000, FDR = 0.000 — the second most negative NES of the run, after the planted bottom set — and a 20-gene all-zero set near the start of the block as ES −0.4418, NES −1.11, p = 0.285 (`verify/gs3_zero_weight_set.py`).

**Fix**

Two options; the patch implements the first:

1. In the three weighted tables, return 1 / N_H from `getHitScore` when the total weight is 0 and log a warning naming the set (equal scores, equal weights; the ES is then finite and equals the classic ES). A patch with this change and `ZeroWeightGeneSetTest` (fails on `master`, passes with the change) is ready and can follow as a pull request.
2. Exclude such sets from the run with a warning, since their ES is an artefact of the tie order either way; that would also be the natural place for a general warning about ties in the ranked list, which fgsea prints and GSEA does not.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/gsea)

---
_Generated by [Claude Code](https://claude.ai/code)_
