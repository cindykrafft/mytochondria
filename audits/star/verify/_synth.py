#!/usr/bin/env python3
"""Shared synthetic genome / annotation / read simulator and STAR runner for the
STAR audit harnesses (audits/star/verify).

Everything the harnesses compare against is built here with a fixed seed, so the
truth is known: a random two-chromosome genome with planted intron motifs and
repeated segments, a GTF of multi-exon genes on both strands (overlapping genes,
an antisense gene, two isoforms, a strand-less gene, genes inside 2-, 3- and
12-copy repeats), and reads simulated from the transcripts (single-end 100 nt and
paired-end 2 x 75 nt, unstranded, 0.3 % substitutions, a few indel reads, junk and
half-junk reads). Read names carry an index into the truth table.

Usage from a harness:
    from _synth import Synth, run_star_genome, run_star_map, bam_by_read, ...
    S = Synth(workdir)          # builds genome.fa, genes.gtf, reads_se.fq, reads_1/2.fq
"""
import os, sys, subprocess, json, math, random, collections
import numpy as np
import pysam

COMP = str.maketrans("ACGTN", "TGCAN")
def rc(s): return s.translate(COMP)[::-1]

# intron motifs on the + strand of the genome (donor dinucleotide, acceptor dinucleotide)
MOTIF = {"GTAG": ("GT", "AG"), "CTAC": ("CT", "AC"), "GCAG": ("GC", "AG"), "CTGC": ("CT", "GC"),
         "ATAC": ("AT", "AC"), "GTAT": ("GT", "AT"), "NONCAN": ("CA", "TG")}
# STAR's numeric motif code for the dinucleotides read on the + strand
MOTIF_CODE = {("GT", "AG"): 1, ("CT", "AC"): 2, ("GC", "AG"): 3, ("CT", "GC"): 4, ("AT", "AC"): 5, ("GT", "AT"): 6}

# gene_id, chrom, strand, list of transcripts (tid, [(start,end),...] 1-based inclusive), intron motif
GENES = [
    ("G1",  "chr1", "+", [("T1",  [(1001, 1300), (2001, 2200), (3501, 3900), (6001, 6500)])], "GTAG"),
    ("G2",  "chr1", "-", [("T2",  [(12001, 12400), (13001, 13150), (15001, 15600)])], "CTAC"),
    ("G3",  "chr1", "+", [("T3",  [(20001, 21500)])], None),
    ("G4",  "chr1", "+", [("T4",  [(30001, 30400), (31001, 31600)])], "GTAG"),
    ("G5",  "chr1", "+", [("T5",  [(31201, 31800), (33001, 33400)])], "GTAG"),        # overlaps G4 exon 2
    ("G6",  "chr1", "-", [("T6",  [(6201, 6800)])], None),                             # antisense to G1 exon 4
    ("G7",  "chr1", "+", [("T7a", [(40001, 40300), (41001, 41300), (42001, 42500)]),
                          ("T7b", [(40001, 40300), (42001, 42500)])], "GTAG"),         # two isoforms
    ("G8",  "chr1", "+", [("T8",  [(50001, 50300), (51001, 51400), (52001, 52400)])], ["GCAG", "ATAC"]),
    ("G9",  "chr1", "+", [("T9",  [(55001, 55300), (56001, 56400)])], "NONCAN"),
    ("G10", "chr1", "+", [("T10", [(300101, 300400), (300801, 301200), (301801, 302400)])], "GTAG"),  # in a 3-copy repeat
    ("G11", "chr1", "+", [("T11", [(340101, 341400)])], None),                         # in a 2-copy repeat
    ("G12", "chr1", "+", [("T12", [(320101, 320900)])], None),                         # in a 12-copy repeat
    ("G13", "chr2", "-", [("T13", [(120001, 120300), (121001, 121400), (123001, 123500)])], "CTAC"),
    ("G14", "chr2", ".", [("T14", [(140001, 140600)])], None),                         # strand-less gene
]
CHR_LEN = {"chr1": 400000, "chr2": 150000}
# (source chrom, start0, end0) -> list of (dest chrom, start0)
REPEATS = [
    ("chr1", 300000, 303000, [("chr2", 10000), ("chr2", 50000)]),                     # 3 copies (G10)
    ("chr1", 340000, 341500, [("chr2", 100000)]),                                       # 2 copies (G11)
    ("chr1", 320000, 321000, [("chr2", 70000 + 1000 * k) for k in range(11)]),         # 12 copies (G12)
]

