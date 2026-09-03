#!/usr/bin/env python3
"""NOTE (latent, API only): PrefixComparer.__init__ (_align.pyx:628) computes
    effective_length -= reference.count('N') - reference.count('n')
i.e. it *subtracts* the lowercase-n count instead of adding it, so a reference
with lowercase n wildcards keeps them in the effective length and gets a larger
max_k. Aligner._set_reference counts both cases. Not reachable from the CLI:
SingleAdapter.__init__ upper-cases every adapter sequence first.
"""
import cutadapt
from cutadapt.align import Aligner, PrefixComparer
from cutadapt.adapters import PrefixAdapter

print("cutadapt", cutadapt.__version__)
for ref in ("ACGTACGTNN", "ACGTACGTnn", "ACGTACGTNn"):
    a = Aligner(ref, 0.25, wildcard_ref=True)
    p = PrefixComparer(ref, 0.25, wildcard_ref=True)
    print(f"reference {ref}: Aligner.effective_length={a.effective_length}  PrefixComparer.effective_length={p.effective_length} "
          f"max_k={p.max_k if hasattr(p, 'max_k') else repr(p).split('max_k=')[1].split(',')[0]}")
print("via PrefixAdapter('ACGTACGTnn', indels=False) (CLI path, upper-cased):",
      repr(PrefixAdapter("ACGTACGTnn", max_errors=0.25, indels=False).aligner))
