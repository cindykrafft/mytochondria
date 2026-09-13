Title: Transcripts with undefined GTF strand ('.') get inverted strand flags and reverse-complemented sequences in Aligned.toTranscriptome.out.bam, and lose their sense reads in STARsolo --soloStrand Forward

<!-- alexdobin/STAR has no issue template; CONTRIBUTING.md asks for: exact steps and commands, copy-pasteable snippets, observed behaviour, expected behaviour and why, system information, reproducibility, Log.out attached -->

**Summary.** A transcript whose strand column in the GTF is `.` is stored with strand 0 (`GTF.cpp:138-144`). `Transcriptome::quantAlign` sets the transcriptomic strand with `trStr[tr1]==1 ? aG.Str : 1-aG.Str` (`Transcriptome_quantAlign.cpp:107`), so a `.` transcript is treated like a `-` transcript there, while `alignToTranscript` converts the coordinates only for `trStr1==2`. The result is a record at the `+`-strand position with the strand flag inverted and the sequence reverse-complemented, i.e. a read that does not match the transcript at its own position. The same expression in `Transcriptome_classifyAlign.cpp:208`, `Transcriptome_geneFullAlignOverlap.cpp:24`, `Transcriptome_geneFullAlignOverlap_ExonOverIntron.cpp:30` and `Transcriptome_alignExonOverlap.cpp:58` makes STARsolo `--soloStrand Forward` (the default) drop every sense read of a `.` gene. `--quantMode GeneCounts` handles `.` genes deliberately ("genes w/o strand will accept reads from both strands", `Transcriptome_geneCountsAddAlign.cpp:34`) and is correct. Undefined strands are common in StringTie output (single-exon transcripts) and in merged/de novo annotations used with STAR + RSEM/salmon.

**Steps to reproduce.** The script below builds a 3-kb genome with two identical two-exon gene structures, `TP` on `+` and `TD` on `.`, eight 60-bp reads (exonic and junction-spanning, forward and reverse-complemented, from each), and runs STAR 2.7.11b with defaults plus `--quantMode TranscriptomeSAM`, then STARsolo with one cell barcode.

```sh
STAR=/path/to/STAR
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
mkdir gidx
$STAR --runMode genomeGenerate --genomeDir gidx --genomeFastaFiles g.fa --sjdbGTFfile g.gtf --sjdbOverhang 59 --genomeSAindexNbases 4 --outFileNamePrefix gidx/
$STAR --genomeDir gidx --readFilesIn r.fq --outFileNamePrefix tr/ --outSAMtype SAM --quantMode TranscriptomeSAM
samtools view tr/Aligned.toTranscriptome.out.bam | cut -f 1-4,6,10
```

**Observed** (STAR 2.7.11b; identical output from 2.7.10a and 2.7.9a). The genomic alignments are right for all eight reads (`TP_fwd_270` and `TD_fwd_270` are `30M300N30M` at 471 and 1971, forward; the `_rev_` reads reverse). In the transcriptome BAM the `TP` records are as expected, but every `TD` record has the opposite flag and the reverse-complemented sequence at the same position:

```
TP_fwd_100  0   TP  101  60M  GTACGTACGTACGGCGTATAGCGGTCGCCCATTAAAGCTGATAAATATCTCCTTGTCCTG
TP_rev_100  16  TP  101  60M  GTACGTACGTACGGCGTATAGCGGTCGCCCATTAAAGCTGATAAATATCTCCTTGTCCTG
TP_fwd_270  0   TP  271  60M  AACATCCTAGACAGACGCTATACATTGCACCCCGGATTCTGATTTTCGAGTGTTTGAAAC
TP_rev_270  16  TP  271  60M  AACATCCTAGACAGACGCTATACATTGCACCCCGGATTCTGATTTTCGAGTGTTTGAAAC
TD_fwd_100  16  TD  101  60M  GACCAGGACTAATCTTGGGCCGATATATTTTCATAACACGGTGAGGAACTCGTGGGCCAA
TD_rev_100  0   TD  101  60M  GACCAGGACTAATCTTGGGCCGATATATTTTCATAACACGGTGAGGAACTCGTGGGCCAA
TD_fwd_270  16  TD  271  60M  GTATGGTTGGGCGAGTAAGATAGTAGTTCGGCACTACTCTCCTCTGACGACCATTTCCTA
TD_rev_270  0   TD  271  60M  GTATGGTTGGGCGAGTAAGATAGTAGTTCGGCACTACTCTCCTCTGACGACCATTTCCTA
```

**Expected.** `TD_fwd_100` is an exact substring of transcript TD starting at base 101, so its record should be flag 0 at 101 with the read sequence, exactly like `TP_fwd_100` (and `TD_rev_100` flag 16 with the same sequence); the position is right but the sequence stored is the reverse complement of the transcript at that position. RSEM/salmon score such records against the transcript sequence, so the reads of every `.` transcript are mismatched at all 60 (or 100+) bases. A larger check (300 100-bp single-end and 200 2x75 paired-end reads per transcript on a 16-transcript synthetic annotation, compared with an independent projection of the genomic alignments onto the transcripts) gives the same picture: every read on the two `.` transcripts differs in flag and sequence, 0 of the reads on the 14 `+`/`-` transcripts differ.

**STARsolo counterpart.** With barcode reads added (one cell, distinct UMIs) and
`--soloType CB_UMI_Simple --soloFeatures Gene GeneFull --soloStrand Forward`, the sum of the count matrix is gTP 2 (the two forward reads, as expected) and gTD 2 — but the two counted gTD reads are the *reverse* ones: with 300 sense reads per gene, a `.` gene gets 0 under `Forward` and 300 under `Reverse` for Gene, GeneFull and GeneFull_ExonOverIntron, and 0 under both for GeneFull_Ex50pAS, while `--quantMode GeneCounts` column 3 on the same reads counts 300.

**Shrinking.** One `+`/`.` pair of identical structure with one forward and one reverse read is enough; the defect does not depend on splicing (the exonic reads show it) or on read orientation; the transcriptome position and CIGAR are always right, only the flag and sequence are inverted, which points at the strand assignment after the coordinate conversion.

**Cause and fix.** `Transcriptome_quantAlign.cpp:107`: `trStr[tr1]==1 ? aG.Str : 1-aG.Str` should invert only for `trStr==2`, so that `.` follows the `+` convention used by the coordinate conversion. For STARsolo, genes with undefined strand should accept reads from both strands under `Forward`/`Reverse`, as GeneCounts does. A patch with a self-contained regression test (`extras/tests/scripts/testUndefinedStrand.sh`, fails on 2.7.11b, passes with the fix) and a `CHANGES.md` entry is ready and will follow as a PR.

**System.** Linux 6.18 (Ubuntu 24.04 container), x86_64, gcc 13.3.0, `make STAR` from the 2.7.11b tag; 4 CPUs, 15 GB RAM, local disk; reproduces every time (also on 2.7.10a and 2.7.9a built from their tags). `Log.out` of the `tr/` run has no ERROR/WARNING lines (attached).

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/star)

---
_Generated by [Claude Code](https://claude.ai/code)_
