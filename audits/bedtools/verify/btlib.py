"""Shared helpers for the BEDTools harnesses: run the binary, write BED files,
and independent pure-Python interval arithmetic (no pybedtools, no bedtools code).

The binary under test is taken from the BT environment variable (default: the
master build in the session scratchpad)."""
import os
import random
import subprocess
import sys
import tempfile

SCRATCH = "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/bedtools"
BT = os.environ.get("BT", os.path.join(SCRATCH, "src", "bin", "bedtools"))


def version():
    return subprocess.run([BT, "--version"], capture_output=True, text=True).stdout.strip()


def run(args, stdin=None, check=True):
    r = subprocess.run([BT, *args], input=stdin, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("bedtools %s failed (%d): %s" % (" ".join(args), r.returncode, r.stderr.strip()[-500:]))
    return r.stdout


def run_full(args, stdin=None):
    r = subprocess.run([BT, *args], input=stdin, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def lines(out):
    return [l.split("\t") for l in out.splitlines() if l and not l.startswith("#")]


def write(path, rows):
    with open(path, "w") as f:
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")
    return path


def bed12(chrom, start, blocks, name="r", strand="+"):
    """BED12 record from a list of (blockStart, blockSize) relative to start."""
    end = start + blocks[-1][0] + blocks[-1][1]
    sizes = ",".join(str(s) for _, s in blocks)
    starts = ",".join(str(o) for o, _ in blocks)
    return [chrom, start, end, name, 0, strand, start, end, 0, len(blocks), sizes, starts]


def rand_blocks(rng, nblocks, minsize=5, maxsize=60, mingap=10, maxgap=300):
    blocks, off = [], 0
    for i in range(nblocks):
        size = rng.randint(minsize, maxsize)
        blocks.append((off, size))
        off += size + rng.randint(mingap, maxgap)
    return blocks


def overlap(a0, a1, b0, b1):
    return max(0, min(a1, b1) - max(a0, b0))


def merged_length(ivs):
    """Total length of the union of half-open intervals on one chromosome."""
    ivs = sorted(ivs)
    total, cs, ce = 0, None, None
    for s, e in ivs:
        if cs is None or s > ce:
            if cs is not None:
                total += ce - cs
            cs, ce = s, e
        else:
            ce = max(ce, e)
    if cs is not None:
        total += ce - cs
    return total


def sorted_bed(rows):
    return sorted(rows, key=lambda r: (r[0], int(r[1]), int(r[2])))
