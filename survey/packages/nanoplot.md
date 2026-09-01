# NanoPlot

- **Category:** genomics
- **Papers in survey:** 9
- **Journals:** Nature (4), PNAS (4), Cell (1)
- **Years:** 2022 (1), 2023 (2), 2024 (1), 2025 (2), 2026 (3)
- **Versions named:** 1.46.0 (1), 1.41.6 (1), 1.42.0 (1), 1.30.1 (1), 1.40.0 (1), 1.29.1 (1)
- **Pipeline stages it appears in:** differential/statistical testing (3), quality control (1), alignment/mapping (1)

## Papers

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Version used: **1.29.1**
- Evidence: .../zenodo.7759428 https://github.com/hilgers-lab/LASER R 4.1.1 N/A https://www.R-project.org/ Minimap2 v2.17-r941 Li 87 https://github.com/lh3/minimap2 NanoPlot 1.29.1 N/A https://github.com/wdecoster/NanoPlot guppy-5.0.7 model: dna_r9.4.1_450bps_sup.cfg Oxford Nanopore https://github.com/nanoporetech/pyguppyclient snakePipes v1.2.2 Bhardwaj et al.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **1.42.0**
- Evidence: Basic statistics of reads were obtained with NanoStat and NanoPlot (v.1.42.0) 81 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: NanoPlot 77 (v.1.41.6) was used to evaluate sequencing quality per sample with default parameters.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Natural maternal immunity protects neonates from Escherichia coli sepsis. (Nature 2026)

- DOI: 10.1038/s41586-026-10225-z | PMCID: PMC13108393 | PMID: 41813901
- Version used: **1.46.0**
- Evidence: Raw reads were quality-assessed using FastQC (v.0.12.1) and NanoPlot (v.1.46.0) 86 .
- Full pipeline: quality control [FastQC v0.12.1, NanoPlot v1.46.0] -> alignment/mapping [MAFFT v7.526, QUAST v5.2.0.2] -> stage not stated [Python, SPAdes]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **1.41.6**
- Evidence: Read quality and length distribution were assessed using NanoPlot (v.1.41.6) before and after the removal of human reads (read mapping against the human genome (v.38) using minimap2 (v.2.26-r1175)).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: Sequencing was done using two flowcells of the Nanopore PromethION system, base calling with ont-guppy-for-minknow 3.2.10, and reads were separated based on barcode using NanoComp.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### The genome of a bunyavirus cannot be defined at the level of the viral particle but only at the scale of the viral population. (PNAS 2023)

- DOI: 10.1073/pnas.2309412120 | PMCID: PMC10691328 | PMID: 37983500
- Version used: **1.40.0**
- Evidence: Quality of the reads was investigated using NanoPlot v1.40.0 ( 51 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [IMOD] -> structure determination [IMOD] -> stage not stated [BLAST, ImageJ, NanoPlot v1.40.0]

### Wet-dry cycles cause nucleic acid monomers to polymerize into long chains. (PNAS 2024)

- DOI: 10.1073/pnas.2412784121 | PMCID: PMC11626162 | PMID: 39585974
- Evidence: Sample summary statistics computed by NanoStats using NanoComp to compare multiple samples.
- Full pipeline: differential/statistical testing [NanoPlot]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **1.30.1**
- Evidence: Read statistics were calculated with NanoPlot v1.30.1.
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

