# Rcpp

- **Category:** general
- **Papers in survey:** 6
- **Journals:** Nature (4), PNAS (2)
- **Years:** 2021 (2), 2023 (1), 2024 (2), 2025 (1)
- **Pipeline stages it appears in:** differential/statistical testing (2), variant calling (1), dimensionality reduction/clustering (1)

## Papers

### The origins and spread of domestic horses from the Western Eurasian steppes. (Nature 2021)

- DOI: 10.1038/s41586-021-04018-9 | PMCID: PMC8550961 | PMID: 34671162
- Evidence: Struct-f4 is implemented in Rcpp and only takes the full set of f 4 -statistics as input to automatically return individual ancestry coefficients, without requiring pre-defined, ad-hoc sets of reference and test populations.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [Rcpp] -> structure determination [RAxML] -> stage not stated [ANGSD, R]

### Sympathetic cooling of a trapped proton mediated by an LC circuit. (Nature 2021)

- DOI: 10.1038/s41586-021-03784-w | PMCID: PMC8387233 | PMID: 34433946
- Evidence: Data preparation and analysis are performed in R 46 , while the intensive part of the calculation is performed using C++ via the Rcpp-package 47 .
- Full pipeline: stage not stated [Rcpp]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Evidence: We also rewrote the inner loops of the most time-intensive functions (choose_sigma_c and fitPixels) with Rcpp 82 for efficiency.
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Evidence: The mixed-model logistic regression method SAIGE (R package developed with Rcpp for genome-wide association tests in large-scale datasets and biobanks) was used for association analysis and included the following covariates in the model: sex, age, genotyping batch and ten principle components.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### Predicting resilience of migratory birds to environmental change. (PNAS 2024)

- DOI: 10.1073/pnas.2311146121 | PMCID: PMC11087779 | PMID: 38648469
- Evidence: All analyses were done in R [Version 4.1, R Core Team ( 75 )], with integration of C++ code using the R package Rcpp ( 76 ).
- Full pipeline: stage not stated [R, Rcpp]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Evidence: We inferred clusters and individual ancestry proportions using the Struct-f4 Rcpp package ( 23 ) for all populations between K = 1 and K = 5.
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

