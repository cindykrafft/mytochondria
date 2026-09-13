#!/bin/bash
# MCVE for the STAR issue "Aligned.toTranscriptome.out.bam: strand flag inverted and sequence
# reverse-complemented for transcripts whose GTF strand is '.'" (and the STARsolo counterpart).
# Usage: mcve_st1_transcriptome_strandless.sh /path/to/STAR    (samtools in PATH)
# Two identical two-exon gene structures on a 3-kb pseudo-random genome (deterministic LCG in awk):
# TP on '+' (exons 201-500, 801-1100) and TD on '.' (1701-2000, 2301-2600), GT..AG at both introns.
# Reads: 60-mers at transcript offsets 100 (exonic) and 270 (junction-spanning), forward and
# reverse-complemented, from each transcript. The transcriptome records of TD must equal those of TP.
set -e
STAR=${1:?STAR binary}
T=$(mktemp -d); cd "$T"
awk 'BEGIN{x=12345; s=""; for(i=0;i<3000;i++){x=(x*1103515245+12345)%2147483648; s=s substr("ACGT",int(x/65536)%4+1,1)};
  s=substr(s,1,499) "CGT" substr(s,503,296) "AGC" substr(s,802);
  s=substr(s,1,1999) "CGT" substr(s,2003,296) "AGC" substr(s,2302);
  print ">chr1"; print s}' > g.fa
printf 'chr1\tt\texon\t201\t500\t.\t+\t.\tgene_id "gTP"; transcript_id "TP";\nchr1\tt\texon\t801\t1100\t.\t+\t.\tgene_id "gTP"; transcript_id "TP";\n' > g.gtf
printf 'chr1\tt\texon\t1701\t2000\t.\t.\t.\tgene_id "gTD"; transcript_id "TD";\nchr1\tt\texon\t2301\t2600\t.\t.\t.\tgene_id "gTD"; transcript_id "TD";\n' >> g.gtf
awk 'NR==2{g=$0; n=split("TP 201 500 801 1100,TD 1701 2000 2301 2600",tr,",");
  for(i=1;i<=n;i++){split(tr[i],f," "); t=substr(g,f[2],f[3]-f[2]+1) substr(g,f[4],f[5]-f[4]+1);
    for(o=100;o<=270;o+=170){r=substr(t,o+1,60); rc=""; for(k=60;k>=1;k--){c=substr(r,k,1); rc=rc (c=="A"?"T":c=="C"?"G":c=="G"?"C":"A")};
      q="IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII";
      print "@" f[1] "_fwd_" o "\n" r "\n+\n" q; print "@" f[1] "_rev_" o "\n" rc "\n+\n" q}}}' g.fa > r.fq
awk 'BEGIN{split("ACACACACACAC AGAGAGAGAGAG ATATATATATAT CGCGCGCGCGCG CTCTCTCTCTCT GTGTGTGTGTGT AACCAACCAACC GGTTGGTTGGTT",u," ")} NR%4==1{print $0; print "ACGTACGTACGTACGT" u[(NR-1)/4+1]; print "+"; print "IIIIIIIIIIIIIIIIIIIIIIIIIIII"}' r.fq > b.fq
echo ACGTACGTACGTACGT > wl.txt
mkdir gidx
"$STAR" --runMode genomeGenerate --genomeDir gidx --genomeFastaFiles g.fa --sjdbGTFfile g.gtf --sjdbOverhang 59 --genomeSAindexNbases 4 --outFileNamePrefix gidx/ > /dev/null
"$STAR" --genomeDir gidx --readFilesIn r.fq --outFileNamePrefix tr/ --outSAMtype SAM --quantMode TranscriptomeSAM > /dev/null
echo "STAR $("$STAR" --version)"
echo "--- genomic alignments (name flag chr pos CIGAR)"
grep -v '^@' tr/Aligned.out.sam | awk '{print $1, $2, $3, $4, $6}'
echo "--- Aligned.toTranscriptome.out.bam (name flag transcript pos CIGAR SEQ): TD lines must equal TP lines"
samtools view tr/Aligned.toTranscriptome.out.bam | awk '{print $1, $2, $3, $4, $6, $10}'
"$STAR" --genomeDir gidx --readFilesIn r.fq b.fq --outFileNamePrefix solo/ --outSAMtype None --soloType CB_UMI_Simple --soloCBwhitelist wl.txt --soloUMIlen 12 \
        --soloFeatures Gene GeneFull --soloStrand Forward > /dev/null
echo "--- STARsolo --soloStrand Forward, reads counted (gene index 1 = gTP, 2 = gTD; 4 reads each, 2 forward + 2 reverse)"
for f in Gene GeneFull; do echo "$f: $(awk 'NR>3{c[$1]+=$3} END{printf "gTP %d, gTD %d", c[1], c[2]}' solo/Solo.out/$f/raw/matrix.mtx)"; done
cd /; rm -rf "$T"
