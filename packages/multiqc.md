# MultiQC

- **Category:** genomics
- **Papers in survey:** 61
- **Journals:** PNAS (30), Nature (27), Cell (3), Science (1)
- **Years:** 2021 (6), 2022 (8), 2023 (9), 2024 (15), 2025 (16), 2026 (7)
- **Versions named:** 1.9 (7), 1.8 (5), 1.12 (3), 1.11 (3), 1.23 (2), 1.13 (2), 1.10 (2), 0.9 (2), 1.10.1 (1), 0.92 (1)
- **Pipeline stages it appears in:** quality control (61), alignment/mapping (11), read trimming (11), visualisation (6), quantification (4), differential/statistical testing (3), dimensionality reduction/clustering (1)

## Papers

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Version used: **1.9**
- Evidence: ...w.graphpad.com/ FlowJo 10.5.3 FlowJo, LLC https://www.flowjo.com FastQC Babraham Institute https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ MultiQC 1.9 MultiQC https://multiqc.info/ Trimmomatic 0.39 USADELLAB http://www.usadellab.org/cms/?page=trimmomatic MiXCR MI Lanoratory https://mixcr.readthedocs.io/en/master/index.html NumPy NumPy https://numpy.org/ Python 3.7.4 Python Software Foun...
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **1.9**
- Evidence: The quality of the reads from the RNA sequencing was analysed with FastQC v0.11.9, 99 and visualized using MultiQC v1.9.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **1.8**
- Evidence: 102 https://bioconductor.org/packages/release/bioc/html/DESeq2.html FastQC v0.11.9 Andrew 103 http://www.bioinformatics.babraham.ac.uk/projects/fastqc MultiQC v1.8 Ewels et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Evidence: We used MultiQC 50 (v1.8) to summarize the FastQC results.
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Akkermansia muciniphila phospholipid induces homeostatic immune responses. (Nature 2022)

- DOI: 10.1038/s41586-022-04985-7 | PMCID: PMC9328018 | PMID: 35896748
- Version used: **1.8**
- Evidence: FastQC v.0.11.5 and MultiQC v.1.8 were used to confirm the quality of the sequenced libraries 42 , 43 .
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.8] -> alignment/mapping [BLAST, kallisto v0.46.1] -> differential/statistical testing [edgeR v3.35.1] -> stage not stated [ChimeraX v1.0, Coot v0.9, FSL]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Version used: **1.7**
- Evidence: Read and tool performance statistics were aggregated across samples and steps using MultiQC (v.1.7).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### RNA profiles reveal signatures of future health and disease in pregnancy. (Nature 2022)

