# Seurat

- **Category:** single-cell
- **Papers in survey:** 767
- **Journals:** Nature (377), PNAS (304), Cell (59), Science (27)
- **Years:** 2021 (58), 2022 (96), 2023 (130), 2024 (169), 2025 (216), 2026 (98)
- **Versions named:** 4.3.0 (37), 4.1.0 (24), 5.1.0 (18), 4.1.1 (18), 5.0.1 (12), 4.0.3 (12), 3.2.2 (12), 4.0.4 (10), 4.0 (9), 4.0.2 (9)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (199), normalisation (109), quality control (51), visualisation (49), differential/statistical testing (48), alignment/mapping (27), quantification (22), read trimming (9), simulation/modelling (3), structure determination (2), variant calling (1), machine learning (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **3.2.2**
- Evidence: ... GSEA 2.0 Subramanian et al., 2005 https://www.gsea-msigdb.org/gsea/index.jsp R version 3.6.3 R Core Team, 2020 https://cran.r-project.org/ R package Seurat version 3.2.2 Stuart et al., 2019 https://cran.r-project.org/web/packages/Seurat/index.html R package leiden version 0.3.3 Traag et al., 2019 ; Kelly, 2019 https://cran.r-project.org/web/packages/leiden/index.html R package scran version 1.14....
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Microenvironment drives cell state, plasticity, and drug response in pancreatic cancer. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.017 | PMCID: PMC8822455 | PMID: 34890551
- Version used: **2.3.4**
- Evidence: Initial exploration of the data was performed using the R package Seurat (v2.3.4) and followed two steps: 1) SNN-guided quality assessment and 2) cell type composition determination.
- Full pipeline: quality control [RSEM] -> alignment/mapping [GATK v1.6] -> registration [GATK v1.6] -> differential/statistical testing [R v4.0] -> stage not stated [Mutect2 v1.1.45, Picard, Python v3.7.4, Seurat v2.3.4]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Version used: **3.2.2**
- Evidence: ...B Integrated DNA Technologies N/A Software and Algorithms R Project for Statistical Computing 4.0.2 R Core Team https://www.r-project.org R package – Seurat v3.2.2 Github https://github.com/satijalab/seurat R package – DESeq2 v1.30.0 Bioconductor https://bioconductor.org/packages/DESeq2/ R package – Circlize v0.4.11 CRAN https://CRAN.R-project.org/package=circlize R package – ggplot2 v3.3.2 CRAN h...
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Endogenous retroviruses promote homeostatic and inflammatory responses to the microbiota. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.020 | PMCID: PMC8381240 | PMID: 34166614
- Evidence: ...tascape.org/gp/index.html#/main/step1 RRID: SCR_016620 Prism software version 9 GraphPad RRID: SCR_002798 R version 4.05 http://www.r-project.org N/A Seurat package version 4.0 Hao et al., 2021 RRID: SCR_007322 STAR aligner version 2.7.5 Dobin et al., 2013 RRID: SCR_015899 Other Adjusted Calories Diet (60% Fat Kcal, Irradiated) - High Fat Diet Envigo Teklad Diets Cat #TD.06414 Control Diet (10% Fa...
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [Metascape, R v4.05, STAR, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### SARS-CoV-2 mRNA vaccination induces functionally diverse antibodies to NTD, RBD, and S2. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.005 | PMCID: PMC8185186 | PMID: 34192529
- Version used: **3.2.2**
- Evidence: ...smid https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5584442/ N/A Software and algorithms Cell Ranger (v5) 10x Genomics https://support.10xgenomics.com/ Seurat (v3.2.2) Stuart et al., 2019 https://satijalab.org/seurat/ scRepertoire (v1.1.3) Borcherding et al., 2020 https://github.com/ncborcherding/scRepertoire schex (v1.3.0) Saskia Freytag https://github.com/SaskiaFreytag/schex IgBLAST v1.14.0 Ye et ...
- Full pipeline: quantification [PyMOL] -> normalisation [igraph v1.2.6] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [PyMOL] -> visualisation [PyMOL, UMAP] -> stage not stated [R v4.0.2, Seurat v3.2.2]

### Integrated analysis of multimodal single-cell data. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.048 | PMCID: PMC8238499 | PMID: 34062119
- Version used: **3.2.0**
- Evidence: ...t_al_Nat_Med_DOI_https_d/4753772 Human PBMC – scRNA-seq Wilk et al., 2020 https://www.covid19cellatlas.org/index.patient.html Software and algorithms Seurat v4 This paper https://github.com/satijalab/seurat Azimuth This paper https://azimuth.hubmapconsortium.org/ Seurat v3.2.0 Stuart et al., 2019 https://github.com/satijalab/seurat/releases/tag/v3.2.0 SCTransform v0.3.2 Hafemeister and Satija, 201...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat v3.2.0, Signac v1.0.0]

### Fab-dimerized glycan-reactive antibodies are a structural category of natural antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.042 | PMCID: PMC8135257 | PMID: 34019795
- Evidence: Matrices of cell barcodes and gene counts generated by Cell Ranger were loaded into Seurat R package (v3.2.0) for graph-based cell clustering, dimensionality reduction and data visualization ( Macosko et al., 2015 ; Satija et al., 2015 ; Stuart et al., 2019 ).
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, R, Seurat, UMAP] -> stage not stated [PyMOL, RELION, UCSF Chimera, ggplot2]

### Charting human development using a multi-endodermal organ atlas and organoid models. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.028 | PMCID: PMC8208823 | PMID: 34019796
- Version used: **3.1**
- Evidence: ...X2.3 ACD Cat#581651 Software and algorithms R (version 3.6.0) N/A https://www.r-project.org Cell Ranger N/A https://github.com/10XGenomics/cellranger Seurat (version 3.1) Butler et al., 2018 https://github.com/satijalab/seurat simspec He et al., 2020 https://github.com/quadbiolab/simspec SPRING Weinreb et al., 2018 https://github.com/AllonKleinLab/SPRING e1071 N/A https://github.com/cran/e1071 pre...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB v2.0, R v3.6.0, SCENIC, Seurat v3.1, igraph]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...tps://bioconductor.org/packages/release/bioc/html/fgsea.html DoubletFinder McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder Seurat Stuart et al., 2019 https://satijalab.org/seurat/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ChIP-seq Analysis pipeline This study https://github.com/MarioPujato/NextGenAligner bedtools Quinlan and...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.053 | PMCID: PMC7857060 | PMID: 33657410
- Version used: **2.3.0**
- Evidence: ...ab/kallisto bustools v0.39.3 Melsted et al., 2019 https://github.com/BUStools/bustools STARTRAC Zhang et al., 2018 https://github.com/Japrin/STARTRAC Seurat 2.3.0/3.0 ( Butler et al., 2018 ) http://satijalab.org/seurat scanpy 1.4.6/1.5.1 Wolf et al., 2018 https://scanpy.readthedocs.io/en/latest/ CSOmap Ren et al., 2020 https://github.com/zhongguojie1998/CSOmap SCENIC 1.1.2-2 Aibar et al., 2017 htt...
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [SCENIC v1.1.2, Scanpy v1.4.6, Seurat v2.3.0, kallisto, scDblFinder]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: ...es used) This paper https://github.com/niaid/covid19-time-resolved R (versions 3.5.2, 3.6.0, 3.6.1, 3.6.3) The R Foundation https://www.r-project.org Seurat (versions 3.1.0, 3.1.4, 3.2.2) Stuart et al., 2019 https://cran.r-project.org/web/packages/Seurat/index.html dsb (beta) Mulè et al., 2020 https://github.com/niaid/dsb CytoML (1.12.0) Finak et al., 2018 https://www.bioconductor.org/packages/rel...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Maturation and persistence of the anti-SARS-CoV-2 memory B cell response. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.050 | PMCID: PMC7994111 | PMID: 33571429
- Version used: **3.2.2**
- Evidence: Outputs of Cell Ranger were directly loaded into Seurat v3.2.2 ( Stuart et al., 2019 ) for further QC steps and analysis.
- Full pipeline: quality control [Seurat v3.2.2] -> alignment/mapping [R v4.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, igraph v1.2.6] -> stage not stated [Docker, ggplot2 v3.3.2]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **3.1.5.9900**
- Evidence: ...ckage DropletUtils version 1.4.2 R Bioconductor; Lun et al., 2019 https://www.bioconductor.org/packages/release/bioc/html/DropletUtils.html R package Seurat version 3.1.5.9900 Github; Butler et al., 2018 https://github.com/satijalab/seurat R package Harmony version 1.0 Github; Korsunsky et al., 2019 https://github.com/immunogenomics/harmony R package MAST version 1.14.0 R Bioconductor; Finak et al...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Genome-Scale Identification of SARS-CoV-2 and Pan-coronavirus Host Factor Networks. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.006 | PMCID: PMC7796900 | PMID: 33382968
- Evidence: ...-wide CRISPR-Cas9 Knockout (MAGeCK) Li et al., 2014 https://sourceforge.net/p/mageck/wiki/Home/ Cytoscape Shannon et al., 2003 https://cytoscape.org/ Seurat Stuart et al., 2019 https://satijalab.org/seurat/ Other Revolve inverted microscope ECHO https://discover-echo.com/revolve Resource Availability Lead Contact Further information and requests for resources and reagents should be directed to and...
- Full pipeline: differential/statistical testing [R] -> stage not stated [Cytoscape, STRING db, Seurat]

### Synergism of TNF-α and IFN-γ Triggers Inflammatory Cell Death, Tissue Damage, and Mortality in SARS-CoV-2 Infection and Cytokine Shock Syndromes. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.025 | PMCID: PMC7674074 | PMID: 33278357
- Evidence: ...Algorithms GraphPad Prism 8.0 GraphPad Software, Inc. https://www.graphpad.com/ Morpheus Broad Institute https://software.broadinstitute.org/morpheus Seurat R package v3.1.4 Satija et al., 2015 N/A Resource Availability Lead Contact Further information and requests for reagents may be directed to, and will be fulfilled by the lead contact Thirumala-Devi Kanneganti ( thirumala-devi.kanneganti@stjud...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Version used: **3.1.5**
- Evidence: ...94213B4581121AA02E710A5BE27FBE9F CellRanger v3.1.0 10x Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest Seurat v3.1.5 Stuart et al., 2019 https://satijalab.org/seurat SingleR v2.0.3 Aran et al., 2019 https://bioconductor.org/packages/SingleR DoubletFinder v2.0.3 McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder ggplot2 Wickham,...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.030 | PMCID: PMC7584921 | PMID: 33147445
- Evidence: ...he analysis of the CRISPR screen Chen et al., 2018 N/A FlowJo v10 BD Biosciences N/A GraphPad Prism 8 GraphPad N/A Cellranger v3.0.1 10x Genomics N/A Seurat R package v3.2 Stuart et al., 2019 N/A DESeq2 Love et al., 2014 N/A STRING tool Szklarczyk et al., 2019 N/A Resource Availability Lead Contact Further information and requests for resources and reagents should be directed to and will be fulfil...
- Full pipeline: read trimming [Cutadapt v1.13] -> alignment/mapping [STAR] -> stage not stated [DESeq2, GSEA, R, Seurat, fgsea]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Version used: **3.2.2**
- Evidence: 106 https://github.com/macs3-project/MACS Space Ranger (version: 1.1.0) 10X genomics https://support.10xgenomics.com/spatial-gene-expression/software/pipelines/latest/what-is-space-ranger Seurat (version 3.2.2) Stuart et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: ...studio.com/ DEP-LFQ package for R, BiocManager 1.30.16 CRAN repositories https://bioconductor.org/packages/devel/bioc/vignettes/DEP/inst/doc/DEP.html Seurat package for R, version 4.0.2 Satija Lab https://satijalab.org/seurat/ Prism 9.0 GraphPad Software, USA RRID: SCR_002798 DIALS (via XIA2) Winter et al., 2013, 2018 https://doi.org/10.1107/S0907444913015308 https://doi.org/10.1107/S2059798317017...
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Post-gastrulation synthetic embryos generated ex utero from mouse naive ESCs. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.028 | PMCID: PMC9439721 | PMID: 35988542
- Evidence: ...oftware/cellsens/ 10X Genomics CellRanger 7.0 10X Genomics Inc. https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest Seurat R package v3.2.2 Satija Lab, USA https://satijalab.org/seurat/ AUCell R package v1.8 Bioconductor project, USA https://bioconductor.org/packages/release/bioc/html/AUCell.html UTAP Bioinformatics unit, Weizmann Institute of Science, Israel http...
- Full pipeline: alignment/mapping [STAR v2.4.2a] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, R, Seurat, pheatmap]

### Non-canonical odor coding in the mosquito. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.024 | PMCID: PMC9480278 | PMID: 35985288
- Evidence: (2019) https://github.com/immunogenomics/harmony Sctransform Hafemeister and Satija (2019) https://github.com/satijalab/sctransform Seurat Satija et al.
- Full pipeline: normalisation [ComplexHeatmap] -> stage not stated [ImageJ, R, Seurat, ggplot2, scDblFinder, tidyverse]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: As a summary of single-cell cell cycle states, we performed a Uniform Manifold Approximation and Projection (UMAP) dimension reduction based on the expression n=199 known cell cycle genes [obtained from Seurat ( Satija et al., 2015 ) and ( Adamson et al., 2016 )].
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Mild respiratory COVID can cause multi-lineage neural cell and myelin dysregulation. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.008 | PMCID: PMC9189143 | PMID: 35768006
- Version used: **4.1.0**
- Evidence: Seurat (v4.1.0) ( Hao et al., 2021 ) was used for preprocessing, dimensionality reduction, clustering, and differential expression testing.
- Full pipeline: dimensionality reduction/clustering [Seurat v4.1.0, UMAP, clusterProfiler] -> differential/statistical testing [Seurat v4.1.0] -> stage not stated [ImageJ, R v4.1.1]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: (2011) https://software.broadinstitute.org/software/igv/ R version 4.0.5 ggplot2 package The R Foundation https://cran.r-project.org/web/packages/ggplot2/index.html R version 4.0.5 Seurat package The R Foundation https://cran.r-project.org/web/packages/Seurat/index.html Cellranger 5.0.1 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/release-notes...
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...ab/scvelo Sparse Decomposition of Arrays ( Hore et al., 2016 ) https://jmarchini.org/software/#sda Seaborn Waskom v0.11.1 https://seaborn.pydata.org/ Seurat ( Stuart et al., 2019 ) v3.9.9.9010 SIMON ( Tomic et al., 2019 ) https://genular.org/ singleR ( Aran et al., 2019 ) https://github.com/dviraran/SingleR STAR ( Dobin et al., 2013 ) v2.7.3 stringdist ( van der Loo, 2014 ) https://github.com/mark...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: ...genomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger FastCAR R Package N/A https://github.com/LungCellAtlas/FastCAR Seurat R Package V3 ( Stuart et al., 2019 ) https://satijalab.org/seurat/ Scater R Package ( McCarthy et al., 2017 ) https://bioconductor.org/packages/release/bioc/html/scater.html BioMart N/A https://www.ensembl.org/biomart/martview/3e2c65a5e3f783f8...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: ...6.1b Cutadapt ( Martin, 2011 ) v1.16 Dropseq-tools https://github.com/broadinstitute/Drop-seq/ v2.0.0 R https://www.cran.r-project.org v3.6.2; v4.0.3 Seurat (R package) ( Butler et al., 2018 ; Hafemeister and Satija, 2019 ; Stuart et al., 2019 ) v3.1.4; v3.1.2; v3.9.9.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Early cellular mechanisms of type I interferon-driven susceptibility to tuberculosis. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.002 | PMCID: PMC10757650 | PMID: 38029747
- Version used: **4.1.1**
- Evidence: The raw counts for mRNA, ADT, and HTO were analyzed in R 114 via the RStudio integrated development environment with Seurat v4.1.1 42 using default settings for normalizing the data, finding variable features, and scaling the data.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR, Trimmomatic v0.36] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: We quantified gene expression at the single-cell level with Seurat 111 .
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Serotonin reduction in post-acute sequelae of viral infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.013 | PMCID: PMC11227373 | PMID: 37848036
- Evidence: 52 Data was analyzed with Seurat v4.
- Full pipeline: read trimming [edgeR] -> quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1, limma] -> stage not stated [Bioconductor v3.8, GSEA, ImageJ v2.1.0, Seurat, kallisto v0.46.0]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **4.1.1**
- Evidence: 26 https://github.com/bayesiancook/pbmpi ASTRAL 1.15.2.3 Zhang and Mirarab 93 https://github.com/smirarab/ASTRAL Seurat 4.1.1 Hao et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Humanized mouse liver reveals endothelial control of essential hepatic metabolic functions. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.017 | PMCID: PMC10544749 | PMID: 37562401
- Version used: **3.2**
- Evidence: The count matrix of human cells and human genes was used in the downstream analysis with Seurat 3.2 53 .
- Full pipeline: alignment/mapping [DESeq2, HTSeq, STAR] -> normalisation [DESeq2, HTSeq, STAR] -> stage not stated [Seurat v3.2]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Evidence: 90 N/A Seurat V4.1.0 N/A https://github.com/satijalab/seurat/ STARlong v2.7.8a Dobin et al.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Version used: **3.0.0**
- Evidence: More customized analyses were processed by Seurat (v 3.0.0) which was developed on R language (version 3.5.2).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Apoptotic cell fragments locally activate tingible body macrophages in the germinal center. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.004 | PMCID: PMC7614509 | PMID: 36868219
- Evidence: 81 https://github.com/Hoohm/CITE-seq-Count R 4.1.0 The Comprehensive R Archive Network https://cran.r-project.org/ RStudio 1.4.1717 RStudio https://www.rstudio.com/ Seurat_4.1.0 Phan et al.
- Full pipeline: simulation/modelling [ggplot2] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, GSEA v4.2.3, ImageJ, Python v3.9, QuPath, R v4.1, Seurat, edgeR]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Version used: **4.0.2**
- Evidence: Once dead cells and doublets had been removed, the patient and control samples were analyzed together with the Seurat v4.0.2 R package 207 and cell clustering was performed by the Uniform Manifold Approximation and Projection dimension reduction method 208 applied to the most variable genes, but excluding mitochondrial and ribosomal protein genes, together with sex-related genes as both patients w...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Lymphatic vessels in bone support regeneration after injury. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.031 | PMCID: PMC11913777 | PMID: 36669473
- Evidence: Cell-type clustering analysis and marker identification The feature count matrix was further processed using Seurat (CRAN, version 4.0.1).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: 89 https://doi.org/10.18129/B9.bioc.batchelor Seurat v5 Hao et al.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### Thyroid hormone remodels cortex to coordinate body-wide metabolism and exploration. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.041 | PMCID: PMC11455614 | PMID: 39178853
- Evidence: Using Cell Ranger v5, sequencing reads were demultiplexed, aligned to the GRCm38 reference genome, which was custom annotated to facilitate readout of Cre and DN/WT-THR transgene expression, and filtered for valid 10x barcodes, UMI correction, and cell-calling. snRNA-seq data preprocessing Filtered gene expression counts matrices were loaded into R and converted to Seurat objects.
- Full pipeline: read trimming [Seurat] -> alignment/mapping [Seurat] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, R v4.2.2] -> stage not stated [GSEA, PyTorch]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Version used: **4.4**
- Evidence: 92 scRNA-seq processing The single cell expression data was loaded in R version 4.1.1 using Seurat v4.4. and SeuratObject v4.0.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Version used: **4.3.0**
- Evidence: 119 RRID: SCR_018139 Seurat v4.3.0 Hao et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Version used: **4.0.2**
- Evidence: 53 https://scvelo.readthedocs.io Seurat (v4.0.2) Stuart et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Version used: **4.3.0**
- Evidence: Subsequently, data filtering, integration, normalization and scaling were performed using the R package Seurat version 4.3.0 111 , 140 and dimensionality reduction and clustering were further done by Uniform Manifold Approximation and Projection (UMAP) analysis.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Evidence: Gene expression in single cells was quantified with Seurat.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Microglia maintain structural integrity during fetal brain morphogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.012 | PMCID: PMC10869139 | PMID: 38309258
- Version used: **4.3.0.1**
- Evidence: ...org/ ; RRID: SCR_001905 R package: Metascape 3.5.20230501 Metascape Team http://metascape.org/gp/index.html#/main/step1 ; RRID: SCR_016620 R package: Seurat 4.3.0.1 N/A https://satijalab.org/seurat/get_started.html ; RRID: SCR_016341 R package: Tidyverse 2.0.0 N/A https://CRAN.R-project.org/ package=tidyverse ; RRID: SCR_019186 R package: Viridis 0.6.4 N/A https://cran.r-project.org/web/packages/v...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Bowtie2, ImageJ, Metascape v3.5.20230501, R, Seurat v4.3.0.1, ggplot2, tidyverse]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Evidence: Data were filtered manually according to common quality-control metrics (i.e., the number of unique genes detected in each cell, the total number of RNA molecules detected in each cell, and the percentage of reads that mapping to the mitochondrial genome) with Seurat.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### Distinct components of mRNA vaccines cooperate to instruct efficient germinal center responses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.023 | PMCID: PMC12878702 | PMID: 41406961
- Evidence: Individual count tables were read into R and downstream analysis was performed using Seurat v4 82 .
- Full pipeline: dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [GSEA, R, fgsea] -> stage not stated [Seurat]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Version used: **4.0.2**
- Evidence: 55 Analysis was performed using Seurat v4.0.2 and R v4.0.4.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Evidence: 81 We retrieved the raw count data using the scanpy package 84 (version 1.10.1), and then re-processed the data using the sctransform-based pipeline 130 from the R package Seurat.
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### Molecular and neural control of social hierarchy by a forebrain-thalamocortical circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.024 | PMCID: PMC12458795 | PMID: 40795854
- Version used: **2.3.4**
- Evidence: The matrices were then analyzed in Seurat version 2.3.4 84 .
- Full pipeline: normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, GSEA, R, Seurat v2.3.4]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Version used: **4.4.0**
- Evidence: 32 , 35 , 71 Canonical correlation analysis (CCA) was performed using Seurat (v4.4.0) to align our snATAC-derived gene activity profiles with these reference states.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Human interpretable grammar encodes multicellular systems biology models to democratize virtual cell laboratories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.048 | PMCID: PMC13012569 | PMID: 40713951
- Version used: **4.1.0**
- Evidence: 72 , 108 , 109 To locate fibroblasts, Seurat version 4.1.0 was used to compute module scores from a pan-CAF gene signature as described previously.
- Full pipeline: dimensionality reduction/clustering [R] -> simulation/modelling [R, ggpubr] -> stage not stated [ImageJ, Python, Seurat v4.1.0]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Within AtoMx, pipelines were executed for each study, and data was exported in various formats, including TileDB arrays and Seurat objects, for in-house analysis.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Serotonin transporter inhibits antitumor immunity through regulating the intratumoral serotonin axis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.032 | PMCID: PMC12255530 | PMID: 40403728
- Version used: **4.0.0**
- Evidence: For cell clustering and annotation, the merged digital expression matrix generated by Cell Ranger was analyzed using the R package Seurat (v.4.0.0) following the guidelines.
- Full pipeline: quantification [R, Seurat v4.0.0] -> dimensionality reduction/clustering [GSEA, R, Seurat v4.0.0, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2, velocyto]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: Single cell gene expression count matrix was processed by the Harmony package in Seurat with default parameters and subsequently constructed into a Seurat object by the CreateSeuratObject function with default parameters.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **5.1.0**
- Evidence: Signac (v1.13.0) 117 and Seurat (v5.1.0) 118 were used to import sample files into chromatin assay objects, followed by Seurat objects.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Inflammation switches the chemoattractant requirements for naive lymphocyte entry into lymph nodes. (Cell 2025)

- DOI: 10.1016/j.cell.2024.11.031 | PMCID: PMC11845304 | PMID: 39708807
- Version used: **4.3.0**
- Evidence: Our analysis utilized R (version 4.2.1) and Seurat (version 4.3.0) 68 focusing on AD5–8 skin biopsy samples.
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2 v1.4.2, Metascape] -> visualisation [UMAP] -> stage not stated [R v4.2.1, Seurat v4.3.0, deepTools v3.5.4]

### Genome instability triggers intercellular DNA transfer between human cells. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.041 | PMCID: PMC13193222 | PMID: 42161273
- Evidence: Count matrices were normalized using the NormalizeData () function from the R package Seurat 80 using the normalization method “LogNormalize”.
- Full pipeline: normalisation [R, Seurat] -> dimensionality reduction/clustering [UMAP]

### Renal PIEZO2 is an essential regulator of renin. (Cell 2026)

- DOI: 10.1016/j.cell.2025.11.013 | PMCID: PMC12695021 | PMID: 41349545
- Evidence: Library preparation and sequencing were done by the OHSU Integrated Genomics Laboratory. snRNA-seq data analysis: snRNA-seq analysis was performed like what has previously been described 37 using a Seurat pipeline that included doublet removal, ambient RNA removal, and normalization.
- Full pipeline: quality control [SoupX v1.6.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [scDblFinder]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Version used: **3.1.4**
- Evidence: The combined matrix of counts was normalized by applying the LogNormalize method and scaled using Seurat (v.3.1.4) 71 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Version used: **3.0**
- Evidence: We performed integrative analysis with scRNA-seq using Seurat 3.0 (RRID:SCR_016341) to compare cell annotation between different modalities 75 .
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: Unlike Seurat/CCA 57 , which aims to find aligned common reduced dimensions across multiple datasets, this method directly builds a common adjacency graph using the cells from all datasets, and then applies the Louvain community detection algorithm 58 .
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: The scRNA-seq were processed using Seurat and computed the top 15 components from CCA for input into scAlign, and the latent dimension was set to 20 using the small architecture with batch normalization and 15,000 iterations.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Evidence: Integrating 10x v3 snRNA-seq datasets across species To identify homologous cell types across species, human, marmoset and mouse 10x v3 snRNA-seq datasets were integrated using Seurat’s SCTransform workflow.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### A transcriptomic atlas of mouse cerebellar cortex comprehensively defines cell types. (Nature 2021)

- DOI: 10.1038/s41586-021-03220-z | PMCID: PMC8494635 | PMID: 34616064
- Version used: **2.3.4**
- Evidence: For the preliminary clustering step, we performed standard preprocessing (UMI normalization, highly variable gene selection, scaling) with Seurat v2.3.4 as previously described 38 .
- Full pipeline: quantification [Monocle] -> normalisation [Monocle, Seurat v2.3.4] -> dimensionality reduction/clustering [Seurat v2.3.4, UMAP] -> stage not stated [ImageJ]

### Human neocortical expansion involves glutamatergic neuron diversification. (Nature 2021)

- DOI: 10.1038/s41586-021-03813-8 | PMCID: PMC8494638 | PMID: 34616067
- Evidence: Second, the Seurat pipeline 39 , 40 (more details below) was used to scale the data, reduce the dimensionality using principal component analysis (PCA) (30 PCs).
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [ImageJ] -> dimensionality reduction/clustering [Seurat, UMAP, scikit-learn] -> visualisation [scikit-learn] -> stage not stated [statsmodels]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **3.1.1**
- Evidence: ...(for example, Cv3 GABAergic and SSv4 GABAergic); (2) finding marker genes for all clusters within each technology; (3) integrating both datasets with Seurat’s standard workflow using marker genes to guide integration (Seurat v3.1.1) 45 ; (4) overclustering the data to a greater number of clusters than were originally identified within a given individual dataset; (5) finding marker genes for all in...
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Transcriptional programs of neoantigen-specific TIL in anti-PD-1-treated lung cancers. (Nature 2021)

- DOI: 10.1038/s41586-021-03752-4 | PMCID: PMC8338555 | PMID: 34290408
- Evidence: Single-cell data integration and clustering Seurat 40 (3.1.5) was used to normalize the raw count data, identify highly variable features, scale features, and integrate samples.
- Full pipeline: alignment/mapping [velocyto] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [velocyto] -> structure determination [UMAP] -> visualisation [pheatmap]

### A vaccine targeting mutant IDH1 in newly diagnosed glioma. (Nature 2021)

- DOI: 10.1038/s41586-021-03363-z | PMCID: PMC8046668 | PMID: 33762734
- Evidence: The filtered matrices were then analysed using Seurat 28 .
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### NASH limits anti-tumour surveillance in immunotherapy-treated HCC. (Nature 2021)

- DOI: 10.1038/s41586-021-03362-0 | PMCID: PMC8046670 | PMID: 33762733
- Evidence: A gene–barcode matrix containing cell barcodes and gene expression counts was generated by counting the single-cell 3′ UMIs, which were imported into R (v4.0.2), where quality control and normalization were executed using Seurat v3 57 .
- Full pipeline: quality control [Seurat] -> alignment/mapping [velocyto v0.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2 v1.28.1] -> stage not stated [R v3.4, scVelo v0.2.2]

### Lipid signalling enforces functional specialization of T<sub>reg</sub> cells in tumours. (Nature 2021)

- DOI: 10.1038/s41586-021-03235-6 | PMCID: PMC8168716 | PMID: 33627871
- Evidence: Seurat R package (v3.1.2) 48 was used for downstream analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, limma v3.34.9] -> visualisation [UMAP] -> stage not stated [GSEA, Seurat, ggplot2 v2.2.1]

### Sulfur sequestration promotes multicellularity during nutrient limitation. (Nature 2021)

- DOI: 10.1038/s41586-021-03270-3 | PMCID: PMC7969356 | PMID: 33627869
- Evidence: Samples were demultiplexed and aligned using Cell Ranger 2.2 (10X genomics) to genome build release 2-12, then processed and analysed in R using Seurat v.3 and uniform manifold approximation and projection (UMAP) as a dimensionality reduction approach.
- Full pipeline: read trimming [Seurat, UMAP, deepTools, featureCounts] -> alignment/mapping [DESeq2, R, Seurat, UMAP, deepTools, featureCounts] -> quantification [DESeq2, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R]

### Skin-resident innate lymphoid cells converge on a pathogenic effector state. (Nature 2021)

- DOI: 10.1038/s41586-021-03188-w | PMCID: PMC8336632 | PMID: 33536623
- Evidence: Normalization To normalize gene counts, we used the SCTransform function from Seurat v3, setting the ‘vars.to.regress’ parameter to the percentage of mitochondrial genes and defaults for other parameters [ 45 ].
- Full pipeline: normalisation [SciPy, Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Scanpy, UMAP] -> visualisation [UMAP] -> stage not stated [Bioconductor]

### Dynamic regulation of T<sub>FH</sub> selection during the germinal centre reaction. (Nature 2021)

- DOI: 10.1038/s41586-021-03187-x | PMCID: PMC7979475 | PMID: 33536617
- Version used: **3.1.2**
- Evidence: We used Seurat (v3.1.2), an R package to analyze single cell RNA-seq data, to identify differentially expressed genes.
- Full pipeline: quantification [DESeq2 v1.24.0, R] -> differential/statistical testing [DESeq2 v1.24.0, R, Seurat v3.1.2, kallisto v0.46] -> stage not stated [GSEA]

### Defining HPV-specific B cell responses in patients with head and neck cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-2931-3 | PMCID: PMC9462833 | PMID: 33208941
- Version used: **3.1.4**
- Evidence: Data were further analysed using Seurat v.3.1.4 36 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [R, Seurat v3.1.4]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: We followed a graph clustering approach to determine cell clusters, similar to that of Seurat 40 and inspired initially by Xu et al.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Identification of SARS-CoV-2 inhibitors using lung and colonic organoids. (Nature 2021)

- DOI: 10.1038/s41586-020-2901-9 | PMCID: PMC8034380 | PMID: 33116299
- Version used: **3.1.0**
- Evidence: We identified highly variable genes using the FindVariableFeatures function in the R Seurat (v3.1.0) 27 , and selected the top 3,000 variable genes after excluding mitochondria genes, ribosomal genes and dissociation-related genes.
- Full pipeline: quality control [R, edgeR] -> alignment/mapping [Bowtie2] -> quantification [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, edgeR] -> machine learning [UMAP] -> visualisation [Bowtie2] -> stage not stated [GSEA, Seurat v3.1.0]

### Ovarian cancer mutational processes drive site-specific immune evasion. (Nature 2022)

- DOI: 10.1038/s41586-022-05496-1 | PMCID: PMC9771812 | PMID: 36517593
- Evidence: Quality control CellRanger-filtered matrices were loaded into individual Seurat objects using the Seurat R package (version 3.0.1) 34 , 35 .
- Full pipeline: quality control [R, Seurat] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [UMAP] -> machine learning [QuPath v0.2.3, StarDist] -> stage not stated [Strelka v2.8.2, scDblFinder v0.2.1]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Version used: **4.0.0**
- Evidence: Filtering of cells, integration, dimensionality reduction and clustering The filtered expression matrix with cell barcodes and gene names was loaded with the ‘Read10X’ function of the Seurat (v.4.0.0) R package 53 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### A transcriptional switch controls sex determination in Plasmodium falciparum. (Nature 2022)

- DOI: 10.1038/s41586-022-05509-z | PMCID: PMC9750867 | PMID: 36477538
- Version used: **4.0.4**
- Evidence: Single-cell analysis The 10x data were initially filtered by using Seurat (v.4.0.4) 46 .
- Full pipeline: alignment/mapping [minimap2 v2.17] -> quantification [HTSeq v0.12.4] -> visualisation [R] -> stage not stated [BEDTools v2.29.1, HISAT2 v2.0.0, SAMtools, Seurat v4.0.4, scDblFinder v1.6.0]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **3.1.1**
- Evidence: The AddModuleScore function of Seurat (v.3.1.1) was used to calculate the average expression levels of each gene set at the single-cell level, subtracted by the aggregated expression of control feature sets, as originally described 64 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Effect of the intratumoral microbiota on spatial and cellular heterogeneity in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05435-0 | PMCID: PMC9684076 | PMID: 36385528
- Evidence: Cluster ID indicates a unique transcriptional cellular group predicted by Seurat package (See methods).
- Full pipeline: alignment/mapping [GATK, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA]

### The neurons that restore walking after paralysis. (Nature 2022)

