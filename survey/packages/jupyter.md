# Jupyter

- **Category:** workflow
- **Papers in survey:** 110
- **Journals:** PNAS (52), Nature (50), Cell (7), Science (1)
- **Years:** 2021 (6), 2022 (19), 2023 (30), 2024 (24), 2025 (24), 2026 (7)
- **Versions named:** 7.34.0 (1), 7.31 (1), 7.3.10 (1), 5.1 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (9), visualisation (9), simulation/modelling (7), differential/statistical testing (6), machine learning (3), quality control (3), normalisation (1), structure determination (1), read trimming (1)

## Papers

### A global metagenomic map of urban microbiomes and antimicrobial resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.002 | PMCID: PMC8238498 | PMID: 34043940
- Evidence: In addition to general-purpose data analysis tools, essentially all analysis in this paper is available as a series of Jupyter notebooks.
- Full pipeline: read trimming [BLAST, Bowtie2 v2.3.0] -> dimensionality reduction/clustering [R, UMAP] -> structure determination [R] -> visualisation [UMAP] -> stage not stated [Jupyter, SciPy]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...da Anaconda http://www.anaconda.com Anaconda Version 2-2.4.0 Miniconda Version 4.9.0 Folding@home Shirts and Pande, 2000 ; Zimmerman et al., 2020 N/A IPython Perez and Granger, 2007 Version 7.14.0 Jupyter Notebook Kluyver et al., 2016 Version 6.1.5 MDAnalysis Michaud-Agrawal et al., 2011 ; Gowers et al., 2016 Version 1.0.0 NumPy https://numpy.org Version 1.19.1 OpenMM Eastman et al., 2017 Version ...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: The Jupyter notebook used to perform such an analysis is available at: https://github.com/MChavent/Hbond-analysis .
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### A pseudovirus system enables deep mutational scanning of the full SARS-CoV-2 spike. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.001 | PMCID: PMC9922669 | PMID: 36868218
- Evidence: The dms-vep-pipeline consists of a series of Snakemake 72 rules that run Python scripts or Jupyter notebooks, and specifies a conda environment that provides details on the software used for the analysis.
- Full pipeline: stage not stated [Jupyter, Nextstrain, Python, Snakemake]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Evidence: ...e Of Life (iTOL) v5 https://doi.org/10.1093/nar/gkae268 https://itol.embl.de/ Python v3.9 Python https://www.python.org/downloads/release/python-390/ Jupyter Notebook v6.5.2 Jupyter Notebook https://jupyter-notebook.readthedocs.io/en/v6.5.2/ R v.3.6.3 The Comprehensive R Archive Network https://cran.r-project.org/ R packages N/A seqinr v.4.2.5, tidyverse, v.1.3.1, knitr v.1.33, ggpubr v.0.4.0, Des...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Synthetic protein circuits for programmable control of mammalian cell death. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.031 | PMCID: PMC11127782 | PMID: 38657604
- Evidence: For plots that required coding, we used the Jupyter Notebook ( jupyter.org ) with the assistance of ChatGPT (version 4, OpenAI).
- Full pipeline: visualisation [ImageJ, Matplotlib, PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.2, Jupyter]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: Most analysis was carried out in Jupyter notebooks 185 , and all scripts and additional data are available on Zenodo Supplemental Data.
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: Jupyter notebooks are available for data preprocessing, clustering and visualization, and cell annotation, as well as for TCR analysis, at https://github.com/bedapub/PD1-IL2v_in-vivo_TILs_Panc02_publication .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### Rapid shifting of a deep magmatic source at Fagradalsfjall volcano, Iceland. (Nature 2022)

- DOI: 10.1038/s41586-022-04981-x | PMCID: PMC9477742 | PMID: 36104557
- Evidence: A Jupyter Notebook is supplied in the Supplementary Information with the scripts used to perform the calculations.
- Full pipeline: stage not stated [Jupyter]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: The integration of imaging and the automated fluidics delivery system was controlled by custom-written scripts in µManager and Python using Jupyter notebooks.
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: The computer code used is at https://github.com/jbloomlab/2B06_DMS , and the Jupyter notebook that performed most of the analysis is at https://github.com/jbloomlab/2B06_DMS/blob/master/analysis_notebook.ipynb .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### Evidence for European presence in the Americas in AD 1021. (Nature 2022)

- DOI: 10.1038/s41586-021-03972-8 | PMCID: PMC8770119 | PMID: 34671168
- Evidence: The pattern-matching analyses are predominantly carried out using Python 3 in Jupyter Notebook 6.3.0.
- Full pipeline: stage not stated [Jupyter, Python]

