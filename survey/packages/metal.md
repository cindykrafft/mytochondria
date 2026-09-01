# METAL

- **Category:** statgen
- **Papers in survey:** 5
- **Journals:** Nature (3), PNAS (2)
- **Years:** 2022 (3), 2023 (1), 2024 (1)
- **Versions named:** 3.0 (1)

## Papers

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **3.0**
- Evidence: Z -scores were initially calculated using METAL (v.3.0) 71 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Evidence: Multi-ancestry meta-analysis We performed a meta-analysis across all ancestries using an inverse-variance weighting method and control for population stratification for each separate analysis in the METAL software 46 .
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Evidence: Meta-analyses All meta-analyses across studies were performed using a fixed-effect inverse-variance weighting method and control for population stratification in the METAL software 23 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Genetics, leadership position, and well-being: An investigation with a large-scale GWAS. (PNAS 2022)

- DOI: 10.1073/pnas.2114271119 | PMCID: PMC8944770 | PMID: 35286190
- Evidence: We meta-analyzed results from both discovery and replication samples using the inverse-variance weighted fixed-effects model with METAL software ( https://genome.sph.umich.edu/wiki/METAL ).
- Full pipeline: alignment/mapping [ANNOVAR] -> differential/statistical testing [LDSC v1.0.1] -> stage not stated [METAL, PLINK v1.07]

### Genetic risk factors for Mesoamerican nephropathy. (PNAS 2024)

- DOI: 10.1073/pnas.2404848121 | PMCID: PMC11626114 | PMID: 39585978
- Evidence: Joint analysis of the discovery and replication sets using METAL software ( 17 ) revealed the lead OPCML SNP was associated with MeN at P = 4 × 10 −8 (2.9% in cases and 0.005% in controls: Table 2 and SI Appendix , Fig.
- Full pipeline: variant calling [Beagle, Picard] -> visualisation [ggplot2] -> stage not stated [METAL]

