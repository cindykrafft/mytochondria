# Python

- **Category:** general
- **Papers in survey:** 964
- **Journals:** PNAS (514), Nature (360), Cell (60), Science (16), Lancet (14)
- **Years:** 2021 (77), 2022 (165), 2023 (160), 2024 (200), 2025 (260), 2026 (102)
- **Versions named:** 3.7 (27), 3.9 (19), 3.6 (18), 3.8 (14), 3.10 (13), 2.7 (12), 3.0 (7), 3.9.7 (7), 3.10.4 (7), 3.8.5 (5)
- **Pipeline stages it appears in:** differential/statistical testing (78), simulation/modelling (61), visualisation (58), alignment/mapping (50), dimensionality reduction/clustering (37), machine learning (26), quantification (20), structure determination (12), normalisation (12), quality control (6), read trimming (6), registration (3), variant calling (2)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **3.7.8**
- Evidence: ...on 3.4 Hijmans, 2020 https://cran.r-project.org/web/packages/raster R package sf version 0.9 Pebesma, 2018 https://cran.r-project.org/web/packages/sf Python 3.7.8 Van Rossum and Drake, 2009 https://www.python.org/ SCANPY version 1.7.2 Wolf et al., 2018 https://scanpy.readthedocs.io/en/stable/ scVI version 0.6.7 Gayoso et al., 2021 https://scvi-tools.org/ Python package seaborn version 0.10.1 Wasko...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Microenvironment drives cell state, plasticity, and drug response in pancreatic cancer. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.017 | PMCID: PMC8822455 | PMID: 34890551
- Version used: **3.7.4**
- Evidence: Given plate well randomization, raw luminescence data were deconvoluted with an in-house Python script (Python v3.7.4).
- Full pipeline: quality control [RSEM] -> alignment/mapping [GATK v1.6] -> registration [GATK v1.6] -> differential/statistical testing [R v4.0] -> stage not stated [Mutect2 v1.1.45, Picard, Python v3.7.4, Seurat v2.3.4]

### Identification of a therapeutic interfering particle-A single-dose SARS-CoV-2 antiviral intervention with a high barrier to resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.004 | PMCID: PMC8577993 | PMID: 34838159
- Evidence: All simulations were performed in Python.
- Full pipeline: quantification [DESeq2, featureCounts] -> simulation/modelling [Python] -> visualisation [Matplotlib v3.3.3, seaborn v0.11.0] -> stage not stated [ImageJ, NumPy v1.19.4, SciPy v1.5.4]

### The emergence and ongoing convergent evolution of the SARS-CoV-2 N501Y lineages. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.003 | PMCID: PMC8421097 | PMID: 34537136
- Evidence: We combined the results of all these analyses using a Python script and visualized them using several open source libraries in an ObservableHQ notebook ( https://observablehq.com/@spond/n501y-clades ).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> visualisation [Python] -> stage not stated [Pangolin]

### Generation and transmission of interlineage recombinants in the SARS-CoV-2 pandemic. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.014 | PMCID: PMC8367733 | PMID: 34499854
- Evidence: We genotyped these sequences at the set of 22 sites that discriminate B.1.1.7 from its parental lineage (B.1.1) using a custom script in Python ( https://github.com/cov-ert/type_variants ), then discarded sequences with missing data at any of the 22 sites.
- Full pipeline: alignment/mapping [Pangolin, minimap2] -> variant calling [Python] -> structure determination [IQ-TREE v2.1] -> stage not stated [SAMtools, TreeTime]

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: All the morphological clustering analysis was performed in Python with scikit-image ( van der Walt et al., 2014 ), vigra ( http://ukoethe.github.io/vigra/ ), scipy ( Virtanen et al., 2020 ), mahotas ( Coelho, 2012 ), scikit-learn ( Pedregosa et al., 2012 ), networkx ( Hagberg et al., 2008 ), python-louvain ( https://github.com/taynaud/python-louvain ), umap-learn ( McInnes et al., 2018 ), pandas (...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### TDP-43 condensation properties specify its RNA-binding and regulatory repertoire. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.018 | PMCID: PMC8445024 | PMID: 34380047
- Version used: **3.7.3**
- Evidence: Customized downstream analysis of iCLIP data was done using scripts described below, and written in Python 3.7.3.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools] -> quantification [Cutadapt, DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Fiji, ImageJ, Snakemake v5.31.1] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3]

### Functional diversity for body actions in the mesencephalic locomotor region. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.002 | PMCID: PMC8382160 | PMID: 34302739
- Version used: **3.7**
- Evidence: All plots, scripts and analysis were generated or performed in MATLAB v2017b (The Mathworks Inc.), GraphPadPrism7 (GraphPad Inc.), Python 3.7 or KNIME (v3.3.1).
- Full pipeline: differential/statistical testing [R, scikit-learn] -> visualisation [seaborn] -> stage not stated [DeepLabCut, Python v3.7, SciPy, ilastik v1.1.5]

### Genome-wide gene expression tuning reveals diverse vulnerabilities of M. tuberculosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.033 | PMCID: PMC8382161 | PMID: 34297925
- Version used: **2.7.18**
- Evidence: ... This paper Github: https://github.com/rock-lab/vulnerability_2021/ Subread aligner (version 1.6.0) Liao et al., 2013 http://subread.sourceforge.net/ Python (version 2.7.18) van Rossum, 1995 https://www.python.org/ SciPy (version 1.2.2) Virtanen et al., 2020 https://www.scipy.org/ statsmodels (version 0.10.1) Seabold and Perktold, 2010 https://www.statsmodels.org/stable/index.html Rstan (version 2...
- Full pipeline: alignment/mapping [Python v2.7.18, SciPy v1.2.2] -> stage not stated [BLAST, Stan v2.19.3, statsmodels v0.10.1]

### Microbial exposure during early human development primes fetal immune cells. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.039 | PMCID: PMC8240556 | PMID: 34077752
- Version used: **2.7.0**
- Evidence: ...E http://qiime.org/ emperor 1.0 Biocore https://biocore.github.io/emperor/ vegan v2.5.7 CRAN https://cran.r-project.org/web/packages/vegan/index.html Python 2.7.0 Python Software Foundation https://www.python.org/ Python 3.7.0 Python Software Foundation https://www.python.org/ matplotlib 3.2.1 PyPI https://pypi.org/ numpy 1.19.4 PyPI https://pypi.org/ pandas 0.25.3 PyPI https://pypi.org/ seaborn 0...
- Full pipeline: alignment/mapping [pandas] -> dimensionality reduction/clustering [QIIME 2 v1.8.0, R v4.4, UMAP] -> stage not stated [ImageJ, Matplotlib v3.2.1, NumPy v1.19.4, Python v2.7.0, seaborn v0.9.0]

### Profiling SARS-CoV-2 HLA-I peptidome reveals T cell epitopes from out-of-frame ORFs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.046 | PMCID: PMC8173604 | PMID: 34171305
- Version used: **3.7.3**
- Evidence: Scoring pMHC-TCR interactions Tetramer data analysis was performed using Python 3.7.3.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Python v3.7.3, Scanpy v1.6.0]

### Transmission, infectivity, and neutralization of a spike L452R SARS-CoV-2 variant. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.025 | PMCID: PMC8057738 | PMID: 33991487
- Version used: **3.7.9**
- Evidence: Welch’s t test, as implemented in R (version 4.0.3) using the rstatix_0.7.0 package and Python (version 3.7.9) using scipy package (version 1.5.2), was used to compare the N gene C t values between B.1.427/B.1.429 variant and non-B.1.427/B.1.429 groups.
- Full pipeline: alignment/mapping [BLAST, MAFFT, Nextstrain] -> stage not stated [IQ-TREE v1.6, Python v3.7.9, R v4.0, SciPy]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Evidence: NuGen diversity adaptors were removed with a Python script supplied by NuGen “trimRRBSdiversityAdaptCustomers.py” (version 1.11 https://github.com/nugentechnologies/NuMetRRBS ) ( Martin, 2011 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Version used: **3.7.4**
- Evidence: ...B http://www.usadellab.org/cms/?page=trimmomatic MiXCR MI Lanoratory https://mixcr.readthedocs.io/en/master/index.html NumPy NumPy https://numpy.org/ Python 3.7.4 Python Software Foundation https://www.python.org/ Other BD FACS Aria III Cell Sorter BD Biosciences https://www.bdbiosciences.com BD FACS Canto II BD Biosciences https://www.bdbiosciences.com Leica DMI-microscope Leica Biosystem https:/...
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Evidence: By parsing GFF files with custom Python scripts, for each sequence we calculated 3 high-level features, namely number of genes/kb, number of hypothetical proteins/total genes, and 5-kmer relative frequency (4 5 = 1024 kmers).
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: Data and code availability The custom Python scripts for the phylogenetic analysis are accessible via https://github.com/MolecularBioinformatics/Phylogenetic-analysis and were manually curated as described earlier ( Bockwoldt et al., 2019 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### Dynamic 3D proteomes reveal protein functional alterations at high resolution in situ. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.021 | PMCID: PMC7836100 | PMID: 33357446
- Evidence: Using a custom-made PyMOL-Python script, we measured the minimal Euclidean distance in angstroms (Å) between all the atoms of the LiP peptide and those of the substrate or allosteric regulator, if present, or alternatively all the atoms of the peptide or amino acid defining the predicted active site (as reported in the Uniprot database).
- Full pipeline: differential/statistical testing [SciPy, limma] -> stage not stated [AutoDock Vina v1.1.2, Bioconductor, NAMD v2.13, PyMOL v2.4, Python, R, pheatmap, seaborn]

### A brainstem integrator for self-location memory and positional homeostasis in zebrafish. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.022 | PMCID: PMC11605990 | PMID: 36563666
- Evidence: All the statistical analyses were performed using custom-written scripts in Python.
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs]

### Cell-type-specific population dynamics of diverse reward computations. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.019 | PMCID: PMC10387374 | PMID: 36113428
- Evidence: All code was written in Python 3 with Jax for auto-differentiation ( Frostig et al., 2018 ) and is available at https://github.com/google-research/computation-thru-dynamics .
- Full pipeline: quality control [Kilosort v2.5] -> stage not stated [DeepLabCut, Python]

### A serotonergic axon-cilium synapse drives nuclear signaling to alter chromatin accessibility. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.026 | PMCID: PMC9789380 | PMID: 36055200
- Evidence: Permutation tests to compare these two distributions were performed using Mlxtend in Python ( Raschka, 2018 ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python] -> simulation/modelling [ImageJ] -> stage not stated [Conda, Fiji, PHENIX]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **3.6**
- Evidence: WIS cohort: ITS2 sequencing analysis ITS2 read classification pipeline The ITS2 classification pipeline was built with Python 3.6.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Deep mutational scanning identifies SARS-CoV-2 Nucleocapsid escape mutations of currently available rapid antigen tests. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.010 | PMCID: PMC9420710 | PMID: 36084631
- Evidence: Sequencing data analysis and calculation of escape scores Sequences were analyzed using custom scripts in Python and R .
- Full pipeline: structure determination [ChimeraX] -> stage not stated [Python]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Evidence: Mutagenized regions of interest were then extracted using custom Python scripts, followed by translation to amino acid sequences.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Neutralizing immunity in vaccine breakthrough infections from the SARS-CoV-2 Omicron and Delta variants. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.019 | PMCID: PMC8930394 | PMID: 35429436
- Version used: **3.7.10**
- Evidence: Quantification and statistical analysis Statistical analyses and data visualization were performed using R (version 4.0.3) and Python (version 3.7.10).
- Full pipeline: read trimming [BLAST] -> quantification [Python v3.7.10] -> differential/statistical testing [Python v3.7.10] -> visualisation [Python v3.7.10] -> stage not stated [Pangolin, R v4.0, ggplot2, seaborn]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: Following inspection of the PCA scree (knee/elbow) plot, Harmony alignment of samples (n = 140 levels) was performed in Python using the top n = 65 PCs.
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: ...u/new-cgi-bin/site/pages/viral_genome_sequencing_pages/viral_genome_sequencing_data.jsp Automated in-house proviral intactness bioinformatic pipeline in Python Lee et al., 2017 https://github.com/BWH-Lichterfeld-Lab/Intactness-Pipeline Los Alamos National Laboratory (LANL) HIV Sequence Database Hypermut 2.0 Rose and Korber, 2000 https://www.hiv.lanl.gov/content/sequence/HYPERMUT/background.html Pr...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### SARS-CoV-2 Omicron-B.1.1.529 leads to widespread escape from neutralizing antibody responses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.046 | PMCID: PMC8723827 | PMID: 35081335
- Version used: **3.7**
- Evidence: ...ve fitting were done by the standard non-cooperative Hill equation, fitted by nonlinear least-squares regression with two additional parameters using Python 3.7 Zahradnik et al., 2021b N/A IBM SPSS Software 27 IBM https://www.ibm.com mabscape This paper https://github.com/helenginn/mabscape https://snapcraft.io/mabscape Other X-ray data were collected at beamline I03, Diamond Light Source, under p...
- Full pipeline: differential/statistical testing [Python v3.7] -> stage not stated [AlphaFold v0.01, PHENIX, PyMOL]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Data visualization and plots were generated in R with ggplot and pheatmap packages, in GraphPad Prism, and in Python using the scikitimage, matplotlib, and seaborn packages.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Cytoplasmic division cycles without the nucleus and mitotic CDK/cyclin complexes. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.010 | PMCID: PMC10659773 | PMID: 37832525
- Evidence: Python scripts to generate 3D renders of the fly embryo images and to quantify FRET measurements are deposited at GitHub with their accession links listed in the key resources table .
- Full pipeline: quantification [Python] -> stage not stated [ImageJ, SciPy]

### Corticotropin-releasing hormone signaling from prefrontal cortex to lateral septum suppresses interaction with familiar mice. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.010 | PMCID: PMC7615103 | PMID: 37669667
- Version used: **3.10.2**
- Evidence: ...fice Word Microsoft 2019 16.56 Microsoft Office Exel Microsoft 2019 Adobe Illustrator Adobe 2020 v24.1 FIDJI GPL v2 2.3.0/1.53f MATLAB Mathworks 2018 Python 3.10.2 Guppy Lerner Lab 78 1.1.4 Leica Application Suite X Leica v3.7.4 ANY-maze Stoelting Co.
- Full pipeline: stage not stated [Python v3.10.2]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Version used: **3.7**
- Evidence: 0.7.5) in Python 3.7.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Phage-assisted evolution and protein engineering yield compact, efficient prime editors. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.039 | PMCID: PMC10482982 | PMID: 37657419
- Evidence: Python 3 Python https://www.python.org/downloads/ Mutato Mok et al., 2022 61 https://hub.docker.com/r/araguram/mutato/ Scaffold insertion analysis Anzalone et al., 2019 1 Note S1 TDT analysis This paper Note S2 Resource availability Lead contact Please direct requests for resources and reagents to lead contact: David R.
- Full pipeline: stage not stated [AlphaFold, Python]

### Pyramidal neurons form active, transient, multilayered circuits perturbed by autism-associated mutations at the inception of neocortex. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.025 | PMCID: PMC10156177 | PMID: 37071993
- Version used: **3.7.7**
- Evidence: 98 Single-cell RNA sequencing alignment and pre-processing Analysis was performed in Python (v3.7.7).
- Full pipeline: alignment/mapping [Python v3.7.7] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scDblFinder v0.2.1] -> stage not stated [Snakemake v5.19.3]

### The T-cell-directed vaccine BNT162b4 encoding conserved non-spike antigens protects animals from severe SARS-CoV-2 infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.007 | PMCID: PMC10099181 | PMID: 37164012
- Version used: **3.9.15**
- Evidence: ...ersion 8.0.1 BD Biosciences N/A FlowJo v 10.7.2 BD Biosciences N/A cellranger-6.0.1 10x Genomics N/A R v 4.1.0 The R Foundation N/A RStudio Posit N/A Python 3.9.15 Python Software Foundation N/A Scanpy PyPI N/A Scirpy PyPI N/A Muon PyPI N/A Spectrum Mill v BI.07.04.210 The Broad Institute of MIT and Harvard N/A Interactive Peptide Spectral Annotator tool Brademan et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Python v3.9.15, Scanpy]

### Apoptotic cell fragments locally activate tingible body macrophages in the germinal center. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.004 | PMCID: PMC7614509 | PMID: 36868219
- Version used: **3.9**
- Evidence: ...cquisition/bd-facsdiva-software/m/333333/overview Java JRE 17.0.1 Oracle https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html Python 3.9 Python https://www.python.org/downloads/release/python-390/ Mathematical modeling GitHub https://github.com/theimagelab/tbm https://doi.org/10.5281/zenodo.7587414 BioRender BioRender https://biorender.com/ Other Nil Materials availability ...
- Full pipeline: simulation/modelling [ggplot2] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, GSEA v4.2.3, ImageJ, Python v3.9, QuPath, R v4.1, Seurat, edgeR]

### A pseudovirus system enables deep mutational scanning of the full SARS-CoV-2 spike. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.001 | PMCID: PMC9922669 | PMID: 36868218
- Evidence: The dms-vep-pipeline consists of a series of Snakemake 72 rules that run Python scripts or Jupyter notebooks, and specifies a conda environment that provides details on the software used for the analysis.
- Full pipeline: stage not stated [Jupyter, Nextstrain, Python, Snakemake]

### Structural and functional map for forelimb movement phases between cortex and medulla. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.009 | PMCID: PMC9842395 | PMID: 36608651
- Version used: **3.7**
- Evidence: 36 Extracted coordinates were used to plot the distribution of labeled neurons using custom-built scripts in Python 3.7.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [DeepLabCut, Kilosort, Python v3.7, SciPy, TrackMate v6.0.3, scikit-learn]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: The resulting data were analyzed in Python using standard methods implemented in the package Scanpy.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Version used: **3.10**
- Evidence: ....ucsf.edu/chimerax/ Prism 10 GraphPad Software https://www.graphpad.com/features Scikit-learn Pedregosa et al., 2011 70 scikit-learn: machinelearning in Python—scikit-learn 1.5.0documentation Python version 3.10 Python software foundation www.python.org Highlights Potent anti-SARS-CoV-2 mAb VIR-7229 is derived from human memory B cells VIR-7229 uniquely competes with ACE2 and has pan-sarbecovirus ...
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: Efficiency of plaquing (EOP) calculations were calculated as mean(p.f.u.condition)/ mean(p.f.u.negativecontrol) in Python.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Evidence: 107 Custom Python scripts were used to parse the eggNOG outputs to identify the presence of genes or gene functions of interest in each genome.
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Rapid DNA unwinding accelerates genome editing by engineered CRISPR-Cas9. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.031 | PMCID: PMC11658890 | PMID: 38781968
- Evidence: NGS analysis for PAM depletion assays PAM specificity was characterized from FASTQs using a custom Python script.
- Full pipeline: structure determination [Coot v0.9.8.7] -> stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, PHENIX v1.19.2, Python, Topaz, fastp]

### Global, site-resolved analysis of ubiquitylation occupancy and turnover rate reveals systems properties. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.024 | PMCID: PMC11136510 | PMID: 38626770
- Version used: **3.7.1**
- Evidence: Python 3.7.1 N/A https://www.python.org/ Coot v0.9.4.1 Emsley et al.
- Full pipeline: stage not stated [AlphaFold, ComplexHeatmap v2.6.2, PyMOL v2.5.0, Python v3.7.1, R, ggplot2 v3.3.5, tidyverse v1.0.5]

### Macromolecular condensation organizes nucleolar sub-phases to set up a pH gradient. (Cell 2024)

- DOI: 10.1016/j.cell.2024.02.029 | PMCID: PMC11938373 | PMID: 38503281
- Evidence: 104 https://github.com/Pappulab/LASSI Custom Python 3 scripts for plot generation This paper https://zenodo.org/doi/10.5281/zenodo.10661405 EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS Xenopus laevis (frog) oocytes were used for live cell analysis of protein localization in nucleoli and as source material for biochemical purification of mature rRNA.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [BLAST, ImageJ, Python]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: 90 N/A Ingenuity Pathway Analysis Qiagen version 90348151 FlowJo Tree Star LLC version 10.5.3 Wave Agilent Technologies version 2.6.0 QuantaSoft software Bio-Rad Cat#1864011 GraphPad Prism version 9.5.1 MUSCLE Edgar 91 http://www.drive5.com/muscle/ Automated in-house proviral intactness bioinformatic pipeline in Python Lee et al.
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Version used: **3.6**
- Evidence: Data and Statistical analyses Data and statistical analyses were performed in Python 3.6 ( https://www.python.org/downloads/release/python-363/ ), using the packages scipy 139 , numpy 140 , matplotlib 141 , seaborn 142 , pandas 143 , scikit-learn 144 .
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: Quality control and cell filtering For all downstream analysis, we used the Scanpy package (referred to as sc from here on 54 , in Python 184 , 202 in addition to standard Python libraries such as numpy, pandas, matplotlib, csv, os, datetime 186 – 188 .
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: Initial CD8 + foci were segmented using the “Blob finder” tool in Arivis Vision4D, and their spatial coordinates were exported for analysis in Python.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Uncovering phenotypic inheritance from single cells with Microcolony-seq. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.001 | PMCID: PMC12456302 | PMID: 40865524
- Version used: **3.7.12**
- Evidence: The code uses FastQC version v0.11.8 129 for sequence quality control before and after adaptor removal, cutadapt 130 version 3.5 with Python 3.7.12 for adaptor removal, SAMtools 131 version 1.9 for indexing, bwa 132 version 0.7.17-r1188 for mapping.
- Full pipeline: quality control [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> alignment/mapping [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, DESeq2, Prokka, R]

### Inner speech in motor cortex and implications for speech neuroprostheses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.015 | PMCID: PMC12360486 | PMID: 40816265
- Version used: **3.9**
- Evidence: ...ms MATLAB R2023b MathWorks Inc. https://www.mathworks.com/products/matlab.html RRID:SCR_001622 BRAND Ali et al 2024 https://github.com/brandbci/brand Python 3.9 python.org/downloads/ RRID:SCR_008394 SciPy 1.11.4 scipy.org RRID:SCR_008058 NumPy 1.26.2 numpy.org RRID:SCR_008633 Pandas 2.1.3 pandas.pydata.org RRID:SCR_018214 scikit-learn 1.3.2 scikit-learn.org RRID:SCR_002577 matplotlib 3.8.2 matplot...
- Full pipeline: stage not stated [Matplotlib v3.8.2, NumPy v1.26.2, Python v3.9, SciPy v1.11.4, scikit-learn v1.3.2, seaborn v0.13.0]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: We then applied NMF, utilizing the sklearn.decomposition package in Python, to factorize the non-negative matrix V into two smaller non-negative matrices: the basis matrix W (with dimensions N × R ) and the coefficient matrix H (with dimensions R × M ), following methodologies used in prior research.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Quantifying the varying harvest of fermentation products from the human gut microbiota. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.005 | PMCID: PMC12556654 | PMID: 40744013
- Evidence: Chromatography data from the RID detector was recorded for 40min, exported as plain text files, and analyzed using custom Python scripts which have subsequently been released as a standalone software package.
- Full pipeline: stage not stated [Python]

### Human interpretable grammar encodes multicellular systems biology models to democratize virtual cell laboratories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.048 | PMCID: PMC13012569 | PMID: 40713951
- Evidence: To determine colony formation, the entire ECM was imaged in 3D, maximum intensity projections were generated, and colonies were counted using custom ImageJ and Python scripts.
- Full pipeline: dimensionality reduction/clustering [R] -> simulation/modelling [R, ggpubr] -> stage not stated [ImageJ, Python, Seurat v4.1.0]

### Brain endothelial gap junction coupling enables rapid vasodilation propagation during neurovascular coupling. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.030 | PMCID: PMC12337775 | PMID: 40675149
- Evidence: Cell-cell tracer transfer was then quantified using a custom Python script to calculate a ‘coupling index’ metric, defined as the background-corrected intensity ratio of serotonin signal within a given SERT + probe cell / serotonin signal within the most proximal 𝑎 × 3 pixels in a mask of contiguous vasculature, where 𝑎 was set as area of the probe cell.
- Full pipeline: quantification [ImageJ, Python] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.2.4]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: We used a custom implementation of this algorithm written in Python, which can be found in our analysis code repository.
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### Nanoscale DNA tracing reveals the self-organization mechanism of mitotic chromosomes. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.028 | PMCID: PMC12127698 | PMID: 40132578
- Evidence: Cells were analyzed using a custom-written Python script.
- Full pipeline: quantification [NumPy] -> normalisation [SciPy] -> simulation/modelling [NumPy, OpenMM] -> machine learning [scikit-learn] -> stage not stated [Python, napari, scikit-image]

### Contextual computation by competitive protein dimerization networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.036 | PMCID: PMC11973712 | PMID: 39978343
- Version used: **3.8.13**
- Evidence: STAR Methods Method Details All analysis was performed in Python version 3.8.13.
- Full pipeline: stage not stated [NetworkX, Python v3.8.13, SciPy, seaborn v0.12.2]

### Inflammation switches the chemoattractant requirements for naive lymphocyte entry into lymph nodes. (Cell 2025)

- DOI: 10.1016/j.cell.2024.11.031 | PMCID: PMC11845304 | PMID: 39708807
- Evidence: 62 In all cases, redundant reads were removed using FastUniq, 63 and customized Python scripts were used to calculate the fragment length of each pair of uniquely mapped paired-end (PE) reads.
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2 v1.4.2, Metascape] -> visualisation [UMAP] -> stage not stated [R v4.2.1, Seurat v4.3.0, deepTools v3.5.4]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **3.10**
- Evidence: All analyses were conducted in Python 3.10 using anndata 0.11, numpy 1.26, scipy 1.15, and matplotlib 3.10.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### Tracking development assistance for health and for COVID-19: a review of development assistance, government, out-of-pocket, and other private spending on health for 204 countries and territories, 1990-2050. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)01258-7 | PMCID: PMC8457757 | PMID: 34562388
- Version used: **3.7.0**
- Evidence: We completed all the analyses using Stata (versions 13 and 15), R (versions 3.6.0 and 3.6.1), and Python (version 3.7.0).
- Full pipeline: stage not stated [Python v3.7.0, R]

### Redefining β-blocker response in heart failure patients with sinus rhythm and atrial fibrillation: a machine learning cluster analysis. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)01638-x | PMCID: PMC8542730 | PMID: 34474011
- Version used: **3.7.2**
- Evidence: Analyses were performed using the Python library statsmodel (version 0.12.1) on Python (version 3.7.2), and Stata (version 14.2).
- Full pipeline: stage not stated [Python v3.7.2]

### Estimating the cause-specific relative risks of non-optimal temperature on daily mortality: a two-part modelling approach applied to the Global Burden of Disease Study. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)01700-1 | PMCID: PMC8387975 | PMID: 34419204
- Evidence: RRs were calculated in R and Python, PAFs and TMRELs were calculated in R, and burden of disease was calculated in Python.
- Full pipeline: stage not stated [Python]

### Spatial, temporal, and demographic patterns in prevalence of smoking tobacco use and attributable disease burden in 204 countries and territories, 1990-2019: a systematic analysis from the Global Burden of Disease Study 2019. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)01169-7 | PMCID: PMC8223261 | PMID: 34051883
- Version used: **2.7**
- Evidence: We did all analyses using R (versions 3.1–3.6) and Python (version 2.7).
- Full pipeline: stage not stated [Python v2.7, R]

### Measuring the availability of human resources for health and its relationship to universal health coverage for 204 countries and territories from 1990 to 2019: a systematic analysis for the Global Burden of Disease Study 2019. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)00532-3 | PMCID: PMC9168805 | PMID: 35617980
- Version used: **2.7.14**
- Evidence: 32 , 33 Analyses were done with R (version 3.4.4), Python (version 2.7.14), or Stata (version 13.1), and figures were generated with R (version 3.4.4).
- Full pipeline: visualisation [Python v2.7.14, R v3.4.4]

### The burden of diseases, injuries, and risk factors by state in the USA, 1990-2021: a systematic analysis for the Global Burden of Disease Study 2021. (Lancet 2024)

- DOI: 10.1016/s0140-6736(24)01446-6 | PMCID: PMC11694014 | PMID: 39645376
- Evidence: Software packages used in GBD 2021 were Python (versions 3.8.17, 3.10, 3.10.4, and 3.10.12), Stata (versions 13.1, 15, and 15.1), and R (versions 3.5, 3.5.1, and 4.2.1).
- Full pipeline: stage not stated [Python, R]

### National-level and state-level prevalence of overweight and obesity among children, adolescents, and adults in the USA, 1990-2021, and forecasts up to 2050. (Lancet 2024)

- DOI: 10.1016/s0140-6736(24)01548-4 | PMCID: PMC11694015 | PMID: 39551059
- Version used: **3.10.6**
- Evidence: Analyses were completed with R (version 4.4.0) and Python (version 3.10.6).
- Full pipeline: stage not stated [Python v3.10.6, R v4.4.0]

### Global burden and strength of evidence for 88 risk factors in 204 countries and 811 subnational locations, 1990-2021: a systematic analysis for the Global Burden of Disease Study 2021. (Lancet 2024)

- DOI: 10.1016/s0140-6736(24)00933-4 | PMCID: PMC11120204 | PMID: 38762324
- Version used: **3.10.4**
- Evidence: 43 Analyses were completed with Python (version 3.10.4), Stata (version 13.1), and R (version 4.2.1).
- Full pipeline: stage not stated [Python v3.10.4, R v4.2.1]

### Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted life-years (DALYs), and healthy life expectancy (HALE) for 371 diseases and injuries in 204 countries and territories and 811 subnational locations, 1990-2021: a systematic analysis for the Global Burden of Disease Study 2021. (Lancet 2024)

- DOI: 10.1016/s0140-6736(24)00757-8 | PMCID: PMC11122111 | PMID: 38642570
- Version used: **3.10.4**
- Evidence: Analyses were completed using Python (version 3.10.4), Stata (version 13.1), and R (version 4.2.1).
- Full pipeline: stage not stated [Python v3.10.4, R v4.2.1]

### Global burden of 288 causes of death and life expectancy decomposition in 204 countries and territories and 811 subnational locations, 1990-2021: a systematic analysis for the Global Burden of Disease Study 2021. (Lancet 2024)

- DOI: 10.1016/s0140-6736(24)00367-2 | PMCID: PMC11126520 | PMID: 38582094
- Version used: **3.10.4**
- Evidence: 14 Software packages used in the cause-of-death analysis for GBD 2021 were Python (version 3.10.4), Stata (version 13.1), and R (version 4.2.1).
- Full pipeline: stage not stated [Python v3.10.4, R v4.2.1]

### Global age-sex-specific mortality, life expectancy, and population estimates in 204 countries and territories and 811 subnational locations, 1950-2021, and the impact of the COVID-19 pandemic: a comprehensive demographic analysis for the Global Burden of Disease Study 2021. (Lancet 2024)

- DOI: 10.1016/s0140-6736(24)00476-8 | PMCID: PMC11126395 | PMID: 38484753
- Version used: **3.8.17**
- Evidence: Python (version 3.8.17 and 3.10.4), Stata (version 15.1), and R (version 3.5 and 4.2) were used for statistical analysis This manuscript was produced with the GBD Collaborator Network and in accordance with the GBD Protocol.
- Full pipeline: differential/statistical testing [Python v3.8.17, R v3.5]

### Burden of 375 diseases and injuries, risk-attributable burden of 88 risk factors, and healthy life expectancy in 204 countries and territories, including 660 subnational locations, 1990-2023: a systematic analysis for the Global Burden of Disease Study 2023. (Lancet 2025)

- DOI: 10.1016/s0140-6736(25)01637-x | PMCID: PMC12535840 | PMID: 41092926
- Version used: **3.10.4**
- Evidence: The software used for analyses included Python (version 3.10.4), Stata (version 13.1), and R (version 4.2.1).
- Full pipeline: stage not stated [Python v3.10.4, R v4.2.1]

### Global age-sex-specific all-cause mortality and life expectancy estimates for 204 countries and territories and 660 subnational locations, 1950-2023: a demographic analysis for the Global Burden of Disease Study 2023. (Lancet 2025)

- DOI: 10.1016/s0140-6736(25)01330-3 | PMCID: PMC12535839 | PMID: 41092927
- Version used: **3.10.4**
- Evidence: The software used for analyses included Python (version 3.10.4), Stata (version 15.1), and R (versions 4.2 and 4.4).
- Full pipeline: stage not stated [Python v3.10.4, R]

### Disease burden attributable to intimate partner violence against females and sexual violence against children in 204 countries and territories, 1990-2023: a systematic analysis for the Global Burden of Disease Study 2023. (Lancet 2026)

- DOI: 10.1016/s0140-6736(25)02503-6 | PMCID: PMC12775558 | PMID: 41386261
- Version used: **3.10.4**
- Evidence: All analyses were completed in R (version 4.2.1) and Python (version 3.10.4).
- Full pipeline: stage not stated [Python v3.10.4, R v4.2.1]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: To identify and visualize gene expression differences among genes in changing compartments, k -means clustering was performed on triplicate pseudo-replicates of each cell type using a custom Python script (Extended Data Fig.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### Global potential for harvesting drinking water from air using solar energy. (Nature 2021)

- DOI: 10.1038/s41586-021-03900-w | PMCID: PMC8550973 | PMID: 34707305
- Evidence: The JMP national and subnational data were joined to GIS boundaries using a custom geoprocessing tool built in Python and ArcGIS 10.
- Full pipeline: stage not stated [Python]

### The cellular environment shapes the nuclear pore complex architecture. (Nature 2021)

- DOI: 10.1038/s41586-021-03985-3 | PMCID: PMC8550940 | PMID: 34646014
- Evidence: This workflow was performed using a Python script running SciPy.Stats (for P value and Z -score analysis) 51 , the StatsModels module (for Benjamini–Hochberg analysis) 52 and Matplotlib (for plots) 53 .
- Full pipeline: alignment/mapping [IMOD] -> differential/statistical testing [Matplotlib, Python, SciPy] -> stage not stated [RELION, UCSF Chimera]

### Cellular anatomy of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03970-w | PMCID: PMC8494646 | PMID: 34616071
- Version used: **3.7**
- Evidence: In brief, ARA 2D slices were pre-aligned to a subset of CCF slices spaced 100 μm apart, producing a total of 132 slices as in the ARA (using a custom Python 3.7 script).
- Full pipeline: alignment/mapping [Python v3.7] -> stage not stated [Fiji, ImageJ]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Version used: **3.6**
- Evidence: Identification of cCREs For peak calling in the snATAC-seq data, we extracted all the fragments for each cluster, and then performed peak calling on each aggregate profile using MACS2 81 v2.2.7.1. using Python 3.6 with parameter: “--nomodel --shift −100 --ext 200 --qval 1e-2 –B --SPMR”.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### The mouse cortico-basal ganglia-thalamic network. (Nature 2021)

- DOI: 10.1038/s41586-021-03993-3 | PMCID: PMC8494639 | PMID: 34616074
- Evidence: Network analysis The network structure of the dataset was assessed with the Louvain community detection algorithm 52 , obtained from the Brain Connectivity Toolbox ( https://sites.google.com/site/bctnet ), and executed in Python.
- Full pipeline: stage not stated [Python]

### Transposon-associated TnpB is a programmable RNA-guided DNA endonuclease. (Nature 2021)

- DOI: 10.1038/s41586-021-04058-1 | PMCID: PMC8612924 | PMID: 34619744
- Evidence: The Python scripts used in the cleavage position identifications and TAM characterization are provided in the GitHub repository ( https://github.com/tkarvelis/Nuclease_manuscript ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [AlphaFold, Cutadapt, Python]

### Extremely anisotropic van der Waals thermal conductors. (Nature 2021)

- DOI: 10.1038/s41586-021-03867-8 | PMCID: PMC8481126 | PMID: 34588671
- Evidence: Computational methodology Structural models Structural models were created according to an algorithm previously described in literature 59 , which was implemented in Python using the atomic simulation environment package 60 .
- Full pipeline: simulation/modelling [Python] -> stage not stated [ImageJ, LAMMPS]

### RecA finds homologous DNA by reduced dimensionality search. (Nature 2021)

- DOI: 10.1038/s41586-021-03877-6 | PMCID: PMC8443446 | PMID: 34471288
- Evidence: Image analysis Data analysis was done in MATLAB (Mathworks), with the exception of the cell segmentation, which was done in Python.
- Full pipeline: machine learning [PyTorch v1.7.1] -> visualisation [ImageJ] -> stage not stated [Python]

### Highly accurate protein structure prediction with AlphaFold. (Nature 2021)

- DOI: 10.1038/s41586-021-03819-2 | PMCID: PMC8371605 | PMID: 34265844
- Evidence: For neural network construction, running and other analyses, we used TensorFlow 70 , Sonnet 71 , NumPy 72 , Python 73 and Colab 74 .
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [OpenMM v7.3.1] -> machine learning [HMMER, NumPy, OpenMM v7.3.1, Python, TensorFlow]

### Age-related immune response heterogeneity to SARS-CoV-2 vaccine BNT162b2. (Nature 2021)

- DOI: 10.1038/s41586-021-03739-1 | PMCID: PMC8373615 | PMID: 34192737
- Evidence: Immunoglobulin gene use and sequence annotation were performed in IMGT V-QUEST, and repertoire differences were analysed by custom scripts in Python.
- Full pipeline: differential/statistical testing [R v3.5.1] -> stage not stated [Python]

### Experimental quantum speed-up in reinforcement learning agents. (Nature 2021)

- DOI: 10.1038/s41586-021-03242-7 | PMCID: PMC7612051 | PMID: 33692560
- Evidence: A Python script converts the time tags into arrival times, and it iterates through until it finds a coincidence event between either D0 and D1, or D0 and D2/D3.
- Full pipeline: stage not stated [Python]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Version used: **3.9.0**
- Evidence: Enrichment of motifs at and around CLIP regions was performed using the Emboss Compseq 6.0.0 44 , R package ‘randomizeR 2.0.0’ 45 and ‘Random’ 46 module in Python 3.9.0.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### Functional refolding of the penetration protein on a non-enveloped virus. (Nature 2021)

- DOI: 10.1038/s41586-020-03124-4 | PMCID: PMC8297411 | PMID: 33442061
- Evidence: We retrieved rotavirus sequences from GenBank 46 with BioPython 47 , aligned them with MAFFT 48 , and used ESPript 49 to display the multiple sequence alignments of VP4 ( Supplementary Data 1 ), VP7 ( Supplementary Data 2 ), and VP6 ( Supplementary Data 3 ).
- Full pipeline: alignment/mapping [IMOD, MAFFT, MotionCor2, Python] -> registration [MotionCor2] -> structure determination [EMAN2] -> stage not stated [CTFFIND, Matplotlib, PyMOL]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **3.6**
- Evidence: Statistical analysis: Statistical analysis was performed using base R version 3.6.3 with tidyverse version 1.3.0 69 and Python 3.6.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Version used: **2.7**
- Evidence: The simulation was implemented in Python 2.7.
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Pairing of segmentation clock genes drives robust pattern formation. (Nature 2021)

- DOI: 10.1038/s41586-020-03055-0 | PMCID: PMC7932681 | PMID: 33361814
- Evidence: The image analysis pipeline performed in Python (see code availability statement) as previously described 14 .
- Full pipeline: stage not stated [Python]

### Phenotypic variation of transcriptomic cell types in mouse motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-020-2907-3 | PMCID: PMC8113357 | PMID: 33184512
- Evidence: 4 ) using Python scripts from the Allen Software Development Kit (SDK) ( https://github.com/AllenInstitute/AllenSDK ) with some modifications to account for our experimental paradigm ( https://github.com/berenslab/EphysExtraction ).
- Full pipeline: alignment/mapping [STAR v2.5.4b] -> differential/statistical testing [scikit-learn] -> stage not stated [Python]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: We then passed the multiple sequence alignments to the Python module AlignIO from BioPython 87 to create a reference consensus fasta sequence for each set of taxa.
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### Global hotspots of salt marsh change and carbon emissions. (Nature 2022)

- DOI: 10.1038/s41586-022-05355-z | PMCID: PMC9771810 | PMID: 36450979
- Version used: **3.8.10**
- Evidence: We calculated salt marsh anomaly metrics for four 5-year epochs from 2000 to 2019 using a combination of Python 3.8.10 and R 3.6.2.
- Full pipeline: stage not stated [Python v3.8.10, QGIS v3.12.263, R v3.6, ggplot2, tidyverse]

### Dopamine promotes head direction plasticity during orienting movements. (Nature 2022)

- DOI: 10.1038/s41586-022-05485-4 | PMCID: PMC9729112 | PMID: 36450986
- Version used: **3.9.5**
- Evidence: Data analysis Data analysis was carried out using Matlab R2016b, R2017a, R2017b, 2019b, R2020b (MathWorks), Python 3.9.5, R 4.1.0 and RStudio 1.4.1717.
- Full pipeline: stage not stated [Python v3.9.5, R v4.1]

### The neurons that restore walking after paralysis. (Nature 2022)

- DOI: 10.1038/s41586-022-05385-7 | PMCID: PMC9668750 | PMID: 36352232
- Version used: **2.7**
- Evidence: Computer simulations were performed in Python 2.7 using the NEURON simulation environment 83 .
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat, velocyto] -> normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.3, fgsea] -> simulation/modelling [Python v2.7] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **3.9**
- Evidence: For the p35S::H2B.8-scrambledIDR–eGFP , p35S::H2B.8-EWSR1-IDR–eGFP and p35S::H2B.8-TAF15-IDR–eGFP constructs, the scrambledIDR (randomly shuffled amino acid sequence of the IDR by Python 3.9: DEVIQDISANPPVLENEPVTPSEPTVQEDTRECIETPEETPISVPEGEATPETKVQGDNSDFSSQTRTVDLKEVPSVPPREGTPPTPVVDDVE); EWSR1-IDR 31 (ASTDYSTYSQAAAQQGYSAYTAQPTQGYAQTTQAYGQQSYGTYGQPTDVSYTQAQTTATYGQTAYATSYGQPPTGYTTPTAPQAYSQPVQGYGTGAYD...
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### Hydroclimatic vulnerability of peat carbon in the central Congo Basin. (Nature 2022)

- DOI: 10.1038/s41586-022-05389-3 | PMCID: PMC9729114 | PMID: 36323786
- Version used: **3.7.3**
- Evidence: The geospatial analyses and mapping were performed using open source Jupyterhub notebooks (5.7.8; https://jupyter.org/ ) running Python 3.7.3 on server (16 Intel Xeon Gold 52Go RAM calculation core; 18R CPU (2.10 GHz)) with fiona (1.8.20), geocube (0.1.0), geopandas (0.10.1), ipykernel (6.4.1), ipython (7.28.0), jupyter (1.0.0), KDE-diffusion (1.0.3), matplotlib (3.4.3), notebook (6.4.4), numpy (1...
- Full pipeline: alignment/mapping [Python v3.7.3] -> differential/statistical testing [R] -> stage not stated [Matplotlib v3.4.3, NumPy v1.20.3, SciPy v1.7.1]

### Extracellular fluid viscosity enhances cell migration and cancer dissemination. (Nature 2022)

- DOI: 10.1038/s41586-022-05394-6 | PMCID: PMC9646524 | PMID: 36323783
- Version used: **3.8**
- Evidence: Theoretical methods Stochastic model of actin network A stochastic 2D model of actin-based lamellipodia protrusion was constructed in Python v.3.8 using frameworks and public code established in ref.
- Full pipeline: alignment/mapping [HISAT2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Python v3.8, TrackMate]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: Cofilin severing quantification Videos were analysed using custom Python scripts that measured the change in filament intensity over the course of the experiments.
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: Sequence motifs were generated using the selected TAMs in the top scoring fraction with the custom Python script used in our previous report 4 .
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: (4) The aligned sequences from Clustal Omega were used to detect the nucleotide changes between NUMT sequences and mitochondrial reference genome sequences using BioPython 87 .
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### Antibiotic combinations reduce Staphylococcus aureus clearance. (Nature 2022)

- DOI: 10.1038/s41586-022-05260-5 | PMCID: PMC9533972 | PMID: 36198788
- Evidence: Automated image analysis The number of red and green colonies in each microplating spot was counted using a custom Python script 64 , implementing the following steps.
- Full pipeline: dimensionality reduction/clustering [scikit-image] -> stage not stated [Python, SciPy]

### Visualizing translation dynamics at atomic detail inside a bacterial cell. (Nature 2022)

- DOI: 10.1038/s41586-022-05255-2 | PMCID: PMC9534751 | PMID: 36171285
- Version used: **3.7.7**
- Evidence: Tree was reconstructed from the file taxidlineage.dmp in Python v.3.7.7 with ETE3 Toolkit v.3.1.2 (ref.
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> structure determination [Coot, PHENIX, Python v3.7.7] -> visualisation [ChimeraX] -> stage not stated [RELION v3.0]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: TCR analysis was performed in Python with the toolkit scirpy 61 , and clonotypes were determined on the basis of CDR3 sequence identity, with the parameters receptor_arms = "all", dual_ir = "primary_only".
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### Delayed fluorescence from inverted singlet and triplet excited states. (Nature 2022)

- DOI: 10.1038/s41586-022-05132-y | PMCID: PMC9477729 | PMID: 36104553
- Version used: **3.7**
- Evidence: Thus, k r + k nr , k ISC and k RISC were determined without assuming k ISC >> k RISC by fitting the S 1 population in equation ( 1 ) to the transient PL decay data using the scipy.integrate.odeint and scipy.optimize.curve_fit functions in Python 3.7 50 . k r and k nr were determined from Φ PL = k r /( k r + k nr ) assuming negligible non-radiative decay of T 1 to S 0 .
- Full pipeline: stage not stated [Python v3.7, SciPy]

### Large harvested energy with non-linear pyroelectric modules. (Nature 2022)

- DOI: 10.1038/s41586-022-05069-2 | PMCID: PMC9492539 | PMID: 36097191
- Evidence: A Python script governed and synchronized all of the instrumentation (sourcemeter, pump, valves and thermocouples) so that proper Olsen cycles were run, that is, the hot fluid loop started circulating through the PST stack after the sourcemeter had charged them so that they were heated up at the desired applied voltage of a given Olsen cycle.
- Full pipeline: stage not stated [Python]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: Plots were generated using Scanpy (in Python for dot plots and velocity) and Seurat (in R for UMAP plots), as well ggplot2 for the remainder of the plots (in R for bar plots and proportion scatter plots).
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: Statistical analyses Statistical analyses were carried out either in Python, mainly with the libraries Pandas 61 and NumPy 62 , or in R.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Spatial profiling of chromatin accessibility in mouse and human tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05094-1 | PMCID: PMC9452302 | PMID: 35978191
- Evidence: Data visualization We first identified pixels on tissue samples by manual selection from microscopy images using Adobe Illustrator (v.25.4.3) ( https://github.com/rongfan8/DBiT-seq ), and a custom Python script was used to generate metadata files that were compatible with the Seurat workflow for spatial datasets.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [Python, Seurat] -> stage not stated [ArchR, Snakemake]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: The generative process above is implemented in Python code and available as a CLI application that can be accessed at GitHub ( https://github.com/almaan/growmeatissue ).
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### A mechanically strong and ductile soft magnet with extremely low coercivity. (Nature 2022)

- DOI: 10.1038/s41586-022-04935-3 | PMCID: PMC9365696 | PMID: 35948715
- Evidence: The algorithm was constructed using a Python 62 .
- Full pipeline: stage not stated [Python]

### Context-specific emergence and growth of the SARS-CoV-2 Delta variant. (Nature 2022)

- DOI: 10.1038/s41586-022-05200-3 | PMCID: PMC9534748 | PMID: 35952712
- Evidence: Visualizations were madeusing a custom Python script.
- Full pipeline: alignment/mapping [minimap2] -> structure determination [BEAST v1.10] -> visualisation [Python] -> stage not stated [Pangolin]

### 4-bit adhesion logic enables universal multicellular interface patterning. (Nature 2022)

- DOI: 10.1038/s41586-022-04944-2 | PMCID: PMC9365691 | PMID: 35948712
- Evidence: A custom Python script was written to control the Raspberry Pi Camera V2 and ring light activation.
- Full pipeline: stage not stated [ImageJ, Python]

### Diverse tsunamigenesis triggered by the Hunga Tonga-Hunga Ha'apai eruption. (Nature 2022)

- DOI: 10.1038/s41586-022-05170-6 | PMCID: PMC9472183 | PMID: 35940206
- Evidence: Distances from the explosion were calculated as Euclidean 'as the crow flies' distance (in kilometres) from the weather station to the location of Hunga Tonga island (−20.536000, −175.382000) using the Haversine equation implemented in Python, which assumes a spherical Earth and ignores ellipsoid effects.
- Full pipeline: stage not stated [Python]

### A physical wiring diagram for the human immune system. (Nature 2022)

- DOI: 10.1038/s41586-022-05028-x | PMCID: PMC9365698 | PMID: 35922511
- Evidence: To automate our comparisons of the molecular masses observed by electrophoresis to the computationally expected masses, we made a custom Python script that translates each expression construct using the Biopython library and identifies post-translational processing sites through automated queries to Uniprot.
- Full pipeline: differential/statistical testing [DESeq2, Seurat] -> stage not stated [CellProfiler, PHENIX, Python, R v1.0.0, Scanpy, igraph]

### Retrograde movements determine effective stem cell numbers in the intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-04962-0 | PMCID: PMC7614894 | PMID: 35831497
- Version used: **3.10**
- Evidence: Analysis of the cell tracking results was performed using custom scripts in Python (v3.10).
- Full pipeline: read trimming [STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> differential/statistical testing [Bioconductor v3.14, R v4.1.1] -> stage not stated [ImageJ, NumPy v1.19.5, Python v3.10, TrackMate]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Evidence: The resulting ventral-to-dorsal transform was then applied to re-register all ventral stacks into one common (dorsal) reference frame. c-fos signal intensity quantification Image analysis was performed using custom scripts in Python.
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### Wastewater sequencing reveals early cryptic SARS-CoV-2 variant transmission. (Nature 2022)

- DOI: 10.1038/s41586-022-05049-6 | PMCID: PMC9433318 | PMID: 35798029
- Evidence: Constrained minimization was performed in Python using the cvxpy convex optimization package 32 , 33 .
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Python] -> stage not stated [SAMtools, kallisto]

### A time-resolved, multi-symbol molecular recorder via sequential genome editing. (Nature 2022)

- DOI: 10.1038/s41586-022-04922-8 | PMCID: PMC9352581 | PMID: 35794474
- Evidence: Insertion sequences, in the form of NNGGA (5-mer) to NNNNNNGGA (9-mer), were extracted from sequencing reads of the TAPE arrays, including 2×TAPE-1, 3×TAPE-1 and 5×TAPE-1, using pattern-matching software such as Regular Expression (package REGEX) in Python.
- Full pipeline: stage not stated [Python]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Evidence: In-house Python scripts were used to transfer aligned regions between two species to the BED format required by MCScanX.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Nanoscale imaging of phonon dynamics by electron microscopy. (Nature 2022)

- DOI: 10.1038/s41586-022-04736-8 | PMCID: PMC9177420 | PMID: 35676428
- Evidence: Implementation of this acquisition scheme was achieved using Nion Swift software and custom Python scripts designed to directly control the necessary hardware parameters.
- Full pipeline: alignment/mapping [Matplotlib] -> visualisation [Matplotlib] -> stage not stated [Python, SciPy]

### MCM complexes are barriers that restrict cohesin-mediated loop extrusion. (Nature 2022)

- DOI: 10.1038/s41586-022-04730-0 | PMCID: PMC9159944 | PMID: 35585235
- Evidence: Single-molecule data analysis Single-molecule data were analysed in Fiji using the Molecule Archive Suite (Mars) plug-in ( https://github.com/duderstadt-lab/ ) 74 and custom Python scripts.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R] -> stage not stated [Fiji, ImageJ, NumPy, Python, SciPy, ggplot2]

### A global reptile assessment highlights shared conservation needs of tetrapods. (Nature 2022)

- DOI: 10.1038/s41586-022-04664-7 | PMCID: PMC9095493 | PMID: 35477765
- Evidence: Code availability Python scripts used for the spatial analyses are permanently available at https://transfer.natureserve.org/download/Publications/Global_Reptiles/ .
- Full pipeline: stage not stated [Python, R]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Evidence: All images were stitched using a custom Python script and ImageJ’s max correlation grid/collection stitching (release 1.2).
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### A biophysical account of multiplication by a single neuron. (Nature 2022)

- DOI: 10.1038/s41586-022-04428-3 | PMCID: PMC8891015 | PMID: 35197635
- Version used: **3.7**
- Evidence: Data were corrected for the liquid junction potential and analysed using custom-written software in Python v.3.7 (Python Software Foundation) using NumPy v.1.15, Pandas v.0.25, SciPy v.1.3, Matplotlib v.3.0 and pyABF v.2.1 ( https://pypi.org/project/pyabf/ ).
- Full pipeline: stage not stated [ImageJ v2.0, Matplotlib v3.0, NumPy v1.15, Python v3.7, SciPy v1.3]

### Mechanism-based traps enable protease and hydrolase substrate discovery. (Nature 2022)

- DOI: 10.1038/s41586-022-04414-9 | PMCID: PMC8866121 | PMID: 35173328
- Version used: **3.8.1**
- Evidence: Data preparation and processing were then performed using custom Python (version 3.8.1) scripts written with the pyOpenMS package (version 2.4.0) 56 .
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL v2.5] -> stage not stated [Python v3.8.1]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Evidence: Subsequently, the Seurat object was converted into the .h5ad format for further trajectory analysis and calculation of diffusion maps using the SCANPY analysis framework implemented in Python 62 .
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **3.8.5**
- Evidence: Mutational signatures De novo extraction and decomposition of mutational signatures was performed in Python v.3.8.5 using SigProfilerExtractor (v.1.1.0) 5 , along with SigprofilerMatrixGenerator (v.1.1.14/1.1.15) 83 and SigprofilerPlotting (v.1.1.27).
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Version used: **3.6**
- Evidence: These analyses were performed in Python (v.3.6) using Scikit-learn for PCA (v.0.23.2), Scipy for hierarchical clustering (v.1.5.1) and nheatmap for heat map and clustering visualization (v.0.1.4).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Toroidal topology of population activity in grid cells. (Nature 2022)

- DOI: 10.1038/s41586-021-04268-7 | PMCID: PMC8810387 | PMID: 35022611
- Evidence: Data analysis and statistics Data analyses were performed with custom-written scripts in Python and MATLAB.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.1.3, NumPy v1.18.1, UMAP, scikit-learn v0.22.1] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, SciPy]

### HELQ is a dual-function DSB repair enzyme modulated by RPA and RAD51. (Nature 2022)

- DOI: 10.1038/s41586-021-04261-0 | PMCID: PMC8755542 | PMID: 34937945
- Evidence: 4i–k ), we used a custom-made single-particle tracking algorithm in Python ( https://github.com/singlemoleculegroup ).
- Full pipeline: stage not stated [ImageJ, Python]

### Omicron escapes the majority of existing SARS-CoV-2 neutralizing antibodies. (Nature 2022)

- DOI: 10.1038/s41586-021-04385-3 | PMCID: PMC8866119 | PMID: 35016194
- Evidence: Finally, we built global epistasis models with the dms_variants package for each library to estimate single mutation escape scores, using the Python scripts provided in a previous report 16 .
- Full pipeline: normalisation [MACS2, R] -> dimensionality reduction/clustering [ComplexHeatmap, R, ggplot2 v3.3.3] -> stage not stated [Python]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: The code was written in Python and used the OpenCV and OpenSlide library.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Evidence for European presence in the Americas in AD 1021. (Nature 2022)

- DOI: 10.1038/s41586-021-03972-8 | PMCID: PMC8770119 | PMID: 34671168
- Evidence: The pattern-matching analyses are predominantly carried out using Python 3 in Jupyter Notebook 6.3.0.
- Full pipeline: stage not stated [Jupyter, Python]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: All aging models are available and easily accessible using the organage package in Python and the associated github repository ( https://github.com/hamiltonoh/organage ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### HIV-1 Env trimers asymmetrically engage CD4 receptors in membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06762-6 | PMCID: PMC10686830 | PMID: 37993716
- Evidence: Custom Python scripts were used to generate kernel density heat maps and histogram profiles fit with Gaussian curves depicting the distributions of Env–CD4 complexes.
- Full pipeline: simulation/modelling [NAMD v3.0] -> structure determination [ChimeraX] -> visualisation [ChimeraX, IMOD] -> stage not stated [Python, RELION]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: The Python script count_spacers.py 65 was used as an additional measure for quality control.
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Bacterial cGAS senses a viral RNA to initiate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06743-9 | PMCID: PMC10686824 | PMID: 37968393
- Evidence: A custom Python script was used to convert the output SAM alignments into CSV files containing the number of aligned reads at each nucleotide location along a given reference genome.
- Full pipeline: alignment/mapping [Bowtie2, PyMOL, Python] -> visualisation [Bowtie2] -> stage not stated [AlphaFold, ColabFold]

### The social and structural architecture of the yeast protein interactome. (Nature 2023)

- DOI: 10.1038/s41586-023-06739-5 | PMCID: PMC10700138 | PMID: 37968396
- Evidence: The accompanying Python script is available in Supplementary Data 1 as CorrelationAnalysis.py.
- Full pipeline: visualisation [ChimeraX v1.4, Cytoscape, Matplotlib, NumPy v1.20.3] -> stage not stated [AlphaFold, NetworkX v2.6.2, Python]

### Stress granules plug and stabilize damaged endolysosomal membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06726-w | PMCID: PMC10686833 | PMID: 37968398
- Evidence: Once we have defined the vesicle surface, we evaluate condensation by running a clustering algorithm on the solute and protein particles (part of the Ovito library in Python 61 ).
- Full pipeline: dimensionality reduction/clustering [Python] -> stage not stated [Fiji, ImageJ, MACS2, PHENIX, R v3.0]

### Vision-controlled jetting for composite systems and robots. (Nature 2023)

- DOI: 10.1038/s41586-023-06684-3 | PMCID: PMC10651485 | PMID: 37968527
- Evidence: The motor’s actuation patterns and control sequences are written in Python, and the sensor signal from the microcontroller is read out via a serial connection.
- Full pipeline: stage not stated [Python]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: Analysis software All data analysis was carried out using Python code in Jupyter IPython 56 Notebooks.
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Preserved neural dynamics across animals performing similar behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06714-0 | PMCID: PMC10665198 | PMID: 37938772
- Evidence: All the analyses were implemented in Python using open-source packages such as numpy, matplotlib, sci-kit, scipy and pandas 70 – 74 and custom code.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, Kilosort v2.0, Matplotlib, NumPy, Python, SciPy]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: For genes overlapping multiple segments, a custom Python script was used to call that gene as amplified, neutral or deleted based on a weighted copy-number ratio calculated from copy ratios of each segment overlapped, the lengths of the overlaps and the z -score threshold used by the CallCopyRatioSegments function.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Normative spatiotemporal fetal brain maturation with satisfactory development at 2 years. (Nature 2023)

- DOI: 10.1038/s41586-023-06630-3 | PMCID: PMC10620088 | PMID: 37880365
- Version used: **3.9.6**
- Evidence: All data analysis scripts were written in Python (v.3.9.6).
- Full pipeline: dimensionality reduction/clustering [FSL] -> differential/statistical testing [FSL, statsmodels] -> simulation/modelling [FSL] -> stage not stated [Python v3.9.6, seaborn]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: Python scripts were used to categorize ROH by length, and to overlap ROH with local ancestry calls from rfmix to obtain ancestry-specific ROH summary statistics (Supplementary Table 5 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Unraveling the functional dark matter through global metagenomics. (Nature 2023)

- DOI: 10.1038/s41586-023-06583-7 | PMCID: PMC10584684 | PMID: 37821698
- Evidence: The resulting MSAs were then filtered to produce seed (non-redundant) alignments using a script written in Python and the ProDy/Evol and Biopython modules 43 (90% sequence identity, 75% alignment coverage) ( Supplementary Methods ).
- Full pipeline: alignment/mapping [Clustal Omega, Python] -> dimensionality reduction/clustering [Clustal Omega] -> differential/statistical testing [R] -> stage not stated [AlphaFold, HMMER v3.1, ggplot2]

### Flexible circuit mechanisms for context-dependent song sequencing. (Nature 2023)

- DOI: 10.1038/s41586-023-06632-1 | PMCID: PMC10600009 | PMID: 37821705
- Version used: **2.7**
- Evidence: ... 1300, BFS-U3-13Y3M-C, with TechSpec 25 mm C Series VIS-NIR fixed focal length lens) using the Motif recording system and API (loopbio GmbH), run via Python 2.7, and using infrared illumination of around 22 μW mm − 2 (Advanced Illumination High Performance Bright Field Ring Light, 6.0′′ O.D., wash down, IR LEDs, iC2, flying leads) and an infrared bandpass filter to block the red light used for opt...
- Full pipeline: differential/statistical testing [Brian2] -> simulation/modelling [Brian2] -> machine learning [CaImAn, PyTorch] -> stage not stated [Python v2.7, SLEAP]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **3.9.1**
- Evidence: Data were analysed and figures generated using Python (version 3.9.1), along with packages numpy (version 1.20.3), scipy (version 1.7.1), matplotlib (version 3.4.3), and pandas (version 1.3.0), and R (version 3.6.0).
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **3.6**
- Evidence: Software The following packages and software 50 , 52 – 62 were used in the data analysis: ClusterMap is implemented based on MATLAB R2019b and Python 3.6.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Cingulate dynamics track depression recovery with deep brain stimulation. (Nature 2023)

- DOI: 10.1038/s41586-023-06541-3 | PMCID: PMC10550829 | PMID: 37730990
- Version used: **3.6**
- Evidence: All LFP analyses were performed using custom-written scripts in Python (v.3.6) and Matlab (R2018b).
- Full pipeline: machine learning [PyTorch, scikit-learn v1.1.1] -> stage not stated [AFNI, FSL, Python v3.6]

### Cryo-EM structures reveal native GABA&lt;sub&gt;A&lt;/sub&gt; receptor assemblies and pharmacology. (Nature 2023)

- DOI: 10.1038/s41586-023-06556-w | PMCID: PMC10550821 | PMID: 37730991
- Evidence: Single-molecule fluorescence time traces of nα1-GABA A R–Fab were generated using a custom Python script.
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, CCP4, ChimeraX, Python, RELION]

### Structural mobility tunes signalling of the GluA1 AMPA glutamate receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06528-0 | PMCID: PMC10533411 | PMID: 37704721
- Evidence: Next, particle coordinate files generated from Homogeneous Refinement were converted to RELION star files by using the Python script csparc2star.py (ref.
- Full pipeline: structure determination [Coot, PHENIX, Python, RELION] -> stage not stated [AlphaFold, ChimeraX, MotionCor2, PyMOL, UCSF Chimera]

### Hippocampal representation during collective spatial behaviour in bats. (Nature 2023)

- DOI: 10.1038/s41586-023-06478-7 | PMCID: PMC10533399 | PMID: 37648869
- Version used: **3.9**
- Evidence: Data were recorded and saved using custom written scripts in Python v.3.9.
- Full pipeline: registration [ImageJ v1.53c] -> stage not stated [Python v3.9]

### An orexigenic subnetwork within the human hippocampus. (Nature 2023)

- DOI: 10.1038/s41586-023-06459-w | PMCID: PMC10499606 | PMID: 37648849
- Version used: **3.6**
- Evidence: Imaging data were analysed using publicly available methods and custom scripts in Python v.3.6, as described below.
- Full pipeline: alignment/mapping [SPM] -> normalisation [ANTs v2.1.0] -> registration [ANTs v2.1.0] -> differential/statistical testing [SPM] -> stage not stated [FSL, FieldTrip, Python v3.6, fMRIPrep v1.2.3]

### Epitope editing enables targeted immunotherapy of acute myeloid leukaemia. (Nature 2023)

- DOI: 10.1038/s41586-023-06496-5 | PMCID: PMC10499609 | PMID: 37648862
- Evidence: Custom Python scripts 65 were used to filter search results to 1% FDR, as well as extract TMT reporter ion intensities and correct for isotopic impurities.
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [Python] -> visualisation [ggplot2] -> stage not stated [Bioconductor, R]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Version used: **3.8.3**
- Evidence: 72 ) in Python v.3.8.3.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: A custom Python script (Data availability) was used to genotype the 1 Mb windows and to identify the recombination breakpoints.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Small protein modules dictate prophage fates during polylysogeny. (Nature 2023)

- DOI: 10.1038/s41586-023-06376-y | PMCID: PMC10432266 | PMID: 37495698
- Evidence: Groups of cells that could not be accurately resolved were excluded from downstream analysis and coordinates of remaining cells were exported. smFISH data were analysed using custom Python scripts.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, Prokka v1.11, Python]

### A spatially resolved timeline of the human maternal-fetal interface. (Nature 2023)

- DOI: 10.1038/s41586-023-06298-9 | PMCID: PMC10356615 | PMID: 37468587
- Evidence: Tools for this analysis were written in Python, with the bootstrapping accelerated using Cython.
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [limma, scikit-learn] -> stage not stated [ImageJ, Jupyter, Python, QuPath v0.4.0, R]

### Mega-scale experimental analysis of protein folding stability in biology and design. (Nature 2023)

- DOI: 10.1038/s41586-023-06328-6 | PMCID: PMC10412457 | PMID: 37468638
- Version used: **3.9**
- Evidence: Both models are implemented in Python 3.9 using the Numpyro package 58 version 0.80.
- Full pipeline: read trimming [Cutadapt] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [AlphaFold, Python v3.9]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Evidence: Activity analysis Data analysis was performed using Python 3.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### PLSCR1 is a cell-autonomous defence factor against SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06322-y | PMCID: PMC10371867 | PMID: 37438530
- Evidence: MDS analysis A coarse-grained simulation using the AlphaFold 57 structure of PLSCR1 with the N-terminal region truncated was assembled using the insane.py Python script 58 , memembed (ref.
- Full pipeline: alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, R] -> simulation/modelling [AlphaFold, GROMACS v2021.3, Python] -> stage not stated [PyMOL, VMD]

### Diverse organic-mineral associations in Jezero crater, Mars. (Nature 2023)

- DOI: 10.1038/s41586-023-06143-z | PMCID: PMC10371864 | PMID: 37438522
- Evidence: Exported Loupe data were then further processed using custom Python scripts, Microsoft Excel and Spectragryph 52 .
- Full pipeline: stage not stated [OpenCV, Python, SciPy]

### The carbon costs of global wood harvests. (Nature 2023)

- DOI: 10.1038/s41586-023-06187-1 | PMCID: PMC10396961 | PMID: 37407827
- Evidence: The principal version of the model runs in Python using input files from Excel.
- Full pipeline: stage not stated [Python]

### Evolution of a minimal cell. (Nature 2023)

- DOI: 10.1038/s41586-023-06288-x | PMCID: PMC10396959 | PMID: 37407813
- Evidence: We then used Python 59 to simulate the placement of these mutations at random across all genes.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> simulation/modelling [Python] -> stage not stated [ImageJ, R]

### Wake-like skin patterning and neural activity during octopus sleep. (Nature 2023)

- DOI: 10.1038/s41586-023-06203-4 | PMCID: PMC10322707 | PMID: 37380770
- Version used: **3.6**
- Evidence: Core analysis was written in Python (v.3.6 and 3.7), with further analysis written using MATLAB 2019a.
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> machine learning [Keras, TensorFlow v2.0] -> stage not stated [Python v3.6, scikit-image]

### Continuous synthesis of E. coli genome sections and Mb-scale human DNA assembly. (Nature 2023)

- DOI: 10.1038/s41586-023-06268-1 | PMCID: PMC7614783 | PMID: 37380776
- Evidence: Sequencing data analysis We performed short-read sequencing data analysis for recoding and CGS with a custom Python script ( https://github.com/JWChin-Lab ) as previously described in detail 1 , 45 .
- Full pipeline: read trimming [minimap2] -> alignment/mapping [SAMtools v1.16.1, minimap2] -> variant calling [Mutect2] -> stage not stated [GATK v4.3.0, Python, RepeatMasker, deepTools v3.5.1]

### Heritable transcriptional defects from aberrations of nuclear architecture. (Nature 2023)

- DOI: 10.1038/s41586-023-06157-7 | PMCID: PMC10322708 | PMID: 37286600
- Evidence: Analysis of generation 2 re-incorporated MN chromosomes Analysis of incorporated MN chromosomes were performed primarily using an automated script written in Python 47 .
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, GATK v4.1.9.0, STAR v2.7.6a] -> quantification [RSEM, featureCounts] -> stage not stated [ImageJ, MACS2, Python]

### Health system-scale language models are all-purpose prediction engines. (Nature 2023)

- DOI: 10.1038/s41586-023-06160-y | PMCID: PMC10338337 | PMID: 37286606
- Version used: **3.8.13**
- Evidence: Code availability We used sql and Python 3.8.13 to collect data from the NYU Langone EHR.
- Full pipeline: stage not stated [Matplotlib v3.5.2, Python v3.8.13, XGBoost, scikit-learn, seaborn v0.12.2]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: The sequencing output files from different lanes were concatenated, aligned to GRCH38 using HISAT2 and transcripts were counted using HTSeq in Python.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: Custom Python scripts were used to determine the overall median T cell fluorescence intensity and categorize radial fluorescence profiles as desert, excluded or inflamed.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Engineered tRNAs suppress nonsense mutations in cells and in vivo. (Nature 2023)

- DOI: 10.1038/s41586-023-06133-1 | PMCID: PMC10284701 | PMID: 37258671
- Evidence: Scanned microarray slides were analysed using inhouse Python scripts.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> stage not stated [Python]

### Ångström-resolution fluorescence microscopy. (Nature 2023)

- DOI: 10.1038/s41586-023-05925-9 | PMCID: PMC10208979 | PMID: 37225882
- Evidence: This was performed outside of Picasso in a custom Python script, not only to find the optimal translation between channels but also to correct for possible rotations of the DNA origami.
- Full pipeline: stage not stated [Python]

### Gap junctions desynchronize a neural circuit to stabilize insect flight. (Nature 2023)

- DOI: 10.1038/s41586-023-06099-0 | PMCID: PMC10232364 | PMID: 37225999
- Evidence: All of the Python scripts are available on request.
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, Python, SciPy, seaborn]

### Structural basis of NINJ1-mediated plasma membrane rupture in cell death. (Nature 2023)

- DOI: 10.1038/s41586-023-05991-z | PMCID: PMC10307626 | PMID: 37198476
- Evidence: 15 N R 2 spin relaxation measurements were performed on a 50 µM sample of GB1–NINJ1(1–81) without detergent with a CPMG pulse sequence (10 delay values, 24 h total experimental time), and analysed with in-house Python scripts.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, ChimeraX, Python]

### Recombination between heterologous human acrocentric chromosomes. (Nature 2023)

- DOI: 10.1038/s41586-023-05976-y | PMCID: PMC10172130 | PMID: 37165241
- Evidence: We then used the paf2net.py Python script (delivered in the PGGB repository) to build a graph representation of the result (a mapping graph), with nodes and edges representing contigs and mappings between them, respectively. python3 ~/pggb/scripts/paf2net.py -p HPRCy1.1Mbps.paf The script produces a file representing the edges, a file representing the edge weights, and a file to map graph nodes to...
- Full pipeline: alignment/mapping [Python, igraph] -> stage not stated [BEDTools, PLINK v1.9, R v3.6.3, ggplot2 v3.3.3, tidyverse v1.3.0]

### Glioblastoma remodelling of human neural circuits decreases survival. (Nature 2023)

- DOI: 10.1038/s41586-023-06036-1 | PMCID: PMC10191851 | PMID: 37138086
- Evidence: Statistics Compiler output files were processed in Microsoft Excel (Microsoft) and with custom Python scripts to organize and extract individual parameter data for each well of each MEA plate and for data normalization.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [HISAT2, featureCounts] -> normalisation [Python, Seurat v3.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Python, R v3.1, Seurat v3.0.1, featureCounts] -> stage not stated [ImageJ]

### Multisensory learning binds neurons into a cross-modal memory engram. (Nature 2023)

- DOI: 10.1038/s41586-023-06013-8 | PMCID: PMC10208976 | PMID: 37100911
- Version used: **3.8.8**
- Evidence: Neuroanatomy, connectivity and dendrograms Neuromorphological calculations and connectivity analyses were performed, and dendrograms were calculated and plotted, with scripts based on NAVis 1.2.1 library functions in Python 3.8.8 ( https://pypi.org/project/navis/ ; https://github.com/navis-org/navis ) 80 and data from the Drosophila hemibrain (v.1.2.1) ( https://neuprint.janelia.org ) 32 , 33 .
- Full pipeline: visualisation [Python v3.8.8]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Evidence: Classifier to predict seeding and non-seeding tumour regions We built the machine-learning framework in Python using Tensorflow (v.2.6.0) 104 and sklearn (v.0.0) 105 .
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Evidence: EGFR mutant cell foci were quantified from cell coordinate data by clustering cell positions by density using the DBSCAN algorithm, implemented in Python with the scikit-learn library 62 .
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Evidence: Data visualization Plots were generated using matplotlib (version 3.3.2), seaborn (version 0.11.0) and plotly (version 5.6.0) packages in Python software (version 3.7.12), Jupyter notebook (version 6.1.4), RStudio (version 1.4) and Adobe Illustrator (version 26.4.1) software.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### Hybrid 2D-CMOS microchips for memristive applications. (Nature 2023)

- DOI: 10.1038/s41586-023-05973-1 | PMCID: PMC10232361 | PMID: 36972685
- Evidence: 46 ), an SNN simulator written in Python.
- Full pipeline: simulation/modelling [Brian2, Python]

### Fast and sensitive GCaMP calcium indicators for imaging neural populations. (Nature 2023)

- DOI: 10.1038/s41586-023-05828-9 | PMCID: PMC10060165 | PMID: 36922596
- Evidence: Image analysis was performed using custom Python scripts.
- Full pipeline: structure determination [REFMAC] -> stage not stated [CaImAn, PyMOL, Python, Suite2p, ilastik]

### Coordination of bacterial cell wall and outer membrane biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-05750-0 | PMCID: PMC9995270 | PMID: 36859542
- Version used: **3.8.8**
- Evidence: Interaction scores were mapped onto the tree in Python v3.8.8 and visualized with the interactive tree of life (ITOL) v5 (ref.
- Full pipeline: alignment/mapping [Python v3.8.8] -> quantification [ImageJ] -> visualisation [ChimeraX v1.1.1, Python v3.8.8] -> stage not stated [AlphaFold, scikit-learn v1.0.2]

### Coastal phytoplankton blooms expand and intensify in the 21st century. (Nature 2023)

- DOI: 10.1038/s41586-023-05760-y | PMCID: PMC9995273 | PMID: 36859547
- Version used: **3.8**
- Evidence: Map created using Python 3.8.
- Full pipeline: stage not stated [Python v3.8]

### The cellular coding of temperature in the mammalian cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-05705-5 | PMCID: PMC9946826 | PMID: 36755097
- Evidence: Two-photon analysis Motion correction of data, identification of putative neurons and calculation of Δ F / F was carried out using the Suite2p package (v0.9.3) in Python 42 .
- Full pipeline: registration [Python, Suite2p] -> stage not stated [Fiji, ImageJ, Kilosort]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: We implemented and tested CellOracle in Python (versions 3.6 and 3.8) and designed it for use in the Jupyter notebook environment.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Single-cell spatial immune landscapes of primary and metastatic brain tumours. (Nature 2023)

- DOI: 10.1038/s41586-022-05680-3 | PMCID: PMC9931580 | PMID: 36725935
- Version used: **3.7.12**
- Evidence: Statistics and reproducibility All image analysis steps were performed in MATLAB (version 2019b) and Python (version 3.7.12).
- Full pipeline: normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1] -> differential/statistical testing [Python v3.7.12] -> stage not stated [ImageJ v1.53k, scikit-learn]

### Single-cell spatial landscapes of the lung tumour immune microenvironment. (Nature 2023)

- DOI: 10.1038/s41586-022-05672-3 | PMCID: PMC9931585 | PMID: 36725934
- Version used: **3.7.12**
- Evidence: Deep learning All deep-learning analysis steps were performed in Python (version 3.7.12).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> machine learning [Python v3.7.12] -> stage not stated [Keras, TensorFlow v2.8.0]

### Tissue CD14&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; T cells reprogrammed by myeloid cells and modulated by LPS. (Nature 2023)

- DOI: 10.1038/s41586-022-05645-6 | PMCID: PMC7619353 | PMID: 36697826
- Version used: **3.6**
- Evidence: 8) or Python 3.6 using appropriate tests (Mann-Whitney t test, Wilcoxon Signed-rank t test, Kruskal-Wallis test [ANOVA] with Dunn’s post hoc test for pairwise multiple comparisons between each group) as indicated in the legends.
- Full pipeline: quality control [STAR, Seurat] -> alignment/mapping [STAR] -> quantification [HTSeq v0.10.0, ImageJ, STAR] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [seaborn] -> simulation/modelling [scDblFinder] -> visualisation [seaborn] -> stage not stated [Python v3.6]

### Visualization of translation and protein biogenesis at the ER membrane. (Nature 2023)

- DOI: 10.1038/s41586-022-05638-5 | PMCID: PMC9892003 | PMID: 36697828
- Version used: **3.8.11**
- Evidence: Polysome analysis For the neighbourhood analysis, ribosome positions and orientations were read from the RELION star files resulting from subtomogram alignment in a python script (Python 3.8.11, Numpy 1.20.3, Scipy 1.7.1).
- Full pipeline: alignment/mapping [IMOD v4.10.25, NumPy v1.20.3, Python v3.8.11, RELION v3.1.1, SciPy v1.7.1] -> structure determination [ChimeraX v1.3.0, UCSF Chimera v1.14.0] -> visualisation [ChimeraX v1.3.0] -> stage not stated [AlphaFold]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: If the targeted syllable could not be reasonably excluded then data from the day after a stimulation day was excluded entirely. dLight behaviour procedures OFA experiments Depth videos of mouse behaviour were acquired at 30 Hz using a Kinect 2 for Windows (Microsoft) using a custom user interface written in Python (similar to ref.
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### An atlas of substrate specificities for the human serine/threonine kinome. (Nature 2023)

- DOI: 10.1038/s41586-022-05575-3 | PMCID: PMC9876800 | PMID: 36631611
- Version used: **3.7.6**
- Evidence: The linkage matrix was computed using the SciPy package in Python (v.3.7.6), using the Ward method.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, PyMOL, Python v3.7.6, SciPy]

### Early Release Science of the exoplanet WASP-39b with JWST NIRISS. (Nature 2023)

- DOI: 10.1038/s41586-022-05674-1 | PMCID: PMC9946829 | PMID: 36623550
- Evidence: Code availability The following are open-source pipelines written in Python available either through the Python Package Index (PyPI) or GitHub that were used throughout this work: Eureka!
- Full pipeline: normalisation [SciPy] -> differential/statistical testing [dynesty] -> simulation/modelling [emcee] -> stage not stated [Astropy, PyMC, PyMC3, Python]

### Cas12a2 elicits abortive infection through RNA-triggered destruction of dsDNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05559-3 | PMCID: PMC9811890 | PMID: 36599979
- Evidence: The resulting data were analysed in Python.
- Full pipeline: read trimming [RAxML] -> alignment/mapping [Bowtie2, MAFFT v7.490, RAxML] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST, Python]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Version used: **3.6**
- Evidence: To calculate the adjusted P value for the 64 bins statsmodels v0.11.1 60 multipletests methods with the parameter method=’fdr_bh’ in Python 3.6 61 was used.
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Evidence: We used statsmodels (v0.12.2) in Python and, specifically, the ordinary least-squares model found in the statsmodels.api.OLS module to estimate the coefficients of the selected predictors in their corresponding multiple linear regression model 54 .
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: Bipartite weighted kNN graph reconstruction With the primary reference 27 and query (HNOCA) data projected to the same latent space, an unweighted bipartite kNN graph was constructed by identifying 100 nearest neighbours of each query cell in the reference data with either PyNNDescent or RAPIDS-cuML ( https://github.com/rapidsai/cuml ) in Python, depending on availability of GPU acceleration.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Releasing a sugar brake generates sweeter tomato without yield penalty. (Nature 2024)

- DOI: 10.1038/s41586-024-08186-2 | PMCID: PMC11578880 | PMID: 39537922
- Evidence: Tajima’s D value was analysed by VCFtools (version 0.1.16), and the F ST value was calculated using the Python script popgenWindows.py as described previously 72 , 73 .
- Full pipeline: alignment/mapping [MAFFT v7.525] -> quantification [ImageJ] -> visualisation [ggplot2 v3.4.4] -> stage not stated [IQ-TREE, PLINK, Python, VCFtools v0.1.16]

### Central pattern generator control of a vertebrate ultradian sleep rhythm. (Nature 2024)

- DOI: 10.1038/s41586-024-08162-w | PMCID: PMC11655359 | PMID: 39506115
- Evidence: We then extracted the Hilbert transform, using the scipy.signal.hilbert function in Python.
- Full pipeline: differential/statistical testing [pandas v2.0.3, xarray v2023.6.0] -> stage not stated [DeepLabCut, NumPy, Python, SciPy]

### Autonomous mobile robots for exploratory synthetic chemistry. (Nature 2024)

- DOI: 10.1038/s41586-024-08173-7 | PMCID: PMC11602721 | PMID: 39506122
- Evidence: The data from the Fourier80 instrument were acquired and analysed using a custom software package (10.5281/zenodo.11174257) communicating with TopSpin 4.3.0 through official TopSpin Python API distributed by Bruker.
- Full pipeline: stage not stated [Python]

### Ab initio characterization of protein molecular dynamics with AI&lt;sup&gt;2&lt;/sup&gt;BMD. (Nature 2024)

- DOI: 10.1038/s41586-024-08127-z | PMCID: PMC11602711 | PMID: 39506110
- Evidence: After the workload is distributed from the main component to the computation servers, it will be processed in parallel, and the main Python process can immediately resume processing other tasks such as persisting trajectory data, without being blocked by the servers.
- Full pipeline: simulation/modelling [GROMACS, Python] -> stage not stated [Docker, MDTraj]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Reads were demultiplexed into individual sample FASTQ files based on their barcode sequence using a custom Python script.
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: For genes overlapping multiple segments, a custom Python script was used to call that gene as amplified, neutral or deleted based on a weighted copy number ratio calculated from the copy ratios of each overlapped segment, the lengths of the overlaps and the z score threshold used by the CallCopyRatioSegments function.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Evidence: The container entrypoint was set to a Python script for model training (boda2/src/main.py).
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: Cell–cell interaction analysis Cell–cell interaction analysis was performed in Python.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### One-shot entorhinal maps enable flexible navigation in novel environments. (Nature 2024)

- DOI: 10.1038/s41586-024-08034-3 | PMCID: PMC11602719 | PMID: 39385034
- Evidence: RGB video was captured at 50 fps with 10 pixels cm −1 resolution (BFS-U3-23S3C-C, FLIR Blackfly) using a custom Python script using FLIR Spinnaker API.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut v2.2.0.6] -> stage not stated [Kilosort, Python, SciPy]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: All of the machine learning methods, including training, validation, and testing, were implemented using the scikit-learn library in Python.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### A Drosophila computational brain model reveals sensorimotor processing. (Nature 2024)

- DOI: 10.1038/s41586-024-07763-9 | PMCID: PMC11446845 | PMID: 39358519
- Evidence: Then, in Python, background subtraction was carried out for each timepoint ( F t ).
- Full pipeline: stage not stated [Brian2, NumPy, Python]

### Network statistics of the whole-brain connectome of Drosophila. (Nature 2024)

- DOI: 10.1038/s41586-024-07968-y | PMCID: PMC11446825 | PMID: 39358527
- Evidence: Code availability The analyses presented in this paper were performed in Python with the numpy and graph-tool 71 packages, and in MATLAB (standard toolboxes).
- Full pipeline: stage not stated [NumPy, Python]

### Whole-brain annotation and multi-connectome cell typing of Drosophila. (Nature 2024)

- DOI: 10.1038/s41586-024-07686-5 | PMCID: PMC11446831 | PMID: 39358521
- Evidence: Root IDs were updated every 30 min by a Python script based on the fafbseg package (Table 1 ) to account for any edits.
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [Python]

### Neural circuit mechanisms underlying context-specific halting in Drosophila. (Nature 2024)

- DOI: 10.1038/s41586-024-07854-7 | PMCID: PMC11446846 | PMID: 39358520
- Evidence: Data analysis was performed using custom scripts in Python and MATLAB.
- Full pipeline: dimensionality reduction/clustering [DeepLabCut v2.2.3] -> structure determination [DeepLabCut v2.2.3] -> stage not stated [Cytoscape, ImageJ, Python]

### Bendable non-silicon RISC-V microprocessor. (Nature 2024)

- DOI: 10.1038/s41586-024-07976-y | PMCID: PMC11464375 | PMID: 39322672
- Evidence: The Python script running on the processing system controls the test.
- Full pipeline: stage not stated [Python, TensorFlow]

### Self-organized tissue mechanics underlie embryonic regulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07934-8 | PMCID: PMC11424473 | PMID: 39261736
- Evidence: For numerical simulations, it was implemented in Python, using the FEniCS finite element platform 33 , 34 .
- Full pipeline: simulation/modelling [Python]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Evidence: Custom Python scripts were used to break up sequences for folding and extract metrics from outputs (that is, pLDDT confidence and MSA depth).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Evidence: The Python scripts and the parameters used for generating the principal bundle decomposition can be found in the associated GitHub repository.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: All scRNA-seq data were preprocessed in Python using Scanpy v.1.9.1.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### Mechanisms that clear mutations drive field cancerization in mammary tissue. (Nature 2024)

- DOI: 10.1038/s41586-024-07882-3 | PMCID: PMC11374684 | PMID: 39232148
- Evidence: For simulations, we have generated clustered and unclustered data in Python.
- Full pipeline: alignment/mapping [BWA, Cutadapt] -> dimensionality reduction/clustering [Python] -> simulation/modelling [Python] -> visualisation [ImageJ, ggplot2] -> stage not stated [QuPath]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Evidence: Immunostained cells were counted with Jupyter Notebook in Python 3.
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Version used: **3.10.4**
- Evidence: Seurat analysis was performed in R v.4.3.1, velocity analysis was performed in Python v.3.10.4 and regulon analysis was performed in Python v.3.7.12 in accordance with the respective pipeline requirements.
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Evidence: 14 using the Python scripts available at ( https://github.com/wheatgenetics/owwc/tree/master/kGWAS ) and the phenotype data for stem rust and leaf rust available for this panel to specifically run the association mapping and plotting using default parameters.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### De novo design of allosterically switchable protein assemblies. (Nature 2024)

- DOI: 10.1038/s41586-024-07813-2 | PMCID: PMC11338832 | PMID: 39143214
- Evidence: Distributions were exported from DiscoverMP and plotted with a custom script in Python.
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [PHENIX] -> visualisation [ChimeraX, Python] -> stage not stated [PyMOL, UCSF Chimera]

### Molecular architecture of coronavirus double-membrane vesicle pore complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07817-y | PMCID: PMC11374677 | PMID: 39143215
- Evidence: The motion-corrected images were then stacked into individual tilt series and aligned using batchruntomo, using the previous Python script (tomo_toolbox.py: https://github.com/ffyr2w/cet_toolbox ).
- Full pipeline: alignment/mapping [Python] -> structure determination [ChimeraX, Coot, RELION] -> visualisation [Topaz] -> stage not stated [AlphaFold, IMOD]

### Human organoids with an autologous tissue-resident immune compartment. (Nature 2024)

- DOI: 10.1038/s41586-024-07791-5 | PMCID: PMC11374719 | PMID: 39143209
- Version used: **3.7**
- Evidence: This workflow results from an adaptation and integration of CellOracle 71 and scVelo 72 in Python (v.3.7).
- Full pipeline: quality control [R] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [CellChat, CellProfiler v4.2.5, ImageJ v1.54i, Python v3.7, scDblFinder, scVelo]

### Encoding of female mating dynamics by a hypothalamic line attractor. (Nature 2024)

- DOI: 10.1038/s41586-024-07916-w | PMCID: PMC11499253 | PMID: 39142338
- Evidence: All data analyses were performed in Python.
- Full pipeline: stage not stated [Python]

### The ribosome lowers the entropic penalty of protein folding. (Nature 2024)

- DOI: 10.1038/s41586-024-07784-4 | PMCID: PMC11374706 | PMID: 39112704
- Evidence: Code availability Python scripts used to calculate PRE-NMR data from the ensembles and to refine the ensembles by reweighting are available on Github ( https://github.com/julian-streit/PREreweighting ).
- Full pipeline: simulation/modelling [GROMACS, PyMOL v2.3] -> structure determination [Python] -> stage not stated [ImageJ, MDAnalysis, MDTraj, SciPy]

### Molecular mimicry in multisystem inflammatory syndrome in children. (Nature 2024)

- DOI: 10.1038/s41586-024-07722-4 | PMCID: PMC11324515 | PMID: 39112696
- Evidence: Statistical methods All statistical analysis was performed in Python using the Scipy Stats package unless otherwise indicated.
- Full pipeline: differential/statistical testing [Python, SciPy, scikit-learn, tidyverse v1.1.4] -> machine learning [scikit-learn] -> stage not stated [Scanpy v1.10.0, Seurat, igraph v2.0.3]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Version used: **3.9**
- Evidence: Single-molecule data interpretation Raw data exported from LUMICKS Bluelake as .h5 files were processed with custom-written Jupyter Notebooks in Python 3.9 using LUMICKS Pylake v.1.2.1, numpy v.1.26.0, matplotlib v.3.7.2, scipy v.1.11.3 and peakutils v.1.3.4 ( https://github.com/singlemoleculegroup ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### Neural general circulation models for weather and climate. (Nature 2024)

- DOI: 10.1038/s41586-024-07744-y | PMCID: PMC11357988 | PMID: 39039241
- Evidence: Our differentiable dynamical core is implemented in JAX, a library for high-performance code in Python that supports automatic differentiation 42 .
- Full pipeline: stage not stated [Python]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Processing of the PCR sgRNA dial-out data The PCR dial-out data was processed by a custom in-house Python script.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### De novo variants in the RNU4-2 snRNA cause a frequent neurodevelopmental syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07773-7 | PMCID: PMC11338827 | PMID: 38991538
- Evidence: Assessing the sensitivity to detect the n.64_65insT variant in exome sequencing data We used a Python script that uses samtools mpileup to retrieve the coverage and base change at the n.64_65 critical locus to identify putative carriers of the insertion ( https://github.com/francois-lecoquierre/genomics_shortcuts/blob/main/find_RNU4-2_recurrent_variant.py ).
- Full pipeline: alignment/mapping [BEDTools v2.31.0, STAR] -> quantification [STAR] -> normalisation [STAR] -> stage not stated [Python, R v4.0.2, SAMtools]

### In situ targeted base editing of bacteria in the mouse gut. (Nature 2024)

- DOI: 10.1038/s41586-024-07681-w | PMCID: PMC11338833 | PMID: 38987595
- Evidence: For each position of the reference genome, the frequency of each nucleotide was computed with a custom Python script using the pile-up function of pysam v.0.20.0 (ref.
- Full pipeline: alignment/mapping [MAFFT, Python] -> dimensionality reduction/clustering [QIIME 2] -> stage not stated [Cutadapt v3.3, Matplotlib, fastp, seaborn]

### Semantic encoding during language comprehension at single-cell resolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07643-2 | PMCID: PMC11254762 | PMID: 38961302
- Evidence: Audio presentation and recordings The linguistic materials were given to the participants in audio format using a Python script utilizing the PyAudio library (version 0.2.11).
- Full pipeline: dimensionality reduction/clustering [SPM] -> visualisation [SPM] -> stage not stated [Kilosort, Python]

### Kinetic features dictate sensorimotor alignment in the superior colliculus. (Nature 2024)

- DOI: 10.1038/s41586-024-07619-2 | PMCID: PMC11236723 | PMID: 38961292
- Evidence: Two-photon recordings were then registered and ROIs were determined manually and extracted using CaImAn 58 (Flatiron Institute) in Python.
- Full pipeline: stage not stated [CaImAn, DeepLabCut, PsychoPy, Python]

### Bridge RNAs direct programmable recombination of target and donor DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07552-4 | PMCID: PMC11208160 | PMID: 38926615
- Evidence: Barcodes were then extracted from the amplicons using custom Python scripts.
- Full pipeline: alignment/mapping [BWA, minimap2] -> dimensionality reduction/clustering [HMMER] -> stage not stated [BEDTools, BLAST, Python]

### Chemical reservoir computation in a self-organizing reaction network. (Nature 2024)

- DOI: 10.1038/s41586-024-07567-x | PMCID: PMC11254755 | PMID: 38926572
- Evidence: Images were adapted to plots using OpenCV-Python 50 .
- Full pipeline: stage not stated [OpenCV, Python, scikit-learn]

### The mechanism for directional hearing in fish. (Nature 2024)

- DOI: 10.1038/s41586-024-07507-9 | PMCID: PMC11222163 | PMID: 38898274
- Evidence: Twelve target sounds were generated from a recorded pressure waveform (see the section of the Methods entitled Sound stimulation waveforms), targeted to the fish’s current position to cancel reverberations (see the section of the Methods entitled Calibration and reverberation cancellation), and presented to the fish in random order following trigger events using custom-written code in Python 3.
- Full pipeline: stage not stated [ImageJ v1.5, Python, SLEAP, SciPy]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: L.M.D. assisted with data analyses and implemented Cell2TCR in Python.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### Computational design of soluble and functional membrane protein analogues. (Nature 2024)

- DOI: 10.1038/s41586-024-07601-y | PMCID: PMC11236705 | PMID: 38898281
- Version used: **3.9**
- Evidence: Steady-state response units were plotted against analyte concentration, and a sigmoid function was fitted to the experimental data in Python 3.9 to derive the K d .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, Python v3.9] -> stage not stated [AlphaFold]

### Hybrid working from home improves retention without damaging performance. (Nature 2024)

- DOI: 10.1038/s41586-024-07500-2 | PMCID: PMC11208135 | PMID: 38867040
- Evidence: We first used the most popular Chinese word segmentation package in Python, named Jieba, to identify the most frequent Chinese words from task titles across four performance reviews.
- Full pipeline: stage not stated [Python, R]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Evidence: Scale factors between the observed copy number and the Poisson distributions, as well as the λ parameters of the Poisson distributions, were estimated using a least squares method implemented in a Python script.
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### The solar dynamo begins near the surface. (Nature 2024)

- DOI: 10.1038/s41586-024-07315-1 | PMCID: PMC11111411 | PMID: 38778233
- Evidence: Code availability We use the Dedalus code and additional analysis tools written in Python, as noted and referenced in the Methods .
- Full pipeline: stage not stated [Python]

### Life-cycle-coupled evolution of mitosis in close relatives of animals. (Nature 2024)

- DOI: 10.1038/s41586-024-07430-z | PMCID: PMC11153136 | PMID: 38778110
- Evidence: The tracing of bundles and twist calculations were previously written in Python programming language using PyCharm IDE, with external libraries such as NumPy, scikit-image, Matplotlib, PIL, OpenCV and SciPy.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [HMMER v3.3.2, ImageJ, Matplotlib, NumPy, OpenCV, Python, SciPy, scikit-image]

### The intrinsic substrate specificity of the human tyrosine kinome. (Nature 2024)

- DOI: 10.1038/s41586-024-07407-y | PMCID: PMC11136658 | PMID: 38720073
- Version used: **3.7.6**
- Evidence: Linkage matrices were computed using the SciPy package in Python (v.3.7.6), using the ‘ward’ method.
- Full pipeline: visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python v3.7.6, SciPy]

### Sleep pressure modulates single-neuron synapse number in zebrafish. (Nature 2024)

- DOI: 10.1038/s41586-024-07367-3 | PMCID: PMC11096099 | PMID: 38693264
- Evidence: The colocalization and relationships between FingR(PSD95)–GFP and antibody staining were analysed using custom Python scripts (available at GitHub ( https://github.com/anyasupp/single-neuron-synapse )).
- Full pipeline: normalisation [SciPy v1.11.4] -> stage not stated [ImageJ, Python]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **3.7**
- Evidence: Global clustering was performed using Scanpy (v.1.8.1) 63 in Python (v.3.7).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: Image analysis Mean intensity analyses for parvalbumin and WFA stainings were performed in ImageJ with a custom-made script in Python.
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### DNA glycosylases provide antiviral defence in prokaryotes. (Nature 2024)

- DOI: 10.1038/s41586-024-07329-9 | PMCID: PMC11078745 | PMID: 38632404
- Evidence: Illumina paired-end sequencing reads were aligned to phage genomes using a custom Python script, where the recorded number of phage-derived sequencing reads at a specific base pair position within the phage genome was normalized to the total sequencing reads for each sample.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MUSCLE, Python] -> normalisation [Python] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, ColabFold]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: Spurious labels arising from plate defects, debris or pillars were manually removed in napari following automatic edge-based filtering in Python.
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Control of working memory by phase-amplitude coupling of human hippocampal neurons. (Nature 2024)

- DOI: 10.1038/s41586-024-07309-z | PMCID: PMC11078732 | PMID: 38632400
- Evidence: To extract and characterize each theta cycle during the delay period in all significant hippocampal PAC channels, we used the bycycle toolbox 72 in Python.
- Full pipeline: stage not stated [EEGLAB v2019.1, FieldTrip, FreeSurfer, Python]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Evidence: Code availability The shell, R and Python scripts that enabled the main steps of the analyses performed in this project are available on request.
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### Neural and behavioural state switching during hippocampal dentate spikes. (Nature 2024)

- DOI: 10.1038/s41586-024-07192-8 | PMCID: PMC11023929 | PMID: 38480889
- Evidence: Bayesian decoding analyses were performed using custom codes written in Python.
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [Python] -> machine learning [DeepLabCut] -> stage not stated [Kilosort, NetworkX]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Version used: **3.9.12**
- Evidence: All subsequent analysis was implemented in Python (v.3.9.12) based on the Scanpy 42 (v.1.9.1) single-cell data analysis package, except where stated otherwise.
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Evidence: HPRT1R noCpG was designed starting with the HPRT1R sequence, using a Python script to scan the sequence for occurrences of CG and randomly delete either the C or the G.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### Incomplete transcripts dominate the Mycobacterium tuberculosis transcriptome. (Nature 2024)

- DOI: 10.1038/s41586-024-07105-9 | PMCID: PMC10937400 | PMID: 38418874
- Evidence: The RNA coverage plots were generated using Matplotlib package 45 and custom Python scripts.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, SAMtools v1.17] -> visualisation [Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1] -> stage not stated [Cutadapt v4.1, Python]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: No-map and soft-clipped reads (more than 20 bp soft-clipped) were extracted using Python scripts.
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Version used: **3.6.10**
- Evidence: HD-MEA data analysis Data analysis was performed using custom-written codes in MATLAB R2021a and Python 3.6.10, which are available upon request.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Evidence: A modified staging tool, implemented in Python and exhibiting better performance on E14.0–E15.0 samples, was used to confirm staging of samples within this window (documentation and Python scripts available at https://github.com/marcomusy/welsh_embryo_stager ).
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### Transforming a head direction signal into a goal-oriented steering command. (Nature 2024)

- DOI: 10.1038/s41586-024-07039-2 | PMCID: PMC10881397 | PMID: 38326621
- Evidence: We used a custom Python script to output the forward axis ball displacement, yaw axis ball displacement, forward ball displacement and gain-modified yaw ball displacement to an analogue output device (Phidget Analog 4-Output 1002_0B) and recorded these signals along with other experimental timeseries data on a data acquisition card (NiDAQ PCIe-6363) card at 20 kHz.
- Full pipeline: stage not stated [Python]

### Converting an allocentric goal into an egocentric steering signal. (Nature 2024)

- DOI: 10.1038/s41586-023-07006-3 | PMCID: PMC10881393 | PMID: 38326612
- Evidence: We defined ROIs for the left and right side of the LAL, the glomeruli of the bridge and columns of the fan-shaped body using a custom graphical user interface written in Python.
- Full pipeline: stage not stated [CaImAn, Python, SciPy]

### Single-photon superradiance in individual caesium lead halide quantum dots. (Nature 2024)

- DOI: 10.1038/s41586-023-07001-8 | PMCID: PMC10866711 | PMID: 38297126
- Evidence: Simulation of photon statistics Monte Carlo simulations of (multi-)exciton emission and of the HBT experiments were performed in Python using the pycorrelate package ( https://github.com/tritemio/pycorrelate ).
- Full pipeline: differential/statistical testing [Python] -> simulation/modelling [Python]

### Minute-scale oscillatory sequences in medial entorhinal cortex. (Nature 2024)

- DOI: 10.1038/s41586-023-06864-1 | PMCID: PMC10781645 | PMID: 38123682
- Evidence: Step values of the encoder (4,096 per full revolution, ∼130 µm resolution) were digitized by a microcontroller (Teensy 3.5, PJRC) and recorded using custom Python scripts at 40–50 Hz.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, Suite2p]

### The genetic legacy of the expansion of Bantu-speaking peoples in Africa. (Nature 2024)

- DOI: 10.1038/s41586-023-06770-6 | PMCID: PMC10794141 | PMID: 38030719
- Evidence: 12 with homemade scripts implemented in Python.
- Full pipeline: quality control [PLINK v1.90b] -> variant calling [PLINK v1.90b, SHAPEIT, UMAP] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [Python, R]

### Heavy-element production in a compact object merger observed by JWST. (Nature 2024)

- DOI: 10.1038/s41586-023-06759-1 | PMCID: PMC10881391 | PMID: 37879361
- Evidence: MUSE data were reduced using standard esorex recipes embedded in a single Python script that performs the entire data-reduction procedure.
- Full pipeline: stage not stated [Python]

### Satellite megaconstellations will threaten space-based astronomy. (Nature 2025)

- DOI: 10.1038/s41586-025-09759-5 | PMCID: PMC12675296 | PMID: 41339506
- Evidence: All analysis tools were programmed in Python.
- Full pipeline: stage not stated [Python]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Evidence: Python scripts were written and used to calculate the number of pixels in each annotated slice.
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: For all microglia within the cortex, the distance between each microglia and the nearest plaque was calculated using a custom Python script (find_nearest_neighbors2.py).
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: For this, we used the RandomForestClassifier implementation from the sklearn.ensemble module in Python, with default parameters except for n_estimators = 100.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Version used: **3.9**
- Evidence: Cell type and niche deconvolution We performed cell2location (v.0.1.3) 102 to deconvolute the cell types of our spatial transcriptomics data using public references in Python v.3.9.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### Origins of chromosome instability unveiled by coupled imaging and genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09632-5 | PMCID: PMC12695650 | PMID: 41162705
- Evidence: Manual annotation was performed with the assistance of a customized tool written in Python.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2] -> variant calling [DELLY, WhatsHap] -> quantification [ImageJ] -> machine learning [XGBoost] -> stage not stated [Bioconductor, Python]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Evidence: A custom Python script was used to parse CIGAR strings from the resulting BAM files and quantify indels.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Technological pathways for cost-effective steel decarbonization. (Nature 2025)

- DOI: 10.1038/s41586-025-09658-9 | PMCID: PMC12589104 | PMID: 41162702
- Evidence: It includes both R and Python scripts for implementing the plant-level net-zero pathway model, as well as procedures for conducting one-factor and multi-factor sensitivity analyses.
- Full pipeline: stage not stated [Python]

### Integration of hunger and hormonal state gates infant-directed aggression. (Nature 2025)

- DOI: 10.1038/s41586-025-09651-2 | PMCID: PMC12675289 | PMID: 41125886
- Version used: **3.7**
- Evidence: Offline data analysis was performed with Clampfit 10 software (Molecular Devices), WinEDR (v.4), WinWCP (v.5; http://spider.science.strath.ac.uk/sipbs/software_ses.htm ) and custom routines written in Python (v.3.7).
- Full pipeline: quantification [QuPath] -> registration [ImageJ] -> machine learning [scikit-learn] -> stage not stated [Python v3.7]

### Oxidative potential of atmospheric particles in Europe and exposure scenarios. (Nature 2025)

- DOI: 10.1038/s41586-025-09666-9 | PMCID: PMC12589103 | PMID: 41125890
- Evidence: 1 and 3 and Supplementary Table 2 ) using relative weights calculated as follows (using DescrStatsW() function of the statsmodels package in Python): 1 \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$${p}_{{\rm{c}}{\rm{...
- Full pipeline: stage not stated [Python, statsmodels]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Version used: **3.10**
- Evidence: The resulting count matrix for each sample was processed and filtered using Scanpy (v.1.9.1) in Python (v.3.10) 56 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Version used: **3.0.0**
- Evidence: Signal analyses were performed in Python (v.3.0.0) using JupyterLab (v.3.6.7, Project Jupyter).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Evidence: A custom Python script was then used to refine the start stop positions of the prophage regions within each genome, removing flanking 100 bp increments with coverage less than 25% of the mean prophage coverage (code is available at 10.26180/29946902.v1).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### Efficient and accurate search in petabase-scale sequence repositories. (Nature 2025)

- DOI: 10.1038/s41586-025-09603-w | PMCID: PMC12657231 | PMID: 41062695
- Evidence: For easy integration of results and coordination of different MetaGraph instances, we provide client interfaces in Python (Extended Data Fig.
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.0] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [Docker, Python, R v71.2, Snakemake]

### Age and gender distortion in online media and large language models. (Nature 2025)

- DOI: 10.1038/s41586-025-09581-z | PMCID: PMC12571887 | PMID: 41062689
- Evidence: Next, we applied the OpenCV deep learning module in Python to automatically extract the face from each image.
- Full pipeline: machine learning [OpenCV, Python]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Evidence: Visualizations were performed using Seaborn (v0.13.2) in Python.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Evidence: Missing value imputation To address missing values in our dataset, we used the K -nearest neighbours imputation method using the KNNImputer function from the scikit-learn library in Python 28 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Version used: **3.8.8**
- Evidence: Initial quality control and normalization Quality control and downstream analysis were performed in Python (v.3.8.8) using Scanpy (v.1.10.0), according to current expert recommendations for single-cell best practices 78 .
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### Learning the natural history of human disease with generative transformers. (Nature 2025)

- DOI: 10.1038/s41586-025-09529-3 | PMCID: PMC12589094 | PMID: 40963019
- Evidence: The transformer model is an encoder model based on the standard implementation provided in Python:pytorch (TransformerEncoder, TransformerEncoderLayer) with a context length of 128 tokens, an embedding size of 128, 2 multi-head attention blocks and a total of 2 sub-encoder layers, and the otherwise default parameters were used.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Jupyter, PyTorch, Python, scikit-learn]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: Analyses were done in Python.
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Evidence: Code availability Python scripts generated in this study are available from GitHub ( https://github.com/beleggia-lab/neuron-to-SCLC-synapses ) and Zenodo (10.5281/zenodo.15667860) 86 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: The Kernighan–Lin algorithm was implemented in Python as described previously 60 with the parameters C=0, KL_modified=True, random_labels=True, unweighted=True, and K=50 to partition the graph into eight groups.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### A brain-wide map of neural activity during complex behaviour. (Nature 2025)

- DOI: 10.1038/s41586-025-09235-0 | PMCID: PMC12408349 | PMID: 40903598
- Evidence: The task logic was programmed in Python, and the visual stimulus presentation and video capture were handled by Bonsai 93 and the BonVision package 94 .
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5, Python]

### A circuit that integrates drive state and social contact to gate mating. (Nature 2025)

- DOI: 10.1038/s41586-025-09327-x | PMCID: PMC12507686 | PMID: 40903568
- Evidence: Top and side infrared cameras (Basler, acquired at 10 Hz) were used to record behaviours and triggered in Python.
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [ImageJ, Python]

### Divergent evolutionary strategies pre-empt tissue collision in gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09447-4 | PMCID: PMC12527943 | PMID: 40903584
- Evidence: Quantitative data were analysed and processed using Excel, or custom-made ImageJ or FIJI macros and Python scripts using Numpy, Pandas and SciPy libraries.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [ImageJ, Matplotlib, NumPy, Python, SciPy, seaborn]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Evidence: We exploited this specificity by writing a Python script comparing each SNP of each hybrid worker with variants of a reference maternal genome ( M. ibericus queen genome with the highest coverage, SH19-06).
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### Spatial joint profiling of DNA methylome and transcriptome in tissues. (Nature 2025)

- DOI: 10.1038/s41586-025-09478-x | PMCID: PMC12571926 | PMID: 40903587
- Evidence: Clustering and data visualization We mapped the exact location of pixels on the bright-field tissue image using a custom Python script ( https://github.com/zhou-lab/Spatial-DMT-2024/tree/main/Data_preprocess/Image ), before removing additional empty barcodes on the basis of read-count thresholds determined by the knee plot (Extended Data Fig.
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [Python, R, UMAP, clusterProfiler, pheatmap] -> visualisation [Python] -> stage not stated [HOMER, Seurat]

### Patterned invagination prevents mechanical instability during gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09480-3 | PMCID: PMC12527948 | PMID: 40903575
- Version used: **3.10.7**
- Evidence: We performed the data wrangling, statistical analyses and plotting in R (v4.2.1) 61 using R Markdown notebooks in RStudio (v2022.7.2.576) 62 , and in Python (v3.10.7) using Jupyter notebooks (v6.5.4) 63 .
- Full pipeline: differential/statistical testing [Jupyter, Python v3.10.7, R v4.2.1] -> visualisation [Fiji v2.16.0, ImageJ v2.16.0] -> stage not stated [ilastik v1.3.3b]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: Methods Overview of software, data and workflow We conducted our LSP mapping workflow using Google Earth Engine (GEE) (v.0.1.404 or later) 65 and performed additional analyses using Python 66 with a set of core scientific packages (numpy 67 , shapely 68 , pandas 69 , geopandas 70 , rasterio 71 , xarray 72 , rasterstats 73 , dask 74 , scipy 75 , scikit-learn 76 , statsmodels 77 and matplotlib 78 ).
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### One-shot design of functional protein binders with BindCraft. (Nature 2025)

- DOI: 10.1038/s41586-025-09429-6 | PMCID: PMC12507698 | PMID: 40866699
- Version used: **3.9**
- Evidence: Steady-state response units were plotted against analyte concentration and a sigmoid function was fitted to the experimental data in Python v.3.9 to derive the K d .
- Full pipeline: alignment/mapping [AlphaFold] -> quantification [R] -> structure determination [PHENIX] -> visualisation [ChimeraX, Python v3.9]

### A compressed hierarchy for visual form processing in the tree shrew. (Nature 2025)

- DOI: 10.1038/s41586-025-09441-w | PMCID: PMC12545169 | PMID: 40866712
- Evidence: Visual stimulation Visual stimuli presentation Visual stimuli were generated and presented using custom Python scripts.
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [Python]

### Mapping urban gullies in the Democratic Republic of the Congo. (Nature 2025)

- DOI: 10.1038/s41586-025-09371-7 | PMCID: PMC12390838 | PMID: 40866674
- Evidence: 3 ), as well as other Python scripts used to create figures, are available at 10.48804/HTEZR0.
- Full pipeline: stage not stated [Python]

### Network synchrony creates neural filters promoting quiescence in Drosophila. (Nature 2025)

- DOI: 10.1038/s41586-025-09376-2 | PMCID: PMC12527942 | PMID: 40836080
- Evidence: Behavioural and connectome data were analysed using custom-made Python scripts.
- Full pipeline: quantification [OpenCV v4.9.0] -> stage not stated [Python]

### Data-driven de novo design of super-adhesive hydrogels. (Nature 2025)

- DOI: 10.1038/s41586-025-09269-4 | PMCID: PMC12328221 | PMID: 40770436
- Evidence: Protein sequences were exported in FASTA format 45 using the Bio.SeqIO interface in BioPython 46 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost] -> machine learning [UMAP] -> stage not stated [Python, scikit-learn v1.0.2]

### One-third of Sun-like stars are born with misaligned planet-forming disks. (Nature 2025)

- DOI: 10.1038/s41586-025-09324-0 | PMCID: PMC12350154 | PMID: 40770103
- Evidence: Code availability The Python script used to conduct the analysis and figure generation is publicly available on Zenodo 106 (10.5281/zenodo.15499660).
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, Python, SciPy]

### Excised DNA circles from V(D)J recombination promote relapsed leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-09372-6 | PMCID: PMC12443594 | PMID: 40770098
- Evidence: A custom Python script was used to automate BLAST searches against a custom BLAST database, consisting of all V-J recombination events or all head-to-head RSS combinations from the immunoglobulin kappa and lambda loci, for recombination and SJ libraries, respectively https://github.com/Boyes-Lab/LAM-ESC-Recombination 33 .
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [Python]

### Diffusing protein binders to intrinsically disordered proteins. (Nature 2025)

- DOI: 10.1038/s41586-025-09248-9 | PMCID: PMC12367549 | PMID: 40739343
- Version used: **3.9.7**
- Evidence: Microscopic images of both phase-separated and homogeneous droplets were analysed using a custom Python script (Python v3.9.7).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX v1.21.1] -> machine learning [RoseTTAFold] -> stage not stated [AlphaFold, ImageJ v1.54p, PyMOL v2.4.0, Python v3.9.7, UCSF Chimera v1.14]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Version used: **3.6.0**
- Evidence: The regression model was implemented using LinearRegression().fit from the scikit-learn package in Python (v.3.6.0 or newer).
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Longer scans boost prediction and cut costs in brain-wide association studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09250-1 | PMCID: PMC12367542 | PMID: 40670782
- Version used: **3.7**
- Evidence: Analyses were conducted in MATLAB (2018b) and Python 3.7.
- Full pipeline: stage not stated [FreeSurfer, Python v3.7]

### Replay and representation dynamics in the hippocampus of freely flying bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09341-z | PMCID: PMC12460160 | PMID: 40633570
- Evidence: Data were recorded and saved using custom-written scripts in Python.
- Full pipeline: stage not stated [Python]

### Plants monitor the integrity of their barrier by sensing gas diffusion. (Nature 2025)

- DOI: 10.1038/s41586-025-09223-4 | PMCID: PMC12350151 | PMID: 40604279
- Version used: **3.9**
- Evidence: Data analysis was performed with MS Excel v2308, R (v2024.04.2) and Python 3.9.
- Full pipeline: stage not stated [ImageJ, Python v3.9]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Evidence: Each object was related to its corresponding dilated GC object before exporting to a csv for further analysis in Python.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### Discovering cognitive strategies with tiny recurrent neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09142-4 | PMCID: PMC12390849 | PMID: 40604278
- Version used: **3.9**
- Evidence: Methods All data were analysed using Python 3.9 and PyTorch 1.13.
- Full pipeline: stage not stated [PyTorch v1.13, Python v3.9]

### Architecture, dynamics and biogenesis of GluA3 AMPA glutamate receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09325-z | PMCID: PMC12422969 | PMID: 40592473
- Evidence: These aligned particle stacks were exported to RELION using the Python script csparc2star.py 58 .
- Full pipeline: alignment/mapping [Python] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot v0.9.8.95, PHENIX v1.20, PyMOL v2.5] -> stage not stated [RELION v5.0]

### Nerve-to-cancer transfer of mitochondria during cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09176-8 | PMCID: PMC12328229 | PMID: 40562940
- Evidence: A custom Python script (available via GitHub at https://github.com/GreletLab/mtDNA-heteroplasmy ) was developed specifically for this project to process the obtained raw reads, align them to the target sequence, classify each read as wild type (mouse host-derived) or mutated (cancer cell-derived) and generate statistical output.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Python, SAMtools] -> quantification [DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Python] -> stage not stated [GSEA]

### Interactions between TTYH2 and APOE facilitate endosomal lipid transfer. (Nature 2025)

- DOI: 10.1038/s41586-025-09200-x | PMCID: PMC12328215 | PMID: 40562935
- Evidence: Further analysis, including Bell–Evans fitting for k off and X β values, was performed using in-house software developed in Python.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, ImageJ, Python, RELION, Topaz]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: From the sequence alignment map (.sam) file, those chromosome hits with only one alternative were filtered according to the ‘XA:Z:’ flag using a Python script written by GPT-4 (ChatGPT Plus, OpenAI).
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Unsupervised pretraining in biological neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09180-y | PMCID: PMC12367527 | PMID: 40533561
- Evidence: Data analysis For analysis, we used Python 3 (ref.
- Full pipeline: visualisation [Matplotlib] -> stage not stated [NumPy, Python, SciPy, Suite2p, scikit-learn]

### Vertically stacked monolithic perovskite colour photodetectors. (Nature 2025)

- DOI: 10.1038/s41586-025-09062-3 | PMCID: PMC12176651 | PMID: 40533540
- Evidence: The ColorChecker image was rendered from the individual pixel data through a dedicated Python script.
- Full pipeline: visualisation [Python]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Version used: **3.10**
- Evidence: Correlation plots were calculated using the SciPy package 77 in Python v.3.10 and plotted with Seaborn (Extended Data Fig.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Discovery analyses involving more than 20 comparisons underwent multiple testing correction using the p.adjust function in R or multipletests function in Python, applying the Benjamini–Hochberg method to control the false discovery rate at 0.05.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Evidence: Analysis and plotting were conducted with custom scripts in MATLAB 2022b, and Scipy 1.13.0 and Seaborn 0.13.2 in Python 3.
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Dynamic basal ganglia output signals license and suppress forelimb movements. (Nature 2025)

- DOI: 10.1038/s41586-025-09066-z | PMCID: PMC12367548 | PMID: 40437098
- Evidence: Obtained predictions were median-filtered with a filter size of 5 or filtered using sosfiltfilt in Python with an order of 4 and frequency of 15.
- Full pipeline: visualisation [ImageJ] -> stage not stated [DeepLabCut, Kilosort, Python]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: To calculate mean and median values, the built-in Python statistics module was used.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### In vivo screen of Plasmodium targets for mosquito-based malaria control. (Nature 2025)

- DOI: 10.1038/s41586-025-09039-2 | PMCID: PMC12267055 | PMID: 40399670
- Version used: **3.5**
- Evidence: Compound library evaluation through CACTI SMILES for each compound tested in this study were saved as a tabular file and queried using CACTI 55 command line version and Python 3.5 (Supplementary Table 4 ).
- Full pipeline: alignment/mapping [GATK v3.5] -> stage not stated [ImageJ, Python v3.5, SnpEff]

### Unravelling cysteine-deficiency-associated rapid weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-08996-y | PMCID: PMC12267064 | PMID: 40399674
- Evidence: The centroided data were searched using a custom Python script Mighty_skeleton v.0.0.2 and peak heights were extracted from the mzXML files based on a previously established library of metabolite retention times and accurate masses adapted from the Whitehead Institute 69 and verified with authentic standards and/or high resolution MS/MS spectral manually curated against the NIST14MS/MS 70 and METL...
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [DESeq2 v1.48, SciPy v1.1.0] -> visualisation [DESeq2 v1.48] -> stage not stated [HTSeq, Python, R]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Version used: **3.10**
- Evidence: The DEGs were detected using the scanpy.tl.rank_genes_groups() function with the default t -test from the Scanpy_1.8.2 in Python (v.3.10).
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: The results from single-cell analyses were plotted in Python.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Dopaminergic action prediction errors serve as a value-free teaching signal. (Nature 2025)

- DOI: 10.1038/s41586-025-09008-9 | PMCID: PMC12310545 | PMID: 40369067
- Evidence: The signal was then passed to a NIDAQ (National Instruments) and recorded and analysed using custom Python scripts as described in ‘Statistical analysis’.
- Full pipeline: quantification [DeepLabCut] -> differential/statistical testing [Python, scikit-learn, statsmodels] -> stage not stated [SciPy, pingouin]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Afterwards, gene expression counts were computed per cell and extracted using further custom Python scripts.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Light-microscopy-based connectomic reconstruction of mammalian brain tissue. (Nature 2025)

- DOI: 10.1038/s41586-025-08985-1 | PMCID: PMC12158774 | PMID: 40335689
- Version used: **3.8**
- Evidence: Data conversion for downstream analysis was performed with custom Python scripts implemented in Python v.3.8 or higher, including the Imaris-ims-file-reader, zarr, webKnossos and tifffile packages.
- Full pipeline: machine learning [PyTorch v1.12.1] -> stage not stated [BigStitcher, Jupyter, NumPy, Python v3.8, SciPy, scikit-image, seaborn]

### Native nucleosomes intrinsically encode genome organization principles. (Nature 2025)

- DOI: 10.1038/s41586-025-08971-7 | PMCID: PMC12240700 | PMID: 40335690
- Evidence: Condensability calculation for the PTM library The PTM library was de-multiplexed on the basis of the DNA hexamer barcodes by using a custom Python script and Bowtie2 aligner 52 .
- Full pipeline: alignment/mapping [Bowtie2, Python] -> simulation/modelling [OpenMM] -> stage not stated [GSEA, Jupyter, scikit-learn]

### Striatum supports fast learning but not memory recall. (Nature 2025)

- DOI: 10.1038/s41586-025-08969-1 | PMCID: PMC12244412 | PMID: 40335692
- Evidence: We then used a custom code in Python wrapping scikit-learn to find a weight or GLM coefficient (Extended Data Fig.
- Full pipeline: stage not stated [DeepLabCut, PyTorch, Python, scikit-learn]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **0.24**
- Evidence: The results of the optimization phase and the preregistered replication phase were compared and deemed to be largely compatible, with some minor exceptions (section 4 of Supplementary Information ). iEEG preprocessing Data were converted to BIDS 67 and preprocessed using MNE-Python (v0.24) 68 , and custom-written functions in Python and Matlab.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### A distributed coding logic for thermosensation and inflammatory pain. (Nature 2025)

- DOI: 10.1038/s41586-025-08875-6 | PMCID: PMC12222022 | PMID: 40269164
- Evidence: The ISH image was morphed to match its in vivo counterpart using these coordinates with a custom Python script that builds on the OpenCV library 3 .
- Full pipeline: quantification [NumPy v1.19.2, SciPy v1.5.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.19.2, SciPy v1.5.2] -> stage not stated [ImageJ, OpenCV, Python, Seurat, scDblFinder]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: Poly(A) lengths for each sequencing read were extracted from the pt:i tag (in the basecalled bam file) with a Python script.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### Functional connectomics spanning multiple areas of mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08790-w | PMCID: PMC11981939 | PMID: 40205214
- Evidence: A custom semi-automated user interface in Python was built for dynamic adaptation of fitting parameters throughout the scan to maximize pupil tracking accuracy and coverage.
- Full pipeline: machine learning [CaImAn] -> visualisation [Matplotlib, NumPy] -> stage not stated [Python, SciPy]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: Graph decomposition We decompose skeletons of axonal and dendritic processes into a directed tree graph (NetworkX object in Python 22 ; we provide a step-by-step online tutorial on how to export these as SWC files).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Evidence: All statistical analyses were performed using the scipy package in Python.
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Evidence: A custom Python script was used to parse the annotated FASTQ files and generate a count matrix containing all possible sgRNA pairs.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: The statistical analysis was done with the SciPy package v.1.10.1 in Python using a two-sided binomial test with a probability of success equal to 0.5.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: FOS density maps We generated 3D maps of FOS + cell density by applying a Gaussian kernel-density estimate (KDE) (function, scipy.stats.gaussian_kde) in Python to all FOS + cells across all animals in a given experimental condition (for example, novel flavour + consumption time point).
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### Connectome-driven neural inventory of a complete visual system. (Nature 2025)

- DOI: 10.1038/s41586-025-08746-0 | PMCID: PMC12119369 | PMID: 40140576
- Evidence: Clustering was performed in Python using the scipy.hierarchy 92 and fastcluster 93 libraries.
- Full pipeline: dimensionality reduction/clustering [Python, SciPy] -> structure determination [BigStitcher] -> stage not stated [Jupyter, NumPy, Snakemake]

### Changes in neurotensin signalling drive hedonic devaluation in obesity. (Nature 2025)

- DOI: 10.1038/s41586-025-08748-y | PMCID: PMC12119351 | PMID: 40140571
- Version used: **3.6.7**
- Evidence: All data analysis was performed using Python (version 3.6.7) and R (version 3.5.1).
- Full pipeline: alignment/mapping [kallisto v0.45.1] -> normalisation [kallisto v0.45.1] -> differential/statistical testing [edgeR v3.24.3] -> stage not stated [DeepLabCut, ImageJ, Python v3.6.7, R v3.5.1]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Evidence: The trimmed sequences were then added to their respective read names using an available Python script 39 .
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Record sea surface temperature jump in 2023-2024 unlikely but not unexpected. (Nature 2025)

- DOI: 10.1038/s41586-025-08674-z | PMCID: PMC11946890 | PMID: 40074909
- Evidence: All maps were created using the Basemap tool in Python ( https://matplotlib.org/basemap/stable/ ).
- Full pipeline: stage not stated [Matplotlib, Python]

### An operating system for executing applications on quantum network nodes. (Nature 2025)

- DOI: 10.1038/s41586-025-08704-w | PMCID: PMC11903313 | PMID: 40075182
- Evidence: Python was chosen because the NetQASM SDK is implemented in Python.
- Full pipeline: stage not stated [Python]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Evidence: Moreover, small contigs (<100,000 bp) with >80% of the sequence mapping to a named chromosome that contained one or more duplicated BUSCO genes, but no single BUSCO genes, were also removed using a Python script.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Impact of Amazonian deforestation on precipitation reverses between seasons. (Nature 2025)

- DOI: 10.1038/s41586-024-08570-y | PMCID: PMC11882456 | PMID: 40044888
- Evidence: Code availability All analysis and figure scripts were written in Python and are available at figshare (10.6084/m9.figshare.24911454.v4; ref.
- Full pipeline: stage not stated [CESM, Cartopy, Python, WRF]

### Aspirin prevents metastasis by limiting platelet TXA&lt;sub&gt;2&lt;/sub&gt; suppression of T cell immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-08626-7 | PMCID: PMC12018268 | PMID: 40044852
- Version used: **3.7.3**
- Evidence: Here, we modified the Linux-community and the core.py script to fix the seed to “123456” (run in Python version 3.7.3).
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3, QuPath]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: 3b ) comprises a combination of R and Python scripts described previously 27 ( https://zenodo.org/records/7113422 ) that we adapted.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Brain-wide presynaptic networks of functionally distinct cortical neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-08631-w | PMCID: PMC12043506 | PMID: 40011781
- Evidence: Processing of two-photon calcium images Two-photon Ca 2+ images were processed using Suite2p 78 , in Python, with default parameters, unless otherwise indicated.
- Full pipeline: stage not stated [Python, Suite2p]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Version used: **3.11.6**
- Evidence: All analyses were performed using GraphPad Prism (version 10.1.1) or Python (version 3.11.6).
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: Initial parameter estimation: g and A tensors were estimated using laboratory-developed scripts in Python (SciPy/NumPy) 74 .
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Evidence: Fatash is implemented in Python/Cython as a submodule in the HaploNet software suite.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **3.9.12**
- Evidence: In brief, LOESS regression was performed on using the lowess function of the statsmodels package (v.0.13.5) in Python (v.3.9.12) with a 20 amino acid sliding window (‘frac = (20 AA/ L )’, where L is the total length of the protein), and ‘it = 0’ to fit observed log 2 [fold change in sgRNA enrichment], hereafter the sgRNA enrichment score, as a function of amino acid position.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Evidence: These post-processing steps were written in Python and available at GitHub ( https://github.com/Wu-Lab-DFCI-Harvard/bulkrhTCR_Script) .
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Emergence of collective oscillations in massive human crowds. (Nature 2025)

- DOI: 10.1038/s41586-024-08514-6 | PMCID: PMC11798876 | PMID: 39910390
- Evidence: We used a Python script available on GitHub to homogenize the brightness of the image 32 , 33 .
- Full pipeline: stage not stated [NumPy, Python]

### Engineering a genomically recoded organism with one stop codon. (Nature 2025)

- DOI: 10.1038/s41586-024-08501-x | PMCID: PMC11903333 | PMID: 39910296
- Evidence: Data were analysed with a custom Python script.
- Full pipeline: stage not stated [AlphaFold, Python]

### SARS-CoV-2 evolution on a dynamic immune landscape. (Nature 2025)

- DOI: 10.1038/s41586-024-08477-8 | PMCID: PMC11882442 | PMID: 39880955
- Version used: **3.11.3**
- Evidence: Code availability Codes were written in Python 3.11.3 and R version 4.2.3 (15 March 2023) and are available via GitHub at https://github.com/KleistLab/VASIL and via Zenodo at 10.5281/zenodo.8349295 (ref.
- Full pipeline: stage not stated [Pangolin, Python v3.11.3, R v4.2.3, SciPy]

### Regional and institutional trends in assessment for academic promotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08422-9 | PMCID: PMC11821531 | PMID: 39843736
- Evidence: Data visualization Data from Stata were imported into Python 3 and plotted using Python’s Matplotlib, seaborn and geopandas libraries.
- Full pipeline: visualisation [Matplotlib, Python, seaborn]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: For further analysis using moscot.time in Python, the Seurat objects were transformed into AnnData 96 objects using SeuratData 97 .
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: All statistical analysis and plotting were performed in GraphPad 9 and 10 (GraphPad) or in Python.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### The sequence-structure-function relationship of intrinsic ERα disorder. (Nature 2025)

- DOI: 10.1038/s41586-024-08400-1 | PMCID: PMC11864982 | PMID: 39779860
- Evidence: R 1 and R 1ρ rates were obtained by fitting mono-exponential decays using in-house Python scripts.
- Full pipeline: quantification [ImageJ] -> machine learning [AlphaFold] -> stage not stated [Python]

### Steering perovskite precursor solutions for multijunction photovoltaics. (Nature 2025)

- DOI: 10.1038/s41586-024-08546-y | PMCID: PMC11882461 | PMID: 39715627
- Evidence: Optical simulations and optimizations were performed using a custom-made program 65 , written in Python, based on the ‘tmm’ transfer-matrix modelling Python module 66 .
- Full pipeline: simulation/modelling [Python]

### The conformational space of RNase P RNA in solution. (Nature 2025)

- DOI: 10.1038/s41586-024-08336-6 | PMCID: PMC11779636 | PMID: 39695229
- Evidence: The optimized volume fraction, ν , for each component of the ensemble is obtained by minimizing the discrepancy between the back-calculated I Total and I experimental ( χ 2 ) curves using an in-house Python script that implements an iterative least-squares process 70 by applying a trust region reflective algorithm 71 , with boundaries of 0 ≤ ν i ≥1.
- Full pipeline: quantification [ImageJ] -> stage not stated [Python]

### Hierarchical design of pseudosymmetric protein nanocages. (Nature 2025)

- DOI: 10.1038/s41586-024-08360-6 | PMCID: PMC11821544 | PMID: 39695230
- Version used: **3.8.8**
- Evidence: Scripts and plots All data were processed and plotted using Python 3.8.8, matplotlib 3.3.4 and seaborn 0.11.1.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [RELION, UCSF Chimera] -> visualisation [Matplotlib v3.3.4, Python v3.8.8, seaborn v0.11.1] -> stage not stated [ChimeraX, ImageJ]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Evidence: The final graphs and videos were prepared using a custom Python script.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### Understanding the neural code of stress to control anhedonia. (Nature 2025)

- DOI: 10.1038/s41586-024-08241-y | PMCID: PMC11735319 | PMID: 39633053
- Evidence: The new distance d assigned to the agglomerated clusters was defined as d ( u , v ) = max(dist( u [ p ], v [ q ])), in which p and q represent all of the points in the merged clusters u and v , also known as the farthest point algorithm (sklearn.cluster.AgglomerativeClustering, built-in class in scikit-learn in Python 67 ).
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [DeepLabCut, Kilosort]

### Synthetic GPCRs for programmable sensing and control of cell behaviour. (Nature 2025)

- DOI: 10.1038/s41586-024-08282-3 | PMCID: PMC11666456 | PMID: 39633047
- Evidence: Data analysis was performed using custom written Python scripts.
- Full pipeline: quantification [Matplotlib] -> differential/statistical testing [SciPy, seaborn] -> stage not stated [AlphaFold, ImageJ, MACS2, PHENIX, Python]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Version used: **3.9**
- Evidence: Non-negative matrix factorization was performed using the cNMF package in Python (v.3.9) 59 .
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Evidence: Specifically, Nxr/Nar and PmoA/AmoA amino acid reference sequences were downloaded 30 , 88 , 89 and this set of reference sequences was combined with amino acid sequences of homologues from the GROWdb, aligned separately using MUSCLE (v.3.8.31) and run through a Python script for generating phylogenetic trees (ProtPipeliner; https://github.com/WrightonLabCSU/Protpipeliner/tree/main ) 90 , 91 .
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Social state alters vision using three circuit mechanisms in Drosophila. (Nature 2025)

- DOI: 10.1038/s41586-024-08255-6 | PMCID: PMC11735400 | PMID: 39567699
- Evidence: Using custom Python scripts, regions of interest (ROIs) corresponding to cell compartments were identified in the high-resolution images.
- Full pipeline: stage not stated [Python]

### Engineered receptors for soluble cellular communication and disease sensing. (Nature 2025)

- DOI: 10.1038/s41586-024-08366-0 | PMCID: PMC11839477 | PMID: 39542025
- Evidence: Acquisition was controlled with NIS Elements software and data were analysed with Fiji and custom-written Python scripts.
- Full pipeline: stage not stated [Jupyter, Python]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Evidence: The distributions for each cell type and tumour type are visualized using the sns.kdeplot function in Python Seaborn (v.0.11.2) ( Extended Data Fig.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Designed endocytosis-inducing proteins degrade targets and amplify signals. (Nature 2025)

- DOI: 10.1038/s41586-024-07948-2 | PMCID: PMC11839401 | PMID: 39322662
- Evidence: Acquisition was controlled via NIS Elements software and data were analysed via Fiji and custom-written Python scripts.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, Python, RoseTTAFold]

### A prototype differential atom interferometer for fundamental physics. (Nature 2026)

- DOI: 10.1038/s41586-026-10617-1 | PMCID: PMC13275304 | PMID: 42310113
- Evidence: The control software is written in Python and is available as open source at ref.
- Full pipeline: simulation/modelling [PyMC] -> stage not stated [Python]

### Light-induced quantum friction of carbon nanotubes in water. (Nature 2026)

- DOI: 10.1038/s41586-026-10632-2 | PMCID: PMC13293881 | PMID: 42271052
- Version used: **3.10.5**
- Evidence: All analyses were conducted using Python 3.10.5.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Python v3.10.5]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Module network visualization and association analyses The rodent gene correlation network was visualized through spectral embedding 249 , 250 in Python.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **3.12.8**
- Evidence: The Leiden method was implemented using the Python module leidenalg (v.0.10.2) in Python (v.3.12.8), which was loaded with reticulate (v.1.40.0) into R.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### Plasticity and language in the anaesthetized human hippocampus. (Nature 2026)

- DOI: 10.1038/s41586-026-10448-0 | PMCID: PMC13275293 | PMID: 42092132
- Evidence: The acquired back-projection images were reconstructed using Scout-and-Scan Reconstructor (Carl Zeiss, v.16.8) and converted to NRRD format using the Harwell Automated Recon Processor (HARP, v.2.4.1) 57 , an open-source, cross-platform application developed in Python.
- Full pipeline: registration [Kilosort] -> structure determination [Python] -> stage not stated [SpikeInterface]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: Scatterplots visualizing PFS preferences were generated using Matplotlib in Python.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Systematic partisan content skews in TikTok during the 2024 US elections. (Nature 2026)

- DOI: 10.1038/s41586-026-10447-1 | PMCID: PMC13293873 | PMID: 42092134
- Version used: **3.13.1**
- Evidence: Code availability All data analysis was conducted using Python 3.13.1.
- Full pipeline: stage not stated [Python v3.13.1]

### Pervasive and programmed nucleosome distortion on single chromatin fibres. (Nature 2026)

- DOI: 10.1038/s41586-026-10418-6 | PMCID: PMC13253354 | PMID: 42056506
- Evidence: Computing the enrichment of nucleosomal distortion patterns and translational positions across distinct genomic loci To compute ORs for Leiden-defined clusters across epigenomic domains and repeat elements, or for bound versus randomly sampled TF motifs, Fisher’s exact tests were done with scipy (in Python).
- Full pipeline: dimensionality reduction/clustering [ChimeraX v1.7.1, Python, Scanpy v1.9.3, UMAP] -> visualisation [ChimeraX v1.7.1, Scanpy v1.9.3, UMAP] -> stage not stated [SciPy]

### Demography and life histories across the Roman frontier in Germany 400-700 CE. (Nature 2026)

- DOI: 10.1038/s41586-026-10437-3 | PMCID: PMC13293882 | PMID: 42056513
- Evidence: 7.4 , 8.17 and 10.1 – 10.7 , were created using the basemap toolkit from the matplotlib library 84 in Python 3, which uses cartographic data from Generic Mapping Tools ( https://www.generic-mapping-tools.org/ ).
- Full pipeline: alignment/mapping [Matplotlib, Python] -> registration [GATK v3.8] -> differential/statistical testing [statsmodels v0.14.4]

### Training language models to be warm can reduce accuracy and increase sycophancy. (Nature 2026)

- DOI: 10.1038/s41586-026-10410-0 | PMCID: PMC13128435 | PMID: 42056545
- Version used: **3.11.4**
- Evidence: We used α = 0.05 for all tests conducted in Python 3.11.4 with the statsmodels package.
- Full pipeline: stage not stated [Python v3.11.4, statsmodels]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Evidence: VMD (v.1.9) 66 was used for visualization of molecular dynamics simulation results; Python 3 and MDAnalysis (v.2.7.0) 67 were used to analyse molecular dynamics results and generate molecular dynamics-related figures.
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### Myosin forces remodel F-actin for mechanosensitive protein recognition. (Nature 2026)

- DOI: 10.1038/s41586-026-10398-7 | PMCID: PMC13233326 | PMID: 42020745
- Evidence: Coarse-grained molecular dynamics Parameterization Coarse-grained molecular dynamics simulations of individual actin filaments under force were performed using the software package ESPResSO 101 and custom Python scripts.
- Full pipeline: simulation/modelling [Python] -> structure determination [IMOD] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [EMAN2, MotionCor2, PHENIX, RELION, SciPy]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: Python scripts were run using v.3.10 with polars v.1.20.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Focal white matter lesions drive grey matter inflammation and synapse loss. (Nature 2026)

- DOI: 10.1038/s41586-026-10414-w | PMCID: PMC13293868 | PMID: 42020752
- Evidence: Spatial barcodes were extracted from sequencing reads using a custom Python script and written to separate FASTQ files.
- Full pipeline: read trimming [Snakemake v7.24.0] -> quantification [ImageJ v1.54p] -> dimensionality reduction/clustering [UMAP] -> visualisation [Bioconductor, ComplexHeatmap, UMAP] -> stage not stated [Python, R, Seurat, igraph]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Evidence: We applied hierarchical clustering on the top 30 principal components (PCs) using the sklearn.cluster.AgglomerativeClustering function in Python with default parameters and n_clusters = m.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **3.8**
- Evidence: The sgRNA count matrices were constructed using Python 3.8.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: Gene counts per cell were subsequently aggregated using custom Python scripts.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Molecular basis for methylation-sensitive editing by Cas9. (Nature 2026)

- DOI: 10.1038/s41586-026-10384-z | PMCID: PMC13216068 | PMID: 41986708
- Evidence: An in-house program based on Python scripts and bed utilities was used to identify genes that are differentially methylated in different cell lines.
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [Python, R] -> structure determination [PHENIX, RELION v4.0] -> stage not stated [Topaz]

### Composable neural emulators accelerate thermoelectric generator design. (Nature 2026)

- DOI: 10.1038/s41586-026-10223-1 | PMCID: PMC13083250 | PMID: 41986625
- Version used: **3.10**
- Evidence: All algorithms were implemented in Python (version 3.10) using the PyTorch module.
- Full pipeline: stage not stated [PyTorch, Python v3.10]

### Biodiversity resilience in a tropical rainforest. (Nature 2026)

- DOI: 10.1038/s41586-026-10365-2 | PMCID: PMC13128449 | PMID: 41951739
- Evidence: We used the function optimize.curve_fit from the scipy package v.1.10.0 in Python to fit equation ( 5 ) to the data.
- Full pipeline: stage not stated [Jupyter, Python, R, SciPy]

### Satellite imagery reveals increasing volatility in human night-time activity. (Nature 2026)

- DOI: 10.1038/s41586-026-10260-w | PMCID: PMC13061621 | PMID: 41951967
- Version used: **3.10**
- Evidence: Code availability The global ALAN change dataset and analyses were produced with custom code using MATLAB 2022b and Python 3.10, which are available at Zenodo 61 (10.5281/zenodo.18264642).
- Full pipeline: stage not stated [Python v3.10]

### Saturation editing of RNU4-2 reveals distinct dominant and recessive disorders. (Nature 2026)

- DOI: 10.1038/s41586-026-10334-9 | PMCID: PMC13253345 | PMID: 41951737
- Evidence: For each variant, P values were determined using the norm.cdf function in Python, defining a normal distribution from the mean and standard deviation of function scores for negative control insertions.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: DEGs for DTA mice were determined instead in Python using Scanpy’s rank_genes_groups function and using Wilcoxon rank-sum tests to determine statistical significance.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### An enteric neuron ionotropic receptor regulates salt stress resistance. (Nature 2026)

- DOI: 10.1038/s41586-026-10348-3 | PMCID: PMC13293861 | PMID: 41922765
- Evidence: To calculate the pumping rates, 2 min of pumping events from the recording was analysed using custom software written in Python ( https://github.com/venkatachalamlab/Yeon-2025-pumping-analysis ).
- Full pipeline: read trimming [Trim Galore v10.5281] -> alignment/mapping [IMOD, Trim Galore v10.5281] -> structure determination [IMOD] -> stage not stated [Python]

### General scales unlock AI evaluation with explanatory and predictive power. (Nature 2026)

- DOI: 10.1038/s41586-026-10303-2 | PMCID: PMC13043289 | PMID: 41922702
- Version used: **3.11**
- Evidence: For implementation, the RF models were trained using the scikit-learn library 88 , whereas the fine-tuned LLaMA-3.1-8B was trained on the Transformers library 89 using the PyTorch backend running on Python 3.11.
- Full pipeline: machine learning [PyTorch, Python v3.11, scikit-learn]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Version used: **3.8.2**
- Evidence: Reconstruction of gene regulatory and TF networks The activity of specific TFs in each cell type was inferred in the mouse glial lineage cells using the package pySCENIC (v.0.10.3), implemented in Python (v.3.8.2).
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Towards end-to-end automation of AI research. (Nature 2026)

- DOI: 10.1038/s41586-026-10265-5 | PMCID: PMC13017497 | PMID: 41882133
- Evidence: Unlike other node types, aggregation nodes do not conduct new experiments but simply generate a Python script to aggregate and summarize previous results.
- Full pipeline: machine learning [NumPy] -> stage not stated [Python]

### Observing the tidal pulse of rivers from wide-swath satellite altimetry. (Nature 2026)

- DOI: 10.1038/s41586-026-10287-z | PMCID: PMC13061602 | PMID: 41851459
- Evidence: Tidal analysis We used the unified tidal analysis and prediction functions (UTide) 58 implemented in Python 59 to conduct a harmonic analysis to estimate the node-scale M 2 and O 1 amplitudes from the RiverSP WSE time series.
- Full pipeline: visualisation [Matplotlib, QGIS] -> stage not stated [Python]

### Synthetic circuits for cell ratio control. (Nature 2026)

- DOI: 10.1038/s41586-026-10259-3 | PMCID: PMC13171440 | PMID: 41851453
- Version used: **3.8.5**
- Evidence: All simulations were performed in Python (v.3.8.5).
- Full pipeline: quantification [ImageJ v1.54g] -> simulation/modelling [Python v3.8.5] -> stage not stated [CellProfiler v4.2.1]

### Climbing fibres recruit disinhibition to enhance Purkinje cell calcium signals. (Nature 2026)

- DOI: 10.1038/s41586-026-10220-4 | PMCID: PMC13171427 | PMID: 41851460
- Evidence: The network simulator along with its analysis was written in Python using the package ANNarchy 53 and run on a 16-core machine.
- Full pipeline: simulation/modelling [Python] -> stage not stated [Kilosort v2.0]

### In vivo site-specific engineering to reprogram T cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10235-x | PMCID: PMC13083257 | PMID: 41851456
- Evidence: Clonality metrics and visualization were performed using custom Python scripts.
- Full pipeline: visualisation [Python] -> stage not stated [MACS2, Slingshot]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **7.34.0**
- Evidence: Data processing, model training and evaluation were implemented in Python using numpy v.2.0.2, tensorflow v.2.19.0, scipy v.1.16.3, statsmodels v.0.14.6, sklearn v.1.6.1, shap v.0.50.0, xgboost v.3.1.2, torch v.2.9.0, pandas v.2.2.2, umap v.0.5.9.post2, pickle v.4.0, pytz v.2025.2, re v.2.2.1, tqdm v.4.67.1, IPython v.7.34.0, json v.2.0.9 and altair v.5.5.0.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Version used: **3.10**
- Evidence: All computational analyses and visualizations were performed in Python (v3.10), using the NumPy 76 , Pandas 77 , SciPy 78 and Matplotlib 79 libraries.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### Natural maternal immunity protects neonates from Escherichia coli sepsis. (Nature 2026)

- DOI: 10.1038/s41586-026-10225-z | PMCID: PMC13108393 | PMID: 41813901
- Evidence: Pairwise SNP distances were calculated from the resulting VCF file using custom Python scripts.
- Full pipeline: quality control [FastQC v0.12.1, NanoPlot v1.46.0] -> alignment/mapping [MAFFT v7.526, QUAST v5.2.0.2] -> stage not stated [Python, SPAdes]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: The merged reads were parsed by SeqIO module in BioPython 51 .
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Snapshots of the dynamic basis of NTSR1 G protein subtype promiscuity. (Nature 2026)

- DOI: 10.1038/s41586-026-10120-7 | PMCID: PMC13083256 | PMID: 41813894
- Evidence: VMD 55 and Python scripting were employed for analysis.
- Full pipeline: simulation/modelling [NAMD] -> structure determination [Coot, PHENIX] -> stage not stated [Python, VMD]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: The Seurat object, along with Slingshot pseudotime coordinates, was converted to an AnnData object with Seurat’s Convert function for analysis in Python.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Version used: **3.0**
- Evidence: To quantify the density distribution, the nuclear membrane surface was divided into ~100 patches using a Python 3.0 script ( https://github.com/gparlakgul/nuclear_pore ), with each patch assigned a unique pixel intensity as an identifier (Supplementary Fig.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: MARINE is implemented in Python, leveraging pysam for alignment manipulation, pandas and polars for data handling and multiprocessing for parallelization.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: We examined the differential expression of LCN2 and ATF4 between inflamed and immune-excluded phenotypes using analysis done with the Wilcoxon rank-sum test (Mann–Whitney U test), implemented in Python’s scipy.stats library to identify significant differences between these specific immune contexts.
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Version used: **3.10**
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### Rete ridges form via evolutionarily distinct mechanisms in mammalian skin. (Nature 2026)

- DOI: 10.1038/s41586-025-10055-5 | PMCID: PMC12959975 | PMID: 41639458
- Version used: **3.8.20**
- Evidence: SAW realign Visualization output.gef files were loaded into Stereopy (1.5.0) in Python (3.8.20) using read_gef() and bin_size = 20.
- Full pipeline: quality control [UMAP] -> quantification [Fiji v1.53c, ImageJ v1.53c, R v4.2.2] -> normalisation [UMAP] -> registration [Python v3.8.20] -> dimensionality reduction/clustering [CellChat, ComplexHeatmap, UMAP] -> visualisation [Python v3.8.20, R v4.2.2] -> stage not stated [Monocle, Seurat]

### GlycoRNA complexed with heparan sulfate regulates VEGF-A signalling. (Nature 2026)

- DOI: 10.1038/s41586-025-10052-8 | PMCID: PMC12999495 | PMID: 41606331
- Evidence: Colocalization of spots from paired channels were analysed by implementing a custom Python script ( https://github.com/FlynnLab/jonperr ) to identify the nearest neighbours of each spot (in nm) with a k-d tree algorithm (scipy.spatial.KDTree).
- Full pipeline: read trimming [Cutadapt v4.9, DESeq2 v1.42.1] -> alignment/mapping [Bowtie2 v2.5.4] -> differential/statistical testing [DESeq2 v1.42.1] -> stage not stated [ImageJ, Python, SciPy]

### Construction of complex and diverse DNA sequences using DNA three-way junctions. (Nature 2026)

- DOI: 10.1038/s41586-025-10006-0 | PMCID: PMC12979194 | PMID: 41565816
- Evidence: The junctions for all sequencing runs were generated and analysed as described above and visualized using custom Python scripts.
- Full pipeline: alignment/mapping [BLAST] -> visualisation [Python]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **3.10.12**
- Evidence: Statistical analysis Statistical analyses were performed in Python (v3.10.12) using libraries scikit-bio (v0.5.9), scipy (v1.10.1) and statsmodels (v0.14.0).
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: Processed and merged reads were then analysed using custom Python scripts to count the frequency of the LetA variants 75 .
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Version used: **3.6**
- Evidence: Doublets were identified from the filtered aggregated count files using Scrublet 74 in Python v.3.6 or scDblFinder v.1.12 in R statistical software v.4.2.2.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Dominant contribution of Asgard archaea to eukaryogenesis. (Nature 2026)

- DOI: 10.1038/s41586-025-09960-6 | PMCID: PMC12872458 | PMID: 41535464
- Evidence: The resulting hits were then clustered using greedy set clustering, as described in mmseqs2, implemented in Python.
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn v1.3.0] -> stage not stated [SciPy]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: Pearson’s R values above the channel intensity thresholds determined by the Coloc 2 bisection algorithm were plotted using custom Python scripts.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### A mechanical ratchet drives unilateral cytokinesis. (Nature 2026)

- DOI: 10.1038/s41586-025-09915-x | PMCID: PMC12916326 | PMID: 41501469
- Evidence: The kymographs were processed in Python: the data were thresholded with the Otsu method and contours were detected using skimage.measure.find_contours 63 .
- Full pipeline: differential/statistical testing [SciPy] -> visualisation [SciPy] -> stage not stated [Python, TrackMate, scikit-image]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Evidence: The log 2 fold change values for these scores were computed for the nucleotides at PFS positions (+1 to +5), and scatterplots visualizing the PFS preferences were generated using Matplotlib in Python.
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: Analysis Image processing Scanbox.sbx files were converted to tiff format and motion-corrected and segmented using Suite2p in Python ( https://github.com/MouseLand/suite2p ).
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Human gut M cells resemble dendritic cells and present gluten antigen. (Nature 2026)

- DOI: 10.1038/s41586-025-09829-8 | PMCID: PMC12872457 | PMID: 41372409
- Version used: **3.11.9**
- Evidence: Analysis was performed in Python (v.3.11.9) using the Scanpy library and the recipe based on Wu et al.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler v3.14.3] -> visualisation [Seurat v3.1.4] -> stage not stated [Enrichr, Python v3.11.9, R, Scanpy]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: The command line tool in Python implementation was adapted to be able to work with BAM files generated by BD Rhapsody, using samtools 64 to format the files, mainly by removing all possible alignments with antibodies and renaming the UMI barcode tag to ‘UB’ instead of ‘MA’.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **3.7.6**
- Evidence: This was performed by fitting the equation 100 × e (− x × tau) in Python (v.3.7.6) and the package scipy (v.1.4.1) to each kinase’s CHX screening trajectory. t -SNE plots were generated with sklearn and matplotlib (v.1.0.1 and v.3.5.3, respectively) from ChEMBL drug-binding data processed as described in the Chemical Checker (CC) 24 and compounds were characterized with CC global bioactivity signa...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Vicarious body maps bridge vision and touch in the human brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09796-0 | PMCID: PMC12872459 | PMID: 41299177
- Evidence: Model fitting All model fitting was conducted in Python, exploiting the routines implemented by the ‘Himalaya’ package 60 .
- Full pipeline: stage not stated [Connectome Workbench, Python, R, afex, emmeans]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Evidence: 62 ) in Python to identify and remove branches in the tree with branch lengths greater than 20 times the median branch length.
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Version used: **3.11.8**
- Evidence: All code for sampling and downstream analysis using Evo was written in Python (v3.11.8).
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Repulsions instruct synaptic partner matching in an olfactory circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09768-4 | PMCID: PMC12804089 | PMID: 41261130
- Evidence: The preference index is calculated in Python by ( I ¯ VA 1 d − I ¯ VA 1 v ) / ( I ¯ VA 1 d + I ¯ VA 1 v ) .
- Full pipeline: stage not stated [Python]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Version used: **3.9**
- Evidence: All subsequent image analyses were then performed in Python (v.3.9).
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Olympiad-level formal mathematical reasoning with reinforcement learning. (Nature 2026)

- DOI: 10.1038/s41586-025-09833-y | PMCID: PMC12999475 | PMID: 41225005
- Evidence: Supplementary Data 1 Pseudocode written in Python elaborating the high-level structure of AlphaProof: RL, auto-formalization and variant generation.
- Full pipeline: stage not stated [Python]

### Neuroendocrine control of calcium mobilization in the fruit fly. (Nature 2026)

- DOI: 10.1038/s41586-025-09670-z | PMCID: PMC12727502 | PMID: 41125891
- Version used: **3.9**
- Evidence: The speed of individual larvae was calculated using Python 3.9 by averaging 2–4 speed measurements along a consecutive trajectory.
- Full pipeline: simulation/modelling [Python v3.9] -> stage not stated [ImageJ]

### Constructing local cell-specific networks from single-cell data. (PNAS 2021)

- DOI: 10.1073/pnas.2113178118 | PMCID: PMC8713783 | PMID: 34903665
- Version used: **3.7.6**
- Evidence: Runtimes are measured under Python 3.7.6 [MSC v.1916 32 bit (Intel)].
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot, UMAP] -> stage not stated [Python v3.7.6, WGCNA]

### An open repository of real-time COVID-19 indicators. (PNAS 2021)

- DOI: 10.1073/pnas.2111452118 | PMCID: PMC8713778 | PMID: 34903654
- Evidence: All processing is done using open-source code written primarily in Python and R, and available publicly at https://github.com/cmu-delphi/covidcast-indicators/ .
- Full pipeline: stage not stated [Python, R]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Evidence: Meanwhile, we estimated the divergence patterns for these outlier windows using the d XY statistic calculated by an egglib_sliding_windows.py Python script ( https://github.com/johnomics ) and defined windows in the top 1% percentile of d XY values as d XY “islands” and the bottom 1% windows as d XY “valleys.” For comparison purposes, we generated 20 replicates of randomly selected sets of 186 aut...
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### Global monitoring of the impact of the COVID-19 pandemic through online surveys sampled from the Facebook user base. (PNAS 2021)

- DOI: 10.1073/pnas.2111455118 | PMCID: PMC8713788 | PMID: 34903657
- Version used: **3.8**
- Evidence: Therefore, this method was used for all analyses and is presented throughout (LightGBM in Python 3.8 with Shapley values visualization package for predictor visualization).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap v2.3.4, R v3.6] -> differential/statistical testing [LightGBM] -> visualisation [ComplexHeatmap v2.3.4, Python v3.8, R v3.6]

### Closed microbial communities self-organize to persistently cycle carbon. (PNAS 2021)

- DOI: 10.1073/pnas.2013564118 | PMCID: PMC8609437 | PMID: 34740965
- Evidence: Sensor readout, temperature feedback, and control of illumination were performed by a Raspberry Pi computer running custom Python scripts.
- Full pipeline: stage not stated [DADA2, Python, QIIME 2]

### Shared neural codes for visual and semantic information about familiar faces in a common representational space. (PNAS 2021)

- DOI: 10.1073/pnas.2110474118 | PMCID: PMC8609335 | PMID: 34732577
- Evidence: All analyses were implemented in Python and PyMVPA ( 47 ).
- Full pipeline: stage not stated [AFNI, Python, SUMA, fMRIPrep v1.0.3]

### Miniaturized wireless, skin-integrated sensor networks for quantifying full-body movement behaviors and vital signs in infants. (PNAS 2021)

- DOI: 10.1073/pnas.2104925118 | PMCID: PMC8639372 | PMID: 34663725
- Version used: **2.7.15**
- Evidence: Simultaneous computations of the rotation minimize these errors ( 20 ), as executed in software code written in Python 2.7.15+ and ROS Melodic, available on a web-based source code management cloud ( 21 ).
- Full pipeline: stage not stated [Python v2.7.15]

### Relict inland mangrove ecosystem reveals Last Interglacial sea levels. (PNAS 2021)

- DOI: 10.1073/pnas.2024518118 | PMCID: PMC8522267 | PMID: 34607943
- Evidence: To set the parameters α and β describing the Γ distribution, we used the pylue Python script ( https://github.com/joaks1/pyule ) to calculate the expected height of the population tree.
- Full pipeline: differential/statistical testing [BEAST] -> simulation/modelling [BEAST] -> stage not stated [Python, VCFtools v0.1.14]

### Computational prediction of the effect of amino acid changes on the binding affinity between SARS-CoV-2 spike RBD and human ACE2. (PNAS 2021)

- DOI: 10.1073/pnas.2106480118 | PMCID: PMC8594574 | PMID: 34588290
- Evidence: All codes were developed in Python using the PyTorch library.
- Full pipeline: stage not stated [PyTorch, Python]

### The translatome of neuronal cell bodies, dendrites, and axons. (PNAS 2021)

- DOI: 10.1073/pnas.2113929118 | PMCID: PMC8639352 | PMID: 34670838
- Evidence: An in-house Python script was used to count mRNA puncta in the somata and the neuropil layer, respectively.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt] -> alignment/mapping [Bowtie2 v2.3.5.1, STAR v2.7.3, featureCounts v2.0.0] -> stage not stated [DESeq2 v1.30.1, Python]

### Visual exposure enhances stimulus encoding and persistence in primary cortex. (PNAS 2021)

- DOI: 10.1073/pnas.2105276118 | PMCID: PMC8639370 | PMID: 34663727
- Evidence: A similar implementation of the model in Python (with absent W II connections) can be found at https://github.com/chrhartm ( 42 ).
- Full pipeline: stage not stated [FieldTrip, Python]

### Amyloid-β peptide dimers undergo a random coil to β-sheet transition in the aqueous phase but not at the neuronal membrane. (PNAS 2021)

- DOI: 10.1073/pnas.2106210118 | PMCID: PMC8488611 | PMID: 34544868
- Evidence: This calculation was accomplished with a Python script available at https://github.com/NMRLipids/MATCH ( 64 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> visualisation [VMD] -> stage not stated [Python]

### Trapping or slowing the diffusion of T cell receptors at close contacts initiates T cell signaling. (PNAS 2021)

- DOI: 10.1073/pnas.2024250118 | PMCID: PMC8488633 | PMID: 34526387
- Version used: **3.8**
- Evidence: A bespoke parallel processing Python script (Python 3.8) was used to loop simulations many times for each set of parameters.
- Full pipeline: simulation/modelling [Python v3.8] -> stage not stated [TrackMate]

### Shotgun scanning glycomutagenesis: A simple and efficient strategy for constructing and characterizing neoglycoproteins. (PNAS 2021)

- DOI: 10.1073/pnas.2107440118 | PMCID: PMC8488656 | PMID: 34551980
- Evidence: Data Availability Python scripts have been deposited in GitHub ( https://github.com/tdm76/Li_PNAS_2021 ).
- Full pipeline: stage not stated [Python]

### Three-color single-molecule imaging reveals conformational dynamics of dynein undergoing motility. (PNAS 2021)

- DOI: 10.1073/pnas.2101391118 | PMCID: PMC8346880 | PMID: 34326255
- Evidence: Afterward the data were plotted using a custom Python script as previously described ( 35 ).
- Full pipeline: visualisation [Python] -> stage not stated [ImageJ]

### Non-Markovian modeling of protein folding. (PNAS 2021)

- DOI: 10.1073/pnas.2023856118 | PMCID: PMC8346879 | PMID: 34326249
- Evidence: Our Python scripts for the numerical extraction of the memory kernel, for performing a GLE simulation, and computing MFPTs can be found in GitHub ( https://github.com/lucastepper/memtools ).
- Full pipeline: simulation/modelling [GROMACS, Python]

### How multisensory neurons solve causal inference. (PNAS 2021)

- DOI: 10.1073/pnas.2106235118 | PMCID: PMC8364184 | PMID: 34349023
- Version used: **3.6.4**
- Evidence: All the networks described in the study were implemented in Python version 3.6.4 ( https://python.org ) using TensorFlow ( http://www.tensorflow.org ), a library for efficient optimization of mathematical expressions.
- Full pipeline: stage not stated [Psychtoolbox v3.0.11, Python v3.6.4, TensorFlow]

### Microbiome signatures of progression toward celiac disease onset in at-risk children in a longitudinal prospective cohort study. (PNAS 2021)

- DOI: 10.1073/pnas.2020322118 | PMCID: PMC8307711 | PMID: 34253606
- Evidence: Analyses of microbial species, strains, and pathways were performed in Python (using scipy.stats.mannwhitneyu and scipy.stats.wilcoxon functions), and those for metabolites were performed in R [using the Ttest.Anal function of the MetaboAnalyst 4.0 ( 100 ) using parameters nonpar = TRUE and paired = FALSE for the cross-sectional analysis and paired = TRUE for the longitudinal analysis].
- Full pipeline: quality control [MultiQC] -> read trimming [MultiQC] -> stage not stated [Python, SciPy]

### Structural basis for ligand binding modes of CTP synthase. (PNAS 2021)

- DOI: 10.1073/pnas.2026621118 | PMCID: PMC8325340 | PMID: 34301892
- Evidence: The tetramer models were subsequently real-space refined in Python-based hierarchical environment for integrated xtallography (Phenix) software ( 40 ).
- Full pipeline: structure determination [PHENIX, Python]

### Statistical analysis of ENDOR spectra. (PNAS 2021)

- DOI: 10.1073/pnas.2023615118 | PMCID: PMC8271618 | PMID: 34215694
- Evidence: An algorithm for carrying out the estimation given the complex data matrix Y has been implemented in Python.
- Full pipeline: stage not stated [Python]

### The circadian clock gates <i>Drosophila</i> adult emergence by controlling the timecourse of metamorphosis. (PNAS 2021)

- DOI: 10.1073/pnas.2023249118 | PMCID: PMC8271606 | PMID: 34183412
- Evidence: Analysis software was written in Python and Java.
- Full pipeline: stage not stated [Python]

### Active dendrites enable strong but sparse inputs to determine orientation selectivity. (PNAS 2021)

- DOI: 10.1073/pnas.2017339118 | PMCID: PMC8325157 | PMID: 34301882
- Version used: **2.7**
- Evidence: All simulations were performed using NEURON [version 7.4 ( 102 )] and Python (version 2.7/IPython version 5.1).
- Full pipeline: simulation/modelling [Jupyter v5.1, Python v2.7]

### Testing the effects of Facebook usage in an ethnically polarized setting. (PNAS 2021)

- DOI: 10.1073/pnas.2022819118 | PMCID: PMC8237683 | PMID: 34131075
- Evidence: The deactivation was monitored via a Python script that automatically checked Facebook URLs twice a day and sent a report to researchers with the IDs of participants who remained active.
- Full pipeline: stage not stated [Python]

### A modular computational framework for medical digital twins. (PNAS 2021)

- DOI: 10.1073/pnas.2024287118 | PMCID: PMC8157963 | PMID: 33972437
- Evidence: The most important current limitation of the platform we have developed at this time is the fact that all component models in the modules have to be written in Python.
- Full pipeline: stage not stated [Docker, NumPy, Python, SciPy]

### Automated, multiparametric monitoring of respiratory biomarkers and vital signs in clinical and home settings for COVID-19 patients. (PNAS 2021)

- DOI: 10.1073/pnas.2026610118 | PMCID: PMC8126790 | PMID: 33893178
- Version used: **3.0**
- Evidence: All analysis used Python 3.0 with SciPy, PyWavelets, and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### Nonparametric coalescent inference of mutation spectrum history and demography. (PNAS 2021)

- DOI: 10.1073/pnas.2013798118 | PMCID: PMC8166128 | PMID: 34016747
- Evidence: The mushi software is available as a Python 3 package in ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> stage not stated [BCFtools, Jupyter, Nextflow, Python]

### Declining greenness in Arctic-boreal lakes. (PNAS 2021)

- DOI: 10.1073/pnas.2021219118 | PMCID: PMC8053985 | PMID: 33876758
- Evidence: Satellite remote sensing analyses were performed in Google Earth Engine ( 125 ); statistics were calculated in Python ( 126 ) using a suite of packages and spatial joins were conducted in QGIS ( 127 ).
- Full pipeline: differential/statistical testing [Python, QGIS] -> stage not stated [SciPy]

### Transferrin receptor targeting by de novo sheet extension. (PNAS 2021)

- DOI: 10.1073/pnas.2021569118 | PMCID: PMC8092486 | PMID: 33879614
- Evidence: For steady-state fits, in each design, seven Req values were fitted with a custom Python script to a saturation binding curve to obtain B max and the equilibrium dissociation constant K D .
- Full pipeline: structure determination [PHENIX] -> stage not stated [Python]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Version used: **3.7**
- Evidence: All plots were generated using Matplotlib ( 58 ), Seaborn ( https://seaborn.pydata.org ) adjustText ( https://github.com/Phlya/adjustText ), mpl-scatter-density ( https://github.com/astrofrog/mpl-scatter-density ), Astropy ( 59 , 60 ), and Scanpy ( 50 ) libraries under Python 3.7.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Exposure density and neighborhood disparities in COVID-19 infection risk. (PNAS 2021)

- DOI: 10.1073/pnas.2021258118 | PMCID: PMC8020638 | PMID: 33727410
- Evidence: The rasterization process was implemented in Python and deployed on NYU Center for Urban Science and Progress’ (CUSP’s) Research Computing Facility (RCF), and the activity computation was performed with PySpark on a Hadoop distributed computing cluster using NYU’s High Performance Computing platform.
- Full pipeline: dimensionality reduction/clustering [Python]

### Genomic analysis of the brassica pathogen turnip mosaic potyvirus reveals its spread along the former trade routes of the Silk Road. (PNAS 2021)

- DOI: 10.1073/pnas.2021221118 | PMCID: PMC8000540 | PMID: 33741737
- Evidence: We used a Python script to analyze the inferred load and direction of migration through time (available at https://github.com/admiralenola/globall4scripts ).
- Full pipeline: stage not stated [Python]

### Immunoediting role for major vault protein in apoptotic signaling induced by bacterial <i>N</i>-acyl homoserine lactones. (PNAS 2021)

- DOI: 10.1073/pnas.2012529118 | PMCID: PMC8000436 | PMID: 33723037
- Evidence: Data analysis was performed as detailed above, and then the labeled peptides were identified using a custom Python script, which searched for heavy and light labeled peptides of a similar intensity (at least 80% similarity) within 2-min retention time windows.
- Full pipeline: visualisation [PyMOL] -> stage not stated [Python]

### Tissue folding at the organ-meristem boundary results in nuclear compression and chromatin compaction. (PNAS 2021)

- DOI: 10.1073/pnas.2017859118 | PMCID: PMC7923354 | PMID: 33608459
- Evidence: All scripts have been developed in Python ( https://python.org ) and MATLAB (MathWorks Inc.), and the protocol is dependent on the MorphoGraphX [ https://www.mpipz.mpg.de/MorphoGraphX ( 16 )] and MARS/ALT ( 50 ) software.
- Full pipeline: stage not stated [ImageJ, Python]

### Chemokine-biased robust self-organizing polarization of migrating cells in vivo. (PNAS 2021)

- DOI: 10.1073/pnas.2018480118 | PMCID: PMC7896345 | PMID: 33574063
- Evidence: The angles were plotted into a rose plot generated in Python.
- Full pipeline: visualisation [Python]

### Climate control on terrestrial biospheric carbon turnover. (PNAS 2021)

- DOI: 10.1073/pnas.2011585118 | PMCID: PMC7923348 | PMID: 33593902
- Version used: **3.5**
- Evidence: Regression analyses were performed using the Numpy and Scipy packages in Python version 3.5; all analysis code is provided in Dataset S1 .
- Full pipeline: differential/statistical testing [NumPy, Python v3.5, SciPy]

### Pattern formation and polarity sorting of driven actin filaments on lipid membranes. (PNAS 2021)

- DOI: 10.1073/pnas.2017047118 | PMCID: PMC8017684 | PMID: 33536338
- Evidence: To compute the local curvature, a spline fit with a two-pixel interval is performed to the selected line and the best fitting radius is computed by a Python script, considering at each point the five closest points for the fit.
- Full pipeline: stage not stated [Python]

### Structure and assembly of the diiron cofactor in the heme-oxygenase-like domain of the <i>N</i>-nitrosourea-producing enzyme SznF. (PNAS 2021)

- DOI: 10.1073/pnas.2015931118 | PMCID: PMC7848743 | PMID: 33468680
- Evidence: Using length filters and a custom Python script, this pool was analyzed for conservation of the HDO core helix diiron ligands ( SI Appendix , Fig.
- Full pipeline: stage not stated [Python]

### Computational chromatography: A machine learning strategy for demixing individual chemical components in complex mixtures. (PNAS 2022)

- DOI: 10.1073/pnas.2211406119 | PMCID: PMC9907149 | PMID: 36534806
- Version used: **3.7**
- Evidence: All code written by us is in Python 3.7.
- Full pipeline: stage not stated [Python v3.7]

### Microtubule nucleation complex behavior is critical for cortical array homogeneity <i>and</i> xylem wall patterning. (PNAS 2022)

- DOI: 10.1073/pnas.2203900119 | PMCID: PMC9897462 | PMID: 36475944
- Evidence: CorticalSimple ( 55 ) is written in Python and can be downloaded from git.wur.nl/Biometris/articles/corticalsimple .
- Full pipeline: stage not stated [Python]

### Type IV pili trigger episymbiotic association of Saccharibacteria with its bacterial host. (PNAS 2022)

- DOI: 10.1073/pnas.2215990119 | PMCID: PMC9894109 | PMID: 36454763
- Evidence: A Python script was used to separate amplicon sequences that contained both the TM7 primer and universal primer fragments.
- Full pipeline: read trimming [fastp v0.20.0] -> stage not stated [ImageJ, Python, QIIME 2]

### Transcriptome-based molecular subtypes and differentiation hierarchies improve the classification framework of acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2211429119 | PMCID: PMC9894241 | PMID: 36442087
- Evidence: Autogluon (v0.2.0) ( https://github.com/awslabs/autogluon ) in Python was applied in the training and assessment of predictive models of GEP-defined subgroups.
- Full pipeline: alignment/mapping [kallisto v0.46.2] -> quantification [DESeq2 v1.28.0] -> normalisation [DESeq2 v1.28.0] -> dimensionality reduction/clustering [ComplexHeatmap] -> machine learning [Python]

### A proteome-wide map of chaperone-assisted protein refolding in a cytosol-like milieu. (PNAS 2022)

- DOI: 10.1073/pnas.2210536119 | PMCID: PMC9860312 | PMID: 36417429
- Evidence: Standard proteomics mass spec sample preparation followed, and data were analyzed with custom scripts built in Python.
- Full pipeline: stage not stated [AlphaFold, Python]

### Prospective and retrospective values integrated in frontal cortex drive predictive choice. (PNAS 2022)

- DOI: 10.1073/pnas.2206067119 | PMCID: PMC9889848 | PMID: 36417435
- Version used: **3.6**
- Evidence: Data analysis was performed in MATLAB (MathWorks) and Python 3.6.
- Full pipeline: stage not stated [ImageJ, Python v3.6]

### Transposable elements drive intron gain in diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2209766119 | PMCID: PMC9860276 | PMID: 36417430
- Evidence: We then used custom Python scripts to identify, for each intron, the number of splicing events that used the annotated splice junctions, as well as the number of splicing events that used non-canonical junctions within 50 nucleotides on either side of the annotated junction.
- Full pipeline: alignment/mapping [MAFFT, SAMtools] -> differential/statistical testing [R, lme4] -> stage not stated [Python, RepeatMasker, phytools]

### Neuronally produced betaine acts via a ligand-gated ion channel to control behavioral states. (PNAS 2022)

- DOI: 10.1073/pnas.2201783119 | PMCID: PMC9860315 | PMID: 36413500
- Evidence: Python scripts for TEVC analysis and tracking analysis are deposited on GitHub at hiris25/TEVC-analysis-scripts and hiris25/Tierpsy-Tracking-Analysis, respectively.
- Full pipeline: stage not stated [Python]

### Dynamics of plosive consonants via imaging, computations, and soft electronics. (PNAS 2022)

- DOI: 10.1073/pnas.2214164119 | PMCID: PMC9674252 | PMID: 36343234
- Version used: **3.0**
- Evidence: All analyses used Python 3.0 with SciPy and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### A tool for monitoring cell type-specific focused ultrasound neuromodulation and control of chronic epilepsy. (PNAS 2022)

- DOI: 10.1073/pnas.2206828119 | PMCID: PMC9674244 | PMID: 36343238
- Evidence: Epileptiform events were quantified offline in Python by band pass filtering data according to spike dynamics and locating peaks in the absolute signal (Scipy).
- Full pipeline: alignment/mapping [SPM] -> quantification [Python, SciPy] -> differential/statistical testing [NumPy, SPM]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: A Python script (prepDE.py) was used to extract read count information from the files generated by StringTie.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Adult neurogenesis acts as a neural regularizer. (PNAS 2022)

- DOI: 10.1073/pnas.2206704119 | PMCID: PMC9659416 | PMID: 36322739
- Version used: **3.6**
- Evidence: Models were built and analyzed in Python 3.6 ( 65 ) with custom scripts that are freely available on GitHub, and were developed using the following packages: PyTorch ( 66 ), Ax ( https://github.com/facebook/Ax ), NumPy ( 67 ), SciPy ( 68 ), Pandas ( 69 ), Matplotlib ( 70 ), Seaborn ( 71 ), and Scikit-learn 0.21.1 ( 72 ).
- Full pipeline: stage not stated [Matplotlib, NumPy, PyTorch, Python v3.6, SciPy, scikit-learn v0.21.1, seaborn]

### Genetic algorithms reveal profound individual differences in emotion recognition. (PNAS 2022)

- DOI: 10.1073/pnas.2201380119 | PMCID: PMC9659399 | PMID: 36322724
- Version used: **3.8.5**
- Evidence: An analysis of GA expressions was run via custom code written in Python 3.8.5.
- Full pipeline: stage not stated [Python v3.8.5]

### Police agencies on Facebook overreport on Black suspects. (PNAS 2022)

- DOI: 10.1073/pnas.2203089119 | PMCID: PMC9661189 | PMID: 36322743
- Version used: **0.9.0**
- Evidence: We relied on the darts package in Python, v0.9.0 ( https://github.com/unit8co/darts ) to train the model.
- Full pipeline: stage not stated [Python v0.9.0]

### Charting C-C coupling pathways in electrochemical CO<sub>2</sub> reduction on Cu(111) using embedded correlated wavefunction theory. (PNAS 2022)

- DOI: 10.1073/pnas.2202931119 | PMCID: PMC9636923 | PMID: 36306330
- Evidence: The embedding subroutine (extpot.F) that is not packaged with the standard VASP code and associated Python scripts, and the standalone embedding integral generator code used to transform the embedding potential from a Cartesian grid to atomic orbital (GTO) bases, are available via GitHub: https://github.com/EACcodes/VASPEmbedding ( 90 ) and https://github.com/EACcodes/EmbeddingIntegralGenerator ( ...
- Full pipeline: stage not stated [Python]

### Recurrent Hippocampo-neocortical sleep-state divergence in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2123427119 | PMCID: PMC9636919 | PMID: 36279474
- Evidence: Amount of time spent in each state was averaged across subjects and compared between the hippocampus and cortex using a two-tailed paired t test function from the Pingouin Python toolbox.
- Full pipeline: stage not stated [Python]

### Neuronal signature of spatial decision-making during navigation by freely moving rats by using calcium imaging. (PNAS 2022)

- DOI: 10.1073/pnas.2212152119 | PMCID: PMC9636941 | PMID: 36279456
- Evidence: Spatial tuning was inferred using custom Python scripts.
- Full pipeline: machine learning [CaImAn] -> stage not stated [Fiji v2.1, ImageJ v2.1, Python]

### Mammalian octopus cells are direction selective to frequency sweeps by excitatory synaptic sequence detection. (PNAS 2022)

- DOI: 10.1073/pnas.2203748119 | PMCID: PMC9636937 | PMID: 36279465
- Evidence: The model was run in the NEURON 8.0 environment in Python ( https://www.neuron.yale.edu/neuron/ ) ( 80 ), with the default parameters (RM03, II-o) from Manis and Campagnola ( 21 ); i.e., it contains HCN, KL, KH (high-voltage activated potassium channels), leak, and voltage-gated sodium channels (jsrna in the model).
- Full pipeline: stage not stated [Python]

### Controlling inversion disorder in a stoichiometric spinel magnet. (PNAS 2022)

- DOI: 10.1073/pnas.2208748119 | PMCID: PMC9618041 | PMID: 36256823
- Evidence: Collected neutron-scattering events in the 240 exposures were used to construct a three-dimensional dataset in the coordinates of reciprocal space, using Python scripts locally developed at CORELLI, together with the Mantid program for visualization ( 37 ).
- Full pipeline: dimensionality reduction/clustering [Python] -> visualisation [Python]

### Pan-mitogenomics reveals the genetic basis of cytonuclear conflicts in citrus hybridization, domestication, and diversification. (PNAS 2022)

- DOI: 10.1073/pnas.2206076119 | PMCID: PMC9618123 | PMID: 36260744
- Evidence: The statistics of divergence ( D xy ), differentiation ( F st ), and genetic diversity (π) were calculated based on the nuclear variation map and the mitochondrial variation map as recommended by Python scripts in genomics_general ( https://github.com/simonhmartin/genomics_general ) ( 67 ).
- Full pipeline: dimensionality reduction/clustering [PLINK v1.90b, R] -> differential/statistical testing [Python, ggplot2] -> visualisation [PLINK v1.90b, R, ggplot2] -> stage not stated [GEMMA v0.98.5, IQ-TREE v2.0, SnpEff v5.1]

### Dynamic processing of hunger and thirst by common mesolimbic neural ensembles. (PNAS 2022)

- DOI: 10.1073/pnas.2211688119 | PMCID: PMC9618039 | PMID: 36252036
- Evidence: For two-photon imaging experiments, behavioral data, and imaging data were analyzed using the Suite2p pipeline ( 38 ) and custom Python scripts.
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [Python, Suite2p]

### Transmembrane proteins tetraspanin 4 and CD9 sense membrane curvature. (PNAS 2022)

- DOI: 10.1073/pnas.2208993119 | PMCID: PMC9618112 | PMID: 36252000
- Evidence: All data analysis was performed with custom-written Python scripts.
- Full pipeline: stage not stated [Python]

### Multiple forms of working memory emerge from synapse-astrocyte interactions in a neuron-glia network model. (PNAS 2022)

- DOI: 10.1073/pnas.2207912119 | PMCID: PMC9618090 | PMID: 36256810
- Evidence: Simulations and mean field analysis used custom code implemented in C/C + + , Python 3+, and the Python-based Brian 2 simulator ( 59 ).
- Full pipeline: simulation/modelling [Brian2, Python]

### Sharp turns and gyrotaxis modulate surface accumulation of microorganisms. (PNAS 2022)

- DOI: 10.1073/pnas.2206738119 | PMCID: PMC9586295 | PMID: 36219692
- Version used: **3.0**
- Evidence: The Python program (Python 3.0) together with an open source library (NumPy; https://numpy.org/ ) was used to compute the variation of V s , ω , D r , and PDF ( P ) with y (or z ) and orientation ϕ (or θ ) in the horizontal (or vertical) plane.
- Full pipeline: simulation/modelling [ImageJ, TrackMate] -> stage not stated [NumPy, Python v3.0]

### Adaptive processing and perceptual learning in visual cortical areas V1 and V4. (PNAS 2022)

- DOI: 10.1073/pnas.2213080119 | PMCID: PMC9586333 | PMID: 36223395
- Evidence: Another system for stimulus generation involved custom written software in Python Core Team, on an Asus Rog Swift monitor at a resolution of 2,560 × 1,440 pixels and a refresh rate of 105 Hz.
- Full pipeline: stage not stated [Python]

### Mind blanking is a distinct mental state linked to a recurrent brain profile of globally positive connectivity during ongoing mentation. (PNAS 2022)

- DOI: 10.1073/pnas.2200511119 | PMCID: PMC9564098 | PMID: 36194631
- Evidence: Analyses were performed with locally developed codes in Python and R.
- Full pipeline: alignment/mapping [AFNI, FSL v6.0, Nipype, SPM] -> differential/statistical testing [AFNI, FSL v6.0, Nipype, SPM] -> machine learning [scikit-learn] -> stage not stated [Python]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: We used a custom Python script to parse barcodes and split reads into individual fastq files for each cell, allowing up to one mismatch.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Data-driven emergence of convolutional structure in neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2201854119 | PMCID: PMC9546588 | PMID: 36161906
- Evidence: For moderate input size D , we use the Tensorly package in Python ( 102 ).
- Full pipeline: stage not stated [Python]

### Brain dysfunction during warming is linked to oxygen limitation in larval zebrafish. (PNAS 2022)

- DOI: 10.1073/pnas.2207052119 | PMCID: PMC9522358 | PMID: 36122217
- Evidence: Images were collected at 5 Hz via a custom-written Python script using the Pymba wrapper for interfacing with the camera (Mako G319B, Allied Vision).
- Full pipeline: stage not stated [Python, lme4]

### A scalable framework for the discovery of functional helicase substrates and helicase-driven regulatory switches. (PNAS 2022)

- DOI: 10.1073/pnas.2209608119 | PMCID: PMC9499579 | PMID: 36095194
- Evidence: Bioinformatics analyses were performed with in-house Python scripts and software tools from the Galaxy server ( 45 ).
- Full pipeline: quality control [Cutadapt v1.15, FastQC v0.11.5] -> read trimming [Cutadapt v1.15, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [Galaxy, MACS2, Python]

### Gull dynamic pitch stability is controlled by wing morphing. (PNAS 2022)

- DOI: 10.1073/pnas.2204847119 | PMCID: PMC9477410 | PMID: 36067296
- Evidence: To quantify the free response of the system, we solved for the eigenvalues and eigenvectors of A at all trimmed configurations using a custom Python script.
- Full pipeline: read trimming [Python] -> quantification [Python]

### Coordination of gene expression with cell size enables <i>Escherichia coli</i> to efficiently maintain motility across conditions. (PNAS 2022)

- DOI: 10.1073/pnas.2110342119 | PMCID: PMC9478672 | PMID: 36067284
- Evidence: A custom-made Python script was then used to obtain cell trajectories and swimming characteristics.
- Full pipeline: simulation/modelling [Python]

### Rapid timescale for an oxic transition during the Great Oxidation Event and the instability of low atmospheric O<sub>2</sub>. (PNAS 2022)

- DOI: 10.1073/pnas.2205618119 | PMCID: PMC9477391 | PMID: 36067299
- Evidence: The version of the code (v0.2.14) used in this paper and the corresponding Python scripts to reproduce work done in this article are at https://zenodo.org/record/6824092 .
- Full pipeline: stage not stated [Python]

### Adaptive exchange sustains cullin-RING ubiquitin ligase networks and proper licensing of DNA replication. (PNAS 2022)

- DOI: 10.1073/pnas.2205608119 | PMCID: PMC9456757 | PMID: 36037385
- Version used: **2.7**
- Evidence: All additional CRISPR screen data analyses were performed in Python 2.7 using a combination of Numpy (v1.12.1), Pandas (v0.17.1), and Scipy (v0.17.0).
- Full pipeline: stage not stated [NumPy v1.12.1, Python v2.7, SciPy v0.17.0]

### Mapping the per-residue surface electrostatic potential of CAPRIN1 along its phase-separation trajectory. (PNAS 2022)

- DOI: 10.1073/pnas.2210492119 | PMCID: PMC9457416 | PMID: 36040869
- Version used: **3.7**
- Evidence: Exponential curve fits were performed by using in-house-written programs (Python 3.7), exploiting the Levenberg–Marquardt algorithm of the Lmfit python software package ( https://lmfit.github.io/lmfit-py/ ).
- Full pipeline: stage not stated [Python v3.7]

### Taxonomic classification of DNA sequences beyond sequence similarity using deep neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2122636119 | PMCID: PMC9436379 | PMID: 36018838
- Version used: **3.7**
- Evidence: BERTax was implemented in Python 3.7 and uses the Python packages scipy (1.6.1) ( 40 ), keras (2.4.3), tensorflow (2.4.1) ( 41 ), numpy (1.19.2) ( 42 ), and keras-bert (0.86.0).
- Full pipeline: stage not stated [Kraken2, NumPy v1.19.2, Python v3.7, SciPy v1.6.1, minimap2]

### Fine-scaled climate variation in equatorial Africa revealed by modern and fossil primate teeth. (PNAS 2022)

- DOI: 10.1073/pnas.2123366119 | PMCID: PMC9440354 | PMID: 35994633
- Version used: **3.1**
- Evidence: Paired δ 18 O measurements and day of formation estimates were provided to the Lomb–Scargle periodogram algorithm hosted by the AstroPy 4.0.1 library run with Python 3.1.
- Full pipeline: simulation/modelling [CESM] -> stage not stated [Python v3.1]

### Optimizing the human learnability of abstract network representations. (PNAS 2022)

- DOI: 10.1073/pnas.2121338119 | PMCID: PMC9436382 | PMID: 35994661
- Evidence: Network symmetries were computed by using the iGraph package in Python ( 52 ).
- Full pipeline: stage not stated [Python, SciPy]

### In vitro reconstitution of calcium-dependent recruitment of the human ESCRT machinery in lysosomal membrane repair. (PNAS 2022)

- DOI: 10.1073/pnas.2205590119 | PMCID: PMC9436306 | PMID: 35994655
- Evidence: Custom-made scripts were used to perform puncta recognition analysis in Python.
- Full pipeline: stage not stated [ImageJ, OpenCV, Python, scikit-image]

### A photo-switchable assay system for dendrite degeneration and repair in &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2204577119 | PMCID: PMC9407391 | PMID: 35969739
- Evidence: The code used for deep learning–based automatic dendrite structure prediction is written in Python/TensorFlow.
- Full pipeline: machine learning [Python, TensorFlow]

### Repertoire-scale measures of antigen binding. (PNAS 2022)

- DOI: 10.1073/pnas.2203505119 | PMCID: PMC9407674 | PMID: 35969768
- Version used: **3.7.6**
- Evidence: Recon v3.0 was performed using Python 3.7.6 with NumPy version 1.18.0 and SciPy version 1.4.1.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [NumPy v1.18.0, PyMOL v2.2, Python v3.7.6, SciPy v1.4.1]

### Distinct neural networks derived from galanin-containing nociceptors and neurotensin-expressing pruriceptors. (PNAS 2022)

- DOI: 10.1073/pnas.2118501119 | PMCID: PMC9388111 | PMID: 35943985
- Evidence: Python scripts written by ourselves for determination of cell number in each nucleus are available in https://github.com/chenyan-sh/neuronCounting ( 64 ).
- Full pipeline: stage not stated [Python]

### Revisiting [Formula: see text]-wavelet compressed-sensing MRI in the era of deep learning. (PNAS 2022)

- DOI: 10.1073/pnas.2201062119 | PMCID: PMC9388129 | PMID: 35939712
- Evidence: Supervised training was performed with a normalized ℓ 1 - ℓ 2 loss in k space ( 3 , 7 ), using TensorFlow in Python.
- Full pipeline: normalisation [Python, TensorFlow] -> machine learning [Python, TensorFlow]

### A neural network solves, explains, and generates university math problems by program synthesis and few-shot learning at human level. (PNAS 2022)

- DOI: 10.1073/pnas.2123433119 | PMCID: PMC9371704 | PMID: 35917350
- Evidence: We add the text “write a program” before the question and focus on the Python programming language by placing the text within Pythonic triple quotes like a docstring.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Matplotlib, NumPy, Python, SciPy]

### Random encounters and amoeba locomotion drive the predation of &lt;i&gt;Listeria monocytogenes&lt;/i&gt; by &lt;i&gt;Acanthamoeba castellanii&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122659119 | PMCID: PMC9371647 | PMID: 35914149
- Evidence: Image processing and analysis were performed using ImageJ (NIH) and in-house Python scripts ( SI Appendix , Python Scripts ).
- Full pipeline: stage not stated [ImageJ, OpenCV, Python, SciPy]

### Archaeal lipids trace ecology and evolution of marine ammonia-oxidizing archaea. (PNAS 2022)

- DOI: 10.1073/pnas.2123193119 | PMCID: PMC9351445 | PMID: 35905325
- Evidence: Seawater density calculations, statistical analysis, and seawater density (sigma-T or σ T ) were performed in Python using the Xarray package ( 101 ).
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> differential/statistical testing [Jupyter, Python, SciPy, scikit-learn] -> visualisation [Jupyter]

### Deep neural networks constrained by neural mass models improve electrophysiological source imaging of spatiotemporal brain dynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2201128119 | PMCID: PMC9351497 | PMID: 35881787
- Version used: **0.22.0**
- Evidence: The data analysis results for sLORETA and unit–noise–gain minimum variance Beamformer were calculated using MNE-Python (version 0.22.0) ( 41 ); CMEM was calculated using the BrainEntropy plug-in (version 2.7.3) in Brainstorm, and FAST-IRES was calculated using the published code. * Otsu’s ( 74 ) method was used to find the extent of the imaging solution when calculating the precision and recall fo...
- Full pipeline: machine learning [PyTorch] -> stage not stated [FreeSurfer, MNE-Python v0.22.0, Python v0.22.0]

### Ciliogenesis requires sphingolipid-dependent membrane and axoneme interaction. (PNAS 2022)

- DOI: 10.1073/pnas.2201096119 | PMCID: PMC9351462 | PMID: 35895683
- Evidence: All statistical analyses were carried out using custom-written Python scripts and the R statistical language.
- Full pipeline: quality control [Bowtie2] -> alignment/mapping [Bowtie2, IMOD] -> dimensionality reduction/clustering [seaborn] -> differential/statistical testing [Bioconductor, Python, edgeR] -> visualisation [seaborn] -> stage not stated [ImageJ, MotionCor2]

### Plant genetic effects on microbial hubs impact host fitness in repeated field trials. (PNAS 2022)

- DOI: 10.1073/pnas.2201285119 | PMCID: PMC9335298 | PMID: 35867817
- Evidence: The images were processed using a custom script employing cv2 in Python ( 70 ), which quantified plant surface area in each well by scaling based on the wells’ size, converting images into binary images, and measuring nonwhite pixels within each well (i.e., plant surface area).
- Full pipeline: read trimming [Cutadapt] -> quantification [Python] -> normalisation [Python] -> stage not stated [Prokka, R, SPAdes, igraph, lme4]

### Motor learning without movement. (PNAS 2022)

- DOI: 10.1073/pnas.2204379119 | PMCID: PMC9335319 | PMID: 35858450
- Version used: **3.8.5**
- Evidence: Data were processed in Python 3.8.5 and MATLAB 2018a.
- Full pipeline: differential/statistical testing [R v4.0.3, emmeans, ggplot2, ggpubr, lme4] -> stage not stated [Python v3.8.5]

### Propagation of societal gender inequality by internet search algorithms. (PNAS 2022)

- DOI: 10.1073/pnas.2204529119 | PMCID: PMC9304000 | PMID: 35858360
- Evidence: The data-analysis code (in Python) can be accessed as a Jupyter notebook on GitHub .
- Full pipeline: stage not stated [Jupyter, Python]

### Mass spectrometry imaging to explore molecular heterogeneity in cell culture. (PNAS 2022)

- DOI: 10.1073/pnas.2114365119 | PMCID: PMC9303856 | PMID: 35858333
- Evidence: 2021a Pro, SCiLS Lab/Bruker Daltonics) was used to generate ion images with a reduced-mass list of the most prominent peaks in the csv or imzML format ( 59 ) for further processing in Python.
- Full pipeline: normalisation [scikit-learn v0.21.3] -> dimensionality reduction/clustering [SciPy] -> stage not stated [Python, scikit-image v0.14.0]

### Self-consistent dispersal puts tight constraints on the spatiotemporal organization of species-rich metacommunities. (PNAS 2022)

- DOI: 10.1073/pnas.2200390119 | PMCID: PMC9245702 | PMID: 35727977
- Evidence: All calculations were performed in Python ( 103 ), and the results were evaluated using Mathematica ( 104 ) (the Python code developed for this study is available at https://github.com/Hallatscheklab/Self-Consistent-Metapopulations ).
- Full pipeline: stage not stated [Python]

### Host protease activity classifies pneumonia etiology. (PNAS 2022)

- DOI: 10.1073/pnas.2121778119 | PMCID: PMC9231472 | PMID: 35696579
- Evidence: For disease classification based on urinary ABN signatures, randomly assigned sets of paired data samples consisting of features (i.e., standardized scores of peak area ratio of individual urinary reporters measured by LC-MS/MS) and labels (i.e., bacterial or viral) were used to train linear SVM classifiers implemented in Python 3.
- Full pipeline: dimensionality reduction/clustering [R] -> machine learning [Python] -> stage not stated [QuPath]

### Chemotactic self-caging in active emulsions. (PNAS 2022)

- DOI: 10.1073/pnas.2122269119 | PMCID: PMC9214524 | PMID: 35679341
- Evidence: We further used Python scripts to mine trajectory data for droplet–trail interactions.
- Full pipeline: simulation/modelling [Python]

### Alternative splicing encodes functional intracellular CD59 isoforms that mediate insulin secretion and are down-regulated in diabetic islets. (PNAS 2022)

- DOI: 10.1073/pnas.2120083119 | PMCID: PMC9214515 | PMID: 35666870
- Evidence: In all cases, PDB files were manipulated with Python scripts available in PDB-Tools ( 15 ) and with MayaChemTools Perl scripts ( 16 ).
- Full pipeline: stage not stated [Python]

### Responsive robotic prey reveal how predators adapt to predictability in escape tactics. (PNAS 2022)

- DOI: 10.1073/pnas.2117858119 | PMCID: PMC9191677 | PMID: 35658072
- Version used: **3.6.9**
- Evidence: Prey coordinates were extracted manually from each frame using a custom-built program written in Python (version 3.6.9).
- Full pipeline: stage not stated [Python v3.6.9, R v3.5.1]

### Structural and mechanistic basis of σ-dependent transcriptional pausing. (PNAS 2022)

- DOI: 10.1073/pnas.2201301119 | PMCID: PMC9191641 | PMID: 35653571
- Evidence: ( 65 ), and the resulting data were analyzed using custom Python scripts.
- Full pipeline: stage not stated [Python]

### A feedforward inhibitory premotor circuit for auditory-vocal interactions in zebra finches. (PNAS 2022)

- DOI: 10.1073/pnas.2118448119 | PMCID: PMC9191632 | PMID: 35658073
- Version used: **3.7**
- Evidence: We used Plexon Offline Sorter for spike detection and clustering and MATLAB R2020a and Python 3.7 for data analysis.
- Full pipeline: dimensionality reduction/clustering [Python v3.7] -> simulation/modelling [Brian2 v2.2.2.1]

### Design principles of PI(4,5)P<sub>2</sub> clustering under protein-free conditions: Specific cation effects and calcium-potassium synergy. (PNAS 2022)

- DOI: 10.1073/pnas.2202647119 | PMCID: PMC9295730 | PMID: 35605121
- Evidence: Visualization and analysis of networks were carried out using tailored Python scripts and the Python package NetworkX (version 2.1) ( 53 ).
- Full pipeline: simulation/modelling [R] -> visualisation [NetworkX v2.1, Python]

### Neural representations of others' traits predict social decisions. (PNAS 2022)

- DOI: 10.1073/pnas.2116944119 | PMCID: PMC9295729 | PMID: 35605117
- Evidence: The task was programmed in Python using the Pygame package.
- Full pipeline: dimensionality reduction/clustering [FSL] -> differential/statistical testing [FSL, SPM] -> stage not stated [Python]

### Diffusion MRI-guided theta burst stimulation enhances memory and functional connectivity along the inferior longitudinal fasciculus in mild cognitive impairment. (PNAS 2022)

- DOI: 10.1073/pnas.2113778119 | PMCID: PMC9173759 | PMID: 35594397
- Evidence: Statistical analyses were performed using RStudio (RStudio, Inc.), Python 3, and MATLAB (MathWorks).
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs, CONN toolbox, FSL, FreeSurfer, MRtrix3]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: Python scripts for obtaining guanine and cytosine (GC) content and GC skew were generated.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Determining containment policy impacts on public sentiment during the pandemic using social media data. (PNAS 2022)

- DOI: 10.1073/pnas.2117292119 | PMCID: PMC9171635 | PMID: 35503914
- Evidence: We then computed the daily public sentiment scores from the text using the VADER NLP library in Python, to obtain our main dependent variable (DV), daily average public sentiment.
- Full pipeline: stage not stated [Python]

### Deep brain stimulation in the subthalamic nucleus for Parkinson's disease can restore dynamics of striatal networks. (PNAS 2022)

- DOI: 10.1073/pnas.2120808119 | PMCID: PMC9171607 | PMID: 35500112
- Evidence: The model output was analyzed using Python 3.
- Full pipeline: stage not stated [Python]

### Revisiting the recombinant history of HIV-1 group M with dynamic network community detection. (PNAS 2022)

- DOI: 10.1073/pnas.2108815119 | PMCID: PMC9171507 | PMID: 35500121
- Evidence: We used a Python script to update the MCC tree with recombination events by switching random branches that span a randomly selected time.
- Full pipeline: alignment/mapping [IQ-TREE v1.3.11.1, R] -> structure determination [IQ-TREE v1.3.11.1] -> stage not stated [Python, igraph]

### Small-world connectivity dictates collective endothelial cell signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2118927119 | PMCID: PMC9170162 | PMID: 35482920
- Version used: **2.7**
- Evidence: Ca 2+ imaging recordings were analyzed using custom FIJI macros and custom analysis software written in the Python 2.7 programming language ( 5 , 24 ).
- Full pipeline: stage not stated [NetworkX, Python v2.7]

### Nanoscale engineering of gold particles in 18th century Böttger lusters and glazes. (PNAS 2022)

- DOI: 10.1073/pnas.2120753119 | PMCID: PMC9170166 | PMID: 35446687
- Evidence: While this provided an analytical solution, numerical approximations were necessary to evaluate that solution, and Python scripts such as PyMieScatt ( 37 ) were used to evaluate the extinction, absorption, and scattering efficiencies of nanoparticles both individually and in a size-density distribution.
- Full pipeline: stage not stated [Python]

### Genetic architecture facilitates then constrains adaptation in a host-parasite coevolutionary arms race. (PNAS 2022)

- DOI: 10.1073/pnas.2121752119 | PMCID: PMC9170059 | PMID: 35412865
- Evidence: The sequence data were processed using a combination of custom Python scripts and publicly available software ( 58 , 59 ); current versions of the code are available at https://github.com/BU-RAD-seq/Digital_RADs .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1] -> stage not stated [Python]

### Predicting relative efficiency of amide bond formation using multivariate linear regression. (PNAS 2022)

- DOI: 10.1073/pnas.2118451119 | PMCID: PMC9169781 | PMID: 35412905
- Evidence: All DFT-level molecular descriptors were extracted from Gaussian ( 36 ) output files using an in-house Python script.
- Full pipeline: stage not stated [Python]

### Glycosaminoglycans modulate long-range mechanical communication between cells in collagen networks. (PNAS 2022)

- DOI: 10.1073/pnas.2116718119 | PMCID: PMC9169665 | PMID: 35394874
- Evidence: The reaction forces at the boundary nodes over all surfaces except the top and bottom surfaces were recorded at the expanded state using the Abaqus scripting interface in Python.
- Full pipeline: alignment/mapping [ImageJ] -> stage not stated [Python]

### In situ optical spectroscopy of crystallization: One crystal nucleation at a time. (PNAS 2022)

- DOI: 10.1073/pnas.2122990119 | PMCID: PMC9169808 | PMID: 35394901
- Evidence: The cleaned spectra were analyzed by nonnegative matrix factorization (NMF) using the Scikit_Learn library in Python ( 59 ).
- Full pipeline: simulation/modelling [OpenMM] -> stage not stated [Python]

### Phenotype-Based Threat Assessment. (PNAS 2022)

- DOI: 10.1073/pnas.2112886119 | PMCID: PMC9168455 | PMID: 35363569
- Version used: **3.7**
- Evidence: All ML models were developed with Python 3.7 using the Pandas and Scikit-learn libraries, with all plots visualized using seaborn.
- Full pipeline: visualisation [Python v3.7, scikit-learn, seaborn]

### Structural conservation among variants of the SARS-CoV-2 spike postfusion bundle. (PNAS 2022)

- DOI: 10.1073/pnas.2119467119 | PMCID: PMC9169775 | PMID: 35363556
- Evidence: Since each original scaffolded HR1HR2 particle only contains four copies of a HR1HR2 bundle, the extra eight copies in the tetrahedral symmetry expanded particle set were discarded by a Python script.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [CTFFIND, ChimeraX, Coot, PyMOL, Python, RELION, UCSF Chimera]

### Horizontal transmission enables flexible associations with locally adapted symbiont strains in deep-sea hydrothermal vent symbioses. (PNAS 2022)

- DOI: 10.1073/pnas.2115608119 | PMCID: PMC9168483 | PMID: 35349333
- Evidence: The number of observed nonsynonymous and synonymous polymorphisms was determined with SNP eff ( 102 ), while the number of expected mutations was assessed with a modified Python script from ref.
- Full pipeline: variant calling [GATK] -> quantification [GATK] -> stage not stated [Python, R]

### Protein cost minimization promotes the emergence of coenzyme redundancy. (PNAS 2022)

- DOI: 10.1073/pnas.2110787119 | PMCID: PMC9168515 | PMID: 35344442
- Evidence: To this end, we identified NAD(P) binding orthogroups (KO) using the KEGG REST API and developed a custom Python script to identify sequence of NAD(P)-bound structures from the PDB within each orthogroup.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> stage not stated [Python]

### <i>Drosophila</i> females have an acoustic preference for symmetric males. (PNAS 2022)

- DOI: 10.1073/pnas.2116136119 | PMCID: PMC9060496 | PMID: 35312357
- Evidence: The center position of flies was tracked in the videos using custom routines written in Python.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Python]

### Implicit data crimes: Machine learning bias arising from misuse of public data. (PNAS 2022)

- DOI: 10.1073/pnas.2117203119 | PMCID: PMC9060447 | PMID: 35312366
- Evidence: We implemented the DictL algorithm in Python using our open-source code ( 63 ).
- Full pipeline: stage not stated [PyTorch, Python]

### A tethered ligand assay to probe SARS-CoV-2:ACE2 interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2114397119 | PMCID: PMC9168514 | PMID: 35312342
- Evidence: Equilibrium measurements with MT and rupture experiments with an AFM were evaluated with custom MATLAB and Python scripts to deduce force stability and kinetics.
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [Python, VMD]

### Contiguously hydrophobic sequences are functionally significant throughout the human exome. (PNAS 2022)

- DOI: 10.1073/pnas.2116267119 | PMCID: PMC8944643 | PMID: 35294280
- Version used: **3.6**
- Evidence: All computations were done in Python 3.6 using the numpy ( 70 ), scipy ( 68 ), and pandas ( 71 ) packages.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [Matplotlib, NumPy, Python v3.6, SciPy]

### Minority salience and the overestimation of individuals from minority groups in perception and memory. (PNAS 2022)

- DOI: 10.1073/pnas.2116884119 | PMCID: PMC8944588 | PMID: 35286213
- Evidence: The matrices were generated using a Python 3 script randomly selecting from 330 images from the Chicago Face Database ( 73 ); all pictures were rated by above 90% of the participants in a norms study ( 73 ) as belonging to an Black American or a White American, and all displayed neutral facial expressions.
- Full pipeline: stage not stated [Python]

### A system for multiplexed selection of aptamers with exquisite specificity without counterselection. (PNAS 2022)

- DOI: 10.1073/pnas.2119945119 | PMCID: PMC8944265 | PMID: 35290115
- Evidence: Curve fitting was performed in Python using the “curve_fit” function from the “scipy” library.
- Full pipeline: stage not stated [Python, SciPy]

### Cross-linkers at growing microtubule ends generate forces that drive actin transport. (PNAS 2022)

- DOI: 10.1073/pnas.2112799119 | PMCID: PMC8931237 | PMID: 35271394
- Evidence: Image processing and analysis were performed using plugins for Fiji ( 59 ) or ImageJ and custom-written programs in Python or MATLAB.
- Full pipeline: stage not stated [ImageJ, Python]

### Resolving the subtle details of human DNA alkyltransferase lesion search and repair mechanism by single-molecule studies. (PNAS 2022)

- DOI: 10.1073/pnas.2116218119 | PMCID: PMC8931253 | PMID: 35259021
- Evidence: Coordinates of QD-labeled AGT along the lesion containing DNA as well as the photon counts (integrated over 2 pixels due to downsampling, pixel time of 0.1 ms) were extracted from kymographs using a custom-written kymotracker Python script ( https://harbor.lumicks.com/ ) ( SI Appendix for details).
- Full pipeline: quantification [ImageJ] -> stage not stated [Python]

### ERK signaling dissolves ERF repression condensates in living embryos. (PNAS 2022)

- DOI: 10.1073/pnas.2119187119 | PMCID: PMC8892517 | PMID: 35217620
- Evidence: Further processing was done in Python to fill in the information for frames without droplets as containing 0 droplets of diameter 0.
- Full pipeline: normalisation [Matplotlib] -> visualisation [Matplotlib] -> stage not stated [Python]

### Scaling laws in enzyme function reveal a new kind of biochemical universality. (PNAS 2022)

- DOI: 10.1073/pnas.2106655119 | PMCID: PMC8892295 | PMID: 35217602
- Evidence: Using a text-mining Python script, we retrieved metadata, genome statistics data, and EC lists for samples from the DOE-JGI IMG/M database.
- Full pipeline: differential/statistical testing [Python] -> stage not stated [SciPy]

### CSB-independent, XPC-dependent transcription-coupled repair in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2123163119 | PMCID: PMC8892495 | PMID: 35217627
- Evidence: RPKM for each bin was determined and the average RPKM of bins corresponding to the same relative location was calculated using custom Python scripts and plotted with GraphPad Prism 8 software.
- Full pipeline: quantification [Python] -> visualisation [Python]

### Evolutionarily conserved inhibitory uORFs sensitize &lt;i&gt;Hox&lt;/i&gt; mRNA translation to start codon selection stringency. (PNAS 2022)

- DOI: 10.1073/pnas.2117226119 | PMCID: PMC8892498 | PMID: 35217614
- Evidence: Mapped reads were visualized from WIG files using the Integrative Genome Browser software (v2.8.0), and plots were constructed from BAM files using Python 2.
- Full pipeline: alignment/mapping [Python] -> visualisation [Python]

### Co-condensation of proteins with single- and double-stranded DNA. (PNAS 2022)

- DOI: 10.1073/pnas.2107871119 | PMCID: PMC8915884 | PMID: 35238639
- Evidence: Experimental work flows were controlled using custom Python scripts through the inbuilt Bluelake software.
- Full pipeline: stage not stated [Python]

### Label-free sensing of cells with fluorescence lifetime imaging: The quest for metabolic heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2118241119 | PMCID: PMC8892511 | PMID: 35217616
- Version used: **3.7**
- Evidence: All simulation and data analysis were performed using custom-build Python 3.7 scripts with the use of Numpy, Scipy, Scikit-Learn Matplotlib, Pandas and LmFit modules.
- Full pipeline: simulation/modelling [Matplotlib, NumPy, Python v3.7, SciPy] -> stage not stated [scikit-learn]

### LINEAGE: Label-free identification of endogenous informative single-cell mitochondrial RNA mutation for lineage analysis. (PNAS 2022)

- DOI: 10.1073/pnas.2119767119 | PMCID: PMC8812554 | PMID: 35086932
- Evidence: The total number of reads aligned to per allele on each site of mitochondrial genome were counted using a Python script ( 15 ).
- Full pipeline: alignment/mapping [Python, SAMtools v1.9] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [GSEA, Seurat]

### <i>Mycobacterium tuberculosis</i> DNA repair helicase UvrD1 is activated by redox-dependent dimerization via a 2B domain cysteine. (PNAS 2022)

- DOI: 10.1073/pnas.2114501119 | PMCID: PMC8872793 | PMID: 35173050
- Evidence: Python 3 was installed via Anaconda along with modules such as numpy, scipy, matpotlib, lmfit, emcee, corner, os, and pandas, and then the globalfit model was used to fit the data for unwinding using the n-step unwinding model and translocation using a two-step dissociation model ( 64 ).
- Full pipeline: stage not stated [Conda, NumPy, Python, SciPy, emcee]

### Sharp, localized phase transitions in single neuronal cells. (PNAS 2022)

- DOI: 10.1073/pnas.2117521119 | PMCID: PMC8872731 | PMID: 35165183
- Evidence: The data were further processed with Python scripts where, among others, ratios were calculated without background.
- Full pipeline: stage not stated [Python]

### Topographically organized representation of space and context in the medial prefrontal cortex. (PNAS 2022)

- DOI: 10.1073/pnas.2117300119 | PMCID: PMC8833199 | PMID: 35121665
- Evidence: All analysis (except for initial spike sorting; see above) including statistics were performed in Python (versions 2.7 and 3.7).
- Full pipeline: differential/statistical testing [Python] -> machine learning [scikit-learn]

### High-value decisions are fast and accurate, inconsistent with diminishing value sensitivity. (PNAS 2022)

- DOI: 10.1073/pnas.2101508119 | PMCID: PMC8832986 | PMID: 35105801
- Version used: **3.6.7**
- Evidence: We fitted the choice and RT data in each experiment using the HDDM package ( 85 ) in Python (version 3.6.7).
- Full pipeline: dimensionality reduction/clustering [R v3.6.1] -> differential/statistical testing [R v3.6.1] -> stage not stated [Python v3.6.7]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Version used: **3.6.8**
- Evidence: Differential expression (DE) analyses were conducted using DESeq2 ( 63 ) ( E. nindensis , E. tef , and O. thomaeum ) or edgeR ( 23 ) ( S. stapfianus and S. pyramidalis ), and resulting outputs were processed using Pandas 0.25.0 in Python 3.6.8.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Impact of ADAR-induced editing of minor viral RNA populations on replication and transmission of SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2112663119 | PMCID: PMC8833170 | PMID: 35064076
- Evidence: A custom Python script was used to extract the four regions of interest from all genomes and to determine the percentage of A→G, A→C, and A→T changes per adenosine site at these regions compared to the original Wuhan sequence.
- Full pipeline: differential/statistical testing [ggplot2, tidyverse] -> stage not stated [Python]

### Stochastic microbiome assembly depends on context. (PNAS 2022)

- DOI: 10.1073/pnas.2115877119 | PMCID: PMC8851475 | PMID: 35135881
- Version used: **3.9.7**
- Evidence: Analyses were performed with Python (version 3.9.7) and R (version 4.1.1).
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [Python v3.9.7, R v4.1.1]

### In vitro cell cycle oscillations exhibit a robust and hysteretic response to changes in cytoplasmic density. (PNAS 2022)

- DOI: 10.1073/pnas.2109547119 | PMCID: PMC8832984 | PMID: 35101974
- Version used: **3.7.10**
- Evidence: Fitting was performed in Python 3.7.10 using the logistic regression function from the package scikit-learn 0.22.2.
- Full pipeline: differential/statistical testing [Python v3.7.10, scikit-learn v0.22.2] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [ggplot2]

### Annealing synchronizes the 70<i>S</i> ribosome into a minimum-energy conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2111231119 | PMCID: PMC8872765 | PMID: 35177473
- Evidence: The resulting subregions were adjusted to the same volume among different structures, and the values of the local resolution within the mask were read via our Python script ( https://github.com/soothing35/cryoEM_annealling ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.17.1, RELION v3.0.8] -> stage not stated [CTFFIND, Python, UCSF Chimera v1.16]

### A comprehensive map of genetic relationships among diagnostic categories based on 48.6 million relative pairs from the Danish genealogy. (PNAS 2022)

- DOI: 10.1073/pnas.2118688119 | PMCID: PMC8833149 | PMID: 35131856
- Evidence: Bearing this in mind, we used the networkx module in Python ( 28 ) to explore network connectivity in our data.
- Full pipeline: stage not stated [NetworkX, Python]

### Sector search strategies for odor trail tracking. (PNAS 2022)

- DOI: 10.1073/pnas.2107431118 | PMCID: PMC8740577 | PMID: 34983837
- Evidence: At each casting step, we optimize (using standard black box optimization methods using the SciPy library in Python) for Δ r = r − r ′ > 0 and θ by expanding Eq.
- Full pipeline: stage not stated [Python, SciPy]

### Higher-order effects, continuous species interactions, and trait evolution shape microbial spatial dynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2020956119 | PMCID: PMC8740587 | PMID: 34969851
- Version used: **3.7**
- Evidence: We ran a total of 10.49 million runs of our model with various parameter initializations and performed data analysis with Python 3.7 and the R statistical language.
- Full pipeline: differential/statistical testing [Python v3.7]

### A synergy between mechanosensitive calcium- and membrane-binding mediates tension-sensing by C2-like domains. (PNAS 2022)

- DOI: 10.1073/pnas.2112390119 | PMCID: PMC8740744 | PMID: 34969839
- Version used: **3.7**
- Evidence: Specifically, custom Python 3.7 scripts were written based on the Numpy ( 36 ), Scipy ( 37 ), Scikit-image ( 38 ), Allen Cell Structure Segmenter ( 39 ), Cellpose ( 40 ) and Napari libraries ( 41 ).
- Full pipeline: stage not stated [Cellpose, Conda, NumPy, PyMOL, Python v3.7, SciPy]

### Acquisition of the arginine deiminase system benefits epiparasitic Saccharibacteria and their host bacteria in a mammalian niche environment. (PNAS 2022)

- DOI: 10.1073/pnas.2114909119 | PMCID: PMC8764695 | PMID: 34992141
- Evidence: Windows containing a few genes upstream of the ADS operon(s) were extracted with a custom Python script.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE, RAxML v8.2.11] -> visualisation [MUSCLE] -> stage not stated [Python, eggNOG]

### Narratives imagined in response to instrumental music reveal culture-bounded intersubjectivity. (PNAS 2022)

- DOI: 10.1073/pnas.2110406119 | PMCID: PMC8795501 | PMID: 35064081
- Version used: **3.6.2**
- Evidence: All preprocessing and analyses were done in Python version 3.6.2 (Python Software Foundation, https://www.python.org/ ).
- Full pipeline: stage not stated [Python v3.6.2, scikit-learn]

### Fundamental limitations on efficiently forecasting certain epidemic measures in network models. (PNAS 2022)

- DOI: 10.1073/pnas.2109228119 | PMCID: PMC8794801 | PMID: 35046025
- Evidence: Our experimental results were generated by using simulation software written in Python.
- Full pipeline: simulation/modelling [Python]

### Slow expanders invade by forming dented fronts in microbial colonies. (PNAS 2022)

- DOI: 10.1073/pnas.2108653119 | PMCID: PMC8740590 | PMID: 34983839
- Evidence: We used scikit-image ( 83 ) for image processing in Python.
- Full pipeline: stage not stated [Python, scikit-image]

### Synaptic plasticity at the dentate gyrus granule cell to somatostatin-expressing interneuron synapses supports object location memory. (PNAS 2023)

- DOI: 10.1073/pnas.2312752120 | PMCID: PMC10742375 | PMID: 38091292
- Evidence: Data analysis was performed using StimFit and custom-made scripts in Python.
- Full pipeline: stage not stated [Python]

### Navigating the new normal: Examining coattendance in a hybrid work environment. (PNAS 2023)

- DOI: 10.1073/pnas.2310431120 | PMCID: PMC10743359 | PMID: 38079553
- Evidence: Data, Materials, and Software Availability R and Python scripts used to estimate statistical models and generate figures, regression coefficients including absolute and relative effects and standard errors data have been deposited in Github ( 16 ).
- Full pipeline: differential/statistical testing [Python]

### Structural basis of substrate progression through the bacterial chaperonin cycle. (PNAS 2023)

- DOI: 10.1073/pnas.2308933120 | PMCID: PMC10723157 | PMID: 38064510
- Evidence: Good particles from 2D classification were imported back into Relion using the csparc2star.py Python script ( 51 ).
- Full pipeline: stage not stated [CTFFIND, Python, RELION v3.1]

### Fluid dynamics alters liquid-liquid phase separation in confined aqueous two-phase systems. (PNAS 2023)

- DOI: 10.1073/pnas.2306467120 | PMCID: PMC10710025 | PMID: 38039270
- Evidence: The framework is written in Python but uses compiled libraries for performance, enabling rapid prototyping and model comparisons, as well as efficient high-performance simulations.
- Full pipeline: simulation/modelling [Python]

### In silico evolution of autoinhibitory domains for a PD-L1 antagonist using deep learning models. (PNAS 2023)

- DOI: 10.1073/pnas.2307371120 | PMCID: PMC10710080 | PMID: 38032933
- Version used: **3.8**
- Evidence: The EvoPro pipeline is a genetic algorithm-based protein optimization framework written in Python 3.8 that interfaces with AF2 during the scoring step and ProteinMPNN during the pool refill step.
- Full pipeline: stage not stated [AlphaFold, PyMOL, Python v3.8, RoseTTAFold]

### Generation of de novo miRNAs from template switching during DNA replication. (PNAS 2023)

- DOI: 10.1073/pnas.2310752120 | PMCID: PMC10710096 | PMID: 38019864
- Evidence: Phylogenetic trees were traversed with a Python script using the ete3 library package v.3.1.1 ( 53 ).
- Full pipeline: stage not stated [BEDTools v2.26.0, Matplotlib v3.5.1, Python, R, ggplot2, seaborn v0.11.2]

### Gene expression in the primate orbitofrontal cortex related to anxious temperament. (PNAS 2023)

- DOI: 10.1073/pnas.2305775120 | PMCID: PMC10710052 | PMID: 38011550
- Version used: **2.7**
- Evidence: Alignment was performed using Sequence Alignment for Gene Expression ( https://github.com/tadesouaiaia/sage ) written in Python 2.7.
- Full pipeline: alignment/mapping [Python v2.7] -> stage not stated [CellProfiler v4.2.1, ImageJ v1.53s, QuPath, Scanpy, limma, scDblFinder]

### Sparsity of higher-order landscape interactions enables learning and prediction for microbiomes. (PNAS 2023)

- DOI: 10.1073/pnas.2307313120 | PMCID: PMC10691334 | PMID: 37991947
- Evidence: We used the SPORCO package ( 70 ) in Python to implement BPDN using an alternating direction method of multipliers (ADMM) algorithm ( 71 ).
- Full pipeline: stage not stated [Python, XGBoost, scikit-learn]

### The weekly cycle of photosynthesis in Europe reveals the negative impact of particulate pollution on ecosystem productivity. (PNAS 2023)

- DOI: 10.1073/pnas.2306507120 | PMCID: PMC10710040 | PMID: 37983483
- Evidence: The SEM analysis is carried out using the “semopy” package in Python.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [Python]

### Mapping the configurational landscape and aggregation phase behavior of the tau protein fragment PHF6. (PNAS 2023)

- DOI: 10.1073/pnas.2309995120 | PMCID: PMC10691331 | PMID: 37983502
- Evidence: S18–S22 show plots of the CG potentials, along with AA and CG probability distributions for associated degrees of freedom, and a Python script to tabulate potentials from their parameters is provided as supporting information .
- Full pipeline: simulation/modelling [ChimeraX] -> visualisation [ChimeraX] -> stage not stated [Python]

### High-throughput quantification of red blood cell deformability and oxygen saturation to probe mechanisms of sickle cell disease. (PNAS 2023)

- DOI: 10.1073/pnas.2313755120 | PMCID: PMC10691249 | PMID: 37983504
- Evidence: The control system includes a control board (MCP23008 8-Channel 8 W Open Collector FET Driver I2C Shield with IoT Interface, NCD), an Arduino (Arduino Uno, Arduino), and custom Python scripts.
- Full pipeline: stage not stated [Python, SciPy]

### In vivo selection of synthetic nucleocapsids for tissue targeting. (PNAS 2023)

- DOI: 10.1073/pnas.2306129120 | PMCID: PMC10655225 | PMID: 37939083
- Evidence: Sequencing analysis was performed by aligning the MiSeq output files with PEAR (a fast and accurate Illumina Paired-End reAd mergeR) and using custom Python scripts ( 51 ).
- Full pipeline: alignment/mapping [Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold]

### The roles of surround inhibition for the intrinsic function of the striatum, analyzed in silico. (PNAS 2023)

- DOI: 10.1073/pnas.2313058120 | PMCID: PMC10636308 | PMID: 37922329
- Evidence: The platform is written in Python, and the neuron models are simulated in NEURON ( https://github.com/Hjorthmedh/Snudda ).
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> simulation/modelling [Python]

### Amazon deforestation causes strong regional warming. (PNAS 2023)

- DOI: 10.1073/pnas.2309123120 | PMCID: PMC10636322 | PMID: 37903256
- Version used: **3.9.7**
- Evidence: Halo analysis was conducted in Python version 3.9.7 using the Geopandas package version 0.10.2.
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [Jupyter] -> stage not stated [Python v3.9.7]

### Interspecies interactions determine growth dynamics of biopolymer-degrading populations in microbial communities. (PNAS 2023)

- DOI: 10.1073/pnas.2305198120 | PMCID: PMC10622921 | PMID: 37878716
- Version used: **3.7**
- Evidence: Growth curves were analyzed in Python v3.7 using the Amiga package ( 46 ) and GraphPad Prism v8 (GraphPad Software, USA).
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [Python v3.7]

### Universal abundance fluctuations across microbial communities, tropical forests, and urban populations. (PNAS 2023)

- DOI: 10.1073/pnas.2215832120 | PMCID: PMC10622915 | PMID: 37874854
- Evidence: The data were fit and parameters were estimated by maximum likelihood estimation from the Scipy package in Python.
- Full pipeline: stage not stated [Python, SciPy]

### Curiosity evolves as information unfolds. (PNAS 2023)

- DOI: 10.1073/pnas.2301974120 | PMCID: PMC10614840 | PMID: 37844235
- Evidence: Figures were produced in Python with Seaborn and Matplotlib.
- Full pipeline: differential/statistical testing [lme4] -> visualisation [Matplotlib, Python, seaborn] -> stage not stated [R v4.0]

### Neural evidence of switch processes during semantic and phonetic foraging in human memory. (PNAS 2023)

- DOI: 10.1073/pnas.2312462120 | PMCID: PMC10589708 | PMID: 37824523
- Version used: **2.7**
- Evidence: VFClust version 0.1.1 ( 94 ) with Python 2.7 was used to measure phonetic similarity of letter fluency responses.
- Full pipeline: alignment/mapping [SPM] -> dimensionality reduction/clustering [AFNI] -> differential/statistical testing [SPM] -> stage not stated [Python v2.7]

### Signatures of cross-modal alignment in children's early concepts. (PNAS 2023)

- DOI: 10.1073/pnas.2309688120 | PMCID: PMC10589699 | PMID: 37819984
- Evidence: Clustering and betweenness measures were obtained using networkx in Python ( 59 ).
- Full pipeline: dimensionality reduction/clustering [NetworkX, Python] -> differential/statistical testing [scikit-learn]

### Plants sum and subtract stimuli over different timescales. (PNAS 2023)

- DOI: 10.1073/pnas.2306655120 | PMCID: PMC10589710 | PMID: 37816057
- Evidence: The code was written in Python and based on ref.
- Full pipeline: stage not stated [Python]

### Deciphering RNA splicing logic with interpretable machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2221165120 | PMCID: PMC10576025 | PMID: 37796983
- Version used: **3.8**
- Evidence: The model was implemented in Python 3.8 ( 48 ) using Tensorflow 2.6 ( 49 ) and Numpy 1.20 ( 50 ).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [NumPy v1.20, Python v3.8, TensorFlow v2.6]

### Loss of Pde1 function acts as an evolutionary gateway to penicillin resistance in <i>Streptococcus pneumoniae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2308029120 | PMCID: PMC10576035 | PMID: 37796984
- Evidence: Custom Python scripts were written to parse the NHMMER output files, including extracting the sequences identified by NHMMER from the isolate assembly files and translating the sequences to amino acid sequences for use in downstream analyses.
- Full pipeline: alignment/mapping [Clustal Omega, HMMER v3.2.1] -> stage not stated [Python, SPAdes v3.15.5]

### Hippocampal activity predicts contextual misattribution of false memories. (PNAS 2023)

- DOI: 10.1073/pnas.2305292120 | PMCID: PMC10556612 | PMID: 37751551
- Evidence: Linear mixed effects models were run using the MixedLM function in the package statsmodels in Python ( 102 ), and always included a random intercept for each session, nested in participant.
- Full pipeline: differential/statistical testing [Python, statsmodels]

### Convergence in sympatric swallowtail butterflies reveals ecological interactions as a key driver of worldwide trait diversification. (PNAS 2023)

- DOI: 10.1073/pnas.2303060120 | PMCID: PMC10500277 | PMID: 37669385
- Evidence: The method was implemented in Python, mainly using the Pytorch library for machine learning, and the Lightly library for SimCLR-related augmentations, backbone, and loss function.
- Full pipeline: stage not stated [PyTorch, Python, R]

### The spread of interferon-γ in melanomas is highly spatially confined, driving nongenetic variability in tumor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2304190120 | PMCID: PMC10468618 | PMID: 37603742
- Evidence: Analysis was done with FlowJo software (TreeStar) and with custom code written in Python and available on GitHub ( https://github.com/oylab/oyFlow ).
- Full pipeline: stage not stated [GSEA, Python]

### Resource competition can explain simplicity in microbial community assembly. (PNAS 2023)

- DOI: 10.1073/pnas.2212113120 | PMCID: PMC10469513 | PMID: 37603734
- Version used: **3.9.13**
- Evidence: The simulations are implemented with Python 3.9.13.
- Full pipeline: simulation/modelling [Python v3.9.13]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **3.9.5**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### The structural basis of hyperpromiscuity in a core combinatorial network of type II toxin-antitoxin and related phage defense systems. (PNAS 2023)

- DOI: 10.1073/pnas.2305393120 | PMCID: PMC10440598 | PMID: 37556498
- Evidence: TA pairs were predicted with the Python script NetFlax, which is a modification of our FlaGs program.
- Full pipeline: visualisation [Cytoscape v3.5.0] -> stage not stated [AlphaFold, Python]

### Human white matter myelinates faster in utero than ex utero. (PNAS 2023)

- DOI: 10.1073/pnas.2303491120 | PMCID: PMC10438384 | PMID: 37549280
- Evidence: To distinguish developmental hypotheses on the impact of birth on white matter myelination, first, we developed and shared open-source software [baby automated fiber quantification in Python (pyBabyAFQ)] that enables the identification of 20 white matter bundles in individual infants and the analysis of T1w/T2w and other measures along their lengths on a large scale.
- Full pipeline: quantification [Python] -> stage not stated [FSL, MRtrix3]

### Modulatory dynamics mark the transition between anesthetic states of unconsciousness. (PNAS 2023)

- DOI: 10.1073/pnas.2300058120 | PMCID: PMC10372635 | PMID: 37467269
- Evidence: The model output was analyzed using Python 3.
- Full pipeline: stage not stated [Python]

### Genomic and geographical structure of human cytomegalovirus. (PNAS 2023)

- DOI: 10.1073/pnas.2221797120 | PMCID: PMC10372631 | PMID: 37459519
- Evidence: A Python script using Biopython ( 80 ), specifically the Entrez module, was used to access the SRA and NCBI nucleotide databases for sequence information and extract country and continent assignment for sequences.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> registration [MAFFT, MUSCLE] -> stage not stated [IQ-TREE, Python, R]

### A variant-dependent molecular clock with anomalous diffusion models SARS-CoV-2 evolution in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2303578120 | PMCID: PMC10372551 | PMID: 37459528
- Evidence: All top–down biostatistical and bioinformatic analyses were carried out in Python.
- Full pipeline: differential/statistical testing [Python]

### Decoupling of catalysis and transition state analog binding from mutations throughout a phosphatase revealed by high-throughput enzymology. (PNAS 2023)

- DOI: 10.1073/pnas.2219074120 | PMCID: PMC10629569 | PMID: 37428919
- Evidence: PDB structures containing tungstate and vanadate compounds bound to proteins were analyzed using the Bio.PDB package in Python.
- Full pipeline: dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [UMAP] -> stage not stated [Python]

### A cellular and molecular spatial atlas of dystrophic muscle. (PNAS 2023)

- DOI: 10.1073/pnas.2221249120 | PMCID: PMC10629561 | PMID: 37410813
- Evidence: To further explore how local muscle damage may signal to surrounding tissue to promote widespread pathology, we investigated spatial patterns of cell clusters associated with damaged areas by calculating neighborhood enrichment scores based on proximity on the connectivity graph of spot clusters (via Spatial Quantification of Molecular Data in Python; Squidpy) ( 25 ).
- Full pipeline: quantification [Python] -> normalisation [Seurat] -> dimensionality reduction/clustering [Python, R, Seurat, Squidpy, UMAP] -> differential/statistical testing [R] -> visualisation [UMAP]

### Comprehensive tissue deconvolution of cell-free DNA by deep learning for disease diagnosis and monitoring. (PNAS 2023)

- DOI: 10.1073/pnas.2305236120 | PMCID: PMC10334733 | PMID: 37399400
- Evidence: Data, Materials, and Software Availability cfSort is implemented in Python and is freely available for academic and research usage through the GitHub repository, https://github.com/jasminezhoulab/cfSort ( 45 ).
- Full pipeline: stage not stated [HOMER, Python]

### Gating of homeostatic regulation of intrinsic excitability produces cryptic long-term storage of prior perturbations. (PNAS 2023)

- DOI: 10.1073/pnas.2222016120 | PMCID: PMC10293857 | PMID: 37339223
- Evidence: The model and the integration routine were implemented in Python.
- Full pipeline: visualisation [Matplotlib, NumPy] -> stage not stated [Python]

### Speckle-correlation imaging through a kaleidoscopic multimode fiber. (PNAS 2023)

- DOI: 10.1073/pnas.2221407120 | PMCID: PMC10293815 | PMID: 37343065
- Evidence: Data, Materials, and Software Availability Raw experimental data and Python scripts are available for this article (DOI: https://doi.org/10.57745/B6PSX0 ) ( 56 ).
- Full pipeline: stage not stated [Python]

### Development potential of nanoenabled agriculture projected using machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2301885120 | PMCID: PMC10288598 | PMID: 37314934
- Version used: **3.8**
- Evidence: RF models were built by the scikit-learn “RandomForestRegressor” in Python 3.8.
- Full pipeline: stage not stated [Keras, Python v3.8, R v4.0, TensorFlow, igraph, scikit-learn]

### In vivo bone marrow microenvironment siRNA delivery using lipid-polymer nanoparticles for multiple myeloma therapy. (PNAS 2023)

- DOI: 10.1073/pnas.2215711120 | PMCID: PMC10288566 | PMID: 37310997
- Evidence: Python scripts were written to quantify barcodes from Illumina fastq files.
- Full pipeline: quantification [Python]

### Biological neurons act as generalization filters in reservoir computing. (PNAS 2023)

- DOI: 10.1073/pnas.2217008120 | PMCID: PMC10288593 | PMID: 37307467
- Evidence: The output layer was implemented offline in a custom Python script.
- Full pipeline: stage not stated [Python]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Version used: **3.7**
- Evidence: Volumetric segmentation and analysis were performed using the NumPy, ANTsPy , and NiBabel packages in Python (Python 3.7).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### Programmable self-organization of heterogeneous microrobot collectives. (PNAS 2023)

- DOI: 10.1073/pnas.2221913120 | PMCID: PMC10268276 | PMID: 37276400
- Evidence: A Python script was developed using the OpenCV library to process the experimental videos and extract the positions of the microrobots.
- Full pipeline: stage not stated [OpenCV, Python]

### Adaptive and maladaptive introgression in grapevine domestication. (PNAS 2023)

- DOI: 10.1073/pnas.2222041120 | PMCID: PMC10268302 | PMID: 37276420
- Evidence: Sequence similarity ( D xy ), and fixation indices ( F ST ) were calculated using the Python script: popgenWindows.py ( https://github.com/simonhmartin/genomics_general ) with 50-kb nonoverlapping windows.
- Full pipeline: stage not stated [Python]

### Sensing prior constraints in deep neural networks for solving exploration geophysical problems. (PNAS 2023)

- DOI: 10.1073/pnas.2219573120 | PMCID: PMC10265955 | PMID: 37262111
- Evidence: Such an integration can be simply implemented with the cumsum function in Python.
- Full pipeline: stage not stated [Python]

### HIV-1 usurps transcription start site heterogeneity of host RNA polymerase II to maximize replication fitness. (PNAS 2023)

- DOI: 10.1073/pnas.2305103120 | PMCID: PMC10266039 | PMID: 37252967
- Evidence: A custom Python script was used to calculate the relative fitness s for each pair-wise time interval (e.g., day 3 vs. day 4; day 3 vs. day 5), and all pair-wise values were used to calculate s mean for the experiment.
- Full pipeline: stage not stated [Python]

### Brain imaging and neuropsychological assessment of individuals recovered from a mild to moderate SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217232120 | PMCID: PMC10235949 | PMID: 37220275
- Version used: **3.9.1**
- Evidence: All statistical analyses were conducted in Python 3.9.1 ( 70 , 71 ), CAT12 ( 66 , 67 , 72 ), as well as mrclusterstats ( 73 ).
- Full pipeline: normalisation [FSL] -> dimensionality reduction/clustering [Python v3.9.1] -> differential/statistical testing [Python v3.9.1] -> stage not stated [R, scikit-learn v1.0.2]

### Quantification of gallium cryo-FIB milling damage in biological lamellae. (PNAS 2023)

- DOI: 10.1073/pnas.2301852120 | PMCID: PMC10266028 | PMID: 37216561
- Evidence: We used Python scripts to extract the rotation angle and pretilt from the cis TEM ( 36 ) database generated using the tilt-enabled version of the program CTFFIND4 ( 21 , 22 ), perform a coordinate transform to convert the 2DTM coordinates to the lamella coordinate frame, and plot the 2DTM SNR as a function of lamella z-coordinate.
- Full pipeline: stage not stated [ChimeraX, EMAN2, Python]

### Cortical activity emerges in region-specific patterns during early brain development. (PNAS 2023)

- DOI: 10.1073/pnas.2208654120 | PMCID: PMC10235933 | PMID: 37216522
- Evidence: A custom script in Python was used to linearly interpolate images to the size of largest sample per stage, and VGluT2 grey values were normalized between minimum and maximum values (min-max) into a 0 to 1 scale.
- Full pipeline: quantification [ImageJ] -> normalisation [Python] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [Matplotlib] -> stage not stated [NetworkX, NumPy, SciPy]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Evidence: The linear regression was performed using the statsmodels package and the Pearson correlation coefficient was calculated using the pingouin package in Python.
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Direct neuronal reprogramming by temporal identity factors. (PNAS 2023)

- DOI: 10.1073/pnas.2122168120 | PMCID: PMC10175841 | PMID: 37126716
- Evidence: Filtered output files were analyzed in Python (Python core team, Python) using Scanpy version 1.9.1 ( 75 ).
- Full pipeline: quality control [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, Signac] -> stage not stated [Python, Scanpy v1.9.1]

### Marginal specificity in protein interactions constrains evolution of a paralogous family. (PNAS 2023)

- DOI: 10.1073/pnas.2221163120 | PMCID: PMC10160972 | PMID: 37098061
- Evidence: Data, Materials, and Software Availability Python scripts for analysis are available at https://github.com/d-ghose/laub ( 53 ).
- Full pipeline: alignment/mapping [HMMER] -> stage not stated [Python, SciPy]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: Data analysis functions were written in Python using Snakemake for workflow control ( 58 ).
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### Early path dominance as a principle for neurodevelopment. (PNAS 2023)

- DOI: 10.1073/pnas.2218007120 | PMCID: PMC10120000 | PMID: 37053187
- Evidence: Connectivity matrices are calculated using the Diffusion Imaging in Python (DIPY) software ( 54 ).
- Full pipeline: stage not stated [DIPY, Python]

### Genetic factors predict hybrid formation in the British flora. (PNAS 2023)

- DOI: 10.1073/pnas.2220261120 | PMCID: PMC10120012 | PMID: 37040419
- Evidence: Additional ploidy information was added from the Botanical Society of Britain and Ireland (BSBI) Cytology database ( 43 ) and the Kew Plant DNA C-values database ( 20 ) using custom Python scripts (see https://github.com/Euphrasiologist/web_mining ).
- Full pipeline: visualisation [R] -> stage not stated [IQ-TREE, Python, data.table, ggplot2, tidyverse]

### Identification of hidden associations among eukaryotic genes through statistical analysis of coevolutionary transitions. (PNAS 2023)

- DOI: 10.1073/pnas.2218329120 | PMCID: PMC10120013 | PMID: 37043529
- Evidence: A memory-efficient algorithm for the enumeration of cotransitions was implemented in Python ( https://github.com/lab83bio/Cotransitions ).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Python, RAxML v8.2.12]

### NeuronMotif: Deciphering cis-regulatory codes by layer-wise demixing of deep neural networks. (PNAS 2023)

- DOI: 10.1073/pnas.2216698120 | PMCID: PMC10104575 | PMID: 37023129
- Evidence: NeuronMotif was implemented in Python.
- Full pipeline: visualisation [ggplot2] -> stage not stated [Python]

### Neuronal activity regulates Matrin 3 abundance and function in a calcium-dependent manner through calpain-mediated cleavage and calmodulin binding. (PNAS 2023)

- DOI: 10.1073/pnas.2206217120 | PMCID: PMC10104577 | PMID: 37011198
- Evidence: Separate Python scripts were used for image processing, neuron segmentation, establishment of regions of interest surrounding each cell, and measurement of mean GFP intensity (integrated density/area) for each neuron.
- Full pipeline: stage not stated [Python]

### Cellular segregation in cocultures is driven by differential adhesion and contractility on distinct timescales. (PNAS 2023)

- DOI: 10.1073/pnas.2213186120 | PMCID: PMC10104523 | PMID: 37011207
- Evidence: Neighbor analysis was performed with self-written Python scripts.
- Full pipeline: dimensionality reduction/clustering [scikit-image] -> stage not stated [Cellpose v1.0, OpenCV, Python]

### Disruption of energetic and dynamic base pairing cooperativity in DNA duplexes by an abasic site. (PNAS 2023)

- DOI: 10.1073/pnas.2219124120 | PMCID: PMC10083564 | PMID: 36976762
- Evidence: Data, Materials, and Software Availability Python scripts for generating abasic configurations from intact 3SPN.2 files, performing metadynamics simulations, and reweighting free energy surfaces are available at https://github.com/mrjoness/abasic-thermo/ ( 68 ).
- Full pipeline: simulation/modelling [LAMMPS, Python] -> stage not stated [PLUMED]

### Patterning of morphogenetic anisotropy fields. (PNAS 2023)

- DOI: 10.1073/pnas.2220167120 | PMCID: PMC10068776 | PMID: 36947516
- Version used: **3.8**
- Evidence: The numerical simulations were implemented in Python 3.8 using FEniCS ( 55 ).
- Full pipeline: simulation/modelling [Python v3.8]

### Theoretical guarantees for phylogeny inference from single-cell lineage tracing. (PNAS 2023)

- DOI: 10.1073/pnas.2203352120 | PMCID: PMC10041172 | PMID: 36927151
- Evidence: Materials and Methods Simulations and algorithms are implemented in Python in the Cassiopeia software suite ( 6 ) ( https://github.com/YosefLab/Cassiopeia ).
- Full pipeline: simulation/modelling [Python] -> stage not stated [NetworkX]

### Learning critically drives parkinsonian motor deficits through imbalanced striatal pathway recruitment. (PNAS 2023)

- DOI: 10.1073/pnas.2213093120 | PMCID: PMC10041136 | PMID: 36920928
- Evidence: Standard immunohistochemistry techniques were used, and images were analyzed with ImageJ and custom software written in Python.
- Full pipeline: stage not stated [ImageJ, Python]

### Transcription shapes 3D chromatin organization by interacting with loop extrusion. (PNAS 2023)

- DOI: 10.1073/pnas.2210480120 | PMCID: PMC10089175 | PMID: 36897969
- Evidence: Pileups were computed from Python scripts by collecting snippets of maps (“observed”) around sites of interest (such as ends of genes, CTCF sites, or island–island contacts), normalizing each diagonal by the value of the scaling (“expected”) at that diagonal, and averaging “observed-over-expected” values across the collected snippets ( https://github.com/mirnylab/moving-barriers-paper ).
- Full pipeline: normalisation [Python] -> simulation/modelling [OpenMM]

### Genes and sites under adaptation at the phylogenetic scale also exhibit adaptation at the population-genetic scale. (PNAS 2023)

- DOI: 10.1073/pnas.2214977120 | PMCID: PMC10089192 | PMID: 36897968
- Version used: **3.9**
- Evidence: The Snakemake pipeline for integrating polymorphism and divergence data uses custom scripts written in Python 3.9.
- Full pipeline: stage not stated [Python v3.9, Snakemake]

### Self-propelling colloids with finite state dynamics. (PNAS 2023)

- DOI: 10.1073/pnas.2213481120 | PMCID: PMC10089169 | PMID: 36881619
- Evidence: All the particles in the field of view were located and tracked using the TrackPy library in Python ( 56 ).
- Full pipeline: stage not stated [Python]

### Activation energy for pore opening in lipid membranes under an electric field. (PNAS 2023)

- DOI: 10.1073/pnas.2213112120 | PMCID: PMC10089165 | PMID: 36881617
- Evidence: Statistical analysis of our data required the development of homemade Python scripts implemented on Visual Studio.
- Full pipeline: differential/statistical testing [Python]

### <i>Leishmania</i> allelic selection during experimental sand fly infection correlates with mutational signatures of oxidative DNA damage. (PNAS 2023)

- DOI: 10.1073/pnas.2220828120 | PMCID: PMC10013807 | PMID: 36848551
- Version used: **3.10**
- Evidence: Further SNP analyses were performed based on the filtered outputs of GIP using custom Python 3.10 code relying on the following libraries: Pandas (1.4.2) ( 24 ), Pysam (0.19.0) ( 25 ), Numpy (1.22.3) ( 26 ), Matplotlib (3.5.1) ( 27 ), Seaborn (0.11.2) ( 28 ), Biotite (0.32.0) ( 29 ), and Upsetplot (0.6.0) ( 30 ).
- Full pipeline: stage not stated [Matplotlib v3.5.1, NumPy v1.22.3, Python v3.10, seaborn v0.11.2]

### Closed-loop network of skin-interfaced wireless devices for quantifying vocal fatigue and providing user feedback. (PNAS 2023)

- DOI: 10.1073/pnas.2219394120 | PMCID: PMC9992836 | PMID: 36802437
- Version used: **3.0**
- Evidence: All analyses used Python 3.0 with SciPy and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### Bayesian inference in ring attractor networks. (PNAS 2023)

- DOI: 10.1073/pnas.2210622120 | PMCID: PMC9992764 | PMID: 36812206
- Version used: **3.9.1**
- Evidence: For all our simulations, we used Python 3.9.1 with NumPy 1.19.2.
- Full pipeline: simulation/modelling [NumPy v1.19.2, Python v3.9.1]

### Peptide-binding specificity prediction using fine-tuned protein structure prediction networks. (PNAS 2023)

- DOI: 10.1073/pnas.2216697120 | PMCID: PMC9992841 | PMID: 36802421
- Evidence: A Python script that performs parameter fine-tuning, together with command line parameters and example inputs, is provided in the GitHub repository associated with this manuscript.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AlphaFold, Python, RoseTTAFold]

### Effective bet-hedging through growth rate dependent stability. (PNAS 2023)

- DOI: 10.1073/pnas.2211091120 | PMCID: PMC9974493 | PMID: 36780518
- Evidence: The numerical calculations for the general model were done in Python.
- Full pipeline: stage not stated [Python]

### Decoding the metabolic response of <i>Escherichia coli</i> for sensing trace heavy metals in water. (PNAS 2023)

- DOI: 10.1073/pnas.2210061120 | PMCID: PMC9963153 | PMID: 36745806
- Version used: **3.6**
- Evidence: The transferred CNN is built by Tensorflow 1.8 in Python 3.6.
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> machine learning [scikit-learn] -> stage not stated [Keras, Python v3.6, TensorFlow]

### Quantitative analysis of sterol-modulated monomer-dimer equilibrium of the β&lt;sub&gt;1&lt;/sub&gt;-adrenergic receptor by DEER spectroscopy. (PNAS 2023)

- DOI: 10.1073/pnas.2221036120 | PMCID: PMC9963004 | PMID: 36745787
- Evidence: The raw DEER echo curves in digital format and the Python scripts used to globally fit the data have been deposited in Figshare (DOI: 10.6084/m9.figshare.21810408 ) ( 61 ).
- Full pipeline: stage not stated [Python]

### Genome-wide CRISPRi screen identifies enhanced autolithotrophic phenotypes in acetogenic bacterium <i>Eubacterium limosum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216244120 | PMCID: PMC9963998 | PMID: 36716373
- Evidence: The in-house Python scripts are available on our website (cholab.or.kr).
- Full pipeline: differential/statistical testing [Conda] -> stage not stated [Python]

### Supramolecular organization and dynamics of mannosylated phosphatidylinositol lipids in the mycobacterial plasma membrane. (PNAS 2023)

- DOI: 10.1073/pnas.2212755120 | PMCID: PMC9945971 | PMID: 36693100
- Evidence: Simulations of the bilayer were set up using a modified version of insane.py Python script ( 30 ), available on the P Stansfeld lab Github page (see Data Availability section), using the composition shown in Fig.
- Full pipeline: simulation/modelling [GROMACS v2021.3, Python] -> stage not stated [AlphaFold, Clustal Omega, Matplotlib, PLUMED]

### Genome-wide analysis of heat stress-stimulated transposon mobility in the human fungal pathogen &lt;i&gt;Cryptococcus deneoformans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2209831120 | PMCID: PMC9942834 | PMID: 36669112
- Evidence: Python scripts developed for the detection of TE movement and permutation analysis (and figure generation) are publicly available on GitHub: https://github.com/magwenelab/Transposon-mobility ( 69 ).
- Full pipeline: differential/statistical testing [Python]

### Evidence for high-performance suction feeding in the Pennsylvanian stem-group holocephalan <i>Iniopera</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2207854119 | PMCID: PMC9942859 | PMID: 36649436
- Evidence: We modified a Python script from Lautenschlager ( 32 ) that was used to calculate the extension of the muscle cylinders and output the strain factor for each frame.
- Full pipeline: stage not stated [Python]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: We calculated nucleotide diversity for each of the six sample sites as well as F ST and D XY between all pairs of sites using the Python scripts parseVCF.py and popgenWindows.py ( https://github.com/simonhmartin/genomics_general ).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### Multimodal epigenetic changes and altered NEUROD1 chromatin binding in the mouse hippocampus underlie FOXG1 syndrome. (PNAS 2023)

- DOI: 10.1073/pnas.2122467120 | PMCID: PMC9926245 | PMID: 36598943
- Evidence: All other data types and codes recreating the analyses from the data files can be found at https://github.com/Vogel-lab/Integrative-multiomics-analyses-of-FOXG1-functions as R markdown files, Python scripts, and Galaxy workflows.
- Full pipeline: stage not stated [Python, STRING db]

### Anatomically interpretable deep learning of brain age captures domain-specific cognitive impairment. (PNAS 2023)

- DOI: 10.1073/pnas.2214634120 | PMCID: PMC9926270 | PMID: 36595679
- Version used: **3.6**
- Evidence: The DL architecture was implemented in Python 3.6 using TensorFlow 2.7.0 and executed on a computer with an Intel Core i7 processor (2.2 GHz clock speed) with 16 GB of RAM and a 12 GB NVIDIA Tesla K80 graphical processing unit.
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [Python v3.6, TensorFlow v2.7.0]

### SUMO enhances unfolding of SUMO-polyubiquitin-modified substrates by the Ufd1/Npl4/Cdc48 complex. (PNAS 2023)

- DOI: 10.1073/pnas.2213703120 | PMCID: PMC9910466 | PMID: 36574706
- Evidence: Composite maps were generated in Python-based Hierarchical ENvironment for Integrated Xtallography (PHENIX) ( 63 ) with focused refinement maps and atomic models were refined using PHENIX ( 63 ) and model geometry analyzed using Molprobity ( 64 ).
- Full pipeline: structure determination [PHENIX, Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2, RELION v3.0]

### Rapid infant learning of syntactic-semantic links. (PNAS 2023)

- DOI: 10.1073/pnas.2209153119 | PMCID: PMC9910616 | PMID: 36574655
- Version used: **3.5**
- Evidence: The experiment was coded in Python 3.5, using the Psychopy 2.7 toolbox (all codes are available on the study’s OSF page).
- Full pipeline: stage not stated [Python v3.5, lme4]

### Computational design of CRISPR guide RNAs to enable strain-specific control of microbial consortia. (PNAS 2023)

- DOI: 10.1073/pnas.2213154120 | PMCID: PMC9910470 | PMID: 36574681
- Version used: **3.7**
- Evidence: All programming was performed using Python 3.7, Spyder IDE, and Anaconda software package.
- Full pipeline: stage not stated [Conda, Python v3.7]

### Microscopic phage adsorption assay: High-throughput quantification of virus particle attachment to host bacterial cells. (PNAS 2024)

- DOI: 10.1073/pnas.2410905121 | PMCID: PMC11670125 | PMID: 39700139
- Evidence: Our algorithm is described in SI Appendix , which is equivalent to popular particle tracking programs such as trackpy in Python, and TrackMate in ImageJ/Fiji.
- Full pipeline: stage not stated [ImageJ, Python, TrackMate]

### Photosynthetic demands on translational machinery drive retention of redundant tRNA metabolism in plant organelles. (PNAS 2024)

- DOI: 10.1073/pnas.2421485121 | PMCID: PMC11670086 | PMID: 39693336
- Evidence: Once we had a curated set of protein sequences for all species, they were checked for completeness of length and subsequent visualization with a custom Python script.
- Full pipeline: read trimming [MAFFT v7.525, RAxML v8.2.12, SPAdes v3.15.4] -> alignment/mapping [MAFFT v7.525, RAxML v8.2.12] -> visualisation [Python]

### Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase. (PNAS 2024)

- DOI: 10.1073/pnas.2423270121 | PMCID: PMC11670102 | PMID: 39689177
- Evidence: We then used custom Python scripts to extract C-to-T conversion states for deduplicated reads and generate a conversion ratio for every genome position.
- Full pipeline: quality control [ArchR, UMAP] -> read trimming [Bismark, Python, Trim Galore v0.6.10, Trimmomatic v0.39] -> alignment/mapping [Bismark, Trim Galore v0.6.10, Trimmomatic v0.39] -> dimensionality reduction/clustering [ArchR, UMAP]

### Nutrient colimitation is a quantitative, dynamic property of microbial populations. (PNAS 2024)

- DOI: 10.1073/pnas.2400304121 | PMCID: PMC11670248 | PMID: 39693349
- Version used: **3.10.9**
- Evidence: We performed all numerical calculations in Python version 3.10.9, using tools from NumPy ( 76 ) version 1.24.1 and SciPy ( 77 ) version 1.10.0.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python v3.10.9, SciPy]

### 3D electron microscopy for analyzing nanoparticles in the tumor endothelium. (PNAS 2024)

- DOI: 10.1073/pnas.2406331121 | PMCID: PMC11665908 | PMID: 39665759
- Evidence: The roughly aligned dataset was processed in Python by a customized elastic alignment algorithm called SAToRI.
- Full pipeline: alignment/mapping [Python] -> stage not stated [ImageJ, OpenCV, scikit-learn]

### Kinetic principles of chemical cross-link formation for protein-protein interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2402040121 | PMCID: PMC11665911 | PMID: 39652756
- Evidence: The results obtained by simulation are evaluated and visualized using the Python library altair ( 48 ), using a combination of Python scripts and Python notebooks (the user front-end).
- Full pipeline: alignment/mapping [ChimeraX] -> simulation/modelling [Python] -> visualisation [Python]

### AI-boosted and motion-corrected, wireless near-infrared sensing system for continuously monitoring laryngeal muscles. (PNAS 2024)

- DOI: 10.1073/pnas.2410750121 | PMCID: PMC11665861 | PMID: 39652765
- Version used: **3.10.11**
- Evidence: The training and validation were conducted in Visual Studio Code (version 1.86) environment embedded with Python 3.10.11.
- Full pipeline: machine learning [PyTorch, Python v3.10.11]

### Intracortical recordings reveal the neuronal selectivity for bodies and body parts in the human visual cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2408871121 | PMCID: PMC11665852 | PMID: 39652751
- Evidence: We utilized the MDS implementation from the scikit-learn library (implemented in Python).
- Full pipeline: stage not stated [FreeSurfer, Python, SPM, scikit-learn]

### Structural insights into the assembly and energy transfer of haptophyte photosystem I-light-harvesting supercomplex. (PNAS 2024)

- DOI: 10.1073/pnas.2413678121 | PMCID: PMC11648859 | PMID: 39642204
- Evidence: Wallingford, CT, USA) and custom Python scripts ( 10.5281/zenodo.10791187 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Python]

### eLemur: A cellular-resolution 3D atlas of the mouse lemur brain. (PNAS 2024)

- DOI: 10.1073/pnas.2413687121 | PMCID: PMC11648901 | PMID: 39630862
- Evidence: Tissue part in the histology images were aligned to the corresponding parts in the block face image via multiscale 2D rigid registration from Advanced Normalization Tools ( 69 ) in Python.
- Full pipeline: alignment/mapping [ANTs, Python] -> normalisation [ANTs, Python] -> registration [ANTs, Python] -> machine learning [Cellpose v2.0]

### C9orf72-linked arginine-rich dipeptide repeats aggravate pathological phase separation of G3BP1. (PNAS 2024)

- DOI: 10.1073/pnas.2402847121 | PMCID: PMC11648655 | PMID: 39621905
- Evidence: The figure was created in Python3 using the “matplotlib” module ( https://matplotlib.org/ ) Analysis of MLO Proteomes and Their Overlap with the R-DPR Interactome.
- Full pipeline: stage not stated [Matplotlib, Python]

### Diversification of pectoral control through motor pool extension. (PNAS 2024)

- DOI: 10.1073/pnas.2413415121 | PMCID: PMC11626184 | PMID: 39602261
- Evidence: 8.04, Wavemetrics, Portland, OR, United States) and a custom-written Python script (v.
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [SciPy] -> stage not stated [Matplotlib, NumPy, Python, seaborn]

### Mutation-based mechanism and evolution of the potent multidrug efflux pump RE-CmeABC in &lt;i&gt;Campylobacter&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2415823121 | PMCID: PMC11665921 | PMID: 39602248
- Evidence: The entire region (~6.4 Kb) of cmeR - cmeABC of each isolate was retrieved from genomes by an in-house Python script.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic] -> alignment/mapping [Bowtie2, MAFFT] -> stage not stated [Python]

### Compartmentalized pooling generates orientation selectivity in wide-field amacrine cells. (PNAS 2024)

- DOI: 10.1073/pnas.2411130121 | PMCID: PMC11626119 | PMID: 39602271
- Version used: **3.12**
- Evidence: The minimal biophysical model was implemented using NEURON version 8.2.6 in Python 3.12 and analyzed using Mathematica 14.1.
- Full pipeline: stage not stated [Python v3.12]

### Dissecting neurofilament tail sequence-phosphorylation-structure relationships with multicomponent reconstituted protein brushes. (PNAS 2024)

- DOI: 10.1073/pnas.2410109121 | PMCID: PMC11626179 | PMID: 39602260
- Evidence: Locally averaged net charge per residue was calculated in Python for each sequence as the average charge within a moving w https://github.com/eading-7/nf-brushes indow along the sequence length, with a window size of 31 residues.
- Full pipeline: stage not stated [ImageJ, Python]

### Stabilizing selection in an identified multisensory neuron in blind cavefish. (PNAS 2024)

- DOI: 10.1073/pnas.2415854121 | PMCID: PMC11626160 | PMID: 39556758
- Evidence: For further processing and analysis, we used the acquisition software package Spike2 (version 6; Cambridge Electronic Design Limited, Cambridge, UK) and custom-made software written in Python.
- Full pipeline: stage not stated [Python]

### Frontotemporal network contribution to occluded face processing. (PNAS 2024)

- DOI: 10.1073/pnas.2407457121 | PMCID: PMC11621840 | PMID: 39556727
- Evidence: Data analysis was conducted using MATLAB (MathWorks) with the exception of Granger causality analysis, which was performed in Python.
- Full pipeline: stage not stated [Python]

### Osmotic and phoretic competition explains chemotaxic assembly and sorting. (PNAS 2024)

- DOI: 10.1073/pnas.2410840121 | PMCID: PMC11588119 | PMID: 39541356
- Evidence: These particle trajectories are tracked and analyzed using the TrackPy library in Python ( 45 ) based on the Crocker-Grier algorithm ( 46 ), which yields the velocity vs. distance curves as presented It is known that the background ionic strength and pH will affect the magnitude and sign of the velocity, and we do see such an effect in this system as others have studied ( 4 , 29 ).
- Full pipeline: simulation/modelling [Python]

### DeSide: A unified deep learning approach for cellular deconvolution of tumor microenvironment. (PNAS 2024)

- DOI: 10.1073/pnas.2407096121 | PMCID: PMC11573681 | PMID: 39514318
- Evidence: Supplementary Material Appendix 01 (PDF) Dataset S01 (XLSX) Dataset S02 (XLSX) Dataset S03 (XLSX) Dataset S04 (XLSX) Dataset S05 (XLSX) Dataset S06 (XLSX) Dataset S07 (XLSX) Dataset S08 (XLSX) Dataset S09 (XLSX) Data, Materials, and Software Availability DeSide is implemented in Python using the TensorFlow library for constructing the DNN model.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, Python, TensorFlow]

### Cholinergic regulation of dendritic Ca&lt;sup&gt;2+&lt;/sup&gt; spikes controls firing mode of hippocampal CA3 pyramidal neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2321501121 | PMCID: PMC11572977 | PMID: 39503887
- Evidence: Clustering of Ca 2+ spikes measured in TTX was performed with the Ward hierarchical clustering method, using the sklearn.cluster module in Python.
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [ImageJ]

### Bioenergetic suppression by redox-active metabolites promotes antibiotic tolerance in &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406555121 | PMCID: PMC11573671 | PMID: 39503891
- Version used: **3.8.17**
- Evidence: Data were analyzed and processed in Python 3.8.17 using Pandas 2.0.3, NumPy 1.24.3, and SciPy 1.9.3.
- Full pipeline: stage not stated [ImageJ v1.52, NumPy v1.24.3, Python v3.8.17, SciPy v1.9.3]

### Effects of oxycodone on placental lineages: Evidence from the transcriptome profile of mouse trophoblast giant cells. (PNAS 2024)

- DOI: 10.1073/pnas.2412349121 | PMCID: PMC11551428 | PMID: 39475633
- Evidence: Given that Seurat operates in R and available RNA Velocity packages are in Python, we exported the required data for RNA Velocity analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, Python, Seurat v5.0.1]

### Hyperspectral unmixing for Raman spectroscopy via physics-constrained autoencoders. (PNAS 2024)

- DOI: 10.1073/pnas.2407439121 | PMCID: PMC11551349 | PMID: 39471214
- Evidence: This is performed using the RamanSPy package ( 83 ) in Python.
- Full pipeline: machine learning [TensorFlow] -> stage not stated [Python]

### Seawater alkalization via an energy-efficient electrochemical process for CO&lt;sub&gt;2&lt;/sub&gt; capture. (PNAS 2024)

- DOI: 10.1073/pnas.2410841121 | PMCID: PMC11551434 | PMID: 39467125
- Evidence: The one-way ANOVA was conducted by using the Scipy library (version 1.3.1) in Python.
- Full pipeline: stage not stated [Python, SciPy]

### Anomalous wet summers and rising atmospheric CO<sub>2</sub> concentrations increase the CO<sub>2</sub> sink in a poorly drained forest on permafrost. (PNAS 2024)

- DOI: 10.1073/pnas.2414539121 | PMCID: PMC11536150 | PMID: 39453750
- Evidence: The trend analysis was performed with the pymannkendall library (version 1.4.2) in Python.
- Full pipeline: stage not stated [Python]

### Meta-learning of human motor adaptation via the dorsal premotor cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2417543121 | PMCID: PMC11536165 | PMID: 39441634
- Version used: **3.7.9**
- Evidence: The manipulandum was homemade and operated with Python 3.7.9, LabView 2019, and C++.
- Full pipeline: differential/statistical testing [R v4.3.2, lme4] -> stage not stated [Python v3.7.9]

### Heat waves may trigger unexpected surge in aerosol and ozone precursor emissions from sedges in urban landscapes. (PNAS 2024)

- DOI: 10.1073/pnas.2412817121 | PMCID: PMC11551377 | PMID: 39432767
- Evidence: Isoprene emission was estimated using the MEGAN model in Python with different temperature response curves, and the meteorological data used in this study were measured at central Los Angeles (34.10351 N, −118.26970 W) and are available through the MesoWest Database ( https://mesowest.utah.edu/ ).
- Full pipeline: stage not stated [Python]

### Deciphering the neural responses to a naturalistic persuasive message. (PNAS 2024)

- DOI: 10.1073/pnas.2401317121 | PMCID: PMC11513929 | PMID: 39413130
- Evidence: The ISC analyses were conducted in Python 3, using the packages nilearn and nltools ( 103 , 104 ).
- Full pipeline: stage not stated [Nilearn, PsychoPy, Python, dcm2niix, fMRIPrep]

### A role for cross-linking proteins in actin filament network organization and force generation. (PNAS 2024)

- DOI: 10.1073/pnas.2407838121 | PMCID: PMC11513903 | PMID: 39405356
- Version used: **3.7**
- Evidence: Maximum fluorescence intensities and fimbrin and transgelin patch lifetimes were extracted from the trajectories using custom code in Python (3.7) with Jupyter Notebook (Project Jupyter).
- Full pipeline: simulation/modelling [Jupyter, Python v3.7]

### The topology and geometry of neural representations. (PNAS 2024)

- DOI: 10.1073/pnas.2317881121 | PMCID: PMC11494346 | PMID: 39374397
- Version used: **3.5.4**
- Evidence: 39 , we trained the DNNs on the complete CIFAR-10 image dataset (both training and test sets), which comprises 10 distinct object categories, each represented by 5,000 training and 1,000 test images, implemented with TensorFlow (version 1.3.0) and Python 3.5.4.
- Full pipeline: machine learning [Python v3.5.4, TensorFlow v1.3.0]

### Minimal motifs for habituating systems. (PNAS 2024)

- DOI: 10.1073/pnas.2409330121 | PMCID: PMC11474051 | PMID: 39365818
- Version used: **3.9.6**
- Evidence: Unless otherwise specified, the numerical trajectories are obtained in Python 3.9.6 using either direct convolution or an implicit Runge–Kutta scheme via the SciPy library.
- Full pipeline: simulation/modelling [Python v3.9.6, SciPy]

### A conserved peptide-binding pocket in HyNaC/ASIC ion channels. (PNAS 2024)

- DOI: 10.1073/pnas.2409097121 | PMCID: PMC11474038 | PMID: 39365813
- Version used: **3.9.7**
- Evidence: The interaction fingerprints were analyzed with Python 3.9.7 and pandas 1.3.2 and visualized with matplotlib 3.4.3.
- Full pipeline: dimensionality reduction/clustering [UCSF Chimera v1.14] -> visualisation [Matplotlib v3.4.3, Python v3.9.7] -> stage not stated [BLAST]

### Coupling of cell growth modulation to asymmetric division and cell cycle regulation in &lt;i&gt;Caulobacter crescentus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406397121 | PMCID: PMC11474046 | PMID: 39361646
- Evidence: The Python scripts used to run the analysis pipeline, the library file with the relevant custom-written functions (library.py), as well as the retrained Omnipose model used for cell segmentation (merge_model_omni.py) are available on GitHub ( https://github.com/JacobsWagnerLab/published/tree/master/Glenn_et_al_2024 ) ( 76 ).
- Full pipeline: machine learning [Python] -> stage not stated [SciPy]

### Synaptic weight dynamics underlying memory consolidation: Implications for learning rules, circuit organization, and circuit function. (PNAS 2024)

- DOI: 10.1073/pnas.2406010121 | PMCID: PMC11474072 | PMID: 39365821
- Evidence: All simulations were performed in Python by integrating the differential equations for the learning rules with the Radau solver (implemented in solve_ivp in the scipy.integrate package).
- Full pipeline: differential/statistical testing [Python, SciPy] -> simulation/modelling [Python, SciPy]

### Snowmelt duration controls red algal blooms in the snow of the European Alps. (PNAS 2024)

- DOI: 10.1073/pnas.2400362121 | PMCID: PMC11474047 | PMID: 39312681
- Evidence: We tested multiple supervised machine learning methods to classify pixels in the GBND-RGND space using scipy in Python, namely, nearest neighbors, linear support vector machine (linear SVM), Gaussian process, decision tree, random forest, and neural network.
- Full pipeline: normalisation [Matplotlib] -> machine learning [Python, SciPy] -> visualisation [Matplotlib] -> stage not stated [BLAST]

### Measurement of adhesion and traction of cells at high yield reveals an energetic ratchet operating during nephron condensation. (PNAS 2024)

- DOI: 10.1073/pnas.2404586121 | PMCID: PMC11441508 | PMID: 39292750
- Evidence: Cellular Potts modeling was implemented in Python.
- Full pipeline: stage not stated [Python]

### On the development and validation of large language model-based classifiers for identifying social determinants of health. (PNAS 2024)

- DOI: 10.1073/pnas.2320716121 | PMCID: PMC11441499 | PMID: 39284061
- Version used: **3.10.12**
- Evidence: Python 3.10.12 was used for all statistical analysis.
- Full pipeline: differential/statistical testing [Python v3.10.12]

### Leader-follower dynamics during early social interactions matter for infant word learning. (PNAS 2024)

- DOI: 10.1073/pnas.2321008121 | PMCID: PMC11420154 | PMID: 39254996
- Evidence: Brightness and contrast were normalized using the cv2 toolbox in Python.
- Full pipeline: normalisation [Python] -> stage not stated [EEGLAB, Psychtoolbox]

### Fluorescence-activated droplet sequencing (FAD-seq) directly provides sequences of screening hits in antibody discovery. (PNAS 2024)

- DOI: 10.1073/pnas.2405342121 | PMCID: PMC11406258 | PMID: 39240970
- Evidence: Sequences were analyzed with Python scripts running on v.3.9 and are available at https://github.com/aautour/nano_fadseq .
- Full pipeline: stage not stated [Python]

### Relative genotoxicity of polycyclic aromatic hydrocarbons inferred from free energy perturbation approaches. (PNAS 2024)

- DOI: 10.1073/pnas.2322155121 | PMCID: PMC11406254 | PMID: 39226345
- Evidence: ... adduct and the nucleobases that form each intercalation pocket ( E vdW:dT 16 | dT 17 and E vdW:dA 6 ∗ | dA 7 respectively) were calculated utilizing Python scripts and VMD as described in SI Appendix , Section 2 .
- Full pipeline: simulation/modelling [NAMD, VMD] -> stage not stated [Python]

### &lt;i&gt;Prevotella&lt;/i&gt; are major contributors of sialidases in the human vaginal microbiome. (PNAS 2024)

- DOI: 10.1073/pnas.2400341121 | PMCID: PMC11388281 | PMID: 39186657
- Evidence: Plots were generated using Python 3 and PRISM.
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508, RAxML v8.2.10] -> stage not stated [AlphaFold, InterProScan, Python]

### MICU1 and MICU2 control mitochondrial calcium signaling in the mammalian heart. (PNAS 2024)

- DOI: 10.1073/pnas.2402491121 | PMCID: PMC11363308 | PMID: 39163336
- Version used: **3.9.12**
- Evidence: Individual cells were masked and mean gray values were exported and further processed in Excel, Visual Studio Code 1.76.2 (using Python 3.9.12, Numpy 1.21.5, Matplotlib 3.5.1, Statsmodels 0.13.2, Pandas 1.4.2), SigmaPlot 12.5, and GraphPad Prism 9.3.0.
- Full pipeline: stage not stated [Matplotlib v3.5.1, NumPy v1.21.5, Python v3.9.12]

### Mice lacking &lt;i&gt;Astn2&lt;/i&gt; have ASD-like behaviors and altered cerebellar circuit properties. (PNAS 2024)

- DOI: 10.1073/pnas.2405901121 | PMCID: PMC11348334 | PMID: 39150780
- Evidence: All analyses on PC dendritic spines are performed using custom scripts in Python.
- Full pipeline: quantification [ImageJ v1.53c] -> differential/statistical testing [DESeq2] -> stage not stated [Python]

### The importance of the location of the N-terminus in successful protein folding in vivo and in vitro. (PNAS 2024)

- DOI: 10.1073/pnas.2321999121 | PMCID: PMC11348275 | PMID: 39145938
- Evidence: Sequencing data were analyzed using in-house Python scripts.
- Full pipeline: quantification [ImageJ] -> stage not stated [DESeq2, Python]

### Light-induced H&lt;sub&gt;2&lt;/sub&gt; generation in a photosystem I-O&lt;sub&gt;2&lt;/sub&gt;-tolerant [FeFe] hydrogenase nanoconstruct. (PNAS 2024)

- DOI: 10.1073/pnas.2400267121 | PMCID: PMC11348241 | PMID: 39136990
- Evidence: Data analysis was performed using home-built software in Python.
- Full pipeline: stage not stated [Python]

### Genetic mechanisms for impaired synaptic plasticity in schizophrenia revealed by computational modeling. (PNAS 2024)

- DOI: 10.1073/pnas.2312511121 | PMCID: PMC11348150 | PMID: 39141354
- Evidence: Our model and its implementation in Python with NEURON (RxD) interface as well as scripts for data analyses are publicly available in https://modeldb.science/267741 .
- Full pipeline: stage not stated [Python]

### Circadian period is compensated for repressor protein turnover rates in single cells. (PNAS 2024)

- DOI: 10.1073/pnas.2404738121 | PMCID: PMC11348271 | PMID: 39141353
- Evidence: For quality control, we developed a Python script (available on GitHub) that detects abrupt changes in the nuclear size of >20% and cell division events, defined as a peak in average H2B-iRFP720 fluorescence due to chromatin condensation, followed by a decrease (>20%) in nuclear size.
- Full pipeline: quality control [Python] -> stage not stated [CellProfiler, SciPy]

### GPT is an effective tool for multilingual psychological text analysis. (PNAS 2024)

- DOI: 10.1073/pnas.2308950121 | PMCID: PMC11348013 | PMID: 39133853
- Evidence: The code for querying was written in R for GPT-3.5 and in Python for GPT-4 and GPT-4 Turbo.
- Full pipeline: stage not stated [Python]

### Riemannian geometry for efficient analysis of protein dynamics data. (PNAS 2024)

- DOI: 10.1073/pnas.2318951121 | PMCID: PMC11331106 | PMID: 39121160
- Version used: **3.8**
- Evidence: Finally, all of the experiments are implemented using PyTorch in Python 3.8 and run on a 2 GHz Quad-Core Intel Core i5 with 16GB RAM.
- Full pipeline: stage not stated [PyTorch, Python v3.8]

### Length control emerges from cytoskeletal network geometry. (PNAS 2024)

- DOI: 10.1073/pnas.2401816121 | PMCID: PMC11331072 | PMID: 39106306
- Evidence: Actin cables were counted by automated detection of fluorescence peaks from line scan profiles using custom Python scripts.
- Full pipeline: stage not stated [ImageJ, Python]

### Plasticity of the selectivity filter is essential for permeation in lysosomal TPC2 channels. (PNAS 2024)

- DOI: 10.1073/pnas.2320153121 | PMCID: PMC11317647 | PMID: 39074274
- Evidence: In-built GROMACS tools, in-house Python scripts, and the MDAnalysis package ( 68 , 69 ) were used for trajectory analysis.
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.7, Python, VMD] -> visualisation [VMD] -> stage not stated [MDAnalysis]

### Antigenic cartography using variant-specific hamster sera reveals substantial antigenic variation among Omicron subvariants. (PNAS 2024)

- DOI: 10.1073/pnas.2310917121 | PMCID: PMC11317614 | PMID: 39078681
- Evidence: For the analysis of reactivity patterns of different hamster serum groups and for antigenic cartography, NT90 titers were determined from the raw plaque counts ( Dataset S2 ) using the neutcurve package (version 0.5.7) ( 39 ) written in Python, constraining the lower end of the neutralization curve to zero ( SI Appendix , Titer Determination ).
- Full pipeline: machine learning [Python] -> stage not stated [R v4.2.0]

### A combinatorially complete epistatic fitness landscape in an enzyme active site. (PNAS 2024)

- DOI: 10.1073/pnas.2400439121 | PMCID: PMC11317637 | PMID: 39074291
- Evidence: Python scripts and documentation can be found in the associated code.
- Full pipeline: read trimming [minimap2] -> alignment/mapping [minimap2] -> stage not stated [NetworkX, Python, scikit-learn]

### An ankyrin G-binding motif mediates TRAAK periodic localization at axon initial segments of hippocampal pyramidal neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2310120121 | PMCID: PMC11295008 | PMID: 39058579
- Version used: **3.9**
- Evidence: For creating a negative periodicity control, in lack of previously established and characterized nonperiodic AIS proteins, STED mimicking images were simulated using Python 3.9.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Python v3.9] -> stage not stated [AlphaFold, ImageJ, NumPy, napari]

### Aversive memories can be weakened during human sleep via the reactivation of positive interfering memories. (PNAS 2024)

- DOI: 10.1073/pnas.2400678121 | PMCID: PMC11295023 | PMID: 39052838
- Version used: **3.8**
- Evidence: All EEG processing steps were carried out using MNE-Python [v1.5.1, ( 82 )] and Python 3.8.
- Full pipeline: differential/statistical testing [Docker] -> stage not stated [MNE-Python, Python v3.8]

### GABA&lt;sub&gt;A&lt;/sub&gt; receptor subunit composition regulates circadian rhythms in rest-wake and synchrony among cells in the suprachiasmatic nucleus. (PNAS 2024)

- DOI: 10.1073/pnas.2400339121 | PMCID: PMC11295074 | PMID: 39047036
- Evidence: To locate and track cellular bioluminescence, we used a custom Python code ( 45 ) which identified cells in each frame using a standard difference of Gaussian blob detector, in addition, videos underwent pixel-based analysis using a custom Python script to measure instantaneous phase, amplitude, and synchronization index (SI).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [Python]

### Molecular mechanisms of proteoglycan-mediated semaphorin signaling in axon guidance. (PNAS 2024)

- DOI: 10.1073/pnas.2402755121 | PMCID: PMC11295036 | PMID: 39042673
- Evidence: We developed a Python script for Visual Studio Code for semiautomated analysis of the concentration gradient on the cell surface.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ImageJ, Python]

### Activating an invertebrate bistable opsin with the all-trans 6.11 retinal analog. (PNAS 2024)

- DOI: 10.1073/pnas.2406814121 | PMCID: PMC11295067 | PMID: 39042699
- Evidence: Spectroscopy data were processed and plotted using custom Python scripts; experimental data and processing scripts are available on Zenodo ( https://zenodo.org/records/1270387 ) ( 11 ).
- Full pipeline: visualisation [Python]

### Geometry-induced friction at a soft interface. (PNAS 2024)

- DOI: 10.1073/pnas.2320068121 | PMCID: PMC11287152 | PMID: 39024108
- Evidence: We determine the radii of the sheet W ( t ) and the hydrogel substrate R ( t ) from the fluorescence and bright field images, respectively, by using image analysis codes written in Python.
- Full pipeline: stage not stated [Python]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: To estimate the number of trees required to sample from each seed zone to recapitulate the multivariate allele-frequencies (AFs) at adaptive loci and inform germplasm conservation, we used a custom Python script to compare AFs for adaptive SNPs in the full population with bootstrap samples of varying size using linear regression ( https://github.com/alex-sandercock/Capturing_genomic_diversity ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Clustered protocadherin <i>cis</i>-interactions are required for combinatorial cell-cell recognition underlying neuronal self-avoidance. (PNAS 2024)

- DOI: 10.1073/pnas.2319829121 | PMCID: PMC11260096 | PMID: 38976736
- Evidence: 2 and 5 were quantified using a custom Python script.
- Full pipeline: quantification [Python] -> stage not stated [ImageJ]

### Mechanism of phosphate release from actin filaments. (PNAS 2024)

- DOI: 10.1073/pnas.2408156121 | PMCID: PMC11260136 | PMID: 38980907
- Evidence: The data generated from the simulations were analyzed by VMD ( 56 ), PyMol ( 61 , 62 ) and Python library MDanalysis ( 63 , 64 ), and an in-house Python script.
- Full pipeline: simulation/modelling [GROMACS v2020.4, PLUMED v2.4, PyMOL, Python] -> stage not stated [VMD]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: Model-based analysis for ChIP-Seq (MACS2) callpeak (Version 2.2.7.1) in Python (Anaconda 2020.11) was used to distinguish any peaks from background observed in all samples ( 48 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### TMEM16F exacerbates tau pathology and mediates phosphatidylserine exposure in phospho-tau-burdened neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2311831121 | PMCID: PMC11228522 | PMID: 38941274
- Evidence: Traced ImageJ ROIs were extracted and color deconvoluted into cresyl violet and DAB channels using the scikit-image package in Python ( 63 ).
- Full pipeline: stage not stated [ImageJ, Python, napari, scikit-image]

### Nanoscale architecture of synaptic vesicles and scaffolding complexes revealed by cryo-electron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2403136121 | PMCID: PMC11228483 | PMID: 38923992
- Evidence: All analysis was implemented in Python.
- Full pipeline: quality control [IMOD] -> alignment/mapping [IMOD] -> machine learning [EMAN2] -> visualisation [ChimeraX] -> stage not stated [Python]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Evidence: The in-house Python scripts for frequency calculate and gene annotation of SVs are available on GitHub ( https://github.com/xiaolongliang/TibetanSheep_SVs ).
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Modular binder technology by NGS-aided, high-resolution selection in yeast of designed armadillo modules. (PNAS 2024)

- DOI: 10.1073/pnas.2318198121 | PMCID: PMC11228518 | PMID: 38917007
- Evidence: The remaining sequences were clustered at 100% identity by a custom Python script.
- Full pipeline: alignment/mapping [Bowtie2, UMAP] -> dimensionality reduction/clustering [Python, UMAP] -> structure determination [PHENIX] -> visualisation [UMAP] -> stage not stated [CCP4]

### Multiple evolutionary pressures shape identical consonant avoidance in the world's languages. (PNAS 2024)

- DOI: 10.1073/pnas.2316677121 | PMCID: PMC11228491 | PMID: 38917001
- Evidence: Data were processed using Python 3 as well as version 0.6-99 of the R package phytools ( 99 ).
- Full pipeline: stage not stated [Python, R, Stan v2.26.13, phytools]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Evidence: This graph was further divided into clusters (i.e., gene families) by the Markov clustering algorithm implemented in the markov_clustering package in Python with default parameters except that inflation was set to 1.1.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### The role of shear forces in primary and secondary nucleation of amyloid fibrils. (PNAS 2024)

- DOI: 10.1073/pnas.2322572121 | PMCID: PMC11194593 | PMID: 38875148
- Evidence: Using a custom-written Python script, single-molecule events were recorded as discrete events using a Lee filter of three from the acquired photon stream as fluorescence bursts with 0.001 μ s of the interphoton time and containing 22 photons minimum.
- Full pipeline: stage not stated [ImageJ, Python]

### Measuring and modeling the dynamics of mitotic error correction. (PNAS 2024)

- DOI: 10.1073/pnas.2323009121 | PMCID: PMC11194551 | PMID: 38875144
- Evidence: Z-stacks were run through the custom Python 3 kinetochore counting code in JupyterLab.
- Full pipeline: stage not stated [NumPy, Python, SciPy]

### Primordial magnetotaxis in putative giant paleoproterozoic magnetofossils. (PNAS 2024)

- DOI: 10.1073/pnas.2319148121 | PMCID: PMC11161745 | PMID: 38805285
- Evidence: The data are subdivided into folders, including the meshes used in our simulations (.pat files), Python scripts, MERRILL scripts, and outputs achieved from the simulations (.out files).
- Full pipeline: simulation/modelling [Python]

### Molecular basis for antibody recognition of multiple drug-peptide/MHC complexes. (PNAS 2024)

- DOI: 10.1073/pnas.2319029121 | PMCID: PMC11145297 | PMID: 38781214
- Evidence: Sequencing data were analyzed using a set of in-house developed Python scripts to deduce the number of reads for each mutation ( 21 ).
- Full pipeline: structure determination [UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [MotionCor2 v1.5, PHENIX v1.18.2, Python]

### The evolution of sex roles: The importance of ecology and social environment. (PNAS 2024)

- DOI: 10.1073/pnas.2321294121 | PMCID: PMC11145285 | PMID: 38771872
- Version used: **3.10**
- Evidence: S1 ) using sumtree in DendroPy package in Python 3.10.
- Full pipeline: differential/statistical testing [R, lavaan] -> simulation/modelling [R] -> stage not stated [Python v3.10]

### Ketamine can produce oscillatory dynamics by engaging mechanisms dependent on the kinetics of NMDA receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2402732121 | PMCID: PMC11145256 | PMID: 38768339
- Evidence: The model output was analyzed using Python 3.
- Full pipeline: stage not stated [Python]

### Foundations of reasoning with uncertainty via real-valued logics. (PNAS 2024)

- DOI: 10.1073/pnas.2309905121 | PMCID: PMC11126966 | PMID: 38753505
- Version used: **3.6**
- Evidence: We implemented the algorithm as a Python package named socratic, which requires Python 3.6 or newer and makes use of IBM ® ILOG ® CPLEX ® Optimization Studio V12.10.0 or newer via the docplex Python package.
- Full pipeline: stage not stated [Python v3.6]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Evidence: We used a custom pipeline and Python scripts ( 85 ) to combine these two data types.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### Robust inference of causality in high-dimensional dynamical processes from the Information Imbalance of distance ranks. (PNAS 2024)

- DOI: 10.1073/pnas.2317256121 | PMCID: PMC11087807 | PMID: 38687797
- Evidence: Statistical assessment on Imbalance Gain data was performed using SciPy ( 49 ) and statsmodels ( 51 ) packages in Python.
- Full pipeline: differential/statistical testing [Python, statsmodels] -> stage not stated [SciPy]

### Myospreader improves gene editing in skeletal muscle by myonuclear propagation. (PNAS 2024)

- DOI: 10.1073/pnas.2321438121 | PMCID: PMC11087771 | PMID: 38687782
- Evidence: All code is written in R and Python 3.
- Full pipeline: stage not stated [ImageJ, Python]

### Dissection and integration of bursty transcriptional dynamics for complex systems. (PNAS 2024)

- DOI: 10.1073/pnas.2306901121 | PMCID: PMC11067469 | PMID: 38669186
- Evidence: 1 ) in Python, accelerated via Numba ( 72 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Python, SciPy, scVelo]

### Maximum entropy determination of mammalian proteome dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2313107121 | PMCID: PMC11067036 | PMID: 38652742
- Evidence: Although our mathematical method is simple and rapid to implement (<1 wk) for researchers familiar with calculus and with coding in Python, we appreciate many cell biology labs will not have these personnel capabilities.
- Full pipeline: stage not stated [Python]

### Evolutionarily conserved neural responses to affective touch in monkeys transcend consciousness and change with age. (PNAS 2024)

- DOI: 10.1073/pnas.2322157121 | PMCID: PMC11067024 | PMID: 38648473
- Evidence: Stimulation speed was maintained according to visual cues (i.e., speed condition and time left in block) presented on a monitor at the edge of the scanner bore controlled by a custom Python script.
- Full pipeline: stage not stated [AFNI, CIVET, Python, R v4.3.1, emmeans, lme4]

### A generic approach to infer community-level fitness of microbial genes. (PNAS 2024)

- DOI: 10.1073/pnas.2318380121 | PMCID: PMC11047084 | PMID: 38635629
- Evidence: Strain-specific barcodes were counted using a custom Python script allowing up to two mismatched base pairs per barcode.
- Full pipeline: stage not stated [Python]

### Bmal1 integrates circadian function and temperature sensing in the suprachiasmatic nucleus. (PNAS 2024)

- DOI: 10.1073/pnas.2316646121 | PMCID: PMC11047078 | PMID: 38625943
- Evidence: Using custom Python script, the timeseries of each region of interest were normalized and a K-Means clustering algorithm was implemented using the K-Means algorithm from scikit-learn 1.2.2 ( 41 ) with k = 5 and the classical EM-style Lloyd algorithm.
- Full pipeline: normalisation [Python, scikit-learn v1.2.2] -> dimensionality reduction/clustering [Matplotlib, Python, SciPy, scikit-learn v1.2.2] -> differential/statistical testing [SciPy]

### Distinct lateral hypothalamic CaMKIIα neuronal populations regulate wakefulness and locomotor activity. (PNAS 2024)

- DOI: 10.1073/pnas.2316150121 | PMCID: PMC11032496 | PMID: 38593074
- Evidence: Locomotion was exported as a .csv file in 10 min bins and processed with custom scripts in Python.
- Full pipeline: stage not stated [Python]

### Brain activity of professional investors signals future stock performance. (PNAS 2024)

- DOI: 10.1073/pnas.2307982121 | PMCID: PMC11032448 | PMID: 38593084
- Evidence: Next, we used a custom Python script to extract activation estimates from predefined VOIs from the whole-brain β-maps.
- Full pipeline: stage not stated [Nipype, Python, fMRIPrep v20.2.0]

### Top-down modulation in canonical cortical circuits with short-term plasticity. (PNAS 2024)

- DOI: 10.1073/pnas.2311040121 | PMCID: PMC11032497 | PMID: 38593083
- Evidence: Simulations were performed in Python.
- Full pipeline: simulation/modelling [Python]

### Conformational changes in the Niemann-Pick type C1 protein NCR1 drive sterol translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2315575121 | PMCID: PMC11009665 | PMID: 38568972
- Evidence: Intensity line profiles of FM4-64 and ConA-Alexa 488 were measured using Macros in ImageJ and plotted in Python software using Matplotlib ( 42 ).
- Full pipeline: alignment/mapping [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, Matplotlib, Python]

### Genomes of historical specimens reveal multiple invasions of LTR retrotransposons in <i>Drosophila melanogaster</i> during the 19th century. (PNAS 2024)

- DOI: 10.1073/pnas.2313866121 | PMCID: PMC11009621 | PMID: 38564639
- Evidence: We merged fragmented matches using a Python script ( rm - d e f r a g m e n t e r . p y –dist 100) and visualized the joint distribution of the insert size and the divergence using hexagonal heatmaps [ggplot2 ( 74 )].
- Full pipeline: alignment/mapping [BEDTools, MUSCLE v3.8.1551] -> visualisation [Python, ggplot2] -> stage not stated [Cutadapt, RepeatMasker]

### Crystal size, shape, and conformational changes drive both the disappearance and reappearance of ritonavir polymorphs in the mill. (PNAS 2024)

- DOI: 10.1073/pnas.2319127121 | PMCID: PMC11009673 | PMID: 38557191
- Evidence: Particle energies were calculated using our Particle Energy Calculator (PEC) ( 37 ) code written in Python 3, which utilizes modules of the CSD Python API ( 38 ).
- Full pipeline: stage not stated [Python]

### Unraveling sources of emission heterogeneity in Silicon Vacancy color centers with cryo-cathodoluminescence microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2308247121 | PMCID: PMC10998621 | PMID: 38551833
- Evidence: Data analysis was performed in Python, utilizing multiple common packages, such as numpy, scipy, and matplotlib.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python, SciPy]

### Abundant resources can trigger reduced consumption: Unveiling the paradox of excessive scrounging. (PNAS 2024)

- DOI: 10.1073/pnas.2322955121 | PMCID: PMC10990140 | PMID: 38502696
- Evidence: All codes were implemented in Python.
- Full pipeline: stage not stated [Python]

### Unsupervised identification of significant lineages of SARS-CoV-2 through scalable machine learning methods. (PNAS 2024)

- DOI: 10.1073/pnas.2317284121 | PMCID: PMC10962941 | PMID: 38478692
- Version used: **3.10.0**
- Evidence: To characterize the sequences, we wrote code in Python v3.10.0.
- Full pipeline: alignment/mapping [MAFFT v7.453] -> dimensionality reduction/clustering [Pangolin, UMAP] -> stage not stated [Python v3.10.0]

### Network of epistatic interactions in an enzyme active site revealed by large-scale deep mutational scanning. (PNAS 2024)

- DOI: 10.1073/pnas.2313513121 | PMCID: PMC10962969 | PMID: 38483989
- Version used: **3.0**
- Evidence: Following deep sequencing, codon counts were determined using a custom Python 3.0 script.
- Full pipeline: stage not stated [Matplotlib, Python v3.0, seaborn]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Evidence: Statistical analyses were performed using the pingouin Python package ( 111 ).
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Diverging neural dynamics for syntactic structure building in naturalistic speaking and listening. (PNAS 2024)

- DOI: 10.1073/pnas.2310766121 | PMCID: PMC10945772 | PMID: 38442171
- Evidence: We used the Stanford parser with CoreNLP in Python 3 via the Natural Language Toolkit package ( 51 , 85 ).
- Full pipeline: differential/statistical testing [R v4.0.3, lme4] -> stage not stated [FreeSurfer, Nilearn, Python, TensorFlow, emmeans]

### RNA-catalyzed evolution of catalytic RNA. (PNAS 2024)

- DOI: 10.1073/pnas.2321592121 | PMCID: PMC10945747 | PMID: 38437533
- Evidence: Sequences of pre-cleaved and cleaved HHR+ RNAs were processed using a custom Python script to determine the frequency of each distinct sequence in each round of evolution ( SI Appendix , Methods ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2] -> visualisation [R] -> stage not stated [Python]

### Thiophene-based lipids for mRNA delivery to pulmonary and retinal tissues. (PNAS 2024)

- DOI: 10.1073/pnas.2307813120 | PMCID: PMC10945828 | PMID: 38437570
- Evidence: Python script used to interpret NGS data is available on GitHub ( https://github.com/antonyjozic/lnp_barcode_script ) ( 37 ). mRNA was sourced from TriLink Biotechnologies (San Diego, CA; substituted with 5-methoxy-U); the ORF sequences are available on the manufacturer's website ( 38 – 40 ).
- Full pipeline: stage not stated [Python]

### Data-driven classification of ligand unbinding pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2313542121 | PMCID: PMC10927508 | PMID: 38412121
- Evidence: The pairwise distance matrix is used to perform a k-medoids clustering of the trajectories using the FasterPAM ( 53 ) algorithm employed in the kmedoids package ( 54 ) in Python.
- Full pipeline: dimensionality reduction/clustering [Python] -> simulation/modelling [GROMACS v2021.5, PLUMED v2.9, Python]

### Spatially resolved land and grid model of carbon neutrality in China. (PNAS 2024)

- DOI: 10.1073/pnas.2306517121 | PMCID: PMC10927511 | PMID: 38408236
- Evidence: RESPO is implemented with the Gurobi optimizer in Python, requiring roughly 200 GB of memory to solve.
- Full pipeline: stage not stated [Python]

### Mechanism and cellular function of direct membrane binding by the ESCRT and ERES-associated Ca<sup>2+</sup>-sensor ALG-2. (PNAS 2024)

- DOI: 10.1073/pnas.2318046121 | PMCID: PMC10907313 | PMID: 38386713
- Evidence: Custom-made scripts were used to perform puncta recognition analysis in Python.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis v2.0] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, ImageJ, OpenCV, PyMOL, Python, scikit-image]

### Homologous mutations in human β, embryonic, and perinatal muscle myosins have divergent effects on molecular power generation. (PNAS 2024)

- DOI: 10.1073/pnas.2315472121 | PMCID: PMC10907259 | PMID: 38377203
- Evidence: Trajectory analysis was conducted in Python using the library MDTraj ( 89 ).
- Full pipeline: simulation/modelling [GROMACS v2022.4, MDTraj, Python] -> stage not stated [scikit-learn]

### The contribution of gene flow, selection, and genetic drift to five thousand years of human allele frequency change. (PNAS 2024)

- DOI: 10.1073/pnas.2312377121 | PMCID: PMC10907250 | PMID: 38363870
- Evidence: Results were recorded as tree sequences and analyzed in Python using tskit ( 56 ).
- Full pipeline: stage not stated [Python]

### Homophily, selection, and choice in segregation models. (PNAS 2024)

- DOI: 10.1073/pnas.2313752121 | PMCID: PMC10873625 | PMID: 38324571
- Evidence: The simulation of our model is programmed in Python using Mesa agent-based modeling framework ( https://github.com/projectmesa/mesa/ ).
- Full pipeline: simulation/modelling [Python]

### Genetic disruption of the bacterial <i>raiA</i> motif noncoding RNA causes defects in sporulation and aggregation. (PNAS 2024)

- DOI: 10.1073/pnas.2318008121 | PMCID: PMC10861870 | PMID: 38306478
- Evidence: Genes in the vicinity of the raiA motif were identified using a custom Python script implementing the Biopython package ( 69 ).
- Full pipeline: stage not stated [Python]

### CRISPR-based screening of small RNA modulators of bile susceptibility in <i>Bacteroides thetaiotaomicron</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2311323121 | PMCID: PMC10861873 | PMID: 38294941
- Evidence: Python scripts for PAM frequency determination and CRISPRi library design are deposited at https://github.com/gprezza/CRISPRi_tools .
- Full pipeline: quantification [edgeR v3.32.1] -> differential/statistical testing [edgeR v3.32.1] -> stage not stated [Python]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Evidence: Initially, paired-end sequencing reads were aligned to Arabidopsis TAIR10 reference genome ( 105 ) using Hisat2 (v2.1.0) ( 106 ) with the parameters “--min-intronlen 20 --max_intronlen 12000.” The reads aligned to rDNA, mitochondria and chloroplast genomes were excluded by a custom Python script “filter_rRNA_bam.py” ( 20 ).
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Structure and function of the hippocampal CA3 module. (PNAS 2024)

- DOI: 10.1073/pnas.2312281120 | PMCID: PMC10861929 | PMID: 38289953
- Evidence: Network simulations and analyses of the spiking network data were performed in Python ( www.python.org ), with the neural network being implemented with the package Brian ( 55 ).
- Full pipeline: simulation/modelling [Python] -> machine learning [Python]

### A disinhibitory circuit mechanism explains a general principle of peak performance during mid-level arousal. (PNAS 2024)

- DOI: 10.1073/pnas.2312898121 | PMCID: PMC10835062 | PMID: 38277436
- Version used: **2.7**
- Evidence: All tasks were programmed in Python 2.7 using PsychoPy ( 79 ) and in-house scripts.
- Full pipeline: stage not stated [PsychoPy, Python v2.7]

### Logic-based mechanistic machine learning on high-content images reveals how drugs differentially regulate cardiac fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2303513121 | PMCID: PMC10835125 | PMID: 38266046
- Version used: **3.8.5**
- Evidence: Automated data analysis and statistical calculations were performed using Python 3.8.5 and the “statsmodels” Python module version 0.13.2.
- Full pipeline: quantification [CellProfiler] -> differential/statistical testing [Python v3.8.5, statsmodels]

### Efficient mapping of the thalamocortical monosynaptic connectivity in vivo by tangential insertions of high-density electrodes in the cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2313048121 | PMCID: PMC10823237 | PMID: 38241439
- Evidence: Except for sorting with Kilosort ( 31 ) ( https://github.com/MouseLand/Kilosort ) which was done in MATLAB 2018 and 2019 ( www.mathworks.com ), all data analysis was performed in Python 3 ( www.anaconda.com ); statistical tests were performed using either the two-sided Wilcoxon rank-sum test except for the pharmacological recording where we use a two-sided Wilcoxon signed-rank test ( Fig.
- Full pipeline: quantification [SciPy] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [Kilosort, Python]

### High UV damage and low repair, but not cytosine deamination, stimulate mutation hotspots at ETS binding sites in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2310854121 | PMCID: PMC10823218 | PMID: 38241433
- Evidence: The intersection data were further processed with custom Python scripts to calculate average mutation density (i.e., number of mutations per tumor per gene at each position) for genes aligned by the TSS (e.g., Fig.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, Python] -> simulation/modelling [GROMACS, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [BEDTools, SAMtools]

### Development of prediction models to identify hotspots of schistosomiasis in endemic regions to guide mass drug administration. (PNAS 2024)

- DOI: 10.1073/pnas.2315463120 | PMCID: PMC10786280 | PMID: 38181058
- Version used: **3.9.7**
- Evidence: We implemented all models using the Scikit-learn Python package (version 1.1.1) and Python (version 3.9.7).
- Full pipeline: stage not stated [Python v3.9.7, XGBoost, scikit-learn]

### Sound propagation in realistic interactive 3D scenes with parameterized sources using deep neural operators. (PNAS 2024)

- DOI: 10.1073/pnas.2312159120 | PMCID: PMC10786273 | PMID: 38175862
- Version used: **3.10.7**
- Evidence: JAX 0.4.10 ( 38 ), Flax 0.6.10 ( 39 ) and Python 3.10.7 have been used for all experiments and the code is available here: https://github.com/dtu-act/deeponet-acoustic-wave-prop .
- Full pipeline: stage not stated [Python v3.10.7]

### eSoil: A low-power bioelectronic growth scaffold that enhances crop seedling growth. (PNAS 2024)

- DOI: 10.1073/pnas.2304135120 | PMCID: PMC10786271 | PMID: 38147542
- Evidence: Porosity analysis is performed in Python using the PoreSpy package ( 55 ).
- Full pipeline: stage not stated [ImageJ, Python]

### Social anxiety disorder-associated gut microbiota increases social fear. (PNAS 2024)

- DOI: 10.1073/pnas.2308706120 | PMCID: PMC10769841 | PMID: 38147649
- Evidence: Further statistical analysis was handled in R (v4.2.2) using the R Studio GUI (version 2022.7.2.576) and in Python with SciPy (v1.9.3).
- Full pipeline: differential/statistical testing [Python, SciPy v1.9.3, lme4] -> stage not stated [R v4.2.2, ggplot2]

### A myosin hypertrophic cardiomyopathy mutation disrupts the super-relaxed state and boosts contractility by enhanced actin attachment. (PNAS 2025)

- DOI: 10.1073/pnas.2521561122 | PMCID: PMC12772213 | PMID: 41439707
- Evidence: Stopped-flow data were fitted by single exponentials and rates were fitted where appropriate by the Michaelis–Menten equation using custom Python scripts.
- Full pipeline: stage not stated [ImageJ, Python]

### Competition between glycine and GABA&lt;sub&gt;A&lt;/sub&gt; receptors for gephyrin controls their equilibrium populations at inhibitory synapses. (PNAS 2025)

- DOI: 10.1073/pnas.2500226122 | PMCID: PMC12771574 | PMID: 41433069
- Evidence: Spatiotemporal analysis of mEos4b-GlyRβ diffusion was done with the Python script TRamWAy ( 27 ).
- Full pipeline: stage not stated [Python]

### A neuromorphic robotic electronic skin with active pain and injury perception. (PNAS 2025)

- DOI: 10.1073/pnas.2520922122 | PMCID: PMC12772184 | PMID: 41428887
- Evidence: Pulse processing is managed by a custom Python 3 program that continuously monitors the incoming data.
- Full pipeline: stage not stated [Python]

### Contrastive independent component analysis for salient patterns and dimensionality reduction. (PNAS 2025)

- DOI: 10.1073/pnas.2425119122 | PMCID: PMC12718309 | PMID: 41370342
- Evidence: The synthetic datasets were generated in Python to model mixtures of statistically independent sources.
- Full pipeline: differential/statistical testing [Python]

### An electron transport complex required in the gut sensitizes &lt;i&gt;Bacteroides&lt;/i&gt; to a pore-forming type VI secretion toxin. (PNAS 2025)

- DOI: 10.1073/pnas.2523503122 | PMCID: PMC12718326 | PMID: 41364769
- Evidence: Illumina sequencing reads were analyzed using a custom Python script and the Fitness Browser resources ( https://morgannprice.org/FEBA/Btheta/ ).
- Full pipeline: alignment/mapping [ChimeraX v10.1] -> dimensionality reduction/clustering [ChimeraX v10.1] -> stage not stated [AlphaFold, Python]

### HLA-DQB1*03:01 strongly affects age of onset of type 1 narcolepsy independently of DQA1 and ethnicity. (PNAS 2025)

- DOI: 10.1073/pnas.2513989122 | PMCID: PMC12718323 | PMID: 41364757
- Evidence: Next, we built 2 × 2 contingency tables for each segment (i.e., TRAV4 and non-TRAV4 counts in DQB1*0301-positive and negative) and used the chi2_contingency function from scipy.stats in Python to compare groups.
- Full pipeline: stage not stated [Python, SciPy]

### Multiple weak brakes act in concert to control STIM1 and store-operated calcium entry. (PNAS 2025)

- DOI: 10.1073/pnas.2518622122 | PMCID: PMC12718381 | PMID: 41359834
- Evidence: Data were analyzed using custom Python scripts as detailed previously ( 30 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, ImageJ, Python]

### Carbonate burial regimes, the Meso-Cenozoic climate, and nannoplankton expansion. (PNAS 2025)

- DOI: 10.1073/pnas.2516468122 | PMCID: PMC12704742 | PMID: 41343679
- Evidence: R and Python scripts as well as the Jupyter notebooks used in our pre- and postprocessing workflows are available from the following GitHub link: https://github.com/Geodels/paleoReef .
- Full pipeline: stage not stated [Jupyter, Python]

### Warming from cold pools: A pathway for mesoscale organization to alter Earth's radiation budget. (PNAS 2025)

- DOI: 10.1073/pnas.2513699122 | PMCID: PMC12704769 | PMID: 41325531
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Original data created for this study, including atmospheric simulation outputs and the Python scripts to reproduce figure results, are available in a persistent repository (Zenodo) at https://doi.org/10.5281/zenodo.15544026 ( 79 ).
- Full pipeline: simulation/modelling [Python]

### Uncovering heterogeneous intercommunity disease transmission from neutral allele frequency time series. (PNAS 2025)

- DOI: 10.1073/pnas.2500663122 | PMCID: PMC12684928 | PMID: 41296719
- Evidence: Data, Materials, and Software Availability Some study data are available (The Python scripts for the HMM-EM method and the C++ code for the HMM-MCMC method, along with the Python scripts to reproduce the figures in this manuscript, are available at https://github.com/Hallatscheklab/NetworkInfer ( 52 ).
- Full pipeline: stage not stated [Python]

### Native metabolomics identifies pteridines as CutA ligands and modulators of copper binding. (PNAS 2025)

- DOI: 10.1073/pnas.2509468122 | PMCID: PMC12685090 | PMID: 41289401
- Evidence: Dose–response data were analyzed with MO.Affinity Analysis Software v2.3 (NanoTemper) and further fitted using a custom Python script applying nonlinear regression with a one_site_binding model.
- Full pipeline: differential/statistical testing [Cytoscape, Python] -> visualisation [ChimeraX, Cytoscape]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Version used: **3.7.3**
- Evidence: Data exploration, transformation, visualization, and analysis were conducted using Jupyter Lab (version 0.35.4; https://jupyter.org/ ) with Python 3.7.3, running via Anaconda Distribution 4.6.14 ( https://www.anaconda.com ).
- Full pipeline: quantification [CellProfiler] -> visualisation [Conda, Jupyter, Python v3.7.3] -> stage not stated [ImageJ, Matplotlib v3.0.3, NumPy v1.16.3, SciPy v1.2.1, seaborn v0.9.0]

### Engineered calcium-regulated affinity protein for efficient internalization and lysosomal toxin delivery. (PNAS 2025)

- DOI: 10.1073/pnas.2509081122 | PMCID: PMC12685030 | PMID: 41289384
- Evidence: Image processing was performed in Fiji for background subtraction and in Python (OpenCV, SciPy, NumPy, scikit-image) for analysis.
- Full pipeline: structure determination [ChimeraX v1.9, PHENIX v1.21.2] -> visualisation [ChimeraX v1.9, PHENIX v1.21.2] -> stage not stated [AlphaFold, NumPy, OpenCV, Python, SciPy, scikit-image]

### Light-field deep learning enables high-throughput, scattering-mitigated calcium imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2510337122 | PMCID: PMC12685042 | PMID: 41289378
- Evidence: The PMT was powered by a programmable DC power supply (Radiospares, RSPD3303C) controlled by a custom graphical user interface GUI written in Python 3.
- Full pipeline: visualisation [napari] -> stage not stated [PyTorch, Python]

### Dimeric gold nanoparticles enable multiplexed labeling in cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2524034122 | PMCID: PMC12685141 | PMID: 41284882
- Evidence: Radial profiles and center-to-center distances were computed with custom Python scripts.
- Full pipeline: structure determination [AlphaFold, IMOD] -> stage not stated [Python]

### The molecular-level diagenetic clock of sinking marine organic matter. (PNAS 2025)

- DOI: 10.1073/pnas.2504769122 | PMCID: PMC12685107 | PMID: 41284868
- Evidence: All statistical analysis was conducted using the Spyder environment hosted in Python ( 103 ).
- Full pipeline: differential/statistical testing [Python] -> stage not stated [SciPy]

### How social learning enhances-or undermines-efficiency and flexibility in collective decision-making under uncertainty. (PNAS 2025)

- DOI: 10.1073/pnas.2516827122 | PMCID: PMC12685029 | PMID: 41284859
- Version used: **3.12.4**
- Evidence: All the simulations and visualization are implemented in Python (v3.12.4).
- Full pipeline: simulation/modelling [Python v3.12.4] -> visualisation [Python v3.12.4]

### High-throughput screening for class I peptide MHC binding via yeast surface display. (PNAS 2025)

- DOI: 10.1073/pnas.2514741122 | PMCID: PMC12663924 | PMID: 41264236
- Version used: **3.7**
- Evidence: Analyses were all performed in Python 3.7, and figures were generated using matplotlib ( 51 ) and seaborn ( 52 ) packages.
- Full pipeline: visualisation [Matplotlib, Python v3.7, seaborn]

### The potential existential threat of large language models to online survey research. (PNAS 2025)

- DOI: 10.1073/pnas.2518075122 | PMCID: PMC12663962 | PMID: 41264250
- Evidence: This study utilized an autonomous synthetic respondent built in Python.
- Full pipeline: stage not stated [Python]

### Advancing stochastic 3-SAT solvers by dissipating oversatisfied constraints. (PNAS 2025)

- DOI: 10.1073/pnas.2517297122 | PMCID: PMC12646238 | PMID: 41237207
- Evidence: Materials and Methods Solver methods are described in the main text and algorithms for numerical benchmarks are implemented in Python and C without any nonstandard libraries.
- Full pipeline: stage not stated [Python]

### GH25 lysozyme mediates tripartite interkingdom interactions and microbial competition on the plant leaf surface. (PNAS 2025)

- DOI: 10.1073/pnas.2510124122 | PMCID: PMC12626018 | PMID: 41201826
- Evidence: Di-Codon Optimization of R. solani GH25 was performed using Python 3.x (Python Software Foundation, 2023).
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [AlphaFold] -> stage not stated [ImageJ v1.53K, Python]

### Chemical propulsion of hemozoin crystal motion in malaria parasites. (PNAS 2025)

- DOI: 10.1073/pnas.2513845122 | PMCID: PMC12595501 | PMID: 41150719
- Evidence: We used scipy.optimize.curve_fit function in Python to empirically fit our data ( 66 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Python, SciPy, TrackMate]

### A new late Neanderthal from Crimea reveals long-distance connections across Eurasia. (PNAS 2025)

- DOI: 10.1073/pnas.2518974122 | PMCID: PMC12625898 | PMID: 41144685
- Evidence: Pairwise nucleotide differences between Star 1 and other genomes in the alignment were calculated using a custom Python script available on the GitHub page of the project.
- Full pipeline: alignment/mapping [ANGSD, Python] -> stage not stated [GATK, SAMtools v1.20]

### Transcriptional condensates encode a "golden mean" to optimize enhancer-promoter communication across genomic distances. (PNAS 2025)

- DOI: 10.1073/pnas.2513371122 | PMCID: PMC12582294 | PMID: 41134621
- Evidence: It includes the following components: 1) simulation files: Gromacs input files for running the chromatin polymer model simulations; 2) analysis tools: Python scripts for downstream analysis of simulation output files, including calculations of TF clustering, MFPT, and landscape.
- Full pipeline: dimensionality reduction/clustering [Python] -> simulation/modelling [GROMACS v4.5.7, PLUMED, Python]

### On the scale of heterogeneity in composite electrodes of batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2520136122 | PMCID: PMC12582338 | PMID: 41129219
- Evidence: These data are fed into a Pandas DataFrame in Python.
- Full pipeline: alignment/mapping [scikit-image] -> dimensionality reduction/clustering [SciPy] -> structure determination [scikit-image] -> visualisation [Matplotlib, NumPy] -> stage not stated [OpenCV, Python]

### Descattering and image restoration with a transformer-based neural network in deep tissue imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2503576122 | PMCID: PMC12582269 | PMID: 41118214
- Evidence: The code for calculating these metrics is written in Python.
- Full pipeline: stage not stated [PyTorch, Python]

### Foot placement control underlies stable locomotion across species. (PNAS 2025)

- DOI: 10.1073/pnas.2413958122 | PMCID: PMC12582247 | PMID: 41118219
- Evidence: We used the function scipy.stats.linregress in Python to fit these regressions and kept track of the individual slopes and p values associated with each of them.
- Full pipeline: differential/statistical testing [NumPy, Python, SciPy]

### From retinotopic to ordinal coding: Dissecting the cortical stages of visual word recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2507291122 | PMCID: PMC12582272 | PMID: 41118216
- Evidence: Specifically, logistic regression with a “liblinear” solver was performed after scaling the data using “robustscalar” from the sci-kit learn package in Python.
- Full pipeline: normalisation [Python] -> differential/statistical testing [Python] -> stage not stated [FSL, MNE-Python, PyTorch, SPM]

### Temporal and spatial coordination of DNA segregation and cell division in an archaeon. (PNAS 2025)

- DOI: 10.1073/pnas.2513939122 | PMCID: PMC12557731 | PMID: 41091768
- Evidence: Each cropped sequence was subsequently processed via a custom Python script to segment cellular and DNA components, quantify apparent motion, and visualize the results.
- Full pipeline: quantification [Python] -> visualisation [Python] -> stage not stated [Cellpose, ImageJ, scikit-image]

### &lt;i&gt;WUSCHEL-D1&lt;/i&gt; upregulation enhances grain number by inducing formation of multiovary-producing florets in wheat. (PNAS 2025)

- DOI: 10.1073/pnas.2510889122 | PMCID: PMC12557809 | PMID: 41086219
- Evidence: Custom Python scripts and Fiji macros were used to perform cell segmentation of confocal image stacks, measure inflorescence meristem areas, and define the position of cells within the shoot meristem ( 82 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [minimap2] -> stage not stated [BUSCO, Python, hifiasm]

### Adaptable microplastic classification using similarity learning on µFTIR spectra collected from µFTIR focal plane array imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2509745122 | PMCID: PMC12557549 | PMID: 41086209
- Evidence: The similarity and CNN models used in this study were constructed in Python using a combination of Tensorflow (v 2.10.1) and the Tensorflow Similarity package (v 0.17.1).
- Full pipeline: stage not stated [Python, TensorFlow v2.10.1, scikit-learn v1.3.2]

### Dynamic sensor selection for biomarker discovery. (PNAS 2025)

- DOI: 10.1073/pnas.2501324122 | PMCID: PMC12541339 | PMID: 41055977
- Evidence: All experiments were performed and analyzed in Python or MATLAB: https://github.com/Jpickard1/dynamic-sensor-selection-for-biomarker-discovery .
- Full pipeline: stage not stated [NumPy, Python]

### Mineral dissolution by dimeric complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2504109122 | PMCID: PMC12541406 | PMID: 41052339
- Evidence: The Jupyter Notebook Python script of a U-Net training example can be found on GitHub: https://uofi.box.com/s/k45wffrq3xf04taa7yeir19cqijyt7of ( 84 ).
- Full pipeline: simulation/modelling [PLUMED] -> machine learning [Jupyter, Keras, Python, TensorFlow] -> stage not stated [ImageJ]

### Generalized convolutional many-body distribution functional representations. (PNAS 2025)

- DOI: 10.1073/pnas.2415662122 | PMCID: PMC12541311 | PMID: 41052323
- Evidence: Furthermore, our cMBDF code is currently implemented entirely in Python , whereas SLATM, FCHL19, and SOAP are generated using Python libraries that leverage lower-level programming languages ( Fortran , C ) for the computations and looping (see Data and Code for details).
- Full pipeline: stage not stated [NumPy, PySCF, Python, SciPy, XGBoost]

### Manifold-constrained nucleus-level denoising diffusion model for structure-based drug design. (PNAS 2025)

- DOI: 10.1073/pnas.2415666122 | PMCID: PMC12541315 | PMID: 41052340
- Version used: **3.8.13**
- Evidence: All algorithms and models have been developed using Python 3.8.13, with PyTorch version 1.12.1 and PyTorch Geometric version 2.5.2, under CUDA 11.0.
- Full pipeline: simulation/modelling [AutoDock Vina] -> stage not stated [PyTorch v1.12.1, Python v3.8.13]

### A TGF-βR/IL-2R immunomodulatory fusion protein transforms immunosuppression into T cell activation to enhance adoptive T cell therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2516951122 | PMCID: PMC12501114 | PMID: 40986340
- Evidence: Aligned single cell read data were further processed using custom code based around the Scanpy package ( 59 ) in Python 3.
- Full pipeline: alignment/mapping [Python, Scanpy] -> stage not stated [GSEA v4.1.0, scDblFinder]

### Emergence of activation or repression in transcriptional control under a fixed molecular context. (PNAS 2025)

- DOI: 10.1073/pnas.2413715122 | PMCID: PMC12501156 | PMID: 40982681
- Evidence: The steady state probability of vertex i is then calculated as [9] P i ∗ = μ i Σ i μ i These calculations are done in Python.
- Full pipeline: stage not stated [Python]

### An open-source photobleacher for fluorescence imaging of large pigment-rich tissues. (PNAS 2025)

- DOI: 10.1073/pnas.2426628122 | PMCID: PMC12478079 | PMID: 40961137
- Version used: **3.9**
- Evidence: Statistical analyses were performed using SciPy with Python 3.9.
- Full pipeline: differential/statistical testing [Python v3.9, SciPy]

### Φ value analysis underscores strong functional and structural compactness of the GABA&lt;sub&gt;A&lt;/sub&gt; receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2512278122 | PMCID: PMC12478134 | PMID: 40956892
- Evidence: Calculations were done using Python scripts ( 61 ).
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> visualisation [ChimeraX] -> stage not stated [Python]

### Heterogeneity in the coordination of delta cells with beta cells is driven by both paracrine signals and low-density Cx36 gap junctions. (PNAS 2025)

- DOI: 10.1073/pnas.2504151122 | PMCID: PMC12478151 | PMID: 40956879
- Evidence: A detailed description of the custom Python script used to filter the slow and fast components of each Ca 2+ trace is available in the extended materials and methods section.
- Full pipeline: machine learning [Cellpose v3.1.1.1] -> stage not stated [Python]

### Dynamic and precise electromagnetic levitation of single cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512246122 | PMCID: PMC12452889 | PMID: 40920932
- Evidence: To model the magnetic field generated by the two permanent magnets and two electromagnets, we used the “Magpylib” library in Python.
- Full pipeline: stage not stated [MACS2, Python]

### Topology and kinetic pathways of colloidosome assembly and disassembly. (PNAS 2025)

- DOI: 10.1073/pnas.2427024122 | PMCID: PMC12435265 | PMID: 40906801
- Evidence: We then fit each ridge detection image in the z-scan with a circle fit using a RANSAC algorithm in Python.
- Full pipeline: stage not stated [Python]

### Inverse stable isotope probing-metabolomics (InverSIP) identifies an iron acquisition system in a methane-oxidizing bacterial community. (PNAS 2025)

- DOI: 10.1073/pnas.2507323122 | PMCID: PMC12435222 | PMID: 40901884
- Evidence: Next, the aligned feature table was processed along with the .h5 files for each condition using the InverSIL custom Python script (available at https://github.com/purilab/inverse ).
- Full pipeline: read trimming [SPAdes v4.0.0, Trimmomatic] -> alignment/mapping [Python]

### Magnetic decoupling as a proofreading strategy for high-yield, time-efficient microscale self-assembly. (PNAS 2025)

- DOI: 10.1073/pnas.2502361122 | PMCID: PMC12415251 | PMID: 40875809
- Evidence: A custom Python script captured time-stamped recordings, such that the magnetic field and particle dynamics could be synchronized.
- Full pipeline: stage not stated [Python]

### CRISPR with Transcriptional Readout reveals influenza transcription is modulated by NELF and can precipitate an interferon response. (PNAS 2025)

- DOI: 10.1073/pnas.2515564122 | PMCID: PMC12415228 | PMID: 40864651
- Evidence: Data for nondebris events were analyzed using custom Python scripts, which can be found at https://github.com/Russell-laboratory/CRITRseq_Interferon_Flu .
- Full pipeline: stage not stated [GSEA, Python]

### Tunable effective diffusion of CO&lt;sub&gt;2&lt;/sub&gt; in aqueous foam. (PNAS 2025)

- DOI: 10.1073/pnas.2504617122 | PMCID: PMC12415188 | PMID: 40857309
- Evidence: Data, Materials, and Software Availability Images and Python scripts for data analysis have been deposited in Zenodo ( https://zenodo.org/records/16534916 ) ( 55 ).
- Full pipeline: stage not stated [Python]

### Efficiently quantifying dependence in massive scientific datasets using InterDependence Scores. (PNAS 2025)

- DOI: 10.1073/pnas.2509860122 | PMCID: PMC12403096 | PMID: 40833404
- Evidence: Here, we implemented IDS ∞ in Python with finite-dimensional feature maps approximating the Gaussian kernel with bandwidth parameter B = 1 by using the first k = 6 terms of the Taylor series expansion.
- Full pipeline: dimensionality reduction/clustering [Python, UMAP] -> visualisation [UMAP]

### Efficient neural encoding as revealed by bilingualism. (PNAS 2025)

- DOI: 10.1073/pnas.2513768122 | PMCID: PMC12403110 | PMID: 40828024
- Evidence: We trained a neural network for speech recognition in a supervised manner, implemented in Python with the PyTorch package ( 58 ).
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [PyTorch, Python, scikit-learn]

### Warming climate and water withdrawals threaten river flow connectivity in China. (PNAS 2025)

- DOI: 10.1073/pnas.2421046122 | PMCID: PMC12403000 | PMID: 40825132
- Evidence: The SciPy library in Python was used to implement the t -test based on the t -distribution for CI and P -values.
- Full pipeline: stage not stated [Python, SciPy]

### Layer 1 NDNF interneurons form distinct subpopulations with opposite activation patterns during sleep in freely behaving mice. (PNAS 2025)

- DOI: 10.1073/pnas.2503139122 | PMCID: PMC12377762 | PMID: 40811472
- Evidence: All analyses were performed using custom-made Python scripts ( https://github.com/AurelieBre/L1NDNFsubpop_PNAS2025 ) ( 48 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [lme4] -> visualisation [ImageJ] -> stage not stated [Python]

### Ludwig-Soret microscopy with the vibrational photothermal effect. (PNAS 2025)

- DOI: 10.1073/pnas.2510703122 | PMCID: PMC12377731 | PMID: 40811468
- Evidence: A numerical program, implemented in Python with GPU acceleration, was developed based on the Forward Time Centered Space method.
- Full pipeline: stage not stated [Python]

### Analytical solutions for light propagation of LED. (PNAS 2025)

- DOI: 10.1073/pnas.2508163122 | PMCID: PMC12377766 | PMID: 40802683
- Evidence: Offline analysis is conducted in Python.
- Full pipeline: stage not stated [Python]

### Familial transmission of neural representations for mental arithmetic across two generations. (PNAS 2025)

- DOI: 10.1073/pnas.2421528122 | PMCID: PMC12377651 | PMID: 40789033
- Evidence: First-level individual analysis of fMRI data was performed using the Nilearn package in Python ( 104 ).
- Full pipeline: quality control [MRIQC v0.15.1] -> normalisation [ANTs] -> registration [FSL] -> stage not stated [AFNI, FreeSurfer, Nilearn, PsychoPy, Python, fMRIPrep v20.2.5]

### &lt;i&gt;Sox11&lt;/i&gt; genes affect neuronal differentiation in the developing zebrafish enteric nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2510548122 | PMCID: PMC12342651 | PMID: 40789027
- Evidence: The analysis was accomplished in Python with the help of ChatGPT 3.0.
- Full pipeline: alignment/mapping [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Python, Scanpy]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Evidence: Python scripts were developed to calculate the number of duplications for each Arabidopsis gene within syntenic block regions, as well as the number of syntenic blocks containing each deleted syntenic gene ( Dataset S1 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### Immiscible proteins compete for RNA binding to order condensate layers. (PNAS 2025)

- DOI: 10.1073/pnas.2504778122 | PMCID: PMC12338069 | PMID: 40768359
- Evidence: Sequence logos for each PWM were created using the logomaker package in Python.
- Full pipeline: stage not stated [ImageJ, Python, SciPy, scikit-image v0.25.0]

### Anisotropic stretch biases the self-organization of actin fibers in multicellular Hydra aggregates. (PNAS 2025)

- DOI: 10.1073/pnas.2423437122 | PMCID: PMC12358849 | PMID: 40758890
- Evidence: Starting with the ImageJ plugin OrientationJ ( 55 ), a custom image analysis pipeline in Python was created to measure the nematic and smectic order parameters and the characteristic length.
- Full pipeline: normalisation [SciPy] -> stage not stated [ImageJ, Python]

### Generation of actionable, cancer-specific neoantigens from KRAS(G12C) with adagrasib. (PNAS 2025)

- DOI: 10.1073/pnas.2509012122 | PMCID: PMC12337345 | PMID: 40737322
- Evidence: After amplification, scFv genes were sequenced on a MiSeq sequencer (Illumina), and the data were analyzed using a set of in-house developed Python scripts ( 8 ) to deduce the frequency of occurrence of each mutation in the binders and nonbinder samples.
- Full pipeline: structure determination [UCSF Chimera] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.5, PHENIX v1.18.2, Python]

### Surface delivery quantification reveals distinct trafficking efficiencies among clustered protocadherin isoforms. (PNAS 2025)

- DOI: 10.1073/pnas.2514178122 | PMCID: PMC12337331 | PMID: 40737325
- Evidence: The subsequent alignment manipulations were performed in Python 3 using bioviper v.0.20 ( 67 ).
- Full pipeline: alignment/mapping [MUSCLE v5.1, Python, SciPy v1.11.4] -> stage not stated [AlphaFold, seaborn v0.13.0]

### PyReconstruct: A fully open-source, collaborative successor to Reconstruct. (PNAS 2025)

- DOI: 10.1073/pnas.2505822122 | PMCID: PMC12337286 | PMID: 40737319
- Evidence: The meshing strategies employed natively in PyReconstruct are modularized, such that users proficient in Python can implement more complex meshing algorithms accessible from the user interface should they choose to do so.
- Full pipeline: quantification [NumPy] -> structure determination [Python] -> visualisation [NumPy]

### Leveraging chromatin packing domains to target chemoevasion in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2425319122 | PMCID: PMC12318189 | PMID: 40694328
- Evidence: All statistical analyses were performed in Python with a Welch’s t test employed for pairwise comparisons between a reference condition and other conditions across groups, including assessments of D n , cell viability, and PDX tumor volumes.
- Full pipeline: differential/statistical testing [Python]

### Mutualisms within light microhabitats are associated with sensory convergence in a mimetic butterfly community. (PNAS 2025)

- DOI: 10.1073/pnas.2422397122 | PMCID: PMC12305024 | PMID: 40663600
- Evidence: OSpRad comes with a custom-built app written in Python and was run via the Pydroid 3 app installed onto a CUBOT Quest Lite smartphone (Android 9.0).
- Full pipeline: stage not stated [ImageJ, Python, R, lme4, phytools]

### A genetically defined pontine nucleus essential for ingestion in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2411174122 | PMCID: PMC12305073 | PMID: 40663610
- Evidence: Depending on the outcome of the normality test, either a paired-samples t test or a Wilcoxon signed-rank test was performed, as appropriate, using the scipy.stats library in Python.
- Full pipeline: differential/statistical testing [NumPy] -> machine learning [DeepLabCut v2.3.8] -> stage not stated [Fiji, ImageJ, Python, SciPy]

### Electrokinetic propulsion for electronically integrated microscopic robots. (PNAS 2025)

- DOI: 10.1073/pnas.2500526122 | PMCID: PMC12305017 | PMID: 40663604
- Evidence: Images from a USB camera (Basler Ace2 USB Camera) are sent to a Python script where robot positions and engine locations are determined by using adaptive thresholding in OpenCV ( 52 ) to extract contours.
- Full pipeline: stage not stated [ImageJ, OpenCV, Python]

### A quantitative imaging framework for lithium morphology: Linking deposition uniformity to cycle stability in lithium metal batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2502518122 | PMCID: PMC12305041 | PMID: 40663608
- Evidence: Images were binarized in Python using OpenCV’s cv2.THRESH_BINARY method by retaining a fixed percentage of the brightest pixels in each image to account for contrast variations.
- Full pipeline: stage not stated [OpenCV, Python]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Evidence: Using linear modeling and principal component analysis in Python programming, action potential spikes were identified and extracted.
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### HIF1α mediates circadian regulation of skeletal muscle metabolism and substrate preference in response to time-of-day exercise. (PNAS 2025)

- DOI: 10.1073/pnas.2504080122 | PMCID: PMC12280960 | PMID: 40627397
- Evidence: The data were corrected for natural abundance of carbon 13 using IsoCor and processed and analyzed using custom Python scripts ( 42 ).
- Full pipeline: alignment/mapping [STAR, featureCounts] -> quantification [Python] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [emmeans]

### Adaptive arousal regulation: Pharmacologically shifting the peak of the Yerkes-Dodson curve by catecholaminergic enhancement of arousal. (PNAS 2025)

- DOI: 10.1073/pnas.2419733122 | PMCID: PMC12280923 | PMID: 40623185
- Version used: **2.7**
- Evidence: All tasks were programmed in Python 2.7 using PsychoPy ( 80 ) and in-house scripts.
- Full pipeline: stage not stated [PsychoPy, Python v2.7]

### PLAA/UFD-3 regulates P-bodies through its intrinsic disordered domain. (PNAS 2025)

- DOI: 10.1073/pnas.2427250122 | PMCID: PMC12232612 | PMID: 40560612
- Evidence: DCAP-1 fluorescence in the head region was analyzed using a custom Python script, that automatically selected a 100 × 50 pixel 2 region of interest (ROI) centered around the region of maximum average fluorescence intensity in the head and calculated the average intensity in the ROI.
- Full pipeline: normalisation [limma] -> stage not stated [Python, R v4.2.2]

### Representation of locomotive action affordances in human behavior, brains, and deep neural networks. (PNAS 2025)

- DOI: 10.1073/pnas.2414005122 | PMCID: PMC12184334 | PMID: 40504155
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Anonymized behavioral data, fMRI data, and feature activations of neural networks data, as well as a code repository containing Python scripts to perform preprocessing and analysis to reproduce the results, have been deposited in Locomotive action affordances in brains, behavior and DNNs ( https://osf.io/v3rcq/ ) (...
- Full pipeline: machine learning [Python]

### Controlling DNA-RNA strand displacement kinetics with base distribution. (PNAS 2025)

- DOI: 10.1073/pnas.2416988122 | PMCID: PMC12167940 | PMID: 40478881
- Evidence: During single-cuvette measurements large intensity fluctuations at around t 0 , caused by the insertion of the pipette tip into the cuvette, were removed from the raw data using the Hampel filter in Python3.
- Full pipeline: stage not stated [Python, SciPy]

### Increased excitatory synapse size in hippocampal place cells compared to silent cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505322122 | PMCID: PMC12167973 | PMID: 40472030
- Evidence: The Suite2p output files were further analyzed by custom-made Python scripts.
- Full pipeline: registration [Suite2p] -> stage not stated [Cellpose, ImageJ, Python, SciPy]

### Assembly of a functional neuronal circuit in embryos of an ancestral metazoan is influenced by temperature and the microbiome. (PNAS 2025)

- DOI: 10.1073/pnas.2501225122 | PMCID: PMC12168009 | PMID: 40472034
- Evidence: The used codes and scripts to reproduce the main experiments of this study implemented in Python, Matlab, and R are available at GitHub ( https://github.com/ChNoack-Ki/Hydra-Embryos ) ( 73 ).
- Full pipeline: stage not stated [Python]

### High-throughput metabolic engineering of &lt;i&gt;Yarrowia lipolytica&lt;/i&gt; through gene expression tuning. (PNAS 2025)

- DOI: 10.1073/pnas.2426686122 | PMCID: PMC12168020 | PMID: 40460129
- Evidence: These arms, generated via a custom Python script, exclude the SapI restriction site.
- Full pipeline: alignment/mapping [minimap2] -> quantification [SAMtools] -> stage not stated [Python]

### Detection of the knee point in lithium-ion battery degradation using a state-of-charge-dependent parameter. (PNAS 2025)

- DOI: 10.1073/pnas.2424838122 | PMCID: PMC12167950 | PMID: 40460124
- Evidence: Data processing and machine-learning-based model construction were performed in Python with the Pandas, NumPy, and Scikit-learn packages.
- Full pipeline: stage not stated [NumPy, Python, scikit-learn]

### MyD88 knockdown by RNAi prevents bacterial stimulation of tubeworm metamorphosis. (PNAS 2025)

- DOI: 10.1073/pnas.2505805122 | PMCID: PMC12167997 | PMID: 40455987
- Evidence: RUNX , IL17, Fos, and NHR2 probes were designed in Python using in situ probe generator v.0.3.2 ( 71 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Python]

### Genomic analyses identify 15 risk loci and reveal &lt;i&gt;HDAC2&lt;/i&gt;, &lt;i&gt;SOX2-OT&lt;/i&gt;, and &lt;i&gt;IGF2BP2&lt;/i&gt; in a naturally occurring canine model of gastric cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2416723122 | PMCID: PMC12146739 | PMID: 40445765
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Python scripts are available on GitHub ( https://github.com/JessicaHayward/imputation_accuracy_GC ) ( 141 ).
- Full pipeline: stage not stated [GEMMA, Python]

### Environmental DNA adsorption to chitin can promote horizontal gene transfer by natural transformation. (PNAS 2025)

- DOI: 10.1073/pnas.2420708122 | PMCID: PMC12146716 | PMID: 40445756
- Evidence: Further data analysis, statistical tests, and figure generation were performed in Python.
- Full pipeline: differential/statistical testing [Python]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Version used: **3.9**
- Evidence: All postprocessing calculations and data analyses were done with GROMACS internal tools, Python 3.9 ( 95 ), Numpy v1.26 ( 96 ), and SciPy v1.11 ( 97 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: Ka/Ks (nonsynonymous/synonymous substitution) ratio was calculated, and the genes under positive selection were identified using a Python script.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### Physical activity stimulates clock neurons of the day-active rodent &lt;i&gt;Arvicanthis ansorgei&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2424545122 | PMCID: PMC12130842 | PMID: 40388616
- Version used: **3.0.9**
- Evidence: Data from the in vivo electrophysiology experiments were analyzed using Python 3.0.9 with the Pandas module version 1.3.0 and visualized using Matplotlib version 3.4.2 or RStudio version 1.4.1103.
- Full pipeline: visualisation [Matplotlib v3.4.2, Python v3.0.9] -> stage not stated [SciPy v1.7.0]

### Visualization and quantification of local concentration gradients in evaporating water/glycerol droplets with micrometer resolution. (PNAS 2025)

- DOI: 10.1073/pnas.2423660122 | PMCID: PMC12107088 | PMID: 40366690
- Evidence: Ray tracing was performed via a custom Python script.
- Full pipeline: stage not stated [Python]

### Real-world implementation of a noninvasive, AI-augmented, anemia-screening smartphone app and personalization for hemoglobin level self-monitoring. (PNAS 2025)

- DOI: 10.1073/pnas.2424677122 | PMCID: PMC12107174 | PMID: 40359048
- Evidence: All phase 1 data were imported from the RDS database into a pandas DataFrame in Python to enable the calculation of each participant’s personal correction factor parameter.
- Full pipeline: stage not stated [Python]

### Transition ability to safe states reduces fear responses to height. (PNAS 2025)

- DOI: 10.1073/pnas.2416920122 | PMCID: PMC12107115 | PMID: 40359043
- Evidence: We used the statsmodels 0.11.1 package in Python to assess the statistical significance of differences and set the significance level at P < 0.05.
- Full pipeline: differential/statistical testing [Python, statsmodels v0.11.1]

### Identifying intermolecular interactions in single-molecule localization microscopy. (PNAS 2025)

- DOI: 10.1073/pnas.2409426122 | PMCID: PMC12107154 | PMID: 40354526
- Evidence: Implementation of iMEC. iMEC was implemented in Python.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> stage not stated [NetworkX, Python]

### Antigen mobility regulates the dynamics and precision of antigen capture in the B cell immune synapse. (PNAS 2025)

- DOI: 10.1073/pnas.2422528122 | PMCID: PMC12107191 | PMID: 40354540
- Evidence: The ImageJ/Fiji, CellProfiler, Icy, and Python scripts used for image analysis are available on GitHub ( https://github.com/SpillaneLab ) ( 85 ).
- Full pipeline: stage not stated [CellProfiler, ImageJ, Python]

### A mechanism for MEX-5-driven disassembly of PGL-3/RNA condensates in vitro. (PNAS 2025)

- DOI: 10.1073/pnas.2412218122 | PMCID: PMC12107180 | PMID: 40354522
- Evidence: Analysis of the PhaseScan images was carried out by means of a custom-written Python script.
- Full pipeline: stage not stated [Python]

### Dopamine induces fear extinction by activating the reward-responding amygdala neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2501331122 | PMCID: PMC12067255 | PMID: 40294263
- Evidence: Raw photometry traces were preprocessed with custom Python scripts for timestamp corrections and alignment to behavior, then processed using the open-source photometry analysis tool, GuPPy.
- Full pipeline: alignment/mapping [Python] -> stage not stated [DeepLabCut, ImageJ]

### Behavioral resilience via dynamic circuit firing homeostasis. (PNAS 2025)

- DOI: 10.1073/pnas.2421386122 | PMCID: PMC12067288 | PMID: 40299703
- Evidence: A custom Python script was used to fit a Gaussian function for each channel, and data were centered for the nearest position to the Gaussian peak (as true peak values are sensitive to local maxima).
- Full pipeline: stage not stated [Fiji, ImageJ, Python]

### LACE-UP: An ensemble machine-learning method for health subtype classification on multidimensional binary data. (PNAS 2025)

- DOI: 10.1073/pnas.2423341122 | PMCID: PMC12054798 | PMID: 40267132
- Evidence: For all analyses, LCA was performed using the poLCA ( 33 ) package in R and UMAP was performed using the umap ( 61 ) package in R, which is a wrapper for the original umap ( 62 ) package in Python.
- Full pipeline: dimensionality reduction/clustering [Python, UMAP] -> simulation/modelling [igraph]

### Proteostasis landscapes of cystic fibrosis variants reveal drug response vulnerability. (PNAS 2025)

- DOI: 10.1073/pnas.2418407122 | PMCID: PMC12054793 | PMID: 40261935
- Evidence: To determine statistically significant CFTR interactors, we used a two-tailed paired t test with scipy.stats.ttest_rel ( https://docs.scipy.org/doc/scipy/ ) package in Python to calculate the p-value between the log2 TMT intensity of each protein over the corresponding log2 TMT intensity in the mock-transfected control condition.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Python, SciPy]

### Reducing the effects of radiation damage in cryo-EM using liquid helium temperatures. (PNAS 2025)

- DOI: 10.1073/pnas.2421538122 | PMCID: PMC12054821 | PMID: 40261934
- Evidence: Movies ( ≈ 100 for each hole size and tilt angle) were aligned using Unblur ( 50 ), and gold nanoparticles not bound to others or the foil were selected using custom Python scripts.
- Full pipeline: alignment/mapping [Python] -> registration [MotionCor2, RELION v4.0] -> stage not stated [CTFFIND]

### A diverse single-stranded DNA-annealing protein library enables efficient genome editing across bacterial phyla. (PNAS 2025)

- DOI: 10.1073/pnas.2414342122 | PMCID: PMC12054835 | PMID: 40258142
- Evidence: Next-generation sequencing was run in an Illumina MiSeq and examined with custom Python scripts to track the barcodes corresponding to each SSAP, which are provided in Dataset S1 .
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, Python]

### Virion-associated influenza hemagglutinin clusters upon sialic acid binding visualized by cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426427122 | PMCID: PMC12037027 | PMID: 40244672
- Evidence: Inter-HA distances for both HA and LSTc-bound HA were calculated using a custom Python script.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [PHENIX] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Matplotlib, Python, RELION, seaborn]

### Dynamic coexistence driven by physiological transitions in microbial communities. (PNAS 2025)

- DOI: 10.1073/pnas.2405527122 | PMCID: PMC12037064 | PMID: 40244660
- Evidence: All other results were obtained using simulations performed in Python 3 using forward Euler integration.
- Full pipeline: simulation/modelling [Python]

### Downregulation of Nesprin1 by Runx2 deficiency is critical for the development of skeletal laminopathy-like pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2320138122 | PMCID: PMC12012476 | PMID: 40208950
- Evidence: Single-cell RNA-seq data were processed with STARsolo and analyzed using Scanpy in Python.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP, scVelo] -> stage not stated [Galaxy, ImageJ, Python, Scanpy, deepTools]

### Multiplexing of cognitive encoding by oculomotor networks leads to incidental gaze shifts. (PNAS 2025)

- DOI: 10.1073/pnas.2422331122 | PMCID: PMC12012544 | PMID: 40198709
- Version used: **3.8**
- Evidence: All analyses were performed using custom software written in Python v3.8.
- Full pipeline: stage not stated [Kilosort, Python v3.8]

### An integrated AI knowledge graph framework of bacterial enzymology and metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2425048122 | PMCID: PMC12012490 | PMID: 40193601
- Evidence: We implement these Boolean rules in Python to programmatically infer the associated KEGG modules.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HMMER, PyTorch, Python, SciPy]

### An unusual potassium conductance protects &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; pharyngeal muscle rhythms against environmental noise. (PNAS 2025)

- DOI: 10.1073/pnas.2422709122 | PMCID: PMC12002347 | PMID: 40178897
- Evidence: ...c conductance in the current balance equation during simulation at the arrival times sampled from the Poisson distribution using the Poisson function in Python’s NumPy package.
- Full pipeline: simulation/modelling [NumPy, Python]

### Monomers and short oligomers of human RAD52 promote single-strand annealing. (PNAS 2025)

- DOI: 10.1073/pnas.2420771122 | PMCID: PMC12002259 | PMID: 40184180
- Evidence: Generated HDF5 files were processed and fitted using a custom-written Python script.
- Full pipeline: stage not stated [Python]

### Lung B cells in ectopic germinal centers undergo affinity maturation. (PNAS 2025)

- DOI: 10.1073/pnas.2416855122 | PMCID: PMC12002176 | PMID: 40168127
- Evidence: Analysis of transcriptomic data was done in Python using Scanpy (v1.10.4) ( 62 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3.1] -> stage not stated [Python, Scanpy v1.10.4]

### Cotranslational membrane insertion of the voltage-sensitive K&lt;sup&gt;+&lt;/sup&gt; channel KvAP. (PNAS 2025)

- DOI: 10.1073/pnas.2412492122 | PMCID: PMC12002286 | PMID: 40163725
- Version used: **3.12**
- Evidence: 4 was estimated by the multiple comparisons Dunnett’s test ( P < 0.05) ( 50 ), using the Python (version 3.12) library SciPy ( 51 ).
- Full pipeline: stage not stated [ImageJ, Python v3.12, SciPy]

### Climate change amplifies neurotoxic methylmercury threat to Asian fish consumers. (PNAS 2025)

- DOI: 10.1073/pnas.2421921122 | PMCID: PMC12002180 | PMID: 40127279
- Version used: **3.8.18**
- Evidence: The annual mean values of potential evaporation, surface wind speed (at 10 m), surface solar radiation downward, the annual sum of precipitation, and the 30-d running mean of maximum temperature (at 2 m) of the year were calculated using cdo in Python (v.3.8.18).
- Full pipeline: stage not stated [Python v3.8.18, R v4.3.2]

### Large-scale combination screens reveal small-molecule sensitization of antibiotic-resistant gram-negative ESKAPE pathogens. (PNAS 2025)

- DOI: 10.1073/pnas.2402017122 | PMCID: PMC12002207 | PMID: 40127266
- Evidence: A Snakemake analysis pipeline was developed for the integration of DropArray image analysis and antibiotic potentiation scoring with previously developed custom Python scripts ( SI Appendix , SI Methods ) ( 18 ).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> stage not stated [Python, Snakemake]

### Energy landscape analysis of the development of the chromosome structure across the cell cycle. (PNAS 2025)

- DOI: 10.1073/pnas.2425225122 | PMCID: PMC11962442 | PMID: 40112110
- Evidence: Data analysis utilized OpenMiChroM toolkit that includes CNDBtools in Python 3 ( 44 , 69 ).
- Full pipeline: simulation/modelling [OpenMM] -> visualisation [VMD] -> stage not stated [Python]

### Vortex reversal is a precursor of confined bacterial turbulence. (PNAS 2025)

- DOI: 10.1073/pnas.2414446122 | PMCID: PMC11929451 | PMID: 40085657
- Evidence: Data, Materials, and Software Availability All the relevant experimental and numerical data, the MATLAB codes for analyzing the experimental data, Python scripts for the numerical simulations of the TTSHE, and the Mathematica code for analytical theory are deposited on Zenodo ( 53 ).
- Full pipeline: simulation/modelling [Python]

### A solvable model for strongly interacting nonequilibrium excitons. (PNAS 2025)

- DOI: 10.1073/pnas.2424663122 | PMCID: PMC11929435 | PMID: 40085654
- Evidence: Materials and Methods We implement numerically finding the steady state in Python.
- Full pipeline: stage not stated [NumPy, Python, SciPy]

### A global estimate of multiecosystem photosynthesis losses under microplastic pollution. (PNAS 2025)

- DOI: 10.1073/pnas.2423957122 | PMCID: PMC11929485 | PMID: 40063820
- Version used: **3.8.8**
- Evidence: The ML models were implemented using the scikit-learn 1.2.2 package in Python 3.8.8.
- Full pipeline: stage not stated [Python v3.8.8, R v4.0.3, ggplot2, lme4, metafor, scikit-learn v1.2.2]

### Learning reshapes the hippocampal representation hierarchy. (PNAS 2025)

- DOI: 10.1073/pnas.2417025122 | PMCID: PMC11929462 | PMID: 40063792
- Version used: **3.11**
- Evidence: We utilized the routine GLM.fit_regularized offered by the package statsmodels v0.14 in Python 3.11 ( 65 ).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [Python v3.11, statsmodels v0.14]

### Epstein-Barr virus and the immune microenvironment in multiple sclerosis: Insights from high-dimensional brain tissue imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2425670122 | PMCID: PMC11929469 | PMID: 40063794
- Evidence: These histograms were generated using the Seaborn package in Python, with the density plot overlaid using the seaborn.histplot function and the kde=True argument to provide a smooth density estimate of the distribution.
- Full pipeline: stage not stated [Python, seaborn]

### Input-driven circuit reconfiguration in critical recurrent neural networks. (PNAS 2025)

- DOI: 10.1073/pnas.2418818122 | PMCID: PMC11912373 | PMID: 40053358
- Evidence: For example, in Python using PyTorch, where z is the state, I the input, and Ut the Fourier transform of the kernel U , all three torch.tensor()s of the same shape. where one would use fft2/ifft2 for two-dimensional tensor layers.
- Full pipeline: dimensionality reduction/clustering [PyTorch, Python]

### A general framework for interpretable neural learning based on local information-theoretic goal functions. (PNAS 2025)

- DOI: 10.1073/pnas.2408125122 | PMCID: PMC11912414 | PMID: 40042906
- Evidence: The experiments have been implemented in Python and have been made available on GitLab at https://gitlab.gwdg.de/wibral/infomorphic_networks ( 84 ).
- Full pipeline: stage not stated [Python]

### The effect of salt additives on the glycine crystallization pathway revealed by studying one crystal nucleation at a time. (PNAS 2025)

- DOI: 10.1073/pnas.2419638122 | PMCID: PMC11912379 | PMID: 40035758
- Evidence: The raw data were noise-filtered by Singular Value Decomposition before the analysis by NMF algorithm using the Scikit-Learn library in Python ( 61 ).
- Full pipeline: stage not stated [Python]

### Immobile lipopolysaccharides and outer membrane proteins differentially segregate in growing &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2414725122 | PMCID: PMC11912417 | PMID: 40030021
- Evidence: In all cases, binary image clean-up to remove erroneously segmented noise and cell clumps was conducted in Python.
- Full pipeline: stage not stated [ImageJ, Matplotlib, Python, R v4.1.0]

### Defects induce phase transition from dynamic to static rippling in graphene. (PNAS 2025)

- DOI: 10.1073/pnas.2416932122 | PMCID: PMC11892612 | PMID: 40020187
- Evidence: The entire postprocessing analysis for all simulations was performed in Python using the ASE ( 71 ), MDAnalysis ( 72 , 73 ), and OVITO ( 74 ) software packages.
- Full pipeline: simulation/modelling [LAMMPS, MDAnalysis, Python]

### A spectral machine learning approach to derive central aortic pressure waveforms from a brachial cuff. (PNAS 2025)

- DOI: 10.1073/pnas.2416006122 | PMCID: PMC11892652 | PMID: 40009644
- Version used: **3.7**
- Evidence: All analysis performed on the clinical data uses codes written in Python 3.7.
- Full pipeline: stage not stated [Python v3.7]

### Deep learning to quantify the pace of brain aging in relation to neurocognitive changes. (PNAS 2025)

- DOI: 10.1073/pnas.2413442122 | PMCID: PMC11912385 | PMID: 39993207
- Version used: **3.8**
- Evidence: The model was implemented using Python 3.8 and TensorFlow 2.12.0 on a computer with an Intel Core i7 processor, a clock speed of 2.2 GHz, 16 GB of RAM, and a 32 GB NVIDIA V100 graphical processing unit (GPU) for training and evaluation.
- Full pipeline: structure determination [FreeSurfer] -> machine learning [Python v3.8, TensorFlow v2.12.0]

### Abrupt changes in algal biomass of thousands of US lakes are related to climate and are more likely in low-disturbance watersheds. (PNAS 2025)

- DOI: 10.1073/pnas.2416172122 | PMCID: PMC11892623 | PMID: 39993195
- Evidence: CHL time series were clustered using agglomerative hierarchical clustering using scikit-learn in Python ( 73 ) by initially treating each lake as its own cluster, then recursively merging clusters step-wise while subject to a criterion ( 30 , 74 , 75 ).
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [R]

### Subfunctionalization and epigenetic regulation of a biosynthetic gene cluster in &lt;i&gt;Solanaceae&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2420164122 | PMCID: PMC11874288 | PMID: 39977312
- Version used: **3.9**
- Evidence: Microsynteny analysis and figures were done with MCScan implemented in Python (v3.9) with JCVI utility libraries (v1.1.11) following the package workflow: https://github.com/tanghaibao/jcvi/wiki/MCscan-(Python-version) .
- Full pipeline: alignment/mapping [MAFFT v7.490] -> quantification [DESeq2] -> normalisation [DESeq2] -> visualisation [Python v3.9] -> stage not stated [IQ-TREE v2.1.4, OrthoFinder v2.5.4]

### Evolutionary rewiring of the dynamic network underpinning allosteric epistasis in NS1 of the influenza A virus. (PNAS 2025)

- DOI: 10.1073/pnas.2410813122 | PMCID: PMC11873825 | PMID: 39977319
- Evidence: The NetworkX package ( 87 ) in Python was used to perform the graph theory analysis.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [NetworkX, OpenMM v7.6.0, Python]

### Modeling energy requirements for oxygen production on the Moon. (PNAS 2025)

- DOI: 10.1073/pnas.2306146122 | PMCID: PMC11874342 | PMID: 39964715
- Evidence: The modeling is implemented in Python, and is available on our github repository ( 74 ).
- Full pipeline: stage not stated [Python]

### A deep learning-enabled smart garment for accurate and versatile monitoring of sleep conditions in daily life. (PNAS 2025)

- DOI: 10.1073/pnas.2420498122 | PMCID: PMC11848432 | PMID: 39932995
- Version used: **3.8.13**
- Evidence: Network training was conducted using Python 3.8.13, Miniconda 3, and PyTorch 2.0.1 in a performance-optimized environment.
- Full pipeline: machine learning [Conda, PyTorch v2.0.1, Python v3.8.13]

### Abscisic acid signaling gates salt-induced responses of plant roots. (PNAS 2025)

- DOI: 10.1073/pnas.2406373122 | PMCID: PMC11831169 | PMID: 39908104
- Version used: **2.7**
- Evidence: First read quality was analyzed with FastQC ( 56 ) and MultiQC ( 57 ) packages in Python 2.7, followed by trimming of low quality reads with Trim Galore!
- Full pipeline: quality control [FastQC, MultiQC, Python v2.7, Trim Galore] -> read trimming [FastQC, MultiQC, Python v2.7, Trim Galore] -> alignment/mapping [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, R] -> stage not stated [OpenCV v4.5.1.48]

### Cataract-prone variants of γD-crystallin populate a conformation with a partially unfolded N-terminal domain under native conditions. (PNAS 2025)

- DOI: 10.1073/pnas.2410860122 | PMCID: PMC11831119 | PMID: 39899721
- Evidence: All downstream quantitative analysis was performed using Python scripts in Jupyter notebooks.
- Full pipeline: stage not stated [Jupyter, Python]

### Calcineurin governs baseline and homeostatic regulations of non-rapid eye movement sleep in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2418317122 | PMCID: PMC11789068 | PMID: 39847332
- Version used: **3.9.7**
- Evidence: The dynamic changes of NREMS delta power of each mouse during a 48 h period, including 24 h baseline sleep and 6 h SD followed by 18 h recovery sleep, was used to simulate process S using Python 3.9.7 with code provided by Masashi Yanagisawa and Hiromasa Funato ( 17 ).
- Full pipeline: simulation/modelling [Python v3.9.7]

### Automating alloy design and discovery with physics-aware multimodal multiagent AI. (PNAS 2025)

- DOI: 10.1073/pnas.2414074122 | PMCID: PMC11789045 | PMID: 39854228
- Evidence: The plan involves using a computation tool to derive material properties from atomistic simulations, a knowledge retrieval tool to extract these properties from papers, and coding tools to write a Python script for saving the results.
- Full pipeline: simulation/modelling [ASE, LAMMPS, Python]

### Dispersal of influenza virus populations within the respiratory tract shapes their evolutionary potential. (PNAS 2025)

- DOI: 10.1073/pnas.2419985122 | PMCID: PMC11789087 | PMID: 39835898
- Evidence: A custom Python script is then employed to screen and identify barcode sequences present in each sample, calculate diversity statistics, and generate summary tables.
- Full pipeline: differential/statistical testing [Python] -> visualisation [ggplot2] -> stage not stated [R v4.1.3, vegan v2.6]

### Discrepancies between subjective and objective sleep assessments revealed by in-home electroencephalography during real-world sleep. (PNAS 2025)

- DOI: 10.1073/pnas.2412895121 | PMCID: PMC11761674 | PMID: 39819218
- Evidence: The analyses were performed using statsmodels in Python ( 40 ).
- Full pipeline: stage not stated [Python, scikit-learn, statsmodels]

### Spatially programmed alignment and actuation in printed liquid crystal elastomers. (PNAS 2025)

- DOI: 10.1073/pnas.2414960122 | PMCID: PMC11761666 | PMID: 39813252
- Evidence: Data processing and stitching were performed using custom Python scripts based on pyFAI ( 50 ) and the SMI beamline analysis package ( 51 ).
- Full pipeline: stage not stated [Python]

### Decoding the elite soccer player's psychological profile. (PNAS 2025)

- DOI: 10.1073/pnas.2415126122 | PMCID: PMC11760505 | PMID: 39808661
- Evidence: The ANN architecture was constructed using the TensorFlow and Keras frameworks in Python.
- Full pipeline: differential/statistical testing [R] -> stage not stated [Keras, Python, TensorFlow]

### Codon bias, nucleotide selection, and genome size predict in situ bacterial growth rate and transcription in rewetted soil. (PNAS 2025)

- DOI: 10.1073/pnas.2413032122 | PMCID: PMC11761963 | PMID: 39805015
- Version used: **3.8.2**
- Evidence: Genomic traits were calculated using custom scripts written in Python (v 3.8.2)—using the packages pandas ( 76 ) and NumPy ( 77 ); they can be found at https://github.com/PChuckran/Wet_up_traits .
- Full pipeline: alignment/mapping [DESeq2, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [R v4.2.1, ggplot2, tidyverse] -> visualisation [R v4.2.1, ggplot2, tidyverse] -> stage not stated [NumPy, Python v3.8.2]

### High organofluorine concentrations in municipal wastewater affect downstream drinking water supplies for millions of Americans. (PNAS 2025)

- DOI: 10.1073/pnas.2417156122 | PMCID: PMC11761303 | PMID: 39761386
- Version used: **3.9.7**
- Evidence: 1 and using Bayesian linear regression implemented in PyMC3 version 3.11.5 ( 59 ) in Python version 3.9.7.
- Full pipeline: differential/statistical testing [PyMC v3.11.5, PyMC3 v3.11.5, Python v3.9.7]

### A minimal vertex model explains how the amnioserosa avoids fluidization during &lt;i&gt;Drosophila&lt;/i&gt; dorsal closure. (PNAS 2025)

- DOI: 10.1073/pnas.2322732121 | PMCID: PMC11725931 | PMID: 39793057
- Evidence: Analysis and illustration of model and experiment data was performed with custom Python scripts.
- Full pipeline: quantification [ImageJ] -> stage not stated [Python]

### Synapse-specific catecholaminergic modulation of neuronal glutamate release. (PNAS 2025)

- DOI: 10.1073/pnas.2420496121 | PMCID: PMC11725921 | PMID: 39793084
- Evidence: Targeted regions were selected and wobbled via use of a Python script, where base pairs were replaced with those of viable alternative codons typically by modifying the third base pair for each codon.
- Full pipeline: stage not stated [Clustal Omega, ImageJ, Python]

### Reclassification and weighting of multiple causes of death: US death certificates 2003-2023. (PNAS 2026)

- DOI: 10.1073/pnas.2604493123 | PMCID: PMC13291531 | PMID: 42308034
- Evidence: All analyses were performed using Python scripts developed iteratively with LLM assistance (Claude, Anthropic).
- Full pipeline: stage not stated [Python]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: MA plots were generated in Python with Matplotlib, pandas, and NumPy.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### Genome-wide analysis of mRNA regionalization in a giant single cell. (PNAS 2026)

- DOI: 10.1073/pnas.2537760123 | PMCID: PMC13291615 | PMID: 42296355
- Evidence: PCA was performed using the scikit-learn implementation (sklearn.decomposition.PCA) in Python.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [kallisto] -> normalisation [kallisto] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [kallisto]

### Damselflies overcome color saturation barriers of photonic glasses via pigment loading and refractive index modulation. (PNAS 2026)

- DOI: 10.1073/pnas.2527433123 | PMCID: PMC13250596 | PMID: 42213815
- Version used: **3.11**
- Evidence: All calculations were performed using a custom Python script (Python 3.11, NumPy, SciPy, Matplotlib, and Pandas libraries).
- Full pipeline: stage not stated [ImageJ, Matplotlib, NumPy, Python v3.11, SciPy]

### Large language models pass a standard three-party Turing test. (PNAS 2026)

- DOI: 10.1073/pnas.2524472123 | PMCID: PMC13214042 | PMID: 42154549
- Evidence: For the fourth AI model, ELIZA, we used an implementation in Python based on the DOCTOR script ( 39 , 66 ).
- Full pipeline: stage not stated [Python]

### Geometric ordering in bacterial communities. (PNAS 2026)

- DOI: 10.1073/pnas.2526643123 | PMCID: PMC13187718 | PMID: 42118839
- Evidence: All simulations were implemented in Python.
- Full pipeline: simulation/modelling [Python] -> visualisation [Matplotlib v3.7.1, SciPy] -> stage not stated [ImageJ v1.54d, NumPy]

### Interspecies interaction controls &lt;i&gt;Escherichia coli&lt;/i&gt; growth in human gut microbiome samples. (PNAS 2026)

- DOI: 10.1073/pnas.2527793123 | PMCID: PMC13123830 | PMID: 42018414
- Evidence: We processed the data in Python using SciPy.
- Full pipeline: quantification [vegan v2.7] -> normalisation [vegan v2.7] -> dimensionality reduction/clustering [vegan v2.7] -> visualisation [phyloseq v1.46] -> stage not stated [DADA2 v3.18, Matplotlib, Python, SciPy, emmeans]

### Rotational 3D printing of active-passive filaments and lattices with programmable shape morphing. (PNAS 2026)

- DOI: 10.1073/pnas.2537250123 | PMCID: PMC13123922 | PMID: 42018409
- Evidence: Data reduction and stitching were performed using custom Python scripts based on pyFAI ( 76 ).
- Full pipeline: stage not stated [ImageJ v1.53t, Python]

### Simple biological controllers drive the evolution of soft modes. (PNAS 2026)

- DOI: 10.1073/pnas.2523032123 | PMCID: PMC13123806 | PMID: 42012951
- Evidence: Materials and Methods We briefly review the methods employed in this study, which were implemented in Python.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [Python]

### Quinones operate as proton-collecting antennas in energy-transducing membranes. (PNAS 2026)

- DOI: 10.1073/pnas.2534025123 | PMCID: PMC13099693 | PMID: 41980103
- Evidence: The recorded correlation curves were analyzed using a Levenberg–Marquardt nonlinear least-square curve fitting algorithm written in Python ( 73 ).
- Full pipeline: simulation/modelling [MDAnalysis, VMD] -> stage not stated [Python]

### Fast automated adjoints for spectral PDE solvers. (PNAS 2026)

- DOI: 10.1073/pnas.2530440123 | PMCID: PMC13080004 | PMID: 41961849
- Evidence: Dedalus is written in Python, with compiled extensions for performance-critical routines, and it automatically handles distributed-memory parallelism via MPI.
- Full pipeline: simulation/modelling [PyTorch] -> machine learning [PyTorch] -> stage not stated [OpenFOAM, Python, SciPy]

### Reconstruction of human metabolic models with large language models. (PNAS 2026)

- DOI: 10.1073/pnas.2516511123 | PMCID: PMC13079975 | PMID: 41950094
- Version used: **3.7.16**
- Evidence: The analysis and visualization were facilitated by Python 3.7.16, SHAP 0.41.0, scikit-learn 1.0.2, pandas 1.1.3, SciPy 1.7.3, NumPy 1.21.5, and Matplotlib 3.4.3 packages.
- Full pipeline: visualisation [Matplotlib v3.4.3, NumPy v1.21.5, Python v3.7.16, SciPy v1.7.3, scikit-learn v1.0.2]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: It was implemented in Python, utilizing OpenCV, PIL, Tkinter/CustomTkinter, Matplotlib, NumPy, and Pandas for image processing, visualization, and data management, and with aicspylibczi for handling czi files.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Proteome-wide prediction of interactions between structured domains and peptide motifs reveals functionally coherent subnetworks. (PNAS 2026)

- DOI: 10.1073/pnas.2527957123 | PMCID: PMC13080015 | PMID: 41941631
- Evidence: This computation was implemented using a Python script that iteratively evaluated thresholds and summarized TP coverage and PrePPI coverage.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [AlphaFold, HMMER, Python, R, STRING db, scikit-learn]

### Functional role of small extrachromosomal circular DNA in colorectal cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523047123 | PMCID: PMC13056112 | PMID: 41926541
- Evidence: Kaplan–Meier curves were compared using log-rank tests, with all analyses performed in Python 3 and R v4.1.2.
- Full pipeline: quantification [DESeq2, kallisto v0.50.1] -> differential/statistical testing [DESeq2, kallisto v0.50.1] -> stage not stated [CNVkit v0.9.9, Python, R v4.1]

### Dynamic switching of cell-substrate contact sites allows gliding diatoms to modulate the curvature of their paths. (PNAS 2026)

- DOI: 10.1073/pnas.2506122123 | PMCID: PMC13056149 | PMID: 41920863
- Evidence: The raphes were then manually traced using the segmented line tool, and the extracted x–y coordinate data were used to reconstruct raphe shapes and analyze their curvature with a custom Python script.
- Full pipeline: structure determination [Python] -> stage not stated [ImageJ]

### Dynamical modeling of individual sensory reactivity and habituation learning. (PNAS 2026)

- DOI: 10.1073/pnas.2524738123 | PMCID: PMC13037877 | PMID: 41894333
- Version used: **3.10**
- Evidence: Bayesian models were coded in Stan ( 59 ) and fit using Python 3.10 through the CmdStanPy package (v1.2.4).
- Full pipeline: differential/statistical testing [Python v3.10, Stan] -> simulation/modelling [Stan]

### Tau catalyzes amyloid-β aggregation and toxicity in a polymorph-dependent manner. (PNAS 2026)

- DOI: 10.1073/pnas.2532775123 | PMCID: PMC13037932 | PMID: 41880569
- Evidence: Analyses were performed using a custom Python script with the statsmodels module.
- Full pipeline: differential/statistical testing [SciPy v1.13.1] -> stage not stated [Python, statsmodels]

### Self-regulated dual-mode solar energy harvesting. (PNAS 2026)

- DOI: 10.1073/pnas.2534717123 | PMCID: PMC13037869 | PMID: 41875152
- Evidence: 2 B —was measured by taking pixel values along a temporary surface slotted across the focal plane (between x = 0 to x = 1), photographed using a digital camera (Canon, EOS Rebel T3i) and analyzed using a custom script developed in Python.
- Full pipeline: stage not stated [Python]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Version used: **3.8.3**
- Evidence: We calculated the sequencing depth in 800 bp sliding windows every 400 bp and normalized it to the 3 kb regions upstream and downstream of the breakpoints with a Python (version 3.8.3) custom script, and reported the median as an estimate for BOR1 CN.
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Spatially structured inflammatory response in the presence of a uniform stimulus. (PNAS 2026)

- DOI: 10.1073/pnas.2507102123 | PMCID: PMC13012133 | PMID: 41860960
- Version used: **3.7**
- Evidence: To identify candidate genes that activated in epithelial tissue, the software packages decontX, scrublet (run in RStudio), and scanpy (run in Python v3.7) were used to generate quality scores for cells; cells with >12% mitochondrial reads, scrublet score >0.3, or decontX score >0.5, were eliminated, as well as genes expressed in <10 cells.
- Full pipeline: stage not stated [ImageJ, Python v3.7, Scanpy, scikit-image]

### Online supervised learning of temporal patterns in biological neural networks under feedback control. (PNAS 2026)

- DOI: 10.1073/pnas.2521560123 | PMCID: PMC12994192 | PMID: 41818149
- Evidence: Technically, the entire system was realized by controlling the HD-MEA in real time with custom-written C++/Python scripts ( Fig.
- Full pipeline: stage not stated [Python]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Evidence: The assembled transcripts were then aligned to the C. virginica genome using BLAST to detect residual oyster transcripts, which were filtered out using a Python script.
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### Class-I myosin responds to changes in membrane tension during clathrin-mediated endocytosis in human induced pluripotent stem cells. (PNAS 2026)

- DOI: 10.1073/pnas.2532817123 | PMCID: PMC12956820 | PMID: 41734073
- Evidence: Events, which are deemed as tracked diffraction-limited spots, were extracted using the MATLAB tracking package, cmeAnalysis, and processed in Python Jupyter Notebooks ( 29 ).
- Full pipeline: stage not stated [Jupyter, Python]

### Compounded effects on wetland greenhouse gas fluxes from climate change and water management along a saline to freshwater gradient. (PNAS 2026)

- DOI: 10.1073/pnas.2513685123 | PMCID: PMC12933060 | PMID: 41701819
- Evidence: Calibrated models were then run in a bootstrap ensemble (n = 100) approach using “Scikit-Learn” ( 99 ) in Python ( 100 ) on the NASA Center for Climate Simulation (NCCS) Discover Supercomputer to produce robust aggregated predictions of flux intensity and uncertainty.
- Full pipeline: simulation/modelling [Python] -> machine learning [R] -> stage not stated [lavaan]

### Distinct impact of PI(4)P flux on PI(4,5)P&lt;sub&gt;2&lt;/sub&gt; steady states and oscillations. (PNAS 2026)

- DOI: 10.1073/pnas.2518354123 | PMCID: PMC12933082 | PMID: 41701834
- Version used: **3.10.12**
- Evidence: Image stacks were analyzed using a combination of standard library functions and custom-written routines in Python (version 3.10.12, Anaconda distribution) and MATLAB (R2023b, MathWorks), together with built-in routines in Fiji ( 89 ) (version 2.3.0/1.53t, ImageJ distribution).
- Full pipeline: stage not stated [Conda, ImageJ, Python v3.10.12]

### Molecular assemblies and pharmacology of cerebellar GABA&lt;sub&gt;A&lt;/sub&gt; receptors. (PNAS 2026)

- DOI: 10.1073/pnas.2524504123 | PMCID: PMC12890884 | PMID: 41650215
- Evidence: Data analysis was performed in Python using SciPy, applying either a one-site binding or competitive inhibition model.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Python, SciPy]

### Olfactory inputs to appetite neurons in the hypothalamus. (PNAS 2026)

- DOI: 10.1073/pnas.2524926123 | PMCID: PMC12867749 | PMID: 41591908
- Evidence: All data visualization and downstream analyses were performed in Python.
- Full pipeline: alignment/mapping [Cufflinks] -> quantification [AnnData v0.10, Cufflinks, Matplotlib v3.8, Scanpy v1.9] -> visualisation [Matplotlib v3.8, Python]

### The Japanese Archipelago sheltered cave lions, not tigers, during the Late Pleistocene. (PNAS 2026)

- DOI: 10.1073/pnas.2523901123 | PMCID: PMC12890994 | PMID: 41587328
- Evidence: Deamidation rates, as indicators of protein preservation, were calculated using a Python script following Mackie et al.
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [ANGSD, BWA v0.7.17, SAMtools v1.11] -> stage not stated [MAFFT v7.505, Python]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Evidence: The simulation was implemented in Python using standard scientific computing libraries, including NumPy and Matplotlib, with additional functionality from Biopython for lineage tree construction.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

### Network structure shapes consensus dynamics through individual decisions. (PNAS 2026)

- DOI: 10.1073/pnas.2520483123 | PMCID: PMC12799169 | PMID: 41499391
- Evidence: We used the open-source framework oTree written in Python ( 40 ), and hosted experiments on a Linux server.
- Full pipeline: stage not stated [Python]

### Income insufficiency impacts early brain development in infants facing increased psychosocial adversity: A network-based approach. (PNAS 2026)

- DOI: 10.1073/pnas.2513598123 | PMCID: PMC12799155 | PMID: 41490482
- Version used: **3.6.8**
- Evidence: A modified version of SpecParam v1.0.0 (Also known as FOOOF, https://github.com/fooof-tools/fooof ; in Python v3.6.8) was used to model periodic and aperiodic components of the power spectra. [See Wilkinson et al.
- Full pipeline: stage not stated [Python v3.6.8, ggplot2]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Evidence: All subsequent analyses were carried out using a custom Python script.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### Vapor-mediated wetting and imbibition control on micropatterned surfaces. (PNAS 2026)

- DOI: 10.1073/pnas.2519761122 | PMCID: PMC12773719 | PMID: 41481441
- Evidence: Image analysis was done by a self-developed Python script.
- Full pipeline: stage not stated [Python]

### Dosa: A method to covalently barcode proteins for high-throughput biochemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2529762123 | PMCID: PMC12773776 | PMID: 41481464
- Version used: **3.0**
- Evidence: Proportion tests were performed using the prop.test function from the statsmodels package in Python 3.0, executed within a Google Colab environment.
- Full pipeline: stage not stated [Python v3.0, statsmodels]

### Experimental manipulation of ecological and cognitive conditions produces the entire conformity-diversity spectrum in a single species. (PNAS 2026)

- DOI: 10.1073/pnas.2517195123 | PMCID: PMC12773784 | PMID: 41468428
- Version used: **3.13.7**
- Evidence: 1 were generated using Python 3.13.7.
- Full pipeline: stage not stated [Python v3.13.7]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **3.8.2**
- Evidence: Software The following Python (version 3.8.2) software packages were used in the data analysis and in the production of figures: Scipy (version 1.4.1) ( 78 ), pandas (version 1.0.3) ( 79 ), statsmodels (version 0.11.1) ( 80 ), matplotlib (version 3.2.1) ( 81 ), numpy (1.18.3) ( 82 ), seaborn_sinaplot ( 83 ), simanneal (version 0.5.0) ( 71 ), and seaborn (version 0.10.1) ( 84 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Evidence: Chen for help with Python scripts; D.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Uncovering the functional diversity of rare CRISPR-Cas systems with deep terascale clustering. (Science 2023)

- DOI: 10.1126/science.adi1910 | PMCID: PMC10910872 | PMID: 37995242
- Evidence: FLSHclust implementation The FLSHclust algorithm was implemented in Python 3 using PySpark for distributed computation on clusters without shared memory or disk.
- Full pipeline: dimensionality reduction/clustering [Python] -> stage not stated [AlphaFold]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: Regulon matrix heatmaps were plotted using the Seaborn (v0.12.1) package in Python.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Epigenetic plasticity cooperates with cell-cell interactions to direct pancreatic tumorigenesis. (Science 2023)

- DOI: 10.1126/science.add5327 | PMCID: PMC10316746 | PMID: 37167403
- Evidence: Processed transcriptomic and epigenomic datasets were analyzed with custom Python scripts for visualization, cell-state annotation, metacell inference, multimodal integration, plasticity scoring, and Calligraphy communication inference, among other analyses fully described in ( 27 ). smFISH image analysis was performed on maximum projection images with segmentation on the DAPI channel using Mesmer...
- Full pipeline: quality control [ArchR] -> normalisation [ArchR] -> visualisation [Python] -> stage not stated [GSEA]

### Hidden state inference requires abstract contextual representations in the ventral hippocampus. (Science 2024)

- DOI: 10.1126/science.adq5874 | PMCID: PMC7618349 | PMID: 39571013
- Evidence: Photometry data processing Photometry data were analyzed with custom-written Python scripts.
- Full pipeline: differential/statistical testing [R, lme4, pingouin, scikit-learn, statsmodels] -> stage not stated [Python, SciPy]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: Mapping along each read was visualized with a custom Python script: each read is represented as a series of line segments, one segment per 11-mer, where the x coordinate is determined by the mapping positions of the longest consecutive run of 11-mers, and all other 11-mers in the read are given x coordinates relative to this consecutive run.
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: GO analyses were conducted using the gseapy.enrichr() function in Python.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### Metagenomic editing of commensal bacteria in vivo using CRISPR-associated transposases. (Science 2025)

- DOI: 10.1126/science.adx7604 | PMCID: PMC12969935 | PMID: 41231980
- Evidence: Untargeted reads and on-target reads were assigned using a custom Python script.
- Full pipeline: alignment/mapping [BLAST, Bowtie2, ggplot2] -> quantification [ggplot2] -> normalisation [ggplot2, seaborn] -> visualisation [ggplot2, seaborn] -> stage not stated [Python]

### High-resolution spatial mapping of cell state and lineage dynamics in vivo with PEtracer. (Science 2025)

- DOI: 10.1126/science.adx3800 | PMCID: PMC12766569 | PMID: 40705858
- Evidence: A custom Python script was used to extract lineage information from the BAM alignment file generated by Cellranger.
- Full pipeline: alignment/mapping [Python, scikit-image v0.24.0] -> normalisation [Scanpy v1.10.0] -> dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> stage not stated [Cellpose v3.1.0, R v4.2.3, Seurat, Squidpy v1.6.2, scDblFinder]

### Interphase cell morphology defines the mode, symmetry, and outcome of mitosis. (Science 2025)

- DOI: 10.1126/science.adu9628 | PMCID: PMC7619237 | PMID: 40310923
- Evidence: A Python script using the scikit-image library was used to define the medial spine of the cell shape masks generated in ImageJ.
- Full pipeline: stage not stated [ImageJ, Python, scikit-image]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: Each subset was prepared for downstream processing in RELION using an in-house Python script which implements PyEM ( 93 ) and Starparser ( 94 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Evidence: Other plots were made using a combination of matplotlib (3.8.1) and seaborn (0.13.0) libraries in Python.
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Evidence: With a Nikon LTTL 3 microscope, micromanager, and a Python script, a strategy to automatically map and image individual sperm heads was designed.
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

### Cryo-electron microscopy structure of the budding yeast telomerase holoenzyme. (Science 2026)

- DOI: 10.1126/science.adz5344 | PMCID: PMC7619062 | PMID: 41886584
- Evidence: PAE plot of predicted models were made using a Python script ( https://github.com/nayimgr/af3analysis ).
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, CTFFIND v4.1, Python, RELION v5.0, Topaz]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: A Python script ( https://github.com/josephreplogle/CRISPRi-dual-sgRNA-screens ; ( 105 )) was used to align the reads to the trigger library sequences and quantifying them.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

