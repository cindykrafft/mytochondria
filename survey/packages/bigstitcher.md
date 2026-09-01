# BigStitcher

- **Category:** imaging
- **Papers in survey:** 8
- **Journals:** Nature (4), Science (2), PNAS (1), Cell (1)
- **Years:** 2021 (1), 2023 (1), 2024 (1), 2025 (5)
- **Pipeline stages it appears in:** structure determination (1), alignment/mapping (1), registration (1), visualisation (1)

## Papers

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: For image data visualization, the MoBIE viewer uses BigDataViewer (BDV) ( Pietzsch et al., 2015 ).
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### A gut sense for a microbial pattern regulates feeding. (Nature 2025)

- DOI: 10.1038/s41586-025-09301-7 | PMCID: PMC12443592 | PMID: 40702192
- Evidence: In brief, tdTomato + neurons visible in both RNAscope sections and in vivo planes were identified as landmark reference points and were manually paired using the BigWarp tool within the Fiji BigDataViewer plugin.
- Full pipeline: alignment/mapping [featureCounts] -> stage not stated [BigStitcher, DESeq2, ImageJ]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: All images were processed using Fiji and the BigDataViewer plugin 54 , 55 .
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Light-microscopy-based connectomic reconstruction of mammalian brain tissue. (Nature 2025)

- DOI: 10.1038/s41586-025-08985-1 | PMCID: PMC12158774 | PMID: 40335689
- Evidence: We then used a BigStitcher-based Fiji macro to concatenate the data and convert to n5 format.
- Full pipeline: machine learning [PyTorch v1.12.1] -> stage not stated [BigStitcher, Jupyter, NumPy, Python v3.8, SciPy, scikit-image, seaborn]

### Connectome-driven neural inventory of a complete visual system. (Nature 2025)

- DOI: 10.1038/s41586-025-08746-0 | PMCID: PMC12119369 | PMID: 40140576
- Evidence: The surfaces of the slabs were automatically identified using a combination of a hand-engineered 67 and machine-learning-based cost estimation 63 before graph-cut computation 63 , 67 , followed by manual refinements using a custom tool based on BigDataViewer 68 to correct remaining issues interactively.
- Full pipeline: dimensionality reduction/clustering [Python, SciPy] -> structure determination [BigStitcher] -> stage not stated [Jupyter, NumPy, Snakemake]

### V2a neurons restore diaphragm function in mice following spinal cord injury. (PNAS 2024)

- DOI: 10.1073/pnas.2313594121 | PMCID: PMC10945804 | PMID: 38442182
- Evidence: Multiple images spanning the length of the cervical region of the spinal cord were acquired and stitched together using Imaris Stitcher software (BitPlane) or the FIJI BigStitcher plugin.
- Full pipeline: stage not stated [BigStitcher, ImageJ]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: The BigStitcher software ( 72 ) was then used to stitch the transformed tiles together and the final stitched image exported for further analysis.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Deep-tissue transcriptomics and subcellular imaging at high spatial resolution. (Science 2025)

- DOI: 10.1126/science.adq2084 | PMCID: PMC12005972 | PMID: 39977545
- Evidence: Image processing and analysis Large multi-tile images were stitched using BigStitcher ( 20 ) and aligned with bigstream-based image registration ( 15 ).
- Full pipeline: alignment/mapping [BigStitcher] -> registration [BigStitcher, Nextflow] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose]

