# scikit-learn

- **Category:** general
- **Papers in survey:** 322
- **Journals:** Nature (156), PNAS (132), Cell (22), Science (12)
- **Years:** 2021 (26), 2022 (43), 2023 (60), 2024 (72), 2025 (83), 2026 (38)
- **Versions named:** 1.0.2 (8), 1.2.2 (5), 0.21.3 (5), 0.24.2 (4), 0.22 (3), 1.3.2 (3), 1.3.0 (2), 1.6.1 (2), 0.24.1 (2), 0.0 (2)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (81), machine learning (65), differential/statistical testing (54), normalisation (19), visualisation (16), quantification (7), simulation/modelling (3), alignment/mapping (3), variant calling (2), quality control (2)

## Papers

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: ...ython-louvain UMAP McInnes et al., 2018 https://umap-learn.readthedocs.io/en/latest/ scikit-image van der Walt et al., 2014 https://scikit-image.org/ scikit-learn Pedregosa et al., 2012 https://scikit-learn.org vigra N/A http://ukoethe.github.io/vigra/ mahotas Coelho, 2012 https://mahotas.readthedocs.io/en/latest/ networkx Hagberg et al., 2008 https://networkx.org/ pandas McKinney, 2010 https://pa...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### Functional diversity for body actions in the mesencephalic locomotor region. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.002 | PMCID: PMC8382160 | PMID: 34302739
- Evidence: For decoding analyses, we used scikit-learn, a Python library for statistical learning and glmnet (version 2.2.1), a Python wrapper for the fortran library used in the homonymous R package.
- Full pipeline: differential/statistical testing [R, scikit-learn] -> visualisation [seaborn] -> stage not stated [DeepLabCut, Python v3.7, SciPy, ilastik v1.1.5]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: PCA was performed using scikit-learn ( Pedregosa et al., 2011 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 82 https://github.com/satijalab/seurat sklearn (version: 0.24.2) Pedregosa et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: Regarding plotting, we adapted an approach from the scikit-learn python package ( https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html ) in R to estimate the average AUROC and AUPR curves among their 10 repeated iterations.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Mapping transcriptomic vector fields of single cells. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.045 | PMCID: PMC9332140 | PMID: 35108499
- Evidence: To globally quantify the accuracy of our LAP method in prioritizing TFs of cell fate transitions, we used the roc_curve function from sklearn ( Pedregosa et al., 2011 ) to perform a universal ROC (receiver operating characteristic) curve analysis using priority scores from all transitions.
- Full pipeline: quantification [scVelo, scikit-learn] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [SciPy]

### Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.018 | PMCID: PMC8786601 | PMID: 35148837
- Version used: **1.0**
- Evidence: For the principal component analysis (PCA) we log-transformed, calculated z-scores, and ran PCA on MSD antibody concentration measurements or Wuhan-Hu-1/variant RBD IgG concentration ratios from a reference time point after COVID-19 vaccination or SARS-CoV-2 infection using Python v3.7.10 and packages numpy v1.19.1, pandas v1.2.5, and scikit-learn v1.0.
- Full pipeline: dimensionality reduction/clustering [NumPy v1.19.1, scikit-learn v1.0] -> visualisation [SciPy v1.6.2] -> stage not stated [Matplotlib v3.3.2, QuPath v0.2.3, R v4.0.5, ggplot2, seaborn v0.11.2]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Version used: **0.24.2**
- Evidence: .../blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins Lifelines v0.26.0 (Python package) Davidson-Pilon, 2021 https://github.com/CamDavidsonPilon/lifelines scikit-learn v0.24.2 (Python package) Pedregosa et al., 2011 https://github.com/scikit-learn/scikit-learn IgBLAST Ye et al., 2013 https://www.ncbi.nlm.nih.gov/igblast/ Immunarch v0.6.5 (R package) ImmunoMind Team, 2019 https://immunarch.com/ IsoSpeak...
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ... al., 2018 ) https://github.com/theislab/scanpy Scater ( McCarthy et al., 2017 ) v3.12 http://bioconductor.org/packages/release/bioc/html/scater.html Scikit-learn ( Pedregosa et al., 2011 ) https://github.com/scikit-learn/scikit-learn Scipy ( Virtanen et al., 2020 ) https://scipy.org/ ScVelo ( Bergen et al., 2020 ) v0.1.24 https://github.com/theislab/scvelo Sparse Decomposition of Arrays ( Hore et...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: ...ml version 1.20.0 FIREcaller https://github.com/yycunc/FIREcaller version 1.40 Python Python Software Foundation, https://www.python.org/ version 3.9 Scikit-learn https://scikit-learn.org/ Version 0.24.0 Biorender https://biorender.com Other QX200 Droplet Digital PCR System Bio-Rad https://www.bio-rad.com/en-us/life-science/digital-pcr/qx200-droplet-digital-pcr-system C1000 Touch Thermal Cycler wi...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: KNN imputation was our method of choice using KNNImputer (n_neighbors=5) from the sklearn package (v.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Structural and functional map for forelimb movement phases between cortex and medulla. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.009 | PMCID: PMC9842395 | PMID: 36608651
- Evidence: To perform spatial correlation analysis, the density of synapses (binning into 100x100 pixels for each injection site) from one or multiple sections calculated using 2D-KDE was vectorized, and a correlogram was formed by calculating pairwise cosine similarity (scikit-learn library) between any two injection sites.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [DeepLabCut, Kilosort, Python v3.7, SciPy, TrackMate v6.0.3, scikit-learn]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: For each individual astrocyte or microglial cell, the nearest neighbor of a particular comparison cell type was identified within a radius of 80 μm of that astrocyte or microglia using a k D-tree search implemented in scikit-learn.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Evidence: Several types of algorithms were used, including logistic regression, neural networks, support-vector machines, and decision trees (implemented with one-hot encoding in Scikit-learn).
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Version used: **0.19.1**
- Evidence: We then applied factor analysis using the scikit-learn 0.19.1 package ( https://pypi.org/project/scikit-learn/ ).
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: For box plot in Figure S3J , pairwise Euclidean distances were computed to approximate phenotypic distance based on diffusion embeddings using sklearn.metrics.pairwise_distances 221 and plotted with matplotlib.boxplot .
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: These quantitative data were exported to Python for further statistical analysis and data visualization, utilizing the scikit-learn and seaborn libraries.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Inner speech in motor cortex and implications for speech neuroprostheses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.015 | PMCID: PMC12360486 | PMID: 40816265
- Version used: **1.3.2**
- Evidence: ...wnloads/ RRID:SCR_008394 SciPy 1.11.4 scipy.org RRID:SCR_008058 NumPy 1.26.2 numpy.org RRID:SCR_008633 Pandas 2.1.3 pandas.pydata.org RRID:SCR_018214 scikit-learn 1.3.2 scikit-learn.org RRID:SCR_002577 matplotlib 3.8.2 matplotlib.org RRID:SCR_008624 seaborn 0.13.0 seaborn.pydata.org RRID:SCR_018132 AWS Polly aws-cli/2.22.29 Amazon Web Services aws.amazon.com RRID:SCR_012854 Custom analysis code Re...
- Full pipeline: stage not stated [Matplotlib v3.8.2, NumPy v1.26.2, Python v3.9, SciPy v1.11.4, scikit-learn v1.3.2, seaborn v0.13.0]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: We then applied NMF, utilizing the sklearn.decomposition package in Python, to factorize the non-negative matrix V into two smaller non-negative matrices: the basis matrix W (with dimensions N × R ) and the coefficient matrix H (with dimensions R × M ), following methodologies used in prior research.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: To do this, we used scikit-learn’s Gaussian process regression package 70 to fit a gaussian process with an RBF kernel (with tunable scaling and length-scale) to the session-by-session metrics.
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### Nanoscale DNA tracing reveals the self-organization mechanism of mitotic chromosomes. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.028 | PMCID: PMC12127698 | PMID: 40132578
- Evidence: Full chromosome regions were segmented from regional barcodes using a random forest classifier (scikit-learn 55 ) trained on 5–10 small foreground and background regions in one field of view.
- Full pipeline: quantification [NumPy] -> normalisation [SciPy] -> simulation/modelling [NumPy, OpenMM] -> machine learning [scikit-learn] -> stage not stated [Python, napari, scikit-image]

### Rapid microbial methanogenesis during CO<sub>2</sub> storage in hydrocarbon reservoirs. (Nature 2021)

- DOI: 10.1038/s41586-021-04153-3 | PMCID: PMC8695373 | PMID: 34937895
- Evidence: Taxonomy was assigned to amplicon sequence variants using the q2‐feature‐classifier 51 classify‐sklearn Naïve Bayes taxonomy classifier against the Greengenes 13_8 99% operational taxonomic unit (OTU) reference sequences 52 .
- Full pipeline: read trimming [DADA2] -> machine learning [scikit-learn] -> stage not stated [QIIME 2 v2017.4]

### Cortical responses to touch reflect subcortical integration of LTMR signals. (Nature 2021)

- DOI: 10.1038/s41586-021-04094-x | PMCID: PMC9289451 | PMID: 34789880
- Evidence: PCA and k-means clustering was implemented with the scikit-learn python package.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Matplotlib v3.3.1, NumPy v1.18.5, SciPy v1.5.2, scikit-image v0.16.2, seaborn v0.11.0]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: Taxonomy was assigned to OTUs with a sklearn-based classifier 55 throughthe feature-classifier plugin 56 using the full-length 16S SILVA-SSU-132 database (QIIME-compatible release from April 2018; https://www.arb-silva.de/documentation/release-132/ ).
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: We adapted non-negative matrix factorization (Python package: sklearn 77 ) to decompose the cell-by-cCRE matrix V ( N × M , N rows: cCRE, M columns: cell clusters) into a coefficient matrix H ( R × M , R rows: number of modules) and a basis matrix W ( N × R ), with a given rank R : \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \u...
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Version used: **0.24.2**
- Evidence: We adapted NMF (Python package: sklearn v.0.24.2) to decompose the cluster-by-cCRE matrix V ( N × M , N rows: cCRE, M columns: cell clusters) into a coefficient matrix H ( R × M , R rows: number of modules) and a basis matrix W ( N × R ), with a given rank R : V ≈ WH .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Evidence: We then used the outlier-aware DBSCAN algorithm from the scikit-learn package to perform consensus clustering over the Leiden feature matrix using the hamming distance.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Human neocortical expansion involves glutamatergic neuron diversification. (Nature 2021)

- DOI: 10.1038/s41586-021-03813-8 | PMCID: PMC8494638 | PMID: 34616067
- Evidence: Analysis of features by t-type and species Combined datasets of electrophysiological and morphological features across homologous t-types from mouse and human were visualized by an analysis pipeline of data imputation and standardization, followed by projection to two dimensions using UMAP or SPCA (sklearn and umap python packages) 67 , 68 .
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [ImageJ] -> dimensionality reduction/clustering [Seurat, UMAP, scikit-learn] -> visualisation [scikit-learn] -> stage not stated [statsmodels]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Evidence: 1d ). t -SNE was computed using sklearn.manifold. t -SNE was generated with default parameters and random state 42.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **0.21.3**
- Evidence: We then used the outlier-aware DBSCAN algorithm from the scikit-learn v0.21.3 package (RRID SCR_002577) to perform consensus clustering over the Leiden feature matrix using the hamming distance.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### The structural basis of odorant recognition in insect olfactory receptors. (Nature 2021)

- DOI: 10.1038/s41586-021-03794-8 | PMCID: PMC8410599 | PMID: 34349260
- Evidence: A multiple regression analysis using the scikit-learn Linear Regression module was used to assess the accuracy with which the receptor activity could be predicted by individual descriptors (1-dimensional analysis) or combinations of two descriptors (2-dimensional analysis) (Extended Data Table 2 ).
- Full pipeline: alignment/mapping [MAFFT, MotionCor2, RELION v3.0] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, PyMOL]

### Swarm Learning for decentralized and confidential clinical machine learning. (Nature 2021)

- DOI: 10.1038/s41586-021-03583-3 | PMCID: PMC8189907 | PMID: 34040261
- Evidence: We used scikit-learn library version 0.23.1 to calculate values for the metrics.
- Full pipeline: alignment/mapping [kallisto v0.43.1] -> normalisation [DESeq2 v1.22.2, R] -> machine learning [Docker] -> stage not stated [Keras v2.3.1, TensorFlow v2.2.0, scikit-learn]

### Phenotypic variation of transcriptomic cell types in mouse motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-020-2907-3 | PMCID: PMC8113357 | PMID: 33184512
- Evidence: To estimate the rheobase (the minimum current needed to elicit any spikes), we used robust regression (random sample consensus algorithm, as implemented in sklearn.linear_model.RANSACRegressor) of the spiking frequency onto the injected current using the five lowest depolarizing currents with non-zero spike count (if there were fewer than five, we used those available).
- Full pipeline: alignment/mapping [STAR v2.5.4b] -> differential/statistical testing [scikit-learn] -> stage not stated [Python]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Evidence: Analyses and visualization of data were conducted in a Python environment built on the Numpy, SciPy, matplotlib, scikit-learn package and pandas libraries.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Personalizing exoskeleton assistance while walking in the real world. (Nature 2022)

- DOI: 10.1038/s41586-022-05191-1 | PMCID: PMC9556303 | PMID: 36224415
- Version used: **0.21.3**
- Evidence: The required python packages are numpy (1.17.4), scikit-learn (0.21.3), scipy (1.3.2) and matplotlib (2.0.2).
- Full pipeline: stage not stated [Matplotlib v2.0.2, NumPy v1.17.4, SciPy v1.3.2, scikit-learn v0.21.3]

### In vivo single-molecule analysis reveals COOLAIR RNA structural diversity. (Nature 2022)

- DOI: 10.1038/s41586-022-05135-9 | PMCID: PMC9452300 | PMID: 35978193
- Evidence: The dimensionality reduction results were clustered using k -means clustering with the k -means function from the scikit-learn Python package 32 .
- Full pipeline: dimensionality reduction/clustering [scikit-learn]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Evidence: Gaussian KDE To generate a kernel density estimate of BPNs in anatomical space, BPN coordinates were used to fit a Gaussian Kernel (sklearn.neighbors.KernelDensity(*, bandwidth = 10 (14 for 7 d.p.f.), algorithm=‘auto’, kernel=‘gaussian’, metric=‘euclidean’).
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: We then trained an SVM classifier (sklearn.svm.SVC) on human data and projected the cell type annotations onto the mouse datasets.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### BA.2.12.1, BA.4 and BA.5 escape antibodies elicited by Omicron infection. (Nature 2022)

- DOI: 10.1038/s41586-022-04980-y | PMCID: PMC9385493 | PMID: 35714668
- Evidence: Informative sites were selected using sklearn.feature_selection.VarianceThreshold of scikit-learn Python package (v0.24.2) with the variance threshold as 0.1.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.20, RELION v3.1, UCSF Chimera v1.16] -> visualisation [ChimeraX v1.3, R, Seurat] -> stage not stated [Pangolin, ggplot2 v3.3.3, scikit-learn]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Evidence: These analyses were performed in Python (v.3.6) using Scikit-learn for PCA (v.0.23.2), Scipy for hierarchical clustering (v.1.5.1) and nheatmap for heat map and clustering visualization (v.0.1.4).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Toroidal topology of population activity in grid cells. (Nature 2022)

