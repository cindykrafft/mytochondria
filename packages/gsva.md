# GSVA

- **Category:** genomics
- **Papers in survey:** 71
- **Journals:** PNAS (36), Nature (30), Cell (4), Science (1)
- **Years:** 2021 (5), 2022 (8), 2023 (9), 2024 (13), 2025 (27), 2026 (9)
- **Versions named:** 1.46.0 (3), 1.50.5 (1), 1.46 (1), 1.44.1 (1), 1.44.5 (1), 1.4 (1), 1.42.0 (1), 1.44.3 (1)
- **Pipeline stages it appears in:** differential/statistical testing (7), quantification (4), dimensionality reduction/clustering (4), normalisation (3), visualisation (3), simulation/modelling (1)

## Papers

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: (B and C) Scatterplot showing the correlations between the indicated signature scores (computed using GSVA) and the glucocorticoid response signature score (B) or the TSC22D3 mRNA expression level (C) in CD56 dim CD16 hi NK cells.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Evidence: Patient grouping defined by immune polarization and enriched GSVA ( Gene Set Variation Analysis ) pathways and plasma proteins, related to Figures 5, S3, S4, and S6 Patient groupings defined by immune polarization in Figure 5 and enriched GSVA pathways and plasma proteins for each of the patient groupings are shown.
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### CSF proteomics identifies early changes in autosomal dominant Alzheimer's disease. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.049 | PMCID: PMC11531390 | PMID: 39332414
- Evidence: Co-expression network analysis of significant pseudo-trajectory proteins and pathway enrichment for each module (A) Heatmap showing GSVA scores for each cell type across modules.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.0] -> simulation/modelling [GSVA] -> visualisation [ggplot2] -> stage not stated [R v4.1.3, WGCNA]

### Pan-cancer proteogenomics characterization of tumor immunity. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.027 | PMCID: PMC10988632 | PMID: 38359819
- Evidence: To visualize differential pathway activity, pathway scores based on proteomics and RNAseq were computed via combined z-score using the R package GSVA.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, Enrichr] -> differential/statistical testing [GSVA, SciPy] -> machine learning [R] -> visualisation [GSVA] -> stage not stated [Cellpose, scikit-image]

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Evidence: For each multi-region tumour ( n = 17), the TPM expression of protein-coding genes converted to entrez gene IDs ( n = 18,950) was used as input for single-sample gene set enrichment analysis using the GSVA R package v.1.42.0 (ref.
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### Non-viral, specifically targeted CAR-T cells achieve high safety and efficacy in B-NHL. (Nature 2022)

- DOI: 10.1038/s41586-022-05140-y | PMCID: PMC9452296 | PMID: 36045296
- Evidence: The gene set variation analysis (GSVA) scores of CD8 memory, dysfunction and cytotoxicity signatures are shown at the top. b, tSNE plots showing C1 and C2 in each sample. c, Percentages of C1 and C2 in mixed samples. d-e, Comparison of C1 and C2 proportion between CAR+ and CAR− cells in mixed (d) and individual (e) samples.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [GSVA, UMAP] -> differential/statistical testing [Seurat] -> stage not stated [GSEA, fastp]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Evidence: Enrichment scores were computed by ssGSEA applying the ‘GSVA’ package in R 55 , using the top and bottom 150 differentially expressed genes. ssGSEA scores of patients from the TCGA were then plotted with regard to the occurrence of lymph node metastasis.
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: GSEA GSVA and ssGSEA were performed using the GSVA R package (version 1.34) 79 on (1) the GGI gene set 24 , (2) the core embryonic stem-cell-like module 25 and (3) the STAT1 immune signature 31 .
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Autoantibodies against type I IFNs in humans with alternative NF-κB pathway deficiency. (Nature 2023)

- DOI: 10.1038/s41586-023-06717-x | PMCID: PMC10665196 | PMID: 37938781
- Evidence: We calculated an IFN module enrichment score for individual samples by performing single-sample gene set enrichment analysis (ssGSEA) (GSVA package v.1.48.3), with the six IFN-response modules of the BloodGen3Module gene set (1.8.0), aggregate A28 as input.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSVA]

