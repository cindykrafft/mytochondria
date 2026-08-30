# HISAT2

- **Category:** genomics
- **Papers in survey:** 185
- **Journals:** PNAS (117), Nature (61), Cell (6), Science (1)
- **Years:** 2021 (12), 2022 (36), 2023 (30), 2024 (32), 2025 (59), 2026 (16)
- **Versions named:** 2.1.0 (38), 2.2.1 (33), 2.0.5 (6), 2.0.4 (4), 2.1 (3), 2.0.0 (2), 2.0.1 (2), 2.0.3 (2), 2.2 (1), 2.10.2 (1)
- **Pipeline stages it appears in:** alignment/mapping (171), read trimming (33), quality control (14), quantification (9), differential/statistical testing (6), visualisation (1), variant calling (1), structure determination (1)

## Papers

### An early cell shape transition drives evolutionary expansion of the human forebrain. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.050 | PMCID: PMC8054913 | PMID: 33765444
- Version used: **2.0.0**
- Evidence: ...alore/releases Cutadapt v2.4 Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ FASTQC v0.11.5 Andrews, 2010 https://github.com/s-andrews/FastQC HISAT2 v2.0.0-beta Kim et al., 2015 http://daehwankimlab.github.io/hisat2/ HTSeq v0.11.2 Anders et al., 2015 https://htseq.readthedocs.io/en/master/ g:Profiler Reimand et al., 2007 https://biit.cs.ut.ee/gprofiler/gost TCseq Wu and Gu, 2020 https://rd...
- Full pipeline: quality control [Cutadapt v2.4, FastQC, HISAT2 v2.0.0, HTSeq v0.11.2, Trim Galore] -> stage not stated [R v3.5]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Evidence: Trimmed reads were aligned to the library designs using hisat2.
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ..., 2018 ) v2.1.0 Dendextend ( Galili, 2015 ) v1.15.1 R (statistics) https://www.r-project.org/ v4.1.0 BBmap (BBtools) ( Bushnell et al., 2017 ) v38.90 HISAT2 ( Kim et al., 2015 ) v2.1.0 FastQC https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ v0.11.9 FeatureCounts ( Liao et al., 2014 ) v2.0.1 Astra Wyatt Technology v8.0 Compass Bruker Daltonics v1.2 TopSpin Bruker BioSpin GmbH V4.1.3 Resou...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **2.2.1**
- Evidence: The reads were mapped with HISAT2 v2.2.1, 101 the .sam files resulting from each mapping were converted into .bam files and indexed using SAMtools v1.10 102 and the reads mapped against each gene were counted using featureCounts v2.0.1.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Version used: **2.2.1**
- Evidence: The biological replicates for each cell type were aligned with the hg38 reference human genome assembly with HISAT2 v2.2.1 117 and were combined to obtain greater coverage at exon-splicing junctions.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Version used: **2.1.0**
- Evidence: 119 RRID: SCR_003070 https://imagej.nih.gov/ij/ Measure Rosette Area Tool (ImageJ macro) Remote-ImageJ project http://dev.mri.cnrs.fr/projects/remote-imagej/files FastQC v0.11.9 Babraham Institute (UK) www.bioinformatics.babraham.ac.uk/projects/fastqc HISAT2 v2.1.0 Kim et al.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: The PSC N cells ±NSD3 depletion RNA-seq reads were aligned to mouse genome mm10 by HISAT2 ( ccb.jhu.edu/software/hisat2 ) 59 .
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Version used: **2.1.0**
- Evidence: For reference-guided assembly, all reads were aligned to the N. forsteri genome (each sample independently) using the program HISAT2 v.2.1.0 51 (maximum intron length set to 3 Mb).
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Platypus and echidna genomes reveal mammalian biology and evolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03039-0 | PMCID: PMC8081666 | PMID: 33408411
- Evidence: We also mapped RNA-sequencing reads of the platypus from a previously published study 57 and echidna to their respective assemblies using HISAT2 58 (v.2.0.4), and constructed transcripts using stringTie 59 (v.1.2.3).
- Full pipeline: alignment/mapping [BWA, HISAT2, minimap2 v2.13] -> quantification [ggplot2 v3.2.1] -> normalisation [ggplot2 v3.2.1] -> stage not stated [ImageJ v2.0.0, RepeatMasker v4.0.6]

### Defining HPV-specific B cell responses in patients with head and neck cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-2931-3 | PMCID: PMC9462833 | PMID: 33208941
- Evidence: Briefly, reads were aligned to the human genome (GRCh38; accessed via Ensembl 41 ) with HISAT2 42 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [R, Seurat v3.1.4]

### A transcriptional switch controls sex determination in Plasmodium falciparum. (Nature 2022)