- DOI: 10.1038/s41586-021-04268-7 | PMCID: PMC8810387 | PMID: 35022611
- Version used: **0.22.1**
- Evidence: Open-source Python packages used were: umap (version 0.3.10), ripser (0.4.1), numba (0.48.0), scipy (1.4.1), numpy (1.18.1), scikit-learn (0.22.1), matplotlib (3.1.3), h5py (2.10.0) and gudhi (3.4.1.post1).
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.1.3, NumPy v1.18.1, UMAP, scikit-learn v0.22.1] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, SciPy]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Version used: **0.21.2**
- Evidence: Predictor architecture The machine learning framework was built on Python (version 3.7.4) using the following libraries: scikit-learn (version 0.21.2), numpy (version 1.16.4), scipy (version 1.3), pandas (version 0.24.2) within a Singularity container (version 2.4.6-dist).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Molecularly defined and spatially resolved cell atlas of the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06808-9 | PMCID: PMC10719103 | PMID: 38092912
- Evidence: We began by finding the 50 spatially nearest neighbours for each cell using scikit-learn 73 .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose v2.0] -> stage not stated [CellChat, scDblFinder, scikit-learn]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Most functions were derived from the allcools 9 , scanpy 73 and scikit-learn 74 packages.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: The parameter resolution, which affected the number of clusters a lot, was selected from 0.1 to 2 with a step size 0.1 based on the silhouette coefficient 89 using the Python package Scikit-learn 90 .
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: 3 ) using the scikit-learn 68 python package.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: These analyses relied heavily on Numpy 57 , Scipy 58 , Pandas 59 , and Scikit-learn 60 .
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Version used: **0.24.2**
- Evidence: After each iteration, cells are clustered on doublet scores using the KMeans object (with parameters: n_clusters=2, init=‘k-means++’, n_init=10, and max_iter=10000) and fit_predict method using the Python package sklearn v.0.24.2.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Evidence: A matrix of edit distances was passed to sklearn DBSCAN to call clusters with an epsilon of 1 and minimum samples as 2.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **0.22**
- Evidence: ..., Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-image 0.18.1, squidpy 1.1.2, anndata 0.8.0 and itertools 8.0.0.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Cingulate dynamics track depression recovery with deep brain stimulation. (Nature 2023)

- DOI: 10.1038/s41586-023-06541-3 | PMCID: PMC10550829 | PMID: 37730990
- Version used: **1.1.1**
- Evidence: A random forest classifier with tenfold cross-validation was implemented in the Python sklearn (v.1.1.1) library 64 to discriminate the ‘sick’ from the ‘stable response’ state for each participant.
- Full pipeline: machine learning [PyTorch, scikit-learn v1.1.1] -> stage not stated [AFNI, FSL, Python v3.6]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Version used: **1.1.1**
- Evidence: For this, we trained the Isolation Forest outlier detection algorithm 59 as implemented in scikit-learn (v.1.1.1) 60 on the ProteinNet CASP12 FastText sentence embeddings with 1% contamination rate.
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### Dopamine and glutamate regulate striatal acetylcholine in decision-making. (Nature 2023)

- DOI: 10.1038/s41586-023-06492-9 | PMCID: PMC10511323 | PMID: 37557915
- Evidence: The sources for the least squares regression models are listed below: OLS: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html .
- Full pipeline: differential/statistical testing [scikit-learn]

### A spatially resolved timeline of the human maternal-fetal interface. (Nature 2023)

- DOI: 10.1038/s41586-023-06298-9 | PMCID: PMC10356615 | PMID: 37468587
- Evidence: Ridge regression for predicting GA from immune composition Ridge regression was implemented using the sklearn Python package (sklearn.linear_model.Ridge, RidgeCV).
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [limma, scikit-learn] -> stage not stated [ImageJ, Jupyter, Python, QuPath v0.4.0, R]

### Mega-scale experimental analysis of protein folding stability in biology and design. (Nature 2023)

- DOI: 10.1038/s41586-023-06328-6 | PMCID: PMC10412457 | PMID: 37468638
- Evidence: Using the data, we performed principal components analysis using the scikit-learn library implemented in Python 3.
- Full pipeline: read trimming [Cutadapt] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [AlphaFold, Python v3.9]

### Relaxed targeting rules help PIWI proteins silence transposons. (Nature 2023)

- DOI: 10.1038/s41586-023-06257-4 | PMCID: PMC10338343 | PMID: 37344600
- Evidence: The logistic function was fit using the Limited-memory Broyden–Fletcher–Goldfarb–Shanno algorithm (L-BFGS) implemented in LogisticRegression from the Python module scikit-learn 69 using L2-regularization ( λ = 1) with default parameters on acceptance of convergence and the maximum number of iterations set at 1,000.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> differential/statistical testing [DESeq2 v1.18.1, scikit-learn] -> stage not stated [SciPy v1.8.1]

