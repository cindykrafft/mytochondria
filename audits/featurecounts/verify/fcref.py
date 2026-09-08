"""Independent reference implementation of featureCounts' documented
assignment rules (Subread users guide, section "featureCounts"), written from
the documentation and the option help, not from readSummary.c.

It takes the same synthetic annotation and the same BAM records the harness
writes, and returns, per fragment, the status label featureCounts prints in
its `-R CORE` file and the (target -> count) increments.  Where the manual is
silent, the rule adopted is stated in a comment marked DOC-SILENT; the
brute-force harness reports every disagreement so those choices are checked
by execution rather than assumed.
"""
import re
from collections import defaultdict

NH_INT = 65536  # the fixed-point unit featureCounts uses for fractional counts


def ceil3(x):
    """featureCounts' rounding of fraction*length: floor, +1 if the remainder is >= 0.001."""
    i = int(x)
    return i + 1 if x - i >= 0.001 else i


class Ann:
    """Annotation: features (exon lines) and meta-features (genes)."""

    def __init__(self, genes, feature_level=False):
        # genes: list of (gene_id, chrom, strand, [(s, e), ...])
        self.feats = []  # (fid, chrom, strand, s, e, gene)
        for gid, chrom, strand, exons in genes:
            for s, e in exons:
                fid = len(self.feats)
                self.feats.append((fid, chrom, strand, s, e, gid))
        self.feature_level = feature_level
        self.by_chrom = defaultdict(list)
        for f in self.feats:
            self.by_chrom[f[1]].append(f)

    def key(self, f):
        return f[0] if self.feature_level else f[5]

    def name(self, f):
        return f"LINE_{f[0]+1:07d}" if self.feature_level else f[5]


def parse_cigar(cigar):
    return [(int(n), op) for n, op in re.findall(r"(\d+)([MIDNSHP=X])", cigar)]


class Read:
    """One SAM record, with its aligned blocks and the quantities the rules need."""

    def __init__(self, rec, five_ext=0, three_ext=0, read2pos=0):
        self.rec = rec
        self.flag = rec.get("flag", 0)
        self.unmapped = bool(self.flag & 4)
        self.chrom = rec.get("chrom")
        self.mapq = rec.get("mapq", 60)
        self.nh = rec.get("tags", {}).get("NH", 1)
        self.rev = bool(self.flag & 16)
        self.second = bool(self.flag & 128)
        self.dup = bool(self.flag & 1024)
        self.secondary = bool(self.flag & 256)
        self.blocks = []       # aligned reference blocks (chrom, start, end) 1-based inclusive
        self.split = False
        self.covered = set()   # reference positions counted in the fragment length (incl. soft clips)
        self.insertions = []   # (ref_pos_after, length)
        if self.unmapped or self.chrom is None:
            return
        pos = rec["pos"]
        ops = parse_cigar(rec["cigar"])
        cur = pos
        blk_start = pos
        blk_len = 0
        lead_S = 0
        trail_S = 0
        read_cursor = 0
        for i, (n, op) in enumerate(ops):
            if op in "M=X":
                cur += n
                blk_len += n
                read_cursor += n
            elif op in "DN":
                if op == "N":
                    self.split = True
                if blk_len:
                    self.blocks.append((self.chrom, blk_start, blk_start + blk_len - 1))
                cur += n
                blk_start = cur
                blk_len = 0
            elif op == "I":
                self.insertions.append((cur, n))
                if blk_len:
                    self.blocks.append((self.chrom, blk_start, blk_start + blk_len - 1))
                blk_start = cur
                blk_len = 0
                read_cursor += n
            elif op == "S":
                if read_cursor == 0:
                    lead_S = n
                else:
                    trail_S = n
                read_cursor += n
        if blk_len:
            self.blocks.append((self.chrom, blk_start, blk_start + blk_len - 1))
        # fragment-length coverage: the reference span of every aligned section,
        # extended by the soft clips at either end (manual: soft-clipped bases are
        # counted in the read length, not in the overlap).
        for c, s, e in self.blocks:
            self.covered.update(range(s, e + 1))
        if self.blocks:
            first_s = self.blocks[0][1]
            last_e = self.blocks[-1][2]
            self.covered.update(range(max(0, first_s - lead_S), first_s))
            self.covered.update(range(last_e + 1, last_e + 1 + trail_S))
        # --readExtension5 / --readExtension3 (upstream of the 5' end, downstream of the 3' end)
        # then --read2pos.  DOC-SILENT: extension applies to the outermost blocks only.
        if self.blocks and (five_ext or three_ext):
            left_ext = three_ext if self.rev else five_ext
            right_ext = five_ext if self.rev else three_ext
            c, s, e = self.blocks[0]
            self.blocks[0] = (c, max(1, s - left_ext), e)
            c, s, e = self.blocks[-1]
            self.blocks[-1] = (c, s, e + right_ext)
        if self.blocks and read2pos:
            want_left = (read2pos == 5) != self.rev   # 5' end of a + read is its leftmost base
            if want_left:
                c, s, e = self.blocks[0]
                self.blocks = [(c, s, s)]
            else:
                c, s, e = self.blocks[-1]
                self.blocks = [(c, e, e)]

    def frag_strand_negative(self):
        # manual (-s): the strand of the first read is the strand of the fragment
        return (not self.rev) if self.second else self.rev


