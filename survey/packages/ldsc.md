# LDSC

- **Category:** statgen
- **Papers in survey:** 62
- **Journals:** Nature (34), PNAS (21), Science (4), Cell (3)
- **Years:** 2021 (5), 2022 (14), 2023 (10), 2024 (10), 2025 (12), 2026 (11)
- **Versions named:** 1.0.1 (4), 1.0.0 (1)
- **Pipeline stages it appears in:** differential/statistical testing (41), dimensionality reduction/clustering (2), quantification (2), variant calling (2), normalisation (1), simulation/modelling (1), alignment/mapping (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Evidence: .../ldsc PRsice2 Choi and O’Reilly, 2019 ; Choi et al., 2020 https://www.prsice.info LDpred Vilhjálmsson et al., 2015 https://github.com/bvilhjal/ldpred LDSC (LD SCore) Bulik-Sullivan et al., 2015a , 2015b https://github.com/bulik/ldsc/ fast.coloc Genetics ToolboX Created by Toby Johnson 2019. https://github.com/tobyjohnson/gtx/blob/526120435bb3e29c39fc71604eee03a371ec3753/R/coloc.R ConsensusPathDB-h...
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Version used: **1.0.1**
- Evidence: 178 GWAS heritability enrichment analysis was carried out using linkage disequilibrium (LD) score regression (LDSC, v.1.0.1) following the tutorial guidelines.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.002 | PMCID: PMC11829167 | PMID: 39814019
- Evidence: ...) associations This paper https://doi.org/10.6084/m9.figshare.27089614 Hi-C chromatin mapping This paper https://doi.org/10.6084/m9.figshare.27089614 LDSC genetic correlation estimates This paper https://doi.org/10.6084/m9.figshare.27089614 Principal components plots for genotyped studies This paper. https://doi.org/10.6084/m9.figshare.27089614 DrugTargetor enrichment tests This paper https://doi....
- Full pipeline: alignment/mapping [LDSC] -> variant calling [LDSC] -> dimensionality reduction/clustering [LDSC] -> stage not stated [Bioconductor, GCTA, MAGMA v1.08, PLINK v1.9]

### Exome sequencing and analysis of 454,787 UK Biobank participants. (Nature 2021)

- DOI: 10.1038/s41586-021-04103-z | PMCID: PMC8596853 | PMID: 34662886
- Evidence: We did this by estimating the genetic correlation between each trait and 357 disease outcomes (specifically, 3-digit ICD codes, expert-curated definitions, self-report and doctor-diagnosed diseases; we only considered diseases that had at least 1 rare variant association at P < 10 −7 ), using LD score regression 44 and association results from the TOPMed-based GWAS described above.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [LDSC, REGENIE] -> stage not stated [GCTA v1.91.7, SnpEff]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Version used: **1.0.1**
- Evidence: We applied stratified LD score regression (LDSC version 1.0.1 75 , 76 ) to these summary statistics to evaluate the enrichment of trait heritability in each of ten predicted enhancer sets.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### Mapping the human genetic architecture of COVID-19. (Nature 2021)

- DOI: 10.1038/s41586-021-03767-x | PMCID: PMC8674144 | PMID: 34237774
- Version used: **1.0.1**
- Evidence: Heritability LD score regression v.1.0.1 49 was used to estimate the SNP heritability of the phenotypes from the meta-analysis summary statistic files.
- Full pipeline: differential/statistical testing [LDSC v1.0.1] -> stage not stated [PLINK, R, SAIGE, TwoSampleMR]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: To further evaluate robustness of our results, we estimated LD score regression (LDSC) intercepts and attenuation ratios to account for bias in the intercept test when sample sizes become extreme, as in the present case.
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### A saturated map of common genetic variants associated with human height. (Nature 2022)

- DOI: 10.1038/s41586-022-05275-y | PMCID: PMC9605867 | PMID: 36224396
- Evidence: To further assess whether LD in our META FE could be reasonably approximated by the LD from EUR, we performed an LD score regression 16 analysis of our META FE using LD scores estimated in EUR.
- Full pipeline: dimensionality reduction/clustering [MAGMA] -> differential/statistical testing [LDSC, R] -> stage not stated [GCTA, PLINK]

### Stroke genetics informs drug discovery and risk prediction across ancestries. (Nature 2022)