- DOI: 10.1038/s41586-022-05385-7 | PMCID: PMC9668750 | PMID: 36352232
- Evidence: Seurat 30 was used to calculate quality control metrics for each cell barcode, including the number of genes detected, number of UMIs, and proportion of reads aligned to mitochondrial genes.
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat, velocyto] -> normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.3, fgsea] -> simulation/modelling [Python v2.7] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Version used: **4.0.3**
- Evidence: Gene expression was analysed with Seurat (v4.0.3) 64 – 67 .
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: CellRanger filtered matrices were loaded into individual Seurat objects using the Seurat R package (v.4.1.0) (refs.
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Version used: **4.1.0**
- Evidence: Expression data were normalized with Seurat v.4.1.0 (ref.
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### Maturation and circuit integration of transplanted human cortical organoids. (Nature 2022)

- DOI: 10.1038/s41586-022-05277-w | PMCID: PMC9556304 | PMID: 36224417
- Version used: **4.1.1**
- Evidence: All subsequent analyses were performed on the filtered barcode matrices outputted from CellRanger using the R (version 4.1.2) package Seurat (version 4.1.1) 32 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Fiji v2.1.0, ImageJ, R v4.1.2, Seurat v4.1.1, edgeR v3.36.0, scDblFinder]

### Collagenolysis-dependent DDR1 signalling dictates pancreatic cancer outcome. (Nature 2022)

- DOI: 10.1038/s41586-022-05169-z | PMCID: PMC9588640 | PMID: 36198801
- Evidence: The datasets were processed in R (v.4.0.2) and Seurat 34 (v.4.0.5) and cells with at least 200 genes and genes expressed in at least 3 cells were retained for further quality control analysis for the percentage of mitochondrial genes expressed, total genes expressed and unique molecular identifier (UMI) counts.
- Full pipeline: quality control [R v4.0.2, Seurat] -> alignment/mapping [STAR] -> quantification [HOMER v4.11] -> dimensionality reduction/clustering [GSEA]

### Stroke genetics informs drug discovery and risk prediction across ancestries. (Nature 2022)

- DOI: 10.1038/s41586-022-05165-3 | PMCID: PMC9524349 | PMID: 36180795
- Evidence: Average expression levels and the percentage of expressed genes were calculated for genes of interest using the DotPlot function from the Seurat package v.4.0.4 in R v.4.1.1.
- Full pipeline: quality control [R] -> differential/statistical testing [LDSC] -> stage not stated [GCTA, MAGMA, SAIGE, Seurat, TwoSampleMR]

### LRRC15<sup>+</sup> myofibroblasts dictate the stromal setpoint to suppress tumour immunity. (Nature 2022)

- DOI: 10.1038/s41586-022-05272-1 | PMCID: PMC9630141 | PMID: 36171287
- Evidence: For gene expression counts, individual samples were merged into one expression matrix and analysed using the package Seurat.
- Full pipeline: quantification [R, Seurat, UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [R, UMAP]

### Long-primed germinal centres with enduring affinity maturation and clonal migration. (Nature 2022)

- DOI: 10.1038/s41586-022-05216-9 | PMCID: PMC9491273 | PMID: 36131022
- Evidence: Sequences were de-multiplexed by hashtags using the MULTIseqDemux command in Seurat v.4 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [UCSF Chimera v1.13] -> visualisation [UCSF Chimera v1.13] -> stage not stated [GSEA, RELION v3.0, Seurat, fgsea]

### Brainstem ADCYAP1<sup>+</sup> neurons control multiple aspects of sickness behaviour. (Nature 2022)

- DOI: 10.1038/s41586-022-05161-7 | PMCID: PMC9492535 | PMID: 36071158
- Version used: **4.0**
- Evidence: The following analysis was based on Orchestrating Single-Cell Analysis from Bioconductor (v1.0.6; https://bioconductor.org/books/release/OSCA/ ) and vignettes from Seurat (v4.0; https://satijalab.org/seurat/ ) 50 .
- Full pipeline: quality control [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor v1.0.6, Seurat v4.0]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **4.0.4**
- Evidence: Dimensionality reduction, cell clustering, and visualization For each scRNA-seq dataset, the filtered count matrix was library-size-normalized, log-transformed (‘log-normalized’ expression values) and then centred and scaled (‘scaled’ expression values) using Seurat v4.0.4.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Non-viral, specifically targeted CAR-T cells achieve high safety and efficacy in B-NHL. (Nature 2022)

- DOI: 10.1038/s41586-022-05140-y | PMCID: PMC9452296 | PMID: 36045296
- Evidence: The Seurat package (v.3.1.4; https://satijalab.org/seurat/ ) was used for cell normalization and regression based on the expression table according to the UMI counts of each sample and the mitochondrial rate to obtain scaled data.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [GSVA, UMAP] -> differential/statistical testing [Seurat] -> stage not stated [GSEA, fastp]

### A brainstem map for visceral sensations. (Nature 2022)

- DOI: 10.1038/s41586-022-05139-5 | PMCID: PMC9452305 | PMID: 36045291
- Evidence: Count matrices of unique transcripts for each library were normalized using regularized negative binomial regression with the function SCTransform in Seurat 59 .
- Full pipeline: normalisation [Seurat] -> differential/statistical testing [Seurat] -> visualisation [R v4.1.1]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: The count matrices with exonic and intronic counts were then used as an input for downstream analysis using Seurat 66 version 3.
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### RASA2 ablation in T cells boosts antigen sensitivity and long-term function. (Nature 2022)

- DOI: 10.1038/s41586-022-05126-w | PMCID: PMC9433322 | PMID: 36002574
- Evidence: Differentially expressed genes between stimulated cells expressing RASA2 sgRNA and non-targeting control guide (ctrl) were analysed using the FindMarkers function from Seurat 61 4.0 R package.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [DESeq2, Seurat, fgsea] -> stage not stated [GSEA, ImageJ v1.52q, R]

### Spatial profiling of chromatin accessibility in mouse and human tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05094-1 | PMCID: PMC9452302 | PMID: 35978191
- Evidence: Data visualization We first identified pixels on tissue samples by manual selection from microscopy images using Adobe Illustrator (v.25.4.3) ( https://github.com/rongfan8/DBiT-seq ), and a custom Python script was used to generate metadata files that were compatible with the Seurat workflow for spatial datasets.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [Python, Seurat] -> stage not stated [ArchR, Snakemake]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: Subsequent data analysis was performed using Seurat R package (v.3.2) 43 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Evidence: The downstream analysis followed the procedures of the Seurat R package (v.3.0).
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Version used: **3.2.2**
- Evidence: Processing and visualization of non-prostate samples Data processing and visualization were carried out using the Seurat (version 3.2.2) 37 and STUtility (version 0.1.0) 38 R packages.
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Evidence: The option ‘–reorient-images’ was enabled to allow for automatic image alignment. hg38 was used as the reference genome for human data alignment. snRNA-seq data processing To identify the major lineages representative of all of our specimens, we created a single-nuclei atlas analysing and integrating each snRNA-seq dataset using Seurat 59 (v4.0.1).
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Version used: **3.2.2**
- Evidence: Additionally, putative doublets were removed using Scrublet (v0.2.1) for each sample 47 . scRNA-seq computational pipelines and basic analysis The R package Seurat (v3.2.2) was used for data scaling, transformation, clustering, dimensionality reduction, differential expression analysis and most visualization 48 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### A physical wiring diagram for the human immune system. (Nature 2022)

- DOI: 10.1038/s41586-022-05028-x | PMCID: PMC9365698 | PMID: 35922511
- Evidence: Differential expression testing between diseased and paired reference tissue was done with the Seurat package (v.3.1.5) 73 using a non-parametric Wilcoxon rank sum test.
- Full pipeline: differential/statistical testing [DESeq2, Seurat] -> stage not stated [CellProfiler, PHENIX, Python, R v1.0.0, Scanpy, igraph]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: We identified highly variable genes ( n = 2,000) using Seurat v3 flavour on the raw counts, which were used to correct for batch effect with single-cell variational inference (scVI) v.0.6.8.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### BA.2.12.1, BA.4 and BA.5 escape antibodies elicited by Omicron infection. (Nature 2022)

- DOI: 10.1038/s41586-022-04980-y | PMCID: PMC9385493 | PMID: 35714668
- Evidence: Raw counts were normalized and scaled with Seurat 46 (v 4.0.3), while principal components analysis and uniform manifold approximation and projection were performed for cluster and visualization.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.20, RELION v3.1, UCSF Chimera v1.16] -> visualisation [ChimeraX v1.3, R, Seurat] -> stage not stated [Pangolin, ggplot2 v3.3.3, scikit-learn]

### Molecularly defined circuits for cardiovascular and cardiopulmonary control. (Nature 2022)

- DOI: 10.1038/s41586-022-04760-8 | PMCID: PMC9297035 | PMID: 35650438
- Version used: **3.1.4**
- Evidence: Using Seurat v3.1.4 ( https://satijalab.org/seurat/ ), read counts per gene were normalized across cells, scaled per 10,000 and converted to log scale using the ‘NormalizeData’ function.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [Seurat v3.1.4] -> normalisation [Seurat v3.1.4]

### Developmental dynamics of two bipotent thymic epithelial progenitor types. (Nature 2022)

- DOI: 10.1038/s41586-022-04752-8 | PMCID: PMC9159946 | PMID: 35614226
- Evidence: Data normalization, dimensionality reduction and visualization with UMAP were then performed using the default parameters of the scRNA-seq data analysis CRAN package Seurat version 3 (ref.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor]

### Extricating human tumour immune alterations from tissue inflammation. (Nature 2022)

- DOI: 10.1038/s41586-022-04718-w | PMCID: PMC9132772 | PMID: 35545675
- Evidence: The final output of Cell Ranger (the molecule per cell count matrix) was then analysed in R using the package Seurat 60 , 61 (3.0) as described below.
- Full pipeline: quality control [Harmony, SAMtools v1.2] -> read trimming [STAR] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [R] -> stage not stated [Galaxy, HTSeq, Seurat]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Adult snRNA-seq and single-cell RNA-seq analysis Mouse BNST snRNA-seq data containing 76,693 neurons across 7 adult female and 8 adult male biological replicates 26 were accessed from GEO: GSE126836 and loaded into a Seurat object 85 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Intermittent PI3Kδ inhibition sustains anti-tumour immunity and curbs irAEs. (Nature 2022)

- DOI: 10.1038/s41586-022-04685-2 | PMCID: PMC9132770 | PMID: 35508656
- Version used: **3.1.5**
- Evidence: Filtered cells were analysed using the package Seurat (v3.1.5).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [GSEA, MACS2, Seurat v3.1.5, fgsea v1.10.1]

### TLR7 gain-of-function genetic variation causes human lupus. (Nature 2022)

- DOI: 10.1038/s41586-022-04642-z | PMCID: PMC9095492 | PMID: 35477763
- Version used: **4.0.1**
- Evidence: Statistical analysis, clustering and visualization were conducted using Seurat v.4.0.1 in the R environment.
- Full pipeline: dimensionality reduction/clustering [Seurat v4.0.1] -> differential/statistical testing [R, Seurat v4.0.1] -> visualisation [Seurat v4.0.1] -> stage not stated [edgeR, limma]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Evidence: Principal-component analysis was then performed using the top 12,000 most variable genes by applying the original Seurat variable gene selection method implemented in the scanpy package, with the 100 most variance-encompassing principal components used for the following steps.
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### A multidimensional coding architecture of the vagal interoceptive system. (Nature 2022)

- DOI: 10.1038/s41586-022-04515-5 | PMCID: PMC8967724 | PMID: 35296859
- Evidence: Control scRNA-seq and Projection-seq data were then integrated and processed using the R package Seurat v.3 55 , and 42 cell clusters identified using the top 30 principal components (PCs) were visualized using UMAP 56 ( Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [R, Seurat, UMAP, pheatmap] -> stage not stated [CellPhoneDB, Fiji, ImageJ]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Version used: **4.0.3**
- Evidence: Then, we processed the filtered UMI count matrices using the R package Seurat (version 4.0.3) 59 .
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### GD2-CAR T cell therapy for H3K27M-mutated diffuse midline gliomas. (Nature 2022)

- DOI: 10.1038/s41586-022-04489-4 | PMCID: PMC8967714 | PMID: 35130560
- Evidence: Unique molecular identifier (UMI) count matrices from Cell Ranger were analysed using Seurat 33 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: Single-cell datasets were analysed using Seurat 3 toolkit (Version 3.2.0).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### Single-cell delineation of lineage and genetic identity in the mouse brain. (Nature 2022)

- DOI: 10.1038/s41586-021-04237-0 | PMCID: PMC8770128 | PMID: 34912118
- Evidence: Cell barcodes (Cell) were extracted from the corresponding Seurat object of the dataset to generate a cell barcode whitelist.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [R v3.6.0, Seurat, scDblFinder v2.0.3, velocyto]

### Signature of long-lived memory CD8<sup>+</sup> T cells in acute SARS-CoV-2 infection. (Nature 2022)

- DOI: 10.1038/s41586-021-04280-x | PMCID: PMC8810382 | PMID: 34875673
- Version used: **4.0.3**
- Evidence: Downstream analysis was conducted in R version 4.1.0 with the package Seurat version 4.0.3 (ref.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R v4.1.0, Seurat v4.0.3, fgsea]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Version used: **4.0.1**
- Evidence: Further analysis was performed in R v4.0.3 with Seurat v4.0.1.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### Brain-wide correspondence of neuronal epigenomics and distant projections. (Nature 2023)

- DOI: 10.1038/s41586-023-06823-w | PMCID: PMC10719087 | PMID: 38092919
- Evidence: Transfer of cell labels from one dataset to another with weighted k -nearest neighbours This method is similar to the label transfer method in Seurat v3 (ref.
- Full pipeline: stage not stated [BEDTools, SCENIC, Seurat]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Version used: **4.3.0**
- Evidence: We then used Seurat v.4.3.0 for downstream analysis 57 .
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: We performed unsupervised clustering with RNA UMI counts using the Seurat (v.4) 71 standard analysis pipeline.
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Version used: **4.0.1**
- Evidence: All functions mentioned above are part of the Seurat v.4.0.1 package in R 34 , 35 .
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Evidence: We normalized the data with Seurat’s LogNormalize normalization (scale.factor=1e4) and averaged each cell type’s five nearest neighbours’ expressions.
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Atlas-level data integration and cluster annotation We established a highly efficient framework based on the Seurat R package 30 integration algorithm to perform atlas-level data integration with millions of cells.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Evolution of neuronal cell classes and types in the vertebrate retina. (Nature 2023)

- DOI: 10.1038/s41586-023-06638-9 | PMCID: PMC10719112 | PMID: 38092908
- Version used: **4.3.0**
- Evidence: Our workflow was based on Seurat v4.3.0 for single-cell analysis developed and maintained by the Satija laboratory 29 , 62 ( https://satijalab.org/seurat/ ) and includes several packages used for statistical calculations and data visualizations including MASS v7.3.60, pvclust v2.2.0, reshape2 v1.4.4, stats v4.3.0, ggplot2 v3.4.2, dendextend v1.17.1 and ggdendro v0.1.23 We describe the analysis ste...
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat v4.3.0, ggplot2 v3.4.2] -> visualisation [Seurat v4.3.0, UMAP, ggplot2 v3.4.2]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: We next performed integration analysis using Seurat 32 for neuronal cells and non-neuronal cells separately.
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **4.1.0**
- Evidence: The filtered matrix of WT and Msl2 KO were merged together with Signac (v.1.5.0) 72 and Seurat (v.4.1.0) 73 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **4.0.4**
- Evidence: The filtered feature matrices were imported into Seurat (v.4.0.4) 67 , 68 to create assays for a Seurat object containing both gene expression and CRISPR guide capture matrices.
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Evidence: As the second strategy, we used an iterative clustering strategy based on Seurat v3 (ref.
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Embryo-scale reverse genetics at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06720-2 | PMCID: PMC10665197 | PMID: 37968389
- Evidence: Datasets were then aligned with the IntegrateData function in Seurat V3.
- Full pipeline: alignment/mapping [Seurat] -> dimensionality reduction/clustering [Monocle v1.3.1, UMAP] -> differential/statistical testing [GSEA, R] -> stage not stated [ImageJ, fgsea v1.26.0]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Version used: **4.0.5**
- Evidence: The resulting gene-by-cell unique molecular identifier (UMI) count matrix was used by the R package Seurat (v.4.0.5) 67 for subsequent processing.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Vagal sensory neurons mediate the Bezold-Jarisch reflex and induce syncope. (Nature 2023)

- DOI: 10.1038/s41586-023-06680-7 | PMCID: PMC10632149 | PMID: 37914931
- Evidence: The data were filtered and re-plotted using the Seurat (v.3) package.
- Full pipeline: visualisation [Seurat] -> stage not stated [DeepLabCut]

### Dopaminergic systems create reward seeking despite adverse consequences. (Nature 2023)

- DOI: 10.1038/s41586-023-06671-8 | PMCID: PMC10632144 | PMID: 37880370
- Evidence: UMAP reduction 79 of the data and clustering was performed using the Seurat v3 R package 80 .
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [ComplexHeatmap v1.10.2, Cytoscape v3.9.1]

### Targeting myeloid chemotaxis to reverse prostate cancer therapy resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06696-z | PMCID: PMC10686834 | PMID: 37844613
- Version used: **4.3.0**
- Evidence: Both datasets were processed with Seurat (v.4.3.0) and underwent scaling, clustering, dimensional reduction and cell type assignment with SingleR (v.1.8.1) using the Blueprint ENCODE reference dataset from the celldex (v.1.4.0) library.
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, TopHat v2.0.7] -> quantification [Cufflinks v2.2.1] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSVA v1.4, R]

### Assembloid CRISPR screens reveal impact of disease genes in human neurodevelopment. (Nature 2023)

- DOI: 10.1038/s41586-023-06564-w | PMCID: PMC10567561 | PMID: 37758944
- Evidence: Briefly, the raw gene count matrix was downloaded from Gene Expression Omnibus (accession number GSE162170 ) and processed using the standard workflow of the R package Seurat 52 (v.4.1.0): including normalization using the sctransform function (vst.flavor = ‘v2’).
- Full pipeline: normalisation [ComplexHeatmap, R, Seurat] -> visualisation [ComplexHeatmap] -> stage not stated [Fiji v1.0, ImageJ v1.0, ggplot2]

### Transcriptional linkage analysis with in vivo AAV-Perturb-seq. (Nature 2023)

- DOI: 10.1038/s41586-023-06570-y | PMCID: PMC10567566 | PMID: 37730998
- Version used: **3.0**
- Evidence: Normalization and cell-type clustering were performed using the Seurat v.3.0 package in R 18 .
- Full pipeline: normalisation [Seurat v3.0] -> dimensionality reduction/clustering [Seurat v3.0, UMAP] -> differential/statistical testing [R v3.36.0, edgeR] -> stage not stated [Enrichr v2.1, GSEA, Nextstrain v1.0.0, fgsea v3.17]

### Transgenic ferret models define pulmonary ionocyte diversity and function. (Nature 2023)

- DOI: 10.1038/s41586-023-06549-9 | PMCID: PMC10533402 | PMID: 37730992
- Evidence: Expression values E i,j for gene i in cell j were calculated by dividing UMI count values for gene i by the sum of the UMI counts in cell j , to normalize for differences in coverage, and then multiplying by 10,000 to create TPM-like values, and finally calculating log 2 (TPM + 1) values, implemented using the NormalizeData function in the ‘Seurat’ R package.
- Full pipeline: alignment/mapping [kallisto] -> variant calling [UMAP] -> quantification [R, Seurat] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [brms] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Evidence: UMI counts were then analysed in R using the Seurat v.4 (ref.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: Glutamatergic astrocyte identification The spatial count matrix for RNA ( Slc17a6 , Slc17a7 , Syt1 , Snap25 ) and protein (tdTomato, GS/S100β) was normalized using the CLR method from the Seurat package.
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Complete human day 14 post-implantation embryo models from naive ES cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06604-5 | PMCID: PMC10584686 | PMID: 37673118
- Evidence: Seurat cluster analysis did not produce a separate cluster containing cytotrophoblast-like cells (probably due to the low capture rate for trophoblasts after SEM enzymatic dissociation) when mapping cytotrophoblast-specific markers such as PAGE4 and S100P (ref.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Signac v1.6.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [SciPy v1.8.0, seaborn v0.11.0] -> visualisation [SciPy v1.8.0, seaborn v0.11.0] -> stage not stated [R, pheatmap, scDblFinder v1.6]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Version used: **4.1.1**
- Evidence: Since NicheNet is based on the Seurat toolkit, expression was preprocessed using a typical preprocessing workflow including its SCTransform ‘v2’ workflow (Seurat v.4.1.1, SCTransform v.0.3.3), with a consistent number of variable features as used for ContactTracing.
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Version used: **3.1.1**
- Evidence: RNA and HTO data were loaded into Seurat 3.1.1 and combined by intersecting cell barcodes found in both datasets.
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### Platelet factors attenuate inflammation and rescue cognition in ageing. (Nature 2023)

- DOI: 10.1038/s41586-023-06436-3 | PMCID: PMC10468395 | PMID: 37587343
- Evidence: Downstream single-cell analysis was performed using the R package Seurat 56 .
- Full pipeline: alignment/mapping [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> quantification [DESeq2, ImageJ, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> stage not stated [Enrichr, Seurat]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Version used: **3.2.0**
- Evidence: UMI count matrices were then imported to Seurat (v3.2.0) 55 with the following arguments: min.cells = 10 and min.features = 100.
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Version used: **4.1.1**
- Evidence: We first performed low-resolution (res. parameter = 0.8) shared nearest-neighbour graph-based ( k = 25) clustering using FindClusters from Seurat (v.4.1.1) with assignment to one of three meta-clusters (that is, myeloid, B lymphoid and T/NK lymphoid) on the basis of the transcriptional profiles of the cells for canonical markers (for example, CD3E-F , CD14 , FCGR3A , MS4A1 ) (Supplementary Fig.
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Version used: **4.0.6**
- Evidence: All downstream analysis of single-cell RNA-seq data was performed using Seurat v.4.0.6 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### cGAS-STING drives ageing-related inflammation and neurodegeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-06373-1 | PMCID: PMC10412454 | PMID: 37532932
- Evidence: Sample processing and analysis were performed using the R package Seurat 59 (v.4.1.1.9003).
- Full pipeline: alignment/mapping [HTSeq, STAR, featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.38.2, ImageJ, Seurat]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Evidence: Filtered barcoded matrices from single-cell RNA-seq data were imported into R using the Seurat package (v.4.1.1).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Version used: **4.0.0**
- Evidence: Principal components and cluster annotations were then imported into Seurat (v.4.0.0) and uniform manifold approximation and projection (UMAP) dimensionality reduction was performed using the top 50 principal components identified using Pagoda2.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: Quality control, dimensionality reduction and clustering of snRNA-seq data After running Cell Ranger, the raw_feature_bc_matrix produced by Cell Ranger was read into R with the Seurat 84 function Read10X.
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Version used: **4.0.2**
- Evidence: The output from Cell Ranger was imported into R (version 4.0.5) and analysed with Seurat (version 4.0.2).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Version used: **4.3.0**
- Evidence: Data for D4 and D6 were processed separately using the Seurat (v.4.3.0) package in R (v.4.2.3).
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Evidence: Matrices were then read into Seurat 50 and Signac 51 using the Read10X_h5 command.
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### Single-cell quantification of ribosome occupancy in early mouse development. (Nature 2023)

- DOI: 10.1038/s41586-023-06228-9 | PMCID: PMC10307641 | PMID: 37344592
- Evidence: 71 , was applied to centred log ratio of ribosome occupancies (‘FindVariableFeatures’ function with the selection method ‘vst’ in the Seurat package v4 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ, R v4.0, Seurat]

### Signalling by senescent melanocytes hyperactivates hair growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06172-8 | PMCID: PMC10284692 | PMID: 37344645
- Evidence: Clustering of cells was performed using the Seurat R package (V2.3).
- Full pipeline: alignment/mapping [RSEM v1.2.25, STAR v2.4.2a] -> quantification [RSEM v1.2.25] -> normalisation [RSEM v1.2.25] -> dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [edgeR v3.2.2] -> stage not stated [Metascape]

### Injury prevents Ras mutant cell expansion in mosaic skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06198-y | PMCID: PMC10322723 | PMID: 37344586
- Evidence: The resulting matrix was then processed with the Seurat package 62 (v.3, https://satijalab.org/seurat/index.html ), to retain genes or features that are detected in at least 3 cells and include cells for which at least 200 genes or features are detected.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Scanpy v1.6, Seurat, SoupX, scDblFinder, scikit-learn v0.24.2]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Evidence: We added the genotyping information as metadata to Seurat objects with scRNA-seq expression data by joining based on cell barcodes.
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Myelin dysfunction drives amyloid-β deposition in models of Alzheimer's disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06120-6 | PMCID: PMC10247380 | PMID: 37258678
- Version used: **4.1.1**
- Evidence: Dimensionality reduction, clustering analysis and cell type annotation The normalized UMI matrix for 3-month and 6-month time point data were mainly analysed using the R package Seurat (v.4.1.1) 77 , 78 .
- Full pipeline: quality control [STAR v2.5.2b] -> alignment/mapping [DESeq2 v1.26.0, STAR v2.5.2b, featureCounts v1.6.3] -> quantification [DESeq2 v1.26.0, featureCounts v1.6.3] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts v1.6.3] -> visualisation [DESeq2 v1.26.0, featureCounts v1.6.3] -> stage not stated [MACS2, R v4.04, afex v0.28]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: Analyses of the count matrices were conducted in R (v.4.0.5; 31 March 2021) using Seurat 39 (v.4.0.4).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Glioblastoma remodelling of human neural circuits decreases survival. (Nature 2023)

- DOI: 10.1038/s41586-023-06036-1 | PMCID: PMC10191851 | PMID: 37138086
- Version used: **3.0.1**
- Evidence: Single-cell UMI count data were preprocessed in Seurat (v.3.0.1) 74 , 75 using the sctransform workflow 76 , with scaling based on the regression of UMI count and the percentage of reads attributed to mitochondrial genes per cell.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [HISAT2, featureCounts] -> normalisation [Python, Seurat v3.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Python, R v3.1, Seurat v3.0.1, featureCounts] -> stage not stated [ImageJ]

### Dedifferentiation maintains melanocyte stem cells in a dynamic niche. (Nature 2023)

- DOI: 10.1038/s41586-023-05960-6 | PMCID: PMC10132989 | PMID: 37076619
- Evidence: Further analysis and visualization were performed using Seurat package (v.4.1.0) 59 , using R Studio Desktop (v.1.4.1717) and R (v.4.1.2).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> structure determination [ImageJ] -> visualisation [Seurat] -> stage not stated [GSEA]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: ... each cell, which we used to test for differential transcription factor binding activity between trophoblast cell states with FindMarkers function in Seurat (default parameters) in the same way as described in ‘Differential gene expression analysis’ (backwards along invading trophoblast trajectory).
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Spatial epigenome-transcriptome co-profiling of mammalian tissues. (Nature 2023)

- DOI: 10.1038/s41586-023-05795-1 | PMCID: PMC10076218 | PMID: 36922587
- Version used: **4.1**
- Evidence: In regard to RNA spatial data visualization, the gene matrix obtained from RNA was loaded into Seurat v.4.1 (ref.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.2] -> visualisation [ArchR v1.0.1, Seurat v4.1] -> stage not stated [Monocle, Signac v1.8]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: The Seurat R package (v.3.1.5) 83 was utilized for data processing.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### An airway-to-brain sensory pathway mediates influenza-induced sickness. (Nature 2023)

- DOI: 10.1038/s41586-023-05796-0 | PMCID: PMC10033449 | PMID: 36890237
- Version used: **4.1.0**
- Evidence: Single-cell transcriptomics All UMAP plots in this manuscript were made from published single-cell transcriptome data (GEO Accession ID: GSE145216 ) 22 using Seurat (4.1.0) and R Studio (4.1.2).
- Full pipeline: dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> stage not stated [ImageJ v1.53q]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: The datasets were loaded into R and analysed using the Seurat (v.3) 66 and Monocle3 67 packages.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: For data preprocessing, we recommend using Scanpy ( https://scanpy.readthedocs.io/en/stable/ ) or Seurat ( https://satijalab.org/seurat/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Single-cell spatial immune landscapes of primary and metastatic brain tumours. (Nature 2023)

- DOI: 10.1038/s41586-022-05680-3 | PMCID: PMC9931580 | PMID: 36725935
- Version used: **4.1.1**
- Evidence: Using the Seurat object file GSE154795_GBM.AllCell.Integrated.Scaled.ClusterRes.0.1.rds, a new Seurat object was created (Seurat 4.1.1), with the RNA assay counts from the subset of the 14 new patients with glioblastoma and was normalized with the default parameters of the Seurat function NormalizeData.
- Full pipeline: normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1] -> differential/statistical testing [Python v3.7.12] -> stage not stated [ImageJ v1.53k, scikit-learn]

### Tissue CD14&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; T cells reprogrammed by myeloid cells and modulated by LPS. (Nature 2023)

- DOI: 10.1038/s41586-022-05645-6 | PMCID: PMC7619353 | PMID: 36697826
- Evidence: Single-cell RNA-sequencing: Clustering and annotation Following quality control gene expression was normalised by cell to correct for cell-to-cell variation in total reads and log transformed using the NormalizeData tool in Seurat.
- Full pipeline: quality control [STAR, Seurat] -> alignment/mapping [STAR] -> quantification [HTSeq v0.10.0, ImageJ, STAR] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [seaborn] -> simulation/modelling [scDblFinder] -> visualisation [seaborn] -> stage not stated [Python v3.6]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Version used: **3.1.5**
- Evidence: Downstream analysis was performed using Seurat (v.3.1.5) according to the author’s instructions 55 .
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: Counts were log 10 -normalized and then genes were scaled using default parameters of Seurat’s NormalizeData and ScaleData functions.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Evidence: We created a Seurat 62 object using the Seurat R package v.3.1.4 from the subset raw UMI count table generated by CellRanger corresponding to the usable droplets identified upstream, normalized the data using the NormalizeData function, identified the top 10,000 most variables genes using the FindVariableFeatures function, scaled the data using the ScaleData function, performed the PCA using the R...
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **4.0.3**
- Evidence: Quality control, filtering, data clustering, visualization and differential expression analysis were performed using the Seurat (v.4.0.3) and DoubletFinder (v.2.0) R packages 85 , 86 .
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Microglia regulate central nervous system myelin growth and integrity. (Nature 2023)

- DOI: 10.1038/s41586-022-05534-y | PMCID: PMC9812791 | PMID: 36517604
- Version used: **4.1.0**
- Evidence: Differential gene expression between cluster 1 (specific to the Fire Δ/Δ mice) and the mean expression of all other cells was performed using FindMarkers from Seurat (v.4.1.0) (Supplementary Table 1 ).
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [Seurat v4.1.0] -> stage not stated [QuPath v0.3.0, ggplot2 v3.3.5]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Version used: **4.0.3**
- Evidence: Downstream analysis was conducted in R v.4.1.0 with the package Seurat v.4.0.3 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Evidence: Count matrices were further preprocessed using the Seurat R package (v.3.2) 19 .
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Exaptation of ancestral cell-identity networks enables C&lt;sub&gt;4&lt;/sub&gt; photosynthesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08204-3 | PMCID: PMC11618092 | PMID: 39567684
- Evidence: Nuclei clustering Transcriptional atlases were generated separately for each species using Seurat 54 .
- Full pipeline: dimensionality reduction/clustering [Seurat, Signac, UMAP] -> differential/statistical testing [OrthoFinder] -> stage not stated [DESeq2, MACS2]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: We first calculated DEGs of osteogenic clusters and tip cells across the two niches using the Wilcoxon test implemented in Seurat, and minimum log fold change per cluster was used to summarize the differentially expressed ligands and receptors.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: CITE-seq quality control and denoising CITE-seq data were processed using the R packages Seurat 58 (v.4.3.0), SeuratObject (v.4.1.4), SeuratDisk (v.0.0.0.9021), SingleCellExperiment (v.1.24.0), Matrix (v.1.6-4), matrixStats (v.1.2.0), dplyr (v.1.1.4), tidyr (v.1.3.1), reshape2 (v.1.4.4), BiocNeighbors (v.1.20.2), BiocParallel (v.1.36.0), stringr (V.1.5.1), reticulate (v.1.35.0) and sceasy (v.0.0.7...
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Version used: **4.1.0**
- Evidence: The R package Seurat v.4.1.0 (ref.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### NK2R control of energy expenditure and feeding to treat metabolic diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-08207-0 | PMCID: PMC11602716 | PMID: 39537932
- Version used: **4.3.0**
- Evidence: Filtered count matrices were analysed in R with Seurat (v4.3.0) 70 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> stage not stated [GEMMA, Seurat v4.3.0, VEP, data.table v1.14.2, tidyverse v1.3.1]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Version used: **3.2.3**
- Evidence: Subsequent analyses on RNA were performed using Seurat (v.3.2.3) 63 , and those on ATAC-seq were performed using ArchR (v.1.0.1) 64 .
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Version used: **4.1.1**
- Evidence: Seurat (version 4.1.1) 80 was used for normalization, dimensionality reduction, and clustering of PETRI-seq data.
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### Leptin-activated hypothalamic BNC2 neurons acutely suppress food intake. (Nature 2024)

- DOI: 10.1038/s41586-024-08108-2 | PMCID: PMC11618066 | PMID: 39478220
- Evidence: The snRNA-seq data for ARC (WT) was preprocessed individually using the Seurat v.4 (v.4.0.3) 55 .
- Full pipeline: quality control [UMAP] -> read trimming [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: UMI counts were then normalized so that each cell had a total of 10,000 UMIs across all genes, and these normalized counts were log-transformed with a pseudocount of 1 using the ‘LogNormalize’ function in the Seurat package.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: Seurat was used for all subsequent analyses.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Rhythmic IL-17 production by γδ T cells maintains adipose de novo lipogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08131-3 | PMCID: PMC11618085 | PMID: 39478228
- Version used: **4.1.0**
- Evidence: Downstream scRNA-seq data analysis A total of 22,748 cells mouse γδ T cells, iNKT cells and MAIT cells expressing a median of 1,423 genes and 3,556 UMIs per cell were loaded from feature-barcode UMI count matrices using the Seurat v.4.1.0 package 62 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.1.0]

### Selective utilization of glucose metabolism guides mammalian gastrulation. (Nature 2024)

- DOI: 10.1038/s41586-024-08044-1 | PMCID: PMC11499262 | PMID: 39415005
- Version used: **4.3.0**
- Evidence: Counts were log-normalized using Seurat (v.
- Full pipeline: normalisation [Seurat v4.3.0] -> differential/statistical testing [DESeq2 v1.40.1] -> simulation/modelling [Slingshot v2.8.0] -> visualisation [Slingshot v2.8.0] -> stage not stated [ImageJ]

### CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors. (Nature 2024)

- DOI: 10.1038/s41586-024-07943-7 | PMCID: PMC11560846 | PMID: 39385035
- Evidence: The Seurat R package (v.4.3) was used to analyse the normalized gene–cell matrix and Harmony (v.0.1.1) was applied for batch-effect correction.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> normalisation [DESeq2, Harmony v0.1.1, R, Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Version used: **5.0.3**
- Evidence: Within each of the four merged datasets, we applied log-normalization, using the scaling factor 10,000 to correct for between-sample differences in library size, and calculated highly variable genes, using the Seurat (v5.0.3) implementation 56 .
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Single-cell CAR T atlas reveals type 2 function in 8-year leukaemia remission. (Nature 2024)

- DOI: 10.1038/s41586-024-07762-w | PMCID: PMC11485231 | PMID: 39322664
- Evidence: The subsequent data analysis was conducted according to the Seurat v.4 pipeline 38 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### The type 2 cytokine Fc-IL-4 revitalizes exhausted CD8&lt;sup&gt;+&lt;/sup&gt; T cells against cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07962-4 | PMCID: PMC11485240 | PMID: 39322665
- Evidence: Downstream data analysis was performed with the Seurat v.4 pipeline 38 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### Temporal BMP4 effects on mouse embryonic and extraembryonic development. (Nature 2024)

- DOI: 10.1038/s41586-024-07937-5 | PMCID: PMC11485214 | PMID: 39294373
- Evidence: In brief, after creating a Seurat object for each batch 69 , Seurat principal component analysis was performed on the basis of the 2,000 most variable feature genes.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [ImageJ, scDblFinder]

### Early intermittent hyperlipidaemia alters tissue macrophages to fuel atherosclerosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07993-x | PMCID: PMC11464399 | PMID: 39231480
- Version used: **5.0.0**
- Evidence: Both individual and integrated study analyses were applied for the data using R package Seurat (v.5.0.0) 56 with integration method scVI 57 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.4.4] -> visualisation [clusterProfiler v4.4.4] -> stage not stated [DESeq2 v1.36.0, R, Seurat v5.0.0]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: Specifically, differentially expressed genes between samples from baseline and after 3 months of testosterone treatment were identified using Seurat’s (v.4.3.0) built in function FindMarkers and filtered with an adjusted P value of less than 0.05 and an absolute value for the average fold change of at least 0.15.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **4.1.0**
- Evidence: Dimensionality reduction and pseudotime We used Seurat 4.1.0 77 to process the scRNA-seq data.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### Spatially clustered type I interferon responses at injury borderzones. (Nature 2024)

- DOI: 10.1038/s41586-024-07806-1 | PMCID: PMC11374671 | PMID: 39198639
- Evidence: Normalization was performed using Seurat’s SCTransform v.2 method based on negative binomial models that account for technical artifacts such as sequencing depth variations but detect and preserve highly variant biological features.
- Full pipeline: quality control [Scanpy, Squidpy] -> normalisation [ImageJ, Scanpy, Seurat, Squidpy] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose, R, SoupX]

### Sympathetic neuropeptide Y protects from obesity by sustaining thermogenic fat. (Nature 2024)

- DOI: 10.1038/s41586-024-07863-6 | PMCID: PMC11446830 | PMID: 39198648
- Version used: **4.2.0**
- Evidence: After filtering, the gene x cell matrix was normalized using ‘NormalizeData()’ in Seurat v.4.2.0 (ref.
- Full pipeline: normalisation [Seurat v4.2.0, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.2.2]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Evidence: Downstream analysis was performed with the Seurat V4 R package 22 .
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Human organoids with an autologous tissue-resident immune compartment. (Nature 2024)

- DOI: 10.1038/s41586-024-07791-5 | PMCID: PMC11374719 | PMID: 39143209
- Evidence: Normalization with SCTransform For normalization and variance stabilization of the molecular count data of each scRNA-seq experiment we used the modelling framework of SCTransform in Seurat v.3 (ref.
- Full pipeline: quality control [R] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [CellChat, CellProfiler v4.2.5, ImageJ v1.54i, Python v3.7, scDblFinder, scVelo]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: After quality-control filtering to remove low-quality sequenced cells, all downstream analysis, including pseudotime analysis, a technique that models single-cell transcriptional change as a continuum, was performed using the Seurat 63 , 64 , Monocle 65 or dynverse 66 implementations in R.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### Molecular mimicry in multisystem inflammatory syndrome in children. (Nature 2024)

- DOI: 10.1038/s41586-024-07722-4 | PMCID: PMC11324515 | PMID: 39112696
- Evidence: Highly variable genes were calculated using the scanpy function highly_variable_genes using Seurat flavor with the default parameters (min_mean = 0.0125, max_mean = 3, and min_disp = 0.5) 64 .
- Full pipeline: differential/statistical testing [Python, SciPy, scikit-learn, tidyverse v1.1.4] -> machine learning [scikit-learn] -> stage not stated [Scanpy v1.10.0, Seurat, igraph v2.0.3]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Version used: **4.1.0**
- Evidence: Unsupervised expression classification for generation of CRPS We used Seurat (v.4.1.0) to identify stable clusters of all CRC samples and among MSI tumours 100 .
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Specifically, two datasets of primary CRC 18 and liver tumour microenvironment 19 were integrated using the Seurat integration method 64 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07752-y | PMCID: PMC11291290 | PMID: 39048822
- Evidence: For downstream analysis, the Seurat package (v4.0.4) was used; genes expressed in fewer than three cells were additionally filtered out from expression matrices, and cells that contained fewer than 200 expressed genes were removed.
- Full pipeline: normalisation [DESeq2 v1.30.1, limma] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [limma] -> stage not stated [R, Seurat, fgsea]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: Cell type annotations For the UMAP visualization of individual major cell type classes (excitatory neurons, inhibitory neurons, astrocytes, oligodendrocytes, OPCs, immune cells), the SCTransform-based integration workflow of Seurat was used to align data from individual samples, using the default settings 89 , 90 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Neural circuit basis of placebo pain relief. (Nature 2024)

- DOI: 10.1038/s41586-024-07816-z | PMCID: PMC11358037 | PMID: 39048016
- Version used: **4.0**
- Evidence: Normalization, clustering and differential gene expression scRNA-seq data were analysed using Seurat (v.4.0) 73 .
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, UMAP] -> differential/statistical testing [Seurat v4.0] -> stage not stated [DeepLabCut, ImageJ, R]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Seurat R package (version 4.9.9.9041) was used to plot these cell-type deconvolution results.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Brainstem Dbh&lt;sup&gt;+&lt;/sup&gt; neurons control allergen-induced airway hyperreactivity. (Nature 2024)

- DOI: 10.1038/s41586-024-07608-5 | PMCID: PMC11254774 | PMID: 38987587
- Version used: **4.0**
- Evidence: The R package Seurat (v4.0) 29 was then used to perform data quality control, normalization, principal components analysis, UMAP generation and differential gene expression testing.
- Full pipeline: quality control [R, Seurat v4.0, UMAP] -> normalisation [R, Seurat v4.0, UMAP, scDblFinder v2.0] -> dimensionality reduction/clustering [R, Seurat v4.0, UMAP, ggplot2 v3.3.2, tidyverse] -> differential/statistical testing [R, Seurat v4.0, UMAP] -> visualisation [ggplot2 v3.3.2, tidyverse]

### Plasmacytoid dendritic cells control homeostasis of megakaryopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07671-y | PMCID: PMC11254756 | PMID: 38987596
- Evidence: The count data were analysed using Seurat 78 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [Monocle] -> stage not stated [DESeq2 v1.30.0, GSEA, Seurat]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Evidence: After quality control, 977 HBV-specific cells from the 21 liver samples could be analysed using R v.4.1.2 with the Seurat package v.4.3.0.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### Single-cell atlas of the human brain vasculature across development, adulthood and disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07493-y | PMCID: PMC11324530 | PMID: 38987604
- Evidence: The generated Seurat objects of FACS-sorted (CD31 + CD45 − ) ECs for the individual entities can be downloaded from 10.5281/zenodo.10058183, and for the overall merges from 10.5281/zenodo.10057779.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> stage not stated [Seurat]

### The cortical amygdala consolidates a socially transmitted long-term memory. (Nature 2024)

- DOI: 10.1038/s41586-024-07632-5 | PMCID: PMC11306109 | PMID: 38961294
- Evidence: First, we aligned the raw data from all groups using the first ten canonical components of the ‘canonical correlation analysis’ function from the Seurat package (v.4.9.9) 78 .
- Full pipeline: alignment/mapping [STAR v2.7.10a, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Cellpose, R v4.2.2, featureCounts v2.0.0]

### Adenosine signalling to astrocytes coordinates brain metabolism and function. (Nature 2024)

- DOI: 10.1038/s41586-024-07611-w | PMCID: PMC11291286 | PMID: 38961289
- Evidence: Data processing and visualization were performed using the Seurat package 49 in R (v.4.2.2, ‘Innocent and Trusting’).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ImageJ, R v4.2.2, Seurat, UMAP] -> stage not stated [Fiji]

### Multiscale topology classifies cells in subcellular spatial transcriptomics. (Nature 2024)

- DOI: 10.1038/s41586-024-07563-1 | PMCID: PMC11208150 | PMID: 38898271
- Evidence: We cluster cells in the snRNA-seq dataset using Seurat 19 and annotate cell types according to top marker genes.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [UMAP] -> stage not stated [MACS2]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Version used: **4.1.0**
- Evidence: Aligned scRNA-seq data were imported from the filtered_feature_bc_matrix folder into Seurat (v.4.1.0) for processing, keeping only cells with at least 200 RNA features detected.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: Quality control and cell annotation were performed on the snGEX gene-cell matrices using the R Seurat package (v4.2.0) 36 .
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Raw data were preprocessed, normalized and variance-stabilized using Seurat (v.4) 96 .
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Myelin plasticity in the ventral tegmental area is required for opioid reward. (Nature 2024)

- DOI: 10.1038/s41586-024-07525-7 | PMCID: PMC11186775 | PMID: 38839962
- Version used: **4.3.0**
- Evidence: Seurat (v.4.3.0) was used for preprocessing, dimensionality reduction, clustering and differential expression testing.
- Full pipeline: dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [Seurat v4.3.0] -> stage not stated [CellChat v1.6.1]

### MYCT1 controls environmental sensing in human haematopoietic stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07478-x | PMCID: PMC11168926 | PMID: 38839950
- Version used: **3.1.2**
- Evidence: The data from the three fractions were balanced when aggregating the samples to equilibrate the sequencing depth. scRNA-seq data analysis The scRNA-seq data were analysed using the R package Seurat (v.3.1.2).
- Full pipeline: quantification [Bioconductor] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> stage not stated [AlphaFold, GSEA, R, Seurat v3.1.2]

### Single-cell nascent RNA sequencing unveils coordinated global transcription. (Nature 2024)

- DOI: 10.1038/s41586-024-07517-7 | PMCID: PMC11222150 | PMID: 38839954
- Evidence: Differentially expressed genes among G1/S, S and G2/M phases of the cell cycle were identified using the ‘FindAllFeatures’ function of Seurat 68 (single-cell analysis package).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Cutadapt] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Seurat]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: Cell Ranger-filtered count matrices for each sample were imported into R and Seurat R objects (version 4.3.0) were created 62 .
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Acquisition of epithelial plasticity in human chronic liver disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07465-2 | PMCID: PMC11153150 | PMID: 38778114
- Version used: **4.0.3**
- Evidence: Quality control Seurat (v.4.0.3) 67 objects were created considering genes expressed in more than three cells, and cells with more than 200 features expressed.
- Full pipeline: quality control [Seurat v4.0.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [velocyto v0.17.17]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Evidence: Comparison of hPGCLC-derived cells in vitro and human germ cells in vivo The analysis of gene–barcode matrices was performed using the Seurat R package (v.4.2.1) 72 following online tutorials ( https://satijalab.org/seurat/index.html ).
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: In brief, we performed analysis as follows: we performed per-dataset quality control in the Seurat 45 R package v4.1.1.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Evidence: Single-cell RNA-seq quality control All subsequent steps were performed in R (v.4.1.2) using the Seurat package 76 .
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### A body-brain circuit that regulates body inflammatory responses. (Nature 2024)

- DOI: 10.1038/s41586-024-07469-y | PMCID: PMC11186780 | PMID: 38692285
- Evidence: Analysis of scRNA-seq data, including the generation of cell clusters and identification of neuronal cluster markers, was performed using a custom R code developed following Seurat online instructions and vignettes 77 , 78 .
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Version used: **4.2.0**
- Evidence: Raw count matrices were imported into R and analysed using Seurat (v.4.2.0) 56 .
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Evidence: If a site was not conserved in at least half of the species, we then assessed whether it displayed glider-specific conservation. scRNA-seq analysis of laboratory mouse data An existing scRNA-seq dataset 75 from dorsal skin of mouse embryos at E12.5, E13.5, E14.5 and E15.5 was reprocessed using the Seurat package (v.4.3.0) 76 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **4.0.1**
- Evidence: The initial downstream analysis was performed in R (v.4.0.4) with the R package Seurat (v.4.0.1) 50 .
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **4.0.2**
- Evidence: For the reclustering of myonuclei, data were processed in Seurat (v.4.0.2) 65 , and only snRNA-seq data were retained for further analysis.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Version used: **4.3.0**
- Evidence: Low-quality cells with fewer than 300 or more than 7,500 genes or more than 10% mitochondrial reads were removed using Seurat v.4.3.0 (ref.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Evidence: Cell counts were produced by Cell Ranger pipelines and transformed into Seurat objects (see ‘Extended scRNA-seq and data analysis’).
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Version used: **4.3.0**
- Evidence: Using Seurat (version 4.3.0), cells with less than 200 features and more than 5% mitochondrial reads were excluded.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### A brain-specific angiogenic mechanism enabled by tip cell specialization. (Nature 2024)

- DOI: 10.1038/s41586-024-07283-6 | PMCID: PMC11041701 | PMID: 38570687
- Evidence: The plates were stored at −80 °C before mRNA-seq using the Smart-Seq2 protocol 72 and analysis using the Seurat v4 toolkit in Rstudio (v.1.1.463) 73 .
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore v0.4.4] -> alignment/mapping [Bowtie2, SAMtools v1.16.1, TopHat v2.1.1, Trim Galore v0.4.4, featureCounts] -> quantification [featureCounts] -> stage not stated [DESeq2 v1.12, ImageJ v1.53c, Seurat]

### Single-cell multiplex chromatin and RNA interactions in ageing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07239-w | PMCID: PMC11023937 | PMID: 38538789
- Version used: **4.3.0**
- Evidence: We then constructed one Seurat object (Seurat v.4.3.0) 65 , 66 for each brain sample with the parameters ‘min.cells = 2 and min.features = 200’ (filtering out genes expressed in no more than two cells and filtering out cells with no more than 200 expressed genes).
- Full pipeline: alignment/mapping [Bowtie2 v5.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Docker, Harmony v0.1.1, R, Seurat v4.3.0, Snakemake]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Evidence: Quality control and downstream analysis was performed using Seurat R package v4.3.0.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Version used: **4.3.0.1**
- Evidence: The resulting feature–barcode raw matrices were loaded in Seurat v.4.3.0.1 and consolidated into one Seurat object.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: Single-cell differential gene expression We performed DGE analysis on the subsampled data with MAST 51 in R (v.4.3) by using the Seurat package.
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **4.0.1**
- Evidence: Cell filtering and clustering After generating the gene–barcode matrix file from Cell Ranger, the individual count matrices were merged together and processed using the Seurat (v.4.0.1) R package 62 ( https://satijalab.org/seurat/ ).
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### A vagal reflex evoked by airway closure. (Nature 2024)

- DOI: 10.1038/s41586-024-07144-2 | PMCID: PMC10972749 | PMID: 38448588
- Version used: **4.1.1**
- Evidence: For analysis, sequence reads were aligned to the mm10 reference transcriptome, and feature barcode matrices were generated using Cell Ranger (10x Genomics; pipeline v.3.1.0), and analysed in R (v.4.1.3) using Seurat (v.4.1.1) for quality control, pre-processing, normalization, clustering and differential expression analysis.
- Full pipeline: quality control [R v4.1.3, Seurat v4.1.1] -> alignment/mapping [R v4.1.3, Seurat v4.1.1] -> normalisation [R v4.1.3, Seurat v4.1.1] -> dimensionality reduction/clustering [R v4.1.3, Seurat v4.1.1, UMAP] -> differential/statistical testing [Enrichr, R v4.1.3, Seurat v4.1.1] -> stage not stated [Fiji v1.52p, ImageJ v1.52p]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **3.2.2**
- Evidence: DGE matrices were processed using the following R and python packages: Seurat (v.3.2.2) 64 , SeuratDisk (v.0.0.0.9010) 65 , anndata (v.0.8.0) 66 , numpy (v.1.17.5) 67 , pandas (v.1.0.5) 68 , 69 and Scanpy (v.1.9.1) 70 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Evidence: For scRNA-seq analysis of Gprc5a −/− ; Sftpc creER/+ ; Rosa Sun1GFP/+ mice, cells with ≤500 detected genes or with a mitochondrial gene fraction that is ≥15% were filtered out using Seurat 41 .
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Basic processing and visualization of the scRNA-seq data were performed with the Seurat package (v.4.0.5) in R (v.4.0.3).
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### Compartmentalized ocular lymphatic system mediates eye-brain immunity. (Nature 2024)

- DOI: 10.1038/s41586-024-07130-8 | PMCID: PMC10990932 | PMID: 38418880
- Version used: **4.9.9.9040**
- Evidence: The generated libraries were sequenced and analysed using Space Ranger (version 2.1.0), and data were analysed using Seurat 4.9.9.9040.
- Full pipeline: stage not stated [ImageJ, Seurat v4.9.9.9040]

### Anti-TIGIT antibody improves PD-L1 blockade through myeloid and T&lt;sub&gt;reg&lt;/sub&gt; cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07121-9 | PMCID: PMC11139643 | PMID: 38418879
- Evidence: Data were converted to a Seurat object and analysed using the Seurat R package (v.3.2.2) according to the standard workflow (Seurat) 53 .
- Full pipeline: alignment/mapping [Bioconductor, R] -> quantification [Bioconductor, R] -> normalisation [Harmony v1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [fgsea] -> stage not stated [Seurat]

### Multisensory gamma stimulation promotes glymphatic clearance of amyloid. (Nature 2024)

- DOI: 10.1038/s41586-024-07132-6 | PMCID: PMC10917684 | PMID: 38418876
- Version used: **4.0.3**
- Evidence: Seurat (v4.0.3) was used for downstream analysis 57 .
- Full pipeline: alignment/mapping [Suite2p] -> quantification [ImageJ] -> normalisation [ImageJ] -> registration [Suite2p] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [Seurat v4.0.3, scDblFinder]

### IL-10 constrains sphingolipid metabolism to limit inflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07098-5 | PMCID: PMC10954550 | PMID: 38383790
- Version used: **4.3.0**
- Evidence: Data analysis was performed using Seurat v4.3.0 R package 66 , including cell-type identification and comparative analyses between conditions.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HTSeq, Picard] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v4.3.0]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: To regress out the cell–cell variation in gene expression driven by batch and cluster data with corrected data in different time points, we used a standard Seurat v3 integration workflow with functions FindIntegrationAnchors() and IntegrateData().
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Evidence: Seurat v3 74 was used for log-normalization and to identify the top 2,000 highly variable genes per sample.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Evidence: In addition, we identified differentially expressed genes between early ( n = 4,949 cells) and late ( n = 3,910 cells) NMPs, using the FindMarkers function of Seurat v3 63 , after filtering out genes that are detected in <10% of cells in both of the two populations.
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Evidence: The non-tumour dataset ( GSE115469 ) 51 control contained five non-tumour individuals. scRNA-seq analysis was conducted using the Seurat package (v.4.3.0) in R studio (4.2.0).
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Circulating myeloid-derived MMP8 in stress susceptibility and depression. (Nature 2024)

- DOI: 10.1038/s41586-023-07015-2 | PMCID: PMC10901735 | PMID: 38326622
- Version used: **3.1.5**
- Evidence: The expression matrix for single-cell data was processed using the package Seurat v3.1.5 in R 74 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, HTSeq v0.12.4, STAR v2.5] -> quantification [ImageJ, Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Version used: **4.2.0**
- Evidence: Data analysis was performed with R v4.1 using Seurat v4.2.0 85 .
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Deciphering cell states and genealogies of human haematopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07066-z | PMCID: PMC10937407 | PMID: 38253266
- Evidence: First we performed community detection-based clustering for all cells on WNN using Seurat 71 .
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### Autoreactive T cells target peripheral nerves in Guillain-Barré syndrome. (Nature 2024)

- DOI: 10.1038/s41586-023-06916-6 | PMCID: PMC10830418 | PMID: 38233524
- Version used: **4.9.9.9059**
- Evidence: After quality control, which involved the filtering of low-quality cells and cell doublets or multiples, and cells with mitochondrial counts higher than 5%, we normalized the data and performed scaling, dimensionality reduction and clustering on the top 2,000 highly variable features in the dataset (Seurat v.4.9.9.9059).
- Full pipeline: quality control [Seurat v4.9.9.9059] -> normalisation [Seurat v4.9.9.9059] -> dimensionality reduction/clustering [Seurat v4.9.9.9059, UMAP] -> stage not stated [R]

### Nasopharyngeal lymphatic plexus is a hub for cerebrospinal fluid drainage. (Nature 2024)

- DOI: 10.1038/s41586-023-06899-4 | PMCID: PMC10808075 | PMID: 38200313
- Evidence: Clustering analysis For clustering and visualization of single cells, the R package Seurat was used (v.4.1.0).
- Full pipeline: read trimming [STAR v2.7.9] -> alignment/mapping [STAR v2.7.9] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [R, Seurat, UMAP] -> stage not stated [ImageJ]

### MRE11 liberates cGAS from nucleosome sequestration during tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-023-06889-6 | PMCID: PMC10794148 | PMID: 38200309
- Version used: **3.1.2**
- Evidence: Processing of scRNA-seq data Data were imported into Seurat (v.3.1.2) using R (v.3.6.0).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Seurat v3.1.2]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Version used: **4.1.0**
- Evidence: All multiome data were analysed in R v.4.1.3 using packages Signac v.1.6.0 and Seurat v.4.1.0.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Modelling post-implantation human development to yolk sac blood emergence. (Nature 2024)

- DOI: 10.1038/s41586-023-06914-8 | PMCID: PMC10849971 | PMID: 38092041
- Evidence: Seurat V4 was used for downstream processing of the scRNA-seq data 66 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Enrichr, Fiji, ImageJ, Seurat]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Version used: **4.3.0**
- Evidence: Mouse brain analysis Quality control and cell type assignment The output generated by Cell Ranger was read into R (v.4.1.1) using Seurat (v.4.3.0) 21 .
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Dictionary of immune responses to cytokines at single-cell resolution. (Nature 2024)

- DOI: 10.1038/s41586-023-06816-9 | PMCID: PMC10781646 | PMID: 38057668
- Evidence: Gene expression and hashtag were matched using the MULTIseqDemux function of the Seurat R package (v.4.1) 42 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.1] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat]

### Hypoblast from human pluripotent stem cells regulates epiblast development. (Nature 2024)

- DOI: 10.1038/s41586-023-06871-2 | PMCID: PMC10849967 | PMID: 38052228
- Evidence: According to the above CheckBlastoids scripts with the gene expression matrices, we performed quality control, normalization, cell annotation, integrated analyses, clustering and visualization using the R Seurat package (v.4.0.4).
- Full pipeline: quality control [Seurat] -> read trimming [Cutadapt v1.15, TopHat] -> alignment/mapping [RSEM v1.3.1, STAR, TopHat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### Lineage-resolved atlas of the developing human cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-09033-8 | PMCID: PMC12589122 | PMID: 41193842
- Version used: **4.3.0.9002**
- Evidence: Cellranger outputs were processed using Seurat v4.3.0.9002 (RRID:SCR_016341).
- Full pipeline: dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [Seurat v4.3.0.9002]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **5.0.3**
- Evidence: Bioinformatics analysis of MERFISH data Single-cell gene expression matrices were obtained by counting messenger RNA (mRNA) molecules within segmented cell boundaries and were further analysed in RStudio using R 4.2.2, Seurat 5.0.3 and custom-made scripts ( https://github.com/SchaferLabUMassChan/Ayata-et-al_2025 ).
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: For earlier developmental ages (P0–P28), cell types were assigned using Seurat 80 (RRID: SCR_016341 ) with the reciprocal PCA (RPCA) label transfer approach (Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Evidence: The remaining 7,665 cells were re-embedded (UMAP from 30 PCs) using 2,000 variable features (Seurat ‘vst’) and reclustered using Louvain (at arbitrary resolution 0.8) into 22 clusters.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Version used: **4.1**
- Evidence: Seurat (v.4.1) 92 was loaded in R (v.4.1) to construct Seurat objects for each sample using RNA matrices.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### Transcriptomic and spatial organization of telencephalic GABAergic neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09296-1 | PMCID: PMC12589142 | PMID: 41193843
- Version used: **5.1.0**
- Evidence: In brief, Seurat (v.5.1.0, RRID: SCR_016341) was used for initial clustering (default parameters).
- Full pipeline: quantification [R, UMAP] -> dimensionality reduction/clustering [R, Seurat v5.1.0, UMAP] -> stage not stated [scDblFinder]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Version used: **5.0.1**
- Evidence: We also labelled our cells using Seurat (v.5.0.1) 54 ( https://zenodo.org/doi/10.5281/zenodo.7779016 ), first transforming to reference dataset using SCTransform followed by FindTransferAnchors and MapQuery to assign cell types.
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Evidence: The count matrix from each sample was merged into a single AnnData object by Scanpy, and doublets were removed running Scrublet software in Python before conversion to Seurat using SeuratDisk’s function Convert 57 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: A single counts matrix directory containing all samples for a particular analysis was used as input for Seurat analysis in R (4.1.1) 31 , 57 .
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Evidence: Single-cell data processing was done using R (v4.2.3), R-studio (Build 513) and the Seurat package (v5.2.1) 75 .
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Evidence: Principal component analysis was performed on the expression data matrix using the Seurat.
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### A parabrachial hub for need-state control of enduring pain. (Nature 2025)

- DOI: 10.1038/s41586-025-09602-x | PMCID: PMC12630001 | PMID: 41062698
- Evidence: Seurat’s default LogNormalize method was used, where feature counts per cell were divided by the total transcript counts for that cell, and counts were multiplied by a scale factor and then transformed using natural log (log1p).
- Full pipeline: quantification [NumPy, Scanpy] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP, seaborn] -> visualisation [UMAP, seaborn] -> stage not stated [AnnData, ImageJ]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: Full count matrices with background RNA removed were further analysed using Seurat 90 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### Tracking clonal evolution during treatment in ovarian cancer using cell-free DNA. (Nature 2025)

- DOI: 10.1038/s41586-025-09580-0 | PMCID: PMC12629990 | PMID: 41034582
- Evidence: Pathway scoring was performed with PROGENY 54 or the Seurat module scoring function using hallmark pathways.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Mutect2, Seurat]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Version used: **3.2.2**
- Evidence: Uniform manifold approximation and projection plots were generated using the R package Seurat (v.3.2.2) with default settings.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Evidence: For violin plots, data were first converted from anndata objects to Seurat objects using the readH5AD() function in the zellkonverter package and the CreateSeuratObject() function in the SeuratObject package and then plotted in R using Seurat’s VlnPlot() function or the plotColData function in the scater package.
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Evidence: The Seurat workflow within the singleCellTK package was used for clustering starting with the decontaminated counts from decontx 48 .
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### A neuronal architecture underlying autonomic dysreflexia. (Nature 2025)

- DOI: 10.1038/s41586-025-09487-w | PMCID: PMC12571909 | PMID: 40963010
- Evidence: Seurat 31 was used to calculate quality control metrics for each cell barcode, including the number of genes detected, number of UMIs and proportion of reads aligned to mitochondrial genes.
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain, QuPath v0.4.3]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Evidence: To annotate the cells from the cloaca, the raw matrix of single-cell RNA sequencing (scRNA-seq) from a previous study 38 was downloaded from GEO ( GSE223922 ) and stored in a Seurat object.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Neuronal activity-dependent mechanisms of small cell lung cancer pathogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09492-z | PMCID: PMC12571889 | PMID: 40931074
- Evidence: Seurat 62 (v.5.0.1) was employed for data loading at the individual sample level.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scDblFinder] -> stage not stated [Fiji v2.1.0, GSEA, GSVA, ImageJ v2.1.0, Seurat, fgsea]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: The expression matrices were then quality-controlled, dimensionally reduced, annotated and visualized using the Seurat package 45 in R .
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### Single-cell transcriptomic and genomic changes in the ageing human brain. (Nature 2025)

- DOI: 10.1038/s41586-025-09435-8 | PMCID: PMC12527935 | PMID: 40903571
- Evidence: The barcode and UMI solved counts were further processed with Seurat 62 (v.4.3.0).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Cellpose, GATK v4.1.8.1, Picard, Seurat]

### Spatial joint profiling of DNA methylome and transcriptome in tissues. (Nature 2025)

- DOI: 10.1038/s41586-025-09478-x | PMCID: PMC12571926 | PMID: 40903587
- Evidence: The gene matrix was then imported into R for downstream spatial transcriptomic analysis using Seurat package (v.5.1.0) 57 .
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [Python, R, UMAP, clusterProfiler, pheatmap] -> visualisation [Python] -> stage not stated [HOMER, Seurat]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Data were processed using the Seurat R package, version 4.2.1 95 .
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Maternal stress triggers early-life eczema through fetal mast cell programming. (Nature 2025)

- DOI: 10.1038/s41586-025-09419-8 | PMCID: PMC12488486 | PMID: 40866704
- Evidence: Seurat package v.4.3.0.1 (ref.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2 v1.34.0, ImageJ v2.16.0, Seurat, Signac v1.14.0]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: For scRNA-seq, output from the Cell Ranger software was analysed using two different pipelines: (1) Scanpy, which is explained in detail under the SCENIC+ analysis; and (2) the Seurat pipeline, which is explained below.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: All analyses were performed in R using Seurat 83 (v.4.4.0 and v.5.0.1).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Evidence: Data were processed and analysed using the Seurat package (v5.0.3) in R (v4.4.1).
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Version used: **5.1.0**
- Evidence: Transcript count matrices were used as inputs to the Seurat (v.5.1.0) gene expression analysis pipeline.
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Version used: **4.1.1**
- Evidence: Functions in the R package Seurat (v.4.1.1) were used for downstream analysis 66 .
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: PDX and normal mouse brain data were then merged after selection of common features using the SelectIntegrationFeatures function from Seurat 60 , using RunHarmony in the Harmony package 58 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Expanding the cytokine receptor alphabet reprograms T cells into diverse states. (Nature 2025)

- DOI: 10.1038/s41586-025-09393-1 | PMCID: PMC12460165 | PMID: 40804519
- Version used: **5.1.0**
- Evidence: Analysis of scRNA-seq data The gene expression matrix was first processed using Seurat (v.5.1.0).
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC, MACS2 v3.0.1] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [R v4.4, SCENIC v0.12.1]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Evidence: Counts were analysed using Seurat (v.5) 98 and all cells with fewer than 500 or more than 20,000 unique molecular identifiers, fewer than 200 genes and mitochondrial content higher than 20% were filtered out.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Version used: **5.0.3**
- Evidence: Filtered counts matrices were loaded with Seurat v.5.0.3 (ref.
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: The generated counts table was loaded to Seurat (v.4) 72 to generate Seurat objects.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Microglia regulate GABAergic neurogenesis in prenatal human brain through IGF1. (Nature 2025)

- DOI: 10.1038/s41586-025-09362-8 | PMCID: PMC12527950 | PMID: 40770097
- Version used: **5.1.0**
- Evidence: The output (count matrix) was used as the main input file for all downstream analyses using Seurat v.5.1.0.
- Full pipeline: quantification [ImageJ v1.54] -> normalisation [UMAP] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [ImageJ v1.54] -> simulation/modelling [Monocle] -> visualisation [Monocle] -> stage not stated [CellChat, Enrichr, Scanpy v1.10.3, Seurat v5.1.0, scDblFinder v2.0.3]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: Seurat (R package, v.2.3.0), Scanpy (v.1.8) and cellxgene (v.1.0.1) were used for cell clustering and annotation.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: The counts were analysed using the Seurat R package 57 .
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### A molecular cell atlas of mouse lemur, an emerging model primate. (Nature 2025)

- DOI: 10.1038/s41586-025-09113-9 | PMCID: PMC12328211 | PMID: 40739356
- Evidence: Cell clustering, annotation and cluster markers from scRNA-seq profiles Cell clustering and annotation of each tissue processed by 10x Transcriptomic profiles of cells from each tissue and from each individual lemur were clustered separately using Seurat software (v.2.3.0) for R studio (v.3.6.1).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: Downstream analyses included quality control, normalization, dimensional reduction and clustering, variable gene selection, spatially variable feature detection, annotation, differential expression and integration with multiple samples using Seurat 62 .
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Mitochondrial origins of the pressure to sleep. (Nature 2025)

- DOI: 10.1038/s41586-025-09261-y | PMCID: PMC12443607 | PMID: 40670797
- Version used: **4.1**
- Evidence: All subsequent analyses were performed in R, using the Seurat v.4.1 package 102 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [STAR v2.6.1b, Seurat v4.1]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: Cell-cycle analysis Discrete cell-cycle phase information was computed using Seurat’s CellCycleScoring function, excluding samples with fewer than 20 malignant cells.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Gene counts were read into R using Seurat and converted to AnnData 74 with SeuratData and SeuratDisk.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **4.1.0**
- Evidence: ...0), forcats (0.5.1), stringr (1.4.0), dplyr (1.0.7), purrr (0.3.4), readr (2.1.2), tidyr (1.1.4), tibble (3.1.6), ggplot2 (3.3.5), tidyverse (1.3.1), SeuratObject (4.0.4), Seurat (4.1.0), SingleCellExperiment (1.16.0), SummarizedExperiment (1.24.0), GenomicRanges (1.46.1), GenomeInfoDb (1.30.1), IRanges (2.28.0), S4Vectors (0.32.3), MatrixGenerics (1.6.0), matrixStats (0.61.0), GEOquery (2.62.2), ...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Version used: **4.0.6**
- Evidence: Obtained raw unique molecular identifier (UMI) count matrices of valid barcoded cells for each port were loaded into R (v.4.1.2) for further analyses using Bioconductor packages 66 and Seurat (v.4.0.6) 67 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: Filtered count matrices were processed separately using Seurat 54 and SeuratObject.
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Nutrients activate distinct patterns of small-intestinal enteric neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09228-z | PMCID: PMC12390836 | PMID: 40634617
- Version used: **4.1.0**
- Evidence: The data were analysed in R (v.4.1.2) using the Seurat (v.4.1.0) package.
- Full pipeline: stage not stated [ImageJ, R v4.1.2, Seurat v4.1.0]

### Rewiring endogenous genes in CAR T cells for tumour-restricted payload delivery. (Nature 2025)

- DOI: 10.1038/s41586-025-09212-7 | PMCID: PMC12328239 | PMID: 40604285
- Evidence: Seurat was then used to further cluster integrated datasets into meta-clusters.
- Full pipeline: quality control [Cutadapt v2.1] -> read trimming [edgeR v3.8.5] -> alignment/mapping [HISAT2] -> normalisation [edgeR v3.8.5] -> dimensionality reduction/clustering [Seurat] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### Range extender mediates long-distance enhancer activity. (Nature 2025)

- DOI: 10.1038/s41586-025-09221-6 | PMCID: PMC12267059 | PMID: 40604280
- Evidence: Transcriptome data were normalized and dimensionality was reduced using PCA (Seurat).
- Full pipeline: alignment/mapping [BEDTools] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER] -> stage not stated [MACS2, R, Signac]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: Quality control and cell filtration Datasets were analysed in R v4.0.3 with Seurat v4 (ref.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: Count matrices were further preprocessed using the Seurat R package (v4.3.0) and R (version 4.4.0) 63 .
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: Then, addClusters, which uses Seurat’s graph clustering as the default clustering method, was used to call clusters in the reduced dimension subspace.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: Single-cell RNA-seq and ATAC-seq data were processed using mainly the Seurat and Signac packages in R.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: Seurat 60 – 63 was used to perform the scRNA-seq data analysis, and the.h5ad file was converted into a Seurat object using the R package zellkonverter.
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### Increased CSF drainage by non-invasive manipulation of cervical lymphatics. (Nature 2025)

- DOI: 10.1038/s41586-025-09052-5 | PMCID: PMC12267054 | PMID: 40468071
- Version used: **5.0.3**
- Evidence: Raw expression matrices were constructed using Read10X function in the ‘R’ package Seurat (v5.0.3).
- Full pipeline: stage not stated [ImageJ, Seurat v5.0.3]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Evidence: In data from the in vivo model, CAR19–IL-15 NK cells from time points with greater than 100 NK cells were retained (before and after infusion (day 7 and day 14)) and were processed using a standard Seurat workflow 58 .
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: The gene expression matrices obtained from CellRanger were analysed using the R package Seurat (v.5).
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Evidence: The scRNA-seq analysis was performed using Seurat 56 package (v5.0.1).
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: Utilizing the Seurat R package 66 , we applied the AddModuleScore function to calculate scores for individual RNA-seq samples based on these CMT signature sets.
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### A coordinated cellular network regulates tolerance to food. (Nature 2025)

- DOI: 10.1038/s41586-025-09173-x | PMCID: PMC12328219 | PMID: 40425043
- Evidence: Demultiplexing of cell hashing oligo-tagged antibodies was applied to the Cell Ranger feature-barcode matrix file ‘filtered_feature_bc_matrix.h5’ using the HTODemux function and the Seurat package v.5.0.0 in R (v.4.3.1), applying a positive.quantile threshold of 0.95.
- Full pipeline: read trimming [R v4.3.1, Seurat] -> dimensionality reduction/clustering [UMAP]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: Unsupervised clustering and differential gene expression analysis was performed with the Seurat R toolkit 69 .
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### Clonal tracing with somatic epimutations reveals dynamics of blood ageing. (Nature 2025)

- DOI: 10.1038/s41586-025-09041-8 | PMCID: PMC12240852 | PMID: 40399669
- Evidence: Data integration and annotation of cell states We constructed Seurat 61 objects for each of the scTAM-seq samples individually using the binary DNA methylation matrix.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, Seurat]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Evidence: For visualization and clustering, Seurat_5.0.1 and R (v.4.3.1, 2023-06-16) were used on the BCH compute nodes.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Version used: **4.3.0**
- Evidence: The single-cell RNA-seq analysis of TNBC (cohort 3) (dataset GSE169246 ) was conducted in R using Seurat (v.4.3.0), ssGSEA, and standard data wrangling and plotting packages.
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Version used: **4.3.0**
- Evidence: Raw counts were loaded into Seurat (4.3.0) 80 for analysis in R (4.2.2).
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Taurine from tumour niche drives glycolysis to promote leukaemogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09018-7 | PMCID: PMC12328231 | PMID: 40369079
- Version used: **4.1.0**
- Evidence: Seurat v.4.1.0 within R v.4.1.1 was used for most of processing.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> differential/statistical testing [DESeq2 v1.28.1, Enrichr] -> stage not stated [Seurat v4.1.0, tidyverse v1.2.0]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Further, the gene expression matrices from all samples were merged together in the full matrix and processed by means of the Seurat package 43 to normalize, compute top principal complements ( n = 30), find most highly variable genes ( n = 2,500) and visualize by means of UMAP.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Version used: **3.1.5**
- Evidence: Normalization, annotation and integration of scRNA-seq datasets Downstream analyses were conducted using Seurat v.3.1.5.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Cell cycle duration determines oncogenic transformation capacity. (Nature 2025)

- DOI: 10.1038/s41586-025-08935-x | PMCID: PMC12119354 | PMID: 40307557
- Evidence: Quality control and normalization After removing non-retinal cells, data was further processed and analysed mainly by Scanpy Python toolkit ( https://github.com/scverse/scanpy ) and Seurat R toolkit ( https://github.com/satijalab/seurat ).
- Full pipeline: quality control [Scanpy, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr]

### A distributed coding logic for thermosensation and inflammatory pain. (Nature 2025)

- DOI: 10.1038/s41586-025-08875-6 | PMCID: PMC12222022 | PMID: 40269164
- Evidence: Single-cell sequencing data from DRG 28 were obtained from GEO Series GSE254789 and analysed with Seurat v.5 in RStudio.
- Full pipeline: quantification [NumPy v1.19.2, SciPy v1.5.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.19.2, SciPy v1.5.2] -> stage not stated [ImageJ, OpenCV, Python, Seurat, scDblFinder]

### PRDM16-dependent antigen-presenting cells induce tolerance to gut antigens. (Nature 2025)

- DOI: 10.1038/s41586-025-08982-4 | PMCID: PMC12176658 | PMID: 40228524
- Version used: **5.1**
- Evidence: We utilized a completely unsupervised computational workflow that analysed all cells in aggregate, utilizing the most recent methods 61 within Seurat version 5.1 (including the sctransform function) for normalization of gene expression, anchor-based integration (based on 3,000 features), and shared nearest-neighbour cluster identification.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.3, Picard, SAMtools v0.1.19] -> normalisation [Seurat v5.1] -> dimensionality reduction/clustering [Seurat v5.1, UMAP] -> stage not stated [Signac v1.14]

### Human assembloid model of the ascending neural sensory pathway. (Nature 2025)

- DOI: 10.1038/s41586-025-08808-3 | PMCID: PMC12137141 | PMID: 40205039
- Version used: **4.3.0**
- Evidence: Further downstream analyses were performed using the R package Seurat (v.4.3.0).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0]

### Spatially resolved mapping of cells associated with human complex traits. (Nature 2025)

- DOI: 10.1038/s41586-025-08757-x | PMCID: PMC12095064 | PMID: 40108460
- Evidence: The module score of these 417 drug targets genes for individual spots was computed using the AddModuleScore function in the Seurat (V4.4.0) R package with the default settings 83 , 84 GO term enrichment We performed GO term enrichment analysis using the clusterProfiler 85 (V3.18) R package with the default settings.
- Full pipeline: alignment/mapping [R] -> variant calling [GCTA] -> normalisation [Scanpy] -> dimensionality reduction/clustering [PLINK, Seurat, clusterProfiler] -> differential/statistical testing [MAGMA] -> simulation/modelling [PLINK] -> stage not stated [LDSC]

### Transient silencing of hypermutation preserves B cell affinity during clonal bursting. (Nature 2025)

- DOI: 10.1038/s41586-025-08687-8 | PMCID: PMC12058519 | PMID: 40108454
- Version used: **5.1.0**
- Evidence: Transcriptomic analysis was performed using Seurat v.5.1.0.
- Full pipeline: differential/statistical testing [R v4.3.1] -> stage not stated [Seurat v5.1.0]

### Regulated somatic hypermutation enhances antibody affinity maturation. (Nature 2025)

- DOI: 10.1038/s41586-025-08728-2 | PMCID: PMC12058521 | PMID: 40108475
- Version used: **4.3.0**
- Evidence: Single-cell library processing scRNA-seq and Hashtag-oligos unique molecular identifier quantification were performed with Cell Ranger multi v.7.1.0 (10x Genomics), using the Cell Ranger GEX reference mm10, and analysed in R with Seurat v.4.3.0 (ref.
- Full pipeline: quantification [Seurat v4.3.0]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **4.1**
- Evidence: For gene expression sequencing, the filtered count matrices were read into the R package Seurat (v.4.1).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### TGFβ links EBV to multisystem inflammatory syndrome in children. (Nature 2025)

- DOI: 10.1038/s41586-025-08697-6 | PMCID: PMC12003184 | PMID: 40074901
- Evidence: Next, cellranger’s aggr was used to merge the libraries without size normalization and further analysed in R (version 4.1.2) using the Seurat package (version 4.0.5) 65 .
- Full pipeline: normalisation [GSEA, R v4.1.2, Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, pheatmap]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: The libraries from each condition ( iDTR WT , iDTR het , Rspo3 fl/fl , Rspo3 ΔHSC ) were integrated together using the R package Seurat 76 .
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Version used: **5.1.0**
- Evidence: Raw Xenium data were imported in Seurat (v5.1.0) and integrated using reciprocal principal component analysis to remove batch effect correction.
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Evidence: Cross-species integration, clustering, visualization and differential expression Integration, clustering, visualization, and differential expression analysis were performed using Seurat.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: For initial analysis, we relied on the R package Seurat (RRID:SCR_016341) and standard data analysis practices.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Version used: **4.3.0**
- Evidence: Clustering of embryonic cells on the basis of histone modifications was performed using Seurat (v.4.3.0).
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: Data processing and visualization The raw matrices outputs of STARsolo (no filtration of cells) for each tumour and GBO library were gzipped and used as input for Seurat 61 using the Read10X() function with the default parameters.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Glycocalyx dysregulation impairs blood-brain barrier in ageing and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08589-9 | PMCID: PMC11946907 | PMID: 40011765
- Version used: **4.1.1**
- Evidence: We used Seurat (v4.1.1) to further exclude cells with fewer than 200 or more than 5,000 features and cells with more than 10% mitochondrial genes.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.32, Metascape] -> visualisation [DESeq2 v1.32] -> stage not stated [ImageJ, Seurat v4.1.1, SoupX v1.6.2, scDblFinder v2.0.4]

### GABAergic neuron-to-glioma synapses in diffuse midline gliomas. (Nature 2025)

- DOI: 10.1038/s41586-024-08579-3 | PMCID: PMC11946904 | PMID: 39972132
- Evidence: To examine the various GABA A R signatures of each of the cells in each cluster, we used the function AddModuleScore by the Seurat package, which calculates the average expression levels of the gene set subtracted by the aggregated expression of 100 randomly chosen control gene sets, where the control gene sets are chosen from matching 25 expression bins corresponding to the tested gene set expres...
- Full pipeline: quantification [ImageJ v2.1.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [ggpubr]

### Macrophages protect against sensory axon loss in peripheral neuropathy. (Nature 2025)

- DOI: 10.1038/s41586-024-08535-1 | PMCID: PMC11964918 | PMID: 39939762
- Version used: **5.0.1**
- Evidence: Seurat version 5.0.1 implemented in R version 4.3.2 was used for downstream analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.3.2, Seurat v5.0.1]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: The data from each of the 11 batches were filtered using the Seurat R package version 5.1.0 61 , to ensure analysis of high quality cells, including filtering out cells expressing less than 600 or higher than 4,000 genes, cells with more than 7,500 UMIs, or containing higher than 10% mitochondrial genes.
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Evidence: We additionally ran an initial Seurat-based processing of the whole dataset, including detection of highly variable features, scaling of data, principal component analysis and preliminary clustering 54 .
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Version used: **4.3.0**
- Evidence: Analysis of scRNA-seq and scTCR-seq data from vaccine-site skin scRNA-seq data were imported and read using a custom function built on the Seurat (v.4.3.0) pipeline 76 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: These datasets were preprocessed and annotated 7 , and we downloaded them as Seurat objects from http://tome.gs.washington.edu/ .
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Evidence: Seurat v.3 (v.5.0.3) 59 was used to scale the digital gene expression matrix by total UMI count, multiplied by the mean number of transcripts, and values were log transformed.
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: To find cell-type marker genes, we used the Seurat FindMarkers function.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: To establish a human intratumoural ILC2 transcriptional signature (ILC2 score), we first identified candidate differentially expressed genes in rIL-33-activated KLRG1 + ILC2s in tumours and DLNs of PDAC mice, based on purified single-cell transcriptomes (from scRNA-seq above) using the Seurat package on R.
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Version used: **3.0.2**
- Evidence: 56 ), and principal component analyses was done by using the ‘plotPCA’ function after variance-stabilizing transformation. scRNA-seq analyses CellRanger (v.3.0) was used to generate gene expression matrix for each cell, which was further processed by Seurat (v.3.0.2) 57 for data combination, dimension reduction, clustering and gene differential expression analysis.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Evidence: For RNA-seq data, normalization and data scaling were performed using SCTransform v2 (v.0.4.1) 53 in Seurat (v.4) 6 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: Count data were analysed using the R packages Seurat (v.5) 49 and Signac 50 .
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Version used: **4.0.3**
- Evidence: Data were analysed in R (v.4.1.0) using Seurat (v.4.0.3) 46 and Signac (v.1.3.0) 47 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Version used: **4.5**
- Evidence: Seurat (v4.5) was used to integrate and cluster data from all samples together.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Version used: **4.1.0**
- Evidence: Raw UMI count matrices for all samples were first imported using Seurat (v4.1.0) 42 ( www.satijalab.org/seurat ), and immediately subject to ambient RNA correction using a customized version of the SoupX (v1.6.2) R pipeline ( https://github.com/constantAmateur/SoupX ) 43 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Version used: **4.3.0**
- Evidence: R (v.4.3.0) 53 and Seurat (v.4.3.0) 54 were used for data processing.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: Perturb-seq analysis was performed in R (v4.3.1) using Seurat 48 (v4.3.0.1) based on code previously published 49 .
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Skin autonomous antibody production regulates host-microbiota interactions. (Nature 2025)

- DOI: 10.1038/s41586-024-08376-y | PMCID: PMC11864984 | PMID: 39662506
- Version used: **5.0.2**
- Evidence: In the downstream analysis of the expression data, the cellranger output (filtered_feature_bc_matrix) was loaded into Seurat (v5.0.2) 61 using the CreateSeuratObject function, which retained the genes detected in at least 3 cells with at least 200 genes detected per cell (min.cells = 3 and min.features = 200).
- Full pipeline: normalisation [R, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v5.0.2]

### Macrophages excite muscle spindles with glutamate to bolster locomotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08272-5 | PMCID: PMC11735391 | PMID: 39633045
- Evidence: Seurat objects for each sample were created by converting the count matrix and performing initial quality control.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [DESeq2, ImageJ, ggplot2, scDblFinder]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Version used: **4.0.5**
- Evidence: The computational analysis of the 10x Genomics UMI count matrices was performed using the R package Seurat (v.4.0.5).
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Version used: **4.3.0**
- Evidence: Further processing was performed in R (v.4.2.2) with Seurat (v.4.3.0).
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: Annotated gene counts were processed with Seurat 54 v.3.6.3 (organoids) or v.4.1.1 (SI tissue).
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### Endogenous self-peptides guard immune privilege of the central nervous system. (Nature 2025)

- DOI: 10.1038/s41586-024-08279-y | PMCID: PMC11666455 | PMID: 39476864
- Evidence: The resulting log 2 -transformed values were transformed to the natural-log scale for compatibility with the Seurat (v.3) pipeline 45 – 47 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR, limma] -> stage not stated [Seurat]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Evidence: The reads were mapped to mouse genome (mm10) using hisat2 (v.2.1.0) 63 , and mapped reads were assembled with FeatureCounts (v.2.0.0). scRNA-seq data analysis of cerebellar cell types A publicly available Seurat object containing single-cell RNA-seq (scRNA-seq) data from cerebellar tissue (24,409 genes across 611,034 cells) was obtained from a previously published study ( https://singlecell.broadi...
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **5.0.1**
- Evidence: Processing of Klotho -KO snRNA-seq data The sequenced snRNA-seq raw data were processed with Cell Ranger (v7.0.0) and Seurat (v5.0.1) package.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **4.3.0**
- Evidence: Cell Ranger filtered outputs were analysed using Seurat v4.3.0 81 , and mitochondrial RNA content per cell was calculated using the GRCm39 (mm10) genome annotation and regressed out using SCTransform normalization protocol included in the Seurat toolkit with 20 principal components and a resolution of 0.1.
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: The cell (or spot)-gene-expression matrix of each sample was normalized to 1 × 10 5 and log 2 -scaled using Seurat (v.5) 62 .
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Version used: **4.3.0**
- Evidence: Cohort 1 scRNA-seq data, as well as publicly available data without cell-type annotations (bladder cancer, lung cancer, ovarian cancer, prostate cancer and pancreatic cancer), were analysed using Seurat (v.4.3.0) 67 as described below.
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **5.2.1**
- Evidence: Filtered feature matrices were loaded to Seurat (v.5.2.1) 67 .
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: We identified 3,000 highly variable genes using the Seurat flavour in Scanpy with dataid as the batch key.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Early fibrotic niches establish tumour-permissive microenvironments. (Nature 2026)

- DOI: 10.1038/s41586-026-10399-6 | PMCID: PMC13149335 | PMID: 42020743
- Evidence: Quality control Analysis of count matrices was performed in R using the Seurat package 59 or Scanpy 60 pipeline (v.1.9.1).
- Full pipeline: quality control [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [CellChat, Fiji, ImageJ, QuPath]

### Focal white matter lesions drive grey matter inflammation and synapse loss. (Nature 2026)

- DOI: 10.1038/s41586-026-10414-w | PMCID: PMC13293868 | PMID: 42020752
- Evidence: Count matrices were loaded into a Seurat object (v.5.1.0) 65 , retaining only barcodes corresponding to tissue-covered pixels.
- Full pipeline: read trimming [Snakemake v7.24.0] -> quantification [ImageJ v1.54p] -> dimensionality reduction/clustering [UMAP] -> visualisation [Bioconductor, ComplexHeatmap, UMAP] -> stage not stated [Python, R, Seurat, igraph]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Version used: **5.3.0**
- Evidence: Count matrices per organ were imported into R (v.4.3.3) and processed using Seurat (v.5.3.0) in RStudio (v.2025.05.1).
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **4.2.0**
- Evidence: Seurat (4.2.0; ref.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **5.0.1**
- Evidence: Gene expression was analysed using Seurat (v.5.0.1) 74 .
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Polyclonal selection of immune checkpoint mutations in thyroid autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10493-9 | PMCID: PMC13233322 | PMID: 41981327
- Evidence: Xenium output data were imported into an R v.4.4.1 environment and processed with the Seurat R package 80 , 81 (v.5.3.0).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [R, Seurat, ggpubr, tidyverse]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: For snRNA-seq, gene expression count matrices were integrated using reciprocal principal components analysis projection in Seurat (v.4) 39 .
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Version used: **4.3.0**
- Evidence: RNA normalization, ambient RNA removal, dimensionality reduction and clustering We used Seurat (v4.3.0) 100 in R (v4.1.2) to process filtered RNA sparse matrices into Seurat objects per organ 100 .
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: The data were normalized using ‘LogNormalize’, and principal component analysis was performed based on the top 2,000 variant genes using the R package ‘Seurat’ (v.5.0.3).
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: Gene list scores were calculated using Scanpy’s score_genes or Seurat’s AddModuleScore function, with 500 random genes selected as negative controls to establish baseline scores.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Evidence: CellRanger-filtered count matrices per sample were preprocessed individually with the Seurat pipeline and filtered further (nFeature_RNA > 400, percent.mt < 3/4 quartile+ 3 times interquartile, genes expressed > 3 cells) and doublets were identified by DoubletFinder (v.2.0.3) 62 .
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **5.1.0**
- Evidence: We assessed data quality at the individual nucleus level and retained high-quality nuclei using Seurat (v.5.1.0, https://satijalab.org/seurat ) and Signac (v.1.14.0, https://github.com/timoast/signac ), applying the following criteria: total ATAC fragment count (nCount_ATAC) of at least 3,000, transcription start site enrichment scores between 2 and 15, total RNA counts (nCount_RNA) of at least 2,...
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: Transcriptional data were analysed using Seurat 99 (v.5.1.0) for R.
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Evidence: Principal component analysis, UMAP projection and clustering were performed using Seurat (v5) 47 .
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Version used: **4.3.0**
- Evidence: Downstream analyses were performed in R v.4.2.2 using Seurat (v.4.3.0 or newer), including quality control, data normalization, data scaling, dimension reduction (both linear and nonlinear), clustering, differential expression analysis, batch-effect correction, data visualization, and UMAP generation.
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Facile induction of immune tolerance by an interleukin-2-TGFβ surrogate agonist. (Nature 2026)

- DOI: 10.1038/s41586-026-10208-0 | PMCID: PMC13190267 | PMID: 41813890
- Version used: **5.1.0**
- Evidence: The gene expression matrix was processed and analysed using Seurat (v.5.1.0) 46 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, featureCounts, fgsea] -> stage not stated [Metascape, SCENIC]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Evidence: Single-cell RNA sequencing analysis To determine Gpr84 expression in intestinal immune cells, a single cell RNA sequencing dataset of intestinal leucocytes was re-analysed 38 using Seurat v.4 (ref.
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Evidence: To discriminate between malignant and non-malignant cells, we used (1) Seurat clustering; (2) unbiased cell type annotation using the automated annotation package SingleR (v.1.6.1) using the Human Primary Cell Atlas 55 as a reference; and (3) inference of copy-number variation (CNV) using the InferCNV R package (v.1.8.0).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **4.3.0**
- Evidence: ...roups ( n = 15 for healthy individuals and n = 15 for patients with DLBCL in plasma clustering analyses), were first transformed and normalized using Seurat (v.4.3.0). log-normalization with a scale factor of 100,000 was applied, followed by the identification of highly variable features using variance-stabilizing transformation.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Precancerous niche remodelling dictates nascent tumour persistence. (Nature 2026)

- DOI: 10.1038/s41586-026-10157-8 | PMCID: PMC13148994 | PMID: 41781610
- Evidence: Count matrices were processed using a standard Seurat workflow 67 (v.5.0.3) up to dimensionality reduction.
- Full pipeline: variant calling [R] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [SAMtools, scDblFinder]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Version used: **4.3.0**
- Evidence: Seurat v.4.3.0 (ref.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: Clustering was performed on the RNA-seq data, anticipating that gene expression would have a higher dynamic range than open chromatin, using the Seurat package in R 49 .
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### Dynamic antigen expression and cytotoxic T cell resistance in HIV reservoir clones. (Nature 2026)

- DOI: 10.1038/s41586-026-10298-w | PMCID: PMC13190302 | PMID: 41735521
- Version used: **5.1.0**
- Evidence: Seurat normalization The count matrices of all modalities were loaded into a Seurat v5 object (Seurat v5.1.0).
- Full pipeline: normalisation [Seurat v5.1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> visualisation [limma] -> stage not stated [MACS2]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Evidence: Following data processing using the Seurat package (v5.2.1) in R (v4.3.2), 37,033 cells annotated to 8 cell types remained for the scDRS analysis.
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: Cell-containing droplets were selected using the HTODemux function available in the Seurat programme.
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Evidence: Single-cell gene expression analysis Count matrices were analysed using Seurat software v.5.1.0 42 .
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### Agouti integrates environmental cues to regulate paternal behaviour. (Nature 2026)

- DOI: 10.1038/s41586-026-10123-4 | PMCID: PMC13019464 | PMID: 41708861
- Evidence: Subsequent bioinformatic steps were carried out in the R package Seurat 66 .
- Full pipeline: read trimming [R, scDblFinder] -> dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [DESeq2, Seurat]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: For each guide RNA KO, Seurat’s FindMarkers() function was used to quantify log 2 FC in the expression of a gene with respect to the gScramble condition.
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: The UMI count matrix underwent preprocessing utilizing the Scanpy package (v.1.9.2) and the Seurat R package (v.2.4.3).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Rete ridges form via evolutionarily distinct mechanisms in mammalian skin. (Nature 2026)

- DOI: 10.1038/s41586-025-10055-5 | PMCID: PMC12959975 | PMID: 41639458
- Evidence: ...eq analysis We analysed our pig scRNA-seq datasets and reanalysed previously published human and mouse scRNA-seq datasets 12 , 26 , 35 , 36 using the Seurat package 70 in R.
- Full pipeline: quality control [UMAP] -> quantification [Fiji v1.53c, ImageJ v1.53c, R v4.2.2] -> normalisation [UMAP] -> registration [Python v3.8.20] -> dimensionality reduction/clustering [CellChat, ComplexHeatmap, UMAP] -> visualisation [Python v3.8.20, R v4.2.2] -> stage not stated [Monocle, Seurat]

### Tumour-brain crosstalk restrains cancer immunity via a sensory-sympathetic axis. (Nature 2026)

- DOI: 10.1038/s41586-025-10028-8 | PMCID: PMC12935554 | PMID: 41639447
- Evidence: Low-quality cells were filtered and the remaining cells were clustered using the R package Seurat v.3 as described previously 15 .
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [GSEA, ImageJ, QuPath]

### Ontogeny and transcriptional regulation of Thetis cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10198-z | PMCID: PMC13171621 | PMID: 41634202
- Version used: **4.4.0**
- Evidence: Each sample was further demultiplexed based on HTO counts using HTODemux function in Seurat v.4.4.0.
- Full pipeline: read trimming [Seurat v4.4.0] -> alignment/mapping [STAR v2.7.11a] -> dimensionality reduction/clustering [ArchR v1.0.3, Scanpy, UMAP] -> visualisation [ArchR v1.0.3, UMAP]

### A cross-population compendium of gene-environment interactions. (Nature 2026)

- DOI: 10.1038/s41586-025-10054-6 | PMCID: PMC12999510 | PMID: 41606330
- Version used: **4.3.0.1**
- Evidence: ...terPlus v.1.50.0 ( https://bioconductor.org/packages/release/bioc/html/ConsensusClusterPlus.html ), ACAT v.0.91 ( https://github.com/yaowuliu/ACAT ), Seurat v.4.3.0.1 ( https://satijalab.org/seurat/ ) and susieR v.0.12.35 ( https://stephenslab.github.io/susieR/ ).
- Full pipeline: variant calling [IMPUTE2] -> dimensionality reduction/clustering [R, Seurat v4.3.0.1, UMAP] -> differential/statistical testing [MAGMA] -> stage not stated [BCFtools, LDSC v1.0.0, PLINK v2.00a]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: Single-cell datasets were processed and integrated separately using standard Seurat v.5 workflows.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Evidence: The 148 ExWAS-associated genes were input alongside the preprocessed Seurat 41 object into the AddModuleScore function with default hyperparameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### Vagal blood volume receptors compensate for haemorrhage and posture change. (Nature 2026)

- DOI: 10.1038/s41586-025-10010-4 | PMCID: PMC13017543 | PMID: 41606321
- Evidence: UMAP plots UMAP plots were generated by analysis of published single-cell transcriptomic data of vagal sensory neurons 16 using Seurat in R.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [Fiji, ImageJ, ilastik, scikit-image]

### Intestinal macrophages modulate synucleinopathy along the gut-brain axis. (Nature 2026)

- DOI: 10.1038/s41586-025-09984-y | PMCID: PMC12960212 | PMID: 41606336
- Version used: **4.3**
- Evidence: Integrated analysis of multimodal single-cell data in R (v.4.0) were used to first examine each dataset individually using Seurat (v.4.3) and SeuratObject (v.4.1.3) 66 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, R v4.0, SciPy, Seurat v4.3]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **4.0.3**
- Evidence: Both datasets were pre-processed using the pipeline suggested by Seurat (v.4.0.3) 72 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Evidence: 66 ) using Seurat v.4 (ref.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Evidence: The dataset was down sampled to 10,000 cells and marker genes were determined using the ‘FindAllMarkers’ command in Seurat 59 .
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: Sequence reads corresponding to ribosomal and global genes were removed, cells filtered according to library size and mitochondrial content, normalized, followed by uniform manifold approximation and projection (UMAP) dimension reduction, clustering (louvain) and cell-cycle analysis using Seurat 75 v.4.1.1.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Microbiota-induced T cell plasticity enables immune-mediated tumour control. (Nature 2026)

- DOI: 10.1038/s41586-025-09913-z | PMCID: PMC12960244 | PMID: 41535459
- Version used: **5.1.0**
- Evidence: Downstream data were processed and analysis were performed with the R packages Seurat v.5.1.0 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [AlphaFold, MACS2, Seurat v5.1.0]

### Mimicking opioid analgesia in cortical pain circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09908-w | PMCID: PMC12823415 | PMID: 41501467
- Version used: **4.3**
- Evidence: Clustering and comparison Count matrices for each individual sample were converted to Seurat objects using Seurat 4.3, and nuclei were filtered with thresholds of greater than 200 minimum features and less than 5% mitochondrial reads.
- Full pipeline: read trimming [STAR v2.7.1] -> alignment/mapping [STAR v2.7.1] -> dimensionality reduction/clustering [DESeq2, Seurat v4.3, SoupX, UMAP, scDblFinder] -> stage not stated [DeepLabCut]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: Raw sequencing data were processed and aligned to the mouse genome (GRCm39 — mm39) using the CellRanger pipeline (10X Genomics, v7.1.0). scRNA-seq analysis of circulating T cells Seurat datasets were generated for blood T cells at each time point.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Version used: **5.1.0**
- Evidence: Subsequent analyses were run in R Studio (R v.4.4.1) using Seurat (v.5.1.0).
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: After splitting both cell clusters into male and female, differentially expressed genes for each cell type–sex combination were identified using the FindAllMarkers() function in Seurat 86 , with only positive markers being considered.
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Human gut M cells resemble dendritic cells and present gluten antigen. (Nature 2026)

- DOI: 10.1038/s41586-025-09829-8 | PMCID: PMC12872457 | PMID: 41372409
- Version used: **3.1.4**
- Evidence: The scRNA-seq datasets were loaded into Seurat (v.3.1.4) objects in R Studio (v.3.6.3) for data integration, analysis and visualization 64 , according to the standard pipeline.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler v3.14.3] -> visualisation [Seurat v3.1.4] -> stage not stated [Enrichr, Python v3.11.9, R, Scanpy]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **4.0.5**
- Evidence: All subsequent downstream analyses were implemented using R (v.4.0.3) and the package Seurat (v.4.0.5) 61 .
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Sustained HIV-1 remission after heterozygous CCR5Δ32 stem cell transplantation. (Nature 2026)

- DOI: 10.1038/s41586-025-09893-0 | PMCID: PMC12916306 | PMID: 41326734
- Evidence: Fcs files from patient B2 and seven HIV-negative individuals (as the control group) were combined into a flowset and then converted into a Seurat object before being downsampled to approximately 20,000 cells per donor and transformed using the arcsinh transformation method.
- Full pipeline: alignment/mapping [MUSCLE v3.8.155] -> dimensionality reduction/clustering [R v4.4.1, UMAP] -> stage not stated [MACS2, Seurat]

### CD8&lt;sup&gt;+&lt;/sup&gt; T cell stemness precedes post-intervention control of HIV viraemia. (Nature 2026)

- DOI: 10.1038/s41586-025-09932-w | PMCID: PMC12872466 | PMID: 41326735
- Version used: **5.3.0**
- Evidence: After processing by Cell Ranger, the count matrix in sample_filtered_feature_bc_matrix was analysed using Seurat v.5.3.0 in R v.4.3.1.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R, Seurat v5.3.0]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **4.1.3**
- Evidence: For differential gene expression analysis Seurat (v.4.1.3) was used, with parameter test.use set to DESeq2 (v.1.28.0) in the ‘FindMarkers’ function.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Evidence: Subsequent analysis was performed using R software (v4.5.1) and Seurat package (v5.2.1).
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Version used: **4.4.0**
- Evidence: For all samples, the gene expression data from the CellRanger output was loaded using Seurat (v.4.4.0) 68 .
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Evidence: Afterwards, the raw counts were normalized and log-transformed, and highly variable genes were identified using ‘highly_variable_genes’ in Seurat 65 implemented in Scanpy with default settings.
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Version used: **5.1.0**
- Evidence: All samples were merged using R package Seurat (v.5.1.0) 58 .
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Independent mechanisms of inflammation and myeloid bias in VEXAS syndrome. (Nature 2026)

- DOI: 10.1038/s41586-025-09815-0 | PMCID: PMC12851934 | PMID: 41183570
- Evidence: Cell hashing data were quantified and demultiplexed using HTODemux in Seurat.
- Full pipeline: read trimming [Seurat] -> variant calling [Bioconductor] -> quantification [Seurat]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **5.2.1**
- Evidence: We conducted a focused analysis on the CD8 + T cells, performing integration with Harmony (v.1.2.3) 49 using the default parameters (using dataset and donor as covariates), and dimensionality reduction and visualization with Seurat (v.5.2.1) 50 .
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Single-cell quantification of a broad RNA spectrum reveals unique noncoding patterns associated with cell types and states. (PNAS 2021)

- DOI: 10.1073/pnas.2113568118 | PMCID: PMC8713755 | PMID: 34911763
- Evidence: Standard procedures for filtering, variable gene selection, dimensionality reduction, and clustering were performed using the Seurat package v3.1.4 ( 54 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [featureCounts v1.6.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [R, UMAP]

### Altered cell and RNA isoform diversity in aging Down syndrome brains. (PNAS 2021)

- DOI: 10.1073/pnas.2114326118 | PMCID: PMC8617492 | PMID: 34795060
- Version used: **3.0.3**
- Evidence: Using Seurat (v3.0.3), sample matrices were filtered and normalized by the default global-scaling method in Seurat.
- Full pipeline: normalisation [Seurat v3.0.3] -> dimensionality reduction/clustering [Monocle v0.2.1, UMAP] -> visualisation [UMAP]

### Trained innate immunity, long-lasting epigenetic modulation, and skewed myelopoiesis by heme. (PNAS 2021)

- DOI: 10.1073/pnas.2102698118 | PMCID: PMC8545490 | PMID: 34663697
- Evidence: We then used singular value decomposition implementation and created a Seurat ( 67 ) (version 3.1.5) object for nonlinear dimension reduction.
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [R] -> dimensionality reduction/clustering [ArchR v0.9.5, UMAP] -> differential/statistical testing [R] -> visualisation [ArchR v0.9.5] -> stage not stated [HOMER, MACS2, Seurat]

### Bcl6 controls meningeal Th17-B cell interaction in murine neuroinflammation. (PNAS 2021)

- DOI: 10.1073/pnas.2023174118 | PMCID: PMC8433502 | PMID: 34479995
- Version used: **3.1.1**
- Evidence: Downstream analysis was performed with R package Seurat version 3.1.1 ( 54 ) using R version 3.6.1 ( 55 ).
- Full pipeline: stage not stated [R v3.6.1, Seurat v3.1.1]

### Profound Treg perturbations correlate with COVID-19 severity. (PNAS 2021)

- DOI: 10.1073/pnas.2111315118 | PMCID: PMC8449354 | PMID: 34433692
- Evidence: Using the Seurat pipeline ( 52 ), PCs and UMAP coordinates were recomputed for just the CD4 + and CD8 + T cell populations.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Translational targeting of inflammation and fibrosis in frozen shoulder: Molecular dissection of the T cell/IL-17A axis. (PNAS 2021)

- DOI: 10.1073/pnas.2102715118 | PMCID: PMC8488623 | PMID: 34544860
- Evidence: Using the Seurat Package (Sajita Lab), we normalized and scaled the data.
- Full pipeline: quantification [ImageJ] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, UMAP] -> visualisation [ImageJ]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Version used: **3.1.5**
- Evidence: We used Seurat (version 3.1.5) ( 46 ) to further process the single-cell RNA-seq data.
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### Single-nuclear transcriptomics reveals diversity of proximal tubule cell states in a dynamic response to acute kidney injury. (PNAS 2021)

- DOI: 10.1073/pnas.2026684118 | PMCID: PMC8271768 | PMID: 34183416
- Version used: **3.2.2**
- Evidence: The R packages Seurat v.3.2.2 ( 18 ), ggplot2 v.3.3.2, Matrix v.2.3-18, and dplyr v.1.0.2 were used for preprocessing, data analysis, and visualization in R Studio (R version 3.6.3).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Monocle v0.2.3.0, SCENIC v1.1.2, STAR, UMAP] -> visualisation [Monocle v0.2.3.0, R v3.6.3, Seurat v3.2.2, ggplot2 v3.3.2, tidyverse v1.0.2]

### Developmental and sexual dimorphic atlas of the prenatal mouse external genitalia at the single-cell level. (PNAS 2021)

- DOI: 10.1073/pnas.2103856118 | PMCID: PMC8237666 | PMID: 34155146
- Evidence: Seurat V4.0 was used for all data analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v3.6, Seurat]

### cGAS restricts colon cancer development by protecting intestinal barrier integrity. (PNAS 2021)

- DOI: 10.1073/pnas.2105747118 | PMCID: PMC8201956 | PMID: 34074794
- Evidence: The epithelial cell dataset ( GSE92332 ) was loaded to Seurat v3 ( 26 , 50 ).
- Full pipeline: stage not stated [Seurat]

### Single-cell sequencing reveals suppressive transcriptional programs regulated by MIS/AMH in neonatal ovaries. (PNAS 2021)

- DOI: 10.1073/pnas.2100920118 | PMCID: PMC8157966 | PMID: 33980714
- Evidence: The analysis of the demultiplexed data were performed using the Seurat package in R ( 24 ).
- Full pipeline: read trimming [R, Seurat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [CellPhoneDB, CellProfiler]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Version used: **3.2.2**
- Evidence: We processed the counts using Seurat (version 3.2.2) ( 75 ).
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### Identification of EMT signaling cross-talk and gene regulatory networks by single-cell RNA sequencing. (PNAS 2021)

- DOI: 10.1073/pnas.2102050118 | PMCID: PMC8126782 | PMID: 33941680
- Version used: **3.1.0**
- Evidence: The downstream analysis, including the quality control steps, normalization, batch correction, and downstream analysis and visualization, were performed in R using Seurat v3.1.0 R package ( 57 ).
- Full pipeline: quality control [R, Seurat v3.1.0] -> normalisation [R, Seurat v3.1.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, Seurat v3.1.0, UMAP] -> stage not stated [GSVA, fgsea]

### A single-cell resolution developmental atlas of hematopoietic stem and progenitor cell expansion in zebrafish. (PNAS 2021)

- DOI: 10.1073/pnas.2015748118 | PMCID: PMC8040670 | PMID: 33785593
- Evidence: We used the Seurat package ( 17 ) for scRNA-seq data analysis, and the batch effect was removed by using the canonical-correlation analysis algorithm ( 18 ).
- Full pipeline: quality control [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, ImageJ]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: UMAP was calculated using Scanpy ( 50 ) using hyperparameters taken from Seurat’s default settings.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### A specific RIP3<sup>+</sup> subpopulation of microglia promotes retinopathy through a hypoxia-triggered necroptotic mechanism. (PNAS 2021)

- DOI: 10.1073/pnas.2023290118 | PMCID: PMC7980367 | PMID: 33836603
- Evidence: After unsupervised clustering by Seurat package, we selected clusters of microglia that expressed marker genes such as Aif1, Trem2, Csf1r, etc.
- Full pipeline: dimensionality reduction/clustering [Seurat]

### Integration and transfer learning of single-cell transcriptomes via cFIT. (PNAS 2021)

- DOI: 10.1073/pnas.2024383118 | PMCID: PMC7958425 | PMID: 33658382
- Evidence: It can be achieved by finding the mutual nearest neighbors (MNNs), as used in MNNcorrect ( 12 ) and Seurat v3 ( 10 ), where the target data are mapped to the query data, guided by the pairwise points identified by MNN.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### ELF3 activated by a superenhancer and an autoregulatory feedback loop is required for high-level HLA-C expression on extravillous trophoblasts. (PNAS 2021)

- DOI: 10.1073/pnas.2025512118 | PMCID: PMC7936349 | PMID: 33622787
- Evidence: The scRNA-seq data were also processed using Seurat ( 49 ).
- Full pipeline: stage not stated [Picard, Seurat]

### Single-cell atlas of developing murine adrenal gland reveals relation of Schwann cell precursor signature to neuroblastoma phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2022350118 | PMCID: PMC7865168 | PMID: 33500353
- Evidence: Subsequently, unique transcript counts were normalized using sctranform ( 50 ) and analyzed using the Seurat R package, version 3.1.5 ( 51 ).
- Full pipeline: normalisation [R, Seurat, limma] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [featureCounts v1.5.2]

### Pluripotent stem cell-derived epithelium misidentified as brain microvascular endothelium requires ETS factors to acquire vascular fate. (PNAS 2021)

- DOI: 10.1073/pnas.2016950118 | PMCID: PMC7923590 | PMID: 33542154
- Evidence: All single-cell analyses were performed using the Seurat package in R (version 3.2.2).
- Full pipeline: quality control [FastQC v0.11.5, R, edgeR] -> read trimming [R, STAR, edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Major alterations in the mononuclear phagocyte landscape associated with COVID-19 severity. (PNAS 2021)

- DOI: 10.1073/pnas.2018587118 | PMCID: PMC8017719 | PMID: 33479167
- Evidence: Seurat v3 was used to reanalyze single cell data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Targeting transcriptional regulation of SARS-CoV-2 entry factors <i>ACE2</i> and <i>TMPRSS2</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2021450118 | PMCID: PMC7817128 | PMID: 33310900
- Evidence: Data processing (including normalization and identification of highly variable genes) and integration were performed with Seurat v3 ( 46 ).
- Full pipeline: quantification [CellProfiler] -> normalisation [Seurat]

### Correlated gene modules uncovered by high-precision single-cell transcriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2206938119 | PMCID: PMC9907105 | PMID: 36508663
- Version used: **3.9.9.9024**
- Evidence: For both MALBAC-DT and 10× libraries from K562 cell lines, UMI counts are processed using Seurat 3.9.9.9024 ( 34 ).
- Full pipeline: read trimming [STAR v2.5.2] -> alignment/mapping [RepeatMasker, STAR v2.5.2] -> dimensionality reduction/clustering [R, SciPy] -> stage not stated [PyTorch, STRING db, Seurat v3.9.9.9024, WGCNA]

### Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT. (PNAS 2022)

- DOI: 10.1073/pnas.2214414119 | PMCID: PMC9894175 | PMID: 36459654
- Evidence: We compare scVAEIT with Seurat ( 8 ), totalVI ( 9 ), and MultiVI ( 10 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat, TensorFlow]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Version used: **3.1.5**
- Evidence: Synchronized HeLa cells combined with MDA-MB-468 and unsynchronized Hela cells from the other inlet of IFC were projected on UMAP by Seurat 3.1.5 ( 47 , 48 ) ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### CTLA-4 on thymic epithelial cells complements Aire for T cell central tolerance. (PNAS 2022)

- DOI: 10.1073/pnas.2215474119 | PMCID: PMC9860321 | PMID: 36409920
- Evidence: Population-level and single-cell RNA-seq and microarray analyses were performed on published datasets using edgeR for bulk RNA-seq, Seurat for scRNA-seq, and R for microarray analyses.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.1.0, Seurat, edgeR]

### Specification of neuronal subtypes in the spiral ganglion begins prior to birth in the mouse. (PNAS 2022)

- DOI: 10.1073/pnas.2203935119 | PMCID: PMC9860252 | PMID: 36409884
- Version used: **3.2**
- Evidence: Data was processed and analyzed using the following R-based packages: Seurat (v3.2) ( 47 ), DoubletFinder (v2.0.3) ( 48 ), Harmony (v1.0) ( 49 ), Slingshot (v1.8) ( 17 ), tradeSeq (v1.4)( 20 ), Monocle 3 ( 21 , 50 ), and SCENIC ( 23 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle, SCENIC, Seurat v3.2, Slingshot v1.8, scDblFinder v2.0.3]

### Integrated gene analyses of de novo variants from 46,612 trios with autism and developmental disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2203491119 | PMCID: PMC9674258 | PMID: 36350923
- Evidence: Unsupervised clustering with Seurat identified 120 distinct transcriptomic clusters, including 54 GABAergic (inhibitory) neuronal, 56 glutamatergic (excitatory) neuronal, and 10 nonneuronal cell types.
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [R v3.6.2] -> stage not stated [Cytoscape, GATK, STRING db, freebayes]

### Mapping prohormone processing by proteases in human enteroendocrine cells using genetically engineered organoid models. (PNAS 2022)

- DOI: 10.1073/pnas.2212057119 | PMCID: PMC9674236 | PMID: 36343264
- Evidence: Data were clustered and visualized using Seurat (dims = 10).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [DESeq2] -> visualisation [R, Seurat] -> stage not stated [ImageJ]

### Intestinal precursors avoid being misinduced to liver cells by activating Cdx-Wnt inhibition cascade. (PNAS 2022)

- DOI: 10.1073/pnas.2205110119 | PMCID: PMC9659337 | PMID: 36396123
- Version used: **3.2**
- Evidence: The output gene-expression matrices were further analyzed using the Seurat v3.2 package.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat v3.2]

### Loss of the repressor REST affects progesterone receptor function and promotes uterine leiomyoma pathogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2205524119 | PMCID: PMC9636955 | PMID: 36282915
- Evidence: Results from Seurat single-cell RNA-sequencing data analysis ( 27 ) on uteri from 5-mo-old Rest f/f PR Cre/+ cKO mice and littermate Rest f /f controls ( GSE178141 ), which passed the quality-control markers before being analyzed ( SI Appendix , Fig.
- Full pipeline: stage not stated [Seurat]

### Treatment with an antigen-specific dual microparticle system reverses advanced multiple sclerosis in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2205417119 | PMCID: PMC9618088 | PMID: 36256820
- Evidence: The analysis used CellRanger (10× genomics) in Mobaxterm, and Seurat (Satija Lab) in Rstudio conducted cluster analysis and differential expression ( SI Appendix , Extended Methods ).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [Seurat]

### Conservation at the uterine-placental interface. (PNAS 2022)

- DOI: 10.1073/pnas.2210633119 | PMCID: PMC9565169 | PMID: 36191208
- Version used: **4.1.0**
- Evidence: The R package Seurat (version 4.1.0) ( 44 ) was used for quality control and downstream analysis.
- Full pipeline: quality control [R, Seurat v4.1.0] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v3.16.1] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, MACS2]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: Cells were clustered using Seurat’s FindClusters function ( 59 ) and embedded using the addUMAP function.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Monocytes maintain central nervous system homeostasis following helminth-induced inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2201645119 | PMCID: PMC9478671 | PMID: 36070344
- Evidence: Processed digital gene-expression matrices were imported into R studio for analysis using the Seurat package.
- Full pipeline: stage not stated [GSEA v4.0.3, ImageJ v1.52a, Seurat]

### The amino acid sensor GCN2 controls red blood cell clearance and iron metabolism through regulation of liver macrophages. (PNAS 2022)

- DOI: 10.1073/pnas.2121251119 | PMCID: PMC9436309 | PMID: 35994670
- Version used: **3.0.1**
- Evidence: The file GSE145241_sce-SPTAmerged-Final.rds.gz was downloaded and analyzed using Seurat v3.0.1 in R ( 74 ).
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BWA v0.7.12] -> differential/statistical testing [MACS2] -> stage not stated [HOMER, R, Seurat v3.0.1]

### Dopamine and GPCR-mediated modulation of DN1 clock neurons gates the circadian timing of sleep. (PNAS 2022)

- DOI: 10.1073/pnas.2206066119 | PMCID: PMC9407311 | PMID: 35969763
- Evidence: In order to identify differentially expressed GPCRs in clock neurons, we first computed all marker genes in each cluster using the FindAllMarkers function of the Seurat package.
- Full pipeline: dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [Bioconductor, Seurat, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [Picard]

### The glioblastoma multiforme tumor site promotes the commitment of tumor-infiltrating lymphocytes to the T&lt;sub&gt;H&lt;/sub&gt;17 lineage in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2206208119 | PMCID: PMC9407554 | PMID: 35969754
- Evidence: The function RunUMAP from the Seurat package ( https://doi.org/10.1038/nbt.3192 ) was used to calculate the uniform manifold approximation and projection (UMAP) representation of the data based on the first 20 PCs.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2 v1.32.0, GSEA, GSVA, R v4.1.0, ggplot2 v3.3.5, tidyverse v1.0.7]

### Model-free prediction test with application to genomics data. (PNAS 2022)

- DOI: 10.1073/pnas.2205518119 | PMCID: PMC9407618 | PMID: 35969737
- Evidence: The marker genes for each cell type are obtained by implementing the FindMarkers function from Seurat ( 4 ).
- Full pipeline: differential/statistical testing [XGBoost] -> stage not stated [Seurat]

### DARPP32, a target of hyperactive mTORC1 in the retinal pigment epithelium. (PNAS 2022)

- DOI: 10.1073/pnas.2207489119 | PMCID: PMC9388070 | PMID: 35939707
- Evidence: Data analyses and cell clustering were performed in Seurat ( 11 ), and annotated with known cell markers ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Postmitotic accumulation of histone variant H3.3 in new cortical neurons establishes neuronal chromatin, transcriptome, and identity. (PNAS 2022)

- DOI: 10.1073/pnas.2116956119 | PMCID: PMC9371731 | PMID: 35930666
- Evidence: Clustering by Seurat ( 38 ) revealed 19 groups that encompassed the full complement of known cell types in the embryonic cortex ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP]

### Tumor-polarized GPX3&lt;sup&gt;+&lt;/sup&gt; AT2 lung epithelial cells promote premetastatic niche formation. (PNAS 2022)

- DOI: 10.1073/pnas.2201899119 | PMCID: PMC9371733 | PMID: 35914155
- Version used: **3.0.2**
- Evidence: The filtered output of gene-barcode matrix was then imported into the Seurat (v3.0.2) R toolkit ( 38 ).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Monocle, clusterProfiler v3.14.0] -> differential/statistical testing [GSEA, clusterProfiler v3.14.0] -> stage not stated [Seurat v3.0.2]

### Characterization of T cell receptors reactive to HCRT&lt;sub&gt;NH2&lt;/sub&gt;, pHA&lt;sub&gt;273-287&lt;/sub&gt;, and NP&lt;sub&gt;17-31&lt;/sub&gt; in control and narcolepsy patients. (PNAS 2022)

- DOI: 10.1073/pnas.2205797119 | PMCID: PMC9371724 | PMID: 35914171
- Evidence: Gene expression of filtered single cells (see quality control in Materials and Methods ) were scaled and clustered using Seurat SCTransform.
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP]

### Id3 expression identifies CD4&lt;sup&gt;+&lt;/sup&gt; memory Th1 cells. (PNAS 2022)

- DOI: 10.1073/pnas.2204254119 | PMCID: PMC9303986 | PMID: 35858332
- Version used: **3.5.1**
- Evidence: Approximately 10,000 sorted SMARTA cells were loaded and partitioned into Gel Bead In-Emulsions. scRNA libraries were sequenced on a HiSeq4000 (Illumina). scRNA-Seq Analysis. scRNA-seq analysis was performed using Cell Ranger software and Seurat version 3.5.1 in R Studio.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Seurat v3.5.1]

### Ablation of lysophosphatidic acid receptor 1 attenuates hypertrophic cardiomyopathy in a mouse model. (PNAS 2022)

- DOI: 10.1073/pnas.2204174119 | PMCID: PMC9282378 | PMID: 35787042
- Version used: **3.1**
- Evidence: Seurat 3.1 and R 4.0.1 ( 55 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ, UMAP] -> stage not stated [R v4.0, Seurat v3.1, scDblFinder]

### Memory-like NK cells armed with a neoepitope-specific CAR exhibit potent activity against NPM1 mutated acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2122379119 | PMCID: PMC9231490 | PMID: 35696582
- Version used: **3.0**
- Evidence: The analysis was performed using the Seurat 3.0 package ( 38 ).
- Full pipeline: stage not stated [Seurat v3.0]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Version used: **4.0.3**
- Evidence: Seurat (v4.0.3) ( 88 ) was used to calculate quality-control metrics.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### Single-cell transcriptomic classification of rabies-infected cortical neurons. (PNAS 2022)

- DOI: 10.1073/pnas.2203677119 | PMCID: PMC9295789 | PMID: 35609197
- Version used: **4.0**
- Evidence: R (version 4.1.1) and Seurat (version 4.0) ( 22 , 23 ) were used for snRNA-seq analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ImageJ, R v4.1.1, Seurat v4.0, scDblFinder]

### Antibody-mediated blockade of the IL23 receptor destabilizes intratumoral regulatory T cells and enhances immunotherapy. (PNAS 2022)

- DOI: 10.1073/pnas.2200757119 | PMCID: PMC9170135 | PMID: 35482921
- Evidence: Concatenated cytometry files were analyzed using the CATALYST ( 27 ) and Seurat ( 28 ) R packages.
- Full pipeline: stage not stated [R, Seurat, edgeR]

### Calcium channel blockers potentiate gemcitabine chemotherapy  in pancreatic cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2200143119 | PMCID: PMC9170157 | PMID: 35476525
- Evidence: Following sequencing, cell populations were visualized via Seurat’s uniform manifold approximation and projection (UMAP) dimensionality reduction.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat, UMAP]

### Extracellular vesicles from triple negative breast cancer promote pro-inflammatory macrophages associated with better clinical outcome. (PNAS 2022)

- DOI: 10.1073/pnas.2107394119 | PMCID: PMC9169908 | PMID: 35439048
- Evidence: The R package Seurat v3 was used to integrate samples and analyze the datasets.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [UMAP, pheatmap] -> stage not stated [Enrichr, MACS2, R, Seurat]

### Single cell enhancer activity distinguishes GABAergic and cholinergic lineages in embryonic mouse basal ganglia. (PNAS 2022)

- DOI: 10.1073/pnas.2108760119 | PMCID: PMC9169651 | PMID: 35377797
- Version used: **3.2.2**
- Evidence: We used the R package Seurat (v3.2.2) ( 16 , 53 ) for feature selection, clustering, and visualization.
- Full pipeline: dimensionality reduction/clustering [R, Seurat v3.2.2, UMAP] -> visualisation [R, Seurat v3.2.2, UMAP]

### Cellular and transcriptional diversity over the course of human lactation. (PNAS 2022)

- DOI: 10.1073/pnas.2121720119 | PMCID: PMC9169737 | PMID: 35377806
- Evidence: We performed module scoring with these in R (v3.6.2) with Seurat (V3), allowing us to stringently filter for immune cells that scored highly for lactocyte gene expression (>2.5 SDs above the mean lactocyte module score) ( 85 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [DESeq2, SciPy, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [Enrichr, R v3.6.2, Scanpy, Seurat, scDblFinder]

### Neutrophil and natural killer cell imbalances prevent muscle stem cell-mediated regeneration following murine volumetric muscle loss. (PNAS 2022)

- DOI: 10.1073/pnas.2111445119 | PMCID: PMC9169656 | PMID: 35377804
- Evidence: A 10× CellRanger was run to generate HDF5 matrix files, which were imported into R using Seurat version 3 ( 92 ).
- Full pipeline: dimensionality reduction/clustering [UMAP, scVelo] -> simulation/modelling [scVelo] -> visualisation [ggplot2] -> stage not stated [ImageJ, Seurat, velocyto]

### Hemogenic and aortic endothelium arise from a common hemogenic angioblast precursor and are specified by the Etv2 dosage. (PNAS 2022)

- DOI: 10.1073/pnas.2119051119 | PMCID: PMC9060440 | PMID: 35333649
- Evidence: Dataset from 21- and 28-hpf roof cECs and floor HECs were analyzed by Seurat package (v.4.0.2).
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, R v4.0.2, Seurat]

### A vasculature niche orchestrates stromal cell phenotype through PDGF signaling: Importance in human fibrotic disease. (PNAS 2022)

- DOI: 10.1073/pnas.2120336119 | PMCID: PMC9060460 | PMID: 35320046
- Evidence: Core steps in the downstream analysis were undertaken using the Seurat R package (Sajita Lab, New York Genome Centre).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [CellPhoneDB, R, Seurat]

### Convergent clonal selection of donor- and recipient-derived CMV-specific T cells in hematopoietic stem cell transplant patients. (PNAS 2022)

- DOI: 10.1073/pnas.2117031119 | PMCID: PMC8833188 | PMID: 35105810
- Version used: **2.3**
- Evidence: The final output of cellranger (molecule per cell matrix) was then analyzed in R using the package Seurat (version 2.3 and 3.0) as described below.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v2.3]

### LINEAGE: Label-free identification of endogenous informative single-cell mitochondrial RNA mutation for lineage analysis. (PNAS 2022)

- DOI: 10.1073/pnas.2119767119 | PMCID: PMC8812554 | PMID: 35086932
- Evidence: Codes of Seurat version 3 and version 4 ( 8 , 23 ), ENCORE ( 40 ), the method developed by Ludwig et al.
- Full pipeline: alignment/mapping [Python, SAMtools v1.9] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [GSEA, Seurat]

### Natural disaster and immunological aging in a nonhuman primate. (PNAS 2022)

- DOI: 10.1073/pnas.2121663119 | PMCID: PMC8872742 | PMID: 35131902
- Evidence: Count matrices were filtered to include only cells with at least 200 genes expressed and only genes expressed in at least 3 cells with Seurat v3 ( 91 ).
- Full pipeline: alignment/mapping [ANGSD, kallisto] -> quantification [limma] -> normalisation [limma] -> differential/statistical testing [R v4.0.2] -> stage not stated [HOMER, Seurat]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Evidence: Gene expression matrices for each sample were analyzed using the Seurat package ( 78 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### Cellular and molecular architecture of submucosal glands in wild-type and cystic fibrosis pigs. (PNAS 2022)

- DOI: 10.1073/pnas.2119759119 | PMCID: PMC8794846 | PMID: 35046051
- Evidence: Matrix data were subjected to ambient RNA correction using the SoupX R package ( 72 ), doublet filtering using the Scrublet Python package ( 73 ), and dead and low-quality cell filtering in Seurat ( 74 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat, SoupX, scDblFinder]

### B cell-derived IL-27 promotes control of persistent LCMV infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116741119 | PMCID: PMC8784116 | PMID: 35022243
- Version used: **4.0.3**
- Evidence: Seurat version 4.0.3 was used for cell filtering, sample demultiplexing, clustering, differential expression analysis, dimensionality reduction, and plotting ( 43 ).
- Full pipeline: read trimming [Seurat v4.0.3] -> dimensionality reduction/clustering [Seurat v4.0.3, UMAP] -> differential/statistical testing [Seurat v4.0.3] -> stage not stated [ComplexHeatmap, R v4.1.0, ggplot2]

### Pathogenic TNF-α drives peripheral nerve inflammation in an Aire-deficient model of autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2114406119 | PMCID: PMC8795502 | PMID: 35058362
- Evidence: Using a Seurat single-cell transcriptome analysis pipeline ( 19 ), 11 heterogeneous immune cell populations were identified ( Fig.
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellChat, Seurat]

### Neuronal identities derived by misexpression of the POU IV sensory determinant in a protovertebrate. (PNAS 2022)

- DOI: 10.1073/pnas.2118817119 | PMCID: PMC8794889 | PMID: 35042818
- Version used: **2.3.4**
- Evidence: All analyses were performed using Seurat version 2.3.4.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [Seurat v2.3.4]

### A distinct human cell type expressing MHCII and RORγt with dual characteristics of dendritic cells and type 3 innate lymphoid cells. (PNAS 2023)

- DOI: 10.1073/pnas.2318710120 | PMCID: PMC10756205 | PMID: 38109523
- Evidence: ( C ) Seurat-derived RNA-based UMAP of the resulting clusters.
- Full pipeline: dimensionality reduction/clustering [ArchR, Seurat, UMAP] -> stage not stated [scVelo]

### Genetic and immune determinants of &lt;i&gt;E. coli&lt;/i&gt; liver abscess formation. (PNAS 2023)

- DOI: 10.1073/pnas.2310053120 | PMCID: PMC10743367 | PMID: 38096412
- Version used: **4.3**
- Evidence: Reads were processed with 10× Genomics Cloud Analysis to generate hdf5 files and further analysis was performed with Seurat v4.3 ( 52 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.3, scDblFinder]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Evidence: The aggregated data were further analyzed using Seurat ( 46 ).
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Single-cell insights into epithelial morphogenesis in the neonatal mouse uterus. (PNAS 2023)

- DOI: 10.1073/pnas.2316410120 | PMCID: PMC10710066 | PMID: 38019863
- Version used: **4.0**
- Evidence: The count matrices were merged, and the dataset was then subjected to the standard quality control and clustering pipeline in Seurat v4.0 ( 81 ).
- Full pipeline: quality control [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, UMAP] -> differential/statistical testing [Monocle] -> simulation/modelling [Monocle]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: Seurat packages with the FindAllMarkers function were used to find the specific highly methylated regions during each stage.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### Controlling donor and newborn neuron migration and maturation in the eye through microenvironment engineering. (PNAS 2023)

- DOI: 10.1073/pnas.2302089120 | PMCID: PMC10655587 | PMID: 37931105
- Evidence: We used Python- and R-based dependencies to process the data by utilizing the packages for the main [Seurat ( 67 ) and scanpy ( 68 ), gene set enrichment analysis [escape ( 69 ), and pseudo-time/cell fates [scFates ( 70 ) analyses.
- Full pipeline: quantification [ImageJ] -> stage not stated [Scanpy, Seurat]

### Cereblon influences the timing of muscle differentiation in <i>Ciona</i> tadpoles. (PNAS 2023)

- DOI: 10.1073/pnas.2309989120 | PMCID: PMC10614628 | PMID: 37856545
- Version used: **4.3.0**
- Evidence: The data were integrated and further analyzed with Seurat version 4.3.0 ( 68 ).
- Full pipeline: differential/statistical testing [R] -> visualisation [ComplexHeatmap v2.10.0] -> stage not stated [Fiji, ImageJ, Seurat v4.3.0]

### Complete miRNA-15/16 loss in mice promotes hematopoietic progenitor expansion and a myeloid-biased hyperproliferative state. (PNAS 2023)

- DOI: 10.1073/pnas.2308658120 | PMCID: PMC10614620 | PMID: 37844234
- Version used: **4.0**
- Evidence: Downstream analysis and UMAP visualization were performed using Seurat 4.0.
- Full pipeline: dimensionality reduction/clustering [Monocle, Seurat v4.0, UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0, UMAP] -> stage not stated [GSEA, ImageJ, SCENIC]

### The developmental hierarchy and scarcity of replicative slender trypanosomes in blood challenges their role in infection maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2306848120 | PMCID: PMC10589647 | PMID: 37824530
- Version used: **4.1.0**
- Evidence: ( 21 ) Gene ID: Tb927.9.4080 Experimental models: Organisms/strains Mus musculus : strain balb/c, female Charles River RRID: IMSR_APB:4790 Software and algorithms GraphPad Prism www.graphpad.com RRID: SCR_002798 R https://www.r-project.org/ RRID: SCR_001905 RStudio https://rstudio.com/ RRID: SCR_000432 Cellranger version 7 10× Genomics N/A Seurat version 4.1.0 Hao et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Seurat v4.1.0, SoupX]

### Loss of PPARγ activity characterizes early protumorigenic stromal reprogramming and dictates the therapeutic window of opportunity. (PNAS 2023)

- DOI: 10.1073/pnas.2303774120 | PMCID: PMC10589683 | PMID: 37816052
- Evidence: Cell Ranger software (10x Genomics, version 1.31), deMULTIplex package (version 1.0.2), and Seurat R package (version 1.2) in R (version 3.6.1) were used for scRNA-seq analysis.
- Full pipeline: read trimming [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1] -> stage not stated [ImageJ]

### Targeting MFGE8 secreted by cancer-associated fibroblasts blocks angiogenesis and metastasis in esophageal squamous cell carcinoma. (PNAS 2023)

- DOI: 10.1073/pnas.2307914120 | PMCID: PMC10589644 | PMID: 37816055
- Evidence: After quality filtering and doublet removal, 531,143 cells underwent principal component analysis and UMAP algorithm in Seurat software, revealing distinct cell clusters.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Normal and Sjogren's syndrome models of the murine lacrimal gland studied at single-cell resolution. (PNAS 2023)

- DOI: 10.1073/pnas.2311983120 | PMCID: PMC10589653 | PMID: 37812717
- Evidence: Eleven principal cell clusters were identified with Seurat, and their identities were assigned by reference to published data on the lacrimal gland and other tissues, as seen in the Uniform Manifold Approximation and Projection (UMAP) plots in Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Endothelial deletion of EPH receptor A4 alters single-cell profile and Tie2/Akap12 signaling to preserve blood-brain barrier integrity. (PNAS 2023)

- DOI: 10.1073/pnas.2204700120 | PMCID: PMC10576133 | PMID: 37796990
- Evidence: Quality control and analysis were done using Seurat (V 4.1.0 Read10X function) ( 58 ).
- Full pipeline: quality control [FastQC, Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Trim Galore, scDblFinder]

### Divergent roles for STAT4 in shaping differentiation of cytotoxic ILC1 and NK cells during gut inflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2306761120 | PMCID: PMC10556635 | PMID: 37756335
- Evidence: ( F ) Top marker genes dividing NCR + innate lymphocytes into clusters were defined using the Seurat pipeline.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA]

### Cell type-specific cytonuclear coevolution in three allopolyploid plant species. (PNAS 2023)

- DOI: 10.1073/pnas.2310881120 | PMCID: PMC10556624 | PMID: 37748065
- Evidence: Seurat was used for sample clustering and cell identity annotation for the wheat seedling leaves ( Dataset S3 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, UMAP] -> structure determination [Monocle] -> visualisation [UMAP] -> stage not stated [OrthoFinder]

### mitoSplitter: A mitochondrial variants-based method for efficient demultiplexing of pooled single-cell RNA-seq. (PNAS 2023)

- DOI: 10.1073/pnas.2307722120 | PMCID: PMC10523499 | PMID: 37725654
- Evidence: Similar to the workflow for single-cell gene expression, Seurat was used to normalize data, as well as scaling, clustering, and dimension reduction based on highly variable mtRNA SNP features.
- Full pipeline: alignment/mapping [Cutadapt v1.18, STAR v2.7.3a, minimap2 v2.24] -> variant calling [Scanpy v1.9.1, minimap2 v2.24] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> stage not stated [scikit-learn v1.0.2]

### Spatial transcriptomics reveals light-induced chlorenchyma cells involved in promoting shoot regeneration in tomato callus. (PNAS 2023)

- DOI: 10.1073/pnas.2310163120 | PMCID: PMC10515167 | PMID: 37703282
- Version used: **4.1.0**
- Evidence: The R package, Seurat (v4.1.0), was employed for quality control, SCT normalization, dimensionality reduction, clustering, and identification of marker genes.
- Full pipeline: quality control [R, Seurat v4.1.0] -> alignment/mapping [STAR] -> normalisation [R, Seurat v4.1.0] -> dimensionality reduction/clustering [R, Seurat v4.1.0, UMAP, clusterProfiler] -> stage not stated [Monocle, velocyto]

### <i>Hey2</i> enhancer activity defines unipotent progenitors for left ventricular cardiomyocytes in juxta-cardiac field of early mouse embryo. (PNAS 2023)

- DOI: 10.1073/pnas.2307658120 | PMCID: PMC10500178 | PMID: 37669370
- Version used: **4.0.4**
- Evidence: The filtered feature-barcode matrix was analyzed using the R package Seurat version 4.0.4 ( 51 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, UMAP] -> stage not stated [R, Seurat v4.0.4]

### IL-6 trans-signaling in a humanized mouse model of scleroderma. (PNAS 2023)

- DOI: 10.1073/pnas.2306965120 | PMCID: PMC10500188 | PMID: 37669366
- Evidence: The raw matrices from Cell Ranger were processed and analyzed using the Seurat version 3 R toolkit for single-cell genomics ( 76 , 77 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### The mechano-chemical circuit drives skin organoid self-organization. (PNAS 2023)

- DOI: 10.1073/pnas.2221982120 | PMCID: PMC10483620 | PMID: 37643215
- Version used: **4.0.3**
- Evidence: The resulting gene-barcode matrix was imported into Seurat v.4.0.3 for quality control, dimensionality reduction, cell clustering, and differential expression analysis.
- Full pipeline: quality control [Seurat v4.0.3] -> dimensionality reduction/clustering [SCENIC, Seurat v4.0.3] -> differential/statistical testing [Seurat v4.0.3]

### Cell type-specific attenuation of brassinosteroid signaling precedes stomatal asymmetric cell division. (PNAS 2023)

- DOI: 10.1073/pnas.2303758120 | PMCID: PMC10483622 | PMID: 37639582
- Evidence: Normalization of the raw counts, detection of highly variable genes, discovery of clusters, and creation of UMAP plots were done by means of the Seurat pipeline (version 4.0.3).
- Full pipeline: quantification [ImageJ] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, Slingshot, UMAP] -> stage not stated [R]

### IL-15 synergizes with CD40 agonist antibodies to induce durable immunity against bladder cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2306782120 | PMCID: PMC10467355 | PMID: 37607227
- Evidence: Seurat was then used for all remaining steps.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### SoxC transcription factors shape the epigenetic landscape to establish competence for sensory differentiation in the mammalian organ of Corti. (PNAS 2023)

- DOI: 10.1073/pnas.2301301120 | PMCID: PMC10450657 | PMID: 37585469
- Evidence: ( A ) UMAP plots of 7,365 cells collected from WT cochlea duct epithelium and 5,693 cells collected from SoxC cKO cochlea duct epithelium at E13.5 generated by integration using Seurat CCA are shown.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [HOMER]

### XCR1 expression distinguishes human conventional dendritic cell type 1 with full effector functions from their immediate precursors. (PNAS 2023)

- DOI: 10.1073/pnas.2300343120 | PMCID: PMC10438835 | PMID: 37566635
- Evidence: Gene expression module analysis was performed using Seurat.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [GSEA, MACS2, Seurat]

### sccomp: Robust differential composition and variability analysis for single-cell data. (PNAS 2023)

- DOI: 10.1073/pnas.2203828120 | PMCID: PMC10438834 | PMID: 37549298
- Evidence: Alternatively, sccomp accepts single-cell data containers [Seurat ( 44 ), SingleCellExperiment ( 45 ), cell metadata, or group size].
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> machine learning [R] -> stage not stated [Seurat, Stan, limma, tidyverse]

### DNA methylation in the mouse cochlea promotes maturation of supporting cells and contributes to the failure of hair cell regeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2300839120 | PMCID: PMC10438394 | PMID: 37549271
- Evidence: Single-cell data were clustered using “uniform manifold approximation and projection” (UMAP) and “weighted-nearest neighbor” (WNN) using the Seurat R package, which integrates both the gene expression and the accessibility information to define a “joint” cellular state ( 55 ).
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP]

### Resolvin D1 prevents injurious neutrophil swarming in transplanted lungs. (PNAS 2023)

- DOI: 10.1073/pnas.2302938120 | PMCID: PMC10400944 | PMID: 37487095
- Version used: **4.0.0**
- Evidence: Analysis was performed using the R Seurat v4.0.0 package.
- Full pipeline: quality control [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Enrichr, ggpubr] -> stage not stated [Seurat v4.0.0]

### Functional interrogation of lymphocyte subsets in alopecia areata using single-cell RNA sequencing. (PNAS 2023)

- DOI: 10.1073/pnas.2305764120 | PMCID: PMC10629527 | PMID: 37428932
- Evidence: S1 B ), cells from each reaction were merged and aligned using the Seurat-based canonical correlation analysis (CCA) workflow to correct batch effects ( Materials and Methods ).
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA]

### A cellular and molecular spatial atlas of dystrophic muscle. (PNAS 2023)

- DOI: 10.1073/pnas.2221249120 | PMCID: PMC10629561 | PMID: 37410813
- Evidence: To separate cell clusters, we downloaded the raw UMI data from GEO and performed log normalization, principal component analysis (PCA), nearest-neighbor graph construction, and cluster determination from Seurat V3 package with default parameters setting.
- Full pipeline: quantification [Python] -> normalisation [Seurat] -> dimensionality reduction/clustering [Python, R, Seurat, Squidpy, UMAP] -> differential/statistical testing [R] -> visualisation [UMAP]

### Functional calcium-responsive parathyroid glands generated using single-step blastocyst complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2216564120 | PMCID: PMC10334775 | PMID: 37379351
- Version used: **4.2.1**
- Evidence: Subsequent analysis was performed using Seurat v.4.2.1 in R.
- Full pipeline: normalisation [DESeq2, R v4.1, ggplot2] -> dimensionality reduction/clustering [UMAP] -> visualisation [DESeq2, R v4.1, ggplot2] -> stage not stated [Seurat v4.2.1, tidyverse]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Version used: **4.1.1**
- Evidence: The matrices were imported into Seurat 4.1.1 ( 61 ) for further scRNA-seq bioinformatics analysis and data visualization.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### Leveraging single-cell RNA sequencing to unravel the impact of aging on stroke recovery mechanisms in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2300012120 | PMCID: PMC10288588 | PMID: 37307473
- Evidence: Cell cycle scoring based on Seurat suggested that 32.1% of OPCs were in the G2/M phase at d3 after stroke ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, R, Seurat]

