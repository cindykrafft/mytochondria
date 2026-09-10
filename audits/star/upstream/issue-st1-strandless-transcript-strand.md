Title: TranscriptomeSAM inverts the strand for transcripts whose GTF strand is '.', and stranded STARsolo gives such genes zero counts

<!-- alexdobin/STAR has no issue form or issue template; CONTRIBUTING.md ("How Do I
     Submit A (Good) Bug Report?") asks for: a clear title, the exact steps and command,
     copy-pasteable snippets, Log.out, the observed behaviour, the expected behaviour,
     system information, and whether it reproduces reliably. The body follows that order. -->

### Summary

A GTF exon line whose strand column is `.` — the value the GTF/GFF specification
prescribes for a feature with no strand — produces two wrong outputs, silently:

1. every record for that transcript in `Aligned.toTranscriptome.out.bam` carries the
   **opposite** `0x10` flag to the one its POS and SEQ imply, so the record is internally
   inconsistent (SEQ no longer matches the transcript at the reported POS) and a
   strand-aware quantifier — `RSEM --forward-prob`, salmon or eXpress in a stranded
   library type — keeps exactly the wrong half of the reads;
2. STARsolo with `--soloStrand Forward` (or `Reverse`) gives that gene **zero** counts in
   `Gene`, `GeneFull` and `GeneFull_Ex50pAS`.

`--quantMode GeneCounts` already gets this right: `Transcriptome_geneCountsAddAlign.cpp`
tests `str1<2` with the comment *"genes w/o strand will accept reads from both strands"*.
The transcriptome and STARsolo paths test only for strand code `1`, so code `0` (`.`) is
treated as the minus strand.

### Steps to reproduce

The script below is self-contained: it builds a 6-kb random genome with one two-exon
transcript (GT/AG intron), maps one sense and one antisense 100-nt read plus four sense
cDNA reads with cell barcodes, and does it twice against two GTFs that differ **only in
the strand column** (`+` and `.`). It needs `samtools` on `PATH` and nothing else.

```sh
#!/bin/bash
set -e
STAR=${1:-STAR}
T=$(mktemp -d); cd "$T"
awk 'BEGIN{srand(1); n["0"]="A";n["1"]="C";n["2"]="G";n["3"]="T"; s="";
  for(i=1;i<=6000;i++){s=s n[int(rand()*4)]};
  s=substr(s,1,1400) "GT" substr(s,1403,598) "AG" substr(s,2003);
  print ">chr1"; for(i=1;i<=6000;i+=80) print substr(s,i,80);
  print substr(s,1001,400) substr(s,2001,400) > "tr.txt"}' > genome.fa
TR=$(cat tr.txt); Q=$(printf 'I%.0s' $(seq 100))
printf "@sense\n%s\n+\n%s\n@anti\n%s\n+\n%s\n" \
  "${TR:20:100}" "$Q" "$(echo ${TR:60:100} | rev | tr ACGT TGCA)" "$Q" > reads.fq
printf "@c1\n%s\n+\n%s\n@c2\n%s\n+\n%s\n@c3\n%s\n+\n%s\n@c4\n%s\n+\n%s\n" \
  "${TR:30:100}" "$Q" "${TR:130:100}" "$Q" "${TR:230:100}" "$Q" "${TR:330:100}" "$Q" > cdna.fq
CB=ACGTACGTACGTACGT; QB=$(printf 'I%.0s' $(seq 26))
printf "@c1\n${CB}AACCGGTTAC\n+\n%s\n@c2\n${CB}CCGGTTAACG\n+\n%s\n@c3\n${CB}GGTTAACCGT\n+\n%s\n@c4\n${CB}TTAACCGGTA\n+\n%s\n" \
  "$QB" "$QB" "$QB" "$QB" > bc.fq
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
  samtools view tr_$d/Aligned.toTranscriptome.out.bam | while read -r q f r p mapq cig rn pn tl seq rest; do
    exp=${TR:$((p-1)):100}
    [ "$seq" = "$exp" ] && m="matches the transcript at this position" || m="DOES NOT MATCH the transcript at this position"
    echo "    $q flag=$f pos=$p  SEQ $m"
  done
  for ft in Gene GeneFull; do
    echo "  STARsolo --soloStrand Forward $ft UMI count: $(grep -v '^%' solo_$d/Solo.out/$ft/raw/matrix.mtx | tail -n +2 | awk '{s+=$3} END{print s+0}')"
  done
done
```

### Observed behaviour

```
--- GTF strand column '+'
Aligned.toTranscriptome.out.bam  (QNAME FLAG POS SEQ-vs-transcript):
    sense flag=0 pos=21  SEQ matches the transcript at this position
    anti flag=16 pos=61  SEQ matches the transcript at this position
  STARsolo --soloStrand Forward Gene UMI count: 4
  STARsolo --soloStrand Forward GeneFull UMI count: 4
--- GTF strand column '.'
Aligned.toTranscriptome.out.bam  (QNAME FLAG POS SEQ-vs-transcript):
    sense flag=16 pos=21  SEQ DOES NOT MATCH the transcript at this position
    anti flag=0 pos=61  SEQ DOES NOT MATCH the transcript at this position
  STARsolo --soloStrand Forward Gene UMI count: 0
  STARsolo --soloStrand Forward GeneFull UMI count: 0
```

The positions are the same in both runs; only the flag differs. Since STAR converted the
coordinates as if the transcript were on `+` (`Transcriptome_quantAlign.cpp`,
`alignToTranscript` transforms only when `trStr1==2`) but set the flag as if it were on
`-`, the SEQ written to the record is no longer the transcript's own sequence at that
POS. STAR itself does not warn, and nothing in `Log.out` mentions the strand column.

### Expected behaviour

A transcript with no annotated strand should behave in the transcriptome BAM and in
STARsolo the way it already behaves in `--quantMode GeneCounts`: treated as `+` for the
coordinate transform and the flag, and accepting reads from both strands when a
strandedness is requested. Concretely, both blocks above should read as the `+` block
does.

### Scope, and how it scales

On a larger synthetic annotation (14 genes, one of them strandless, 10,299 mapped
single-end reads) **400 of 11,189** transcriptome records differ from an independent
reference implementation, and every one of the 400 is a strand flag on the strandless
transcript; paired-end, 800 of 20,748. With 20 sense and 20 antisense reads on that
transcript, `RSEM --forward-prob 1` would keep 10 of 20 either way — but on the `.`
annotation it keeps the antisense ten.

GENCODE, Ensembl and RefSeq give every feature `+` or `-`, so stock human and mouse runs
are unaffected. `.` shows up in custom GTFs built from BED or from strand-agnostic
evidence, repeat/TE annotations, some ncRNA and enhancer catalogues, and GFF3 converted
by tools that preserve `.` — for example #1922, where a user built a GTF from a BED file
and asked what STAR does with the strand column.

### Versions

Reproduced with identical output on **2.7.11b** (the current release; `master` @
`b1edc12`, built here from `source/` with `make STAR`), **2.7.10a** and **2.7.9a**, both
built from their release tags. The line responsible
(`aTall[nAtr].Str = trStr[tr1]==1 ? aG.Str : 1-aG.Str; //TODO strandedness`) predates all
three, so older releases are very likely affected as well — not executed, so not claimed.

### Where it is in the source (2.7.11b / `master` @ `b1edc12`)

- `source/GTF.cpp:138-143` — `+` → 1, `-` → 2, anything else (`.`) → 0.
- `source/Transcriptome_geneCountsAddAlign.cpp:32-36` — the path that gets it right.
- `source/Transcriptome_quantAlign.cpp:107` — transcriptome BAM strand, inverted for 0.
- `source/Transcriptome_classifyAlign.cpp:208` — STARsolo `Gene`.
- `source/Transcriptome_geneFullAlignOverlap.cpp:24` and `:43` — STARsolo `GeneFull`.
- `source/Transcriptome_geneFullAlignOverlap_ExonOverIntron.cpp:30` — `GeneFull_Ex50pAS`.
- `source/Transcriptome_alignExonOverlap.cpp:58` — compares against `trStr[tr1]-1`, which
  is `-1` for code 0, so a strandless transcript never matches.

### What shrinking the example revealed

The first version of the reproduction used a whole simulated annotation and reported a
count difference, which looked like a multimapper or an overlap problem. Cutting it down
to a *single* transcript and mapping the *same* reads against two GTFs that differ only
in one character isolated it completely: the positions are identical and only the flag
moves, which is what showed that the coordinate transform and the flag disagree with each
other rather than both following a (defensible) "treat `.` as `-`" convention. Dropping
the second exon still reproduces it, so splicing is not involved; the intron is kept only
so the example also covers a spliced transcript.

### Environment

- OS: Linux 6.18 (Ubuntu 24.04 container), x86_64
- Compiler: g++ (Ubuntu 13.3.0), `make STAR` in `source/`, zlib, bundled htslib
- Reproduces reliably: every run, single- and paired-end, `--runThreadN 1` and higher.
- `Log.out` contains no ERROR/WARNING/SOLUTION lines in any of the runs above.

A patch with a fix and a regression test
(`extras/tests/scripts/testStrandlessTranscript.sh`) is ready and can be sent as a PR if
you would like it.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/star)

---
_Generated by [Claude Code](https://claude.ai/code)_
