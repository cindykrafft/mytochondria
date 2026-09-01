# survival (R)

- **Category:** general
- **Papers in survey:** 41
- **Journals:** Nature (20), PNAS (17), Cell (3), NEJM (1)
- **Years:** 2022 (3), 2023 (10), 2024 (5), 2025 (18), 2026 (5)
- **Versions named:** 0.4.9 (9), 3.6.4 (1), 3.2.13 (1), 0.5.0 (1)
- **Pipeline stages it appears in:** differential/statistical testing (12), visualisation (7), quantification (1), normalisation (1), dimensionality reduction/clustering (1)

## Papers

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: SNF clusters survival analysis To evaluate the clinical relevance of the identified clusters in COMBAT, we performed a survival analysis and plotted the Kaplan-Meier curve using R packages survival ( Therneau and Grambsch, 2000 ) and survminer.
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Generating parallel representations of position and identity in the olfactory system. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.038 | PMCID: PMC10403364 | PMID: 37236194
- Evidence: Data processing was done in MATLAB, statistical analyses were done in R with the survminer package ( https://rpkgs.datanovia.com/survminer/index.html ).
- Full pipeline: differential/statistical testing [survival (R)] -> stage not stated [DeepLabCut, ImageJ, R]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Evidence: 106 The statistical test applied was the log-rank test using the survminer package.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### Fourth Dose of BNT162b2 mRNA Covid-19 Vaccine in a Nationwide Setting. (NEJM 2022)

- DOI: 10.1056/nejmoa2201688 | PMCID: PMC9020581 | PMID: 35417631
- Evidence: Analyses were performed with the use of R software, version 4.1.0, and the additional freely available R software packages “tidyverse,” version 1.3.1, and “survminer,” version 0.4.9.
- Full pipeline: stage not stated [survival (R), tidyverse]

### Signatures of copy number alterations in human cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-04738-6 | PMCID: PMC9242861 | PMID: 35705804
- Evidence: Survival analysis was performed with the R packages survival and survminer.
- Full pipeline: normalisation [RSEM] -> stage not stated [Beagle v5.1, ComplexHeatmap, R, ggplot2, survival (R), tidyverse]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Version used: **0.4.9**
- Evidence: The survival probability of progression-free survival/overall survival and Kaplan–Meier curves were then calculated for both groups using the survival (v.3.2.7) and survminer (v.0.4.9) R packages.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Evidence: The P values (shown in the figure) were calculated through the log-rank test using the survminer R package, and were adjusted by the Bonferroni correction.
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **0.4.9**
- Evidence: R packages survival(v3.2-13) 57 , survivalAnalysis(v0.3.0) 58 and survminer(v0.4.9) 59 were used to generate hazard ratios, forest plots, 1- and 2-year survival data and cox regression models in the manuscript.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Antibodies against endogenous retroviruses promote lung cancer immunotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05771-9 | PMCID: PMC10115647 | PMID: 37046094
- Version used: **3.2.13**
- Evidence: Patient-level data were split into high and low groups based on the histology-specific cohort median, and the probability of DFS was compared by Kaplan–Meier estimates using the survival R package (v.3.2.13).
- Full pipeline: quantification [Salmon v0.12.0] -> differential/statistical testing [lme4 v1.1.27.1] -> stage not stated [QuPath v0.3, R, RepeatMasker, data.table v1.14.2, survival (R) v3.2.13, tidyverse v1.0.7]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: Survival analysis and visualization of this data were performed using the survminer R package.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Version used: **0.4.9**
- Evidence: The survival best cut-point of mtDNA copy number was identified with surv_cutpoint (maxstat test: Maximally Selected Rank and Statistics) implemented in survminer (v.0.4.9).
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Survival analysis was conducted for HNSCC and other TCGA tumour types in R utilizing the survival and survminer library.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **0.4.9**
- Evidence: Analyses were performed using R (v4.3.0) 61 using R-studio build 561 with packages: arsenal (v3.6.3), survival (v3.6-4) and survminer (v.0.4.9), except for statistical analyses related to RNA-seq, whole-exome sequencing, immunohistochemistry and IMC data, which were conducted using R (v4.2.3) using R-studio build 513 with the packages: tidyverse (v2.0), ggplot2 (v3.4.2), ggpubr (v0.6.0) and pheatm...
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Evidence: To determine the optimal cut-off value for T ex -PSR signature expression in relation to survival outcomes, we used the surv_cutpoint function from the R package survminer.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Evidence: The normalized ComBat batch-corrected expression values were used for categorizing samples to SPP1 high and SPP1 low based on surv_cutpoint function in survminer R package.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### Fluctuating DNA methylation tracks cancer evolution at clinical scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09374-4 | PMCID: PMC12443617 | PMID: 40931062
- Version used: **0.4.9**
- Evidence: Survival (v3.5-7), survminer (v0.4.9) and ggsurvfit (v0.3.1) packages were used under R (v4.3.1).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Bioconductor, R, SAMtools, Stan, dynesty, ggplot2 v3.5.2, survival (R) v0.4.9]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Survival analysis Time-to-event outcomes were presented by using Kaplan–Meier curves and compared by using log-rank test or univariate Cox proportional hazards model (survival R package; v.3.5.8) as noted in each figure.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Evidence: For survival analyses, Kaplan–Meier plotting was performed using the ggsurvplot function of the survminer R (4.3.0) package.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: ...he biopsy subset of cases in the SteatoSITE data commons were used in survival analysis using R (v.4.3.0) in RStudio (v.2023.12.0 build 369) and the ‘survminer’ package (v.0.4.9).
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Version used: **0.4.9**
- Evidence: Analyses and visualizations were generated using the R packages survival (v.3.5.5) and survminer (v.0.4.9).
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **0.4.9**
- Evidence: R packages survival (v.3.6–4) and survminer (v.0.4.9) were used for the survival analysis.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: The hazard ratios and P values of the Wald test were extracted from the modelling result and visualized using the function ‘ggforest’ in the package ‘survminer’ (v.0.4.9).
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Version used: **3.6.4**
- Evidence: To investigate SE prognostic associations, a Cox regression analysis was conducted to examine the association between SE abundance and patient overall survival, adjusting for age and sex, using the survival R package (v.3.6.4).
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Version used: **0.4.9**
- Evidence: OS and PFS were correlated with signature expression by the Kaplan–Meier estimator and plotted with the survival (v.3.3-1) and survminer (v.0.4.9) R packages with default parameters ( https://cran.r-project.org/web/packages/survminer/index.html ).
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Peripheral blood TCR clonotype diversity as an age-associated marker of breast cancer progression. (PNAS 2023)

- DOI: 10.1073/pnas.2316763120 | PMCID: PMC10710020 | PMID: 38011567
- Evidence: The Cox regression analysis was performed with the survival package (v3.5-5) and the survminer package (v0.4.9).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [survival (R)] -> stage not stated [DESeq2, GSEA, QuPath, R v4.3]

### Complete miRNA-15/16 loss in mice promotes hematopoietic progenitor expansion and a myeloid-biased hyperproliferative state. (PNAS 2023)

- DOI: 10.1073/pnas.2308658120 | PMCID: PMC10614620 | PMID: 37844234
- Evidence: Cox regression of the risk groups to overall survival was done using survminer, with people being right censored and any person without any survival time information removed.
- Full pipeline: dimensionality reduction/clustering [Monocle, Seurat v4.0, UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0, UMAP] -> stage not stated [GSEA, ImageJ, SCENIC]

### Resistance to host antimicrobial peptides mediates resilience of gut commensals during infection and aging in <i>Drosophila</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2305649120 | PMCID: PMC10483595 | PMID: 37639605
- Evidence: Survival analysis and individual median survival were performed using Kaplan–Meier method and Log Rank test survival with the R package survminer.
- Full pipeline: differential/statistical testing [R v4.2] -> visualisation [ggplot2, tidyverse] -> stage not stated [survival (R)]

### A simple mechanism for collective decision-making in the absence of payoff information. (PNAS 2023)

- DOI: 10.1073/pnas.2216217120 | PMCID: PMC10629567 | PMID: 37428910
- Evidence: ... ( 78 ) (version 3.3.6), tidyr ( 79 ) (version 1.2.0), dplyr ( 80 ) (version 1.0.10), readr ( 81 ) (version 2.1.2), ggeffects ( 82 ) (version 1.1.3), survminer ( 83 ) (version 0.4.9), data.table ( 84 ) (version 1.14.2), viridis ( 85 ) (version 0.6.2), scales ( 86 ) (version 1.2.1), and survival ( 87 ) (version 3.4-0).
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.2.1, data.table, survival (R), tidyverse]

