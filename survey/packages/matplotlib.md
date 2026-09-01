# Matplotlib

- **Category:** general
- **Papers in survey:** 240
- **Journals:** Nature (128), PNAS (85), Cell (19), Science (8)
- **Years:** 2021 (19), 2022 (30), 2023 (41), 2024 (52), 2025 (61), 2026 (37)
- **Versions named:** 3.7.1 (8), 3.5.2 (6), 3.5.1 (6), 3.3.2 (5), 3.4.3 (5), 3.2.1 (5), 3.7.2 (4), 3.4.2 (4), 3.8.2 (3), 3.8.0 (3)
- **Pipeline stages it appears in:** visualisation (97), differential/statistical testing (12), dimensionality reduction/clustering (11), normalisation (6), alignment/mapping (5), simulation/modelling (4), quantification (4), machine learning (3), quality control (2), registration (1), read trimming (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **3.3.3**
- Evidence: ...cipy version 1.5.2 Virtanen et al., 2020 https://scipy.org/ Python package numpy version 1.20.3 Harris et al., 2020 https://numpy.org/ Python package matplotlib version 3.3.3 Hunter, 2007 https://matplotlib.org/ Other QExactive HF-x Orbitrap MS Thermo Fisher Scientific IQLAAEGAAPFALGMBFZ Waters XBridge Peptide BEH C18 (130A, 3.5μm; 2.1mm x 250mm) Waters 186003566 Bravo Automated Liquid Handling Pl...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Identification of a therapeutic interfering particle-A single-dose SARS-CoV-2 antiviral intervention with a high barrier to resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.004 | PMCID: PMC8577993 | PMID: 34838159
- Version used: **3.3.3**
- Evidence: Data tabulation and visualizations were done with Pandas (v1.1.4), Seaborn (v0.11.0) and Matplotlib (v3.3.3).
- Full pipeline: quantification [DESeq2, featureCounts] -> simulation/modelling [Python] -> visualisation [Matplotlib v3.3.3, seaborn v0.11.0] -> stage not stated [ImageJ, NumPy v1.19.4, SciPy v1.5.4]

### Microbial exposure during early human development primes fetal immune cells. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.039 | PMCID: PMC8240556 | PMID: 34077752
- Version used: **3.2.1**
- Evidence: ...ages/vegan/index.html Python 2.7.0 Python Software Foundation https://www.python.org/ Python 3.7.0 Python Software Foundation https://www.python.org/ matplotlib 3.2.1 PyPI https://pypi.org/ numpy 1.19.4 PyPI https://pypi.org/ pandas 0.25.3 PyPI https://pypi.org/ seaborn 0.9.0 PyPI https://pypi.org/ Resource availability Lead contact Further information and requests for resources and reagents shoul...
- Full pipeline: alignment/mapping [pandas] -> dimensionality reduction/clustering [QIIME 2 v1.8.0, R v4.4, UMAP] -> stage not stated [ImageJ, Matplotlib v3.2.1, NumPy v1.19.4, Python v2.7.0, seaborn v0.9.0]

### Rigidity percolation uncovers a structural basis for embryonic tissue phase transitions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.017 | PMCID: PMC8055543 | PMID: 33730596
- Evidence: By using the multi-point tool in Fiji, the coordinates of each nuclei and their contacting-neighbors were marked and plotted using standard python package matplotlib.
- Full pipeline: visualisation [Matplotlib]

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Evidence: Comparison analysis were performed in Python using NumPy ( https://numpy.org/ ) and, Pandas ( https://pandas.pydata.org/ ) while figures were produced using the Matplotlib tool ( https://matplotlib.org/ ) and Seaborn ( https://seaborn.pydata.org/ ).
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### Accurate de novo design of membrane-traversing macrocycles. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.019 | PMCID: PMC9490236 | PMID: 36041435
- Evidence: ... (IV, PO, SQ) Images and Figures The hydrogen bonding and structure prediction data was plotted using python scripts using pandas ( McKinney, 2010 ), matplotlib ( Hunter, 2007 ) and seaborn ( Waskom, 2021 ) libraries.
- Full pipeline: dimensionality reduction/clustering [PyMOL] -> visualisation [Matplotlib, PyMOL, seaborn] -> stage not stated [CCP4]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **3.3.4**
- Evidence: Data was prepared and visualized using numpy (1.19.2), matplotlib (3.3.4), and pandas (1.2.4).
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.018 | PMCID: PMC8786601 | PMID: 35148837
- Version used: **3.3.2**
- Evidence: Plots were created with Python packages matplotlib version 3.3.2 and seaborn version 0.11.2.
- Full pipeline: dimensionality reduction/clustering [NumPy v1.19.1, scikit-learn v1.0] -> visualisation [SciPy v1.6.2] -> stage not stated [Matplotlib v3.3.2, QuPath v0.2.3, R v4.0.5, ggplot2, seaborn v0.11.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...validation Limma ( Ritchie et al., 2015 ) https://bioconductor.org/packages/release/bioc/html/limma.html MATLAB https://uk.mathworks.com/help/matlab/ Matplotlib ( Hunter, 2007 ) https://matplotlib.org/ MSFragger ( Kong et al., 2017 ) v3.0 MSigDB ( Subramanian et al., 2005 ) https://www.gsea-msigdb.org/gsea/msigdb/index.jsp Pandas v1.2.4 https://pandas.pydata.org/ Pegasus ( Li et al., 2020 ) https:...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Data visualization and plots were generated in R with ggplot and pheatmap packages, in GraphPad Prism, and in Python using the scikitimage, matplotlib, and seaborn packages.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Transmission from vaccinated individuals in a large SARS-CoV-2 Delta variant outbreak. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.027 | PMCID: PMC8695126 | PMID: 35051367
- Evidence: Each of these introductions, with the resulting cluster, was extracted from the ML tree and visualized using matplotlib.
- Full pipeline: dimensionality reduction/clustering [Matplotlib] -> differential/statistical testing [SciPy] -> visualisation [Matplotlib] -> stage not stated [Nextstrain v3.0.3, R]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: Data were plotted using the matplotlib and seaborn package in Python.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **3.7.1**
- Evidence: ..., gridExtra v.2.3, cowplot v.1.1.1, scales v.1.1.1, grid v.3.6.3, broom v.0.7.6, e1071 v.1.7.6, and table1 v.1.4 Python packages N/A biopython v1.79, matplotlib v3.7.1, numpy v1.22.3, pandas v1.5.1, scikit-bio v0.5.8, scipy v1.9.3, seaborn v0.11.2, statannot v0.2.3, and statsmodels v0.13.2 Other Leica Reichert Ultracut-S microtome Leica N/A JEOL 1200EX Transmission electron microscope JEOL USA N/A...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Synthetic protein circuits for programmable control of mammalian cell death. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.031 | PMCID: PMC11127782 | PMID: 38657604
- Evidence: To generate data visualizations, we used ImageJ, 108 Excel (Microsoft), the built-in layout editor in FlowJo (version 10.4, BD Biosciences), GraphPad Prism (version 9, Dotmatics), and Matplotlib (Python).
- Full pipeline: visualisation [ImageJ, Matplotlib, PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.2, Jupyter]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Evidence: All spectrograms were plotted using the matplotlib.pyplot.contourf function.
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: Quality control and cell filtering For all downstream analysis, we used the Scanpy package (referred to as sc from here on 54 , in Python 184 , 202 in addition to standard Python libraries such as numpy, pandas, matplotlib, csv, os, datetime 186 – 188 .
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### Inner speech in motor cortex and implications for speech neuroprostheses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.015 | PMCID: PMC12360486 | PMID: 40816265
- Version used: **3.8.2**
- Evidence: ...:SCR_008058 NumPy 1.26.2 numpy.org RRID:SCR_008633 Pandas 2.1.3 pandas.pydata.org RRID:SCR_018214 scikit-learn 1.3.2 scikit-learn.org RRID:SCR_002577 matplotlib 3.8.2 matplotlib.org RRID:SCR_008624 seaborn 0.13.0 seaborn.pydata.org RRID:SCR_018132 AWS Polly aws-cli/2.22.29 Amazon Web Services aws.amazon.com RRID:SCR_012854 Custom analysis code Repository provided upon acceptance.
- Full pipeline: stage not stated [Matplotlib v3.8.2, NumPy v1.26.2, Python v3.9, SciPy v1.11.4, scikit-learn v1.3.2, seaborn v0.13.0]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: Software packages All data analyses were performed using custom code written in Python 3 using standard analysis and plotting libraries: numpy, scipy, scikit-learn, matplotlib and seaborn.
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **3.10**
- Evidence: 201 https://bioconductor.org/packages/release/bioc/html/limma.html matplotlib (v3.10) Hunter et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### Cortical responses to touch reflect subcortical integration of LTMR signals. (Nature 2021)

- DOI: 10.1038/s41586-021-04094-x | PMCID: PMC9289451 | PMID: 34789880
- Version used: **3.3.1**
- Evidence: Data Analysis and Statistics Data were analyzed in Matlab (versions 2017a and 2017b) and python (version 3.7.7) using the following packages (versions in parentheses): conda (4.8.5), matplotlib (3.3.1), numpy (1.18.5), pims (0.5), pyabf (2.2.6), scipy (1.5.2), scikit-image (0.16.2), scikit-learn (0.23.2), and seaborn (0.11.0).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Matplotlib v3.3.1, NumPy v1.18.5, SciPy v1.5.2, scikit-image v0.16.2, seaborn v0.11.0]

### The cellular environment shapes the nuclear pore complex architecture. (Nature 2021)

- DOI: 10.1038/s41586-021-03985-3 | PMCID: PMC8550940 | PMID: 34646014
- Evidence: This workflow was performed using a Python script running SciPy.Stats (for P value and Z -score analysis) 51 , the StatsModels module (for Benjamini–Hochberg analysis) 52 and Matplotlib (for plots) 53 .
- Full pipeline: alignment/mapping [IMOD] -> differential/statistical testing [Matplotlib, Python, SciPy] -> stage not stated [RELION, UCSF Chimera]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Version used: **3.0.3**
- Evidence: Software versions Software versions used were: Anndata 0.7.1 , bustools 0.39.4 , awk (GNU awk) 4.1.4 , grep (GNU grep) 3.1 , kallisto 0.46.1 , kb_python 0.24.4 , Matplotlib 3.0.3 , Numpy 1.18.1 , Pandas 0.25.3 , Scanpy 1.4.5.post3 , Scipy 1.4.1 , sed (GNU sed) 4.4 , sklearn 0.22.1 , statsmodels 0.12.1 , tar (GNU tar) 1.29 , umap 0.3.10.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: Data analysis and visualization for M. smithii tip dating were performed using the Python libraries pandas, NumPy and Matplotlib.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Functional refolding of the penetration protein on a non-enveloped virus. (Nature 2021)

- DOI: 10.1038/s41586-020-03124-4 | PMCID: PMC8297411 | PMID: 33442061
- Evidence: Figure preparation We prepared the figures with PyMOL (The PyMOL Molecular Graphics System, Version 2.1 Schrödinger, LLC), POV-Ray ( www.povray.org ), and matplotlib 45 .
- Full pipeline: alignment/mapping [IMOD, MAFFT, MotionCor2, Python] -> registration [MotionCor2] -> structure determination [EMAN2] -> stage not stated [CTFFIND, Matplotlib, PyMOL]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **3.2.1**
- Evidence: Figure 4 and extended data figures 4 and 5 were generated with matplotlib v3.2.1 73 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Evidence: Analyses and visualization of data were conducted in a Python environment built on the Numpy, SciPy, matplotlib, scikit-learn package and pandas libraries.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Hydroclimatic vulnerability of peat carbon in the central Congo Basin. (Nature 2022)

- DOI: 10.1038/s41586-022-05389-3 | PMCID: PMC9729114 | PMID: 36323786
- Version used: **3.4.3**
- Evidence: ...PU (2.10 GHz)) with fiona (1.8.20), geocube (0.1.0), geopandas (0.10.1), ipykernel (6.4.1), ipython (7.28.0), jupyter (1.0.0), KDE-diffusion (1.0.3), matplotlib (3.4.3), notebook (6.4.4), numpy (1.20.3), pandas (1.3.3), rioxarray (0.7.1), scipy (1.7.1) and shapely (1.7.1) packages.
- Full pipeline: alignment/mapping [Python v3.7.3] -> differential/statistical testing [R] -> stage not stated [Matplotlib v3.4.3, NumPy v1.20.3, SciPy v1.7.1]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: Plots, statistics and molecular graphics Plots were generated using GraphPad Prism or Matplotlib 86 .
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Personalizing exoskeleton assistance while walking in the real world. (Nature 2022)

- DOI: 10.1038/s41586-022-05191-1 | PMCID: PMC9556303 | PMID: 36224415
- Version used: **2.0.2**
- Evidence: The required python packages are numpy (1.17.4), scikit-learn (0.21.3), scipy (1.3.2) and matplotlib (2.0.2).
- Full pipeline: stage not stated [Matplotlib v2.0.2, NumPy v1.17.4, SciPy v1.3.2, scikit-learn v0.21.3]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: Figures were generated using R and Matplotlib ( https://matplotlib.org ) in Python.
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### Nanoscale imaging of phonon dynamics by electron microscopy. (Nature 2022)

- DOI: 10.1038/s41586-022-04736-8 | PMCID: PMC9177420 | PMID: 35676428
- Evidence: Data visualization Contour plots of mapping data were created using matplotlib.pyplot, another Python library.
- Full pipeline: alignment/mapping [Matplotlib] -> visualisation [Matplotlib] -> stage not stated [Python, SciPy]

### Instantaneous tracking of earthquake growth with elastogravity signals. (Nature 2022)

- DOI: 10.1038/s41586-022-04672-7 | PMCID: PMC9177427 | PMID: 35545670
- Evidence: Figures were produced with the Generic Mapping Tool (GMT) 58 and matplotlib 59 .
- Full pipeline: alignment/mapping [Matplotlib] -> machine learning [PyTorch] -> visualisation [Matplotlib]

### A biophysical account of multiplication by a single neuron. (Nature 2022)

- DOI: 10.1038/s41586-022-04428-3 | PMCID: PMC8891015 | PMID: 35197635
- Version used: **3.0**
- Evidence: Data were corrected for the liquid junction potential and analysed using custom-written software in Python v.3.7 (Python Software Foundation) using NumPy v.1.15, Pandas v.0.25, SciPy v.1.3, Matplotlib v.3.0 and pyABF v.2.1 ( https://pypi.org/project/pyabf/ ).
- Full pipeline: stage not stated [ImageJ v2.0, Matplotlib v3.0, NumPy v1.15, Python v3.7, SciPy v1.3]

### Toroidal topology of population activity in grid cells. (Nature 2022)

- DOI: 10.1038/s41586-021-04268-7 | PMCID: PMC8810387 | PMID: 35022611
- Version used: **3.1.3**
- Evidence: Open-source Python packages used were: umap (version 0.3.10), ripser (0.4.1), numba (0.48.0), scipy (1.4.1), numpy (1.18.1), scikit-learn (0.22.1), matplotlib (3.1.3), h5py (2.10.0) and gudhi (3.4.1.post1).
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.1.3, NumPy v1.18.1, UMAP, scikit-learn v0.22.1] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, SciPy]

### The social and structural architecture of the yeast protein interactome. (Nature 2023)

- DOI: 10.1038/s41586-023-06739-5 | PMCID: PMC10700138 | PMID: 37968396
- Evidence: Cumulative distribution functions were plotted using the matplotlib-library (3.4.2) and NumPy (1.20.3).
- Full pipeline: visualisation [ChimeraX v1.4, Cytoscape, Matplotlib, NumPy v1.20.3] -> stage not stated [AlphaFold, NetworkX v2.6.2, Python]

### CD201&lt;sup&gt;+&lt;/sup&gt; fascia progenitors choreograph injury repair. (Nature 2023)

- DOI: 10.1038/s41586-023-06725-x | PMCID: PMC10665192 | PMID: 37968392
- Evidence: All quantification plots were generated using the Python-based packages Matplotlib and Seaborn.
- Full pipeline: alignment/mapping [STAR v2.5.2a, Scanpy] -> quantification [Matplotlib, seaborn] -> dimensionality reduction/clustering [UMAP, scVelo] -> differential/statistical testing [SciPy] -> simulation/modelling [scVelo]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: Matplotlib 63 was used for all other plots.
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Preserved neural dynamics across animals performing similar behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06714-0 | PMCID: PMC10665198 | PMID: 37938772
- Evidence: All the analyses were implemented in Python using open-source packages such as numpy, matplotlib, sci-kit, scipy and pandas 70 – 74 and custom code.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, Kilosort v2.0, Matplotlib, NumPy, Python, SciPy]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **3.4.3**
- Evidence: Data were analysed and figures generated using Python (version 3.9.1), along with packages numpy (version 1.20.3), scipy (version 1.7.1), matplotlib (version 3.4.3), and pandas (version 1.3.0), and R (version 3.6.0).
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **3.1.3**
- Evidence: The following packages and software were used in data analysis: UCSF ChimeraX 1.0, ImageJ 1.51, MATLAB R2019b, R 4.0.4, RStudio 1.4.1106, Jupyter Notebook 6.0.3, Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-i...
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Seasonal advance of intense tropical cyclones in a warming climate. (Nature 2023)

- DOI: 10.1038/s41586-023-06544-0 | PMCID: PMC10620083 | PMID: 37758952
- Evidence: The basemap in c was plotted using the Matplotlib basemap toolkit with the geographical coordinate system World Geodetic system 1984 generated by the Global Positioning System (maintained by the National Oceanic and Atmospheric Administration).
- Full pipeline: simulation/modelling [CESM] -> visualisation [Matplotlib]

### Clustering predicted structures at the scale of the known protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06510-w | PMCID: PMC10584675 | PMID: 37704730
- Version used: **3.6.2**
- Evidence: For plotting, Python v.3.10.6 ( https://www.python.org/ ), Matplotlib v.3.6.2 ( https://matplotlib.org/ ), seaborn v.0.12.2 ( https://github.com/mwaskom/seaborn ), ChimeraX v.1.5 ( https://www.cgl.ucsf.edu/chimerax/ ), Pavian commit: cd2f21 ( https://fbreitwieser.shinyapps.io/pavian/ ) and pandas v.1.5.2 ( https://github.com/pandas-dev/pandas ) were used.
- Full pipeline: stage not stated [AlphaFold, BLAST, ChimeraX v1.5, ColabFold, Matplotlib v3.6.2, seaborn v0.12.2]

### A foundation model for generalizable disease detection from retinal images. (Nature 2023)

- DOI: 10.1038/s41586-023-06555-x | PMCID: PMC10550819 | PMID: 37704728
- Version used: **3.6.1**
- Evidence: Results were further analysed and visualized with Python v.3.6, NumPy v.1.19.5, SciPy v.1.5.4, seaborn v.0.12.0, Matplotlib v.3.6.1, pandas v.1.5.0, Scikit-Learn v.1.1.3 and Pillow v.9.2.0.
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.19.5, SciPy v1.5.4, seaborn v0.12.0] -> stage not stated [Keras, PyTorch]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: The turbo colormap from matplotlib was used to assign amplitude values.
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Anthropogenic fingerprints in daily precipitation revealed by deep learning. (Nature 2023)

- DOI: 10.1038/s41586-023-06474-x | PMCID: PMC10567562 | PMID: 37648861
- Evidence: The map was generated using the Basemap Toolkit (version 1.2.0; https://matplotlib.org/basemap/ ).
- Full pipeline: stage not stated [Matplotlib]

### Water in the terrestrial planet-forming zone of the PDS 70 disk. (Nature 2023)

- DOI: 10.1038/s41586-023-06317-9 | PMCID: PMC10432267 | PMID: 37488359
- Version used: **3.5.1**
- Evidence: Figures were made with Matplotlib v.3.5.1. under the Matplotlib license at https://matplotlib.org/ .
- Full pipeline: differential/statistical testing [dynesty] -> visualisation [Matplotlib v3.5.1] -> stage not stated [SciPy]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Version used: **3.5.2**
- Evidence: Python (v.3), Pandas (v.1.3.5), NumPy (v.1.21.5), Matplotlib (v.3.5.2) and Scanpy (v.1.8.2 and v.1.9.1) were used for quality control and downstream processing.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Accurate medium-range global weather forecasting with 3D neural networks. (Nature 2023)

- DOI: 10.1038/s41586-023-06185-3 | PMCID: PMC10356604 | PMID: 37407823
- Evidence: The sub-figures with maps were plotted using the Matplotlib Basemap toolkit.
- Full pipeline: machine learning [PyTorch] -> visualisation [Matplotlib] -> stage not stated [NumPy, xarray]

### Natural short-lived halogens exert an indirect cooling effect on climate. (Nature 2023)

- DOI: 10.1038/s41586-023-06119-z | PMCID: PMC10307623 | PMID: 37380694
- Evidence: All maps and elements were created by our research group using Matplotlib Basemap for Python.
- Full pipeline: stage not stated [CESM, Matplotlib]

### No thick carbon dioxide atmosphere on the rocky exoplanet TRAPPIST-1 c. (Nature 2023)

- DOI: 10.1038/s41586-023-06232-z | PMCID: PMC10447244 | PMID: 37337068
- Evidence: Code availability We used the following codes, resources and Python packages to reduce, analyse and interpret our JWST observations of TRAPPIST-1 c: numpy 81 , matplotlib 82 , astropy 83 , batman 36 , Eureka!
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, dynesty, emcee]

### Health system-scale language models are all-purpose prediction engines. (Nature 2023)

- DOI: 10.1038/s41586-023-06160-y | PMCID: PMC10338337 | PMID: 37286606
- Version used: **3.5.2**
- Evidence: This work used several open-source libraries, including HuggingFace Transformers 4.19.2, Datasets 2.2.2, Evaluate 0.1.1, wandb 0.12.17, matplotlib 3.5.2, seaborn 0.12.2, pandas 1.4.2, ray 2.0.0, sklearn 1.1.1, deepspeed 0.8.0+384f17b, NVIDIA Apex, XGBoost 1.6.1 and nltk 3.6.3.
- Full pipeline: stage not stated [Matplotlib v3.5.2, Python v3.8.13, XGBoost, scikit-learn, seaborn v0.12.2]

### Gap junctions desynchronize a neural circuit to stabilize insect flight. (Nature 2023)

- DOI: 10.1038/s41586-023-06099-0 | PMCID: PMC10232364 | PMID: 37225999
- Evidence: For additional functions, the Python libraries NumPy, pickle, SciPy, Matplotlib and seaborn were imported.
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, Python, SciPy, seaborn]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Version used: **3.3.2**
- Evidence: Data visualization Plots were generated using matplotlib (version 3.3.2), seaborn (version 0.11.0) and plotly (version 5.6.0) packages in Python software (version 3.7.12), Jupyter notebook (version 6.1.4), RStudio (version 1.4) and Adobe Illustrator (version 26.4.1) software.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### Regime shift in Arctic Ocean sea ice thickness. (Nature 2023)