### Targeting myeloid chemotaxis to reverse prostate cancer therapy resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06696-z | PMCID: PMC10686834 | PMID: 37844613
- Version used: **1.4**
- Evidence: Gene set variation analysis (GSVA, R package GSVA v.1.4) was used for molecular signature analysis.
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, TopHat v2.0.7] -> quantification [Cufflinks v2.2.1] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSVA v1.4, R]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **1.42.0**
- Evidence: Pathway enrichment analysis was carried out on logCPM data including 17815 protein-coding genes using Gene Set Variation Analysis (GSVA v1.42.0) 18 .
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Evidence: ...ta were first converted into pathway profiles by single-sample gene set enrichment analysis (ssGSEA 104 ) implemented in Gene Set Variation Analysis (GSVA 105 (v.1.42.0), parameters ‘min.sz=5, max.sz=300’) using MSigDB 106 – 108 (v.7.4).
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Gene set variation analysis 62 (using the GSVA package in R) was performed to identify the activation condition that most closely resembled CD14 + monocytes/macrophages from active IBD using disease-associated lists of differentially expressed genes 63 .
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### PGE&lt;sub&gt;2&lt;/sub&gt; inhibits TIL expansion by disrupting IL-2 signalling and mitochondrial function. (Nature 2024)

- DOI: 10.1038/s41586-024-07352-w | PMCID: PMC11078736 | PMID: 38658764
- Version used: **1.44.5**
- Evidence: Pathways scores were generated using ssGSEA from the R-package GSVA (version 1.44.5). scRNA-seq and scTCR-seq in TIL-ACT patients Thirteen patients were enrolled in a phase I trial designed to test the feasibility of ACT with TILs (ClinicalTrials.gov ID NCT03475134 ).
- Full pipeline: alignment/mapping [IMOD, STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.54.0] -> visualisation [UMAP] -> stage not stated [GSEA, GSVA v1.44.5, HTSeq v0.9.1, ImageJ, R]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Version used: **1.46.0**
- Evidence: Cell-type enrichment was performed through the single-sample extension of gene set enrichment analysis (ssGSEA) in the GSVA v.1.46.0 R package using signature genes from previous studies 8 , 55 using R v.4.1.0.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **1.46**
- Evidence: Differential expression was performed with DESeq2 (v1.38.3) and enrichment analysis was performed with enrichR (v3.2) using genes with adjusted P < 0.05. ssGSEA scores for curated signatures (Supplementary Table 2 ) were calculated using the GSVA (v1.46) package and gene sets consisting of individual genes were compared using log 2 (reads per million + 1) values instead.
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### Neuronal activity-dependent mechanisms of small cell lung cancer pathogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09492-z | PMCID: PMC12571889 | PMID: 40931074
- Evidence: Finally, the GSVA 67 (v.1.50.0) package was used to calculate the ssGSEA scores for synaptome, astrocytes, and cell proliferation signatures.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scDblFinder] -> stage not stated [Fiji v2.1.0, GSEA, GSVA, ImageJ v2.1.0, Seurat, fgsea]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Evidence: The GSVA method 33 , using the MSigDb Hallmark collection of RNA-seq data, was then used to calculate GSVA scores for E2F targets and G2/M checkpoint pathway using the GSVA Bioconductor package (v.1.50.5).
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Based on single-sample GSEA (ssGSEA) 48 conducted with the GSVA 49 R package (v.1.44.5), we observed that patients with low levels of YchrS exhibited characteristics similar to those of people with LOY DNA , whereas those with high YchrS levels resembled people with an intact Y chromosome (WTY DNA ).
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: This was performed by calculating the single-sample GSEA score using GSVA in R and selecting the samples above the third, second or first quantile for the respective category.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: The enrichment of proliferation, differentiation and progenitor-like activity of medulloblastoma-specific markers per cell was performed using the single sample function from the GSVA R package 44 using two independent reference datasets 8 , 9 .
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **1.44.1**
- Evidence: Gene set variation analysis was used to calculate a per-sample activity score for each of the BTMs (excluding unannotated modules labelled ‘TBA’) using R Bioconductor package GSVA v.1.44.1 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: We used GSVA 66 by categorizing the rows of the matrix as PBMC specific or tumour microenvironment specific.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: To estimate a TLS chemokine signature 7 in myeloid cells, a signature score was computed for the 12 chemokines 7 using the GSVA method 80 in R (v.4.0.3).
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: The normalized count matrix and activation score were used as input for GSVA 85 (v1.40.1) using the gsva function with min.sz=10, max.sz=6000, kcdf = ‘Poisson’.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Evidence: Then, an enrichment score was calculated using GSVA with the following parameters: minSize = 5, maxSize = 500, kcdf = “Gaussian”.
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **1.46.0**
- Evidence: Subsequently, ssGSEA analysis was conducted utilizing the R package GSVA (v.1.46.0) 73 .
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: To compute a gene signature, the overall expressions in patients were computed using the function ‘gsva’ of the package ‘GSVA’ 74 (v.1.42) with the parameter ‘method’ set as ‘ssgsea’, and then the z -score was computed.
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **1.46.0**
- Evidence: For gene set enrichment analysis (GSEA), two methods were applied: preranked GSEA (fgsea 67 v.1.24.0) and single-sample GSEA (ssGSEA 68 implemented in GSVA v.1.46.0).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: GSVA was performed on rlog-normalized gene expression data using the GSVA R package (v.1.52.3) 76 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: The human ATF6α-activation signature was used to quantify relative gene set enrichment scores across HCC and non-tumour samples in each dataset using the GSVA (gene set variation analysis) Bioconductor package 79 .
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: To estimate the activity of pathways of interest at a single sample level we performed GSVA.
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **1.50.5**
- Evidence: Single-sample gene set enrichment analysis was carried out using GSVA (v1.50.5).
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: Human tumour data: GSVA analysis For Extended Data Fig.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Dendritic cell paucity in mismatch repair-proficient colorectal cancer liver metastases limits immune checkpoint blockade efficacy. (PNAS 2021)

