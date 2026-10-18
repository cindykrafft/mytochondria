"""X1: the minimal reproduction used in the MM1 issue: five 150-bp reads with one mismatch
1-5 bp from the 3' end. Run: python3 x1_as_issue_repro.py; minimap2 -ax sr ref.fa reads.fq"""
import random
r = random.Random(1)
ref = ''.join(r.choice('ACGT') for _ in range(20000))
open('ref.fa', 'w').write('>chr1\n' + ref + '\n')
comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
with open('reads.fq', 'w') as out:
    for d in range(1, 6):                       # one mismatch d bp from the 3' end
        s = list(ref[5000 + d * 1000:5000 + d * 1000 + 150])
        s[150 - d] = comp[s[150 - d]]
        out.write(f'@mm{d}_from_3p\n{"".join(s)}\n+\n{"I" * 150}\n')