### Injury prevents Ras mutant cell expansion in mosaic skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06198-y | PMCID: PMC10322723 | PMID: 37344586
- Version used: **0.24.2**
- Evidence: Next, the selected cells were scored for stress, immune and infundibulum related gene expression signatures (see the notebooks on GitHub: https://github.com/kasperlab/Gallini_et_al_2023_Nature ), classified with a Gaussian mixture model (scikit-learn, 0.24.2 67 ) and positive cells were filtered out.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Scanpy v1.6, Seurat, SoupX, scDblFinder, scikit-learn v0.24.2]

### Health system-scale language models are all-purpose prediction engines. (Nature 2023)

- DOI: 10.1038/s41586-023-06160-y | PMCID: PMC10338337 | PMID: 37286606
- Evidence: We used scikit-learn’s randomized search to search hyperparameters among minimum_child_weight from {1, 5, 10}, gamma from {0.5, 1, 1.5, 2, 5}, subsample from {0.6, 0.8, 1}, col_sample_bytree from {0.6, 0.8, 1.0}, max_depth from {3, 4, 5}, learning_rates from {0.001, 0.01, 0.1, 0.5} and n_estimators from {10, 100, 1000} for 100 iterations based on AUROC score (ovr-auroc score for multiple classes) ...
- Full pipeline: stage not stated [Matplotlib v3.5.2, Python v3.8.13, XGBoost, scikit-learn, seaborn v0.12.2]

### A broadband thermal emission spectrum of the ultra-hot Jupiter WASP-18b. (Nature 2023)

- DOI: 10.1038/s41586-023-06230-1 | PMCID: PMC10412449 | PMID: 37257843
- Evidence: We track the trend of these systematics throughout the observations by performing incremental principal components analysis (PCA) with the open-source scikit-learn 80 package on the processed detector images (Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [emcee] -> stage not stated [MOM6, dynesty, scikit-image]

### Learnable latent embeddings for joint behavioural and neural analysis. (Nature 2023)

- DOI: 10.1038/s41586-023-06031-6 | PMCID: PMC10172131 | PMID: 37138088
- Evidence: CEBRA API and example usage The Python implementation of CEBRA is written in PyTorch 55 and NumPy 56 and provides an application programming interface (API) that is fully compatible with scikit-learn 57 , a package commonly used for machine learning.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [NumPy, PyTorch, scikit-learn]

### De novo design of protein interactions with learned surface fingerprints. (Nature 2023)

- DOI: 10.1038/s41586-023-05993-x | PMCID: PMC10131520 | PMID: 37100904
- Evidence: To compute the angular coordinate, all pairwise geodesic distances between vertices in the patch are computed, and the multidimensional scaling algorithm 47 in scikit-learn 48 is then used to map all vertices to the 2D plane.
- Full pipeline: alignment/mapping [AlphaFold] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> structure determination [Coot v0.9.5] -> machine learning [TensorFlow v1.12] -> visualisation [ChimeraX] -> stage not stated [PHENIX v1.20.1, UCSF Chimera]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **0.0**
- Evidence: Classifier to predict seeding and non-seeding tumour regions We built the machine-learning framework in Python using Tensorflow (v.2.6.0) 104 and sklearn (v.0.0) 105 .
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Evidence: EGFR mutant cell foci were quantified from cell coordinate data by clustering cell positions by density using the DBSCAN algorithm, implemented in Python with the scikit-learn library 62 .
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Coordination of bacterial cell wall and outer membrane biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-05750-0 | PMCID: PMC9995270 | PMID: 36859542
- Version used: **1.0.2**
- Evidence: To estimate the percentage of interacting sequences in each clade, we fitted a two-component Gaussian mixture model using sklearn v1.0.2 (ref.
- Full pipeline: alignment/mapping [Python v3.8.8] -> quantification [ImageJ] -> visualisation [ChimeraX v1.1.1, Python v3.8.8] -> stage not stated [AlphaFold, scikit-learn v1.0.2]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: For the computational implementation of the above machine-learning models, we use a Python library, scikit-learn ( https://scikit-learn.org/stable/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Single-cell spatial immune landscapes of primary and metastatic brain tumours. (Nature 2023)

- DOI: 10.1038/s41586-022-05680-3 | PMCID: PMC9931580 | PMID: 36725935
- Evidence: Cellular neighbourhood discovery on glioblastoma and BrM-cores combined (performed in 2021) was performed using Scikit-learn, a software machine learning library for Python.
- Full pipeline: normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1] -> differential/statistical testing [Python v3.7.12] -> stage not stated [ImageJ v1.53k, scikit-learn]

### Single-cell spatial landscapes of the lung tumour immune microenvironment. (Nature 2023)

- DOI: 10.1038/s41586-022-05672-3 | PMCID: PMC9931585 | PMID: 36725934
- Evidence: 7a ) were clustered using Scikit-learn, a software machine-learning library for Python, and MiniBatchKMeans clustering algorithm version 0.24.2 with default batch size = 100 and random_state = 0.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> machine learning [Python v3.7.12] -> stage not stated [Keras, TensorFlow v2.8.0]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **1.0.2**
- Evidence: We then performed a quantile transformation of TPM values using scikit-learn (v.1.0.2) 133 and calculated the Jensen–Shannon divergence (JSD) value from (1) all single-copy orthologues, (2) the set single-copy transcription factor orthologues and (3) the set of common single-copy orthologues across all lineages, either between all possible one-to-one species comparisons (1) or between all species ...
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: 71 , using 50 pose states and excluding outlier poses using the EllipticEnvelope method from sklearn.
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### A DNA methylation atlas of normal human cell types. (Nature 2023)

- DOI: 10.1038/s41586-022-05580-6 | PMCID: PMC9811898 | PMID: 36599988
- Evidence: We then computed the average methylation for each block and sample calculated using wgbstools (--beta_to_table -c 10), marked blocks with fewer than ten observations as missing values and imputed their methylation values using sklearn KNNImputer (v.0.24.2) 55 .
- Full pipeline: alignment/mapping [SAMtools v1.9] -> dimensionality reduction/clustering [SciPy v1.6.3] -> differential/statistical testing [HOMER] -> stage not stated [BEDTools v2.26.0, deepTools v3.4.1, scikit-learn]

### Cas12a2 elicits abortive infection through RNA-triggered destruction of dsDNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05559-3 | PMCID: PMC9811890 | PMID: 36599979
- Evidence: First, clusters of bacteria exhibiting distinct FSC and Pacific Blue signals were identified using density-based spatial clustering of applications with noise (DBSCAN; https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html ).
- Full pipeline: read trimming [RAxML] -> alignment/mapping [Bowtie2, MAFFT v7.490, RAxML] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST, Python]

### Integrated intracellular organization and its variations in human iPS cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05563-7 | PMCID: PMC9834050 | PMID: 36599983
- Evidence: We used the PCA implementation from the Python library scikit-learn 36 with default parameters (Fig.
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> stage not stated [NumPy]

### Imprinted SARS-CoV-2 humoral immunity induces convergent Omicron RBD evolution. (Nature 2023)

- DOI: 10.1038/s41586-022-05644-7 | PMCID: PMC9931576 | PMID: 36535326
- Evidence: To project the dataset onto a 2D space for visualization, we performed multidimensional scaling to represent each antibody in a 32-dimensional space, and then t -SNE to get the 2D representation, using sklearn.manifold.MDS and sklearn.manifold.TSNE (v0.24.2).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [R, ggplot2 v3.3.3, scikit-learn] -> stage not stated [SciPy]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Evidence: We implemented support for all generalized linear models provided by the stats R package, regularized linear models provided by the glmnet R package 69 , Bayesian regression models implemented through the brms R package 70 , gradient boosting regression through the xgboost R package 70 , 71 , as well as bagging and Bayesian ridge models through scikit-learn 72 .
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **0.22.0**
- Evidence: Cosine similarity was calculated based on the median values of the pooled sample bins between fetal and paediatric gene profiles with sklearn.metrics.pairwise.cosine_similarity from scikit-learn v.0.22.0.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Evidence: Principal components were calculated from all proteins using sklearn 72 .
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Version used: **1.2.2**
- Evidence: We calculated the average Manhattan distance to the k -nearest neighbours distances for 200-mers ( k = 4) by splitting sequences into groups based on design method, target cell line and penalty level and using the NearestNeighbors module from scikit-learn (v.1.2.2).
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Version used: **0.2**
- Evidence: The following packages have been used for Good–Turing and Bayesian regression: R v.4.2.2 (2022-10-31), plyr_1.8.9, tools_4.2.2, jsonlite_1.8.8, grid_4.2.2, tidyselect_1.2.0; Python v.3.8.15, packaged by conda-forge, sklearn v.0.2, joblib v.1.2.0, numpy v.1.24.1, scipy v.1.10.1 and threadpoolctl v.3.1.0.
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Evidence: ElasticNet LR models were built using the linear_model.LogisticRegression module in the sklearn package (v.0.22).
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: Missing data points where imputed using scikit-learn’s IterativeImputer with a RandomForestRegressor.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: All of the machine learning methods, including training, validation, and testing, were implemented using the scikit-learn library in Python.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### CRISPR-Cas9 screens reveal regulators of ageing in neural stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07972-2 | PMCID: PMC11525198 | PMID: 39358505
- Evidence: For PCA, we used the Python sklearn.decomposition.PCA module with CasTLE-computed gene scores as input (Fig.
- Full pipeline: quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Enrichr]

### Connectome-constrained networks predict neural activity across the fly visual system. (Nature 2024)

- DOI: 10.1038/s41586-024-07939-3 | PMCID: PMC11525180 | PMID: 39261740
- Evidence: Next, we computed a nonlinear dimensionality reduction to two dimensions using the UMAP (uniform manifold approximation and projection) algorithm, and fitted Gaussian mixtures of 2 to 5 components, with the number of components that minimize the Bayesian information criterion, using the Python libraries umap-learn and scikit-learn 38 , 74 .
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [UMAP, scikit-learn] -> simulation/modelling [PyTorch] -> machine learning [PyTorch]

### Multi-pass, single-molecule nanopore reading of long protein strands. (Nature 2024)

- DOI: 10.1038/s41586-024-07935-7 | PMCID: PMC11410661 | PMID: 39261738
- Evidence: VR classification We used scikit-learn to develop and test classical machine learning models and Pytorch to develop and test convolutional neural-network models.
- Full pipeline: quantification [ImageJ] -> stage not stated [PyTorch, SciPy, scikit-learn]

### A population code for spatial representation in the zebrafish telencephalon. (Nature 2024)

- DOI: 10.1038/s41586-024-07867-2 | PMCID: PMC11464381 | PMID: 39198641
- Evidence: Isomap and quantification Isomap 37 embedding was performed using Scikit-learn 55 with ‘n_neighbors = 100’.
- Full pipeline: quantification [scikit-learn]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **1.2.0**
- Evidence: ... Analysis and visualization of the data were conducted in a Python environment built on Pandas (v.2.0.1), NumPy (v.1.24.2) 73 , SciPy (v.1.10.1) 74 , scikit-learn (v.1.2.0), SCANPY (v1.9.3) 75 , AnnData (v.0.9.1) 75 , matplotlib (v.3.7.1) 76 and seaborn (v.0.13.1) 77 packages.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Black holes regulate cool gas accretion in massive galaxies. (Nature 2024)

- DOI: 10.1038/s41586-024-07821-2 | PMCID: PMC11357995 | PMID: 39143219
- Evidence: Partial least square regression To derive the most significant physical parameters in determining μ HI statistically, we used the Python package Scikit-learn 49 with partial least squares (PLS) Regression function, which uses a non-linear iterative partial least squares (NIPALS) 50 algorithm.
- Full pipeline: differential/statistical testing [scikit-learn]

### Molecular mimicry in multisystem inflammatory syndrome in children. (Nature 2024)

- DOI: 10.1038/s41586-024-07722-4 | PMCID: PMC11324515 | PMID: 39112696
- Evidence: For logistic-regression feature weighting, the Scikit-learn package 68 was used, and logistic-regression classifiers were applied to z -scored PhIP-seq values from individuals with MIS-C versus at-risk controls.
- Full pipeline: differential/statistical testing [Python, SciPy, scikit-learn, tidyverse v1.1.4] -> machine learning [scikit-learn] -> stage not stated [Scanpy v1.10.0, Seurat, igraph v2.0.3]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Evidence: Representative sequences not aligned to any Sanger sequence were assigned a taxonomy with a pre-fitted sklearn-based classifier 35 , trained over the Greengenes 13_8 99% operational taxonomic unit full-length sequences.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### Symbolic recording of signalling and cis-regulatory element activity to DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07706-4 | PMCID: PMC11357993 | PMID: 39020177
- Evidence: A linear lasso regression model to predict editing score of 5 bp barcodes was trained using the python package scikit-learn.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.3] -> alignment/mapping [Cutadapt, STAR v2.7.3] -> differential/statistical testing [DESeq2, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Jupyter]

### Chemical reservoir computation in a self-organizing reaction network. (Nature 2024)

- DOI: 10.1038/s41586-024-07567-x | PMCID: PMC11254755 | PMID: 38926572
- Evidence: An implementation from the Scikit-learn computational package 48 , 49 was used to perform the calculations (code available in the analysis/mutual_information.ipynb notebook).
- Full pipeline: stage not stated [OpenCV, Python, scikit-learn]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Evidence: The remaining SNPs were used to quantify the genome-wide population structures using ADMIXTURE 9 . t -SNE and PCAs For the haplotype matrix, we first imported the data into a Python environment and then transformed the matrix into a one-hot encoded format using the OneHotEncoder class from the sklearn.preprocessing module.
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Single-cell analysis reveals context-dependent, cell-level selection of mtDNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07332-0 | PMCID: PMC11078733 | PMID: 38658765
- Version used: **0.23.1**
- Evidence: The analyses were performed using Python v3.7.12, with the following modules: matplotlib v3.4.2, numpy v1.21.0, pandas v1.1.5, plotly v5.16.1, pysam v0.16.0.1, scikit-learn v0.23.1, scipy v1.7.0 and seaborn v0.11.1.
- Full pipeline: quality control [MultiQC v1.11] -> stage not stated [Matplotlib v3.4.2, NumPy v1.21.0, R, SciPy v1.7.0, scikit-learn v0.23.1, seaborn v0.11.1]

### Neural and behavioural state switching during hippocampal dentate spikes. (Nature 2024)

- DOI: 10.1038/s41586-024-07192-8 | PMCID: PMC11023929 | PMID: 38480889
- Evidence: Both principal components analysis and DBSCAN analysis were done using the Scikit-learn Python package ( https://scikit-learn.org/stable/ ).
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [Python] -> machine learning [DeepLabCut] -> stage not stated [Kilosort, NetworkX]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **0.22**
- Evidence: We then clustered the zones using Python’s scikit-learn (v.0.22) implementation of Kmeans with k = 13 for the overall MERFISH dataset or k = 9 for the ventricular subset of the MERFISH dataset, chosen by silhouette score.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Evidence: The count matrix was imported into a Jupyter notebook with pandas: peaks = pd.read_csv("merged_peaks.counts.txt", sep = "\t", index_col = "Geneid"), scaled with sklearn.preprocessing.StardardScaler: peaks_scaled = StandardScaler().fit_transform(peaks), which was then used to create the UMAP: peaks_scaled_mapper = umap.UMAP(n_neighbors=15, random_state=42).fit(peaks_scaled), and plotted using umap....
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Version used: **0.21.3**
- Evidence: The software used for this methodology was as follows: Python (v.3), Keras (v.2.3.1), tensorflow (v.2.1.0), scikit-learn (v.0.21.3), deeplift (v.0.6.10.0) and biopython (v.1.76).
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Single-neuronal elements of speech production in humans. (Nature 2024)

- DOI: 10.1038/s41586-023-06982-w | PMCID: PMC10866697 | PMID: 38297120
- Evidence: We used the tSNE implantation in the scikit-learn Python module (v.1.3.0).
- Full pipeline: dimensionality reduction/clustering [Kilosort v1.0, scikit-learn] -> structure determination [FreeSurfer v7.4.1] -> stage not stated [FieldTrip, statsmodels v0.13.5]

### Satellite mapping reveals extensive industrial activity at sea. (Nature 2024)

- DOI: 10.1038/s41586-023-06825-8 | PMCID: PMC10764273 | PMID: 38172362
- Evidence: For model learning and selection, we followed a training–validation scheme that uses fivefold cross-validation ( https://scikit-learn.org/stable/modules/cross_validation.html ), in which, for each fold (a training cycle), 80% of the data is reserved for model learning and 20% for model validation, with the validation subset non-overlapping across folds.
- Full pipeline: machine learning [scikit-learn] -> visualisation [Cartopy, Matplotlib]

### Functional and evolutionary significance of unknown genes from uncultivated taxa. (Nature 2024)

- DOI: 10.1038/s41586-023-06955-z | PMCID: PMC10849945 | PMID: 38109938
- Evidence: We restricted the tSNE analysis to families detected in more than 1,000 samples and to a maximum of 150 samples per habitat/human population. tSNE was computed with the python scikit-learn manifold package following logarithmic transformation of the data.
- Full pipeline: alignment/mapping [BLAST, Clustal Omega, DIAMOND] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [R] -> structure determination [Clustal Omega] -> stage not stated [ColabFold, HMMER, eggNOG]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: For each MAG query protein, we used the top 50 hits based on the bitscore, clustered the start and end position coordinates of the corresponding alignments (DBSCAN function, Scikit-learn 79 , 80 , v.0.22.1), used the centre of each clustered start and end position as potential domain boundary coordinates, and split query proteins into domains with database hits attributed to the corresponding doma...
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: To identify microenvironments of colocalizing cell clusters, we used non-negative matrix factorization implementation in scikit-learn, utilizing the wrapper in the cell2location package 86 .
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Evidence: PCA and t -SNE dimensionality reductions 56 were performed using Scikit-learn 89 .
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Fair human-centric image dataset for ethical AI benchmarking. (Nature 2025)

- DOI: 10.1038/s41586-025-09716-2 | PMCID: PMC12675298 | PMID: 41193813
- Version used: **1.5.1**
- Evidence: We used the available implementation in the scikit-learn v.1.5.1 library for both of these models.
- Full pipeline: stage not stated [scikit-learn v1.5.1]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: For this, we used the RandomForestClassifier implementation from the sklearn.ensemble module in Python, with default parameters except for n_estimators = 100.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Integration of hunger and hormonal state gates infant-directed aggression. (Nature 2025)

- DOI: 10.1038/s41586-025-09651-2 | PMCID: PMC12675289 | PMID: 41125886
- Evidence: The SVM classifier was implemented using SVC from scikit-learn with default parameters.
- Full pipeline: quantification [QuPath] -> registration [ImageJ] -> machine learning [scikit-learn] -> stage not stated [Python v3.7]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Statistical model generation A penalized generalized linear model (logistic regression with L1 penality) selected genes with expression predictive of labelled disomic or trisomic cells (scikit-learn pipeline: SelectKBest(n = 5000), RobustScaler(), LogisticRegression(C = 0.1, penalty = ‘l1’, solver = ‘liblinear’, class_weight = ‘balanced’, random_state = 0)).
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Version used: **1.2.2**
- Evidence: The area under the curve of fluorescence traces was calculated with scikit-learn (sklearn, v.1.2.2, RRID: SCR_002577 ), and half-decay times of signal responses were extracted.
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### Arousal as a universal embedding for spatiotemporal brain dynamics. (Nature 2025)

- DOI: 10.1038/s41586-025-09544-4 | PMCID: PMC12611781 | PMID: 40993399
- Evidence: In practice, this value was computed as the pixel-wise weighted average of R 2 scores, with weights determined by pixel variance (computed using the built-in function sklearn.metrics.r2_score, with ‘multioutput’ set to ‘variance weighted’).
- Full pipeline: stage not stated [DeepLabCut, SciPy, scikit-learn]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Evidence: Missing value imputation To address missing values in our dataset, we used the K -nearest neighbours imputation method using the KNNImputer function from the scikit-learn library in Python 28 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### Learning the natural history of human disease with generative transformers. (Nature 2025)

- DOI: 10.1038/s41586-025-09529-3 | PMCID: PMC12589094 | PMID: 40963019
- Evidence: Performance measures and calibration To assess the discriminatory power of the predicted rates for the longitudinal test, we use the area under the receiver operating curve (ROC-AUC) and the average precision-recall curve (APS) as implemented in Python:scikit-learn.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Jupyter, PyTorch, Python, scikit-learn]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: The ROC curves and area under the curve (AUC) were computed using the roc_curve and auc functions from scikit-learn, while the precision-recall curves and average precision were computed using precision_recall_curve and average_precision_score from the same library.
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: We log-transformed mitochondrial fractions and fitted a Gaussian mixture model (GMM, sklearn GaussianMixture) to identify and remove cells assigned to the GMM component with the highest mean mitochondrial fraction.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### A brain-wide map of neural activity during complex behaviour. (Nature 2025)

- DOI: 10.1038/s41586-025-09235-0 | PMCID: PMC12408349 | PMID: 40903598
- Evidence: We used the LogisticRegression module from scikit-learn 111 (v.1.1.2) with 0.001 tolerance, 20,000 maximum iterations, “l1” penalty, “liblinear” solver and “fit_intercept” set to True.
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5, Python]

### Brain-wide representations of prior information in mouse decision-making. (Nature 2025)

- DOI: 10.1038/s41586-025-09226-1 | PMCID: PMC12408363 | PMID: 40903597
- Evidence: We used L1-regularized linear regression to decode the Bayes-optimal prior from the binned spike count data using the scikit-learn function sklearn.linear_model.Lasso (using one regularization parameter).
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [DeepLabCut]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: Methods Overview of software, data and workflow We conducted our LSP mapping workflow using Google Earth Engine (GEE) (v.0.1.404 or later) 65 and performed additional analyses using Python 66 with a set of core scientific packages (numpy 67 , shapely 68 , pandas 69 , geopandas 70 , rasterio 71 , xarray 72 , rasterstats 73 , dask 74 , scipy 75 , scikit-learn 76 , statsmodels 77 and matplotlib 78 ).
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### Data-driven de novo design of super-adhesive hydrogels. (Nature 2025)

- DOI: 10.1038/s41586-025-09269-4 | PMCID: PMC12328221 | PMID: 40770436
- Version used: **1.0.2**
- Evidence: XGB was of v.1.6.2, whereas the other models were implemented using Scikit-learn (v.1.0.2) and Scikit-optimize (v.0.9.0).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost] -> machine learning [UMAP] -> stage not stated [Python, scikit-learn v1.0.2]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Evidence: The regression model was implemented using LinearRegression().fit from the scikit-learn package in Python (v.3.6.0 or newer).
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: The former is possible through the integration of the dimension.pca, dimension.tsne and dimension.umap classes, which internally rely on the Python packages scikit-learn 78 , umap-learn 79 and cuml 21 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Evidence: Differential expression was calculated in R by DESeq2 time course analysis with LRT and the top 200 most differentially expressed genes (log 2 [FC]) across WT meristem maturation were used for PCA of all meristem samples using Python scikit-learn PCA.transform 66 .
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Version used: **0.18.3**
- Evidence: Owing to the multi-terabyte size of the dataset, a Python pixel-wise segmentation classifier using both scikit-learn (v0.18.3) 72 and scikit-image (v1.1.1) 73 was implemented ( https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_trainable_segmentation.html#id4 ).
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Unsupervised pretraining in biological neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09180-y | PMCID: PMC12367527 | PMID: 40533561
- Evidence: 59 ), primarily based on numpy and scikit-learn 60 , 61 , as well as Rastermap 39 .
- Full pipeline: visualisation [Matplotlib] -> stage not stated [NumPy, Python, SciPy, Suite2p, scikit-learn]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Employing the train_test_split function from sklearn.model_selection, we divided data from the normal samples into training and test sets, with a split ratio of 70% for training and 30% for testing.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Evidence: The cells segmented with and without dilation were combined, preprocessed and clustered into 30 unsupervised clusters using sklearn.cluster.KMeans().
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### Dopaminergic action prediction errors serve as a value-free teaching signal. (Nature 2025)

- DOI: 10.1038/s41586-025-09008-9 | PMCID: PMC12310545 | PMID: 40369067
- Evidence: Psychometric fitting The LogisticRegressionCV from scikit-learn package in Python was used to fit the data from the psychometric version of the task.
- Full pipeline: quantification [DeepLabCut] -> differential/statistical testing [Python, scikit-learn, statsmodels] -> stage not stated [SciPy, pingouin]

### Native nucleosomes intrinsically encode genome organization principles. (Nature 2025)

- DOI: 10.1038/s41586-025-08971-7 | PMCID: PMC12240700 | PMID: 40335690
- Evidence: NMF decomposition The genetic–epigenetic features of all mononucleosomes in chromosome 1 were linearly decomposed into ten basis property classes using a Scikit-learn NMF Python package.
- Full pipeline: alignment/mapping [Bowtie2, Python] -> simulation/modelling [OpenMM] -> stage not stated [GSEA, Jupyter, scikit-learn]

### Striatum supports fast learning but not memory recall. (Nature 2025)