### Regionally distinct progenitor cells in the lower airway give rise to neuroendocrine and multiciliated cells in the developing human lung. (PNAS 2023)

- DOI: 10.1073/pnas.2210113120 | PMCID: PMC10268599 | PMID: 37279279
- Evidence: For scRNA-seq analysis and visualization the standard Seurat workflow was performed including cell filtering by number of features (<500, >10,000 removed), percentage of mitochondrial reads (>10% removed), normalization, variable feature selection (n = 500), dimensional reduction (10 principle components), and Louvain clustering (resolution = 0.3).
- Full pipeline: alignment/mapping [UMAP] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### Tuft cells mediate commensal remodeling of the small intestinal antimicrobial landscape. (PNAS 2023)

- DOI: 10.1073/pnas.2216908120 | PMCID: PMC10266004 | PMID: 37253002
- Evidence: ( B ) Harmonized UMAP plots of ST spots organized by cluster identity ( Left ); corresponding hematoxylin and eosin (H&E)-stained tissue scans with overlaid Seurat clustering ( Right ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Glial dysregulation in the human brain in fragile X-associated tremor/ataxia syndrome. (PNAS 2023)

- DOI: 10.1073/pnas.2300052120 | PMCID: PMC10265985 | PMID: 37252957
- Evidence: To obtain a final high-quality nuclei set, filtering metrics were applied to nuclei in Seurat including: # UMIs> 500, # Genes > 250, log10GenesPerUMI (complexity measure) >0.8, and mitoRatio <0.1.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> stage not stated [Seurat]

### MicroRNA-205 promotes hair regeneration by modulating mechanical properties of hair follicle stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2220635120 | PMCID: PMC10235966 | PMID: 37216502
- Version used: **3.0**
- Evidence: The barcodes, features, and matrix files were loaded into Seurat 3.0 for downstream analysis ( https://satijalab.org/seurat/articles/install.html ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v3.0]

### COVID-19-related hyperglycemia is associated with infection of hepatocytes and stimulation of gluconeogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2217119120 | PMCID: PMC10214153 | PMID: 37186819
- Evidence: We analyzed 8,135 liver cells from five patients using Seurat-R package v4.0.0 (PMID: 34062119).
- Full pipeline: stage not stated [R, Seurat]

### A single-cell multiomic analysis of kidney organoid differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2219699120 | PMCID: PMC10193973 | PMID: 37155865
- Evidence: Singlet datasets of each time point from different PSC clones were merged and subjected to batch effect correction for RNA and ATAC assays using the RunHarmony function in Seurat R package (v.4.1.0).
- Full pipeline: quantification [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.20.0] -> stage not stated [MACS2, R, Signac, scDblFinder]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: For downstream analysis, to identify cell types and merge samples, we used the Seurat version 3 package ( 57 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### CDYL reinforces male gonadal sex determination through epigenetically repressing <i>Wnt4</i> transcription in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2221499120 | PMCID: PMC10193937 | PMID: 37155872
- Evidence: The data were log2-normalized and clustered using Seurat R package (version 4.1.0) ( 43 ).
- Full pipeline: alignment/mapping [STAR] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat] -> stage not stated [MACS2, featureCounts v1.6.4]

### A tessellated lymphoid network provides whole-body T cell surveillance in zebrafish. (PNAS 2023)

- DOI: 10.1073/pnas.2301137120 | PMCID: PMC10193988 | PMID: 37155881
- Version used: **4.1.1**
- Evidence: Filtered cell-by-gene count matrices generated were used for graph-based clustering with Seurat v4.1.1 ( 54 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> stage not stated [ImageJ v2.1.0, scDblFinder]

### Reprogramming by drug-like molecules leads to regeneration of cochlear hair cell-like cells in adult mice. (PNAS 2023)

- DOI: 10.1073/pnas.2215253120 | PMCID: PMC10151514 | PMID: 37068229
- Version used: **3.2**
- Evidence: S3 B ) by the Seurat v.3.2 ( 27 ), the scRNA-seq data were clustered by the principal component which identified nine distinct clusters.
- Full pipeline: dimensionality reduction/clustering [Seurat v3.2, UMAP] -> simulation/modelling [Monocle] -> stage not stated [GSEA]

### Single-nuclei RNA sequencing (snRNA-seq) uncovers trophoblast cell types and lineages in the mature bovine placenta. (PNAS 2023)

- DOI: 10.1073/pnas.2221526120 | PMCID: PMC10041116 | PMID: 36913592
- Evidence: Seurat was used to normalize expression profiles ( 32 ) and identified 13 distinct clusters in the cotyledonary and 11 in the intercotyledonary area, which were assigned to cell types based on the expression of previously reported marker genes ( Materials and Methods and Datasets S1 and S2 ).
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, Slingshot] -> stage not stated [STRING db]

### Nasal administration of anti-CD3 mAb (Foralumab) downregulates <i>NKG7</i> and increases <i>TGFB1</i> and <i>GIMAP7</i> expression in T cells in subjects with COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2220272120 | PMCID: PMC10243127 | PMID: 36881624
- Version used: **4.1.1**
- Evidence: Resultant demultiplexed TCR data were then merged with the single-cell objects created with Seurat (v.4.1.1) prior to analysis and visualization.
- Full pipeline: read trimming [Seurat v4.1.1] -> alignment/mapping [STAR] -> quantification [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [Seurat v4.1.1] -> stage not stated [ggplot2 v3.3.6]

### Innate immune cell activation causes lung fibrosis in a humanized model of long COVID. (PNAS 2023)

- DOI: 10.1073/pnas.2217199120 | PMCID: PMC10013740 | PMID: 36848564
- Evidence: The filtered expression datasets were integrated with Seurat v4 1 by following the reciprocal principal component analysis (PCA) workflow to remove batch effects across different donors.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### Type III interferon drives thymic B cell activation and regulatory T cell generation. (PNAS 2023)

- DOI: 10.1073/pnas.2220120120 | PMCID: PMC9992806 | PMID: 36802427
- Evidence: The Seurat R package (v3.2.2, R version 4.0.0) was used for analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R v4.0.0, Seurat, edgeR v3.24.3, ggplot2, pheatmap]

### <i>Cspg4<sup>high</sup></i> microglia contribute to microgliosis during neurodegeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2210643120 | PMCID: PMC9974490 | PMID: 36795751
- Evidence: Single-cell transcriptional information was analyzed using Seurat package ( https://satijalab.org/seurat/ ) ( 60 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Seurat]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: For gene expression data, raw gene expression matrices were input into Seurat ( 25 ) (v4.1) for further analysis.
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Losartan controls immune checkpoint blocker-induced edema and improves survival in glioblastoma mouse models. (PNAS 2023)

- DOI: 10.1073/pnas.2219199120 | PMCID: PMC9963691 | PMID: 36724255
- Version used: **4.0.0**
- Evidence: Following the methods of our recent study ( 20 ), cell-type states were identified using the R package Seurat (v4.0.0) ( 56 ).
- Full pipeline: quantification [RSEM v1.2.19] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [survival (R)] -> visualisation [UMAP] -> stage not stated [ImageJ, R, Seurat v4.0.0, seaborn v0.9.0]

### Generation and analysis of context-specific genome-scale metabolic models derived from single-cell RNA-Seq data. (PNAS 2023)

- DOI: 10.1073/pnas.2217868120 | PMCID: PMC9963017 | PMID: 36719923
- Evidence: Analysis with Seurat ( 25 ) yielded a good agreement between the cell subtype definition by Booeshaghi et al. and the Uniform Manifold Approximation and Projection (UMAP) projection ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2, R v4.1.1]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Evidence: We processed this dataset using Seurat V4 ( 122 ) and used the R package scMappR to assign differentially expressed genes or genes with differentially used exons to cell types ( Dataset S5 ; ( 63 ); SI Appendix ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### Mammalian life depends on two distinct pathways of DNA damage tolerance. (PNAS 2023)

- DOI: 10.1073/pnas.2216055120 | PMCID: PMC9942833 | PMID: 36669105
- Evidence: The downstream analysis was performed using Seurat in R.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Distinct and opposite effects of leukemogenic <i>Idh</i> and <i>Tet2</i> mutations in hematopoietic stem and progenitor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2208176120 | PMCID: PMC9942850 | PMID: 36652477
- Evidence: The raw sequencing reads were first processed and mapped to mouse genome build GRCm38 using the CellRanger software (v2.1.0, 10X Genomics), followed by analysis using Seurat ( 47 , 97 ), SCENIC ( 45 ), and Slingshot ( 46 ) as detailed in SI Appendix , Supplementary Methods .
- Full pipeline: alignment/mapping [SCENIC, Seurat, Slingshot] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, MACS2]

### Molecular imaging of chemokine-like receptor 1 (CMKLR1) in experimental acute lung injury. (PNAS 2023)

- DOI: 10.1073/pnas.2216458120 | PMCID: PMC9934297 | PMID: 36626557
- Version used: **4.1.0**
- Evidence: Differential gene expression was performed using the Seurat (v4.1.0) ( 68 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat v4.1.0]

### CITED2 is a conserved regulator of the uterine-placental interface. (PNAS 2023)

- DOI: 10.1073/pnas.2213622120 | PMCID: PMC9934066 | PMID: 36626551
- Evidence: The Seurat data pipeline (version 3.1.5) was used for additional data analysis, including identification of differentially expressed genes using FindMarkers ( 65 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat] -> stage not stated [Metascape]

### Neighbor-specific gene expression revealed from physically interacting cells during mouse embryonic development. (PNAS 2023)

- DOI: 10.1073/pnas.2205371120 | PMCID: PMC9926237 | PMID: 36595695
- Evidence: To remove any batch effect, we used the Seurat v3 standard integration workflow ( 61 ).
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, Enrichr, scDblFinder]