- DOI: 10.1073/pnas.2105323118 | PMCID: PMC8609309 | PMID: 34725151
- Evidence: GSVA ( 79 ) was used to obtain GSVA enrichment scores for each immune cell type.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK] -> quantification [Bioconductor, DESeq2, R] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, GSVA, SnpEff]

### The genetic source tracking of human urinary exosomes. (PNAS 2021)

- DOI: 10.1073/pnas.2108876118 | PMCID: PMC8639375 | PMID: 34663731
- Evidence: The R package GSVA ( 14 ) with default settings was applied for the ssGSEA.
- Full pipeline: stage not stated [GSVA, R]

### Identification of EMT signaling cross-talk and gene regulatory networks by single-cell RNA sequencing. (PNAS 2021)

- DOI: 10.1073/pnas.2102050118 | PMCID: PMC8126782 | PMID: 33941680
- Evidence: Single-sample gene-set enrichment analysis was performed using the GSVA package (v1.28.0) using hallmarks from MSigDB (v6.2).
- Full pipeline: quality control [R, Seurat v3.1.0] -> normalisation [R, Seurat v3.1.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, Seurat v3.1.0, UMAP] -> stage not stated [GSVA, fgsea]

### Systems level profiling of chemotherapy-induced stress resolution in cancer cells reveals druggable trade-offs. (PNAS 2021)

- DOI: 10.1073/pnas.2018229118 | PMCID: PMC8092411 | PMID: 33883278
- Evidence: ( D ) Enrichment of glycolysis pathways as determined via GSVA of RNA-sequencing data.
- Full pipeline: stage not stated [GSVA]

