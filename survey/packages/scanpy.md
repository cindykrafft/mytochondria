# Scanpy

- **Category:** single-cell
- **Papers in survey:** 200
- **Journals:** Nature (129), PNAS (38), Cell (24), Science (9)
- **Years:** 2021 (17), 2022 (19), 2023 (31), 2024 (36), 2025 (62), 2026 (35)
- **Versions named:** 1.9.1 (13), 1.6.0 (7), 1.8.2 (4), 1.9.3 (4), 1.10.0 (4), 1.8.1 (3), 1.4.3 (3), 1.9 (3), 1.9.8 (2), 1.10.3 (2)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (46), normalisation (31), quality control (16), visualisation (9), differential/statistical testing (6), quantification (5), alignment/mapping (5), simulation/modelling (4), variant calling (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: This droplet matrix was processed as an AnnData object using our preprocessing pipeline which utilizes the Scanpy toolkit ( Wolf et al., 2018 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Evidence: ...s://cran.r-project.org/web/packages/sf Python 3.7.8 Van Rossum and Drake, 2009 https://www.python.org/ SCANPY version 1.7.2 Wolf et al., 2018 https://scanpy.readthedocs.io/en/stable/ scVI version 0.6.7 Gayoso et al., 2021 https://scvi-tools.org/ Python package seaborn version 0.10.1 Waskom, 2021 https://seaborn.pydata.org/ Python package scipy version 1.5.2 Virtanen et al., 2020 https://scipy.org/...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Profiling SARS-CoV-2 HLA-I peptidome reveals T cell epitopes from out-of-frame ORFs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.046 | PMCID: PMC8173604 | PMID: 34171305
- Version used: **1.6.0**
- Evidence: Except where noted, Scanpy (v1.6.0; Wolf et al., 2018 ) was used to perform the subsequent single-cell analyses.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Python v3.7.3, Scanpy v1.6.0]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: ...er N/A RRID: SCR_017344 Cutadapt Martin, 2011 RRID: SCR_011841 RNA-SeQC DeLuca et al., 2012 RRID: SCR_005120 RSEM Li and Dewey, 2011 RRID: SCR_013027 Scanpy Wolf et al., 2018 RRID: SCR_018139 Bioconductor R Huber et al., 2015 RRID: SCR_001905 Bioconductor packages edgeR Robinson et al., 2010 RRID: SCR_012802 Resource availability Lead contact Further information and requests for resources and reag...
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Version used: **1.6.0**
- Evidence: The data processed using Scanpy version 1.6.0 and Scrublet version 0.2.1.
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.053 | PMCID: PMC7857060 | PMID: 33657410
- Version used: **1.4.6**
- Evidence: ...BUStools/bustools STARTRAC Zhang et al., 2018 https://github.com/Japrin/STARTRAC Seurat 2.3.0/3.0 ( Butler et al., 2018 ) http://satijalab.org/seurat scanpy 1.4.6/1.5.1 Wolf et al., 2018 https://scanpy.readthedocs.io/en/latest/ CSOmap Ren et al., 2020 https://github.com/zhongguojie1998/CSOmap SCENIC 1.1.2-2 Aibar et al., 2017 https://github.com/aertslab/SCENIC Scrublet ( Wolock et al., 2019 ) http...
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [SCENIC v1.1.2, Scanpy v1.4.6, Seurat v2.3.0, kallisto, scDblFinder]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: In order to better understand the higher level connectivity structure of 101 single cell populations identified in our atlas, we employed a partition-based graph abstraction algorithm ( Wolf et al., 2019 ) (scanpy accessed via reticulate (version 1.16) and SeuratWrappers (version 0.1.0) in R) using batch-corrected, dimension-reduced data as defined above and cell identities as defined above from t...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: GraphPad Prism ( https://graphpad.com ); RRID:SCR_015807 FlowJo software (version: 10.0.0) FlowJo, LLC FlowJo ( https://www.flowjo.com/ ); RRID:SCR_008520 Scanpy (version: 1.5.0, 1.8.1) Wolf et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Version used: **1.6.0**
- Evidence: ...pression/software/pipelines/latest/what-is-cell-ranger Scrublet v0.2.1 (Python package) Wolock et al., 2019 https://github.com/AllonKleinLab/scrublet Scanpy v1.6.0 (Python package) Wolf et al., 2018 https://github.com/theislab/scanpy UMAP v0.5.1 (Python package) McInnes et al., 2020 https://github.com/lmcinnes/umap Leiden v0.8.0 (Python package) Traag et al., 2019 https://github.com/vtraag/leidena...
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...t.org/ RNASeQC ( DeLuca et al., 2012 ) v2.3.5 https://github.com/getzlab/rnaseqc Scanorama ( Hie et al., 2019 ) https://github.com/brianhie/scanorama Scanpy ( Wolf et al., 2018 ) https://github.com/theislab/scanpy Scater ( McCarthy et al., 2017 ) v3.12 http://bioconductor.org/packages/release/bioc/html/scater.html Scikit-learn ( Pedregosa et al., 2011 ) https://github.com/scikit-learn/scikit-learn...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: ...artview/3e2c65a5e3f783f8c9e5d648e4b64126 pheatmap R package N/A https://rdrr.io/cran/pheatmap/ ggplot2 ( Wickham 2016 ) https://ggplot2.tidyverse.org Scanpy ( Wolf et al., 2018 ) https://scanpy.readthedocs.io/en/stable/ PyTorch N/A https://pytorch.org TotalVI ( Gayoso et al., 2021 ) https://docs.scvi-tools.org/en/stable/user_guide/models/totalvi.html ScVI ( Lopez et al., 2018 ) https://docs.scvi-t...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### LRRC37B is a human modifier of voltage-gated sodium channels and axon excitability in cortical neurons. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.028 | PMCID: PMC10754148 | PMID: 38134874
- Evidence: 94 N/A pCAG-GEPH.FingR-tdTomato-IL2RGTC Gift from Juan Burrone (King’s College London, UK) N/A Software and algorithms R R project https://www.r-project.org/ Scanpy Scanpy https://scanpy.readthedocs.io/en/stable/ Matlab Mathworks https://www.mathworks.com/ Fidji ImageJ https://imagej.net/software/fiji/ GraphPad Prism https://www.graphpad.com/ Resource availability Lead contact Further information ...
- Full pipeline: stage not stated [ImageJ, R, Scanpy, ggplot2]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: 82 https://ImageJ.net/software/fiji/ syGlass VR syGlass https://www.syglass.io Scanpy v.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### The T-cell-directed vaccine BNT162b4 encoding conserved non-spike antigens protects animals from severe SARS-CoV-2 infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.007 | PMCID: PMC10099181 | PMID: 37164012
- Evidence: ....2 BD Biosciences N/A cellranger-6.0.1 10x Genomics N/A R v 4.1.0 The R Foundation N/A RStudio Posit N/A Python 3.9.15 Python Software Foundation N/A Scanpy PyPI N/A Scirpy PyPI N/A Muon PyPI N/A Spectrum Mill v BI.07.04.210 The Broad Institute of MIT and Harvard N/A Interactive Peptide Spectral Annotator tool Brademan et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Python v3.9.15, Scanpy]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: 35 https://github.com/slowkow/harmonypy Scanpy Wolf et al.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Version used: **1.8.2**
- Evidence: 74 N/A scanpy v1.8.2 and 1.9.1 Wolf et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: Quality control and cell filtering For all downstream analysis, we used the Scanpy package (referred to as sc from here on 54 , in Python 184 , 202 in addition to standard Python libraries such as numpy, pandas, matplotlib, csv, os, datetime 186 – 188 .
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: Clustering and analysis of the single cell data was performed using the Scanpy 62 python package.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Evidence: 81 We retrieved the raw count data using the scanpy package 84 (version 1.10.1), and then re-processed the data using the sctransform-based pipeline 130 from the R package Seurat.
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Version used: **1.9.3**
- Evidence: 166 We used the Scanpy (v.1.9.3) for the quality control, data integration, normalization, dimensionality reduction, clustering, and visualization.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Perturb-Multimodal: A platform for pooled genetic screens with imaging and sequencing in intact mammalian tissue. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.022 | PMCID: PMC12324982 | PMID: 40513557
- Evidence: ...lRanger 10x Genomics https://www.10xgenomics.com/software Custom Analysis Software This Paper https://github.com/weallen/InVivoMultimodalPerturbation Scanpy Ref.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose, XGBoost] -> stage not stated [AnnData, Scanpy]

### Simultaneous CRISPR screening and spatial transcriptomics reveal intracellular, intercellular, and functional transcriptional circuits. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.012 | PMCID: PMC12135205 | PMID: 40081369
- Evidence: Cell type labeling in the tumor Cell typing was performed using scanpy on log-transformed raw counts matrices.
- Full pipeline: stage not stated [Scanpy]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **1.9**
- Evidence: 225 https://numpy.org/ Scanpy (v1.9. ∗ ) Wolf et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### Spatially resolved cell atlas of the mouse primary motor cortex by MERFISH. (Nature 2021)

- DOI: 10.1038/s41586-021-03705-x | PMCID: PMC8494645 | PMID: 34616063
- Evidence: We used the scRNA-seq 10x v2 A dataset generated by a companion study 23 and determined highly variable genes using the Scanpy 46 package.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Scanpy, scDblFinder]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: Two-dimensional embedding using t -distributed stochastic neighbour embedding 59 ( t -SNE; perplexity = 30) was calculated based on the top principal components using the implementation from the scanpy package 60 .
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Evidence: Top 5,000 highly variable genes were identified with Scanpy 78 (v1.8.1) and z -score was scaled across all the cells.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Version used: **1.4.3**
- Evidence: Highly variable methylation features were selected with a modified approach using the scanpy.pp.highly_variable_genes function from the scanpy 1.4.3 package 40 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Evidence: This was computed 58 using scanpy.pp.highly_variable_genes with n_top_genes = 5000, flavor=seurat, and n_bins=20.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **1.4.4**
- Evidence: Highly variable methylation features were selected on the basis of a modified approach using the scanpy v1.4.4 package scanpy.pp.highly_variable_genes function 63 .
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Version used: **1.5.1**
- Evidence: RNA velocity and diffusion map pseudotime analyses For neural cell trajectory analysis we use scVelo 0.21 package implementation in Scanpy 1.5.1 74 .
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Skin-resident innate lymphoid cells converge on a pathogenic effector state. (Nature 2021)

- DOI: 10.1038/s41586-021-03188-w | PMCID: PMC8336632 | PMID: 33536623
- Evidence: Force-directed layout embedding and diffusion maps We computed a 30-nearest-neighbour graph with scanpy’s pp.neighbours function (v1.4.4.post1) [ 59 ] on the top 20 principal components of the Pearson residuals of the scTransformed data, for all cells and variable genes.
- Full pipeline: normalisation [SciPy, Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Scanpy, UMAP] -> visualisation [UMAP] -> stage not stated [Bioconductor]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **1.5.1**
- Evidence: Data were processed using Scanpy v1.5.1 62 , doublets were detected with scrublet v0.2.1 63 and removed, ambient RNA was corrected with FastCAR ( https://github.com/LungCellAtlas/FastCAR ), and multisample integration was performed with BBKNN v1.3.12 64 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Version used: **1.8.2**
- Evidence: Pseudotime trajectory analysis of Gut The Seurat object with scale data of Gut was converted to the h5ad file by the SeuratDisk (v.0.0.0.9013) R package 59 , and the h5ad file was then loaded to the python environment by the ‘sc.read’ function of the Scanpy (v.1.8.2) python package 60 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: All cells showing >200 counts were further merged across all samples and processed with scanpy 59 and the besca 60 standard workflow.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **1.6.0**
- Evidence: Count matrices were filtered, normalized, and log-transformed (min_shared_counts = 10, n_top_genes = 3000), cell cycle effect was corrected by regressing out S-phase and G2/M-phase scores, using Scanpy 1.6.0 67 .
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: Pearson correlation coefficients between cell types for each system, single-cell velocity profiles and latent times were computed using the Scanpy 69 v1.0 and scVelo 70 v0.2.4 tools.
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Evidence: Log normalization with a scaling factor of 10,000 was performed with scanpy’s 64 (v1.7.0) normalize_total function.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### A physical wiring diagram for the human immune system. (Nature 2022)

- DOI: 10.1038/s41586-022-05028-x | PMCID: PMC9365698 | PMID: 35922511
- Evidence: Processing of single-cell RNA-sequencing data Single-cell RNA-sequencing (RNA-seq) datasets 38 , 66 – 70 were processed following a standard data-cleaning pipeline using the Scanpy package in Python (v.1.4.5) 71 .
- Full pipeline: differential/statistical testing [DESeq2, Seurat] -> stage not stated [CellProfiler, PHENIX, Python, R v1.0.0, Scanpy, igraph]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Version used: **1.7.0**
- Evidence: Quality filters, alignment of data across different batches and clustering For scRNA-seq libraries, we integrated the filtered count matrices from Cell Ranger and analysed them with Scanpy v.1.7.0, with the pipeline following their recommended standard practices.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Evidence: Clustering and determination of homologous cell types Much of the analysis pipeline was based on scanpy infrastructure and AnnData data structures 49 .
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### Altered TMPRSS2 usage by SARS-CoV-2 Omicron impacts infectivity and fusogenicity. (Nature 2022)

- DOI: 10.1038/s41586-022-04474-x | PMCID: PMC8942856 | PMID: 35104837
- Version used: **1.7.1**
- Evidence: Scanpy v.1.7.1 was used to process the data.
- Full pipeline: read trimming [Bowtie2 v2.3.4.3] -> alignment/mapping [Bowtie2 v2.3.4.3] -> dimensionality reduction/clustering [Fiji] -> visualisation [ChimeraX v1.3] -> stage not stated [GROMACS, ImageJ, Pangolin, Scanpy v1.7.1]

### Molecularly defined and spatially resolved cell atlas of the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06808-9 | PMCID: PMC10719103 | PMID: 38092912
- Evidence: Then, we preprocessed the dataset using the Scanpy pipeline 70 : normalized the total count of each cell to 1,000, log1p transformed the counts and scaled the transformed counts to Z scores.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose v2.0] -> stage not stated [CellChat, scDblFinder, scikit-learn]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Evidence: Using the Scanpy package, we calculated the first 250 principal components of our subsampled cells.
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Most functions were derived from the allcools 9 , scanpy 73 and scikit-learn 74 packages.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### CD201&lt;sup&gt;+&lt;/sup&gt; fascia progenitors choreograph injury repair. (Nature 2023)

- DOI: 10.1038/s41586-023-06725-x | PMCID: PMC10665192 | PMID: 37968392
- Evidence: STAR (version 2.5.2a) was used for mapping the reads and to align them to the mm10 genome reference (provided by Drop‐seq group, GSE63269 ) that was tailored to include the eGFP cDNA transcript. scRNA-seq data analysis All the analyses were performed using the phyton toolkit Scanpy 50 and complementary tools under its ecosystem.
- Full pipeline: alignment/mapping [STAR v2.5.2a, Scanpy] -> quantification [Matplotlib, seaborn] -> dimensionality reduction/clustering [UMAP, scVelo] -> differential/statistical testing [SciPy] -> simulation/modelling [scVelo]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Evidence: The relevant subset of the MMCA data was preprocessed in Scanpy, but the metadata were inherited from the results generated in the section above entitled Cell clustering and annotation.
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: Using the library Scanpy 65 , the cell by feature matrix was first reduced in dimension using principal components analysis, then a neighbourhood graph of observations was computed using n = 5 neighbours, then a uniform manifold approximation and projection 66 manifold was computed, and finally clusters were identified on this manifold using Leiden clustering 67 .
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **1.7.2**
- Evidence: Additional cell and gene filtering was performed using scanpy (v.1.7.2) 57 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **1.6.0**
- Evidence: ...019b, R 4.0.4, RStudio 1.4.1106, Jupyter Notebook 6.0.3, Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-image 0.18.1, squidpy 1.1.2, anndata 0.8.0 and itertools 8.0.0.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Transgenic ferret models define pulmonary ionocyte diversity and function. (Nature 2023)

- DOI: 10.1038/s41586-023-06549-9 | PMCID: PMC10533402 | PMID: 37730992
- Evidence: The PAGA algorithm 34 , implemented using scanpy 53 , was used to project cells into a low-dimensional manifold, after defining unsupervised clusters generated using the Leiden algorithm 54 .
- Full pipeline: alignment/mapping [kallisto] -> variant calling [UMAP] -> quantification [R, Seurat] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [brms] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Evidence: We then use scanpy to compute principal components on this matrix, choosing an optimal number of principal components for data dimensionality based on kneepoint analysis of the cumulative variance described by each component, and visualize in two dimensions with UMAP (Extended Data Fig.
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Version used: **1.8.1**
- Evidence: Then UMAP embedding was conducted with Scanpy v.1.8.1 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: Then the data were overclustered with X-shift ( https://github.com/nolanlab/vortex ) or Leiden-based clustering with the scanpy Python package (v.1.9.1).
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Version used: **1.8.2**
- Evidence: Python (v.3), Pandas (v.1.3.5), NumPy (v.1.21.5), Matplotlib (v.3.5.2) and Scanpy (v.1.8.2 and v.1.9.1) were used for quality control and downstream processing.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### The dynamics of pattern matching in camouflaging cuttlefish. (Nature 2023)

- DOI: 10.1038/s41586-023-06259-2 | PMCID: PMC10322717 | PMID: 37380772
- Evidence: 5 )) was used to detect non-overlapping communities from the network of chromatophores 60 (scanpy package 61 ).
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> machine learning [Keras, OpenCV] -> visualisation [R, UMAP] -> stage not stated [PsychoPy, Scanpy]

### Injury prevents Ras mutant cell expansion in mosaic skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06198-y | PMCID: PMC10322723 | PMID: 37344586
- Version used: **1.6**
- Evidence: For interfollicular epidermis (IFE) keratinocytes, all mosaic samples were integrated and annotated using Scanpy (1.6-1.9) 64 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Scanpy v1.6, Seurat, SoupX, scDblFinder, scikit-learn v0.24.2]

