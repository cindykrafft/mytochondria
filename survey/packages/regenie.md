# REGENIE

- **Category:** statgen
- **Papers in survey:** 21
- **Journals:** Nature (21)
- **Years:** 2021 (2), 2022 (2), 2023 (3), 2024 (3), 2025 (4), 2026 (7)
- **Versions named:** 3.5 (2), 3.2 (1), 4.1 (1), 3.4.1 (1), 3.2.9 (1), 2.2.4 (1), 3.1.3 (1), 2.2.1 (1), 1.0.6.7 (1), 2.0.2 (1)
- **Pipeline stages it appears in:** differential/statistical testing (9), dimensionality reduction/clustering (3), variant calling (2)

## Papers

### Exome sequencing and analysis of 454,787 UK Biobank participants. (Nature 2021)

- DOI: 10.1038/s41586-021-04103-z | PMCID: PMC8596853 | PMID: 34662886
- Evidence: Genetic association analyses Association analyses were performed using the genome-wide regression test implemented in REGENIE 7 , separately for data derived from exome-sequencing and TOPMed imputation.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [LDSC, REGENIE] -> stage not stated [GCTA v1.91.7, SnpEff]

### Rare variant contribution to human disease in 281,104 UK Biobank exomes. (Nature 2021)

- DOI: 10.1038/s41586-021-03855-y | PMCID: PMC8458098 | PMID: 34375979
- Version used: **2.0.2**
- Evidence: We performed single-variant association tests across all autosomal variants for 324 Chapter IX binary phenotypes (diseases of the circulatory system; Supplementary Table 29 ) using SAIGE SPA 12 and REGENIE 2.0.2 (ref.
- Full pipeline: differential/statistical testing [R] -> stage not stated [REGENIE v2.0.2, SAIGE, SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Evidence: Association analyses in each study were performed using the genome-wide Firth logistic regression test implemented in REGENIE.
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### Genetic associations of protein-coding variants in human disease. (Nature 2022)

- DOI: 10.1038/s41586-022-04394-w | PMCID: PMC8891017 | PMID: 35197637
- Version used: **1.0.6.7**
- Evidence: We used REGENIE v1.0.6.7 for association analyses via a two-step procedure as detailed in ref.
- Full pipeline: differential/statistical testing [SAIGE v0.39] -> stage not stated [PLINK, REGENIE v1.0.6.7]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Version used: **3.1.3**
- Evidence: GWAS GWAS analyses for both binary and quantitative traits were carried out with regenie (v3.1.3) 69 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Genotyping, sequencing and analysis of 140,000 adults from Mexico City. (Nature 2023)

- DOI: 10.1038/s41586-023-06595-3 | PMCID: PMC10600010 | PMID: 37821707
- Evidence: Generation of PRS values for BMI To generate source datasets for assessing trans-ancestry portability of BMI PRS, whole genome regression was performed using Regenie ( https://rgcgithub.github.io/regenie/ ) in individuals in the MCPS and in a predominantly European-ancestry cohort from the UK Biobank.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [REGENIE] -> stage not stated [BCFtools, DeepVariant v0.10.0, GATK, WhatsHap]

### Plasma proteomic associations with genetics and health in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06592-6 | PMCID: PMC10567551 | PMID: 37794186
- Version used: **2.2.1**
- Evidence: Genetic association analyses GWAS analyses were performed using REGENIE v.2.2.1 through a two-step procedure to account for population structure detailed previously 59 .
- Full pipeline: machine learning [R] -> stage not stated [PLINK, REGENIE v2.2.1, VEP]

### Genetic links between ovarian ageing, cancer risk and de novo mutation rates. (Nature 2024)

- DOI: 10.1038/s41586-024-07931-x | PMCID: PMC11410666 | PMID: 39261734
- Version used: **2.2.4**
- Evidence: WES sensitivity analysis using REGENIE To replicate the primary findings and account for potential bias that could be introduced by exclusively using one discovery approach, a second analyst independently derived the age at menopause phenotype using a previously published method 78 and conducted additional burden association analysis using the REGENIE regression algorithm (REGENIEv2.2.4; https://g...
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> differential/statistical testing [REGENIE v2.2.4, statsmodels] -> visualisation [pheatmap, tidyverse] -> stage not stated [R v4.1.2]

### Agonist antibody to guanylate cyclase receptor NPR1 regulates vascular tone. (Nature 2024)

- DOI: 10.1038/s41586-024-07903-1 | PMCID: PMC11410649 | PMID: 39261724
- Evidence: Association analyses We estimated associations between protein-altering variants in NPR1 and phenotypes by fitting additive genetic, linear regression models (for quantitative traits; BP and NT-proBNP) or Firth bias-corrected logistic regression models (for binary traits; HF) using REGENIE (v.2+) software 42 .
- Full pipeline: differential/statistical testing [REGENIE] -> structure determination [PHENIX]

### Genomic data in the All of Us Research Program. (Nature 2024)

- DOI: 10.1038/s41586-023-06957-x | PMCID: PMC10937371 | PMID: 38374255
- Evidence: A linear regression was carried out with REGENIE 48 on variants with a minor allele frequency >5%, further adjusting for relatedness to the first five ancestry PCs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [REGENIE] -> stage not stated [Picard]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Version used: **4.1**
- Evidence: In addition, a logistic mixed-effect model adjusted by the same covariates (age, sex, BMI and ten PCs) was implemented by REGENIE (v.4.1) on a related-samples dataset.
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Version used: **3.4.1**
- Evidence: Association analyses and candidate SNV identification We conducted association analyses using REGENIE (v.3.4.1) 48 .
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Parent-of-origin effects on complex traits in up to 236,781 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-09357-5 | PMCID: PMC12527933 | PMID: 40770099
- Version used: **3.2.9**
- Evidence: Association tests To perform GWAS analysis, we used REGENIE (v3.2.9) 38 .
- Full pipeline: quality control [BCFtools v1.8] -> variant calling [PLINK v1.90b] -> dimensionality reduction/clustering [igraph] -> stage not stated [R, REGENIE v3.2.9]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Evidence: Genetic associations using these genetic instruments with CH as the outcome were performed using Firth logistic regression implemented by REGENIE software 101 , assuming an additive effect, adjusted for age, sex and the first 10 genetic principal components.
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### Population-scale repeat expansions elucidate disease risk and brain atrophy. (Nature 2026)

- DOI: 10.1038/s41586-026-10345-6 | PMCID: PMC13190288 | PMID: 41951733
- Version used: **3.2**
- Evidence: Statistical analysis Association analyses between repeat length genotypes and binary phenotypes were performed for the three largest cohorts with ICD-10 based diagnoses (GHS, UKB and Mayo-Clinic) using REGENIE (v.3.2+), which adjusts for relatedness and population structure 65 .
- Full pipeline: variant calling [R, REGENIE v3.2] -> registration [FSL v6.0.7.8] -> differential/statistical testing [REGENIE v3.2] -> stage not stated [FreeSurfer v7.3.2, PLINK, dcm2niix]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Evidence: Applying a high-quality set of common genotyped variants for principal component analysis and for regenie step 1 (Supplementary Note 9 ) led to the exclusion of an additional 180 individuals (Supplementary Note 2 ), leaving n = 403,014 individuals for analyses (UKB EUR cohort).
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### Phenome-wide analysis of copy number variants in 470,727 UK Biobank genomes. (Nature 2026)

- DOI: 10.1038/s41586-025-10087-x | PMCID: PMC13083251 | PMID: 41639462
- Version used: **3.5**
- Evidence: For each of these 237 traits, we repeated CNV variant-level association testing using REGENIE (v.3.5), including age, sex and the first four ancestry principal components as covariates.
- Full pipeline: dimensionality reduction/clustering [REGENIE v3.5] -> differential/statistical testing [PLINK] -> stage not stated [R]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Version used: **3.5**
- Evidence: We then used REGENIE v.3.5 (ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Evidence: We performed burden tests using REGENIE 84 , largely following the procedure previously described 58 , which is based on ref.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### Estimation and mapping of the missing heritability of human phenotypes. (Nature 2026)

- DOI: 10.1038/s41586-025-09720-6 | PMCID: PMC12851931 | PMID: 41225014
- Evidence: GWAS analyses were performed using REGENIE available through GitHub at https://rgcgithub.github.io/regenie/ .
- Full pipeline: variant calling [PLINK] -> dimensionality reduction/clustering [PLINK] -> differential/statistical testing [LDSC] -> stage not stated [R, REGENIE]

### Specificity, length and luck drive gene rankings in association studies. (Nature 2026)

- DOI: 10.1038/s41586-025-09703-7 | PMCID: PMC12823407 | PMID: 41193809
- Evidence: Burden tests were run using REGENIE 59 on inverse rank normal-transformed phenotypes.
- Full pipeline: differential/statistical testing [MAGMA] -> stage not stated [BEDTools, LDSC, REGENIE, VEP]

