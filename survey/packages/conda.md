# Conda

- **Category:** workflow
- **Papers in survey:** 27
- **Journals:** PNAS (14), Nature (10), Cell (3)
- **Years:** 2021 (4), 2022 (5), 2023 (6), 2024 (3), 2025 (5), 2026 (4)
- **Versions named:** 2020.11 (1), 2020.02 (1)
- **Pipeline stages it appears in:** visualisation (2), dimensionality reduction/clustering (1), simulation/modelling (1), machine learning (1), differential/statistical testing (1)

## Papers

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...altic Python library https://github.com/evogytis/baltic N/A Artic sequencing bioinformatic pipeline Artic network https://artic.network/ncov-2019 N/A Miniconda Anaconda http://www.anaconda.com Anaconda Version 2-2.4.0 Miniconda Version 4.9.0 Folding@home Shirts and Pande, 2000 ; Zimmerman et al., 2020 N/A IPython Perez and Granger, 2007 Version 7.14.0 Jupyter Notebook Kluyver et al., 2016 Version ...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### A serotonergic axon-cilium synapse drives nuclear signaling to alter chromatin accessibility. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.026 | PMCID: PMC9789380 | PMID: 36055200
- Evidence: ...gej.net/software/fiji/ Prism v9.2 Graphpad Software https://www.graphpad.com MATLAB 2020b, 2021a The MathWorks https://www.mathworks.com/ Python 3.8 (Anaconda) Anaconda https://www.anaconda.com/ DABEST Ho et al., 2019 https://acclab.github.io/DABEST-python-docs/index.html OrientationJ Püspöki et al., 2016 ; Rezakhaniha et al., 2012 https://github.com/Biomedical-Imaging-Group/OrientationJ VAST Lite...
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python] -> simulation/modelling [ImageJ] -> stage not stated [Conda, Fiji, PHENIX]