### CD4<sup>+</sup> T cell-induced inflammatory cell death controls immune-evasive tumours. (Nature 2023)

- DOI: 10.1038/s41586-023-06199-x | PMCID: PMC10307640 | PMID: 37316667
- Evidence: Dimensionality reduction, unsupervised clustering and differential gene expression analyses Analysis of normalized data was performed using the scanpy Python package 60 .
- Full pipeline: quantification [velocyto] -> normalisation [AnnData, Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [ImageJ v1.52i, R, scVelo]

### Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06063-y | PMCID: PMC10171177 | PMID: 37165196
- Evidence: Uniform manifold approximation and projection visualizations were constructed using the python library Scanpy 59 .
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [Scanpy] -> stage not stated [Mutect2 v1.1.7, SciPy, SnpEff v4.3t, Strelka v1.0.15]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Version used: **1.7.1**
- Evidence: Quality filters, alignment of data across different batches and clustering We integrated the filtered count matrices from Cell Ranger and analysed them with scanpy (version 1.7.1), with the pipeline following their recommended standard practises.
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: For data preprocessing, we recommend using Scanpy ( https://scanpy.readthedocs.io/en/stable/ ) or Seurat ( https://satijalab.org/seurat/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Version used: **1.7.0**
- Evidence: RNA velocity was subsequently calculated using scVelo (v.0.2.2) 27 and further analysed using scanpy (v.1.7.0) 61 .
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Version used: **1.8.0**
- Evidence: Annotations of the healthy reference Cells from the core atlas were grouped by Scanpy (v1.8.0) leiden clustering into seven broad lineages based on marker gene expression (annotation level 1; Extended Data Fig.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: The droplets were then overclustered through the standard scanpy workflow using default parameters up to Leiden clustering.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **1.9.1**
- Evidence: Scanpy v.1.9.1 with anndata v.0.10.7 and the statistics and plotting libraries pandas v.2.2.2, numpy v.1.26.4, scipy v.1.13.0, seaborn v.0.13.2 and matplotlib v.3.8.4 were used for data analysis and visualization.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: Preprocessing of the HNOCA scRNA-seq data All processing and analyses were carried out using scanpy 81 (v.1.9.3) unless indicated otherwise.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Adult skull bone marrow is an expanding and resilient haematopoietic reservoir. (Nature 2024)

- DOI: 10.1038/s41586-024-08163-9 | PMCID: PMC11618084 | PMID: 39537918
- Evidence: 67 and the scanpy 68 (1.9.6) sc.tl.score_genes_cell_cycle function.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [Matplotlib, UMAP] -> visualisation [Matplotlib] -> stage not stated [AnnData, ImageJ, Scanpy]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Version used: **1.4.3**
- Evidence: Data pre-processing was performed using scanpy (v.1.4.3) 89 .
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **1.9.6**
- Evidence: Matrix files for each pair of samples (GFP and mCherry cells under the same treatment) were read with Scanpy (v.1.9.6) 118 and concatenated in the same AnnData object (v.0.10.3) 119 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Evidence: Principal component analysis (PCA) was then run using Scanpy 50 default parameters followed by k -nearest neighbours using only the top 20 principal components by the amount of variance explained and k = 15.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: We then merged all CellRanger outputs into a single Scanpy object 54 .
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Version used: **1.9.1**
- Evidence: All scRNA-seq data were preprocessed in Python using Scanpy v.1.9.1.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### Spatially clustered type I interferon responses at injury borderzones. (Nature 2024)

- DOI: 10.1038/s41586-024-07806-1 | PMCID: PMC11374671 | PMID: 39198639
- Evidence: Quality control, normalization and integration for RNA MERFISH Data analysis of RNA MERFISH data was performed with single-cell sequencing analysis tools such as Scanpy and Squidpy 53 , 54 .
- Full pipeline: quality control [Scanpy, Squidpy] -> normalisation [ImageJ, Scanpy, Seurat, Squidpy] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose, R, SoupX]

### Molecular mimicry in multisystem inflammatory syndrome in children. (Nature 2024)

- DOI: 10.1038/s41586-024-07722-4 | PMCID: PMC11324515 | PMID: 39112696
- Version used: **1.10.0**
- Evidence: Gene expression data from 59,572 pre-filtered cells were downloaded from the Gene Expression Omnibus database under accession GSE149689 for analysis and downstream processing with scanpy v1.10.0 (ref.
- Full pipeline: differential/statistical testing [Python, SciPy, scikit-learn, tidyverse v1.1.4] -> machine learning [scikit-learn] -> stage not stated [Scanpy v1.10.0, Seurat, igraph v2.0.3]

### A maternal brain hormone that builds bone. (Nature 2024)

- DOI: 10.1038/s41586-024-07634-3 | PMCID: PMC11306098 | PMID: 38987585
- Version used: **1.9**
- Evidence: Data were explored, and plots were generated using Scanpy (v.1.9).
- Full pipeline: read trimming [RSEM v1.2.21, STAR v2.4] -> alignment/mapping [RSEM v1.2.21, STAR v2.4, kallisto] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy v1.9, scDblFinder]

### The cortical amygdala consolidates a socially transmitted long-term memory. (Nature 2024)

- DOI: 10.1038/s41586-024-07632-5 | PMCID: PMC11306109 | PMID: 38961294
- Evidence: The MERFISH matrix for each section was concatenated, normalized, log-transformed with Scanpy 82 and integrated using Harmony 83 .
- Full pipeline: alignment/mapping [STAR v2.7.10a, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Cellpose, R v4.2.2, featureCounts v2.0.0]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: 5 , 6 , 31 – 33 were processed using the single-cell analysis Python workflow Scanpy 46 .
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **1.9.1**
- Evidence: Partition-based graph abstraction (PAGA) analysis 77 was performed using the Python package scanpy (v1.9.1).
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: Diffusion maps and force-directed graphs were generated in Scanpy 50 Python module v1.9.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Evidence: All of the datasets were processed and analysed using Scanpy 2 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **1.8.1**
- Evidence: Global clustering was performed using Scanpy (v.1.8.1) 63 in Python (v.3.7).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Version used: **1.6.1**
- Evidence: Trajectory analysis RNA velocity analysis was conducted using the scVelo package (v0.2.2) with Scanpy (v1.6.1) on Python (v3.8.5).
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Evidence: Gene expression for each cell was normalized (scanpy.pp.normalize_total, scaling factor 10,000) and log-transformed (scanpy.pp.log1p).
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: All subsequent analysis was implemented in Python (v.3.9.12) based on the Scanpy 42 (v.1.9.1) single-cell data analysis package, except where stated otherwise.
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **1.8**
- Evidence: Cell clustering analysis of MERFISH With the cell-by-gene matrix, we followed a standard procedure as suggested in the Scanpy (v.1.8) 75 tutorial using Python (v.3.9) for processing MERFISH data.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.9.1**
- Evidence: DGE matrices were processed using the following R and python packages: Seurat (v.3.2.2) 64 , SeuratDisk (v.0.0.0.9010) 65 , anndata (v.0.8.0) 66 , numpy (v.1.17.5) 67 , pandas (v.1.0.5) 68 , 69 and Scanpy (v.1.9.1) 70 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Version used: **1.9.1**
- Evidence: Gene level expression visualization of Krt8 and Plaur was generated using the scatter function from scanpy (v.1.9.1).
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Version used: **1.6.0**
- Evidence: The clustering was performed based on Scanpy v.1.6.0 20 .
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: The differential expression testing was performed by Wilcoxon test using Scanpy (sc.tl.rank_gene_group).
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Evidence: The secondary cell subclustering to match the ‘level 2’ annotation of the iHBCA was completed in Python (v3.10.13) using the Leiden algorithm through the scanpy package (v1.9.6) 59 .
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Evidence: Clustering and assignment of cell types Analysis of developmental data was based on the Scanpy package and tutorial 40 and to be consistent with a previous report 6 .
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: Mitochondrial content was assessed using the scanpy function calculate_qc_metrics ( https://scanpy-tutorials.readthedocs.io/en/latest/pbmc3k.html ).
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Version used: **1.9.1**
- Evidence: The resulting count matrix for each sample was processed and filtered using Scanpy (v.1.9.1) in Python (v.3.10) 56 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### A parabrachial hub for need-state control of enduring pain. (Nature 2025)

- DOI: 10.1038/s41586-025-09602-x | PMCID: PMC12630001 | PMID: 41062698
- Evidence: The stitched expression matrix, polygon, metadata, and FOV files were stored as unique variables and used to construct an annotated data (AnnData) object using Scanpy.
- Full pipeline: quantification [NumPy, Scanpy] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP, seaborn] -> visualisation [UMAP, seaborn] -> stage not stated [AnnData, ImageJ]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Version used: **1.9.5**
- Evidence: Quality control and preprocessing of the pan-cancer scRNA-seq data We applied rigorous quality control measures using the package Scanpy (v.1.9.5) 101 to filter and preprocess single-cell transcriptomic data.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Version used: **1.10.0**
- Evidence: Initial quality control and normalization Quality control and downstream analysis were performed in Python (v.3.8.8) using Scanpy (v.1.10.0), according to current expert recommendations for single-cell best practices 78 .
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **1.9.3**
- Evidence: The resulting raw count matrices and cell annotation files, together with the Ensembl GRCm39.110 gene annotations, were assembled into an Anndata object using scanpy v1.9.3.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Using Harmony-corrected principal components, we computed a neighbourhood graph (default Scanpy parameters) 57 and clustered cells with the Leiden algorithm (Scanpy implementation) 58 .
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: For scRNA-seq, output from the Cell Ranger software was analysed using two different pipelines: (1) Scanpy, which is explained in detail under the SCENIC+ analysis; and (2) the Seurat pipeline, which is explained below.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Version used: **1.9.8**
- Evidence: All the analyses were performed using scanpy (v1.9.8).
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Microglia regulate GABAergic neurogenesis in prenatal human brain through IGF1. (Nature 2025)

- DOI: 10.1038/s41586-025-09362-8 | PMCID: PMC12527950 | PMID: 40770097
- Version used: **1.10.3**
- Evidence: Once the data were collected and preprocessed, the pooled samples were processed using Scanpy v.1.10.3 ( https://github.com/scverse/scanpy ).
- Full pipeline: quantification [ImageJ v1.54] -> normalisation [UMAP] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [ImageJ v1.54] -> simulation/modelling [Monocle] -> visualisation [Monocle] -> stage not stated [CellChat, Enrichr, Scanpy v1.10.3, Seurat v5.1.0, scDblFinder v2.0.3]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: Mouse data were all from 10x data of Tabula Muris Senis 65 ( https://figshare.com/articles/dataset/Processed_files_to_use_with_scanpy_/8273102/2 ), except for the testis, which was based on a previously published 10x dataset 88 ( https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-6946 ).
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Next, all observations were combined into a single AnnData object, quality-control metrics were quantified and cell clustering was performed using the Python package scanpy 97 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: Then we calculated the PCA space on the highly variable genes, detected by Scanpy 61 , followed by correction of the PCA space with Harmonypy 62 using samples as batches.
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: Scanpy 76 and morphometrics were used to normalize, dimensionally reduce using PCA and cluster (Leiden) the dataset.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Version used: **1.10.1**
- Evidence: Scanpy (v.1.10.1) 58 was used for processing and plotting post-filtered nuclear transcriptomes.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Quality control and preprocessing of pan-cancer scRNA-seq data We performed quality control filtering and integration using the Scanpy package (v.1.9.5).
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Evidence: The analysis of the above data and corresponding plotting were conducted using the Python based software scanpy.
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Version used: **1.9.2**
- Evidence: The sequencing data was further processed with scanpy (1.9.2 76 ).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: Methods Single-cell data collection and preprocessing of healthy samples To assemble a comprehensive pan-tissue cell atlas, we collected scRNA-seq datasets and conducted quality control procedures via the Scanpy 48 toolkit, as detailed in subsequent sections (Extended Data Fig.
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Evidence: We then normalized each cell by its total transcript count using scanpy.pp.normlize_total().
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: UMAP, t -SNE and heat-map plotting was performed using the Scanpy 59 and scVelo 60 toolkits.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Cell cycle duration determines oncogenic transformation capacity. (Nature 2025)

- DOI: 10.1038/s41586-025-08935-x | PMCID: PMC12119354 | PMID: 40307557
- Evidence: Quality control and normalization After removing non-retinal cells, data was further processed and analysed mainly by Scanpy Python toolkit ( https://github.com/scverse/scanpy ) and Seurat R toolkit ( https://github.com/satijalab/seurat ).
- Full pipeline: quality control [Scanpy, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr]

### Spatially resolved mapping of cells associated with human complex traits. (Nature 2025)

- DOI: 10.1038/s41586-025-08757-x | PMCID: PMC12095064 | PMID: 40108460
- Evidence: We select HVGs based on the normalized variance of each gene, which adjusts for mean-variance associations, as implemented in Scanpy 59 .
- Full pipeline: alignment/mapping [R] -> variant calling [GCTA] -> normalisation [Scanpy] -> dimensionality reduction/clustering [PLINK, Seurat, clusterProfiler] -> differential/statistical testing [MAGMA] -> simulation/modelling [PLINK] -> stage not stated [LDSC]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **1.7.2**
- Evidence: SL-Smart-seq3xpress data analysis Count matrices were processed with JupyterLab (v.4) notebooks using IPython (v.7.31) using the following modules: pandas (v.1.5.3), numpy (v.1.23.5), scipy (v.1.10.1), scanpy (v.1.7.2), openpyxl (v.3.1.2), matplotlib (v.3.6.3) and seaborn (v.0.12.2).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Version used: **1.9.1**
- Evidence: To plot UMAPs, all Cell_Type from other species were transfered to human data by using SAMaps ‘transfer_annotations’-function, all results were visualized by Scanpy (v1.9.1).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: We subset Seurat objects by cell types (inhibitory, excitatory), then converted them first to H5 format (with SaveH5Seurat) and then to h5ad format for import in scanpy (with the Convert function from the SeuratDisk package https://github.com/mojaveazure/seurat-disk ).
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Evidence: Single-cell analysis Quality control Filtered count matrices generated by Cellranger (v6) were integrated into a single matrix using Scanpy 36 .
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Evidence: Results were visualized using scanpy and Seurat.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Evidence: Clustering analyses of grid-cell modules and bursting subtypes of grid cells were conducted using the python package Scanpy 87 and its dependencies (including numpy, pandas, scipy, scikit-learn and matplotlib).
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

### Engineered heart muscle allografts for heart repair in primates and humans. (Nature 2025)

- DOI: 10.1038/s41586-024-08463-0 | PMCID: PMC11903342 | PMID: 39880949
- Evidence: The Scanpy package was used for pre-filtering, normalization and clustering 40 .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: Leiden clustering was performed on the scVI learned embeddings using scanpy.tl.leiden with a resolution of 1, and every Leiden cluster was further subclustered at a resolution of 1.2.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: As it is difficult to adjust the hyperparameters of the birth–death problem, we also implemented a more intuitive and more easily adjustable estimation of the growth rates using 8 a i = exp p i − q i c where p i denotes a proliferation score and q i an apoptosis score, obtained using scanpy.tl.score_genes. c denotes a scaling parameter.
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: We used the function scanpy.tl.dpt with n_dcs=2.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Evidence: To guarantee that downstream analysis is not biased by the integration method, we used FastMNN 60 , implemented in SeuratWrappers, and BBKNN 61 , implemented in scanpy 62 , to redo the batch correction.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Timely TGFβ signalling inhibition induces notochord. (Nature 2025)

- DOI: 10.1038/s41586-024-08332-w | PMCID: PMC11735409 | PMID: 39695233
- Evidence: The remaining analyses were performed using Scanpy 81 (v1.7.0) unless otherwise indicated.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> stage not stated [PyTorch, R, Scanpy, scDblFinder]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: Cell-type clustering and identification For clustering, we converted each log-normalized gene expression value to a z -score using scanpy.pp.scale with max_value = 10 in the scanpy package 98 .
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### A cell atlas foundation model for scalable search of similar human cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08411-y | PMCID: PMC11864978 | PMID: 39566551
- Evidence: Data preprocessing All UMI count data were natural-log normalized per cell with a scaling factor of 10,000 using the scanpy.pp.normalize_to_target(adata, 10000) and scanpy.pp.log1p(adata) functions from scanpy 70 .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **1.9.1**
- Evidence: We then selected highly variable genes (HVGs) using the highly_variable_genes function in Scanpy (v.1.9.1) and flavour = seurat_v3 (we chose bins = 40).
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: In brief, total read depth was normalized per cell using counts-per-10,000 (CP10k) scaling (normalize_total function in Scanpy 256 v1.9.6 package, with target_sum = 1 × 10 4 ), followed by log1p transformation to stabilize variance.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Eosinophils drive intestinal remodelling and innate defence in reproduction. (Nature 2026)

- DOI: 10.1038/s41586-026-10531-6 | PMCID: PMC13233317 | PMID: 42129565
- Version used: **1.8.2**
- Evidence: Data were analysed using Scanpy (v.1.8.2).
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Scanpy v1.8.2]

### Pervasive and programmed nucleosome distortion on single chromatin fibres. (Nature 2026)

- DOI: 10.1038/s41586-026-10418-6 | PMCID: PMC13253354 | PMID: 42056506
- Version used: **1.9.3**
- Evidence: UMAP visualization of footprint types within epigenomic domains and at repeat sequences From accessibility data for footprints within histone-modification-defined domains and at mouse repeat elements, we used Scanpy (v.1.9.3) for principal component analysis (PCA)-based dimensionality reduction, construction of a k -nearest neighbours graph (metric = correlation, n _neighbours = 15) and UMAP visua...
- Full pipeline: dimensionality reduction/clustering [ChimeraX v1.7.1, Python, Scanpy v1.9.3, UMAP] -> visualisation [ChimeraX v1.7.1, Scanpy v1.9.3, UMAP] -> stage not stated [SciPy]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: All samples were merged and preprocessed and analysed together using scanpy.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Early fibrotic niches establish tumour-permissive microenvironments. (Nature 2026)

- DOI: 10.1038/s41586-026-10399-6 | PMCID: PMC13149335 | PMID: 42020743
- Evidence: Quality control Analysis of count matrices was performed in R using the Seurat package 59 or Scanpy 60 pipeline (v.1.9.1).
- Full pipeline: quality control [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [CellChat, Fiji, ImageJ, QuPath]

### A spatial atlas of the healthy human liver from live donors. (Nature 2026)

- DOI: 10.1038/s41586-026-10377-y | PMCID: PMC13216088 | PMID: 41986723
- Version used: **1.10.0**
- Evidence: The Harmony-corrected PCs were used to build the neighbourhood graph and UMAP visualization, using Scanpy (version 1.10.0) standard functions (n_neighbors = 20, resolution = 1.7).
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> machine learning [QuPath] -> visualisation [Scanpy v1.10.0] -> stage not stated [AnnData, Cellpose, GSEA]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: We ran Scanpy’s (v.1.9.5) highly variable genes routine with the default settings, except for 40 mean-variance bins, and selected the top 200 genes per batch; a gene was retained as a highly variable gene if it was called variable in ≥2 batches.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: We used the Deep Embedding for Single-cell Clustering (DESC, v.2.1.1) 59 package for dimension deduction, batch normalization and clustering, using the top 2,048 high DEGs (scanpy 60 , v.1.8.1) and a three-layer encoder network (1,024, 256, 32) for feature extraction.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Expansion of outer cortical CUX2 neurons requires adaptations for DNA repair. (Nature 2026)

- DOI: 10.1038/s41586-026-10290-4 | PMCID: PMC13190340 | PMID: 41922774
- Version used: **1.8.1**
- Evidence: Cell-type annotation and clustering Downstream analyses were done mainly using Scanpy (v.1.8.1) and DESC (v.2.1.1).
- Full pipeline: variant calling [UMAP] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [R, Scanpy v1.8.1, UMAP, clusterProfiler]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **1.9.3**
- Evidence: Single-cell sequencing and pseudobulk analyses Single-cell RNA-seq datasets from multiple human tissues were processed for tissue-specific pseudobulk analysis using Python (v.3.9.12) with Scanpy (v.1.9.3), Pandas (v.1.5.3) and Numpy (v.1.24.4).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: Scanpy was used for single-cell analysis and plotting ( https://scanpy.readthedocs.io/en/stable/ ).
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: The UMI count matrix underwent preprocessing utilizing the Scanpy package (v.1.9.2) and the Seurat R package (v.2.4.3).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Ontogeny and transcriptional regulation of Thetis cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10198-z | PMCID: PMC13171621 | PMID: 41634202
- Evidence: For the 3′ scRNA-seq data, analysis was done using Scanpy as per the steps above, with the first 50 principal components and 25 nearest neighbours.
- Full pipeline: read trimming [Seurat v4.4.0] -> alignment/mapping [STAR v2.7.11a] -> dimensionality reduction/clustering [ArchR v1.0.3, Scanpy, UMAP] -> visualisation [ArchR v1.0.3, UMAP]

### Dissecting gene regulatory networks governing human cortical cell fate. (Nature 2026)

- DOI: 10.1038/s41586-025-09997-7 | PMCID: PMC12999477 | PMID: 41565813
- Evidence: The resulting counts were processed by Scanpy 109 to remove low quality cells containing fewer than 1,000 genes, a high abundance of mitochondrial reads (greater than 15% of total transcripts) or a high abundance of ribosomal reads (greater than 40% of total transcripts).
- Full pipeline: quantification [Scanpy, velocyto] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Monocle, SCENIC, scVelo]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Evidence: After quality control-based filtering, Scanpy 80 was used to normalize cells by means of counts per million normalization (UMI count per cell was set to 10 6 ) and log 1 p transformation (natural log of counts per million plus one).
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Data were analysed using the scanpy implementation 54 . scRNA-seq analysis and cell type identification Gene expression normalization was performed on the combined scRNA-seq dataset to account for differences in sequencing depth across cells.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: Gene expression profiles were normalized and scaled using standard Scanpy procedures 70 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: Further analysis was performed using scanpy 79 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: In brief, we used the scanpy 97 function sc.tl.score_genes() to compute the score and then performed the Jonckheere’s trend test 98 with the alternative hypothesis ‘decreasing’ (2000 permutations) to quantify the significance of the trend.
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Human gut M cells resemble dendritic cells and present gluten antigen. (Nature 2026)

- DOI: 10.1038/s41586-025-09829-8 | PMCID: PMC12872457 | PMID: 41372409
- Evidence: Analysis was performed in Python (v.3.11.9) using the Scanpy library and the recipe based on Wu et al.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler v3.14.3] -> visualisation [Seurat v3.1.4] -> stage not stated [Enrichr, Python v3.11.9, R, Scanpy]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **1.9.1**
- Evidence: Pre-processing of scRNA-seq and snRNA-seq data scRNA-seq and snRNA-seq samples were processed independently using scanpy (v.1.9.1) for Python (v.3.9) 67 .
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **1.11.2**
- Evidence: Cells with less than 10 counts were discarded using scanpy.pp.filter_cells(min_counts=10) (scanpy v1.11.2).
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Evidence: Graph-based clustering was performed using the default Leiden algorithm implemented in Scanpy.
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Evidence: To generate UMAPs for these data, we did the following, using Python and the single-cell analysis libraries Scanpy and AnnData: for each of the four scRNA-seq datasets, the raw counts were filtered to contain genes represented in a minimum of 30 cells.
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Version used: **1.4.3**
- Evidence: Many of the described preprocessing steps are done via the Python packages Scanpy, version 1.4.3, and AnnData, version 0.6.22 ( 50 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Hedgehog-interacting protein acts in the habenula to regulate nicotine intake. (PNAS 2022)

- DOI: 10.1073/pnas.2209870119 | PMCID: PMC9674224 | PMID: 36346845
- Evidence: 6000 platforms, with reads mapped to a reference genome using CellRanger from 10x Genomics, and transcriptomes clustered using the Scanpy toolkit ( 53 ) ( Materials and Methods ) ( Fig.
- Full pipeline: alignment/mapping [HTSeq, STAR, Scanpy] -> quantification [HTSeq] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Enrichr]

### Splice factor polypyrimidine tract-binding protein 1 (Ptbp1) primes endothelial inflammation in atherogenic disturbed flow conditions. (PNAS 2022)

- DOI: 10.1073/pnas.2122227119 | PMCID: PMC9335344 | PMID: 35858420
- Evidence: Statistical analysis was generally performed in GraphPad Prism, with the exception of single-cell analysis (performed in Scanpy, as described in the previous section and figure legends) and GTEx analysis (performed in R using corr function).
- Full pipeline: differential/statistical testing [GSEA, Scanpy]

### Cellular and transcriptional diversity over the course of human lactation. (PNAS 2022)

- DOI: 10.1073/pnas.2121720119 | PMCID: PMC9169737 | PMID: 35377806
- Evidence: For each milk stage, all samples were combined into a single Scanpy object, cells were filtered with parameters: >400 genes, >750 UMI, <750 counts, <20% UMIs from mitochondrial genes.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [DESeq2, SciPy, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [Enrichr, R v3.6.2, Scanpy, Seurat, scDblFinder]

### Gene expression in the primate orbitofrontal cortex related to anxious temperament. (PNAS 2023)

- DOI: 10.1073/pnas.2305775120 | PMCID: PMC10710052 | PMID: 38011550
- Evidence: The final counts file was analyzed using Scanpy ( 31 ) with methods detailed in SI Appendix , Materials .
- Full pipeline: alignment/mapping [Python v2.7] -> stage not stated [CellProfiler v4.2.1, ImageJ v1.53s, QuPath, Scanpy, limma, scDblFinder]

### Controlling donor and newborn neuron migration and maturation in the eye through microenvironment engineering. (PNAS 2023)

- DOI: 10.1073/pnas.2302089120 | PMCID: PMC10655587 | PMID: 37931105
- Evidence: We used Python- and R-based dependencies to process the data by utilizing the packages for the main [Seurat ( 67 ) and scanpy ( 68 ), gene set enrichment analysis [escape ( 69 ), and pseudo-time/cell fates [scFates ( 70 ) analyses.
- Full pipeline: quantification [ImageJ] -> stage not stated [Scanpy, Seurat]

### mitoSplitter: A mitochondrial variants-based method for efficient demultiplexing of pooled single-cell RNA-seq. (PNAS 2023)

- DOI: 10.1073/pnas.2307722120 | PMCID: PMC10523499 | PMID: 37725654
- Version used: **1.9.1**
- Evidence: We used scanpy v1.9.1 ( 37 ) to select high-variable SNPs across bulk samples from a mitochondrial mutation matrix for mitochondrial genotyping.
- Full pipeline: alignment/mapping [Cutadapt v1.18, STAR v2.7.3a, minimap2 v2.24] -> variant calling [Scanpy v1.9.1, minimap2 v2.24] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> stage not stated [scikit-learn v1.0.2]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Evidence: PAGA ( 33 ) from the Scanpy toolkit ( 68 ) was used for trajectory inference on in vitro and Tx-RPE cells, which is based on estimating connectivity between manifold partitions from a topology preserving map of the cells.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### Direct neuronal reprogramming by temporal identity factors. (PNAS 2023)

- DOI: 10.1073/pnas.2122168120 | PMCID: PMC10175841 | PMID: 37126716
- Version used: **1.9.1**
- Evidence: Filtered output files were analyzed in Python (Python core team, Python) using Scanpy version 1.9.1 ( 75 ).
- Full pipeline: quality control [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, Signac] -> stage not stated [Python, Scanpy v1.9.1]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Version used: **1.9.1**
- Evidence: For SI3 and SI4 data, cells labeled with hashtags for ileal cells were extracted using R 4.1.2, Seurat 4.1.0, Scanpy 1.9.1, and python 3.9.12 and then used for analysis.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### In vivo CRISPR screens identify &lt;i&gt;Mga&lt;/i&gt; as an immunotherapy target in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406325121 | PMCID: PMC11441491 | PMID: 39298484
- Evidence: Scanpy ( 53 ) was used for processing the scRNA-seq data.
- Full pipeline: alignment/mapping [HISAT2] -> variant calling [CellChat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [HTSeq v0.6.1p, Scanpy]

### NRF2 is a spatiotemporal metabolic hub essential for the polyfunctionality of Th2 cells. (PNAS 2024)

- DOI: 10.1073/pnas.2319994121 | PMCID: PMC11252815 | PMID: 38959032
- Evidence: Consistent with flow cytometric analyses and BAL fluid cytokine data, CD4 + T cells from CD4 ΔNRF2 mice consisted of less Th2 cells than littermates with a significant reduction in Th2-ness score calculated from Il4 , Il5 , Il13 , Gata3 , Pparg , Il1rl1 , and Areg expression using Scanpy ( Fig.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP] -> stage not stated [Scanpy]

### A time-resolved single-cell roadmap of the logic driving anterior neural crest diversification from neural border to migration stages. (PNAS 2024)

- DOI: 10.1073/pnas.2311685121 | PMCID: PMC11087755 | PMID: 38683994
- Evidence: In the cells of interest (Ectoderm and NC cells), mean counts number was 1,778, and mean gene number 1035. scRNA-seq postprocessing was done using Scanpy ( 59 ).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy]

### Pharmacological expansion of type 2 alveolar epithelial cells promotes regenerative lower airway repair. (PNAS 2024)

- DOI: 10.1073/pnas.2400077121 | PMCID: PMC11032444 | PMID: 38598345
- Evidence: The resulting expression matrices were processed using the scanpy package (v1.9.1, https://scanpy.readthedocs.io/en/stable/ ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> stage not stated [Scanpy, scDblFinder]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Evidence: Data normalization was achieved using the “scanpy.pp.normalize_total” function.
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### A spatiotemporal molecular atlas of the ovulating mouse ovary. (PNAS 2024)

- DOI: 10.1073/pnas.2317418121 | PMCID: PMC10835069 | PMID: 38252830
- Evidence: Slide-seq count matrix and the position information for every bead barcode were loaded into an AnnData object using scanpy ( 54 ) (v1.9.1).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SCENIC, scikit-learn] -> visualisation [Squidpy] -> stage not stated [AnnData, CellPhoneDB, Scanpy]

### Adipose-tissue regulatory T cells are a consortium of subtypes that evolves with age and diet. (PNAS 2024)

- DOI: 10.1073/pnas.2320602121 | PMCID: PMC10823167 | PMID: 38227656
- Evidence: Downstream analysis was done with the scanpy python package ( 46 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Scanpy, scVelo]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: ( F ) Heatmap displaying key marker gene expression across cell types, with scores from the rank_genes_groups function in Scanpy colored brown (high) and purple (low).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### HIF2α negatively regulates MYCN protein levels and promotes a low-risk noradrenergic phenotype in neuroblastoma. (PNAS 2025)

- DOI: 10.1073/pnas.2516922122 | PMCID: PMC12582314 | PMID: 41118218
- Evidence: Plots were done using Scanpy.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2, FastQC, GSEA] -> visualisation [UMAP] -> stage not stated [R, Scanpy, Seurat]

### Higher-order interactions in neuronal function: From genes to ionic currents in biophysical models. (PNAS 2025)

- DOI: 10.1073/pnas.2500048122 | PMCID: PMC12519081 | PMID: 41021808
- Evidence: We analyzed single-cell RNA-seq data using Scanpy ( 45 ), applying standard preprocessing, log-transformation, and gene-wise standardization.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy]

### A TGF-βR/IL-2R immunomodulatory fusion protein transforms immunosuppression into T cell activation to enhance adoptive T cell therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2516951122 | PMCID: PMC12501114 | PMID: 40986340
- Evidence: Aligned single cell read data were further processed using custom code based around the Scanpy package ( 59 ) in Python 3.
- Full pipeline: alignment/mapping [Python, Scanpy] -> stage not stated [GSEA v4.1.0, scDblFinder]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Version used: **1.9.1**
- Evidence: We then filtered out low-quality cells and doublets with scanpy (v1.9.1) ( 41 ).
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### &lt;i&gt;Sox11&lt;/i&gt; genes affect neuronal differentiation in the developing zebrafish enteric nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2510548122 | PMCID: PMC12342651 | PMID: 40789027
- Evidence: Scanpy package83 was then used for analysis.
- Full pipeline: alignment/mapping [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Python, Scanpy]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Scanpy was used for further quality control, filtering, clustering, and downstream analysis ( 27 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Downregulation of Nesprin1 by Runx2 deficiency is critical for the development of skeletal laminopathy-like pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2320138122 | PMCID: PMC12012476 | PMID: 40208950
- Evidence: Single-cell RNA-seq data were processed with STARsolo and analyzed using Scanpy in Python.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP, scVelo] -> stage not stated [Galaxy, ImageJ, Python, Scanpy, deepTools]

### Lung B cells in ectopic germinal centers undergo affinity maturation. (PNAS 2025)

- DOI: 10.1073/pnas.2416855122 | PMCID: PMC12002176 | PMID: 40168127
- Version used: **1.10.4**
- Evidence: Analysis of transcriptomic data was done in Python using Scanpy (v1.10.4) ( 62 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3.1] -> stage not stated [Python, Scanpy v1.10.4]

### Single cell-resolved cellular, transcriptional, and epigenetic changes in mouse T cell populations linked to age-associated immune decline. (PNAS 2025)

- DOI: 10.1073/pnas.2425992122 | PMCID: PMC12002302 | PMID: 40163732
- Version used: **1.4.6**
- Evidence: Quality control. scRNA-seq data from 83 mice across 10 ages were filtered using Scanpy (v.1.4.6) based on UMI counts, gene detection ratios, and mitochondrial gene expression.
- Full pipeline: quality control [Scanpy v1.4.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [ArchR v1.0.1, MACS2, Seurat, UMAP]

### Spatial profiling of the interplay between cell type- and vision-dependent transcriptomic programs in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421022122 | PMCID: PMC11848306 | PMID: 39946537
- Evidence: We used scanpy.tl.rank_genes_groups to identify differentially expressed genes (DEGs) if a gene meets the following criteria: a) false discovery rate (FDR) < 0.05 based on Wilcoxon rank-sum test; b) fold change > 2, and c) the gene was expressed in >30% cells in the up-regulated type.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [Enrichr, NumPy, SciPy, scikit-learn, seaborn]

### Diffusive topology preserving manifold distances for single-cell data analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2404860121 | PMCID: PMC11789025 | PMID: 39854240
- Evidence: Summary of single-cell datasets used in this study Datasets Number of cells Download link Paul 2,730 “scanpy.datasets.paul15()” Nestorowa 1,656 https://github.com/theislab/paga/blob/master/blood/nestorowa16/nestorowa16.ipynb Pancreas 3,696 https://scvelo.readthedocs.io/en/stable/scvelo.datasets.pancreas/ Lymphoid 8,221 https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129785 Embryoid Body 16,8...
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> visualisation [UMAP] -> stage not stated [Monocle, Scanpy, scVelo]

### Gonadal sex and temperature independently influence germ cell differentiation and meiotic progression in &lt;i&gt;Trachemys scripta&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2413191121 | PMCID: PMC11725912 | PMID: 39793067
- Evidence: Both the UMAP dimensionality reduction and the clusters were calculated from SCVI latent variables using scanpy ( https://github.com/scverse/scanpy ).
- Full pipeline: dimensionality reduction/clustering [Scanpy, UMAP, clusterProfiler]

### Collagen-producing eye cell atlas reveals distinct fibroblast fates in early injury vs. fibrotic subretinal disease. (PNAS 2026)

- DOI: 10.1073/pnas.2519056123 | PMCID: PMC13320955 | PMID: 42361041
- Version used: **1.9.6**
- Evidence: Secondary analysis utilized Scanpy (v1.9.6).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Scanpy v1.9.6]

### APOBEC2 deficiency disrupts hematopoietic lineage commitment, resulting in emergence of dual identity lymphocytes in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2531122123 | PMCID: PMC13250534 | PMID: 42247564
- Evidence: Data were processed using Cell Ranger and analyzed in Scanpy, including filtering, normalization, and exclusion of receptor-related genes.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, scDblFinder]

### Spatially structured inflammatory response in the presence of a uniform stimulus. (PNAS 2026)

- DOI: 10.1073/pnas.2507102123 | PMCID: PMC13012133 | PMID: 41860960
- Evidence: To identify candidate genes that activated in epithelial tissue, the software packages decontX, scrublet (run in RStudio), and scanpy (run in Python v3.7) were used to generate quality scores for cells; cells with >12% mitochondrial reads, scrublet score >0.3, or decontX score >0.5, were eliminated, as well as genes expressed in <10 cells.
- Full pipeline: stage not stated [ImageJ, Python v3.7, Scanpy, scikit-image]

### Single-cell analyses identify independent aging processes that compete to determine cellular fate in budding yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2534452123 | PMCID: PMC12993945 | PMID: 41811451
- Version used: **1.11.0**
- Evidence: Subsequent analysis was done using scanpy (v1.11.0).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, kallisto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Scanpy v1.11.0, statsmodels]

### Pareto optimality reveals an atlas of cellular archetypes. (PNAS 2026)

- DOI: 10.1073/pnas.2530194123 | PMCID: PMC12993957 | PMID: 41802062
- Version used: **1.10.3**
- Evidence: Additional preprocessing and filtering for the present study was performed in python 3.9 using Scanpy v1.10.3 (custom fork modified to add the intercept back to the results of scanpy.pp.regress_out(): https://github.com/ggit12/scanpy ).
- Full pipeline: alignment/mapping [igraph v1.5.1] -> dimensionality reduction/clustering [WGCNA, igraph v1.5.1] -> simulation/modelling [WGCNA] -> structure determination [WGCNA] -> stage not stated [R v0.0.0.9000, Scanpy v1.10.3]

### Olfactory inputs to appetite neurons in the hypothalamus. (PNAS 2026)

- DOI: 10.1073/pnas.2524926123 | PMCID: PMC12867749 | PMID: 41591908
- Version used: **1.9**
- Evidence: The imputed, cell-by-gene expression matrix (downloaded from the “ABC Atlas Cache”) was processed using Scanpy v1.9 and AnnData v0.10 in Python 3.12.
- Full pipeline: alignment/mapping [Cufflinks] -> quantification [AnnData v0.10, Cufflinks, Matplotlib v3.8, Scanpy v1.9] -> visualisation [Matplotlib v3.8, Python]

### A temporal and spatial atlas of adaptive immune responses in the lymph node following viral infection. (PNAS 2026)

- DOI: 10.1073/pnas.2504742123 | PMCID: PMC12867689 | PMID: 41587309
- Version used: **1.9.8**
- Evidence: By integrating the corresponding bead barcode location files downloaded from Curio Bioscience website, slide-seq count matrix with spatial position information for each sample was generated and loaded into an AnnData object using Scanpy (v1.9.8) ( 60 ).
- Full pipeline: stage not stated [AnnData, Docker, Scanpy v1.9.8, SciPy]

### Functionally heterogeneous intratumoral CD4&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; double-positive T cells can give rise to single-positive T cells. (PNAS 2026)

- DOI: 10.1073/pnas.2506168123 | PMCID: PMC12849695 | PMID: 41557789
- Evidence: Filtered single-cell gene expression matrices (Cell Ranger v3.0.2, hg38) were processed using the scanpy ( 60 ) toolkit.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler, Monocle, Scanpy]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Evidence: Data integration and annotation Data normalization and preprocessing were performed using the Scanpy workflow (v1.8.1) ( 79 ).
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### Cross-tissue immune cell analysis reveals tissue-specific features in humans. (Science 2022)

- DOI: 10.1126/science.abl5197 | PMCID: PMC7612735 | PMID: 35549406
- Version used: **1.6.0**
- Evidence: Downstream analysis from data normalization to graph-based clustering were performed using Scanpy (version 1.6.0) ( 69 ), with details described in Supplementary Materials .
- Full pipeline: normalisation [Scanpy v1.6.0] -> dimensionality reduction/clustering [Scanpy v1.6.0, UMAP] -> visualisation [UMAP] -> stage not stated [PHENIX, scDblFinder]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: ...and expressing >5000 reads) ( data S4 , S19 , and S22 ). scRNA-seq count matrix transformation, normalization, and preprocessing were performed using Scanpy ( 62 ) (v1.9.0) in python (v3.8.6).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### The dawn of spatial omics. (Science 2023)

- DOI: 10.1126/science.abq4964 | PMCID: PMC7614974 | PMID: 37535749
- Evidence: Tools designed for disaggregated data [such as the Seurat, ScateR, Scanpy, and Monocle packages ( 90 – 94 )] can provide good results but need to be used cautiously because the nuances of data generation can cause biases.
- Full pipeline: stage not stated [Monocle, Scanpy, Seurat]

### High-resolution spatial mapping of cell state and lineage dynamics in vivo with PEtracer. (Science 2025)

- DOI: 10.1126/science.adx3800 | PMCID: PMC12766569 | PMID: 40705858
- Version used: **1.10.0**
- Evidence: Processed data were analyzed using Scanpy (v1.10.0) ( 160 ) following standard best practices: data were normalized and log-transformed, 2,000 highly variable genes were identified, and the data were scaled and reduced to 20 principal components (PCs).
- Full pipeline: alignment/mapping [Python, scikit-image v0.24.0] -> normalisation [Scanpy v1.10.0] -> dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> stage not stated [Cellpose v3.1.0, R v4.2.3, Seurat, Squidpy v1.6.2, scDblFinder]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Clusters were obtained with agglomerative clustering using Scanpy ( 97 ): principle components were computed using solver = “arpack”; a neighborhood graph was computed using n_neighbors = 30 and n_pcs = 20; a uniform manifold approximation and projection (UMAP) embedding was computed ( 98 ); and clusters were assigned using leiden clustering on the UMAP embedding ( 99 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Evidence: Single-cell expression analysis The cell × gene count matrix was normalized by the library size of each cell using Scanpy ( 78 ) after removing genes that were expressed in <10 cells.
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Then, a k -nearest neighbor (k-NN) graph ( k = 15, cosine metric) was computed in the latent SVD space ('X_svd') using sc.pp.neighbors from Scanpy ( 84 ).
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries as described before ( 49 , 52 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