- DOI: 10.1038/s41586-022-05509-z | PMCID: PMC9750867 | PMID: 36477538
- Version used: **2.0.0**
- Evidence: HISAT2 (v.2.0.0) (ref.
- Full pipeline: alignment/mapping [minimap2 v2.17] -> quantification [HTSeq v0.12.4] -> visualisation [R] -> stage not stated [BEDTools v2.29.1, HISAT2 v2.0.0, SAMtools, Seurat v4.0.4, scDblFinder v1.6.0]

### Extracellular fluid viscosity enhances cell migration and cancer dissemination. (Nature 2022)

- DOI: 10.1038/s41586-022-05394-6 | PMCID: PMC9646524 | PMID: 36323783
- Evidence: We mapped the reads to the human GRCh38.p13 genome (hg38) using the HISAT2 package 54 , annotated each gene using Ensemble104 and totalled the number of exon reads for each pair using the HTSEQ package.
- Full pipeline: alignment/mapping [HISAT2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Python v3.8, TrackMate]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Version used: **2.1.0**
- Evidence: ...end 1 µg ml –1 Analysis of RNA-seq data for virus-specific CD8 + T cells during chronic infection Reads were mapped to the GRCm38/mm10 genome 54 with HISAT2 (v2.1.0) 55 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### ADAR1 averts fatal type I interferon induction by ZBP1. (Nature 2022)

- DOI: 10.1038/s41586-022-04878-9 | PMCID: PMC9329096 | PMID: 35859176
- Version used: **2.1.0**
- Evidence: Remaining reads were passed to HISAT2 (v2.1.0) 51 for strand-aware alignment, and strand-specific counts of uniquely mapping reads were prepared using featureCounts (within Subread v1.6.4; ref.
- Full pipeline: quality control [Cutadapt v3.4, FastQC v0.11.8] -> read trimming [Cutadapt v3.4, FastQC v0.11.8] -> alignment/mapping [HISAT2 v2.1.0, SAMtools, featureCounts] -> quantification [DESeq2 v1.22.1] -> normalisation [DESeq2 v1.22.1] -> differential/statistical testing [DESeq2 v1.22.1] -> visualisation [DESeq2 v1.22.1] -> stage not stated [QuPath v0.3.2]

### A male steroid controls female sexual behaviour in the malaria mosquito. (Nature 2022)

- DOI: 10.1038/s41586-022-04908-6 | PMCID: PMC9352575 | PMID: 35794471
- Version used: **2.0.5**
- Evidence: Sequencing reads were aligned to the A. gambiae genome (PEST strain, version 4.12) using HISAT2 (version 2.0.5) with the default parameters.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, HTSeq v0.9.1, SAMtools v1.3.1] -> quantification [DESeq2, R v4.0.3] -> normalisation [DESeq2, R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Version used: **2.10.2**
- Evidence: RNA evidence was collected by aligning RNA-sequencing (RNA-seq) reads to the repeat-masked assembly using HISAT2 (v.2.10.2) 57 and assembling them to transcripts with StringTie (v.1.3.0) 58 .
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Potentiating adoptive cell therapy using synthetic IL-9 receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04801-2 | PMCID: PMC9283313 | PMID: 35676488
- Version used: **2.0.4**
- Evidence: Reads were aligned to the mouse reference genome (mm9/GRCm38) using HISAT2 (v.2.0.4) (ref.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> quantification [HTSeq] -> normalisation [pheatmap] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [R, fgsea]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **2.0.1**
- Evidence: HISAT2 (v.2.0.1-beta) (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **2.2.1**
- Evidence: Cleaned reads were mapped to the complete ABO sequence from the Bamaxiang reference genome sequence using HISAT2 (v.2.2.1) 85 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Intron-mediated induction of phenotypic heterogeneity. (Nature 2022)

- DOI: 10.1038/s41586-022-04633-0 | PMCID: PMC9068511 | PMID: 35444278
- Evidence: Intron retention analysis The reads resulting from sequencing were aligned to the annotated reference S. cerevisiae genome R64-2 using TopHat 51 or HISAT2 52 .
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, TopHat, featureCounts] -> quantification [featureCounts] -> visualisation [Clustal Omega] -> stage not stated [ImageJ]

### A joint NCBI and EMBL-EBI transcript set for clinical genomics and research. (Nature 2022)

- DOI: 10.1038/s41586-022-04558-8 | PMCID: PMC9007741 | PMID: 35388217
- Version used: **2.1**
- Evidence: HISAT 2.2.1 is available at http://daehwankimlab.github.io/hisat2/ .
- Full pipeline: stage not stated [HISAT2 v2.1, HOMER, VEP]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Version used: **2.2.1**
- Evidence: For gene-expression quantification RNA-seq reads were first trimmed using trim-galore v0.6.6 and thereafter aligned to the human genome using hisat2 v2.2.1.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: Bioinformatics data processing and analyses were performed using Bash (v4.2.46), R (v3.6) and Python (v3.8.5) programming languages as well as the following tools: FastQC (Babraham Bioinformatics) (v0.11.7) cutadapt 37 (v1.16), HISAT2 38 (v2.1.0), SAMtools 39 (v1.9), sambamba 40 (v0.6.6) and deepTools 41 (v3.1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Evidence: 10 ): adapters were trimmed using fastp with default parameters 62 , and mapped to hg19 using HISAT2 with the options–no-mixed–dta–rna-strandness RF -k 2 63 .
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Version used: **2.2.1**
- Evidence: Reads were aligned to a reference genome composed of an E. coli K12 ( U00096.3 ), bacteriophage T4 ( NC_000866.4 ) and RNAI (our design) with hisat2 (v.2.2.1).
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: The sequencing output files from different lanes were concatenated, aligned to GRCH38 using HISAT2 and transcripts were counted using HTSeq in Python.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Evidence: Reads were aligned to CRGh38/hg38 using HISAT2 with the default parameters.
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Glioblastoma remodelling of human neural circuits decreases survival. (Nature 2023)

- DOI: 10.1038/s41586-023-06036-1 | PMCID: PMC10191851 | PMID: 37138086
- Evidence: Reads were subsequently mapped to the human reference genome GRCh38 ( https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.39/ ) 67 using HISAT2 68 (v.2.1.0) with the default parameters.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [HISAT2, featureCounts] -> normalisation [Python, Seurat v3.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Python, R v3.1, Seurat v3.0.1, featureCounts] -> stage not stated [ImageJ]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Version used: **2.1.0**
- Evidence: Quantification of gene expression and identification of differential genes All the reads were mapped to the mouse genome (UCSC mm10) ( http://www.ccb.jhu.edu/software/hisat/index.shtml ) using HISAT2 (v.2.1.0) 39 with the default settings.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Version used: **2.2.1**
- Evidence: Filtered reads were aligned against the reference mouse genome assembly mm10 using HISAT2 v.2.2.1.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Version used: **2.2.1**
- Evidence: Nascent RNA-seq data analysis Raw reads were trimmed with Trimmomatic (v.0.39) 54 , and then aligned to mouse genome and transcriptome (mm10, version M19) as well as external RNA Control Consortium (ERCC) RNA spike-in control (Thermo Fisher Scientific) using HISAT2 (v.2.2.1) 58 .
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Reads were aligned to the human genome (hg38) using HISAT2 (ref.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Senescent glia link mitochondrial dysfunction and lipid accumulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07516-8 | PMCID: PMC11168935 | PMID: 38839958
- Version used: **2.1.0**
- Evidence: Paired-end reads were aligned to the fly genome using HISAT2 (v.2.1.0) 63 .
- Full pipeline: alignment/mapping [DESeq2, HISAT2 v2.1.0, HTSeq v0.9.1, SAMtools] -> differential/statistical testing [DESeq2, HTSeq v0.9.1, edgeR, ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: Sequence alignment against the mouse reference genome mm10 or the human genome hg19 was performed using HISAT2.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Version used: **2.1**
- Evidence: Extracted 21U and 22G reads aligned to the genome using hisat2 v2.1 (ref.
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### Circulating myeloid-derived MMP8 in stress susceptibility and depression. (Nature 2024)

- DOI: 10.1038/s41586-023-07015-2 | PMCID: PMC10901735 | PMID: 38326622
- Version used: **2.1.0**
- Evidence: Raw sequencing reads from the samples were mapped to mm10 using HISAT2 v2.1.0 65 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, HTSeq v0.12.4, STAR v2.5] -> quantification [ImageJ, Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: ...article/view/200 ) and FastQC v.0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and mapped to the human genome (hg38) using the HISAT2 package (v.2.2.0) (ref.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Version used: **2.2.1**
- Evidence: The filtered reads were mapped to the mouse reference genome mm10 using HISAT2 (v.2.2.1) 76 , and samtools (v.1.17) 77 was used to convert and sort BAM files.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: To this end, the RNA-seq reads were aligned using HISAT2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Resulting reads were mapped, using default parameters, with HISAT2 71 , using a GRCm38, release 101 genome and index.
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: Sequencing data were aligned using HISAT2 in human reference genome (GRCh38), with reads counting performed by featureCounts.
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Evidence: The raw reads were aligned to the mm10 (GRCm38) genome assembly using hisat2 (ref.
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: Genome alignment was performed using HISAT2 and the Mus musculus mm10 reference genome.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Rewiring endogenous genes in CAR T cells for tumour-restricted payload delivery. (Nature 2025)

- DOI: 10.1038/s41586-025-09212-7 | PMCID: PMC12328239 | PMID: 40604285
- Evidence: Sequence alignment against the mouse reference genome mm10 or the human reference genome hg19 was done using HISAT2.
- Full pipeline: quality control [Cutadapt v2.1] -> read trimming [edgeR v3.8.5] -> alignment/mapping [HISAT2] -> normalisation [edgeR v3.8.5] -> dimensionality reduction/clustering [Seurat] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **2.1.0**
- Evidence: RNA alignment was done using hisat2 (v.2.1.0) 125 with the flag --no-mixed.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Version used: **2.1.0**
- Evidence: For UCSC genome browser visualization, reads were mapped to the mm10 mouse reference genome ( https://genome.ucsc.edu/cgi-bin/hgGateway?db=mm10 ) using hisat2 v.2.1.0 with the options ‘--no-softclip -k 100 | samtools view -q 10 -Sb - | samtools sort’.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Version used: **2.1.0**
- Evidence: Transcriptomes were analysed on the Galaxy platform 59 using Trim Galore! version 0.4.3.1 (developed by Felix Krueger at the Babraham Institute), HISAT2 version 2.1.0 60 and featureCounts version 1.6.1.0 61 . snRNA-seq of thymic tissue The Chromium GEM-X Single Cell 3′ v4 protocol ( CG000731 , Rev B) was followed starting from step 1.1 according to the manufacturer’s guidelines.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **2.2.1**
- Evidence: RNA-seq libraries (Supplementary Table 2 ) were aligned with either hisat2 (v2.2.1) 93 for short-read mapping, or minimap2 (v2.24) 75 for full-length cDNA.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Molecular basis of positional memory in limb regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09036-5 | PMCID: PMC12176643 | PMID: 40399677
- Evidence: Trimmed sequenced reads were mapped to axolotl genome AmexG_v6.0-DD with HISAT2 (ref.
- Full pipeline: read trimming [HISAT2, Trimmomatic v0.39] -> alignment/mapping [HISAT2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, ggplot2 v3.3.6, pheatmap]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Expression analysis of opossum DNA methylation factors and repetitive elements Opossum embryo RNA-seq data 23 and DNMT 1-knockout RNA-seq data were mapped to the modified MonDom5 reference genome and ASM229v1 reference genome, respectively, using HISAT2 (ref.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: The RNA-seq was also directly mapped to genome using HISAT2 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: HISAT2 was used to align reads to the Oryza sativa (Japonica) genome, and gene-expression levels were quantified using the fragments per kilobase of transcript sequence per million mapped reads) method.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Microbial metabolite drives ageing-related clonal haematopoiesis via ALPK1. (Nature 2025)

- DOI: 10.1038/s41586-025-08938-8 | PMCID: PMC12137129 | PMID: 40269158
- Evidence: Paired-end FASTQ files were aligned to mm10 (mouse) genomes using HISAT2 ( http://www.ccb.jhu.edu/software/hisat ) or Tophat ( https://ccb.jhu.edu/software/tophat ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [HISAT2] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, FastQC v0.11.8, R] -> stage not stated [MACS2, ggplot2, phyloseq]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: RNA-seq reads from four different tissues of each accession were mapped to their respective assembled genomes using HISAT2 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **2.1.0**
- Evidence: Reads that passed all quality control steps were then aligned to the human genome (GRCh38) using HISAT2 v.2.1.0 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **2.2.1**
- Evidence: First, we aligned RNA-seq reads to assembled haplotypes using HISAT2 (v.2.2.1) 76 with the “--dta” parameter and then assembled by StringTie (v.2.2.1) 77 with the “--rf” parameter.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **2.2.1**
- Evidence: The resulting clean reads were then aligned to the mouse reference genome (mm10) using hisat2 (v2.2.1).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **2.1.0**
- Evidence: The reads were mapped to mouse genome (mm10) using hisat2 (v.2.1.0) 63 , and mapped reads were assembled with FeatureCounts (v.2.0.0). scRNA-seq data analysis of cerebellar cell types A publicly available Seurat object containing single-cell RNA-seq (scRNA-seq) data from cerebellar tissue (24,409 genes across 611,034 cells) was obtained from a previously published study ( https://singlecell.broadi...
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **2.2.1**
- Evidence: We mapped Hi-C, DNA-seq and RNA-seq short reads into the genome using BWA and HISAT2 (v2.2.1) 64 to detect multiple mapping.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Evidence: We then aligned RNA-seq reads to the assemblies using HISAT2 (v.2,2.1) 104 , and performed transcriptome assembly with StringTie (v.2.2.1) 105 , using Liftoff annotations as guidance.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Version used: **2.1.0**
- Evidence: We aligned raw sequencing reads to hg19 genome by hisat2 (v.2.1.0) and quantified gene counts using RSEM (v.1.3.0) as raw counts.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Version used: **2.2.1**
- Evidence: HISAT2 (v.2.2.1) was used to build the index of the reference genome, and HISAT2 was used to align paired-end clean reads to the reference genome. featureCounts (v.2.0.6) was used to count the reads numbers mapped to each gene.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: After sequencing, data was aligned to the human reference genome Hg38/GRCh38 using HISAT2 54 (v.2.1.0) and the number of reads per gene were calculated using HTSeq count 55 (v.0.5.3).
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **2.1.0**
- Evidence: RNA-seq reads were aligned to the mouse reference genome (mm10) using HISAT2 (v.2.1.0).
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Version used: **2.1.0**
- Evidence: The trimmed sequences were aligned to the mouse genome build GRCm38.98 using HISAT2 (v2.1.0), with raw counts per gene subsequently determined using FeatureCounts (v1.6.4).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Reads were mapped to mm10 (hisat2), duplicates removed (Picard) and peaks were called using MACS2.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **2.2**
- Evidence: Adaptor trimming was performed, and reads were aligned to the mm10 reference genome using HISAT2 (v.2.2) 46 .
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Emergent RNA-RNA interactions can promote stability in a facultative phototrophic endosymbiosis. (PNAS 2021)

- DOI: 10.1073/pnas.2108874118 | PMCID: PMC8463893 | PMID: 34521754
- Evidence: Trimmed reads were mapped against the “endosymbiont” dataset of assembled transcripts using the HISAT2 alignment program with default settings.
- Full pipeline: quality control [FastQC] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2] -> quantification [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [BLAST]

### The DME demethylase regulates sporophyte gene expression, cell proliferation, differentiation, and meristem resurrection. (PNAS 2021)

- DOI: 10.1073/pnas.2026806118 | PMCID: PMC8307533 | PMID: 34266952
- Version used: **2.1.0**
- Evidence: We mapped filtered reads onto the reference genome using HISAT2 (v2.1.0) identifying a total of 24,739 genes ( 77 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0] -> visualisation [R, ggplot2] -> stage not stated [DESeq2, StringTie v2.1.3]

### Transposon-mediated insertional mutagenesis unmasks recessive insecticide resistance in the aphid <i>Myzus persicae</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100559118 | PMCID: PMC8201860 | PMID: 34074777
- Version used: **2.1.0**
- Evidence: Clean reads were aligned to the G006v2 genome assembly using HISAT2 version 2.1.0 ( 50 ) and gene expression estimated using the HTSeq count tool implemented in the HTSeq package ( 51 ).
- Full pipeline: quality control [FastQC, Trim Galore v0.4.5] -> read trimming [FastQC] -> alignment/mapping [HISAT2 v2.1.0, HTSeq] -> differential/statistical testing [edgeR v3.9] -> stage not stated [MUSCLE v3.8]

### HIF-1α is a negative regulator of interferon regulatory factors: Implications for interferon production by hypoxic monocytes. (PNAS 2021)

- DOI: 10.1073/pnas.2106017118 | PMCID: PMC8256008 | PMID: 34108245
- Version used: **2.0.5**
- Evidence: The quality of unstranded paired read files (FASTQ) were checked using FASTQC (v0.11.7, https://www.bioinformatics.babraham.ac.uk/projects/fastqc ) then aligned to human GRCh38 genome using HISAT2 (v2.0.5).
- Full pipeline: quality control [HISAT2 v2.0.5] -> read trimming [edgeR, featureCounts v1.5.2] -> alignment/mapping [HISAT2 v2.0.5] -> normalisation [edgeR, featureCounts v1.5.2]

### The imprinted lncRNA <i>Peg13</i> regulates sexual preference and the sex-specific brain transcriptome in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2022172118 | PMCID: PMC7958240 | PMID: 33658376
- Evidence: Reads were mapped to the mouse mm10 reference genome (Genome Sequencing Consortium 2002) by using HISAT2 ( 43 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### Transcriptional heterogeneity and tightly regulated changes in gene expression during &lt;i&gt;Plasmodium berghei&lt;/i&gt; sporozoite development. (PNAS 2021)

- DOI: 10.1073/pnas.2023438118 | PMCID: PMC7958459 | PMID: 33653959
- Evidence: We mapped all reads using HISAT2 [version 2.0.4 ( 72 )] to the P. berghei ANKA genome ( 38 ), allowing for a maximum intron length of 5,000 bp, and to the An. stephensi genome [AsteS1 ( 73 )].
- Full pipeline: alignment/mapping [HISAT2]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: For N. parkeri , all the clean reads obtained from mRNA-seq were mapped to the reference genome in HISAT2 ( 67 ) (–phred33 –sensitive –no-discordant –no-mixed -I 1 -X 1000).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Version used: **2.0.5**
- Evidence: The reference human genome and annotation files were downloaded from the Ensembl database ( 88 ) and the clean data were mapped onto the reference genome using HISAT2 (v2.0.5) ( 89 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### A family of unusual immunoglobulin superfamily genes in an invertebrate histocompatibility complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207374119 | PMCID: PMC9546547 | PMID: 36161920
- Evidence: To calculate expression levels of our annotated Alr genes, paired-end RNAseq reads were mapped to the entire genome assembly using HISAT2 ( 69 ).
- Full pipeline: alignment/mapping [AlphaFold, HISAT2] -> stage not stated [Cufflinks, HMMER]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **2.0.3**
- Evidence: RNA-sequencing reads were aligned with HISAT2 v2.0.3 ( 90 ), and gene - expression levels were quantified with Cufflinks 2.2.1 ( 91 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Winter warming post floral initiation delays flowering via bud dormancy activation and affects yield in a winter annual crop. (PNAS 2022)

- DOI: 10.1073/pnas.2204355119 | PMCID: PMC9522361 | PMID: 36122201
- Version used: **2.2.1**
- Evidence: The clean reads were mapped to B. napus genome v4.1 ( 24 ) by HISAT2 v2.2.1 with default parameters ( 35 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HISAT2 v2.2.1] -> normalisation [deepTools v2.3] -> visualisation [deepTools v2.3] -> stage not stated [HOMER, Picard, R, WGCNA]

### Miat and interacting protein Metadherin maintain a stem-like niche to promote medulloblastoma tumorigenesis and treatment resistance. (PNAS 2022)

- DOI: 10.1073/pnas.2203738119 | PMCID: PMC9478675 | PMID: 36067288
- Version used: **2.0.3**
- Evidence: Reads were aligned to the mouse genome mm10 using the spliced-read aligner HISAT2 v2.0.3 with default parameters.
- Full pipeline: alignment/mapping [HISAT2 v2.0.3] -> quantification [DESeq2] -> differential/statistical testing [DESeq2]

### Root angle is controlled by &lt;i&gt;EGT1&lt;/i&gt; in cereal crops employing an antigravitropic mechanism. (PNAS 2022)

- DOI: 10.1073/pnas.2201350119 | PMCID: PMC9351459 | PMID: 35881796
- Evidence: High quality paired-end clean reads were mapped to reference genome IBSC_v2 using HISAT2 ( 54 ) software.
- Full pipeline: alignment/mapping [BWA v7.12, Cufflinks, HISAT2, HTSeq, SAMtools v1.3] -> stage not stated [AlphaFold, DESeq2, ImageJ, R]

### Genetic variation that determines &lt;i&gt;TAPBP&lt;/i&gt; expression levels associates with the course of malaria in an HLA allotype-dependent manner. (PNAS 2022)

- DOI: 10.1073/pnas.2205498119 | PMCID: PMC9303992 | PMID: 35858344
- Version used: **2.1.0**
- Evidence: Trimmed reads were aligned to the human genome (GRCh38 build 88 to 92) by using HISAT2 v2.1.0 and counted with HTSeq (v0.6.1 to 0.9.1) ( 48 , 49 ).
- Full pipeline: read trimming [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, Trimmomatic v0.33, edgeR] -> alignment/mapping [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, edgeR] -> variant calling [BCFtools v1.9, R, edgeR] -> normalisation [BCFtools v1.9, R, edgeR]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Version used: **2.2.1**
- Evidence: HISAT2 (v2.2.1) was then used to build a genome index from GalGal6 (amended to include a GFP sequence) before extracting splice sites from the GTF and aligning reads.
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### Voltage-gated sodium channel &lt;i&gt;scn8a&lt;/i&gt; is required for innervation and regeneration of amputated adult zebrafish fins. (PNAS 2022)

- DOI: 10.1073/pnas.2200342119 | PMCID: PMC9282381 | PMID: 35867745
- Evidence: Sequences were aligned to the zebrafish genome (genome assembly GRCz11, Ensembl gene annotation release 104) using HISAT2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [ImageJ]

### Distinct gene expression dynamics in developing and regenerating crustacean limbs. (PNAS 2022)

- DOI: 10.1073/pnas.2119297119 | PMCID: PMC9271199 | PMID: 35776546
- Version used: **2.1.0**
- Evidence: Sequenced reads were mapped to a modified version of the available P. hawaiensis genome assembly Phaw_5.0 ( https://www.ncbi.nlm.nih.gov/assembly/GCA_001587735.2/ , see SI Appendix , Methods ), using hisat2 v2.1.0.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, kallisto v0.42.5] -> quantification [R, limma] -> normalisation [R, limma] -> dimensionality reduction/clustering [clusterProfiler v4.0.0] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, JAGS]

### The evening complex integrates photoperiod signals to control flowering in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2122582119 | PMCID: PMC9245669 | PMID: 35733265
- Evidence: HISAT2 with parameters ‘–no-mixed, –rna-strandness RF –dta –fr’ was used for aligning the raw RNA-seq reads to the rice genome assemblies ( 63 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [StringTie, deepTools] -> normalisation [deepTools] -> stage not stated [BEDTools v2.30.0, BWA, MACS2, R, SAMtools v1.11]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **2.1.0**
- Evidence: The trimmed Illumina RNA-seq libraries from KR01 and MYN1 were independently mapped against their associated reference genomes using HISAT2 (v2.1.0; -q –phred33 –no-unal –dta –rf) ( 44 ), and transcripts were constructed for each library using StringTie2 (v2.0.6; –rf) ( 45 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### Caspase-4/11 exacerbates disease severity in SARS-CoV-2 infection by promoting inflammation and immunothrombosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202012119 | PMCID: PMC9173818 | PMID: 35588457
- Version used: **2.1.0**
- Evidence: Briefly, raw RNA sequencing data (fastq) were aligned to mouse reference genome (GRCh38) using hisat2 (v2.1.0) ( 56 ) and converted to counts using the “subread” package (v1.5.1) ( 57 ) in R.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [limma] -> visualisation [DESeq2] -> stage not stated [ComplexHeatmap]

### Variation in upstream open reading frames contributes to allelic diversity in maize protein abundance. (PNAS 2022)

- DOI: 10.1073/pnas.2112516119 | PMCID: PMC9169109 | PMID: 35349347
- Evidence: Reads were mapped against version 5 of the B73 genome using hisat2 ( 71 ) version 2.2.1 with default parameters except for “–trim5 1” to remove the first base pair from each read, which the original authors describe as frequently representing an untemplated addition during reverse transcription ( 39 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2, HTSeq, SAMtools] -> stage not stated [BLAST, R]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: The processed reads from different samples were then mapped to the BaGv2 genome, using hisat2 ( 41 ) (mapping statistics in SI Appendix , Table S6 ), resulting in bam files that were sorted by genomic positions, using samtools ( 31 ).
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### Molecular parallelism in signaling function across different sexually selected ornaments in a warbler. (PNAS 2022)

- DOI: 10.1073/pnas.2120482119 | PMCID: PMC8872772 | PMID: 35165176
- Version used: **2.1.0**
- Evidence: For each RNA-seq sample, we used HISAT2 (v2.1.0) ( 49 ) to map reads to the common yellowthroat genome.
- Full pipeline: alignment/mapping [R, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.1.0, HISAT2 v2.1.0, ImageJ, SAMtools v1.7]

### Electrophysiological measures from human iPSC-derived neurons are associated with schizophrenia clinical status and predict individual cognitive performance. (PNAS 2022)

- DOI: 10.1073/pnas.2109395119 | PMCID: PMC8784142 | PMID: 35017298
- Version used: **2.0.4**
- Evidence: Raw sequencing reads from all samples were aligned to a custom concatenated Gencode hg38 + rn6 reference genome using HISAT2 2.0.4 ( 53 ) (including NPC samples without any rodent RNA, for comparability with neuronal samples).
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> variant calling [SAMtools] -> quantification [featureCounts v1.5.0, kallisto] -> dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [limma]

### CHAF1A/B mediate silencing of unintegrated HIV-1 DNAs early in infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116735119 | PMCID: PMC8795523 | PMID: 35074917
- Version used: **2.1.0**
- Evidence: ATAC-seq reads were mapped to the HIV-1 genome and human genome assembly hg38 using HISAT2 (v2.1.0, parameter: -X 2000).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> stage not stated [Picard v2.23.1]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: The clean reads were mapped to the TAIR10 Arabidopsis genome build using HISAT2.
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### Locust density shapes energy metabolism and oxidative stress resulting in divergence of flight traits. (PNAS 2022)

- DOI: 10.1073/pnas.2115753118 | PMCID: PMC8740713 | PMID: 34969848
- Evidence: Raw data were filtered, and the cleaned data were mapped to the locust genome sequence with HISAT2 software.
- Full pipeline: alignment/mapping [HISAT2] -> stage not stated [edgeR]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Evidence: Reads were aligned to TAIR10 with chloroplasts and mitochondria excluded using HISAT2 ( 35 ) with default settings.
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Evidence: RNA sequencing reads were aligned onto mm10 mouse genome by HISAT2 ( 33 ) and counted by HTSeq ( 34 ).
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### &lt;i&gt;INDETERMINATE1&lt;/i&gt;-mediated expression of &lt;i&gt;FT&lt;/i&gt; family genes is required for proper timing of flowering in &lt;i&gt;Brachypodium distachyon&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312052120 | PMCID: PMC10655584 | PMID: 37934817
- Version used: **2.1.0**
- Evidence: The cleaned paired-end reads were aligned to the B. distachyon genome v3.1 ( https://phytozome-next.jgi.doe.gov/brachypan ) by HISAT2 v2.1.0 package ( 85 ).
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, SAMtools v1.9] -> stage not stated [Galaxy, featureCounts v1.6.2, tidyverse]

### Scattered differentiation of unlinked loci across the genome underlines ecological divergence of the selfing grass &lt;i&gt;Brachypodium stacei&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2304848120 | PMCID: PMC10636366 | PMID: 37903254
- Evidence: Transcriptome analysis was conducted using the “HISAT2-Stringtie-DESeq” pipeline.
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BUSCO, HISAT2, IQ-TREE v1.6.12]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Version used: **2.1.0**
- Evidence: Trimmed reads were then mapped to the human genome (HG38 assembly) using HISAT2 (v.
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Evidence: The RNAseq data were also mapped to the genome using HISAT2 ( 70 ) and the reads were assembled into transcripts using StringTie ( 71 ), and then, TransDecoder ( 66 ) was subsequently used to perform ORFs prediction with the assembled transcripts.
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### Disruption of the rice <i>4-DEOXYOROBANCHOL HYDROXYLASE</i> unravels specific functions of canonical strigolactones. (PNAS 2023)

- DOI: 10.1073/pnas.2306263120 | PMCID: PMC10589652 | PMID: 37819983
- Evidence: Total reads were mapped to the rice transcripts using HISAT2 ( 53 ).
- Full pipeline: alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Version used: **2.2.1**
- Evidence: For transcriptome-based prediction, RNA-seq data were mapped against the assembly using HISAT2 v2.2.1 ( 77 ), and the transcripts were converted to gene models using Cufflinks v2.3.1 ( 78 ).
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### PIF4 enhances the expression of <i>SAUR</i> genes to promote growth in response to nitrate. (PNAS 2023)

- DOI: 10.1073/pnas.2304513120 | PMCID: PMC10523462 | PMID: 37725643
- Evidence: The reads were aligned to the Arabidopsis genome (TAIR10) using HISAT2 ( 74 ) and counts were calculated with Htseq ( 75 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [ImageJ] -> normalisation [ImageJ]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Version used: **2.0.1**
- Evidence: Single-cell RNA-seq libraries were aligned with hisat2 version 2.0.1-beta to a mouse mm10 hisat2 index with the inserted CFP cDNA sequence included in the index.
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Version used: **2.1**
- Evidence: Reads were trimmed using Trimgalore v0.6.5 and mapped using hisat2.2.1 to the hg38/GRCh38 genome assembly.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Version used: **2.2.1**
- Evidence: For the second run, RNA-seq data from 102 libraries were downloaded from the NCBI ( SI Appendix , Table S3 ), trimmed using TrimGalore v0.6.7 ( 87 ) and aligned against the unaligned pangenome using hisat2 v2.2.1 ( 88 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### Visualizing the activation of encephalitogenic T cells in the ileal lamina propria by in vivo two-photon imaging. (PNAS 2023)

- DOI: 10.1073/pnas.2302697120 | PMCID: PMC10372570 | PMID: 37467267
- Evidence: The sequence alignment to the reference genome was performed using HISAT2 (Hierarchical Indexing for Spliced Alignment of Transcripts two) ( 19 ).
- Full pipeline: alignment/mapping [HISAT2] -> stage not stated [ImageJ]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Evidence: Polyporus brumalis ), using the HISAT2 program (v2.1.0) ( 80 ).
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### Adaptive structural and functional evolution of the placenta protects fetal growth in high-elevation deer mice. (PNAS 2023)

- DOI: 10.1073/pnas.2218049120 | PMCID: PMC10288601 | PMID: 37307471
- Evidence: Sequences were then aligned to the Peromyscus maniculatus bairdii genome (assembly HU_Pman_2.1.3) using HISAT2 ( 96 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [ImageJ v2.0.0, featureCounts] -> stage not stated [R v4.0, WGCNA, emmeans, lme4]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: Using splice-aware read aligner HISAT2, FASTQ files were aligned with the UCSC mm10 mouse genome.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: The clean reads were mapped to the combined X. tropicalis v10.0 and X. laevis v10.1 reference genomes downloaded from Xenbase ( http://www.xenbase.org/ , Research Resource Identifiers (RRID): SCR_003280) using HISAT2 ( 50 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Experimental evidence for the functional importance and adaptive advantage of A-to-I RNA editing in fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2219029120 | PMCID: PMC10041177 | PMID: 36917661
- Evidence: RNA-seq reads were mapped to the PH-1 genome using HISAT2 ( 67 ) with the two-step model as described ( 68 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [R v4.1, featureCounts] -> normalisation [featureCounts] -> visualisation [AlphaFold, R v4.1, UCSF Chimera v1.16] -> stage not stated [BLAST]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Evidence: The raw reads were trimmed using Trimomatic v0.33 software ( 51 ), and the trimmed reads were mapped against either WYMV RNA1 (GenBank accession AB627808.1 ) using Bowtie2 software ( bowtie-bio.sourceforge.net/bowtie2/ ), or onto the wheat genome assembly refseq.2 (GCA_900519105: Ensembl plants) using HISAT2 v2-2.2.1 software ( 52 ).
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### KMT2D acetylation by CREBBP reveals a cooperative functional interaction at enhancers in normal and malignant germinal center B cells. (PNAS 2023)

- DOI: 10.1073/pnas.2218330120 | PMCID: PMC10089214 | PMID: 36893259
- Evidence: RNA-seq reads were mapped to the Mus musculus (mm10/GRCm38) genome assembly using the hisat2 prebuilt genome index ( 61 ).
- Full pipeline: alignment/mapping [HISAT2, featureCounts v1.6.3] -> quantification [ImageJ, featureCounts v1.6.3] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v4.2, SciPy] -> stage not stated [GSEA, HOMER]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **2.0.4**
- Evidence: RNA-seq data of multiple Bf developmental stages were downloaded from NCBI SRA (PRJDB3785) for estimating the Hox gene expression level using HISAT2 (2.0.4) and featureCounts (v1.5.2).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **2.1.0**
- Evidence: We further used the HISAT2 (2.1.0) ( 69 )-StringTie (2.1.1) ( 70 ) pipeline to assemble the transcripts through a genome-guided method.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### PCIF1-mediated deposition of 5'-cap &lt;i&gt;N&lt;/i&gt;&lt;sup&gt;6&lt;/sup&gt;,2'-&lt;i&gt;O&lt;/i&gt;-dimethyladenosine in ACE2 and TMPRSS2 mRNA regulates susceptibility to SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210361120 | PMCID: PMC9945940 | PMID: 36689652
- Version used: **2.1.0**
- Evidence: For the analysis, paired-end reads were trimmed by cutadapt (v1.18) and then mapped to the human genome (hg38) using HISAT2 (v2.1.0).
- Full pipeline: read trimming [Cutadapt v1.18, HISAT2 v2.1.0] -> alignment/mapping [Cutadapt v1.18, HISAT2 v2.1.0] -> quantification [DESeq2, HTSeq v0.11.2] -> stage not stated [SAMtools]

### Glutamate-GABA imbalance mediated by miR-8-5p and its STTM regulates phase-related behavior of locusts. (PNAS 2023)

- DOI: 10.1073/pnas.2215660120 | PMCID: PMC9910461 | PMID: 36574679
- Evidence: Raw data were filtered, and the cleaned data were mapped to the locust genome sequence with HISAT2 software.
- Full pipeline: alignment/mapping [HISAT2] -> stage not stated [ImageJ, StringTie, edgeR]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: The resulting reads were mapped, using default parameters, with HISAT2 ( 72 ) using a GRCh38, release 84 genome and index.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### A receptor kinase senses sterol by coupling with elicitins in auxotrophic &lt;i&gt;Phytophthora&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2408186121 | PMCID: PMC11551405 | PMID: 39475635
- Evidence: The sequencing data underwent initial filtration, followed by the mapping of clean reads to the P. sojae P6497 genome using HISAT2 ( 60 ).
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [pheatmap]

### Free-swimming bacteria transcriptionally respond to shear flow. (PNAS 2024)

- DOI: 10.1073/pnas.2406688121 | PMCID: PMC11494325 | PMID: 39383001
- Evidence: Quality control and adapter trimming were performed with Illumina’s software bcl-convert, read mapping was performed with HISAT2 ( 40 ), and read quantification was performed using Subread’s featureCounts ( 41 ) functionality.
- Full pipeline: quality control [HISAT2, featureCounts] -> read trimming [HISAT2, edgeR, featureCounts] -> alignment/mapping [HISAT2, featureCounts] -> quantification [HISAT2, edgeR, featureCounts] -> normalisation [edgeR] -> stage not stated [ImageJ]

### The extension of mammalian pregnancy required taming inflammation: Independent evolution of extended placentation in the tammar wallaby. (PNAS 2024)

- DOI: 10.1073/pnas.2310047121 | PMCID: PMC11494332 | PMID: 39378090
- Evidence: Raw reads were aligned to the tammar wallaby genome v3.0 using hisat2, and reads were counted using htseq-count.
- Full pipeline: alignment/mapping [HISAT2, HTSeq]

### The &lt;i&gt;ivory&lt;/i&gt; lncRNA regulates seasonal color patterns in buckeye butterflies. (PNAS 2024)

- DOI: 10.1073/pnas.2403426121 | PMCID: PMC11474026 | PMID: 39352931
- Evidence: RNA-Seq datasets were aligned using HISAT2 on jcgen_v2.fa genome followed by Featurecounts using the Iso-Seq informed v3 annotations ( SI Appendix , Table S1 ).
- Full pipeline: alignment/mapping [HISAT2, MACS2] -> differential/statistical testing [DESeq2] -> stage not stated [AUGUSTUS, BUSCO v5.4.7]

### In vivo CRISPR screens identify &lt;i&gt;Mga&lt;/i&gt; as an immunotherapy target in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406325121 | PMCID: PMC11441491 | PMID: 39298484
- Evidence: Genome mapping was carried out using HISAT2 software ( 50 ) (v2.1.0) with the mouse reference genome (UCSC GRCm38/mm10).
- Full pipeline: alignment/mapping [HISAT2] -> variant calling [CellChat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [HTSeq v0.6.1p, Scanpy]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **2.2.1**
- Evidence: The processed reads were then mapped to the GRCm38 reference genome using HISAT2 (v2.2.1) ( 65 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Transdifferentiation occurs without resetting development-specific DNA methylation, a key determinant of full-function cell identity. (PNAS 2024)

- DOI: 10.1073/pnas.2411352121 | PMCID: PMC11441492 | PMID: 39292740
- Evidence: Low-quality bases and sequencing adaptors of raw fastq files RNA-seq containing single-end 61 bp-long reads were trimmed using Trim Galore (V 0.6.0, https://github.com/FelixKrueger/TrimGalore ) and then mapped to the mm10 reference genome using HISAT2 (V 2.1.0) with default parameters.
- Full pipeline: read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, SAMtools, Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, R]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Version used: **2.1.0**
- Evidence: Following quality assessment by FastQC (0.11.5, https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), the clean reads were aligned to their corresponding reference genomes with HISAT2 (version 2.1.0) ( 44 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### <i>Rickettsia</i> symbionts spread via mixed mode transmission, increasing female fecundity and sex ratio shift by host hormone modulating. (PNAS 2024)

- DOI: 10.1073/pnas.2406788121 | PMCID: PMC11194588 | PMID: 38865267
- Version used: **2.1.0**
- Evidence: Briefly, all of the clean tags were mapped to the reference genome of the whitefly with HISAT2 (v2.1.0) allowing no mismatches [( 64 ); http://www.whiteflygenomics.org/ftp/MED/ ].
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, MAFFT v7.520] -> differential/statistical testing [edgeR] -> structure determination [MrBayes v3.2.7]

### The role of mitochondria in sex- and age-specific gene expression in a species without sex chromosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2321267121 | PMCID: PMC11181141 | PMID: 38838014
- Version used: **2.1.0**
- Evidence: HISAT2 v2.1.0 ( 91 ) was utilized to align the reads with strict parameters (--score-min L,0,-0.6 --no-softclip --no-mixed --no-discordant) to only allow concordantly aligned read pairs.
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.38] -> read trimming [FastQC v0.11.8, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.7.2] -> stage not stated [WGCNA, featureCounts]

### SUMO-specific protease 1 regulates germinal center B cell response through deSUMOylation of PAX5. (PNAS 2024)

- DOI: 10.1073/pnas.2314619121 | PMCID: PMC11145296 | PMID: 38776375
- Evidence: Raw sequence was aligned to mouse genome (mm10) with HISAT2 software.
- Full pipeline: alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Clocking out and letting go to unleash green biotech applications in a photosynthetic host. (PNAS 2024)

- DOI: 10.1073/pnas.2318690121 | PMCID: PMC11127020 | PMID: 38739791
- Version used: **2.2.1**
- Evidence: Then, hisat2 v.
- Full pipeline: alignment/mapping [SAMtools v1.11.0] -> quantification [DESeq2 v1.36.0] -> normalisation [R] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HISAT2 v2.2.1, ggplot2, pheatmap v1.0.12]

### DELLA proteins recruit the Mediator complex subunit MED15 to coactivate transcription in land plants. (PNAS 2024)

- DOI: 10.1073/pnas.2319163121 | PMCID: PMC11087773 | PMID: 38696472
- Evidence: ...apt (with parameters ‘--minimum-length=20 --max-n=0.1 --quality-cutoff=30,30’) ( 46 ) and then mapped to the TAIR10 A. thaliana reference genome with HISAT2 ( 47 ). htseq-count was used for read count (parameters: ‘--format=bam --order=name --stranded=no’) ( 48 ), and TPMs calculated as a proxy to absolute gene expression levels.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9] -> alignment/mapping [Cutadapt, FastQC v0.11.9, HISAT2, HTSeq, MAFFT v7.0] -> quantification [Cutadapt, DESeq2 v1.24.0, FastQC v0.11.9, HISAT2, HTSeq] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [ggplot2]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Version used: **2.2.1**
- Evidence: Long RNA reads were mapped using HISAT2 version 2.2.1 ( 84 ) and multimapping reads were only mapped once to the reference genome adjusting the parameter - k to 1 .
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### Integrated mutational landscape analysis of poorly differentiated high-grade neuroendocrine carcinoma of the uterine cervix. (PNAS 2024)

- DOI: 10.1073/pnas.2321898121 | PMCID: PMC11046577 | PMID: 38625939
- Evidence: Sequencing reads were aligned and processed using HISAT2 ( 47 ) and HTSeq-count ( 48 ).
- Full pipeline: alignment/mapping [HISAT2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [CNVkit, GATK]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: Processed files were aligned to the mm10 assembly with hisat2 ( 32 ) and converted to bigwig files with deepTools ( 33 ) bamCoverage function.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Version used: **2.2.1**
- Evidence: Reads were aligned to the reference genome using hisat2 v2.2.1 ( 80 ) with parameters –no-unal –max-intronlen 25000 –dta and sorted using samtools ( 81 ) v1.12.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Normalizing granuloma vasculature and matrix improves drug delivery and reduces bacterial burden in tuberculosis-infected rabbits. (PNAS 2024)

- DOI: 10.1073/pnas.2321336121 | PMCID: PMC10998582 | PMID: 38530888
- Version used: **2.0.5**
- Evidence: The remaining reads (averaging 150 million/sample) were aligned to the Oryctolagus cuniculus genome (GenBank assembly GCA_000003625.1) using HISAT2 v2.0.5 ( 53 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> normalisation [DESeq2 v1.42.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.0] -> stage not stated [ImageJ]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Version used: **2.1.0**
- Evidence: Next, trimmed reads were aligned to the mSarHar1.11 ( 25 ) reference genome using HISAT2 version 2.1.0 ( 101 ) with the –dta flag and sorted using Samtools ( 82 ).
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### Enhanced weathering in the US Corn Belt delivers carbon removal with agronomic benefits. (PNAS 2024)

- DOI: 10.1073/pnas.2319436121 | PMCID: PMC10907306 | PMID: 38386712
- Evidence: The cleaned paired-read libraries were aligned against their reference genome sequence (Gmax JGI Wm82.a2.v1 for soybean, and Zmays 493 APGv4 for maize) using HISAT2 ( 66 ).
- Full pipeline: alignment/mapping [HISAT2, StringTie] -> differential/statistical testing [DESeq2]

### COP1 controls light-dependent chromatin remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2312853121 | PMCID: PMC10895365 | PMID: 38349881
- Evidence: RNA-seq clean reads were aligned to TAIR10 genome release using HISAT2 with default parameters.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, deepTools] -> normalisation [deepTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [ImageJ, MACS2]

### Ace2 safeguards embryonic hematopoietic stem and progenitor cell production by restraining Nlrp3-mediated pyroptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2515641122 | PMCID: PMC12704739 | PMID: 41348733
- Version used: **2.1.0**
- Evidence: Reads were mapped back to the zebrafish genome (danRer11 assembly) using HISAT2 (version 2.1.0) ( 66 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.1.0] -> quantification [StringTie v1.3.3b] -> dimensionality reduction/clustering [clusterProfiler v4.6.1] -> differential/statistical testing [DESeq2 v1.10.1, R v3.2.3] -> stage not stated [GSEA, ImageJ]

### Lamprey &lt;i&gt;FOXN1&lt;/i&gt; rescues the block of thymic epithelial cell development in the mouse &lt;i&gt;Foxn1&lt;/i&gt;-deficient thymic rudiment. (PNAS 2025)

- DOI: 10.1073/pnas.2520664122 | PMCID: PMC12685072 | PMID: 41289399
- Version used: **2.1.0**
- Evidence: Reads were aligned to the mouse reference genome GRCm38 with HISAT2 v2.1.0 ( 55 ).
- Full pipeline: read trimming [Cutadapt v4.9, STAR v2.7.11b] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, STAR v2.7.11b] -> differential/statistical testing [emmeans, limma] -> visualisation [STAR v2.7.11b] -> stage not stated [featureCounts v1.6.1]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Version used: **2.2.1**
- Evidence: Adapter sequences were trimmed using Trimmomatic v0.39 ( 80 ), and the processed reads were mapped to the reference genome using HISAT2 v2.2.1 ( 81 ).
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### An ADAR2-mimic base editor for efficient C-to-U RNA editing in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2505269122 | PMCID: PMC12625888 | PMID: 41196347
- Evidence: Subsequently, the filtered reads were mapped to the reference genome (GRCm39) by HISAT2 software (v.2.2.1).
- Full pipeline: quality control [FastQC v0.12.1, Trim Galore v0.6.10] -> read trimming [FastQC v0.12.1, HISAT2, Trim Galore v0.6.10] -> alignment/mapping [HISAT2] -> stage not stated [SAMtools v1.21, SnpEff v5.2]

### Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage. (PNAS 2025)

- DOI: 10.1073/pnas.2517473122 | PMCID: PMC12626013 | PMID: 41196353
- Version used: **2.1.0**
- Evidence: Raw transcript reads (in FastQ format) were used as an input for read alignment to the M. acetivorans C2A reference genome using HISAT2 (v.2.1.0).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [Cufflinks v2.2.1, DESeq2 v1.20.0, HISAT2 v2.1.0, MAFFT] -> stage not stated [Prokka, RAxML, SciPy]

### Lipid raft proteomics identify endothelial myosin-9 (MYH9) as a regulator of low-density lipoprotein transcytosis and atherosclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2509315122 | PMCID: PMC12582289 | PMID: 41134623
- Evidence: The filtered reads were then aligned to the hg38 reference genome by HISAT2 aligner ( 57 ).
- Full pipeline: read trimming [HISAT2] -> alignment/mapping [HISAT2] -> quantification [Cufflinks, ImageJ] -> stage not stated [Metascape]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **2.21**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Version used: **2.0.5**
- Evidence: After quality control, sequences were aligned to the closest available reference genome, Boleophthalmus pectinirostris (NCBI), the great blue-spotted mudskipper (belonging to the sister family Oxudercidae) using HISAT2 v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Ubiquitin-mediated degradation restricts spatiotemporal accumulation of the cytoplasmic male sterility protein WA352 to anthers in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2504381122 | PMCID: PMC12557538 | PMID: 41100672
- Evidence: The clean reads were first aligned to the rice (ZS97) reference genome ( http://rice.hzau.edu.cn/rice_rs2/ ) ( 46 ) using HISAT2; then StringTie was used to assemble transcripts and calculate the fragments per kilobase of transcript per million mapped reads (FPKM) for estimating gene expression levels ( 47 ).
- Full pipeline: alignment/mapping [HISAT2, StringTie] -> quantification [HISAT2, StringTie] -> stage not stated [AlphaFold, ColabFold]

### Genetic dissection of nonconventional introns reveals codominant noncanonical splicing code in &lt;i&gt;Euglena&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509937122 | PMCID: PMC12501133 | PMID: 40986342
- Evidence: Clean RNA-seq reads were mapped to the E. agilis genome scaffolds using HISAT2-v2.0.5 ( 43 ) with the parameters: “--pen-noncansplice = 0 -no-softclip”.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BLAST, HMMER, ImageJ]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: RNAseq reads were aligned to the annotated reference genome using HISAT2 ( 74 ) and StringTie2 ( 75 ).
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### Evidence for coopetition at the maternal-fetal interface shaping placental invasion. (PNAS 2025)

- DOI: 10.1073/pnas.2323038122 | PMCID: PMC12435225 | PMID: 40906814
- Evidence: RNAseq reads were aligned to the human transcriptome (GRCh38) using hisat2.
- Full pipeline: alignment/mapping [HISAT2] -> quantification [ImageJ] -> differential/statistical testing [DESeq2]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Evidence: After sequencing, data were aligned to the human reference genome Hg38/GRCh38 using HISAT2 [v2.1.0 ( 61 )] and to calculate the number of reads per gene HTSeq count [v0.5.3 ( 62 )] was used.
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### A 65-kb deletion survey identifies a distal &lt;i&gt;cis-&lt;/i&gt;regulatory region for red-light induction of &lt;i&gt;Ghd7&lt;/i&gt;, a key rice floral repressor. (PNAS 2025)

- DOI: 10.1073/pnas.2423119122 | PMCID: PMC12377723 | PMID: 40811470
- Version used: **2.2.1**
- Evidence: High-quality reads were aligned to the O. sativa ssp. japonica Nipponbare IRGSP-1.0 reference genome using HISAT2 (version 2.2.1).
- Full pipeline: quality control [FastQC v0.12.1, fastp v0.23.4] -> read trimming [FastQC v0.12.1, fastp v0.23.4] -> alignment/mapping [HISAT2 v2.2.1, minimap2] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [SAMtools v1.19, featureCounts]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **2.1.0**
- Evidence: To produce the aligned RNA-seq evidence, the RNAseq reads were quality filtered, trimmed, and paired with fastp ( 86 ) v0.22.0 (–qualified_quality_phred 20, –unqualified_percent_limit 20), and aligned to their source genome with hisat2 v2.1.0 ( 111 ) (–rna-strandness RF).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Version used: **2.2.1**
- Evidence: RNA-seq libraries were mapped to the Araport11 ( 46 ) reference genome using hisat2(v2.2.1) ( 47 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Version used: **2.2.1**
- Evidence: To reconstruct transcripts expressed in anthers, RNA-seq and nanoPARE reads were mapped to the reference genome using HISAT2 v2.2.1 ( 43 ) with default parameters.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### Deficiency in transmitter release triggers homeostatic transcriptional changes that increase presynaptic excitability. (PNAS 2025)

- DOI: 10.1073/pnas.2322714122 | PMCID: PMC12337328 | PMID: 40729383
- Version used: **2.1.0**
- Evidence: Mapping was performed with HISAT2 (ver 2.1.0) ( 81 ), and the counts matrix was generated with the featureCounts function from the Subread package (ver 1.6.4) ( 82 ).
- Full pipeline: quality control [FastQC v0.11.7, Trimmomatic v0.38] -> read trimming [FastQC v0.11.7, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0, featureCounts] -> normalisation [DESeq2 v1.26.0] -> visualisation [ggplot2 v3.2.1] -> stage not stated [R v4.1.0]

### A granulin-positive macrophage subtype in mycobacterial granulomas alleviates tissue damage by limiting excessive inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2413946122 | PMCID: PMC12337285 | PMID: 40729382
- Evidence: Briefly, RNA quality control was done with RseQC ( 119 ), and reads were aligned to the GRCz11 zebrafish reference genome ( 120 ) using HISAT2.
- Full pipeline: quality control [HISAT2] -> alignment/mapping [HISAT2] -> quantification [HTSeq] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler] -> stage not stated [DESeq2, STRING db]

### Foxn3 is required to suppress aberrant ciliogenesis in nonphotoreceptor retinal neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2500871122 | PMCID: PMC12304973 | PMID: 40663603
- Evidence: For data analysis, raw sequencing reads were aligned to the mm10 mouse reference genome using HISAT2 ( 74 ).
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [HOMER, Seurat, deepTools, scDblFinder]

### A transcriptomic, proteomic, and functional genetic atlas dissects neurofibromin function in the peripheral nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2506823122 | PMCID: PMC12260521 | PMID: 40587782
- Evidence: Reads were mapped to the appropriate reference genome (hg19) using HISAT2 with default parameters ( 32 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, ImageJ] -> differential/statistical testing [DESeq2, R] -> visualisation [Cytoscape, STRING db]

### Antlers on does: An unexpected role of macrophages in deer biology. (PNAS 2025)

- DOI: 10.1073/pnas.2424448122 | PMCID: PMC12184406 | PMID: 40512783
- Evidence: After cleaning the raw data, and using the deer reference genome, we utilized the workflows of HISAT2, StringTie, and DESeq2 ( 33 ) to analyze differentially expressed genes (DEGs) with |log 2 FoldChange| ≥ 2 and Benjamini–Hochberg P -value < 0.001 between two groups.
- Full pipeline: alignment/mapping [DESeq2, HISAT2, StringTie] -> quantification [ImageJ] -> normalisation [ImageJ] -> differential/statistical testing [DESeq2, HISAT2, StringTie] -> stage not stated [GSEA, Seurat]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Version used: **2.2.1**
- Evidence: To integrate these various efforts and incorporate new data from this study, we aligned sequence data from several independent studies to the assembly using HISAT2 v.2.2.1 ( 48 ) and generated provisional gene models using Stringtie v.2.2.3 ( 49 ).
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### A synthetic jasmonate receptor agonist uncouples the growth-defense trade-off in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2505675122 | PMCID: PMC12184649 | PMID: 40493190
- Evidence: Clean reads were mapped to the reference rice genome ( https://rice.plantbiology.msu.edu/pub/data/Eukaryotic_Projects/o_sativa/annotation_dbs/pseudomolecules/ ) using hisat2 ( 36 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> stage not stated [edgeR]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Evidence: Hisat2 v2.2.1 ( https://daehwankimlab.github.io/hisat2/ ) was used to align the reads to the house mouse genome (GCF_000001635.26), Stringtie v2.2.1 ( https://ccb.jhu.edu/software/stringtie/ ) to assemble the transcriptome, and DESeq2 v1.34.0 ( https://bioconductor.org/packages/release/bioc/html/DESeq2.html ) to analyze differential gene expression.
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: Transcriptomic data were aligned using HISAT2 and assembled with StringTie ( 34 , 35 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Unified molecular approach for spatial epigenome, transcriptome, and cell lineages. (PNAS 2025)

- DOI: 10.1073/pnas.2424070122 | PMCID: PMC12037033 | PMID: 40249782
- Evidence: ...q files to the mm10 or hg38 reference genome using parameters “--no-spliced-alignment --very-sensitive -X 2000.” The CB and UB tags were added to the hisat2 ATAC-seq alignments using the read name table created from spaceranger as well as a custom python script utilizing the “simplesam” package.
- Full pipeline: quality control [ArchR, Seurat] -> read trimming [fastp] -> alignment/mapping [HISAT2, Seurat, fastp] -> quantification [ArchR] -> dimensionality reduction/clustering [ArchR] -> visualisation [ggplot2]

### Diet-regulated transcriptional plasticity of plant parasites in plant-mutualist environments. (PNAS 2025)

- DOI: 10.1073/pnas.2421367122 | PMCID: PMC12037023 | PMID: 40244681
- Evidence: Reads were mapped to a G. pallida genome (PRJNA702104) via HISAT2 ( 52 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, HTSeq, ImageJ] -> differential/statistical testing [DESeq2, HTSeq] -> stage not stated [IQ-TREE]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Version used: **2.0.5**
- Evidence: Read mapping was conducted with HISAT2 (v2.0.5) using the Homo sapiens (human) genome assembly GRCh38 (hg38) as the reference.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Version used: **2.2.1**
- Evidence: Trimmed, paired-end, 150-bp reads were generated using Trim Galore (version 0.6.6, https://github.com/FelixKrueger/TrimGalore ) and aligned to the TAIR10 reference genome using HISAT2 (version 2.2.1, https://daehwankimlab.github.io/hisat2 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### The NAE1-mediated neddylation operates as an essential post-translational modification checkpoint for effector CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424061122 | PMCID: PMC11912420 | PMID: 40030035
- Evidence: The resulting raw reads were trimmed by Trim Galore v0.6.10 and aligned to reference genome mm10 with HISAT2 V2.2.1 in combination with Samtools V1.2.
- Full pipeline: read trimming [HISAT2, SAMtools, Trim Galore v0.6.10] -> alignment/mapping [HISAT2, SAMtools, Trim Galore v0.6.10] -> stage not stated [DESeq2, GSEA, pheatmap]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Version used: **2.0.4**
- Evidence: To identify differentially expressed genes, the deduplicated and trimmed reads were aligned with hisat2 v2.0.4 to the GENCODE Release M31 mouse assembly.
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### Druggable genome screens identify SPP as an antiviral host target for multiple flaviviruses. (PNAS 2025)

- DOI: 10.1073/pnas.2421573122 | PMCID: PMC11874179 | PMID: 39969998
- Evidence: Raw reads were aligned on the GRCh38 reference genome using HISAT2 ( 70 ).
- Full pipeline: alignment/mapping [HISAT2] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Version used: **2.2.1**
- Evidence: Raw RNA-seq reads were processed using Trimmomatic (v0.39) ( 78 ) for quality trimming and subsequently mapped to their respective genomes with HISAT2 (v.2.2.1) ( 79 ).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Extrinsic induction of apoptosis and tumor suppression via the p53-Reprimo-Hippo-YAP/TAZ-p73 pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2413126122 | PMCID: PMC11831151 | PMID: 39913207
- Version used: **2.1.0**
- Evidence: Sequenced reads from the RNA-seq experiment were aligned using HISAT2 2.1.0, and the transcriptome was assembled using Cufflinks 2.2.1.
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, HISAT2 v2.1.0] -> stage not stated [GSEA]

### Estimating realized relatedness in free-ranging macaques by inferring identity-by-descent segments. (PNAS 2025)

- DOI: 10.1073/pnas.2401106122 | PMCID: PMC11760927 | PMID: 39808663
- Evidence: After quality control (removing bases with Phred-score of a base call <20 starting from both 5′ and 3′ end of each read) and adapter trimming using cutadapt ( 82 ), we aligned the resulting reads to the rhesus macaque reference genome Mmul10 ( 83 ) using hisat2 ( 84 ).
- Full pipeline: quality control [Cutadapt, HISAT2] -> read trimming [Cutadapt, HISAT2] -> alignment/mapping [BCFtools v1.9, Cutadapt, HISAT2] -> variant calling [BCFtools v1.9] -> simulation/modelling [R v4.4] -> stage not stated [Picard]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: The RNA sequence was subjected to quality control (FastQC, a quality control tool for high-throughput sequence data and available online at: http://www.bioinformatics.babraham.ac.uk/projects/fastqc ), and trimmomatic (0.37; https://github.com/timflutre/trimmomatic ) to remove adapters, followed by alignment to the human genome (GRCh38) using HISAT2.2 ( https://daehwankimlab.github.io/hisat2/ ).
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **2.2.1**
- Evidence: Sequences were aligned to the reference genome assembly with hisat2 (version 2.2.1) ( 77 ), using default parameters to remove host sequences.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Version used: **2.2.1**
- Evidence: RNA-seq data from NCBI SRA were filtered ( Dataset S15 ), and then aligned to TM-1 genome via HISAT2 (v2.2.1) ( 77 ), and gene expression quantified by featureCounts (v2.0.1) ( 78 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Dynamic diversification of lignan metabolism in sesame via coordinated oxygenation and glucosylation across germination. (PNAS 2026)

- DOI: 10.1073/pnas.2605774123 | PMCID: PMC13250549 | PMID: 42247565
- Version used: **2.2.0**
- Evidence: RNA-seq reads were mapped to the S. indicum reference genome assembly (GCF_000512975.1) using HISAT2 version 2.2.0 ( 68 ), together with previously reported RNAseq data from S. indicum cv.
- Full pipeline: alignment/mapping [HISAT2 v2.2.0] -> quantification [StringTie v2.2.1]

### WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2534844123 | PMCID: PMC13099603 | PMID: 41984841
- Evidence: For ChIP-seq analysis, raw single-end reads were trimmed with Trim Galore! and aligned to the human reference genome (hg38) using HISAT2, retaining only uniquely mapped reads with mapping quality ≥10.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, Trim Galore] -> quantification [deepTools] -> normalisation [deepTools] -> differential/statistical testing [DESeq2 v1.28.1, R] -> stage not stated [GSEA, SAMtools]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Version used: **2.2.1**
- Evidence: RNA-seq reads were aligned with the indexed Lcr BT-1 genome assembly ( NC_019907.1 ) and were parsed to it using HISAT2 v.2.2.1 ( 68 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### A host-derived volatile primes context-dependent foraging behavior in parasitic nematodes via a lysosome-associated neural pathway. (PNAS 2026)

- DOI: 10.1073/pnas.2520778123 | PMCID: PMC12933127 | PMID: 41706887
- Version used: **2.1.0**
- Evidence: Clean reads were aligned to the S. carpocapsae reference genome (GCA_000757645.3) using HISAT2 v2.1.0 ( 60 ), and PCR duplicates were removed using Picard Tools v2.25.1.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HISAT2 v2.1.0, Picard] -> quantification [HTSeq] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [AlphaFold, PyMOL v3.1]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Version used: **2.2.1**
- Evidence: We aligned the RNA-seq reads to their corresponding fungal genome using HISAT2 v.2.2.1 ( 80 ).
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

### The immunopathological landscape of human pre-TCRα deficiency: From rare to common variants. (Science 2024)

- DOI: 10.1126/science.adh4059 | PMCID: PMC10958617 | PMID: 38422122
- Version used: **2.2.1**
- Evidence: The sequence reads were aligned with the human hg38 reference genome assembly with HISAT2 v2.2.1, using the -k 1 function ( 49 ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, SAMtools v1.14] -> differential/statistical testing [R, tidyverse] -> visualisation [R, tidyverse] -> stage not stated [MACS2, Seurat v4.0.4, kallisto v0.46.1]

