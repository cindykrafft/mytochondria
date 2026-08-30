# Salmon

- **Category:** genomics
- **Papers in survey:** 23
- **Journals:** Nature (17), PNAS (6)
- **Years:** 2021 (2), 2022 (3), 2023 (2), 2024 (4), 2025 (5), 2026 (7)
- **Versions named:** 0.14.1 (3), 1.10.1 (3), 1.4.0 (3), 1.10.2 (2), 1.5.1 (2), 0.7.2 (1), 0.13.1 (1), 1.2.1 (1), 1.10.0 (1), 1.9.0 (1)
- **Pipeline stages it appears in:** quantification (16), alignment/mapping (13), read trimming (2), quality control (1), normalisation (1)

## Papers

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **0.14**
- Evidence: ...gmentation and Integer Copy Number’ Analysis of Bulk RNA-Seq Expression Data Transcript abundances for expanded clones triplicates were quantified by Salmon (v.0.14) 58 with GENCODE transcript v30 59 and options -l A −1 read1 −2 read2 -p 40 --validateMappings --seqBias --gcBias.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **1.4.0**
- Evidence: For PDV-WT and Lepr KO grafted SCC samples, raw reads were mapped to the decoy-aware mouse genome (UCSC release mm10) using Salmon (v.1.4.0) 59 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### The role of somatosensory innervation of adipose tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05137-7 | PMCID: PMC9477745 | PMID: 36045288
- Version used: **1.5.1**
- Evidence: RNA-seq analysis Sequenced reads were aligned to the GRCm39 reference genome (Ensembl, v.104; http://uswest.ensembl.org/Mus_musculus/Info/Index ), and gene counts were quantified using Salmon (v.1.5.1) 59 .
- Full pipeline: alignment/mapping [SAMtools v1.10, Salmon v1.5.1] -> quantification [ImageJ, Salmon v1.5.1] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [Metascape]

### Post-translational control of beige fat biogenesis by PRDM16 stabilization. (Nature 2022)

- DOI: 10.1038/s41586-022-05067-4 | PMCID: PMC9433319 | PMID: 35978186
- Version used: **1.4.0**
- Evidence: Salmon (v.1.4.0) 43 was used to simultaneously map and quantify reads to transcripts in the GENCODE M24 genome annotation of GRCm38/mm10 mouse assembly.
- Full pipeline: read trimming [edgeR, fastp v0.20.1] -> alignment/mapping [Bowtie2 v2.1.0, RSEM v1.2.15] -> quantification [Salmon v1.4.0] -> normalisation [edgeR] -> stage not stated [Enrichr]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **1.9.0**
- Evidence: The mpmap-RPVG pipeline was compared with Salmon (v.1.9.0) 131 and RSEM (v.1.3.3) 132 .
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Antibodies against endogenous retroviruses promote lung cancer immunotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05771-9 | PMCID: PMC10115647 | PMID: 37046094
- Version used: **0.12.0**
- Evidence: In brief, TPM values were calculated for all transcripts in the transcript assembly with a custom Bash pipeline using GNU parallel and Salmon (v.0.12.0) 59 .
- Full pipeline: quantification [Salmon v0.12.0] -> differential/statistical testing [lme4 v1.1.27.1] -> stage not stated [QuPath v0.3, R, RepeatMasker, data.table v1.14.2, survival (R) v3.2.13, tidyverse v1.0.7]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **1.2.1**
- Evidence: Gene-level read counts were obtained using Salmon (v.1.2.1, RRID: SCR_017036 ) for all libraries.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Version used: **0.14.1**
- Evidence: Salmon (v.0.14.1) 79 was used to create a customized reference transcriptome set that includes human genome transcriptome (hg38) and ERVmap database.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **1.4.0**
- Evidence: The expression values of each gene were quantified as both raw counts and transcripts per million (TPM) using Salmon (v.1.4.0) 70 , and compiled in R (v.3.6.1) using RStudio (v.3.4.2) by Tximport (v.1.12.3) 71 .
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **1.10.0**
- Evidence: The expression of paralogous genes in lamprey neural crest was assessed by quantifying gene expression using Salmon (v.1.10.0) 107 from RNA-seq data generated in a previous study 56 on dissected cranial and trunk dissected tissues using the latest lamprey genome and annotation 7 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **1.5.1**
- Evidence: For all species, the clean reads were aligned using Salmon (v.1.5.1) 66 to longest coding sequence (CDS) of each gene extracted from corresponding genome assembly based on human-referenced TOGA annotations.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Version used: **1.10.1**
- Evidence: Reads were trimmed with Cutadapt 69 and aligned to the mouse transcriptome (GRCm38, Ensembl release 102) using STAR (v.2.7.9a) 70 and quantified using Salmon (v.1.10.1) 71 .
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Version used: **0.13.1**
- Evidence: For transcript quantification, reads were mapped to mm10 (gencode.vM18.annotation.gtf) using Salmon v.0.13.1 with the options ‘--libType A --validateMappings --rangeFactorizationBins 4 --gcBias’.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **0.14.1**
- Evidence: Expression quantification of the transcripts was done using Salmon (v.0.14.1) 61 with the GRCm38 (mm10) mouse reference genome.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **1.10.1**
- Evidence: Briefly, FASTQ files underwent quality control (FastQC v.0.12.1), adaptors were trimmed (Trim Galore! v.0.6.7), reads were aligned to the GRCh38 human reference transcriptome (STAR v.2.7.9a) and a gene expression matrix was generated (Salmon v.1.10.1).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Version used: **1.10.2**
- Evidence: We first performed transcript quantification from FASTQ files using Salmon (v.1.10.2) 59 and GENCODE (v.43) 60 reference files.
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Version used: **0.7.2**
- Evidence: Transcript abundance was quantified with Salmon v.0.7.2 using quasi-mapping mode and corrected for sequence, GC and positional biases, using the mouse genome GRCm38 GENCODE release M11.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Heat stress destabilizes symbiotic nutrient cycling in corals. (PNAS 2021)

- DOI: 10.1073/pnas.2022653118 | PMCID: PMC7865147 | PMID: 33500354
- Version used: **1.0.0**
- Evidence: Gene expression was quantified with Salmon v.1.0.0 ( 91 ) using the alignment-based mode.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [FastQC v0.11.5, Trimmomatic v0.39] -> alignment/mapping [Salmon v1.0.0] -> quantification [Salmon v1.0.0, lme4] -> differential/statistical testing [R, vegan v2.5] -> stage not stated [ImageJ]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Version used: **1.10.1**
- Evidence: Transcripts were indexed using Salmon v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Methanogenesis inhibition remodels microbial fermentation and stimulates acetogenesis in ruminants. (PNAS 2025)

- DOI: 10.1073/pnas.2514823122 | PMCID: PMC12541428 | PMID: 41052332
- Version used: **1.10.2**
- Evidence: An overall mapping rate of 65.7% was achieved based on predicted gene sequences from MAGs using Salmon (v 1.10.2) ( 104 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.13] -> alignment/mapping [Salmon v1.10.2] -> normalisation [seaborn] -> simulation/modelling [AlphaFold]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Version used: **1.10.3**
- Evidence: Sequence alignment map (SAM) files from STAR mapper were used to quantify oyster transcripts at the isoform level and normalized by gene length and sample sequencing depth as fragments per kilobase million (FPKM) using Salmon v.1.10.3 ( 72 ).
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### The Nemp1-Nesprin complex mediates cellular responses to matrix mechanics. (PNAS 2026)

- DOI: 10.1073/pnas.2521253123 | PMCID: PMC12956887 | PMID: 41730104
- Version used: **1.8.0**
- Evidence: For transcriptome analysis, RNA-seq reads were aligned and quantitated to the reference transcriptome and quantitated to GRCh38 (Ensembl release 111) transcriptome using Salmon v.1.8.0 [1].
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [Salmon v1.8.0] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [R, clusterProfiler v4.10.1, edgeR] -> visualisation [pheatmap v1.0.12]

### Early life-stage thermal resilience is determined by climate-linked regulatory variation. (PNAS 2026)

- DOI: 10.1073/pnas.2518358123 | PMCID: PMC12799179 | PMID: 41505517
- Version used: **0.14.1**
- Evidence: Reads were aligned to the reference genome (DM6 with ensembl gene annotation v.10) and quantified using salmon (v.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Salmon v0.14.1] -> quantification [Salmon v0.14.1] -> stage not stated [DESeq2, R, SAMtools v1.10]

