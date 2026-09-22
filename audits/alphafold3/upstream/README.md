# Filing kit: AlphaFold 3

Fork: https://github.com/cindykrafft/alphafold3 (base `main`; all branches made on c0f97ed,
2026-08-19; all still merge cleanly into `main` a66cc52, 2026-09-21, checked with
`git merge-tree --write-tree` on 2026-09-22).

## Order

1. Sign the Google CLA.
2. AF1: issue `issue-af1-to-json-chain-order.md`, then PR 1 from `pr-bodies.md`
   (`fix/to-json-preserves-chain-order`, two commits: fix 42ca328, test 58c198f).
3. AF2: read the reply on #150 first (helper transcript "Mytochondria thread af3 150"; the
   question there predates `chain_ids` and asks exactly what this field was added to answer),
   then issue `issue-af2-summary-confidences-chain-ids.md` and PR 2
   (`fix/summary-confidences-chain-ids`, 07505f9).
4. Everything else waits for a reply.

Prior-report search, 2026-09-22, from the session (GitHub search over the repository) and a
helper session that searched all thirteen unfiled findings against every open and closed issue
and PR (artifact "Mytochondria prior af3"): **no finding has been reported before.** Two have a
related thread: AF2 and PR #678 (closed without merge: a request to key the chain scores in
`summary_confidences.json` by chain id because cross-referencing `token_chain_ids` is
error-prone; `chain_ids` was presumably the answer), AF13 and #557 (a user could not reconcile
the documented RNA Z-value with the database size; the maintainer said it is in megabases).
Adjacent to AF1: #476 (maintainer: the token order follows the `sequences` field) and #150
(maintainer: the chain-level arrays follow the input JSON order), which is the promise that a
reordered `_data.json` breaks. Adjacent to AF4: PR #719 (open; float32 overflow in the same
paired-MSA ranking, a different defect). #150, #678 and #476 are being transcribed by helpers
("Mytochondria thread af3 150", "Mytochondria threads af3 678 476"); the issue texts do not cite
them yet and may once they have been read in full (`audits/TRIAGE.md`, "Read the whole thread
first").

## All fifteen branches

Grades follow `audits/TRIAGE.md`: "file now" changes a number or file users read under ordinary
settings on the current release; "held" is a crash, a rare path, a latent table or docs.

| id | branch | finding (from the commit message) | file | grade | why held / notes |
|---|---|---|---|---|---|
| — | `fix/ccd-user-ccd-copy` | user CCD mutated the memoised base CCD dict; one input's overrides leaked into every later input | `constants/chemical_components.py` | **filed** | PR #734; fixed upstream as 3485995 with credit |
| AF1 | `fix/to-json-preserves-chain-order` | `to_json` reorders interleaved identical chains; `_data.json` round trip changes the complex | `common/folding_input.py` (+ test) | **file now** | kit ready |
| AF2 | `fix/summary-confidences-chain-ids` | `chain_ids` one per token, docs say per chain; 150 vs 2 on shipped output | `model/confidence_types.py` | **file now** | kit ready |
| AF3 | `fix/cross-attention-key-mask` | cross-attention bias multiplies the two mask terms instead of adding, so padded keys are never masked; 98 of 128 key slots are padding on a 5-residue peptide and take 0.76 of the softmax mass; runs at every diffusion step | `model/network/diffusion_transformer.py` | held (issue first, not a PR) | changes model behaviour; the released weights were trained with this code path, so a fix may move predictions in either direction. Report as an issue with the numbers and let the maintainers decide; no PR |
| AF4 | `fix/msa-pairing-stable-sort` | species grouping uses an unstable `argsort`, so the per-species crop keeps arbitrary homologs and pairs rows the docstring says not to pair; 2853 of 2995 chain-A rows paired differently on an 8000/3000-row heteromer | `model/msa_pairing.py` | held (issue first) | same training-time consistency question as AF3; one upstream commit since base touches the file, re-check before filing |
| AF5 | `fix/per-chain-template-cache-key` | template features cached per sequence, so a second chain with the same sequence but different templates silently reuses the first chain's templates | `model/features.py` | held | non-default input (same sequence, different templates) |
| AF6 | `fix/mse-residue-key-lookup` | `fix_mse_residues` masks by residue position where keys are meant, so selenomethionine SE atoms survive under the wrong residue and the residue loses its SD atom | `structure/parsing.py` | held | user-supplied template mmCIFs / `from_mmcif` only; needs an mmCIF whose `_atom_site` chain order differs from the scheme tables to show |
| AF7 | `fix/template-hit-keep-alignment-error` | `Hit.keep`'s `is_valid` check sits outside the `try` that is meant to catch `AlignmentError`, so one bad hit aborts template featurisation for the input | `data/templates.py` | held | crash path; needs a template whose structure sequence is longer than its seqres |
| AF8 | `fix/ref-max-modified-date-none` | `ref_max_modified_date=None` (the library default) raises `TypeError` when a component's ideal coordinates contain `?` | `model/features.py` | held | library callers only; the CLI always passes a date |
| AF9 | `fix/params-bin-shard-regex` | stray `]` in the pattern for uncompressed split parameters: `model.bin.0, .1, ...` match nothing, "No models matched" | `model/params.py` | held | rare layout (uncompressed shards); one-character fix, cheap to file after a reply |
| AF10 | `fix/ligand-bond-hydrogen-filter` | ligand bonds to atoms whose *name* starts with H are dropped as "hydrogen", which also drops HG (mercury), HF, HO; a `C[Hg]Cl` ligand loses both bonds; the hydrogen filter is redundant by then | `model/features.py` | held | rare elements |
| AF11 | `fix/arginine-hh22-rename` | `FixArginine` renames a lone HH22 to HH21 (the other pair's name) instead of HH12 | `structure/cpp/mmcif_utils_pybind.cc` | held | C++; hydrogens are dropped from the flat atom layout so the effect is on written names only |
| AF12 | `fix/nucleic-rigidgroup-dense-atom-idx` | DNA rows of `RESTYPE_RIGIDGROUP_DENSE_ATOM_IDX` resolved against RNA adenosine select the base nitrogen instead of C1' | `model/protein_data_processing.py` | held | not reachable today (template aatypes are protein only) |
| AF13 | `docs/performance-rna-z-value-and-continuation` | docs ask for the RNA `-Z` as a base count where nhmmer takes megabases (the example is already in megabases); missing `\` in the example | `docs/performance.md` | held (docs) | cheap; file after a reply as the maintainers welcome doc patches |

## Thread log

- 2026-09-22: PR #734 read in full (two comments: CLA bot; Augustin-Zidek's close with the
  commit reference). Nothing to answer.
- 2026-09-22: #150 transcription requested (helper); to be read before AF2 is posted.
