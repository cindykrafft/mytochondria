"""Minimal reproduction for CA3: demultiplexing assigns a read differently with
and without the adapter index.

Two anchored 5' adapters: A = ACGTACGTACGT (12 nt) and B = ACGTACGTACA (11 nt),
-e 0.1 (one error each). The read starts with ACGTACGTACAGT: that is B exactly
(11 matches, 0 errors, alignment score 11) and A with one inserted base
(12 matches, 1 indel, alignment score 12 - 2 = 10).
"""
import subprocess, tempfile, os

read = "ACGTACGTACAGT" + "TTTTTTTTTTTTTTTTTTTT"
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{'I' * len(read)}\n")
    for extra in ([], ["--no-index"]):
        d = os.path.join(tmp, "noindex" if extra else "index")
        os.mkdir(d)
        subprocess.run(
            ["cutadapt", "--quiet", "-e", "0.1", "-g", "A=^ACGTACGTACGT", "-g", "B=^ACGTACGTACA",
             *extra, "-o", os.path.join(d, "{name}.fastq"), path],
            check=True,
        )
        assigned = [n for n in ("A", "B", "unknown") if os.path.exists(os.path.join(d, n + ".fastq")) and os.path.getsize(os.path.join(d, n + ".fastq"))]
        print(f"{'--no-index' if extra else 'default   '}: read written to {assigned}.fastq")
