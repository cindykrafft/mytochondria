"""C5: unstable argsort breaks the documented within-species MSA pairing order.

model/msa_pairing.py:137 groups MSA rows by species with

    sort_idxs = species_ids.argsort()

numpy's default kind is 'quicksort' (introsort), which is NOT stable, so rows
within one species come out in arbitrary order. _align_species then documents
the opposite (msa_pairing.py:47-49):

    Within a species, MSAs are aligned based on their original order (the first
    sequence for a species in the first chain's MSA is aligned to the first
    sequence for the same species in the second chain's MSA).

and crops each species to the smallest per-chain hit count:

    row_indices = species_to_rows[species][:min_msa_size]   # :79

a3m rows arrive in ascending E-value order, so "original order" is "best hit
first". With an unstable sort the crop keeps arbitrary homologs instead of the
best ones, and pairs the wrong rows across chains.

Needs numpy only. Usage: python c5_msa_pairing_unstable_sort.py
"""
import numpy as np


def group_rows(species_ids, kind=None):
    """msa_pairing.py:134-142, verbatim apart from the sort kind."""
    row_indices = np.arange(len(species_ids))
    sort_idxs = species_ids.argsort() if kind is None else species_ids.argsort(kind=kind)
    species_ids = species_ids[sort_idxs]
    row_indices = row_indices[sort_idxs]
    species, unique_row_indices = np.unique(species_ids, return_index=True)
    grouped = np.split(row_indices, unique_row_indices[1:])
    return dict(zip(species, grouped, strict=True))


rng = np.random.default_rng(0)
n_a, n_b, n_species = 8000, 3000, 400
# Row 0 of each MSA is the query, which carries an empty species id.
sp_a = np.array([b''] + [b'UP%03d' % rng.integers(n_species) for _ in range(n_a - 1)])
sp_b = np.array([b''] + [b'UP%03d' % rng.integers(n_species) for _ in range(n_b - 1)])

for name, ids in (('chain A', sp_a), ('chain B', sp_b)):
    g = group_rows(ids)
    unordered = sum(1 for rows in g.values() if list(rows) != sorted(rows))
    print('%s: %d species, %d of them come out NOT in original MSA order'
          % (name, len(g), unordered))

fast_a, fast_b = group_rows(sp_a), group_rows(sp_b)
stable_a, stable_b = group_rows(sp_a, 'stable'), group_rows(sp_b, 'stable')

kept_fast, kept_stable, pair_diff = [], [], 0
for sp in sorted(set(fast_a) & set(fast_b)):
    if not sp:
        continue
    n = min(len(fast_a[sp]), len(fast_b[sp]))          # min_hits_per_species
    kept_fast.extend(fast_a[sp][:n])
    kept_stable.extend(stable_a[sp][:n])
    pair_diff += int((fast_a[sp][:n] != stable_a[sp][:n]).sum())

kept_fast, kept_stable = np.array(kept_fast), np.array(kept_stable)
print('\npaired rows kept for chain A: %d' % len(kept_fast))
print('median MSA rank kept, shipped (unstable) : %d' % np.median(kept_fast))
print('median MSA rank kept, stable sort        : %d' % np.median(kept_stable))
print('rows in common between the two           : %d of %d'
      % (len(set(kept_fast.tolist()) & set(kept_stable.tolist())), len(kept_fast)))
print('rows from the MSA top 100, shipped %d vs stable %d'
      % ((kept_fast < 100).sum(), (kept_stable < 100).sum()))
print('chain-A rows paired against a different chain-B row than documented: %d'
      % pair_diff)