- DOI: 10.1038/s41586-022-05165-3 | PMCID: PMC9524349 | PMID: 36180795
- Evidence: We applied the covariate adjusted linkage disequilibrium score regression (cov-LDSC) method to ancestry-specific GWAS meta-analyses without GC correction to test for genomic inflation and to compute robust SNP-heritability estimates in admixed populations 51 .
- Full pipeline: quality control [R] -> differential/statistical testing [LDSC] -> stage not stated [GCTA, MAGMA, SAIGE, Seurat, TwoSampleMR]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Evidence: Effect sizes based on the leave-one-chromosome out residuals were shrunk and we rescaled them based on the shrinkage of the 1.1 million variants used in the LD score regression.
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Evidence: Heritability For the SNP-based narrow-sense heritabilities of severe COVID-19 and HGI COVID phenotypes, both high-definition likelihood (HDL) and LD score regression (LDSC) 59 methods were applied.
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: To test this, we performed stratified linkage disequilibrium score regression (LDSC) 62 .
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Evidence: We used LD score regression to account for inflation in test statistics due to cryptic relatedness and stratification 72 .
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Evidence: Heritability estimation and enrichment analyses for mtCN S-LDSC 25 was used for heritability estimation and enrichment analyses for mtCN in UKB as performed previously 24 .
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Polygenic scoring accuracy varies across the genetic ancestry continuum. (Nature 2023)

- DOI: 10.1038/s41586-023-06079-4 | PMCID: PMC10284707 | PMID: 37198491
- Evidence: For all chains, we set the initial heritability as the LD score regression heritability 72 estimated by the built-in function snp_ldsc.
- Full pipeline: variant calling [PLINK] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [R]

### Examining the role of common variants in rare neurodevelopmental conditions. (Nature 2024)