class Synth:
    def __init__(self, workdir, seed=1, n_scale=1.0):
        self.workdir = workdir
        os.makedirs(workdir, exist_ok=True)
        self.rng = np.random.default_rng(seed)
        self.pyrng = random.Random(seed)
        self.fa = os.path.join(workdir, "genome.fa")
        self.gtf = os.path.join(workdir, "genes.gtf")
        self.fq_se = os.path.join(workdir, "reads_se.fq")
        self.fq_1 = os.path.join(workdir, "reads_1.fq")
        self.fq_2 = os.path.join(workdir, "reads_2.fq")
        self.truth_file = os.path.join(workdir, "truth.json")
        self.n_scale = n_scale
        self._build_genome()
        self._write_gtf()
        if os.path.exists(self.truth_file) and os.path.exists(self.fq_2):
            self.truth = json.load(open(self.truth_file))
        else:
            self._simulate_reads()

    # ------------------------------------------------------------------ genome
    def _build_genome(self):
        g = {c: np.array(list("ACGT"))[self.rng.integers(0, 4, n)] for c, n in CHR_LEN.items()}
        self.junctions = []   # (chrom, intron_start1, intron_end1, strand, motif code, gene, transcript)
        for gid, chrom, strand, trs, motif in GENES:
            for k, (tid, exons) in enumerate(trs):
                for i in range(len(exons) - 1):
                    s = exons[i][1] + 1; e = exons[i + 1][0] - 1        # 1-based intron
                    m = motif[i] if isinstance(motif, list) else motif
                    d, a = MOTIF[m]
                    arr = g[chrom]
                    arr[s - 1], arr[s] = d[0], d[1]
                    arr[e - 2], arr[e - 1] = a[0], a[1]
                    # no repeat around the junction, so STAR's shiftSJ is 0 and the locus is unambiguous
                    if arr[s - 2] == arr[e - 1]:
                        arr[s - 2] = {"A": "C", "C": "A", "G": "T", "T": "G"}[arr[e - 1]]
                    if arr[e] == arr[s - 1]:
                        arr[e] = {"A": "C", "C": "A", "G": "T", "T": "G"}[arr[s - 1]]
                    self.junctions.append((chrom, s, e, strand, MOTIF_CODE.get((d, a), 0), gid, tid))
        for chrom, s0, e0, dests in REPEATS:
            seg = g[chrom][s0:e0].copy()
            for dc, ds in dests:
                g[dc][ds:ds + len(seg)] = seg
        self.genome = {c: "".join(a) for c, a in g.items()}
        if not os.path.exists(self.fa):
            with open(self.fa, "w") as fh:
                for c in CHR_LEN:
                    fh.write(">%s\n" % c)
                    s = self.genome[c]
                    for i in range(0, len(s), 80): fh.write(s[i:i + 80] + "\n")
        # annotated junction set (chrom, start, end) and per-gene exon lists
        self.annot_sj = {(c, s, e) for c, s, e, *_ in self.junctions}
        self.gene_exons = {}   # gid -> (chrom, strand, [(s,e)...] union of transcript exons)
        self.transcripts = {}  # tid -> (gid, chrom, strand, [(s,e)...])
        for gid, chrom, strand, trs, motif in GENES:
            ex = sorted({e for _, exs in trs for e in exs})
            self.gene_exons[gid] = (chrom, strand, ex)
            for tid, exs in trs:
                self.transcripts[tid] = (gid, chrom, strand, list(exs))

    def _write_gtf(self):
        if os.path.exists(self.gtf): return
        with open(self.gtf, "w") as fh:
            for gid, chrom, strand, trs, motif in GENES:
                for tid, exs in trs:
                    for s, e in exs:
                        fh.write("%s\tsynth\texon\t%d\t%d\t.\t%s\t.\tgene_id \"%s\"; transcript_id \"%s\"; gene_name \"%s\"; gene_biotype \"protein_coding\";\n"
                                 % (chrom, s, e, strand, gid, tid, gid))

    def tr_seq(self, tid):
        gid, chrom, strand, exs = self.transcripts[tid]
        s = "".join(self.genome[chrom][a - 1:b] for a, b in exs)
        return rc(s) if strand == "-" else s

    # ------------------------------------------------------------------ reads
    def _mutate(self, seq, rate=0.003, n_rate=0.002):
        out = list(seq); nmm = 0
        for i in range(len(out)):
            r = self.pyrng.random()
            if r < rate:
                out[i] = self.pyrng.choice([b for b in "ACGT" if b != out[i]]); nmm += 1
            elif r < rate + n_rate:
                out[i] = "N"
        return "".join(out), nmm

    def _simulate_reads(self):
        truth = {}
        se, pe1, pe2 = [], [], []
        sc = self.n_scale
        # reads per transcript (single-end / paired-end)
        per_tr = {"T1": 1500, "T2": 900, "T3": 800, "T4": 600, "T5": 600, "T6": 400, "T7a": 700, "T7b": 500,
                  "T8": 800, "T9": 600, "T10": 600, "T11": 300, "T12": 300, "T13": 900, "T14": 400}
        i = 0
        def name(): return "r%06d" % i
        # --- single-end reads from transcripts
        for tid, n in per_tr.items():
            tseq = self.tr_seq(tid); gid, chrom, strand, exs = self.transcripts[tid]
            for _ in range(int(n * sc)):
                p = self.pyrng.randrange(0, len(tseq) - 100 + 1)
                frag = tseq[p:p + 100]
                sense = self.pyrng.random() < 0.5
                seq = frag if sense else rc(frag)
                seq, nmm = self._mutate(seq)
                se.append((name(), seq))
                truth[name()] = {"kind": "tr", "tid": tid, "gid": gid, "tpos": p, "sense": sense, "nmm": nmm, "lib": "se"}
                i += 1
        # --- single-end indel reads from the single-exon gene G3
        tseq = self.tr_seq("T3")
        for _ in range(int(200 * sc)):
            p = self.pyrng.randrange(0, len(tseq) - 105)
            frag = tseq[p:p + 105]
            k = self.pyrng.randrange(30, 70); L = self.pyrng.choice([1, 2, 3])
            if self.pyrng.random() < 0.5:
                frag = frag[:k] + frag[k + L:]; kind = "del"
            else:
                frag = frag[:k] + "".join(self.pyrng.choice("ACGT") for _ in range(L)) + frag[k:]; kind = "ins"
            seq = frag[:100]
            sense = self.pyrng.random() < 0.5
            seq = seq if sense else rc(seq)
            se.append((name(), seq))
            truth[name()] = {"kind": kind, "tid": "T3", "gid": "G3", "tpos": p, "sense": sense, "indelL": L, "lib": "se"}
            i += 1
        # --- intergenic, intronic and antisense reads
        for _ in range(int(300 * sc)):
            p = self.pyrng.randrange(200000, 250000)
            seq = self.genome["chr1"][p:p + 100]
            sense = self.pyrng.random() < 0.5
            seq, nmm = self._mutate(seq if sense else rc(seq))
            se.append((name(), seq)); truth[name()] = {"kind": "intergenic", "gpos": p, "sense": sense, "lib": "se"}; i += 1
        for _ in range(int(200 * sc)):
            p = self.pyrng.randrange(2300, 3300)     # inside G1 intron 2 (2201..3500)
            seq = self.genome["chr1"][p:p + 100]
            sense = self.pyrng.random() < 0.5
            seq, nmm = self._mutate(seq if sense else rc(seq))
            se.append((name(), seq)); truth[name()] = {"kind": "intronic", "gid": "G1", "gpos": p, "sense": sense, "lib": "se"}; i += 1
        # --- junk (unmapped: other) and half-junk (unmapped: too short)
        for _ in range(int(100 * sc)):
            seq = "".join(self.pyrng.choice("ACGT") for _ in range(100))
            se.append((name(), seq)); truth[name()] = {"kind": "junk", "lib": "se"}; i += 1
        for _ in range(int(100 * sc)):
            p = self.pyrng.randrange(0, len(tseq) - 50)
            seq = tseq[p:p + 50] + "".join(self.pyrng.choice("ACGT") for _ in range(50))
            se.append((name(), seq)); truth[name()] = {"kind": "halfjunk", "gid": "G3", "lib": "se"}; i += 1
        # --- paired-end reads from transcripts (2 x 75, fragment ~N(260,30))
        for tid, n in per_tr.items():
            tseq = self.tr_seq(tid); gid, chrom, strand, exs = self.transcripts[tid]
            for _ in range(int(n * sc)):
                fl = int(min(max(self.rng.normal(260, 30), 160), 400))
                fl = min(fl, len(tseq))
                p = self.pyrng.randrange(0, len(tseq) - fl + 1)
                frag = tseq[p:p + fl]
                sense = self.pyrng.random() < 0.5
                if not sense: frag = rc(frag)
                m1, nmm1 = self._mutate(frag[:75]); m2, nmm2 = self._mutate(rc(frag)[:75])
                pe1.append((name(), m1)); pe2.append((name(), m2))
                truth[name()] = {"kind": "tr", "tid": tid, "gid": gid, "tpos": p, "flen": fl, "sense": sense, "nmm": nmm1 + nmm2, "lib": "pe"}
                i += 1
        for _ in range(int(100 * sc)):
            m1 = "".join(self.pyrng.choice("ACGT") for _ in range(75)); m2 = "".join(self.pyrng.choice("ACGT") for _ in range(75))
            pe1.append((name(), m1)); pe2.append((name(), m2)); truth[name()] = {"kind": "junk", "lib": "pe"}; i += 1
        # one mate junk, the other from G3 (single-end alignment of a PE read)
        tseq = self.tr_seq("T3")
        for _ in range(int(150 * sc)):
            p = self.pyrng.randrange(0, len(tseq) - 75)
            m1 = tseq[p:p + 75]; m2 = "".join(self.pyrng.choice("ACGT") for _ in range(75))
            pe1.append((name(), m1)); pe2.append((name(), m2)); truth[name()] = {"kind": "mate2junk", "gid": "G3", "tid": "T3", "tpos": p, "sense": True, "lib": "pe"}; i += 1
        self.truth = truth
        def wfq(path, reads):
            with open(path, "w") as fh:
                for nm, sq in reads: fh.write("@%s\n%s\n+\n%s\n" % (nm, sq, "I" * len(sq)))
        wfq(self.fq_se, se); wfq(self.fq_1, pe1); wfq(self.fq_2, pe2)
        json.dump(truth, open(self.truth_file, "w"))