### Structural evolution of fibril polymorphs during amyloid assembly. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.025 | PMCID: PMC7617692 | PMID: 38134875
- Evidence: 72 https://imagej.nih.gov/ij/ Prism9 GraphPad https://www.graphpad.com/how-to-buy/ ChimeraX-1.5 UCSF 56 https://www.cgl.ucsf.edu/chimerax/download.html PyMol V2.3.2 Schrödinger https://pymol.org/2/ Anaconda (Python3) ANACONDA https://www.anaconda.com/download FoldX FoldX consortium (EMBL) https://foldxsuite.crg.eu/ Eisenberg/Sawaya free energy calculation Bash script provided by Michael Sawaya, UC...
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND v4.16, ChimeraX, Conda, PyMOL]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: Analyses and plots were produced with the Anaconda package v.4.7.12, and 3D structure visualizations were produced with POV Ray, v.3.7 ( http://www.povray.org/download/ ).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### Functional antibodies exhibit light chain coherence. (Nature 2022)

- DOI: 10.1038/s41586-022-05371-z | PMCID: PMC9607724 | PMID: 36289331
- Evidence: A reproducible Conda environment, scripts to generate these files, and simulation data are provided at https://plus.figshare.com/articles/dataset/Dataset_supporting_Functional_antibodies_exhibit_light_chain_coherence_/20338177?file=36354231 .
- Full pipeline: simulation/modelling [Conda]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Evidence: The following packages and software were used in data analysis: UCSF ChimeraX 1.0, ImageJ 1.51, MATLAB R2019b, R 4.0.4, RStudio 1.4.1106, Jupyter Notebook 6.0.3, Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-i...
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: Glutamate image analysis In situ experiments We first developed an analytical pipeline called AstroGlu as an application program interface within a Python v.3.7.6 virtual environment (venv) running Jupyter Lab/Notebook (Anaconda; Jupyterhub v.1.0.0) on an Ubuntu v.18.04.4 server (CPU, 48 cores; RAM, 1 TB; storage, 2 TB solid-state driver; GPU, NVIDIA Quadro P5000).
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### FXR inhibition may protect from SARS-CoV-2 infection by reducing ACE2. (Nature 2023)

- DOI: 10.1038/s41586-022-05594-0 | PMCID: PMC9977684 | PMID: 36470304
- Evidence: The 10X raw data (fastq files) have been deposited in the repository ArrayExpress with the accession number E-MTAB-8495 . scRNA-seq data were analysed using Anaconda-Navigator v.1.9.12, Jupyter Notebook v.6.0.3 and Rstudio v.1.1.463.
- Full pipeline: stage not stated [Conda, Jupyter]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Evidence: Computational analysis environment Except where otherwise noted, analysis was performed in Conda environments and choreographed with Snakemake 72 running in an LSF 965 or Univa Grid Engine batch control system (Supplementary Table 3 ).
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Elementary 3D organization of active and silenced E. coli genome. (Nature 2025)

- DOI: 10.1038/s41586-025-09396-y | PMCID: PMC12460168 | PMID: 40804527
- Evidence: Data processing was conducted using the nf-core/rnaseq (v3.16.0) workflow (10.5281/zenodo.1400710), part of the nf-core collection 69 , utilizing reproducible software environments from Bioconda 70 and Biocontainers 71 .
- Full pipeline: alignment/mapping [BWA] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [BEDTools, Conda, HOMER v4.11.1]

### Limited thermal tolerance in tropical insects and its genomic signature. (Nature 2026)

- DOI: 10.1038/s41586-026-10155-w | PMCID: PMC12999521 | PMID: 41781608
- Evidence: Anaconda PowerShell was used to create a conda environment and Python programming language (v.3.13) to run the script 66 .
- Full pipeline: structure determination [phytools] -> visualisation [phytools] -> stage not stated [AlphaFold, BUSCO, Conda]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: RNA-seq data processing Raw bulk RNA-seq data were processed using nf-core/rnaseq v3.18.0 (10.5281/zenodo.1400710) of the nf-core collection of workflows 66 , using reproducible software environments from the Bioconda 67 and Biocontainers 68 projects.
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Evidence: The MetaPhlAn code for the taxonomic profiling is available at GitHub ( https://github.com/biobakery/MetaPhlAn ), Zenodo (10.5281/zenodo.17236261) 70 and Bioconda ( https://bioconda.github.io/recipes/metaphlan/README.html ).
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### Deep learning for early warning signals of tipping points. (PNAS 2021)

- DOI: 10.1073/pnas.2106140118 | PMCID: PMC8488604 | PMID: 34544867
- Version used: **2020.02**
- Evidence: The code was written using TensorFlow 2.0 in Anaconda 2020.02.
- Full pipeline: simulation/modelling [SciPy] -> stage not stated [Conda v2020.02, TensorFlow v2.0]

### Structural basis for selective AMPylation of Rac-subfamily GTPases by <i>Bartonella</i> effector protein 1 (Bep1). (PNAS 2021)

- DOI: 10.1073/pnas.2023245118 | PMCID: PMC8000347 | PMID: 33723071
- Evidence: Fitting of single-substrate kinetic measurements by the Michaelis–Menten equation was developed in python 3 with standard modules provided in the Anaconda distribution.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Conda]

### Estimating bonobo (<i>Pan</i><i>paniscus</i>) and chimpanzee (<i>Pan</i><i>troglodytes</i>) evolutionary history from nucleotide site patterns. (PNAS 2022)

- DOI: 10.1073/pnas.2200858119 | PMCID: PMC9170072 | PMID: 35452306
- Evidence: The repository also contains a Conda environment with all software versions and origins, most of which are available through Bioconda ( 74 ).
- Full pipeline: visualisation [ggplot2 v3.3.3] -> stage not stated [BCFtools, Conda, Jupyter, Snakemake]

### <i>Mycobacterium tuberculosis</i> DNA repair helicase UvrD1 is activated by redox-dependent dimerization via a 2B domain cysteine. (PNAS 2022)

- DOI: 10.1073/pnas.2114501119 | PMCID: PMC8872793 | PMID: 35173050
- Evidence: Python 3 was installed via Anaconda along with modules such as numpy, scipy, matpotlib, lmfit, emcee, corner, os, and pandas, and then the globalfit model was used to fit the data for unwinding using the n-step unwinding model and translocation using a two-step dissociation model ( 64 ).
- Full pipeline: stage not stated [Conda, NumPy, Python, SciPy, emcee]

### A synergy between mechanosensitive calcium- and membrane-binding mediates tension-sensing by C2-like domains. (PNAS 2022)

- DOI: 10.1073/pnas.2112390119 | PMCID: PMC8740744 | PMID: 34969839
- Evidence: All image processing and analysis was conducted with the Anaconda distribution of Python (Python ≥ 3.5).
- Full pipeline: stage not stated [Cellpose, Conda, NumPy, PyMOL, Python v3.7, SciPy]

### Genome-wide CRISPRi screen identifies enhanced autolithotrophic phenotypes in acetogenic bacterium <i>Eubacterium limosum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216244120 | PMCID: PMC9963998 | PMID: 36716373
- Evidence: Data were analyzed, and statistical testing (Pearson’s correlation coefficient, two-tailed Student’s t test, Wilcoxon signed-rank test, and Wilcoxon–Mann–Whitney test) performed in Anaconda ( https://www.anaconda.com/ ) and GraphPad Prism v8 software (GraphPad, San Diego, CA).
- Full pipeline: differential/statistical testing [Conda] -> stage not stated [Python]

### Computational design of CRISPR guide RNAs to enable strain-specific control of microbial consortia. (PNAS 2023)

- DOI: 10.1073/pnas.2213154120 | PMCID: PMC9910470 | PMID: 36574681
- Evidence: All programming was performed using Python 3.7, Spyder IDE, and Anaconda software package.
- Full pipeline: stage not stated [Conda, Python v3.7]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Evidence: Analysis of an initial assembly with Flye v2.8.1 ( 91 ) (option: --pacbio-hifi) showed that the genome was probably diploid; therefore, CCS reads were assembled again with the diploid-aware assembler Falcon (Bioconda package pb-falcon 2.2.4 installed with package pb-assembly v0.0.8) ( 92 ) using a relatively low identity threshold of 0.96 for collapsing heterozygosity (option: overlap_filtering_se...
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Version used: **2020.11**
- Evidence: Model-based analysis for ChIP-Seq (MACS2) callpeak (Version 2.2.7.1) in Python (Anaconda 2020.11) was used to distinguish any peaks from background observed in all samples ( 48 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### Anellovirus protein encoded by &lt;i&gt;ORF2/3&lt;/i&gt; functions as the viral replication initiation protein. (PNAS 2025)

- DOI: 10.1073/pnas.2516306122 | PMCID: PMC12772153 | PMID: 41433061
- Evidence: Sequencing reads were processed using nf-core/rnaseq v3.17.0 (DOI: 10.5281/zenodo.1400710 ) of the nf-core collection of workflows ( 77 ), utilizing reproducible software environments from the Bioconda ( 78 ) and Biocontainers ( 79 ) projects.
- Full pipeline: alignment/mapping [SAMtools v1.20, StringTie v2.2.3] -> quantification [SAMtools v1.20, StringTie v2.2.3] -> stage not stated [AlphaFold, Conda, fastp v0.23.4]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Evidence: Data exploration, transformation, visualization, and analysis were conducted using Jupyter Lab (version 0.35.4; https://jupyter.org/ ) with Python 3.7.3, running via Anaconda Distribution 4.6.14 ( https://www.anaconda.com ).
- Full pipeline: quantification [CellProfiler] -> visualisation [Conda, Jupyter, Python v3.7.3] -> stage not stated [ImageJ, Matplotlib v3.0.3, NumPy v1.16.3, SciPy v1.2.1, seaborn v0.9.0]

### Genome-wide strand-specific UV mutagenesis in &lt;i&gt;&lt;i&gt;Escherichia coli&lt;/i&gt;&lt;/i&gt; is directed by the Mfd translocase. (PNAS 2025)

- DOI: 10.1073/pnas.2523368122 | PMCID: PMC12646321 | PMID: 41231941
- Evidence: All steps were executed using a reproducible Snakemake ( 31 ) workflow, with isolated software environments managed through Conda.
- Full pipeline: read trimming [STAR v2.7, Trimmomatic] -> alignment/mapping [SAMtools, STAR v2.7] -> normalisation [deepTools] -> stage not stated [Conda, Snakemake]

### A deep learning-enabled smart garment for accurate and versatile monitoring of sleep conditions in daily life. (PNAS 2025)

- DOI: 10.1073/pnas.2420498122 | PMCID: PMC11848432 | PMID: 39932995
- Evidence: Network training was conducted using Python 3.8.13, Miniconda 3, and PyTorch 2.0.1 in a performance-optimized environment.
- Full pipeline: machine learning [Conda, PyTorch v2.0.1, Python v3.8.13]

### Distinct impact of PI(4)P flux on PI(4,5)P&lt;sub&gt;2&lt;/sub&gt; steady states and oscillations. (PNAS 2026)

- DOI: 10.1073/pnas.2518354123 | PMCID: PMC12933082 | PMID: 41701834
- Evidence: Image stacks were analyzed using a combination of standard library functions and custom-written routines in Python (version 3.10.12, Anaconda distribution) and MATLAB (R2023b, MathWorks), together with built-in routines in Fiji ( 89 ) (version 2.3.0/1.53t, ImageJ distribution).
- Full pipeline: stage not stated [Conda, ImageJ, Python v3.10.12]

