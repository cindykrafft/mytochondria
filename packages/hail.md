# Hail

- **Category:** statgen
- **Papers in survey:** 1
- **Journals:** Nature (1)
- **Years:** 2026 (1)
- **Versions named:** 0.1 (1)
- **Pipeline stages it appears in:** quality control (1)

## Papers

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Version used: **0.1**
- Evidence: Next, we did thorough, multiple-round quality checks on the samples and the genetic variations using Hail 0.1.
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