### Losartan controls immune checkpoint blocker-induced edema and improves survival in glioblastoma mouse models. (PNAS 2023)

- DOI: 10.1073/pnas.2219199120 | PMCID: PMC9963691 | PMID: 36724255
- Evidence: Relative pop The Cox proportional hazard regression models were generated using the “survminer” and “survival” packages in the R platform.
- Full pipeline: quantification [RSEM v1.2.19] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [survival (R)] -> visualisation [UMAP] -> stage not stated [ImageJ, R, Seurat v4.0.0, seaborn v0.9.0]

### Aging and comprehensive molecular profiling in acute myeloid leukemia. (PNAS 2024)

- DOI: 10.1073/pnas.2319366121 | PMCID: PMC10927507 | PMID: 38422020
- Version used: **0.4.9**
- Evidence: The R package survival (v3.5-7) and survminer (v0.4.9) was used to construct the Kaplan–Meier (KM) model and draw the survival curve.
- Full pipeline: normalisation [DESeq2] -> stage not stated [R, survival (R) v0.4.9]

### p53 regulates the expression of histone modifiers to restrict stemness and maintain differentiated luminal identity in breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2522646122 | PMCID: PMC12595495 | PMID: 41160600
- Evidence: Kaplan–Meier survival plots were generated by the R packages “survival” and “survminer,” based on the data available in the METABRIC dataset ( 114 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ggplot2, survival (R), tidyverse]

