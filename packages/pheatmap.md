# pheatmap

- **Category:** general
- **Papers in survey:** 167
- **Journals:** PNAS (84), Nature (67), Cell (15), Science (1)
- **Years:** 2021 (18), 2022 (32), 2023 (22), 2024 (37), 2025 (41), 2026 (17)
- **Versions named:** 1.0.12 (40)
- **Pipeline stages it appears in:** visualisation (52), dimensionality reduction/clustering (35), normalisation (17), differential/statistical testing (13), quantification (8), alignment/mapping (2), variant calling (1), structure determination (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **1.0.12**
- Evidence: ...b/packages/readr/index.html R package ggalluvial version 0.12.2 Brunson, 2020 https://cran.r-project.org/web/packages/ggalluvial/index.html R package pheatmap version 1.0.12 Raivo, 2019 https://cran.r-project.org/web/packages/pheatmap/index.html R package httr version 1.4.2 Wickham, 2020a https://cran.r-project.org/web/packages/httr/index.html R package jsonlite version 1.7.1 Ooms, 2014 https://cr...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: Supervised clustering of gene expression was performed with pheatmap (version2012) using Ward’s minimum variance method ( Murtagh and Legendre, 2014 ).
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Evidence: Throughout the manuscript we have visualized enrichments for specific genes using heatmaps–rectangular heatmaps (e.g., in Figure 4 ) were visualized using R package `pheatmap` while circular heatmaps (e.g., in Figure 7 ) were visualized using R package `RCircos`.
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **1.0.12**
- Evidence: ...es/release/bioc/html/clusterProfiler.html R package ggplot2 version 3.3.2 R CRAN https://cran.r-project.org/web/packages/ggplot2/index.html R package pheatmap version 1.0.12 R CRAN https://cran.r-project.org/web/packages/pheatmap/index.html R package ggraph version 2.0.3 R CRAN https://cran.r-project.org/web/packages/ggraph/index.html R package igraph version 1.2.4.2 R CRAN https://cran.r-project....
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Dynamic 3D proteomes reveal protein functional alterations at high resolution in situ. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.021 | PMCID: PMC7836100 | PMID: 33357446
- Evidence: The heatmap was generated using the pheatmap package (version 1.0.12) and was also based on consistently identified modified peptide sequences.
- Full pipeline: differential/statistical testing [SciPy, limma] -> stage not stated [AutoDock Vina v1.1.2, Bioconductor, NAMD v2.13, PyMOL v2.4, Python, R, pheatmap, seaborn]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **1.0.12**
- Evidence: VennDiagram 1.6.20, pheatmap 1.0.12, ggforce 0.3.3, ggpubr 0.4.0, RColorBrewer 1.1-2, proxy 0.4-26, reshape2 1.4.4, stringr 1.4.0, dplyr 1.0.7, purrr 0.3.4, readr 1.4.0, tidyr 1.1.3, tidyverse 1.3.1.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **1.0.12**
- Evidence: Graphics were generated using the ggplot2 3.3.3 ( Wickham, 2009 ), ComplexHeatmap 2.4.3 ( Gu et al., 2016 ), pheatmap 1.0.12 ( Kolde, 2019 ), igraph 1.2.6 ( Csardi and Nepusz, 2006 ), RCy3 2.8.1 ( Gustavsen et al., 2019 ), stringr 1.4.0 ( Wickham, 2019 ), dplyr 1.0.6 ( Wickham et al., 2020 ), and RColorBrewer 1.1-2 ( Neuwirth, 2014 ) R package.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Post-gastrulation synthetic embryos generated ex utero from mouse naive ESCs. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.028 | PMCID: PMC9439721 | PMID: 35988542
- Evidence: Expression heatmap was generated using R pheatmap package.
- Full pipeline: alignment/mapping [STAR v2.4.2a] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, R, Seurat, pheatmap]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: Heatmaps were generated using R function pheatmap().
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: ...https://bioconductor.org/packages/release/bioc/html/scater.html BioMart N/A https://www.ensembl.org/biomart/martview/3e2c65a5e3f783f8c9e5d648e4b64126 pheatmap R package N/A https://rdrr.io/cran/pheatmap/ ggplot2 ( Wickham 2016 ) https://ggplot2.tidyverse.org Scanpy ( Wolf et al., 2018 ) https://scanpy.readthedocs.io/en/stable/ PyTorch N/A https://pytorch.org TotalVI ( Gayoso et al., 2021 ) https:/...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: Data visualization All the graphical visualization of the data was performed in R with the ggplot2 package with the exception of the heatmaps, which were displayed using the pheatmap library Box plots: Box plots are calculated in the style of Tukey, shortly the center of the box represents the median of the values, the hinges the 25th and 75th percentile and the whiskers are extended no further th...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Data visualization and plots were generated in R with ggplot and pheatmap packages, in GraphPad Prism, and in Python using the scikitimage, matplotlib, and seaborn packages.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 50 https://bioconductor.org/packages/release/bioc/html/limma.html pheatmap R Kolde 51 https://www.rdocumentation.org/packages/pheatmap/versions/1.0.12/topics/pheatmap Prism 10 GraphPad software https://www.graphpad.com/scientific-software/prism RSEM tool Li and Dewey 52 https://deweylab.github.io/RSEM/ scVelo Bergen et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: The coefficient p values and log 2 (odds ratio) were obtained from the generalized quasi-binomial linear model and visualized using the pheatmap R package (v.1.0.12).
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Design principles of cell-state-specific enhancers in hematopoiesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.017 | PMCID: PMC12173716 | PMID: 40345201
- Evidence: All other plots were created with the ggplot2 or pheatmap packages in R.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ArchR] -> machine learning [TensorFlow] -> stage not stated [R, ggplot2, kallisto, pheatmap]

### Transcriptional programs of neoantigen-specific TIL in anti-PD-1-treated lung cancers. (Nature 2021)

- DOI: 10.1038/s41586-021-03752-4 | PMCID: PMC8338555 | PMID: 34290408
- Evidence: Top ranked DEGs (by log-fold changes) with a log 2 -fold changes >0.8 and DEGs relating to T cell function were extracted for further visualization in a heat map using pheatmap package.
- Full pipeline: alignment/mapping [velocyto] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [velocyto] -> structure determination [UMAP] -> visualisation [pheatmap]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: Most of the statistical analysis and data visualization were performed in R using the packages tidyverse, ggplot2, purrr, tibble, dplyr, tidyr, stringr, readr, forcats, scales, grid, reshape2, Rtsne, ggfortify, factoextra, ggpubr, ggforce, ggrepel, RColorBrewer and pheatmap.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: For heatmap visualization of DEGs, samples were z-score normalized and plotted using ‘pheatmap’ package in R.
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **1.0.12**
- Evidence: Samples were then clustered using Ward’s method and plotted using pheatmap version 1.0.12.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: The SCENIC AUC heatmap was plotted with binarized activity regulons of each cell cluster by the ‘pheatmap’ R package with the annotation information in the Seurat object.
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **1.0.12**
- Evidence: The R (v.3.6.1) package pheatmap (v.1.0.12) was then used to generate the heat map.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Dysregulated naive B cells and de novo autoreactivity in severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05273-0 | PMCID: PMC9630115 | PMID: 36044993
- Evidence: Heat maps were generated using the pheatmap library (v.1.0.12), with data prenormalized (log-transformed z scores calculated per feature) before plotting.
- Full pipeline: normalisation [pheatmap] -> stage not stated [Docker, R v3.6.2, ggplot2]

