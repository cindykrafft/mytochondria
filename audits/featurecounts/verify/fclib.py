"""Shared helpers for the featureCounts harnesses.

Writes synthetic annotations (GTF/SAF) and BAM files (pysam), runs the
featureCounts binary named by $FEATURECOUNTS (default: the master build in
the scratchpad), and parses the count table, the `.summary` file and the
`-R CORE` per-read assignment file.

Coordinates everywhere in this module are 1-based inclusive, as in GTF/SAF
and in featureCounts' own output.
"""
import os
import re
import subprocess
import tempfile

import pysam

FC = os.environ.get(
    "FEATURECOUNTS",
    "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/"
    "scratchpad/featurecounts/bin_master/featureCounts",
)

SUMMARY_ROWS = [
    "Assigned", "Unassigned_Unmapped", "Unassigned_Read_Type", "Unassigned_Singleton",
    "Unassigned_MappingQuality", "Unassigned_Chimera", "Unassigned_FragmentLength",
    "Unassigned_Duplicate", "Unassigned_MultiMapping", "Unassigned_Secondary",
    "Unassigned_NonSplit", "Unassigned_Split", "Unassigned_NoFeatures",
    "Unassigned_Overlapping_Length", "Unassigned_Ambiguity",
]


def fc_version():
    out = subprocess.run([FC, "-v"], capture_output=True, text=True)
    m = re.search(r"featureCounts v(\S+)", out.stdout + out.stderr)
    return m.group(1) if m else "?"


# ---------------------------------------------------------------- annotation
def write_gtf(path, genes, feature="exon", attr="gene_id"):
    """genes: list of (gene_id, chrom, strand, [(start, end), ...])."""
    with open(path, "w") as f:
        for gid, chrom, strand, exons in genes:
            for s, e in exons:
                f.write(f'{chrom}\tsyn\t{feature}\t{s}\t{e}\t.\t{strand}\t.\t{attr} "{gid}"; transcript_id "{gid}.t";\n')


def write_saf(path, genes):
    with open(path, "w") as f:
        f.write("GeneID\tChr\tStart\tEnd\tStrand\n")
        for gid, chrom, strand, exons in genes:
            for s, e in exons:
                f.write(f"{gid}\t{chrom}\t{s}\t{e}\t{strand}\n")


# ----------------------------------------------------------------------- BAM
def cigar_ref_len(cigar):
    """Reference bases consumed by a CIGAR string."""
    return sum(int(n) for n, op in re.findall(r"(\d+)([MIDNSHP=X])", cigar) if op in "MDN=X")


def cigar_read_len(cigar):
    return sum(int(n) for n, op in re.findall(r"(\d+)([MIDNSHP=X])", cigar) if op in "MIS=X")


def make_bam(path, chroms, records, sort=False):
    """chroms: {name: length}; records: list of dicts with keys
    name, flag, chrom (None for unmapped), pos (1-based), mapq, cigar,
    mchrom, mpos, tlen, tags (dict). Missing keys get SAM defaults."""
    names = list(chroms)
    header = {"HD": {"VN": "1.6", "SO": "unsorted"},
              "SQ": [{"SN": n, "LN": chroms[n]} for n in names]}
    with pysam.AlignmentFile(path, "wb", header=header) as bam:
        for r in records:
            a = pysam.AlignedSegment(bam.header)
            a.query_name = r["name"]
            a.flag = r.get("flag", 0)
            chrom = r.get("chrom")
            a.reference_id = names.index(chrom) if chrom is not None else -1
            a.reference_start = (r.get("pos", 1) - 1) if chrom is not None else -1
            a.mapping_quality = r.get("mapq", 60)
            cig = r.get("cigar")
            if cig and chrom is not None:
                a.cigarstring = cig
                rl = cigar_read_len(cig)
            else:
                rl = r.get("readlen", 50)
            a.query_sequence = "A" * rl
            a.query_qualities = pysam.qualitystring_to_array("I" * rl)
            mchrom = r.get("mchrom")
            a.next_reference_id = names.index(mchrom) if mchrom is not None else -1
            a.next_reference_start = (r.get("mpos", 1) - 1) if mchrom is not None else -1
            a.template_length = r.get("tlen", 0)
            tags = list(r.get("tags", {}).items())
            if tags:
                a.set_tags([(k, v) for k, v in tags])
            bam.write(a)
    if sort:
        pysam.sort("-o", path + ".s", path)
        os.replace(path + ".s", path)