- DOI: 10.1038/s41586-021-04249-w | PMCID: PMC8770117 | PMID: 34987224
- Evidence: Analysis for outliers qPCR of ACTB as well as MultiQC sequencing metrics were monitored to eliminate sample outliers before performing gene expression analyses.
- Full pipeline: quality control [MultiQC] -> read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, Picard, R, fgsea]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Version used: **1.9**
- Evidence: Data quality was assessed with FastQC v.0.11.9 ( https://github.com/s-andrews/FastQC ) and MultiQC v.1.9 ( https://multiqc.info/ ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Pervasive downstream RNA hairpins dynamically dictate start-codon selection. (Nature 2023)

- DOI: 10.1038/s41586-023-06500-y | PMCID: PMC10499604 | PMID: 37674078
- Version used: **1.9**
- Evidence: 54 ) and MultiQC v.1.9 (ref.
- Full pipeline: quality control [Cutadapt, FastQC, MultiQC v1.9, Trim Galore v0.6.6] -> read trimming [Bowtie2 v2.4.2, Cutadapt, FastQC, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [AlphaFold, STAR v2.7.8a]

### GDF15 promotes weight loss by enhancing energy expenditure in muscle. (Nature 2023)

- DOI: 10.1038/s41586-023-06249-4 | PMCID: PMC10322716 | PMID: 37380764
- Evidence: MultiQC was used for quality control of raw data from RNA-seq 57 .
- Full pipeline: quality control [MultiQC, Trim Galore] -> read trimming [Trim Galore] -> quantification [DESeq2] -> stage not stated [R, TwoSampleMR]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **1.9**
- Evidence: FastQC, QoRTs and Somalier outputs were visualized using MultiQC (v.1.9) 59 .
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Version used: **1.12**
- Evidence: Sample quality was assessed using FastQC v0.11.9 39 and MultiQC 1.12 40 ; sample reads were trimmed for both quality and length using Trimmomatic 0.39 41 with the following options: removal of TruSeq adapters sequences; sliding window trimming, clipping the read once the average quality within the window (4 bp) falls below 20; finally, drop the read if it is shorter than 38 bp (Supplementary Table...
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Libraries were sequenced on either the NextSeq 2000 (50 bp paired-end reads: CRISPR, roxadustat and PD-0325901 experiments) or NovaSeq 6000 (100 bp paired-end reads: overexpression experiments) system and preprocessed using MultiQC.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Version used: **1.11**
- Evidence: Although allowing robust detection of all sncRNA biotypes, this library preparation method does not efficiently capture highly modified sncRNAs, such as tsRNAs and rsRNAs. sncRNA-seq analysis Raw sequencing data were quality checked using MultiQC v1.11.
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Single-cell analysis reveals context-dependent, cell-level selection of mtDNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07332-0 | PMCID: PMC11078733 | PMID: 38658765
- Version used: **1.11**
- Evidence: The read quality in each FASTQ file was verified using the FASTQC tool v0.11.9 and aggregated into a single report per sequencing run using MultiQC v1.11.
- Full pipeline: quality control [MultiQC v1.11] -> stage not stated [Matplotlib v3.4.2, NumPy v1.21.0, R, SciPy v1.7.0, scikit-learn v0.23.1, seaborn v0.11.1]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: The quality of the raw sequencing reads was assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and MultiQC.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: 62 ) and RSeQC 63 , with the results visualized using MultiQC 64 .
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### Cas9 senses CRISPR RNA abundance to regulate CRISPR spacer acquisition. (Nature 2025)

- DOI: 10.1038/s41586-025-09577-9 | PMCID: PMC12477760 | PMID: 40902823
- Version used: **0.92**
- Evidence: Bioinformatics analysis for NGS datasets Read processing Sequencing reads were assessed for quality using FastQC (v.0.11.8) 55 and MultiQC (v.0.92) 56 to ensure the general quality of the datasets.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v0.92] -> read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9, minimap2] -> stage not stated [BEDTools]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Version used: **6.14**
- Evidence: The quality of each raw FASTQ file (for both scRNA-seq and scATAC-seq) was initially checked using MultiQC (6.14).
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **1.13**
- Evidence: Quality assessment of RNA-seq data, including sequence, alignment and quantification metrics, was conducted using FastQC v.0.12.1 and summarized with MultiQC v.1.13.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Evidence: Mapping rates, GC content and other sample quality metrics were derived from nf-core via MultiQC.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **1.8**
- Evidence: 46 ) and summarized with MultiQC v.1.8 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Version used: **1.9**
- Evidence: Mapping of RNA-seq expression data Quality checks and trimming on the raw RNA-seq data files were done using FastQC v.0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), FastP (v.0.20.1) 58 , MultiQC (v.1.9) 59 and FastQ Screen (v.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Version used: **1.23**
- Evidence: Bioinformatic analysis After Illumina sequencing, standard bioinformatics analysis were used to generate fastq files, followed by quality assessment (fastqc v0.11.9 and MultiQC v1.23).
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **1.8**
- Evidence: Read quality was verified using FastQC v.0.11.8 and MultiQC v.1.8.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **1.8**
- Evidence: RNA-seq sequence, alignment and quantification qualities were assessed using FastQC (v.0.11.5) and MultiQC (v.1.8) 69 .
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **1.10.1**
- Evidence: The quality of the raw sequencing data was assessed using FastQC (v.0.11.9) and MultiQC (v.1.10.1).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: Sequencing quality was assessed using FastQC 71 v.0.11.6 and MultiQC 72 v.1.7 viewer for aggregated reports.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: The resulting MultiQC report was inspected to ensure overall sequencing quality and pipeline performance.
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: The MultiQC tool was used to aggregate quality metrics.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Amino acids activate mTORC1 to release roe deer embryos from decelerated proliferation during diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2100500118 | PMCID: PMC8536382 | PMID: 34452997
- Evidence: Basic read statistics and read quality was evaluated based on FastQC reports ( 64 ), and a MultiQC overview report of all samples was generated ( 65 ).
- Full pipeline: quality control [FastQC, MultiQC] -> differential/statistical testing [FastQC, MultiQC, R] -> stage not stated [Galaxy, Trim Galore]

### Microbiome signatures of progression toward celiac disease onset in at-risk children in a longitudinal prospective cohort study. (PNAS 2021)

- DOI: 10.1073/pnas.2020322118 | PMCID: PMC8307711 | PMID: 34253606
- Evidence: In accordance with our previously published work ( 19 ), sequence quality assessment and trimming of metagenomic reads were performed by using the MultiQC approach ( 79 ).
- Full pipeline: quality control [MultiQC] -> read trimming [MultiQC] -> stage not stated [Python, SciPy]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Evidence: For a better visualization and comparison of the qualities of all libraries, MultiQC ( 55 ) was used to concatenate the results of FastQC.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **0.9**
- Evidence: Quality control was performed using fastQC (v0.11.17) and MultiQC (v0.9).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### A male pheromone that improves the quality of the oogenic germline. (PNAS 2022)

- DOI: 10.1073/pnas.2015576119 | PMCID: PMC9173808 | PMID: 35576466
- Evidence: The pipeline used MultiQC to assemble the final HTML report ( 78 ).
- Full pipeline: quality control [MultiQC, Nextflow] -> differential/statistical testing [DESeq2 v1.32.0, NumPy, R v4.1, SciPy] -> stage not stated [Matplotlib, seaborn]

### Prevention of the foreign body response to implantable medical devices by inflammasome inhibition. (PNAS 2022)

- DOI: 10.1073/pnas.2115857119 | PMCID: PMC8944905 | PMID: 35298334
- Version used: **0.9**
- Evidence: Alignments and quality control (QC) were processed using Cluster Flow (v0.5dev) ( 49 ) pipelines (FASTQC, Trim_galore) and summarized using MultiQC (0.9.dev0) ( 50 ).
- Full pipeline: quality control [MultiQC v0.9, featureCounts v1.5.0] -> alignment/mapping [MultiQC v0.9, STAR] -> quantification [DESeq2, HTSeq, R v3.4] -> normalisation [DESeq2, R v3.4] -> dimensionality reduction/clustering [MultiQC v0.9] -> differential/statistical testing [DESeq2, R v3.4] -> stage not stated [ImageJ]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: Quality control was conducted using fastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and MultiQC ( 57 ).
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Version used: **1.9**
- Evidence: At each step, MultiQC v1.9 was used to track analysis quality ( 55 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### Mouse models of <i>SYNGAP1</i>-related intellectual disability. (PNAS 2023)

- DOI: 10.1073/pnas.2308891120 | PMCID: PMC10500186 | PMID: 37669379
- Evidence: The quality of STAR alignments was assessed for evenness of coverage, ribosomal RNA content, exon and intron mapping rate, complexity, and other criteria using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), Qualimap ( 59 ), and MultiQC ( 60 ).
- Full pipeline: quality control [FastQC, MultiQC, STAR, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [GSEA, R]

### SARS-CoV-2 mouse adaptation selects virulence mutations that cause TNF-driven age-dependent severe disease with human correlates. (PNAS 2023)

- DOI: 10.1073/pnas.2301689120 | PMCID: PMC10410703 | PMID: 37523564
- Version used: **1.12**
- Evidence: Individual FastQC files were consolidated into a single report using MultiQC (v1.12, https://multiqc.info/ , Dataset S3 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.12] -> alignment/mapping [featureCounts, minimap2 v2.2.4] -> quantification [featureCounts] -> machine learning [StarDist] -> stage not stated [R v4.2, edgeR, limma]

### Application of a quantitative framework to improve the accuracy of a bacterial infection model. (PNAS 2023)

- DOI: 10.1073/pnas.2221542120 | PMCID: PMC10175807 | PMID: 37126703
- Version used: **1.10**
- Evidence: At each step, MultiQC v1.10 was used to track analysis quality ( 54 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.10] -> read trimming [Bowtie2 v2.3.5, Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> normalisation [DESeq2 v1.28.1, R] -> stage not stated [BLAST]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Reads were aligned to hg38 using a Bpipe ( 92 ) RNA-Seq pipeline that incorporated FastQC quality control, adaptor trimming with Trimmomatic v.0.35 ( 93 ), mapping with STAR 2.7.3a ( 94 ), summarizing reads over genes with featureCounts ( 95 ), and MultiQC ( 96 ) to summarize the analyses.
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### CryoSeek: A strategy for bioentity discovery using cryoelectron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2417046121 | PMCID: PMC11494351 | PMID: 39382995
- Evidence: For data analysis, the metagenomic sequencing samples were quality controlled using MultiQC ( 40 ).
- Full pipeline: quality control [MultiQC] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2]

### Machine learning reveals the transcriptional regulatory network and circadian dynamics of &lt;i&gt;Synechococcus elongatus&lt;/i&gt; PCC 7942. (PNAS 2024)

- DOI: 10.1073/pnas.2410492121 | PMCID: PMC11420160 | PMID: 39269777
- Evidence: The quality control metrics are compiled using MultiQC ( 56 ), and the final expression dataset is reported in units of log-transformed Transcripts per Million (log-TPM).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore, featureCounts] -> read trimming [FastQC, Trim Galore] -> quantification [MultiQC, featureCounts] -> dimensionality reduction/clustering [STRING db] -> stage not stated [scikit-learn]

### Beneficial metabolic effects of PAHSAs depend on the gut microbiota in diet-induced obese mice but not in chow-fed mice. (PNAS 2024)

- DOI: 10.1073/pnas.2318691121 | PMCID: PMC11252816 | PMID: 38968121
- Evidence: To ensure read quality, raw reads were assessed using FastQC and MultiQC, and host reads with low quality ends (Phred scores < 28) were filtered using Kneaddata quality control software ( 25 ) for automatic adapter detection, trimming low-quality read bases, and removing host (mouse genome) reads prior to downstream analyses.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, MultiQC] -> alignment/mapping [BLAST, HUMAnN, MetaPhlAn] -> quantification [HUMAnN, MetaPhlAn] -> dimensionality reduction/clustering [BLAST] -> stage not stated [DADA2]

### The DNA damage response of <i>Escherichia coli</i>, revisited: Differential gene expression after replication inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2407832121 | PMCID: PMC11228462 | PMID: 38935560
- Evidence: MultiQC was used to evaluate the quality of reads, trimming and alignment; all mean FASTQC Phred scores were >30.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, MultiQC] -> alignment/mapping [MultiQC, STAR] -> quantification [edgeR v3.18] -> normalisation [Bioconductor, DESeq2 v1.42.0] -> differential/statistical testing [Bioconductor, DESeq2 v1.42.0] -> stage not stated [R v4.3, ggplot2 v3.5.0]