### The glioblastoma multiforme tumor site promotes the commitment of tumor-infiltrating lymphocytes to the T&lt;sub&gt;H&lt;/sub&gt;17 lineage in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2206208119 | PMCID: PMC9407554 | PMID: 35969754
- Evidence: GSVA ( https://doi.org/10.1186/1471-2105-14-7 ) was run on the variance-stabilized expression data for the gene sets “HALLMARK_IL6_JAK_STAT3_SIGNALING” and “GSE15659_CD45RA_NEG_CD4_TCELL_VS_RESTING_TREG_DN” from the MSig database collection as well as with the marker genes determined by the pairwise comparisons of CD4 + T cells.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2 v1.32.0, GSEA, GSVA, R v4.1.0, ggplot2 v3.3.5, tidyverse v1.0.7]

### Transforming growth factor-β signaling governs the differentiation program of extravillous trophoblasts in the developing human placenta. (PNAS 2022)

- DOI: 10.1073/pnas.2120667119 | PMCID: PMC9282384 | PMID: 35867736
- Evidence: Furthermore, gene set variation analysis (GSVA) using a secretome-specific gene signature indicated higher GSVA scores in iEVTs compared with pEVTs ( Fig.
- Full pipeline: stage not stated [GSVA]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: Single-sample GSEA (ssGSEA) was used to quantify the activity of gene sets compared to genes outside the gene set within a sample using the GSVA R package.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### Compression drives diverse transcriptomic and phenotypic adaptations in melanoma. (PNAS 2023)

- DOI: 10.1073/pnas.2220062120 | PMCID: PMC10523457 | PMID: 37722033
- Evidence: ( F ) GSVA hallmarks analysis of the uncompressed and compressed B16F0 cells is shown.
- Full pipeline: alignment/mapping [SAMtools v1.11] -> dimensionality reduction/clustering [clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.18.1, GSEA, R] -> stage not stated [Cytoscape, GSVA, HTSeq v0.13.5, ImageJ]

### Transcription factor expression repertoire basis for epigenetic and transcriptional subtypes of colorectal cancers. (PNAS 2023)

- DOI: 10.1073/pnas.2301536120 | PMCID: PMC10401032 | PMID: 37487069
- Evidence: In order to identify the low and high expression groups associated with the CIMP-H specific hypermethylated cCRE-associated TF (N = 145), the gene set variation analysis (GSVA) method was used ( 80 ).
- Full pipeline: stage not stated [GSVA]

### PHGDH preserves one-carbon cycle to confer metabolic plasticity in chemoresistant gastric cancer during nutrient stress. (PNAS 2023)

- DOI: 10.1073/pnas.2217826120 | PMCID: PMC10214193 | PMID: 37192160
- Evidence: ( H ) GSVA was performed to calculate enrichment score with GO pathway “HALLMARK_ EPITHELIAL_MESENCHYMAL_TRANSITION” from MSigDB v7.4.
- Full pipeline: dimensionality reduction/clustering [CellChat, R, SCENIC, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> structure determination [SCENIC] -> visualisation [UMAP] -> stage not stated [GSVA]

### Thioredoxin-interacting protein is essential for memory T cell formation via the regulation of the redox metabolism. (PNAS 2023)

- DOI: 10.1073/pnas.2218345120 | PMCID: PMC9926250 | PMID: 36595680
- Evidence: In both pathways, the GSVA score was decreased in Txnip -deficient transferred Th2 cells compared with wild-type transferred Th2 cells ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSVA]

### c-JUN-mediated transcriptional responses in lymphatic endothelial cells are required for lung fluid clearance at birth. (PNAS 2023)

- DOI: 10.1073/pnas.2215449120 | PMCID: PMC9926280 | PMID: 36595691
- Evidence: ( H ) Ridge plots for AP-1 pathway signatures based on GSVA scores in the LEC clusters.
- Full pipeline: dimensionality reduction/clustering [GSVA, Monocle, Slingshot, UMAP]

### Staged suppression of microglial autophagy facilitates regeneration in CNS demyelination by enhancing the production of linoleic acid. (PNAS 2023)

- DOI: 10.1073/pnas.2209990120 | PMCID: PMC9910603 | PMID: 36577069
- Evidence: ( D ) Heatmap showing the differences in biological processes by GSVA enrichment scores across the different groups.
- Full pipeline: stage not stated [GSVA]

### Corticosteroids reduce pathological angiogenesis yet compromise reparative vascular remodeling in a model of retinopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2411640121 | PMCID: PMC11670060 | PMID: 39693344
- Evidence: Single-cell gene expression profiles from each separate cell type identified by scRNA-Seq were further analyzed using GSVA.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [UMAP, edgeR] -> structure determination [Seurat] -> visualisation [UMAP, clusterProfiler] -> stage not stated [DESeq2, GSEA, GSVA, ImageJ]

### Magnetic soft microrobots for erectile dysfunction therapy. (PNAS 2024)

- DOI: 10.1073/pnas.2407809121 | PMCID: PMC11626158 | PMID: 39556757
- Evidence: ( H ) Heatmap presenting the top pathways associated with genes whose expression was activated or inhibited in Schwann cells from the ED model and MSC-Rob groups based on the GSVA of DEGs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSVA]

### Augmenting antitumor efficacy of Th17-derived Th1 cells through IFN-γ-induced type I interferon response network via IRF7. (PNAS 2024)

- DOI: 10.1073/pnas.2412120121 | PMCID: PMC11588128 | PMID: 39541355
- Evidence: Pathway analysis using Gene Set Variation Analysis (GSVA) showed an upregulation of memory and effector-related pathways in Th 17 1 cells, contrasting with down-regulated dysfunctional and Treg-associated pathways ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA, GSVA]

