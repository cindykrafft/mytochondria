#!/usr/bin/env python3
"""Independent Python port of the documented `htseq-count` semantics, plus a
synthetic BAM/GTF generator with known truth.

Everything here is written from the documentation (doc/htseqcount.rst: the
S(i) definition of the three overlap modes, the --nonunique modes, the special
counters, the strand rules for single-end and paired-end reads) and from the
SAM specification -- not from HTSeq's code. The port enumerates every reference
base covered by an M/=/X CIGAR operation of the read (or of both mates of the
pair) and looks up the set of features covering that base in a per-base
dictionary built from the GTF by brute force; it never uses HTSeq's
GenomicArrayOfSets, StepVector or pairing code.

The generator knows which BAM records belong to one counting unit (a read, a
read pair, a lone mate, a chimeric segment), so the truth is independent of
HTSeq's mate-pairing logic; the BAM is written twice, name-sorted and
coordinate-sorted, so `-r name` and `-r pos` can be checked against each other
and against the truth.
"""
import os
import random
import subprocess
import sys
from collections import defaultdict
from fractions import Fraction

import pysam

SPECIAL = ["__no_feature", "__ambiguous", "__too_low_aQual", "__not_aligned",
           "__alignment_not_unique"]


# --------------------------------------------------------------------- GTF
def write_gtf(path, features):
    """features: list of (chrom, start0, end0, strand, ftype, attrs dict).
    Coordinates are 0-based half-open and are converted to 1-based closed GTF."""
    with open(path, "w") as f:
        for chrom, s, e, strand, ftype, attrs in features:
            attr = " ".join(f'{k} "{v}";' for k, v in attrs.items())
            f.write(f"{chrom}\tsrc\t{ftype}\t{s + 1}\t{e}\t.\t{strand}\t.\t{attr}\n")


def per_base_sets(features, feature_type, idattr, stranded):
    """Brute-force S(i): dict (chrom, strand-or-'.', base) -> set of feature ids."""
    sets = defaultdict(set)
    ids = set()
    for chrom, s, e, strand, ftype, attrs in features:
        if ftype not in feature_type:
            continue
        fid = ":".join(attrs[a] for a in idattr)
        ids.add(fid)
        key_strand = strand if stranded else "."
        for b in range(s, e):
            sets[(chrom, key_strand, b)].add(fid)
    return sets, ids


# --------------------------------------------------------------------- reads
class Rec:
    """One BAM record; `unit` groups records into a counting unit."""

    def __init__(self, name, chrom=None, start=None, cigar=None, strand="+",
                 mapq=60, nh=None, secondary=False, supplementary=False,
                 paired=False, which=None, mate=None, unit=None):
        self.name, self.chrom, self.start, self.cigar = name, chrom, start, cigar
        self.strand, self.mapq, self.nh = strand, mapq, nh
        self.secondary, self.supplementary = secondary, supplementary
        self.paired, self.which, self.mate, self.unit = paired, which, mate, unit
        self.tlen = 0
        self.mate_chrom = self.mate_start = None
        self.mate_strand = "+"
        self.mate_unmapped = False
        self.placed_at = None  # (chrom, pos) for unmapped reads placed at mate

    @property
    def aligned(self):
        return self.chrom is not None

    def ref_end(self):
        e = self.start
        for op, n in self.cigar:
            if op in "MDN=X":
                e += n
        return e

    def ref_bases(self):
        """Reference bases covered by M/=/X operations (the read's positions)."""
        pos = self.start
        out = []
        for op, n in self.cigar:
            if op in "M=X":
                out.extend(range(pos, pos + n))
                pos += n
            elif op in "DN":
                pos += n
        return out

    def query_len(self):
        return sum(n for op, n in self.cigar if op in "MIS=X") if self.cigar else 20


OPCODE = {"M": 0, "I": 1, "D": 2, "N": 3, "S": 4, "H": 5, "P": 6, "=": 7, "X": 8}


def to_segment(r, tid_of):
    a = pysam.AlignedSegment()
    a.query_name = r.name
    L = r.query_len()
    a.query_sequence = "A" * L
    a.query_qualities = pysam.qualitystring_to_array("I" * L)
    flag = 0
    if r.paired:
        flag |= 0x1
        flag |= 0x40 if r.which == 1 else 0x80
        if r.mate_unmapped:
            flag |= 0x8
        if r.mate_strand == "-":
            flag |= 0x20
    if not r.aligned:
        flag |= 0x4
        a.reference_id, a.reference_start = -1, -1
        if r.placed_at is not None:
            a.reference_id, a.reference_start = tid_of[r.placed_at[0]], r.placed_at[1]
    else:
        if r.strand == "-":
            flag |= 0x10
        a.reference_id = tid_of[r.chrom]
        a.reference_start = r.start
        a.cigartuples = [(OPCODE[op], n) for op, n in r.cigar]
    if r.secondary:
        flag |= 0x100
    if r.supplementary:
        flag |= 0x800
    a.flag = flag
    a.mapping_quality = r.mapq if r.aligned else 0
    if r.mate_chrom is not None:
        a.next_reference_id = tid_of[r.mate_chrom]
        a.next_reference_start = r.mate_start
    else:
        a.next_reference_id, a.next_reference_start = -1, -1
    a.template_length = r.tlen
    tags = []
    if r.nh is not None:
        tags.append(("NH", r.nh))
    a.set_tags(tags)
    return a


