# Upstream filing kit

AlphaFold 3 takes issues and pull requests on GitHub at
`google-deepmind/alphafold3`, base `main`. Every patch in
[`patches/`](patches/) is a single commit on `c0f97eda` ("Add validation that templates
is a list", 19 Aug 2026, post-v3.0.4) and applies independently of the others.

```bash
git clone https://github.com/<you>/alphafold3 && cd alphafold3
for p in ../patches/0001-*.patch; do
  b=fix/$(basename "$p" .patch | sed 's/^0001-//' | cut -c1-40)
  git checkout -b "$b" c0f97eda && git am "$p" && git checkout main
done
git push -u origin --all
```

Each finding was checked against `docs/known_issues.md`, the 12 open issues, the 6 open
pull requests and the commits merged to `main` since v3.0.4; see
[`../known-issues-crosscheck.md`](../known-issues-crosscheck.md). Two findings that this
audit reproduced independently turned out to be already reported and are **not** filed:
the `ref_space_uid` layout conversion in atom cross-attention (open issue #730) and the
float32 overflow in the paired-MSA rank metric (open pull request #719, open issue #236).

## Suggested order

Highest value first, and the first three are the ones worth a maintainer's attention
today.

| # | finding | patch | note |
|---|---|---|---|
| 1 | user CCD mutates the shared cached CCD dict | `0001-Do-not-let-a-user-CCD-mutate-...` | file the issue first; it is a regression from the fix for #509 |
| 2 | ligand bonds to mercury deleted as hydrogens | `0001-Stop-dropping-ligand-bonds-...` | mention that the filter is redundant, not just wrong |
| 3 | cross-attention key mask is a no-op | `0001-Add-the-query-and-key-masks-...` | affects inputs under 128 heavy atoms; changes predictions |
| 4 | unstable species sort in MSA pairing | `0001-Group-MSA-rows-by-species-...` | ask whether the trained model expects the documented order |
| 5 | `fix_mse_residues` key/position confusion | `0001-Look-up-MSE-residues-by-key-...` | validated against a local build of the C++ extension |
| 6 | `chain_ids` per token, not per chain | `0001-Make-summary_confidences-chain_ids-...` | regression from `e68269f` |
| 7 | per-chain templates discarded for repeated sequences | `0001-Key-the-template-feature-cache-...` | |
| 8 | `to_json` reorders chains | `0001-Keep-chain-order-stable-...` | affects the documented two-stage workflow |
| 9 | `AlignmentError` escapes `Hit.keep` | `0001-Catch-AlignmentError-...` | |
| 10 | RNA Z-value units and a missing line continuation | `0001-Document-the-RNA-Z-value-...` | docs only, two independent errors in one section |
| 11 | `ref_max_modified_date=None` raises `TypeError` | `0001-Handle-ref_max_modified_date-None-...` | library entry point only |
| 12 | lone arginine `HH22` renamed to `HH21` | `0001-Rename-a-lone-arginine-...` | C++ |
| 13 | DNA backbone frames select the base nitrogen | `0001-Resolve-nucleic-backbone-frame-...` | latent today |
| 14 | uncompressed multi-part parameter files unloadable | `0001-Fix-the-pattern-for-uncompressed-...` | one character |

## Better filed as questions than patches

These are real but turn on a judgement the maintainers own, so they are written up in the
component reviews rather than patched:

- **Selenocysteine maps to alanine** (`constants/residue_names.py:199`). `SEC -> 'A'`
  against `MSE -> 'M'` for selenomethionine, and 35 of 38 cysteine-family codes mapping to
  `'C'`. One-word change, but it alters a shipped constant table, and the CCD's own parent
  field could not be fetched from the audit environment to close the argument.
- **Ending-node triangle attention uses the transposed pair bias**
  (`model/network/modules.py:222-249`). Verified numerically against SI Algorithm 15, but
  the released checkpoint was trained with this code, so predictions from released weights
  are unaffected and the right fix may be a note in the supplementary information.
- **`bias_init=1.0` ignored on all five gating projections** — whether to honour it or
  delete it depends on what the released weights contain.
- **Alt-loc run-grouping**, the **`_entity_poly_seq` fallback keys**, and the **CIF
  tokenizer's handling of quoted tokens** are robustness gaps that fail loudly or need
  awkward input; worth an issue apiece, not a patch.
- **Per-residue pLDDT rows merging for branched ligand chains**
  (`model/mmcif_metadata.py:200-206`) and the **documented pTM floor for short chains**
  (`docs/output.md`) are small and self-contained; either could carry a patch if the
  maintainers want one.
- **`seen_entities` never populated in `MSA.compute_features`** is dead-but-wrong code
  worth deleting or completing.

## Not filed

`constants/periodic_table.py:127` spells niobium `'Niobiu'`. The field is never used in
any computation.