- DOI: 10.1038/s41586-025-08969-1 | PMCID: PMC12244412 | PMID: 40335692
- Evidence: We then used a custom code in Python wrapping scikit-learn to find a weight or GLM coefficient (Extended Data Fig.
- Full pipeline: stage not stated [DeepLabCut, PyTorch, Python, scikit-learn]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Evidence: Decoding analysis All decoding analyses were performed using a linear support vector machine (SVM; scikit learn (0.23.2), https://scikit-learn.org/ ) classifier.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: PCA and t -distributed stochastic neighbour embedding analyses were first performed using beta Python modules sklearn.decomposition and sklearn.manifold.
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Deep Visual Proteomics maps proteotoxicity in a genetic liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08885-4 | PMCID: PMC12158776 | PMID: 40240610
- Evidence: Using the spectral clustering algorithm from scikit-learn 45 , the resulting UMAP space was split into 50 clusters.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, scikit-learn] -> differential/statistical testing [GSEA, limma] -> stage not stated [Cellpose v2.0, STRING db]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Version used: **1.2.1**
- Evidence: ...(1.16), NEURD (1.0.0) and pcg_skel (0.3,0.2) were used for morphology analysis; Numpy (1.23.5), pandas (1.5.3), SciPy (1.10.1), statsmodels (0.13.5), scikit-learn (1.2.1), PyTorch (1.12.1), tidyverse (2.0.0), glmmTMB (1.1.10), performance (0.12.2) and emmeans (1.10.3) were used for model training and statistical analysis; Matplotlib (3.7.0), seaborn (0.12.2), HoloViews (1.15.4), Ipyvolume (0.5.2) ...
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Inhibitory specificity from a connectomic census of mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-024-07780-8 | PMCID: PMC11981935 | PMID: 40205209
- Evidence: To compute the importance of each feature for each M-type, for each M-type we trained a random forest classifier to predict whether a cell belonged to it using scikit-learn 79 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [scikit-learn]

### Connectomics of predicted Sst transcriptomic types in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08805-6 | PMCID: PMC11981948 | PMID: 40205210
- Evidence: We used the following libraries for visualization and analysis: Matplotlib 73 , Seaborn 74 , Numpy 75 , Pandas 76 , VTK 77 , Scipy 78 , Scikit-posthocs 79 , Scikit-learn 80 , scrattch-hicat ( https://github.com/AllenInstitute/scrattch.hicat/ ) and statsmodels 81 .
- Full pipeline: differential/statistical testing [limma] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn, seaborn, statsmodels]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Evidence: ...use ( x , y ) to predict protein–protein semantic similarities from the Gene Ontology (June 2023 release), trained as previously described 21 (Python Scikit-learn package, fivefold cross-validation, n_estimators=1000, max_depth=30).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: 3g – i , o , r ), we trained a multinomial logistic regression decoder using the LogisticRegression class from the Python package scikit-learn 97 ( https://scikit-learn.org ; v.1.0.2) separately for each mouse using all CEA neurons during the consumption period on the conditioning day and then evaluated this decoder across the entire conditioning session.
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Evidence: Taxonomy was assigned to sequences with the sklearn plugin for QIIME2 with an 80% confidence threshold, using the SILVA v.138 database 66 .
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **0.0**
- Evidence: Python packages used: beautifulsoup4 v.4.12.2, bio v.1.6.2, GSEApy v.1.1.0, matplotlib v.3.7.1, NumPy v.1.24.3, pandas v.2.0.2, SciPy v.1.10.1, seaborn v.0.12.2, sklearn v.0.0.post5, urllib3 v.2.0.3.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: We used sklearn.decomposition.non_negative_factorization in which X is the filtered normalized expression matrix and H is the filtered gene-spectra consensus matrix.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: Each time series average of the 12 imaging planes were registered to this stack using the scikit-learn template matching algorithm.
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Evidence: Clustering analyses of grid-cell modules and bursting subtypes of grid cells were conducted using the python package Scanpy 87 and its dependencies (including numpy, pandas, scipy, scikit-learn and matplotlib).
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: Transcriptional neighbourhood decomposition was performed using Scikit-learn 71 non-negative matrix factorization on a matrix of the summed transcript count values for the ten nearest neighbours of each cell, calculated with a SciPy 72 K -dimensional tree, to create a transformed data matrix W with 15 latent factors.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: The spots from all three channels were aggregated, and DBSCAN from scikit-learn.cluster was used on all spots with eps=35 and min_samples=5.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: SVM: we used scikit-learn Support Vector Regression with epsilon 0.2, linear kernel and max iterations 1,000.
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: Taxonomy was assigned against the SILVA reference database 56 (v.138) using classify-sklearn from QIIME2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: Each trajectory was standardized by centring and scaling to unit variance with sklearn.preprocessing.StandardScaler 102 .
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Understanding the neural code of stress to control anhedonia. (Nature 2025)

- DOI: 10.1038/s41586-024-08241-y | PMCID: PMC11735319 | PMID: 39633053
- Evidence: The new distance d assigned to the agglomerated clusters was defined as d ( u , v ) = max(dist( u [ p ], v [ q ])), in which p and q represent all of the points in the merged clusters u and v , also known as the farthest point algorithm (sklearn.cluster.AgglomerativeClustering, built-in class in scikit-learn in Python 67 ).
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [DeepLabCut, Kilosort]

### Foundation models for fast, label-free detection of glioma infiltration. (Nature 2025)

- DOI: 10.1038/s41586-024-08169-3 | PMCID: PMC11711092 | PMID: 39537921
- Version used: **1.4.1**
- Evidence: Scikit-learn (v.1.4.1) was used to compute performance metrics on model predictions at both training and inference.
- Full pipeline: machine learning [scikit-learn v1.4.1] -> stage not stated [PyTorch, R v3.6.3]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Evidence: To create an image that will define the boundaries of multiple cell types, we combined the channels for several cell-type-specific membrane or cytoplasmic markers into a single image by min–max scaling each channel (using the MinMaxScaler function in the sklearn.preprocessing (v.1.4.2) package with the default parameters) and summing them.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: Scikit-learn and statsmodel were used for more complex calculations and pynndescent was used for fast nearest-neighbour computations. scATAC-seq quality control TSS enrichment was calculated using pycisTopic 51 (TSS window 50 base pairs (bp), flanking window 1,000 bp) as we noticed discernible change in some of the samples after updating Cellranger-arc.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Models were implemented in Python (v3.8.18) using the ElasticNet, BayesianRidge, SVM, RandomForestRegressor and KNeighborsRegressor functions from the scikit-learn library (v1.3.2), and the LGBMRegressor function from the lightgbm package (v4.1.0).
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Version used: **1.3.0**
- Evidence: Decoding was performed on these 8D representations using a linear support vector machine classifier (SVC) (LinearSVC, scikit-learn (v.1.3.0), regularization parameter C set to 0.1), with 10-fold cross-validation.
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### An AI system to help scientists write expert-level empirical software. (Nature 2026)

- DOI: 10.1038/s41586-026-10658-6 | PMCID: PMC13293872 | PMID: 42156545
- Evidence: For each dataset, we used a search of 300 nodes, with the system permitted to use a broad suite of machine learning libraries, including scikit-learn, XGBoost and statsmodels.
- Full pipeline: stage not stated [NumPy, XGBoost, scikit-learn, statsmodels]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Evidence: We applied hierarchical clustering on the top 30 principal components (PCs) using the sklearn.cluster.AgglomerativeClustering function in Python with default parameters and n_clusters = m.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### General scales unlock AI evaluation with explanatory and predictive power. (Nature 2026)

- DOI: 10.1038/s41586-026-10303-2 | PMCID: PMC13043289 | PMID: 41922702
- Evidence: For implementation, the RF models were trained using the scikit-learn library 88 , whereas the fine-tuned LLaMA-3.1-8B was trained on the Transformers library 89 using the PyTorch backend running on Python 3.11.
- Full pipeline: machine learning [PyTorch, Python v3.11, scikit-learn]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **1.6.1**
- Evidence: Data processing, model training and evaluation were implemented in Python using numpy v.2.0.2, tensorflow v.2.19.0, scipy v.1.16.3, statsmodels v.0.14.6, sklearn v.1.6.1, shap v.0.50.0, xgboost v.3.1.2, torch v.2.9.0, pandas v.2.2.2, umap v.0.5.9.post2, pickle v.4.0, pytz v.2025.2, re v.2.2.1, tqdm v.4.67.1, IPython v.7.34.0, json v.2.0.9 and altair v.5.5.0.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: The model was fit using the GaussianMixture implementation from scikit-learn ( n _components = 2; random_state = 42).
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Evidence: For each 10x dataset, we trained a multiclass logistic regression model using the scikit-learn LogisticRegression class with options multi_class=’multinomial’ and solver=‘lbfgs’ using our original cluster labels (hereafter, cell state identities) and gene counts from our previous work 4 , using only the genes in common between both datasets.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Quantum spin resonance in engineered proteins for multimodal sensing. (Nature 2026)

- DOI: 10.1038/s41586-025-09971-3 | PMCID: PMC12851924 | PMID: 41565820
- Version used: **1.6.1**
- Evidence: Data processing was performed using Python (v3.11.11), SciPy (v1.15.1) 64 , NumPy (v.126.4) 65 , scikit-learn (v1.6.1) 66 and scikit-image (v0.20.0) 66 .
- Full pipeline: machine learning [XGBoost] -> stage not stated [NumPy v126.4, SciPy v1.15.1, scikit-image v0.20.0, scikit-learn v1.6.1]

### Predatory aggression evolved through adaptations to noradrenergic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-10009-x | PMCID: PMC12960248 | PMID: 41565818
- Evidence: For preprocessing, the original features were preprocessed and downsampled before analysis using the following pipeline implemented in sklearn.
- Full pipeline: dimensionality reduction/clustering [UMAP, XGBoost] -> machine learning [UMAP, XGBoost] -> stage not stated [ImageJ, scikit-learn]

### Dominant contribution of Asgard archaea to eukaryogenesis. (Nature 2026)

- DOI: 10.1038/s41586-025-09960-6 | PMCID: PMC12872458 | PMID: 41535464
- Version used: **1.3.0**
- Evidence: This embedding was clustered using HDBSCAN as implemented in scikit-learn v.1.3.0 with default parameters 80 .
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn v1.3.0] -> stage not stated [SciPy]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: ...br and Hmisc toolkits (versions ggplot2_3.5.1, tidyr_1.3.1, dplyr_1.1.4, ggpubr_0.6.0, Hmisc_5.2.1), Python (version 3.12.9) using the pandas, scipy, scikit-learn, matplotlib and seaborn packages (versions pandas_2.2.3, scipy_1.14.1, scikit-learn_1.5.2, matplotlib_3.9.2, seaborn_0.13.2) or Microsoft Excel for Mac (Office 365, version 16.9).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Language model-guided anticipation and discovery of mammalian metabolites. (Nature 2026)

- DOI: 10.1038/s41586-025-09969-x | PMCID: PMC12960238 | PMID: 41535467
- Evidence: A random forest classifier was then trained to distinguish between known metabolites and generated molecules, using the implementation in scikit-learn.
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> machine learning [scikit-learn] -> stage not stated [PyTorch, RDKit]

### Distinct neuronal populations in the human brain combine content and context. (Nature 2026)

- DOI: 10.1038/s41586-025-09910-2 | PMCID: PMC12916488 | PMID: 41501461
- Version used: **0.24.1**
- Evidence: In general, decoders were implemented with functions from the LIBSVM library (v3.24) using standard parameters (unless stated otherwise) in custom scripts written in MATLAB R2021a or Python (scikit-learn 0.24.1), and a fivefold cross-validation scheme without overlap between training and testing data was used with five repetitions.
- Full pipeline: machine learning [scikit-learn v0.24.1]

### Plastic landmark anchoring in zebrafish compass neurons. (Nature 2026)

- DOI: 10.1038/s41586-025-09888-x | PMCID: PMC12916487 | PMID: 41501455
- Version used: **1.1.2**
- Evidence: The Ridge regression was performed using scikit-learn 1.1.2 with \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\alpha =1$$\end{document} α = 1 , and the regression coefficients (that is, the gain of path integration)...
- Full pipeline: differential/statistical testing [scikit-learn v1.1.2] -> stage not stated [SciPy, Suite2p]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Version used: **0.22**
- Evidence: Next, we implemented a k -means clustering approach using the scikit-learn (v.0.22) package and evaluated the stability of clusters across a range of k values (5–35) using the silhouette score.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: We used the Yeo–Johnson transformation function with the default parameters from the Python scikit-learn package.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Palaeometabolomes yield biological and ecological profiles at early human sites. (Nature 2026)

- DOI: 10.1038/s41586-025-09843-w | PMCID: PMC12851940 | PMID: 41407854
- Evidence: PLS-DA was performed using the PLSRegression module in Scikit-learn, adapted for classification by labelling categorical outcomes numerically 100 .
- Full pipeline: dimensionality reduction/clustering [seaborn] -> differential/statistical testing [SciPy, scikit-learn] -> visualisation [seaborn]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: NMF from sklearn was run with the following parameters: (n_components=8, alpha=0.9,max_iter=1000, shuffle=True, init = “nndsvda”,l1_ratio=0.9).
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Version used: **1.3.2**
- Evidence: Machine learning To assess the link to the human gut microbiome composition, we developed and used a machine learning framework based on random forest classification and regression algorithms from the scikit-learn (v.1.3.2) Python package (as implemented in the RandomForestClassifier and RandomForestRegressor functions, respectively), both with ‘n_estimators=1000’ and ‘max_features=sqrt’ parameter...
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Evidence: This was performed by fitting the equation 100 × e (− x × tau) in Python (v.3.7.6) and the package scipy (v.1.4.1) to each kinase’s CHX screening trajectory. t -SNE plots were generated with sklearn and matplotlib (v.1.0.1 and v.3.5.3, respectively) from ChEMBL drug-binding data processed as described in the Chemical Checker (CC) 24 and compounds were characterized with CC global bioactivity signa...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Inhibitory PD-1 axis maintains high-avidity stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09440-x | PMCID: PMC12727512 | PMID: 41299179
- Evidence: Principal component analysis was performed using the Python-based scikit-learn library on z -score-normalized marker intensity and plotted using matplotlib library to visualize relative marker expression.
- Full pipeline: quantification [seaborn] -> normalisation [Matplotlib, scikit-learn] -> dimensionality reduction/clustering [Matplotlib, scikit-learn] -> visualisation [Matplotlib, scikit-image, scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2, napari]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **1.7.2**
- Evidence: For PCA analysis and visualization, probability vectors were centred, log-ratio transformed and used as input to sklearn.decomposition.PCA (scikit-learn v1.7.2).
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Version used: **1.5.2**
- Evidence: Nearest-neighbour analysis was performed using scikit-learn (v.1.5.2).
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: All analyses were conducted using skimage for image processing 71 , 72 , numpy and pandas for data handling, matplotlib and seaborn for visualization, and scipy and scikit-learn for statistical and machine learning operations.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Comprehensive echocardiogram evaluation with view primed vision language AI. (Nature 2026)

