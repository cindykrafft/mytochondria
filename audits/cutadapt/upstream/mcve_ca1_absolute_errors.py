"""Minimal reproduction for CA1: `-e 1` with a 49-nt adapter allows no errors.

Creates one read that carries the adapter with exactly one substitution and runs
cutadapt on it with -e 1 (should be trimmed) and with -e 1.0000001 (control).
"""
import subprocess, sys, tempfile, os

adapter = "CAGATTTTCATATTATGCAGAAAATCTACTTCGCCTGATACGAGTCGGT"  # 49 nt
assert len(adapter) == 49
occurrence = adapter[:20] + "T" + adapter[21:]  # one substitution (A -> T at position 20)
read = "GGGG" + occurrence + "GGGG"
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{'I' * len(read)}\n")
    for e in ("1", "1.0000001"):
        out = subprocess.run(
            ["cutadapt", "-e", e, "-a", adapter, path], capture_output=True, text=True
        ).stdout
        trimmed = out.splitlines()[-3]
        print(f"-e {e}: output read {trimmed} ({len(trimmed)} nt; expected 4 nt 'GGGG')")
