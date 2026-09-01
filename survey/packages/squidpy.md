# Squidpy

- **Category:** single-cell
- **Papers in survey:** 19
- **Journals:** Nature (15), Science (2), PNAS (2)
- **Years:** 2022 (1), 2023 (3), 2024 (2), 2025 (9), 2026 (4)
- **Versions named:** 1.1.2 (2), 1.2.3 (1), 1.3.0 (1), 1.6.2 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (5), quantification (2), quality control (2), normalisation (2), visualisation (2), structure determination (1), alignment/mapping (1)

## Papers

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **1.1.2**
- Evidence: ....6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-image 0.18.1, squidpy 1.1.2, anndata 0.8.0 and itertools 8.0.0.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: These are not new approaches and many packages have emerged for integrating these clustering algorithms into libraries such as Squidpy 75 .
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### Spatially clustered type I interferon responses at injury borderzones. (Nature 2024)

- DOI: 10.1038/s41586-024-07806-1 | PMCID: PMC11374671 | PMID: 39198639
- Evidence: Quality control, normalization and integration for RNA MERFISH Data analysis of RNA MERFISH data was performed with single-cell sequencing analysis tools such as Scanpy and Squidpy 53 , 54 .
- Full pipeline: quality control [Scanpy, Squidpy] -> normalisation [ImageJ, Scanpy, Seurat, Squidpy] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose, R, SoupX]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: For each spot, the area occupied by nuclei was calculated using Squidpy 55 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: For quality control and filtering, we used Squidpy 33 (v1.6.1), a tool for analyzing spatial single-cell data, to create a UMAP embedding for each sample.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: ...KiloSort 9 and MountainSort 10 ), label-free behavioural tracking (DeepLabCut 11 , MoSeq 12 and SLEAP 13 ) and spatial transcriptomics (Giotto 14 and Squidpy 15 ), the goal of NEURD is to make ‘big neuroscience data’ (in this case, large-scale electron microscopy reconstructions) accessible to a larger community.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: ( a ) and an aggregated network format in which edges between nodes represent a normalized Squidpy interaction score lying above a 0.1 threshold (10% of the connections) ( b ).
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: To facilitate further downstream analyses of mapped spatial data, moscot.space.mapping interfaces with squidpy 81 , a spatial analysis toolkit that contains various visualization and testing capabilities.
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Version used: **1.2.3**
- Evidence: Neighbourhood enrichment and intercellular communication modelling To evaluate the spatial proximity of cell types in each sample, we obtained a neighbourhood enrichment z -score using the nhood_enrichment function from Squidpy (v.1.2.3) 63 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Version used: **1.3.0**
- Evidence: Analysis of the spatial transcriptomics datasets We analysed spot gene expression in Visium data using Scanpy v1.9.3 and Squidpy v1.3.0.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: To compute the distribution of nearest neighbour distances, we constructed a triangulation mesh graph connecting neighbouring cells on a given sample using squidpy.gr.spatial_neighbors with delaunay=True 103 .
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: The expression matrix and metadata from each CosMx run was exported from the AtoMx platform and was converted to a Python object using squidpy.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: To assess the effects of DSC subtypes on neighbouring EVTs, iScores of EVTs in direct spatial proximity to annotated DSC subtypes (within five neighbouring tiles on grids, by Squidpy 75 ) were analysed and compared with depth-matched EVTs that were not in spatial proximity to any DSCs.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: We used the Squidpy 74 integration of CellPhoneDB 75 and Omnipath 76 to identify shifts in receptor–ligand interactions at each time point.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: The resulting spot-by-transcript abundance matrix was analysed using the package squidpy.
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### A cellular and molecular spatial atlas of dystrophic muscle. (PNAS 2023)

- DOI: 10.1073/pnas.2221249120 | PMCID: PMC10629561 | PMID: 37410813
- Evidence: To compute the neighborhood enrichment between each MDX cluster, nhood_enrichment function in Squidpy was used with its default parameter ( 25 ).
- Full pipeline: quantification [Python] -> normalisation [Seurat] -> dimensionality reduction/clustering [Python, R, Seurat, Squidpy, UMAP] -> differential/statistical testing [R] -> visualisation [UMAP]

### A spatiotemporal molecular atlas of the ovulating mouse ovary. (PNAS 2024)

- DOI: 10.1073/pnas.2317418121 | PMCID: PMC10835069 | PMID: 38252830
- Evidence: Individual Slide-seq datasets were read using the squidpy ( 56 ) package (v1.2.3) and visualized in the interactive Napari image viewer ( 57 ) (v0.4.15).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SCENIC, scikit-learn] -> visualisation [Squidpy] -> stage not stated [AnnData, CellPhoneDB, Scanpy]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Version used: **1.1.2**
- Evidence: To annotate cortex and medulla from histology images, we extracted image features from the high resolution images of H&E staining using the python package squidpy (v1.1.2) ( 97 ) and performed Leiden clustering on image features.
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### High-resolution spatial mapping of cell state and lineage dynamics in vivo with PEtracer. (Science 2025)

- DOI: 10.1126/science.adx3800 | PMCID: PMC12766569 | PMID: 40705858
- Version used: **1.6.2**
- Evidence: Cell type neighborhood enrichment and density analysis Cell neighborhood enrichment analysis was performed using Squidpy (v1.6.2).
- Full pipeline: alignment/mapping [Python, scikit-image v0.24.0] -> normalisation [Scanpy v1.10.0] -> dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> stage not stated [Cellpose v3.1.0, R v4.2.3, Seurat, Squidpy v1.6.2, scDblFinder]