### A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06812-z | PMCID: PMC10719114 | PMID: 38092916
- Evidence: Additionally, the Allen Brain Cell Atlas provides valuable links to related resources, including an open source project repository for data download, complete with comprehensive documentation and a Jupyter Notebook that illustrates data retrieval and analysis techniques (available at https://alleninstitute.github.io/abc_atlas_access/intro.html ).
- Full pipeline: quantification [UMAP] -> normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [Cellpose, Jupyter, WGCNA, limma, scDblFinder]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: We also provide information about annotated Jupyter notebooks in the Code availability section, detailing the functions and parameters used in each step.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Landscape dynamics and the Phanerozoic diversification of the biosphere. (Nature 2023)

- DOI: 10.1038/s41586-023-06777-z | PMCID: PMC10700141 | PMID: 38030724
- Evidence: We also provide a series of Jupyter notebooks used for processing the datasets and model outputs that can be followed to reproduce some of the figures presented in the paper, which can be accessed from https://github.com/Geodels/paleoPhysiography .
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [Jupyter]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: Analysis software All data analysis was carried out using Python code in Jupyter IPython 56 Notebooks.
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Preserved neural dynamics across animals performing similar behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06714-0 | PMCID: PMC10665198 | PMID: 37938772
- Evidence: All the result panels are reproducible by running Jupyter notebooks.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, Kilosort v2.0, Matplotlib, NumPy, Python, SciPy]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Evidence: The following packages and software were used in data analysis: UCSF ChimeraX 1.0, ImageJ 1.51, MATLAB R2019b, R 4.0.4, RStudio 1.4.1106, Jupyter Notebook 6.0.3, Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-i...
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: Glutamate image analysis In situ experiments We first developed an analytical pipeline called AstroGlu as an application program interface within a Python v.3.7.6 virtual environment (venv) running Jupyter Lab/Notebook (Anaconda; Jupyterhub v.1.0.0) on an Ubuntu v.18.04.4 server (CPU, 48 cores; RAM, 1 TB; storage, 2 TB solid-state driver; GPU, NVIDIA Quadro P5000).
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### A spatially resolved timeline of the human maternal-fetal interface. (Nature 2023)

- DOI: 10.1038/s41586-023-06298-9 | PMCID: PMC10356615 | PMID: 37468587
- Evidence: An intuitive, easy-to-use Jupyter Notebook interface was created to allow for easy implementation of this algorithm.
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [limma, scikit-learn] -> stage not stated [ImageJ, Jupyter, Python, QuPath v0.4.0, R]

### Gap junctions desynchronize a neural circuit to stabilize insect flight. (Nature 2023)

