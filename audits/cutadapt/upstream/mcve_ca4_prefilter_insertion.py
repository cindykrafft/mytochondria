"""Minimal reproduction for CA4: an anchored 5' adapter is not found when the
read carries it with one inserted base, although the error rate allows it.

Adapter CTGTCTCTTATACACATCT (Nextera, 19 nt); the default -e 0.1 allows one
error. The read is the adapter with a G inserted after position 3, followed by
eight A. As a regular 5' adapter (-g ADAPTER) the same read is trimmed.
"""
import subprocess, tempfile, os

adapter = "CTGTCTCTTATACACATCT"
read = adapter[:3] + "G" + adapter[3:] + "AAAAAAAA"
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{'I' * len(read)}\n")
    for spec in ("^" + adapter, adapter):
        out = subprocess.run(["cutadapt", "-g", spec, path], capture_output=True, text=True).stdout
        print(f"-g {spec:21s}: output read {out.splitlines()[-3]} (expected AAAAAAAA)")
