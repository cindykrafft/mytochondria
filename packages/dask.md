# Dask

- **Category:** workflow
- **Papers in survey:** 5
- **Journals:** Nature (2), PNAS (2), Cell (1)
- **Years:** 2021 (1), 2023 (2), 2024 (1), 2025 (1)
- **Versions named:** 2022.4.1 (1)
- **Pipeline stages it appears in:** alignment/mapping (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: We used a Dask client to parallelize the grnboost2 version of this step on an AMD Threadripper 2990WX CPU.
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Data analysis was conducted using ALLCools 9 , Xarray 67 and dask 68 packages.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: Methods Overview of software, data and workflow We conducted our LSP mapping workflow using Google Earth Engine (GEE) (v.0.1.404 or later) 65 and performed additional analyses using Python 66 with a set of core scientific packages (numpy 67 , shapely 68 , pandas 69 , geopandas 70 , rasterio 71 , xarray 72 , rasterstats 73 , dask 74 , scipy 75 , scikit-learn 76 , statsmodels 77 and matplotlib 78 ).
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **2022.4.1**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### Highly parallelizable path sampling with minimal rejections using asynchronous replica exchange and infinite swaps. (PNAS 2024)

- DOI: 10.1073/pnas.2318731121 | PMCID: PMC10873605 | PMID: 38315841
- Evidence: We run an in-house ∞ RETIS Python code which mainly consists of PyRETIS ( 17 ) function imports together with the use of the Dask ( 39 ) package which handles scheduling worker tasks.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [Dask]