### Dry eye disease in mice activates adaptive corneal epithelial regeneration distinct from constitutive renewal in homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2204134120 | PMCID: PMC9926235 | PMID: 36595669
- Evidence: We performed scRNAseq using the 10× Genomics platform with analysis using the Seurat package ( 81 ).
- Full pipeline: dimensionality reduction/clustering [SCENIC, UMAP] -> stage not stated [Seurat]

### Identification of a unique subset of tissue-resident memory CD4<sup>+</sup> T cells in Crohn's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2204269120 | PMCID: PMC9910620 | PMID: 36574662
- Evidence: Cell lineage and pseudotime inference analysis using Slingshot ( 39 ) by Seurat divided CD4 + lymphocytes into four lineages ( SI Appendix , fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat, Slingshot]

### Permanent cilia loss during cerebellar granule cell neurogenesis involves withdrawal of cilia maintenance and centriole capping. (PNAS 2024)

- DOI: 10.1073/pnas.2408083121 | PMCID: PMC11670249 | PMID: 39705308
- Version used: **4.2.1**
- Evidence: Materials and Methods scRNA-Seq Clustering and Analysis. scRNA-seq gene expression matrices for mouse cerebellum P5 ( GSM3318005 ), P7 ( GSM3318006 ), and P14 ( GSM3318007 ) developmental time points ( 26 ) were imported into Seurat v4.2.1 and combined [see notebooks ( 100 )].
- Full pipeline: dimensionality reduction/clustering [Seurat v4.2.1, UMAP]

