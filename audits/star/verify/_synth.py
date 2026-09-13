"""Shared synthetic genome / GTF / read builder and STAR runner for the STAR audit.

Everything the harnesses compare against is computed here or in the harness from
first principles (the FASTA, the GTF and the simulated reads' known origins), or
from STAR's own SAM records re-analysed with independent Python code. Nothing is
taken from STAR's counting, quantification or junction code.

Genome: two random chromosomes (chrA 300 kb, chrB 120 kb, seed 20260913). Genes
are placed at fixed coordinates and their intron motifs are planted into the random
sequence; the bases flanking each intron are chosen so that no junction position is
ambiguous (no repeat to flush into). After planting, a 1,300-bp gene (G13, exons
plus intron) is copied verbatim to chrB (G13copy, present in the GTF too) and a
500-bp segment is copied to four places on chrB (five loci in total, no GTF entry).

Coordinates below are 1-based, inclusive, as in the GTF.
"""
import os, random, subprocess, sys, shutil, collections

SEED = 20260913
COMP = str.maketrans("ACGTN", "TGCAN")

def rc(s):
    return s.translate(COMP)[::-1]

CHROMS = [("chrA", 300000), ("chrB", 120000)]

# gene id, chrom, strand, {transcript id: [(exon start, exon end), ...]}, intron motifs per
# transcript (list, one per intron; None = canonical for the strand), in_gtf flag
GENES = [
 ("G1",  "chrA", "+", {"T1":  [(1001, 1400), (2001, 2300), (5001, 5500)]}, None, True),
 ("G2",  "chrA", "-", {"T2":  [(10001, 10300), (11001, 11400), (13001, 13300)]}, None, True),
 ("G3",  "chrA", ".", {"T3":  [(20001, 20400), (21001, 21400)]}, ["GTAG"], True),   # undefined strand, GT/AG intron
 ("G4",  "chrA", ".", {"T4":  [(25001, 25800)]}, None, True),                        # undefined strand, single exon (StringTie style)
 ("G5",  "chrA", "+", {"T5":  [(30001, 30500), (31001, 31500)]}, None, True),
 ("G6",  "chrA", "+", {"T6":  [(31301, 31900)]}, None, True),                        # same-strand overlap with G5 exon 2 (31301-31500)
 ("G7",  "chrA", "+", {"T7":  [(40001, 40600)]}, None, True),
 ("G8",  "chrA", "-", {"T8":  [(40301, 40900)]}, None, True),                        # antisense overlap with G7 (40301-40600)
 ("G9",  "chrA", "+", {"T9":  [(50001, 50300), (51001, 51300), (52001, 52300), (53001, 53300)]},
                       ["GCAG", "ATAC", "CCGG"], True),                             # GC/AG, AT/AC, non-canonical introns, all annotated
 ("G11", "chrA", "+", {"T11": [(70001, 70300), (71001, 71300), (72001, 72300)]}, None, True),  # reads also simulated from an exon-2-skipping isoform (novel junction)
 ("G12", "chrA", "+", {"T12": [(80001, 80300), (81001, 81300)]}, None, False),      # not in the GTF: novel GT/AG junction
 ("G13", "chrA", "+", {"T13": [(90001, 90300), (91001, 91300)]}, None, True),       # copied verbatim to chrB:10001-11300 as G13copy
 ("G13copy", "chrB", "+", {"T13copy": [(10001, 10300), (11001, 11300)]}, None, True),
 ("G14", "chrB", "-", {"T14": [(60001, 60400), (61001, 61400)]}, None, True),
 ("G15", "chrA", "+", {"T15a": [(100001, 100300), (101001, 101300), (102001, 102300)],
                       "T15b": [(100001, 100300), (102001, 102300)]}, None, True),   # alternative isoforms
 ("G16", "chrA", "+", {"T16": [(130001, 130300), (131001, 131300)]}, ["CCGG"], False),  # not in the GTF: novel non-canonical junction
 ("G17", "chrA", "+", {"T17": [(140001, 140500)]}, None, True),                      # single exon, for intronic/intergenic controls nearby
]
MULTI5 = ("chrA", 95001, 95500, [("chrB", 20001), ("chrB", 30001), ("chrB", 40001), ("chrB", 50001)])

