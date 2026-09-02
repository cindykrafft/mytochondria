# Cluster-level inference (published-design style)

`3dttest++ -Clustsim` (sign-flip randomisation of the residuals, 10,000 iterations,
NN1, bi-sided) on the SCHZ vs CONTROL contrast under each build and mask, then
`3dClusterize` at alpha = 0.05 for cluster-forming p = 0.001 and p = 0.01
(`scripts/cluster_inference.sh`, `scripts/cluster_extract.sh`).

| mask | p_thr | build | cluster-size threshold (vox) | largest cluster found (vox) | surviving |
|---|---|---|---|---|---|
| 90 %-coverage (25,227 vox) | 0.001 | before fix | 24 | 21 | none |
| | 0.001 | after fix | 24 | 20 | none |
| | 0.01 | before fix | 151 | 114 | none |
| | 0.01 | after fix | 179 | 138 | none |
| intersection (8,657 vox) | 0.001 | before fix | 14 | 0 | none |
| | 0.001 | after fix | 16 | 3 | none |
| | 0.01 | before fix | 93 | 31 | none |
| | 0.01 | after fix | 88 | 57 | none |

Nothing survives whole-brain cluster correction under either build at n = 20 + 20.
The `*_CSimA.NN1_bisided.1D` files are the full threshold tables.