def pair(name, chrom, pos1, cigar1, pos2, cigar2, r1_rev=False, r2_rev=True,
         mapq=60, tags=None, extra_flag=0, chrom2=None):
    """Two records for a proper-looking pair. Returns [R1, R2]."""
    chrom2 = chrom2 or chrom
    end1 = pos1 + cigar_ref_len(cigar1) - 1
    end2 = pos2 + cigar_ref_len(cigar2) - 1
    if chrom2 == chrom:
        lo, hi = min(pos1, pos2), max(end1, end2)
        tlen = hi - lo + 1
        t1 = tlen if pos1 <= pos2 else -tlen
        t2 = -t1
    else:
        t1 = t2 = 0
    f1 = 1 | 64 | (16 if r1_rev else 0) | (32 if r2_rev else 0) | extra_flag
    f2 = 1 | 128 | (16 if r2_rev else 0) | (32 if r1_rev else 0) | extra_flag
    tags = tags or {}
    return [
        dict(name=name, flag=f1, chrom=chrom, pos=pos1, cigar=cigar1, mapq=mapq,
             mchrom=chrom2, mpos=pos2, tlen=t1, tags=dict(tags)),
        dict(name=name, flag=f2, chrom=chrom2, pos=pos2, cigar=cigar2, mapq=mapq,
             mchrom=chrom, mpos=pos1, tlen=t2, tags=dict(tags)),
    ]


def single(name, chrom, pos, cigar, rev=False, mapq=60, tags=None, extra_flag=0):
    return dict(name=name, flag=(16 if rev else 0) | extra_flag, chrom=chrom, pos=pos,
                cigar=cigar, mapq=mapq, tags=dict(tags or {}))


# --------------------------------------------------------------------- runner
def run_fc(ann, bam, args=(), fmt="GTF", core=True, workdir=None, quiet=True):
    """Run featureCounts; return (counts, summary, details, stderr).

    counts: {feature_or_gene: float}; summary: {row: int};
    details: {read_name: (status, n_targets, targets_str)} from -R CORE."""
    wd = workdir or tempfile.mkdtemp(prefix="fc_")
    out = os.path.join(wd, "counts.txt")
    cmd = [FC, "-a", ann, "-F", fmt, "-o", out, *map(str, args)]
    if core:
        cmd += ["-R", "CORE", "--Rpath", wd]
    cmd.append(bam)
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0 or not os.path.exists(out):
        raise RuntimeError(f"featureCounts failed ({p.returncode}): {' '.join(cmd)}\n{p.stderr}\n{p.stdout}")
    counts = {}
    # In feature-level mode (-f) with a GTF, featureCounts names every row by
    # the gene_id attribute, so rows are keyed by their 0-based row index there.
    feature_level = "-f" in map(str, args)
    with open(out) as f:
        i = 0
        for line in f:
            if line.startswith("#") or line.startswith("Geneid"):
                continue
            t = line.rstrip("\n").split("\t")
            counts[f"LINE_{i+1:07d}" if feature_level else t[0]] = float(t[-1])
            i += 1
    summary = {}
    with open(out + ".summary") as f:
        next(f)
        for line in f:
            t = line.rstrip("\n").split("\t")
            summary[t[0]] = int(t[1])
    details = {}
    if core:
        det = os.path.join(wd, os.path.basename(bam) + ".featureCounts")
        with open(det) as f:
            for line in f:
                t = line.rstrip("\n").split("\t")
                details[t[0]] = (t[1], int(t[2]), t[3] if len(t) > 3 else "")
    return counts, summary, details, p.stderr + p.stdout


def summary_total(summary):
    return sum(v for k, v in summary.items())