CANON = {"+": "GTAG", "-": "CTAC"}
# flanking bases that differ from the motif ends so that the junction cannot be shifted
FLANK = {"GTAG": ("C", "C"), "CTAC": ("A", "A"), "GCAG": ("C", "C"), "ATAC": ("C", "C"), "CCGG": ("A", "T")}


def build_genome(rng):
    g = {}
    for name, L in CHROMS:
        g[name] = bytearray(rng.choice(b"ACGT") for _ in range(L))
    # plant intron motifs
    for gid, chrom, strand, trs, motifs, in_gtf in GENES:
        for tid, exons in trs.items():
            for k in range(len(exons) - 1):
                m = motifs[k] if motifs else CANON[strand if strand != "." else "+"]
                istart, iend = exons[k][1] + 1, exons[k + 1][0] - 1
                seq = g[chrom]
                left, right = FLANK[m]
                seq[istart - 2] = ord(left)               # last exon base
                seq[istart - 1] = ord(m[0]); seq[istart] = ord(m[1])
                seq[iend - 2] = ord(m[2]); seq[iend - 1] = ord(m[3])
                seq[iend] = ord(right)                    # first base of the next exon
    # multimapper copies (after planting)
    src = g["chrA"][90001 - 1:91300]
    g["chrB"][10001 - 1:11300] = src
    seg = g["chrA"][MULTI5[1] - 1:MULTI5[2]]
    for chrom, start in MULTI5[3]:
        g[chrom][start - 1:start - 1 + len(seg)] = seg
    return {k: bytes(v).decode() for k, v in g.items()}


def write_fasta(g, path):
    with open(path, "w") as fh:
        for name, _ in CHROMS:
            fh.write(">%s\n" % name)
            s = g[name]
            for i in range(0, len(s), 80):
                fh.write(s[i:i + 80] + "\n")


def write_gtf(path):
    with open(path, "w") as fh:
        for gid, chrom, strand, trs, motifs, in_gtf in GENES:
            if not in_gtf:
                continue
            gs = min(e[0] for ex in trs.values() for e in ex)
            ge = max(e[1] for ex in trs.values() for e in ex)
            attr = 'gene_id "%s"; gene_name "%s"; gene_biotype "protein_coding";' % (gid, gid)
            fh.write("\t".join([chrom, "synth", "gene", str(gs), str(ge), ".", strand, ".", attr]) + "\n")
            for tid, exons in trs.items():
                tattr = 'gene_id "%s"; transcript_id "%s"; gene_name "%s"; gene_biotype "protein_coding";' % (gid, tid, gid)
                fh.write("\t".join([chrom, "synth", "transcript", str(exons[0][0]), str(exons[-1][1]), ".", strand, ".", tattr]) + "\n")
                for i, (s, e) in enumerate(exons):
                    fh.write("\t".join([chrom, "synth", "exon", str(s), str(e), ".", strand, ".",
                                        tattr + ' exon_number "%d";' % (i + 1)]) + "\n")


def transcripts():
    """All transcripts (including the ones not in the GTF and the G11 skipping isoform)."""
    out = {}
    for gid, chrom, strand, trs, motifs, in_gtf in GENES:
        for tid, exons in trs.items():
            out[tid] = dict(gene=gid, chrom=chrom, strand=strand, exons=list(exons), in_gtf=in_gtf)
    out["T11skip"] = dict(gene="G11", chrom="chrA", strand="+", exons=[(70001, 70300), (72001, 72300)], in_gtf=False)
    return out


def tr_seq(g, tr):
    """Spliced sequence in the sense of the transcript ('.' treated as '+')."""
    s = "".join(g[tr["chrom"]][a - 1:b] for a, b in tr["exons"])
    return rc(s) if tr["strand"] == "-" else s


