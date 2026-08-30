# seaborn

- **Category:** general
- **Papers in survey:** 149
- **Journals:** Nature (75), PNAS (40), Cell (23), Science (11)
- **Years:** 2021 (13), 2022 (17), 2023 (28), 2024 (27), 2025 (48), 2026 (16)
- **Versions named:** 0.12.2 (14), 0.11.0 (8), 0.11.2 (8), 0.13.2 (6), 0.9.0 (5), 0.11.1 (3), 0.10.1 (3), 0.13.0 (3), 0.13 (2), 0.13.1 (1)
- **Pipeline stages it appears in:** visualisation (62), differential/statistical testing (17), dimensionality reduction/clustering (16), normalisation (6), machine learning (3), simulation/modelling (3), quantification (2), registration (1), alignment/mapping (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: Further, these score distributions were visualized through a normalized kernel density estimation implemented in the Seaborn python package.
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **0.10.1**
- Evidence: ...ersion 1.7.2 Wolf et al., 2018 https://scanpy.readthedocs.io/en/stable/ scVI version 0.6.7 Gayoso et al., 2021 https://scvi-tools.org/ Python package seaborn version 0.10.1 Waskom, 2021 https://seaborn.pydata.org/ Python package scipy version 1.5.2 Virtanen et al., 2020 https://scipy.org/ Python package numpy version 1.20.3 Harris et al., 2020 https://numpy.org/ Python package matplotlib version 3...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Identification of a therapeutic interfering particle-A single-dose SARS-CoV-2 antiviral intervention with a high barrier to resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.004 | PMCID: PMC8577993 | PMID: 34838159
- Version used: **0.11.0**
- Evidence: Data tabulation and visualizations were done with Pandas (v1.1.4), Seaborn (v0.11.0) and Matplotlib (v3.3.3).
- Full pipeline: quantification [DESeq2, featureCounts] -> simulation/modelling [Python] -> visualisation [Matplotlib v3.3.3, seaborn v0.11.0] -> stage not stated [ImageJ, NumPy v1.19.4, SciPy v1.5.4]

### Functional diversity for body actions in the mesencephalic locomotor region. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.002 | PMCID: PMC8382160 | PMID: 34302739
- Evidence: For each behavior, the distribution of the duration of behavioral episodes was studied by computing KDE density through Seaborn, a Python data visualization.
- Full pipeline: differential/statistical testing [R, scikit-learn] -> visualisation [seaborn] -> stage not stated [DeepLabCut, Python v3.7, SciPy, ilastik v1.1.5]

### Microbial exposure during early human development primes fetal immune cells. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.039 | PMCID: PMC8240556 | PMID: 34077752
- Version used: **0.9.0**
- Evidence: ...e Foundation https://www.python.org/ matplotlib 3.2.1 PyPI https://pypi.org/ numpy 1.19.4 PyPI https://pypi.org/ pandas 0.25.3 PyPI https://pypi.org/ seaborn 0.9.0 PyPI https://pypi.org/ Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact: Florent Ginhoux ( florent_ginhoux@immunol.a-star.edu....
- Full pipeline: alignment/mapping [pandas] -> dimensionality reduction/clustering [QIIME 2 v1.8.0, R v4.4, UMAP] -> stage not stated [ImageJ, Matplotlib v3.2.1, NumPy v1.19.4, Python v2.7.0, seaborn v0.9.0]

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Evidence: Comparison analysis were performed in Python using NumPy ( https://numpy.org/ ) and, Pandas ( https://pandas.pydata.org/ ) while figures were produced using the Matplotlib tool ( https://matplotlib.org/ ) and Seaborn ( https://seaborn.pydata.org/ ).
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### Dynamic 3D proteomes reveal protein functional alterations at high resolution in situ. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.021 | PMCID: PMC7836100 | PMID: 33357446
- Evidence: 2.7, 3.0 Python Software Foundation https://www.python.org Pandas library for python, 0.18.1 NumFOCUS https://pandas.pydata.org/ Seaborn library for python v.
- Full pipeline: differential/statistical testing [SciPy, limma] -> stage not stated [AutoDock Vina v1.1.2, Bioconductor, NAMD v2.13, PyMOL v2.4, Python, R, pheatmap, seaborn]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: 1.3.0) hierarchy linkage function ( Virtanen et al., 2020 ) via Seaborn’s (v.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Accurate de novo design of membrane-traversing macrocycles. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.019 | PMCID: PMC9490236 | PMID: 36041435
- Evidence: ... The hydrogen bonding and structure prediction data was plotted using python scripts using pandas ( McKinney, 2010 ), matplotlib ( Hunter, 2007 ) and seaborn ( Waskom, 2021 ) libraries.
- Full pipeline: dimensionality reduction/clustering [PyMOL] -> visualisation [Matplotlib, PyMOL, seaborn] -> stage not stated [CCP4]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Neutralizing immunity in vaccine breakthrough infections from the SARS-CoV-2 Omicron and Delta variants. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.019 | PMCID: PMC8930394 | PMID: 35429436
- Evidence: Plots were generated using ggplot2 package (version 3.3.5) in R and seaborn package (version 0.11.0) in Python.
- Full pipeline: read trimming [BLAST] -> quantification [Python v3.7.10] -> differential/statistical testing [Python v3.7.10] -> visualisation [Python v3.7.10] -> stage not stated [Pangolin, R v4.0, ggplot2, seaborn]

### Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.018 | PMCID: PMC8786601 | PMID: 35148837
- Version used: **0.11.2**
- Evidence: Plots were created with Python packages matplotlib version 3.3.2 and seaborn version 0.11.2.
- Full pipeline: dimensionality reduction/clustering [NumPy v1.19.1, scikit-learn v1.0] -> visualisation [SciPy v1.6.2] -> stage not stated [Matplotlib v3.3.2, QuPath v0.2.3, R v4.0.5, ggplot2, seaborn v0.11.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...en et al., 2020 ) v0.1.24 https://github.com/theislab/scvelo Sparse Decomposition of Arrays ( Hore et al., 2016 ) https://jmarchini.org/software/#sda Seaborn Waskom v0.11.1 https://seaborn.pydata.org/ Seurat ( Stuart et al., 2019 ) v3.9.9.9010 SIMON ( Tomic et al., 2019 ) https://genular.org/ singleR ( Aran et al., 2019 ) https://github.com/dviraran/SingleR STAR ( Dobin et al., 2013 ) v2.7.3 strin...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Data visualization and plots were generated in R with ggplot and pheatmap packages, in GraphPad Prism, and in Python using the scikitimage, matplotlib, and seaborn packages.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: For cell density visualization along pseudotime 44 the cell count was smoothed with a Gaussian kernel according to the default parameters of seaborn's (v 0.11.1) kdeplot function.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: Visualizations were performed using GraphPad Prism or Seaborn in Python.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **0.11.2**
- Evidence: ...1071 v.1.7.6, and table1 v.1.4 Python packages N/A biopython v1.79, matplotlib v3.7.1, numpy v1.22.3, pandas v1.5.1, scikit-bio v0.5.8, scipy v1.9.3, seaborn v0.11.2, statannot v0.2.3, and statsmodels v0.13.2 Other Leica Reichert Ultracut-S microtome Leica N/A JEOL 1200EX Transmission electron microscope JEOL USA N/A AMT 2k CCD camera Advanced Microscopy Techniques N/A Illumina NovaSeq SP 100 Illu...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Evidence: Data and Statistical analyses Data and statistical analyses were performed in Python 3.6 ( https://www.python.org/downloads/release/python-363/ ), using the packages scipy 139 , numpy 140 , matplotlib 141 , seaborn 142 , pandas 143 , scikit-learn 144 .
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: Volcano plots were made with seaborn.scatterplot on −log 10 (false discovery rate) 192 .
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: These quantitative data were exported to Python for further statistical analysis and data visualization, utilizing the scikit-learn and seaborn libraries.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Inner speech in motor cortex and implications for speech neuroprostheses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.015 | PMCID: PMC12360486 | PMID: 40816265
- Version used: **0.13.0**
- Evidence: ...33 Pandas 2.1.3 pandas.pydata.org RRID:SCR_018214 scikit-learn 1.3.2 scikit-learn.org RRID:SCR_002577 matplotlib 3.8.2 matplotlib.org RRID:SCR_008624 seaborn 0.13.0 seaborn.pydata.org RRID:SCR_018132 AWS Polly aws-cli/2.22.29 Amazon Web Services aws.amazon.com RRID:SCR_012854 Custom analysis code Repository provided upon acceptance.
- Full pipeline: stage not stated [Matplotlib v3.8.2, NumPy v1.26.2, Python v3.9, SciPy v1.11.4, scikit-learn v1.3.2, seaborn v0.13.0]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: Software packages All data analyses were performed using custom code written in Python 3 using standard analysis and plotting libraries: numpy, scipy, scikit-learn, matplotlib and seaborn.
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### Contextual computation by competitive protein dimerization networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.036 | PMCID: PMC11973712 | PMID: 39978343
- Version used: **0.12.2**
- Evidence: More specifically, violins show the kernel density estimate calculated using the kdeplot function of seaborn (version 0.12.2).
- Full pipeline: stage not stated [NetworkX, Python v3.8.13, SciPy, seaborn v0.12.2]

### Cortical responses to touch reflect subcortical integration of LTMR signals. (Nature 2021)

- DOI: 10.1038/s41586-021-04094-x | PMCID: PMC9289451 | PMID: 34789880
- Version used: **0.11.0**
- Evidence: Data Analysis and Statistics Data were analyzed in Matlab (versions 2017a and 2017b) and python (version 3.7.7) using the following packages (versions in parentheses): conda (4.8.5), matplotlib (3.3.1), numpy (1.18.5), pims (0.5), pyabf (2.2.6), scipy (1.5.2), scikit-image (0.16.2), scikit-learn (0.23.2), and seaborn (0.11.0).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Matplotlib v3.3.1, NumPy v1.18.5, SciPy v1.5.2, scikit-image v0.16.2, seaborn v0.11.0]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: The data were plotted using Seaborn package bar plot and swarmplot functions (v.0.11.0).
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Expression dynamics of gene sets associated with bulk ATAC-seq clusters across Normal , Injury , Kras* , Kras*+Injury and PDAC sample were visualized as heatmap of normalized median expression values plotted with seaborn in python.
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Evidence: Hierarchical clustering of the activity clusters was performed on the effect sizes using the seaborn method clustermap with the default parameters for average Euclidean clustering.
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Evidence: Having identified the optimal number of clusters, k , we labelled every DEG with its assigned cluster and visualized average behaviour (median) and the 95% CI (bootstrapped using 1,000 iterations) per cluster using Seaborn line plot (v.0.10.0).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### CD201&lt;sup&gt;+&lt;/sup&gt; fascia progenitors choreograph injury repair. (Nature 2023)

- DOI: 10.1038/s41586-023-06725-x | PMCID: PMC10665192 | PMID: 37968392
- Evidence: All quantification plots were generated using the Python-based packages Matplotlib and Seaborn.
- Full pipeline: alignment/mapping [STAR v2.5.2a, Scanpy] -> quantification [Matplotlib, seaborn] -> dimensionality reduction/clustering [UMAP, scVelo] -> differential/statistical testing [SciPy] -> simulation/modelling [scVelo]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: Seaborn 62 was used for bar plots, box-and-whisker plots and KDE plots.
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Normative spatiotemporal fetal brain maturation with satisfactory development at 2 years. (Nature 2023)

- DOI: 10.1038/s41586-023-06630-3 | PMCID: PMC10620088 | PMID: 37880365
- Evidence: Plots were generated using the Python seaborn package (v.0.12.1), and cortical surface maps were created using the Python-based ggseg package (v.0.1).
- Full pipeline: dimensionality reduction/clustering [FSL] -> differential/statistical testing [FSL, statsmodels] -> simulation/modelling [FSL] -> stage not stated [Python v3.9.6, seaborn]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **0.11.0**
- Evidence: The following packages and software were used in data analysis: UCSF ChimeraX 1.0, ImageJ 1.51, MATLAB R2019b, R 4.0.4, RStudio 1.4.1106, Jupyter Notebook 6.0.3, Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-i...
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Clustering predicted structures at the scale of the known protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06510-w | PMCID: PMC10584675 | PMID: 37704730
- Version used: **0.12.2**
- Evidence: For plotting, Python v.3.10.6 ( https://www.python.org/ ), Matplotlib v.3.6.2 ( https://matplotlib.org/ ), seaborn v.0.12.2 ( https://github.com/mwaskom/seaborn ), ChimeraX v.1.5 ( https://www.cgl.ucsf.edu/chimerax/ ), Pavian commit: cd2f21 ( https://fbreitwieser.shinyapps.io/pavian/ ) and pandas v.1.5.2 ( https://github.com/pandas-dev/pandas ) were used.
- Full pipeline: stage not stated [AlphaFold, BLAST, ChimeraX v1.5, ColabFold, Matplotlib v3.6.2, seaborn v0.12.2]

### A foundation model for generalizable disease detection from retinal images. (Nature 2023)

- DOI: 10.1038/s41586-023-06555-x | PMCID: PMC10550819 | PMID: 37704728
- Version used: **0.12.0**
- Evidence: Results were further analysed and visualized with Python v.3.6, NumPy v.1.19.5, SciPy v.1.5.4, seaborn v.0.12.0, Matplotlib v.3.6.1, pandas v.1.5.0, Scikit-Learn v.1.1.3 and Pillow v.9.2.0.
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.19.5, SciPy v1.5.4, seaborn v0.12.0] -> stage not stated [Keras, PyTorch]

### Complete human day 14 post-implantation embryo models from naive ES cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06604-5 | PMCID: PMC10584686 | PMID: 37673118
- Version used: **0.11.0**
- Evidence: Visualization and statistical analyses of the cell numbers and SEM efficiencies were performed using Python (v.3.8.5) software with scipy (v.1.8.0) and seaborn (v.0.11.0) libraries.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Signac v1.6.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [SciPy v1.8.0, seaborn v0.11.0] -> visualisation [SciPy v1.8.0, seaborn v0.11.0] -> stage not stated [R, pheatmap, scDblFinder v1.6]

### Health system-scale language models are all-purpose prediction engines. (Nature 2023)

- DOI: 10.1038/s41586-023-06160-y | PMCID: PMC10338337 | PMID: 37286606
- Version used: **0.12.2**
- Evidence: This work used several open-source libraries, including HuggingFace Transformers 4.19.2, Datasets 2.2.2, Evaluate 0.1.1, wandb 0.12.17, matplotlib 3.5.2, seaborn 0.12.2, pandas 1.4.2, ray 2.0.0, sklearn 1.1.1, deepspeed 0.8.0+384f17b, NVIDIA Apex, XGBoost 1.6.1 and nltk 3.6.3.
- Full pipeline: stage not stated [Matplotlib v3.5.2, Python v3.8.13, XGBoost, scikit-learn, seaborn v0.12.2]

### Class B1 GPCR activation by an intracellular agonist. (Nature 2023)

- DOI: 10.1038/s41586-023-06169-3 | PMCID: PMC10307627 | PMID: 37286611
- Evidence: The simulation results were analysed and visualized using mdtraj (v.1.9.8) 51 , seaborn ( https://zenodo.org/record/54844 ) and CUEMOL (v.2.2.3.443) ( http://www.cuemol.org ).
- Full pipeline: registration [RELION] -> simulation/modelling [MDTraj v1.9.8, NAMD v2.13, seaborn] -> visualisation [MDTraj v1.9.8, seaborn] -> stage not stated [Fiji, ImageJ, VMD v1.9.3]

### Gap junctions desynchronize a neural circuit to stabilize insect flight. (Nature 2023)

- DOI: 10.1038/s41586-023-06099-0 | PMCID: PMC10232364 | PMID: 37225999
- Evidence: For additional functions, the Python libraries NumPy, pickle, SciPy, Matplotlib and seaborn were imported.
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, Python, SciPy, seaborn]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Version used: **0.11.0**
- Evidence: Data visualization Plots were generated using matplotlib (version 3.3.2), seaborn (version 0.11.0) and plotly (version 5.6.0) packages in Python software (version 3.7.12), Jupyter notebook (version 6.1.4), RStudio (version 1.4) and Adobe Illustrator (version 26.4.1) software.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### Tropical deforestation causes large reductions in observed precipitation. (Nature 2023)

- DOI: 10.1038/s41586-022-05690-1 | PMCID: PMC9995269 | PMID: 36859548
- Evidence: 2 and 3 ) show ±1 standard error from the mean calculated and displayed using the Python package Seaborn 56 .
- Full pipeline: stage not stated [Cartopy, seaborn, xarray]

### Tissue CD14&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; T cells reprogrammed by myeloid cells and modulated by LPS. (Nature 2023)

- DOI: 10.1038/s41586-022-05645-6 | PMCID: PMC7619353 | PMID: 36697826
- Evidence: Relevant visualisations were created using Python 3.6 and seaborn, the statistical visualisation package.
- Full pipeline: quality control [STAR, Seurat] -> alignment/mapping [STAR] -> quantification [HTSeq v0.10.0, ImageJ, STAR] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [seaborn] -> simulation/modelling [scDblFinder] -> visualisation [seaborn] -> stage not stated [Python v3.6]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: Software packages In addition to analysis-specific packages cited in the relevant sections above, the following packages were used for analysis: NumPy 83 , Python 84 , Seaborn 85 , Matplotlib 86 and Python 3 (ref.
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Version used: **0.9.0**
- Evidence: Data visualization was performed using Matplotlib (v.3.2.1) and Seaborn (v.0.9.0). scRNA-seq data were analysed using Cell Ranger (v.3.1.0), R (v.4.1.0) and Seurat (v.3.1.5).
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Multiple pathways for SARS-CoV-2 resistance to nirmatrelvir. (Nature 2023)

- DOI: 10.1038/s41586-022-05514-2 | PMCID: PMC9849135 | PMID: 36351451
- Evidence: 2c using ‘seaborn.clustermap’ under default settings, which utilizes the UPGMA algorithm through SciPy 51 , 52 .
- Full pipeline: dimensionality reduction/clustering [SciPy, seaborn] -> stage not stated [CellProfiler v4.0.7, Nextflow, Pangolin v4.0.6]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **0.13.2**
- Evidence: Scanpy v.1.9.1 with anndata v.0.10.7 and the statistics and plotting libraries pandas v.2.2.2, numpy v.1.26.4, scipy v.1.13.0, seaborn v.0.13.2 and matplotlib v.3.8.4 were used for data analysis and visualization.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Version used: **0.13.2**
- Evidence: This used custom-made code but made use of libraries such as numpy (1.22.0), scipy (1.10.1), matplotlib (3.7.3), sciKit learn (1.3.2), pandas (2.0.3) and seaborn (0.13.2).
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### Coral photosymbiosis on Mid-Devonian reefs. (Nature 2024)

- DOI: 10.1038/s41586-024-08101-9 | PMCID: PMC11655356 | PMID: 39443794
- Evidence: The data were imported using the Pandas library and plotted using the Seaborn or Matplotlib libraries.
- Full pipeline: visualisation [Matplotlib, seaborn] -> stage not stated [Jupyter]

### Future increase in extreme El Niño supported by past glacial changes. (Nature 2024)

- DOI: 10.1038/s41586-024-07984-y | PMCID: PMC11464383 | PMID: 39322673
- Evidence: Code availability Open-sourced Python code was used to create the figures, perform the analyses and all calculations, including the following modules and their required dependencies: matplotlib 78 , pandas 79 , NumPy 80 , seaborn 81 , xarray 82 , cartopy 83 and SciPy 84 .
- Full pipeline: simulation/modelling [CESM v1.2] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn, xarray]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **0.13.1**
- Evidence: ...v.2.0.1), NumPy (v.1.24.2) 73 , SciPy (v.1.10.1) 74 , scikit-learn (v.1.2.0), SCANPY (v1.9.3) 75 , AnnData (v.0.9.1) 75 , matplotlib (v.3.7.1) 76 and seaborn (v.0.13.1) 77 packages.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Evidence: The fitted data were plotted using the Python seaborn library (v0.11.2) 78 to visualize the k -mer-based accumulation curve.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Other plots were made using the ggplot2 library in R and seaborn library in Python.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### In situ targeted base editing of bacteria in the mouse gut. (Nature 2024)

