# COLOC

- **Category:** statgen
- **Papers in survey:** 3
- **Journals:** Nature (2), PNAS (1)
- **Years:** 2022 (1), 2023 (1), 2025 (1)
- **Versions named:** 5.2.3 (1)
- **Pipeline stages it appears in:** differential/statistical testing (1)

## Papers

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Evidence: Colocalization analysis Significant genes from the TWAS, splicing TWAS, metaTWAS and splicing metaTWAS, as well as genes for which one of the top variants was a significant eQTL or sQTL, were selected for a colocalization analysis using the coloc R package 56 .
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Evidence: Colocalization Significant genes in the TWAS and metaTWAS were selected for a colocalization analysis using the coloc R package.
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Multiomics integration prioritizes potential drug targets for multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2425537122 | PMCID: PMC12232717 | PMID: 40577117
- Version used: **5.2.3**
- Evidence: To further address the potential effects of LD on the pleiotropic associations, Bayesian colocalization analysis was performed to assess the posterior probability of shared genetic variants being responsible for both protein expression and MS development using the coloc R package (version 5.2.3).
- Full pipeline: differential/statistical testing [COLOC v5.2.3, R] -> stage not stated [TwoSampleMR, edgeR]

