#!/usr/bin/env python3
"""BC1 on real data, part 2: the same two samples and builds, every mpileup record with at least
two alternate reads (the sites a minor-variant analysis looks at), counting scores that differ,
differ by one or more, and fall on different sides of a -3 filter threshold."""
import subprocess, collections, sys
S = "/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/bcftools"
BASE, PATCHED = f"{S}/src-base/bcftools", f"{S}/src/bcftools"
TAGS = ["MQBZ", "BQBZ", "RPBZ", "SCBZ", "MQSBZ"]
def raw(binary, bams, d):
    p = subprocess.run([binary, "mpileup", "-f", "genome.fasta", "-d", str(d), "-a", "INFO/AD", "-Ov"] + bams, capture_output=True, text=True)
    recs = {}
    for line in p.stdout.splitlines():
        if line[0] == "#": continue
        f = line.split("\t"); info = dict(kv.split("=", 1) for kv in f[7].split(";") if "=" in kv)
        ad = [int(x) for x in info["AD"].split(",")]; alt = sum(ad[1:]) if f[4] != "<*>" else 0
        recs[f[1]] = dict(dp=int(info["DP"]), alt=alt, af=alt / max(1, sum(ad)), **{t: float(info[t]) for t in TAGS if t in info})
    return recs
for label, bams, d in [("sample1 -d 1e6", ["sample1.bam"], 1000000), ("sample2 -d 1e6", ["sample2.bam"], 1000000), ("sample1+sample2 -d 1e6", ["sample1.bam", "sample2.bam"], 1000000), ("sample1+sample2 default -d 250", ["sample1.bam", "sample2.bam"], 250)]:
    b, p = raw(BASE, bams, d), raw(PATCHED, bams, d)
    sites = [k for k in b if b[k]["alt"] >= 2]          # sites with at least two alternate reads (minor-variant candidates)
    deep = [k for k in sites if b[k]["dp"] >= 1291]
    ch = collections.Counter(); big = collections.Counter(); cross = collections.Counter(); ex = {}
    for k in sites:
        for t in TAGS:
            if t in b[k] and t in p[k]:
                dlt = abs(b[k][t] - p[k][t])
                if dlt > 1e-6: ch[t] += 1
                if dlt >= 1: big[t] += 1
                if (b[k][t] < -3) != (p[k][t] < -3): cross[t] += 1
                if dlt > ex.get(t, (0,))[0]: ex[t] = (dlt, k, b[k][t], p[k][t], b[k]["dp"], b[k]["alt"], b[k]["af"])
    print(f"\n[{label}] positions with >= 2 alt reads: {len(sites)}, of which DP >= 1291: {len(deep)}")
    print(f"  scores that differ: {dict(ch) or 'none'};  differ by >= 1: {dict(big) or 'none'};  cross a -3 threshold: {dict(cross) or 'none'}")
    for t, e in sorted(ex.items(), key=lambda kv: -kv[1][0])[:5]:
        print(f"    {t}: pos {e[1]} DP {e[4]} alt {e[5]} (AF {e[6]:.3f}): base {e[2]:.3f} -> patched {e[3]:.3f}")
