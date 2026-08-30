# MAGMA

- **Category:** statgen
- **Papers in survey:** 33
- **Journals:** Nature (19), PNAS (12), Cell (2)
- **Years:** 2021 (2), 2022 (4), 2023 (4), 2024 (6), 2025 (11), 2026 (6)
- **Versions named:** 1.10 (3), 1.08 (2)
- **Pipeline stages it appears in:** differential/statistical testing (9), alignment/mapping (2), dimensionality reduction/clustering (1)

## Papers

### Osteoclasts recycle via osteomorphs during RANKL-stimulated bone resorption. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.002 | PMCID: PMC7938889 | PMID: 33636130
- Evidence: ...and Seoighe, 2010 ) https://CRAN.R-project.org/package=NMF MASS ( Venables and Ripley, 2013 ) https://cran.r-project.org/web/packages/MASS/index.html MAGMA ( de Leeuw et al., 2015 ) https://doi.org/10.1371/journal.pcbi.1004219 MtrackJ ( Meijering et al., 2012 ) https://doi.org/10.1016/b978-0-12-391857-4.00009-4 Osteomeasure Osteometrics https://www.osteometrics.com/ plink ( Chang et al., 2015 ) ht...
- Full pipeline: alignment/mapping [STAR v2.4.1] -> normalisation [STAR v2.4.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [RSEM, STAR v2.4.1] -> stage not stated [Cutadapt, ImageJ, MAGMA, ggplot2]

### Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.002 | PMCID: PMC11829167 | PMID: 39814019
- Version used: **1.08**
- Evidence: 44 https://github.com/bulik/ldsc MAGMA v1.08 de Leeuw et al.
- Full pipeline: alignment/mapping [LDSC] -> variant calling [LDSC] -> dimensionality reduction/clustering [LDSC] -> stage not stated [Bioconductor, GCTA, MAGMA v1.08, PLINK v1.9]

### A saturated map of common genetic variants associated with human height. (Nature 2022)

- DOI: 10.1038/s41586-022-05275-y | PMCID: PMC9605867 | PMID: 36224396
- Evidence: Using two popular gene-set prioritization methods (DEPICT 42 and MAGMA 43 ), we found that the same broad clusters of related gene sets (including most of the clusters enriched for OMIM genes) are prioritized at all GWAS sample sizes (Supplementary Fig.
- Full pipeline: dimensionality reduction/clustering [MAGMA] -> differential/statistical testing [LDSC, R] -> stage not stated [GCTA, PLINK]

### Stroke genetics informs drug discovery and risk prediction across ancestries. (Nature 2022)

- DOI: 10.1038/s41586-022-05165-3 | PMCID: PMC9524349 | PMID: 36180795
- Evidence: Gene-based analyses We performed gene-based tests of common variant associations using VEGAS2 8 and MAGMA 9 .
- Full pipeline: quality control [R] -> differential/statistical testing [LDSC] -> stage not stated [GCTA, MAGMA, SAIGE, Seurat, TwoSampleMR]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Version used: **1.10**
- Evidence: We used MAGMA v.1.10 (ref.
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Version used: **1.10**
- Evidence: Gene-level analysis We used Multi-marker Analysis of GenoMic Annotation (MAGMA v.1.10) 34 to conduct a gene-level analysis.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: We calculated the disease-relevance score of each cell in the dataset against a recent Alzheimer’s GWAS, using scDRS (based on MAGMA) 54 , 55 , 116 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### GLP-1-directed NMDA receptor antagonism for obesity treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07419-8 | PMCID: PMC11136670 | PMID: 38750368
- Evidence: SNP, single-nucleotide polymorphism. k , Overlap analyses using the MAGMA and S-LDSC tools to compute BMI GWAS integration. l – r , Treatment of Mc4r -KO mice with once-daily s.c. administration of MK-801, GLP-1, GLP-1–MK-801 or vehicle for 9 days. n = 6–7 mice.
- Full pipeline: differential/statistical testing [DESeq2 v1.30.1, R, limma v3.54.2] -> stage not stated [LDSC, MAGMA]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Evidence: Heritability analyses MAGMA Summary statistics from ref.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Genetic determinants of micronucleus formation in vivo. (Nature 2024)

- DOI: 10.1038/s41586-023-07009-0 | PMCID: PMC10917660 | PMID: 38355793
- Evidence: To do this, we first performed MAGMA analyses (v.1.08) 28 using all genomic variants within each MN gene extracting gene-level associations to the LOY phenotype.
- Full pipeline: variant calling [emmeans] -> differential/statistical testing [R v3.18] -> stage not stated [ImageJ v1.53a, MAGMA]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Evidence: Moreover, FUMA incorporates multimarker analysis of genomic annotation (MAGMA) for both gene-based and gene-set analysis.
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: To do the GWAS-DEG enrichment analysis for microglia isolated from Li-deficient mice, we used MAGMA 87 v.1.10.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Spatially resolved mapping of cells associated with human complex traits. (Nature 2025)

- DOI: 10.1038/s41586-025-08757-x | PMCID: PMC12095064 | PMID: 40108460
- Evidence: These genes were derived from GWAS summary statistics using gene-based association tests (for example, MAGMA 76 ).
- Full pipeline: alignment/mapping [R] -> variant calling [GCTA] -> normalisation [Scanpy] -> dimensionality reduction/clustering [PLINK, Seurat, clusterProfiler] -> differential/statistical testing [MAGMA] -> simulation/modelling [PLINK] -> stage not stated [LDSC]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Evidence: Using the resulting cell-type specificity matrices, we ran CELLECT 28 with MAGMA 29 , alongside GWAS data from the GIANT BMI meta-analysis ( N max = 806,834) 27 , to prioritize hypothalamic cell types that showed enrichment in the BMI GWAS.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: Two different MAGMA 68 tests were conducted with default settings.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Version used: **1.08**
- Evidence: Gene-level analyses Gene-based association testing as well as enrichment analyses were conducted using MAGMA (v1.08) 45 , using default settings unless stated otherwise.
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### A cross-population compendium of gene-environment interactions. (Nature 2026)

- DOI: 10.1038/s41586-025-10054-6 | PMCID: PMC12999510 | PMID: 41606330
- Evidence: Dashed line: FDR threshold of 0.05. b , Same as a , for cross-population portability. c and d , Examples of PGS prediction accuracy within ( c ) and across ( d ) populations, for hematocrit (Ht) stratified by sex. e , MAGMA one-sided gene-set enrichment analyses of age-stratified genetic effects on pulse pressure (PP), using the gene ontologies for biological processes.
- Full pipeline: variant calling [IMPUTE2] -> dimensionality reduction/clustering [R, Seurat v4.3.0.1, UMAP] -> differential/statistical testing [MAGMA] -> stage not stated [BCFtools, LDSC v1.0.0, PLINK v2.00a]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Evidence: Overlap with H-MAGMA Neurodegenerative and neurodevelopmental risk genes were derived from the H-MAGMA study 28 .
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Mapping the genetic landscape across 14 psychiatric disorders. (Nature 2026)

- DOI: 10.1038/s41586-025-09820-3 | PMCID: PMC12779569 | PMID: 41372416
- Evidence: MAGMA gene-set enrichment analyses were performed using the MAGMA.Celltyping package in R 81 .
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [MAGMA, PLINK v1.9, R]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Evidence: Overlap with common-variant risk loci Common-variant gene-based associations were calculated using MAGMA 72 and summary statistics from our previous GWAS meta-analysis of ADHD 13 .
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Specificity, length and luck drive gene rankings in association studies. (Nature 2026)

- DOI: 10.1038/s41586-025-09703-7 | PMCID: PMC12823407 | PMID: 41193809
- Evidence: Ranking genes in GWAS by MAGMA P value We used MAGMA 57 to obtain gene-level P values from GWAS data.
- Full pipeline: differential/statistical testing [MAGMA] -> stage not stated [BEDTools, LDSC, REGENIE, VEP]

### Powerful gene-based testing by integrating long-range chromatin interactions and knockoff genotypes. (PNAS 2021)

- DOI: 10.1073/pnas.2105191118 | PMCID: PMC8617518 | PMID: 34799441
- Evidence: Details of existing gene-based association tests and additional tests for comparison, including GeneScan1D, MAGMA/H-MAGMA, and STAAR-O, as well as KnockoffScreen, are in SI Appendix .
- Full pipeline: stage not stated [MAGMA, R, SAIGE]

### Genome-wide analyses of individual differences in quantitatively assessed reading- and language-related skills in up to 34,000 people. (PNAS 2022)

- DOI: 10.1073/pnas.2202764119 | PMCID: PMC9436320 | PMID: 35998220
- Evidence: Functional Enrichment Using Heritability Partitioning and MAGMA Gene Property Analysis.
- Full pipeline: alignment/mapping [FUMA] -> stage not stated [LDSC, MAGMA]

### Entanglement-assisted concatenated quantum codes. (PNAS 2022)

- DOI: 10.1073/pnas.2202235119 | PMCID: PMC9214521 | PMID: 35687669
- Evidence: By using the MAGMA software ( 40 ), we know that there exists a nondegenerate [[15, 8,6;7]] EAQECC.
- Full pipeline: stage not stated [MAGMA]

### Genomic loci influence patterns of structural covariance in the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2300842120 | PMCID: PMC10756284 | PMID: 38127979
- Evidence: Based on these gene-level P -values, we performed hypothesis-free gene set pathway analysis using MAGMA ( 16 ) ( Method 4E ): a more stringent correction for multiple comparisons was performed than the prioritized gene set enrichment analysis using GENE2FUN from FUMA ( Method 4F and Fig.
- Full pipeline: differential/statistical testing [FUMA, MAGMA, PLINK] -> stage not stated [GCTA, GSEA, LDSC]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Evidence: We used the web tool Functional Mapping and Annotation of Genome-Wide Association Studies (FUMA) ( https://fuma.ctglab.nl/ ) ( 69 ) to conduct a generalized gene set analysis using MAGMA within FUMA ( 70 ) to generate gene lists from GWAS r and GWAS g+r results, as well as gene lists for global area and thickness.
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### The neocortical infrastructure for language involves region-specific patterns of laminar gene expression. (PNAS 2024)

- DOI: 10.1073/pnas.2401687121 | PMCID: PMC11348331 | PMID: 39133845
- Evidence: Genetic variants were mapped to each of the 56 genes based on National Center for Biotechnology Information build 37.3 gene definitions as implemented in MAGMA software ( 93 ), including 50 kb upstream and 50 kb downstream of each gene.
- Full pipeline: quality control [Bioconductor] -> alignment/mapping [MAGMA, STAR v2.5.1b, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [ImageJ v1.53t, R]

### Deciphering the functional specialization of whole-brain spatiomolecular gradients in the adult brain. (PNAS 2024)

- DOI: 10.1073/pnas.2219137121 | PMCID: PMC11194492 | PMID: 38861593
- Evidence: MAGMA ( 110 ) was further used to assess enrichment of genes that are associated with psychiatric disorder through GWAS ( 52 ).
- Full pipeline: stage not stated [MAGMA]

### GWAS for behavioral traits in golden retrievers identifies genes implicated in human temperament, mental health, and cognition. (PNAS 2025)

- DOI: 10.1073/pnas.2421757122 | PMCID: PMC12684936 | PMID: 41284867
- Version used: **1.10**
- Evidence: The gene-based and gene-set enrichment analyses were performed using MAGMA v1.10 on GWAS summary statistics for 14 C-BARQ behavioral traits.
- Full pipeline: variant calling [PLINK v1.9] -> normalisation [GEMMA, tidyverse] -> dimensionality reduction/clustering [GEMMA, tidyverse] -> differential/statistical testing [MAGMA v1.10] -> visualisation [GEMMA, tidyverse] -> stage not stated [GCTA]

### A unified framework for identification of cell-type-specific spatially variable genes in spatial transcriptomic studies. (PNAS 2025)

- DOI: 10.1073/pnas.2503952122 | PMCID: PMC12646224 | PMID: 41223223
- Evidence: We further performed a gene analysis using MAGMA ( 66 ) with GWAS summary statistics data as input and found that NRXN3 was significantly associated with IQ (adjusted P -value 1.284 × 10 − 4 ).
- Full pipeline: differential/statistical testing [LDSC, MAGMA] -> stage not stated [CellChat, R]

### Life without sex: Large-scale study links sexlessness to physical, cognitive, and personality traits, socioecological factors, and DNA. (PNAS 2025)

- DOI: 10.1073/pnas.2418257122 | PMCID: PMC12478097 | PMID: 40956885
- Evidence: We used the GWAS summary statistics to compute gene-based P -value in MAGMA ( 36 ) for 18,714 protein-coding genes using FUMA ( 37 ).
- Full pipeline: differential/statistical testing [FUMA, LDSC, MAGMA] -> stage not stated [R]

### Extreme weather variability on hot rocky exoplanet 55 Cancri e explained by magma temperature-cloud feedback. (PNAS 2025)

- DOI: 10.1073/pnas.2423473122 | PMCID: PMC12054827 | PMID: 40261927
- Evidence: ( 45 ), which used the MAGMA chemical equilibrium code ( 44 , 47 , 48 ).
- Full pipeline: stage not stated [MAGMA]

### Retrospective SARS-CoV-2 human antibody development trajectories are largely sparse and permissive. (PNAS 2025)

- DOI: 10.1073/pnas.2412787122 | PMCID: PMC11789010 | PMID: 39841142
- Evidence: MAGMA-seq Sorting and Parameter Estimation.
- Full pipeline: stage not stated [MAGMA]