- DOI: 10.1038/s41586-025-09850-x | PMCID: PMC12935550 | PMID: 41219498
- Evidence: For k -nearest neighbour probing, we used KNeighborsClassifier, and for linear probing, we applied LogisticRegression, both from scikit-learn library.
- Full pipeline: dimensionality reduction/clustering [SciPy v1.12.0] -> differential/statistical testing [SciPy v1.12.0, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [PyTorch v2.1.2]

### Systems biology analysis of human genomes points to key pathways conferring spina bifida risk. (PNAS 2021)

- DOI: 10.1073/pnas.2106844118 | PMCID: PMC8713748 | PMID: 34916285
- Evidence: RF ( 32 )—a machine learning technique which uses numerous decision trees—was employed to build a predictive model of SB using Python’s scikit-learn library ( 89 ).
- Full pipeline: stage not stated [ADMIXTURE, BEDTools, GATK, R, VEP, WGCNA, scikit-learn]

### Transformational machine learning: Learning how to learn from many related scientific problems. (PNAS 2021)

- DOI: 10.1073/pnas.2108013118 | PMCID: PMC8670494 | PMID: 34845013
- Evidence: For example, Auto-WEKA and Auto-sklearn ( 39 ) search through a space of possible ML methods, and hyper-parameters, to optimize ML predictions.
- Full pipeline: stage not stated [scikit-learn]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Evidence: Processing within the pipeline made use of the following Python libraries: Nipype ( 49 ), the Advanced Normalization Tools ( 50 ), the Insight Toolkit ( 51 ), Scikit-image ( 52 ), Scikit-learn ( 53 ), and SciPy ( 54 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Deep learning identifies synergistic drug combinations for treating COVID-19. (PNAS 2021)

- DOI: 10.1073/pnas.2105070118 | PMCID: PMC8488647 | PMID: 34526388
- Evidence: We run the RF and SVM baselines using the “sklearn_train.py” script in Chemprop.
- Full pipeline: stage not stated [RDKit, scikit-learn]

### Morphological cell profiling of SARS-CoV-2 infection identifies drug repurposing candidates for COVID-19. (PNAS 2021)

- DOI: 10.1073/pnas.2105815118 | PMCID: PMC8433531 | PMID: 34413211
- Evidence: Briefly, for a set of cells, each feature was per-plate standardized and jointly orthogonalized using sklearn.IncrementalPCA(n_components = 379, batch_size = 1,000).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ] -> stage not stated [CellProfiler, scikit-learn]

### A catalog of tens of thousands of viruses from human metagenomes reveals hidden associations with chronic diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2023202118 | PMCID: PMC8201803 | PMID: 34083435
- Evidence: Random Forest Classifiers from scikit-learn were used ( 105 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2, NumPy, SAMtools, SciPy] -> machine learning [scikit-learn] -> stage not stated [Cytoscape, RepeatMasker]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Evidence: Linear regression (sklearn package; v0.21.3) ( 64 ) was used to describe the relationship between the number of information-rich features and the dissimilarity score between PCA plots; the results were utilized to optimize the threshold selected for information-rich feature calling.
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Density estimation using deep generative neural networks. (PNAS 2021)

- DOI: 10.1073/pnas.2101344118 | PMCID: PMC8054014 | PMID: 33833061
- Evidence: For outlier detection tasks, we implemented one-class SVM and Isolation Forest using Scikit-learn library ( 30 ), where the default parameters were used.
- Full pipeline: machine learning [TensorFlow] -> stage not stated [scikit-learn]

### Learning the molecular grammar of protein condensates from sequence determinants and embeddings. (PNAS 2021)

- DOI: 10.1073/pnas.2019053118 | PMCID: PMC8053968 | PMID: 33827920
- Evidence: All classifiers were built using the Python scikit-learn package ( 40 ) with default parameters.
- Full pipeline: machine learning [scikit-learn]

### <i>Arabidopsis</i> cell wall composition determines disease resistance specificity and fitness. (PNAS 2021)

- DOI: 10.1073/pnas.2010243118 | PMCID: PMC7865177 | PMID: 33509925
- Evidence: The correlation and paired comparison analyses were implemented using the SAS software ( glm and corr procedures), while the CRT classification model fitting and validation were implemented using Python ( scikit-learn library: Data Set 2_CRTPythonscript, or see link: https://github.com/tinguarorg/PNAS_CellWall.git ).
- Full pipeline: stage not stated [R, scikit-learn]

### Automatic detection of influential actors in disinformation networks. (PNAS 2021)

- DOI: 10.1073/pnas.2011216118 | PMCID: PMC7848582 | PMID: 33414276
- Evidence: IO account classifier design is implemented using this semisupervised machine-learning approach built with the open source libraries scikit-learn and Snorkel ( 20 , 21 ) and soft labeling functions based on heuristics of IO account metadata, content, and behavior.
- Full pipeline: machine learning [scikit-learn]

### The molecular basis for pore pattern morphogenesis in diatom silica. (PNAS 2022)

- DOI: 10.1073/pnas.2211549119 | PMCID: PMC9894196 | PMID: 36459651
- Version used: **0.21.3**
- Evidence: For the partitioning of the mRNA microarray, we implemented the spectral clustering segmentation technique ( 59 – 61 ) by using the scikit-learn (v0.21.3)) python package ( 62 ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn v0.21.3] -> differential/statistical testing [Matplotlib v3.5, seaborn v0.11] -> visualisation [Matplotlib v3.5, seaborn v0.11] -> stage not stated [BLAST, NumPy, SciPy, scikit-image]

### Impact of cultural and genetic structure on food choices along the Silk Road. (PNAS 2022)

- DOI: 10.1073/pnas.2209311119 | PMCID: PMC9704696 | PMID: 36375050
- Evidence: Then, we normalized the individual profiles with the StandardScaler() function of the python library scikit-learn .
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SciPy, lme4] -> differential/statistical testing [lme4] -> machine learning [ADMIXTURE] -> stage not stated [PLINK v1.9, R, vegan]

### Adult neurogenesis acts as a neural regularizer. (PNAS 2022)

- DOI: 10.1073/pnas.2206704119 | PMCID: PMC9659416 | PMID: 36322739
- Version used: **0.21.1**
- Evidence: Models were built and analyzed in Python 3.6 ( 65 ) with custom scripts that are freely available on GitHub, and were developed using the following packages: PyTorch ( 66 ), Ax ( https://github.com/facebook/Ax ), NumPy ( 67 ), SciPy ( 68 ), Pandas ( 69 ), Matplotlib ( 70 ), Seaborn ( 71 ), and Scikit-learn 0.21.1 ( 72 ).
- Full pipeline: stage not stated [Matplotlib, NumPy, PyTorch, Python v3.6, SciPy, scikit-learn v0.21.1, seaborn]

### Structure of an amorphous calcium carbonate phase involved in the formation of <i>Pinctada margaritifera</i> shells. (PNAS 2022)

- DOI: 10.1073/pnas.2212616119 | PMCID: PMC9659418 | PMID: 36322756
- Evidence: Non-negative matrix factorization of the preshaped data were done using the python-scikit-learn package ( 95 ).
- Full pipeline: stage not stated [scikit-learn]

### Multiple traces and altered signal-to-noise in systems consolidation: Evidence from the 7T fMRI Natural Scenes Dataset. (PNAS 2022)

- DOI: 10.1073/pnas.2123426119 | PMCID: PMC9636924 | PMID: 36279446
- Evidence: Models were trained within each subject according to a randomly shuffled k-fold (inner = 20 splits; outer = 40 splits) nested cross-validation procedure (via sklearn’s cross_val_score method).
- Full pipeline: machine learning [scikit-learn]

### Dynamic processing of hunger and thirst by common mesolimbic neural ensembles. (PNAS 2022)

- DOI: 10.1073/pnas.2211688119 | PMCID: PMC9618039 | PMID: 36252036
- Evidence: The statistical models used for imaging data analysis as described above were carried out using the scikit-learn Python package ( 39 ).
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [Python, Suite2p]

### Mind blanking is a distinct mental state linked to a recurrent brain profile of globally positive connectivity during ongoing mentation. (PNAS 2022)

- DOI: 10.1073/pnas.2200511119 | PMCID: PMC9564098 | PMID: 36194631
- Evidence: Precision (a parameter between 0 and 1) is also defined as the ability of the classifier not to label as positive a sample that is negative ( https://scikit-learn.org/stable/modules/model_evaluation.html ).
- Full pipeline: alignment/mapping [AFNI, FSL v6.0, Nipype, SPM] -> differential/statistical testing [AFNI, FSL v6.0, Nipype, SPM] -> machine learning [scikit-learn] -> stage not stated [Python]

### Gendered citation patterns among the scientific elite. (PNAS 2022)

- DOI: 10.1073/pnas.2206070119 | PMCID: PMC9546584 | PMID: 36161888
- Evidence: The classifier parameters were set to their default values in sklearn.
- Full pipeline: machine learning [scikit-learn]

### False-positive IRESes from &lt;i&gt;Hoxa9&lt;/i&gt; and other genes resulting from errors in mammalian 5' UTR annotations. (PNAS 2022)

- DOI: 10.1073/pnas.2122170119 | PMCID: PMC9456764 | PMID: 36037358
- Evidence: To perform classification of active versus nonactive transcript leaders, we used LogisticRegressionCV from scikit learn (sklearn.linear_model.LogisticRegressionCV) with the default solver = lbfgs, Cs = 10, intercept = True, and cv = 10 parameters.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [scikit-learn] -> stage not stated [BEDTools, Cutadapt]

### Repertoire-scale measures of antigen binding. (PNAS 2022)

- DOI: 10.1073/pnas.2203505119 | PMCID: PMC9407674 | PMID: 35969768
- Evidence: A random forest classifier was trained (using scikit-learn’s RandomForestClassifier module) to predict the probability that a repertoire was CMV seronegative.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [NumPy v1.18.0, PyMOL v2.2, Python v3.7.6, SciPy v1.4.1]

### Evolution and folding of repeat proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2204131119 | PMCID: PMC9351489 | PMID: 35905321
- Evidence: We made multivariate polynomial fits on the selected set, making fivefold cross-validation and using python sklearn library preprocessing.PolynomialFeatures and linear_model.LinearRegression.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [SciPy]

### Archaeal lipids trace ecology and evolution of marine ammonia-oxidizing archaea. (PNAS 2022)

- DOI: 10.1073/pnas.2123193119 | PMCID: PMC9351445 | PMID: 35905325
- Evidence: For OSL regressions, we used sklearn.linear_model.LinearRegression from the community-built machine learning library Scikit-learn ( 99 ).
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> differential/statistical testing [Jupyter, Python, SciPy, scikit-learn] -> visualisation [Jupyter]

### Mass spectrometry imaging to explore molecular heterogeneity in cell culture. (PNAS 2022)

- DOI: 10.1073/pnas.2114365119 | PMCID: PMC9303856 | PMID: 35858333
- Version used: **0.21.3**
- Evidence: The Python package scikit-learn 0.21.3 was used to create a pipeline of mean centering, scaling to unit variance and a linear SVM with balanced class weightings.
- Full pipeline: normalisation [scikit-learn v0.21.3] -> dimensionality reduction/clustering [SciPy] -> stage not stated [Python, scikit-image v0.14.0]

### Anti-bat ultrasound production in moths is globally and phylogenetically widespread. (PNAS 2022)

- DOI: 10.1073/pnas.2117485119 | PMCID: PMC9231501 | PMID: 35704762
- Evidence: We used the software tools Scikit-learn ( 67 ) and pandas ( 68 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, R] -> dimensionality reduction/clustering [UMAP] -> structure determination [R] -> stage not stated [IQ-TREE v1.6.2, scikit-learn]

### The neural signature of the decision value of future pain. (PNAS 2022)

- DOI: 10.1073/pnas.2119931119 | PMCID: PMC9191656 | PMID: 35658082
- Evidence: Using scikit-learn, we trained separate LASSO-PCR algorithms to predict the level of pain (1 to 10) and money (1 to 10) and assessed their performance using a 10-fold cross-validation with participants as the grouping factor.
- Full pipeline: differential/statistical testing [Nilearn] -> machine learning [scikit-learn] -> stage not stated [fMRIPrep v20.1.1]

### Accurate virus identification with interpretable Raman signatures by machine learning. (PNAS 2022)

- DOI: 10.1073/pnas.2118836119 | PMCID: PMC9191668 | PMID: 35653572
- Evidence: S1 ), we use the scikit-learn ( 40 ) ML package to perform the t-SNE dimensionality reduction and map high-dimensional data points to a 2D space.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> stage not stated [XGBoost]

### Provable Boolean interaction recovery from tree ensemble obtained via random forests. (PNAS 2022)

- DOI: 10.1073/pnas.2118636119 | PMCID: PMC9295780 | PMID: 35609192
- Evidence: We grow RF using the scikit-learn package with 100 trees.
- Full pipeline: stage not stated [scikit-learn]

### Physicochemical classification of organisms. (PNAS 2022)

- DOI: 10.1073/pnas.2122957119 | PMCID: PMC9171632 | PMID: 35500111
- Evidence: Data analysis was carried out using custom Python code (version 3.6) and the scikit-learn module ( 91 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [scikit-learn]

### Dynamics of <i>Drosophila</i> endoderm specification. (PNAS 2022)

- DOI: 10.1073/pnas.2112892119 | PMCID: PMC9169638 | PMID: 35412853
- Evidence: We used the sklearn python implementation for the random forest classification and gradient boosting and k-nearest neighbors (kNN) classifiers from the same package to perform the following cross-validation comparison.
- Full pipeline: dimensionality reduction/clustering [ilastik] -> differential/statistical testing [PyMC, PyMC3] -> machine learning [scikit-learn]

### Phenotype-Based Threat Assessment. (PNAS 2022)

- DOI: 10.1073/pnas.2112886119 | PMCID: PMC9168455 | PMID: 35363569
- Evidence: All ML models were developed with Python 3.7 using the Pandas and Scikit-learn libraries, with all plots visualized using seaborn.
- Full pipeline: visualisation [Python v3.7, scikit-learn, seaborn]

### Label-free sensing of cells with fluorescence lifetime imaging: The quest for metabolic heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2118241119 | PMCID: PMC8892511 | PMID: 35217616
- Evidence: The implementations of K-means and expectation maximization algorithms from the Scikit-learn module were used in the calculations ( 44 ).
- Full pipeline: simulation/modelling [Matplotlib, NumPy, Python v3.7, SciPy] -> stage not stated [scikit-learn]

### Topographically organized representation of space and context in the medial prefrontal cortex. (PNAS 2022)

- DOI: 10.1073/pnas.2117300119 | PMCID: PMC8833199 | PMID: 35121665
- Evidence: Position decoding was performed with a linear support vector classifier using the scikit learn package (sklearn.svm.LinearSVC with C = 5).
- Full pipeline: differential/statistical testing [Python] -> machine learning [scikit-learn]

### In vitro cell cycle oscillations exhibit a robust and hysteretic response to changes in cytoplasmic density. (PNAS 2022)

- DOI: 10.1073/pnas.2109547119 | PMCID: PMC8832984 | PMID: 35101974
- Version used: **0.22.2**
- Evidence: Fitting was performed in Python 3.7.10 using the logistic regression function from the package scikit-learn 0.22.2.
- Full pipeline: differential/statistical testing [Python v3.7.10, scikit-learn v0.22.2] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [ggplot2]

### Epistatic genetic interactions govern morphogenesis during sexual reproduction and infection in a global human fungal pathogen. (PNAS 2022)

- DOI: 10.1073/pnas.2122293119 | PMCID: PMC8872808 | PMID: 35169080
- Evidence: This analysis was conducted using the Python package scikit-learn ( 91 ) and repeated for various coding schemes of the selfing and cellular growth phenotypes such as binary (yeast: 0 and nonyeast forms: 1), ternary (yeast: 0, large cell: 1, selfing: 2), or quaternary (yeast: 0, large cell: 1, selfing: 2, transgressive selfing: 3) scores.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [ImageJ, scikit-learn]

### Narratives imagined in response to instrumental music reveal culture-bounded intersubjectivity. (PNAS 2022)

- DOI: 10.1073/pnas.2110406119 | PMCID: PMC8795501 | PMID: 35064081
- Evidence: Prior to calculating similarity, we used TfidfVectorizer() from the Scikit-learn package version 0.21.3 ( 44 ) with the default parameters to transform each narrative document into a feature vector.
- Full pipeline: stage not stated [Python v3.6.2, scikit-learn]

### Sparsity of higher-order landscape interactions enables learning and prediction for microbiomes. (PNAS 2023)

- DOI: 10.1073/pnas.2307313120 | PMCID: PMC10691334 | PMID: 37991947
- Evidence: We implemented the random forest regressor as available in scikit-learn in Python ( 73 ).
- Full pipeline: stage not stated [Python, XGBoost, scikit-learn]

### Growth hormone-releasing hormone receptor antagonist MIA-602 attenuates cardiopulmonary injury induced by BSL-2 rVSV-SARS-CoV-2 in hACE2 mice. (PNAS 2023)

- DOI: 10.1073/pnas.2308342120 | PMCID: PMC10691341 | PMID: 37983492
- Evidence: We programmed this model using python 3.9, and the model was taken from a scikit-learn package.
- Full pipeline: stage not stated [scikit-learn]

### Machine-guided discovery of a real-world rogue wave model. (PNAS 2023)

- DOI: 10.1073/pnas.2306275120 | PMCID: PMC10691345 | PMID: 37983488
- Evidence: This publication was made possible by the following opensource software stack: JAX ( 57 ), flax ( 58 ), optax ( 59 ), PySR ( 9 ), scikit-learn ( 63 ), PyALE ( 64 ), NumPy ( 65 ), SciPy ( 66 ), matplotlib ( 67 ), Seaborn ( 68 ), pandas ( 69 ), and Jupyter ( 70 ).
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, SciPy, scikit-learn, seaborn]

### DNA language models are powerful predictors of genome-wide variant effects. (PNAS 2023)

- DOI: 10.1073/pnas.2311219120 | PMCID: PMC10622914 | PMID: 37883436
- Evidence: Genomic region classification was performed with logistic regression as implemented by scikit-learn ( 58 ), using class weight inversely proportional to frequency and L2 regularization strength chosen via cross-validation.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [VEP]

### An amino-domino model described by a cross-peptide-bond Ramachandran plot defines amino acid pairs as local structural units. (PNAS 2023)

- DOI: 10.1073/pnas.2301064120 | PMCID: PMC10623034 | PMID: 37878722
- Evidence: The set of all such vectors from all the pairs was then clustered into k = 20 clusters using Lloyd’s k -means algorithm with the Euclidean metric implemented in the sklearn python package.
- Full pipeline: dimensionality reduction/clustering [AlphaFold, scikit-learn] -> simulation/modelling [GROMACS]

### Signatures of cross-modal alignment in children's early concepts. (PNAS 2023)

- DOI: 10.1073/pnas.2309688120 | PMCID: PMC10589699 | PMID: 37819984
- Evidence: Logistic regression was performed using scikit-learn in Python ( 60 ).
- Full pipeline: dimensionality reduction/clustering [NetworkX, Python] -> differential/statistical testing [scikit-learn]

### Prediction and design of protease enzyme specificity using a structure-aware graph convolutional network. (PNAS 2023)

- DOI: 10.1073/pnas.2303590120 | PMCID: PMC10523478 | PMID: 37729196
- Version used: **0.20.1**
- Evidence: We used the Scikit-learn 0.20.1 ( 66 ) to implement logistic regression (lg), random forest (rf), decision tree (dt), SVM classification, and Tensorflow 1.13.1 ( 67 ) for ANN.
- Full pipeline: differential/statistical testing [TensorFlow v1.13.1, scikit-learn v0.20.1] -> machine learning [PyTorch]

### mitoSplitter: A mitochondrial variants-based method for efficient demultiplexing of pooled single-cell RNA-seq. (PNAS 2023)

- DOI: 10.1073/pnas.2307722120 | PMCID: PMC10523499 | PMID: 37725654
- Version used: **1.0.2**
- Evidence: To conduct performance verification on pooled single-cell sequencing data, we calculated the AUC value, accuracy, and recall of single cells using the Python package sklearn v1.0.2.
- Full pipeline: alignment/mapping [Cutadapt v1.18, STAR v2.7.3a, minimap2 v2.24] -> variant calling [Scanpy v1.9.1, minimap2 v2.24] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> stage not stated [scikit-learn v1.0.2]

### Mixed, nonclassical behavior in a classic allosteric protein. (PNAS 2023)

- DOI: 10.1073/pnas.2308338120 | PMCID: PMC10515163 | PMID: 37695919
- Evidence: Principal component analysis was done in the python scikit-learn package with n_components=2.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [GROMACS v2020.3] -> stage not stated [PyMOL, R]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **1.0.2**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### Understanding the first-offer conundrum: How buyer offers impact sale price and impasse risk in 26 million eBay negotiations. (PNAS 2023)

- DOI: 10.1073/pnas.2218582120 | PMCID: PMC10410759 | PMID: 37527338
- Evidence: We conducted machine learning analyses using Python’s scikit-learn module ( 38 ).
- Full pipeline: stage not stated [scikit-learn]

### Urban visual intelligence: Uncovering hidden city profiles with street view images. (PNAS 2023)

- DOI: 10.1073/pnas.2220417120 | PMCID: PMC10319000 | PMID: 37364096
- Evidence: To estimate neighborhood socioeconomic statistics, we train LASSO regression models using the Python package scikit-learn.
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [PyTorch]

### Development potential of nanoenabled agriculture projected using machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2301885120 | PMCID: PMC10288598 | PMID: 37314934
- Evidence: RF models were built by the scikit-learn “RandomForestRegressor” in Python 3.8.
- Full pipeline: stage not stated [Keras, Python v3.8, R v4.0, TensorFlow, igraph, scikit-learn]

### Contrastive learning in protein language space predicts interactions between drugs and protein targets. (PNAS 2023)

- DOI: 10.1073/pnas.2220778120 | PMCID: PMC10268324 | PMID: 37289807
- Evidence: For each domain, we trained a logistic regression classifier from sklearn with balanced class weights.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [PyTorch v1.11, STRING db]

### Brain imaging and neuropsychological assessment of individuals recovered from a mild to moderate SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217232120 | PMCID: PMC10235949 | PMID: 37220275
- Version used: **1.0.2**
- Evidence: To further evaluate their predictive capacities, all brain imaging markers calculated in the study were averaged within regions of interest where applicable (Desikan–Killiany cortical atlas parcels and TractSeg-derived anatomical white matter tracts) and propagated to a comparative supervised machine learning pipeline (scikit-learn v1.0.2) ( 65 , 74 , 75 ).
- Full pipeline: normalisation [FSL] -> dimensionality reduction/clustering [Python v3.9.1] -> differential/statistical testing [Python v3.9.1] -> stage not stated [R, scikit-learn v1.0.2]

### Cortical activity emerges in region-specific patterns during early brain development. (PNAS 2023)

- DOI: 10.1073/pnas.2208654120 | PMCID: PMC10235933 | PMID: 37216522
- Evidence: Principal components analysis was performed on the same data using Scikit-learn.
- Full pipeline: quantification [ImageJ] -> normalisation [Python] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [Matplotlib] -> stage not stated [NetworkX, NumPy, SciPy]

### Fragmentation landscape of cell-free DNA revealed by deconvolutional analysis of end motifs. (PNAS 2023)

- DOI: 10.1073/pnas.2220982120 | PMCID: PMC10151549 | PMID: 37075072
- Evidence: Such factorization analysis was implemented in the Python language by using the function of sklearn.decomposition.NMF (v1.1.1) ( 43 ).
- Full pipeline: stage not stated [SciPy, scikit-learn]

### Turning high-throughput structural biology into predictive inhibitor design. (PNAS 2023)

- DOI: 10.1073/pnas.2214168120 | PMCID: PMC10089178 | PMID: 36877844
- Evidence: All the models were trained using the scikit-learn package ( 38 ), and the list of hyperparameters considered for each architecture are shown in Dataset 3 .
- Full pipeline: machine learning [scikit-learn] -> stage not stated [RDKit]

### Cross-species predictive modeling reveals conserved drought responses between maize and sorghum. (PNAS 2023)

- DOI: 10.1073/pnas.2216894120 | PMCID: PMC10013860 | PMID: 36848555
- Evidence: After splitting the data into training and test sets, we scaled the data using the StandardScalar function from the scikit-learn python package (v1.1.0) ( 50 ).
- Full pipeline: quality control [fastp v0.23.2] -> read trimming [fastp v0.23.2] -> variant calling [DESeq2 v1.36.0] -> normalisation [scikit-learn] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [scikit-learn] -> stage not stated [R]

### Peptide-binding specificity prediction using fine-tuned protein structure prediction networks. (PNAS 2023)

- DOI: 10.1073/pnas.2216697120 | PMCID: PMC9992841 | PMID: 36802421
- Evidence: The AlphaFold MHC-peptide inter-PAE scores for the training set, together with their binder/non-binder labels, were provided to the LogisticRegression class from the Scikit-learn ( 26 ) package linear_model.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AlphaFold, Python, RoseTTAFold]

