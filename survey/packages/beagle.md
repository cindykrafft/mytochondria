# Beagle

- **Category:** statgen
- **Papers in survey:** 6
- **Journals:** Nature (5), PNAS (1)
- **Years:** 2022 (2), 2024 (3), 2025 (1)
- **Versions named:** 5.1 (2)
- **Pipeline stages it appears in:** variant calling (4), differential/statistical testing (1)

## Papers

### Signatures of copy number alterations in human cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-04738-6 | PMCID: PMC9242861 | PMID: 35705804
- Version used: **5.1**
- Evidence: We then provide ASCAT.sc with the available matched-normal germline sample and generate phased germline SNPs using Beagle (v.5.1) 71 as part of the subclonal copy number calling pipeline, Battenberg 72 .
- Full pipeline: normalisation [RSEM] -> stage not stated [Beagle v5.1, ComplexHeatmap, R, ggplot2, survival (R), tidyverse]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Evidence: Missing genotypes were imputed with Beagle (v.40) 55 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Evidence: Population LD-based haplotype analysis First, the SNP dataset 2 was phased by Beagle (v 21Apr21.304) 51 .
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Version used: **5.1**
- Evidence: Statistical phasing and imputation were performed using Beagle v.5.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: For population LD-based haplotype analysis, the filtered SNPs were phased using Beagle (v.21Apr21.304) 70 .
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Genetic risk factors for Mesoamerican nephropathy. (PNAS 2024)

- DOI: 10.1073/pnas.2404848121 | PMCID: PMC11626114 | PMID: 39585978
- Evidence: RFmix requires phased data without missing genotypes: We implemented Beagle (v.4) to phase and impute sporadically missing ( 50 ) genotypes in a combined dataset of MeN and HGDP.
- Full pipeline: variant calling [Beagle, Picard] -> visualisation [ggplot2] -> stage not stated [METAL]