### Corticosteroids reduce pathological angiogenesis yet compromise reparative vascular remodeling in a model of retinopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2411640121 | PMCID: PMC11670060 | PMID: 39693344
- Evidence: Unique molecular identifier (UMI) counts for normoxic and OIR retina scRNA-Seq replicates were merged into one single Digital Gene Expression (DGE) matrix and processed using the Seurat package (Spatial reconstruction of single-cell gene expression data).
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [UMAP, edgeR] -> structure determination [Seurat] -> visualisation [UMAP, clusterProfiler] -> stage not stated [DESeq2, GSEA, GSVA, ImageJ]

### Complement C3d enables cell-mediated immunity capable of distinguishing spontaneously transformed from nontransformed cells. (PNAS 2024)

- DOI: 10.1073/pnas.2405824121 | PMCID: PMC11670236 | PMID: 39693340
- Evidence: The downstream analysis was done with Seurat in R using the filtered count matrices from Cell Ranger.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [Seurat, pheatmap]

### Accelerated cell-type-specific regulatory evolution of the human brain. (PNAS 2024)

- DOI: 10.1073/pnas.2411918121 | PMCID: PMC11670112 | PMID: 39680759
- Evidence: For the studies where CellBender was applicable, we converted the count matrices into the .h5 format using Seurat’s Write10×Counts() function.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [Seurat]

