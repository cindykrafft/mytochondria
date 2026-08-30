# pandas

- **Category:** general
- **Papers in survey:** 22
- **Journals:** Nature (19), PNAS (2), Cell (1)
- **Years:** 2021 (2), 2022 (2), 2023 (2), 2024 (5), 2025 (7), 2026 (4)
- **Versions named:** 2.0.3 (2), 1.5.3 (2), 1.5.1 (2), 1.0.1 (1), 2.2.3 (1), 2.1.4 (1), 1.1.5 (1), 2.0.0 (1), 2.0.1 (1), 1.2.3 (1)
- **Pipeline stages it appears in:** differential/statistical testing (3), visualisation (2), quality control (2), normalisation (1), alignment/mapping (1)

## Papers

### Microbial exposure during early human development primes fetal immune cells. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.039 | PMCID: PMC8240556 | PMID: 34077752
- Evidence: A curated pandas Python library version v0.25.3 was used to extract and align the OTU reads.
- Full pipeline: alignment/mapping [pandas] -> dimensionality reduction/clustering [QIIME 2 v1.8.0, R v4.4, UMAP] -> stage not stated [ImageJ, Matplotlib v3.2.1, NumPy v1.19.4, Python v2.7.0, seaborn v0.9.0]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Version used: **1.1.2**
- Evidence: The 10x Genomics V(D)J Ig heavy and light chains were processed using cellranger vdj v.3.1.0 and the reference cellranger-vdj-GRCh38-alts-ensembl-3.1.0 with default settings. scRNA-seq quality control and processing of 10x sequencing data Pandas (v.1.1.2), NumPy (v.0.25.2), Anndata (v.0.6.19), ScanPy (v.1.4) and Python (v.3) were used to pool single-cell counts and for downstream analyses.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Version used: **1.3.0**
- Evidence: Data analysis software The following data analysis software was used: Python (v.3.9) with NumPy (v.1.21.0), Scipy (v.1.7.0), MatplotLib (v.3.4.2), Pandas (v.1.3.0) and additional packages (full python environments are available with our code on bitbucket); Ants (v.1.9); Suite2p (v.0.9.3); and ImageJ (v.1.53c).
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Version used: **1.3.5**
- Evidence: Python (v.3), Pandas (v.1.3.5), NumPy (v.1.21.5), Matplotlib (v.3.5.2) and Scanpy (v.1.8.2 and v.1.9.1) were used for quality control and downstream processing.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Version used: **0.25.1**
- Evidence: Numpy (v.1.17.2) and Pandas (v.0.25.1) were used for array and data frame operations, respectively.
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Central pattern generator control of a vertebrate ultradian sleep rhythm. (Nature 2024)

