# TopHat

- **Category:** genomics
- **Papers in survey:** 54
- **Journals:** PNAS (33), Nature (17), Cell (4)
- **Years:** 2021 (10), 2022 (16), 2023 (6), 2024 (10), 2025 (8), 2026 (4)
- **Versions named:** 2.1.1 (7), 2.0.7 (4), 2.1.0 (3), 2.0.13 (3), 2.0.9 (3), 1.0.13 (1), 2.0.10 (1), 2.1.2 (1), 1.3.2 (1), 2.2.1 (1)
- **Pipeline stages it appears in:** alignment/mapping (51), read trimming (7), quality control (5), differential/statistical testing (4), quantification (1)

## Papers

### A defective viral genome strategy elicits broad protective immunity against respiratory viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.023 | PMCID: PMC8598942 | PMID: 34852237
- Evidence: Differential gene and transcript expression analysis of mRNA-seq experiments with TopHat-Cufflinks-Cuffdiff pipeline ( Trapnell et al., 2012 ).
- Full pipeline: differential/statistical testing [Cufflinks, TopHat] -> visualisation [ggplot2] -> stage not stated [ImageJ]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Evidence: DNA copy number analysis inferred by single-cell RNA-seq data Single-cell RNA-seq reads were aligned to human genome using TopHat, and large-scale chromosomal copy number alterations were determined by InferCNV ( https://github.com/broadinstitute/infercnv ).
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Proximity-specific ribosome profiling reveals the logic of localized mitochondrial translation. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.002 | PMCID: PMC12650760 | PMID: 40876456
- Version used: **2.1.1**
- Evidence: Reads were then mapped to the genome using TopHat v2.1.1 with the following parameters: tophat --bowtie1 --read-mismatches 1 -g 64 –no-novel-juncs -T.
- Full pipeline: alignment/mapping [STAR v2.7.1a, TopHat v2.1.1, featureCounts v1.6.2] -> quantification [STAR v2.7.1a, featureCounts v1.6.2]

### Encoding and decoding selectivity and promiscuity in the human chemokine-GPCR interaction network. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.046 | PMCID: PMC12435897 | PMID: 40273912
- Evidence: Background signal in the green fluorescent channel was subtracted using TopHat segmentation.
- Full pipeline: alignment/mapping [ANNOVAR, MUSCLE, R] -> stage not stated [Cytoscape, PyMOL, TopHat]

### Control of osteoblast regeneration by a train of Erk activity waves. (Nature 2021)

- DOI: 10.1038/s41586-020-03085-8 | PMCID: PMC7864885 | PMID: 33408418
- Evidence: Gene expression analyses by RNA-Seq Reads were trimmed by Trim Galore (0.4.1, with -q 15 --paired) and then mapped with TopHat 33 (v 2.1.1, with parameters --b2-very-sensitive --no-coverage-search and supplying the UCSC danRer10 refSeq annotation).
- Full pipeline: read trimming [TopHat, Trim Galore v0.4.1] -> alignment/mapping [TopHat, Trim Galore v0.4.1] -> quantification [featureCounts] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> stage not stated [ilastik v1.3.3]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Evidence: Quality of sequencing reads was assessed using FastQC (Babraham Bioinformatics) and aligned to a reference genome (hg19, UCSC Genome Browser) using TopHat.
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **2.0.10**
- Evidence: Sequencing reads were mapped to TAIR10 with TopHat (v.2.0.10) 84 .
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### Intron-mediated induction of phenotypic heterogeneity. (Nature 2022)

- DOI: 10.1038/s41586-022-04633-0 | PMCID: PMC9068511 | PMID: 35444278
- Evidence: Intron retention analysis The reads resulting from sequencing were aligned to the annotated reference S. cerevisiae genome R64-2 using TopHat 51 or HISAT2 52 .
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, TopHat, featureCounts] -> quantification [featureCounts] -> visualisation [Clustal Omega] -> stage not stated [ImageJ]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Evidence: The reference genome was indexed using bowtie2-build, and reads were aligned onto the GRCh38/hg38 human reference genome using TopHat2 34 with strand-specificity and allowing only for the best match for each read.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Targeting myeloid chemotaxis to reverse prostate cancer therapy resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06696-z | PMCID: PMC10686834 | PMID: 37844613
- Version used: **2.0.7**
- Evidence: The SU2C–PCF transcriptomes were aligned to the human reference genome (GRCh37/hg19) using TopHat2 (v.2.0.7).
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, TopHat v2.0.7] -> quantification [Cufflinks v2.2.1] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSVA v1.4, R]

