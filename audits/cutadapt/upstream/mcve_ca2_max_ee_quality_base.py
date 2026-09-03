"""Minimal reproduction for CA2: --max-expected-errors ignores --quality-base.

One 50-nt read whose qualities are all Phred 2 in phred+64 encoding ('B'),
i.e. 50 * 10**-0.2 = 31.5 expected errors. With --quality-base 64 and
--max-ee 1 it should be discarded; -q 20 --quality-base 64 (control) does
interpret the offset and trims the whole read.
"""
import subprocess, tempfile, os

read = "ACGT" * 12 + "AC"
qualities = chr(2 + 64) * 50
with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "read.fastq")
    with open(path, "w") as f:
        f.write(f"@r1\n{read}\n+\n{qualities}\n")
    out = subprocess.run(["cutadapt", "--max-ee", "1", "--quality-base", "64", path], capture_output=True, text=True).stdout
    print(f"--max-ee 1 --quality-base 64: {out.count('@r1')} read(s) written (expected 0: 31.5 expected errors > 1)")
    out = subprocess.run(["cutadapt", "-q", "20", "--quality-base", "64", path], capture_output=True, text=True).stdout
    print(f"-q 20 --quality-base 64 (control): read trimmed to {len(out.splitlines()[-3])} nt (expected 0: every base is below Q20)")