def hits_for_read(read, ann, strand_mode):
    """{key: {feature positions overlapped}} plus per-feature overlap sets."""
    per_feat = defaultdict(set)
    if read.unmapped:
        return per_feat
    neg = read.frag_strand_negative()
    for chrom, s, e in read.blocks:
        for f in ann.by_chrom.get(chrom, []):
            fid, fc, fstrand, fs, fe, gid = f
            if fe < s or fs > e:
                continue
            if strand_mode:
                fneg = {"+": 0, "-": 1}.get(fstrand, -1)
                ok = (int(neg) == fneg) if strand_mode == 1 else (int(neg) != fneg)
                if not ok:
                    continue
            lo, hi = max(s, fs), min(e, fe)
            per_feat[fid].update(range(lo, hi + 1))
    return per_feat


def fragment_length(reads):
    """Union of the reads' covered reference positions plus insertions.
    DOC-SILENT: an insertion inside a region covered by both mates counts once,
    and only if both mates carry an identical insertion there."""
    mapped = [r for r in reads if not r.unmapped]
    if not mapped:
        return 0
    if len(mapped) == 1:
        return len(mapped[0].covered) + sum(n for _, n in mapped[0].insertions)
    r1, r2 = mapped
    if r1.chrom != r2.chrom:
        return len(r1.covered) + sum(n for _, n in r1.insertions) + len(r2.covered) + sum(n for _, n in r2.insertions)
    union = len(r1.covered | r2.covered)
    both = r1.covered & r2.covered
    ins = 0
    i2 = set(r2.insertions)
    for p, n in r1.insertions:
        if (p in both) or (p - 1 in both):
            if (p, n) in i2:
                ins += n
        else:
            ins += n
    for p, n in r2.insertions:
        if (p in both) or (p - 1 in both):
            continue  # counted above if shared, dropped otherwise
        ins += n
    return union + ins