- DOI: 10.1038/s41586-024-08217-y | PMCID: PMC11634775 | PMID: 39567701
- Evidence: We also used linkage disequilibrium score regression (LDSC) 83 to estimate SNP heritability using summary statistics from the GWAS of neurodevelopmental conditions in DDD, in GEL, and a meta-analysis of the two cohorts.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GCTA, LDSC] -> stage not stated [PLINK, VEP]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Evidence: Polygenic heritability enrichment analysis Polygenic heritability enrichment of DMRs and/or chromatin loops was analysed using a stratified linkage disequilibrium score regression (S-LDSC)-based partitioned heritability approach 61 .
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### GLP-1-directed NMDA receptor antagonism for obesity treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07419-8 | PMCID: PMC11136670 | PMID: 38750368
- Evidence: SNP, single-nucleotide polymorphism. k , Overlap analyses using the MAGMA and S-LDSC tools to compute BMI GWAS integration. l – r , Treatment of Mc4r -KO mice with once-daily s.c. administration of MK-801, GLP-1, GLP-1–MK-801 or vehicle for 9 days. n = 6–7 mice.
- Full pipeline: differential/statistical testing [DESeq2 v1.30.1, R, limma v3.54.2] -> stage not stated [LDSC, MAGMA]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Evidence: The LDSC analysis was performed according to the standard workflow ( https://github.com/bulik/ldsc/wiki ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Evidence: Stratified LD score regression To partition SNP heritability, we used stratified LD score regression (S-LDSC; v.1.0.1) 26 , which assesses the contribution of gene expression programs to disease heritability.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Identification of constrained sequence elements across 239 primate genomes. (Nature 2024)

- DOI: 10.1038/s41586-023-06798-8 | PMCID: PMC10808062 | PMID: 38030727
- Evidence: A similar enrichment analysis was performed using stratified LD score regression (S-LDSC) 72 to estimate the heritability in each annotation.
- Full pipeline: alignment/mapping [SAIGE, minimap2] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [RepeatMasker v4.1.2, VEP]

### Population-specific polygenic risk scores for people of Han Chinese ancestry. (Nature 2025)

- DOI: 10.1038/s41586-025-09350-y | PMCID: PMC12675292 | PMID: 41094136
- Evidence: Heritability, genetic correlation and clustering To quantify the genomic contribution of the specific traits, we applied linkage disequilibrium score regression to estimate the SNP-based heritability with LDSC 26 .
- Full pipeline: quantification [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, LDSC] -> differential/statistical testing [LDSC, PLINK, SAIGE] -> stage not stated [ANNOVAR, R]

### Polygenic and developmental profiles of autism differ by age at diagnosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09542-6 | PMCID: PMC12571882 | PMID: 41034588
- Evidence: We conducted genetic correlation analyses using LDSC, with linkage disequilibrium scores from the northwest European populations.
- Full pipeline: differential/statistical testing [PLINK, lme4 v1.1.27.1] -> stage not stated [GCTA, LDSC, lavaan v0.6]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: These CREs were also used in the GWAS analyses to assess LDSC trait heritability and fine-map causal variants at PTSD risk loci in a cell-type-specific manner.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Translational genomics of osteoarthritis in 1,962,069 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-08771-z | PMCID: PMC12119359 | PMID: 40205036
- Evidence: In brief, we first estimated the genetic correlation matrix between the 11 osteoarthritis traits by using bivariate LD score regression 53 with genome-wide meta-analysis summary statistics.
- Full pipeline: quality control [BCFtools v1.13, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [Enrichr, GCTA, PLINK]

### Spatially resolved mapping of cells associated with human complex traits. (Nature 2025)

- DOI: 10.1038/s41586-025-08757-x | PMCID: PMC12095064 | PMID: 40108460
- Evidence: 20200722YJ001). gsMap method Design principles To effectively illustrate gsMap, we first summarize its design principles. gsMap utilizes the framework of S-LDSC 17 to assess whether genetic variants, mainly SNPs, located in or near genes specifically expressed in a spot in ST data are enriched for genetic associations with a trait of interest.
- Full pipeline: alignment/mapping [R] -> variant calling [GCTA] -> normalisation [Scanpy] -> dimensionality reduction/clustering [PLINK, Seurat, clusterProfiler] -> differential/statistical testing [MAGMA] -> simulation/modelling [PLINK] -> stage not stated [LDSC]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: Each trait is assigned to a group of related traits (Immune, blood pressure, cognitive, hayfever and psychiatric) and LDSC analysis (one-sided) is used to identify susceptible cell types.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Evidence: Analyzing correlation between trait effect sizes and selection coefficients We used LD score regression (LDSC) version 1.0.1 40 , 49 , 70 to estimate the genetic correlation between trait effect sizes and selection coefficients (s).
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### The DNA virome varies with human genes and environments. (Nature 2026)

- DOI: 10.1038/s41586-026-10288-y | PMCID: PMC13215884 | PMID: 41882355
- Evidence: To compute genetic correlation between viral phenotypes in UKB, AoU, and SPARK, LDSC 93 (v.2.0.0) was run with standard settings and pairs of viral summary statistics as input.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [DeepVariant] -> differential/statistical testing [LDSC] -> stage not stated [R]

### A cross-population compendium of gene-environment interactions. (Nature 2026)

- DOI: 10.1038/s41586-025-10054-6 | PMCID: PMC12999510 | PMID: 41606330
- Version used: **1.0.0**
- Evidence: ...ethods/GEM ), OSCA v.0.46 ( https://cnsgenomics.com/software/osca ), bgenie v.1.3 ( https://jmarchini.org/bgenie/ ), LocusZoom v.1.4 (locuszoom.org), LDSC v.1.0.0 ( https://github.com/bulik/ldsc ), PRScs version 4 June 2021 ( https://github.com/getian107/PRScs ), MAGMA v1.09a ( https://ctg.cncr.nl/software/magma ), scDRS v.1.0.2 ( https://martinjzhang.github.io/scDRS/ ), enformer ( https://github....
- Full pipeline: variant calling [IMPUTE2] -> dimensionality reduction/clustering [R, Seurat v4.3.0.1, UMAP] -> differential/statistical testing [MAGMA] -> stage not stated [BCFtools, LDSC v1.0.0, PLINK v2.00a]

### Human and bacterial genetic variation shape oral microbiomes and health. (Nature 2026)

- DOI: 10.1038/s41586-025-10037-7 | PMCID: PMC12979206 | PMID: 41606319
- Evidence: Stratified LD score regression for estimating enrichment of heritability at genes with tissue-specific expression We observed that the same mathematical framework that enables partitioning of heritability by means of stratified LD score regression on summary statistics from GWAS of a single trait 74 could be extended to analyse test statistics for association with oral microbiome composition (base...
- Full pipeline: quality control [DeepVariant v1.3.0, PLINK v2.00a] -> alignment/mapping [DeepVariant v1.3.0] -> variant calling [DeepVariant v1.3.0] -> differential/statistical testing [LDSC, R] -> visualisation [ChimeraX v1.9] -> stage not stated [AlphaFold, Bowtie2, MetaPhlAn v4.0.6, SAMtools v1.15.1]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: Datasets used for genome-wide association study enrichment are available through LDSC: for ASD from ref.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Evidence: To estimate heritability of SNPs and genomic inflation, we performed linkage disequilibrium score regression (LDSC) by applying the ldsc package (v.1.0.1).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Evidence: Linkage disequilibrium score regression To identify traits whose heritability is enriched in open chromatin regions in K562, we used S-LDSC 9 .
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### Mapping the genetic landscape across 14 psychiatric disorders. (Nature 2026)

- DOI: 10.1038/s41586-025-09820-3 | PMCID: PMC12779569 | PMID: 41372416
- Evidence: Genomic SEM Genome-wide models All GWAS summary statistics were run through the munge function before running the multivariable version of LDSC used as input to genomic SEM 7 .
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [MAGMA, PLINK v1.9, R]

### Estimation and mapping of the missing heritability of human phenotypes. (Nature 2026)

- DOI: 10.1038/s41586-025-09720-6 | PMCID: PMC12851931 | PMID: 41225014
- Evidence: (b) Genetic correlations estimated from common variants LD score regression.
- Full pipeline: variant calling [PLINK] -> dimensionality reduction/clustering [PLINK] -> differential/statistical testing [LDSC] -> stage not stated [R, REGENIE]

### Specificity, length and luck drive gene rankings in association studies. (Nature 2026)

- DOI: 10.1038/s41586-025-09703-7 | PMCID: PMC12823407 | PMID: 41193809
- Evidence: Linking traits to tissues To identify which tissue (or cell type) is predominantly associated with a given trait, we ran S-LDSC 9 , 41 to partition the heritability of all of our traits that had an estimated heritability of more than 0.04.
- Full pipeline: differential/statistical testing [MAGMA] -> stage not stated [BEDTools, LDSC, REGENIE, VEP]

### Mendelian randomization identifies blood metabolites previously linked to midlife cognition as causal candidates in Alzheimer's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2009808118 | PMCID: PMC8072203 | PMID: 33879569
- Evidence: To meet criterion b, pairwise genetic correlations ( rg ) across metabolites were computed using linkage disequilibrium score regression (LDSC) ( 48 ).
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [TwoSampleMR]

### Quality assessment and refinement of chromatin accessibility data using a sequence-based predictive model. (PNAS 2022)

- DOI: 10.1073/pnas.2212810119 | PMCID: PMC9907136 | PMID: 36508674
- Evidence: S-LDSC.
- Full pipeline: quality control [Jupyter] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [LDSC, MACS2, featureCounts]

### Using neuroimaging genomics to investigate the evolution of human brain structure. (PNAS 2022)

- DOI: 10.1073/pnas.2200638119 | PMCID: PMC9546597 | PMID: 36161899
- Evidence: The LDSC ( 60 ) intercept for each set of summary statistics was estimated as an additional measure of population stratification, following the guidelines given in the LDSC website ( https://github.com/bulik/ldsc/wiki/LD-Score-Estimation-Tutorial ).
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [LDSC] -> stage not stated [FreeSurfer, PLINK, R, ggplot2]

### A quantile integral linear model to quantify genetic effects on phenotypic variability. (PNAS 2022)

- DOI: 10.1073/pnas.2212959119 | PMCID: PMC9522331 | PMID: 36122202
- Evidence: Additionally, we used the estimated intercept from LD score regression ( 48 ) to quantify the level of unadjusted confounding in genome-wide vQTL analysis.
- Full pipeline: quantification [LDSC] -> differential/statistical testing [LDSC, PLINK]

### Genome-wide analyses of individual differences in quantitatively assessed reading- and language-related skills in up to 34,000 people. (PNAS 2022)

- DOI: 10.1073/pnas.2202764119 | PMCID: PMC9436320 | PMID: 35998220
- Evidence: To do so, we used LDSC heritability partitioning ( 39 ), a method that uses GWAS results to investigate whether common DNA variants in a certain set of genomic regions, named an annotation, explain a larger proportion of the SNP-based heritability of the trait than is expected based on the size of that annotation.
- Full pipeline: alignment/mapping [FUMA] -> stage not stated [LDSC, MAGMA]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: S-LDSC Regression.
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### Mendelian randomization for causal inference accounting for pleiotropy and sample structure using genome-wide summary statistics. (PNAS 2022)

- DOI: 10.1073/pnas.2106858119 | PMCID: PMC9282238 | PMID: 35787050
- Evidence: Sample overlap × MR-APSS × × All IVs can be invalid; assumptions of LDSC ( 16 ) in the background model; InSIDE in the foreground model. ✓ ✓ Three IV assumptions: (A-I) IVs are associated with the exposure; (A-II) IVs are independent of confounders; and (A-III) IVs only affect the outcome through the exposure.
- Full pipeline: stage not stated [LDSC]

### GWAS on birth year infant mortality rates provides evidence of recent natural selection. (PNAS 2022)

- DOI: 10.1073/pnas.2117312119 | PMCID: PMC8944929 | PMID: 35290122
- Evidence: We also applied LD score regression-based genomic control where we inflated the SE of SNP effects using s e G C = s e × LDSC intercept to conservatively control unadjusted confounding in association tests.
- Full pipeline: differential/statistical testing [LDSC] -> visualisation [R]

### Genetics, leadership position, and well-being: An investigation with a large-scale GWAS. (PNAS 2022)

- DOI: 10.1073/pnas.2114271119 | PMCID: PMC8944770 | PMID: 35286190
- Version used: **1.0.1**
- Evidence: We used the software LDSC version 1.0.1 ( https://github.com/bulik/ldsc ) with GWAS summary statistics to estimate common SNP -h 2 for three phenotypes: leadership position, managing demands, and MTAG-leadership for the whole sample and subsamples by sex in the UKB discovery data ( 26 ).
- Full pipeline: alignment/mapping [ANNOVAR] -> differential/statistical testing [LDSC v1.0.1] -> stage not stated [METAL, PLINK v1.07]

### Identification of genetic risk loci and prioritization of genes and pathways for myasthenia gravis: a genome-wide association study. (PNAS 2022)

- DOI: 10.1073/pnas.2108672119 | PMCID: PMC8812681 | PMID: 35074870
- Evidence: The shared genetic risks between myasthenia gravis and other diseases were estimated using the Linkage Disequilibrium Score Regression method ( 13 ) using the LDSC tool (available on https://github.com/bulik/ldsc ).
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Jupyter, LDSC]

### Genomic loci influence patterns of structural covariance in the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2300842120 | PMCID: PMC10756284 | PMID: 38127979
- Evidence: ..., 33,541 people of European ancestry) and a previous independent study of Alzheimer’s disease ( 29 ) (i.e., 63,926 people of European ancestry) using LDSC ( 30 ).
- Full pipeline: differential/statistical testing [FUMA, MAGMA, PLINK] -> stage not stated [GCTA, GSEA, LDSC]

### Contraception ends the genetic maintenance of human same-sex sexual behavior. (PNAS 2023)

- DOI: 10.1073/pnas.2303418120 | PMCID: PMC10214190 | PMID: 37186855
- Evidence: Genome-wide association analysis (GWAS) was respectively performed on these two traits in the OSB European ancestry population mentioned to obtain summary statistics ( Materials and Methods ), based on which the genetic correlation was computed using crosstrait LD score regression ( 12 ).
- Full pipeline: differential/statistical testing [LDSC]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Evidence: We then computed genetic correlations using LDSC ( 68 ) per region between GWAS g and GWAS g+r ( Fig.
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### Neuron-specific transcriptomic signatures indicate neuroinflammation and altered neuronal activity in ASD temporal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2206758120 | PMCID: PMC10013873 | PMID: 36862688
- Evidence: Stratified LD score regression (sLDSC) ( 83 ) was used to test whether a gene set of interest is enriched for SNP-heritability in a given GWAS dataset.
- Full pipeline: quantification [featureCounts v1.6.4] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [DESeq2 v1.22.2, GSEA, WGCNA]

### Controlling for polygenic genetic confounding in epidemiologic association studies. (PNAS 2024)

- DOI: 10.1073/pnas.2408715121 | PMCID: PMC11536117 | PMID: 39432782
- Evidence: We used LD score regression to obtain both ρ ^ g X , Y and h ^ X 2 throughout this study ( 14 , 15 ).
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [PLINK]

### Fast and scalable ensemble learning method for versatile polygenic risk prediction. (PNAS 2024)

- DOI: 10.1073/pnas.2403210121 | PMCID: PMC11331062 | PMID: 39110727
- Evidence: For this grid search, we use 0.7, 1, and 1.3 times the heritability h 2 estimated from LD score regression ( 78 ) –21 values of π between 10 −5 and 1, as well as “True” and “False” for the “sparse” setting that forces more posterior SNP effects to be 0.
- Full pipeline: differential/statistical testing [LDSC] -> simulation/modelling [GCTA] -> machine learning [R]

### Multivariate genetic architecture reveals testosterone-driven sexual antagonism in contemporary humans. (PNAS 2024)

- DOI: 10.1073/pnas.2404364121 | PMCID: PMC11181031 | PMID: 38833469
- Evidence: We used LDSC regression ( 43 ) to estimate all the elements of the G mf matrix (genetic covariances) as well as the genetic correlations using 12 male and 12 female traits.
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [R]

### A unified framework for identification of cell-type-specific spatially variable genes in spatial transcriptomic studies. (PNAS 2025)

- DOI: 10.1073/pnas.2503952122 | PMCID: PMC12646224 | PMID: 41223223
- Evidence: By treating a cell-type-specific SNP set as the annotation set, we evaluated whether the corresponding cell-type-specific genes can explain a higher proportion of heritability for a phenotype using the stratified linkage disequilibrium score regression (S-LDSC) ( 46 , 59 , 60 ).
- Full pipeline: differential/statistical testing [LDSC, MAGMA] -> stage not stated [CellChat, R]

### Life without sex: Large-scale study links sexlessness to physical, cognitive, and personality traits, socioecological factors, and DNA. (PNAS 2025)

- DOI: 10.1073/pnas.2418257122 | PMCID: PMC12478097 | PMID: 40956885
- Evidence: Genetic correlations were computed with LD score regression ( 12 , 15 ), which estimates the slope from the regression of the product of z-scores from two GWASs on the LD score, reflecting the genetic covariation between two traits based on all polygenic effects captured by the included SNPs.
- Full pipeline: differential/statistical testing [FUMA, LDSC, MAGMA] -> stage not stated [R]

### Participation bias in the estimation of heritability and genetic correlation. (PNAS 2025)

- DOI: 10.1073/pnas.2425530122 | PMCID: PMC12207467 | PMID: 40540605
- Evidence: In practice, the heritability and genetic correlation are often estimated with marker-based methods such as LDSC.
- Full pipeline: variant calling [R] -> differential/statistical testing [PLINK v1.90] -> stage not stated [LDSC]

### Observational epidemiological studies can mitigate genetic confounding with a genetic relatedness matrix. (PNAS 2026)

- DOI: 10.1073/pnas.2533909123 | PMCID: PMC13167772 | PMID: 42090255
- Evidence: We next generated LD scores for our simulated genotypes using LDSC ( 1 ) with a window size of 100 kb.
- Full pipeline: variant calling [LDSC] -> differential/statistical testing [PLINK] -> simulation/modelling [LDSC, PLINK] -> stage not stated [GCTA]

### Single-cell DNA methylation and 3D genome architecture in the human brain. (Science 2023)

- DOI: 10.1126/science.adf5357 | PMCID: PMC10572106 | PMID: 37824674
- Evidence: (H) Heatmap showing the results of LDSC analysis of the variants associated with the indicated traits or diseases in DMRs identified from major human cell types.
- Full pipeline: stage not stated [LDSC]

### A genome-wide genetic screen uncovers determinants of human pigmentation. (Science 2023)

- DOI: 10.1126/science.ade6289 | PMCID: PMC10901463 | PMID: 37561850
- Evidence: We applied stratified linkage disequilibrium score regression (S-LDSC) ( 38 ) to assess skin color heritability enrichment in the vicinity (within 100 kb) of our screen hits by using publicly available summary statistics from a GWAS of individuals of white British ancestry in the UKBB.
- Full pipeline: differential/statistical testing [LDSC]

### Diversity and scale: Genetic architecture of 2068 traits in the VA Million Veteran Program. (Science 2024)

- DOI: 10.1126/science.adj1182 | PMCID: PMC12857194 | PMID: 39024449
- Evidence: Following up on each GWAS, we used LDSC ( 50 ) to identify traits with significant heritability in each of the four separate populations and Popcorn ( 13 ) to identify traits with significant genetic correlations across distinct population groups.
- Full pipeline: stage not stated [FUMA, LDSC, SAIGE, VEP]

### Transcription factor networks disproportionately enrich for heritability of blood cell phenotypes. (Science 2025)

- DOI: 10.1126/science.ads7951 | PMCID: PMC12168499 | PMID: 40179192
- Evidence: For each of the blood cell traits, we also examined the proportion of heritability explained by SNPs in various regions, using partitioned linkage disequilibrium score regression (LDSC) ( Materials and Methods ).
- Full pipeline: differential/statistical testing [LDSC]

