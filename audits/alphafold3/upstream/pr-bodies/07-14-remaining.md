# Remaining PR bodies (waves 2 and 3)

Same structure as the individually written ones: what is wrong, why it matters, the
reproduction with real output, the change, and what was and was not tested. Each ends with
the AI-assistance disclosure required by CONTRIBUTING.md.

---

## 07 · `fix/per-chain-template-cache-key`
**Key the template feature cache on the chain's templates, not just its sequence**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/per-chain-template-cache-key?expand=1)

`Templates.compute_features` (`model/features.py:771-782, 814-818`) computes template
features once per sequence entity and caches them, and reads
`templates_by_chain_id[chain_id]` **only** on a cache miss. Two chains with the same
sequence but different `templates` are representable — `Input` keeps them distinct,
`hash_without_id` covers the templates, and the data pipeline builds
`templates_by_chain_id` per chain — but the second such chain silently receives the first
chain's template mmCIFs, coordinates and query-to-template mapping.

The MSA path deliberately does not do this: `Msa.compute_features`
(`features.py:451-540`) uses `seen_entities` only to label `entity_id` and reads the MSAs
per chain. The comment at `features.py:819-821` ("each chains templates can't see each
other") reads as assuming the per-chain behaviour.

Executed with a tracer on the template read:

```
templates_by_chain_id actually read for chains: ['A']
  chain A -> templates ['tmplA_1', 'tmplA_2']
  chain B -> templates ['tmplA_1', 'tmplA_2']
RESULT: chain B's own templates ['tmplB_1'] were silently discarded; it received chain A's.
```

The change adds the chain's templates to the cache key. Homomers whose chains carry the
same templates still share one computation, so the common case is unaffected. Not tested
with a full prediction (weights unavailable).

---

## 08 · `fix/to-json-preserves-chain-order`
**Keep chain order stable across a to_json / from_json round trip**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/to-json-preserves-chain-order?expand=1)

`Input.to_json` (`common/folding_input.py:1487-1496`) groups chains by content across the
whole input and emits one entry per group at the position where the group first appeared.
Two identical chains separated by a different chain are therefore emitted together, and the
chain between them moves after them. `from_json` rebuilds `Input.chains` in the emitted
order, so the round trip reorders the input.

Chain order is load-bearing: `to_structure` (`:1430-1465`) lays out tokens in chain order,
and `model/features.py:146-159` assigns `asym_id`, `entity_id` and `sym_id` by first
appearance in that layout.

```
single-stage chain order : ['A', 'B', 'C']
two-stage (reload) order : ['A', 'C', 'B']
single-stage asym_id: {'A': 1, 'B': 2, 'C': 3}
two-stage   asym_id: {'A': 1, 'C': 2, 'B': 3}
```

(A homodimer with a ligand between the two copies.) `run_alphafold.py:649-658` always
writes `<name>_data.json = fold_input.to_json()`, so in the two-stage workflow documented
in `docs/performance.md` — data pipeline with `--norun_inference`, then inference from that
JSON — the model receives a different token order and different asym ids than a single
end-to-end run of the same input with the same seed.

The change merges only *consecutive* content-identical chains, so interleaved copies are
written as separate entries and the emitted order stays faithful. The upstream
`folding_input_test.py` suite gives an identical pass/fail set before and after the change
(20 failures either way in my environment, all from the CCD pickle and test data that the
repo builds by download rather than ships).

---

## 09 · `fix/template-hit-keep-alignment-error`
**Catch AlignmentError from the is_valid check in Hit.keep**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/template-hit-keep-alignment-error?expand=1)

`Hit.keep` (`data/templates.py:356-368`) wraps the `align_ratio` check in
`try/except template_realign.AlignmentError` so an un-alignable hit is skipped with a
warning. The `is_valid` check one statement above sits **outside** that `try`, and it is
what actually triggers the realignment: `is_valid` reads `query_to_hit_mapping`, whose
cached property calls `realign_hit_to_structure` whenever `full_length` differs from
`len(structure_sequence)`. `realign` raises `AlignmentError` when the structure sequence is
longer than the seqres length (`template_realign.py:74-81`).

So for a realign failure the handler can never fire; the exception escapes `keep()`,
propagates through `_filter_hits`, and aborts template featurisation for the whole input
instead of dropping one hit:

```
!!! UNCAUGHT AlignmentError escaped keep(): The Structure sequence (6) must be shorter
than the PDB seqres sequence (4)
```

The change moves both checks inside the existing `try`. Loud rather than silent, but it
turns a per-hit skip into a failed run.

---

## 10 · `docs/performance-rna-z-value-and-continuation`
**Document the RNA Z-value in megabases and fix the example's line continuation**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:docs/performance-rna-z-value-and-continuation?expand=1)

Two independent errors in the sharded-databases section of `docs/performance.md`.

The prose (`:118-120`) asks for "the total number of nucleic bases in the RNA databases".
That is right for Jackhmmer and wrong for Nhmmer. From the installed binaries:

```
nhmmer    -Z <x> : set database size (Megabases) to <x> for E-value calculations  (x>0)
jackhmmer -Z <x> : set # of comparisons done, for E-value calculation
```