### Capturing the fusion of two ancestries and kinship structures in Merovingian Flanders. (PNAS 2024)

- DOI: 10.1073/pnas.2406734121 | PMCID: PMC11228521 | PMID: 38913897
- Evidence: Sequencing data were quality checked using FASTQC and MultiQC at multiple points during the analysis.
- Full pipeline: quality control [ANGSD, MultiQC] -> dimensionality reduction/clustering [UMAP]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles up-regulate and directly transfer adherence factors promoting host cell colonization. (PNAS 2024)

- DOI: 10.1073/pnas.2401159121 | PMCID: PMC11194581 | PMID: 38865261
- Evidence: Sample alignment and quality was assessed using MultiQC ( SI Appendix , Fig.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [Galaxy]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Version used: **1.12**
- Evidence: Quality was assessed with FastQC v0.11.5 and MultiQC v1.12 ( 50 ).
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Version used: **1.10**
- Evidence: Sequencing run statistics and quality metric were visualized for each sample using FastQC version 0.11.9 and then compared to each other using MultiQC version 1.10 ( 66 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: The quality of the raw and trimmed reads was assessed using FastQC and MultiQC ( 54 , 55 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Version used: **1.11**
- Evidence: Quality checks of raw and concatenated FASTQ files were done by FastQC (v0.11.9), and compared using MultiQC (v1.11) ( 50 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### The sleep-wake history contributes to rhythmic BMAL1 chromatin binding in the cerebral cortex but not in the liver. (PNAS 2025)

- DOI: 10.1073/pnas.2515047122 | PMCID: PMC12685114 | PMID: 41296730
- Evidence: MultiQC ( 68 ) was used to visualize read and alignment QC for all samples simultaneously.
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, MultiQC, edgeR] -> visualisation [MultiQC] -> stage not stated [R]

### Global profiling of polyketide synthases in facultative multicellular eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2515852122 | PMCID: PMC12625978 | PMID: 41191498
- Evidence: MultiQC was used to aggregate quality control metrics.
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> machine learning [Cellpose] -> visualisation [R, clusterProfiler] -> stage not stated [TrackMate]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **1.23**
- Evidence: Raw reads were processed using fastp (v0.23.4; poly-G trimming enabled, minimum length 150 bp, quality/N-content filtering) and assessed for quality (FastQC v0.12.1, MultiQC v1.23).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Methanogenesis inhibition remodels microbial fermentation and stimulates acetogenesis in ruminants. (PNAS 2025)

- DOI: 10.1073/pnas.2514823122 | PMCID: PMC12541428 | PMID: 41052332
- Version used: **1.13**
- Evidence: Read quality assessment was performed using FastQC (v0.11.9) ( 87 ) coupled with MultiQC (v1.13) ( 88 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.13] -> alignment/mapping [Salmon v1.10.2] -> normalisation [seaborn] -> simulation/modelling [AlphaFold]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles suppress IFNε-mediated responses driven by its intracellular bacterial symbiont &lt;i&gt;Mycoplasma hominis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2508297122 | PMCID: PMC12232435 | PMID: 40560611
- Evidence: Sample alignment and quality was assessed using MultiQC ( SI Appendix , Fig.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [GSEA]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Evidence: Reads were demultiplexed with CASAVA (Illumina, San Diego, CA) and read quality was assessed using FastQC ( 93 ) and MultiQC ( 94 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Version used: **1.1**
- Evidence: Quality control was conducted with FastQC v 0.11.8 ( 114 ), Qualimap v.2.2.1 ( 115 ), and MultiQC version 1.1 ( 116 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### Abscisic acid signaling gates salt-induced responses of plant roots. (PNAS 2025)

- DOI: 10.1073/pnas.2406373122 | PMCID: PMC11831169 | PMID: 39908104
- Evidence: First read quality was analyzed with FastQC ( 56 ) and MultiQC ( 57 ) packages in Python 2.7, followed by trimming of low quality reads with Trim Galore!
- Full pipeline: quality control [FastQC, MultiQC, Python v2.7, Trim Galore] -> read trimming [FastQC, MultiQC, Python v2.7, Trim Galore] -> alignment/mapping [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, R] -> stage not stated [OpenCV v4.5.1.48]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: The ratio of the observed-to-expected read count was calculated using the samtools module of MultiQC software.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