### Potentiating adoptive cell therapy using synthetic IL-9 receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04801-2 | PMCID: PMC9283313 | PMID: 35676488
- Evidence: Gene expression was visualized using the normalized gene expression (calculated using the rlog transform from DESeq2 and scaled by row) using the pheatmap R package.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> quantification [HTSeq] -> normalisation [pheatmap] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [R, fgsea]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: The mean expression of Lamp5 + subclass markers (avg_log[FC] > 0.75, P adj < 0.05, <40% in non- Lamp5 + subclasses) was calculated in BNSTp and MPOA Esr1 + clusters and visualized using pheatmap.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### A multidimensional coding architecture of the vagal interoceptive system. (Nature 2022)

- DOI: 10.1038/s41586-022-04515-5 | PMCID: PMC8967724 | PMID: 35296859
- Evidence: 2e ) was calculated on the basis of the numbers of single-UPB and dual-UPB marked VSNs across the seven examined visceral organs and plotted using the R pheatmap package.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [R, Seurat, UMAP, pheatmap] -> stage not stated [CellPhoneDB, Fiji, ImageJ]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Evidence: Heatmaps were drawn using the pheatmap package.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: Heatmaps used to visualize the data were generated using the pheatmap R package (version 1.0.12) and unsupervised column hierarchical clustering based on the Euclidean distance performed.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Evidence: Specifically, we visualized the regulon activity of Lhx1 , Lhx2 , Lhx3 , Lhx4 , Lhx5 , Lhx9 and Lmx1b using ‘pheatmap’ in R.
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **1.0.12**
- Evidence: The MAplots, box plots, violin plots and donut plots were produced using ggplot2 (v.3.3.2; https://ggplot2.tidyverse.org ) and heat maps of gene expression changes were produced using pheatmap (v.1.0.12; https://cran.r-project.org/web/packages/pheatmap/index.html ) in R (v.4.0.3).
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Complete human day 14 post-implantation embryo models from naive ES cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06604-5 | PMCID: PMC10584686 | PMID: 37673118
- Evidence: Heatmaps were generated using the Seurat DoHeatmap() function or with R pheatmap package (v.1.0.12).
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Signac v1.6.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [SciPy v1.8.0, seaborn v0.11.0] -> visualisation [SciPy v1.8.0, seaborn v0.11.0] -> stage not stated [R, pheatmap, scDblFinder v1.6]

### Gut microbial carbohydrate metabolism contributes to insulin resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06466-x | PMCID: PMC10499599 | PMID: 37648852
- Version used: **1.0.12**
- Evidence: To characterize the microbial profiles of the study participants, the individuals were clustered on the basis of the abundance of 28 genera, which includes 20 genera in co-abundance microbial groups identified with CCREPE and 8 unclustered genera, using the ward.D function of the R package pheatmap v.1.0.12.
- Full pipeline: alignment/mapping [BWA v0.5.9, Bowtie2] -> quantification [R, WGCNA, pheatmap v1.0.12] -> dimensionality reduction/clustering [R, WGCNA, pheatmap v1.0.12] -> differential/statistical testing [lme4 v1.1] -> visualisation [Cytoscape v3.7.0] -> stage not stated [Enrichr]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Evidence: Heat maps visualizing expression levels of ATF genes, ISR signature genes and cell marker genes in each sample by genotypes or conditions were generated by pheatmap package ( https://github.com/raivokolde/pheatmap/ ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### A pangenome reference of 36 Chinese populations. (Nature 2023)

- DOI: 10.1038/s41586-023-06173-7 | PMCID: PMC10322713 | PMID: 37316654
- Version used: **1.0.12**
- Evidence: The heatmaps were generated using the R package pheatmap 1.0.12.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> variant calling [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BCFtools, QUAST v5.2.0, pheatmap v1.0.12]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: 3f , hierarchical clustering was done using the pheatmap package in R.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Version used: **1.0.12**
- Evidence: Plots were created using ggplot2 v.3.2.1, tidyverse v.1.3.0, dplyr v.0.8.5, cowplot v.1.0.0 and pheatmap v.1.0.12.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: The package pheatmap (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: The data were converted to 0, 1 and 2 format using VCFtools 122 and samples were clustered using the pheatmap package ( https://cran.r-project.org/web/packages/pheatmap/pheatmap.pdf ) from R statistical environment 57 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Migrating is not enough for modern planktonic foraminifera in a changing ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-08191-5 | PMCID: PMC11634771 | PMID: 39537925
- Evidence: The package pheatmap allowed for the creation of heatmaps 71 .
- Full pipeline: stage not stated [ggplot2, ggpubr, pheatmap, tidyverse]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **1.0.12**
- Evidence: Heatmaps were prepared using pheatmap (v.1.0.12) with hierarchical clustering.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **1.0.12**
- Evidence: Then, a hierarchical clustering based on the presence/absence of pangenes was conducted with the pheatmap v.1.0.12 package in R v.4.3.1 using the complete linkage method.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: The heat maps were generated using the pheatmap package, with the data being zero-centred and scaled before display.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: Volcano plots were generated using EnhancedVolcano and heat maps were generated using pheatmap 63 , 64 .
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### Genetic links between ovarian ageing, cancer risk and de novo mutation rates. (Nature 2024)

- DOI: 10.1038/s41586-024-07931-x | PMCID: PMC11410666 | PMID: 39261734
- Evidence: Software packages for R—tidyverse ( https://www.tidyverse.org/ ), pheatmap, ( https://CRAN.R-project.org/package=pheatmap ) and reshape2 ( https://github.com/hadley/reshape )—were used in processing and visualising the data.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> differential/statistical testing [REGENIE v2.2.4, statsmodels] -> visualisation [pheatmap, tidyverse] -> stage not stated [R v4.1.2]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: A total of 113 unique clusters were annotated on the basis of median marker expression using the pheatmap package.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### Probing plant signal processing optogenetically by two channelrhodopsins. (Nature 2024)

- DOI: 10.1038/s41586-024-07884-1 | PMCID: PMC11424491 | PMID: 39198644
- Evidence: Finally, heat maps were generated with the pheatmap R package (version 1.0.12; https://CRAN.R-project.org/package=pheatmap ).
- Full pipeline: alignment/mapping [fastp, kallisto] -> normalisation [DESeq2] -> stage not stated [PyMOL, R, pheatmap]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: Upset plots were generated using the UpSetR package 61 , and heatmaps were generated using the pheatmap package, which also implements hierarchical clustering for the ordering of columns and rows where indicated.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### Inhibition of IL-11 signalling extends mammalian healthspan and lifespan. (Nature 2024)

- DOI: 10.1038/s41586-024-07701-9 | PMCID: PMC11291288 | PMID: 39020175
- Evidence: Mitocarta v3.0 gene list was downloaded and TPM values in Fat IgG and anti-IL-11 samples were plotted using pheatmap R package for genes which had TPM ≥ 5 in at least one condition.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.7.9a] -> quantification [ImageJ v1.53t, pheatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.36.0, R v4.2] -> visualisation [pheatmap] -> stage not stated [featureCounts, fgsea v1.22.0]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Next the top 2,000 most variable genes in those perturbations were selected and heat maps of correlation matrices were computed using the pheatmap package with ward.D2 method for clustering.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **1.0.12**
- Evidence: Heatmap results were plotted using pheatmap (v.1.0.12) in R.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: For heat maps, the pheatmap R package was used to plot row mean centred and scaled normalized log 2 (CPM + 0.5) values.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.0.12**
- Evidence: ...49 , ggrastr (v.1.0.2) 150 , ggrepel (v.0.9.3) 151 , grid (v.4.1.3) 152 , gridExtra (v.2.3) 153 , gtable (v.0.3.3) 154 , matrixStats (v.0.63.0) 155 , pheatmap (v.1.0.12) 156 , plyr (v.1.8.8) 157 , purrr (v.1.0.1) 158 , RColorBrewer (v.1.1-3) 159 , readxl (v.1.4.2) 160 , reshape2 (v.1.4.4) 161 , scales (v.1.2.1) 162 , splitstackshape (v.1.4.8) 163 , stats (v.4.1.3) 152 , stringi (v.1.7.12) 164 , st...
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Version used: **1.0.12**
- Evidence: Heatmaps were generated using pheatmap (v.1.0.12) R package.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: Heat maps were generated with the pheatmap package 107 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **1.0.12**
- Evidence: ...d IMC data, which were conducted using R (v4.2.3) using R-studio build 513 with the packages: tidyverse (v2.0), ggplot2 (v3.4.2), ggpubr (v0.6.0) and pheatmap (v1.0.12).
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: Differential gene expression analysis was conducted using DESeq2, and downstream heat-map visualization was performed using the R package pheatmap. scRNA-seq used in this study was performed with samples from two sources: human PBMCs and mouse kidney cells.
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### Spatial joint profiling of DNA methylome and transcriptome in tissues. (Nature 2025)

- DOI: 10.1038/s41586-025-09478-x | PMCID: PMC12571926 | PMID: 40903587
- Evidence: To illustrate the relationships between clustering results from different modalities, we generated the confusion matrix and alluvial diagram using the pheatmap and ggalluvial R package 61 .
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [Python, R, UMAP, clusterProfiler, pheatmap] -> visualisation [Python] -> stage not stated [HOMER, Seurat]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Version used: **1.0.12**
- Evidence: Heat maps were generated using the R package pheatmap (v.1.0.12).
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **1.0.12**
- Evidence: ...2 (v.1.4.4), patchwork (v.1.1.3), RColorBrewer (v.1.1.3), ggrepel (v.0.9.4), aplot (v.0.1.10), ggdendro (v.0.1.23), Matrix (v.1.6.4), here (v.1.0.1), pheatmap (v.1.0.12), tidyr (v.1.3.0), cowplot (v.1.1.1) and circlize’ (v.0.4.15); and Matlab built-in functions: plot, scatter, violinplot, imagesc, contour, bar, box, errorbar and pie.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: Plots were produced using the Seurat 57 , ggplot2 63 , ggpubr 64 and pheatmap 65 R packages.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: Results were visualized with the pheatmap package.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **1.0.12**
- Evidence: The session used the following libraries: limma (3.46.0), edgeR (3.32.1), tximport (1.18.0), edgeR (3.32.1), sva (3.38.0), RColorBrewer (1.1-2), pheatmap (1.0.12), biomaRt (2.46.3), ggplot2 (3.3.3), gplots (3.1.1), ggfortify (0.4.11), NMF (0.23.0), cluster (2.1.1), fpc (2.2-9), plyr (1.8.6), dplyr (1.0.5), pvclust (2.2-0), ggrepel (0.9.1), amap (0.8-18), gProfileR (0.7.0), xtable (1.8-4), ggpubr (...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: To visualize the DEGs, the samples were z -score normalized and plotted as a heat map using the ‘pheatmap’ package in R.
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Evidence: The distance matrix was calculated using the dist function in R using the Euclidean distance and visualized with a pheatmap in R (Extended Data Fig.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Version used: **1.0.12**
- Evidence: ...wer (1.1.3, SCR_016697); R package ggrepel (0.9.5, RRID:SCR_016223); R package dplyr (1.1.4); R package FactoMineR (2.11, RRID:SCR_014602); R package pheatmap (1.0.12, RRID:SCR_016418); R package factoextra (1.0.7, RRID:SCR_016692); R package pROC (1.18.5); R package reshape2 (1.4.4); R package igraph (2.1.2); R package tidyr (1.3.1, RRID:SCR_017102); R package lme4 (1.1.13.5, RRID:SCR_015654); R ...
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Molecular basis of positional memory in limb regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09036-5 | PMCID: PMC12176643 | PMID: 40399677
- Evidence: Heatmaps were generated using the pheatmap package v.1.0.12 (R.
- Full pipeline: read trimming [HISAT2, Trimmomatic v0.39] -> alignment/mapping [HISAT2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, ggplot2 v3.3.6, pheatmap]

### Unravelling cysteine-deficiency-associated rapid weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-08996-y | PMCID: PMC12267064 | PMID: 40399674
- Evidence: Heat maps were generated on the basis of z -scores of normalized counts using the R library pheatmap.
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [DESeq2 v1.48, SciPy v1.1.0] -> visualisation [DESeq2 v1.48] -> stage not stated [HTSeq, Python, R]

### TGFβ links EBV to multisystem inflammatory syndrome in children. (Nature 2025)

- DOI: 10.1038/s41586-025-08697-6 | PMCID: PMC12003184 | PMID: 40074901
- Evidence: A heat map was generated using the R package pheatmap.
- Full pipeline: normalisation [GSEA, R v4.1.2, Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, pheatmap]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Plots were generated using ComplexHeatmap (RRID:SCR_01727) and pheatmap (RRID:SCR_016418) R packages. devDEG analysis The devDEG analysis presented in Fig.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: The centroids were visualized using the R package Plotly, hierarchically clustered using complete linkage method implemented in the hclust function with default parameters, and plotted using the R package pheatmap 75 .
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Version used: **1.0.12**
- Evidence: Heatmaps were generated using the R package pheatmap (v.1.0.12).
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **1.0.12**
- Evidence: 121 ), pheatmap v.1.0.12 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: KO abundances were summarized based on KEGG pathways for both GFS and other cryospheric ecosystems, and a heatmap was generated using the package pheatmap 95 (v.1.0.12).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Pearson correlation analysis was performed using the top 500 most variable genes with cor() with method=c(“pearson”) followed by package pheatmap().
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Evidence: The plots were generated using the DimPlot and VlnPlot functions from Seurat as well as the ggplot2 and pheatmap R libraries.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Version used: **1.0.12**
- Evidence: All data analysis and visualization was done in R (v4.2.1) with the following packages: stats (v.4.1.1), vegan (v.2.6), ggplot2 (v.3.3.6), ComplexUpset (v.2.8.0), tidyr (v.1.2.0), dplyr (v.1.0.9), corrplot (v.0.92), pheatmap (v.1.0.12), RColorBrewer (v.1.1-3), pls (v.2.8), edgeR (v.3.16).
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Evidence: To compare correlation between CATCH-seq and STAR ChIP-seq data 23 , read counts over each bin (10 kb) across the whole genome were calculated and the reads per million values for each bin were used to calculate the Spearman correlation coefficient using deepTools suite and visualized using the R function pheatmap.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **1.0.12**
- Evidence: Plots were generated with Python (v.3.9.7), R (v.3.6.1) and Rstudio (v.4.2.2), using ggplot2 (v.4.3.2), pheatmap (v.1.0.12), radarchart (v.0.7.5) and euler (v.6.1.1).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: The protein from each isolate that aligned best to each reference protein was plotted in a heat map using the pheatmap package.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **1.0.12**
- Evidence: Postprocessing and data visualization were performed in R (v.4.4.1) using data.table (v.1.14.8), ggplot2 (v.3.4.2), pheatmap (v.1.0.12) and ComplexHeatmap (v.2.16.0).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: Heatmap visualization of ATAC-seq data was performed using pheatmap. scRNA-seq metadata analysis Analysis was performed primarily in R (v.3.6.1) using the package Seurat 68 , 79 (v.3.1), with the package tidyverse 80 (v.1.2.1) used to organize data and the package ggplot2 (v.3.2.1) to generate figures. scRNA-seq data from GSE10898 , GSE99254 , GSE98638 , GSE199565 and GSE181785 were filtered to ke...
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### Albumin orchestrates a natural host defence mechanism against mucormycosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09882-3 | PMCID: PMC12804082 | PMID: 41501454
- Evidence: The heat maps were produced using the pheatmap package 75 .
- Full pipeline: alignment/mapping [STAR, featureCounts] -> differential/statistical testing [R v4.3.1] -> visualisation [R v4.3.1] -> stage not stated [Fiji, GSEA, ImageJ, pheatmap]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **1.0.12**
- Evidence: Heat maps were generated using the pheatmap (v.1.0.12) package in R (v.4.1.0).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Molecular characterization of Barrett's esophagus at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2113061118 | PMCID: PMC8617519 | PMID: 34795059
- Evidence: The aneuploidy heat maps were generated in R using the pheatmap function and the cluster with hardly any copy number aberrations in each patient was defined as chromosomal stable.
- Full pipeline: alignment/mapping [BWA v0.7.5, GATK] -> variant calling [BWA v0.7.5, GATK] -> registration [BWA v0.7.5, GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [R]

### Computational modeling identifies multitargeted kinase inhibitors as effective therapies for metastatic, castration-resistant prostate cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2103623118 | PMCID: PMC8501846 | PMID: 34593636
- Evidence: Heatmaps were generated either in R Studio using the “pheatmap” package ( 24 ) or in GraphPad Prism.
- Full pipeline: machine learning [R v3.4.1] -> stage not stated [pheatmap]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: The implementation relies significantly upon the R packages data.table ( 52 ), ggplot2 ( 53 ), ggspatial ( 54 ), rnaturalearth ( 55 ), and pheatmap ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: To detect the most differentially abundant species among chronological groups, we used DESeq2 and generated heatmaps with the package pheatmap in R ( Dataset S8 and SI Appendix , Fig.
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### High-salt diet suppresses autoimmune demyelination by regulating the blood-brain barrier permeability. (PNAS 2021)

- DOI: 10.1073/pnas.2025944118 | PMCID: PMC7999868 | PMID: 33723078
- Evidence: Subsequent data filtering and visualizations were performed in the R environment using the tidyverse packages and pheatmap.
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [DESeq2 v1.26.1, kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.1, clusterProfiler v3.14.3, limma] -> visualisation [pheatmap, tidyverse]

### DNA methylation-linked chromatin accessibility affects genomic architecture in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023347118 | PMCID: PMC7865151 | PMID: 33495321
- Evidence: Heat maps were visualized with the R package pheatmap ( 58 ).
- Full pipeline: read trimming [Cutadapt v2.5, SAMtools] -> alignment/mapping [Bowtie2, Cutadapt v2.5, RSEM] -> quantification [Bowtie2, RSEM] -> differential/statistical testing [R v3.30.0, edgeR v3.30.0] -> visualisation [pheatmap] -> stage not stated [BEDTools v2.26.0]

### Ancient DNA from Guam and the peopling of the Pacific. (PNAS 2021)

- DOI: 10.1073/pnas.2022112118 | PMCID: PMC7817125 | PMID: 33443177
- Evidence: We used the tidyverse ( 98 ), data.table ( https://CRAN.R-project.org/package=data.table ), Hmisc ( https://CRAN.R-project.org/package=Hmisc ), and pheatmap ( https://CRAN.R-project.org/package=pheatmap ) packages.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, R, data.table, pheatmap, tidyverse]

### Microbial dynamics of elevated carbon flux in the open ocean's abyss. (PNAS 2021)

- DOI: 10.1073/pnas.2018269118 | PMCID: PMC7848738 | PMID: 33479184
- Evidence: Figures were generated using pheatmap ( 85 ) and ggplot2 ( 86 ) packages in R ( 79 ) and further refined using Adobe Illustrator.
- Full pipeline: read trimming [SPAdes] -> alignment/mapping [SPAdes] -> structure determination [SPAdes, ggplot2, pheatmap] -> visualisation [Cytoscape, ggplot2, pheatmap] -> stage not stated [BWA v0.7.15, R, WGCNA]

### Temporal changes in plasma membrane lipid content induce endocytosis to regulate developmental epithelial-to-mesenchymal transition. (PNAS 2022)

- DOI: 10.1073/pnas.2212879119 | PMCID: PMC9907157 | PMID: 36508654
- Evidence: Complete Euclidean distance clustering was performed using pheatmap ( Fig.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, featureCounts]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: We made plots using ggplot2, cowplot, and pheatmap ( 110 – 113 ) and made extensive use of the tidyverse suite of R packages for data analysis ( 114 ).
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: Heatmaps were generated of the top 50 differentially expressed transcripts using pheatmap ( 66 ) and RColorBrewer ( 67 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Tissue-specific regulation of lipid polyester synthesis genes controlling oxygen permeation into <i>Lotus japonicus</i> nodules. (PNAS 2022)

- DOI: 10.1073/pnas.2206291119 | PMCID: PMC9704718 | PMID: 36375074
- Evidence: The heatmap for each module was created with the function pheatmap ( 61 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [ImageJ] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, R] -> stage not stated [RAxML, ggpubr v0.4.0.999, pheatmap]

### Blockade of the protease ADAM17 ameliorates experimental pancreatitis. (PNAS 2022)

- DOI: 10.1073/pnas.2213744119 | PMCID: PMC9586293 | PMID: 36215509
- Evidence: Heat maps were created using the pheatmap package (v1.0.12) ( 31 ).
- Full pipeline: alignment/mapping [R v4.1.2] -> differential/statistical testing [limma v3.50.0] -> stage not stated [edgeR, pheatmap]

### FGFR redundancy limits the efficacy of FGFR4-selective inhibitors in hepatocellular carcinoma. (PNAS 2022)

- DOI: 10.1073/pnas.2208844119 | PMCID: PMC9546626 | PMID: 36179047
- Evidence: Heat maps were generated with pheatmap in R.
- Full pipeline: alignment/mapping [DESeq2] -> quantification [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [pheatmap]

### Activating STING1-dependent immune signaling in <i>TP53</i> mutant and wild-type acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2123227119 | PMCID: PMC9271208 | PMID: 35759659
- Evidence: Resulting normalized enrichment scores were read into the pheatmap package ( 81 ), Z-score transformed, and then clustered using Ward.D2.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [ggpubr] -> stage not stated [GSEA, R, STRING db, fgsea]

### DNA methylation signatures in airway cells from adult children of asthmatic mothers reflect subtypes of severe asthma. (PNAS 2022)

- DOI: 10.1073/pnas.2116467119 | PMCID: PMC9214527 | PMID: 35666868
- Evidence: Reactions with a mean decrease in accuracy greater than 1 were extracted and plotted in a heatmap using pheatmap from the pheatmap package in R.
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [WGCNA, limma] -> visualisation [pheatmap] -> stage not stated [R]

### GPR174 signals via G&lt;i&gt;α&lt;/i&gt;s to control a CD86-containing gene expression program in B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2201794119 | PMCID: PMC9191659 | PMID: 35639700
- Evidence: The heatmap was generated with pheatmap.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [MACS2, pheatmap]

### Extracellular vesicles from triple negative breast cancer promote pro-inflammatory macrophages associated with better clinical outcome. (PNAS 2022)

- DOI: 10.1073/pnas.2107394119 | PMCID: PMC9169908 | PMID: 35439048
- Evidence: Correlation plots were computed using the same METABRIC TNBC cohort, using Spearman correlation between gene sum from the signatures, and plotted using pheatmap R package (v1.0.12).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [UMAP, pheatmap] -> stage not stated [Enrichr, MACS2, R, Seurat]

### The CHARGE syndrome ortholog CHD-7 regulates TGF-β pathways in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2109508119 | PMCID: PMC9169646 | PMID: 35394881
- Evidence: Heatmaps were generated using pheatmap package (v1.0.12) with hierarchical clustering on the rows with the default options.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.5.4a] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [Bioconductor v3.7, R v3.5]

### Landscape of surfaceome and endocytome in human glioma is divergent and depends on cellular spatial organization. (PNAS 2022)

- DOI: 10.1073/pnas.2114456119 | PMCID: PMC8892282 | PMID: 35217608
- Evidence: Bioinformatics analyses were conducted in R version 4.0.4 and figures were generated using the packages ggplot2, RColorBrewer, viridis, VennDiagram, venneuler (in combination with http://bioinformatics.psb.ugent.be/cgi-bin/liste/Venn/calculate_venn.htpl to perform six-group overlap comparison), and pheatmap (clustering method used was “ward.D2”).
- Full pipeline: dimensionality reduction/clustering [R v4.0.4, ggplot2, pheatmap] -> visualisation [R v4.0.4, ggplot2, pheatmap] -> stage not stated [GSEA]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Plots and heatmaps were created in R using pheatmap and EnhancedVolcano and the ClustVis web tool ( 59 , 60 ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### A distinct role of STING in regulating glucose homeostasis through insulin sensitivity and insulin secretion. (PNAS 2022)

- DOI: 10.1073/pnas.2101848119 | PMCID: PMC8851542 | PMID: 35145023
- Version used: **1.0.12**
- Evidence: Unsupervised clustering and heatmap visualization were performed with pheatmap (v1.0.12; https://cran.r-project.org/web/packages/pheatmap/index.html ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1] -> alignment/mapping [Bowtie2 v2.3.5.1] -> quantification [HOMER v4.11.1] -> normalisation [HOMER v4.11.1] -> dimensionality reduction/clustering [clusterProfiler, pheatmap v1.0.12] -> visualisation [clusterProfiler, pheatmap v1.0.12]

### Circadian key component CLOCK/BMAL1 interferes with segmentation clock in mouse embryonic organoids. (PNAS 2022)

- DOI: 10.1073/pnas.2114083119 | PMCID: PMC8746294 | PMID: 34930826
- Evidence: The heatmaps of gene expression and KEGG pathways were generated with R using the pheatmap and pathview packages, respectively.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [DESeq2, Trimmomatic] -> quantification [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, pheatmap]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: The pheatmap package in R was used to construct heat maps.
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Version used: **1.0.12**
- Evidence: The Euclidian distance matrix was calculated from the rlog-normalized counts of the 1,500 core genes using the R function dist, and the heatmap was produced in pheatmap version 1.0.12 ( 60 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### The exceptional form and function of the giant bacterium <i>Ca.</i> Epulopiscium viviparus revolves around its sodium motive force. (PNAS 2023)

- DOI: 10.1073/pnas.2306160120 | PMCID: PMC10756260 | PMID: 38109545
- Evidence: RPKM values were log transformed and compared using pheatmap in R.
- Full pipeline: quantification [pheatmap] -> stage not stated [Canu v1.1, InterProScan]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **1.0.12**
- Evidence: Packages ggplot2 v3.3.6, ggpubr v0.4.0 pheatmap v1.0.12, RColorBrewer v1.1-3, ggsignif v0.6.3, and tidyverse v1.3.1 were used for data manipulation and representation.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Version used: **1.0.12**
- Evidence: The plots generated for showing the results of the differential HERV expression analysis, such as volcano plots, heatmaps, Venn diagrams, and circos plots, have been drawn using EnhancedVolcano (v.1.16.0) ( 41 ), pheatmap (v.1.0.12) ( https://cran.r-project.org/web/packages/pheatmap/index.html ), InteractiVenn ( 42 ), and circlize (v.0.4.15) ( 43 ), respectively.
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Engineered calprotectin-sensing probiotics for IBD surveillance in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2221121120 | PMCID: PMC10410751 | PMID: 37523538
- Version used: **1.0.12**
- Evidence: Plots were made in R (v4.0.3) using ggplot2 (v3.3.0), pheatmap (v1.0.12).
- Full pipeline: alignment/mapping [STAR v2.7.5] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [R v4.0.3, ggplot2 v3.3.0, pheatmap v1.0.12]

### Disulfiram blocks inflammatory TLR4 signaling by targeting MD-2. (PNAS 2023)

- DOI: 10.1073/pnas.2306399120 | PMCID: PMC10401014 | PMID: 37487070
- Evidence: The differentially expressed genes were subjected to heat map plotting with R package pheatmap.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2, R, pheatmap]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: Heatmaps were produced using the pheatmap R package ( https://github.com/raivokolde/pheatmap ), lattice ( http://lattice.r-forge.r-project.org/ ) or ggplot2 ( https://ggplot2.tidyverse.org ) packages.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: Heatmap plots based on RNA-seq data were generated using R 3.6 and the pheatmap package ( https://github.com/raivokolde/pheatmap ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Computational drug discovery for castration-resistant prostate cancers through in vitro drug response modeling. (PNAS 2023)

- DOI: 10.1073/pnas.2218522120 | PMCID: PMC10151558 | PMID: 37068243
- Evidence: The R package pheatmap was used to plot a heatmap showing normalized expression between cell models.
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [limma] -> stage not stated [ImageJ, R v4.0.3]

### Ancient DNA from a lost Negev Highlands desert grape reveals a Late Antiquity wine lineage. (PNAS 2023)

- DOI: 10.1073/pnas.2213563120 | PMCID: PMC10151551 | PMID: 37068234
- Evidence: For the larger SNP dataset, the samples were ordered and clustered using the R library pheatmap.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.5] -> variant calling [GATK, VCFtools] -> dimensionality reduction/clustering [pheatmap] -> visualisation [ggplot2]

### Contextual modifiers of healthspan, lifespan, and epigenome in mice under chronic social stress. (PNAS 2023)

- DOI: 10.1073/pnas.2211755120 | PMCID: PMC10120026 | PMID: 37043532
- Evidence: For DNA methylation data, heatmaps were generated for CpG islands (defined as regions >500 bp, >55% GC and expected/observed CpG ratio of >0.65; this restricted the sample for this analysis to ~30,000 CpG islands) using the R package “pheatmap” (version 1.0.12) to incorporate strain and DAI to cluster CpG islands by Euclidean distance and the Ward.D2 clustering method.
- Full pipeline: dimensionality reduction/clustering [pheatmap] -> stage not stated [R]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Version used: **1.0.12**
- Evidence: Log (CPM) and visualization were performed using ggplot2 (3.2.1), RColorBrewer (v1.1.2), tibble (2.1.3), pheatmap (v1.0.12), stats (v3.5.1), and gplots (v3.0.1.2).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### Polyamines and linear DNA mediate bacterial threat assessment of bacteriophage infection. (PNAS 2023)

- DOI: 10.1073/pnas.2216430120 | PMCID: PMC9992862 | PMID: 36802441
- Evidence: RNA-seq analysis results were plotted with ggplot2 and pheatmap packages in R.
- Full pipeline: normalisation [edgeR v3.34.1] -> differential/statistical testing [edgeR v3.34.1] -> visualisation [ggplot2, pheatmap]

### Type III interferon drives thymic B cell activation and regulatory T cell generation. (PNAS 2023)

- DOI: 10.1073/pnas.2220120120 | PMCID: PMC9992806 | PMID: 36802427
- Evidence: 4.0.5), including packages EdgeR, ggplot2 and pheatmap.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R v4.0.0, Seurat, edgeR v3.24.3, ggplot2, pheatmap]

### Complement C3d enables cell-mediated immunity capable of distinguishing spontaneously transformed from nontransformed cells. (PNAS 2024)

- DOI: 10.1073/pnas.2405824121 | PMCID: PMC11670236 | PMID: 39693340
- Evidence: Heatmaps were created using “pheatmap”.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [Seurat, pheatmap]

### Histone methyltransferase SETDB1 safeguards mouse fetal hematopoiesis by suppressing activation of cryptic enhancers. (PNAS 2024)

- DOI: 10.1073/pnas.2409656121 | PMCID: PMC11670114 | PMID: 39689172
- Evidence: Heatmaps were plotted with pheatmap either using rlog-normalized expression values from RSEM-normalized data.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, RSEM, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [RSEM, pheatmap] -> stage not stated [BEDTools, GSEA, MACS2, deepTools]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: For the unsupervised clustering, mean expression values from the previously published dataset ( 41 ) and the MitoString analysis were combined and hierarchically clustered and visualized using the pheatmap package ( 81 ) in R with default clustering settings.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: We generated a dendrogram and heatmap of F ST values using R package “pheatmap” ( 106 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### A comprehensive transcriptome characterization of individual nuclear receptor pathways in the human small intestine. (PNAS 2024)

- DOI: 10.1073/pnas.2411189121 | PMCID: PMC11551338 | PMID: 39475639
- Evidence: Heatmaps were generated with pheatmap package version 1.0.12.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [pheatmap]

### A receptor kinase senses sterol by coupling with elicitins in auxotrophic &lt;i&gt;Phytophthora&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2408186121 | PMCID: PMC11551405 | PMID: 39475635
- Evidence: Gene expression patterns were clustered using the pheatmap package in R, employing the ward.D2 clustering algorithm.
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [pheatmap]

### AMBRA1 controls the translation of immune-specific genes in T lymphocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2416722121 | PMCID: PMC11536168 | PMID: 39436665
- Evidence: Volcano plots were generated using the EnhancedVolcano package, while heatmaps were created with pheatmap using the normalized count data from DESeq2.
- Full pipeline: quantification [HTSeq] -> normalisation [pheatmap] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, SAMtools, deepTools]

### Single-cell resolution of intestinal regeneration in pythons without crypts illuminates conserved vertebrate regenerative mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2405463121 | PMCID: PMC11513969 | PMID: 39423244
- Version used: **1.0.12**
- Evidence: Differentially expressed genes were hierarchically clustered and visualized by pheatmap 1.0.12 ( 79 ).
- Full pipeline: read trimming [STAR v2.7.10a, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.10a, Trimmomatic v0.36] -> quantification [STAR v2.7.10a, Trimmomatic v0.36] -> normalisation [Seurat v4.2.0] -> dimensionality reduction/clustering [Seurat v4.2.0, UMAP, pheatmap v1.0.12] -> differential/statistical testing [pheatmap v1.0.12] -> visualisation [UMAP, pheatmap v1.0.12] -> stage not stated [DESeq2 v1.36.0, SCENIC v1.3.1]

### Platelet-activating factor (PAF) promotes immunosuppressive neutrophil differentiation within tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2406748121 | PMCID: PMC11363292 | PMID: 39178229
- Version used: **1.0.12**
- Evidence: Heatmap was created using pheatmap (1.0.12) using DESeq2-normalized counts.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> normalisation [DESeq2, pheatmap v1.0.12] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Gut bacteria are essential for development of an invasive bark beetle by regulating glucose transport. (PNAS 2024)

- DOI: 10.1073/pnas.2410889121 | PMCID: PMC11331112 | PMID: 39110737
- Evidence: Values were centered and scaled in the row direction with −2 to 2 corresponding to the blue and red colors using pheatmap package in R.
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [R] -> stage not stated [BLAST]

### USP11 promotes prostate cancer progression by up-regulating AR and c-Myc activity. (PNAS 2024)

- DOI: 10.1073/pnas.2403331121 | PMCID: PMC11295044 | PMID: 39052835
- Evidence: FPKM values of RNA-seq results were log2-transformed and used for heatmap preparation using the pheatmap package in R.
- Full pipeline: quantification [pheatmap] -> differential/statistical testing [GSEA] -> stage not stated [Enrichr]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Version used: **1.0.12**
- Evidence: From the qpWave distances, we formed an igraph object through the igraph package v.1.4.3 ( https://github.com/igraph ) and performed hierarchical clustering with pheatmap v.1.0.12 in R. f -Statistics.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Evidence: The plots were generated using the DimPlot, FeaturePlot, and VlnPlot functions from Seurat, as well as the ggplot2 and pheatmap R libraries.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### Pathogenic variants in autism gene &lt;i&gt;KATNAL2&lt;/i&gt; cause hydrocephalus and disrupt neuronal connectivity by impairing ciliary microtubule dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2314702121 | PMCID: PMC11228466 | PMID: 38916997
- Evidence: Visualization of the heatmap was by ComplexHeatmap and pheatmap packages, and bar graphs were created with ggplot2 ( 57 , 58 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ANNOVAR, GATK] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [ImageJ] -> visualisation [ComplexHeatmap, ggplot2, pheatmap]

### Transfection of entomopathogenic <i>Metarhizium</i> species with a mycovirus confers hypervirulence against two lepidopteran pests. (PNAS 2024)

- DOI: 10.1073/pnas.2320572121 | PMCID: PMC11214047 | PMID: 38885380
- Evidence: The heatmap was performed using ggplot2 and pheatmap packages in R package.
- Full pipeline: read trimming [fastp] -> alignment/mapping [ggplot2] -> quantification [ggplot2] -> dimensionality reduction/clustering [clusterProfiler, ggplot2] -> stage not stated [BLAST, DESeq2, R, pheatmap]

### Innate acting memory Th1 cells modulate heterologous diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2312837121 | PMCID: PMC11181110 | PMID: 38838013
- Version used: **1.0.12**
- Evidence: To plot the results, the packages ggplot2 ( 66 ) (version 3.3.3), pheatmap (version 1.0.12), UpSetR ( 67 ) (version 1.4.0), and VennDiagaram (version 1.6.20) were used.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [R v4.0.2, featureCounts, ggplot2, pheatmap v1.0.12]

### Nitrogen and sulfur for phosphorus: Lipidome adaptation of anaerobic sulfate-reducing bacteria in phosphorus-deprived conditions. (PNAS 2024)

- DOI: 10.1073/pnas.2400711121 | PMCID: PMC11181052 | PMID: 38833476
- Evidence: 2 E ) was performed using the “ggplot2” and “pheatmap” packages in R, version 4.3.2.
- Full pipeline: visualisation [Cytoscape v3.9.1] -> stage not stated [ggplot2, pheatmap]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: Gene expression was visualized using the R package pheatmap ( 122 ) and GraphPad Prism 10.
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Clocking out and letting go to unleash green biotech applications in a photosynthetic host. (PNAS 2024)

- DOI: 10.1073/pnas.2318690121 | PMCID: PMC11127020 | PMID: 38739791
- Version used: **1.0.12**
- Evidence: Heatmaps were created with the package pheatmap v.
- Full pipeline: alignment/mapping [SAMtools v1.11.0] -> quantification [DESeq2 v1.36.0] -> normalisation [R] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HISAT2 v2.2.1, ggplot2, pheatmap v1.0.12]

### OCA-B/Pou2af1 is sufficient to promote CD4&lt;sup&gt;+&lt;/sup&gt; T cell memory and prospectively identifies memory precursors. (PNAS 2024)

- DOI: 10.1073/pnas.2309153121 | PMCID: PMC10907311 | PMID: 38386711
- Evidence: Figures were generated in R version 4.0.0 using functions from ggplots libraries and pheatmap.
- Full pipeline: quality control [STAR v2.7.3a] -> alignment/mapping [STAR v2.7.3a] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v4.0.0, UMAP, pheatmap]

### Precipitation increase promotes soil organic carbon formation and stability via the mycorrhizal fungal pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2519072122 | PMCID: PMC12685053 | PMID: 41289393
- Evidence: Pearson correlation between AMF colonization and root traits was analyzed using the “pheatmap” package.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, metafor, pheatmap, vegan]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Evidence: To visualize differentially expressed orthologs between large-bodied and miniature species, we applied a variance-stabilizing transformation (VST) to the normalized count data using the “vst” function in the DESeq2 R package and generated a hierarchical clustering heatmap using the “pheatmap” function.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### The balance between microbial arsenic methylation and demethylation in paddy soils underpins global arsenic risk and straighthead disease in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2508311122 | PMCID: PMC12478174 | PMID: 40966281
- Evidence: Differential taxa were visualized with the pheatmap package, and environmental drivers were evaluated via random forest models.
- Full pipeline: quality control [fastp] -> differential/statistical testing [pheatmap] -> visualisation [pheatmap] -> stage not stated [BLAST]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Version used: **1.0.12**
- Evidence: RPM-normalized reads were used to determine phasiRNA accumulation peaks during meiosis progression and to visualize the 21-nt and 24-nt phasiRNA abundances using the R pheatmap v1.0.12 package ( https://rdrr.io/cran/pheatmap/ ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### Ciprofloxacin-driven purifying selection on viral genomes accelerates soil N&lt;sub&gt;2&lt;/sub&gt;O production. (PNAS 2025)

- DOI: 10.1073/pnas.2503199122 | PMCID: PMC12304974 | PMID: 40668828
- Evidence: Heat maps, bar plots, box plots, bar stacking plots, and density plots were drawn using the “ggplot2” and “pheatmap” packages in R.
- Full pipeline: read trimming [fastp] -> visualisation [Cytoscape v3.7.2] -> stage not stated [BLAST v2.12.0, R v4.3.1, eggNOG, ggplot2, pheatmap]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: The ggplot2 and pheatmap packages were applied to generate volcano plots and heatmaps, respectively.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### SARS-CoV-2 nsp15 enhances viral virulence by subverting host antiviral defenses. (PNAS 2025)

- DOI: 10.1073/pnas.2426528122 | PMCID: PMC12184426 | PMID: 40504150
- Evidence: DEGs enriched in GO:0051607 (Defense Response to Virus) in each strain were visualized by their fold changes compared to mock using the R package pheatmap ( 58 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [pheatmap] -> stage not stated [ImageJ, featureCounts]

### Formation of giant ER sheets by pentadecanoic acid causes lipotoxicity in fission yeast. (PNAS 2025)

- DOI: 10.1073/pnas.2422126122 | PMCID: PMC12146749 | PMID: 40424131
- Evidence: Hierarchical clustering and heatmap analysis were performed using the R package “pheatmap.” Log 10 -transformed quantitative data from untargeted lipidomics were used for the analyses.
- Full pipeline: dimensionality reduction/clustering [R, pheatmap] -> stage not stated [ImageJ]

### A symbiotic gene stimulates aggressive behavior favoring the survival of parasitized caterpillars. (PNAS 2025)

- DOI: 10.1073/pnas.2422935122 | PMCID: PMC12067249 | PMID: 40294273
- Evidence: The heatmap plot of starvation-induced CvBV genes in CNS was generated using the pheatmap R package (v1.0.12) with FPKMs standardized by natural logarithm ( 75 ).
- Full pipeline: alignment/mapping [TopHat v2.1.1] -> quantification [R, pheatmap]

### The NAE1-mediated neddylation operates as an essential post-translational modification checkpoint for effector CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424061122 | PMCID: PMC11912420 | PMID: 40030035
- Evidence: Volcano plots were generated by VolcaNoseR, and heatmaps were generated with Morpheus ( https://software.broadinstitute.org/morpheus ) and pheatmap V 1.0.12.
- Full pipeline: read trimming [HISAT2, SAMtools, Trim Galore v0.6.10] -> alignment/mapping [HISAT2, SAMtools, Trim Galore v0.6.10] -> stage not stated [DESeq2, GSEA, pheatmap]

### Extensive location bias of the GPCR-dependent translatome via site-selective activation of mTOR. (PNAS 2025)

- DOI: 10.1073/pnas.2414738122 | PMCID: PMC11874449 | PMID: 39964727
- Evidence: K-means clustering was performed with the R-package pheatmap.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v3.16] -> stage not stated [Cytoscape, R]

### Flake production: A universal by-product of primate stone percussion. (PNAS 2025)

- DOI: 10.1073/pnas.2420067122 | PMCID: PMC11848292 | PMID: 39933001
- Evidence: These differences are visually illustrated using the pheatmap package.
- Full pipeline: differential/statistical testing [R] -> stage not stated [pheatmap]

### Abscisic acid signaling gates salt-induced responses of plant roots. (PNAS 2025)

- DOI: 10.1073/pnas.2406373122 | PMCID: PMC11831169 | PMID: 39908104
- Evidence: Heatmaps were created with the R package pheatmap ( 63 ), using Euclidean distance mapping and Ward.D clustering algorithms.
- Full pipeline: quality control [FastQC, MultiQC, Python v2.7, Trim Galore] -> read trimming [FastQC, MultiQC, Python v2.7, Trim Galore] -> alignment/mapping [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, R] -> stage not stated [OpenCV v4.5.1.48]

### Fatty acid metabolism and the oxidative stress response support bacterial predation. (PNAS 2025)

- DOI: 10.1073/pnas.2420875122 | PMCID: PMC11804543 | PMID: 39869799
- Evidence: These scaled values were plotted using the pheatmap function in R.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap] -> stage not stated [ImageJ]

### Targeting EPHB2/ABL1 restores antitumor immunity in preclinical models of ependymoma. (PNAS 2025)

- DOI: 10.1073/pnas.2319474122 | PMCID: PMC11789170 | PMID: 39841145
- Evidence: R package pheatmap ( https://github.com/raivokolde/pheatmap ) was employed for generating the gene expression profile heatmap and hierarchical clustering.
- Full pipeline: quantification [HTSeq] -> dimensionality reduction/clustering [R, STRING db, pheatmap] -> stage not stated [Bioconductor, DESeq2, Seurat]

### Mitochondrial DNA lineages determine tumor progression through T cell reactive oxygen signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2417252121 | PMCID: PMC11725793 | PMID: 39752523
- Evidence: Heatmaps were generated using the pheatmap R package.
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R] -> stage not stated [MACS2, pheatmap]

### A receptor kinase complex refines cambium activity in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2532481123 | PMCID: PMC13321232 | PMID: 42330278
- Version used: **1.0.12**
- Evidence: Sample correlation heatmap and gene expression heatmap were generated using pheatmap(v1.0.12).
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [ggplot2 v3.4.4] -> stage not stated [pheatmap v1.0.12]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: Heatmaps of selected targets were drawn using pheatmap and RColorBrewer in R, while three-way Venn diagrams of upregulated genes were generated using matplotlib-venn.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### Combined generalist and host-specific transcriptional strategies enable host generalism in the fungal pathogen &lt;i&gt;Botrytis cinerea&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2521414123 | PMCID: PMC13214029 | PMID: 42154555
- Evidence: The heatmap was generated using the pheatmap package in R.
- Full pipeline: stage not stated [pheatmap]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: The pheatmap package was used to create the heatmaps, and display log2foldchange values across samples.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### PMF proteins mediate mitochondrial fusion in Arabidopsis. (PNAS 2026)

- DOI: 10.1073/pnas.2601242123 | PMCID: PMC13123921 | PMID: 42018423
- Evidence: All statistical analysis was performed in Microsoft Excel Version 18.89.1 or in RStudio Version 2024.04.2 + 764 with R packages ggplot2 and pheatmap.
- Full pipeline: differential/statistical testing [ggplot2, pheatmap] -> stage not stated [AlphaFold, ImageJ]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Evidence: Correlation results were visualized as a heatmap using the pheatmap R package v.1.0.12 ( 78 ) with modules annotated along the axes to indicate those significantly correlated with environmental parameters.
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### The Nemp1-Nesprin complex mediates cellular responses to matrix mechanics. (PNAS 2026)

- DOI: 10.1073/pnas.2521253123 | PMCID: PMC12956887 | PMID: 41730104
- Version used: **1.0.12**
- Evidence: Additionally, the expression profile of the transcripts was visualized using pheatmap 1.0.12 ( 51 – 54 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [Salmon v1.8.0] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [R, clusterProfiler v4.10.1, edgeR] -> visualisation [pheatmap v1.0.12]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: Heatmaps were made using R package pheatmap ( 59 ) (v 1.0.12).
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Plant diversity influences plant volatile emission with varying effects at the species and community levels. (PNAS 2026)

- DOI: 10.1073/pnas.2518326123 | PMCID: PMC12818445 | PMID: 41538247
- Evidence: For data visualization, we used ggplot2 , ggeffects , ComplexHeatmap , and pheatmap ( 96 – 99 ).
- Full pipeline: differential/statistical testing [R v4.5.1, lme4, tidyverse] -> visualisation [ComplexHeatmap, R v4.5.1, ggplot2, pheatmap, tidyverse] -> stage not stated [mothur, phyloseq]

### Combination antiviral and anti-inflammatory therapy mitigates persistent neurological deficits in mice post SARS-CoV-2 infection. (PNAS 2026)

- DOI: 10.1073/pnas.2530209123 | PMCID: PMC12799161 | PMID: 41499397
- Evidence: Heatmaps using designated sets of DEGs were generated using pheatmap (R).
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.5, Seurat v5.3.0, pheatmap]

### mRNA vaccines induce durable immune memory to SARS-CoV-2 and variants of concern. (Science 2021)

- DOI: 10.1126/science.abm0829 | PMCID: PMC9284784 | PMID: 34648302
- Evidence: For heatmaps, data were visualized with pheatmap.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> simulation/modelling [UMAP] -> visualisation [UMAP, pheatmap]