# ---------------------------------------------------------------------- STAR
def run(cmd, log=None):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if log:
        with open(log, "a") as fh: fh.write("$ " + " ".join(cmd) + "\n" + p.stdout + "\n")
    if p.returncode != 0:
        sys.stderr.write(p.stdout)
        raise SystemExit("command failed: " + " ".join(cmd))
    return p.stdout

def star_version(star):
    return run([star, "--version"]).strip()

def run_star_genome(star, gdir, fa, gtf=None, overhang=99, extra=()):
    """genomeGenerate once per directory (marker file)."""
    if os.path.exists(os.path.join(gdir, "SAindex")):
        return gdir
    os.makedirs(gdir, exist_ok=True)
    cmd = [star, "--runMode", "genomeGenerate", "--genomeDir", gdir, "--genomeFastaFiles", fa,
           "--genomeSAindexNbases", "8", "--runThreadN", "2", "--outFileNamePrefix", gdir + "/"]
    if gtf: cmd += ["--sjdbGTFfile", gtf, "--sjdbOverhang", str(overhang)]
    cmd += list(extra)
    run(cmd, os.path.join(gdir, "cmd.log"))
    return gdir

def run_star_map(star, gdir, prefix, reads, extra=(), threads=1):
    """Map once per prefix (Log.final.out marker). reads: [fq] or [fq1, fq2]."""
    if os.path.exists(prefix + "Log.final.out"):
        return prefix
    os.makedirs(os.path.dirname(prefix), exist_ok=True)
    cmd = [star, "--runMode", "alignReads", "--genomeDir", gdir, "--readFilesIn"] + list(reads) + \
          ["--outFileNamePrefix", prefix, "--runThreadN", str(threads)] + list(extra)
    run(cmd, prefix + "cmd.log")
    return prefix