def plus_offset_to_blocks(tr, off, L):
    """Genomic blocks [(start,end)] 1-based for a segment at 0-based offset `off`, length L,
    in the plus-strand concatenation of the exons."""
    blocks, cum = [], 0
    for a, b in tr["exons"]:
        el = b - a + 1
        s = max(off, cum); e = min(off + L, cum + el)
        if s < e:
            blocks.append((a + (s - cum), a + (e - cum) - 1))
        cum += el
    return blocks


class ReadSet:
    def __init__(self, rng):
        self.rng = rng
        self.se, self.pe1, self.pe2 = [], [], []
        self.truth = {}
        self.n = 0

    def _mutate(self, seq, k, margin=10, avoid=()):
        rng = self.rng
        pos = set()
        while len(pos) < k:
            p = rng.randrange(margin, len(seq) - margin)
            if p not in avoid:
                pos.add(p)
        s = list(seq)
        for p in pos:
            s[p] = rng.choice([b for b in "ACGT" if b != s[p]])
        return "".join(s), sorted(pos)

    def add_se_from_tr(self, g, tr, tid, n, L=100, kmm=(0, 0, 1, 2, 3), sense_frac=0.5, tag="tx"):
        seq = tr_seq(g, tr)
        for _ in range(n):
            rng = self.rng
            off = rng.randrange(0, len(seq) - L + 1)          # offset in the transcript sense sequence
            k = rng.choice(kmm)
            read = seq[off:off + L]
            read, mmpos = self._mutate(read, k)
            sense = rng.random() < sense_frac
            if not sense:
                read = rc(read)
            # genomic truth: offset in plus concatenation
            plus_off = off if tr["strand"] != "-" else len(seq) - off - L
            blocks = plus_offset_to_blocks(tr, plus_off, L)
            # SAM strand: read as given aligns forward if (sense and strand != '-') or (antisense and strand == '-')
            rev = (tr["strand"] == "-") == sense
            name = "%s_%06d_%s" % (tag, self.n, tid); self.n += 1
            self.se.append((name, read, "I" * L))
            self.truth[name] = dict(tid=tid, gene=tr["gene"], chrom=tr["chrom"], blocks=blocks, rev=rev,
                                    sense=sense, nmm=k, kind=tag)

    def add_se_raw(self, name, chrom, start, seq, rev, tag, **kw):
        self.se.append((name, seq, "I" * len(seq)))
        self.truth[name] = dict(chrom=chrom, blocks=[(start, start + len(seq) - 1)], rev=rev, kind=tag, **kw)

    def add_pe_from_tr(self, g, tr, tid, n, L=75, fmin=180, fmax=320, kmm=(0, 0, 1, 2), r1_sense_frac=0.5, tag="pe"):
        seq = tr_seq(g, tr)
        for _ in range(n):
            rng = self.rng
            F = rng.randrange(fmin, fmax + 1)
            if F > len(seq):
                F = len(seq)
            off = rng.randrange(0, len(seq) - F + 1)
            frag = seq[off:off + F]
            r1, r2 = frag[:L], rc(frag[-L:])                  # r1 sense, r2 antisense (fragment ends)
            r1, _ = self._mutate(r1, rng.choice(kmm)); r2, _ = self._mutate(r2, rng.choice(kmm))
            r1_sense = rng.random() < r1_sense_frac
            if not r1_sense:                                   # dUTP-like: swap which end read 1 comes from
                r1, r2 = r2, r1
            plus_off = off if tr["strand"] != "-" else len(seq) - off - F
            blocks = plus_offset_to_blocks(tr, plus_off, F)
            name = "%s_%06d_%s" % (tag, self.n, tid); self.n += 1
            self.pe1.append((name, r1, "I" * L)); self.pe2.append((name, r2, "I" * L))
            # read1 aligns reverse iff it is the antisense end on a + transcript, or the sense end on a - transcript
            r1_rev = (tr["strand"] == "-") == r1_sense
            self.truth[name] = dict(tid=tid, gene=tr["gene"], chrom=tr["chrom"], fragment=blocks, r1_rev=r1_rev,
                                    r1_sense=r1_sense, kind=tag)

    def write(self, prefix):
        def w(path, reads):
            with open(path, "w") as fh:
                for name, s, q in reads:
                    fh.write("@%s\n%s\n+\n%s\n" % (name, s, q))
        if self.se:
            w(prefix + "se.fq", self.se)
        if self.pe1:
            w(prefix + "pe_1.fq", self.pe1); w(prefix + "pe_2.fq", self.pe2)


