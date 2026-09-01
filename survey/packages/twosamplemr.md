# TwoSampleMR

- **Category:** statgen
- **Papers in survey:** 14
- **Journals:** Nature (9), PNAS (5)
- **Years:** 2021 (2), 2022 (2), 2023 (2), 2024 (2), 2025 (3), 2026 (3)
- **Versions named:** 0.5.6 (2), 0.6.2 (1), 0.6.15 (1), 0.5.10 (1), 0.5.1 (1)
- **Pipeline stages it appears in:** differential/statistical testing (6), dimensionality reduction/clustering (1)

## Papers

### Mapping the human genetic architecture of COVID-19. (Nature 2021)

- DOI: 10.1038/s41586-021-03767-x | PMCID: PMC8674144 | PMID: 34237774
- Evidence: Next, the exposure and outcome datasets were harmonized using the R package TwoSampleMR 55 .
- Full pipeline: differential/statistical testing [LDSC v1.0.1] -> stage not stated [PLINK, R, SAIGE, TwoSampleMR]

### Stroke genetics informs drug discovery and risk prediction across ancestries. (Nature 2022)

- DOI: 10.1038/s41586-022-05165-3 | PMCID: PMC9524349 | PMID: 36180795
- Evidence: We used the TwoSampleMR R package 91 for MR analysis.
- Full pipeline: quality control [R] -> differential/statistical testing [LDSC] -> stage not stated [GCTA, MAGMA, SAIGE, Seurat, TwoSampleMR]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Evidence: We applied the inverse variance weighted method using the TwoSampleMR package (version 0.5.5) in R statistical software (version 4.0.2).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### GDF15 promotes weight loss by enhancing energy expenditure in muscle. (Nature 2023)

- DOI: 10.1038/s41586-023-06249-4 | PMCID: PMC10322716 | PMID: 37380764
- Evidence: 2SMR was performed using the TwoSampleMR R package (v0.5.6) 82 .
- Full pipeline: quality control [MultiQC, Trim Galore] -> read trimming [Trim Galore] -> quantification [DESeq2] -> stage not stated [R, TwoSampleMR]

### Genome-wide characterization of circulating metabolic biomarkers. (Nature 2024)

- DOI: 10.1038/s41586-024-07148-y | PMCID: PMC10990933 | PMID: 38448586
- Version used: **0.5.1**
- Evidence: The Mendelian randomization analyses were performed using the MendelianRandomization package v.
- Full pipeline: differential/statistical testing [R] -> stage not stated [GCTA, PLINK v2.0, SAIGE, TwoSampleMR v0.5.1]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Version used: **0.5.6**
- Evidence: MR analyses were performed using the TwoSampleMR v.0.5.6 R package 102 , 103 (valid in both one-sample and two-sample settings 104 ), with glycaemic-related traits as the exposures and CH as the outcome, and the test statistics reported were derived from inverse variance weighting.
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Version used: **0.5.10**
- Evidence: European independent genome-wide significant ( P < 5 × 10 −8 ) signals within 10 Mb were extracted from summary statistics for the 13 metabolic traits using the extract_instruments function with default parameters from the R package TwoSampleMR v.0.5.10 (ref.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### Dynamics of genetic and somatic trade-offs in ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10407-9 | PMCID: PMC13253337 | PMID: 42020758
- Version used: **0.6.2**
- Evidence: When only a single instrumental variable was available for both the exposure and the outcome, or when principal component analysis yielded a single component, causal effects were estimated using the Wald ratio method implemented in TwoSampleMR (v0.6.2) 63 .
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.3.4.1] -> variant calling [BCFtools, R v4.0] -> dimensionality reduction/clustering [PLINK, TwoSampleMR v0.6.2, clusterProfiler] -> stage not stated [SAMtools v1.6]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Version used: **0.6.15**
- Evidence: Analyses were performed in R (v4.5.0) using the packages ieugwasr (v1.0.3) and TwoSampleMR (v0.6.15) 91 , 92 .
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### Mendelian randomization identifies blood metabolites previously linked to midlife cognition as causal candidates in Alzheimer's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2009808118 | PMCID: PMC8072203 | PMID: 33879569
- Evidence: All data extraction, preprocessing, and analyses were performed within R.3.6.1. using the MR-Base package (v.0.4.25) ( 43 ).
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [TwoSampleMR]

### High-throughput screening of glucocorticoid-induced enhancer activity reveals mechanisms of stress-related psychiatric disorders. (PNAS 2023)

- DOI: 10.1073/pnas.2305773120 | PMCID: PMC10710077 | PMID: 38011552
- Evidence: To test for a causal effect of the differential DRE activity on psychiatric traits, a two-sample MR approach using the R package “TwoSampleMR” was employed.
- Full pipeline: quality control [FastQC] -> differential/statistical testing [TwoSampleMR] -> stage not stated [R]

### Evidence supports a causal association between allele-specific vitamin D receptor binding and multiple sclerosis among Europeans. (PNAS 2024)

- DOI: 10.1073/pnas.2302259121 | PMCID: PMC10895341 | PMID: 38346204
- Evidence: GWAS summary statistics were extracted from MR-Base R platform ( 39 ).
- Full pipeline: differential/statistical testing [TwoSampleMR] -> stage not stated [R]

### Multiomics integration prioritizes potential drug targets for multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2425537122 | PMCID: PMC12232717 | PMID: 40577117
- Evidence: All analyses were conducted with packages “TwoSampleMR”, “MRInstruments”, “MendelianRandomization”, and “mr.raps” in R v3.6.3.
- Full pipeline: differential/statistical testing [COLOC v5.2.3, R] -> stage not stated [TwoSampleMR, edgeR]

### Host genetic regulation of rumen 6-hydroxymelatonin reduces methane emissions in dairy cattle. (PNAS 2026)

- DOI: 10.1073/pnas.2604454123 | PMCID: PMC13291679 | PMID: 42258707
- Version used: **0.5.6**
- Evidence: After determining the instrumental variables, the MR analysis was conducted using TwoSampleMR (version 0.5.6) in the R project, employing five different methods: inverse variance weighting (IVW), MR-Egger regression, weighted median, simple mode, and weighted mode.
- Full pipeline: quality control [fastp] -> alignment/mapping [fastp] -> dimensionality reduction/clustering [R] -> differential/statistical testing [GEMMA, TwoSampleMR v0.5.6] -> stage not stated [GCTA, PLINK, VEP, lavaan]