- DOI: 10.1038/s41586-024-07681-w | PMCID: PMC11338833 | PMID: 38987595
- Evidence: 2 , 3 , 8 and 9 were generated using the libraries Matplotlib and Seaborn.
- Full pipeline: alignment/mapping [MAFFT, Python] -> dimensionality reduction/clustering [QIIME 2] -> stage not stated [Cutadapt v3.3, Matplotlib, fastp, seaborn]

### A multimodal generative AI copilot for human pathology. (Nature 2024)

- DOI: 10.1038/s41586-024-07618-3 | PMCID: PMC11464372 | PMID: 38866050
- Version used: **0.12.2**
- Evidence: Matplotlib (v.3.7.1) and Seaborn (v.0.12.2) were used to create plots and figures.
- Full pipeline: machine learning [PyTorch v2.0.1] -> stage not stated [Matplotlib v3.7.1, QuPath, seaborn v0.12.2]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Recorded F 350 / F 330 was analysed by using Python libraries including pandas, numpy, scipy and seaborn in Visual Studio Code (Microsoft).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Accurate structure prediction of biomolecular interactions with AlphaFold 3. (Nature 2024)

- DOI: 10.1038/s41586-024-07487-w | PMCID: PMC11168924 | PMID: 38718835
- Version used: **0.12.2**
- Evidence: Model performance analysis and visualization Data analysis used Python v.3.11.7 ( https://www.python.org/ ), NumPy v.1.26.3 ( https://github.com/numpy/numpy ), SciPy v.1.9.3 ( https://www.scipy.org/ ), seaborn v.0.12.2 ( https://github.com/mwaskom/seaborn ), Matplotlib v.3.6.1 ( https://github.com/matplotlib/matplotlib ), pandas v.2.0.3 ( https://github.com/pandas-dev/pandas ), statsmodels v.0.12....
- Full pipeline: visualisation [NumPy v1.26.3, SciPy v1.9.3, seaborn v0.12.2] -> stage not stated [AlphaFold, Matplotlib v3.6.1, RDKit, RoseTTAFold, statsmodels v0.12.2]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Figures were created using ggplot, ggnewscale, ggpattern, ggrepel, ggsflabel, ggspatial, ggpubr, cowplot, matplotlib, plotly ( https://plot.ly ), seaborn and TMB_plotter 98 – 108 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Single-cell analysis reveals context-dependent, cell-level selection of mtDNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07332-0 | PMCID: PMC11078733 | PMID: 38658765
- Version used: **0.11.1**
- Evidence: The analyses were performed using Python v3.7.12, with the following modules: matplotlib v3.4.2, numpy v1.21.0, pandas v1.1.5, plotly v5.16.1, pysam v0.16.0.1, scikit-learn v0.23.1, scipy v1.7.0 and seaborn v0.11.1.
- Full pipeline: quality control [MultiQC v1.11] -> stage not stated [Matplotlib v3.4.2, NumPy v1.21.0, R, SciPy v1.7.0, scikit-learn v0.23.1, seaborn v0.11.1]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **0.10.1**
- Evidence: Python (v.3.8.3): matplotlib (v.3.5.2) 136 and seaborn (v.0.10.1) 137 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Affinity-optimizing enhancer variants disrupt development. (Nature 2024)

- DOI: 10.1038/s41586-023-06922-8 | PMCID: PMC10830414 | PMID: 38233525
- Evidence: MPRA data were analysed using standard Python libraries (pandas, numpy, scipy, seaborn, matplotlib).
- Full pipeline: differential/statistical testing [R] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn]

### A parabrachial hub for need-state control of enduring pain. (Nature 2025)

- DOI: 10.1038/s41586-025-09602-x | PMCID: PMC12630001 | PMID: 41062698
- Evidence: A box plot was generated using Seaborn to visualize differences in Fos expression between Npy1r expressing and non-expressing cells within each Leiden cluster.
- Full pipeline: quantification [NumPy, Scanpy] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP, seaborn] -> visualisation [UMAP, seaborn] -> stage not stated [AnnData, ImageJ]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: One protein could not be completed due to limitations of AlphaFold 2 (CHD7). iPTM scores were extracted from individual json files and used to create a heat map with rows clustered using Seaborn and matplotlib (Extended Data Fig.
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Version used: **0.13.2**
- Evidence: Visualizations were performed using Seaborn (v0.13.2) in Python.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: The plots were visualized using Matplotlib and Seaborn.
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **0.11.0**
- Evidence: The packages matplotlib v3.4.2 and seaborn 0.11.0 were used for visualization.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Divergent evolutionary strategies pre-empt tissue collision in gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09447-4 | PMCID: PMC12527943 | PMID: 40903584
- Evidence: Plots were generated in GraphPad Prism or with Python scripts using Matplotlib and Seaborn graphic libraries.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [ImageJ, Matplotlib, NumPy, Python, SciPy, seaborn]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **0.9.0**
- Evidence: ...thon, R and Matlab packages: Python: pandas (v.1.1.5), numpy (v.1.19.3), anndata (v.0.7.4), scanpy (v.1.6.0), matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R packages: ggplot2 (v.3.4.4), gplots (v.3.1.3), readr (v.2.1.4), dplyr (v.1.1.2), reshape2 (v.1.4.4), patchwork (v.1.1.3), RColorBrewer (v.1.1.3), ggrepel (v.0.9.4), aplot (v.0.1.10), ggdendro (v.0.1.23), M...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Plot submodule spatiomic includes plotting functions based on matplotlib 82 and seaborn 83 that facilitate visualizing common plots, for example, image registration metrics, SOM training-quality metrics, cluster projections, spatial adjacency graphs as well as cluster contributor histograms and volcano plots.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Evidence: Correlation plots were calculated using the SciPy package 77 in Python v.3.10 and plotted with Seaborn (Extended Data Fig.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **0.11.2**
- Evidence: Python packages such as Scanpy (v.1.9.5), Pandas (v.2.0.0), Statsmodels (v.0.14.0), NumPy (v.1.24.2), Scipy (v.1.10.1), Matplotlib (v.3.8.0), Seaborn (v.0.11.2) and Sklearn (v.1.3.2), were used for data analysis.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Version used: **0.13.2**
- Evidence: Analysis and plotting were conducted with custom scripts in MATLAB 2022b, and Scipy 1.13.0 and Seaborn 0.13.2 in Python 3.
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Light-microscopy-based connectomic reconstruction of mammalian brain tissue. (Nature 2025)

- DOI: 10.1038/s41586-025-08985-1 | PMCID: PMC12158774 | PMID: 40335689
- Evidence: 2g was generated with seaborn.violin.plot ( https://seaborn.pydata.org/generated/seaborn.violinplot.html ).
- Full pipeline: machine learning [PyTorch v1.12.1] -> stage not stated [BigStitcher, Jupyter, NumPy, Python v3.8, SciPy, scikit-image, seaborn]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Version used: **0.12.2**
- Evidence: ...verse (2.0.0), glmmTMB (1.1.10), performance (0.12.2) and emmeans (1.10.3) were used for model training and statistical analysis; Matplotlib (3.7.0), seaborn (0.12.2), HoloViews (1.15.4), Ipyvolume (0.5.2) and Neuroglancer ( https://github.com/seung-lab/neuroglancer ) were used for graphical visualization; and Jupyter (ipykernel:6.21.2), Docker (23.0.1) and Kubernetes (1.22.11) were used for code ...
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Connectomics of predicted Sst transcriptomic types in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08805-6 | PMCID: PMC11981948 | PMID: 40205210
- Evidence: We used the following libraries for visualization and analysis: Matplotlib 73 , Seaborn 74 , Numpy 75 , Pandas 76 , VTK 77 , Scipy 78 , Scikit-posthocs 79 , Scikit-learn 80 , scrattch-hicat ( https://github.com/AllenInstitute/scrattch.hicat/ ) and statsmodels 81 .
- Full pipeline: differential/statistical testing [limma] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn, seaborn, statsmodels]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **0.12.2**
- Evidence: SL-Smart-seq3xpress data analysis Count matrices were processed with JupyterLab (v.4) notebooks using IPython (v.7.31) using the following modules: pandas (v.1.5.3), numpy (v.1.23.5), scipy (v.1.10.1), scanpy (v.1.7.2), openpyxl (v.3.1.2), matplotlib (v.3.6.3) and seaborn (v.0.12.2).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **0.12.2**
- Evidence: Python packages used: beautifulsoup4 v.4.12.2, bio v.1.6.2, GSEApy v.1.1.0, matplotlib v.3.7.1, NumPy v.1.24.3, pandas v.2.0.2, SciPy v.1.10.1, seaborn v.0.12.2, sklearn v.0.0.post5, urllib3 v.2.0.3.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### A travelling-wave strategy for plant-fungal trade. (Nature 2025)

- DOI: 10.1038/s41586-025-08614-x | PMCID: PMC11882455 | PMID: 40011773
- Evidence: All linear fits computed using regplot function of seaborn Python package 65 .
- Full pipeline: machine learning [StarDist] -> visualisation [Matplotlib] -> stage not stated [SciPy, scikit-image, seaborn]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: The density in the scattered point cloud was visualized using colour-mapped scipy.stats.gaussian_kde values, with density lines overlaid using seaborn.kdeplot for enhanced clarity and interpretation.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Regional and institutional trends in assessment for academic promotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08422-9 | PMCID: PMC11821531 | PMID: 39843736
- Evidence: Data visualization Data from Stata were imported into Python 3 and plotted using Python’s Matplotlib, seaborn and geopandas libraries.
- Full pipeline: visualisation [Matplotlib, Python, seaborn]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: The analysis was performed using Python, with key libraries including Pandas for data manipulation, Seaborn and Matplotlib for visualization, NetworkX for network analysis, and SciPy for statistical tests.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### Hierarchical design of pseudosymmetric protein nanocages. (Nature 2025)

- DOI: 10.1038/s41586-024-08360-6 | PMCID: PMC11821544 | PMID: 39695230
- Version used: **0.11.1**
- Evidence: Scripts and plots All data were processed and plotted using Python 3.8.8, matplotlib 3.3.4 and seaborn 0.11.1.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [RELION, UCSF Chimera] -> visualisation [Matplotlib v3.3.4, Python v3.8.8, seaborn v0.11.1] -> stage not stated [ChimeraX, ImageJ]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: Linear regression of cell-type proportion on sample age with 95% confidence interval was computed using seaborn.regplot.
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Synthetic GPCRs for programmable sensing and control of cell behaviour. (Nature 2025)

- DOI: 10.1038/s41586-024-08282-3 | PMCID: PMC11666456 | PMID: 39633047
- Evidence: Statistical analysis Graphs and statistical analyses were generated using Python (with Pandas, Seaborn, Scipy and Statsmodels packages).
- Full pipeline: quantification [Matplotlib] -> differential/statistical testing [SciPy, seaborn] -> stage not stated [AlphaFold, ImageJ, MACS2, PHENIX, Python]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **0.11.2**
- Evidence: The distributions for each cell type and tumour type are visualized using the sns.kdeplot function in Python Seaborn (v.0.11.2) ( Extended Data Fig.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Autoinhibition of dimeric NINJ1 prevents plasma membrane rupture. (Nature 2025)

- DOI: 10.1038/s41586-024-08273-4 | PMCID: PMC11711097 | PMID: 39476863
- Evidence: The r.m.s.d. and distances were analysed using simulation event analysis and figures were generated with PyMOL (Schrödinger) and Seaborn Python package 36 .
- Full pipeline: simulation/modelling [seaborn] -> structure determination [AlphaFold, ChimeraX] -> visualisation [PyMOL v2.5.2, seaborn] -> stage not stated [PHENIX]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Version used: **0.12.2**
- Evidence: All behavioural and neural analyses were performed using custom-written Python (v.3.8) code unless otherwise noted, incorporating the analysis and plotting libraries numpy (v.1.24.3), scipy (v.1.10.1), scikit-learn (v.1.3.0), pandas (v.2.0.3), seaborn (v.0.12.2), elephant (v.1.0.0) and statsmodels (v.0.14.0).
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: Clustered heat maps were generated using Seaborn’s clustermap and heat map functions, with selected gene pairs highlighted to visualize conserved and differential co-regulation.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **0.13.2**
- Evidence: Visualization methods We used matplotlib v.3.10.0, seaborn v.0.13.2, bokeh v.3.7.3 and Figma to plot most of the figures.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: Spearman correlation was performed between pseudobulk EPR and pseudobulk total normalized RNA counts and visualized using a seaborn.heatmap() (Fig.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: ...ns ggplot2_3.5.1, tidyr_1.3.1, dplyr_1.1.4, ggpubr_0.6.0, Hmisc_5.2.1), Python (version 3.12.9) using the pandas, scipy, scikit-learn, matplotlib and seaborn packages (versions pandas_2.2.3, scipy_1.14.1, scikit-learn_1.5.2, matplotlib_3.9.2, seaborn_0.13.2) or Microsoft Excel for Mac (Office 365, version 16.9).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Palaeometabolomes yield biological and ecological profiles at early human sites. (Nature 2026)

- DOI: 10.1038/s41586-025-09843-w | PMCID: PMC12851940 | PMID: 41407854
- Evidence: Visualizations such as PCA scatter plots and hierarchical clustering heat maps were created using the Seaborn package 99 .
- Full pipeline: dimensionality reduction/clustering [seaborn] -> differential/statistical testing [SciPy, scikit-learn] -> visualisation [seaborn]

### Dated gene duplications elucidate the evolutionary assembly of eukaryotes. (Nature 2026)

- DOI: 10.1038/s41586-025-09808-z | PMCID: PMC12872463 | PMID: 41339551
- Evidence: Tree visualizations were produced in TreeViewer 72 and all other plots using Python Seaborn or Matplotlib, all programs and their versions are listed in Supplementary Table 1 .
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508] -> dimensionality reduction/clustering [HMMER v3.3.2, MAFFT v7.508] -> visualisation [Matplotlib, seaborn]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **0.12.2**
- Evidence: Imaging data, all data related to the drug screen, proteomics, CRISPR screen, as well as in vitro kinase binding/inhibitory assay were plotted with seaborn (v.0.12.2) and matplotlib (v.3.4.2) in Python (v.3.7.6).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Evidence: Violin plots were generated using the seaborn Python library.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Inhibitory PD-1 axis maintains high-avidity stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09440-x | PMCID: PMC12727512 | PMID: 41299179
- Evidence: Quantification of marker expression for each subset was visualized with violin plots using the Python-based seaborn visualization library.
- Full pipeline: quantification [seaborn] -> normalisation [Matplotlib, scikit-learn] -> dimensionality reduction/clustering [Matplotlib, scikit-learn] -> visualisation [Matplotlib, scikit-image, scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2, napari]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **0.13**
- Evidence: Commonly used Python libraries (Python v3.11.13, matplotlib v3.10, Seaborn v0.13, numpy v2.2.6, pandas v2.3.1, scipy v1.16.0, anndata v0.11.4 and shapely v2.1.1) were applied to visualize spatial distribution of cells.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: All analyses were conducted using skimage for image processing 71 , 72 , numpy and pandas for data handling, matplotlib and seaborn for visualization, and scipy and scikit-learn for statistical and machine learning operations.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### A conserved epitope III on hepatitis C virus E2 protein has alternate conformations facilitating cell binding or virus neutralization. (PNAS 2021)

- DOI: 10.1073/pnas.2104242118 | PMCID: PMC8285954 | PMID: 34260404
- Evidence: Finally, the rmsd’s were used to compute a hierarchical clustering heatmap with the Seaborn Python library ( 50 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [seaborn] -> stage not stated [CCP4, PyMOL]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: All plots were generated using Matplotlib ( 58 ), Seaborn ( https://seaborn.pydata.org ) adjustText ( https://github.com/Phlya/adjustText ), mpl-scatter-density ( https://github.com/astrofrog/mpl-scatter-density ), Astropy ( 59 , 60 ), and Scanpy ( 50 ) libraries under Python 3.7.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### The molecular basis for pore pattern morphogenesis in diatom silica. (PNAS 2022)

- DOI: 10.1073/pnas.2211549119 | PMCID: PMC9894196 | PMID: 36459651
- Version used: **0.11**
- Evidence: Differences that were not statistically significant are denoted “ns.” Unless otherwise noted, all figures were generated in Matplotlib 3.5 and Seaborn 0.11.
- Full pipeline: dimensionality reduction/clustering [scikit-learn v0.21.3] -> differential/statistical testing [Matplotlib v3.5, seaborn v0.11] -> visualisation [Matplotlib v3.5, seaborn v0.11] -> stage not stated [BLAST, NumPy, SciPy, scikit-image]

### Adult neurogenesis acts as a neural regularizer. (PNAS 2022)

- DOI: 10.1073/pnas.2206704119 | PMCID: PMC9659416 | PMID: 36322739
- Evidence: Models were built and analyzed in Python 3.6 ( 65 ) with custom scripts that are freely available on GitHub, and were developed using the following packages: PyTorch ( 66 ), Ax ( https://github.com/facebook/Ax ), NumPy ( 67 ), SciPy ( 68 ), Pandas ( 69 ), Matplotlib ( 70 ), Seaborn ( 71 ), and Scikit-learn 0.21.1 ( 72 ).
- Full pipeline: stage not stated [Matplotlib, NumPy, PyTorch, Python v3.6, SciPy, scikit-learn v0.21.1, seaborn]

### Computationally exploring the mechanism of bacteriophage T7 gp4 helicase translocating along ssDNA. (PNAS 2022)

- DOI: 10.1073/pnas.2202239119 | PMCID: PMC9371691 | PMID: 35914145
- Evidence: We generated a hierarchically clustered heat map using the clustermap module with default parameters in Seaborn package and picked out the center one of the largest cluster (upper-left corner) as the representative structure.
- Full pipeline: dimensionality reduction/clustering [seaborn] -> simulation/modelling [LAMMPS, NAMD, OpenMM] -> stage not stated [PyMOL, VMD]

### Ciliogenesis requires sphingolipid-dependent membrane and axoneme interaction. (PNAS 2022)

- DOI: 10.1073/pnas.2201096119 | PMCID: PMC9351462 | PMID: 35895683
- Evidence: Hierarchical clustering and visualization were done using clustermap function from the Python package seaborn ( https://seaborn.pydata.org/ ).
- Full pipeline: quality control [Bowtie2] -> alignment/mapping [Bowtie2, IMOD] -> dimensionality reduction/clustering [seaborn] -> differential/statistical testing [Bioconductor, Python, edgeR] -> visualisation [seaborn] -> stage not stated [ImageJ, MotionCor2]

### In situ architecture of the lipid transport protein VPS13C at ER-lysosome membrane contacts. (PNAS 2022)

- DOI: 10.1073/pnas.2203769119 | PMCID: PMC9303930 | PMID: 35858323
- Version used: **0.11.2**
- Evidence: A violin plot was generated with the Python data visualization library Seaborn (version 0.11.2, https://seaborn.pydata.org/index.html , RRID:SCR_018132) ( 55 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0] -> structure determination [AlphaFold, ChimeraX, IMOD] -> visualisation [RELION, UCSF Chimera v1.13, seaborn v0.11.2] -> stage not stated [CTFFIND v1.18, EMAN2 v2.91]

### A male pheromone that improves the quality of the oogenic germline. (PNAS 2022)

- DOI: 10.1073/pnas.2015576119 | PMCID: PMC9173808 | PMID: 35576466
- Evidence: We generated the heatmap using Python ( 80 ) version 3.7.10, Matplotlib ( 81 ) version 3.3.4, and seaborn ( 82 ) version 0.11.2.
- Full pipeline: quality control [MultiQC, Nextflow] -> differential/statistical testing [DESeq2 v1.32.0, NumPy, R v4.1, SciPy] -> stage not stated [Matplotlib, seaborn]

### Phenotype-Based Threat Assessment. (PNAS 2022)

- DOI: 10.1073/pnas.2112886119 | PMCID: PMC9168455 | PMID: 35363569
- Evidence: All ML models were developed with Python 3.7 using the Pandas and Scikit-learn libraries, with all plots visualized using seaborn.
- Full pipeline: visualisation [Python v3.7, scikit-learn, seaborn]

### Generation of de novo miRNAs from template switching during DNA replication. (PNAS 2023)

- DOI: 10.1073/pnas.2310752120 | PMCID: PMC10710096 | PMID: 38019864
- Version used: **0.11.2**
- Evidence: The heatmaps were generated using Python packages matplotlib v.3.5.1 and seaborn v.0.11.2.
- Full pipeline: stage not stated [BEDTools v2.26.0, Matplotlib v3.5.1, Python, R, ggplot2, seaborn v0.11.2]

### Machine-guided discovery of a real-world rogue wave model. (PNAS 2023)

- DOI: 10.1073/pnas.2306275120 | PMCID: PMC10691345 | PMID: 37983488
- Evidence: This publication was made possible by the following opensource software stack: JAX ( 57 ), flax ( 58 ), optax ( 59 ), PySR ( 9 ), scikit-learn ( 63 ), PyALE ( 64 ), NumPy ( 65 ), SciPy ( 66 ), matplotlib ( 67 ), Seaborn ( 68 ), pandas ( 69 ), and Jupyter ( 70 ).
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, SciPy, scikit-learn, seaborn]

### Curiosity evolves as information unfolds. (PNAS 2023)

- DOI: 10.1073/pnas.2301974120 | PMCID: PMC10614840 | PMID: 37844235
- Evidence: Figures were produced in Python with Seaborn and Matplotlib.
- Full pipeline: differential/statistical testing [lme4] -> visualisation [Matplotlib, Python, seaborn] -> stage not stated [R v4.0]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **0.11.2**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Version used: **0.11.0**
- Evidence: Plots were generated using matplotlib v3.3.2, seaborn v0.11.0, and ggplot2 v3.3.6.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Evidence: Fetal data were plotted as a line plot by time while adult data (due to the lack of a temporal variable) was plotted as box and whisker plots using a combination of tools from the Python packages matplotlib , seaborn , and plotnine .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### <i>Leishmania</i> allelic selection during experimental sand fly infection correlates with mutational signatures of oxidative DNA damage. (PNAS 2023)

- DOI: 10.1073/pnas.2220828120 | PMCID: PMC10013807 | PMID: 36848551
- Version used: **0.11.2**
- Evidence: Further SNP analyses were performed based on the filtered outputs of GIP using custom Python 3.10 code relying on the following libraries: Pandas (1.4.2) ( 24 ), Pysam (0.19.0) ( 25 ), Numpy (1.22.3) ( 26 ), Matplotlib (3.5.1) ( 27 ), Seaborn (0.11.2) ( 28 ), Biotite (0.32.0) ( 29 ), and Upsetplot (0.6.0) ( 30 ).
- Full pipeline: stage not stated [Matplotlib v3.5.1, NumPy v1.22.3, Python v3.10, seaborn v0.11.2]

### A critical analysis of plant science literature reveals ongoing inequities. (PNAS 2023)

- DOI: 10.1073/pnas.2217564120 | PMCID: PMC10013813 | PMID: 36853942
- Version used: **0.11.1**
- Evidence: We computed national summary stats, global patterns of author location, and associations with national development indicators using Python (v3.8.8) packages Pandas (v1.5.0) and Numpy (v1.22.4) and visualized data in Seaborn (v0.11.1) and Matplotlib (v3.6.1).
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.22.4, seaborn v0.11.1]

### Losartan controls immune checkpoint blocker-induced edema and improves survival in glioblastoma mouse models. (PNAS 2023)

- DOI: 10.1073/pnas.2219199120 | PMCID: PMC9963691 | PMID: 36724255
- Version used: **0.9.0**
- Evidence: The heatmap of immune cell populations or their ratios (z-score transformed) for each survival classification was generated using the Seaborn 0.9.0 package in the Python language environment.
- Full pipeline: quantification [RSEM v1.2.19] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [survival (R)] -> visualisation [UMAP] -> stage not stated [ImageJ, R, Seurat v4.0.0, seaborn v0.9.0]

### Diversification of pectoral control through motor pool extension. (PNAS 2024)

- DOI: 10.1073/pnas.2413415121 | PMCID: PMC11626184 | PMID: 39602261
- Evidence: 3.8, Python Software Foundation, www.python.org ), building on the NumPy [v.1.18.5, ( 42 )], matplotlib [v.3.2.2, ( 43 )], pandas [v.2.2.1, ( 44 )] and seaborn [0.12.2, ( 45 )] libraries were used.
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [SciPy] -> stage not stated [Matplotlib, NumPy, Python, seaborn]

### AlphaFold-Multimer accurately captures interactions and dynamics of intrinsically disordered protein regions. (PNAS 2024)

- DOI: 10.1073/pnas.2406407121 | PMCID: PMC11536093 | PMID: 39446390
- Evidence: We extensively used BioPython, NumPy, SciPy, pandas, Matplotlib, and seaborn ( 57 – 62 ) to develop the code and plot the figures for this work.
- Full pipeline: machine learning [AlphaFold] -> visualisation [PyMOL] -> stage not stated [ColabFold, Matplotlib, NumPy, RoseTTAFold, SciPy, seaborn]

### Structural insights into KSHV-GPCR constitutive activation and CXCL1 chemokine recognition. (PNAS 2024)

- DOI: 10.1073/pnas.2403217121 | PMCID: PMC11494311 | PMID: 39378089
- Evidence: The analysis of the resulting trajectories was performed using MDAnalysis ( 35 ), visualization and image rendering were performed with PyMOL, and graphical representations were obtained with the Seaborn Package ( 36 ).
- Full pipeline: simulation/modelling [MDAnalysis, R v6.62, seaborn] -> structure determination [PHENIX] -> visualisation [MDAnalysis, PyMOL, seaborn]

### Multisubstrate specificity shaped the complex evolution of the aminotransferase family across the tree of life. (PNAS 2024)

- DOI: 10.1073/pnas.2405524121 | PMCID: PMC11214133 | PMID: 38885378
- Evidence: A heatmap was generated with columns being clustered (distance metric: “euclidean”, linkage method: “ward”) by the seaborn package v0.11.2 ( 122 ) in a Python environment, whereas rows were arranged phylogenetically by referring to the previous studies ( 39 – 41 , 43 – 45 ) to be able to trace the evolutionary history of individual ATs.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [seaborn] -> simulation/modelling [AutoDock Vina v4.2.6] -> stage not stated [AlphaFold v2.1.0, HMMER v3.3.1, RAxML v1.2.0]

### Subcallosal cingulate deep brain stimulation evokes two distinct cortical responses via differential white matter activation. (PNAS 2024)

- DOI: 10.1073/pnas.2314918121 | PMCID: PMC10998591 | PMID: 38527192
- Version used: **0.12.2**
- Evidence: The source analysis was performed in python 3.11.5 using the following packages: mne 1.5.1, numpy 1.24.4, matplotlib 3.8.0, scipy 1.11.2, pandas 2.1.1, and seaborn 0.12.2 ( 57 – 62 ).
- Full pipeline: stage not stated [AFNI, Camino, FSL, Matplotlib v3.8.0, NumPy v1.24.4, SciPy v1.11.2, seaborn v0.12.2]

### Network of epistatic interactions in an enzyme active site revealed by large-scale deep mutational scanning. (PNAS 2024)

- DOI: 10.1073/pnas.2313513121 | PMCID: PMC10962969 | PMID: 38483989
- Evidence: Heatmaps were created using the Seaborn package as part of Matplotlib, executed in Python.
- Full pipeline: stage not stated [Matplotlib, Python v3.0, seaborn]

### Generative epigenetic landscapes map the topology and topography of cell fates. (PNAS 2025)

- DOI: 10.1073/pnas.2514508122 | PMCID: PMC12718394 | PMID: 41364758
- Evidence: Landscape topography statistics were analyzed using kernel density estimation in Seaborn.
- Full pipeline: differential/statistical testing [seaborn]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Version used: **0.9.0**
- Evidence: The following Python packages were utilized: Matplotlib (version 3.0.3), NumPy (version 1.16.3), Pandas (version 0.24.2), SciPy (version 1.2.1), and Seaborn (version 0.9.0).
- Full pipeline: quantification [CellProfiler] -> visualisation [Conda, Jupyter, Python v3.7.3] -> stage not stated [ImageJ, Matplotlib v3.0.3, NumPy v1.16.3, SciPy v1.2.1, seaborn v0.9.0]

### High-throughput screening for class I peptide MHC binding via yeast surface display. (PNAS 2025)

- DOI: 10.1073/pnas.2514741122 | PMCID: PMC12663924 | PMID: 41264236
- Evidence: Analyses were all performed in Python 3.7, and figures were generated using matplotlib ( 51 ) and seaborn ( 52 ) packages.
- Full pipeline: visualisation [Matplotlib, Python v3.7, seaborn]

### A steady-state pool of calcium-dependent actin is maintained by Homer and controls epithelial mechanosensation. (PNAS 2025)

- DOI: 10.1073/pnas.2509784122 | PMCID: PMC12582288 | PMID: 41134626
- Evidence: The following python packages were used: numpy, pandas, statsmodels, and scipy for organizing, sorting, and processing (normalization, smoothing, peak/trough finding) to automatically determine analysis windows based on displacement and extract data for various parameters; statsmodels for OLS analysis; matplotlib and seaborn for presentation.
- Full pipeline: quantification [napari] -> normalisation [Matplotlib, NumPy, SciPy, seaborn, statsmodels] -> differential/statistical testing [R] -> stage not stated [ImageJ, scikit-image]

### Methanogenesis inhibition remodels microbial fermentation and stimulates acetogenesis in ruminants. (PNAS 2025)

- DOI: 10.1073/pnas.2514823122 | PMCID: PMC12541428 | PMID: 41052332
- Evidence: The plot area represents the normalized fold change (log 2 ) of transcripts per category, calculated using the kernel density estimate (KDE) method implemented in the Python package seaborn.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.13] -> alignment/mapping [Salmon v1.10.2] -> normalisation [seaborn] -> simulation/modelling [AlphaFold]

### De novo design of potent inhibitors of clostridial family toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2509329122 | PMCID: PMC12501149 | PMID: 40982695
- Evidence: The fitting was done using the Biacore 8 K Evaluation software (Cytiva) and then replotted in seaborn.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL, seaborn] -> stage not stated [AlphaFold, ChimeraX, Topaz]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Version used: **0.12.2**
- Evidence: Heatmaps of log-transformed gene counts were generated using seaborn (v 0.12.2) in Python to visualize variation across species.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### Surface delivery quantification reveals distinct trafficking efficiencies among clustered protocadherin isoforms. (PNAS 2025)

- DOI: 10.1073/pnas.2514178122 | PMCID: PMC12337331 | PMID: 40737325
- Version used: **0.13.0**
- Evidence: Histograms were calculated and displayed after applying a logicle transform ( 71 ) using FlowKit v.1.0.1 ( 72 ) and seaborn v.0.13.0 ( 73 ).
- Full pipeline: alignment/mapping [MUSCLE v5.1, Python, SciPy v1.11.4] -> stage not stated [AlphaFold, seaborn v0.13.0]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Version used: **0.13**
- Evidence: Graphs were produced using Matplotlib v3.8.2 ( 98 ) and Seaborn v0.13 ( 99 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Virion-associated influenza hemagglutinin clusters upon sialic acid binding visualized by cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426427122 | PMCID: PMC12037027 | PMID: 40244672
- Evidence: Seaborn and Matplotlib libraries were used to generate histograms ( 47 , 48 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [PHENIX] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Matplotlib, Python, RELION, seaborn]

### Bispecific antibodies against the hepatitis C virus E1E2 envelope glycoprotein. (PNAS 2025)

- DOI: 10.1073/pnas.2420402122 | PMCID: PMC12012487 | PMID: 40193609
- Evidence: Calibrated events were exported and processed by an in-house developed Python pipeline ( 86 ) using NumPy ( 87 ), pandas ( 88 ), Matplotlib ( 89 ), SciPy ( 90 ), and seaborn ( 91 ).
- Full pipeline: visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, Matplotlib, NumPy, SciPy, seaborn]

### Epstein-Barr virus and the immune microenvironment in multiple sclerosis: Insights from high-dimensional brain tissue imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2425670122 | PMCID: PMC11929469 | PMID: 40063794
- Evidence: These histograms were generated using the Seaborn package in Python, with the density plot overlaid using the seaborn.histplot function and the kde=True argument to provide a smooth density estimate of the distribution.
- Full pipeline: stage not stated [Python, seaborn]

### Recessive genetic contribution to congenital heart disease in 5,424 probands. (PNAS 2025)

- DOI: 10.1073/pnas.2419992122 | PMCID: PMC11912448 | PMID: 40030011
- Version used: **0.11.0**
- Evidence: Genes harboring at least two RGs and with available expression data were clustered by their ratio of max expression in different cell types using UPGMA hierarchical clustering algorithm through python package seaborn v0.11.0.
- Full pipeline: dimensionality reduction/clustering [seaborn v0.11.0]

### Spatial profiling of the interplay between cell type- and vision-dependent transcriptomic programs in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421022122 | PMCID: PMC11848306 | PMID: 39946537
- Evidence: We profiled the cell-density distributions of L2/3 cells in PC1 to PC2 space derived from type-identity genes using the python package seaborn.histplot .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [Enrichr, NumPy, SciPy, scikit-learn, seaborn]

### Meiosis-specific genes play roles in ploidy reduction in &lt;i&gt;Cryptococcus neoformans&lt;/i&gt; titan cells. (PNAS 2026)

- DOI: 10.1073/pnas.2522069123 | PMCID: PMC13215162 | PMID: 42189998
- Version used: **0.12.2**
- Evidence: Data visualization and further analysis were performed using matplotlib (v3.5.3) ( 70 ), seaborn (v0.12.2) ( 71 ), and numpy (v1.21.6) ( 72 ), with candidate chimeric reads and breakpoint loci summarized in output tables and plots.
- Full pipeline: alignment/mapping [SAMtools v1.18] -> visualisation [Matplotlib v3.5.3, NumPy v1.21.6, seaborn v0.12.2]

### SAGA1 and SAGA2 localize the starch sheath to the pyrenoid in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2533609123 | PMCID: PMC13167743 | PMID: 42090253
- Evidence: A Kruskal–Wallis ANOVA test followed by Dunn’s multiple comparisons test was used to test for significance in starch coverage between strains and grouped scatter plots were created for data visualization using Python (seaborn.swarmplot).
- Full pipeline: visualisation [seaborn]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **0.10.1**
- Evidence: Software The following Python (version 3.8.2) software packages were used in the data analysis and in the production of figures: Scipy (version 1.4.1) ( 78 ), pandas (version 1.0.3) ( 79 ), statsmodels (version 0.11.1) ( 80 ), matplotlib (version 3.2.1) ( 81 ), numpy (1.18.3) ( 82 ), seaborn_sinaplot ( 83 ), simanneal (version 0.5.0) ( 71 ), and seaborn (version 0.10.1) ( 84 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Evidence: Heatmaps were generated with seaborn.clustermap in python.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Version used: **0.12.1**
- Evidence: Proportions of specific populations (e.g., macrophages) enriched in specific gene modules (e.g., Pre-AGM module) were visualized using violin graphs produced using Matplotlib and Seaborn (v0.12.1) python libraries.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### The connectome of an insect brain. (Science 2023)

- DOI: 10.1126/science.add9330 | PMCID: PMC7614541 | PMID: 36893230
- Evidence: Plotting was performed using matplotlib ( 129 ), Seaborn ( 130 ), and Blender ( https://www.blender.org/ ).
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, SciPy, seaborn]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **0.12.2**
- Evidence: ChIP-seq signal box plots were generated with Python (v3.11.5) ( 120 ), using Pandas (v2.0.3), Matplotlib (v3.7.2), Seaborn (0.12.2), SciPy (1.11.1) and NumPy (v1.24.3) libraries, starting from deep-Tools computeMatrix output values, summing H2A.Z/H2A.Zac ChIP-seq signal across each peak coordinate, dividing it by the input signal and plotting the resulting ratios.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Version used: **0.13.2**
- Evidence: Filtered, sorted, and indexed bam output files were used for methylation visualization (see below) or further processed using modkit tools (ONT, https://github.com/nanoporetech/modkit ) and custom python scripts implementing Numpy v.1.26.3, Pandas v.2.2.0, and Seaborn v.0.13.2 for Pearson correlation and average methylation plots.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Metagenomic editing of commensal bacteria in vivo using CRISPR-associated transposases. (Science 2025)

- DOI: 10.1126/science.adx7604 | PMCID: PMC12969935 | PMID: 41231980
- Evidence: For visualizing normalized plots comparing integration across the genome, raw reads for each coordinate for a sample were normalized and scaled in the same way as above and plotted with Seaborn.
- Full pipeline: alignment/mapping [BLAST, Bowtie2, ggplot2] -> quantification [ggplot2] -> normalisation [ggplot2, seaborn] -> visualisation [ggplot2, seaborn] -> stage not stated [Python]

### Vaccination with mRNA-encoded nanoparticles drives early maturation of HIV bnAb precursors in humans. (Science 2025)

- DOI: 10.1126/science.adr8382 | PMCID: PMC13164876 | PMID: 40373112
- Evidence: S19 to S35 , S40 to S43 , S46 to S48 , and S52 ) were generated using Python with either Matplotlib ( 99 ) or a custom port of the Seaborn package that incorporates Wilson confidence intervals into the statistical analysis [ ( 100 ); https://github.com/tmsincomb/seaborn-fork ].
- Full pipeline: differential/statistical testing [Matplotlib, seaborn] -> structure determination [AlphaFold, ChimeraX, Coot v0.9.8, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [NumPy]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Software libraries used generally for analysis (of both mouse and human data) include Matplotlib ( 89 ), Pandas ( 90 ), Seaborn ( 91 ), and Scikit-learn ( 92 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Version used: **0.13.0**
- Evidence: Other plots were made using a combination of matplotlib (3.8.1) and seaborn (0.13.0) libraries in Python.
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries as described before ( 49 , 52 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