def standard_dataset(workdir, seed=SEED, n_per_tr=300, n_pe=200):
    """Genome, GTF and the standard read sets. Returns (genome dict, transcripts, ReadSet)."""
    os.makedirs(workdir, exist_ok=True)
    rng = random.Random(seed)
    g = build_genome(rng)
    write_fasta(g, os.path.join(workdir, "genome.fa"))
    write_gtf(os.path.join(workdir, "genes.gtf"))
    trs = transcripts()
    rs = ReadSet(random.Random(seed + 1))
    for tid, tr in trs.items():
        if tid in ("T13copy",):
            continue                                   # G13copy reads are the same as G13 reads (they multimap)
        rs.add_se_from_tr(g, tr, tid, n_per_tr)
        rs.add_pe_from_tr(g, tr, tid, n_pe)
    # five-copy segment: reads from chrA 95001-95500 (also on chrB x4)
    seg = g["chrA"][MULTI5[1] - 1:MULTI5[2]]
    for i in range(100):
        off = rs.rng.randrange(0, len(seg) - 100 + 1)
        rs.add_se_raw("m5_%06d" % i, "chrA", MULTI5[1] + off, seg[off:off + 100], False, "multi5")
    # intronic reads (G1 intron 2: 2301-5000) and intergenic reads (150001-160000)
    for i in range(100):
        s = rs.rng.randrange(2400, 4800); rs.add_se_raw("intron_%06d" % i, "chrA", s, g["chrA"][s - 1:s + 99], False, "intronic", gene="G1")
        s = rs.rng.randrange(150001, 159900); rs.add_se_raw("inter_%06d" % i, "chrA", s, g["chrA"][s - 1:s + 99], False, "intergenic")
    # random (unmappable) reads
    for i in range(50):
        rs.add_se_raw("rand_%06d" % i, None, 0, "".join(rs.rng.choice("ACGT") for _ in range(100)), False, "random")
    rs.write(os.path.join(workdir, ""))
    return g, trs, rs


# ----------------------------------------------------------------------------- STAR runner

def genome_generate(star, workdir, gdir, gtf=True, extra=()):
    os.makedirs(gdir, exist_ok=True)
    cmd = [star, "--runMode", "genomeGenerate", "--genomeDir", gdir, "--genomeFastaFiles", os.path.join(workdir, "genome.fa"),
           "--genomeSAindexNbases", "8", "--outFileNamePrefix", gdir + "/", "--runThreadN", "4"]
    if gtf:
        cmd += ["--sjdbGTFfile", os.path.join(workdir, "genes.gtf"), "--sjdbOverhang", "99"]
    cmd += list(extra)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stdout.write(r.stdout + r.stderr)
        raise SystemExit("genomeGenerate failed")
    return gdir


def run_star(star, gdir, outdir, reads, extra=(), quant=("GeneCounts", "TranscriptomeSAM"), attrs=("NH", "HI", "AS", "nM", "jM", "jI", "NM", "MD")):
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir)
    cmd = [star, "--genomeDir", gdir, "--readFilesIn"] + list(reads) + \
          ["--outFileNamePrefix", outdir + "/", "--outSAMtype", "SAM", "--outSAMunmapped", "Within",
           "--outSAMattributes"] + list(attrs) + ["--runThreadN", "4", "--runRNGseed", "777"]
    if quant:
        cmd += ["--quantMode"] + list(quant)
    cmd += list(extra)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stdout.write(r.stdout + r.stderr)
        raise SystemExit("STAR failed: " + " ".join(cmd))
    return outdir


def log_final(outdir):
    d = {}
    for line in open(os.path.join(outdir, "Log.final.out")):
        if "|" in line:
            k, v = line.split("|", 1)
            d[k.strip()] = v.strip()
    return d