- DOI: 10.1038/s41586-022-05686-x | PMCID: PMC10017516 | PMID: 36922610
- Evidence: The Matplotlib basemap toolkit was used to plot the map.
- Full pipeline: stage not stated [Matplotlib]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Version used: **3.4.2**
- Evidence: Matplotlib (v.3.4.2) library 86 was used for data visualization.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: The calculated KDE was visualized with the matplotlib.pyplot.contour function.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: Software packages In addition to analysis-specific packages cited in the relevant sections above, the following packages were used for analysis: NumPy 83 , Python 84 , Seaborn 85 , Matplotlib 86 and Python 3 (ref.
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Version used: **3.2.1**
- Evidence: Data visualization was performed using Matplotlib (v.3.2.1) and Seaborn (v.0.9.0). scRNA-seq data were analysed using Cell Ranger (v.3.1.0), R (v.4.1.0) and Seurat (v.3.1.5).
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Version used: **3.4**
- Evidence: Box plots were prepared with matplotlib (v3.4 or v3.6) as follows unless stated otherwise: the box extends from the first quartile (Q1 or 25th percentile) to the third quartile (Q3 or 75th percentile) of the data, with a line at the median.
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### Identification of carbon dioxide in an exoplanet atmosphere. (Nature 2023)

- DOI: 10.1038/s41586-022-05269-w | PMCID: PMC9946830 | PMID: 36055338
- Evidence: ...ml ) and chromatic ( https://zkbt.github.io/chromatic/ ), each of which use the standard Python libraries scipy 98 , numpy 99 , astropy 100 , 101 and matplotlib 102 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **3.8.4**
- Evidence: Scanpy v.1.9.1 with anndata v.0.10.7 and the statistics and plotting libraries pandas v.2.2.2, numpy v.1.26.4, scipy v.1.13.0, seaborn v.0.13.2 and matplotlib v.3.8.4 were used for data analysis and visualization.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Adult skull bone marrow is an expanding and resilient haematopoietic reservoir. (Nature 2024)

- DOI: 10.1038/s41586-024-08163-9 | PMCID: PMC11618084 | PMID: 39537918
- Evidence: Finally, expression of select marker genes was plotted using Matplotlib 71 (3.8.4) imshow, and clusters were annotated accordingly.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [Matplotlib, UMAP] -> visualisation [Matplotlib] -> stage not stated [AnnData, ImageJ, Scanpy]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Version used: **3.7.3**
- Evidence: This used custom-made code but made use of libraries such as numpy (1.22.0), scipy (1.10.1), matplotlib (3.7.3), sciKit learn (1.3.2), pandas (2.0.3) and seaborn (0.13.2).
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### Coral photosymbiosis on Mid-Devonian reefs. (Nature 2024)

- DOI: 10.1038/s41586-024-08101-9 | PMCID: PMC11655356 | PMID: 39443794
- Evidence: The data were imported using the Pandas library and plotted using the Seaborn or Matplotlib libraries.
- Full pipeline: visualisation [Matplotlib, seaborn] -> stage not stated [Jupyter]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: Bubble plots were created using Matplotlib.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### LYCHOS is a human hybrid of a plant-like PIN transporter and a GPCR. (Nature 2024)

- DOI: 10.1038/s41586-024-08012-9 | PMCID: PMC11525196 | PMID: 39358511
- Evidence: All figures, analysis, video renders and visualizations were produced in ChimeraX 41 or with Python and Matplotlib.
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX v1.20.1] -> visualisation [Matplotlib] -> stage not stated [AlphaFold, CTFFIND v4.1.8, ChimeraX, ImageJ v2.14.0, MotionCor2 v1.1.0]

