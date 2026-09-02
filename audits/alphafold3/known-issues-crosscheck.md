# Cross-check base: what was already known before this audit

Every finding in this audit is checked against the four lists below, captured
from the upstream repository on 2 Sep 2026 with the tree at `main` @ `c0f97eda`
("Add validation that templates is a list", 19 Aug 2026, post-v3.0.4). Anything
matching one of them is not reported as a finding.

## 1. Documented known issues (`docs/known_issues.md`)

| # | Issue | Why it is excluded |
|---|---|---|
| K1 | CUDA Capability 7.x GPUs (e.g. V100) produce clashing output (ranking score ≤ −99) unless `XLA_FLAGS` includes `--xla_disable_hlo_passes=custom-kernel-fusion-rewriter` | documented hardware/XLA numerics issue |
| K2 | Two-letter atoms (Cl, Br) in SMILES ligands mishandled between commits `f8df1c7` and `4e4023c` | historical, already fixed |
| K3 | MSA depth discrepancy vs AlphaFold Server: the Server runs sharded Jackhmmer without `--domZ`, giving a ~100× more permissive `--domE`. Behaviour is deliberately unchanged; raising `--domE` 100× locally replicates it | documented and intentional |
| K4 | Tokamax `gated_linear_unit` `NotImplementedError` on some backends | benign; Tokamax falls back |

## 2. Open issues on the tracker (12 total)

| # | Title |
|---|---|
| 732 | Feature proposal: explicit input preflight validation mode |
| 730 | Incorrect layout conversion of `ref_space_uid` in atom cross-attention |
| 714 | Internal input/output error |
| 675 | Slow featurization when running inference for same input with multiple seeds |
| 609 | AF3 runtime higher than reported for pool of proteins with 5000 tokens |
| 527 | AF3 cannot predict correct ligand isomer even using userCCD |
| 432 | Unified memory for extra large systems — rematerialization problems |
| 322 | Adding Docker image to container registry |
| 236 | RuntimeWarning: overflow encountered in reduce |
| 189 | Bond order information missing in output cif files |
| 152 | AF3 unable to predict covalent bonds between DNA and protein |
| 1 | First issue! Just want to say thank you! |

## 3. Open pull requests (already-proposed fixes)

| # | Title |
|---|---|
| 731 | docs: clarify MSA inputs used for template search |
| 728 | Validate template query indices against the sequence length |
| 721 | Document the measured effect of the JAX compilation cache |
| 719 | Avoid float32 overflow when ranking paired MSA rows |
| 718 | Add configurable worker and CPU counts for database searches |
| 679 | Refactor featurization logic and cache seed-independent inputs |

## 4. Fixed on `main` since v3.0.4 (in the tree, not yet in a tagged release)

Findings must be live at `c0f97eda`; each was checked with
`git log -S'<code>' -- <file>`. Recent fixes deliberately excluded:

`c0f97ed` templates-is-a-list validation · `97d2023` original (not modified) RNA
sequence in `fill_missing_fields` · `2546145` loading empty template maps written
by AF < 3.0.4 · `039eb59` resource leak on sharded Jackhmmer/Nhmmer error ·
`97639ff` pass all options to Jackhmmer/Nhmmer · `62a93af` glycan O1 leaving-atom
cleanup · `0d3facb` `ref_pos` deleted only after the pickle is written ·
`fd39d2c` numerical instability without a GPU · `1dc1e0a` `mask_mean` typing and
error checks · `8d283f3` `chem_comp_atoms`/`chem_comp_bonds` on `ChemCompEntry`.

## Closed bug-labelled issues consulted

Includes #663 (`z_value` not passed to Nhmmer with sharded databases), #650 (O1
dropped from non-linking glycans), #546 (phenix.refine template mmCIF), #513
(`_JACKHMMER_N_CPU` default), #492 (local vs server disagreement — the source of
K3), #471 (`_entity.` loop), #406 (glycan predictions), #163 (C-Br/C-Cl bonds —
the source of K2), #132 (first MSA sequence not the query), #97 (template-free
still searching templates), #59 (the source of K1).
