# Templates

Scope: `data/templates.py`, `data/template_realign.py`, `model/network/template_modules.py`,
and the template paths of `model/features.py`. Tree: `main` @ `c0f97eda`.

---

## T1 — `AlignmentError` escapes the handler written to catch it [verified]

`data/templates.py:356-368`:

```python
    # Exclude hits with unresolved residues.
    if not self.is_valid:                 # <- forces the realignment, outside the try
      return False

    # Exclude hits with too few alignments.
    try:
      if min_align_ratio is not None and self.align_ratio <= min_align_ratio:
        return False
    except template_realign.AlignmentError as e:   # <- can never fire for realign
      logging.warning('Failed to align %s: %s', self, str(e))
      return False
```

`is_valid` (`:276-284`) reads `query_to_hit_mapping`, and that cached property
(`:201-247`) calls `template_realign.realign_hit_to_structure` whenever `full_length`
differs from `len(structure_sequence)`. Realignment raises `AlignmentError` when the
mmCIF structure sequence is longer than the seqres length
(`template_realign.py:74-81`, `max_num_gaps < 0`). Because `is_valid` sits one statement
above the `try`, that exception propagates out of `keep()`, through `_filter_hits`, and
aborts `Templates.from_hmmsearch_a3m` / `from_seq_and_a3m` for the whole input.

The `try/except` exists precisely to turn an un-alignable hit into a logged skip, and
for the realignment failure it cannot. Reproduced against the real `template_realign`
with `hmmsearch_sequence="DEFG"`, `structure_sequence="XDEFGY"`, `full_length=4`:

```
!!! UNCAUGHT AlignmentError escaped keep(): The Structure sequence (6) must be shorter
than the PDB seqres sequence (4)
!!! -> _filter_hits / whole data pipeline crashes for this query
```

The trigger is a hmmsearch hit whose mmCIF chain — read with `include_other=True,
include_missing_residues=True` in `_parse_hit_metadata` (`:814-820`) — yields a
structure sequence longer than the seqres `length:` in the hit description. Such hits
pass the earlier release-date, subsequence and min-length checks and reach `:357`.

Loud rather than silent, but it converts a per-hit skip into a failed run. The fix is to
move both checks inside the existing `try`.

## T2 — Per-chain templates are discarded for repeated sequences [verified]

Written up under [`featurisation.md` A3](featurisation.md), since the caching lives in
`model/features.py`. Two chains that share a sequence but carry different templates:
the second silently receives the first's.

---

## Exonerated

`query_to_hit_mapping` was verified 0-based and in the query-to-template direction, with
correct gap and insertion handling and the correct `+start_index` offset.
`realign_hit_to_structure` matches its own docstring example
(`{3:1, 4:2, 5:3, 6:4, 7:5, 10:6}`) and handles internal deletions; the realign path
offsets by `best_start` without double-adding `start_index`, and the `>=` tie-break never
returns the un-remapped initial mapping.

The release-date cutoff is `release_date > cutoff`, inclusive of the cutoff, and
consistent between `keep()` and the structure guard at `:744`; `query_release_date` is
`None` on the CLI path, so the filter and the structure-load cutoff agree. The
`from_hmmsearch_a3m` filter cutoff equals the constructor's `max_template_date` in the
real pipeline.

The atom37-to-dense-atom conversion (`data3.py:70-85`) gathers by the template aatype
that matches the stored coordinates, zeroes unmapped atoms, and shares the
`_encode_restype` ordering. Backbone frames and pseudo-beta construction are the standard
(N, CA, C) Gram-Schmidt frame with a CA translation, with masks applied consistently.
Empty and absent templates both yield one fully masked row, and padded rows are
zero-masked out of the distogram and unit-vector features. User-template indexing uses
`include_missing_residues=True` on both the sequence and the residue arrays, matching the
documented "count unresolved residues" convention in `docs/input.md:594-615`. Filter
truncation keeps hmmsearch's best-first order.

Neither of the two HEAD-adjacent template commits (`c0f97ed` validation that templates is
a list, `2546145` loading empty template maps written by AlphaFold < 3.0.4) overlaps
these findings.

Open pull request #728, "Validate template query indices against the sequence length",
already proposes validation of out-of-range and negative `queryIndices` in the
`ProteinChain` constructor; that ground is not claimed here.