### Future increase in extreme El Niño supported by past glacial changes. (Nature 2024)

- DOI: 10.1038/s41586-024-07984-y | PMCID: PMC11464383 | PMID: 39322673
- Evidence: Code availability Open-sourced Python code was used to create the figures, perform the analyses and all calculations, including the following modules and their required dependencies: matplotlib 78 , pandas 79 , NumPy 80 , seaborn 81 , xarray 82 , cartopy 83 and SciPy 84 .
- Full pipeline: simulation/modelling [CESM v1.2] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn, xarray]

### Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. (Nature 2024)

- DOI: 10.1038/s41586-024-07881-4 | PMCID: PMC11390480 | PMID: 39261618
- Version used: **3.5.3**
- Evidence: Figures were plotted using R v4.2.2 (packages ggplot2 v3.3.2, ggridges v0.5.3, ggrepel v0.8.0 and RColorBrewer v1.1-3) and python v3 (packages matplotlib v3.5.3 and pandas v1.0.1).
- Full pipeline: alignment/mapping [GATK, SAMtools] -> normalisation [ADMIXTURE] -> registration [GATK, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [Matplotlib v3.5.3, R, ggplot2 v3.3.2] -> stage not stated [ANGSD v0.930, PLINK v1.9.20200712]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **3.7.1**
- Evidence: ...nvironment built on Pandas (v.2.0.1), NumPy (v.1.24.2) 73 , SciPy (v.1.10.1) 74 , scikit-learn (v.1.2.0), SCANPY (v1.9.3) 75 , AnnData (v.0.9.1) 75 , matplotlib (v.3.7.1) 76 and seaborn (v.0.13.1) 77 packages.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Version used: **3.7.2**
- Evidence: Single-molecule data interpretation Raw data exported from LUMICKS Bluelake as .h5 files were processed with custom-written Jupyter Notebooks in Python 3.9 using LUMICKS Pylake v.1.2.1, numpy v.1.26.0, matplotlib v.3.7.2, scipy v.1.11.3 and peakutils v.1.3.4 ( https://github.com/singlemoleculegroup ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### In situ targeted base editing of bacteria in the mouse gut. (Nature 2024)

- DOI: 10.1038/s41586-024-07681-w | PMCID: PMC11338833 | PMID: 38987595
- Evidence: 2 , 3 , 8 and 9 were generated using the libraries Matplotlib and Seaborn.
- Full pipeline: alignment/mapping [MAFFT, Python] -> dimensionality reduction/clustering [QIIME 2] -> stage not stated [Cutadapt v3.3, Matplotlib, fastp, seaborn]

### A multimodal generative AI copilot for human pathology. (Nature 2024)

- DOI: 10.1038/s41586-024-07618-3 | PMCID: PMC11464372 | PMID: 38866050
- Version used: **3.7.1**
- Evidence: Matplotlib (v.3.7.1) and Seaborn (v.0.12.2) were used to create plots and figures.
- Full pipeline: machine learning [PyTorch v2.0.1] -> stage not stated [Matplotlib v3.7.1, QuPath, seaborn v0.12.2]

### Inner core backtracking by seismic waveform change reversals. (Nature 2024)

- DOI: 10.1038/s41586-024-07536-4 | PMCID: PMC11236701 | PMID: 38867052
- Evidence: All the figures were generated using Python packages, Matplotlib ( https://matplotlib.org/ ), Basemap ( https://matplotlib.org/basemap/stable/ ) and ObsPy ( https://docs.obspy.org/ ).
- Full pipeline: visualisation [Matplotlib]

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
- Version used: **3.6.1**
- Evidence: ...NumPy v.1.26.3 ( https://github.com/numpy/numpy ), SciPy v.1.9.3 ( https://www.scipy.org/ ), seaborn v.0.12.2 ( https://github.com/mwaskom/seaborn ), Matplotlib v.3.6.1 ( https://github.com/matplotlib/matplotlib ), pandas v.2.0.3 ( https://github.com/pandas-dev/pandas ), statsmodels v.0.12.2 ( https://github.com/statsmodels/statsmodels ), RDKit v.4.3.0 ( https://github.com/rdkit/rdkit ) and Colab ...
- Full pipeline: visualisation [NumPy v1.26.3, SciPy v1.9.3, seaborn v0.12.2] -> stage not stated [AlphaFold, Matplotlib v3.6.1, RDKit, RoseTTAFold, statsmodels v0.12.2]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Figures were created using ggplot, ggnewscale, ggpattern, ggrepel, ggsflabel, ggspatial, ggpubr, cowplot, matplotlib, plotly ( https://plot.ly ), seaborn and TMB_plotter 98 – 108 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Single-cell analysis reveals context-dependent, cell-level selection of mtDNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07332-0 | PMCID: PMC11078733 | PMID: 38658765
- Version used: **3.4.2**
- Evidence: The analyses were performed using Python v3.7.12, with the following modules: matplotlib v3.4.2, numpy v1.21.0, pandas v1.1.5, plotly v5.16.1, pysam v0.16.0.1, scikit-learn v0.23.1, scipy v1.7.0 and seaborn v0.11.1.
- Full pipeline: quality control [MultiQC v1.11] -> stage not stated [Matplotlib v3.4.2, NumPy v1.21.0, R, SciPy v1.7.0, scikit-learn v0.23.1, seaborn v0.11.1]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **3.5.2**
- Evidence: Python (v.3.8.3): matplotlib (v.3.5.2) 136 and seaborn (v.0.10.1) 137 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Incomplete transcripts dominate the Mycobacterium tuberculosis transcriptome. (Nature 2024)

- DOI: 10.1038/s41586-024-07105-9 | PMCID: PMC10937400 | PMID: 38418874
- Version used: **3.7.1**
- Evidence: Data analysis and visualization scripts used Python packages including Matplotlib (v3.7.1), Numpy (v1.24.3), Scipy (v1.10.1), bioinfokit (v0.3), and pyCircos (v0.3.0).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, SAMtools v1.17] -> visualisation [Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1] -> stage not stated [Cutadapt v4.1, Python]

### A dynamical measure of the black hole mass in a quasar 11 billion years ago. (Nature 2024)

- DOI: 10.1038/s41586-024-07053-4 | PMCID: PMC11636685 | PMID: 38286342
- Evidence: GILDAS is publicly available on the IRAM webpage ( https://www.iram.fr/IRAMFR/GILDAS/ ). astropy, matplotlib, emcee, dynesty, numpy and scipy are all available through the Python Package Index ( https://pypi.org ).
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Affinity-optimizing enhancer variants disrupt development. (Nature 2024)

- DOI: 10.1038/s41586-023-06922-8 | PMCID: PMC10830414 | PMID: 38233525
- Evidence: MPRA data were analysed using standard Python libraries (pandas, numpy, scipy, seaborn, matplotlib).
- Full pipeline: differential/statistical testing [R] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn]

### Satellite mapping reveals extensive industrial activity at sea. (Nature 2024)

- DOI: 10.1038/s41586-023-06825-8 | PMCID: PMC10764273 | PMID: 38172362
- Evidence: All maps were generated using Python ( https://www.python.org ) with the open-source visualization libraries PySeas ( https://github.com/GlobalFishingWatch/pyseas ), Matplotlib ( https://matplotlib.org ) and Cartopy ( https://scitools.org.uk/cartopy ).
- Full pipeline: machine learning [scikit-learn] -> visualisation [Cartopy, Matplotlib]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Version used: **3.1.1**
- Evidence: The results here and throughout the manuscript were visualized using matplotlib (v.3.1.1; RRID: SCR_008624 ) 61 .
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Glasses-free 3D display with ultrawide viewing range using deep learning. (Nature 2025)

- DOI: 10.1038/s41586-025-09752-y | PMCID: PMC12675290 | PMID: 41299166
- Evidence: Figures were generated and processed using Python, Matplotlib, Microsoft PowerPoint and Adobe Photoshop.
- Full pipeline: visualisation [Matplotlib] -> stage not stated [OpenCV]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Evidence: Signal traces were visualized with Matplotlib 86 (v.3.8.0).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: One protein could not be completed due to limitations of AlphaFold 2 (CHD7). iPTM scores were extracted from individual json files and used to create a heat map with rows clustered using Seaborn and matplotlib (Extended Data Fig.
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Version used: **3.7.2**
- Evidence: Visualizations were performed using matplotlib (v3.7.2) and Seaborn (v0.13.2) in Python.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning. (Nature 2025)

- DOI: 10.1038/s41586-025-09422-z | PMCID: PMC12443585 | PMID: 40962978
- Version used: **3.5.2**
- Evidence: Data analysis used Python v.3.8 ( https://www.python.org/ ), NumPy v.1.23.1 ( https://github.com/numpy/numpy ), Matplotlib v.3.5.2 ( https://github.com/matplotlib/matplotlib ) and TensorBoard v.2.9.1 ( https://github.com/tensorflow/tensorboard ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [Matplotlib v3.5.2, NumPy v1.23.1]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: The plots were visualized using Matplotlib and Seaborn.
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **3.4.2**
- Evidence: The packages matplotlib v3.4.2 and seaborn 0.11.0 were used for visualization.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Graph layouts were computed using the spring layout algorithm (networkx, 10,000 iterations) and visualized using matplotlib.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Divergent evolutionary strategies pre-empt tissue collision in gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09447-4 | PMCID: PMC12527943 | PMID: 40903584
- Evidence: Plots were generated in GraphPad Prism or with Python scripts using Matplotlib and Seaborn graphic libraries.
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
- Version used: **3.3.2**
- Evidence: ...es were generated using the following Python, R and Matlab packages: Python: pandas (v.1.1.5), numpy (v.1.19.3), anndata (v.0.7.4), scanpy (v.1.6.0), matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R packages: ggplot2 (v.3.4.4), gplots (v.3.1.3), readr (v.2.1.4), dplyr (v.1.1.2), reshape2 (v.1.4.4), patchwork (v.1.1.3), RColorBrewer (v.1.1.3), ggrepel (v.0.9.4), ...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Plot submodule spatiomic includes plotting functions based on matplotlib 82 and seaborn 83 that facilitate visualizing common plots, for example, image registration metrics, SOM training-quality metrics, cluster projections, spatial adjacency graphs as well as cluster contributor histograms and volcano plots.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Evidence for a sub-Jovian planet in the young TWA 7 disk. (Nature 2025)

- DOI: 10.1038/s41586-025-09150-4 | PMCID: PMC12221965 | PMID: 40562924
- Evidence: We used various functions of the following software packages to perform the analysis and create the figures: numpy, astropy, scipy, matplotlib and photutils.
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Version used: **3.5.2**
- Evidence: The surface meshes were then plotted using matplotlib (v3.5.2) plot_trisurf with the bounding box being equal to the maximum length in any of the xy and z direction.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Unsupervised pretraining in biological neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09180-y | PMCID: PMC12367527 | PMID: 40533561
- Evidence: The figures were made using matplotlib and jupyter-notebook 62 , 63 .
- Full pipeline: visualisation [Matplotlib] -> stage not stated [NumPy, Python, SciPy, Suite2p, scikit-learn]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **3.8.0**
- Evidence: Python packages such as Scanpy (v.1.9.5), Pandas (v.2.0.0), Statsmodels (v.0.14.0), NumPy (v.1.24.2), Scipy (v.1.10.1), Matplotlib (v.3.8.0), Seaborn (v.0.11.2) and Sklearn (v.1.3.2), were used for data analysis.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Visualization was performed using a combination of Matplotlib 70 , SciPy 71 and NumPy 72 , and expression values are shown in heat maps as log 2 TPM to represent log fold change.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### A foundation model for the Earth system. (Nature 2025)

- DOI: 10.1038/s41586-025-09005-y | PMCID: PMC12119322 | PMID: 40399684
- Evidence: All of our plots were made using Matplotlib 77 and the geographical maps were produced using Cartopy 78 .
- Full pipeline: differential/statistical testing [WRF] -> stage not stated [Cartopy, Matplotlib]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **3.3.2**
- Evidence: Plots were generated using Matplotlib (3.3.2) 109 .
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Wide-swath satellite altimetry unveils global submesoscale ocean dynamics. (Nature 2025)

- DOI: 10.1038/s41586-025-08722-8 | PMCID: PMC12003163 | PMID: 40240853
- Evidence: We use ‘cmocean’ colour bars developed by Kristen Thyng and colleagues ( https://matplotlib.org/cmocean/ ) and ‘brewermap’ colour bars developed by Cynthia Brewer and colleagues ( https://colorbrewer2.org/ ).
- Full pipeline: simulation/modelling [MOM6] -> stage not stated [Matplotlib]

### Functional connectomics spanning multiple areas of mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08790-w | PMCID: PMC11981939 | PMID: 40205214
- Evidence: ...VE analysis infrastructure 1 (available at https://github.com/CAVEconnectome ) and CloudVolume 94 to interact with data infrastructure, and libraries Matplotlib 95 , Numpy 96 and Pandas for general computation and data visualization.
- Full pipeline: machine learning [CaImAn] -> visualisation [Matplotlib, NumPy] -> stage not stated [Python, SciPy]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Version used: **3.7.0**
- Evidence: ...Torch (1.12.1), tidyverse (2.0.0), glmmTMB (1.1.10), performance (0.12.2) and emmeans (1.10.3) were used for model training and statistical analysis; Matplotlib (3.7.0), seaborn (0.12.2), HoloViews (1.15.4), Ipyvolume (0.5.2) and Neuroglancer ( https://github.com/seung-lab/neuroglancer ) were used for graphical visualization; and Jupyter (ipykernel:6.21.2), Docker (23.0.1) and Kubernetes (1.22.11)...
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Connectomics of predicted Sst transcriptomic types in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08805-6 | PMCID: PMC11981948 | PMID: 40205210
- Evidence: We used the following libraries for visualization and analysis: Matplotlib 73 , Seaborn 74 , Numpy 75 , Pandas 76 , VTK 77 , Scipy 78 , Scikit-posthocs 79 , Scikit-learn 80 , scrattch-hicat ( https://github.com/AllenInstitute/scrattch.hicat/ ) and statsmodels 81 .
- Full pipeline: differential/statistical testing [limma] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn, seaborn, statsmodels]

### End-to-end data-driven weather prediction. (Nature 2025)

- DOI: 10.1038/s41586-025-08897-0 | PMCID: PMC12119340 | PMID: 40112882
- Evidence: All figures have been generated using a combination of the LaTeX TikZ package and the Matplotlib Python package 83 .
- Full pipeline: stage not stated [Matplotlib]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **3.6.3**
- Evidence: SL-Smart-seq3xpress data analysis Count matrices were processed with JupyterLab (v.4) notebooks using IPython (v.7.31) using the following modules: pandas (v.1.5.3), numpy (v.1.23.5), scipy (v.1.10.1), scanpy (v.1.7.2), openpyxl (v.3.1.2), matplotlib (v.3.6.3) and seaborn (v.0.12.2).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Record sea surface temperature jump in 2023-2024 unlikely but not unexpected. (Nature 2025)

- DOI: 10.1038/s41586-025-08674-z | PMCID: PMC11946890 | PMID: 40074909
- Evidence: All maps were created using the Basemap tool in Python ( https://matplotlib.org/basemap/stable/ ).
- Full pipeline: stage not stated [Matplotlib, Python]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **3.7.1**
- Evidence: Python packages used: beautifulsoup4 v.4.12.2, bio v.1.6.2, GSEApy v.1.1.0, matplotlib v.3.7.1, NumPy v.1.24.3, pandas v.2.0.2, SciPy v.1.10.1, seaborn v.0.12.2, sklearn v.0.0.post5, urllib3 v.2.0.3.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: We plotted trends using matplotlib (12__major-trajectory_dev-DEGs_stage-trend-fits.ipynb) (RRID:SCR_008624).
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### A travelling-wave strategy for plant-fungal trade. (Nature 2025)

- DOI: 10.1038/s41586-025-08614-x | PMCID: PMC11882455 | PMID: 40011773
- Evidence: 5b–f , all violin plots plotted using violinplot function of matplotlib Python library with the parameter show_extrema set to false.
- Full pipeline: machine learning [StarDist] -> visualisation [Matplotlib] -> stage not stated [SciPy, scikit-image, seaborn]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Version used: **3.7.1**
- Evidence: Heatmaps were generated using matplotlib (v.3.7.1).
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **3.7.1**
- Evidence: Scatter and line plots were generated using matplotlib (v.3.7.1).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Evidence: Clustering analyses of grid-cell modules and bursting subtypes of grid cells were conducted using the python package Scanpy 87 and its dependencies (including numpy, pandas, scipy, scikit-learn and matplotlib).
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

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
- Version used: **3.3.4**
- Evidence: Scripts and plots All data were processed and plotted using Python 3.8.8, matplotlib 3.3.4 and seaborn 0.11.1.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [RELION, UCSF Chimera] -> visualisation [Matplotlib v3.3.4, Python v3.8.8, seaborn v0.11.1] -> stage not stated [ChimeraX, ImageJ]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Version used: **3.5.1**
- Evidence: For other data analysis and plotting tasks, we used Python (3.8.13), pandas (1.4.2), matplotlib (3.5.1), seaborn (0.12.2), numpy (1.21.6), scipy (1.8.0), sklearn (1.0.2), anndata (0.8.0), scanpy (1.9.1), squidpy (1.1.2), tissue-sc (0.0.2), tangram-sc (1.0.3), spage (accessed September 1, 2022), gseapy (1.0.4), umap-learn (0.5.3) and statsmodels (0.13.2).
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Synthetic GPCRs for programmable sensing and control of cell behaviour. (Nature 2025)

- DOI: 10.1038/s41586-024-08282-3 | PMCID: PMC11666456 | PMID: 39633047
- Evidence: Quantification and Data Analysis All graphs were created using GraphPad Prism 9 or matplotlib (Python).
- Full pipeline: quantification [Matplotlib] -> differential/statistical testing [SciPy, seaborn] -> stage not stated [AlphaFold, ImageJ, MACS2, PHENIX, Python]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **3.6.0**
- Evidence: The Python package matplotlib (v.3.6.0) was used to produce all plots.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Relativistic electron acceleration at the bow shock of Jupiter and beyond. (Nature 2026)

- DOI: 10.1038/s41586-026-10473-z | PMCID: PMC13233311 | PMID: 42236560
- Evidence: Code availability All figures were plotted using Python (v.3.12.5) and the matplotlib library (v.3.9.2).
- Full pipeline: visualisation [Matplotlib] -> stage not stated [statsmodels v0.14.4]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: Scatterplots visualizing PFS preferences were generated using Matplotlib in Python.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Demography and life histories across the Roman frontier in Germany 400-700 CE. (Nature 2026)

- DOI: 10.1038/s41586-026-10437-3 | PMCID: PMC13293882 | PMID: 42056513
- Evidence: 7.4 , 8.17 and 10.1 – 10.7 , were created using the basemap toolkit from the matplotlib library 84 in Python 3, which uses cartographic data from Generic Mapping Tools ( https://www.generic-mapping-tools.org/ ).
- Full pipeline: alignment/mapping [Matplotlib, Python] -> registration [GATK v3.8] -> differential/statistical testing [statsmodels v0.14.4]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: We then generated pie charts representing the immune composition of each microenvironment using Matplotlib.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Language models transmit behavioural traits through hidden signals in data. (Nature 2026)

- DOI: 10.1038/s41586-026-10319-8 | PMCID: PMC13083239 | PMID: 41986627
- Evidence: Data analysis was performed using Python (NumPy, Pandas) and Matplotlib.
- Full pipeline: stage not stated [Matplotlib, NumPy]

### Observing the tidal pulse of rivers from wide-swath satellite altimetry. (Nature 2026)

- DOI: 10.1038/s41586-026-10287-z | PMCID: PMC13061602 | PMID: 41851459
- Evidence: Figures were plotted with QGIS and Matplotlib.
- Full pipeline: visualisation [Matplotlib, QGIS] -> stage not stated [Python]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **3.10.0**
- Evidence: Visualization methods We used matplotlib v.3.10.0, seaborn v.0.13.2, bokeh v.3.7.3 and Figma to plot most of the figures.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: All computational analyses and visualizations were performed in Python (v3.10), using the NumPy 76 , Pandas 77 , SciPy 78 and Matplotlib 79 libraries.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### Wind shear enhances soil moisture influence on rapid thunderstorm growth. (Nature 2026)

- DOI: 10.1038/s41586-025-10045-7 | PMCID: PMC12960254 | PMID: 41781736
- Evidence: 4 were generated using the Python packages matplotlib 61 and cartopy, made with Natural Earth data – Free vector and raster map data, https://www.naturalearthdata.com/ .
- Full pipeline: stage not stated [Matplotlib]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **10.5281**
- Evidence: The Kaplan–Meier survival analysis was performed in the Python programming language using the lifelines package 95 and visualized using matplotlib (10.5281/zenodo.592536).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Version used: **3.8.4**
- Evidence: Software versions SCANPY (v. ≥1.9), pingouin (v.0.5.4), gseapy (v.1.1.1), numpy (v. ≥1.26), scipy (v. ≥1.12), scikit-learn (v. ≥1.13), leidenalg (v.0.10.2), matplotlib (v.3.8.4), Cellrank (v.2.0.7), Palantir (v.1.4.1), R (v.4.3.3), FIJI/ImageJ (v. >1.54) and GraphPad (v. >9.0) were used.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Ligand-specific activation trajectories dictate GPCR signalling in cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09963-3 | PMCID: PMC12935549 | PMID: 41535472
- Evidence: 4 ) were generated using the NumPy and matplotlib libraries of Python (v.3.7.9) 66 , 67 .
- Full pipeline: visualisation [ChimeraX] -> stage not stated [ImageJ v1.5.4f, Matplotlib, NumPy]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: ...oolkits (versions ggplot2_3.5.1, tidyr_1.3.1, dplyr_1.1.4, ggpubr_0.6.0, Hmisc_5.2.1), Python (version 3.12.9) using the pandas, scipy, scikit-learn, matplotlib and seaborn packages (versions pandas_2.2.3, scipy_1.14.1, scikit-learn_1.5.2, matplotlib_3.9.2, seaborn_0.13.2) or Microsoft Excel for Mac (Office 365, version 16.9).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Evidence: The log 2 fold change values for these scores were computed for the nucleotides at PFS positions (+1 to +5), and scatterplots visualizing the PFS preferences were generated using Matplotlib in Python.
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Version used: **3.8.2**
- Evidence: Analyses we carried out with Python (v.3.12.0), using also the following libraries: numpy (v.1.26.2), scipy (v.1.11.4), statsmodels (v.0.14.0), and matplotlib (v.3.8.2) and seabron (v.0.11.2) for visualization.
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### Dated gene duplications elucidate the evolutionary assembly of eukaryotes. (Nature 2026)

- DOI: 10.1038/s41586-025-09808-z | PMCID: PMC12872463 | PMID: 41339551
- Evidence: Tree visualizations were produced in TreeViewer 72 and all other plots using Python Seaborn or Matplotlib, all programs and their versions are listed in Supplementary Table 1 .
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508] -> dimensionality reduction/clustering [HMMER v3.3.2, MAFFT v7.508] -> visualisation [Matplotlib, seaborn]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **1.0.1**
- Evidence: This was performed by fitting the equation 100 × e (− x × tau) in Python (v.3.7.6) and the package scipy (v.1.4.1) to each kinase’s CHX screening trajectory. t -SNE plots were generated with sklearn and matplotlib (v.1.0.1 and v.3.5.3, respectively) from ChEMBL drug-binding data processed as described in the Chemical Checker (CC) 24 and compounds were characterized with CC global bioactivity signa...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Inhibitory PD-1 axis maintains high-avidity stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09440-x | PMCID: PMC12727512 | PMID: 41299179
- Evidence: Principal component analysis was performed using the Python-based scikit-learn library on z -score-normalized marker intensity and plotted using matplotlib library to visualize relative marker expression.
- Full pipeline: quantification [seaborn] -> normalisation [Matplotlib, scikit-learn] -> dimensionality reduction/clustering [Matplotlib, scikit-learn] -> visualisation [Matplotlib, scikit-image, scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2, napari]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **3.10**
- Evidence: Commonly used Python libraries (Python v3.11.13, matplotlib v3.10, Seaborn v0.13, numpy v2.2.6, pandas v2.3.1, scipy v1.16.0, anndata v0.11.4 and shapely v2.1.1) were applied to visualize spatial distribution of cells.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Evidence: The resulting pairwise sequence identities were visualized using a matplotlib heatmap.
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: All analyses were conducted using skimage for image processing 71 , 72 , numpy and pandas for data handling, matplotlib and seaborn for visualization, and scipy and scikit-learn for statistical and machine learning operations.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Probing solution structure of the pentameric ligand-gated ion channel GLIC by small-angle neutron scattering. (PNAS 2021)

- DOI: 10.1073/pnas.2108006118 | PMCID: PMC8449418 | PMID: 34504004
- Evidence: Graphs were plotted using Matplotlib ( 65 ), and protein images were rendered using Vmd ( 66 ).
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [Matplotlib]

### Comprehensive pregnancy monitoring with a network of wireless, soft, and flexible sensors in high- and low-resource health settings. (PNAS 2021)

- DOI: 10.1073/pnas.2100466118 | PMCID: PMC8157941 | PMID: 33972445
- Evidence: All time-series analyses were done on Python with the scipy package for signal processing and the matplotlib package for graphing.
- Full pipeline: stage not stated [Matplotlib, SciPy]

### Global inequality remotely sensed. (PNAS 2021)

- DOI: 10.1073/pnas.1919913118 | PMCID: PMC8106331 | PMID: 33903226
- Evidence: The analysis was carried out in R ( https://www.r-project.org ) using the packages raster, rasterVis, sp, rgdal, ggplot2, and mixtools and Python ( https://www.python.org/ ) using numpy, matplotlib, scipy, and statsmodels.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, statsmodels]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Version used: **3.1.0**
- Evidence: After selecting information-rich features, results were visualized with matplotlib (v3.1.0) ( 62 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### &lt;i&gt;ARABIDOPSIS THALIANA HOMEOBOX GENE 1&lt;/i&gt; controls plant architecture by locally restricting environmental responses. (PNAS 2021)

- DOI: 10.1073/pnas.2018615118 | PMCID: PMC8092594 | PMID: 33888582
- Evidence: For statistical analysis and plotting graphs, functions were used from Numerical Python ( https://numpy.org ), Scientific Python ( https://www.scipy.org ), and MatPlotLib ( https://matplotlib.org ).
- Full pipeline: differential/statistical testing [Matplotlib, NumPy, SciPy] -> stage not stated [MACS2]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: All plots were generated using Matplotlib ( 58 ), Seaborn ( https://seaborn.pydata.org ) adjustText ( https://github.com/Phlya/adjustText ), mpl-scatter-density ( https://github.com/astrofrog/mpl-scatter-density ), Astropy ( 59 , 60 ), and Scanpy ( 50 ) libraries under Python 3.7.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Noninvasive neuromagnetic single-trial analysis of human neocortical population spikes. (PNAS 2021)

- DOI: 10.1073/pnas.2017401118 | PMCID: PMC7980398 | PMID: 33707209
- Version used: **3.2.1**
- Evidence: Data Availability All analyses were performed in the Python programming language in its most recent version (3.8.2) relying on the additional packages numpy (1.18.2), scipy (1.4.1), matplotlib (3.2.1), and the author-made M/EEG-analysis package “meet” in its most recent version ( https://github.com/neurophysics/meet ).
- Full pipeline: stage not stated [Matplotlib v3.2.1, NumPy v1.18.2, SciPy v1.4.1]

### The molecular basis for pore pattern morphogenesis in diatom silica. (PNAS 2022)

- DOI: 10.1073/pnas.2211549119 | PMCID: PMC9894196 | PMID: 36459651
- Version used: **3.5**
- Evidence: Differences that were not statistically significant are denoted “ns.” Unless otherwise noted, all figures were generated in Matplotlib 3.5 and Seaborn 0.11.
- Full pipeline: dimensionality reduction/clustering [scikit-learn v0.21.3] -> differential/statistical testing [Matplotlib v3.5, seaborn v0.11] -> visualisation [Matplotlib v3.5, seaborn v0.11] -> stage not stated [BLAST, NumPy, SciPy, scikit-image]

### Adult neurogenesis acts as a neural regularizer. (PNAS 2022)

- DOI: 10.1073/pnas.2206704119 | PMCID: PMC9659416 | PMID: 36322739
- Evidence: Models were built and analyzed in Python 3.6 ( 65 ) with custom scripts that are freely available on GitHub, and were developed using the following packages: PyTorch ( 66 ), Ax ( https://github.com/facebook/Ax ), NumPy ( 67 ), SciPy ( 68 ), Pandas ( 69 ), Matplotlib ( 70 ), Seaborn ( 71 ), and Scikit-learn 0.21.1 ( 72 ).
- Full pipeline: stage not stated [Matplotlib, NumPy, PyTorch, Python v3.6, SciPy, scikit-learn v0.21.1, seaborn]

### ADAR regulates APOL1 via A-to-I RNA editing by inhibition of MDA5 activation in a paradoxical biological circuit. (PNAS 2022)

- DOI: 10.1073/pnas.2210150119 | PMCID: PMC9636950 | PMID: 36282916
- Evidence: Matplotlib was used to plot the results ( 45 ).
- Full pipeline: quality control [STAR] -> read trimming [STAR] -> alignment/mapping [SAMtools v1.13, STAR] -> quantification [DESeq2, HTSeq] -> normalisation [R v4.1.2, featureCounts v2.0.0] -> stage not stated [Matplotlib, SciPy]

### Differential interactions of resting, activated, and desensitized states of the α7 nicotinic acetylcholine receptor with lipidic modulators. (PNAS 2022)

- DOI: 10.1073/pnas.2208081119 | PMCID: PMC9618078 | PMID: 36251999
- Evidence: Visualizations were created in VMD ( 68 ); most analyses were performed with GROMACS and MDAnalysis ( 69 ) and plotted with RainCloudPlot ( 70 ) and Matplotlib ( 71 ).
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [MDAnalysis, Matplotlib, VMD]

### How digital media drive affective polarization through partisan sorting. (PNAS 2022)

- DOI: 10.1073/pnas.2207159119 | PMCID: PMC9586282 | PMID: 36215484
- Evidence: The colors are chosen by treating the list of dynamic attributes as a base- m number and then normalizing the result (i.e., ∑ l = 1 … n D i , l m l − 1 / m n ), using this fraction to select a color from matplotlib’s cm_prism.
- Full pipeline: normalisation [Matplotlib]

### Walking is like slithering: A unifying, data-driven view of locomotion. (PNAS 2022)

- DOI: 10.1073/pnas.2113222119 | PMCID: PMC9477242 | PMID: 36067311
- Evidence: Supplementary Material Supplementary File Data, Materials, and Software Availability Motion tracking data (CSV and GZ) and processing and plotting code (python 3, scipy, matplotlib) have been deposited in Deep Blue Data (DOI: 10.7302/gqk6-3x41 , DOI: 10.7302/0fpj-dz57 , DOI: 10.7302/m05a-0d90 , DOI: 10.7302/jh82-fh69 , and DOI: 10.7302/024q-kk06 ).
- Full pipeline: dimensionality reduction/clustering [SciPy v0.17.0] -> stage not stated [Matplotlib]

### A neural network solves, explains, and generates university math problems by program synthesis and few-shot learning at human level. (PNAS 2022)

- DOI: 10.1073/pnas.2123433119 | PMCID: PMC9371704 | PMID: 35917350
- Evidence: Matplotlib is used in classes with questions that require plotting.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Matplotlib, NumPy, Python, SciPy]

### A male pheromone that improves the quality of the oogenic germline. (PNAS 2022)

- DOI: 10.1073/pnas.2015576119 | PMCID: PMC9173808 | PMID: 35576466
- Evidence: We generated the heatmap using Python ( 80 ) version 3.7.10, Matplotlib ( 81 ) version 3.3.4, and seaborn ( 82 ) version 0.11.2.
- Full pipeline: quality control [MultiQC, Nextflow] -> differential/statistical testing [DESeq2 v1.32.0, NumPy, R v4.1, SciPy] -> stage not stated [Matplotlib, seaborn]

### Geometric control of topological dynamics in a singing saw. (PNAS 2022)

- DOI: 10.1073/pnas.2117241119 | PMCID: PMC9169918 | PMID: 35446615
- Evidence: 1 D , Middle and Right , were computed for individual audio signals using matplotlib’s specgram function with options NFFT = 512 Hz (number of fast Fourier transform data points per block), pad_to = 8 , 192 Hz, and noverlap = 256 Hz.
- Full pipeline: stage not stated [Matplotlib, SciPy]

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
- Evidence: All plots are made using the Python matplotlib ( 72 ) package.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [Matplotlib, NumPy, Python v3.6, SciPy]

### ERK signaling dissolves ERF repression condensates in living embryos. (PNAS 2022)

- DOI: 10.1073/pnas.2119187119 | PMCID: PMC8892517 | PMID: 35217620
- Evidence: The remaining values were normalized to cell cycle length and plotted using matplotlib.
- Full pipeline: normalisation [Matplotlib] -> visualisation [Matplotlib] -> stage not stated [Python]

### Label-free sensing of cells with fluorescence lifetime imaging: The quest for metabolic heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2118241119 | PMCID: PMC8892511 | PMID: 35217616
- Evidence: All simulation and data analysis were performed using custom-build Python 3.7 scripts with the use of Numpy, Scipy, Scikit-Learn Matplotlib, Pandas and LmFit modules.
- Full pipeline: simulation/modelling [Matplotlib, NumPy, Python v3.7, SciPy] -> stage not stated [scikit-learn]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: The intersections and differences among the resulting sets of orthogroups were then extracted, and Venn diagrams were constructed using matplotlib_venn (version 3.1.1) ( 64 ) or Python package venn.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Generation of de novo miRNAs from template switching during DNA replication. (PNAS 2023)

- DOI: 10.1073/pnas.2310752120 | PMCID: PMC10710096 | PMID: 38019864
- Version used: **3.5.1**
- Evidence: The heatmaps were generated using Python packages matplotlib v.3.5.1 and seaborn v.0.11.2.
- Full pipeline: stage not stated [BEDTools v2.26.0, Matplotlib v3.5.1, Python, R, ggplot2, seaborn v0.11.2]

### Machine-guided discovery of a real-world rogue wave model. (PNAS 2023)

- DOI: 10.1073/pnas.2306275120 | PMCID: PMC10691345 | PMID: 37983488
- Evidence: This publication was made possible by the following opensource software stack: JAX ( 57 ), flax ( 58 ), optax ( 59 ), PySR ( 9 ), scikit-learn ( 63 ), PyALE ( 64 ), NumPy ( 65 ), SciPy ( 66 ), matplotlib ( 67 ), Seaborn ( 68 ), pandas ( 69 ), and Jupyter ( 70 ).
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, SciPy, scikit-learn, seaborn]

### Diversity of rhodopsin cyclases in zoospore-forming fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2310600120 | PMCID: PMC10622942 | PMID: 37871207
- Version used: **3.4.3**
- Evidence: Molecular visualization and data plotting were done using PyMOL 2.4.1 and Matplotlib 3.4.3, respectively.
- Full pipeline: read trimming [IQ-TREE, SPAdes v3.15.5] -> alignment/mapping [IQ-TREE] -> simulation/modelling [GROMACS v2019.3] -> visualisation [Matplotlib v3.4.3, PyMOL v2.4.1] -> stage not stated [AlphaFold, MDAnalysis v2.4.3]

### Curiosity evolves as information unfolds. (PNAS 2023)

- DOI: 10.1073/pnas.2301974120 | PMCID: PMC10614840 | PMID: 37844235
- Evidence: Figures were produced in Python with Seaborn and Matplotlib.
- Full pipeline: differential/statistical testing [lme4] -> visualisation [Matplotlib, Python, seaborn] -> stage not stated [R v4.0]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **3.5.2**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### Gating of homeostatic regulation of intrinsic excitability produces cryptic long-term storage of prior perturbations. (PNAS 2023)

- DOI: 10.1073/pnas.2222016120 | PMCID: PMC10293857 | PMID: 37339223
- Evidence: The solutions were visualized and analyzed using standard Python libraries (numpy and matplotlib).
- Full pipeline: visualisation [Matplotlib, NumPy] -> stage not stated [Python]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Version used: **3.3.2**
- Evidence: Plots were generated using matplotlib v3.3.2, seaborn v0.11.0, and ggplot2 v3.3.6.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Evidence: Fetal data were plotted as a line plot by time while adult data (due to the lack of a temporal variable) was plotted as box and whisker plots using a combination of tools from the Python packages matplotlib , seaborn , and plotnine .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### Cortical activity emerges in region-specific patterns during early brain development. (PNAS 2023)

- DOI: 10.1073/pnas.2208654120 | PMCID: PMC10235933 | PMID: 37216522
- Evidence: Figures were rendered using Matplotlib.
- Full pipeline: quantification [ImageJ] -> normalisation [Python] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [Matplotlib] -> stage not stated [NetworkX, NumPy, SciPy]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Version used: **3.5.1**
- Evidence: The dot and bar plots for enrichment analysis were drawn by the python package Matplotlib version 3.5.1 ( 61 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### <i>Leishmania</i> allelic selection during experimental sand fly infection correlates with mutational signatures of oxidative DNA damage. (PNAS 2023)

- DOI: 10.1073/pnas.2220828120 | PMCID: PMC10013807 | PMID: 36848551
- Version used: **3.5.1**
- Evidence: Further SNP analyses were performed based on the filtered outputs of GIP using custom Python 3.10 code relying on the following libraries: Pandas (1.4.2) ( 24 ), Pysam (0.19.0) ( 25 ), Numpy (1.22.3) ( 26 ), Matplotlib (3.5.1) ( 27 ), Seaborn (0.11.2) ( 28 ), Biotite (0.32.0) ( 29 ), and Upsetplot (0.6.0) ( 30 ).
- Full pipeline: stage not stated [Matplotlib v3.5.1, NumPy v1.22.3, Python v3.10, seaborn v0.11.2]

### A critical analysis of plant science literature reveals ongoing inequities. (PNAS 2023)

- DOI: 10.1073/pnas.2217564120 | PMCID: PMC10013813 | PMID: 36853942
- Version used: **3.6.1**
- Evidence: We computed national summary stats, global patterns of author location, and associations with national development indicators using Python (v3.8.8) packages Pandas (v1.5.0) and Numpy (v1.22.4) and visualized data in Seaborn (v0.11.1) and Matplotlib (v3.6.1).
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.22.4, seaborn v0.11.1]

### Supramolecular organization and dynamics of mannosylated phosphatidylinositol lipids in the mycobacterial plasma membrane. (PNAS 2023)

- DOI: 10.1073/pnas.2212755120 | PMCID: PMC9945971 | PMID: 36693100
- Evidence: Plots were created using Matplotlib ( 47 ).
- Full pipeline: simulation/modelling [GROMACS v2021.3, Python] -> stage not stated [AlphaFold, Clustal Omega, Matplotlib, PLUMED]

### Nutrient colimitation is a quantitative, dynamic property of microbial populations. (PNAS 2024)

- DOI: 10.1073/pnas.2400304121 | PMCID: PMC11670248 | PMID: 39693349
- Evidence: We prepared all figures using Matplotlib ( 78 ) version 3.9.1.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python v3.10.9, SciPy]

### OmpA controls order in the outer membrane and shares the mechanical load. (PNAS 2024)

- DOI: 10.1073/pnas.2416426121 | PMCID: PMC11648852 | PMID: 39630873
- Evidence: Matplotlib ( 73 ) was used to plot the data.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [BLAST, ImageJ, Matplotlib]

### C9orf72-linked arginine-rich dipeptide repeats aggravate pathological phase separation of G3BP1. (PNAS 2024)

- DOI: 10.1073/pnas.2402847121 | PMCID: PMC11648655 | PMID: 39621905
- Evidence: The figure was created in Python3 using the “matplotlib” module ( https://matplotlib.org/ ) Analysis of MLO Proteomes and Their Overlap with the R-DPR Interactome.
- Full pipeline: stage not stated [Matplotlib, Python]

### Diversification of pectoral control through motor pool extension. (PNAS 2024)

- DOI: 10.1073/pnas.2413415121 | PMCID: PMC11626184 | PMID: 39602261
- Evidence: 3.8, Python Software Foundation, www.python.org ), building on the NumPy [v.1.18.5, ( 42 )], matplotlib [v.3.2.2, ( 43 )], pandas [v.2.2.1, ( 44 )] and seaborn [0.12.2, ( 45 )] libraries were used.
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [SciPy] -> stage not stated [Matplotlib, NumPy, Python, seaborn]

### Atomic view of photosynthetic metabolite permeability pathways and confinement in synthetic carboxysome shells. (PNAS 2024)

- DOI: 10.1073/pnas.2402277121 | PMCID: PMC11551347 | PMID: 39485798
- Evidence: Particle tracking and analysis was performed with python-enabled VMD ( 70 ), extensively using numpy ( 74 ), scipy ( 75 ), and Matplotlib ( 76 ) libraries.
- Full pipeline: simulation/modelling [GROMACS, NAMD v2.14, VMD] -> stage not stated [Matplotlib, NumPy, SciPy]

### Adaptive CVgen: Leveraging reinforcement learning for advanced sampling in protein folding and chemical reactions. (PNAS 2024)

- DOI: 10.1073/pnas.2414205121 | PMCID: PMC11551409 | PMID: 39475640
- Evidence: All data visualizations were generated using the Python library Matplotlib ( 59 ).
- Full pipeline: dimensionality reduction/clustering [PyMOL, scikit-learn] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib, PyMOL] -> stage not stated [AlphaFold, MDTraj]

### AlphaFold-Multimer accurately captures interactions and dynamics of intrinsically disordered protein regions. (PNAS 2024)

- DOI: 10.1073/pnas.2406407121 | PMCID: PMC11536093 | PMID: 39446390
- Evidence: We extensively used BioPython, NumPy, SciPy, pandas, Matplotlib, and seaborn ( 57 – 62 ) to develop the code and plot the figures for this work.
- Full pipeline: machine learning [AlphaFold] -> visualisation [PyMOL] -> stage not stated [ColabFold, Matplotlib, NumPy, RoseTTAFold, SciPy, seaborn]

### A conserved peptide-binding pocket in HyNaC/ASIC ion channels. (PNAS 2024)

- DOI: 10.1073/pnas.2409097121 | PMCID: PMC11474038 | PMID: 39365813
- Version used: **3.4.3**
- Evidence: The interaction fingerprints were analyzed with Python 3.9.7 and pandas 1.3.2 and visualized with matplotlib 3.4.3.
- Full pipeline: dimensionality reduction/clustering [UCSF Chimera v1.14] -> visualisation [Matplotlib v3.4.3, Python v3.9.7] -> stage not stated [BLAST]

### Snowmelt duration controls red algal blooms in the snow of the European Alps. (PNAS 2024)

- DOI: 10.1073/pnas.2400362121 | PMCID: PMC11474047 | PMID: 39312681
- Evidence: ( C ) Dust deposition for each snow season, normalized at each location ( Materials and Methods ) and plotted using violinplot from matplotlib .
- Full pipeline: normalisation [Matplotlib] -> machine learning [Python, SciPy] -> visualisation [Matplotlib] -> stage not stated [BLAST]

### Blobs form during the single-file transport of proteins across nanopores. (PNAS 2024)

- DOI: 10.1073/pnas.2405018121 | PMCID: PMC11420176 | PMID: 39264741
- Evidence: The global minimum and maximum of these profiles were computed using numpy ( 47 ) and plotted along with the profiles using matplotlib ( 48 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [Matplotlib, NumPy] -> stage not stated [ChimeraX, MDAnalysis, PyMOL]

### MICU1 and MICU2 control mitochondrial calcium signaling in the mammalian heart. (PNAS 2024)

- DOI: 10.1073/pnas.2402491121 | PMCID: PMC11363308 | PMID: 39163336
- Version used: **3.5.1**
- Evidence: Individual cells were masked and mean gray values were exported and further processed in Excel, Visual Studio Code 1.76.2 (using Python 3.9.12, Numpy 1.21.5, Matplotlib 3.5.1, Statsmodels 0.13.2, Pandas 1.4.2), SigmaPlot 12.5, and GraphPad Prism 9.3.0.
- Full pipeline: stage not stated [Matplotlib v3.5.1, NumPy v1.21.5, Python v3.9.12]

### MAVS Cys508 palmitoylation promotes its aggregation on the mitochondrial outer membrane and antiviral innate immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2403392121 | PMCID: PMC11348129 | PMID: 39141356
- Evidence: The overlaid histogram with fitted Gaussian distribution was plotted using python script based on python packages Matplotlib and SciPy.
- Full pipeline: quantification [CellProfiler, ImageJ] -> visualisation [Matplotlib, SciPy] -> stage not stated [Fiji]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: To estimate the proportion of wild adaptive diversity represented by the breeding program, we intersected the backcross and wild sample datasets, which left 14,767 shared adaptive loci, and performed linear regressions of their AFs between the two groups using the matplotlib Python package ( 44 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Upstream surface roughness and terrain are strong drivers of contrast in tornado potential between North and South America. (PNAS 2024)

- DOI: 10.1073/pnas.2315425121 | PMCID: PMC11214001 | PMID: 38889148
- Evidence: Supplementary Material Appendix 01 (PDF) Acknowledgments We acknowledge NCAR CISL Cheyenne (DOI: 10.5065/D6RX99HX ) and Purdue RCAC for research computing time and infrastructure and developers of Python software packages including numpy, matplotlib, metpy, and xcape.
- Full pipeline: simulation/modelling [CESM v2.1.1] -> stage not stated [Matplotlib, NumPy]

### Bmal1 integrates circadian function and temperature sensing in the suprachiasmatic nucleus. (PNAS 2024)

- DOI: 10.1073/pnas.2316646121 | PMCID: PMC11047078 | PMID: 38625943
- Evidence: Cluster maps and timeseries graphs were created using the matplotlib package ( 42 ).
- Full pipeline: normalisation [Python, scikit-learn v1.2.2] -> dimensionality reduction/clustering [Matplotlib, Python, SciPy, scikit-learn v1.2.2] -> differential/statistical testing [SciPy]

### Molecular dynamics in multidimensional space explains how mutations affect the association path of neomycin to a riboswitch. (PNAS 2024)

- DOI: 10.1073/pnas.2317197121 | PMCID: PMC11009640 | PMID: 38579011
- Evidence: Figures and movies were generated using Pymol and Matplotlib ( 49 , 50 ).
- Full pipeline: stage not stated [MDAnalysis, Matplotlib]

### Conformational changes in the Niemann-Pick type C1 protein NCR1 drive sterol translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2315575121 | PMCID: PMC11009665 | PMID: 38568972
- Evidence: Intensity line profiles of FM4-64 and ConA-Alexa 488 were measured using Macros in ImageJ and plotted in Python software using Matplotlib ( 42 ).
- Full pipeline: alignment/mapping [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, Matplotlib, Python]

### Unraveling sources of emission heterogeneity in Silicon Vacancy color centers with cryo-cathodoluminescence microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2308247121 | PMCID: PMC10998621 | PMID: 38551833
- Evidence: Data analysis was performed in Python, utilizing multiple common packages, such as numpy, scipy, and matplotlib.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python, SciPy]

### Subcallosal cingulate deep brain stimulation evokes two distinct cortical responses via differential white matter activation. (PNAS 2024)

- DOI: 10.1073/pnas.2314918121 | PMCID: PMC10998591 | PMID: 38527192
- Version used: **3.8.0**
- Evidence: The source analysis was performed in python 3.11.5 using the following packages: mne 1.5.1, numpy 1.24.4, matplotlib 3.8.0, scipy 1.11.2, pandas 2.1.1, and seaborn 0.12.2 ( 57 – 62 ).
- Full pipeline: stage not stated [AFNI, Camino, FSL, Matplotlib v3.8.0, NumPy v1.24.4, SciPy v1.11.2, seaborn v0.12.2]

### Network of epistatic interactions in an enzyme active site revealed by large-scale deep mutational scanning. (PNAS 2024)

- DOI: 10.1073/pnas.2313513121 | PMCID: PMC10962969 | PMID: 38483989
- Evidence: Heatmaps were created using the Seaborn package as part of Matplotlib, executed in Python.
- Full pipeline: stage not stated [Matplotlib, Python v3.0, seaborn]

### Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2314199121 | PMCID: PMC10945847 | PMID: 38451940
- Evidence: Graphics were rendered with Matplotlib ( 81 ) and Inkscape ( 82 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4, MDAnalysis, SciPy, scikit-learn] -> visualisation [Matplotlib, VMD] -> stage not stated [NetworkX]

### The exostosin glycosyltransferase 1/STAT3 axis is a driver of breast cancer aggressiveness. (PNAS 2024)

- DOI: 10.1073/pnas.2316733121 | PMCID: PMC10801894 | PMID: 38215181
- Evidence: Package matplotlib was used for plots.
- Full pipeline: dimensionality reduction/clustering [GSEA, R] -> visualisation [GSEA, R] -> stage not stated [Matplotlib]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Version used: **3.0.3**
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

### On the scale of heterogeneity in composite electrodes of batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2520136122 | PMCID: PMC12582338 | PMID: 41129219
- Evidence: All computations and visualizations are made using various libraries in python (e.g. numpy, scipy, matplotlib, etc.) Finite Element Modeling.
- Full pipeline: alignment/mapping [scikit-image] -> dimensionality reduction/clustering [SciPy] -> structure determination [scikit-image] -> visualisation [Matplotlib, NumPy] -> stage not stated [OpenCV, Python]

### Atomistic mechanisms of calcium permeation modulated by Q/R editing and selectivity filter mutations in GluA2 AMPA receptors. (PNAS 2025)

- DOI: 10.1073/pnas.2425172122 | PMCID: PMC12377769 | PMID: 40811461
- Evidence: Data were plotted with Matplotlib.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis, VMD] -> visualisation [MDAnalysis, Matplotlib, VMD] -> stage not stated [PyMOL]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Version used: **3.8.2**
- Evidence: Graphs were produced using Matplotlib v3.8.2 ( 98 ) and Seaborn v0.13 ( 99 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Physical activity stimulates clock neurons of the day-active rodent &lt;i&gt;Arvicanthis ansorgei&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2424545122 | PMCID: PMC12130842 | PMID: 40388616
- Version used: **3.4.2**
- Evidence: Data from the in vivo electrophysiology experiments were analyzed using Python 3.0.9 with the Pandas module version 1.3.0 and visualized using Matplotlib version 3.4.2 or RStudio version 1.4.1103.
- Full pipeline: visualisation [Matplotlib v3.4.2, Python v3.0.9] -> stage not stated [SciPy v1.7.0]

### Virion-associated influenza hemagglutinin clusters upon sialic acid binding visualized by cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426427122 | PMCID: PMC12037027 | PMID: 40244672
- Evidence: Seaborn and Matplotlib libraries were used to generate histograms ( 47 , 48 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [PHENIX] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Matplotlib, Python, RELION, seaborn]

### Bispecific antibodies against the hepatitis C virus E1E2 envelope glycoprotein. (PNAS 2025)

- DOI: 10.1073/pnas.2420402122 | PMCID: PMC12012487 | PMID: 40193609
- Evidence: Calibrated events were exported and processed by an in-house developed Python pipeline ( 86 ) using NumPy ( 87 ), pandas ( 88 ), Matplotlib ( 89 ), SciPy ( 90 ), and seaborn ( 91 ).
- Full pipeline: visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, Matplotlib, NumPy, SciPy, seaborn]

### Molecular design principles for bipolar spindle organization by two opposing motors. (PNAS 2025)

- DOI: 10.1073/pnas.2422190122 | PMCID: PMC11962486 | PMID: 40117309
- Evidence: The color mapping for the ratio values is assigned as follows: black is used when the ratio is zero; for nonzero ratios, the “hot” Matplotlib color scheme is applied, scaling linearly with the ratio value.
- Full pipeline: alignment/mapping [Matplotlib] -> normalisation [Matplotlib]

### An atlas of early human mandibular endochondral and osteogenic paracrine signaling regions of Meckel's cartilage. (PNAS 2025)

- DOI: 10.1073/pnas.2420466122 | PMCID: PMC11962497 | PMID: 40096606
- Version used: **3.7.2**
- Evidence: Interaction matrices and network diagrams were visualized via the use of libraries such as matplotlib (v.3.7.2).
- Full pipeline: normalisation [Harmony v1.2.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib v3.7.2, UMAP] -> stage not stated [CellChat, CellPhoneDB, Seurat v4.0.0]

### Visualizing agonist-induced M2 receptor activation regulated by aromatic ring dynamics. (PNAS 2025)

- DOI: 10.1073/pnas.2418559122 | PMCID: PMC11912407 | PMID: 40053366
- Evidence: The 2D heatmaps were plot using Matplotlib ( 64 ) with a bin of 100 snapshots.
- Full pipeline: simulation/modelling [AutoDock Vina v1.1.2, PyMOL] -> stage not stated [Matplotlib]

### Immobile lipopolysaccharides and outer membrane proteins differentially segregate in growing &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2414725122 | PMCID: PMC11912417 | PMID: 40030021
- Evidence: Plotting of the final data was conducted using the Python library matplotlib.
- Full pipeline: stage not stated [ImageJ, Matplotlib, Python, R v4.1.0]

### ATP-sensitive potassium channels alter glycolytic flux to modulate cortical activity and sleep. (PNAS 2025)

- DOI: 10.1073/pnas.2416578122 | PMCID: PMC11874466 | PMID: 39964713
- Evidence: For the heatmap, data were pseudobulked by taking the average (or the z score) by cell type and used matplotlib for the plotting/visualization.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib] -> stage not stated [R]

### Restriction-modification systems are required for &lt;i&gt;Neisseria gonorrhoeae&lt;/i&gt; pilin antigenic variation. (PNAS 2026)

- DOI: 10.1073/pnas.2602688123 | PMCID: PMC13321361 | PMID: 42335229
- Evidence: Adapter positions were filtered, and adaptor locations were visualized using matplotlib.
- Full pipeline: read trimming [Matplotlib, minimap2] -> alignment/mapping [SAMtools, minimap2] -> visualisation [Matplotlib]

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
- Version used: **3.5.3**
- Evidence: Data visualization and further analysis were performed using matplotlib (v3.5.3) ( 70 ), seaborn (v0.12.2) ( 71 ), and numpy (v1.21.6) ( 72 ), with candidate chimeric reads and breakpoint loci summarized in output tables and plots.
- Full pipeline: alignment/mapping [SAMtools v1.18] -> visualisation [Matplotlib v3.5.3, NumPy v1.21.6, seaborn v0.12.2]

### Identification of immunostimulatory antigens in Group A &lt;i&gt;&lt;i&gt;Streptococcus&lt;/i&gt;&lt;/i&gt;-derived vesicles. (PNAS 2026)

- DOI: 10.1073/pnas.2537351123 | PMCID: PMC13187779 | PMID: 42118829
- Version used: **3.8.0**
- Evidence: For every gene, the mean pIdent (%) was calculated per M-Family, and a heatmap was generated using Matplotlib v3.8.0 ( 59 ).
- Full pipeline: stage not stated [Matplotlib v3.8.0]

### Geometric ordering in bacterial communities. (PNAS 2026)

- DOI: 10.1073/pnas.2526643123 | PMCID: PMC13187718 | PMID: 42118839
- Version used: **3.7.1**
- Evidence: Convex hulls were rendered as 3D polygons using Poly3DCollection from mpl_toolkits.mplot3d.art3d in Matplotlib (v3.7.1, available at https://matplotlib.org ).
- Full pipeline: simulation/modelling [Python] -> visualisation [Matplotlib v3.7.1, SciPy] -> stage not stated [ImageJ v1.54d, NumPy]

### Interspecies interaction controls &lt;i&gt;Escherichia coli&lt;/i&gt; growth in human gut microbiome samples. (PNAS 2026)

- DOI: 10.1073/pnas.2527793123 | PMCID: PMC13123830 | PMID: 42018414
- Evidence: We verified peak fitting accuracy by generating diagnostic plots with Matplotlib .
- Full pipeline: quantification [vegan v2.7] -> normalisation [vegan v2.7] -> dimensionality reduction/clustering [vegan v2.7] -> visualisation [phyloseq v1.46] -> stage not stated [DADA2 v3.18, Matplotlib, Python, SciPy, emmeans]

### Reconstruction of human metabolic models with large language models. (PNAS 2026)

- DOI: 10.1073/pnas.2516511123 | PMCID: PMC13079975 | PMID: 41950094
- Version used: **3.4.3**
- Evidence: The analysis and visualization were facilitated by Python 3.7.16, SHAP 0.41.0, scikit-learn 1.0.2, pandas 1.1.3, SciPy 1.7.3, NumPy 1.21.5, and Matplotlib 3.4.3 packages.
- Full pipeline: visualisation [Matplotlib v3.4.3, NumPy v1.21.5, Python v3.7.16, SciPy v1.7.3, scikit-learn v1.0.2]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: It was implemented in Python, utilizing OpenCV, PIL, Tkinter/CustomTkinter, Matplotlib, NumPy, and Pandas for image processing, visualization, and data management, and with aicspylibczi for handling czi files.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Olfactory inputs to appetite neurons in the hypothalamus. (PNAS 2026)

- DOI: 10.1073/pnas.2524926123 | PMCID: PMC12867749 | PMID: 41591908
- Version used: **3.8**
- Evidence: The resulting coexpression matrix was plotted using Matplotlib v3.8.
- Full pipeline: alignment/mapping [Cufflinks] -> quantification [AnnData v0.10, Cufflinks, Matplotlib v3.8, Scanpy v1.9] -> visualisation [Matplotlib v3.8, Python]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Evidence: The simulation was implemented in Python using standard scientific computing libraries, including NumPy and Matplotlib, with additional functionality from Biopython for lineage tree construction.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

### A cytokine receptor-targeting chimera toolbox for expanding extracellular targeted protein degradation. (PNAS 2026)

- DOI: 10.1073/pnas.2524129123 | PMCID: PMC12846780 | PMID: 41564137
- Evidence: Expression levels were then displayed for relevant cytokine receptors in a heatmap in python using matplotlib.
- Full pipeline: stage not stated [Matplotlib]

### Structural characterization of the HDV virion and its ribonucleoprotein. (PNAS 2026)

- DOI: 10.1073/pnas.2519809123 | PMCID: PMC12846810 | PMID: 41564123
- Evidence: Curves and bar graphs were made using Python with Matplotlib ( 59 ), Pandas ( 60 ), Numpy ( 61 ), and Scipy ( 62 ).
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX, Coot, Matplotlib, NumPy, SciPy, Topaz, UCSF Chimera]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **3.2.1**
- Evidence: Software The following Python (version 3.8.2) software packages were used in the data analysis and in the production of figures: Scipy (version 1.4.1) ( 78 ), pandas (version 1.0.3) ( 79 ), statsmodels (version 0.11.1) ( 80 ), matplotlib (version 3.2.1) ( 81 ), numpy (1.18.3) ( 82 ), seaborn_sinaplot ( 83 ), simanneal (version 0.5.0) ( 71 ), and seaborn (version 0.10.1) ( 84 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Version used: **3.6.2**
- Evidence: HBZ ) using the sc.tl.enrich function in Scanpy were produced using Matplotlib (v3.6.2).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### The connectome of an insect brain. (Science 2023)

- DOI: 10.1126/science.add9330 | PMCID: PMC7614541 | PMID: 36893230
- Evidence: Plotting was performed using matplotlib ( 129 ), Seaborn ( 130 ), and Blender ( https://www.blender.org/ ).
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, SciPy, seaborn]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **3.7.2**
- Evidence: ChIP-seq signal box plots were generated with Python (v3.11.5) ( 120 ), using Pandas (v2.0.3), Matplotlib (v3.7.2), Seaborn (0.12.2), SciPy (1.11.1) and NumPy (v1.24.3) libraries, starting from deep-Tools computeMatrix output values, summing H2A.Z/H2A.Zac ChIP-seq signal across each peak coordinate, dividing it by the input signal and plotting the resulting ratios.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Vaccination with mRNA-encoded nanoparticles drives early maturation of HIV bnAb precursors in humans. (Science 2025)

- DOI: 10.1126/science.adr8382 | PMCID: PMC13164876 | PMID: 40373112
- Evidence: S19 to S35 , S40 to S43 , S46 to S48 , and S52 ) were generated using Python with either Matplotlib ( 99 ) or a custom port of the Seaborn package that incorporates Wilson confidence intervals into the statistical analysis [ ( 100 ); https://github.com/tmsincomb/seaborn-fork ].
- Full pipeline: differential/statistical testing [Matplotlib, seaborn] -> structure determination [AlphaFold, ChimeraX, Coot v0.9.8, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [NumPy]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Software libraries used generally for analysis (of both mouse and human data) include Matplotlib ( 89 ), Pandas ( 90 ), Seaborn ( 91 ), and Scikit-learn ( 92 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

### Rules of engagement for condensins and cohesins guide mitotic chromosome formation. (Science 2025)

- DOI: 10.1126/science.adq1709 | PMCID: PMC12118822 | PMID: 40208986
- Evidence: The resulting sets of particle coordinates were analyzed with Python and visualized with Matplotlib ( 112 ) and Blender 4.0 Python API ( https://www.blender.org ).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib] -> stage not stated [NetworkX]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Version used: **3.8.1**
- Evidence: Other plots were made using a combination of matplotlib (3.8.1) and seaborn (0.13.0) libraries in Python.
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

