"""AF4: msa_pairing.create_paired_features groups rows by species with an unstable sort.

Usage: python mcve_msa_pairing_species_order.py <alphafold3 checkout>/src

Builds a two-chain heteromer whose uniprot MSAs share species, calls the real
create_paired_features() from the given checkout, and compares the result with the
pairing that _align_species() documents ("the first sequence for a species in the
first chain's MSA is aligned to the first sequence for the same species in the
second chain's MSA"), computed here independently with a stable sort.
"""
import sys

sys.path.insert(0, sys.argv[1])
import numpy as np  # noqa: E402
from alphafold3.model import msa_pairing  # noqa: E402

rng = np.random.default_rng(0)
N_A, N_B, N_SPECIES, N_RES = 8000, 3000, 400, 10
MAX_PAIRED, MAX_PER_SPECIES = 8192, 600
OFFSET = 1000


def chain(chain_id, n_rows):
  species = rng.integers(0, N_SPECIES, size=n_rows).astype(str).astype(object)
  species = np.array([f'SP{s}'.encode() for s in species], dtype=object)
  species[0] = b''  # the query row has no species
  species = species.astype('S')
  rows = np.arange(n_rows)
  return {
      'chain_id': chain_id,
      'msa_species_identifiers_all_seq': species,
      # Column 0 carries the original row index (offset so it never equals the
      # MSA pad value) so the output can be traced.
      'msa_all_seq': np.repeat(rows[:, None] + OFFSET, N_RES, axis=1).astype(np.int32),
      'deletion_matrix_all_seq': np.zeros((n_rows, N_RES), np.float32),
  }


chains = [chain('A', N_A), chain('B', N_B)]
out = msa_pairing.create_paired_features(
    chains, MAX_PAIRED, {'A', 'B'}, MAX_PER_SPECIES)
got = np.stack([c['msa_all_seq'][:, 0] for c in out], axis=1)
# padding rows take the MSA pad value; map them back to -1
pad = msa_pairing.data_constants.MSA_PAD_VALUES['msa']
got = np.where(got == pad, -1, got - OFFSET)


def groups(c, stable):
  sp = c['msa_species_identifiers_all_seq']
  idx = np.argsort(sp, kind='stable') if stable else sp.argsort()
  s, first = np.unique(sp[idx], return_index=True)
  return dict(zip(s, np.split(np.arange(len(sp))[idx], first[1:])))


# Species whose rows come out of the code's grouping in a different order from the MSA's.
g_code = groups(chains[0], stable=False)
reordered = sum(not np.all(np.diff(r) > 0) for s, r in g_code.items() if s)
print(f'numpy {np.__version__}: species_ids.argsort() (the grouping on main) puts the rows of '
      f'{reordered} of {len(g_code) - 1} chain-A species out of MSA order')

# Documented pairing: per species, i-th row of A with i-th row of B, in MSA order.
gA, gB = groups(chains[0], True), groups(chains[1], True)
documented = {}
for s in set(gA) & set(gB):
  if not s:
    continue
  n = min(len(gA[s]), len(gB[s]), MAX_PER_SPECIES)
  for a, b in zip(gA[s][:n], gB[s][:n]):
    documented[int(a)] = int(b)

pairs = [(int(a), int(b)) for a, b in got[1:] if a >= 0 and b >= 0]
differ = sum(documented.get(a) != b for a, b in pairs)
print(f'paired rows: {len(pairs)}; chain-A rows paired with a different chain-B row '
      f'than documented: {differ}')
top = sum(a < 100 for a, _ in pairs)
top_doc = sum(a < 100 for a in documented)
print(f'paired chain-A rows from the MSA top 100: {top} (documented pairing: {top_doc})')