### Long-range &lt;i&gt;Atoh1&lt;/i&gt; enhancers maintain competency for hair cell regeneration in the inner ear. (PNAS 2024)

- DOI: 10.1073/pnas.2418098121 | PMCID: PMC11665905 | PMID: 39671177
- Evidence: Bioinformatic analysis used cellranger, Seurat ( 60 ), Signac ( 61 ), deepTools ( 62 ), DESeq2 ( 63 ), DiffBind ( 64 ), and Homer ( 55 ).
- Full pipeline: stage not stated [DESeq2, Seurat, Signac, deepTools]

### Leukemia inhibitory factor (LIF) receptor amplifies pathogenic activation of fibroblasts in lung fibrosis. (PNAS 2024)

- DOI: 10.1073/pnas.2401899121 | PMCID: PMC11648669 | PMID: 39636853
- Version used: **4.3.0**
- Evidence: Bulk RNA-seq dataset of human IPF lungs (N = 231) and control lungs (N = 267) was obtained from phs001662 [Lung Tissue Research Consortium ( 19 ) and plotted for the expression level of genes in the IL-6 family. sc RNA-seq dataset of human IPF lungs (N = 35) was obtained from GSE136831 ( 21 ) and analyzed via Seurat (v.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Seurat v4.3.0, UMAP] -> stage not stated [ImageJ]

### Glutamine is critical for the maintenance of type 1 conventional dendritic cells in normal tissue and the tumor microenvironment. (PNAS 2024)

- DOI: 10.1073/pnas.2412157121 | PMCID: PMC11648871 | PMID: 39625974
- Evidence: As previously described, For each sample, the processed output files from CellRanger (barcodes, fgenes, matrix) were passed to the Seurat package (v.4.3.0) for downstream processing in R (v.4.3.1).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, R v4.3.1, Seurat]

### Staggered immunization with mRNA vaccines encoding SARS-CoV-2 polymerase or spike antigens broadens the T cell epitope repertoire. (PNAS 2024)

- DOI: 10.1073/pnas.2406332121 | PMCID: PMC11626164 | PMID: 39589869
- Version used: **4.0.4**
- Evidence: The aligned datasets were processed with the Seurat (version 4.0.4) R package in R Studio (version 2021.09.1, R version 4.1.2).
- Full pipeline: alignment/mapping [R v4.1.2, Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Chronologically inappropriate morphogenesis (&lt;i&gt;Chinmo&lt;/i&gt;) is required for maintenance of larval stages of fall armyworm. (PNAS 2024)

- DOI: 10.1073/pnas.2411286121 | PMCID: PMC11626174 | PMID: 39589873
- Evidence: The single-cell multiomics data were analyzed using the open-source Seurat and Signac packages implemented in the R computing environment ( 58 ).
- Full pipeline: quantification [MACS2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, Seurat, Signac]

### Rescue of cochlear vascular pathology prevents sensory hair cell loss in Norrie disease. (PNAS 2024)

- DOI: 10.1073/pnas.2322124121 | PMCID: PMC11626139 | PMID: 39585982
- Evidence: Human fetal cochlea samples provided by the Human Developmental Biology Resource with ethics approval were analyzed by 10× single-cell RNA sequencing and the Seurat package.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### CD2 expressing innate lymphoid and T cells are critical effectors of immunopathogenesis in hidradenitis suppurativa. (PNAS 2024)

- DOI: 10.1073/pnas.2409274121 | PMCID: PMC11621750 | PMID: 39560648
- Version used: **4.0**
- Evidence: The scRNAseq dataset from 27,442 cells were clustered using Seurat 4.0 and annotated to 19 clusters of immune and nonimmune cell populations.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.0, UMAP]

### IFN-γ-induced Th1-Treg polarization in inflamed brains limits exacerbation of experimental autoimmune encephalomyelitis. (PNAS 2024)

- DOI: 10.1073/pnas.2401692121 | PMCID: PMC11621829 | PMID: 39560646
- Evidence: Subsequently, Seurat plugin ver.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Metascape] -> stage not stated [MACS2, Seurat]

### Augmenting antitumor efficacy of Th17-derived Th1 cells through IFN-γ-induced type I interferon response network via IRF7. (PNAS 2024)

- DOI: 10.1073/pnas.2412120121 | PMCID: PMC11588128 | PMID: 39541355
- Evidence: We segregated 18 distinct cell clusters, with 16 of these clusters delineated as various CD4 + T cell subsets, including pre-exhausted, proliferating, resident memory, Th1-like effector, Th17, and Treg cells, by uniform manifold approximation and projection (UMAP) clustering via Seurat ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA, GSVA]

### Modeling extrahepatic hepatitis E virus infection in induced human primary neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2411434121 | PMCID: PMC11588080 | PMID: 39546567
- Evidence: Data visualization was done in the statistical programming language R with in-house scripts using the libraries tidyverse, tidytSingleCellExperiment, Seurat ggplot2, GO-plot, ComplexHeatmap, and venn.
- Full pipeline: differential/statistical testing [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> visualisation [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> stage not stated [CellProfiler, ImageJ]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Version used: **4.3**
- Evidence: Seurat (version 4.3, R version 4.2.1) was applied to snRNA-seq data for downstream analysis.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### Monocytes give rise to Langerhans cells that preferentially migrate to lymph nodes at steady state. (PNAS 2024)

- DOI: 10.1073/pnas.2404927121 | PMCID: PMC11588065 | PMID: 39541348
- Version used: **5.0.1**
- Evidence: A total of 185 cells were sequenced and analyzed using Seurat (v.5.0.1 Satija Lab).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ v1.54, Seurat v5.0.1]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **4.3**
- Evidence: Then, analysis was performed using Seurat v4.3 ( 64 ) with R version 4.3.0.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### Spatiotemporal transcriptomic map of glial cell response in a mouse model of acute brain ischemia. (PNAS 2024)

- DOI: 10.1073/pnas.2404203121 | PMCID: PMC11573666 | PMID: 39499634
- Evidence: Using the Seurat ST pipeline, we first prepared a baseline characterization of the control section.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Metascape, Seurat]

### Effects of oxycodone on placental lineages: Evidence from the transcriptome profile of mouse trophoblast giant cells. (PNAS 2024)

- DOI: 10.1073/pnas.2412349121 | PMCID: PMC11551428 | PMID: 39475633
- Version used: **5.0.1**
- Evidence: The count matrix was generated and analyzed in the package Seurat (v5.0.1) ( 84 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, Python, Seurat v5.0.1]

### Deficiency of &lt;i&gt;DDX3X&lt;/i&gt; results in neurogenesis defects and abnormal behaviors via dysfunction of the Notch signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2404173121 | PMCID: PMC11551356 | PMID: 39471229
- Evidence: We further estimated the status of cell division and differentiation using Seurat and AUCell.
- Full pipeline: dimensionality reduction/clustering [GSEA] -> stage not stated [Seurat]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Version used: **4.3**
- Evidence: For either Cas13bt3-valid or -invalid cells, we further used Seurat v4.3 for data preprocessing, data normalization, feature selection, data scaling, dimensional reduction, and clustering.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### Regional specialization, polyploidy, and seminal fluid transcripts in the &lt;i&gt;Drosophila&lt;/i&gt; female reproductive tract. (PNAS 2024)

- DOI: 10.1073/pnas.2409850121 | PMCID: PMC11536144 | PMID: 39453739
- Version used: **5.0.3**
- Evidence: Using Seurat v5.0.3 ( 52 ), we removed genes detected in fewer than 3 nuclei, nuclei with >30,000 RNAs, nuclei with >275 genes, and nuclei with >2% mitochondrial gene expression.
- Full pipeline: quality control [SoupX v1.5.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ v2.3.0, R v4.1, Seurat v5.0.3]

### &lt;i&gt;Arabidopsis&lt;/i&gt; uses a molecular grounding mechanism and a biophysical circuit breaker to limit floral abscission signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2405806121 | PMCID: PMC11536089 | PMID: 39453742
- Evidence: We then constructed Seurat objects with the expression matrices.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HTSeq, STAR, kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Jupyter, R v3.6, Seurat]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Version used: **4.1.0**
- Evidence: For SI3 and SI4 data, cells labeled with hashtags for ileal cells were extracted using R 4.1.2, Seurat 4.1.0, Scanpy 1.9.1, and python 3.9.12 and then used for analysis.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### Single-cell resolution of intestinal regeneration in pythons without crypts illuminates conserved vertebrate regenerative mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2405463121 | PMCID: PMC11513969 | PMID: 39423244
- Version used: **4.2.0**
- Evidence: Counts and metadata were imported into Seurat 4.2.0 ( 80 ) for quality filtered, normalization and scaling, and clustering following standard protocol.
- Full pipeline: read trimming [STAR v2.7.10a, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.10a, Trimmomatic v0.36] -> quantification [STAR v2.7.10a, Trimmomatic v0.36] -> normalisation [Seurat v4.2.0] -> dimensionality reduction/clustering [Seurat v4.2.0, UMAP, pheatmap v1.0.12] -> differential/statistical testing [pheatmap v1.0.12] -> visualisation [UMAP, pheatmap v1.0.12] -> stage not stated [DESeq2 v1.36.0, SCENIC v1.3.1]

### Multiomics profiling of mouse polycystic kidney disease progression at a single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2410830121 | PMCID: PMC11513963 | PMID: 39405347
- Version used: **4.0.2**
- Evidence: The output of CellRanger ARC was processed through Seurat v4.0.2 ( 16 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.0.2]

### Injury-induced myosin-specific tissue-resident memory T cells drive immune checkpoint inhibitor myocarditis. (PNAS 2024)

- DOI: 10.1073/pnas.2323052121 | PMCID: PMC11494310 | PMID: 39378095
- Version used: **4.3.0**
- Evidence: Data were analyzed using the Seurat (v4.3.0) workflow in R (v4.3.0).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> stage not stated [R v4.3.0, Seurat v4.3.0]

### Modulation of diabetes-related retinal pathophysiology by PTX3. (PNAS 2024)

- DOI: 10.1073/pnas.2320034121 | PMCID: PMC11474045 | PMID: 39348530
- Evidence: Seurat objects of the filtered cells’ barcodes were downloaded from the original paper.
- Full pipeline: normalisation [ImageJ] -> stage not stated [DESeq2, Seurat]

### Paracrine FGF1 signaling directs pituitary architecture and size. (PNAS 2024)

- DOI: 10.1073/pnas.2410269121 | PMCID: PMC11459159 | PMID: 39320918
- Evidence: 4 D ), as identified by Seurat analyses ( Dataset S2 ), supporting the important role of Tpit in corticotrope identity.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, Seurat]

### A sensitive assay for measuring whole-blood responses to type I IFNs. (PNAS 2024)

- DOI: 10.1073/pnas.2402983121 | PMCID: PMC11459193 | PMID: 39312669
- Evidence: The expression matrices were integrated with the Seurat package (v4.3.0) in R.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, fgsea]

### Septo-dentate gyrus cholinergic circuits modulate function and morphogenesis of adult neural stem cells through granule cell intermediaries. (PNAS 2024)

- DOI: 10.1073/pnas.2405117121 | PMCID: PMC11459179 | PMID: 39312657
- Evidence: Following sequencing, individual libraries were integrated using Seurat V3, and unbiased cell clusters were assigned via Louvain–Jaccard clustering with multilevel refinement.
- Full pipeline: dimensionality reduction/clustering [Seurat, Slingshot, UMAP] -> differential/statistical testing [R v4.1] -> simulation/modelling [Slingshot] -> structure determination [Seurat] -> stage not stated [Fiji, ImageJ]

### Single-cell analysis identifies distinct macrophage phenotypes associated with prodisease and proresolving functions in the endometriotic niche. (PNAS 2024)

- DOI: 10.1073/pnas.2405474121 | PMCID: PMC11420174 | PMID: 39255000
- Version used: **4.4.0**
- Evidence: Clustering and analysis of differential gene expression (DGE) was performed using Seurat (v4.4.0 to v5.0.0) in R (v4.3.2).
- Full pipeline: dimensionality reduction/clustering [R v4.3.2, Seurat v4.4.0, UMAP] -> differential/statistical testing [R v4.3.2, Seurat v4.4.0]

### Joint trajectory inference for single-cell genomics using deep learning with a mixture prior. (PNAS 2024)

- DOI: 10.1073/pnas.2316256121 | PMCID: PMC11406253 | PMID: 39226366
- Evidence: To evaluate the performance of VITAE, we conducted a comparison between VITAE and an alternative approach, starting with integration using Seurat CCA ( 24 ), followed by trajectory inference using Slingshot on the integrated embeddings.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle, Seurat, Slingshot] -> visualisation [UMAP]

### Single-cell analysis via manifold fitting: A framework for RNA clustering and beyond. (PNAS 2024)

