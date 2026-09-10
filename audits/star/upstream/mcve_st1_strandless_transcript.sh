#!/bin/bash
# Minimal reproduction: a transcript whose GTF strand column is '.' gets its strand
# inverted in Aligned.toTranscriptome.out.bam, and its gene is not counted by STARsolo
# with --soloStrand Forward.  The two GTFs below differ only in the strand column.
# usage: bash mcve_st1_strandless_transcript.sh /path/to/STAR      (needs samtools)
set -e
STAR=${1:-STAR}
T=$(mktemp -d); cd "$T"
# 6-kb random genome; one two-exon transcript, exons 1001-1400 and 2001-2400, GT..AG intron
awk 'BEGIN{srand(1); n["0"]="A";n["1"]="C";n["2"]="G";n["3"]="T"; s="";
  for(i=1;i<=6000;i++){s=s n[int(rand()*4)]};
  s=substr(s,1,1400) "GT" substr(s,1403,598) "AG" substr(s,2003);
  print ">chr1"; for(i=1;i<=6000;i+=80) print substr(s,i,80);
  print substr(s,1001,400) substr(s,2001,400) > "tr.txt"}' > genome.fa
TR=$(cat tr.txt); Q=$(printf 'I%.0s' $(seq 100))
# one sense read and one antisense read, both wholly inside exon 1 of the transcript
printf "@sense\n%s\n+\n%s\n@anti\n%s\n+\n%s\n" \
  "${TR:20:100}" "$Q" "$(echo ${TR:60:100} | rev | tr ACGT TGCA)" "$Q" > reads.fq
# four sense cDNA reads with one cell barcode and four UMIs, for STARsolo
printf "@c1\n%s\n+\n%s\n@c2\n%s\n+\n%s\n@c3\n%s\n+\n%s\n@c4\n%s\n+\n%s\n" \
  "${TR:30:100}" "$Q" "${TR:130:100}" "$Q" "${TR:230:100}" "$Q" "${TR:330:100}" "$Q" > cdna.fq
CB=ACGTACGTACGTACGT; QB=$(printf 'I%.0s' $(seq 26))
printf "@c1\n${CB}AACCGGTTAC\n+\n%s\n@c2\n${CB}CCGGTTAACG\n+\n%s\n@c3\n${CB}GGTTAACCGT\n+\n%s\n@c4\n${CB}TTAACCGGTA\n+\n%s\n" \
  "$QB" "$QB" "$QB" "$QB" > bc.fq
"$STAR" --version
for strand in + .; do
  d=g_$strand
  printf 'chr1\tm\texon\t1001\t1400\t.\t%s\t.\tgene_id "G"; transcript_id "T";\nchr1\tm\texon\t2001\t2400\t.\t%s\t.\tgene_id "G"; transcript_id "T";\n' $strand $strand > $d.gtf
  "$STAR" --runMode genomeGenerate --genomeDir $d --genomeFastaFiles genome.fa \
          --sjdbGTFfile $d.gtf --sjdbOverhang 99 --genomeSAindexNbases 4 --outFileNamePrefix $d/ > /dev/null
  "$STAR" --genomeDir $d --readFilesIn reads.fq --quantMode TranscriptomeSAM \
          --outSAMtype None --outFileNamePrefix tr_$d/ > /dev/null
  "$STAR" --genomeDir $d --readFilesIn cdna.fq bc.fq --soloType CB_UMI_Simple \
          --soloCBwhitelist None --soloStrand Forward --soloFeatures Gene GeneFull \
          --outSAMtype None --outFileNamePrefix solo_$d/ > /dev/null
  echo "--- GTF strand column '$strand'"
  echo "Aligned.toTranscriptome.out.bam  (QNAME FLAG POS SEQ-vs-transcript):"
  samtools view tr_$d/Aligned.toTranscriptome.out.bam | while read -r q f r p mapq cig rn pn tl seq rest; do
    # SAM stores SEQ on the reference (here transcript) forward strand, whatever the FLAG
    exp=${TR:$((p-1)):100}
    [ "$seq" = "$exp" ] && m="matches the transcript at this position" || m="DOES NOT MATCH the transcript at this position"
    echo "    $q flag=$f pos=$p  SEQ $m"
  done
  for ft in Gene GeneFull; do
    echo "  STARsolo --soloStrand Forward $ft UMI count: $(grep -v '^%' solo_$d/Solo.out/$ft/raw/matrix.mtx | tail -n +2 | awk '{s+=$3} END{print s+0}')"
  done
done
cd /; rm -rf "$T"
