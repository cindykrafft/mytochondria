# NumPy

- **Category:** general
- **Papers in survey:** 253
- **Journals:** Nature (127), PNAS (94), Cell (22), Science (9), Lancet (1)
- **Years:** 2021 (22), 2022 (38), 2023 (37), 2024 (53), 2025 (69), 2026 (34)
- **Versions named:** 1.24.3 (5), 1.19.2 (5), 1.19.5 (5), 1.20.3 (5), 1.21.5 (4), 1.21.6 (4), 1.24.2 (3), 1.23.4 (3), 1.19.4 (3), 1.24.4 (2)
- **Pipeline stages it appears in:** visualisation (29), differential/statistical testing (25), machine learning (9), dimensionality reduction/clustering (9), simulation/modelling (9), quantification (8), normalisation (5), alignment/mapping (4), quality control (3), read trimming (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: ...integrated normal biopsies or polyp-derived normal cells when possible. scRNA-seq, count matrix normalization and heatmap generation Using scanpy and numpy functions, raw count data were normalized by median library size, log-like transformed with Arcsinh, and Z-score standardized per gene ( Harris et al., 2020 ; Wolf et al., 2018 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **1.20.3**
- Evidence: ...rn version 0.10.1 Waskom, 2021 https://seaborn.pydata.org/ Python package scipy version 1.5.2 Virtanen et al., 2020 https://scipy.org/ Python package numpy version 1.20.3 Harris et al., 2020 https://numpy.org/ Python package matplotlib version 3.3.3 Hunter, 2007 https://matplotlib.org/ Other QExactive HF-x Orbitrap MS Thermo Fisher Scientific IQLAAEGAAPFALGMBFZ Waters XBridge Peptide BEH C18 (130A...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Identification of a therapeutic interfering particle-A single-dose SARS-CoV-2 antiviral intervention with a high barrier to resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.004 | PMCID: PMC8577993 | PMID: 34838159
- Version used: **1.19.4**
- Evidence: NumPy (v1.19.4) and SciPy (v1.5.4) were used with additional optimization for solving ODEs using Numba (v0.51.2).
- Full pipeline: quantification [DESeq2, featureCounts] -> simulation/modelling [Python] -> visualisation [Matplotlib v3.3.3, seaborn v0.11.0] -> stage not stated [ImageJ, NumPy v1.19.4, SciPy v1.5.4]

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: ...tworkx Hagberg et al., 2008 https://networkx.org/ pandas McKinney, 2010 https://pandas.pydata.org/ scipy Virtanen et al., 2020 https://www.scipy.org/ numpy van der Walt et al., 2011 https://numpy.org/ snakemake Köster and Rahmann, 2012 https://snakemake.readthedocs.io/en/stable/ tidyverse Wickham et al., 2017 https://www.tidyverse.org/ rgl CRAN https://cran.r-project.org/web/packages/rgl/index.htm...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### Microbial exposure during early human development primes fetal immune cells. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.039 | PMCID: PMC8240556 | PMID: 34077752
- Version used: **1.19.4**
- Evidence: ...n Software Foundation https://www.python.org/ Python 3.7.0 Python Software Foundation https://www.python.org/ matplotlib 3.2.1 PyPI https://pypi.org/ numpy 1.19.4 PyPI https://pypi.org/ pandas 0.25.3 PyPI https://pypi.org/ seaborn 0.9.0 PyPI https://pypi.org/ Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled b...
- Full pipeline: alignment/mapping [pandas] -> dimensionality reduction/clustering [QIIME 2 v1.8.0, R v4.4, UMAP] -> stage not stated [ImageJ, Matplotlib v3.2.1, NumPy v1.19.4, Python v2.7.0, seaborn v0.9.0]

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Evidence: ...info/ Trimmomatic 0.39 USADELLAB http://www.usadellab.org/cms/?page=trimmomatic MiXCR MI Lanoratory https://mixcr.readthedocs.io/en/master/index.html NumPy NumPy https://numpy.org/ Python 3.7.4 Python Software Foundation https://www.python.org/ Other BD FACS Aria III Cell Sorter BD Biosciences https://www.bdbiosciences.com BD FACS Canto II BD Biosciences https://www.bdbiosciences.com Leica DMI-mic...
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ..., 2007 Version 7.14.0 Jupyter Notebook Kluyver et al., 2016 Version 6.1.5 MDAnalysis Michaud-Agrawal et al., 2011 ; Gowers et al., 2016 Version 1.0.0 NumPy https://numpy.org Version 1.19.1 OpenMM Eastman et al., 2017 Version 7.4.2 OpenMMTools https://github.com/choderalab/openmmtools Version 0.20.0 PyMOL Schrödinger Version 2.3.2 ISOLDE Croll, 2018 Version 1.0.1 ChimeraX Pettersen et al., 2021 Ver...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **1.19.2**
- Evidence: Data was prepared and visualized using numpy (1.19.2), matplotlib (3.3.4), and pandas (1.2.4).
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Structure of a fully assembled tumor-specific T cell receptor ligated by pMHC. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.010 | PMCID: PMC9630439 | PMID: 35985289
- Version used: **1.19.5**
- Evidence: ... Illustrate Goodsell et al., 2019 github.com/ccsb-scripps/Illustrate MDAnalysis v0.20.1 Gowers et al., 2016 github.com/MDAnalysis/mdanalysis/releases NumPy v1.19.5 Harris et al., 2020 RRID: SCR_008633 OPM database Lomize et al., 2012 RRID:SCR_011961 Phenix Liebschner et al., 2019 RRID:SCR_014224 Prism v9.2.0 N/A https://www.graphpad.com/scientific-software/prism/ PyMOL The PyMOL Molecular Graphics...
- Full pipeline: simulation/modelling [ChimeraX, UCSF Chimera, VMD] -> stage not stated [CCP4, GROMACS v2020.6, MDAnalysis v0.20.1, NumPy v1.19.5, PHENIX, PyMOL]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.018 | PMCID: PMC8786601 | PMID: 35148837
- Version used: **1.19.1**
- Evidence: For the principal component analysis (PCA) we log-transformed, calculated z-scores, and ran PCA on MSD antibody concentration measurements or Wuhan-Hu-1/variant RBD IgG concentration ratios from a reference time point after COVID-19 vaccination or SARS-CoV-2 infection using Python v3.7.10 and packages numpy v1.19.1, pandas v1.2.5, and scikit-learn v1.0.
- Full pipeline: dimensionality reduction/clustering [NumPy v1.19.1, scikit-learn v1.0] -> visualisation [SciPy v1.6.2] -> stage not stated [Matplotlib v3.3.2, QuPath v0.2.3, R v4.0.5, ggplot2, seaborn v0.11.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: The methods were implemented in python and used the packages numpy, scipy and pandas.
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Python packages used for spatial enrichment analysis and collagen morphometrics were sckikit-image, pandas, numpy, xarray, scipy, statsmodels.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### A tridimensional atlas of the developing human head. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.013 | PMCID: PMC10783631 | PMID: 38070509
- Evidence: 91 https://www.meshlab.net/# Numpy (Version 1.22.3) Harris et al.
- Full pipeline: stage not stated [ImageJ v1.50e, NumPy]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: First, images were converted to NumPy arrays for segmentation.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **1.22.3**
- Evidence: ...cowplot v.1.1.1, scales v.1.1.1, grid v.3.6.3, broom v.0.7.6, e1071 v.1.7.6, and table1 v.1.4 Python packages N/A biopython v1.79, matplotlib v3.7.1, numpy v1.22.3, pandas v1.5.1, scikit-bio v0.5.8, scipy v1.9.3, seaborn v0.11.2, statannot v0.2.3, and statsmodels v0.13.2 Other Leica Reichert Ultracut-S microtome Leica N/A JEOL 1200EX Transmission electron microscope JEOL USA N/A AMT 2k CCD camera ...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Evidence: Data and Statistical analyses Data and statistical analyses were performed in Python 3.6 ( https://www.python.org/downloads/release/python-363/ ), using the packages scipy 139 , numpy 140 , matplotlib 141 , seaborn 142 , pandas 143 , scikit-learn 144 .
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: Quality control and cell filtering For all downstream analysis, we used the Scanpy package (referred to as sc from here on 54 , in Python 184 , 202 in addition to standard Python libraries such as numpy, pandas, matplotlib, csv, os, datetime 186 – 188 .
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### Inner speech in motor cortex and implications for speech neuroprostheses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.015 | PMCID: PMC12360486 | PMID: 40816265
- Version used: **1.26.2**
- Evidence: ...001622 BRAND Ali et al 2024 https://github.com/brandbci/brand Python 3.9 python.org/downloads/ RRID:SCR_008394 SciPy 1.11.4 scipy.org RRID:SCR_008058 NumPy 1.26.2 numpy.org RRID:SCR_008633 Pandas 2.1.3 pandas.pydata.org RRID:SCR_018214 scikit-learn 1.3.2 scikit-learn.org RRID:SCR_002577 matplotlib 3.8.2 matplotlib.org RRID:SCR_008624 seaborn 0.13.0 seaborn.pydata.org RRID:SCR_018132 AWS Polly aws-...
- Full pipeline: stage not stated [Matplotlib v3.8.2, NumPy v1.26.2, Python v3.9, SciPy v1.11.4, scikit-learn v1.3.2, seaborn v0.13.0]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: Software packages All data analyses were performed using custom code written in Python 3 using standard analysis and plotting libraries: numpy, scipy, scikit-learn, matplotlib and seaborn.
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### Nanoscale DNA tracing reveals the self-organization mechanism of mitotic chromosomes. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.028 | PMCID: PMC12127698 | PMID: 40132578
- Evidence: Mitotic chromosome simulations 1D loop extrusion simulations were performed using a numpy/numba based framework as described previously, 17 with loop extruder abundance and residence time set to physiological values for Condensins based on in vivo measurements in HeLa cells.
- Full pipeline: quantification [NumPy] -> normalisation [SciPy] -> simulation/modelling [NumPy, OpenMM] -> machine learning [scikit-learn] -> stage not stated [Python, napari, scikit-image]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **1.26**
- Evidence: 224 https://matplotlib.org/ numpy (v1.26) Harris et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### Symptom prevalence, duration, and risk of hospital admission in individuals infected with SARS-CoV-2 during periods of omicron and delta variant dominance: a prospective observational study from the ZOE COVID Study. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)00327-0 | PMCID: PMC8989396 | PMID: 35397851
- Evidence: Statistical analysis Statistical analysis was done using Python version 3.8.10 (pandas, NumPy, SciPy, statsmodel).
- Full pipeline: differential/statistical testing [NumPy, SciPy]

### Cortical responses to touch reflect subcortical integration of LTMR signals. (Nature 2021)

- DOI: 10.1038/s41586-021-04094-x | PMCID: PMC9289451 | PMID: 34789880
- Version used: **1.18.5**
- Evidence: Data Analysis and Statistics Data were analyzed in Matlab (versions 2017a and 2017b) and python (version 3.7.7) using the following packages (versions in parentheses): conda (4.8.5), matplotlib (3.3.1), numpy (1.18.5), pims (0.5), pyabf (2.2.6), scipy (1.5.2), scikit-image (0.16.2), scikit-learn (0.23.2), and seaborn (0.11.0).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Matplotlib v3.3.1, NumPy v1.18.5, SciPy v1.5.2, scikit-image v0.16.2, seaborn v0.11.0]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Version used: **1.18.1**
- Evidence: Software versions Software versions used were: Anndata 0.7.1 , bustools 0.39.4 , awk (GNU awk) 4.1.4 , grep (GNU grep) 3.1 , kallisto 0.46.1 , kb_python 0.24.4 , Matplotlib 3.0.3 , Numpy 1.18.1 , Pandas 0.25.3 , Scanpy 1.4.5.post3 , Scipy 1.4.1 , sed (GNU sed) 4.4 , sklearn 0.22.1 , statsmodels 0.12.1 , tar (GNU tar) 1.29 , umap 0.3.10.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Version used: **0.25.2**
- Evidence: The 10x Genomics V(D)J Ig heavy and light chains were processed using cellranger vdj v.3.1.0 and the reference cellranger-vdj-GRCh38-alts-ensembl-3.1.0 with default settings. scRNA-seq quality control and processing of 10x sequencing data Pandas (v.1.1.2), NumPy (v.0.25.2), Anndata (v.0.6.19), ScanPy (v.1.4) and Python (v.3) were used to pool single-cell counts and for downstream analyses.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Highly accurate protein structure prediction with AlphaFold. (Nature 2021)

- DOI: 10.1038/s41586-021-03819-2 | PMCID: PMC8371605 | PMID: 34265844
- Evidence: For neural network construction, running and other analyses, we used TensorFlow 70 , Sonnet 71 , NumPy 72 , Python 73 and Colab 74 .
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [OpenMM v7.3.1] -> machine learning [HMMER, NumPy, OpenMM v7.3.1, Python, TensorFlow]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: Data analysis and visualization for M. smithii tip dating were performed using the Python libraries pandas, NumPy and Matplotlib.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Design of biologically active binary protein 2D materials. (Nature 2021)

- DOI: 10.1038/s41586-020-03120-8 | PMCID: PMC7855610 | PMID: 33408408
- Evidence: All data was processed using python Dataframe and Numpy packages.
- Full pipeline: alignment/mapping [RELION] -> dimensionality reduction/clustering [RELION] -> stage not stated [CCP4, ImageJ v1.52d, NumPy]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Evidence: Analyses and visualization of data were conducted in a Python environment built on the Numpy, SciPy, matplotlib, scikit-learn package and pandas libraries.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Hydroclimatic vulnerability of peat carbon in the central Congo Basin. (Nature 2022)

- DOI: 10.1038/s41586-022-05389-3 | PMCID: PMC9729114 | PMID: 36323786
- Version used: **1.20.3**
- Evidence: ...ocube (0.1.0), geopandas (0.10.1), ipykernel (6.4.1), ipython (7.28.0), jupyter (1.0.0), KDE-diffusion (1.0.3), matplotlib (3.4.3), notebook (6.4.4), numpy (1.20.3), pandas (1.3.3), rioxarray (0.7.1), scipy (1.7.1) and shapely (1.7.1) packages.
- Full pipeline: alignment/mapping [Python v3.7.3] -> differential/statistical testing [R] -> stage not stated [Matplotlib v3.4.3, NumPy v1.20.3, SciPy v1.7.1]

### Personalizing exoskeleton assistance while walking in the real world. (Nature 2022)

- DOI: 10.1038/s41586-022-05191-1 | PMCID: PMC9556303 | PMID: 36224415
- Version used: **1.17.4**
- Evidence: The required python packages are numpy (1.17.4), scikit-learn (0.21.3), scipy (1.3.2) and matplotlib (2.0.2).
- Full pipeline: stage not stated [Matplotlib v2.0.2, NumPy v1.17.4, SciPy v1.3.2, scikit-learn v0.21.3]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: Statistical analyses Statistical analyses were carried out either in Python, mainly with the libraries Pandas 61 and NumPy 62 , or in R.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Retrograde movements determine effective stem cell numbers in the intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-04962-0 | PMCID: PMC7614894 | PMID: 35831497
- Version used: **1.19.5**
- Evidence: Finally, results were plot as the mean and 95% CI, using a polynomial fit (numpy.polyfit, numpy version 1.19.5) for each of the tracks.
- Full pipeline: read trimming [STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> differential/statistical testing [Bioconductor v3.14, R v4.1.1] -> stage not stated [ImageJ, NumPy v1.19.5, Python v3.10, TrackMate]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Evidence: Statistical analysis All analyses were performed in Python, using NumPy, Scipy, MatplotLib, Suite2p, Pandas and Scikit-learn.
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### MCM complexes are barriers that restrict cohesin-mediated loop extrusion. (Nature 2022)

- DOI: 10.1038/s41586-022-04730-0 | PMCID: PMC9159944 | PMID: 35585235
- Evidence: In Python notation, if M is the 90 × 90 TAD numpy array (where numpy is np) and L = 90 is the length of the matrix, then TAD_strength = box1/box2, where box1 = 0.5 * np.sum(M[0:L//3, L//3:2*L//3]) + 0.5 * np.sum(M[L//3:2*L// 3,2*L//3:L]); and box2 = np.sum(M[L//3:2*L//3,L//3:2*L//3]).
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R] -> stage not stated [Fiji, ImageJ, NumPy, Python, SciPy, ggplot2]

### A biophysical account of multiplication by a single neuron. (Nature 2022)

- DOI: 10.1038/s41586-022-04428-3 | PMCID: PMC8891015 | PMID: 35197635
- Version used: **1.15**
- Evidence: Data were corrected for the liquid junction potential and analysed using custom-written software in Python v.3.7 (Python Software Foundation) using NumPy v.1.15, Pandas v.0.25, SciPy v.1.3, Matplotlib v.3.0 and pyABF v.2.1 ( https://pypi.org/project/pyabf/ ).
- Full pipeline: stage not stated [ImageJ v2.0, Matplotlib v3.0, NumPy v1.15, Python v3.7, SciPy v1.3]

### Toroidal topology of population activity in grid cells. (Nature 2022)

- DOI: 10.1038/s41586-021-04268-7 | PMCID: PMC8810387 | PMID: 35022611
- Version used: **1.18.1**
- Evidence: Open-source Python packages used were: umap (version 0.3.10), ripser (0.4.1), numba (0.48.0), scipy (1.4.1), numpy (1.18.1), scikit-learn (0.22.1), matplotlib (3.1.3), h5py (2.10.0) and gudhi (3.4.1.post1).
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.1.3, NumPy v1.18.1, UMAP, scikit-learn v0.22.1] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, SciPy]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Version used: **1.16.4**
- Evidence: Predictor architecture The machine learning framework was built on Python (version 3.7.4) using the following libraries: scikit-learn (version 0.21.2), numpy (version 1.16.4), scipy (version 1.3), pandas (version 0.24.2) within a Singularity container (version 2.4.6-dist).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Autonomous chemical research with large language models. (Nature 2023)

- DOI: 10.1038/s41586-023-06792-0 | PMCID: PMC10733136 | PMID: 38123806
- Evidence: Once completed, Coscientist was provided with a file name containing a NumPy array with spectra for each well of the microplate.
- Full pipeline: stage not stated [Docker, NumPy, RDKit]

### The social and structural architecture of the yeast protein interactome. (Nature 2023)

- DOI: 10.1038/s41586-023-06739-5 | PMCID: PMC10700138 | PMID: 37968396
- Version used: **1.20.3**
- Evidence: Cumulative distribution functions were plotted using the matplotlib-library (3.4.2) and NumPy (1.20.3).
- Full pipeline: visualisation [ChimeraX v1.4, Cytoscape, Matplotlib, NumPy v1.20.3] -> stage not stated [AlphaFold, NetworkX v2.6.2, Python]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: These analyses relied heavily on Numpy 57 , Scipy 58 , Pandas 59 , and Scikit-learn 60 .
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Preserved neural dynamics across animals performing similar behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06714-0 | PMCID: PMC10665198 | PMID: 37938772
- Evidence: All the analyses were implemented in Python using open-source packages such as numpy, matplotlib, sci-kit, scipy and pandas 70 – 74 and custom code.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, Kilosort v2.0, Matplotlib, NumPy, Python, SciPy]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **1.20.3**
- Evidence: Data were analysed and figures generated using Python (version 3.9.1), along with packages numpy (version 1.20.3), scipy (version 1.7.1), matplotlib (version 3.4.3), and pandas (version 1.3.0), and R (version 3.6.0).
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **1.19.4**
- Evidence: ... RStudio 1.4.1106, Jupyter Notebook 6.0.3, Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-image 0.18.1, squidpy 1.1.2, anndata 0.8.0 and itertools 8.0.0.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### A foundation model for generalizable disease detection from retinal images. (Nature 2023)

- DOI: 10.1038/s41586-023-06555-x | PMCID: PMC10550819 | PMID: 37704728
- Version used: **1.19.5**
- Evidence: Results were further analysed and visualized with Python v.3.6, NumPy v.1.19.5, SciPy v.1.5.4, seaborn v.0.12.0, Matplotlib v.3.6.1, pandas v.1.5.0, Scikit-Learn v.1.1.3 and Pillow v.9.2.0.
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.19.5, SciPy v1.5.4, seaborn v0.12.0] -> stage not stated [Keras, PyTorch]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Version used: **1.19.5**
- Evidence: Raw acquisitions were imported into the AstroGlu pipeline as 3D (2D + t ) NumPy v.1.19.5 arrays.
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Version used: **1.21.5**
- Evidence: Python (v.3), Pandas (v.1.3.5), NumPy (v.1.21.5), Matplotlib (v.3.5.2) and Scanpy (v.1.8.2 and v.1.9.1) were used for quality control and downstream processing.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Accurate medium-range global weather forecasting with 3D neural networks. (Nature 2023)

- DOI: 10.1038/s41586-023-06185-3 | PMCID: PMC10356604 | PMID: 37407823
- Evidence: We used the code provided in a GitHub repository ( https://github.com/pvigier/perlin-numpy ) and modified the code for acceleration.
- Full pipeline: machine learning [PyTorch] -> visualisation [Matplotlib] -> stage not stated [NumPy, xarray]

### No thick carbon dioxide atmosphere on the rocky exoplanet TRAPPIST-1 c. (Nature 2023)

- DOI: 10.1038/s41586-023-06232-z | PMCID: PMC10447244 | PMID: 37337068
- Evidence: Code availability We used the following codes, resources and Python packages to reduce, analyse and interpret our JWST observations of TRAPPIST-1 c: numpy 81 , matplotlib 82 , astropy 83 , batman 36 , Eureka!
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, dynesty, emcee]

### Gap junctions desynchronize a neural circuit to stabilize insect flight. (Nature 2023)

- DOI: 10.1038/s41586-023-06099-0 | PMCID: PMC10232364 | PMID: 37225999
- Evidence: For additional functions, the Python libraries NumPy, pickle, SciPy, Matplotlib and seaborn were imported.
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, Python, SciPy, seaborn]

### Learnable latent embeddings for joint behavioural and neural analysis. (Nature 2023)

- DOI: 10.1038/s41586-023-06031-6 | PMCID: PMC10172131 | PMID: 37138088
- Evidence: CEBRA API and example usage The Python implementation of CEBRA is written in PyTorch 55 and NumPy 56 and provides an application programming interface (API) that is fully compatible with scikit-learn 57 , a package commonly used for machine learning.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [NumPy, PyTorch, scikit-learn]

### CTCF is a DNA-tension-dependent barrier to cohesin-mediated loop extrusion. (Nature 2023)

- DOI: 10.1038/s41586-023-05961-5 | PMCID: PMC10132984 | PMID: 37076620
- Version used: **1.21.6**
- Evidence: Statistical analysis and reproducibility Statistical analysis was performed using GraphPad Prism (v.9.4.1) or Python (v.3.7.7) using scipy (v.1.5.2) 61 , numpy (v.1.21.6), trackpy (v.0.4.2) 62 and statsmodels (v.0.12.2).
- Full pipeline: differential/statistical testing [NumPy v1.21.6, SciPy v1.5.2, statsmodels v0.12.2]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: The code in this step is implemented from scratch, specifically for CellOracle perturbations using NumPy, a python package for numerical computing ( https://numpy.org ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Visualization of translation and protein biogenesis at the ER membrane. (Nature 2023)

- DOI: 10.1038/s41586-022-05638-5 | PMCID: PMC9892003 | PMID: 36697828
- Version used: **1.20.3**
- Evidence: Polysome analysis For the neighbourhood analysis, ribosome positions and orientations were read from the RELION star files resulting from subtomogram alignment in a python script (Python 3.8.11, Numpy 1.20.3, Scipy 1.7.1).
- Full pipeline: alignment/mapping [IMOD v4.10.25, NumPy v1.20.3, Python v3.8.11, RELION v3.1.1, SciPy v1.7.1] -> structure determination [ChimeraX v1.3.0, UCSF Chimera v1.14.0] -> visualisation [ChimeraX v1.3.0] -> stage not stated [AlphaFold]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: Here, all dLight traces were linearly interpolated using the numpy.interp function to a duration of 0.83 s, or 25 samples.
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Version used: **1.17.2**
- Evidence: Numpy (v.1.17.2) and Pandas (v.0.25.1) were used for array and data frame operations, respectively.
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Integrated intracellular organization and its variations in human iPS cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05563-7 | PMCID: PMC9834050 | PMID: 36599983
- Evidence: All correlation values used throughout this paper were calculated using the function corrcoef from the Python package NumPy 37 .
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> stage not stated [NumPy]

### Identification of carbon dioxide in an exoplanet atmosphere. (Nature 2023)

- DOI: 10.1038/s41586-022-05269-w | PMCID: PMC9946830 | PMID: 36055338
- Evidence: ...readthedocs.io/en/stable/index.html ) and chromatic ( https://zkbt.github.io/chromatic/ ), each of which use the standard Python libraries scipy 98 , numpy 99 , astropy 100 , 101 and matplotlib 102 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **1.26.4**
- Evidence: Scanpy v.1.9.1 with anndata v.0.10.7 and the statistics and plotting libraries pandas v.2.2.2, numpy v.1.26.4, scipy v.1.13.0, seaborn v.0.13.2 and matplotlib v.3.8.4 were used for data analysis and visualization.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Central pattern generator control of a vertebrate ultradian sleep rhythm. (Nature 2024)

- DOI: 10.1038/s41586-024-08162-w | PMCID: PMC11655359 | PMID: 39506115
- Evidence: We used the function numpy.wrap in Python to detect large deltas that jump from 1 to 0 and added +1 from that point on.
- Full pipeline: differential/statistical testing [pandas v2.0.3, xarray v2023.6.0] -> stage not stated [DeepLabCut, NumPy, Python, SciPy]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Version used: **1.22.0**
- Evidence: This used custom-made code but made use of libraries such as numpy (1.22.0), scipy (1.10.1), matplotlib (3.7.3), sciKit learn (1.3.2), pandas (2.0.3) and seaborn (0.13.2).
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Version used: **1.24.1**
- Evidence: The following packages have been used for Good–Turing and Bayesian regression: R v.4.2.2 (2022-10-31), plyr_1.8.9, tools_4.2.2, jsonlite_1.8.8, grid_4.2.2, tidyselect_1.2.0; Python v.3.8.15, packaged by conda-forge, sklearn v.0.2, joblib v.1.2.0, numpy v.1.24.1, scipy v.1.10.1 and threadpoolctl v.3.1.0.
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### Anti-viral defence by an mRNA ADP-ribosyltransferase that blocks translation. (Nature 2024)

- DOI: 10.1038/s41586-024-08102-8 | PMCID: PMC11618068 | PMID: 39443800
- Evidence: Sam files generated from bowtie2 mapping were then converted to bam files using samtools 56 (version 1.7) and then further converted to numpy arrays using the genomearray3 python library 57 for use in downstream analyses.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, NumPy, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, HMMER]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Version used: **1.23.4**
- Evidence: The principal component vectors of the downsampled Harmony-integrated object were then used to transform the gene expression matrix (NumPy (v.1.23.4) function ‘linalg.lstsq’, rcond = ‘warn’) of all cells in the non-downsampled pooled data and project for UMAP visualization (Fig.
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **1.23.2**
- Evidence: The analysis and plotting (for this section and the following) were done using R v.4.3.1 and python v.3.10.6, as well as the R packages ggplot2 v.3.3.6 and tidyverse v.1.3.2 and python library numpy v.1.23.2.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### A Drosophila computational brain model reveals sensorimotor processing. (Nature 2024)

- DOI: 10.1038/s41586-024-07763-9 | PMCID: PMC11446845 | PMID: 39358519
- Evidence: Area under the curve was approximated with the trapezoidal rule in Python using the NumPy.trapz function.
- Full pipeline: stage not stated [Brian2, NumPy, Python]

### Network statistics of the whole-brain connectome of Drosophila. (Nature 2024)

- DOI: 10.1038/s41586-024-07968-y | PMCID: PMC11446825 | PMID: 39358527
- Evidence: Code availability The analyses presented in this paper were performed in Python with the numpy and graph-tool 71 packages, and in MATLAB (standard toolboxes).
- Full pipeline: stage not stated [NumPy, Python]

### Future increase in extreme El Niño supported by past glacial changes. (Nature 2024)

- DOI: 10.1038/s41586-024-07984-y | PMCID: PMC11464383 | PMID: 39322673
- Evidence: Code availability Open-sourced Python code was used to create the figures, perform the analyses and all calculations, including the following modules and their required dependencies: matplotlib 78 , pandas 79 , NumPy 80 , seaborn 81 , xarray 82 , cartopy 83 and SciPy 84 .
- Full pipeline: simulation/modelling [CESM v1.2] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn, xarray]

### Brain-wide dynamics linking sensation to action during decision-making. (Nature 2024)

- DOI: 10.1038/s41586-024-07908-w | PMCID: PMC11499283 | PMID: 39261727
- Evidence: The outlier detection model was implemented using custom Python software using the NumPy, SciPy, and PyTorch libraries.
- Full pipeline: machine learning [DeepLabCut] -> stage not stated [Kilosort v2.0, NumPy, PyTorch, SciPy]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **1.24.2**
- Evidence: ...etailed in next paragraph). scRNA-sequencing Analysis and visualization of the data were conducted in a Python environment built on Pandas (v.2.0.1), NumPy (v.1.24.2) 73 , SciPy (v.1.10.1) 74 , scikit-learn (v.1.2.0), SCANPY (v1.9.3) 75 , AnnData (v.0.9.1) 75 , matplotlib (v.3.7.1) 76 and seaborn (v.0.13.1) 77 packages.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Version used: **1.26.0**
- Evidence: Single-molecule data interpretation Raw data exported from LUMICKS Bluelake as .h5 files were processed with custom-written Jupyter Notebooks in Python 3.9 using LUMICKS Pylake v.1.2.1, numpy v.1.26.0, matplotlib v.3.7.2, scipy v.1.11.3 and peakutils v.1.3.4 ( https://github.com/singlemoleculegroup ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: CV calculations were performed using the formula ‘np.std( x , ddof = 0)/np.mean( x )’, where ‘ x ’ is the array of normalized analyte values and ‘np’ refers to the numpy scientific computing package ( v = 1.26).
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### Descending networks transform command signals into population motor control. (Nature 2024)

- DOI: 10.1038/s41586-024-07523-9 | PMCID: PMC11186778 | PMID: 38839968
- Evidence: Statistics on DN connectivity across multiple synapses were computed using matrix multiplication with the numpy library on the adjacency matrix of the network.
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> stage not stated [NetworkX, SLEAP v1.3.0]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Recorded F 350 / F 330 was analysed by using Python libraries including pandas, numpy, scipy and seaborn in Visual Studio Code (Microsoft).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Life-cycle-coupled evolution of mitosis in close relatives of animals. (Nature 2024)

- DOI: 10.1038/s41586-024-07430-z | PMCID: PMC11153136 | PMID: 38778110
- Evidence: The tracing of bundles and twist calculations were previously written in Python programming language using PyCharm IDE, with external libraries such as NumPy, scikit-image, Matplotlib, PIL, OpenCV and SciPy.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [HMMER v3.3.2, ImageJ, Matplotlib, NumPy, OpenCV, Python, SciPy, scikit-image]

### A warm Neptune's methane reveals core mass and vigorous atmospheric mixing. (Nature 2024)

- DOI: 10.1038/s41586-024-07395-z | PMCID: PMC11208151 | PMID: 38768633
- Evidence: Moreover, these codes made use ExoTiC-LD 117 ( https://exotic-ld.readthedocs.io/en/latest/ ) and Emcee ( https://emcee.readthedocs.io/en/stable/ ) 118 , which use the Python libraries scipy 119 , numpy 120 , astropy 121 and matplotlib 122 .
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty, emcee]

### Accurate structure prediction of biomolecular interactions with AlphaFold 3. (Nature 2024)

- DOI: 10.1038/s41586-024-07487-w | PMCID: PMC11168924 | PMID: 38718835
- Version used: **1.26.3**
- Evidence: Model performance analysis and visualization Data analysis used Python v.3.11.7 ( https://www.python.org/ ), NumPy v.1.26.3 ( https://github.com/numpy/numpy ), SciPy v.1.9.3 ( https://www.scipy.org/ ), seaborn v.0.12.2 ( https://github.com/mwaskom/seaborn ), Matplotlib v.3.6.1 ( https://github.com/matplotlib/matplotlib ), pandas v.2.0.3 ( https://github.com/pandas-dev/pandas ), statsmodels v.0.12....
- Full pipeline: visualisation [NumPy v1.26.3, SciPy v1.9.3, seaborn v0.12.2] -> stage not stated [AlphaFold, Matplotlib v3.6.1, RDKit, RoseTTAFold, statsmodels v0.12.2]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Handling of geospatial and other data was conducted using the R packages lme4, matrixStats, Matrix, geojsonio, raster, rgeos, sf, sp, tmaptools, patchwork, leaflet, data.table, dplyr, haven, Hmisc, openxlsx, rgdal, scales, stringr, tidyr, tibble, xlsx, rfPermute, randomForest, forcats, and in python using the packages pandas, numpy, scipy, statsmodels, firthlogist, patsy and jupyter 68 – 97 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Single-cell analysis reveals context-dependent, cell-level selection of mtDNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07332-0 | PMCID: PMC11078733 | PMID: 38658765
- Version used: **1.21.0**
- Evidence: The analyses were performed using Python v3.7.12, with the following modules: matplotlib v3.4.2, numpy v1.21.0, pandas v1.1.5, plotly v5.16.1, pysam v0.16.0.1, scikit-learn v0.23.1, scipy v1.7.0 and seaborn v0.11.1.
- Full pipeline: quality control [MultiQC v1.11] -> stage not stated [Matplotlib v3.4.2, NumPy v1.21.0, R, SciPy v1.7.0, scikit-learn v0.23.1, seaborn v0.11.1]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Version used: **1.20.1**
- Evidence: 0.7.5), Pandas (v.1.2.3), NumPy (v.1.20.1), and Python (v.3) were used to pool single-cell counts and conduct downstream analysis.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.17.5**
- Evidence: DGE matrices were processed using the following R and python packages: Seurat (v.3.2.2) 64 , SeuratDisk (v.0.0.0.9010) 65 , anndata (v.0.8.0) 66 , numpy (v.1.17.5) 67 , pandas (v.1.0.5) 68 , 69 and Scanpy (v.1.9.1) 70 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Incomplete transcripts dominate the Mycobacterium tuberculosis transcriptome. (Nature 2024)

- DOI: 10.1038/s41586-024-07105-9 | PMCID: PMC10937400 | PMID: 38418874
- Version used: **1.24.3**
- Evidence: Data analysis and visualization scripts used Python packages including Matplotlib (v3.7.1), Numpy (v1.24.3), Scipy (v1.10.1), bioinfokit (v0.3), and pyCircos (v0.3.0).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, SAMtools v1.17] -> visualisation [Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1] -> stage not stated [Cutadapt v4.1, Python]

### Influence of pump laser fluence on ultrafast myoglobin structural dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07032-9 | PMCID: PMC10881388 | PMID: 38355794
- Evidence: Structures were analysed using COOT 65 , 66 , PYMOL 67 and custom-written python scripts using NumPy 68 and SciPy 69 .
- Full pipeline: normalisation [CCP4] -> structure determination [CCP4] -> stage not stated [NumPy, SciPy]

### A dynamical measure of the black hole mass in a quasar 11 billion years ago. (Nature 2024)

- DOI: 10.1038/s41586-024-07053-4 | PMCID: PMC11636685 | PMID: 38286342
- Evidence: GILDAS is publicly available on the IRAM webpage ( https://www.iram.fr/IRAMFR/GILDAS/ ). astropy, matplotlib, emcee, dynesty, numpy and scipy are all available through the Python Package Index ( https://pypi.org ).
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Affinity-optimizing enhancer variants disrupt development. (Nature 2024)

- DOI: 10.1038/s41586-023-06922-8 | PMCID: PMC10830414 | PMID: 38233525
- Evidence: MPRA data were analysed using standard Python libraries (pandas, numpy, scipy, seaborn, matplotlib).
- Full pipeline: differential/statistical testing [R] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Version used: **1.19.5**
- Evidence: The deep learning models were run in a conda environment in which python (v.3.7; RRID: SCR_008394 ), tensorflow-gpu (v.1.15; RRID: SCR_016345 ) 62 , numpy (v.1.19.5; RRID: SCR_008633 ) 63 , ipykernel (v.5.1.2; RRID: SCR_024813 ) and h5py (v.2.10.0; RRID: SCR_024812 ) packages were installed.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Exported bed files were used as input to deeptools multiBigWig summary, yielding coverage intensity matrix file sin.npz format, which were then read into R using numpy and reticulate.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Evidence: Numerical computations and data handling were conducted using NumPy 84 (v.1.26.4) and Pandas (v.2.1.4, NumFOCUS).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### A parabrachial hub for need-state control of enduring pain. (Nature 2025)

- DOI: 10.1038/s41586-025-09602-x | PMCID: PMC12630001 | PMID: 41062698
- Evidence: The raw count matrix (stitched expression matrix.csv file), which contained gene expression values per cell, was converted into a dense 2D NumPy array to ensure compatibility with AnnData.
- Full pipeline: quantification [NumPy, Scanpy] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP, seaborn] -> visualisation [UMAP, seaborn] -> stage not stated [AnnData, ImageJ]

### Flexible perceptual encoding by discrete gamma events. (Nature 2025)

- DOI: 10.1038/s41586-025-09604-9 | PMCID: PMC12657229 | PMID: 41062693
- Version used: **1.11.3**
- Evidence: Single-unit clustering Single units were extracted from LFP recording using spikedetekt and clustered using klustakwik2 (Python v2.7.16 and NumPy v1.11.3) 71 .
- Full pipeline: dimensionality reduction/clustering [NumPy v1.11.3, UMAP] -> stage not stated [Psychtoolbox]

### DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning. (Nature 2025)

- DOI: 10.1038/s41586-025-09422-z | PMCID: PMC12443585 | PMID: 40962978
- Version used: **1.23.1**
- Evidence: Data analysis used Python v.3.8 ( https://www.python.org/ ), NumPy v.1.23.1 ( https://github.com/numpy/numpy ), Matplotlib v.3.5.2 ( https://github.com/matplotlib/matplotlib ) and TensorBoard v.2.9.1 ( https://github.com/tensorflow/tensorboard ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [Matplotlib v3.5.2, NumPy v1.23.1]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **1.20**
- Evidence: Statistical analyses were performed with Python v3.8, v3.9 and v3.10 with the packages pandas v1.1.4 and numpy v1.20.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Divergent evolutionary strategies pre-empt tissue collision in gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09447-4 | PMCID: PMC12527943 | PMID: 40903584
- Evidence: Quantitative data were analysed and processed using Excel, or custom-made ImageJ or FIJI macros and Python scripts using Numpy, Pandas and SciPy libraries.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [ImageJ, Matplotlib, NumPy, Python, SciPy, seaborn]

### Seismic detection of a 600-km solid inner core in Mars. (Nature 2025)

- DOI: 10.1038/s41586-025-09361-9 | PMCID: PMC12408336 | PMID: 40903600
- Evidence: Figures were created using matplotlib 73 , seismic data processing was done in ObsPy 74 , and inversions were done in NumPy and SciPy (refs.
- Full pipeline: visualisation [Matplotlib, NumPy, SciPy]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: Methods Overview of software, data and workflow We conducted our LSP mapping workflow using Google Earth Engine (GEE) (v.0.1.404 or later) 65 and performed additional analyses using Python 66 with a set of core scientific packages (numpy 67 , shapely 68 , pandas 69 , geopandas 70 , rasterio 71 , xarray 72 , rasterstats 73 , dask 74 , scipy 75 , scikit-learn 76 , statsmodels 77 and matplotlib 78 ).
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### One-third of Sun-like stars are born with misaligned planet-forming disks. (Nature 2025)

- DOI: 10.1038/s41586-025-09324-0 | PMCID: PMC12350154 | PMID: 40770103
- Evidence: 97 ), Lightkurve 68 , Astropy 102 , NumPy 103 , SciPy 104 and Matplotlib 105 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, Python, SciPy]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **1.19.3**
- Evidence: ...charts, interaction plots, error bars and contour figures were generated using the following Python, R and Matlab packages: Python: pandas (v.1.1.5), numpy (v.1.19.3), anndata (v.0.7.4), scanpy (v.1.6.0), matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R packages: ggplot2 (v.3.4.4), gplots (v.3.1.3), readr (v.2.1.4), dplyr (v.1.1.2), reshape2 (v.1.4.4), patchwork...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Both the computational analysis library and the code for all analyses are available online through GitHub and Zenodo, as detailed in the Code and Data availability sections. spatiomic comes with support for multiple common microscopy imaging formats and flexibly supports AnnData 74 objects, NumPy 75 arrays and pandas DataFrames 76 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Evidence for a sub-Jovian planet in the young TWA 7 disk. (Nature 2025)

- DOI: 10.1038/s41586-025-09150-4 | PMCID: PMC12221965 | PMID: 40562924
- Evidence: We used various functions of the following software packages to perform the analysis and create the figures: numpy, astropy, scipy, matplotlib and photutils.
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy]