### Heritable symbiont producing nonribosomal peptide confers extreme heat sensitivity and antifungal protection on its host. (PNAS 2025)

- DOI: 10.1073/pnas.2509873122 | PMCID: PMC12232616 | PMID: 40569380
- Evidence: The survfit and ggsurvplot functions in the R package survminer were used to generate Kaplan–Meier survival curves.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [MAFFT v7.520, OrthoFinder v2.5.5] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [R, survival (R)]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: The survminer package determined the optimal cut-off values.
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Total whole-arm chromosome losses predict malignancy in human cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505385122 | PMCID: PMC12067283 | PMID: 40314975
- Evidence: Kaplan–Meier survival curves were generated using the survminer R package, and log-rank tests were performed to evaluate the significance of the differences in survival curve distributions.
- Full pipeline: alignment/mapping [STAR v2.7.11] -> registration [STAR v2.7.11] -> stage not stated [R, survival (R)]

### The expanded immunoregulatory protease network in mosquitoes is governed by gene coexpression. (PNAS 2025)

- DOI: 10.1073/pnas.2425863122 | PMCID: PMC12067252 | PMID: 40305045
- Evidence: Survival curves were plotted, and log-rank pairwise comparisons were performed in R (version 4.2.0) using the packages survival ( 45 ), survminer ( 46 ), and patchwork ( 47 ).
- Full pipeline: visualisation [R v4.2.0, survival (R)]

### Cryptic genetic variation in brain gene expression precedes the evolution of cannibalism in spadefoot toad tadpoles. (PNAS 2025)

- DOI: 10.1073/pnas.2418431122 | PMCID: PMC12088425 | PMID: 40294283
- Evidence: First, we applied the Cox proportional hazards model using R packages survival ( 79 ) and survminer ( 80 ).
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [BUSCO, DESeq2, survival (R)]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Evidence: For survival analysis, samples were grouped into high/low expression based on median gene expression using the “survminer” package.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### Validating new limits for human thermoregulation. (PNAS 2025)

- DOI: 10.1073/pnas.2421281122 | PMCID: PMC12002229 | PMID: 40163728
- Evidence: 2 C ) were produced using the R packages “ survival” ( 62 ) and “ survminer ” ( 63 ).
- Full pipeline: differential/statistical testing [lme4] -> simulation/modelling [R] -> visualisation [ggplot2] -> stage not stated [survival (R)]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Evidence: Survival analyses were performed using the survival and survminer packages in R.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: Survival analysis for both datasets was performed using Cox proportional hazards regression models using “survminer” package.
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### CHAMP1 complex promotes heterochromatin assembly and reduces replication stress. (PNAS 2026)

- DOI: 10.1073/pnas.2525144122 | PMCID: PMC12773717 | PMID: 41481470
- Version used: **0.5.0**
- Evidence: The median survivals were derived, and the Kaplan–Meier curves were visualized, using the survminer (version 0.5.0) R package.
- Full pipeline: quantification [ImageJ, limma] -> differential/statistical testing [R, ggplot2, limma] -> visualisation [ImageJ, survival (R) v0.5.0]