- DOI: 10.1038/s41586-024-08162-w | PMCID: PMC11655359 | PMID: 39506115
- Version used: **2.0.3**
- Evidence: Statistical tests were performed using the standard Python packages scipy (v.1.11.4) and pandas (v.2.0.3).
- Full pipeline: differential/statistical testing [pandas v2.0.3, xarray v2023.6.0] -> stage not stated [DeepLabCut, NumPy, Python, SciPy]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **2.0.1**
- Evidence: Heat maps and bar graphs illustrating differential gene expression were constructed in a Python environment (detailed in next paragraph). scRNA-sequencing Analysis and visualization of the data were conducted in a Python environment built on Pandas (v.2.0.1), NumPy (v.1.24.2) 73 , SciPy (v.1.10.1) 74 , scikit-learn (v.1.2.0), SCANPY (v1.9.3) 75 , AnnData (v.0.9.1) 75 , matplotlib (v.3.7.1) 76 and ...
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Data wrangling was done with the pandas library in Python and tidyverse library in R.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Version used: **1.2.3**
- Evidence: 0.7.5), Pandas (v.1.2.3), NumPy (v.1.20.1), and Python (v.3) were used to pool single-cell counts and conduct downstream analysis.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.0.5**
- Evidence: DGE matrices were processed using the following R and python packages: Seurat (v.3.2.2) 64 , SeuratDisk (v.0.0.0.9010) 65 , anndata (v.0.8.0) 66 , numpy (v.1.17.5) 67 , pandas (v.1.0.5) 68 , 69 and Scanpy (v.1.9.1) 70 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Version used: **2.1.4**
- Evidence: Numerical computations and data handling were conducted using NumPy 84 (v.1.26.4) and Pandas (v.2.1.4, NumFOCUS).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **1.1.5**
- Evidence: For data visualization, dot plots, sina plots, violin plots, line plots, bar plots, box plots, heatmaps, pie charts, interaction plots, error bars and contour figures were generated using the following Python, R and Matlab packages: Python: pandas (v.1.1.5), numpy (v.1.19.3), anndata (v.0.7.4), scanpy (v.1.6.0), matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R p...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **2.0.0**
- Evidence: Python packages such as Scanpy (v.1.9.5), Pandas (v.2.0.0), Statsmodels (v.0.14.0), NumPy (v.1.24.2), Scipy (v.1.10.1), Matplotlib (v.3.8.0), Seaborn (v.0.11.2) and Sklearn (v.1.3.2), were used for data analysis.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **1.5.3**
- Evidence: SL-Smart-seq3xpress data analysis Count matrices were processed with JupyterLab (v.4) notebooks using IPython (v.7.31) using the following modules: pandas (v.1.5.3), numpy (v.1.23.5), scipy (v.1.10.1), scanpy (v.1.7.2), openpyxl (v.3.1.2), matplotlib (v.3.6.3) and seaborn (v.0.12.2).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Version used: **1.5.1**
- Evidence: We analysed data using Python (v.3.9.12) with Biopython (v.1.78), Pandas (v.1.5.1) and NumPy (v.1.23.4).
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **1.5.1**
- Evidence: Data analysis was performed using Python (v.3.9.12) with Biopython (v.1.78), Pandas (v.1.5.1), SciPy package (v.1.10.0) and NumPy (v.1.23.4). sgRNA enrichment was calculated as previously described 52 , 69 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Version used: **2.0.3**
- Evidence: All behavioural and neural analyses were performed using custom-written Python (v.3.8) code unless otherwise noted, incorporating the analysis and plotting libraries numpy (v.1.24.3), scipy (v.1.10.1), scikit-learn (v.1.3.0), pandas (v.2.0.3), seaborn (v.0.12.2), elephant (v.1.0.0) and statsmodels (v.0.14.0).
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **1.5.3**
- Evidence: Single-cell sequencing and pseudobulk analyses Single-cell RNA-seq datasets from multiple human tissues were processed for tissue-specific pseudobulk analysis using Python (v.3.9.12) with Scanpy (v.1.9.3), Pandas (v.1.5.3) and Numpy (v.1.24.4).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **1.0.1**
- Evidence: Standard packages such as numpy (v.1.21.5), pandas (v.1.0.1) and scipy (v.1.4.1) were correspondingly used for data handling, processing, normalization, statistical calculations and/or data fitting.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Version used: **2.2.3**
- Evidence: Value files were imported into Python (v.3.12) using Pandas (v.2.2.3).
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### COVID-19, climate change, and the finite pool of worry in 2019 to 2021 Twitter discussions. (PNAS 2022)

- DOI: 10.1073/pnas.2210988119 | PMCID: PMC9618108 | PMID: 36251993
- Evidence: Daily, monthly, and annual cases were created by aggregating the data using the pandas Python library ( https://pandas.pydata.org/ ).
- Full pipeline: stage not stated [pandas]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Evidence: For each candidate SNP, we computed the Spearman correlation coefficient with breed ancestry in python using the pandas library corr method ( 114 ) for all 101 breeds ( Dataset S4 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