### Unsupervised pretraining in biological neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09180-y | PMCID: PMC12367527 | PMID: 40533561
- Evidence: 59 ), primarily based on numpy and scikit-learn 60 , 61 , as well as Rastermap 39 .
- Full pipeline: visualisation [Matplotlib] -> stage not stated [NumPy, Python, SciPy, Suite2p, scikit-learn]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Evidence: Gene–gene correlation was calculated with numpy.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **1.24.2**
- Evidence: Python packages such as Scanpy (v.1.9.5), Pandas (v.2.0.0), Statsmodels (v.0.14.0), NumPy (v.1.24.2), Scipy (v.1.10.1), Matplotlib (v.3.8.0), Seaborn (v.0.11.2) and Sklearn (v.1.3.2), were used for data analysis.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Visualization was performed using a combination of Matplotlib 70 , SciPy 71 and NumPy 72 , and expression values are shown in heat maps as log 2 TPM to represent log fold change.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Light-microscopy-based connectomic reconstruction of mammalian brain tissue. (Nature 2025)

- DOI: 10.1038/s41586-025-08985-1 | PMCID: PMC12158774 | PMID: 40335689
- Evidence: We used the numpy.clip function to clip the intensity range plane by plane typically between 120 and 350, determined by visual inspection.
- Full pipeline: machine learning [PyTorch v1.12.1] -> stage not stated [BigStitcher, Jupyter, NumPy, Python v3.8, SciPy, scikit-image, seaborn]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **1.19.2**
- Evidence: Custom scripts used NumPy (1.19.2) 92 and Pandas (1.1.3) 93 .
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### A distributed coding logic for thermosensation and inflammatory pain. (Nature 2025)

