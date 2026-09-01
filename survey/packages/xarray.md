# xarray

- **Category:** general
- **Papers in survey:** 7
- **Journals:** Nature (5), Cell (2)
- **Years:** 2021 (1), 2022 (1), 2023 (2), 2024 (2), 2025 (1)
- **Versions named:** 2023.6.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (1), differential/statistical testing (1)

## Papers

### High-resolution profiling of pathways of escape for SARS-CoV-2 spike-binding antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.045 | PMCID: PMC8096189 | PMID: 34010620
- Evidence: ...https://www.nextflow.io/ Bowtie https://quay.io/biocontainers/bowtie:1.2.2%5fpy36h2d50403_1 phippery Matsen Lab https://github.com/matsengrp/phippery xarray http://xarray.pydata.org/en/stable/ SAMtools https://quay.io/biocontainers/samtools:1.3%5fh0592bc0_3 R (version 4.0.2) https://www.R-project.org/ tidyverse https://www.tidyverse.org/ ggpubr https://github.com/kassambara/ggpubr corrr https://gi...
- Full pipeline: stage not stated [Clustal Omega, Nextflow, R v4.0.2, SAMtools, ggpubr, tidyverse, xarray]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Python packages used for spatial enrichment analysis and collagen morphometrics were sckikit-image, pandas, numpy, xarray, scipy, statsmodels.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Accurate medium-range global weather forecasting with 3D neural networks. (Nature 2023)

- DOI: 10.1038/s41586-023-06185-3 | PMCID: PMC10356604 | PMID: 37407823
- Evidence: The computation of the CRPS metric relied on the xskillscore Python package, https://github.com/xarray-contrib/xskillscore/ .
- Full pipeline: machine learning [PyTorch] -> visualisation [Matplotlib] -> stage not stated [NumPy, xarray]

### Tropical deforestation causes large reductions in observed precipitation. (Nature 2023)

- DOI: 10.1038/s41586-022-05690-1 | PMCID: PMC9995269 | PMID: 36859548
- Evidence: Data were obtained as monthly means or converted to monthly mean using the Python package xarray 52 .
- Full pipeline: stage not stated [Cartopy, seaborn, xarray]

### Central pattern generator control of a vertebrate ultradian sleep rhythm. (Nature 2024)

- DOI: 10.1038/s41586-024-08162-w | PMCID: PMC11655359 | PMID: 39506115
- Version used: **2023.6.0**
- Evidence: Statistics The data were processed using Python (v.3.11.5) and the standard Python packages numpy (v.1.24.3) and xarray (v.2023.6.0).
- Full pipeline: differential/statistical testing [pandas v2.0.3, xarray v2023.6.0] -> stage not stated [DeepLabCut, NumPy, Python, SciPy]

### Future increase in extreme El Niño supported by past glacial changes. (Nature 2024)

- DOI: 10.1038/s41586-024-07984-y | PMCID: PMC11464383 | PMID: 39322673
- Evidence: Code availability Open-sourced Python code was used to create the figures, perform the analyses and all calculations, including the following modules and their required dependencies: matplotlib 78 , pandas 79 , NumPy 80 , seaborn 81 , xarray 82 , cartopy 83 and SciPy 84 .
- Full pipeline: simulation/modelling [CESM v1.2] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn, xarray]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: Methods Overview of software, data and workflow We conducted our LSP mapping workflow using Google Earth Engine (GEE) (v.0.1.404 or later) 65 and performed additional analyses using Python 66 with a set of core scientific packages (numpy 67 , shapely 68 , pandas 69 , geopandas 70 , rasterio 71 , xarray 72 , rasterstats 73 , dask 74 , scipy 75 , scikit-learn 76 , statsmodels 77 and matplotlib 78 ).
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

