Title: (comment on #2595) MCVE script; your reproduction is the same one-bin condition; refactor checked

<!-- Reply to jkbonfield (CONTRIBUTOR) on PR #2595, 2026-09-28 10:18 (edited 10:19) and 10:33 UTC. Thread read in full 2026-09-28 (helper artifact "Mytochondria threads bcftools 2595"): two comments, no reviews, no review threads, no checks on 83b78889; issue #2594 has no comments. He asks for the MCVE script (the issue names it but it was never attached), reports that his own reproduction changes BQBZ between depth 1292 and 1293 but not MQBZ, notes that int64 still overflows at 2^21 per bin, and posts a Claude-generated refactor that accumulates N^3 - sum(p^3) as 3*S*p*(S+p) in double ("I'm still evaluating whether this is a better alternative").
Facts checked 2026-09-28 (scratch builds of develop edf7fd96, PR 83b78889, and PR + his calc_mwu_biasZ, all on HTSlib develop 7c5e3e7):
- His generator never resets $seq/$qual, so from read2 on every read carries C at 'i' whatever its MQ; with srand(1) only read0/read1 are A. The BQ bin holds d-2 reads -> reaches 1291 at d=1293. MQ splits 638/654 (d=1292), 639/654 (1293), 641/659 (1300).
- d=1292: BQBZ 35.9305 on all three; d=1293: dev 1.73374, PR/refactor 35.9444; d=1300: dev 1.74783, PR/refactor 36.0416; MQBZ unchanged on all.
- d=2097152: PR and refactor BQBZ 1448.15; d=2097160: PR 1.73206, refactor 1448.16.
- MCVE: refactor -36.5924 (1300) / -36.4555 (1290) = PR.
- make test with the refactor (tree = PR + refactor): 2488 passed, 0 failed.
- ../verify/bc1_mpileup_mwu_biasZ_int_overflow.py on the refactor build: 31 ok, 0 affected; output identical to the PR build.
- Random histograms (2,000,000 draws, 1,911,943 finite pairs, some bins 100k-500k): max |diff| 6.5e-9, max relative 9.7e-12, no HUGE_VAL mismatches. Every caller passes do_Z=1.
Do not change the branch until jkbonfield says which he prefers; a replacement commit needs your sign-off (agents may not add it) and attribution for his code. -->

Thanks for digging into this. Here's the script. It takes a bcftools binary and the number of reference reads: 1300 shows the problem, 1290 doesn't.

```sh
#!/bin/sh
# Minimal reproduction: bcftools mpileup INFO/MQBZ once one MAPQ bin holds >= 1291 reads.
# Usage: sh mcve_mpileup_mqbz_overflow.sh /path/to/bcftools [NREF]   (NREF defaults to 1300; 1290 is correct)
set -e
BCF=${1:-bcftools}; NREF=${2:-1300}; NALT=40
D=$(mktemp -d); cd "$D"
# 300-bp reference "ACGTACGT..."; the site is 1-based 150 (REF C); alt reads carry T there.
awk 'BEGIN{s=""; for(i=0;i<300;i++) s=s substr("ACGT",i%4+1,1); print ">ref"; print s}' > ref.fa
printf 'ref\t300\t5\t300\t301\n' > ref.fa.fai
awk -v nref=$NREF -v nalt=$NALT 'BEGIN{
  for(i=0;i<300;i++) ref=ref substr("ACGT",i%4+1,1);
  q=""; for(i=0;i<50;i++) q=q "I";
  print "@HD\tVN:1.6\tSO:coordinate"; print "@SQ\tSN:ref\tLN:300";
  n=nref+nalt; step=int(n/nalt); a=0;
  for(i=0;i<n;i++){
    start=101+int(i*49/n); seq=substr(ref,start,50);      # sorted starts 101..149; every read covers 150
    mq=60; if(i%step==0 && a<nalt){ a++; mq=30; k=150-start+1; seq=substr(seq,1,k-1) "T" substr(seq,k+1) }
    printf "r%d\t%d\tref\t%d\t%d\t50M\t*\t0\t0\t%s\t%s\n", i, (i%2)*16, start, mq, seq, q
  }}' > reads.sam
"$BCF" mpileup -f ref.fa -B -d 100000 reads.sam 2>mpileup.err | awk '$2==150' | cut -f 2,4,5,8 | tr ';' '\n' | grep -E '^150|^DP=|MQBZ' | tr '\n' ' '; echo
# Expected: the tie-corrected Mann-Whitney U Z-score of the MAPQ bins (ref reads: bin 59, alt reads: bin 30).
awk -v na=$NREF -v nb=$NALT 'BEGIN{ N=na+nb; U=0; m=na*nb/2; T=(na^3-na)+(nb^3-nb);
  v=na*nb/12*((N+1)-T/(N*(N-1))); printf "expected MQBZ=%.4f (U=%d, mean=%d, tie-corrected var=%.2f)\n", (U-m)/sqrt(v), U, m, v }'
"$BCF" --version | head -1
cd /; rm -rf "$D"
```

I think your reproduction hits the same condition, just in BQ instead of MQ. In the perl one-liner `$seq` and `$qual` aren't reset inside the loop. Once the first MQ 60 read has set the `C`/`i` at position 6, every later read carries it whatever its MQ. With `srand(1)` only `read0` and `read1` are `A`, so at depth d one base-quality bin holds d−2 reads, and that reaches 1291 at d=1293. The MQ values split about 640/654 between MQ 1 and MQ 60, so neither MQ bin gets near 1291, and MQBZ is the same on all three builds. My numbers are the same as yours: at d=1293, BQBZ is 1.73374 on develop and 35.9444 with the PR; at d=1300 it's 1.74783 and 36.0416.

You're right that MQ isn't special. Any of the Z annotations overflows once one of its bins holds 1291 or more reads. I used MQ in the example because, with most reads at MAPQ 60, the whole reference depth tends to sit in one bin, so on real data it's the easiest one to hit.

I built your refactor on develop and checked it:

- `make test`: 2488 passed, 0 failed (with this PR's regression test in the tree).
- The script above: MQBZ −36.5924 at 1300 reads and −36.4555 at 1290, the same as the PR and as the tie-corrected value.
- Your reproduction: identical to the PR at d=1292, 1293 and 1300. At d=2097160 it gives BQBZ 1448.16, where the PR drops to 1.73206, as you found.
- Our harness against scipy's asymptotic tie-corrected Mann–Whitney (31 cases, including a 48-sample run with default BAQ): all agree.
- Against the PR's int64 version on about 1.9 million random histograms, some with bins of 100k–500k reads: the largest relative difference is about 1e-11, and both return HUGE_VAL in the same cases.

So I think yours is better: it removes the cube instead of moving the limit. I'm happy to replace the change in this PR with your version and keep the regression test and the NEWS entry, or to close this PR if you'd rather commit it yourself. If I update the PR, how would you like your part attributed?

---
_Generated by [Claude Code](https://claude.ai/code)_