### Reducing brassinosteroid signalling enhances grain yield in semi-dwarf wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06023-6 | PMCID: PMC10156601 | PMID: 37100915
- Evidence: After cleaning up raw sequence reads, the clean reads were mapped to the wheat reference genome (International Wheat Genome Sequencing Consortium, RefSeq v1.1) using TopHat2 software 32 .
- Full pipeline: alignment/mapping [TopHat] -> differential/statistical testing [DESeq2, R] -> stage not stated [ImageJ, VCFtools v0.1.13]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Version used: **2.0.13**
- Evidence: Raw reads were trimmed by TrimGalore v.0.4.0 (Babraham Bioinformatics), mapped to mm10 by TopHat v.2.0.13 and analysed by DESeq2.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### dsRNA formation leads to preferential nuclear export and gene expression. (Nature 2024)

- DOI: 10.1038/s41586-024-07576-w | PMCID: PMC11236707 | PMID: 38898279
- Version used: **2.1.1**
- Evidence: RNAi coverage analysis and classification For gene coverage of RNAi degradation products, reads were trimmed using Cutadapt (v.2.1) 56 and aligned to the reference genome with TopHat2 (v.2.1.1) 57 .
- Full pipeline: read trimming [Cutadapt v2.1, TopHat v2.1.1] -> alignment/mapping [Cutadapt v2.1, TopHat v2.1.1] -> quantification [featureCounts] -> stage not stated [BEDTools, Bioconductor, DESeq2]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **2.1.1**
- Evidence: In brief, all reads were processed using Cutadapt (v.1.18) 67 for trimming of adaptor and poly-A sequences, then mapped onto GRCh38.p12 transcript references using TopHat2 (v.2.1.1) 68 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### A brain-specific angiogenic mechanism enabled by tip cell specialization. (Nature 2024)

- DOI: 10.1038/s41586-024-07283-6 | PMCID: PMC11041701 | PMID: 38570687
- Version used: **2.1.1**
- Evidence: Mapping was performed to the zebrafish reference genome build GRCz11, with TopHat v.2.1.1 and Bowtie1 or Bowtie2 option.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore v0.4.4] -> alignment/mapping [Bowtie2, SAMtools v1.16.1, TopHat v2.1.1, Trim Galore v0.4.4, featureCounts] -> quantification [featureCounts] -> stage not stated [DESeq2 v1.12, ImageJ v1.53c, Seurat]

### Hypoblast from human pluripotent stem cells regulates epiblast development. (Nature 2024)