### Spatial molecular profiling of mixed invasive ductal and lobular breast cancers reveals heterogeneity in intrinsic molecular subtypes, oncogenic signatures, and mutations. (PNAS 2024)

- DOI: 10.1073/pnas.2322068121 | PMCID: PMC11295029 | PMID: 39042692
- Evidence: The heatmap shows GSVA scores of each differentially enriched pathway in ductal vs. lobular tumor regions.
- Full pipeline: differential/statistical testing [GSVA] -> stage not stated [Cellpose, scikit-image]

### Cancer-stromal cell interactions in breast cancer brain metastases induce glycocalyx-mediated resistance to HER2-targeting therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322688121 | PMCID: PMC11098130 | PMID: 38709925
- Evidence: The glycosylation gene signatures were taken from GSEA and ( 16 , 49 ) to calculate enrichment scores using GSVA package ( 50 ).
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v1.18.1] -> normalisation [edgeR] -> differential/statistical testing [DESeq2 v1.18.1, MACS2 v2.1.1.20160309] -> stage not stated [GSEA, GSVA]

### Single-cell profiling of African swine fever virus disease in the pig spleen reveals viral and host dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2312150121 | PMCID: PMC10927503 | PMID: 38412127
- Version used: **1.44.3**
- Evidence: R package GSVA (v1.44.3) were performed to assess the relative pathway activities in the macrophages and monocytes.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, ggplot2] -> stage not stated [GSVA v1.44.3, Seurat]

### Single-cell analysis of refractory anti-SRP necrotizing myopathy treated with anti-BCMA CAR-T cell therapy. (PNAS 2024)

- DOI: 10.1073/pnas.2315990121 | PMCID: PMC10861907 | PMID: 38289960
- Evidence: Further exploration of differential gene expression identification, gene module scoring, and GSVA analysis indicated that CD8 + Te-3 cells, characterized by relatively lower expression of GZMB (granzyme B) and higher expression of CCL5 (C-C motif chemokine ligand 5), and KLRG1 (killer cell lectin–like receptor G1), presented a signature of enhanced cell chemotaxis and NK receptor ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSVA] -> stage not stated [GSEA]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Evidence: Per-sample gene set enrichment was calculated by gene set variation analysis (GSVA) v.1.48.3.
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### Dual-targeted ping-pong CAR T cells: Leveraging peripheral expansion to improve solid tumor immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2518996122 | PMCID: PMC12745717 | PMID: 41397127
- Evidence: GSVA results were graphed using the ggplot2 Bioconductor R package.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Bioconductor, GSVA, R, ggplot2]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Evidence: Gene Set Variation Analysis (GSVA) was used to calculate published AR and t-NEPC signatures ( 5 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### Breast cancer cell coculture induces normal lung fibroblast transition to CAFs, promoting tumor cell dormancy and therapy resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2423894122 | PMCID: PMC12663926 | PMID: 41269792
- Evidence: ( F ) Gene set variation analysis (GSVA) enrichment of BC scores for autophagy, dormancy, and therapy resistance gene signatures in MB231 cell subclusters.
- Full pipeline: dimensionality reduction/clustering [GSVA, UMAP] -> visualisation [UMAP] -> stage not stated [CellChat]

### Circadian regulator REV-ERBα is a master regulator of tumor lineage plasticity and an effective therapeutic target. (PNAS 2025)

- DOI: 10.1073/pnas.2513468122 | PMCID: PMC12646269 | PMID: 41231955
- Evidence: ( J ) Correlations between the expression of NR1D1 and LP signature score generated by GSVA.
- Full pipeline: stage not stated [GSVA]

### PD-1 expression identifies proliferating malignant CLL B cells and is a potential biomarker of response to BTK inhibitor therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426935122 | PMCID: PMC12435283 | PMID: 40906805
- Evidence: GSVA (Gene Set Variation Analysis) R package ( 48 ) was then used to compute a sample-level gene set enrichment z-score for significant EnrichmentMap modules to be significantly enriched using GSEA, on the basis of the expression level of the core genes.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HTSeq, Trimmomatic] -> quantification [DESeq2 v1.40.2, HTSeq, R] -> normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [DESeq2 v1.40.2, R] -> stage not stated [GSEA, GSVA, MACS2]