def assign(reads, ann, opt):
    """reads: [R1] (single-end) or [R1, R2] (paired, R2 may be a synthetic
    unmapped placeholder when only one record exists).  Returns
    (status, {name: count_in_NH_INT_units})."""
    pe = opt.get("pe", False)
    s = opt.get("strand", 0)
    Q = opt.get("Q", 0)
    r1 = reads[0]
    r2 = reads[1] if pe else None

    # --- filters ---------------------------------------------------------------
    # The manual lists: unmapped > read type > singleton > mapping quality >
    # chimeric > fragment length > duplicate > multi-mapping > secondary >
    # split > no features > overlap length > ambiguity.  Single-end mode
    # follows that list.  In paired-end mode the shipped code walks the two
    # records one after the other (in file order) and applies the mapping
    # quality test only while looking at the second record, so the labels of
    # fragments that fail more than one filter differ from the manual's order;
    # with opt["code_order"] the reference reproduces that walk (labels only,
    # the set of counted fragments is the same).
    ends = [r1] if not pe else [r1, r2]
    if not pe:
        if r1.unmapped:
            return "Unassigned_Unmapped", {}
        if Q > 0 and r1.mapq < Q:
            return "Unassigned_MappingQuality", {}
        if opt.get("ignoreDup") and r1.dup:
            return "Unassigned_Duplicate", {}
        if r1.nh > 1 and not opt.get("M"):
            return "Unassigned_MultiMapping", {}
        if r1.secondary and opt.get("primary"):
            return "Unassigned_Secondary", {}
        if opt.get("splitOnly") and not r1.split:
            return "Unassigned_NonSplit", {}
        if opt.get("nonSplitOnly") and r1.split:
            return "Unassigned_Split", {}
    else:
        if r1.unmapped and r2.unmapped:
            return "Unassigned_Unmapped", {}
        if opt.get("B") and (r1.unmapped or r2.unmapped):
            return "Unassigned_Singleton", {}

        def pair_geometry():
            if r1.unmapped or r2.unmapped:
                return None
            same_chrom = r1.chrom == r2.chrom
            opposite = r1.rev != r2.rev
            if same_chrom and opposite:
                if opt.get("P"):
                    tl = abs(r1.rec.get("tlen", 0))
                    if tl > opt.get("D", 600) or tl < opt.get("d", 50):
                        return "Unassigned_FragmentLength"
            elif opt.get("C"):
                # DOC (summary section): different chromosomes or unexpected orientation
                return "Unassigned_Chimera"
            return None

        def mapq_fail():
            # DOC: "For paired-end reads, at least one end should satisfy" -Q
            return Q > 0 and max(r1.mapq, r2.mapq) < Q

        def per_read(r, nonsplit_counter):
            if opt.get("ignoreDup") and r.dup:
                return "Unassigned_Duplicate"
            if r.unmapped:
                return None
            if r.nh > 1 and not opt.get("M"):
                return "Unassigned_MultiMapping"
            if r.secondary and opt.get("primary"):
                return "Unassigned_Secondary"
            if opt.get("splitOnly") and not r.split:
                nonsplit_counter.append(r)
                if opt.get("code_order"):
                    # shipped code: the fragment is dropped only once BOTH records
                    # were seen mapped and non-split, so singletons pass through
                    if len(nonsplit_counter) == 2:
                        return "Unassigned_NonSplit"
            if opt.get("nonSplitOnly") and r.split:
                return "Unassigned_Split"
            return None

        if opt.get("code_order"):
            ns = []
            g = pair_geometry()
            if g:
                return g, {}
            f = per_read(r1, ns)
            if f:
                return f, {}
            if mapq_fail():
                return "Unassigned_MappingQuality", {}
            f = per_read(r2, ns)
            if f:
                return f, {}
        else:
            if mapq_fail():
                return "Unassigned_MappingQuality", {}
            g = pair_geometry()
            if g:
                return g, {}
            if opt.get("ignoreDup") and (r1.dup or r2.dup):
                return "Unassigned_Duplicate", {}
            ns = []
            for r in ends:
                f = per_read(r, ns)
                if f:
                    return f, {}
            if opt.get("splitOnly") and all(not r.split for r in ends if not r.unmapped):
                return "Unassigned_NonSplit", {}

    # --- overlaps ------------------------------------------------------------
    need_len = (opt.get("minOverlap", 1) > 1 or opt.get("fracOverlap", 0) > 0
                or opt.get("largestOverlap") or opt.get("fracOverlapFeature", 0) > 0
                or opt.get("nonOverlap") is not None or opt.get("nonOverlapFeature") is not None)
    per_end = []
    for r in ends:
        per_end.append(hits_for_read(r, ann, s))
    # --fracOverlapFeature / --nonOverlapFeature: per feature, over both ends
    if opt.get("fracOverlapFeature", 0) > 0 or opt.get("nonOverlapFeature") is not None:
        fids = set().union(*[set(h) for h in per_end])
        for fid in fids:
            f = ann.feats[fid]
            flen = f[4] - f[3] + 1
            ov = set()
            for h in per_end:
                ov |= h.get(fid, set())
            thr = ceil3(flen * opt.get("fracOverlapFeature", 0))
            if opt.get("nonOverlapFeature") is not None:
                thr = max(thr, max(0, flen - opt["nonOverlapFeature"]))
            if len(ov) < thr:
                for h in per_end:
                    h.pop(fid, None)
    # meta-feature level: union positions and the set of ends
    keys = {}
    for ei, h in enumerate(per_end):
        for fid, posset in h.items():
            k = ann.key(ann.feats[fid])
            d = keys.setdefault(k, {"ends": set(), "pos": set(), "fid": fid})
            d["ends"].add(ei)
            d["pos"] |= posset
    if not keys:
        return "Unassigned_NoFeatures", {}

    O = opt.get("O", False)
    scores = {}
    if need_len:
        flen = fragment_length(ends)
        thr = max(opt.get("minOverlap", 1), ceil3(opt.get("fracOverlap", 0) * flen))
        if opt.get("nonOverlap") is not None:
            thr = max(thr, max(0, flen - opt["nonOverlap"]))
        for k, d in keys.items():
            ov = len(d["pos"])
            if opt.get("largestOverlap"):
                sc = ov * 2 + (1 if (len(d["ends"]) == 2 and not O) else 0)
            else:
                sc = 1 if O else len(d["ends"])
            if ov < thr:
                sc = 0
            scores[k] = sc
        if opt.get("largestOverlap"):
            best = max(scores.values())
            scores = {k: (v if v == best else 0) for k, v in scores.items()}
    else:
        for k, d in keys.items():
            scores[k] = 1 if O else len(d["ends"])
    passing = {k: v for k, v in scores.items() if v >= 1}
    if not passing:
        return "Unassigned_Overlapping_Length", {}
    best = max(passing.values())
    winners = [k for k, v in passing.items() if v == best]

    # --- count value ---------------------------------------------------------
    nh = max(r.nh for r in ends)
    unit = NH_INT
    if opt.get("fraction") and not opt.get("primary"):
        unit = NH_INT // nh if nh > 1 else NH_INT
    if O:
        share = unit // len(winners) if opt.get("fraction") else unit
        return "Assigned", {ann.name(ann.feats[keys[k]["fid"]]): share for k in winners}
    if len(winners) == 1:
        k = winners[0]
        return "Assigned", {ann.name(ann.feats[keys[k]["fid"]]): unit}
    return "Unassigned_Ambiguity", {}