### Gatekeeper mutations activate FGF receptor tyrosine kinases by destabilizing the autoinhibited state. (PNAS 2023)

- DOI: 10.1073/pnas.2213090120 | PMCID: PMC9974468 | PMID: 36791110
- Evidence: From there, PDBs were clustered by the PC1 and PC2 using DBSCAN clustering algorithm ( 59 ) using Scikit-learn ( 60 ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [GROMACS v5.1.4]

### Decoding the metabolic response of <i>Escherichia coli</i> for sensing trace heavy metals in water. (PNAS 2023)

- DOI: 10.1073/pnas.2210061120 | PMCID: PMC9963153 | PMID: 36745806
- Evidence: SVM models are trained with Scikit-learn using default parameters, with radial basis function kernel, Margin parameter (C) = 1, and γ = scale.
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> machine learning [scikit-learn] -> stage not stated [Keras, Python v3.6, TensorFlow]

### 3D electron microscopy for analyzing nanoparticles in the tumor endothelium. (PNAS 2024)

- DOI: 10.1073/pnas.2406331121 | PMCID: PMC11665908 | PMID: 39665759
- Evidence: The centroid coordinates (x, y, and z) of each nanoparticle were determined using scikit-learn ( 1 ) in Python.
- Full pipeline: alignment/mapping [Python] -> stage not stated [ImageJ, OpenCV, scikit-learn]

### Intracortical recordings reveal the neuronal selectivity for bodies and body parts in the human visual cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2408871121 | PMCID: PMC11665852 | PMID: 39652751
- Evidence: We utilized the MDS implementation from the scikit-learn library (implemented in Python).
- Full pipeline: stage not stated [FreeSurfer, Python, SPM, scikit-learn]

### Direct simulation and machine learning structure identification unravel soft martensitic transformation and twinning dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2412476121 | PMCID: PMC11648898 | PMID: 39625980
- Version used: **0.20.3**
- Evidence: The classifier is a random forest implemented in Scikit-learn (version 0.20.3) ( 48 ).
- Full pipeline: machine learning [scikit-learn v0.20.3]

### Cholinergic regulation of dendritic Ca&lt;sup&gt;2+&lt;/sup&gt; spikes controls firing mode of hippocampal CA3 pyramidal neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2321501121 | PMCID: PMC11572977 | PMID: 39503887
- Evidence: Clustering of Ca 2+ spikes measured in TTX was performed with the Ward hierarchical clustering method, using the sklearn.cluster module in Python.
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [ImageJ]

### Adaptive CVgen: Leveraging reinforcement learning for advanced sampling in protein folding and chemical reactions. (PNAS 2024)

- DOI: 10.1073/pnas.2414205121 | PMCID: PMC11551409 | PMID: 39475640
- Evidence: Clustering was carried out using the MiniBatchKMeans module from Scikit-learn ( 55 ).
- Full pipeline: dimensionality reduction/clustering [PyMOL, scikit-learn] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib, PyMOL] -> stage not stated [AlphaFold, MDTraj]

### Aligning the smiles of dating dyads causally increases attraction. (PNAS 2024)

- DOI: 10.1073/pnas.2400369121 | PMCID: PMC11551419 | PMID: 39467124
- Evidence: We computed mutual information using the scikit-learn ( 65 ) mutual_info_regression function, which relies on nonparametric methods based on entropy estimation from k-nearest neighbors distances ( 66 , 67 ).
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [R]

### Virtual patient analysis identifies strategies to improve the performance of predictive biomarkers for PD-1 blockade. (PNAS 2024)

- DOI: 10.1073/pnas.2410911121 | PMCID: PMC11551325 | PMID: 39467131
- Evidence: Feature selection was performed with random forest classifier using the recursive feature selection algorithm of the sklearn toolkit in python.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [scikit-learn]

### Alternating access of a bacterial homolog of neurotransmitter: sodium symporters determined from AlphaFold2 ensembles and DEER spectroscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2406063121 | PMCID: PMC11459141 | PMID: 39302996
- Evidence: We applied K-means clustering (via the sklearn library) to these collective variables ( 57 ), increasing the number of clusters until models with the most extreme values for the 16–343 variable were in their own cluster, which occurred at seven clusters.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [PyMOL, scikit-learn] -> simulation/modelling [AlphaFold]

### Machine learning reveals the transcriptional regulatory network and circadian dynamics of &lt;i&gt;Synechococcus elongatus&lt;/i&gt; PCC 7942. (PNAS 2024)