def write_bams(prefix, recs, chrom_lens, order_seed=0):
    """Write name-sorted and coordinate-sorted BAMs. Returns (name_bam, pos_bam)."""
    chroms = list(chrom_lens)
    tid_of = {c: i for i, c in enumerate(chroms)}
    header = {"HD": {"VN": "1.6"}, "SQ": [{"SN": c, "LN": chrom_lens[c]} for c in chroms]}
    unsorted = prefix + ".unsorted.bam"
    with pysam.AlignmentFile(unsorted, "wb", header=header) as f:
        rng = random.Random(order_seed)
        recs2 = list(recs)
        rng.shuffle(recs2)
        for r in recs2:
            f.write(to_segment(r, tid_of))
    name_bam, pos_bam = prefix + ".byname.bam", prefix + ".bypos.bam"
    pysam.sort("-n", "-o", name_bam, unsorted)
    pysam.sort("-o", pos_bam, unsorted)
    os.remove(unsorted)
    return name_bam, pos_bam


# --------------------------------------------------------------------- port
def unit_positions(unit, stranded):
    """Stranded positions of a counting unit: mate 1 as aligned, mate 2 on the
    opposite strand ('yes'); reversed for 'reverse'; strand ignored for 'no'."""
    out = []
    for r in unit:
        if not r.aligned:
            continue
        s = r.strand
        if r.paired and r.which == 2:
            s = "-" if s == "+" else "+"
        if stranded == "reverse":
            s = "-" if s == "+" else "+"
        if stranded == "no":
            s = "."
        out.extend((r.chrom, s, b) for b in r.ref_bases())
    return out


def resolve(sets, positions, mode):
    S = [sets.get(p, frozenset()) for p in positions]
    if mode == "union":
        fs = set()
        for s in S:
            fs |= s
        return fs
    if mode == "intersection-strict":
        fs = None
        for s in S:
            fs = set(s) if fs is None else fs & s
        return fs or set()
    if mode == "intersection-nonempty":
        fs = None
        for s in S:
            if s:
                fs = set(s) if fs is None else fs & s
        return fs or set()
    raise ValueError(mode)


def port_count(units, sets, ids, mode, stranded, nonunique="none", minaqual=10,
               secondary="ignore", supplementary="ignore", unmapped_mate_mapq=None,
               feature_chroms=None):
    """Counts as the documentation describes them. Returns dict id/special -> Fraction.

    unmapped_mate_mapq: None (documented semantics: only aligned mates are
    subject to -a) or an int -- model HTSeq's shipped behaviour of comparing the
    MAPQ field of an *unmapped* mate record (0 by aligner convention) with -a
    as well (HC2 in the review).
    feature_chroms: None, or the set of chromosomes that carry at least one
    feature -- model HTSeq's UnknownChrom rule: a unit with any aligned record
    on a chromosome without features is `__no_feature` as a whole (N4)."""
    counts = {i: Fraction(0) for i in ids}
    for k in SPECIAL:
        counts[k] = Fraction(0)
    for unit in units:
        present = [r for r in unit if r is not None]
        if not any(r.aligned for r in present):
            counts["__not_aligned"] += 1
            continue
        if secondary == "ignore" and any(r.secondary for r in present):
            continue
        if supplementary == "ignore" and any(r.supplementary for r in present):
            continue
        if any(r.nh is not None and r.nh > 1 for r in present):
            counts["__alignment_not_unique"] += 1
            if nonunique == "none":
                continue
        if any(r.aligned and r.mapq < minaqual for r in present):
            counts["__too_low_aQual"] += 1
            continue
        if unmapped_mate_mapq is not None and any(
                (not r.aligned) and unmapped_mate_mapq < minaqual for r in present):
            counts["__too_low_aQual"] += 1
            continue
        if feature_chroms is not None and any(r.aligned and r.chrom not in feature_chroms for r in present):
            counts["__no_feature"] += 1
            continue
        fs = resolve(sets, unit_positions(present, stranded), mode)
        if len(fs) == 0:
            counts["__no_feature"] += 1
        elif len(fs) > 1:
            counts["__ambiguous"] += 1
            if nonunique == "all":
                for f in fs:
                    counts[f] += 1
            elif nonunique == "fraction":
                for f in fs:
                    counts[f] += Fraction(1, len(fs))
        else:
            counts[next(iter(fs))] += 1
    return counts


# --------------------------------------------------------------------- CLI
def run_htseq_count(bam, gtf, extra, python=None):
    """Run htseq-count and parse its TSV. Returns (dict name->float, stderr)."""
    python = python or sys.executable
    # HTSEQ_PORT_EXTRA_ARGS: e.g. "-f bam" for HTSeq <= 0.11, whose -f defaulted to sam
    extra_env = os.environ.get("HTSEQ_PORT_EXTRA_ARGS", "").split()
    cmd = [python, "-W", "ignore", "-m", "HTSeq.scripts.count", "-q"] + extra_env + list(extra) + [bam, gtf]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError("htseq-count failed: %s\n%s" % (" ".join(cmd), p.stderr))
    out = {}
    for line in p.stdout.splitlines():
        if not line.strip():
            continue
        k, v = line.split("\t")[0], line.split("\t")[-1]
        out[k] = float(v)
    return out, p.stderr


def compare(port, cli, tol=1e-9):
    """Return list of (key, port, cli) mismatches."""
    bad = []
    keys = set(port) | set(cli)
    for k in sorted(keys):
        a = float(port.get(k, 0))
        b = float(cli.get(k, 0))
        if abs(a - b) > tol:
            bad.append((k, a, b))
    return bad
