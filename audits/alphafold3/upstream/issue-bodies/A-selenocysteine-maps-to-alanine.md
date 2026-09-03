**Title:** `CCD_NAME_TO_ONE_LETTER` maps selenocysteine (SEC) to alanine rather than cysteine

---

`src/alphafold3/constants/residue_names.py:199`:

```python
    'SEB': 'S', 'SEC': 'A', 'SEG': 'A', 'SEL': 'S', 'SEM': 'S', 'SEN': 'S',
```

`CCD_NAME_TO_ONE_LETTER` feeds `structure.fix_non_standard_polymer_residues`
(`structure/structure.py:200`) and `constants/mmcif_names.py:207`, which map the one-letter
code back through `PROTEIN_COMMON_ONE_TO_THREE`. Selenocysteine therefore becomes `ALA`
wherever a non-standard polymer residue is normalised — for instance in a user-supplied
template mmCIF or through `Input.from_mmcif`.

Selenocysteine is the selenium analogue of cysteine, exactly as selenomethionine is of
methionine, and `MSE -> 'M'` is the precedent in the same table. Mapping Sec to alanine
deletes the side-chain chalcogen entirely rather than substituting the closest standard
residue, which matters for selenoproteins whose Sec is the catalytic residue (glutathione
peroxidases, thioredoxin reductases, selenoprotein P).

Following the same two hops the structure code takes:

```
code  letter   becomes  name
SEC   A        ALA      selenocysteine
CYS   C        CYS      cysteine
MSE   M        MET      selenomethionine
MET   M        MET      methionine
CSO   C        CYS      s-hydroxycysteine

cysteine-family codes (CS*/CY*/SC*): 38, mapping to {'C': 35, 'N': 1, 'G': 1, 'X': 1}
SE* codes: {'SEB': 'S', 'SEC': 'A', 'SEG': 'A', 'SEL': 'S', 'SEM': 'S', 'SEN': 'S',
            'SEP': 'S', 'SER': 'S', 'SET': 'S'}

gemmi 0.7.5 CCD-derived table:
  SEC  one_letter='U' is_standard=True kind=ResidueKind.AA
  CYS  one_letter='C' is_standard=True kind=ResidueKind.AA
  MSE  one_letter='m' is_standard=False kind=ResidueKind.AA
```

35 of the 38 cysteine-family codes in the same table map to `C`; `SEC` is the outlier.

**Is `'A'` deliberate?** If the table was generated from a source that had no entry for
Sec and fell back to a default, `'C'` looks like the intended value. If it is deliberate —
for instance to keep Sec out of the cysteine entity grouping — a comment on the line would
save the next reader the same investigation. The one-character change would be
`'SEC': 'C'`.

I could not fetch the CCD's own `mon_nstd_parent_comp_id` field to close the argument from
the primary source: RCSB, EBI and PDBj were all unreachable from the environment I ran this
in. So this is filed as a question rather than a patch.

---

_Investigated with AI assistance (Claude Code), disclosed per CONTRIBUTING.md. The output
above is real program output that I reviewed and executed._

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_016r75scPLLYccEbFkCKp3zg