- DOI: 10.1038/s41586-023-06871-2 | PMCID: PMC10849967 | PMID: 38052228
- Evidence: The trimmed reads were mapped to the human reference genome (hg38) using TopHat2 68 with GENCODE v.27 69 .
- Full pipeline: quality control [Seurat] -> read trimming [Cutadapt v1.15, TopHat] -> alignment/mapping [RSEM v1.3.1, STAR, TopHat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Version used: **2.1.1**
- Evidence: Bulk RNA-seq data processing RNA-seq reads were mapped to the mm10 mouse genome assembly using TopHat (v.2.1.1) with the setting –microexon-search.
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Perception of viral infections and initiation of antiviral defence in rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08706-8 | PMCID: PMC12043510 | PMID: 40074903
- Evidence: After adapters and low-quality reads were removed, the clean reads were mapped to the rice genome (MSU Rice Genome Annotation Project Database v.7.0, https://rice.uga.edu/download_osa1r7.shtml ) using TopHat.
- Full pipeline: quality control [FastQC] -> read trimming [TopHat] -> alignment/mapping [TopHat] -> quantification [ImageJ]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Version used: **1.0.13**
- Evidence: Sequencing data were quality controlled using FastQC and aligned to the mouse genome (NCBI38/mm10) using TopHat (v.1.0.13) with up to two mismatches 61 .
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **2.0.7**
- Evidence: Transcriptomes were aligned to the human reference genome (GRCh37/hg19) using TopHat2 (v.2.0.7).
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Version used: **2.1.0**
- Evidence: 65 ) and aligning remaining reads to the human hg38 genome and RefSeq-defined transcriptome with TopHat v2.1.0 (ref.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### Stable lariats bearing a snoRNA (slb-snoRNA) in eukaryotic cells: A level of regulation for guide RNAs. (PNAS 2021)

- DOI: 10.1073/pnas.2114156118 | PMCID: PMC8609340 | PMID: 34725166
- Version used: **2.0.7**
- Evidence: In short, conventional reads were aligned with TopHat (v2.0.7) to the X. tropicalis genome (v9.1), the mouse genome (v10), the human genome (v19), the chicken genome (v5), or the X. laevis genome (v9.0), and intronic reads were quantified with Bedtools (v2.15.0).
- Full pipeline: alignment/mapping [TopHat v2.0.7] -> quantification [TopHat v2.0.7]

### Coordinated bacterial and plant sulfur metabolism in <i>Enterobacter</i> sp. SA187-induced plant salt stress tolerance. (PNAS 2021)

- DOI: 10.1073/pnas.2107417118 | PMCID: PMC8609655 | PMID: 34772809
- Version used: **2.0.9**
- Evidence: Clean reads were then mapped to the reference genomes by using TopHat (version 2.0.9) ( 50 ).
- Full pipeline: quality control [R] -> read trimming [Trimmomatic] -> alignment/mapping [TopHat v2.0.9, featureCounts v1.6.5] -> quantification [Cufflinks v2.2.0, featureCounts v1.6.5] -> differential/statistical testing [Cufflinks v2.2.0] -> stage not stated [ImageJ]

### Early-life midazolam exposure persistently changes chromatin accessibility to impair adult hippocampal neurogenesis and cognition. (PNAS 2021)

- DOI: 10.1073/pnas.2107596118 | PMCID: PMC8463898 | PMID: 34526402
- Evidence: Processed reads were aligned to the mouse reference genome (mm10) using TopHat ( 53 ).
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2, SAMtools v0.1.19]

### The ATP-hydrolyzing ectoenzyme E-NTPD8 attenuates colitis through modulation of P2X4 receptor-dependent metabolism in myeloid cells. (PNAS 2021)

- DOI: 10.1073/pnas.2100594118 | PMCID: PMC8488689 | PMID: 34548395
- Version used: **2.0.12**
- Evidence: Sequenced reads were mapped to the mouse reference genome sequence (mm10) with TopHat version 2.0.12.
- Full pipeline: alignment/mapping [Cufflinks v2.1.1, TopHat v2.0.12] -> quantification [Cufflinks v2.1.1]

### The p53 transcriptional response across tumor types reveals core and senescence-specific signatures modulated by long noncoding RNAs. (PNAS 2021)

- DOI: 10.1073/pnas.2025539118 | PMCID: PMC8346867 | PMID: 34326251
- Evidence: RNA-seq reads were mapped to mm10 with TopHat ( 43 ) to Gencode transcript annotation (M9), and transcripts were annotated with StringTie ( 44 ).
- Full pipeline: alignment/mapping [StringTie, TopHat] -> normalisation [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2]

### Lipid droplets in mammalian eggs are utilized during embryonic diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2018362118 | PMCID: PMC7958255 | PMID: 33649221
- Evidence: Raw reads were checked for quality using FastQC software (Babraham Bioinformatics) filtered to remove accidental adapter sequences and low-quality reads and mapped against the Mus musculus GRCm38 genome assembly using TopHat2 ( 44 ) software set for paired-end reads.
- Full pipeline: quality control [FastQC, TopHat] -> read trimming [FastQC, TopHat] -> alignment/mapping [FastQC, HTSeq, TopHat, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Restriction of food intake by PPP1R17-expressing neurons in the DMH. (PNAS 2021)

- DOI: 10.1073/pnas.2100194118 | PMCID: PMC8020659 | PMID: 33753517
- Evidence: TopHat and Cufflinks apps were used to analyze RNA-seq results.
- Full pipeline: stage not stated [Cufflinks, TopHat]

### The RNA polymerase of cytoplasmically replicating Zika virus binds with chromatin DNA in nuclei and regulates host gene transcription. (PNAS 2022)

- DOI: 10.1073/pnas.2205013119 | PMCID: PMC9894162 | PMID: 36442102
- Evidence: RNA-seq reads were mapped to the human genome (hg38) with TopHat2, and differential expression analysis was performed using DESeq2.
- Full pipeline: alignment/mapping [DESeq2, TopHat] -> differential/statistical testing [DESeq2, TopHat]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: Raw, 75-bp paired-end reads in FASTQ format were initially checked for read quality using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and then aligned to the mouse reference genome (Gencode GRCm38 ( 72 )) using TopHat2 ( 73 ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Sperm-inherited H3K27me3 epialleles are transmitted transgenerationally in &lt;i&gt;cis&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2209471119 | PMCID: PMC9546627 | PMID: 36161922
- Evidence: For differential expression analysis, reads were mapped using TopHat2 for paired-end reads.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> normalisation [R] -> differential/statistical testing [DESeq2, TopHat]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **2.0.13**
- Evidence: For RNA-seq–based predictions, reads from more than four tissues (leaves, stems, and stem apices) RNA-seq data, which were detected in our research were, aligned to the three cotton genomes using TopHat (v2.0.13) ( 93 ) to identify exons region and splice positions.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Version used: **2.0.14**
- Evidence: The raw reads were quality checked and mapped to the maize reference genome (B73 RefGen_v4, AGPv4) ( 49 ) by Bowtie2 software (version 2.2.3) ( 50 ) and TopHat2 (version 2.0.14) ( 51 ).
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### Intestinal tissue-resident T cell activation depends on metabolite availability. (PNAS 2022)

- DOI: 10.1073/pnas.2202144119 | PMCID: PMC9411733 | PMID: 35969785
- Evidence: For the mapping, Ensembl GRCm38 genome annotation together with TopHat alignment software were used.
- Full pipeline: read trimming [Cutadapt v1.1] -> alignment/mapping [TopHat] -> normalisation [Bioconductor, DESeq2, R v3.1.0] -> differential/statistical testing [Bioconductor, DESeq2, R v3.1.0]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Version used: **2.0.7**
- Evidence: Transcriptomes were aligned to the human reference genome (GRCh38/hg38) using TopHat2 (version 2.0.7).
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### <i>TIC236</i> gain-of-function mutations unveil the link between plastid division and plastid protein import. (PNAS 2022)

- DOI: 10.1073/pnas.2123353119 | PMCID: PMC8931380 | PMID: 35275795
- Evidence: The clean reads were mapped to the Arabidopsis genome (TAIR10) using TopHat ( 48 ).
- Full pipeline: read trimming [Cutadapt v1.3, R, edgeR] -> alignment/mapping [BWA, TopHat, VCFtools] -> normalisation [R, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [SAMtools]

### The embryonic node behaves as an instructive stem cell niche for axial elongation. (PNAS 2022)

- DOI: 10.1073/pnas.2108935119 | PMCID: PMC8812687 | PMID: 35101917
- Evidence: Reads were aligned to the galGal6 chicken genome using TopHat2 ( 60 ), alignment rates were 91.9% ± 0.3% (for scRNA-seq) and 86.3% ± 0.65% (for RNA-seq of tissues).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [TopHat] -> normalisation [Cufflinks]

### Spatiotemporal analysis identifies ABF2 and ABF3 as key hubs of endodermal response to nitrate. (PNAS 2022)

- DOI: 10.1073/pnas.2107879119 | PMCID: PMC8794810 | PMID: 35046022
- Evidence: The RNA-seq reads were aligned to the TAIR10 genome assembly using TopHat ( 40 ) and gene expression was estimated using the GenomicFeatures/GenomicAlignments packages.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEDTools, ImageJ, MACS2, R]

### Genomic and transcriptomic analyses of the subterranean termite <i>Reticulitermes speratus</i>: Gene duplication facilitates social evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2110361119 | PMCID: PMC8785959 | PMID: 35042774
- Version used: **2.1.0**
- Evidence: The cleaned reads were mapped onto the genome with TopHat version 2.1.0 guided by the OGS1.0 gene models.
- Full pipeline: read trimming [edgeR, featureCounts] -> alignment/mapping [TopHat v2.1.0] -> quantification [edgeR, featureCounts] -> normalisation [edgeR, featureCounts]

### Translational control of <i>E2f1</i> regulates the <i>Drosophila</i> cell cycle. (PNAS 2022)

- DOI: 10.1073/pnas.2113704119 | PMCID: PMC8795540 | PMID: 35074910
- Version used: **2.0.9**
- Evidence: Raw reads were aligned to the Drosophila genome version 6 using TopHat2 version 2.0.9 ( 72 ), and Bowtie2 version 2.1.0.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, TopHat v2.0.9] -> quantification [Cufflinks]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Evidence: Reads were aligned to TAIR10 using TopHat ( 32 ), allowing up to two mismatches and only keeping reads mapped to one unique location.
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Version used: **1.3.2**
- Evidence: For the data analyses, read sequences (50 bp) were aligned to the mm10 mouse reference genome (University of California, Santa Cruz, CA, USA; December 2011) using Bowtie 2 and TopHat (version 1.3.2) software programs.
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Light cues induce protective anticipation of environmental water loss in terrestrial bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2309632120 | PMCID: PMC10515139 | PMID: 37695906
- Version used: **2.1.0**
- Evidence: The clean reads from each sample were aligned to the B728a genome sequence (GCF_000012245.1, 2005 version) using Bowtie2 v2.2.6 ( 62 ) and TopHat2 v2.1.0 ( 63 , 64 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, HTSeq, TopHat v2.1.0] -> quantification [HTSeq] -> differential/statistical testing [R]

### Epitranscriptic regulation of <i>HRAS</i> by <i>N</i><sup>6</sup>-methyladenosine drives tumor progression. (PNAS 2023)

- DOI: 10.1073/pnas.2302291120 | PMCID: PMC10083612 | PMID: 36996116
- Version used: **2.2.1**
- Evidence: Briefly, TopHat2 (version 2.2.1) with Bowtie1 support ( 62 , 63 ) was run to align the sequence reads to reference genome and transcriptome (hg38).
- Full pipeline: alignment/mapping [TopHat v2.2.1] -> differential/statistical testing [Bioconductor]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Version used: **2.1.1**
- Evidence: Generated reads were mapped to the human (hg19) reference genome using TopHat v2.1.1 in combination with Bowtie2 v2.2.8 and SAMtools v0.1.18.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: Trinity ( 80 ), and Cufflinks [ 81 ; following alignment using TopHat2 ( 82 )] were used to generate de novo transcript assemblies.
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Version used: **2.0.13**
- Evidence: Processed reads were aligned to the mouse genome with TopHat (version 2.0.13), allowing up to three mismatches per read.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### The MUC1-HIF-1α signaling axis regulates pancreatic cancer pathogenesis through polyamine metabolism remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2315509121 | PMCID: PMC10998584 | PMID: 38547055
- Evidence: TopHat2 was used for alignment and differential expression was done through DESeq2 R package.
- Full pipeline: alignment/mapping [DESeq2, R, TopHat] -> differential/statistical testing [DESeq2, R, TopHat] -> stage not stated [GSEA, ImageJ]

### Exitron splicing of odor receptor genes in <i>Drosophila</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2320277121 | PMCID: PMC10990081 | PMID: 38507450
- Version used: **2.1.2**
- Evidence: Reads were aligned to the D. melanogaster genome (BDGP6) using TopHat (version 2.1.2).
- Full pipeline: alignment/mapping [TopHat v2.1.2] -> stage not stated [ImageJ]

### &lt;i&gt;Rroid2&lt;/i&gt; regulates effector-to-memory CD8&lt;sup&gt;+&lt;/sup&gt; T cell differentiation during infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2503450122 | PMCID: PMC12684896 | PMID: 41284876
- Evidence: The sequencing reads were aligned to the Mus musculus reference genome version GRCm38 using TopHat2.
- Full pipeline: alignment/mapping [Cufflinks, STAR, TopHat] -> quantification [Cufflinks] -> differential/statistical testing [DESeq2] -> visualisation [ComplexHeatmap, GSEA, ggplot2] -> stage not stated [R]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: Clean reads were mapped to the lined seahorse genome using the TopHat2 program ( 70 ).
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### The role of estrogen receptor β in maintaining basal cells and modulating the immune environment in the prostate. (PNAS 2025)

- DOI: 10.1073/pnas.2505797122 | PMCID: PMC12232695 | PMID: 40549921
- Version used: **2.0.9**
- Evidence: After paired-end sequencing samples using the Illumina HiSEq 2000 platform, TopHat v2.0.9 was used to align the sequence reads to the mm10 reference genome.
- Full pipeline: quality control [FastQC] -> alignment/mapping [TopHat v2.0.9]

### A symbiotic gene stimulates aggressive behavior favoring the survival of parasitized caterpillars. (PNAS 2025)

- DOI: 10.1073/pnas.2422935122 | PMCID: PMC12067249 | PMID: 40294273
- Version used: **2.1.1**
- Evidence: The CvBV genome index was built using Bowtie (v2.1.0) ( 72 ), and paired-end clean reads were aligned to the CvBV genome using TopHat (v2.1.1) ( 73 ).
- Full pipeline: alignment/mapping [TopHat v2.1.1] -> quantification [R, pheatmap]

### Nf2 orchestrates β-arrestin2-biased PTH1R signaling to couple bone mass with skeletal integrity. (PNAS 2026)

- DOI: 10.1073/pnas.2524671123 | PMCID: PMC13273255 | PMID: 42268882
- Evidence: Reads were aligned to the mouse genome (GRCm39/mm39) using TopHat2.
- Full pipeline: alignment/mapping [TopHat] -> quantification [ImageJ] -> differential/statistical testing [Cufflinks]