- DOI: 10.1073/pnas.2400002121 | PMCID: PMC11406302 | PMID: 39226348
- Evidence: Graph-based methods, such as Seurat ( 15 ), utilize principal component analysis followed by graph clustering to categorize cells.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### Qki5 safeguards spinal motor neuron function by defining the motor neuron-specific transcriptome via pre-mRNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2401531121 | PMCID: PMC11406248 | PMID: 39226364
- Evidence: ( C ) Seurat’s dot plot showing expression of QKI and 16 marker genes in the scRNA-seq.
- Full pipeline: alignment/mapping [Metascape] -> quantification [Metascape, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: The Seurat object was split by racial group and 20,000 cells from each racial group were included in the UMAP plot to ensure an equal number of cells and accurate representation of distribution of cell type.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### Unraveling clonal CD8 T cell expansion and identification of essential factors in γ-herpesvirus-induced lymphomagenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2404536121 | PMCID: PMC11317613 | PMID: 39088396
- Evidence: ( A ) Split UMAP visualization of combined single CD8 + T cell transcriptomes of WT or Mock-infected calves, with unsupervised Seurat clustering analysis.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [Seurat, UMAP] -> stage not stated [GSEA]

### Loss of primary cilia and dopaminergic neuroprotection in pathogenic LRRK2-driven and idiopathic Parkinson's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2402206121 | PMCID: PMC11317616 | PMID: 39088390
- Evidence: Seurat [version 3, https://satijalab.org/seurat/ ; ( 57 ) ] was used for single-cell analysis ( https://doi.org/10.5281/zenodo.10470951 ).
- Full pipeline: dimensionality reduction/clustering [scDblFinder] -> visualisation [CellProfiler] -> stage not stated [Seurat]

### Matrix stiffness-dependent regulation of immunomodulatory genes in human MSCs is associated with the lncRNA CYTOR. (PNAS 2024)

- DOI: 10.1073/pnas.2404146121 | PMCID: PMC11317610 | PMID: 39074278
- Evidence: Data were processed and integrated with Cell Ranger (10× Genomics) and Seurat v4 in R ( 67 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat]

### Transition of signal requirement in hematopoietic stem cell development from hemogenic endothelial cells. (PNAS 2024)

- DOI: 10.1073/pnas.2404193121 | PMCID: PMC11294991 | PMID: 39042698
- Evidence: The Seurat package (v4.3.0) was used for analyses, including quality control, data normalization, data scaling, and visualization ( 42 , 43 ).
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Jupyter, UMAP, scVelo] -> visualisation [Seurat]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Version used: **4.3.0**
- Evidence: Mapped filtered feature barcode matrices were analyzed in Seurat version 4.3.0 ( 43 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### Life stage-specific poly(A) site selection regulated by <i>Trypanosoma brucei</i> DRBD18. (PNAS 2024)

- DOI: 10.1073/pnas.2403188121 | PMCID: PMC11260167 | PMID: 38990950
- Evidence: Single-Cell Analysis Using the R Package Seurat.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, R, Seurat]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Version used: **4.2.0**
- Evidence: Most computational analyses of the resulting UMI filtered count matrix were performed using the R package Seurat (v4.2.0) ( 61 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### A wound-induced differentiation trajectory for neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2322864121 | PMCID: PMC11260127 | PMID: 38976727
- Evidence: We subclustered the neural population from a merged regeneration scRNAseq dataset ( 55 ), which included differentiated neurons and putative neural progenitors, using a standard method from Seurat v3 ( 122 ).
- Full pipeline: read trimming [RAxML v8.2.4] -> alignment/mapping [MUSCLE v3.8.31, RAxML v8.2.4] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [BUSCO v3.0.2, Pilon v1.23]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: We applied a batch correction procedure to integrate the scRNA-seq data for analysis using Seurat package (v4).
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Version used: **4.3.0**
- Evidence: Single-cell analysis was conducted with the Seurat (v4.3.0) ( 89 ) toolkit in R.
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Decoding transcriptomic signatures of cysteine string protein alpha-mediated synapse maintenance. (PNAS 2024)

- DOI: 10.1073/pnas.2320064121 | PMCID: PMC11181078 | PMID: 38833477
- Version used: **4.0.2**
- Evidence: Seurat (version 4.0.2) single-cell analysis R package was used for processing the snRNA-seq data, followed by the integration of all samples and dimensionality reduction using PCA.
- Full pipeline: dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP, clusterProfiler] -> visualisation [UMAP]

### Protective function and differentiation cues of brain-resident CD8+ T cells during surveillance of latent <i>Toxoplasma gondii</i> infection. (PNAS 2024)

- DOI: 10.1073/pnas.2403054121 | PMCID: PMC11181119 | PMID: 38838017
- Evidence: Following successive steps of quality control, the gene expression profiles of 6182 OVA-specific CD8+ T cells pooled from the three conditions (i.e., early encephalitis d52pi, early latency d52pi, late latency d160pi) were integrated with Seurat and included in subsequent analyses ( SI Appendix , Fig.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Evidence: For data integration, variable feature finding, data scaling, and principal component analysis (PCA) calculation based on highly variable genes, the standard pipeline of the Seurat package (version 4.2.0) was used ( 55 ).
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### Incomplete-penetrant hypertrophic cardiomyopathy &lt;i&gt;MYH7&lt;/i&gt; G256E mutation causes hypercontractility and elevated mitochondrial respiration. (PNAS 2024)

- DOI: 10.1073/pnas.2318413121 | PMCID: PMC11087781 | PMID: 38683993
- Evidence: ( D ) Alluvial plot demonstrating the composition of Seurat clusters.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Innate-like T cell subset commitment in the murine thymus is independent of TCR characteristics and occurs during proliferation. (PNAS 2024)

- DOI: 10.1073/pnas.2311348121 | PMCID: PMC10998581 | PMID: 38530897
- Evidence: All analyses were performed using R version 4.2.1 and the following packages: Seurat_4.1.3, clustree_0.4.4.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.2.1, Seurat]

### SRF transcriptionally regulates the oligodendrocyte cytoskeleton during CNS myelination. (PNAS 2024)

- DOI: 10.1073/pnas.2307250121 | PMCID: PMC10962977 | PMID: 38483990
- Evidence: ( A ) UMAP plot showing Seurat clusters and their annotation of 10-mo-old SRF-Flox and SRF-cKO NeuN − nuclei sequenced by 10× snRNA-seq.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### The neuroimmune CGRP-RAMP1 axis tunes cutaneous adaptive immunity to the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2322574121 | PMCID: PMC10945812 | PMID: 38451947
- Evidence: Assigned Seurat clusters are numbered and color-coded.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER, Metascape]

### Generation of human excitatory forebrain neurons by cooperative binding of proneural NGN2 and homeobox factor EMX1. (PNAS 2024)

- DOI: 10.1073/pnas.2308401121 | PMCID: PMC10945857 | PMID: 38446849
- Evidence: ( E ) T-distributed stochastic neighbor embedding (t-SNE) plot for the three different cell populations: ES cells (blue), NGN2 4d (green), and 28d (red) iN cells plotted using Seurat with the following settings (y cutoff = 0.75, x cutoff = 0.5, variable genes = 1,144).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> visualisation [Seurat]

### Cellular and molecular organization of the Drosophila foregut. (PNAS 2024)

- DOI: 10.1073/pnas.2318760121 | PMCID: PMC10945768 | PMID: 38442150
- Evidence: We analyzed three replicate datasets using Cell Ranger and Seurat ( 34 ).
- Full pipeline: dimensionality reduction/clustering [Metascape, UMAP] -> stage not stated [Seurat]

### Cationic cholesterol-dependent LNP delivery to lung stem cells, the liver, and heart. (PNAS 2024)

- DOI: 10.1073/pnas.2307801120 | PMCID: PMC10945827 | PMID: 38437539
- Evidence: The output files were loaded into Seurat.
- Full pipeline: stage not stated [ImageJ, Seurat, scDblFinder]

### Principled and interpretable alignability testing and integration of single-cell data. (PNAS 2024)

- DOI: 10.1073/pnas.2313719121 | PMCID: PMC10927515 | PMID: 38416677
- Evidence: Specifically, for each integrated dataset produced by fastMNN, LIGER, Scanorama, Seurat, or SMAI, we identify the DE genes for each cell type based on the Benjamini–Hochberg adjusted P -values, and compare their agreement with the DE genes identified from the individual datasets before integration using the Jaccard similarity index, which accounts for both power and false positive rate in signal d...
- Full pipeline: normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Seurat]

### Single-cell profiling of African swine fever virus disease in the pig spleen reveals viral and host dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2312150121 | PMCID: PMC10927503 | PMID: 38412127
- Evidence: The Seurat objects were merged and used for downstream analysis.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, ggplot2] -> stage not stated [GSVA v1.44.3, Seurat]

### OCA-B/Pou2af1 is sufficient to promote CD4&lt;sup&gt;+&lt;/sup&gt; T cell memory and prospectively identifies memory precursors. (PNAS 2024)

- DOI: 10.1073/pnas.2309153121 | PMCID: PMC10907311 | PMID: 38386711
- Version used: **4.0.4**
- Evidence: Clustering, filtering, variable gene selection, and dimensionality reduction were performed using Seurat ver.4.0.4 ( 46 ) according to the following workflow: 1, Cells with <200 detected genes were excluded from further analysis.
- Full pipeline: quality control [STAR v2.7.3a] -> alignment/mapping [STAR v2.7.3a] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v4.0.0, UMAP, pheatmap]

### Variable expression of <i>MECP2, CDKL5,</i> and <i>FMR1</i> in the human brain: Implications for gene restorative therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2312757121 | PMCID: PMC10907246 | PMID: 38386709
- Evidence: Fetal/embryonic and adult datasets were normalized and integrated independently in Seurat.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [igraph]

### The GATA transcriptional program dictates cell fate equilibrium to establish the maternal-fetal exchange interface and fetal development. (PNAS 2024)

- DOI: 10.1073/pnas.2310502121 | PMCID: PMC10895349 | PMID: 38346193
- Evidence: Dimensionality reduction and clustering of all single cells was done using Seurat package and projected using t-SNE plots showcasing visible proximity between clusters.
- Full pipeline: dimensionality reduction/clustering [Seurat] -> stage not stated [HOMER]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Version used: **4.3.0.1**
- Evidence: The gene expression matrix of mesophyll cells was extracted from the object created by Scanpy and underwent further analysis using the Seurat (v4.3.0.1) ( 118 ) and Monocle (v2.28.0) ( 73 ) pipelines.
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Extraislet expression of islet antigen boosts T cell exhaustion to partially prevent autoimmune diabetes. (PNAS 2024)

- DOI: 10.1073/pnas.2315419121 | PMCID: PMC10861925 | PMID: 38285952
- Version used: **4.0.0**
- Evidence: The expression matrices were then imported into R (v4.0.4) and processed with Seurat (v4.0.0).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.0.0]

### Expression of <i>Atoh1</i>, <i>Gfi1</i>, and <i>Pou4f3</i> in the mature cochlea reprograms nonsensory cells into hair cells. (PNAS 2024)

- DOI: 10.1073/pnas.2304680121 | PMCID: PMC10835112 | PMID: 38266052
- Evidence: Unbiased clustering using Seurat V4.1 revealed a clear separation between cells from control and experimental samples ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat] -> stage not stated [SCENIC, scVelo]

### Tracking the role of Aire in immune tolerance to the eye with a TCR transgenic mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2311487121 | PMCID: PMC10835137 | PMID: 38261611
- Evidence: The Seurat pipeline was used to cluster and identify the cell subsets with the dataset.
- Full pipeline: dimensionality reduction/clustering [Seurat]

### Single-cell RNA sequencing unveils unique transcriptomic signatures of endothelial cells and role of ENO1 in response to disturbed flow. (PNAS 2024)

- DOI: 10.1073/pnas.2318904121 | PMCID: PMC10835041 | PMID: 38261622
- Version used: **4.0.2**
- Evidence: ( A ) The results were plotted following data normalization, clustering, and dimensional reduction with Seurat v.4.0.2, and eight distinct clusters were identified by UMAP.
- Full pipeline: normalisation [Seurat v4.0.2] -> dimensionality reduction/clustering [GSEA, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0.2]

### Targeted checkpoint control of B cells undergoing positive selection in germinal centers by follicular regulatory T cells. (PNAS 2024)

- DOI: 10.1073/pnas.2304020121 | PMCID: PMC10835130 | PMID: 38261619
- Evidence: All subsequent analysis was done in Seurat ( 45 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### A predisposed motor bias shapes individuality in vocal learning. (PNAS 2024)

- DOI: 10.1073/pnas.2308837121 | PMCID: PMC10801888 | PMID: 38198530
- Evidence: The R package Seurat v.4 was used for data filtering and analyses ( 86 ).
- Full pipeline: dimensionality reduction/clustering [UMAP, WGCNA] -> visualisation [UMAP] -> stage not stated [Metascape, R, Seurat]

### Self-organized BMP signaling dynamics underlie the development and evolution of digit segmentation patterns in birds and mammals. (PNAS 2024)

- DOI: 10.1073/pnas.2304470121 | PMCID: PMC10786279 | PMID: 38175868
- Version used: **3.1.4**
- Evidence: R packages Seurat v3.1.4 ( 79 ), Destiny ( 33 ), Slingshot ( 34 ), and MAST ( 80 ) were used for analyses, and results were visualized in RStudio.
- Full pipeline: quantification [CellProfiler, R] -> visualisation [Seurat v3.1.4, Slingshot]

### A complete spatial map of mouse retinal ganglion cells reveals density and gene expression specializations. (PNAS 2025)

- DOI: 10.1073/pnas.2515449122 | PMCID: PMC12772174 | PMID: 41452983
- Evidence: Differential expression analysis was conducted using the Model-based Analysis of Single-cell Transcriptomics (MAST) framework ( 77 ) implemented in the Seurat package.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat]

### Predicting the unseen: A diffusion-based debiasing framework for transcriptional response prediction at single-cell resolution. (PNAS 2025)

- DOI: 10.1073/pnas.2525268122 | PMCID: PMC12772209 | PMID: 41452988
- Evidence: All other analysis is based on the standard log transformation, as used in Seurat: UMI counts are divided by total counts for the cell, multiplied by 10,000, and then subjected to a log ( x + 1 ) transformation.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Neural crest cell recruitment and reprogramming as central drivers of embryonic limb regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2519994122 | PMCID: PMC12772167 | PMID: 41433066
- Evidence: Meta-analysis of public single-cell data for distal mesenchyme and AER markers ( 13 ) was performed to extract specific markers for AER and Distal mesenchyme populations using Seurat package FindMarkers function in Rstudio which average expression from triplicates was then used for heatmap representation.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [Seurat]

### Maladaptive immunity to the microbiota promotes neuronal hyperinnervation and itch via IL-17A. (PNAS 2025)

- DOI: 10.1073/pnas.2525146122 | PMCID: PMC12772199 | PMID: 41428888
- Version used: **4.4.0**
- Evidence: Downstream expression analysis was performed in R 4.4.2 using Seurat 4.4.0, loading unaggregated filtered_feature_bc_matrix files with CreateSeuratObject(min.cells=3).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.44.0] -> visualisation [UMAP] -> stage not stated [Metascape, R v4.4, Seurat v4.4.0]

### Distinguishing subtypes of endothelial cells in the mouse aorta. (PNAS 2025)

- DOI: 10.1073/pnas.2525755122 | PMCID: PMC12704785 | PMID: 41343672
- Evidence: For each dataset, the raw gene counts data were processed in R Seurat packages (version: 4.3.0) for quality control, normalization, scaling, clustering, and further downstream visualizations.
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat] -> stage not stated [R, SAMtools, featureCounts]

### <i>Lrig1</i>-expressing quiescent stem cells maintain vocal fold mucosal homeostasis via <i>Notch</i> signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2513590122 | PMCID: PMC12685045 | PMID: 41289377
- Evidence: Uniform Manifold Approximation and Projection (UMAP) using Seurat package (v5.1.0) shows Lrig1 + and Lrig1 − cells were distributed across the same cell populations ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Dynamics and variegation in the Treg response to Interleukin-2. (PNAS 2025)

- DOI: 10.1073/pnas.2518991122 | PMCID: PMC12663944 | PMID: 41264258
- Evidence: Data were processed using CellRanger (10× Genomics) and analyzed with Seurat (10903). scATACseq on the 10× Genomics Chromium instrument ( 17 ). used hashtagged cells with a modification of ASAP-seq ( 40 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat, Signac v1.14.0]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Evidence: Published scRNA-seq data of the X. laevis tadpole tails and regeneration buds at stage 41 [DDBJ Sequence Read Archive (DRA) accession number: DRA009253] ( 20 ) and scRNA-seq data from the SP fraction of the regeneration buds at stage 41 [DRA accession number: DRA013526] ( 18 ) were analyzed using the Seurat package v5.1.0 ( 21 ).
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: Raw 10× data were processed using Cellranger (v.3 for the larger screens, v.5 for the smaller screens) to produce h5 files, which were converted to Seurat objects.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### High-resolution single-cell analyses reveal evolutionary constraints and evolvability of sexual circuits in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2516083122 | PMCID: PMC12663948 | PMID: 41248285
- Evidence: Reads were mapped to the corresponding reference genomes using Cell Ranger, restricted to orthologous genes shared across all four species, for subsequent clustering and gene expression analyses primarily conducted with Seurat.
- Full pipeline: alignment/mapping [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP]

### An adipo-osteoprogenitor population in the endosteal niche contributes to bone and fat formation in adult mouse bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2502436122 | PMCID: PMC12663985 | PMID: 41248279
- Version used: **4.1.1**
- Evidence: For downstream analyses, filtered feature matrix files were analyzed with Seurat 4.1.1 for quality control, normalization, variable gene expression, dimension reduction, and clustering with UMAP.
- Full pipeline: quality control [Seurat v4.1.1, UMAP] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.1.1, UMAP]

### MC1R determines healing outcomes in acute and chronic cutaneous wounds. (PNAS 2025)

- DOI: 10.1073/pnas.2503308122 | PMCID: PMC12646273 | PMID: 41218117
- Version used: **4.4**
- Evidence: Public scRNA-seq data (Theocharidis et al., GSE165816 ) were reanalyzed in R (v4.2.2) with Seurat (v4.4).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, ImageJ, R v4.2.2, Seurat v4.4]

### Erythroid precursors regulate local oxygen tension and repair outcomes in the bone marrow niche. (PNAS 2025)

- DOI: 10.1073/pnas.2522548122 | PMCID: PMC12646327 | PMID: 41218120
- Version used: **4.0**
- Evidence: Subsequent analysis employed Seurat v4.0 ( 61 ).
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA v4.3.3, Seurat v4.0]

### Forward genetic screening in engineered colorectal cancer organoids identifies regulators of metastasis. (PNAS 2025)

- DOI: 10.1073/pnas.2510910122 | PMCID: PMC12646219 | PMID: 41218116
- Evidence: ( K and L ) Relative Geneset Expression Score of M1-like genes ( K ) and M2-like genes ( L ) calculated using Seurat.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Seurat]

### Early female germline development in &lt;i&gt;Xenopus laevis&lt;/i&gt;: Stem cells, nurse cells, and germline cysts. (PNAS 2025)

- DOI: 10.1073/pnas.2522343122 | PMCID: PMC12646306 | PMID: 41213017
- Evidence: Transcriptomes were generated from 18,410 cells, including 8,544 germline and 9,866 somatic cells, and processed using Seurat.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> stage not stated [Seurat]

### Glycolipid nanoparticles target the spleen and detarget the liver without charge. (PNAS 2025)

- DOI: 10.1073/pnas.2409569122 | PMCID: PMC12625924 | PMID: 41183194
- Version used: **4.0.4**
- Evidence: All output files were loaded into Seurat (v 4.0.4), and in summary, cells were log normalized to a scale factor of 10,000, then scaled using a linear transformation ( 50 ).
- Full pipeline: normalisation [Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> stage not stated [scDblFinder]

### Metabolic adaptation of glucose-deprived macrophages involves partial gluconeogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2419568122 | PMCID: PMC12595420 | PMID: 41160607
- Version used: **5.1.0**
- Evidence: We used the original annotations to calculate pseudobulk gene expression per cell type using the “AverageExpression” function from Seurat v5.1.0 ( 54 ), for normal samples (including both healthy normal and tumor-adjacent normal), and tumor samples (including both primary tumors and metastases).
- Full pipeline: normalisation [ggplot2] -> dimensionality reduction/clustering [ggplot2] -> visualisation [ComplexHeatmap, R] -> stage not stated [Seurat v5.1.0]

### Serum response factor is essential for endometrial function and prevention of inflammatory fibrosis. (PNAS 2025)

- DOI: 10.1073/pnas.2510060122 | PMCID: PMC12595411 | PMID: 41150713
- Evidence: The tables show selected genes from among the overlaps that are either upregulated in both endometriosis patient cells and Srf d/d mouse cells compared to controls (red) or downregulated in both (blue). **** P adj < 0.0001; ns, P adj > 0.05, calculated via Seurat’s FindMarkers function, which uses the nonparametric Wilcoxon rank-sum test.
- Full pipeline: variant calling [CellChat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Characterization of endothelin-converting enzyme 1 as a key enzyme in the multienzyme Aβ degradation pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2507450122 | PMCID: PMC12595483 | PMID: 41144673
- Evidence: ...16/j.cell.2023.08.039 ) available from the AD and aging brain atlas data repository ( http://compbio.mit.edu/ad_aging_brain/ ) was analyzed using the Seurat package (V5, 10.1038/s41587-023-01767-y ), focusing on neurovascular cells types (Ast, Per, SMC, Fib, and End) whose annotations were directly imported from the brain atlas data repository.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Single-cell metabolome and RNA-seq multiplexing on single plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512828122 | PMCID: PMC12582292 | PMID: 41134629
- Version used: **5.0.1**
- Evidence: The output expected counts were combined into one matrix and subjected to Seurat (v5.0.1) for downstream analyses ( 44 ).
- Full pipeline: read trimming [RSEM v1.3.1, STAR v2.7.10a, fastp] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.10a, fastp] -> quantification [RSEM v1.3.1, STAR v2.7.10a, fastp] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [Cytoscape] -> stage not stated [ImageJ, Seurat v5.0.1]

### Spatial gene expression analysis reveals pathological niches in Japanese encephalitis virus neuroinvasion. (PNAS 2025)

- DOI: 10.1073/pnas.2515006122 | PMCID: PMC12582308 | PMID: 41129224
- Version used: **5.0.3**
- Evidence: Data ( 38 ) were analyzed using the R package Seurat (v5.0.3) following standard workflows with default settings ( 39 ).
- Full pipeline: visualisation [ggplot2 v3.5.1] -> stage not stated [R, Seurat v5.0.3]

### Joint disruption of &lt;i&gt;Ret&lt;/i&gt; and &lt;i&gt;Ednrb&lt;/i&gt; transcription shifts cell fate trajectories in the enteric nervous system in Hirschsprung disease. (PNAS 2025)

- DOI: 10.1073/pnas.2507062122 | PMCID: PMC12582274 | PMID: 41118220
- Evidence: Data were primarily processed in Seurat, ( 44 ) filtering for cells with at least 500 Unique Molecular Identifiers (UMIOs), at least 250 Genes, a log 10 GenesPerUMI ratio greater than 80 percent, and a mitochondrial read ratio of less than 20 percent.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [clusterProfiler] -> stage not stated [Seurat]

### HIF2α negatively regulates MYCN protein levels and promotes a low-risk noradrenergic phenotype in neuroblastoma. (PNAS 2025)

- DOI: 10.1073/pnas.2516922122 | PMCID: PMC12582314 | PMID: 41118218
- Evidence: Gene module scores were computed using the AddModuleScore function from the Seurat R package, version V5.0.0 ( 55 ).
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2, FastQC, GSEA] -> visualisation [UMAP] -> stage not stated [R, Scanpy, Seurat]

### Invariant HVC size in female canaries singing under testosterone: Unlocking function through neural differentiation, not growth. (PNAS 2025)

- DOI: 10.1073/pnas.2426847122 | PMCID: PMC12582222 | PMID: 41115194
- Version used: **5.0.1**
- Evidence: The posterior analysis used the Seurat (5.0.1) ( 54 ) and SCTransform (0.4.1) ( 55 ) R packages.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, ggplot2] -> stage not stated [ImageJ, R, Seurat v5.0.1]

### TMEM16F phospholipid scramblase regulates tumorigenesis by modulating the tumor immune microenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2513910122 | PMCID: PMC12557541 | PMID: 41100671
- Version used: **4.3.0**
- Evidence: The matrix data were loaded into R (4.3.2) and RStudio (2024.04.2) using the Seurat (v.4.3.0) package ( 43 ) for further data analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> visualisation [UMAP] -> stage not stated [ImageJ, Seurat v4.3.0]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: ( 10 ), were analyzed using the Seurat pipeline (v5.1.0).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Unexpected heterogeneity and tissue-specific properties of the thymic hematopoietic antigen-presenting cell network. (PNAS 2025)

- DOI: 10.1073/pnas.2508184122 | PMCID: PMC12541397 | PMID: 41071655
- Evidence: Integration of scRNA-seq datasets was carried out using the Seurat RPCA method.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Ectopic transcription due to inherited histone methylation may interfere with the ongoing function of differentiated neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2513137122 | PMCID: PMC12501177 | PMID: 40991443
- Evidence: Seurat analysis was used for unsupervised hierarchical cluster formation.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [Fiji, ImageJ]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: Scores were calculated using Seurat’s ModuleScore function with the 14-gene T cell exhaustion signature presented in the study by Chu et al., and the senescence score was calculated using the six-gene signature derived from a study by Lu et al.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Triple checkpoint blockade of PD-1, Tim-3, and Lag-3 enhances adoptive T cell immunotherapy in a mouse model of ovarian cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2419888122 | PMCID: PMC12501118 | PMID: 40982684
- Version used: **4.1.1.9001**
- Evidence: Matrix files output from Cell Ranger were subsequently analyzed in R version 4.3.1 using Seurat version 4.1.1.9001 ( 59 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.3.1, Seurat v4.1.1.9001]

### Lymphatic dysfunction is linked to disease pathogenesis in Duchenne muscular dystrophy animal models. (PNAS 2025)

- DOI: 10.1073/pnas.2505656122 | PMCID: PMC12478126 | PMID: 40966282
- Evidence: UMAP of LMCs and PASMCs after integration with the Seurat v5 pipeline ( H ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Version used: **1.9.0**
- Evidence: To construct a peak count matrix, we supplied a fragment file and the peak sets described above to Seurat (v1.9.0) ( 44 ) and Signac (version 4.3.0) ( 45 ).
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Humanization of CD47 enables development of functional human neutrophils via postirradiation remodeling of the bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2426546122 | PMCID: PMC12478129 | PMID: 40956886
- Version used: **5.0.1**
- Evidence: The filtered feature-barcode matrix from Cell Ranger was analyzed in R (v4.2.3) using Seurat (v5.0.1).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [R v4.2.3, Seurat v5.0.1]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: The gene-cell matrices were loaded into the Seurat Package-5.1.0 ( 57 ) with min.cells = 3 and min.features = 200.
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Sorting nexin 3 promotes ischemic retinopathy through RIP1- and RIP3-mediated myeloid cell necroptosis and mitochondrial fission. (PNAS 2025)

- DOI: 10.1073/pnas.2426578122 | PMCID: PMC12452880 | PMID: 40924459
- Evidence: We first screened CD45 + myeloid cells (n = 1,545 cells) from the total cell population before performing unsupervised clustering with the “Seurat” package for downstream analysis.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [Seurat] -> stage not stated [MACS2]

### Tumor-expressed GPNMB orchestrates Siglec-9&lt;sup&gt;+&lt;/sup&gt; TAM polarization and EMT to promote metastasis in triple-negative breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2503081122 | PMCID: PMC12435292 | PMID: 40892920
- Evidence: ( F – I ) UMAP projections of module scores for selected immune programs, calculated using Seurat’s AddModuleScore function and overlaid onto the tumor immune landscape: ( F ) Suppressive_TAM (Hmox1, Fcgr3, Arg1, Il10); ( G ) CD4_Treg (Il2ra, Ctla4, Ikzf2, Tnfrsf18); ( H ) CD8_Exhaustion (Eomes, Gzma, Tox); ( I ) CD8_Effector (Cd8a, Gzmb, Nkg7).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [AlphaFold] -> machine learning [UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AutoDock Vina, GSEA, R v4.3.0]

### Dynamic GLUT trafficking at high glucose levels enhances insulin secretion: Dysregulation leads to decreased insulin secretion during type 2 diabetes. (PNAS 2025)

- DOI: 10.1073/pnas.2425955122 | PMCID: PMC12377745 | PMID: 40811462
- Evidence: Using the Seurat R package, we analyzed the expression of SCL2A1, SCL2A2, PDX1, CLTA, CLTB, CLTC, and PRKKA1 specific to β cells from scRNA-seq data of the pancreatic islets of T2D and ND donors.
- Full pipeline: normalisation [ImageJ] -> stage not stated [R, Seurat]

### Circulating cell-free RNA signatures for the characterization and diagnosis of myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2025)

- DOI: 10.1073/pnas.2507345122 | PMCID: PMC12377778 | PMID: 40789036
- Version used: **4.1.0**
- Evidence: The cell types were grouped into 29 clusters using Seurat (v4.1.0).
- Full pipeline: quantification [Bracken] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> machine learning [DESeq2 v1.34.0] -> visualisation [ggplot2 v3.3.5] -> stage not stated [Kraken2, Snakemake]

### A recurrent de novo damaging variant in &lt;i&gt;EMP2&lt;/i&gt; causes progressive symmetric erythrokeratoderma. (PNAS 2025)

- DOI: 10.1073/pnas.2509896122 | PMCID: PMC12358830 | PMID: 40758889
- Evidence: We merged and integrated data using Seurat v5 and performed principal component analysis, neighbor identification, and cluster identification using default parameters ( 63 , 64 ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [QuPath] -> dimensionality reduction/clustering [Monocle, Seurat, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ANNOVAR]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Version used: **5.1**
- Evidence: We performed normalization and cell type identification using Seurat 5.1 ( 60 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Version used: **4.1.0**
- Evidence: Sequences were transformed into raw count matrices based on an mm10 reference using CellRanger (10X Genomics) and loaded into an R environment ( 51 ) with Seurat 4.1.0 ( 52 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### <i>Prg4</i>+ fibroadipogenic progenitors in muscle are crucial for bone fracture repair. (PNAS 2025)

- DOI: 10.1073/pnas.2417806122 | PMCID: PMC12337308 | PMID: 40729389
- Evidence: Standard Seurat pipeline ( 44 ) was used for filtering, normalization, variable gene selection, dimensionality reduction analysis, and clustering.
- Full pipeline: quantification [ImageJ] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP]

### A granulin-positive macrophage subtype in mycobacterial granulomas alleviates tissue damage by limiting excessive inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2413946122 | PMCID: PMC12337285 | PMID: 40729382
- Evidence: Briefly, gene expression data were normalized using the Seurat package (v4.0.3, https://satijalab.org/seurat/ ), including “NormalizeData,” “IntegrateData,” “FindVariableFeatures,” “RunPCA,” “RunUMAP,” “FindNeighbors,” and “FindClusters” functions.
- Full pipeline: quality control [HISAT2] -> alignment/mapping [HISAT2] -> quantification [HTSeq] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler] -> stage not stated [DESeq2, STRING db]

### SARS-CoV-2 uptake and inflammatory response in senescent endothelial cells are regulated by the BSG/VEGFR2 pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2502724122 | PMCID: PMC12337311 | PMID: 40720650
- Version used: **5.3.0**
- Evidence: To evaluate BSG expression levels in lung ECs from human COVID-19 patients, single-nucleus RNAseq data from previous publications ( 54 ) were obtained from GEO ( GSE159585 ) and analyzed on the Seurat (ver 5.3.0) ( 84 ).
- Full pipeline: stage not stated [Seurat v5.3.0]

### Epigenetic instability and hypofunctionality of fetal Tregs allow a permissive regulatory environment for T effector memory maturation. (PNAS 2025)

- DOI: 10.1073/pnas.2506673122 | PMCID: PMC12318238 | PMID: 40705427
- Evidence: UMAP dimensional reduction of CD3 + T cells (n = 35,589 cells) depicting ( A ) sample type (fetal liver or thymus), ( B ) clusters from Seurat analysis.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Cell type-specific purifying selection of synonymous mitochondrial DNA variation. (PNAS 2025)

- DOI: 10.1073/pnas.2505704122 | PMCID: PMC12318227 | PMID: 40705423
- Evidence: Cell state analyses, including gene activity scores and surface protein visualization, were performed using the Seurat/Signac framework ( 43 , 44 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [freebayes] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat, Signac] -> stage not stated [GATK, Picard]

### Cell-type-informed genotyping of mosaic focal epilepsies reveals cell-autonomous and non-cell-autonomous disease-associated transcriptional programs. (PNAS 2025)

- DOI: 10.1073/pnas.2509622122 | PMCID: PMC12305027 | PMID: 40674414
- Version used: **5.1.0**
- Evidence: Seurat (v5.1.0) ( 26 ) and Harmony (v1.2.0) ( 16 ) were used for data normalization, integration, clustering, and annotation ( SI Appendix ).
- Full pipeline: normalisation [Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [CellChat, fgsea v1.28.0]

### Foxn3 is required to suppress aberrant ciliogenesis in nonphotoreceptor retinal neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2500871122 | PMCID: PMC12304973 | PMID: 40663603
- Evidence: Single-cell library construction, sequencing, Cell Ranger processing, and Seurat analysis were performed as described previously ( 47 , 53 , 70 ).
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [HOMER, Seurat, deepTools, scDblFinder]

### FcγRIIIa is a noncanonical costimulatory molecule for CD8 T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2509016122 | PMCID: PMC12260523 | PMID: 40591599
- Version used: **3.0.0**
- Evidence: More customized analyses were processed by Seurat (v 3.0.0), as described previously ( 50 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat v3.0.0]

### Retinoic acid receptor assembly dynamics governs dual functions in cochlear organogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2426739122 | PMCID: PMC12232719 | PMID: 40577120
- Evidence: Previously published E14.5 and P2 datasets were individually reanalyzed with the Seurat v4 pipeline ( 56 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Bone morphogenetic protein-9 controls pulmonary vascular growth and remodeling. (PNAS 2025)

- DOI: 10.1073/pnas.2410229122 | PMCID: PMC12232436 | PMID: 40549904
- Evidence: Data were processed with Cell Ranger and Seurat for differential gene expression and functional enrichment analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat, UMAP] -> stage not stated [GSEA]

### Antlers on does: An unexpected role of macrophages in deer biology. (PNAS 2025)

- DOI: 10.1073/pnas.2424448122 | PMCID: PMC12184406 | PMID: 40512783
- Evidence: The Unique Molecular Identifiers (UMI) count matrix generated by Cell Ranger was further processed using the Seurat package v4.3.0( 32 ), following the guidelines outlined in the reference manual.
- Full pipeline: alignment/mapping [DESeq2, HISAT2, StringTie] -> quantification [ImageJ] -> normalisation [ImageJ] -> differential/statistical testing [DESeq2, HISAT2, StringTie] -> stage not stated [GSEA, Seurat]

### Feedback regulation between histone lactylation and ALKBH3-mediated glycolysis regulates age-related macular degeneration pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2416046122 | PMCID: PMC12184506 | PMID: 40493193
- Evidence: Using Seurat UMAP for dimensionality reduction and clustering, we identified 10 cell populations ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: Then, the two datasets were analyzed in Seurat ( 70 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Single-cell resolution uncovers neighboring cell subtypes that share steroidogenic capacity during fetal testis development. (PNAS 2025)

- DOI: 10.1073/pnas.2501392122 | PMCID: PMC12167995 | PMID: 40460128
- Version used: **5.0.1**
- Evidence: Dotplots were generated with the R package Seurat v.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v5.0.1]

### Mgat4b-mediated selective &lt;i&gt;N&lt;/i&gt;-glycosylation regulates melanocyte development and melanoma progression. (PNAS 2025)

- DOI: 10.1073/pnas.2423831122 | PMCID: PMC12146715 | PMID: 40424122
- Evidence: Single-cell RNA sequencing was performed on sorted Mitfa+ve cells to analyze gene expression, and data were processed using Seurat.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Specialized molecular pathways drive the formation of light-scattering assemblies in leucophores. (PNAS 2025)

- DOI: 10.1073/pnas.2424979122 | PMCID: PMC12146710 | PMID: 40434648
- Version used: **4.3.0**
- Evidence: Most of the downstream analyses were performed using Seurat 4.3.0.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> structure determination [IMOD] -> stage not stated [Seurat v4.3.0]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Version used: **4.4.0**
- Evidence: Quality control was uniformly applied to each single-cell cohort as follows: 1) The raw gene expression matrix of each single-cell dataset was converted into a Seurat object using the R package Seurat (v4.4.0); 2) Doublets were removed from each sample using the R package DoubletFinder (v2.0.3) ( 33 ); 3) Novelty scores were calculated by determining the ratio of nFeature to nCount to assess the c...
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Evidence: Data analysis with Seurat.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Basement membrane patterning by spatial deployment of a secretion-regulating protease. (PNAS 2025)

- DOI: 10.1073/pnas.2412161122 | PMCID: PMC12107121 | PMID: 40359035
- Evidence: Col4a1 , Col4a2 , and ADAMTS-A in early-to-mid follicle clusters were retrieved and plotted using Seurat 5.
- Full pipeline: dimensionality reduction/clustering [Seurat] -> visualisation [Seurat]

### Dmrt2 and Hmx2 direct intercalated cell diversity in the mammalian kidney through antagonistic and supporting regulatory processes. (PNAS 2025)

- DOI: 10.1073/pnas.2418471122 | PMCID: PMC12107187 | PMID: 40354537
- Evidence: Analysis of published single-cell sequencing data from P0 mouse kidneys ( GSE232482 ), human fetal, or pediatric samples was performed using Seurat v4 packages.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Monocle, Seurat]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Evidence: Data were analyzed using Seurat and scVelo.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### Circadian clock-gated cell renewal controls time-dependent changes in taste sensitivity. (PNAS 2025)