- DOI: 10.1038/s41586-023-06099-0 | PMCID: PMC10232364 | PMID: 37225999
- Evidence: Data were further analysed using Spike2, and custom Python routines were created using Jupyter notebook to count pattern probabilities and create phase histograms.
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, Python, SciPy, seaborn]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: Manual curation was performed using Jupyter notebooks available at GitHub ( https://github.com/human-pangenomics/hpp_production_workflows/tree/master/assembly/y1-notebooks ).
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### COVID-19 amplified racial disparities in the US criminal legal system. (Nature 2023)

- DOI: 10.1038/s41586-023-05980-2 | PMCID: PMC10172107 | PMID: 37076624
- Evidence: Code availability The Python code to reproduce the analyses and construction of the database is available at GitHub ( https://github.com/jkbren/incarcerated-populations-data ) and at Zenodo 6 ; these repositories contain several Jupyter notebooks with analyses and tutorials on how to automate the collection of some of the data used here.
- Full pipeline: stage not stated [Jupyter]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Evidence: Data visualization Plots were generated using matplotlib (version 3.3.2), seaborn (version 0.11.0) and plotly (version 5.6.0) packages in Python software (version 3.7.12), Jupyter notebook (version 6.1.4), RStudio (version 1.4) and Adobe Illustrator (version 26.4.1) software.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: We implemented and tested CellOracle in Python (versions 3.6 and 3.8) and designed it for use in the Jupyter notebook environment.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Early Release Science of the exoplanet WASP-39b with JWST NIRCam. (Nature 2023)

- DOI: 10.1038/s41586-022-05590-4 | PMCID: PMC9946836 | PMID: 36623551
- Evidence: Methods As part of this article’s Reproducible Research Compendium, located on Zenodo at 10.5281/zenodo.7101283, we provide saved outputs from various pipeline stages and the data used to generate relevant figures, as well as a Jupyter Notebook with step-by-step data reduction instructions replicating our chosen analysis (10.5281/zenodo.7510106).
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Jupyter, PyMC, PyMC3]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: Data analysis and visualization Bulk DNA-seq and RNA-seq data were analysed using Python (v.3) and R (v.3.6.1) in Jupyter Notebook (v.6.0.1).
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### FXR inhibition may protect from SARS-CoV-2 infection by reducing ACE2. (Nature 2023)

- DOI: 10.1038/s41586-022-05594-0 | PMCID: PMC9977684 | PMID: 36470304
- Evidence: The 10X raw data (fastq files) have been deposited in the repository ArrayExpress with the accession number E-MTAB-8495 . scRNA-seq data were analysed using Anaconda-Navigator v.1.9.12, Jupyter Notebook v.6.0.3 and Rstudio v.1.1.463.
- Full pipeline: stage not stated [Conda, Jupyter]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: Fastq files were converted to <Sample>_S1_L001_R1_001.fastq.gz format to be compatible with Cell Ranger. scRNA-seq quality control, data integration and annotation Jupyter notebooks used for data quality control, preprocessing, integration and annotations are available in the GitHub repository for this manuscript (Code availability).
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: Jupyter notebooks and scripts to reproduce the analysis are available at https://github.com/theislab/neural_organoid_atlas .
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Coral photosymbiosis on Mid-Devonian reefs. (Nature 2024)

- DOI: 10.1038/s41586-024-08101-9 | PMCID: PMC11655356 | PMID: 39443794
- Evidence: All analyses were conducted using Python3 on a Jupyter Notebook (v.5.7.4).
- Full pipeline: visualisation [Matplotlib, seaborn] -> stage not stated [Jupyter]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Evidence: Immunostained cells were counted with Jupyter Notebook in Python 3.
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Evidence: Statistical and graphical analyses were performed in Jupyter Notebooks, running a custom Python environment built as described in the single cell sequencing analysis section.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Version used: **7.3.10**
- Evidence: Numerical calculations for the thermodynamic model Numerical calculations were done using programming language Python v.3.8.10; all code was run using IPython v.7.3.10.
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Evidence: Single-molecule data interpretation Raw data exported from LUMICKS Bluelake as .h5 files were processed with custom-written Jupyter Notebooks in Python 3.9 using LUMICKS Pylake v.1.2.1, numpy v.1.26.0, matplotlib v.3.7.2, scipy v.1.11.3 and peakutils v.1.3.4 ( https://github.com/singlemoleculegroup ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### Symbolic recording of signalling and cis-regulatory element activity to DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07706-4 | PMCID: PMC11357993 | PMID: 39020177
- Evidence: With the Jupyter notebook provided, all results and figures in the manuscript are fully reproducible.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.3] -> alignment/mapping [Cutadapt, STAR v2.7.3] -> differential/statistical testing [DESeq2, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Jupyter]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Evidence: Syntenic blocks were used to query pairwise peptide differences among progenitor alleles, determine divergence among progenitor orthologs using S. bicolor syntenic anchors and search for progenitor specific orthogroups (scripts, PID_calc.R; GENESPACE_orthogroupParsing.R; Jupyter Notebook: r570_orthogroupProgenitorAnalysis_forSupp.ipynb).
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Evidence: The count matrix was imported into a Jupyter notebook with pandas: peaks = pd.read_csv("merged_peaks.counts.txt", sep = "\t", index_col = "Geneid"), scaled with sklearn.preprocessing.StardardScaler: peaks_scaled = StandardScaler().fit_transform(peaks), which was then used to create the UMAP: peaks_scaled_mapper = umap.UMAP(n_neighbors=15, random_state=42).fit(peaks_scaled), and plotted using umap....
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Evidence: Signal analyses were performed in Python (v.3.0.0) using JupyterLab (v.3.6.7, Project Jupyter).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### Modern sea-level rise breaks 4,000-year stability in southeastern China. (Nature 2025)

- DOI: 10.1038/s41586-025-09600-z | PMCID: PMC12545208 | PMID: 41094134
- Evidence: Code availability PaleoSTeHM, the software used for spatiotemporal hierarchical modelling, along with several Jupyter Notebook-based tutorials for spatiotemporal hierarchical modelling, are available at https://github.com/radical-collaboration/PaleoSTeHM , which is archived on Zenodo with the identifier 10.5281/zenodo.15382745 (ref.
- Full pipeline: stage not stated [Jupyter]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Evidence: A Jupyter notebook was used to further cross-referenced protein IDs with locus tag information from associated annotation files.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### Learning the natural history of human disease with generative transformers. (Nature 2025)

- DOI: 10.1038/s41586-025-09529-3 | PMCID: PMC12589094 | PMID: 40963019
- Evidence: Code availability Code for Delphi and accompanying scripts and Jupyter notebooks are available at GitHub ( https://github.com/gerstung-lab/delphi ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Jupyter, PyTorch, Python, scikit-learn]

### Patterned invagination prevents mechanical instability during gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09480-3 | PMCID: PMC12527948 | PMID: 40903575
- Evidence: We performed the data wrangling, statistical analyses and plotting in R (v4.2.1) 61 using R Markdown notebooks in RStudio (v2022.7.2.576) 62 , and in Python (v3.10.7) using Jupyter notebooks (v6.5.4) 63 .
- Full pipeline: differential/statistical testing [Jupyter, Python v3.10.7, R v4.2.1] -> visualisation [Fiji v2.16.0, ImageJ v2.16.0] -> stage not stated [ilastik v1.3.3b]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Other software Python coding (using Python v3.11.0) was performed in Jupyter Notebook.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Calving-driven fjord dynamics resolved by seafloor fibre sensing. (Nature 2025)

- DOI: 10.1038/s41586-025-09347-7 | PMCID: PMC12350177 | PMID: 40804151
- Evidence: Data availability Data and Jupyter Notebooks for reproducing the analysis of this study are available at Zenodo 73 (10.5281/zenodo.15353304).
- Full pipeline: stage not stated [Jupyter, emcee]

### Light-microscopy-based connectomic reconstruction of mammalian brain tissue. (Nature 2025)

- DOI: 10.1038/s41586-025-08985-1 | PMCID: PMC12158774 | PMID: 40335689
- Evidence: A Jupyter notebook for performing FFN inference on LICONN data is available at https://github.com/google/ffn/blob/master/notebooks/ (git hash: 12d680e).
- Full pipeline: machine learning [PyTorch v1.12.1] -> stage not stated [BigStitcher, Jupyter, NumPy, Python v3.8, SciPy, scikit-image, seaborn]

### Native nucleosomes intrinsically encode genome organization principles. (Nature 2025)

- DOI: 10.1038/s41586-025-08971-7 | PMCID: PMC12240700 | PMID: 40335690
- Evidence: All analysis details are available and documented as IPython notebooks in our Github repository ( https://github.com/spark159/condense-seq ).
- Full pipeline: alignment/mapping [Bowtie2, Python] -> simulation/modelling [OpenMM] -> stage not stated [GSEA, Jupyter, scikit-learn]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: These processing steps are detailed and documented in Jupyter notebooks (provided on GitHub at https://github.com/zhumy09/scRNA-seq-for-rice ).
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Evidence: ...2.2), HoloViews (1.15.4), Ipyvolume (0.5.2) and Neuroglancer ( https://github.com/seung-lab/neuroglancer ) were used for graphical visualization; and Jupyter (ipykernel:6.21.2), Docker (23.0.1) and Kubernetes (1.22.11) were used for code development and deployment.
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Connectome-driven neural inventory of a complete visual system. (Nature 2025)

- DOI: 10.1038/s41586-025-08746-0 | PMCID: PMC12119369 | PMID: 40140576
- Evidence: The example Jupyter notebook ( https://github.com/reiserlab/male-drosophila-visual-system-connectome-code/blob/main/src/python-bootcamp/access_skeleton_and_mesh.ipynb ) shows how to store the skeleton as a *.swc file and the mesh as a Wavefront *.obj file.
- Full pipeline: dimensionality reduction/clustering [Python, SciPy] -> structure determination [BigStitcher] -> stage not stated [Jupyter, NumPy, Snakemake]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **7.31**
- Evidence: SL-Smart-seq3xpress data analysis Count matrices were processed with JupyterLab (v.4) notebooks using IPython (v.7.31) using the following modules: pandas (v.1.5.3), numpy (v.1.23.5), scipy (v.1.10.1), scanpy (v.1.7.2), openpyxl (v.3.1.2), matplotlib (v.3.6.3) and seaborn (v.0.12.2).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Engineered receptors for soluble cellular communication and disease sensing. (Nature 2025)

- DOI: 10.1038/s41586-024-08366-0 | PMCID: PMC11839477 | PMID: 39542025
- Evidence: Supplementary Data Supplementary File 1: Jupyter Notebook code for image colocalization analysis and example image.
- Full pipeline: stage not stated [Jupyter, Python]

### Large-scale discovery, analysis and design of protein energy landscapes. (Nature 2026)

- DOI: 10.1038/s41586-026-10465-z | PMCID: PMC13293878 | PMID: 42129553
- Evidence: A Jupyter Notebook for modelling cooperativity from new data, along with a script to derive cooperativity using our precomputed metrics, are available at GitHub ( https://github.com/Rocklin-Lab/mhdx_analysis ).
- Full pipeline: dimensionality reduction/clustering [Snakemake] -> stage not stated [AlphaFold, ColabFold, Jupyter, SciPy]

### Biodiversity resilience in a tropical rainforest. (Nature 2026)

- DOI: 10.1038/s41586-026-10365-2 | PMCID: PMC13128449 | PMID: 41951739
- Evidence: Calculations of resistance, return rate, recovery time and the percentage of relative recovery after 30 years for our data were done in Python 3.11.4 and for the literature data in Python v.3.10.9 in a Jupyter notebook on a notebook server of v.6.5.2.
- Full pipeline: stage not stated [Jupyter, Python, R, SciPy]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **7.34.0**
- Evidence: Data processing, model training and evaluation were implemented in Python using numpy v.2.0.2, tensorflow v.2.19.0, scipy v.1.16.3, statsmodels v.0.14.6, sklearn v.1.6.1, shap v.0.50.0, xgboost v.3.1.2, torch v.2.9.0, pandas v.2.2.2, umap v.0.5.9.post2, pickle v.4.0, pytz v.2025.2, re v.2.2.1, tqdm v.4.67.1, IPython v.7.34.0, json v.2.0.9 and altair v.5.5.0.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Transferable enantioselectivity models from sparse data. (Nature 2026)

- DOI: 10.1038/s41586-026-10239-7 | PMCID: PMC12999503 | PMID: 41673164
- Evidence: Next, molecule-, atom- and bond-level descriptors of the conserved moiety are computed at the spGFN2-xTB level with the xTB-Gaussian wrapper, then collected and processed using our recently reported 56 Get Properties Jupyter notebook.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> stage not stated [Jupyter]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Evidence: Computational analyses Jupyter notebooks executing the analysis workflow and figure generation are available on GitHub ( https://github.com/dbetel/HPCS_LUAD ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Interpreting machine learning models to investigate circadian regulation and facilitate exploration of clock function. (PNAS 2021)

- DOI: 10.1073/pnas.2103070118 | PMCID: PMC8364196 | PMID: 34353905
- Evidence: We provide the code for this in a Jupyter Notebook and instructions to run this code at https://github.com/AHallLab/PredictingCircadianTime .
- Full pipeline: differential/statistical testing [LightGBM, XGBoost] -> machine learning [LightGBM, TensorFlow v2.0.0, XGBoost] -> stage not stated [Jupyter, WGCNA]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Evidence: Read libraries were trimmed, PhiX contamination-filtered, and quality-checked using BBMAP v37.61’s BBDUK feature ( 53 ); parameters used are in SI Appendix , SI Methods and the Jupyter notebook.
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### Active dendrites enable strong but sparse inputs to determine orientation selectivity. (PNAS 2021)

- DOI: 10.1073/pnas.2017339118 | PMCID: PMC8325157 | PMID: 34301882
- Version used: **5.1**
- Evidence: All simulations were performed using NEURON [version 7.4 ( 102 )] and Python (version 2.7/IPython version 5.1).
- Full pipeline: simulation/modelling [Jupyter v5.1, Python v2.7]

### Nonparametric coalescent inference of mutation spectrum history and demography. (PNAS 2021)

- DOI: 10.1073/pnas.2013798118 | PMCID: PMC8166128 | PMID: 34016747
- Evidence: All of the analyses and figures for this paper can be reproduced using Nextflow pipelines ( 76 ) and Jupyter notebooks ( https://jupyter.org ) available in ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> stage not stated [BCFtools, Jupyter, Nextflow, Python]

### Quality assessment and refinement of chromatin accessibility data using a sequence-based predictive model. (PNAS 2022)

- DOI: 10.1073/pnas.2212810119 | PMCID: PMC9907136 | PMID: 36508674
- Evidence: IPython notebooks to reproduce the results are available in https://github.com/Dongwon-Lee/gkmQC-manuscript .
- Full pipeline: quality control [Jupyter] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [LDSC, MACS2, featureCounts]

### Rapid homeostatic modulation of transsynaptic nanocolumn rings. (PNAS 2022)

- DOI: 10.1073/pnas.2119044119 | PMCID: PMC9659372 | PMID: 36322725
- Evidence: Electrophysiology data were acquired with Clampex (Molecular Devices) and analyzed using routines written with scientific python libraries, including numpy, scipy, IPython, and neo ( 43 ). mEPSPs were detected using an implementation of a template-matching algorithm ( 44 , 45 ).
- Full pipeline: stage not stated [ImageJ v1.51n, Jupyter, NumPy, SciPy]

### Suppressors of fixation can increase average fitness beyond amplifiers of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2205424119 | PMCID: PMC9478682 | PMID: 36067304
- Evidence: Data, Materials, and Software Availability Code to reproduce figures and underlying data (Mathematica files/Jupyter notebooks) has been deposited in GitLab ( https://gitlab.gwdg.de/mpievolbio-scicomp/DynamicsOnGraphs_LowMutationRate.git ) ( 51 ).
- Full pipeline: stage not stated [Jupyter]

### Archaeal lipids trace ecology and evolution of marine ammonia-oxidizing archaea. (PNAS 2022)

- DOI: 10.1073/pnas.2123193119 | PMCID: PMC9351445 | PMID: 35905325
- Evidence: Data Availability Preprocessing and postprocessing datasets (XLSX) ( 108 ) as well as Jupyter Notebooks (IPYNB) containing Python codes ( 109 ) that were used for data preparation, statistical and unsupervised clustering analyses, and data visualization are deposited at cited Figshare repositories ( 108 , 109 ) and available at https://github.com/PaleoLipidRR/marine-AOA-GDGT-distribution/ or upon ...
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> differential/statistical testing [Jupyter, Python, SciPy, scikit-learn] -> visualisation [Jupyter]

### Propagation of societal gender inequality by internet search algorithms. (PNAS 2022)

- DOI: 10.1073/pnas.2204529119 | PMCID: PMC9304000 | PMID: 35858360
- Evidence: The data-analysis code (in Python) can be accessed as a Jupyter notebook on GitHub .
- Full pipeline: stage not stated [Jupyter, Python]

### Harnessing interpretable and unsupervised machine learning to address big data from modern X-ray diffraction. (PNAS 2022)

- DOI: 10.1073/pnas.2109665119 | PMCID: PMC9214512 | PMID: 35679347
- Evidence: The GitHub repository provides instructions to install X-TEC as well as three Jupyter notebook tutorials on X-TEC-d, X-TEC-s with label smoothing, and X-TEC-s with peak averaging.
- Full pipeline: stage not stated [Jupyter]

### Estimating bonobo (<i>Pan</i><i>paniscus</i>) and chimpanzee (<i>Pan</i><i>troglodytes</i>) evolutionary history from nucleotide site patterns. (PNAS 2022)

- DOI: 10.1073/pnas.2200858119 | PMCID: PMC9170072 | PMID: 35452306
- Evidence: Code and input data for generating these figures are available in the repositories described above as a Jupyter notebook.
- Full pipeline: visualisation [ggplot2 v3.3.3] -> stage not stated [BCFtools, Conda, Jupyter, Snakemake]

### Simple, fast, and flexible framework for matrix completion with infinite width neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2115064119 | PMCID: PMC9169779 | PMID: 35412891
- Evidence: A full description of the library and an example of how to use our library for image inpainting is provided in Jupyter notebooks in our linked code.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, scikit-image]

### Identification of genetic risk loci and prioritization of genes and pathways for myasthenia gravis: a genome-wide association study. (PNAS 2022)

- DOI: 10.1073/pnas.2108672119 | PMCID: PMC8812681 | PMID: 35074870
- Evidence: Traynor Data Availability Summary GWAS statistics and the programming code used for analysis are deposited as Jupyter notebooks on https://github.com/ruthchia/MyastheniaGravis_AnalysisCode .
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Jupyter, LDSC]

### A complete description of thermodynamic stabilities of molecular crystals. (PNAS 2022)

- DOI: 10.1073/pnas.2111769119 | PMCID: PMC8832981 | PMID: 35131847
- Evidence: All calculations and simulations are performed using readily available and well-documented software, and Jupyter notebooks for analysis are provided in SI Appendix .
- Full pipeline: simulation/modelling [Jupyter] -> stage not stated [Quantum ESPRESSO v6.3]

### Thermochronologic constraints on the origin of the Great Unconformity. (PNAS 2022)

- DOI: 10.1073/pnas.2118682119 | PMCID: PMC8812566 | PMID: 35078936
- Evidence: The empirical Bayes resampling code is available as a Jupyter notebook from https://github.com/kmcdannell/helium-empirical-bayes.git .
- Full pipeline: stage not stated [Jupyter]

### Epistatic models predict mutable sites in SARS-CoV-2 proteins and epitopes. (PNAS 2022)

- DOI: 10.1073/pnas.2113118119 | PMCID: PMC8795541 | PMID: 35022216
- Evidence: Data Availability To ensure reproducibility and access to our results we provide at https://giancarlocroce.github.io/DCA_SARS-CoV-2/ the data generated in the course of this research and a Jupyter notebook to reproduce key figures and guide data analysis.
- Full pipeline: stage not stated [HMMER, Jupyter, Nextstrain, R]

### Identification of a muropeptide precursor transporter from gut microbiota and its role in preventing intestinal inflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2306863120 | PMCID: PMC10756304 | PMID: 38127978
- Evidence: We investigated the F4D5:ABC, the ABC-Am, and ABC-Hb heterodimers predictions using AlphaFold2 (AF2) through the Jupyter Notebook inside Google Collaboratory program called ColabFold.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, Jupyter]

### Machine-guided discovery of a real-world rogue wave model. (PNAS 2023)

- DOI: 10.1073/pnas.2306275120 | PMCID: PMC10691345 | PMID: 37983488
- Evidence: This publication was made possible by the following opensource software stack: JAX ( 57 ), flax ( 58 ), optax ( 59 ), PySR ( 9 ), scikit-learn ( 63 ), PyALE ( 64 ), NumPy ( 65 ), SciPy ( 66 ), matplotlib ( 67 ), Seaborn ( 68 ), pandas ( 69 ), and Jupyter ( 70 ).
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, SciPy, scikit-learn, seaborn]

### The roles of surround inhibition for the intrinsic function of the striatum, analyzed in silico. (PNAS 2023)

- DOI: 10.1073/pnas.2313058120 | PMCID: PMC10636308 | PMID: 37922329
- Evidence: The assembly was parallelized using IPython for parallel computing, running an ipcluster and Snudda with the --parallel option.
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> simulation/modelling [Python]

### Amazon deforestation causes strong regional warming. (PNAS 2023)

- DOI: 10.1073/pnas.2309123120 | PMCID: PMC10636322 | PMID: 37903256
- Evidence: Percentage point forest fraction loss (0 to 100) XGBoost hyperparameters were selected based on a fivefold cross validation grid-search approach, in addition to a manual trial and error approach (see provided Jupyter notebook python code for hyperparameters used).
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [Jupyter] -> stage not stated [Python v3.9.7]

### Systematic identification of conditionally folded intrinsically disordered regions by AlphaFold2. (PNAS 2023)

- DOI: 10.1073/pnas.2304302120 | PMCID: PMC10622901 | PMID: 37878721
- Evidence: Moreover, for IDRs, we find that the structural predictions of full-length proteins from the versions of AlphaFold2 that have been implemented as Jupyter Notebooks on Google Colaboratory ( 6 , 51 ) are generally of lower quality and do not agree well with AFDB ( SI Appendix , Fig.
- Full pipeline: machine learning [AlphaFold, RoseTTAFold] -> stage not stated [Jupyter]

### The total mass, number, and distribution of immune cells in the human body. (PNAS 2023)

- DOI: 10.1073/pnas.2308511120 | PMCID: PMC10623016 | PMID: 37871201
- Evidence: All code is available in Jupyter notebooks at https://gitlab.com/milo-lab-public/distribution-of-immune-cells ( 66 ).
- Full pipeline: stage not stated [Jupyter]

### Circadian ribosome profiling reveals a role for the <i>Period2</i> upstream open reading frame in sleep. (PNAS 2023)

- DOI: 10.1073/pnas.2214636120 | PMCID: PMC10556633 | PMID: 37769257
- Evidence: Statistical analyses were performed in R version 3.4.3, Prism 7.0, and custom Jupyter notebooks version 6.3.
- Full pipeline: differential/statistical testing [Jupyter, R v3.4.3] -> stage not stated [SciPy v1.7]

### An inference model gives insights into innate immune adaptation and repertoire diversity. (PNAS 2023)

- DOI: 10.1073/pnas.2305859120 | PMCID: PMC10515141 | PMID: 37695895
- Evidence: This repository also contains Jupyter notebooks that can be run to reproduce the results presented here.
- Full pipeline: stage not stated [Jupyter]

### Multitasking via baseline control in recurrent neural networks. (PNAS 2023)

- DOI: 10.1073/pnas.2304394120 | PMCID: PMC10437433 | PMID: 37549275
- Evidence: Data, Materials, and Software Availability Jupyter notebooks reproducing the main figures can be found at https://github.com/mazzulab/multitasking ( 53 ).
- Full pipeline: stage not stated [Jupyter]

### Decoupling of catalysis and transition state analog binding from mutations throughout a phosphatase revealed by high-throughput enzymology. (PNAS 2023)

- DOI: 10.1073/pnas.2219074120 | PMCID: PMC10629569 | PMID: 37428919
- Evidence: UMAP ( 99 ) was performed using its implementation in skikit-learn ( 100 ) in a Jupyter notebook (available at the OSF repository).
- Full pipeline: dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [UMAP] -> stage not stated [Python]

### "Helicase" Activity promoted through dynamic interactions between a ssDNA translocase and a diffusing SSB protein. (PNAS 2023)

- DOI: 10.1073/pnas.2216777120 | PMCID: PMC10104510 | PMID: 37011199
- Evidence: Tracking of Cy5-hRPA molecules, mean squared displacement (MSD) of hRPA, and single-molecule diffusion coefficients were calculated in Pylake (v0.12.1, Lumicks) using python scripts (v3.10.5) executed within Jupyter Notebooks.
- Full pipeline: stage not stated [Jupyter]

### Data assimilation in operator algebras. (PNAS 2023)

- DOI: 10.1073/pnas.2211115120 | PMCID: PMC9974492 | PMID: 36800390
- Evidence: This directory also contains a Python Jupyter notebook that reproduces the quantum circuit simulation results in Fig.
- Full pipeline: simulation/modelling [Jupyter]

### Decoding the metabolic response of <i>Escherichia coli</i> for sensing trace heavy metals in water. (PNAS 2023)

- DOI: 10.1073/pnas.2210061120 | PMCID: PMC9963153 | PMID: 36745806
- Evidence: Machine learning algorithms used in the study, PCA, SVM, tSNE, 1D-CNN, and transfer learning, were done using Python in Jupyter Notebook.
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> machine learning [scikit-learn] -> stage not stated [Keras, Python v3.6, TensorFlow]

### BIFROST: A method for registering diverse imaging datasets of the &lt;i&gt;Drosophila&lt;/i&gt; brain. (PNAS 2024)

- DOI: 10.1073/pnas.2322687121 | PMCID: PMC11588091 | PMID: 39541350
- Evidence: In practice, this is best achieved by visualizing the center point of the subvolume dataset template; to do this, we displayed the center z-slice of the dataset template in a Python Jupyter notebook, and drew centered cross-hairs along the remaining two axes.
- Full pipeline: alignment/mapping [scikit-image] -> registration [ANTs, ImageJ] -> visualisation [Jupyter] -> stage not stated [Snakemake]

### &lt;i&gt;Arabidopsis&lt;/i&gt; uses a molecular grounding mechanism and a biophysical circuit breaker to limit floral abscission signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2405806121 | PMCID: PMC11536089 | PMID: 39453742
- Evidence: Unless otherwise noted, all analyses were performed in R 3.6.3 and are included, along with the output of sessionInfo(), as Jupyter Notebooks in the Supplemental Code.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HTSeq, STAR, kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Jupyter, R v3.6, Seurat]

### Optogenetically engineered Septin-7 enhances immune cell infiltration of tumor spheroids. (PNAS 2024)

- DOI: 10.1073/pnas.2405717121 | PMCID: PMC11536090 | PMID: 39441641
- Evidence: We plotted the contact map of septin-7 using Jupyter Notebook.
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [R v3.5.2] -> simulation/modelling [GROMACS] -> visualisation [Jupyter] -> stage not stated [ImageJ v1.52, PyMOL]

### A role for cross-linking proteins in actin filament network organization and force generation. (PNAS 2024)

- DOI: 10.1073/pnas.2407838121 | PMCID: PMC11513903 | PMID: 39405356
- Evidence: Maximum fluorescence intensities and fimbrin and transgelin patch lifetimes were extracted from the trajectories using custom code in Python (3.7) with Jupyter Notebook (Project Jupyter).
- Full pipeline: simulation/modelling [Jupyter, Python v3.7]

### Transition of signal requirement in hematopoietic stem cell development from hemogenic endothelial cells. (PNAS 2024)

- DOI: 10.1073/pnas.2404193121 | PMCID: PMC11294991 | PMID: 39042698
- Evidence: For the velocity analysis, Seurat-generated UMAP was exported to a Jupyter Notebook, and the dynamical model of the scVelo package ( 44 , 45 ) was used to calculate the RNA velocity. scRNA-seq Analysis (E12.5).
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Jupyter, UMAP, scVelo] -> visualisation [Seurat]

### The mechanics of correlated variability in segregated cortical excitatory subnetworks. (PNAS 2024)

- DOI: 10.1073/pnas.2306800121 | PMCID: PMC11252788 | PMID: 38959037
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Jupyter notebooks that run relevant simulations and reproduce the main figures of the paper can be accessed via a publicly available Zenodo repository ( https://doi.org/10.5281/zenodo.11398126 ) ( 46 ).
- Full pipeline: simulation/modelling [Jupyter]

### Rapid, antibiotic incubation-free determination of tuberculosis drug resistance using machine learning and Raman spectroscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2315670121 | PMCID: PMC11194509 | PMID: 38861604
- Evidence: Python (Jupyter Notebook) was used to process spectral data.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [Jupyter]

### Substrate geometry affects population dynamics in a bacterial biofilm. (PNAS 2024)

- DOI: 10.1073/pnas.2315361121 | PMCID: PMC11047097 | PMID: 38621130
- Evidence: Data, Materials, and Software Availability All code (C++, Jupyter notebooks, and Mathematica notebooks), processed image data, and simulation results are available from a GitHub repository ( https://github.com/Dioscuri-Centre/biofilms_on_corrugated_surfaces ) ( 66 ).
- Full pipeline: simulation/modelling [Jupyter]

### Polyphosphate affects cytoplasmic and chromosomal dynamics in nitrogen-starved <i>Pseudomonas aeruginosa</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313004121 | PMCID: PMC11009631 | PMID: 38564631
- Evidence: For each type of fluorescent spot (chromosome origins or GFP- μ NS), we first tuned the input parameters to trackpy using a Jupyter notebook written for this purpose ( 28 ).
- Full pipeline: stage not stated [Jupyter]

### HDX-MS finds that partial unfolding with sequential domain activation controls condensation of a cellular stress marker. (PNAS 2024)

- DOI: 10.1073/pnas.2321606121 | PMCID: PMC10990091 | PMID: 38513106
- Evidence: Downstream analysis and plotting were performed with Jupyter Notebook.
- Full pipeline: stage not stated [Jupyter]

### Lipid shape and packing are key for optimal design of pH-sensitive mRNA lipid nanoparticles. (PNAS 2024)

- DOI: 10.1073/pnas.2311700120 | PMCID: PMC10786277 | PMID: 38175863
- Evidence: Data, Materials, and Software Availability Data, code, and Jupyter Notebooks for reproducing the simulation results presented in this work are deposited on Zenodo ( https://zenodo.org/doi/10.5281/zenodo.10373101 ) ( 56 ).
- Full pipeline: simulation/modelling [Jupyter, NAMD v2.12] -> stage not stated [VMD]

### Intelligent leaching rare earth elements from waste fluorescent lamps. (PNAS 2024)

- DOI: 10.1073/pnas.2308502120 | PMCID: PMC10769842 | PMID: 38147647
- Evidence: The ML model development was performed on the Jupyter Notebook.
- Full pipeline: stage not stated [Jupyter, scikit-learn]

### Carbonate burial regimes, the Meso-Cenozoic climate, and nannoplankton expansion. (PNAS 2025)

- DOI: 10.1073/pnas.2516468122 | PMCID: PMC12704742 | PMID: 41343679
- Evidence: R and Python scripts as well as the Jupyter notebooks used in our pre- and postprocessing workflows are available from the following GitHub link: https://github.com/Geodels/paleoReef .
- Full pipeline: stage not stated [Jupyter, Python]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Evidence: Data exploration, transformation, visualization, and analysis were conducted using Jupyter Lab (version 0.35.4; https://jupyter.org/ ) with Python 3.7.3, running via Anaconda Distribution 4.6.14 ( https://www.anaconda.com ).
- Full pipeline: quantification [CellProfiler] -> visualisation [Conda, Jupyter, Python v3.7.3] -> stage not stated [ImageJ, Matplotlib v3.0.3, NumPy v1.16.3, SciPy v1.2.1, seaborn v0.9.0]

### Delay-facilitated self-assembly in compartmentalized systems. (PNAS 2025)

- DOI: 10.1073/pnas.2515123122 | PMCID: PMC12685093 | PMID: 41289406
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Julia files, CSV data, and Jupyter Notebooks data have been deposited in Code for “Delay-facilitated self-assembly in compartmentalized systems” (DOI: 10.5281/zenodo.15641009 ( 81 )).
- Full pipeline: stage not stated [Jupyter]

### A yeast mating platform for multiplex screening of fungal GPCR-ligand interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2521198122 | PMCID: PMC12582325 | PMID: 41134624
- Evidence: The data processing and ASV count analysis were done in Jupyter notebooks which can be found at https://github.com/Synthetic-Biology-Tools-for-Yeast/Yeast-Mating-Platform .
- Full pipeline: stage not stated [Jupyter]

### Mineral dissolution by dimeric complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2504109122 | PMCID: PMC12541406 | PMID: 41052339
- Evidence: The Jupyter Notebook Python script of a U-Net training example can be found on GitHub: https://uofi.box.com/s/k45wffrq3xf04taa7yeir19cqijyt7of ( 84 ).
- Full pipeline: simulation/modelling [PLUMED] -> machine learning [Jupyter, Keras, Python, TensorFlow] -> stage not stated [ImageJ]

### Basic interactions responsible for thymus function explain the convoluted medulla shape. (PNAS 2025)

- DOI: 10.1073/pnas.2415288122 | PMCID: PMC12207460 | PMID: 40540597
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Mathematica Notebooks, Jupyter Notebooks, Python files, and Comsol files have been deposited in Zenodo ( 82 ).
- Full pipeline: stage not stated [Jupyter]

### A binary trait model reveals the fitness effects of HIV-1 escape from T cell responses. (PNAS 2025)

- DOI: 10.1073/pnas.2405379122 | PMCID: PMC11873823 | PMID: 39970000
- Evidence: This repository also contains Jupyter notebooks that can be run to reproduce our figures and analysis.
- Full pipeline: stage not stated [Jupyter]

### Hidden complexity of α7 nicotinic acetylcholine receptor desensitization revealed by MD simulations and Markov state modeling. (PNAS 2025)

- DOI: 10.1073/pnas.2420993122 | PMCID: PMC11848294 | PMID: 39946538
- Evidence: 2 ); Jupyter Notebooks to reconstruct the MSM in Fig.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Jupyter]

### Cataract-prone variants of γD-crystallin populate a conformation with a partially unfolded N-terminal domain under native conditions. (PNAS 2025)

- DOI: 10.1073/pnas.2410860122 | PMCID: PMC11831119 | PMID: 39899721
- Evidence: All downstream quantitative analysis was performed using Python scripts in Jupyter notebooks.
- Full pipeline: stage not stated [Jupyter, Python]

### Evolutionary remodeling of a remnant GET pathway factor into PEX38, an essential peroxin. (PNAS 2026)

- DOI: 10.1073/pnas.2533726123 | PMCID: PMC12956874 | PMID: 41746722
- Evidence: The analysis pipeline and statistical tools are documented in a Jupyter notebook hosted at https://github.com/ag-warscheid/Tb_PEX38_manuscript , which will be publicly accessible upon publication.
- Full pipeline: differential/statistical testing [Jupyter]

### Class-I myosin responds to changes in membrane tension during clathrin-mediated endocytosis in human induced pluripotent stem cells. (PNAS 2026)

- DOI: 10.1073/pnas.2532817123 | PMCID: PMC12956820 | PMID: 41734073
- Evidence: Events, which are deemed as tracked diffraction-limited spots, were extracted using the MATLAB tracking package, cmeAnalysis, and processed in Python Jupyter Notebooks ( 29 ).
- Full pipeline: stage not stated [Jupyter, Python]

### RNA-activated protein cleavage with a CRISPR-associated endopeptidase. (Science 2022)

- DOI: 10.1126/science.add7450 | PMCID: PMC10028731 | PMID: 36423276
- Evidence: A putative binding site was identified manually in the remaining sequence ( NC_000913.3 :3880776–3880799) and logos were generated from all 13 loci using LogoMaker ( 48 ) in a Jupyter Notebook.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, Coot, Jupyter, MotionCor2, RELION]

