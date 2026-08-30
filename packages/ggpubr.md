# ggpubr

- **Category:** general
- **Papers in survey:** 83
- **Journals:** Nature (42), PNAS (24), Cell (15), Science (2)
- **Years:** 2021 (8), 2022 (9), 2023 (15), 2024 (12), 2025 (27), 2026 (12)
- **Versions named:** 0.4.0 (18), 0.6.0 (12), 0.5.0 (2), 0.4 (1), 0.4.0.999 (1), 0.2.5 (1)
- **Pipeline stages it appears in:** differential/statistical testing (23), visualisation (22), dimensionality reduction/clustering (4), quality control (1), quantification (1), simulation/modelling (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **0.4.0**
- Evidence: ...ndex.html R package clusterProfiler version 3.14.3 Yu et al., 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html R package ggpubr version 0.4.0 Kassambara, 2020 https://cran.r-project.org/web/packages/ggpubr/index.html R package tidyr version 1.1.2 Wickham, 2020 https://cran.r-project.org/web/packages/tidyr/index.html R package slingshot version 1.4.0 Street et al., 2018...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### High-resolution profiling of pathways of escape for SARS-CoV-2 spike-binding antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.045 | PMCID: PMC8096189 | PMID: 34010620
- Evidence: ...e/ SAMtools https://quay.io/biocontainers/samtools:1.3%5fh0592bc0_3 R (version 4.0.2) https://www.R-project.org/ tidyverse https://www.tidyverse.org/ ggpubr https://github.com/kassambara/ggpubr corrr https://github.com/tidymodels/corrr cowplot https://github.com/wilkelab/cowplot/ scales https://github.com/r-lib/scales rstatix https://github.com/kassambara/rstatix coin http://coin.r-forge.r-project...
- Full pipeline: stage not stated [Clustal Omega, Nextflow, R v4.0.2, SAMtools, ggpubr, tidyverse, xarray]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **0.2.5**
- Evidence: ...roject.org/web/packages/ggraph/index.html R package igraph version 1.2.4.2 R CRAN https://cran.r-project.org/web/packages/igraph/index.html R package ggpubr version 0.2.5 R CRAN https://cran.r-project.org/web/packages/ggpubr/index.html R package ggrepel version 0.8.2 R CRAN https://cran.r-project.org/web/packages/ggrepel/index.html R package circlize version 0.4.8 R CRAN https://cran.r-project.org...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **0.4.0**
- Evidence: VennDiagram 1.6.20, pheatmap 1.0.12, ggforce 0.3.3, ggpubr 0.4.0, RColorBrewer 1.1-2, proxy 0.4-26, reshape2 1.4.4, stringr 1.4.0, dplyr 1.0.7, purrr 0.3.4, readr 1.4.0, tidyr 1.1.3, tidyverse 1.3.1.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Germinal center responses to SARS-CoV-2 mRNA vaccines in healthy and immunocompromised individuals. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.027 | PMCID: PMC8808747 | PMID: 35202565
- Evidence: All statistical analysis was performed in R version 4.0.3, using the following packages: ggplot2, Semblance, multicross, crossmatchtest, dplyr, randtests, ggpubr, and merTools.
- Full pipeline: differential/statistical testing [ggplot2, ggpubr, tidyverse] -> stage not stated [R v4.0.3]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: 104 MA plot The MA plots were generated based on the DESeq2 (see above) results with the ggmaplot function ( https://rpkgs.datanovia.com/ggpubr/reference/ggmaplot.html ) from the R package ggpubr ( https://rpkgs.datanovia.com/ggpubr/ ).
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: 91 https://bioconductor.org/packages/release/bioc/html/scran.html ggscatter Alboukadel Kassambara https://doi.org/10.32614/CRAN.package.ggpubr Zen Black software v2.3 Zeiss https://www.zeiss.com/microscopy/en/products/software/zeiss-zen.html Zen Blue software v2.3 Zeiss https://www.zeiss.com/microscopy/en/products/software/zeiss-zen.html CellProfiler software v4.2.1 Carpenter et al.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **0.4.0**
- Evidence: ...en/v6.5.2/ R v.3.6.3 The Comprehensive R Archive Network https://cran.r-project.org/ R packages N/A seqinr v.4.2.5, tidyverse, v.1.3.1, knitr v.1.33, ggpubr v.0.4.0, DescTools v.0.99.41, gtools v.3.8.2, gridExtra v.2.3, cowplot v.1.1.1, scales v.1.1.1, grid v.3.6.3, broom v.0.7.6, e1071 v.1.7.6, and table1 v.1.4 Python packages N/A biopython v1.79, matplotlib v3.7.1, numpy v1.22.3, pandas v1.5.1, ...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Version used: **0.4.0**
- Evidence: Plots were generated using the package ggplot (v.3.3.6) or ggpubr (v.0.4.0), except where mentioned.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### The fork protection complex promotes parental histone recycling and epigenetic memory. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.017 | PMCID: PMC11383432 | PMID: 39094569
- Version used: **0.6.0**
- Evidence: Flow cytometry.fcs files extracted from Xcytoview were imported and visualised in R using packages flowCore (version 2.10.0), ggcyto (version 1.26.4), and ggpubr (version 0.6.0).
- Full pipeline: differential/statistical testing [R v4.2.2] -> visualisation [PyMOL v1.2r, ggpubr v0.6.0] -> stage not stated [AlphaFold, Bowtie2 v2.4.2, ChimeraX, MACS2, SAMtools v1.12, deepTools]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: Differences in A/T content between active and repressive compartments were statistically assessed using a Wilcoxon rank-sum test implemented in ggpubr R package (v.0.6.0) ( https://github.com/kassambara/ggpubr ).
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Human interpretable grammar encodes multicellular systems biology models to democratize virtual cell laboratories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.048 | PMCID: PMC13012569 | PMID: 40713951
- Evidence: We further estimate the relationship of the baseline TME composition on the ABM-simulated therapeutic response with a Pearson correlation computed with the R package ggpubr.
- Full pipeline: dimensionality reduction/clustering [R] -> simulation/modelling [R, ggpubr] -> stage not stated [ImageJ, Python, Seurat v4.1.0]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Using the R packages ggpubr and ggplot2, a scatter plot was generated to compare the average expression of each protein across the different experiments.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Phages communicate across species to shape microbial ecosystems. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.004 | PMCID: PMC13220667 | PMID: 41923642
- Evidence: ...leotides Please see Table S5 N/A Software and algorithms R R Core Team 31 https://www.R-project.org/ ggplot2 Wickham 32 https://ggplot2.tidyverse.org ggpubr Kassambara.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, IQ-TREE, R, ggplot2, ggpubr, tidyverse]

### Molecular features of human pathological tau distinguish tauopathy-associated dementias. (Cell 2026)

- DOI: 10.1016/j.cell.2025.12.036 | PMCID: PMC13075643 | PMID: 41616780
- Version used: **0.4.0**
- Evidence: Analyses were performed and figures were created in R (v4.1.0) using RStudio (v1.4.1717) with the packages R.utils (v2.11.0), stringr (v1.4.0), GetoptLong (v1.0.5), reshape2 (v1.4.4), circlize (v0.4.13), ComplexHeatmap (v2.11.1), dendsort (v0.3.4), dendextend (v1.15.2), ggplot2 (v3.3.5), ggpubr (v0.4.0), ggdendro (v0.1.22), ggpmisc (v0.4.5), scales (v1.1.1), and gridExtra (v2.3).
- Full pipeline: visualisation [ComplexHeatmap v2.11.1, ggplot2 v3.3.5, ggpubr v0.4.0] -> stage not stated [R v4.1.0]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: Most of the statistical analysis and data visualization were performed in R using the packages tidyverse, ggplot2, purrr, tibble, dplyr, tidyr, stringr, readr, forcats, scales, grid, reshape2, Rtsne, ggfortify, factoextra, ggpubr, ggforce, ggrepel, RColorBrewer and pheatmap.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Apoptotic brown adipocytes enhance energy expenditure via extracellular inosine. (Nature 2022)

- DOI: 10.1038/s41586-022-05041-0 | PMCID: PMC9452294 | PMID: 35790189
- Version used: **0.4.0**
- Evidence: Correlations between gene expression of visceral and subcutaneous WATs of the human cohort were calculated using the R packages ggpubr (v.0.4.0) 54 , based on the Spearman correlation coefficient, and a confidence interval of 0.95.
- Full pipeline: normalisation [DESeq2 v1.32.0] -> stage not stated [MACS2, featureCounts v2.0.1, ggpubr v0.4.0]

### Enhanced fitness of SARS-CoV-2 variant of concern Alpha but not Beta. (Nature 2022)

- DOI: 10.1038/s41586-021-04342-0 | PMCID: PMC8828469 | PMID: 34937050
- Version used: **0.4.0**
- Evidence: Statistical analysis Statistical analysis was performed using GraphPad Prism 8 or R 35 (version 4.1), using the packages tidyverse 36 (v1.3.1), ggpubr (v0.4.0) and rstatix (v.0.7.0).
- Full pipeline: differential/statistical testing [ggpubr v0.4.0, tidyverse]

### Pre-existing polymerase-specific T cells expand in abortive seronegative SARS-CoV-2. (Nature 2022)

- DOI: 10.1038/s41586-021-04186-8 | PMCID: PMC8732273 | PMID: 34758478
- Version used: **0.4.0**
- Evidence: Significant differences between all pairwise combinations of ORF/NSP were assessed using the Wilcoxon rank-sum test implemented in compare_means() in the R package ggpubr v.0.4.0 (Extended Data Table 3 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [R, ggpubr v0.4.0]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Evidence: Statistical significance was assessed with the Wilcoxon test (ggpubr).
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### Global methane emissions from rivers and streams. (Nature 2023)

- DOI: 10.1038/s41586-023-06344-6 | PMCID: PMC10511311 | PMID: 37587344
- Version used: **0.4.0**
- Evidence: Packages used were dplyr (v.1.0.7) for data wrangling 53 , ggplot2 (v.3.3.5) for visualization 54 , lubridate (v.1.7.10) for temporal data 55 , corr (v.0.4.3) to assess correlations in the data 56 , ggtext (v.0.1.1) for labelling figures 57 , ggpubr (v.0.4.0) 58 and patchwork (v.1.1.1) 59 for composing multipaneled figures, sf (v.1.0.3) for spatial analysis of vector data 60 , terra (v.1.4.11) for...
- Full pipeline: machine learning [XGBoost] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4.0, tidyverse v1.0.7] -> stage not stated [R v0.3.2]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Evidence: Where indicated, statistical tests were performed using two-sided t -tests in R (v.4.2.2) implemented in the ggpubr package (v.0.6.0) using a significance level of 0.05.
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Version used: **0.4.0**
- Evidence: R plots used native plotting capabilities of the aforementioned packages together with ggplot2 (v.3.3.5), ggpubr (v.0.4.0) and ComplexHeatmap 42 (v.2.6.2) packages.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **0.4**
- Evidence: For general visualisation purposes, R packages ggplot2 (v3.3.5) 69 , ggpubr (v0.4) 70 , ggrepel (v0.9.2) 71 , ggbeeswarm (v.0.6.0) 72 , scales (v1.2.1.) 73 , ggforce (v0.4.1) 74 , and cowplot (v1.1.1) 75 were used.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **0.4.0**
- Evidence: Unless stated otherwise, plots were generated in the R environment (v.3.6.3), using ggplot2 (v.3.2.1) 64 , ggpubr (v.0.4.0), cowplot (v.1.0.0), scales(v.1.0.0) and ggrepel (v.0.8.1).
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **0.4.0**
- Evidence: Statistical analysis Statistical analyses and graphical representations were performed in R using packages vegan (version 2.5–7), phyloseq (v1.28.0) 126 , QuantPsyc (v1.5), ggplot2 (v3.3.3), ggpubr (v0.4.0) and corrplot (v0.84).
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Migrating is not enough for modern planktonic foraminifera in a changing ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-08191-5 | PMCID: PMC11634771 | PMID: 39537925
- Evidence: The viridis package supplied colourblind-friendly colour palettes 74 , and tidyr enabled easier data cleaning and wrangling 75 . ggplot2 and ggpubr were used to create high-quality graphics 76 , 77 , with reshape2 and reshape facilitating the reshaping of the data structures 78 .
- Full pipeline: stage not stated [ggplot2, ggpubr, pheatmap, tidyverse]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Evidence: Kruskal–Wallis test performed in the R package ggpubr and stat_compare_means function.
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Statistical information Data were plotted in R (v.2022.07.01 and 554 running R v.4.0.3 (2020-10-10)) using the dplyr, ggplot2, tidyr, cowplot, reshape2, ggrepel, ggpubr, scales and RColorBrewer packages (versions dplyr_1.0.4, ggplot2_3.3.3, tidyr_1.1.2, cowplot_1.1.1, scales_1.1.1, reshape2_1.4.4, ggrepel_0.9.1, ggpubr_0.4.0, scales_1.1.1, RColorBrewer_1.1-2) or Microsoft Excel for Mac (v.16).
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Figures were created using ggplot, ggnewscale, ggpattern, ggrepel, ggsflabel, ggspatial, ggpubr, cowplot, matplotlib, plotly ( https://plot.ly ), seaborn and TMB_plotter 98 – 108 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Version used: **0.6.0**
- Evidence: Figures were generated using R (4.3.1) packages ggplot2 (3.4.3) and ggpubr (0.6.0) 58 .
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **0.5.0**
- Evidence: ..., dplyr (v.1.1.2) 143 , gdata (v.2.19.0) 144 , ggforce (v.0.4.1) 145 , ggplot2 (v.3.4.2) 146 , ggpmisc (v.0.5.3) 147 , ggpointdensity (v.0.1.0) 148 , ggpubr (v.0.5.0) 149 , ggrastr (v.1.0.2) 150 , ggrepel (v.0.9.3) 151 , grid (v.4.1.3) 152 , gridExtra (v.2.3) 153 , gtable (v.0.3.3) 154 , matrixStats (v.0.63.0) 155 , pheatmap (v.1.0.12) 156 , plyr (v.1.8.8) 157 , purrr (v.1.0.1) 158 , RColorBrewer ...
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Evidence: Statistical analyses If not stated otherwise, P values were generated using the ‘stat_compare_means’ function from the ‘ggpubr’ package (v0.6.0), applying the wilcox.test method.
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **0.6.0**
- Evidence: ...unohistochemistry and IMC data, which were conducted using R (v4.2.3) using R-studio build 513 with the packages: tidyverse (v2.0), ggplot2 (v3.4.2), ggpubr (v0.6.0) and pheatmap (v1.0.12).
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Version used: **0.4.0**
- Evidence: Pearson’s correlation test between host ANI and phage pair inducibility as well as Kendall’s rank correlation between the number prophages within lysogens and prophage inducibility was calculated and plotted using the R ggpubr (v.0.4.0) package.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### Doughnut of social and planetary boundaries monitors a world out of balance. (Nature 2025)

- DOI: 10.1038/s41586-025-09385-1 | PMCID: PMC12488500 | PMID: 41034533
- Evidence: We also used the zoo package (v1.8-12) for time-series analysis functionality, the lmtest package (v0.9.40) and the sandwich package (v3.1.1) for statistical analysis, the jsonlite package (v1.8.9) to convert vector data to nested json format and the ggpubr package (v0.6.0) for further data visualization functionality.
- Full pipeline: differential/statistical testing [ggpubr] -> visualisation [ggpubr, tidyverse]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Regression between adenosine-ending codon and protein levels were calculated with the R function stat_cor (package ggpubr) to compute Pearson’s r and geom_smooth (package ggplot2) using ‘linear model’ to display the regression line.
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Version used: **0.6.0**
- Evidence: The following packages were used: CellRanger v.6.0.1, singleCellTK v.2.8.0, Seurat v.4.3.0, scater v.1.24.0, harmony v.0.1.1, RColorBrewer v.1.1.3, ComplexHeatmap v.2.14.0, ArchR v.1.0.2, muscat v.1.12.1, readr v.2.1.4, ggplot2 v.3.4.2, ggsignif v.0.6.4, ggpubr v.0.6.0, magrittr v.2.0.3, scCoda v.0.1.9 Python package, celda v.1.19.1 and hdWGCNA v.0.4.5.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: The application was written and developed with the Shiny R package, and data visualizations were made possible with the following packages: shiny, tidyverse, ggpubr, visNetwork, png, dqshiny, DT, gsubfn, shinyjs, glue, shinydashboard and plotly.
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Additional R packages used include Presto, DESeq2, dplyr, ply, ape, cowplot, Matrix, variancePartition, MAST, HGNChelper, openxlsx, RColorBrewer, gridExtra, ggpubr, ComplexHeatmap, tidyverse, tibble, biomaRt, data.table, glmGamPoi, SeuratWrappers, patchwork, magrittr, s2, gplots, stringr, ggnewscale, ggbreak, coin and dunn.test.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: Plots were produced using the Seurat 57 , ggplot2 63 , ggpubr 64 and pheatmap 65 R packages.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **0.4.0**
- Evidence: ...23.0), cluster (2.1.1), fpc (2.2-9), plyr (1.8.6), dplyr (1.0.5), pvclust (2.2-0), ggrepel (0.9.1), amap (0.8-18), gProfileR (0.7.0), xtable (1.8-4), ggpubr (0.4.0), tidyr (1.1.3), DESeq2 (1.30.1), ReactomePA (1.34.0), stringr (1.4.0), Org.Hs.eg.db (3.12.0), pathfindR (1.6.1), CompGO (1.26), EnhancedVolcano (1.8.0) and GeneBook (1.0).
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **0.6.0**
- Evidence: The R package ComplexHeatmap (v.2.11.1) was used to generate heat maps, and visualization was facilitated using ggplot2 (v.3.3.5), ggpubr (v.0.6.0), ggrepel (v.0.9.2), Statannot (v.0.6.0), Circlize (v.0.4.16), GseaVis (v.0.0.5), Enrichplot (v.1.22.0), GridExtra (v.2.3.0), Pheatmap(v.1.0.12) and DEGreport (v.1.38.5) R packages.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Graphical panels were assembled into a single graphic using ggpubr ( https://cran.r-project.org/package=ggpubr ).
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Version used: **0.6.0**
- Evidence: The Wilcoxon signed-rank test was used to compare the ssGSEA scores using the stat_compare_means function from the ggpubr (v.0.6.0) package.
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### Targeting the SHOC2-RAS interaction in RAS-mutant cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-08931-1 | PMCID: PMC12137120 | PMID: 40335703
- Version used: **0.4.0**
- Evidence: Figures and fgsea analysis were created with R v.4.1.0 using the R packages fgsea v.1.18.0, ggplot2 v.3.3.6, cowplot v.1.1.1 and ggpubr v.0.4.0.
- Full pipeline: differential/statistical testing [DESeq2, edgeR] -> stage not stated [Picard, R, fgsea, ggplot2 v3.3.6, ggpubr v0.4.0]

### GABAergic neuron-to-glioma synapses in diffuse midline gliomas. (Nature 2025)

- DOI: 10.1038/s41586-024-08579-3 | PMCID: PMC11946904 | PMID: 39972132
- Evidence: The P values were calculated using Wilcoxon rank-sum test by stat_compare_means by the ggpubr package.
- Full pipeline: quantification [ImageJ v2.1.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [ggpubr]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Evidence: Further analysis and visualization were done in R 74 using tidyverse 75 and ggpubr 76 .
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Produces quality control density plots for each preprocessing step and publication-ready box plots with statistical comparisons using ggpubr.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Genome-wide sweeps create ecological units in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-026-10476-w | PMCID: PMC13322978 | PMID: 42092154
- Version used: **0.6.0**
- Evidence: Statistical analysis Statistical analyses and graphical representations were performed in R (v.4.2.1) 80 using base R statistical functions and ggplot2 (v.3.5.1) 81 , ggpubr (v.0.6.0) 82 , ggtree (v.3.4.4) 83 , ggtreeExtra (v.1.6.1) 84 and ComplexHeatmap (v.2.12.1) 85 .
- Full pipeline: alignment/mapping [MetaPhlAn v4.0.6] -> differential/statistical testing [ComplexHeatmap v2.12.1, ggplot2 v3.5.1, ggpubr v0.6.0] -> stage not stated [Prokka v1.14.6, R, SciPy]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Version used: **0.6.0**
- Evidence: Paired box plots and box plots were generated using the packages ggpubr (0.6.0) and ggplot2 (3.4.4).
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **0.6.0**
- Evidence: Statistics and reproducibility Statistical analysis was performed as noted in the figure legends using R (R base (v.4.2.0 or later), ggplot2 (v.3.5.1), ggpubr (v.0.6.0) Seurat (v.5.0.1)) and GraphPad Prism (v.10.4.1).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Polyclonal selection of immune checkpoint mutations in thyroid autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10493-9 | PMCID: PMC13233322 | PMID: 41981327
- Evidence: ....0), stringi 95 (v.1.8.7), gtools 96 (v.3.9.5), drc 69 (v.3.0-1), pander 97 (v.0.6.6), ape 98 (v.5.8-1), ggtree 99 (v.4.0.4), ggh4x 100 (v.0.3.1) and ggpubr 101 (v.0.6.2).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [R, Seurat, ggpubr, tidyverse]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Version used: **0.4.0**
- Evidence: 5d were acquired using the provided download function. scRNA-seq data analysis All plots and visualizations were performed using Seurat 76 v.4.1.1, ggpubr v.0.4.0 or ggplot2 (ref.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: Quantification and statistical analysis Data were plotted in R (version 4.4.2 (2024-06-14)) using the ggplot2, tidyr, dplyr, ggpubr and Hmisc toolkits (versions ggplot2_3.5.1, tidyr_1.3.1, dplyr_1.1.4, ggpubr_0.6.0, Hmisc_5.2.1), Python (version 3.12.9) using the pandas, scipy, scikit-learn, matplotlib and seaborn packages (versions pandas_2.2.3, scipy_1.14.1, scikit-learn_1.5.2, matplotlib_3.9.2,...
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: Plots were made using ggplot from tidyverse 93 v.2.0.0, patchwork 165 v.1.2.0, ggpmisc 166 v.0.5.6, ggpubr 167 v.0.6.0 and ggtext 168 v.0.1.2 and combined using Adobe Illustrator 2024 and Inkscape v.1.4.2.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **0.6.0**
- Evidence: Boxplots were created using ggplot2 (v3.5.1 or v3.5.2) and ggbeeswarm (v0.7.2) with statistical annotation created by ggpubr (v0.6.0), method = ‘t-test’.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Reprogrammed transsulfuration promotes basal-like breast tumor progression via realigning cellular cysteine persulfidation. (PNAS 2021)

- DOI: 10.1073/pnas.2100050118 | PMCID: PMC8609449 | PMID: 34737229
- Evidence: All analyses were performed in R using the following packages: ggpubr, ggExtra, ComplexHeatmap, circlize, corrr, hyper, DEqMS, and patchwork.
- Full pipeline: differential/statistical testing [R] -> stage not stated [ComplexHeatmap, ImageJ, ggpubr]

### Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself. (PNAS 2021)

- DOI: 10.1073/pnas.2100542118 | PMCID: PMC8449404 | PMID: 34507984
- Evidence: We used the ggplot2 ( 72 ), ggpubr, grid, gridExtra, ggsci, scales, png, ComplexHeatmap ( 73 ), and ggrepel R libraries for visualization.
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [R v3.6.3] -> visualisation [ComplexHeatmap, ggplot2, ggpubr] -> stage not stated [Clustal Omega v1.2]

### Incipient genome erosion and metabolic streamlining for antibiotic production in a defensive symbiont. (PNAS 2021)

- DOI: 10.1073/pnas.2023047118 | PMCID: PMC8092579 | PMID: 33883280
- Evidence: All other graphs were created using ggplot2 and ggpubr ( 97 ).
- Full pipeline: quality control [Bowtie2 v2.3.2, StringTie v1.3.3] -> read trimming [Bowtie2 v2.3.2, StringTie v1.3.3] -> alignment/mapping [Bowtie2 v2.3.2, StringTie v1.3.3] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [BLAST, ggplot2, ggpubr]

### Estimating maximal microbial growth rates from cultures, metagenomes, and single cells via codon usage patterns. (PNAS 2021)

- DOI: 10.1073/pnas.2016810118 | PMCID: PMC8000110 | PMID: 33723043
- Evidence: All figures were made using R packages ggplot2 and ggpubr ( 81 , 82 ).
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [RAxML] -> visualisation [ggplot2, ggpubr] -> stage not stated [R, ape (R)]

### Tissue-specific regulation of lipid polyester synthesis genes controlling oxygen permeation into <i>Lotus japonicus</i> nodules. (PNAS 2022)

- DOI: 10.1073/pnas.2206291119 | PMCID: PMC9704718 | PMID: 36375074
- Version used: **0.4.0.999**
- Evidence: Pairwise comparisons were performed using the function compare_means within the package ggpubr v.0.4.0.999 ( 73 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [ImageJ] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, R] -> stage not stated [RAxML, ggpubr v0.4.0.999, pheatmap]

### Motor learning without movement. (PNAS 2022)

- DOI: 10.1073/pnas.2204379119 | PMCID: PMC9335319 | PMID: 35858450
- Evidence: Statistical tests were conducted in R (version 4.0.3): packages rstatix ( 71 ), coin ( 72 ), MuMIn ( 73 ), lmerTest ( 74 ), lme4 ( 75 ), r2glmm ( 76 ), emmeans ( 77 ), effsize ( 78 ), effectsize ( 79 ), magrittr ( 80 ), ggplot2 ( 81 ), ggpubr ( 82 ), and ggeffects ( 83 ).
- Full pipeline: differential/statistical testing [R v4.0.3, emmeans, ggplot2, ggpubr, lme4] -> stage not stated [Python v3.8.5]

### Activating STING1-dependent immune signaling in <i>TP53</i> mutant and wild-type acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2123227119 | PMCID: PMC9271208 | PMID: 35759659
- Evidence: We used The Wilcoxon rank sum test as implemented in the stat_compare_means function of the ggpubr package to evaluate the statistical significance of log-transformed STING1 gene expression distributional differences.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [ggpubr] -> stage not stated [GSEA, R, STRING db, fgsea]

### Stone Age <i>Yersinia pestis</i> genomes shed light on the early evolution, diversity, and ecology of plague. (PNAS 2022)

- DOI: 10.1073/pnas.2116722119 | PMCID: PMC9169917 | PMID: 35412864
- Evidence: The final figure was generated in R using the ggpubr package ( 42 ).
- Full pipeline: variant calling [GATK, Picard] -> differential/statistical testing [GATK, Picard] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.25.0, RAxML v0.9.0, ggpubr]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **0.4.0**
- Evidence: Packages ggplot2 v3.3.6, ggpubr v0.4.0 pheatmap v1.0.12, RColorBrewer v1.1-3, ggsignif v0.6.3, and tidyverse v1.3.1 were used for data manipulation and representation.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Proteome-wide tagging with an H&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;2&lt;/sub&gt; biosensor reveals highly localized and dynamic redox microenvironments. (PNAS 2023)

- DOI: 10.1073/pnas.2314043120 | PMCID: PMC10691247 | PMID: 37991942
- Evidence: Packages viridis, ggrepel, ggpubr, and cowplot were used for plotting.
- Full pipeline: stage not stated [ggplot2, ggpubr, tidyverse]

### Resolvin D1 prevents injurious neutrophil swarming in transplanted lungs. (PNAS 2023)

- DOI: 10.1073/pnas.2302938120 | PMCID: PMC10400944 | PMID: 37487095
- Evidence: Differential gene expression of violin plots for individual genes between treatment groups was performed using pairwise comparisons using Wilcox test through the ggpubr package.
- Full pipeline: quality control [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Enrichr, ggpubr] -> stage not stated [Seurat v4.0.0]

### Increased gene expression variability hinders the formation of regional mechanical conflicts leading to reduced organ shape robustness. (PNAS 2023)

- DOI: 10.1073/pnas.2302441120 | PMCID: PMC10372692 | PMID: 37459526
- Evidence: Graphs were created in R using ggpubr ( 69 ) and rstatix ( 70 ) packages, or the online tool PlotsOfData ( 71 ), or in Microsoft Excel.
- Full pipeline: differential/statistical testing [R] -> stage not stated [ImageJ, ggpubr]

### Estimating human mobility in Holocene Western Eurasia with large-scale ancient genomic data. (PNAS 2023)

- DOI: 10.1073/pnas.2218375120 | PMCID: PMC9992830 | PMID: 36821583
- Evidence: All data analysis and plotting was done in R ( 87 ) with the following packages: checkmate ( 88 ), cowplot ( 89 ), fractional ( 90 ), future ( 91 ), ggh4x ( 92 ), ggnewscale ( 93 ), ggpubr ( 94 ), ggrepel ( 95 ), ggridges ( 96 ), igraph ( 97 ), khroma ( 98 ), latex2exp ( 99 ), lemon ( 100 ), progress ( 101 ), rnaturalearth ( 102 ), sf ( 103 ), smartsnp ( 104 ), viridis ( 105 ), and, finally, the t...
- Full pipeline: quality control [ANGSD] -> stage not stated [R, ggpubr, igraph, tidyverse]

### Discovery of a rapidly evolving yeast defense factor, &lt;i&gt;KTD1&lt;/i&gt;, against the secreted killer toxin K28. (PNAS 2023)

- DOI: 10.1073/pnas.2217194120 | PMCID: PMC9974470 | PMID: 36800387
- Evidence: Jittered one-dimensional scatter plots were generated using the ggboxplot function in R package ggpubr.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ggpubr] -> visualisation [AlphaFold v2.0.0, PyMOL v2.3.0] -> stage not stated [BLAST, R, ggplot2 v3.3.5]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Evidence: Plots were realized with ggpubr ( 66 ). minION Sequencing. nCATS was performed as in ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### Proteins required for stereocilia elongation during mammalian hair cell development ensure precise and steady heights during adult life. (PNAS 2024)

- DOI: 10.1073/pnas.2405455121 | PMCID: PMC11459194 | PMID: 39320919
- Evidence: Analyses and visualizations were done in R 3.6.2 with tidyverse, ggpubr, and rstatix packages.
- Full pipeline: visualisation [R v3.6, ggpubr, tidyverse] -> stage not stated [ImageJ]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: We compared snow leopard heterozygosity calculated from SNPs called using our pipeline to heterozygosity calculated from SNPs called by Gencove using Pearson correlation coefficient calculated using the ggpubr ( 98 ) package in R ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Founders predict trait evolution and population performance after evolutionary rescue in the red flour beetle. (PNAS 2025)

- DOI: 10.1073/pnas.2506244122 | PMCID: PMC12435296 | PMID: 40906810
- Evidence: Packages used for analysis and visualization were ggplot2, gridExtra, paletteer, dplyr, tidyr, forcats, hrbrthemes, viridis, corrplot, RColorBrewer, survival, sjstats, segmented, broom, ggpubr, MASS, and vegan.
- Full pipeline: visualisation [ggplot2, ggpubr, tidyverse] -> stage not stated [R v3.4.4]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Evidence: We counted seeds from the five most productive tillers and performed pairwise comparisons using the “t_test” function from the “ggpubr” and “rstatix” R packages, with P -values adjusted by the Bonferroni method.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### Evolution and evolvability of rifampicin resistance across the bacterial tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2424307122 | PMCID: PMC12337354 | PMID: 40737327
- Version used: **0.6.0**
- Evidence: Data wrangling and visualization were performed using packages tidyverse v2.0.0 ( 73 ), ggnewscale v0.4.10 ( 74 ), GGally v2.2.1 ( 75 ), ggpubr v0.6.0 ( 76 ), ggh4x v0.2.8 ( 77 ), RColorBrewer v1.1-3 ( 78 ), patchwork v1.2.0 ( 79 ), NGLvieweR ( 80 ), and htmlwidgets ( 81 ).
- Full pipeline: visualisation [ggpubr v0.6.0, tidyverse v2.0.0] -> stage not stated [R v4.4.1]

### The oncoprotein SET promotes serine-derived one-carbon metabolism by regulating SHMT2 enzymatic activity. (PNAS 2025)

- DOI: 10.1073/pnas.2412854122 | PMCID: PMC12088392 | PMID: 40339130
- Evidence: The R packages of ggplot2 and ggpubr were used for data visualization.
- Full pipeline: visualisation [ggplot2, ggpubr]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Version used: **0.5.0**
- Evidence: Statistical analysis of flow cytometry data was performed in GraphPad Prism (v 9.1.0) or in R using ggpubr (v 0.5.0) Kruskal–Wallis test, or Wilcoxon test with Bonferroni correction as indicated in the individual figure legends.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### Mycorrhiza increases plant diversity and soil carbon storage in grasslands. (PNAS 2025)

- DOI: 10.1073/pnas.2412556122 | PMCID: PMC11848320 | PMID: 39937867
- Version used: **0.4.0**
- Evidence: All statistical analyses except SEM were conducted in R, and the following packages: argicolae v.1.3-5, lme4 v.1.1-30, ggtext v.0.1.1, ggplot2 v.3.3.5, ggpubr v.0.4.0, tidyr v.1.1.4, and vegan v.2.5-7 were used.
- Full pipeline: differential/statistical testing [ggplot2 v3.3.5, ggpubr v0.4.0, lme4 v1.1, tidyverse v1.1.4]

### Egress thresholds and wildfire fatalities. (PNAS 2026)

- DOI: 10.1073/pnas.2535081123 | PMCID: PMC13250580 | PMID: 42224582
- Evidence: R analyses relied on the following packages: tidyverse, sf, rnaturalearth, rnaturalearthdata, RColorBrewer, scales, tidycensus, ggpubr, biscale, dplyr, ggplot2, and minpack.lm.
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, R v4.4.0, ggplot2, ggpubr, tidyverse]

### Molecular determinants of ligand efficacy and potency in GPCR signaling. (Science 2023)

- DOI: 10.1126/science.adh1859 | PMCID: PMC7615523 | PMID: 38127743
- Evidence: The following packages were used: tidyverse (especially dplyr, ggplot2, purrr, tibble, tidyr, forcats, stringr), plotly, MASS, reshape, reshape2, ggrepel, patchwork, ggpubr, bio3d ( 53 ), openxlsx.
- Full pipeline: stage not stated [GROMACS, MDTraj, PyMOL v2.5.2, R v4.0, ggplot2, ggpubr, tidyverse]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Version used: **0.6.0**
- Evidence: Data visualization employed ggplot2 v3.5.1 and ggpubr v0.6.0, with boxplots displaying median ± interquartile range.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