# ---------------------------------------------------------------------- parsers
def bam_by_read(path):
    """All records grouped by read name (dict qname -> list of AlignedSegment)."""
    out = collections.OrderedDict()
    with pysam.AlignmentFile(path, "rb", check_sq=False) as bf:
        for r in bf:
            out.setdefault(r.query_name, []).append(r)
    return out

def read_sj(path):
    rows = []
    for line in open(path):
        f = line.rstrip("\n").split("\t")
        rows.append((f[0], int(f[1]), int(f[2]), int(f[3]), int(f[4]), int(f[5]), int(f[6]), int(f[7]), int(f[8])))
    return rows

def read_genecounts(path):
    d = collections.OrderedDict()
    for line in open(path):
        f = line.rstrip("\n").split("\t")
        d[f[0]] = tuple(int(x) for x in f[1:])
    return d

def read_logfinal(path):
    d = {}
    for line in open(path):
        if "|" in line:
            k, v = line.split("|", 1)
            d[k.strip()] = v.strip()
    return d

def blocks_of(rec):
    """Aligned blocks [(ref_start0, ref_end0_excl, query_start0)] from CIGAR: M/=/X only (D and N split blocks,
    as STAR's exons do)."""
    out = []; rpos = rec.reference_start; qpos = 0
    for op, ln in rec.cigartuples:
        if op in (0, 7, 8):
            out.append((rpos, rpos + ln, qpos)); rpos += ln; qpos += ln
        elif op in (2, 3):
            rpos += ln
        elif op in (1, 4):
            qpos += ln
    return out

def read_strand_star(recs):
    """STAR's alignment strand (Str) for a read: 0 if mate 1 (or the single-end read) is forward, 1 otherwise;
    for a single-mate alignment of mate 2, the strand mate 1 would have."""
    r = recs[0]
    if r.is_paired and r.is_read2:
        return 0 if r.is_reverse else 1
    return 1 if r.is_reverse else 0
