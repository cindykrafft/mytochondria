# Trinity

- **Category:** genomics
- **Papers in survey:** 8
- **Journals:** Nature (5), PNAS (2), Science (1)
- **Years:** 2021 (1), 2023 (3), 2024 (1), 2025 (3)
- **Versions named:** 2.5.1 (3), 2.11.0 (1), 2.8.4 (1), 2.13.2 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), quality control (1), read trimming (1)

## Papers

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Version used: **2.5.1**
- Evidence: ...mapped with minimap2 (v.2.23) 84 , and protein orthology identified using ProtHint (v.2.6.0) 91 from ctenophore transcriptomes 92 – 94 assembled with Trinity (v.2.5.1) 95 and translated using TransDecoder (v.5.5; https://github.com/TransDecoder/TransDecoder ).
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Version used: **2.8.4**
- Evidence: RNA-seq reads were also assembled de novo using Trinity (v.2.8.4) 74 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.5.1**
- Evidence: Additionally, we generated de novo transcriptome assemblies for all samples using Trinity (v.2.5.1) 68 with default parameters, which were thereafter mapped to the soft-masked assembly with GMAP (v.2020-04-08) 69 .
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **2.11.0**
- Evidence: In parallel, a de novo assembly of the bulk RNA-seq data was performed using Trinity (v.2.11.0) both in reference-free and genome-guided mode 81 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **2.5.1**
- Evidence: RNA-seq was aligned to the genome using STAR (v.2.5.2b), assembled using stringtie (v.1.3.3b) and also assembled as de novo transcripts using Trinity (v.2.5.1) 72 .
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Phylogenomic and ecological analyses reveal the spatiotemporal evolution of global pines. (PNAS 2021)

- DOI: 10.1073/pnas.2022302118 | PMCID: PMC8157994 | PMID: 33941644
- Evidence: Raw reads were checked with FastQC (v.0.11.5) ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), trimmed using Trimmomatic (v.0.36) ( 63 ), and then assembled using Trinity (v.20140717) ( 64 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> dimensionality reduction/clustering [phytools v0.7] -> stage not stated [IQ-TREE v2.0, R v3.6.2, ggplot2]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Version used: **2.13.2**
- Evidence: For analysis of candidate female-specific sequences, paired-end reads sequenced from RNAs of unfertilized oocytes were assembled with Trinity (v.2.13.2) ( 71 ) yielding 236734 contigs/transcripts.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### Precise targeting of HIV broadly neutralizing antibody precursors in humans. (Science 2025)

- DOI: 10.1126/science.adv5572 | PMCID: PMC12313413 | PMID: 40373114
- Evidence: This pipeline makes use of components of the BALDR package ( 80 ), which in turn makes use of the Trinity assembler ( 81 ).
- Full pipeline: alignment/mapping [Bowtie2] -> structure determination [Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, Nextflow, R, RELION v4.0, Trinity]