### Cellular cartography reveals mouse prostate organization and determinants of castration resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2427116122 | PMCID: PMC12415206 | PMID: 40854129
- Evidence: Gene Set Variation Analysis (GSVA) of cellular transcriptomes ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB, GSVA, SCENIC]

### Blood-labyrinth barrier damage mediated by granzymes from cytotoxic lymphocytes results in hearing loss in systemic lupus erythematosus. (PNAS 2025)

- DOI: 10.1073/pnas.2423240122 | PMCID: PMC12377648 | PMID: 40794837
- Evidence: Furthermore, gene set variation analysis (GSVA) also revealed that pathways of cell adhesion molecules, natural killer cell-mediated cytotoxicity, and apoptosis were significantly upregulated in the SLE mice ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cytoscape, GSVA, STRING db]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Evidence: Single-sample gene set enrichment score of CDK12-loss signature was calculated by GSVA ( 36 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: Additionally, GSVA scores for the FAK, ECM, and CAM pathways were all significantly positively correlated with LMIC score ( Fig.
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Mutant &lt;i&gt;IDH1&lt;/i&gt; cooperates with &lt;i&gt;NPM1c&lt;/i&gt; or &lt;i&gt;FLT3&lt;/i&gt;&lt;sup&gt;ITD&lt;/sup&gt; to drive distinct myeloid diseases and molecular outcomes. (PNAS 2025)

- DOI: 10.1073/pnas.2415779122 | PMCID: PMC12107087 | PMID: 40377995
- Evidence: Shown are gene set variation analysis (GSVA) scores of human AML samples from a published Oregon Health & Science University (OHSU) cohort (Nature, 2018) as determined using the murine differential gene expression signature of Idh1 R132 ; Npm1c vs.
- Full pipeline: differential/statistical testing [DESeq2, GSVA] -> stage not stated [GSEA]

### SNX10 deficiency impairs sensitivity to anti-HER2 antibody-drug conjugates via altering HER2 trafficking in HER2-positive breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2417586122 | PMCID: PMC12037019 | PMID: 40228127
- Evidence: ( D ) Heatmap visualizing GSVA scores of PDO transcriptome data.
- Full pipeline: differential/statistical testing [GSEA] -> visualisation [GSVA]

### Dual mRNA nanoparticles strategy for enhanced pancreatic cancer treatment and β-elemene combination therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2418306122 | PMCID: PMC11929461 | PMID: 40067898
- Evidence: ( A ) GSVA among four groups.
- Full pipeline: stage not stated [GSEA, GSVA]

### Metabolomic insights into pathogenesis and therapeutic potential in adult acute lymphoblastic leukemia. (PNAS 2025)

- DOI: 10.1073/pnas.2423169122 | PMCID: PMC11848409 | PMID: 39946534
- Evidence: Gene set variation analysis (GSVA) ( 32 ) was employed to calculate enrichment scores for metabolism-related pathways in both BCP-ALL and T-ALL samples.
- Full pipeline: stage not stated [GSEA, GSVA]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Evidence: Gene set variation analysis (GSVA) was performed on vst-normalized data with the gsva R package, using as input HALLMARK gene sets collection retrieved from msigdb R package.
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: Enrichment levels of gene and gene signature in each tumor sample were quantified by “GSVA” R package after converting all gene names to human homology using “gprofiler2” R package ( 63 ).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: As we noticed substantial heterogeneity within the “Other” group, we conducted k-means clustering based on single sample gene set enrichment scores (GSVA( 84 )) of hallmark pathways ( 85 ), and divided it into two groups.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