`data/msa_config.py:88` documents the parameter correctly as megabases, and the example
values on the same page are already megabase-scale
(`--rna_central_z_value=13271.415730` for a database of roughly 13.3 Gb). So the prose and
the example disagree by a factor of a million, and following the prose inflates E-values by
that factor and silently shrinks the RNA MSA. With real nhmmer:

```
-Z given in megabases (the doc example):  best E-value 4.6e-36
-Z given in bases (the doc prose):        best E-value 4.6e-30   (inflated exactly 1e+06)
  at -E 1e-9   megabases keeps 2 hits, bases keeps 1
```

Separately, the `--rna_central_z_value` line of the example has no trailing `\`, so the
four flags after it (`--jackhmmer_n_cpu`, `--jackhmmer_max_parallel_shards`,
`--nhmmer_n_cpu`, `--nhmmer_max_parallel_shards`) are parsed as a separate command and
silently dropped — and the surrounding prose is about tuning exactly those. The same class
of defect was fixed in `docs/installation.md` by `8a84535`.

---

## 11 · `fix/ref-max-modified-date-none`
**Handle ref_max_modified_date=None when reading CCD reference positions**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/ref-max-modified-date-none?expand=1)

`model/features.py:1530` compares `max_modified_date < ref_max_modified_date`. The
parameter is annotated `datetime.date` (`:1507`) but is `None` all the way down the public
path: `data/featurisation.py:51` and
`model/pipeline/pipeline.py:145` (`WholePdbPipeline.Config.ref_max_modified_date`) both
default it to `None`.

```
explicit date (run_alphafold.py path) -> [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]
None (featurise_input default)        -> TypeError: '<' not supported between
                                         instances of 'datetime.date' and 'NoneType'
```

The branch is reached whenever a component's CCD ideal coordinates contain `?`, which is
what sends `get_reference` into this fallback in the first place. `run_alphafold.py` always
passes `max_template_date`, so the CLI is unaffected; library callers of the documented
`alphafold3.data.featurisation.featurise_input` are not. The change guards the comparison.

---

## 12 · `fix/arginine-hh22-rename`
**Rename a lone arginine HH22 to HH12, not HH21**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/arginine-hh22-rename?expand=1)

`structure/cpp/mmcif_utils_pybind.cc:339-342`. `FixArginine` swaps the two guanidinium
branches and, where only one of a pair is present, renames it to its partner:
`HH11 <-> HH21`, `HH12 <-> HH22`. The last branch renames a lone `HH22` to `HH21`, which
belongs to the other pair, so the residue comes out with the wrong atom name and, when an
`HH21` is also present, with two atoms called `HH21`. One-token fix (`hh21_` → `hh12_`),
verified against a local build of the extension.

---

## 13 · `fix/nucleic-rigidgroup-dense-atom-idx`
**Resolve nucleic backbone frame atoms per residue type**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/nucleic-rigidgroup-dense-atom-idx?expand=1)

`model/protein_data_processing.py:69-77` resolves `C1'`/`C3'`/`C4'` once against RNA
adenosine and writes those indices for all eight nucleic residue types. DNA rows of
`DENSE_ATOM` have no `O2'`, so everything from `C1'` onwards sits one slot earlier:

```
  DA  idx=[12, 8, 6]   -> ['N9', "C3'", "C4'"]   <-- selects the base nitrogen
  DC  idx=[12, 8, 6]   -> ['N1', "C3'", "C4'"]   <-- selects the base nitrogen
nucleic residue types with a wrong backbone frame: 4 of 8   (0 of 8 after the change)
```

The sibling `_make_restype_pseudobeta_idx` (`:100-108`) already resolves per residue type.

**This is latent today**: the table's only consumer (`template_modules.py:299-306`) is
indexed by template aatype, and `Templates.compute_features` produces protein aatypes only,
so the DNA rows are unreachable in v3.0.4. Filed because the table is shipped wrong and the
nucleic rows were clearly written to be used. Close it if you would rather leave the table
alone until something reads those rows.

---

## 14 · `fix/params-bin-shard-regex`
**Fix the pattern for uncompressed multi-part parameter files**
[open](https://github.com/google-deepmind/alphafold3/compare/main...cindykrafft:alphafold3:fix/params-bin-shard-regex?expand=1)

`model/params.py:207` reads `r'(?P<model_name>.*)\.bin]\.[0-9]+$'`. The stray `]` requires a
literal `]` after `bin`, so it is the uncompressed counterpart of `\.bin\.zst\.[0-9]+$` in
name only:

```
['af3.bin']                       -> OK   compressed=False
['af3.bin.zst.0','af3.bin.zst.1'] -> OK   compressed=True
['af3.0.bin','af3.1.bin']         -> OK   compressed=False
['af3.bin.0','af3.bin.1']         -> FileNotFoundError: No models matched
['af3.bin].0','af3.bin].1']       -> OK   compressed=False   <- the typo's actual effect
```

One character. Low impact, since the shipped parameters are a single `.bin.zst` and the
`.N.bin` layout works.

---

_All of the above were written with AI assistance (Claude Code), disclosed per
CONTRIBUTING.md. Every quoted output is real program output, reviewed and executed by me;
none of it is hallucinated. No full prediction was run against released model parameters,
which are not publicly redistributable — please say if you would like a specific input
folded to check any of these._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
