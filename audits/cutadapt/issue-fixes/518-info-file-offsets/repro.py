"""Reproduction for marcelm/cutadapt#518: --info-file offsets and sequences are
wrong when bases were removed from the read before adapter trimming.

Synthetic read: 5 A, 11 C, the adapter GATTACA, then 4 G (27 nt).
Adapter search is done after `-u 5` (or after 5' quality trimming with -q),
so the match is at 11..18 of the *shortened* read, but the info file slices
the *original* read at those offsets.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

READ = "AAAAACCCCCCCCCCCGATTACAGGGG"
QUAL_HIGH = "I" * len(READ)
QUAL_LOW5 = "#" * 5 + "I" * (len(READ) - 5)  # first five bases have Phred 2


def run(args, qualities):
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "in.fastq").write_text(f"@r1\n{READ}\n+\n{qualities}\n")
        subprocess.run(
            [sys.executable, "-m", "cutadapt", "-a", "GATTACA", "--info-file",
             d / "info.tsv", "-o", d / "out.fastq", *args, d / "in.fastq"],
            check=True, stdout=subprocess.DEVNULL,
        )
        return (d / "info.tsv").read_text().rstrip("\n")


def show(label, args, qualities, expected_offsets, expected_matched):
    line = run(args, qualities)
    fields = line.split("\t")
    got_offsets = (int(fields[2]), int(fields[3]))
    got_matched = fields[5]
    ok = got_offsets == expected_offsets and got_matched == expected_matched
    print(f"{label}: {' '.join(map(str, args))}")
    print(f"  info line: {line}")
    print(f"  got      offsets={got_offsets} matched={got_matched!r} before+matched+after={''.join(fields[4:7])!r}")
    print(f"  expected offsets={expected_offsets} matched={expected_matched!r} before+matched+after={READ!r}")
    print("  OK" if ok else "  WRONG")
    return ok


results = [
    show("no pre-trimming", [], QUAL_HIGH, (16, 23), "GATTACA"),
    show("-u 5 (issue 518)", ["-u", "5"], QUAL_HIGH, (16, 23), "GATTACA"),
    show("-q 20,0 (issue 518)", ["-q", "20,0"], QUAL_LOW5, (16, 23), "GATTACA"),
    show("-u 5 --revcomp", ["-u", "5", "--revcomp"], QUAL_HIGH, (16, 23), "GATTACA"),
]
print("all correct" if all(results) else "some info lines are wrong")
