# statsmodels

- **Category:** general
- **Papers in survey:** 83
- **Journals:** Nature (43), PNAS (28), Cell (8), Science (4)
- **Years:** 2021 (8), 2022 (8), 2023 (13), 2024 (13), 2025 (24), 2026 (17)
- **Versions named:** 0.12.2 (5), 0.14.4 (3), 0.14.0 (3), 0.13.2 (3), 0.13.5 (3), 0.11.1 (3), 0.14.6 (1), 0.12.1 (1), 0.14 (1), 0.10.1 (1)
- **Pipeline stages it appears in:** differential/statistical testing (44), dimensionality reduction/clustering (4), quantification (3), machine learning (2), visualisation (2), variant calling (1), alignment/mapping (1), normalisation (1)

## Papers

### Genome-wide gene expression tuning reveals diverse vulnerabilities of M. tuberculosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.033 | PMCID: PMC8382161 | PMID: 34297925
- Version used: **0.10.1**
- Evidence: ....sourceforge.net/ Python (version 2.7.18) van Rossum, 1995 https://www.python.org/ SciPy (version 1.2.2) Virtanen et al., 2020 https://www.scipy.org/ statsmodels (version 0.10.1) Seabold and Perktold, 2010 https://www.statsmodels.org/stable/index.html Rstan (version 2.19.3) Stan Development Team, 2020 https://mc-stan.org/ Stan (version 2.19.3) Stan Development Team, 2021 https://mc-stan.org/ Spect...
- Full pipeline: alignment/mapping [Python v2.7.18, SciPy v1.2.2] -> stage not stated [BLAST, Stan v2.19.3, statsmodels v0.10.1]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: ...ype and all others through a Mann-Whitney U test via Scipy ( Virtanen et al., 2020 ) with an FDR multiple test correction across cancer types through statsmodels ( Seabold and Perktold, 2010 ), as shown in Data S3.2 G.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: The 20 labeled genes are the most outlying from the lowess local regression between the standard deviation of leverage scores and the log of the number of differentially expressed genes detected by the Anderson-Darling test (computed using statsmodels.nonparametric.smoothers_lowess.lowess).
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Python packages used for spatial enrichment analysis and collagen morphometrics were sckikit-image, pandas, numpy, xarray, scipy, statsmodels.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Structural and functional map for forelimb movement phases between cortex and medulla. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.009 | PMCID: PMC9842395 | PMID: 36608651
- Evidence: All statistical analyses were performed using Scipy, statsmodels, and Pingouin packages in Python 3.7.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [DeepLabCut, Kilosort, Python v3.7, SciPy, TrackMate v6.0.3, scikit-learn]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: Briefly, using statsmodels, a Generalized Linear Model with a Negative Binomial link function was fit to the log-transformed UMI counts per cell for each gene y i : y i ~ C ( age ) + log 10 ( total _ counts ) + intercept + ε where C( age ) is a binary categorical variable with the 4-week value set to be the reference level (i.e.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **0.13.2**
- Evidence: ...ackages N/A biopython v1.79, matplotlib v3.7.1, numpy v1.22.3, pandas v1.5.1, scikit-bio v0.5.8, scipy v1.9.3, seaborn v0.11.2, statannot v0.2.3, and statsmodels v0.13.2 Other Leica Reichert Ultracut-S microtome Leica N/A JEOL 1200EX Transmission electron microscope JEOL USA N/A AMT 2k CCD camera Advanced Microscopy Techniques N/A Illumina NovaSeq SP 100 Illumina N/A NanoDrop 2000 Thermo Fisher Sc...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: Analyses were performed using custom code written in Python 3 using standard analysis libraries: numpy, scipy, statsmodels.
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### Human neocortical expansion involves glutamatergic neuron diversification. (Nature 2021)

- DOI: 10.1038/s41586-021-03813-8 | PMCID: PMC8494638 | PMID: 34616067
- Evidence: For each feature, differentiation by t-type was assessed by running a one-way ANOVA for the feature by t-type, using the statsmodels package 69 .
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [ImageJ] -> dimensionality reduction/clustering [Seurat, UMAP, scikit-learn] -> visualisation [scikit-learn] -> stage not stated [statsmodels]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Version used: **0.12.1**
- Evidence: Software versions Software versions used were: Anndata 0.7.1 , bustools 0.39.4 , awk (GNU awk) 4.1.4 , grep (GNU grep) 3.1 , kallisto 0.46.1 , kb_python 0.24.4 , Matplotlib 3.0.3 , Numpy 1.18.1 , Pandas 0.25.3 , Scanpy 1.4.5.post3 , Scipy 1.4.1 , sed (GNU sed) 4.4 , sklearn 0.22.1 , statsmodels 0.12.1 , tar (GNU tar) 1.29 , umap 0.3.10.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Evidence: In Python, we used the mannwhitneyu function from scipy package version 1.3.1 70 for nonparametric tests, and corrected for multiple testing with the statsmodels package version 0.10.1 71 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Version used: **0.12.2**
- Evidence: This yielded linear regression coefficients and two-tailed P values for each gene, which were corrected for multiple-hypothesis testing using the Holm–Sidak method implemented in the statsmodels (release 0.12.2) package to derive q values.
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Evidence: For each proportion, we calculated 90% CIs using Jeffrey’s interval 51 and the function, proportion_confint, from statsmodels.stats.proportion.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: We fit a local regression between predicted and chronological age using the lowess function from the statsmodels 69 python package with fraction parameter set to 2/3 to estimate the true population mean (Supplementary Fig.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### Normative spatiotemporal fetal brain maturation with satisfactory development at 2 years. (Nature 2023)

- DOI: 10.1038/s41586-023-06630-3 | PMCID: PMC10620088 | PMID: 37880365
- Evidence: We then tested whether to reject the null hypothesis of equality (that is, absence of asymmetry) between the left and right hemispheres by computing the Cohen’s d estimates for each brain region with the statsmodels Python package (v.0.13.2).
- Full pipeline: dimensionality reduction/clustering [FSL] -> differential/statistical testing [FSL, statsmodels] -> simulation/modelling [FSL] -> stage not stated [Python v3.9.6, seaborn]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **0.13.5**
- Evidence: FDR Correction for multiple hypothesis testing was performed using the Benjamini–Hochberg procedure (statsmodels v.0.13.5).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### CTCF is a DNA-tension-dependent barrier to cohesin-mediated loop extrusion. (Nature 2023)

- DOI: 10.1038/s41586-023-05961-5 | PMCID: PMC10132984 | PMID: 37076620
- Version used: **0.12.2**
- Evidence: Statistical analysis and reproducibility Statistical analysis was performed using GraphPad Prism (v.9.4.1) or Python (v.3.7.7) using scipy (v.1.5.2) 61 , numpy (v.1.21.6), trackpy (v.0.4.2) 62 and statsmodels (v.0.12.2).
- Full pipeline: differential/statistical testing [NumPy v1.21.6, SciPy v1.5.2, statsmodels v0.12.2]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: ...kage Scipy 49 (v.1.3.1)) for unadjusted analyses and logistic regression (as implemented by the Python package Statsmodels ( https://pypi.org/project/statsmodels/ ; v.0.10.1) for analyses adjusted for the continuous TMB per Mb and/or the primary site of the tumour.
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Version used: **0.11.1**
- Evidence: To calculate the adjusted P value for the 64 bins statsmodels v0.11.1 60 multipletests methods with the parameter method=’fdr_bh’ in Python 3.6 61 was used.
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Version used: **0.12.2**
- Evidence: We used statsmodels (v0.12.2) in Python and, specifically, the ordinary least-squares model found in the statsmodels.api.OLS module to estimate the coefficients of the selected predictors in their corresponding multiple linear regression model 54 .
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: Two-way ANOVA for age group (fetal versus paediatric) and CMA bin was calculated with statsmodels.api.stats.anova_lm(model, type=2).
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Forest fire size amplifies postfire land surface warming. (Nature 2024)

- DOI: 10.1038/s41586-024-07918-8 | PMCID: PMC11424489 | PMID: 39322733
- Evidence: The test corrected for FDR was carried out using the stats.multitest module in the statsmodels Python package based on the Benjamini–Hochberg method.
- Full pipeline: differential/statistical testing [statsmodels]

### Genetic links between ovarian ageing, cancer risk and de novo mutation rates. (Nature 2024)

- DOI: 10.1038/s41586-024-07931-x | PMCID: PMC11410666 | PMID: 39261734
- Evidence: To generate accurate odds ratio and standard error estimates for binary traits, we also implemented a generalized linear model using the statsmodels package 73 for Python in a three-step process.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> differential/statistical testing [REGENIE v2.2.4, statsmodels] -> visualisation [pheatmap, tidyverse] -> stage not stated [R v4.1.2]

### Accurate structure prediction of biomolecular interactions with AlphaFold 3. (Nature 2024)

- DOI: 10.1038/s41586-024-07487-w | PMCID: PMC11168924 | PMID: 38718835
- Version used: **0.12.2**
- Evidence: ...thub.com/mwaskom/seaborn ), Matplotlib v.3.6.1 ( https://github.com/matplotlib/matplotlib ), pandas v.2.0.3 ( https://github.com/pandas-dev/pandas ), statsmodels v.0.12.2 ( https://github.com/statsmodels/statsmodels ), RDKit v.4.3.0 ( https://github.com/rdkit/rdkit ) and Colab ( https://research.google.com/colaboratory ).
- Full pipeline: visualisation [NumPy v1.26.3, SciPy v1.9.3, seaborn v0.12.2] -> stage not stated [AlphaFold, Matplotlib v3.6.1, RDKit, RoseTTAFold, statsmodels v0.12.2]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Handling of geospatial and other data was conducted using the R packages lme4, matrixStats, Matrix, geojsonio, raster, rgeos, sf, sp, tmaptools, patchwork, leaflet, data.table, dplyr, haven, Hmisc, openxlsx, rgdal, scales, stringr, tidyr, tibble, xlsx, rfPermute, randomForest, forcats, and in python using the packages pandas, numpy, scipy, statsmodels, firthlogist, patsy and jupyter 68 – 97 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Network-level encoding of local neurotransmitters in cortical astrocytes. (Nature 2024)

- DOI: 10.1038/s41586-024-07311-5 | PMCID: PMC11062919 | PMID: 38632406
- Version used: **0.12.2**
- Evidence: These P values were adjusted across tested time bins and NTs using the Benjamini–Hochberg procedure to obtain q values, as implemented in statsmodels 0.12.2 (ref.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [statsmodels v0.12.2] -> stage not stated [SciPy v1.6.2]

### Single-neuronal elements of speech production in humans. (Nature 2024)

- DOI: 10.1038/s41586-023-06982-w | PMCID: PMC10866697 | PMID: 38297120
- Version used: **0.13.5**
- Evidence: Models were fit using the Python (v.3.9.17) library statsmodels (v.0.13.5) by iterative least-squares minimization of the Poisson negative log-likelihood function 86 .
- Full pipeline: dimensionality reduction/clustering [Kilosort v1.0, scikit-learn] -> structure determination [FreeSurfer v7.4.1] -> stage not stated [FieldTrip, statsmodels v0.13.5]

### Oxidative potential of atmospheric particles in Europe and exposure scenarios. (Nature 2025)

- DOI: 10.1038/s41586-025-09666-9 | PMCID: PMC12589103 | PMID: 41125890
- Evidence: 1 and 3 and Supplementary Table 2 ) using relative weights calculated as follows (using DescrStatsW() function of the statsmodels package in Python): 1 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$${p}_{{\rm{c}}{\rm{...
- Full pipeline: stage not stated [Python, statsmodels]

### Efficient and accurate search in petabase-scale sequence repositories. (Nature 2025)

- DOI: 10.1038/s41586-025-09603-w | PMCID: PMC12657231 | PMID: 41062695
- Evidence: 4b , we report all antibiotics for which we measure statistically significant growth in at least one continent (modelled through a binomial GLM using the Python statsmodels package v.0.14.0).
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.0] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [Docker, Python, R v71.2, Snakemake]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: A linear mixed-effects model (mixedlm() from statsmodels) tested cell-level fluorescence intensities, modelling genotype or treatment as a fixed effect and well of origin as a random effect.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: Methods Overview of software, data and workflow We conducted our LSP mapping workflow using Google Earth Engine (GEE) (v.0.1.404 or later) 65 and performed additional analyses using Python 66 with a set of core scientific packages (numpy 67 , shapely 68 , pandas 69 , geopandas 70 , rasterio 71 , xarray 72 , rasterstats 73 , dask 74 , scipy 75 , scikit-learn 76 , statsmodels 77 and matplotlib 78 ).
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: These tools internally rely on scipy 101 and statsmodels 102 and were used to perform either Benjamini-Hochberg or Holm–Šidák-corrected two-tailed t -tests (for cluster composition and differential abundance analysis), Mann–Whitney U -tests (for differences in nucleus counts and cell-level metacluster abundance) or nonparametric Wilcoxon rank-sum tests (for differential gene expression from single...
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Evidence: Models were defined and fit using the statsmodels 55 Python package using Poisson and negative binomial likelihoods with the identity ( f ( x ) = x ) and log link functions ( f ( x ) = log x ).
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: A multiple test correction 119 was performed on the P values using the Python library statsmodels 120 .
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Dopaminergic action prediction errors serve as a value-free teaching signal. (Nature 2025)

- DOI: 10.1038/s41586-025-09008-9 | PMCID: PMC12310545 | PMID: 40369067
- Evidence: Regression predicting current trial dopamine from past choices We performed a linear regression (using statsmodels.api.OLS) predicting the size of the dopamine response (TS dopamine at time of choice, VS dopamine at time of cue) on correct contralateral trials from previous choices for the same stimulus.
- Full pipeline: quantification [DeepLabCut] -> differential/statistical testing [Python, scikit-learn, statsmodels] -> stage not stated [SciPy, pingouin]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Evidence: To account for multiple comparisons, we adjusted P values using the Benjamini–Hochberg procedure as implemented in the statsmodels package.
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Connectomics of predicted Sst transcriptomic types in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08805-6 | PMCID: PMC11981948 | PMID: 40205210
- Evidence: We used the following libraries for visualization and analysis: Matplotlib 73 , Seaborn 74 , Numpy 75 , Pandas 76 , VTK 77 , Scipy 78 , Scikit-posthocs 79 , Scikit-learn 80 , scrattch-hicat ( https://github.com/AllenInstitute/scrattch.hicat/ ) and statsmodels 81 .
- Full pipeline: differential/statistical testing [limma] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn, seaborn, statsmodels]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Evidence: In brief, LOESS regression was performed on using the lowess function of the statsmodels package (v.0.13.5) in Python (v.3.9.12) with a 20 amino acid sliding window (‘frac = (20 AA/ L )’, where L is the total length of the protein), and ‘it = 0’ to fit observed log 2 [fold change in sgRNA enrichment], hereafter the sgRNA enrichment score, as a function of amino acid position.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Complete human recombination maps. (Nature 2025)

- DOI: 10.1038/s41586-024-08450-5 | PMCID: PMC11922761 | PMID: 39843742
- Version used: **0.13.2**
- Evidence: ...NCOurd ; R (v.4.2.2 with lm v.4.2.2, xoi v.0.67-1), https://www.r-project.org/ ; Python (v.3.8.1 with numpy v.1.24.2, pandas v.1.4.0, scipy v.1.10.1, statsmodels v.0.13.2), https://www.python.org/downloads/ .
- Full pipeline: stage not stated [NumPy v1.24.2, SciPy v1.10.1, lme4, statsmodels v0.13.2]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Version used: **0.13.2**
- Evidence: For other data analysis and plotting tasks, we used Python (3.8.13), pandas (1.4.2), matplotlib (3.5.1), seaborn (0.12.2), numpy (1.21.6), scipy (1.8.0), sklearn (1.0.2), anndata (0.8.0), scanpy (1.9.1), squidpy (1.1.2), tissue-sc (0.0.2), tangram-sc (1.0.3), spage (accessed September 1, 2022), gseapy (1.0.4), umap-learn (0.5.3) and statsmodels (0.13.2).
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Relativistic electron acceleration at the bow shock of Jupiter and beyond. (Nature 2026)

- DOI: 10.1038/s41586-026-10473-z | PMCID: PMC13233311 | PMID: 42236560
- Version used: **0.14.4**
- Evidence: We performed a linear fit for each model in the log–log space using ordinary least squares as implemented by the statsmodels (v.0.14.4) of Python library.
- Full pipeline: visualisation [Matplotlib] -> stage not stated [statsmodels v0.14.4]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Version used: **0.14.0**
- Evidence: All behavioural and neural analyses were performed using custom-written Python (v.3.8) code unless otherwise noted, incorporating the analysis and plotting libraries numpy (v.1.24.3), scipy (v.1.10.1), scikit-learn (v.1.3.0), pandas (v.2.0.3), seaborn (v.0.12.2), elephant (v.1.0.0) and statsmodels (v.0.14.0).
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### An AI system to help scientists write expert-level empirical software. (Nature 2026)

- DOI: 10.1038/s41586-026-10658-6 | PMCID: PMC13293872 | PMID: 42156545
- Evidence: For each dataset, we used a search of 300 nodes, with the system permitted to use a broad suite of machine learning libraries, including scikit-learn, XGBoost and statsmodels.
- Full pipeline: stage not stated [NumPy, XGBoost, scikit-learn, statsmodels]

### Demography and life histories across the Roman frontier in Germany 400-700 CE. (Nature 2026)

- DOI: 10.1038/s41586-026-10437-3 | PMCID: PMC13293882 | PMID: 42056513
- Version used: **0.14.4**
- Evidence: A regression analysis with the Python package statsmodels (v.0.14.4) 82 was used to determine the relationships between N , m and r for both communities, given the observed values (see Supplementary Information 16 ).
- Full pipeline: alignment/mapping [Matplotlib, Python] -> registration [GATK v3.8] -> differential/statistical testing [statsmodels v0.14.4]

### Training language models to be warm can reduce accuracy and increase sycophancy. (Nature 2026)

- DOI: 10.1038/s41586-026-10410-0 | PMCID: PMC13128435 | PMID: 42056545
- Evidence: We used α = 0.05 for all tests conducted in Python 3.11.4 with the statsmodels package.
- Full pipeline: stage not stated [Python v3.11.4, statsmodels]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Evidence: For analysis of relative changes in pseudotype entry, significance was quantified using the Python3 module statsmodels ( https://www.statsmodels.org/ ) with technical replicates averaged and treatment effects quantified as log 10 -transformed fold changes relative to the control (untreated) sample.
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **0.14.6**
- Evidence: Data processing, model training and evaluation were implemented in Python using numpy v.2.0.2, tensorflow v.2.19.0, scipy v.1.16.3, statsmodels v.0.14.6, sklearn v.1.6.1, shap v.0.50.0, xgboost v.3.1.2, torch v.2.9.0, pandas v.2.2.2, umap v.0.5.9.post2, pickle v.4.0, pytz v.2025.2, re v.2.2.1, tqdm v.4.67.1, IPython v.7.34.0, json v.2.0.9 and altair v.5.5.0.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **0.14.0**
- Evidence: Statistical analysis Statistical analyses were performed in Python (v3.10.12) using libraries scikit-bio (v0.5.9), scipy (v1.10.1) and statsmodels (v0.14.0).
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Version used: **0.14.0**
- Evidence: Analyses we carried out with Python (v.3.12.0), using also the following libraries: numpy (v.1.26.2), scipy (v.1.11.4), statsmodels (v.0.14.0), and matplotlib (v.3.8.2) and seabron (v.0.11.2) for visualization.
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### Microbial population dynamics and evolutionary outcomes under extreme energy limitation. (PNAS 2021)

- DOI: 10.1073/pnas.2101691118 | PMCID: PMC8379937 | PMID: 34385301
- Evidence: We tested whether p N / p S was less than 1 in each taxon using a left-tailed one-sided t test and corrected for multiple testing using the Benjamini–Hochberg procedure from statsmodels ( 70 ).
- Full pipeline: read trimming [Cutadapt] -> stage not stated [R v3.5, statsmodels]

### Global inequality remotely sensed. (PNAS 2021)

- DOI: 10.1073/pnas.1919913118 | PMCID: PMC8106331 | PMID: 33903226
- Evidence: The analysis was carried out in R ( https://www.r-project.org ) using the packages raster, rasterVis, sp, rgdal, ggplot2, and mixtools and Python ( https://www.python.org/ ) using numpy, matplotlib, scipy, and statsmodels.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, statsmodels]

### Topographic connectivity reveals task-dependent retinotopic processing throughout the human brain. (PNAS 2021)

- DOI: 10.1073/pnas.2017032118 | PMCID: PMC7812773 | PMID: 33372144
- Evidence: Correlations across vertices between CF parameters, as well as t tests of the differences in CF parameters across experiments ( SI Appendix , Table S1 ), were calculated weighted by the null-model–corrected correlation values using the statsmodels.stats.weightstats package, which adjusts the degrees of freedom based on the applied weighting.
- Full pipeline: stage not stated [FSL, FreeSurfer, SciPy, statsmodels]

### Hippocampal ripples signal contextually mediated episodic recall. (PNAS 2022)

- DOI: 10.1073/pnas.2201657119 | PMCID: PMC9546603 | PMID: 36161912
- Evidence: Equations Linear mixed-effects models are run by using the function MixedLM in the python package statsmodels with restricted maximum likelihood and Nelder–Mead optimization with a maximum of 2,000 iterations.
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> differential/statistical testing [statsmodels]

### Face neurons encode nonsemantic features. (PNAS 2022)

- DOI: 10.1073/pnas.2118705119 | PMCID: PMC9169805 | PMID: 35377737
- Evidence: One or two tailedness of tests and other types of tests are noted in the text and were implemented using the Python library “scipy.stats.” P values for multiple comparisons were corrected to control false discovery rate at the level of 0.05 using the two-stage Benjamini–Krieger–Yekutieli procedure ( 38 ) as implemented in the Python library “statsmodels” ( 39 ).
- Full pipeline: differential/statistical testing [SciPy, statsmodels]

### Stochastic microbiome assembly depends on context. (PNAS 2022)

- DOI: 10.1073/pnas.2115877119 | PMCID: PMC8851475 | PMID: 35135881
- Evidence: 2 and 3 A–C were computed using the Jeffreys interval (derived from Bayesian statistics) as implemented in the statsmodels.stats.proportion.proportion_confint Python function.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [Python v3.9.7, R v4.1.1]

### The weekly cycle of photosynthesis in Europe reveals the negative impact of particulate pollution on ecosystem productivity. (PNAS 2023)

- DOI: 10.1073/pnas.2306507120 | PMCID: PMC10710040 | PMID: 37983483
- Evidence: The regression analysis is conducted by “statsmodels” package in Python.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [Python]

### Hippocampal activity predicts contextual misattribution of false memories. (PNAS 2023)

- DOI: 10.1073/pnas.2305292120 | PMCID: PMC10556612 | PMID: 37751551
- Evidence: Linear mixed effects models were run using the MixedLM function in the package statsmodels in Python ( 102 ), and always included a random intercept for each session, nested in participant.
- Full pipeline: differential/statistical testing [Python, statsmodels]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Evidence: The linear regression was performed using the statsmodels package and the Pearson correlation coefficient was calculated using the pingouin package in Python.
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### People who share encounters with racism are silenced online by humans and machines, but a guideline-reframing intervention holds promise. (PNAS 2024)

- DOI: 10.1073/pnas.2322764121 | PMCID: PMC11420153 | PMID: 39250662
- Evidence: We fitted a logistic regression model, using standard Python libraries numpy and statsmodels ( 87 , 88 ).
- Full pipeline: differential/statistical testing [NumPy, statsmodels]

### Robust inference of causality in high-dimensional dynamical processes from the Information Imbalance of distance ranks. (PNAS 2024)

- DOI: 10.1073/pnas.2317256121 | PMCID: PMC11087807 | PMID: 38687797
- Evidence: Statistical assessment on Imbalance Gain data was performed using SciPy ( 49 ) and statsmodels ( 51 ) packages in Python.
- Full pipeline: differential/statistical testing [Python, statsmodels] -> stage not stated [SciPy]

### Logic-based mechanistic machine learning on high-content images reveals how drugs differentially regulate cardiac fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2303513121 | PMCID: PMC10835125 | PMID: 38266046
- Evidence: Automated data analysis and statistical calculations were performed using Python 3.8.5 and the “statsmodels” Python module version 0.13.2.
- Full pipeline: quantification [CellProfiler] -> differential/statistical testing [Python v3.8.5, statsmodels]

### Distinct classes of gut bacterial molybdenum-dependent enzymes produce urolithins. (PNAS 2025)

- DOI: 10.1073/pnas.2501312122 | PMCID: PMC12771579 | PMID: 41439715
- Evidence: A “statsmodels” python package (v0.14.1) was used to perform multivariate linear regression analysis between the gene abundances and urolithin A levels in paired metagenome and metabolome samples.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [statsmodels] -> differential/statistical testing [DESeq2 v1.44.0, statsmodels]

### The variability of evolvability: Properties of dynamic fitness landscapes determine how phenotypic variability evolves. (PNAS 2025)

- DOI: 10.1073/pnas.2519469122 | PMCID: PMC12745803 | PMID: 41397131
- Evidence: Maximum and average fitness was compared between variable and static runs for each fitness landscape pair using the Mann–Whitney U [scipy.stats, ( 48 )] test followed by Benjamini/Hochberg calculation of false discovery rate [statsmodels, ( 49 )] to account for multiple testing across fitness landscape pairs.
- Full pipeline: variant calling [scikit-learn] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, statsmodels]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Evidence: We used ordinary least squares regression, implemented in the python package statstmodels in statsmodels.formula.api.ols, to fit a model predicting the phenotype from factors.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### Habenula-ventral tegmental area functional coupling and risk aversion in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2500815122 | PMCID: PMC12595472 | PMID: 41166429
- Evidence: Adjusted P values were calculated using the Python package “statsmodels” (0.14.4) with the Benjamini–Hochberg Procedure for Controlling the False Positive Rate (reported as P FDR ).
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [FSL, PsychoPy v2021.1.4, lavaan]

### A steady-state pool of calcium-dependent actin is maintained by Homer and controls epithelial mechanosensation. (PNAS 2025)

- DOI: 10.1073/pnas.2509784122 | PMCID: PMC12582288 | PMID: 41134626
- Evidence: The following python packages were used: numpy, pandas, statsmodels, and scipy for organizing, sorting, and processing (normalization, smoothing, peak/trough finding) to automatically determine analysis windows based on displacement and extract data for various parameters; statsmodels for OLS analysis; matplotlib and seaborn for presentation.
- Full pipeline: quantification [napari] -> normalisation [Matplotlib, NumPy, SciPy, seaborn, statsmodels] -> differential/statistical testing [R] -> stage not stated [ImageJ, scikit-image]

### Spatially resolved DNP-assisted NMR illuminates the conformational ensemble of α-synuclein in intact viable cells. (PNAS 2025)

- DOI: 10.1073/pnas.2500367122 | PMCID: PMC12168001 | PMID: 40465629
- Evidence: In-cell spectra were fit to a linear combination of the experimental spectra of nanodisc bound α-syn, which is α-helical, and purified frozen intrinsically disordered α-syn using the generalized least squares regression function in statsmodels.api.
- Full pipeline: differential/statistical testing [NumPy, statsmodels]

### Transition ability to safe states reduces fear responses to height. (PNAS 2025)

- DOI: 10.1073/pnas.2416920122 | PMCID: PMC12107115 | PMID: 40359043
- Version used: **0.11.1**
- Evidence: We used the statsmodels 0.11.1 package in Python to assess the statistical significance of differences and set the significance level at P < 0.05.
- Full pipeline: differential/statistical testing [Python, statsmodels v0.11.1]

### Pulse timing dominates binaural hearing with cochlear implants. (PNAS 2025)

- DOI: 10.1073/pnas.2416697122 | PMCID: PMC12036976 | PMID: 40244669
- Evidence: This three-way repeated measures ANOVA, performed with the statsmodels python library ( https://statsmodels.org ), leads to identical conclusions to those obtained with the two separate two-way ANOVAs described above.
- Full pipeline: stage not stated [pingouin, statsmodels]

### Learning reshapes the hippocampal representation hierarchy. (PNAS 2025)

- DOI: 10.1073/pnas.2417025122 | PMCID: PMC11929462 | PMID: 40063792
- Version used: **0.14**
- Evidence: We utilized the routine GLM.fit_regularized offered by the package statsmodels v0.14 in Python 3.11 ( 65 ).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [Python v3.11, statsmodels v0.14]

### Discrepancies between subjective and objective sleep assessments revealed by in-home electroencephalography during real-world sleep. (PNAS 2025)

- DOI: 10.1073/pnas.2412895121 | PMCID: PMC11761674 | PMID: 39819218
- Evidence: The analyses were performed using statsmodels in Python ( 40 ).
- Full pipeline: stage not stated [Python, scikit-learn, statsmodels]

### Multimodal analysis reveals cellular diversity and divergent circuits of the zona incerta. (PNAS 2026)

- DOI: 10.1073/pnas.2509781123 | PMCID: PMC13143026 | PMID: 42054363
- Evidence: Parametric tests (statsmodels) were used as default when data were found to exhibit normal distributions, and Welch’s correction was applied in the case of unequal variance between the groups under comparison.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [SciPy, statsmodels]

### Tau catalyzes amyloid-β aggregation and toxicity in a polymorph-dependent manner. (PNAS 2026)

- DOI: 10.1073/pnas.2532775123 | PMCID: PMC13037932 | PMID: 41880569
- Evidence: Analyses were performed using a custom Python script with the statsmodels module.
- Full pipeline: differential/statistical testing [SciPy v1.13.1] -> stage not stated [Python, statsmodels]

### Control of microglial dynamics by the Arp2/3 complex and the autism- and schizophrenia-associated protein CYFIP1. (PNAS 2026)

- DOI: 10.1073/pnas.2532488123 | PMCID: PMC12993954 | PMID: 41818151
- Evidence: All statistical analysis was carried out using GraphPad Prism (GraphPad Software, CA, USA) or the Python statsmodels package.
- Full pipeline: registration [ImageJ] -> differential/statistical testing [statsmodels]

### Single-cell analyses identify independent aging processes that compete to determine cellular fate in budding yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2534452123 | PMCID: PMC12993945 | PMID: 41811451
- Evidence: The models were fit using the statsmodels Python package.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, kallisto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Scanpy v1.11.0, statsmodels]

### Soluble adenylyl cyclase in nonmammalian sperm is directly controlled by pH, not by HCO&lt;sub&gt;3&lt;/sub&gt;&lt;sup&gt;-&lt;/sup&gt; or Ca&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2505026123 | PMCID: PMC12867704 | PMID: 41591904
- Version used: **0.14.4**
- Evidence: 2 and 4 were performed with scipy (version 1.15.1) and statsmodels (version 0.14.4) in python (3.12.3).
- Full pipeline: alignment/mapping [AlphaFold v2.2.4, ColabFold v1.5.2, MAFFT] -> stage not stated [BLAST, SciPy v1.15.1, statsmodels v0.14.4]

### Dosa: A method to covalently barcode proteins for high-throughput biochemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2529762123 | PMCID: PMC12773776 | PMID: 41481464
- Evidence: Proportion tests were performed using the prop.test function from the statsmodels package in Python 3.0, executed within a Google Colab environment.
- Full pipeline: stage not stated [Python v3.0, statsmodels]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **0.11.1**
- Evidence: Software The following Python (version 3.8.2) software packages were used in the data analysis and in the production of figures: Scipy (version 1.4.1) ( 78 ), pandas (version 1.0.3) ( 79 ), statsmodels (version 0.11.1) ( 80 ), matplotlib (version 3.2.1) ( 81 ), numpy (1.18.3) ( 82 ), seaborn_sinaplot ( 83 ), simanneal (version 0.5.0) ( 71 ), and seaborn (version 0.10.1) ( 84 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Version used: **0.13.5**
- Evidence: Background-signal regression was then carried out using a Gaussian linear model (GLM) per protein, constructed using the GLM function from statsmodels (v0.13.5) on standardized, per cell background scores (BG_score).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Hidden state inference requires abstract contextual representations in the ventral hippocampus. (Science 2024)

- DOI: 10.1126/science.adq5874 | PMCID: PMC7618349 | PMID: 39571013
- Evidence: Statistical analysis All statistics were calculated using the Python packages scipy, pingouin and statsmodels , and lme4 R package implemented in Python through rpy2.
- Full pipeline: differential/statistical testing [R, lme4, pingouin, scikit-learn, statsmodels] -> stage not stated [Python, SciPy]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: Significance was determined using Mann-Whitney U test with Bonferroni correction (with scipy.stats.mannwhitneyu and statsmodels.stats.multitest.multipletests) ( Fig.
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