def read_sam(path):
    """Group STAR's SAM records by read name: {name: [pysam.AlignedSegment,...]} (mapped and unmapped)."""
    import pysam
    out = collections.OrderedDict()
    with pysam.AlignmentFile(path, "r", check_sq=False) as fh:
        for rec in fh:
            out.setdefault(rec.query_name, []).append(rec)
    return out


def alignments(recs):
    """Split a read's mapped records into alignments keyed by HI: {hi: [rec (mate1?), rec]}."""
    al = collections.OrderedDict()
    for r in recs:
        if r.is_unmapped:
            continue
        al.setdefault(r.get_tag("HI"), []).append(r)
    return al


def blocks_of(rec):
    """Aligned genomic blocks (1-based inclusive) of M/=/X runs; D and N split blocks (as STAR's exons do)."""
    blocks, pos = [], rec.reference_start + 1
    cur = None
    for op, ln in rec.cigartuples:
        if op in (0, 7, 8):
            if cur is None:
                cur = [pos, pos + ln - 1]
            else:
                cur[1] = pos + ln - 1
            pos += ln
        elif op == 2 or op == 3:              # D / N consume reference and end the block
            if cur is not None:
                blocks.append(tuple(cur)); cur = None
            pos += ln
        elif op == 1:                          # I ends the block, no reference consumed
            if cur is not None:
                blocks.append(tuple(cur)); cur = None
        # S/H: nothing
    if cur is not None:
        blocks.append(tuple(cur))
    return blocks


def junctions_of(rec):
    """(intron start, intron end, left block length, right block length) for each N op, 1-based."""
    out, pos = [], rec.reference_start + 1
    runs = []                                    # list of (kind, ref_start, ref_end, len)
    for op, ln in rec.cigartuples:
        if op in (0, 7, 8):
            runs.append(("M", pos, pos + ln - 1, ln)); pos += ln
        elif op == 3:
            runs.append(("N", pos, pos + ln - 1, ln)); pos += ln
        elif op == 2:
            runs.append(("D", pos, pos + ln - 1, ln)); pos += ln
        elif op == 1:
            runs.append(("I", pos, pos - 1, ln))
    for i, r in enumerate(runs):
        if r[0] == "N":
            left = runs[i - 1][3] if i > 0 and runs[i - 1][0] == "M" else 0
            right = runs[i + 1][3] if i + 1 < len(runs) and runs[i + 1][0] == "M" else 0
            out.append((r[1], r[2], left, right))
    return out


def motif_code(g, chrom, istart, iend):
    s = g[chrom]
    d, a = s[istart - 1:istart + 1], s[iend - 2:iend]
    return {("GT", "AG"): 1, ("CT", "AC"): 2, ("GC", "AG"): 3, ("CT", "GC"): 4, ("AT", "AC"): 5, ("GT", "AT"): 6}.get((d, a), 0)


def gtf_junctions(trs):
    """Annotated junction set {(chrom, istart, iend)} from GTF transcripts, and per-junction strands."""
    out = {}
    for tid, tr in trs.items():
        if not tr["in_gtf"]:
            continue
        for k in range(len(tr["exons"]) - 1):
            key = (tr["chrom"], tr["exons"][k][1] + 1, tr["exons"][k + 1][0] - 1)
            out.setdefault(key, set()).add(tr["strand"])
    return out


def mismatches(g, rec):
    """Mismatches between the read and the genome over M blocks (N in read or genome not counted)."""
    n = 0
    q = rec.query_sequence
    qpos, rpos = 0, rec.reference_start
    s = g[rec.reference_name]
    for op, ln in rec.cigartuples:
        if op in (0, 7, 8):
            for i in range(ln):
                a, b = q[qpos + i], s[rpos + i]
                if a != b and a != "N" and b != "N":
                    n += 1
            qpos += ln; rpos += ln
        elif op == 1 or op == 4:
            qpos += ln
        elif op in (2, 3):
            rpos += ln
    return n
