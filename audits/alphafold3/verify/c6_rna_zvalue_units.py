"""C6: docs/performance.md states the RNA Z-value in bases; nhmmer's -Z is megabases.

docs/performance.md:118-120 says:

    Save the total number of sequences in the protein databases, and the total
    number of nucleic bases in the RNA databases - these will be needed later as
    a flag to Jackhmmer/Nhmmer to correctly scale e-values across all shards.

That is right for Jackhmmer (-Z is a count of comparisons) and wrong for Nhmmer,
whose -Z is in MEGABASES. The example values further down the same page are
already megabase-scale (--rna_central_z_value=13271.415730 for a ~13.3 Gb
database), so the prose and the example disagree by a factor of 1e6. A user who
follows the prose passes a Z that is 1e6 too large; E-values scale linearly with
Z, so hits fail the inclusion threshold and the RNA MSA is silently truncated.

Runs the real nhmmer if it is on PATH. Usage: python c6_rna_zvalue_units.py
"""
import os, re, shutil, subprocess, tempfile

nhmmer = shutil.which('nhmmer')
if not nhmmer:
    raise SystemExit('nhmmer not on PATH; install HMMER to run this check')

help_txt = subprocess.run([nhmmer, '-h'], capture_output=True, text=True).stdout
for line in help_txt.splitlines():
    if line.strip().startswith('-Z '):
        print('nhmmer   ', line.strip())
jackhmmer = shutil.which('jackhmmer')
if jackhmmer:
    for line in subprocess.run([jackhmmer, '-h'], capture_output=True, text=True).stdout.splitlines():
        if line.strip().startswith('-Z '):
            print('jackhmmer', line.strip())

# A query and a target database with one true homolog plus decoys.
QUERY = ('>query\n'
         'GGCUACGUAGCUAGCUAGGCUAAGCUAGCUAGCUUAGCUAGGCAUCGAUCGUAGCUAGCUA\n'
         'GCUAGCUAGGCUAGCUAGCUAGCAUCGAUCGAUCGUAGCUAGCUAGCUAGCUAGGCUAGCU\n')
HOMOLOG = ('GGCUACGUAGCUAGCUAGGCUAAGCUAGCUAGCUUAGCUAGGCAUCGAUCGUAGCUAGCUA'
           'GCUAGCUAGGCUAGCUAGCUAGCAUCGAUCGAUCGUAGCUAGCUAGCUAGCUAGGCUAGCA')

with tempfile.TemporaryDirectory() as d:
    q = os.path.join(d, 'q.fasta')
    t = os.path.join(d, 'db.fasta')
    open(q, 'w').write(QUERY)
    with open(t, 'w') as fh:
        fh.write('>true_homolog\n%s\n' % HOMOLOG)
        import random
        random.seed(0)
        for i in range(200):
            fh.write('>decoy%d\n%s\n' % (i, ''.join(random.choice('ACGU') for _ in range(120))))

    db_megabases = (os.path.getsize(t) / 1e6)
    print('\ntarget database size: %.6f Mb  (= %d bases, roughly)'
          % (db_megabases, int(db_megabases * 1e6)))

    def run(z, evalue='1e-3'):
        """Returns (hit count kept, best E-value reported)."""
        tbl = os.path.join(d, 'out.tbl')
        aln = os.path.join(d, 'out.sto')
        cmd = [nhmmer, '--noali', '-A', aln, '--tblout', tbl,
               '-E', evalue, '--cpu', '1']
        if z is not None:
            cmd += ['-Z', str(z)]
        cmd += [q, t]
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        rows = [l.split() for l in open(tbl) if not l.startswith('#') and l.strip()]
        best = min((float(r[12]) for r in rows), default=float('inf'))
        return len(rows), best

    correct = db_megabases                 # what the doc example values use
    as_documented = db_megabases * 1e6     # what the doc prose tells you to compute

    n_ok, e_ok = run(correct)
    n_bad, e_bad = run(as_documented)
    print('\n%-46s %s' % ('-Z given in megabases (the doc example):',
                          'best E-value %.3g, %d hit(s) kept at -E 1e-3' % (e_ok, n_ok)))
    print('%-46s %s' % ('-Z given in bases (the doc prose):',
                        'best E-value %.3g, %d hit(s) kept at -E 1e-3' % (e_bad, n_bad)))
    print('\nE-values inflated by a factor of %.3g purely from the unit.'
          % (e_bad / e_ok))

    # The inflation only costs you sequences once it crosses the threshold, which
    # is where a real RNA search sits: most homologs are far weaker than this one.
    for thr in ('1e-3', '1e-9', '1e-15'):
        n_ok, _ = run(correct, thr)
        n_bad, _ = run(as_documented, thr)
        print('  at -E %-6s  megabases keeps %d, bases keeps %d' % (thr, n_ok, n_bad))