- DOI: 10.1038/s41586-025-08875-6 | PMCID: PMC12222022 | PMID: 40269164
- Version used: **1.19.2**
- Evidence: All quantification and statistical analyses were performed using Python v.3.8, Pandas v.1.1.3, Numpy v.1.19.2 and Scipy v.1.5.2.
- Full pipeline: quantification [NumPy v1.19.2, SciPy v1.5.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.19.2, SciPy v1.5.2] -> stage not stated [ImageJ, OpenCV, Python, Seurat, scDblFinder]

### Functional connectomics spanning multiple areas of mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08790-w | PMCID: PMC11981939 | PMID: 40205214
- Evidence: ...astructure 1 (available at https://github.com/CAVEconnectome ) and CloudVolume 94 to interact with data infrastructure, and libraries Matplotlib 95 , Numpy 96 and Pandas for general computation and data visualization.
- Full pipeline: machine learning [CaImAn] -> visualisation [Matplotlib, NumPy] -> stage not stated [Python, SciPy]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Version used: **1.23.5**
- Evidence: ...E (4.12,4.14,4.16) were used for storing and managing data; Meshparty (1.16), NEURD (1.0.0) and pcg_skel (0.3,0.2) were used for morphology analysis; Numpy (1.23.5), pandas (1.5.3), SciPy (1.10.1), statsmodels (0.13.5), scikit-learn (1.2.1), PyTorch (1.12.1), tidyverse (2.0.0), glmmTMB (1.1.10), performance (0.12.2) and emmeans (1.10.3) were used for model training and statistical analysis; Matplo...
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Connectomics of predicted Sst transcriptomic types in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08805-6 | PMCID: PMC11981948 | PMID: 40205210
- Evidence: We used the following libraries for visualization and analysis: Matplotlib 73 , Seaborn 74 , Numpy 75 , Pandas 76 , VTK 77 , Scipy 78 , Scikit-posthocs 79 , Scikit-learn 80 , scrattch-hicat ( https://github.com/AllenInstitute/scrattch.hicat/ ) and statsmodels 81 .
- Full pipeline: differential/statistical testing [limma] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn, seaborn, statsmodels]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Version used: **1.21.6**
- Evidence: The area under the KDE curves was integrated using the trapz function from Python package numpy (v.1.21.6).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: To achieve this, we used the Python package cloudvolume ( https://github.com/seung-lab/cloud-volume ; v.8.5.1) to convert our 3D KDE volumes from the numpy format to precomputed layers compatible with Neuroglancer and then loaded these layers into the Brainsharer web portal to create the final visualization.
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### Connectome-driven neural inventory of a complete visual system. (Nature 2025)

- DOI: 10.1038/s41586-025-08746-0 | PMCID: PMC12119369 | PMID: 40140576
- Evidence: In the version-controlled code repository ( https://github.com/reiserlab/male-drosophila-visual-system-connectome-code ), we document dependencies such as Pandas 120 , NumPy 121 , SciPy 92 , Jupyter 122 , Plotly 123 , Snakemake 84 and Trimesh 124 .
- Full pipeline: dimensionality reduction/clustering [Python, SciPy] -> structure determination [BigStitcher] -> stage not stated [Jupyter, NumPy, Snakemake]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **1.23.5**
- Evidence: SL-Smart-seq3xpress data analysis Count matrices were processed with JupyterLab (v.4) notebooks using IPython (v.7.31) using the following modules: pandas (v.1.5.3), numpy (v.1.23.5), scipy (v.1.10.1), scanpy (v.1.7.2), openpyxl (v.3.1.2), matplotlib (v.3.6.3) and seaborn (v.0.12.2).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **1.24.3**
- Evidence: Python packages used: beautifulsoup4 v.4.12.2, bio v.1.6.2, GSEApy v.1.1.0, matplotlib v.3.7.1, NumPy v.1.24.3, pandas v.2.0.2, SciPy v.1.10.1, seaborn v.0.12.2, sklearn v.0.0.post5, urllib3 v.2.0.3.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### World and Human Action Models towards gameplay ideation. (Nature 2025)

- DOI: 10.1038/s41586-025-08600-3 | PMCID: PMC11839478 | PMID: 39972228
- Evidence: 2b shows a strong correlation ( r = 0.77, with sample Pearson’s correlation coefficient calculated using numpy’s corrcoef function 76 ) between FVD and the training loss, providing a strong justification for optimizing towards a lower loss (similar observations relating model performance to loss have also been observed in the language domain 73 ).
- Full pipeline: machine learning [NumPy, PyTorch]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: Initial parameter estimation: g and A tensors were estimated using laboratory-developed scripts in Python (SciPy/NumPy) 74 .
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Version used: **1.23.4**
- Evidence: We analysed data using Python (v.3.9.12) with Biopython (v.1.78), Pandas (v.1.5.1) and NumPy (v.1.23.4).
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **1.23.4**
- Evidence: Data analysis was performed using Python (v.3.9.12) with Biopython (v.1.78), Pandas (v.1.5.1), SciPy package (v.1.10.0) and NumPy (v.1.23.4). sgRNA enrichment was calculated as previously described 52 , 69 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Version used: **1.26.4**
- Evidence: ...he analysis and plotting of snRNA-seq and spatial transcriptomics datasets: Python v.3.10.8–v.3.10.12, scvi v.0.19.0, scanpy v.1.9.8, pandas v.1.4.4, numpy v.1.26.4, cell2location v.0.1.2, cellbender v.0.1–v.0.2, cellex v.1.2.2, CELLECT v.1.3.0, R v.4.3.1, future.apply v.1.11.1-9001, future v.1.33.1-9009, pbapply v.1.7-2, Matrix v.1.6-1.1, scUtils v.0.0.1, magrittr v.2.0.3, igraph v.1.5.1, treeio ...
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Emergence of collective oscillations in massive human crowds. (Nature 2025)

- DOI: 10.1038/s41586-024-08514-6 | PMCID: PMC11798876 | PMID: 39910390
- Evidence: Characterization tools We developed all our numerical tools using mostly the numpy package of the Python numerical language.
- Full pipeline: stage not stated [NumPy, Python]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Evidence: Clustering analyses of grid-cell modules and bursting subtypes of grid cells were conducted using the python package Scanpy 87 and its dependencies (including numpy, pandas, scipy, scikit-learn and matplotlib).
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

### Complete human recombination maps. (Nature 2025)

- DOI: 10.1038/s41586-024-08450-5 | PMCID: PMC11922761 | PMID: 39843742
- Version used: **1.24.2**
- Evidence: ...per ; NCOurd, https://github.com/DecodeGenetics/NCOurd ; R (v.4.2.2 with lm v.4.2.2, xoi v.0.67-1), https://www.r-project.org/ ; Python (v.3.8.1 with numpy v.1.24.2, pandas v.1.4.0, scipy v.1.10.1, statsmodels v.0.13.2), https://www.python.org/downloads/ .
- Full pipeline: stage not stated [NumPy v1.24.2, SciPy v1.10.1, lme4, statsmodels v0.13.2]

### Accurate predictions on small data with a tabular foundation model. (Nature 2025)

- DOI: 10.1038/s41586-024-08328-6 | PMCID: PMC11711098 | PMID: 39780007
- Evidence: If we simply provide the data in a tabular format (NumPy matrix), TabPFN will automatically handle missing values, encode categorical variables and normalize features.
- Full pipeline: normalisation [NumPy] -> differential/statistical testing [LightGBM, XGBoost]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: For each sample, a two-dimensional Numpy array of zeroes was generated, which modelled the total pixel area imaged.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: ...s a function of the actual age, and a line of best fit for the median predicted ages as a function of actual age is shown in black and computed using numpy.polyfit with deg = 1.
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Evidence: The resulti ng numpy matrices were concatenated to obtain an ‘augmented’ cell–cell affinity matrix that consists of three main components: (1) similarity between in vivo cells; (2) similarity between in vitro cells; (3) similarity between in vitro and in vivo cells.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: The pybedtools and pybigwig packages were used to work with bed files and bigwig files, the loompy package was used to work with loom files, numpy was used to work with matrices and numba was used to speed up computations wherever possible.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Eigenvalues and eigenvectors of L_norm were calculated using the eig function from the linalg module in NumPy, and the coefficients of the first and third nontrivial eigenvectors were used as coordinates of a node.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Version used: **1.24.3**
- Evidence: All behavioural and neural analyses were performed using custom-written Python (v.3.8) code unless otherwise noted, incorporating the analysis and plotting libraries numpy (v.1.24.3), scipy (v.1.10.1), scikit-learn (v.1.3.0), pandas (v.2.0.3), seaborn (v.0.12.2), elephant (v.1.0.0) and statsmodels (v.0.14.0).
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### An AI system to help scientists write expert-level empirical software. (Nature 2026)

- DOI: 10.1038/s41586-026-10658-6 | PMCID: PMC13293872 | PMID: 42156545
- Evidence: To force the model to reason from first principles, its access was restricted to basic libraries (numpy, pandas and holidays).
- Full pipeline: stage not stated [NumPy, XGBoost, scikit-learn, statsmodels]

### Language models transmit behavioural traits through hidden signals in data. (Nature 2026)

- DOI: 10.1038/s41586-026-10319-8 | PMCID: PMC13083239 | PMID: 41986627
- Evidence: Data analysis was performed using Python (NumPy, Pandas) and Matplotlib.
- Full pipeline: stage not stated [Matplotlib, NumPy]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: Gene expression dynamics over pseudotime and real time were analysed by calculating the mean gene expression or gene list scores at each timepoint, followed by polynomial fitting using numpy.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Towards end-to-end automation of AI research. (Nature 2026)

- DOI: 10.1038/s41586-026-10265-5 | PMCID: PMC13017497 | PMID: 41882133
- Evidence: The system is prompted to save all relevant experimental outputs (training and validation metrics, losses and so on) into structured numpy files.
- Full pipeline: machine learning [NumPy] -> stage not stated [Python]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **2.0.2**
- Evidence: Data processing, model training and evaluation were implemented in Python using numpy v.2.0.2, tensorflow v.2.19.0, scipy v.1.16.3, statsmodels v.0.14.6, sklearn v.1.6.1, shap v.0.50.0, xgboost v.3.1.2, torch v.2.9.0, pandas v.2.2.2, umap v.0.5.9.post2, pickle v.4.0, pytz v.2025.2, re v.2.2.1, tqdm v.4.67.1, IPython v.7.34.0, json v.2.0.9 and altair v.5.5.0.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: All computational analyses and visualizations were performed in Python (v3.10), using the NumPy 76 , Pandas 77 , SciPy 78 and Matplotlib 79 libraries.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **1.24.4**
- Evidence: Single-cell sequencing and pseudobulk analyses Single-cell RNA-seq datasets from multiple human tissues were processed for tissue-specific pseudobulk analysis using Python (v.3.9.12) with Scanpy (v.1.9.3), Pandas (v.1.5.3) and Numpy (v.1.24.4).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Evidence: Sam files generated from bowtie2 mapping were converted to bam files using samtools (v1.7) 52 , and then converted to numpy arrays using the genomearray3 Python library 30 .
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### Regulatory grammar in human promoters uncovered by MPRA-based deep learning. (Nature 2026)

- DOI: 10.1038/s41586-025-10093-z | PMCID: PMC13017510 | PMID: 41639451
- Evidence: As a baseline comparison, we computed the concordance in direction for random predictions by randomly sampling from a uniform distribution using the random.uniform implementation from NumPy set from −1 to +1 (ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1] -> stage not stated [NumPy, PyTorch v2.1.1]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Evidence: Software versions SCANPY (v. ≥1.9), pingouin (v.0.5.4), gseapy (v.1.1.1), numpy (v. ≥1.26), scipy (v. ≥1.12), scikit-learn (v. ≥1.13), leidenalg (v.0.10.2), matplotlib (v.3.8.4), Cellrank (v.2.0.7), Palantir (v.1.4.1), R (v.4.3.3), FIJI/ImageJ (v. >1.54) and GraphPad (v. >9.0) were used.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Quantum spin resonance in engineered proteins for multimodal sensing. (Nature 2026)

- DOI: 10.1038/s41586-025-09971-3 | PMCID: PMC12851924 | PMID: 41565820
- Version used: **126.4**
- Evidence: Data processing was performed using Python (v3.11.11), SciPy (v1.15.1) 64 , NumPy (v.126.4) 65 , scikit-learn (v1.6.1) 66 and scikit-image (v0.20.0) 66 .
- Full pipeline: machine learning [XGBoost] -> stage not stated [NumPy v126.4, SciPy v1.15.1, scikit-image v0.20.0, scikit-learn v1.6.1]

### Ligand-specific activation trajectories dictate GPCR signalling in cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09963-3 | PMCID: PMC12935549 | PMID: 41535472
- Evidence: 4 ) were generated using the NumPy and matplotlib libraries of Python (v.3.7.9) 66 , 67 .
- Full pipeline: visualisation [ChimeraX] -> stage not stated [ImageJ v1.5.4f, Matplotlib, NumPy]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: Subsequently, we performed eigenvector decomposition on the z -scored Pearson correlation matrix using LA.eig() (linalg package in numpy), selecting the eigenvector with the largest eigenvalue.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Version used: **1.26.2**
- Evidence: Analyses we carried out with Python (v.3.12.0), using also the following libraries: numpy (v.1.26.2), scipy (v.1.11.4), statsmodels (v.0.14.0), and matplotlib (v.3.8.2) and seabron (v.0.11.2) for visualization.
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **1.21.5**
- Evidence: Standard packages such as numpy (v.1.21.5), pandas (v.1.0.1) and scipy (v.1.4.1) were correspondingly used for data handling, processing, normalization, statistical calculations and/or data fitting.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Evidence: Next, the random number generator of numpy (seed, 19,680,801) was used to generate a random number from 0 to 15 to pick one random centromere.
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **2.2.6**
- Evidence: Commonly used Python libraries (Python v3.11.13, matplotlib v3.10, Seaborn v0.13, numpy v2.2.6, pandas v2.3.1, scipy v1.16.0, anndata v0.11.4 and shapely v2.1.1) were applied to visualize spatial distribution of cells.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: All analyses were conducted using skimage for image processing 71 , 72 , numpy and pandas for data handling, matplotlib and seaborn for visualization, and scipy and scikit-learn for statistical and machine learning operations.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### A catalog of tens of thousands of viruses from human metagenomes reveals hidden associations with chronic diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2023202118 | PMCID: PMC8201803 | PMID: 34083435
- Evidence: Wilcoxon rank-sum test was computed with 100 bootstraps using Python, NumPy, and SciPy ( 103 ) for each OTU in a given study in which at least 10% of the total samples had an RPKM of at least 0.05 (bacterial OTUs with “IGGsearch abundance” of at least 0.005 in at least 10% of the samples were kept).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2, NumPy, SAMtools, SciPy] -> machine learning [scikit-learn] -> stage not stated [Cytoscape, RepeatMasker]

### A modular computational framework for medical digital twins. (PNAS 2021)

- DOI: 10.1073/pnas.2024287118 | PMCID: PMC8157963 | PMID: 33972437
- Evidence: To achieve this, we provide a high-level API that wraps a series of NumPy data structures ( 11 ).
- Full pipeline: stage not stated [Docker, NumPy, Python, SciPy]

### Global inequality remotely sensed. (PNAS 2021)

- DOI: 10.1073/pnas.1919913118 | PMCID: PMC8106331 | PMID: 33903226
- Evidence: The analysis was carried out in R ( https://www.r-project.org ) using the packages raster, rasterVis, sp, rgdal, ggplot2, and mixtools and Python ( https://www.python.org/ ) using numpy, matplotlib, scipy, and statsmodels.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, statsmodels]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Version used: **1.16.4**
- Evidence: The Pandas (v0.42.2) ( 60 ) and NumPy (v1.16.4) ( 61 ) packages were employed for data processing and calculations of vNE.
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### &lt;i&gt;ARABIDOPSIS THALIANA HOMEOBOX GENE 1&lt;/i&gt; controls plant architecture by locally restricting environmental responses. (PNAS 2021)

- DOI: 10.1073/pnas.2018615118 | PMCID: PMC8092594 | PMID: 33888582
- Evidence: For statistical analysis and plotting graphs, functions were used from Numerical Python ( https://numpy.org ), Scientific Python ( https://www.scipy.org ), and MatPlotLib ( https://matplotlib.org ).
- Full pipeline: differential/statistical testing [Matplotlib, NumPy, SciPy] -> stage not stated [MACS2]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: All metrics are calculated using the Python packages Sklearn version 0.21.2 ( 53 ), SciPy version 1.2.1 ( 54 ), and NumPy.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Noninvasive neuromagnetic single-trial analysis of human neocortical population spikes. (PNAS 2021)

- DOI: 10.1073/pnas.2017401118 | PMCID: PMC7980398 | PMID: 33707209
- Version used: **1.18.2**
- Evidence: Data Availability All analyses were performed in the Python programming language in its most recent version (3.8.2) relying on the additional packages numpy (1.18.2), scipy (1.4.1), matplotlib (3.2.1), and the author-made M/EEG-analysis package “meet” in its most recent version ( https://github.com/neurophysics/meet ).
- Full pipeline: stage not stated [Matplotlib v3.2.1, NumPy v1.18.2, SciPy v1.4.1]

### Climate control on terrestrial biospheric carbon turnover. (PNAS 2021)

- DOI: 10.1073/pnas.2011585118 | PMCID: PMC7923348 | PMID: 33593902
- Evidence: Regression analyses were performed using the Numpy and Scipy packages in Python version 3.5; all analysis code is provided in Dataset S1 .
- Full pipeline: differential/statistical testing [NumPy, Python v3.5, SciPy]

### The molecular basis for pore pattern morphogenesis in diatom silica. (PNAS 2022)

- DOI: 10.1073/pnas.2211549119 | PMCID: PMC9894196 | PMID: 36459651
- Evidence: The python code for image processing was partially adapted from the skimage tutorial repository using python 3.7.4 and various packages [scipy, numpy, pandas and scikit-image ( 64 )].
- Full pipeline: dimensionality reduction/clustering [scikit-learn v0.21.3] -> differential/statistical testing [Matplotlib v3.5, seaborn v0.11] -> visualisation [Matplotlib v3.5, seaborn v0.11] -> stage not stated [BLAST, NumPy, SciPy, scikit-image]

### A tool for monitoring cell type-specific focused ultrasound neuromodulation and control of chronic epilepsy. (PNAS 2022)

- DOI: 10.1073/pnas.2206828119 | PMCID: PMC9674244 | PMID: 36343238
- Evidence: Randomization was performed by assembling arrays of all stimulus protocol iterations and shuffling with the NumPy random permutation function.
- Full pipeline: alignment/mapping [SPM] -> quantification [Python, SciPy] -> differential/statistical testing [NumPy, SPM]

### Adult neurogenesis acts as a neural regularizer. (PNAS 2022)

- DOI: 10.1073/pnas.2206704119 | PMCID: PMC9659416 | PMID: 36322739
- Evidence: Models were built and analyzed in Python 3.6 ( 65 ) with custom scripts that are freely available on GitHub, and were developed using the following packages: PyTorch ( 66 ), Ax ( https://github.com/facebook/Ax ), NumPy ( 67 ), SciPy ( 68 ), Pandas ( 69 ), Matplotlib ( 70 ), Seaborn ( 71 ), and Scikit-learn 0.21.1 ( 72 ).
- Full pipeline: stage not stated [Matplotlib, NumPy, PyTorch, Python v3.6, SciPy, scikit-learn v0.21.1, seaborn]

### Rapid homeostatic modulation of transsynaptic nanocolumn rings. (PNAS 2022)

- DOI: 10.1073/pnas.2119044119 | PMCID: PMC9659372 | PMID: 36322725
- Evidence: Electrophysiology data were acquired with Clampex (Molecular Devices) and analyzed using routines written with scientific python libraries, including numpy, scipy, IPython, and neo ( 43 ). mEPSPs were detected using an implementation of a template-matching algorithm ( 44 , 45 ).
- Full pipeline: stage not stated [ImageJ v1.51n, Jupyter, NumPy, SciPy]

### Sharp turns and gyrotaxis modulate surface accumulation of microorganisms. (PNAS 2022)

- DOI: 10.1073/pnas.2206738119 | PMCID: PMC9586295 | PMID: 36219692
- Evidence: The Python program (Python 3.0) together with an open source library (NumPy; https://numpy.org/ ) was used to compute the variation of V s , ω , D r , and PDF ( P ) with y (or z ) and orientation ϕ (or θ ) in the horizontal (or vertical) plane.
- Full pipeline: simulation/modelling [ImageJ, TrackMate] -> stage not stated [NumPy, Python v3.0]

### Microbial functional diversity across biogeochemical provinces in the central Pacific Ocean. (PNAS 2022)

- DOI: 10.1073/pnas.2200014119 | PMCID: PMC9477243 | PMID: 36067300
- Evidence: Attenuation of protein abundance through the microbial communities with depth was calculated by fitting a power law model to protein abundance using the following equation with NumPy ( 79 ): f protein ( z ) = a z c .
- Full pipeline: quantification [NumPy] -> dimensionality reduction/clustering [SciPy]

### Adaptive exchange sustains cullin-RING ubiquitin ligase networks and proper licensing of DNA replication. (PNAS 2022)

- DOI: 10.1073/pnas.2205608119 | PMCID: PMC9456757 | PMID: 36037385
- Version used: **1.12.1**
- Evidence: All additional CRISPR screen data analyses were performed in Python 2.7 using a combination of Numpy (v1.12.1), Pandas (v0.17.1), and Scipy (v0.17.0).
- Full pipeline: stage not stated [NumPy v1.12.1, Python v2.7, SciPy v0.17.0]

### Taxonomic classification of DNA sequences beyond sequence similarity using deep neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2122636119 | PMCID: PMC9436379 | PMID: 36018838
- Version used: **1.19.2**
- Evidence: BERTax was implemented in Python 3.7 and uses the Python packages scipy (1.6.1) ( 40 ), keras (2.4.3), tensorflow (2.4.1) ( 41 ), numpy (1.19.2) ( 42 ), and keras-bert (0.86.0).
- Full pipeline: stage not stated [Kraken2, NumPy v1.19.2, Python v3.7, SciPy v1.6.1, minimap2]

### Repertoire-scale measures of antigen binding. (PNAS 2022)

- DOI: 10.1073/pnas.2203505119 | PMCID: PMC9407674 | PMID: 35969768
- Version used: **1.18.0**
- Evidence: Recon v3.0 was performed using Python 3.7.6 with NumPy version 1.18.0 and SciPy version 1.4.1.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [NumPy v1.18.0, PyMOL v2.2, Python v3.7.6, SciPy v1.4.1]

### Large-scale distributed linear algebra with tensor processing units. (PNAS 2022)

- DOI: 10.1073/pnas.2122762119 | PMCID: PMC9388123 | PMID: 35939669
- Evidence: We used JAX ( 19 ), a NumPy-like interface to XLA.
- Full pipeline: stage not stated [JAX, NumPy]

### A neural network solves, explains, and generates university math problems by program synthesis and few-shot learning at human level. (PNAS 2022)

- DOI: 10.1073/pnas.2123433119 | PMCID: PMC9371704 | PMID: 35917350
- Evidence: All courses use NumPy and Sympy.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Matplotlib, NumPy, Python, SciPy]

### Nonequilibrium statistical thermodynamics of multicomponent interfaces. (PNAS 2022)

- DOI: 10.1073/pnas.2121405119 | PMCID: PMC9214509 | PMID: 35675427
- Evidence: Analysis of the simulation data was performed using the Pandas ( 50 ), NumPy ( 51 ), SciPy ( 52 ), and CSAPS ( 53 ) Python packages.
- Full pipeline: simulation/modelling [NumPy, SciPy]

### A molecularly enhanced proof of concept for targeting cocrystals at molecular scale in continuous pharmaceuticals cocrystallization. (PNAS 2022)

- DOI: 10.1073/pnas.2114277119 | PMCID: PMC9173768 | PMID: 35594395
- Evidence: Therefore, we computed its Moore–Penrose pseudoinverse using a least-squares solver ( linalg.pinv in the NumPy package) ( 111 ).
- Full pipeline: stage not stated [NumPy]

### A male pheromone that improves the quality of the oogenic germline. (PNAS 2022)

- DOI: 10.1073/pnas.2015576119 | PMCID: PMC9173808 | PMID: 35576466
- Evidence: The hypergeometric P value and other calculations were carried out using SciPy ( 83 ) version 1.6.2 and NumPy ( 84 ) version 1.19.2.
- Full pipeline: quality control [MultiQC, Nextflow] -> differential/statistical testing [DESeq2 v1.32.0, NumPy, R v4.1, SciPy] -> stage not stated [Matplotlib, seaborn]

### Infrastructure inequality is a characteristic of urbanization. (PNAS 2022)

- DOI: 10.1073/pnas.2119890119 | PMCID: PMC9169802 | PMID: 35377809
- Evidence: We analyzed the data in R ( https://www.r-project.org/ ) using ggplot2, sf, rgdal, Hmisc, spdep, spatialreg, raster, tmap, and dplyr packages and in python ( https://www.python.org/ ) programming languages using numpy, scipy, pandas, geopandas, osgeo, scikit-image, matplotlib, and rasterio packages.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, scikit-image, tidyverse]

### A molecular switch controls the impact of cholesterol on a Kir channel. (PNAS 2022)

- DOI: 10.1073/pnas.2109431119 | PMCID: PMC9060494 | PMID: 35333652
- Evidence: The Matplotlib ( 87 ) and NumPy ( 88 ) libraries were used for plotting the results.
- Full pipeline: simulation/modelling [GROMACS v2016.3] -> visualisation [PyMOL] -> stage not stated [ImageJ, Matplotlib, NumPy, VMD v1.9.3]

### Contiguously hydrophobic sequences are functionally significant throughout the human exome. (PNAS 2022)

- DOI: 10.1073/pnas.2116267119 | PMCID: PMC8944643 | PMID: 35294280
- Evidence: All computations were done in Python 3.6 using the numpy ( 70 ), scipy ( 68 ), and pandas ( 71 ) packages.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [Matplotlib, NumPy, Python v3.6, SciPy]

### Label-free sensing of cells with fluorescence lifetime imaging: The quest for metabolic heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2118241119 | PMCID: PMC8892511 | PMID: 35217616
- Evidence: All simulation and data analysis were performed using custom-build Python 3.7 scripts with the use of Numpy, Scipy, Scikit-Learn Matplotlib, Pandas and LmFit modules.
- Full pipeline: simulation/modelling [Matplotlib, NumPy, Python v3.7, SciPy] -> stage not stated [scikit-learn]

### Network modeling predicts personalized gene expression and drug responses in valve myofibroblasts cultured with patient sera. (PNAS 2022)

- DOI: 10.1073/pnas.2117323119 | PMCID: PMC8872767 | PMID: 35181609
- Evidence: All network filtering steps were performed in a python environment using the numpy ( 60 ) and pandas ( 61 ) packages.
- Full pipeline: visualisation [Cytoscape] -> stage not stated [NumPy]

### <i>Mycobacterium tuberculosis</i> DNA repair helicase UvrD1 is activated by redox-dependent dimerization via a 2B domain cysteine. (PNAS 2022)

- DOI: 10.1073/pnas.2114501119 | PMCID: PMC8872793 | PMID: 35173050
- Evidence: Python 3 was installed via Anaconda along with modules such as numpy, scipy, matpotlib, lmfit, emcee, corner, os, and pandas, and then the globalfit model was used to fit the data for unwinding using the n-step unwinding model and translocation using a two-step dissociation model ( 64 ).
- Full pipeline: stage not stated [Conda, NumPy, Python, SciPy, emcee]

### A synergy between mechanosensitive calcium- and membrane-binding mediates tension-sensing by C2-like domains. (PNAS 2022)

- DOI: 10.1073/pnas.2112390119 | PMCID: PMC8740744 | PMID: 34969839
- Evidence: Specifically, custom Python 3.7 scripts were written based on the Numpy ( 36 ), Scipy ( 37 ), Scikit-image ( 38 ), Allen Cell Structure Segmenter ( 39 ), Cellpose ( 40 ) and Napari libraries ( 41 ).
- Full pipeline: stage not stated [Cellpose, Conda, NumPy, PyMOL, Python v3.7, SciPy]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Evidence: Numpy python library ( 87 ) was used for proper formatting of raw input data, psi values of AS events, into LSTM model input.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### Machine-guided discovery of a real-world rogue wave model. (PNAS 2023)

- DOI: 10.1073/pnas.2306275120 | PMCID: PMC10691345 | PMID: 37983488
- Evidence: This publication was made possible by the following opensource software stack: JAX ( 57 ), flax ( 58 ), optax ( 59 ), PySR ( 9 ), scikit-learn ( 63 ), PyALE ( 64 ), NumPy ( 65 ), SciPy ( 66 ), matplotlib ( 67 ), Seaborn ( 68 ), pandas ( 69 ), and Jupyter ( 70 ).
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, SciPy, scikit-learn, seaborn]

### Deciphering RNA splicing logic with interpretable machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2221165120 | PMCID: PMC10576025 | PMID: 37796983
- Version used: **1.20**
- Evidence: The model was implemented in Python 3.8 ( 48 ) using Tensorflow 2.6 ( 49 ) and Numpy 1.20 ( 50 ).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [NumPy v1.20, Python v3.8, TensorFlow v2.6]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **1.21.6**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### Gating of homeostatic regulation of intrinsic excitability produces cryptic long-term storage of prior perturbations. (PNAS 2023)

- DOI: 10.1073/pnas.2222016120 | PMCID: PMC10293857 | PMID: 37339223
- Evidence: The solutions were visualized and analyzed using standard Python libraries (numpy and matplotlib).
- Full pipeline: visualisation [Matplotlib, NumPy] -> stage not stated [Python]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Evidence: Volumetric segmentation and analysis were performed using the NumPy, ANTsPy , and NiBabel packages in Python (Python 3.7).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### Cortical activity emerges in region-specific patterns during early brain development. (PNAS 2023)

- DOI: 10.1073/pnas.2208654120 | PMCID: PMC10235933 | PMID: 37216522
- Evidence: Quantitative analysis was performed using custom code written in Python and using NumPy, SciPy, Scikit-learn, Pandas, NetworkX, Python-Louvain, Filterpy and Scikit-image.
- Full pipeline: quantification [ImageJ] -> normalisation [Python] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [Matplotlib] -> stage not stated [NetworkX, NumPy, SciPy]

### Single-shot time-folded fluorescence lifetime imaging. (PNAS 2023)

- DOI: 10.1073/pnas.2214617120 | PMCID: PMC10120087 | PMID: 37043531
- Evidence: Data, Materials, and Software Availability Raw images, synthetic training data (numpy arrays) for training a neural network, code required to process the data and produce the results in the paper, figures in svg and pdf formats.
- Full pipeline: machine learning [NumPy]

### Johari-Goldstein <i>β</i> relaxation in glassy dynamics originates from two-scale energy landscape. (PNAS 2023)

- DOI: 10.1073/pnas.2215153120 | PMCID: PMC10083593 | PMID: 36989301
- Evidence: The NumPy ( 73 ) and SciPy ( 71 ) packages are used to calculate the Pearson and Spearman correlations, respectively.
- Full pipeline: stage not stated [NumPy, SciPy]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Evidence: After initial fMRI preprocessing, additional steps to create the fMRI features for predictive models and reshape data were conducted using custom code in python 3.7.7 using the packages pandas ( 138 ) and numpy ( 139 ) and R 4.0.2 using the package collections tidyverse ( 140 ) and tidymodels ( 141 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### <i>Leishmania</i> allelic selection during experimental sand fly infection correlates with mutational signatures of oxidative DNA damage. (PNAS 2023)

- DOI: 10.1073/pnas.2220828120 | PMCID: PMC10013807 | PMID: 36848551
- Version used: **1.22.3**
- Evidence: Further SNP analyses were performed based on the filtered outputs of GIP using custom Python 3.10 code relying on the following libraries: Pandas (1.4.2) ( 24 ), Pysam (0.19.0) ( 25 ), Numpy (1.22.3) ( 26 ), Matplotlib (3.5.1) ( 27 ), Seaborn (0.11.2) ( 28 ), Biotite (0.32.0) ( 29 ), and Upsetplot (0.6.0) ( 30 ).
- Full pipeline: stage not stated [Matplotlib v3.5.1, NumPy v1.22.3, Python v3.10, seaborn v0.11.2]

### A critical analysis of plant science literature reveals ongoing inequities. (PNAS 2023)

- DOI: 10.1073/pnas.2217564120 | PMCID: PMC10013813 | PMID: 36853942
- Version used: **1.22.4**
- Evidence: We computed national summary stats, global patterns of author location, and associations with national development indicators using Python (v3.8.8) packages Pandas (v1.5.0) and Numpy (v1.22.4) and visualized data in Seaborn (v0.11.1) and Matplotlib (v3.6.1).
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.22.4, seaborn v0.11.1]

### Bayesian inference in ring attractor networks. (PNAS 2023)

- DOI: 10.1073/pnas.2210622120 | PMCID: PMC9992764 | PMID: 36812206
- Version used: **1.19.2**
- Evidence: For all our simulations, we used Python 3.9.1 with NumPy 1.19.2.
- Full pipeline: simulation/modelling [NumPy v1.19.2, Python v3.9.1]

### Nematic phases and elastoresistivity from a multiorbital non-Fermi liquid. (PNAS 2023)

- DOI: 10.1073/pnas.2207903120 | PMCID: PMC9926168 | PMID: 36603030
- Evidence: The numerical calculations were performed in Julia and Python using the NumPy library.
- Full pipeline: stage not stated [NumPy]

### Nutrient colimitation is a quantitative, dynamic property of microbial populations. (PNAS 2024)

- DOI: 10.1073/pnas.2400304121 | PMCID: PMC11670248 | PMID: 39693349
- Evidence: We performed all numerical calculations in Python version 3.10.9, using tools from NumPy ( 76 ) version 1.24.1 and SciPy ( 77 ) version 1.10.0.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python v3.10.9, SciPy]

### Diversification of pectoral control through motor pool extension. (PNAS 2024)

- DOI: 10.1073/pnas.2413415121 | PMCID: PMC11626184 | PMID: 39602261
- Evidence: 3.8, Python Software Foundation, www.python.org ), building on the NumPy [v.1.18.5, ( 42 )], matplotlib [v.3.2.2, ( 43 )], pandas [v.2.2.1, ( 44 )] and seaborn [0.12.2, ( 45 )] libraries were used.
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [SciPy] -> stage not stated [Matplotlib, NumPy, Python, seaborn]

### Bioenergetic suppression by redox-active metabolites promotes antibiotic tolerance in &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406555121 | PMCID: PMC11573671 | PMID: 39503891
- Version used: **1.24.3**
- Evidence: Data were analyzed and processed in Python 3.8.17 using Pandas 2.0.3, NumPy 1.24.3, and SciPy 1.9.3.
- Full pipeline: stage not stated [ImageJ v1.52, NumPy v1.24.3, Python v3.8.17, SciPy v1.9.3]

### Atomic view of photosynthetic metabolite permeability pathways and confinement in synthetic carboxysome shells. (PNAS 2024)

- DOI: 10.1073/pnas.2402277121 | PMCID: PMC11551347 | PMID: 39485798
- Evidence: Particle tracking and analysis was performed with python-enabled VMD ( 70 ), extensively using numpy ( 74 ), scipy ( 75 ), and Matplotlib ( 76 ) libraries.
- Full pipeline: simulation/modelling [GROMACS, NAMD v2.14, VMD] -> stage not stated [Matplotlib, NumPy, SciPy]

### AlphaFold-Multimer accurately captures interactions and dynamics of intrinsically disordered protein regions. (PNAS 2024)

- DOI: 10.1073/pnas.2406407121 | PMCID: PMC11536093 | PMID: 39446390
- Evidence: We extensively used BioPython, NumPy, SciPy, pandas, Matplotlib, and seaborn ( 57 – 62 ) to develop the code and plot the figures for this work.
- Full pipeline: machine learning [AlphaFold] -> visualisation [PyMOL] -> stage not stated [ColabFold, Matplotlib, NumPy, RoseTTAFold, SciPy, seaborn]

### Blobs form during the single-file transport of proteins across nanopores. (PNAS 2024)

- DOI: 10.1073/pnas.2405018121 | PMCID: PMC11420176 | PMID: 39264741
- Evidence: The global minimum and maximum of these profiles were computed using numpy ( 47 ) and plotted along with the profiles using matplotlib ( 48 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [Matplotlib, NumPy] -> stage not stated [ChimeraX, MDAnalysis, PyMOL]

### People who share encounters with racism are silenced online by humans and machines, but a guideline-reframing intervention holds promise. (PNAS 2024)

- DOI: 10.1073/pnas.2322764121 | PMCID: PMC11420153 | PMID: 39250662
- Evidence: We fitted a logistic regression model, using standard Python libraries numpy and statsmodels ( 87 , 88 ).
- Full pipeline: differential/statistical testing [NumPy, statsmodels]

### Deep learning models map rapid plant species changes from citizen science and remote sensing data. (PNAS 2024)

- DOI: 10.1073/pnas.2318296121 | PMCID: PMC11406280 | PMID: 39236239
- Evidence: ...California using a minimum 0.98 accuracy threshold and 10 test set observations to choose species to display, or species were randomly selected using numpy’s random.choice function and a random seed of 1 ( SI Appendix , SM 4.1 and Figs.
- Full pipeline: machine learning [PyTorch] -> stage not stated [NumPy, R]

### MICU1 and MICU2 control mitochondrial calcium signaling in the mammalian heart. (PNAS 2024)

- DOI: 10.1073/pnas.2402491121 | PMCID: PMC11363308 | PMID: 39163336
- Version used: **1.21.5**
- Evidence: Individual cells were masked and mean gray values were exported and further processed in Excel, Visual Studio Code 1.76.2 (using Python 3.9.12, Numpy 1.21.5, Matplotlib 3.5.1, Statsmodels 0.13.2, Pandas 1.4.2), SigmaPlot 12.5, and GraphPad Prism 9.3.0.
- Full pipeline: stage not stated [Matplotlib v3.5.1, NumPy v1.21.5, Python v3.9.12]

### Layer-by-layer unsupervised clustering of statistically relevant fluctuations in noisy time-series data of complex dynamical systems. (PNAS 2024)

- DOI: 10.1073/pnas.2403771121 | PMCID: PMC11331080 | PMID: 39110730
- Evidence: The cumulative histogram H j of all the data is computed, with 0 ≤ j < n bins . n bins is set automatically by Numpy ( 65 ), but can be also set to a custom value.
- Full pipeline: stage not stated [NumPy]

### An ankyrin G-binding motif mediates TRAAK periodic localization at axon initial segments of hippocampal pyramidal neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2310120121 | PMCID: PMC11295008 | PMID: 39058579
- Evidence: Finally, correlation analysis was performed using the numpy.correlate function.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Python v3.9] -> stage not stated [AlphaFold, ImageJ, NumPy, napari]

### Upstream surface roughness and terrain are strong drivers of contrast in tornado potential between North and South America. (PNAS 2024)

- DOI: 10.1073/pnas.2315425121 | PMCID: PMC11214001 | PMID: 38889148
- Evidence: Supplementary Material Appendix 01 (PDF) Acknowledgments We acknowledge NCAR CISL Cheyenne (DOI: 10.5065/D6RX99HX ) and Purdue RCAC for research computing time and infrastructure and developers of Python software packages including numpy, matplotlib, metpy, and xcape.
- Full pipeline: simulation/modelling [CESM v2.1.1] -> stage not stated [Matplotlib, NumPy]

### Measuring and modeling the dynamics of mitotic error correction. (PNAS 2024)

- DOI: 10.1073/pnas.2323009121 | PMCID: PMC11194551 | PMID: 38875144
- Evidence: We used the resulting covariance matrix to estimate the propagated parameter fit errors and 2 σ CI (shaded region of plot) using Numpy’s uncertainty module.
- Full pipeline: stage not stated [NumPy, Python, SciPy]

### Information content and optimization of self-organized developmental systems. (PNAS 2024)

- DOI: 10.1073/pnas.2322326121 | PMCID: PMC11161761 | PMID: 38819997
- Evidence: Throughout all three examples, the stochastic pattern formation dynamics are simulated using custom-written python code using numpy ( 88 ).
- Full pipeline: differential/statistical testing [SciPy] -> simulation/modelling [NumPy]

### Optimal reaching subject to computational and physical constraints reveals structure of the sensorimotor control system. (PNAS 2024)

- DOI: 10.1073/pnas.2319313121 | PMCID: PMC10998569 | PMID: 38551834
- Evidence: The system of differential equations comprising the equations of motion, neural and muscle dynamics, and adjoint equations was coded in python using the NumPy and SciPy numerical libraries and integrated using an adaptive fifth order Runge–Kutta method ( 41 , 42 ).
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> machine learning [PyTorch]

### Unraveling sources of emission heterogeneity in Silicon Vacancy color centers with cryo-cathodoluminescence microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2308247121 | PMCID: PMC10998621 | PMID: 38551833
- Evidence: Data analysis was performed in Python, utilizing multiple common packages, such as numpy, scipy, and matplotlib.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python, SciPy]

### Subcallosal cingulate deep brain stimulation evokes two distinct cortical responses via differential white matter activation. (PNAS 2024)

- DOI: 10.1073/pnas.2314918121 | PMCID: PMC10998591 | PMID: 38527192
- Version used: **1.24.4**
- Evidence: The source analysis was performed in python 3.11.5 using the following packages: mne 1.5.1, numpy 1.24.4, matplotlib 3.8.0, scipy 1.11.2, pandas 2.1.1, and seaborn 0.12.2 ( 57 – 62 ).
- Full pipeline: stage not stated [AFNI, Camino, FSL, Matplotlib v3.8.0, NumPy v1.24.4, SciPy v1.11.2, seaborn v0.12.2]

### The training process of many deep networks explores the same low-dimensional manifold. (PNAS 2024)

- DOI: 10.1073/pnas.2310002121 | PMCID: PMC10962999 | PMID: 38470929
- Evidence: We reduced the severity of this issue using Numpy’s memmap functionality.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [NumPy]

### Machine learning to predict continuous protein properties from binary cell sorting data and map unseen sequence space. (PNAS 2024)

- DOI: 10.1073/pnas.2311726121 | PMCID: PMC10945751 | PMID: 38451939
- Evidence: Pandas ( https://pandas.pydata.org/ ) and NumPy ( https://numpy.org/ ) were used to handle sequencing and numerical data.
- Full pipeline: normalisation [scikit-learn] -> machine learning [PyTorch] -> stage not stated [MACS2, NumPy]

### Toward the quantification of α-synuclein aggregates with digital seed amplification assays. (PNAS 2024)

- DOI: 10.1073/pnas.2312031121 | PMCID: PMC10801878 | PMID: 38194461
- Version used: **1.23**
- Evidence: Image processing and data analysis were performed using an automated custom Python (3.10) code and the scikit-image (0.19), numpy (1.23), and pandas (1.4) packages.
- Full pipeline: stage not stated [ImageJ, NumPy v1.23, scikit-image v0.19]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Version used: **1.16.3**
- Evidence: The following Python packages were utilized: Matplotlib (version 3.0.3), NumPy (version 1.16.3), Pandas (version 0.24.2), SciPy (version 1.2.1), and Seaborn (version 0.9.0).
- Full pipeline: quantification [CellProfiler] -> visualisation [Conda, Jupyter, Python v3.7.3] -> stage not stated [ImageJ, Matplotlib v3.0.3, NumPy v1.16.3, SciPy v1.2.1, seaborn v0.9.0]

### Engineered calcium-regulated affinity protein for efficient internalization and lysosomal toxin delivery. (PNAS 2025)

- DOI: 10.1073/pnas.2509081122 | PMCID: PMC12685030 | PMID: 41289384
- Evidence: Image processing was performed in Fiji for background subtraction and in Python (OpenCV, SciPy, NumPy, scikit-image) for analysis.
- Full pipeline: structure determination [ChimeraX v1.9, PHENIX v1.21.2] -> visualisation [ChimeraX v1.9, PHENIX v1.21.2] -> stage not stated [AlphaFold, NumPy, OpenCV, Python, SciPy, scikit-image]

### A steady-state pool of calcium-dependent actin is maintained by Homer and controls epithelial mechanosensation. (PNAS 2025)

- DOI: 10.1073/pnas.2509784122 | PMCID: PMC12582288 | PMID: 41134626
- Evidence: The following python packages were used: numpy, pandas, statsmodels, and scipy for organizing, sorting, and processing (normalization, smoothing, peak/trough finding) to automatically determine analysis windows based on displacement and extract data for various parameters; statsmodels for OLS analysis; matplotlib and seaborn for presentation.
- Full pipeline: quantification [napari] -> normalisation [Matplotlib, NumPy, SciPy, seaborn, statsmodels] -> differential/statistical testing [R] -> stage not stated [ImageJ, scikit-image]

### On the scale of heterogeneity in composite electrodes of batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2520136122 | PMCID: PMC12582338 | PMID: 41129219
- Evidence: All computations and visualizations are made using various libraries in python (e.g. numpy, scipy, matplotlib, etc.) Finite Element Modeling.
- Full pipeline: alignment/mapping [scikit-image] -> dimensionality reduction/clustering [SciPy] -> structure determination [scikit-image] -> visualisation [Matplotlib, NumPy] -> stage not stated [OpenCV, Python]

### Foot placement control underlies stable locomotion across species. (PNAS 2025)

- DOI: 10.1073/pnas.2413958122 | PMCID: PMC12582247 | PMID: 41118219
- Evidence: All the statistics were performed using Python3 ( numpy , scipy , and scikit_posthoc ).
- Full pipeline: differential/statistical testing [NumPy, Python, SciPy]

### Dynamic sensor selection for biomarker discovery. (PNAS 2025)

- DOI: 10.1073/pnas.2501324122 | PMCID: PMC12541339 | PMID: 41055977
- Evidence: These optimizations can be implemented with standard functions including numpy.linalg.svd, numpy.linalg.eig, and the corresponding MATLAB commands.
- Full pipeline: stage not stated [NumPy, Python]

### Generalized convolutional many-body distribution functional representations. (PNAS 2025)

- DOI: 10.1073/pnas.2415662122 | PMCID: PMC12541311 | PMID: 41052323
- Evidence: It relies on the Numpy ( 51 ), Scipy ( 52 ) and Numba ( 53 ) Python libraries.
- Full pipeline: stage not stated [NumPy, PySCF, Python, SciPy, XGBoost]

### Φ value analysis underscores strong functional and structural compactness of the GABA&lt;sub&gt;A&lt;/sub&gt; receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2512278122 | PMCID: PMC12478134 | PMID: 40956892
- Evidence: All statistical analyses were performed using Python scripts with the Pandas, Numpy, and Scipy packages.
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> visualisation [ChimeraX] -> stage not stated [Python]

### Characterizing population-level changes in human behavior during the COVID-19 pandemic in the United States. (PNAS 2025)

- DOI: 10.1073/pnas.2500655122 | PMCID: PMC12452891 | PMID: 40932771
- Evidence: Analysis used Python’s numpy corrcoef function ( 83 ).
- Full pipeline: stage not stated [NumPy]

### STIM1 transmembrane helix dimerization captured by AI-guided transition path sampling. (PNAS 2025)

- DOI: 10.1073/pnas.2506516122 | PMCID: PMC12415195 | PMID: 40857319
- Evidence: Trajectory analysis was carried out using the pytraj ( 96 ), mdtraj ( 97 ), MDAnalysis ( 98 , 99 ), numpy ( 100 ), and SciPy ( 101 ) packages.
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [GROMACS v2020.6, MDAnalysis, MDTraj, NumPy, SciPy] -> machine learning [PyTorch]

### PyReconstruct: A fully open-source, collaborative successor to Reconstruct. (PNAS 2025)

- DOI: 10.1073/pnas.2505822122 | PMCID: PMC12337286 | PMID: 40737319
- Evidence: 2D contours are voxelized and represented as NumPy arrays, which are translated through a matrix-to-marching-cubes algorithm provided by the trimesh library ( 58 ) to generate watertight triangle meshes for visualization and quantification ( Fig.
- Full pipeline: quantification [NumPy] -> structure determination [Python] -> visualisation [NumPy]

### A genetically defined pontine nucleus essential for ingestion in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2411174122 | PMCID: PMC12305073 | PMID: 40663610
- Evidence: The isosbestic line was then adjusted to the baseline signal by estimating an offset and a scale using a linear regression (using Numpy’s polyfit function) of the isosbestic control signal and calcium-dependent signal taken at the time of the local minima.
- Full pipeline: differential/statistical testing [NumPy] -> machine learning [DeepLabCut v2.3.8] -> stage not stated [Fiji, ImageJ, Python, SciPy]

### Learning predictive signals within a local recurrent circuit. (PNAS 2025)

- DOI: 10.1073/pnas.2414674122 | PMCID: PMC12260394 | PMID: 40591603
- Version used: **1.17.3**
- Evidence: All simulations were performed in customized Python3 code written by TA with numpy 1.17.3 and scipy 0.18.
- Full pipeline: simulation/modelling [NumPy v1.17.3, SciPy v0.18]

### Spatially resolved DNP-assisted NMR illuminates the conformational ensemble of α-synuclein in intact viable cells. (PNAS 2025)

- DOI: 10.1073/pnas.2500367122 | PMCID: PMC12168001 | PMID: 40465629
- Evidence: The coefficients of the linear regressions were used to weight the monomer and nanodisc-bound data, and a numpy trapezoidal approximation of the integral (trapz) was calculated to determine the relative populations of α-helical and intrinsically disordered α-syn.
- Full pipeline: differential/statistical testing [NumPy, statsmodels]

### Detection of the knee point in lithium-ion battery degradation using a state-of-charge-dependent parameter. (PNAS 2025)

- DOI: 10.1073/pnas.2424838122 | PMCID: PMC12167950 | PMID: 40460124
- Evidence: Data processing and machine-learning-based model construction were performed in Python with the Pandas, NumPy, and Scikit-learn packages.
- Full pipeline: stage not stated [NumPy, Python, scikit-learn]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Version used: **1.26**
- Evidence: All postprocessing calculations and data analyses were done with GROMACS internal tools, Python 3.9 ( 95 ), Numpy v1.26 ( 96 ), and SciPy v1.11 ( 97 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Bispecific antibodies against the hepatitis C virus E1E2 envelope glycoprotein. (PNAS 2025)

- DOI: 10.1073/pnas.2420402122 | PMCID: PMC12012487 | PMID: 40193609
- Evidence: Calibrated events were exported and processed by an in-house developed Python pipeline ( 86 ) using NumPy ( 87 ), pandas ( 88 ), Matplotlib ( 89 ), SciPy ( 90 ), and seaborn ( 91 ).
- Full pipeline: visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, Matplotlib, NumPy, SciPy, seaborn]

### An unusual potassium conductance protects &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; pharyngeal muscle rhythms against environmental noise. (PNAS 2025)

- DOI: 10.1073/pnas.2422709122 | PMCID: PMC12002347 | PMID: 40178897
- Evidence: ...e in the current balance equation during simulation at the arrival times sampled from the Poisson distribution using the Poisson function in Python’s NumPy package.
- Full pipeline: simulation/modelling [NumPy, Python]

### Linear Recursive Feature Machines provably recover low-rank matrices. (PNAS 2025)

- DOI: 10.1073/pnas.2411325122 | PMCID: PMC12002225 | PMID: 40153460
- Evidence: For training lin-RFM, we used linear system solvers from NumPy ( 53 ).
- Full pipeline: machine learning [NumPy] -> stage not stated [PyTorch]

### A solvable model for strongly interacting nonequilibrium excitons. (PNAS 2025)

- DOI: 10.1073/pnas.2424663122 | PMCID: PMC11929435 | PMID: 40085654
- Evidence: We diagonalize H 0 using built-in numpy routines and then compute B α , β , N B using Eq.
- Full pipeline: stage not stated [NumPy, Python, SciPy]

### Spatial profiling of the interplay between cell type- and vision-dependent transcriptomic programs in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421022122 | PMCID: PMC11848306 | PMID: 39946537
- Evidence: Using these Slc6a13+ cells as anchors, we first fit a fourth-order polynomial using numpy.polyfit .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [Enrichr, NumPy, SciPy, scikit-learn, seaborn]

### Codon bias, nucleotide selection, and genome size predict in situ bacterial growth rate and transcription in rewetted soil. (PNAS 2025)

- DOI: 10.1073/pnas.2413032122 | PMCID: PMC11761963 | PMID: 39805015
- Evidence: Genomic traits were calculated using custom scripts written in Python (v 3.8.2)—using the packages pandas ( 76 ) and NumPy ( 77 ); they can be found at https://github.com/PChuckran/Wet_up_traits .
- Full pipeline: alignment/mapping [DESeq2, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [R v4.2.1, ggplot2, tidyverse] -> visualisation [R v4.2.1, ggplot2, tidyverse] -> stage not stated [NumPy, Python v3.8.2]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: MA plots were generated in Python with Matplotlib, pandas, and NumPy.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### Egress thresholds and wildfire fatalities. (PNAS 2026)

- DOI: 10.1073/pnas.2535081123 | PMCID: PMC13250580 | PMID: 42224582
- Evidence: Python analyses relied on the following packages: geopandas, pandas, osmnx, networkx, numpy, matplotlib, rasterio, rasterstats, shapely, tqdm, tenacity, requests, concurrent.futures, multiprocessing, zipfile, io, logging, glob, json, csv, ast, signal, functools, and mpl_toolkits.
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, R v4.4.0, ggplot2, ggpubr, tidyverse]

### Damselflies overcome color saturation barriers of photonic glasses via pigment loading and refractive index modulation. (PNAS 2026)

- DOI: 10.1073/pnas.2527433123 | PMCID: PMC13250596 | PMID: 42213815
- Evidence: All calculations were performed using a custom Python script (Python 3.11, NumPy, SciPy, Matplotlib, and Pandas libraries).
- Full pipeline: stage not stated [ImageJ, Matplotlib, NumPy, Python v3.11, SciPy]

### Meiosis-specific genes play roles in ploidy reduction in &lt;i&gt;Cryptococcus neoformans&lt;/i&gt; titan cells. (PNAS 2026)

- DOI: 10.1073/pnas.2522069123 | PMCID: PMC13215162 | PMID: 42189998
- Version used: **1.21.6**
- Evidence: Data visualization and further analysis were performed using matplotlib (v3.5.3) ( 70 ), seaborn (v0.12.2) ( 71 ), and numpy (v1.21.6) ( 72 ), with candidate chimeric reads and breakpoint loci summarized in output tables and plots.
- Full pipeline: alignment/mapping [SAMtools v1.18] -> visualisation [Matplotlib v3.5.3, NumPy v1.21.6, seaborn v0.12.2]

### Geometric ordering in bacterial communities. (PNAS 2026)

- DOI: 10.1073/pnas.2526643123 | PMCID: PMC13187718 | PMID: 42118839
- Evidence: A regular 3D grid was created using numpy.meshgrid in NumPy ( 76 ) (v1.24.3, available at: https://numpy.org ) and a set of seeding points representing colony centers was defined. scipy.spatial.KDTree (SciPy) was used to assign each grid point to its nearest seed, effectively partitioning the 3D space into Voronoi regions.
- Full pipeline: simulation/modelling [Python] -> visualisation [Matplotlib v3.7.1, SciPy] -> stage not stated [ImageJ v1.54d, NumPy]

### Reconstruction of human metabolic models with large language models. (PNAS 2026)

- DOI: 10.1073/pnas.2516511123 | PMCID: PMC13079975 | PMID: 41950094
- Version used: **1.21.5**
- Evidence: The analysis and visualization were facilitated by Python 3.7.16, SHAP 0.41.0, scikit-learn 1.0.2, pandas 1.1.3, SciPy 1.7.3, NumPy 1.21.5, and Matplotlib 3.4.3 packages.
- Full pipeline: visualisation [Matplotlib v3.4.3, NumPy v1.21.5, Python v3.7.16, SciPy v1.7.3, scikit-learn v1.0.2]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: It was implemented in Python, utilizing OpenCV, PIL, Tkinter/CustomTkinter, Matplotlib, NumPy, and Pandas for image processing, visualization, and data management, and with aicspylibczi for handling czi files.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Evidence: The simulation was implemented in Python using standard scientific computing libraries, including NumPy and Matplotlib, with additional functionality from Biopython for lineage tree construction.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

### Structural characterization of the HDV virion and its ribonucleoprotein. (PNAS 2026)

- DOI: 10.1073/pnas.2519809123 | PMCID: PMC12846810 | PMID: 41564123
- Evidence: Curves and bar graphs were made using Python with Matplotlib ( 59 ), Pandas ( 60 ), Numpy ( 61 ), and Scipy ( 62 ).
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX, Coot, Matplotlib, NumPy, SciPy, Topaz, UCSF Chimera]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **1.18.3**
- Evidence: Software The following Python (version 3.8.2) software packages were used in the data analysis and in the production of figures: Scipy (version 1.4.1) ( 78 ), pandas (version 1.0.3) ( 79 ), statsmodels (version 0.11.1) ( 80 ), matplotlib (version 3.2.1) ( 81 ), numpy (1.18.3) ( 82 ), seaborn_sinaplot ( 83 ), simanneal (version 0.5.0) ( 71 ), and seaborn (version 0.10.1) ( 84 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### The connectome of an insect brain. (Science 2023)

- DOI: 10.1126/science.add9330 | PMCID: PMC7614541 | PMID: 36893230
- Evidence: Code Analyses relied on NumPy ( 125 ), SciPy ( 126 ), Pandas ( 127 ), NetworkX ( 128 ), navis ( 124 ), and pythoncatmaid ( https://pypi.org/project/python-catmaid/ ).
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, SciPy, seaborn]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **1.24.3**
- Evidence: ChIP-seq signal box plots were generated with Python (v3.11.5) ( 120 ), using Pandas (v2.0.3), Matplotlib (v3.7.2), Seaborn (0.12.2), SciPy (1.11.1) and NumPy (v1.24.3) libraries, starting from deep-Tools computeMatrix output values, summing H2A.Z/H2A.Zac ChIP-seq signal across each peak coordinate, dividing it by the input signal and plotting the resulting ratios.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Version used: **1.26.3**
- Evidence: Filtered, sorted, and indexed bam output files were used for methylation visualization (see below) or further processed using modkit tools (ONT, https://github.com/nanoporetech/modkit ) and custom python scripts implementing Numpy v.1.26.3, Pandas v.2.2.0, and Seaborn v.0.13.2 for Pearson correlation and average methylation plots.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Vaccination with mRNA-encoded nanoparticles drives early maturation of HIV bnAb precursors in humans. (Science 2025)

- DOI: 10.1126/science.adr8382 | PMCID: PMC13164876 | PMID: 40373112
- Evidence: 5 E and F , the nearest method ( 97 ) implemented in NumPy ( https://numpy.org/doc/stable/reference/generated/numpy.quantile.html ) was used; similar results were obtained using the midpoint and median-unbiased methods.
- Full pipeline: differential/statistical testing [Matplotlib, seaborn] -> structure determination [AlphaFold, ChimeraX, Coot v0.9.8, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [NumPy]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: ....butter, with scipy.signal.sosfiltfilt), then taking the angle of the filtered signal’s Hilbert transform (using `angle` and `Hilbert` functions from NumPy ( 79 ) and SciPy).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: The Adam optimizer (learning rate 0.001) is used with deterministic behavior enforced by fixing Python, Numpy, TensorFlow and random-seed states.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: To evaluate model performance, we evaluated correlation of model estimated age with true age for all ages of held-out fish using Pearson correlation with numpy.corrcoef ( Fig.
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries as described before ( 49 , 52 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