- DOI: 10.1073/pnas.2410492121 | PMCID: PMC11420160 | PMID: 39269777
- Evidence: ICA was performed using the FastICA algorithm from scikit-learn ( https://github.com/SBRG/iModulonMiner/tree/main/4_optICA ) ( 57 – 59 ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore, featureCounts] -> read trimming [FastQC, Trim Galore] -> quantification [MultiQC, featureCounts] -> dimensionality reduction/clustering [STRING db] -> stage not stated [scikit-learn]

### COVID-19 lockdown effects on adolescent brain structure suggest accelerated maturation that is more pronounced in females than in males. (PNAS 2024)

- DOI: 10.1073/pnas.2403200121 | PMCID: PMC11420155 | PMID: 39250666
- Evidence: The pre-COVID-19 lockdown sample was then further split into train (80%) and validation (20%) samples, stratified by age and sex, using the “train_test_split” function of the scikit-learn Python library ( 60 ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [SciPy, scikit-learn]

### Unsupervised pattern identification in spatial gene expression atlas reveals mouse brain regions beyond established ontology. (PNAS 2024)

- DOI: 10.1073/pnas.2319804121 | PMCID: PMC11406299 | PMID: 39226356
- Evidence: We used the scikit-learn ( 77 ) implementation of NMF with default settings of the tolerance of the stopping condition (tol = 0.0001) and the maximum number of iterations (max_iter = 200).
- Full pipeline: stage not stated [scikit-learn]

### Sustainable H<sub>2</sub>O<sub>2</sub> production via solution plasma catalysis. (PNAS 2024)

- DOI: 10.1073/pnas.2410504121 | PMCID: PMC11348095 | PMID: 39150782
- Evidence: The calculation used the sklearn learning package under the Python model in combination with supervised learning methods.
- Full pipeline: visualisation [VMD] -> stage not stated [scikit-learn]

### Leveraging a large language model to predict protein phase transition: A physical, multiscale, and interpretable approach. (PNAS 2024)

- DOI: 10.1073/pnas.2320510121 | PMCID: PMC11331094 | PMID: 39110734
- Evidence: Next, we trained the RF model using the Python scikit-learn package ( 57 ), setting the class weight to “balanced” and limiting the max depth of the trees to 5 to avoid overfitting.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [AlphaFold]

### The neural basis of swap errors in working memory. (PNAS 2024)

- DOI: 10.1073/pnas.2401032121 | PMCID: PMC11331092 | PMID: 39102534
- Evidence: To ameliorate this, we impute the firing rate of those neurons for their stretch of contiguously zero firing based on the five nearest neighbor trials across the population [KNNImputer in sklearn ( 41 )].
- Full pipeline: stage not stated [Psychtoolbox, Stan, scikit-learn]

### A combinatorially complete epistatic fitness landscape in an enzyme active site. (PNAS 2024)

- DOI: 10.1073/pnas.2400439121 | PMCID: PMC11317637 | PMID: 39074291
- Evidence: To enable the analyses in this paper, fitness values for the missing variants in the 4-site landscape were imputed with the sklearn KNN imputer ( SI Appendix , Fig.
- Full pipeline: read trimming [minimap2] -> alignment/mapping [minimap2] -> stage not stated [NetworkX, Python, scikit-learn]

### Secondary structure determines electron transport in peptides. (PNAS 2024)

- DOI: 10.1073/pnas.2403324121 | PMCID: PMC11317557 | PMID: 39052850
- Evidence: Finally, the first two principal components were calculated with PCA-whitening using the scikit-learn python package ( 85 ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [OpenMM v7.7.0] -> stage not stated [VMD]

### Democratizing protein language models with parameter-efficient fine-tuning. (PNAS 2024)

- DOI: 10.1073/pnas.2405840121 | PMCID: PMC11214071 | PMID: 38900798
- Version used: **1.2.0**
- Evidence: The hyperparameters for the MLP on language model embeddings with frozen weights were chosen by a grid search [implemented in scikit-learn (v.1.2.0), SI Appendix , section S1.E ].
- Full pipeline: stage not stated [AlphaFold, PyTorch v2.0.1, RoseTTAFold, scikit-learn v1.2.0]

### Rapid, antibiotic incubation-free determination of tuberculosis drug resistance using machine learning and Raman spectroscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2315670121 | PMCID: PMC11194509 | PMID: 38861604
- Evidence: To assess the classification performance, we used 10-fold cross-validation, which splits the dataset into 10 equal stratified sets (Scikit-learn StratifiedKFold).
- Full pipeline: machine learning [scikit-learn] -> stage not stated [Jupyter]

### Subthalamic nucleus-language network connectivity predicts dopaminergic modulation of speech function in Parkinson's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2316149121 | PMCID: PMC11145286 | PMID: 38768342
- Evidence: Python package scikit-learn was used for SVR and cross-validation ( https://github.com/scikit-learn/scikit-learn ).
- Full pipeline: machine learning [scikit-learn] -> stage not stated [SPM]

### 3D intrusions transport active surface microbial assemblages to the dark ocean. (PNAS 2024)

- DOI: 10.1073/pnas.2319937121 | PMCID: PMC11087786 | PMID: 38696469
- Evidence: Taxonomies were assigned to each ASV using classify-sklearn by QIIME2 ( 75 ) searching against the SILVA database release 138 ( 76 ).
- Full pipeline: read trimming [Cutadapt v1.13] -> stage not stated [QIIME 2, scikit-learn]

### Human mutations in high-confidence Tourette disorder genes affect sensorimotor behavior, reward learning, and striatal dopamine in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2307156121 | PMCID: PMC11087812 | PMID: 38683996
- Evidence: LDA was completed using scikit-learn implementation.
- Full pipeline: stage not stated [scikit-learn]

### Machine learning enables identification of an alternative yeast galactose utilization pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2315314121 | PMCID: PMC11067038 | PMID: 38669185
- Evidence: The random forest algorithm was trained on 90% of the data, and used the remaining 10% for cross-validation, using the RepeatedStratifiedKFold and cross_val_score functions from the sklearn.model_selection ( 58 ) (1.2.1) package.
- Full pipeline: quantification [ggplot2 v3.4.2] -> machine learning [XGBoost v1.7.3, scikit-learn] -> visualisation [ggplot2 v3.4.2] -> stage not stated [HMMER, InterProScan]

### Organ-delimited gene regulatory networks provide high accuracy in candidate transcription factor selection across diverse processes. (PNAS 2024)

- DOI: 10.1073/pnas.2322751121 | PMCID: PMC11066984 | PMID: 38652750
- Evidence: A KNN-based model was trained using the scikit-learn package ( 60 ) using a minimum of 80% of the labeled samples from each organ.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [ImageJ]

### Functional specialization of hippocampal somatostatin-expressing interneurons. (PNAS 2024)

- DOI: 10.1073/pnas.2306382121 | PMCID: PMC11047068 | PMID: 38640347
- Evidence: Scikit’s sklearn.decomposition.
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [scikit-learn]

### What one genus of showy moths can say about migration, adaptation, and wing pattern. (PNAS 2024)

- DOI: 10.1073/pnas.2319726121 | PMCID: PMC11047066 | PMID: 38630713
- Evidence: We used “diverged positions” present in ≥ 4 specimens from each group where each allele was present in ≥ 3 specimens; we computed Matthew’s correlation coefficient (MCC) between SNPs at each position and the phenotypes using the matthews_corrcoef function from Python scikit-learn module.
- Full pipeline: alignment/mapping [AlphaFold, BUSCO, HMMER, IQ-TREE v1.6.12, MAFFT] -> stage not stated [scikit-learn]

### Bmal1 integrates circadian function and temperature sensing in the suprachiasmatic nucleus. (PNAS 2024)

- DOI: 10.1073/pnas.2316646121 | PMCID: PMC11047078 | PMID: 38625943
- Version used: **1.2.2**
- Evidence: Using custom Python script, the timeseries of each region of interest were normalized and a K-Means clustering algorithm was implemented using the K-Means algorithm from scikit-learn 1.2.2 ( 41 ) with k = 5 and the classical EM-style Lloyd algorithm.
- Full pipeline: normalisation [Python, scikit-learn v1.2.2] -> dimensionality reduction/clustering [Matplotlib, Python, SciPy, scikit-learn v1.2.2] -> differential/statistical testing [SciPy]

### On-the-fly Raman microscopy guaranteeing the accuracy of discrimination. (PNAS 2024)

- DOI: 10.1073/pnas.2304866121 | PMCID: PMC10962959 | PMID: 38483992
- Evidence: Then, we applied an ensemble machine learning, Random Forest (RF) classifier ( 27 ) to classify either anomalous (FTC-133), normal (Nthy-ori 3-1), or background to eight training Raman images excluding one to be tested, where RF classifier was implemented in scikit-learn with 800 trees and other all parameters are kept to the default settings.
- Full pipeline: machine learning [scikit-learn]

### Higher-order homophily on simplicial complexes. (PNAS 2024)

- DOI: 10.1073/pnas.2315931121 | PMCID: PMC10962986 | PMID: 38470928
- Evidence: We train a logistic regression model using the scikit-learn library ( 45 ): Each data point is a set of k nodes with all ( k − 1 ) sized interactions but no size k interactions in the sub-training set, the features for each data point (listed in Section 3 ) are computed using the sub-training set, and the label for the data point is 1 if these nodes have a size k interaction in the validation set ...
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn]

### Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2314199121 | PMCID: PMC10945847 | PMID: 38451940
- Evidence: Reweighting of eABF simulations was done as detailed in SI Appendix , using SciPy ( 73 , 74 ) for interpolation and scikit-learn ( 75 ) for Kernel Density Estimation.
- Full pipeline: simulation/modelling [GROMACS v2020.4, MDAnalysis, SciPy, scikit-learn] -> visualisation [Matplotlib, VMD] -> stage not stated [NetworkX]

### Machine learning to predict continuous protein properties from binary cell sorting data and map unseen sequence space. (PNAS 2024)

- DOI: 10.1073/pnas.2311726121 | PMCID: PMC10945751 | PMID: 38451939
- Evidence: Scikit-learn ( https://scikit-learn.org/stable/ ) was used for LDA, one-hot encoding, scaling label vectors, and other pre-processing steps.
- Full pipeline: normalisation [scikit-learn] -> machine learning [PyTorch] -> stage not stated [MACS2, NumPy]

### Homologous mutations in human β, embryonic, and perinatal muscle myosins have divergent effects on molecular power generation. (PNAS 2024)

- DOI: 10.1073/pnas.2315472121 | PMCID: PMC10907259 | PMID: 38377203
- Evidence: Gaussian mixture models were fitted using the implementation of the EM algorithm in scikit-learn.
- Full pipeline: simulation/modelling [GROMACS v2022.4, MDTraj, Python] -> stage not stated [scikit-learn]

### Cell cycle plasticity underlies fractional resistance to palbociclib in ER+/HER2- breast tumor cells. (PNAS 2024)

- DOI: 10.1073/pnas.2309261121 | PMCID: PMC10873600 | PMID: 38324568
- Version used: **0.24.1**
- Evidence: Following image and data preprocessing, cell cycle phases were annotated using a three-component Gaussian Mixture Model (sklearn v0.24.1) to the log-transformed measurements of DNA content, cyclin A, and cyclin B1, as these features were shown previously to minimally represent the cell cycle ( 79 ).
- Full pipeline: simulation/modelling [Slingshot] -> stage not stated [scikit-learn v0.24.1]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: To perform UMAP, we standardized the gene expression data by scaling it to unit variance using the fit_transform() function from the class StandardScaler() of the Python package “sklearn.preprocessing”.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### A spatiotemporal molecular atlas of the ovulating mouse ovary. (PNAS 2024)

- DOI: 10.1073/pnas.2317418121 | PMCID: PMC10835069 | PMID: 38252830
- Evidence: Predicted gene expression values for all genes were then scaled and clustered using K-means clustering with k from 4 to 6 as implemented in the scikit-learn ( 61 ) package (v1.2.0).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SCENIC, scikit-learn] -> visualisation [Squidpy] -> stage not stated [AnnData, CellPhoneDB, Scanpy]

### Development of prediction models to identify hotspots of schistosomiasis in endemic regions to guide mass drug administration. (PNAS 2024)

- DOI: 10.1073/pnas.2315463120 | PMCID: PMC10786280 | PMID: 38181058
- Evidence: We implemented all models using the Scikit-learn Python package (version 1.1.1) and Python (version 3.9.7).
- Full pipeline: stage not stated [Python v3.9.7, XGBoost, scikit-learn]

### Constraining the oxygen requirements for modern microbial eukaryote diversity. (PNAS 2024)

- DOI: 10.1073/pnas.2303754120 | PMCID: PMC10786294 | PMID: 38165897
- Evidence: For taxonomic assignment of the resulting ASVs, a Naïve Bayes classifier was pre-trained on the PR2 database (version 14.2.0) ( 40 ), and ASVs were assigned using the QIIME2 classify-sklearn plugin ( https://docs.qiime2.org/2022.2/data-resources/ ).
- Full pipeline: dimensionality reduction/clustering [DADA2] -> differential/statistical testing [R] -> machine learning [scikit-learn] -> visualisation [ggplot2, tidyverse] -> stage not stated [QIIME 2]

### Intelligent leaching rare earth elements from waste fluorescent lamps. (PNAS 2024)

- DOI: 10.1073/pnas.2308502120 | PMCID: PMC10769842 | PMID: 38147647
- Evidence: All the data processing and ML methods were conducted with the Python programming language (version 3.6), using the open-source scikit-learn library.
- Full pipeline: stage not stated [Jupyter, scikit-learn]

### Contingency, repeatability, and predictability in the evolution of a prokaryotic pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2304934120 | PMCID: PMC10769857 | PMID: 38147560
- Evidence: All machine learning algorithms were implemented using the scikit-learn Python module version 1.0.1 ( 38 ).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [BLAST, R, scikit-learn]

### The variability of evolvability: Properties of dynamic fitness landscapes determine how phenotypic variability evolves. (PNAS 2025)

- DOI: 10.1073/pnas.2519469122 | PMCID: PMC12745803 | PMID: 41397131
- Evidence: Finally, the multidimensional scaling of GRN weights to evaluate genotypes space exploration was performed using 2 components, scikit-learn ( 50 ).
- Full pipeline: variant calling [scikit-learn] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, statsmodels]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Evidence: Principal component analysis (PCA) was performed using scikit-learn package, and the top two components were plotted to capture dominant axes of transcriptomic variance.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### Rubisco is slow across the tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2501433122 | PMCID: PMC12663927 | PMID: 41248286
- Evidence: For all validations and predictions, we used the scikit-learn package ( 78 ) with the default parameters for SVR (see “ Data, Materials, and Software Availability ” for details).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.475] -> normalisation [UMAP] -> dimensionality reduction/clustering [MAFFT v7.475, UMAP] -> stage not stated [scikit-learn]

### Discarded cigarette butts as overlooked reservoirs and amplifiers of antibiotic resistance genes and pathogens in urban green spaces. (PNAS 2025)

- DOI: 10.1073/pnas.2525377122 | PMCID: PMC12595418 | PMID: 41144667
- Evidence: Amplicon sequence variants were identified with DADA2_CCS ( 55 ), and bacterial taxonomy was assigned against the Silva138 database using classify-sklearn with a confidence threshold of 0.7.
- Full pipeline: differential/statistical testing [R v4.3.3, vegan] -> visualisation [ggplot2 v4.6, vegan] -> stage not stated [DADA2, scikit-learn]

### Adaptable microplastic classification using similarity learning on µFTIR spectra collected from µFTIR focal plane array imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2509745122 | PMCID: PMC12557549 | PMID: 41086209
- Version used: **1.3.2**
- Evidence: Scikit-learn (v 1.3.2) was used to construct the various machine learning algorithms for downstream classification.
- Full pipeline: stage not stated [Python, TensorFlow v2.10.1, scikit-learn v1.3.2]

### Fragmentation signatures in cancer patients resemble those of patients with vascular or autoimmune diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2426890122 | PMCID: PMC12402995 | PMID: 40833414
- Evidence: For the analysis of fragmentation signatures, PCA was first performed on z-scores for each fragmentation pattern independently using sklearn.decomposition.PCA(n_components=0.9) .
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2, SAMtools] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy v1.13.1] -> stage not stated [Picard]

### Minimizing and quantifying uncertainty in AI-informed decisions: Applications in medicine. (PNAS 2025)

- DOI: 10.1073/pnas.2424203122 | PMCID: PMC12402999 | PMID: 40833408
- Evidence: In contrast, the estimates from other machine learning approaches, after calibration, including random forest (RF, blue), nonlinear SVM (green), logistic regression (LR, orange), and k-nearest neighbors (kNN, brown), were all far from the truth (see SI Appendix , Algorithm 5 for details on other algorithms, all use default settings from scikit-learn).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2] -> differential/statistical testing [scikit-learn] -> stage not stated [Picard, RepeatMasker, SAMtools]

### Efficient neural encoding as revealed by bilingualism. (PNAS 2025)

