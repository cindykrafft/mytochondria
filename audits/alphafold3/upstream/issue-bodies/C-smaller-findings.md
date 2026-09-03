# Smaller findings — file individually or as one "minor issues" report

Six items, each small and self-contained. They are grouped here only to keep the tracker
tidy; splitting them into separate issues is fine if you prefer.

---

## C1 · `bias_init=1.0` is silently ignored on all five gating projections

`modules.py:125, 193, 310` and `diffusion_transformer.py:175, 326` pass `bias_init=1.0` to
`hm.Linear`, whose `use_bias` defaults to `False` and which reads `bias_init` only when it
is `True`. No bias parameter is created. AlphaFold 2 created exactly such a gating bias
initialised to 1.0 (`gating_b`, `hk.initializers.Constant(1.0)`), so this reads as intent
carried over and dropped.

At inference it is a no-op **provided** the checkpoint contains no `.../gating_query/bias`
entries — Haiku silently ignores extra parameters, so any that do exist are being dropped.
I could not check, as the weights are not publicly redistributable. For retraining, gates
initialise at `sigmoid(0) = 0.5` rather than `sigmoid(1) ≈ 0.73`. Either pass
`use_bias=True` alongside `bias_init`, or delete the dead argument.

## C2 · `_MultiFileIO.seek(..., SEEK_END)` has the wrong sign and can hang a read

`model/params.py:135-168` computes `pos = self._length - pos` where `io.RawIOBase`
requires `length + offset`:

```
seek(0,SEEK_END): tell()= 20  correct=20
seek(-5,SEEK_END): tell()= 25  correct=15
seek(3,SEEK_END):  tell()= 17  correct=23
```

`seek(0, SEEK_END)` is accidentally correct, which is why the class works today. If such a
seek lands past `_length`, the sub-file read returns zero bytes, `count` stays 0, `_abspos`
never reaches `_length`, and `while mem:` never terminates — a hang rather than an
exception (a subsequent `read(5)` was killed at a 25 s timeout). I could not show that the
current load path issues a non-zero `SEEK_END` seek, so this is latent; it is still a
contract violation in a public file-like object whose failure mode is silent.
Fix: `pos = self._length + pos`, and break out of `readinto`'s loop when `count == 0`.

## C3 · `seen_entities` is never populated in `MSA.compute_features`

`model/features.py:439, 485-488`. The dict is initialised and read but written only in
`Templates.compute_features` (`:814`), so the lookup never hits and every chain gets
`entity_id = 1`. Latent: `feats['entity_id']` is not copied into `cropped_chain`
(`:585-590`), `msa_pairing` never reads it, and the token-level `entity_id` the network
sees comes from the independent and correct `_compute_asym_entity_and_sym_id`
(`:128-168`). Worth deleting or completing, since it sits beside correct code doing the
same job.

## C4 · Alt-loc resolution groups by consecutive runs rather than identity

`structure/cpp/mmcif_altlocs.cc:105-174, 184-206` groups by consecutive runs of atom name
and comp id. Two measured consequences: a non-interleaved file (all of conformer A, then
all of conformer B) keeps **both** conformers — 12 atoms where 6 are expected — and
atom-interleaved microheterogeneity collapses a residue to a single atom. Files in the wild
are usually interleaved per atom, which is the case the run-grouping was written for, so
this is a robustness gap rather than an everyday defect.

## C5 · Per-residue pLDDT rows merge for branched ligand chains in the output mmCIF

`model/mmcif_metadata.py:200-206` groups `_ma_qa_metric_local` rows by
`(label_asym_id, label_seq_id, label_comp_id)`. Non-polymer chains carry
`label_seq_id = '.'`, so two residues of a branched or glycan chain sharing a component id
collapse into one averaged row: `NAG(90) + NAG(10)` became a single row
`('B', '.', 'NAG', '50.00')`. Adding `auth_seq_id` (and the insertion code) to the key
separates them. Happy to send a patch if useful.

## C6 · `docs/output.md` understates the pTM floor for short chains

The docs state pTM is below 0.05 for chains shorter than 20 tokens. The implemented formula
clips `d0` at `N = 19`, giving `d0 = 0.168 Å`, so the TM term for the lowest PAE bin is
0.312 and a confident short peptide can reach pTM of roughly 0.15 to 0.31. The computation
matches the paper; only the documented bound is off.

---

_Investigated with AI assistance (Claude Code), disclosed per CONTRIBUTING.md. Every number
above is real program output that I reviewed and executed._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
