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
