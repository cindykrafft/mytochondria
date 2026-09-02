# AlphaFold 3 audit

AlphaFold 3 (google-deepmind/alphafold3) predicts the joint structure of proteins,
nucleic acids, ligands, ions and modified residues. This is a full-codebase adversarial
review of `main` @ [`c0f97eda`](https://github.com/google-deepmind/alphafold3/commit/c0f97eda)
("Add validation that templates is a list", 19 Aug 2026, post-v3.0.4), covering input
handling, the mmCIF and structure layer with its C++ core, the genetic-search pipeline,
templates, featurisation, the network and diffusion sampler, and the confidence metrics.

Every finding is checked against `docs/known_issues.md`, the 12 open issues, the 6 open
pull requests and everything merged to `main` since v3.0.4
([`known-issues-crosscheck.md`](known-issues-crosscheck.md)). Two defects this audit
found independently turned out to be already reported and are credited, not claimed.

## Findings

Detail with file:line citations in [`component-reviews/`](component-reviews/); runnable
reproductions in [`verify/`](verify/); patches and filing order in
[`upstream/`](upstream/).

| id | component | finding | status |
|---|---|---|---|
| **A1** | `constants/chemical_components.py` | A `userCCD` mutates the **process-global cached CCD dictionary**, so a custom component from one input stays visible to every later input in the same run and can override real CCD codes for inputs that supply none. Regression from `a8ecdb2`, the memory fix for the closed issue #509. The class docstring promises the opposite. | verified; patch validated |
| **A2** | `model/features.py` | The ligand bond filter drops bonds whose atom **name** starts with `H`. Atom names are the uppercased element plus a counter, so mercury is `HG1`: `C[Hg]Cl` reaches the network with 0 of its 2 covalent bonds. The filter is also redundant, since hydrogens are already removed by element upstream. | verified; patch validated |
| **N1** | `model/network/diffusion_transformer.py` | The cross-attention **key mask is a no-op**: the two mask terms are multiplied, not added, so no key is ever masked for a valid query and a fully padded pair gets +1e9. For a 5-residue peptide, 98 of 128 key slots are padding and take a mean 0.76 of the softmax mass. Fires below 128 heavy atoms, in the diffusion encoder and decoder at every denoising step. | verified; patch validated |
| **M1** | `model/msa_pairing.py` | The species grouping uses an **unstable `argsort`**, contradicting the docstring's promise that rows pair in their original MSA order. The per-species crop then keeps arbitrary homologs rather than the best-ranked ones: rows kept from the MSA's top 100 fall from 99 to 30, and 2853 of 2995 rows pair against a different partner than documented. | verified; one-keyword patch |
| **S1** | `structure/parsing.py` | `fix_mse_residues` indexes residues **by key as if by position**. When the `_atom_site` chain order differs from the scheme tables', selenomethionine keeps its `SE` atom inside a residue renamed `MET`, and `SE` is not an ATOM37 name, so the template loses its `SD`. On for user template mmCIFs. | verified against a local build of the C++ extension; patch validated |
| **C1** | `model/confidence_types.py` | `chain_ids` in `summary_confidences.json` is built from `token_chain_ids`, so it carries one entry per **token** where the docs and every neighbouring field are per chain: 150 entries against 2. Regression from `e68269f`. | verified; patch validated |
| **A3** | `model/features.py` | Template features are cached per **sequence entity**, so the second chain of a repeated sequence silently receives the first chain's templates. The MSA path deliberately does not do this. | verified; patch |
| **I1** | `common/folding_input.py` | `to_json` **reorders chains**, and chain order fixes token order and the asym/entity/sym ids. In the documented two-stage workflow the model sees a different layout than a single end-to-end run of the same input and seed. | verified; patch validated |
| **T1** | `data/templates.py` | `AlignmentError` **escapes the handler written to catch it**, because the `is_valid` call that triggers realignment sits outside the `try`. One un-alignable hit aborts template featurisation for the whole input instead of being skipped. | verified; patch |
| **M2/M3** | `docs/performance.md` | The RNA `-Z` value is documented in **bases**; nhmmer's `-Z` is in **megabases**, and the example values on the same page already are. Following the prose inflates E-values by 1e6 and silently shrinks the RNA MSA. The same example also drops four tuning flags through a missing line continuation. | verified with real nhmmer; patch |
| **A7** | `constants/residue_names.py` | **Selenocysteine maps to alanine**, not cysteine, while selenomethionine correctly maps to methionine and 35 of 38 cysteine-family codes map to `C`. | verified; filed as a question |
| **A4** | `model/features.py` | `ref_max_modified_date` is annotated `datetime.date` but defaults to `None` on the public `featurise_input` path, raising `TypeError` for any input with a CCD component lacking ideal coordinates. The CLI always passes a date. | verified; patch |
| **S2** | `structure/cpp/mmcif_utils_pybind.cc` | `FixArginine` renames a lone `HH22` to `HH21`, the other pair's name, producing duplicate atom names. | verified; patch |
| **A5** | `model/protein_data_processing.py` | DNA rows of the backbone-frame index table select the base nitrogen instead of `C1'`, because the indices are resolved once against RNA adenosine. Latent: the only consumer sees protein aatypes today. | verified; patch |
| **N5/I2** | `model/params.py` | A stray `]` in a regex makes uncompressed multi-part parameter files unloadable. | verified; one-character patch |

Lower-severity items (alt-loc run grouping, the `_entity_poly_seq` fallback keys, CIF
tokenizer quoting, per-residue pLDDT rows merging for branched ligands, the documented
pTM floor, an unpopulated `seen_entities`, the ignored gating `bias_init`, and a
`SEEK_END` sign error) are in the component reviews with their evidence.

## Already reported, and credited

Two findings were reproduced here and then matched to existing upstream reports, so they
are not claimed:

- The atom cross-attention encoder converts `ref_space_uid` through the wrong layout,
  destroying the same-reference-space prior — **open issue #730**. This review adds one
  detail: the shape guard in `atom_layout.convert` that would have caught it is disabled
  under `jit`, because its `isinstance(..., np.ndarray)` test is False once the example
  has been mapped through `jnp.asarray`.
- The paired-MSA rank metric overflows float32 for many-chain complexes — **open pull
  request #719** and **open issue #236**.

## What held up

Roughly 120 specific suspicions were traced to a concrete failure mode and cleared, and
they are listed at the end of each component review. The load-bearing ones: the diffusion
sampler matches the published Algorithm 18 to 1.5e-6 while rejecting two deliberately
introduced off-by-one variants; the triangle multiplicative update and starting-node
triangle attention match Algorithms 12 to 14; padding invariance holds bit-exactly across
the whole trunk; `sharded_apply` is exactly equal to the unsharded function over 126
shard/length combinations; the geometry library is correct across composition, inversion,
quaternion and SVD construction; pTM, ipTM, pLDDT, PAE and the ranking score reproduce a
float64 implementation of the published formulas and seven stored quantities from the
shipped run output exactly; sharded and unsharded jackhmmer give identical MSAs; and a
full mmCIF round trip on four wwPDB files is atom-, residue-, bond- and chain-identical.

## Cohort exposure

The intended instrument, [`af3_profile.py`](af3_profile.py), re-reads each paper's full
text from Europe PMC to determine which parts of AlphaFold 3 it used. **It cannot run in
this environment**: the egress proxy denies `www.ebi.ac.uk`, so all 842 fetches failed.

The fallback, [`af3_cohort_from_survey.py`](af3_cohort_from_survey.py), classifies the
survey's 1197 AlphaFold papers by the major version named in the evidence sentence
already stored by the survey:

| | papers |
|---|---|
| AlphaFold-using papers in the six-journal survey | 1197 |
| evidence sentence names AlphaFold 3 / AF3 / the Server | 176 |
| of those, naming the hosted AlphaFold Server | 12 |
| evidence sentence names only AlphaFold 2 | 489 |
| evidence sentence names no major version | 532 |

By journal: PNAS 122, *Nature* 38, *Science* 13, *Cell* 2, NEJM 1. By year: 2024 11,
2025 105, 2026 60. Full list in [`af3_cohort.tsv`](af3_cohort.tsv).

Read these as a **lower bound, not a census**. One sentence per paper is a far weaker
instrument than the full text: a paper that used AlphaFold 3 but whose captured sentence
does not say "3" is invisible here, and per-feature counts from a single sentence are too
sparse to be worth tabulating. Anyone re-running this from an environment with Europe PMC
access should prefer `af3_profile.py`.

Note also that the AlphaFold Server shares weights with this codebase but not its genetic
search, so the 12 Server papers are not exposed to defects in the search pipeline.

## Reading these findings fairly

Nothing here has been adjudicated by the maintainers; their reading wins. "Verified"
means the defect was reproduced by executing code — the shipped Python, a locally built
copy of the C++ extension, or the routine extracted verbatim into a harness — and not
that anyone has run the full model with released weights and watched a prediction change.
Weights are not publicly redistributable, so no end-to-end prediction was run at all.

Three findings carry a stated caveat about released weights, and it matters: where the
released checkpoint was trained with the current code, fixing the code changes what the
weights expect. N1 (cross-attention masking) and the excluded #730 both fall in that
category, and the triangle-attention bias transposition is filed as a documentation
question for exactly that reason.