- DOI: 10.1073/pnas.2421421122 | PMCID: PMC12088436 | PMID: 40339128
- Evidence: The gene-barcode matrices were analyzed and visualized using the Seurat R package (version 4.0.1) ( 21 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [R, Seurat]

### Integrating single-cell data with biological variables. (PNAS 2025)

- DOI: 10.1073/pnas.2416516122 | PMCID: PMC12067276 | PMID: 40294274
- Evidence: These ranged from statistical methods based on similar cells or shared cell types [fastMNN ( 7 ), Seurat ( 8 ), Harmony, LIGER ( 11 ), and scInt] to graph-based methods [BBKNN ( 17 ) and Conos ( 18 ) and deep learning methods [scVI, scANVI ( 19 ), and scPoli ( 20 ).
- Full pipeline: dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Seurat] -> machine learning [Seurat] -> visualisation [UMAP] -> stage not stated [R]

### Phospholipid flippase ATP11A brokers uterine epithelial integrity and function. (PNAS 2025)

- DOI: 10.1073/pnas.2420617122 | PMCID: PMC12054786 | PMID: 40261925
- Version used: **5.1.0**
- Evidence: After quality checks, we merged data from different age groups and estrus cycle stages with the R package Seurat (v 5.1.0) ( 55 ).
- Full pipeline: quality control [R, Seurat v5.1.0] -> alignment/mapping [STAR v2.6.1a] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq, ImageJ v1.53, Metascape]

### Mapping the developmental profile of ventricular zone-derived neurons in the human cerebellum. (PNAS 2025)

- DOI: 10.1073/pnas.2415425122 | PMCID: PMC12054822 | PMID: 40249772
- Version used: **4.0.2**
- Evidence: Low-quality cells were determined and excluded from further analysis based on outlier mitochondrial content (indicative of cellular stress or damage) or gene counts using the R package Seurat v4.0.2 ( 49 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [R, Seurat v4.0.2]

### Unified molecular approach for spatial epigenome, transcriptome, and cell lineages. (PNAS 2025)

- DOI: 10.1073/pnas.2424070122 | PMCID: PMC12037033 | PMID: 40249782
- Evidence: ...2020-A.” After initial mapping, barcode correction, and quality control were performed by spaceranger, the 10× filtered counts matrix was loaded into Seurat v5 for downstream analysis.
- Full pipeline: quality control [ArchR, Seurat] -> read trimming [fastp] -> alignment/mapping [HISAT2, Seurat, fastp] -> quantification [ArchR] -> dimensionality reduction/clustering [ArchR] -> visualisation [ggplot2]

### Dual genetic tracing demonstrates the heterogeneous differentiation and function of neuromesodermal progenitors in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2402305122 | PMCID: PMC12002027 | PMID: 40178900
- Evidence: After quality control, a total of 15,250 cells were retained for further analysis by Seurat ( 24 ).
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [CellChat, UMAP]

### Single cell-resolved cellular, transcriptional, and epigenetic changes in mouse T cell populations linked to age-associated immune decline. (PNAS 2025)

- DOI: 10.1073/pnas.2425992122 | PMCID: PMC12002302 | PMID: 40163732
- Evidence: Harmony was employed for batch correction, and Seurat clustering was applied to CD8+ T cells at a resolution of 0.6, yielding nine clusters.
- Full pipeline: quality control [Scanpy v1.4.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [ArchR v1.0.1, MACS2, Seurat, UMAP]

### Acute TREM2 inhibition depletes MAFB-high microglia and hinders remyelination. (PNAS 2025)

- DOI: 10.1073/pnas.2426786122 | PMCID: PMC12002275 | PMID: 40131948
- Evidence: ( C ) The Monocle prediction of the microglia transition trajectory with Seurat’s cluster information in ( A ) mapped alongside pseudotime tree.
- Full pipeline: alignment/mapping [Monocle, Seurat] -> dimensionality reduction/clustering [Monocle, SCENIC, Seurat, UMAP] -> simulation/modelling [Monocle, Seurat]

### Ectopic germinal centers in the nasal turbinates contribute to B cell immunity to intranasal viral infection and vaccination. (PNAS 2025)

- DOI: 10.1073/pnas.2421724122 | PMCID: PMC11962485 | PMID: 40112112
- Evidence: Raw UMI count matrices generated from the cellranger 10X pipeline were loaded and merged into a single Seurat object (Seurat version 5).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat]

### Dnmt3a-mediated hypermethylation of FoxO3 promotes redox imbalance during osteoclastogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2418023122 | PMCID: PMC11962505 | PMID: 40106360
- Evidence: Then, 26574 cells were analyzed using the R package “Seurat.” The minimum number of genes was 200, the maximum number of genes was 4,500, the minimum number of RNAs was 1,000, the maximum number of RNAs was 35,000, and the maximum percentage of mitochondrial RNA was 10%, which were the conditions for quality control data.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [UMAP]

### An atlas of early human mandibular endochondral and osteogenic paracrine signaling regions of Meckel's cartilage. (PNAS 2025)

- DOI: 10.1073/pnas.2420466122 | PMCID: PMC11962497 | PMID: 40096606
- Version used: **4.0.0**
- Evidence: Seurat (v4.0.0) was used to read the data and filter out low-quality cells.
- Full pipeline: normalisation [Harmony v1.2.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib v3.7.2, UMAP] -> stage not stated [CellChat, CellPhoneDB, Seurat v4.0.0]

### iPSCs engrafted in allogeneic hosts without immunosuppression induce donor-specific tolerance to secondary allografts. (PNAS 2025)

- DOI: 10.1073/pnas.2413398122 | PMCID: PMC11929385 | PMID: 40073064
- Version used: **4.0.1**
- Evidence: Raw sequencing data were processed using the Loupe Cell Browser (10× Genomics) and further processed using the R package Seurat (v4.0.1) to filter low-quality cells ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2, tidyverse] -> stage not stated [R, Seurat v4.0.1]

### Cell type and region-specific transcriptional changes in the endometrium of women with RIF identify potential treatment targets. (PNAS 2025)

- DOI: 10.1073/pnas.2421254122 | PMCID: PMC11929460 | PMID: 40063812
- Version used: **5.0.3**
- Evidence: Endometrial single-cell sequencing data from the Reproductive Cell Atlas ( 38 ) were downloaded from https://cellgeni.cog.sanger.ac.uk/vento/reproductivecellatlas/endometrium_all.h5ad and converted to a Seurat (v 5.0.3) ( 39 ) data object with SeuratDisk (v 0.0.0.9021).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.1] -> differential/statistical testing [lme4 v1.1] -> stage not stated [R, Seurat v5.0.3]

### Hypercholesterolemia-induced LXR signaling in smooth muscle cells contributes to vascular lesion remodeling and visceral function. (PNAS 2025)

- DOI: 10.1073/pnas.2417512122 | PMCID: PMC11912459 | PMID: 40035761
- Evidence: Clusters of cells were identified in an unsupervised manner using Seurat’s default graph-based clustering.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [Monocle]

### The synergistic effect of c-Myb hyperactivation and Pu.1 deficiency induces Pelger-Huët anomaly and promotes sAML. (PNAS 2025)

- DOI: 10.1073/pnas.2416121122 | PMCID: PMC11892618 | PMID: 40020188
- Evidence: Cell Ranger (v5.0) was used for genome comparison and data processing, followed by Seurat for quality control and single-cell analysis.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ]

### RORγt-expressing dendritic cells are functionally versatile and evolutionarily conserved antigen-presenting cells. (PNAS 2025)

- DOI: 10.1073/pnas.2417308122 | PMCID: PMC11892598 | PMID: 39993193
- Evidence: ( E and F ) Annotated UMAP ( E ) of integrated scRNA-seq datasets generated using Seurat Integration of scRNA-seq datasets pipeline, and colored by dataset ( F ).
- Full pipeline: dimensionality reduction/clustering [SCENIC, Seurat, UMAP]

### The RNA-binding protein RBPMS inhibits smooth muscle cell-driven vascular remodeling in atherosclerosis and vascular injury. (PNAS 2025)

- DOI: 10.1073/pnas.2415933122 | PMCID: PMC11892686 | PMID: 39999164
- Evidence: ( D ) Seurat package-based joint clustering of murine and human datasets using canonical correlation analysis.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Bioconductor]

### pTDP-43 levels correlate with cell type-specific molecular alterations in the prefrontal cortex of &lt;i&gt;C9orf72&lt;/i&gt; ALS/FTD patients. (PNAS 2025)

- DOI: 10.1073/pnas.2419818122 | PMCID: PMC11892677 | PMID: 39999167
- Evidence: We obtained a total of 34,874 and 53,331 single-nucleus multiomes (snRNA-seq and snATAC-seq) from the Emory and Mayo cohorts, respectively, after quality control filtration using the ArchR multiome pipeline ( 9 ) and Seurat snRNA-seq guidelines ( 10 ) ( Methods and SI Appendix , Figs.
- Full pipeline: quality control [ArchR, Seurat, SoupX] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [WGCNA]

### Osteocyte connexin hemichannels and prostaglandin E&lt;sub&gt;2&lt;/sub&gt; release dictate bone marrow mesenchymal stromal cell commitment. (PNAS 2025)

- DOI: 10.1073/pnas.2412144122 | PMCID: PMC11848350 | PMID: 39937859
- Evidence: The scRNA-seq data facilitated the clustering of cells, and the identification of MSPC subsets was achieved using the Seurat R package.
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [Monocle, UMAP] -> stage not stated [GSEA]

### Engineered immunological niche directs therapeutic development in models of progressive multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2409852122 | PMCID: PMC11848328 | PMID: 39937858
- Evidence: The Seurat R package (v.4.3.0) ( 27 ) was used to remove cells with more than 5% mitochondrial genes or fewer than 200 and greater than 3,500 transcripts.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [CellChat] -> stage not stated [R, Seurat]

### Uterine organoids reveal insights into epithelial specification and plasticity in development and disease. (PNAS 2025)

- DOI: 10.1073/pnas.2422694122 | PMCID: PMC11804710 | PMID: 39883834
- Evidence: Seurat ( 34 ) unsupervised clustering analysis identified six distinct clusters ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [CellChat, GSEA]

### AMH protects the ovary from doxorubicin by regulating cell fate and the response to DNA damage. (PNAS 2025)

- DOI: 10.1073/pnas.2414734122 | PMCID: PMC11804487 | PMID: 39874288
- Version used: **4.1.0**
- Evidence: The samples were aligned against the mouse reference transcriptome mm10-2020-A and analyzed using Seurat ( 59 ) (R version 4.2.0, Seurat version 4.1.0).
- Full pipeline: alignment/mapping [R v4.2.0, Seurat v4.1.0] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [CellChat, GSEA, scVelo, velocyto]

### Targeting EPHB2/ABL1 restores antitumor immunity in preclinical models of ependymoma. (PNAS 2025)

- DOI: 10.1073/pnas.2319474122 | PMCID: PMC11789170 | PMID: 39841145
- Evidence: Seurat ( 59 ) was employed for the single-cell analysis.
- Full pipeline: quantification [HTSeq] -> dimensionality reduction/clustering [R, STRING db, pheatmap] -> stage not stated [Bioconductor, DESeq2, Seurat]

### Exome sequencing identifies genes for socioeconomic status in 350,770 individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2414018122 | PMCID: PMC11745334 | PMID: 39772748
- Evidence: The relative expression levels of gene set by the AddModuleScore function implemented in Seurat R package ( https://satijalab.org/seurat/ ).
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ANNOVAR, FUMA, PLINK v2.0, SAIGE, Seurat, SnpEff]

### Dissecting the cellular architecture and genetic circuitry of the soybean seed. (PNAS 2025)

- DOI: 10.1073/pnas.2416987121 | PMCID: PMC11725896 | PMID: 39793081
- Version used: **4.1.1**
- Evidence: The cleaned snRNA count matrix was imported to Seurat v4.1.1 ( 55 ) for downstream analyses.
- Full pipeline: quality control [SoupX v1.6.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v4.1.1, WGCNA]

### Integrin-activating &lt;i&gt;Yersinia&lt;/i&gt; protein Invasin sustains long-term expansion of primary epithelial cells as 2D organoid sheets. (PNAS 2025)

- DOI: 10.1073/pnas.2420595121 | PMCID: PMC11725944 | PMID: 39793062
- Evidence: Read counts were analyzed using Seurat (v5).
- Full pipeline: quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ]

### Endothelial KLF4 depletion drives age-related neurovascular dysfunction and neuropsychiatric impairment. (PNAS 2026)

- DOI: 10.1073/pnas.2426990123 | PMCID: PMC13291589 | PMID: 42313933
- Evidence: ( A ) Uniform manifold approximation and projection for dimension reduction (UMAP) and unsupervised clustering analysis using Seurat pipeline identified seven distinct cell populations (endothelial cells, microglia, mural cells, pericytes, neutrophils, oligodendrocytes, astrocytes) from the total of 7398 cells (young WT Cre = 1,285 cells, young EC-K4KO = 1,358 cells, old WT Cre = 2,506 cells, old ...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: Analysis was performed using Seurat ( 47 – 49 ) (v5.1.0).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### APOBEC2 deficiency disrupts hematopoietic lineage commitment, resulting in emergence of dual identity lymphocytes in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2531122123 | PMCID: PMC13250534 | PMID: 42247564
- Evidence: Downstream analysis was conducted in Seurat.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, scDblFinder]

### Reconstructing EBV reactivation and DNA damage response kinetics in morphologic pseudotime. (PNAS 2026)

- DOI: 10.1073/pnas.2609598123 | PMCID: PMC13250554 | PMID: 42234528
- Evidence: Datasets were analyzed by adapting Seurat v5 ( 55 ) to support stratified quantitation ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler, Seurat]

### GPIHBP1 on oligodendrocytes binds lipoprotein lipase within the human brain. (PNAS 2026)

- DOI: 10.1073/pnas.2610646123 | PMCID: PMC13250511 | PMID: 42224591
- Version used: **5.0.3**
- Evidence: Briefly, raw data were processed using Seurat (v5.0.3) in R (v4.3.0).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R v4.3.0, Seurat v5.0.3]

### Purine metabolic adaptation protects the endothelium from disturbed flow-induced DNA damage and atherosclerosis. (PNAS 2026)

- DOI: 10.1073/pnas.2526299123 | PMCID: PMC13142911 | PMID: 42060719
- Evidence: The scRNA-seq and scATAC-seq datasets (NCBI BioProject repository accession number PRJNA646233) were performed with the R package Seurat as described previously ( 28 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R, Seurat]

### Hopx(+) optic nerve head-astrocytes counter neuronal stress and glaucoma damage. (PNAS 2026)

- DOI: 10.1073/pnas.2515277123 | PMCID: PMC13142992 | PMID: 42044330
- Version used: **4.1.1**
- Evidence: Seurat 4.1.1 ( 56 ) was used to perform downstream analysis following the standard pipeline using cells with more than 500 genes and 1,500 UMI counts, mitochondria percentage <10%, resulting in 6,441 cells.
- Full pipeline: stage not stated [Seurat v4.1.1]

### FABP7 controls radial glial scaffold stability during human cortical development. (PNAS 2026)

- DOI: 10.1073/pnas.2523130123 | PMCID: PMC13099611 | PMID: 41984827
- Version used: **4.4.0**
- Evidence: ...ngle-cell RNA-sequencing data; Code data have been deposited in NCBI; Github ( https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE304516 ) ( 47 ); Seurat (v4.4.0, https://satijalab.org/seurat/ ) ( 48 ) for single-cell RNA-seq data normalization and clustering; edgeR (v3.40.2) ( 49 ) for differential gene expression analysis; hdWGCNA (v0.4.00, https://smorabit.github.io/hdWGCNA/ ) ( 50 ) for wei...
- Full pipeline: normalisation [Seurat v4.4.0, edgeR v3.40.2] -> dimensionality reduction/clustering [Seurat v4.4.0, UMAP, edgeR v3.40.2] -> differential/statistical testing [Seurat v4.4.0, edgeR v3.40.2] -> visualisation [UMAP] -> stage not stated [GSEA, WGCNA]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Version used: **5.1.0**
- Evidence: The raw gene count matrix from the study ( 56 ) ( GSE264342 ) was downloaded from GEO and reanalyzed using Seurat v5.1.0, and the same parameters and procedures as described in ( 56 ).
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Meiotic prophase I disruption as a strategy for nonhormonal male contraception using small-molecule inhibitor JQ1. (PNAS 2026)

- DOI: 10.1073/pnas.2517498123 | PMCID: PMC13080027 | PMID: 41945432
- Version used: **4.1.1**
- Evidence: Downstream analyses were performed in R using Seurat (v4.1.1) ( 30 ).
- Full pipeline: quality control [SoupX v1.4.5, scDblFinder v2.0] -> alignment/mapping [STAR v2.5.3b] -> quantification [R] -> dimensionality reduction/clustering [Slingshot v2.4.0, UMAP] -> stage not stated [DESeq2, ImageJ, Seurat v4.1.1]

### Temporal neuronal differentiation programs safeguard neuronal diversity. (PNAS 2026)

- DOI: 10.1073/pnas.2527895123 | PMCID: PMC13056081 | PMID: 41911460
- Evidence: Single-cell RNA-sequencing data were analyzed using the Seurat framework to define neuronal subtypes.
- Full pipeline: stage not stated [Seurat]

### Immune cell profiling reveals expanded stem cell-like memory T cells in anti-GAD65-associated neurological syndromes. (PNAS 2026)

- DOI: 10.1073/pnas.2514753123 | PMCID: PMC13038060 | PMID: 41880578
- Version used: **5.0.1**
- Evidence: Filtered feature-barcode matrix files were then analyzed with the R package “Seurat (v5.0.1)” ( 61 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v5.0.1]

### GFAP&lt;sup&gt;+&lt;/sup&gt; FOXF2&lt;sup&gt;+&lt;/sup&gt; ependymal cells promote blood-brain barrier repair via DLL4-NOTCH signaling after neural injury. (PNAS 2026)

- DOI: 10.1073/pnas.2520352123 | PMCID: PMC13037844 | PMID: 41875155
- Evidence: Subsequent analysis of 60,565 quality-controlled cells in Seurat included projections visualized in Uniform Manifold Approximation and Projection (UMAP) space.
- Full pipeline: dimensionality reduction/clustering [GSEA, Seurat, UMAP] -> visualisation [Seurat, UMAP]

### Quantifying the fidelity of in vitro human cell culture systems using a biomedical foundation model. (PNAS 2026)

- DOI: 10.1073/pnas.2520482123 | PMCID: PMC13012098 | PMID: 41860964
- Version used: **5.0.0**
- Evidence: Gene-barcode matrices were loaded in Seurat (v5.0.0) in R (v4.3.0)/RStudio (v2023.09.1 + 494) ( 41 – 45 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.3.0, Seurat v5.0.0]

### The α-synuclein proteostasis network and its translational applications in Parkinson's disease. (PNAS 2026)

- DOI: 10.1073/pnas.2513317123 | PMCID: PMC13012101 | PMID: 41838907
- Evidence: Single-cell gene expression data were processed using the Seurat package ( 68 ) in R.
- Full pipeline: stage not stated [R, Seurat]

### Bacterial reporter-paired scRNA sequencing reveals cross talk between zinc starvation and zinc toxicity in macrophage antibacterial defense. (PNAS 2026)

- DOI: 10.1073/pnas.2530503123 | PMCID: PMC12993976 | PMID: 41802048
- Version used: **4.0.4**
- Evidence: Outliers were excluded based on the number of genes detected, quantity of transcripts, and percentage of mitochondrial transcripts using Seurat v4.0.4 ( 43 ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, scVelo v0.2.4, velocyto v0.17] -> differential/statistical testing [R v4.0] -> stage not stated [Seurat v4.0.4, scDblFinder v1.4.0]

### The membrane-associated ubiquitin ligase MARCHF8 degrades MHC-I in HPV-positive head and neck cancer for immune evasion. (PNAS 2026)

- DOI: 10.1073/pnas.2525730123 | PMCID: PMC12994185 | PMID: 41802050
- Evidence: Statistical analyses included Seurat-based scRNA-seq workflows, t tests, and Kaplan–Meier survival analyses.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat]

### ABCC1 protects skin dendritic cells from FITC-induced toxicity by efflux and extracellular glutathione buffering. (PNAS 2026)

- DOI: 10.1073/pnas.2538155123 | PMCID: PMC12974473 | PMID: 41785312
- Version used: **4.2**
- Evidence: For the presented bulk and scRNA-sequencing results, published datasets were analyzed running a customized R script with Seurat v.4.2 for single-cell sequencing.
- Full pipeline: stage not stated [Seurat v4.2]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Version used: **5.2.0**
- Evidence: The filtered data were then imported into Seurat (version 5.2.0) ( 45 ) and normalized using SCTransform and decomposed using PCA.
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Lipid nanoparticle GM-CSF replacement for autoimmune pulmonary alveolar proteinosis. (PNAS 2026)

- DOI: 10.1073/pnas.2511483123 | PMCID: PMC12913010 | PMID: 41671176
- Version used: **4.0.4**
- Evidence: All output files were loaded into Seurat (v4.0.4), and in summary, cells were log normalized to a scale factor of 10,000, then scaled using a linear transformation ( 48 ).
- Full pipeline: normalisation [Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, scDblFinder]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: The data were analyzed using the Seurat R package ( 61 ) (v4.4.0).
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Bridging unpaired single-cell multimodal data for integrative analyses with SuperMap. (PNAS 2026)

- DOI: 10.1073/pnas.2505182123 | PMCID: PMC12890892 | PMID: 41650244
- Evidence: Specifically, we first construct the KNN graph in the low-dimensional representation space (e.g., PCA for RNA data) using the FindNeighbors function in Seurat pipeline (default K = 50 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [ArchR, Signac]

### Differential &lt;i&gt;Hes1&lt;/i&gt; activation defines neural stem cell lineage commitment and niche maintenance in embryonic and adult mouse cortex. (PNAS 2026)

- DOI: 10.1073/pnas.2511800123 | PMCID: PMC12849698 | PMID: 41557790
- Version used: **5.3**
- Evidence: To clear this discrepancy, we subclustered the NIHes1 NSC cluster using “FindSubCluster” function of Seurat (v5.3).
- Full pipeline: dimensionality reduction/clustering [Seurat v5.3, UMAP]

### Combination antiviral and anti-inflammatory therapy mitigates persistent neurological deficits in mice post SARS-CoV-2 infection. (PNAS 2026)

- DOI: 10.1073/pnas.2530209123 | PMCID: PMC12799161 | PMID: 41499397
- Version used: **5.3.0**
- Evidence: Downstream analysis was conducted in R v4.5.0 using the Seurat v5.3.0 package.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.5, Seurat v5.3.0, pheatmap]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Version used: **5.2.1**
- Evidence: First, mouse brain scRNA-seq data were normalized and clustered using SNN-based clustering in Seurat (v.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### Mouse and human share conserved transcriptional programs for interneuron development. (Science 2021)

- DOI: 10.1126/science.abj6641 | PMCID: PMC7618238 | PMID: 34882453
- Evidence: Seurat was adopted to perform normalization, dimension reduction, unsupervised clustering and differentially expressed genes identification ( 64 , 65 ).
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> simulation/modelling [R]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Version used: **3.0**
- Evidence: ...ues (accession code SDY998) ( 51 ) generated by CEL-Seq2 were downloaded from the ImmPort repository, and downstream analysis was performed using the Seurat 3.0 package ( 52 ).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Sex-biased gene expression across mammalian organ development and evolution. (Science 2023)

- DOI: 10.1126/science.adf1046 | PMCID: PMC7615307 | PMID: 37917687
- Evidence: All single-cell datasets were analyzed with Seurat ( 87 ), including quality control, dimensionality reduction, clustering and cell-type annotation.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Version used: **3.1**
- Evidence: Clustered gene-set enrichment analysis We ranked conserved markers ( P <0.05) between the endoderm cell state in YS scRNA-seq data against hepatocytes in EL scRNA-seq and endoderm in the mouse gastrulation scRNA-seq data using the FindConservedMarkers function in Seurat (v3.1) with Bonferroni corrected FDR adjusted P -values.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### The dawn of spatial omics. (Science 2023)

- DOI: 10.1126/science.abq4964 | PMCID: PMC7614974 | PMID: 37535749
- Evidence: Tools designed for disaggregated data [such as the Seurat, ScateR, Scanpy, and Monocle packages ( 90 – 94 )] can provide good results but need to be used cautiously because the nuances of data generation can cause biases.
- Full pipeline: stage not stated [Monocle, Scanpy, Seurat]

### Brassinosteroid gene regulatory networks at cellular resolution in the &lt;i&gt;Arabidopsis&lt;/i&gt; root. (Science 2023)

- DOI: 10.1126/science.adf4721 | PMCID: PMC10119888 | PMID: 36996230
- Version used: **3.1.5**
- Evidence: Downstream analysis were carried out using Seurat version 3.1.5 ( 80 ), Waddington-Optimal Transport ( 41 ), muscat ( 81 ), tradeSeq ( 82 ), and GRNs inferred using CellOracle ( 60 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v3.1.5]

### Morphine-responsive neurons that regulate mechanical antinociception. (Science 2024)

- DOI: 10.1126/science.ado6593 | PMCID: PMC7616448 | PMID: 39208104
- Version used: **4.3.0**
- Evidence: R (version 4.1.0, https://www.r-project.org/ ) and Seurat (version 4.3.0) were used to analyze single-cell and single-nucleus sequencing data.
- Full pipeline: stage not stated [R v4.1.0, Seurat v4.3.0]

### Ciliopathy patient variants reveal organelle-specific functions for TUBB4B in axonemal microtubules. (Science 2024)

- DOI: 10.1126/science.adf5489 | PMCID: PMC7616230 | PMID: 38662826
- Evidence: Single cell RNASeq analysis Published 10X single cell data and metadata was read using the Seurat ( 82 – 85 ) SCTransform method to obtain a gene by cell expression matrix using data from ( 86 – 88 ) or the published gene by cell matrix was used with data from ( 89 , 90 ).
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ, Seurat, ilastik] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [ChimeraX, IMOD, PHENIX, RELION] -> visualisation [ImageJ, ilastik] -> stage not stated [VEP]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: ... correct the ambient RNA contaminations with SoupX ( https://github.com/constantAmateur/SoupX ) ( 89 ); ( 3 ) Load the corrected counting matrix into Seurat object with log normalization; ( 4 ) Calculate the proportion of UMIs from mitochondrial genes; and ( 5 ) The cells assigned as doublets or mitochondrial content >1% were removed.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### The immunopathological landscape of human pre-TCRα deficiency: From rare to common variants. (Science 2024)

- DOI: 10.1126/science.adh4059 | PMCID: PMC10958617 | PMID: 38422122
- Version used: **4.0.4**
- Evidence: Evaluation of TCR entropy and TCR chain combinations in scRNA-seq data We processed 10x single-cell transcriptome libraries with Cellranger (v6.1.1) and Seurat (v4.0.4).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, SAMtools v1.14] -> differential/statistical testing [R, tidyverse] -> visualisation [R, tidyverse] -> stage not stated [MACS2, Seurat v4.0.4, kallisto v0.46.1]

### PIEZO channels link mechanical forces to uterine contractions in parturition. (Science 2025)

- DOI: 10.1126/science.ady3045 | PMCID: PMC12807505 | PMID: 41231991
- Evidence: After transcriptome mapping using PIPseeker (Fluent BioSciences), the raw matrix was filtered with CellBender ( 78 ) to remove empty droplets and then filtered out nuclei with high mitochondria reads (>5%) using Seurat ( 79 ).
- Full pipeline: alignment/mapping [Seurat] -> quantification [CellProfiler] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy, edgeR] -> visualisation [UMAP] -> stage not stated [scDblFinder]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Version used: **4.0.5**
- Evidence: Then we used the standard workflow from Seurat (v.4.0.5) ( 53 ) to process the snRNA-seq data.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### High-resolution spatial mapping of cell state and lineage dynamics in vivo with PEtracer. (Science 2025)

- DOI: 10.1126/science.adx3800 | PMCID: PMC12766569 | PMID: 40705858
- Evidence: Additional analysis was performed in R (v.4.2.3) using Seurat ( 157 ) (v.4.3.0) with default function parameters unless otherwise noted.
- Full pipeline: alignment/mapping [Python, scikit-image v0.24.0] -> normalisation [Scanpy v1.10.0] -> dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> stage not stated [Cellpose v3.1.0, R v4.2.3, Seurat, Squidpy v1.6.2, scDblFinder]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Version used: **4.1**
- Evidence: To reduce potential ambient RNA contamination, especially for nuclear libraries, SoupX ( 69 ) was applied to the raw gene count matrix obtained from Cell Ranger, and the corrected read count matrix was used for downstream analyses with Seurat (v4.1)( 70 ) if not specified otherwise.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Intestinal mast cell-derived leukotrienes mediate the anaphylactic response to ingested antigens. (Science 2025)

- DOI: 10.1126/science.adp0246 | PMCID: PMC12513082 | PMID: 40773543
- Evidence: Quality control and single cell RNA sequencing (scRNAseq) analysis The data quality control and processing were performed with Seurat ( 96 ) and R packages (R version 4.3.3).
- Full pipeline: quality control [R v4.3.3, Seurat] -> alignment/mapping [kallisto v0.45.0] -> quantification [kallisto v0.45.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [Monocle, ggplot2] -> stage not stated [QuPath]

### Aberrant basal cell clonal dynamics shape early lung carcinogenesis. (Science 2025)

- DOI: 10.1126/science.ads9145 | PMCID: PMC7617789 | PMID: 40310937
- Version used: **5.0.1**
- Evidence: Integration and data processing were conducted using Seurat v5.0.1.
- Full pipeline: alignment/mapping [SAMtools] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.24.0] -> visualisation [R, UMAP, ggplot2] -> stage not stated [ANNOVAR v1.0.0, Seurat v5.0.1, Slingshot]

### Identification of antigen-presenting cell-T cell interactions driving immune responses to food. (Science 2025)

- DOI: 10.1126/science.ado5088 | PMCID: PMC12017586 | PMID: 39700315
- Version used: **4.1.2**
- Evidence: Subsequently, the matrix of gene/UMI counts were used as input for analysis by the R package Seurat (v.
- Full pipeline: alignment/mapping [RSEM v1.3.1, STAR] -> stage not stated [DESeq2, MACS2, R, Seurat v4.1.2]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Version used: **4.3.1**
- Evidence: Resulting raw count matrices were converted to a Seurat (v4.3.1) ( 74 ) object using functions Read10X and CreateSeuratObject (options: min.cells=3, min.features=50).
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Evidence: Replicates were then processed in the Seurat R package (v4.3.0).
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

### Distinct myeloid-derived suppressor cell populations in human glioblastoma. (Science 2025)

- DOI: 10.1126/science.abm5214 | PMCID: PMC12836367 | PMID: 39818911
- Evidence: Finally, counts were normalized to the total UMI count by cell and log-scaled using Seurat.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R, SCENIC, velocyto]

### Microglia Rank signaling regulates GnRH neuronal function and the hypothalamic-pituitary-gonadal axis. (Science 2026)

- DOI: 10.1126/science.aeb6999 | PMCID: PMC7619046 | PMID: 41818388
- Evidence: Public scRNAseq analyses Analyses of gene expression in mouse hypothalamus ( 20 ), were conducted using the interactive CellxGene viewer ( https://www.mrl.ims.cam.ac.uk ), while analyses of gene expression in human hypothalamus were performed using R/Seurat ( 21 ) or CellxGene viewer ( 22 ).
- Full pipeline: quality control [FastQC, STAR v2.7.1] -> alignment/mapping [FastQC, GATK, STAR v2.7.1] -> normalisation [FastQC, STAR v2.7.1] -> dimensionality reduction/clustering [FastQC, ImageJ, STAR v2.7.1, UMAP] -> stage not stated [GSEA, Seurat]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Version used: **5.1.0**
- Evidence: Analysis of single cell RNA-sequencing data For the low dose regimen of sIL-2, sIL-2 + IL-21, or IL-2/21-treatment in the B16F10 + pmel ACT model, the gene expression matrix was processed and analyzed using Seurat (version 5.1.0).
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Clustering was carried out using the Seurat method with a resolution of 0.2.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Single intramuscular injection of self-amplifying RNA of &lt;i&gt;Nppa&lt;/i&gt; to treat myocardial infarction. (Science 2026)

- DOI: 10.1126/science.adu9394 | PMCID: PMC13124201 | PMID: 41785353
- Version used: **5.3.0**
- Evidence: Data integration was performed by Seurat (version 5.3.0).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, R, Seurat v5.3.0, Slingshot v2.14.0]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **4.0**
- Evidence: For each sample, we used Seurat (v4.0) ( 78 , 79 ) to regress out cell cycle scores (only correcting for the difference between S and G2/M phases), applied SCTransform and projected the data into 50 principal components, which we utilized for low-resolution Louvain clustering (resolution=0.2).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

### Ontogeny of the spinal cord dorsal horn. (Science 2026)

- DOI: 10.1126/science.adx5781 | PMCID: PMC12879194 | PMID: 41505538
- Evidence: Further quality control, clustering and annotation were done using Seurat v4 (although Seurat v5 was released in the interim) in R (v4.4.1).
- Full pipeline: quality control [R v4.4.1, Seurat] -> dimensionality reduction/clustering [AnnData, R v4.4.1, Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [ggplot2] -> stage not stated [ImageJ]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Evidence: A standard Seurat framework (v4.4.0) was used to conduct normalization, principal component analysis (PCA), and dimensionality reduction.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

