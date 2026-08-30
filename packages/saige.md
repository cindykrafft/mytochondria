# SAIGE

- **Category:** statgen
- **Papers in survey:** 21
- **Journals:** Nature (17), PNAS (3), Science (1)
- **Years:** 2021 (5), 2022 (5), 2023 (3), 2024 (5), 2025 (3)
- **Versions named:** 1.1.5 (1), 0.35.8.8 (1), 0.39 (1)
- **Pipeline stages it appears in:** differential/statistical testing (8), alignment/mapping (2), dimensionality reduction/clustering (2), variant calling (1), quality control (1)

## Papers

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: ..., rheumatoid arthritis 95 , educational attainment 96 , schizophrenia 97 , age at menarche 98 , tobacco use disorder ( ftp://share.sph.umich.edu/UKBB_SAIGE_HRC/, Phenotype code: 318 ) 99 , intelligence 100 , amyotrophic lateral sclerosis 101 , anorexia nervosa 102 and height 103 .
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### Rare variant contribution to human disease in 281,104 UK Biobank exomes. (Nature 2021)

- DOI: 10.1038/s41586-021-03855-y | PMCID: PMC8458098 | PMID: 34375979
- Evidence: We performed single-variant association tests across all autosomal variants for 324 Chapter IX binary phenotypes (diseases of the circulatory system; Supplementary Table 29 ) using SAIGE SPA 12 and REGENIE 2.0.2 (ref.
- Full pipeline: differential/statistical testing [R] -> stage not stated [REGENIE v2.0.2, SAIGE, SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Mapping the human genetic architecture of COVID-19. (Nature 2021)

- DOI: 10.1038/s41586-021-03767-x | PMCID: PMC8674144 | PMID: 34237774
- Evidence: We recommended that genome-wide association study (GWAS) analyses were run using Scalable and Accurate Implementation of GEneralized mixed model (SAIGE) 39 on chromosomes 1–22 and X.
- Full pipeline: differential/statistical testing [LDSC v1.0.1] -> stage not stated [PLINK, R, SAIGE, TwoSampleMR]

### Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program. (Nature 2021)

- DOI: 10.1038/s41586-021-03205-y | PMCID: PMC7875770 | PMID: 33568819
- Evidence: To perform the association analyses, we used a logistic mixed model test implemented in SAIGE 114 with birth year and the top four principal components (computed from the white British subset) as covariates.
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> stage not stated [BWA, Docker, GATK v3.5.0, R, SAMtools, VEP]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: GWAS summary statistics were generated in each study sample typically using RVTESTS 43 , BOLT-LMM 44 or SAIGE 45 with covariates of sex, age, age squared and genetic principal components according to an analysis plan detailed in the Supplementary Note .
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### Stroke genetics informs drug discovery and risk prediction across ancestries. (Nature 2022)

- DOI: 10.1038/s41586-022-05165-3 | PMCID: PMC9524349 | PMID: 36180795
- Evidence: Similar profiles were observed in the UK Biobank ( https://pheweb.org/UKB-SAIGE/variant/4-187207381-C-T ) and FinnGen ( https://r7.finngen.fi/variant/4-186286227-C-T ), with no significant associations with other disorders and no overlap of subthreshold signals with side-effects reported in clinical trials 33 .
- Full pipeline: quality control [R] -> differential/statistical testing [LDSC] -> stage not stated [GCTA, MAGMA, SAIGE, Seurat, TwoSampleMR]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Evidence: Genome-wide association study analysis After quality control procedures, we used a logistic mixed model regression, implemented in SAIGE 12 , to perform association analyses with unrelated individuals (critically ill cases, n = 7,491; controls, n = 48,400 (100,000 Genomes Project (100k) cohort, n = 46,770; mild COVID-19, n = 1,630) ( Methods , Supplementary Table 2 ).
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### Genetic associations of protein-coding variants in human disease. (Nature 2022)

- DOI: 10.1038/s41586-022-04394-w | PMCID: PMC8891017 | PMID: 35197637
- Version used: **0.39**
- Evidence: Association analyses in FG were performed using mixed model logistic regression method SAIGE v0.39 42 .
- Full pipeline: differential/statistical testing [SAIGE v0.39] -> stage not stated [PLINK, REGENIE v1.0.6.7]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Version used: **1.1.5**
- Evidence: For GWAS, SAIGE v.1.1.5 (ref.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Mono- and biallelic variant effects on disease at biobank scale. (Nature 2023)

- DOI: 10.1038/s41586-022-05420-7 | PMCID: PMC9849130 | PMID: 36653560
- Evidence: GWAS searching for additive and recessive associations We performed a GWAS on 2,444 disease end-points, investigating the effects of 82,647 coding variants with an additive and recessive model using the method SAIGE 23 .
- Full pipeline: stage not stated [SAIGE]

### FinnGen provides genetic insights from a well-phenotyped isolated population. (Nature 2023)

- DOI: 10.1038/s41586-022-05473-8 | PMCID: PMC9849126 | PMID: 36653562
- Version used: **0.35.8.8**
- Evidence: Association analysis and fine-mapping The mixed-model logistic regression method SAIGE (v.0.35.8.8) 54 was used for association analysis.
- Full pipeline: alignment/mapping [SAIGE v0.35.8.8] -> variant calling [GATK] -> differential/statistical testing [SAIGE v0.35.8.8] -> stage not stated [R v4.0, VEP]

### Refining the impact of genetic evidence on clinical success. (Nature 2024)

- DOI: 10.1038/s41586-024-07316-0 | PMCID: PMC11096124 | PMID: 38632401
- Evidence: 31 ) ( n = 2,338) or SAIGE ( n = 1,229).
- Full pipeline: differential/statistical testing [R v4.2] -> stage not stated [SAIGE]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Evidence: The mixed-model logistic regression method SAIGE (R package developed with Rcpp for genome-wide association tests in large-scale datasets and biobanks) was used for association analysis and included the following covariates in the model: sex, age, genotyping batch and ten principle components.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### Genome-wide characterization of circulating metabolic biomarkers. (Nature 2024)

- DOI: 10.1038/s41586-024-07148-y | PMCID: PMC10990933 | PMID: 38448586
- Evidence: The ICP GWAS was performed with scalable and accurate implementation of generalized mixed model (SAIGE).
- Full pipeline: differential/statistical testing [R] -> stage not stated [GCTA, PLINK v2.0, SAIGE, TwoSampleMR v0.5.1]

### Identification of constrained sequence elements across 239 primate genomes. (Nature 2024)

- DOI: 10.1038/s41586-023-06798-8 | PMCID: PMC10808062 | PMID: 38030727
- Evidence: In brief, fine mapping was performed using FINEMAP 65 , 66 and SuSiE 67 with GWAS summary statistics from SAIGE/BOLT-LMM and in-sample dosage linkage disequilibrium (LD) computed by LDstore 2 68 .
- Full pipeline: alignment/mapping [SAIGE, minimap2] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [RepeatMasker v4.1.2, VEP]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Evidence: Alternatively, a generalized mixed-effect approach, which analyses sample correlation by considering a random effect—such as SAIGE 16 and REGENIE 17 for case–control studies and BOLT-LMM 18 and REGENIE 17 for quantitative trait studies—can be used for genome-wide association studies (GWASs) without a reduction in sample size.
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### Population-specific polygenic risk scores for people of Han Chinese ancestry. (Nature 2025)

- DOI: 10.1038/s41586-025-09350-y | PMCID: PMC12675292 | PMID: 41094136
- Evidence: SAIGE was applied for the mixed-effect model GWAS 67 .
- Full pipeline: quantification [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, LDSC] -> differential/statistical testing [LDSC, PLINK, SAIGE] -> stage not stated [ANNOVAR, R]

### Powerful gene-based testing by integrating long-range chromatin interactions and knockoff genotypes. (PNAS 2021)

- DOI: 10.1073/pnas.2105191118 | PMCID: PMC8617518 | PMID: 34799441
- Evidence: These gene-based results for the UK Biobank traits complement existing databases for single-variant tests ( 63 ) and rare variant-focused tests, such as SAIGE-GENE, a scalable generalized mixed-model region-based association test ( 6 ).
- Full pipeline: stage not stated [MAGMA, R, SAIGE]

### Microbiome-associated human genetic variants impact phenome-wide disease risk. (PNAS 2022)

- DOI: 10.1073/pnas.2200551119 | PMCID: PMC9245617 | PMID: 35749358
- Evidence: Analyses on binary outcomes were computed using the SAIGE method ( 54 ) to account for size and case–control imbalances.
- Full pipeline: variant calling [PLINK] -> visualisation [ComplexHeatmap v2.12] -> stage not stated [R, SAIGE, VEP]

### Exome sequencing identifies genes for socioeconomic status in 350,770 individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2414018122 | PMCID: PMC11745334 | PMID: 39772748
- Evidence: We first aggregated rare variants of putative loss-of-function (pLOF) alone and in combination with likely deleterious missense variants, and performed gene-based collapsing analysis with 4 maximum MAF (max-MAF) cutoffs, utilizing a generalized mixed model implemented in SAIGE-GENE+ ( 20 ).
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ANNOVAR, FUMA, PLINK v2.0, SAIGE, Seurat, SnpEff]

### Diversity and scale: Genetic architecture of 2068 traits in the VA Million Veteran Program. (Science 2024)

- DOI: 10.1126/science.adj1182 | PMCID: PMC12857194 | PMID: 39024449
- Evidence: The existing implementation of the Scalable and Accurate Implementation of Generalized mixture model (SAIGE) algorithm ( 10 )—ideal for our design in order to address case/control imbalances—was not analytically tractable at this scale of computation and would have required ~251 compute years to complete.
- Full pipeline: stage not stated [FUMA, LDSC, SAIGE, VEP]

