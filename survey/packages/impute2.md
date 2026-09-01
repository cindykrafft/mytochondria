# IMPUTE2

- **Category:** statgen
- **Papers in survey:** 12
- **Journals:** Nature (7), Cell (3), PNAS (2)
- **Years:** 2021 (2), 2022 (4), 2023 (3), 2025 (2), 2026 (1)
- **Versions named:** 2.3.2 (2), 2.3.1 (1)
- **Pipeline stages it appears in:** variant calling (4), quality control (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Evidence: After sample and SNP quality control (QC) of the directly-typed genotypes, resulting in 670,739 autosomal markers in 487,442 individuals, data were prephased using SHAPEIT3 ( O’Connell et al., 2016 ) and imputed using the IMPUTE4 program ( https://jmarchini.org/software/ ).
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### Characterizing genetic intra-tumor heterogeneity across 2,658 human cancer genomes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.009 | PMCID: PMC8054914 | PMID: 33831375
- Evidence: To improve sensitivity for the detection of genomic imbalances, SNPs in the matched normal are phased with IMPUTE2 ( Howie et al., 2009 ).
- Full pipeline: quantification [SAMtools] -> stage not stated [GSEA, IMPUTE2, Mutect2, R, fgsea]

### Limb development genes underlie variation in human fingerprint patterns. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.008 | PMCID: PMC8740935 | PMID: 34995520
- Evidence: ...PLINK v1.9 Purcell et al., 2007 https://www.cog-genomics.org/plink2 ; RRID: N/A SHAPEIT Delaneau et al., 2011 http://www.shapeitforum.com ; RRID: N/A IMPUTE2 Howie et al., 2009 https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ; RRID: SCR_013055 EIGENSOFT Price et al., 2006 https://data.broadinstitute.org/alkesgroup/EIGENSOFT/ ; RRID: SCR_004965 qqman v0.1.4 Turner, 2014 https://cran.r-project....
- Full pipeline: stage not stated [Cytoscape, GCTA, IMPUTE2, ImageJ, PLINK v1.9, R v3.6, SHAPEIT]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: ...DSC, https://github.com/immunogenomics/cov-ldsc ; EAGLE, https://alkesgroup.broadinstitute.org/Eagle/ ; GCTA, http://cnsgenomics.com/software/gcta/ ; IMPUTE2, https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ; LDpred, https://github.com/bvilhjal/ldpred/ ; LDSC, https://github.com/bulik/ldsc/ ; MEMO (rareGWAMA), https://github.com/dajiangliu/rareGWAMA/ ; Minimac3, https://genome.sph.umich.edu/w...
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Evidence: These weights along with allele probabilities for each haplotype in the haplotype reference panel allow imputation with a Li and Stephens 66 model similar to the one used in IMPUTE2 (ref.
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **2.3.1**
- Evidence: ...ct Predictor (release 100, https://github.com/Ensembl/ensembl-vep ), BOLT-LMM (v2.1, https://data.broadinstitute.org/alkesgroup/BOLT-LMM/downloads ), IMPUTE2 (v2.3.1, https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ), dbSNP (v140, https://www.ncbi.nlm.nih.gov/SNP ), BiNGO (v3.0.3, https://www.psb.ugent.be/cbd/papers/BiNGO/Download.html ), Cytoscape (v3.7.1, https://cytoscape.org/download.html...
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Version used: **2.3.2**
- Evidence: For the RCC cohort alone, given that this cohort was a subset of the much larger GPC cohort ( n = 4,778) including HIV uninfected individuals, pre-phasing with SHAPEIT2 (v.2.12) 53 was performed to maximize phasing accuracy, after which imputation was performed using IMPUTE2 (v.2.3.2) 54 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Version used: **2.3.2**
- Evidence: SHAPEIT 58 (v.2.r900) was used to infer haplotypes, and imputation was done in IMPUTE2 (v.2.3.2) 59 using a 1,000 genomes reference panel phase 3 (all ancestries).
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Evidence: We then imputed the MEGA-chip data with IMPUTE2 (refs.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### A cross-population compendium of gene-environment interactions. (Nature 2026)

- DOI: 10.1038/s41586-025-10054-6 | PMCID: PMC12999510 | PMID: 41606330
- Evidence: The genotypes were then imputed by IMPUTE4 software using a combination reference panel of the Haplotype Reference Consortium, UK10K and 1000 Genomes Project Phase 3.
- Full pipeline: variant calling [IMPUTE2] -> dimensionality reduction/clustering [R, Seurat v4.3.0.1, UMAP] -> differential/statistical testing [MAGMA] -> stage not stated [BCFtools, LDSC v1.0.0, PLINK v2.00a]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: GWAS data were imputed into 1000 Genomes Phase 3 variants using SHAPEIT2 ( 54 ) and IMPUTE2 ( 55 ).
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### The impact of COVID-19 on a college freshman sample reveals genetic and nongenetic forms of susceptibility and resilience to stress. (PNAS 2023)

- DOI: 10.1073/pnas.2305779120 | PMCID: PMC10710019 | PMID: 38011555
- Evidence: The data were imputed using Minimac 4 on the Michigan Imputation Server ( https://imputationserver.sph.umich.edu/index.html ) ( 10 ).
- Full pipeline: quality control [PLINK] -> variant calling [PLINK] -> differential/statistical testing [R v4.2] -> stage not stated [IMPUTE2]