- DOI: 10.1073/pnas.2513768122 | PMCID: PMC12403110 | PMID: 40828024
- Evidence: We implemented a leave-one-out cross-validation scheme ( 60 ) using logistic regression classifiers implemented in scikit-learn ( 61 ).
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [PyTorch, Python, scikit-learn]

### Unveiling organ-specific metabolism of &lt;i&gt;Citrus clementina&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2503406122 | PMCID: PMC12305039 | PMID: 40668834
- Evidence: The data are scaled using the StandardScaler() function from sklearn python module.
- Full pipeline: normalisation [scikit-learn] -> structure determination [BLAST]

### Diverse and dynamic influences of saccades on visual representations in the mouse superior colliculus. (PNAS 2025)

- DOI: 10.1073/pnas.2425788122 | PMCID: PMC12305052 | PMID: 40668831
- Evidence: The first model, a multilayer perceptron classifier (scikit-learn), classified putative saccades as nasal, temporal, or nonsaccadic eye movements.
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.0] -> machine learning [scikit-learn] -> stage not stated [DeepLabCut, PsychoPy]

### AI-driven design of multiprincipal element alloys for optimal water splitting. (PNAS 2025)

- DOI: 10.1073/pnas.2504226122 | PMCID: PMC12280936 | PMID: 40623190
- Evidence: The GPR model was implemented using scikit-learn’s Gaussian Process Regressor.
- Full pipeline: stage not stated [scikit-learn]

### Predicting high-fitness viral protein variants with Bayesian active learning and biophysics. (PNAS 2025)

- DOI: 10.1073/pnas.2503742122 | PMCID: PMC12184641 | PMID: 40489612
- Evidence: The kernel hyperparameters were optimized by maximizing the marginalized likelihood function using sklearn.gaussianprocess library.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [scikit-learn]

### Detection of the knee point in lithium-ion battery degradation using a state-of-charge-dependent parameter. (PNAS 2025)

- DOI: 10.1073/pnas.2424838122 | PMCID: PMC12167950 | PMID: 40460124
- Evidence: Data processing and machine-learning-based model construction were performed in Python with the Pandas, NumPy, and Scikit-learn packages.
- Full pipeline: stage not stated [NumPy, Python, scikit-learn]

### Behavioral sequences across multiple animal species in the wild share common structural features. (PNAS 2025)

- DOI: 10.1073/pnas.2503962122 | PMCID: PMC12107123 | PMID: 40372439
- Version used: **1.3.1**
- Evidence: Adjusted mutual information was found using the python package scikit-learn 1.3.1 ( 80 ).
- Full pipeline: stage not stated [scikit-learn v1.3.1]

### Identifying intermolecular interactions in single-molecule localization microscopy. (PNAS 2025)

- DOI: 10.1073/pnas.2409426122 | PMCID: PMC12107154 | PMID: 40354526
- Evidence: They were then filtered, drift-corrected, and clusters were identified and subsequently removed using DBSCAN ( 37 ), implemented using the sklearn.cluster.DBSCAN package, with parameters eps = 75 nm and min _ samples = 10 .
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> stage not stated [NetworkX, Python]

### Proteostasis landscapes of cystic fibrosis variants reveal drug response vulnerability. (PNAS 2025)

- DOI: 10.1073/pnas.2418407122 | PMCID: PMC12054793 | PMID: 40261935
- Evidence: Dimensionality reduction was calculated in Python using sklearn.decomposition.PCA library for principal component analysis, sklearn.manifold.TSNE library for T-distributed Stochastic Neighbor Embedding, and umap library for uniform manifold approximation.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Python, SciPy]

### Structure in conversation: Evidence for the vocabulary, semantics, and syntax of prosody. (PNAS 2025)

- DOI: 10.1073/pnas.2403262122 | PMCID: PMC12054737 | PMID: 40258156
- Evidence: Clustering was done using the variational Bayesian Gaussian mixture model implemented by the scikit-learn software package ( 107 ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [Keras]

### Prediction of phase-separation propensities of disordered proteins from sequence. (PNAS 2025)

- DOI: 10.1073/pnas.2417920122 | PMCID: PMC12002312 | PMID: 40131954
- Evidence: We used the sklearn python package ( 78 ) for all ML models in this work.
- Full pipeline: stage not stated [scikit-learn]

### A global estimate of multiecosystem photosynthesis losses under microplastic pollution. (PNAS 2025)

- DOI: 10.1073/pnas.2423957122 | PMCID: PMC11929485 | PMID: 40063820
- Version used: **1.2.2**
- Evidence: The ML models were implemented using the scikit-learn 1.2.2 package in Python 3.8.8.
- Full pipeline: stage not stated [Python v3.8.8, R v4.0.3, ggplot2, lme4, metafor, scikit-learn v1.2.2]

### Abrupt changes in algal biomass of thousands of US lakes are related to climate and are more likely in low-disturbance watersheds. (PNAS 2025)

- DOI: 10.1073/pnas.2416172122 | PMCID: PMC11892623 | PMID: 39993195
- Evidence: CHL time series were clustered using agglomerative hierarchical clustering using scikit-learn in Python ( 73 ) by initially treating each lake as its own cluster, then recursively merging clusters step-wise while subject to a criterion ( 30 , 74 , 75 ).
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [R]

### Toward equitable major histocompatibility complex binding predictions. (PNAS 2025)

- DOI: 10.1073/pnas.2405106122 | PMCID: PMC11874272 | PMID: 39964728
- Evidence: For performance benchmarking, training and validation folds were generated from the full training set utilizing the KFold function from scikit-learn with parameters, n _ splits=10 and shuffle=True .
- Full pipeline: machine learning [TensorFlow, scikit-learn]

### Spatial profiling of the interplay between cell type- and vision-dependent transcriptomic programs in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421022122 | PMCID: PMC11848306 | PMID: 39946537
- Evidence: Cell type labels were transferred from the published snRNA-seq data to MERFISH based on k-nearest-neighbor-based assignment using sklearn.neighbors.NearestNeighbors .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [Enrichr, NumPy, SciPy, scikit-learn, seaborn]

### A method for unsupervised learning of coherent spatiotemporal patterns in multiscale data. (PNAS 2025)

- DOI: 10.1073/pnas.2415786122 | PMCID: PMC11848389 | PMID: 39951505
- Evidence: The number of frequency bands, both for the global and local separations, can be provided as an a priori expectation or found objectively using k-means clustering from scikit-learn ( 27 ) with a hyperparameter sweep.
- Full pipeline: dimensionality reduction/clustering [scikit-learn]

### Scavenger endothelial cells alleviate tissue damage by engulfing toxic molecules derived from hemolysis. (PNAS 2025)

- DOI: 10.1073/pnas.2406794122 | PMCID: PMC11848282 | PMID: 39932996
- Evidence: For the curve fitting process, we utilized the PolynomialFeatures function from Python's sklearn package, setting the “degree” parameter to 2, which corresponds to a quadratic polynomial fit.
- Full pipeline: stage not stated [scikit-learn]

### Evidence for domain-general arousal from semantic and neuroimaging meta-analyses reconciles opposing views on arousal. (PNAS 2025)

- DOI: 10.1073/pnas.2413808122 | PMCID: PMC11831115 | PMID: 39899711
- Evidence: The “number of clusters” parameter was optimized using the elbow method as implemented in the Kneedle algorithm ( 16 ) and validated post hoc using the silhouette method ( 17 ) as implemented in the scikit-learn ( 18 ) library ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> stage not stated [SciPy]

### Diffusive topology preserving manifold distances for single-cell data analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2404860121 | PMCID: PMC11789025 | PMID: 39854240
- Evidence: We employ Python library Scanpy ( 34 ) for Louvain and Leiden clustering and scikit-learn ( 35 ) for hierarchical agglomerative clustering analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> visualisation [UMAP] -> stage not stated [Monocle, Scanpy, scVelo]

### Discrepancies between subjective and objective sleep assessments revealed by in-home electroencephalography during real-world sleep. (PNAS 2025)

- DOI: 10.1073/pnas.2412895121 | PMCID: PMC11761674 | PMID: 39819218
- Evidence: To compare objective and subjective sleep quality, differences in feature importance in the logistic model were assessed using scikit-learn in Python ( 41 ).
- Full pipeline: stage not stated [Python, scikit-learn, statsmodels]

### Epistatic hotspots organize antibody fitness landscape and boost evolvability. (PNAS 2025)

- DOI: 10.1073/pnas.2413884122 | PMCID: PMC11745389 | PMID: 39773024
- Evidence: We use Python’s sklearn package (function sklearn.manifold.TSNE) to perform sequence-space embedding in two dimensions.
- Full pipeline: variant calling [igraph] -> dimensionality reduction/clustering [scikit-learn]

### Transforming literature screening: The emerging role of large language models in systematic reviews. (PNAS 2025)

- DOI: 10.1073/pnas.2411962122 | PMCID: PMC11745399 | PMID: 39761403
- Evidence: For a deeper quantitative assessment of the model’s performance, we calculate a range of standard statistical metrics using the scikit-learn Python package ( 28 ).
- Full pipeline: differential/statistical testing [scikit-learn]

### Genome-wide analysis of mRNA regionalization in a giant single cell. (PNAS 2026)

- DOI: 10.1073/pnas.2537760123 | PMCID: PMC13291615 | PMID: 42296355
- Evidence: PCA was performed using the scikit-learn implementation (sklearn.decomposition.PCA) in Python.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [kallisto] -> normalisation [kallisto] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [kallisto]

### Transformations of the spatial activity manifold convey aversive information in CA3. (PNAS 2026)

- DOI: 10.1073/pnas.2517639123 | PMCID: PMC13273363 | PMID: 42284325
- Evidence: We solve this system numerically using the eigh function from scikit-learn ( 31 ).
- Full pipeline: differential/statistical testing [XGBoost] -> stage not stated [scikit-learn]

### amyloid-predict and LLPS-predict: Predicting phase separation propensities in the intrinsically disordered proteome. (PNAS 2026)

- DOI: 10.1073/pnas.2531932123 | PMCID: PMC13229271 | PMID: 42190015
- Evidence: Classifiers used scikit-learn.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [AlphaFold]

### Reconstruction of human metabolic models with large language models. (PNAS 2026)

- DOI: 10.1073/pnas.2516511123 | PMCID: PMC13079975 | PMID: 41950094
- Version used: **1.0.2**
- Evidence: The analysis and visualization were facilitated by Python 3.7.16, SHAP 0.41.0, scikit-learn 1.0.2, pandas 1.1.3, SciPy 1.7.3, NumPy 1.21.5, and Matplotlib 3.4.3 packages.
- Full pipeline: visualisation [Matplotlib v3.4.3, NumPy v1.21.5, Python v3.7.16, SciPy v1.7.3, scikit-learn v1.0.2]

### Proteome-wide prediction of interactions between structured domains and peptide motifs reveals functionally coherent subnetworks. (PNAS 2026)

- DOI: 10.1073/pnas.2527957123 | PMCID: PMC13080015 | PMID: 41941631
- Evidence: Performance metrics were computed using the scikit-learn package ( 70 ) in Python.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [AlphaFold, HMMER, Python, R, STRING db, scikit-learn]

### Probing the dark energy in the functional protein universe. (PNAS 2026)

- DOI: 10.1073/pnas.2531111123 | PMCID: PMC12846839 | PMID: 41570070
- Evidence: We fit the data using the python library sklearn , testing multiple initial conditions to ensure a robust minimization of the chi-squared.
- Full pipeline: stage not stated [scikit-learn]

### Identifying direct risk factors in UK Biobank via simultaneous Bayesian-frequentist model-averaged hypothesis testing using Doublethink. (PNAS 2026)

- DOI: 10.1073/pnas.2514138122 | PMCID: PMC12773712 | PMID: 41481468
- Evidence: For initialization, we clustered variables into 200 groups with the scikit-learn-extra KMedoids algorithm, using rank correlation distance.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [R]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Evidence: To verify conservation of biological variation after integration, we collected and harmonized the available cell type labels from the published datasets (66% of cells) and quantified the agreement between labels across different datasets in the cell clusters identified post-integration, using the normalized mutual information (NMI) score, as implemented in scikit-learn ( 81 ).
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: We used the sckitlearn (v.1.1.3) sklearn.mixture.GaussianMixture module to fit 20 models with an increasing number of cell clusters k (between k =2 and k =21) to represent expression patterns of each protein by cell.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Deploying synthetic coevolution and machine learning to engineer protein-protein interactions. (Science 2023)

- DOI: 10.1126/science.adh1720 | PMCID: PMC10403280 | PMID: 37499032
- Version used: **1.2.2**
- Evidence: Finally, to facilitate visualization via circos plots, the data set was subsetted using the ‘train_test_split’ function of the python scikit-learn (version 1.2.2) package.
- Full pipeline: dimensionality reduction/clustering [igraph] -> visualisation [scikit-learn v1.2.2] -> stage not stated [AlphaFold, MACS2, PyTorch, RoseTTAFold]

### The contribution of historical processes to contemporary extinction risk in placental mammals. (Science 2023)

- DOI: 10.1126/science.abn5856 | PMCID: PMC10184782 | PMID: 37104572
- Version used: **1.0.2**
- Evidence: We used the scikit-learn 1.0.2 package for fitting all the models( 66 ).
- Full pipeline: alignment/mapping [BWA v0.7.15] -> variant calling [BWA v0.7.15] -> differential/statistical testing [R] -> stage not stated [GATK, SnpEff v5.0e, scikit-learn v1.0.2]

### Hidden state inference requires abstract contextual representations in the ventral hippocampus. (Science 2024)

- DOI: 10.1126/science.adq5874 | PMCID: PMC7618349 | PMID: 39571013
- Evidence: To model the animal’s choice given its trial history, the regression coefficients were fit using LogisticRegression function of scikit-learn Python library.
- Full pipeline: differential/statistical testing [R, lme4, pingouin, scikit-learn, statsmodels] -> stage not stated [Python, SciPy]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: The statistical models used for imaging data analysis as described above were carried out using the scikit-learn Python package ( 99 ).
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### Comparative connectomics of two distantly related nematode species reveals patterns of nervous system evolution. (Science 2025)

- DOI: 10.1126/science.adx2143 | PMCID: PMC12330220 | PMID: 40743352
- Evidence: Our models (MLPClassifier, DecisionTreeClassifier, RandomForestClassifier, and LogisticRegression from the scikit-learn library ( 42 ) were then evaluated on the test dataset of P. pacificus adjacency and connectivity data.
- Full pipeline: quantification [SciPy] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Cytoscape]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Software libraries used generally for analysis (of both mouse and human data) include Matplotlib ( 89 ), Pandas ( 90 ), Seaborn ( 91 ), and Scikit-learn ( 92 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: To identify outlier cells on the basis of their library complexity and transcriptional richness, we applied the LocalOutlierFactor (LOF) algorithm from sklearn.neighbors.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: 1G ) for select animals, we measured linear separability as classification accuracy of a linear kernel support vector classifier fitted on the top five pose feature PCs using sklearn.svm.SVC with kernel=“linear” ( 97 ).
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries as described before ( 49 , 52 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: We used NMF, as implemented in the python package sklearn.decomposition.NMF (v0.24.2), to summarize the standardized accessibility of human and mouse CREs along the 45 corresponding cell subsets into a set of factors.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

