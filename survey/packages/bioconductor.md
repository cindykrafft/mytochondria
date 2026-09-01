# Bioconductor

- **Category:** general
- **Papers in survey:** 216
- **Journals:** PNAS (94), Nature (89), Cell (30), Science (3)
- **Years:** 2021 (24), 2022 (38), 2023 (50), 2024 (39), 2025 (42), 2026 (23)
- **Versions named:** 3.14 (3), 3.8 (3), 3.15 (2), 3.19 (2), 3.11 (2), 3.13 (1), 3.12 (1), 3.18 (1), 3.6 (1), 1.0.6 (1)
- **Pipeline stages it appears in:** differential/statistical testing (72), quantification (24), normalisation (23), alignment/mapping (19), dimensionality reduction/clustering (14), visualisation (5), read trimming (4), quality control (3), variant calling (2)

## Papers

### Visualizing in deceased COVID-19 patients how SARS-CoV-2 attacks the respiratory and olfactory mucosae but spares the olfactory bulb. (Cell 2021)

- DOI: 10.1016/j.cell.2021.10.027 | PMCID: PMC8564600 | PMID: 34798069
- Evidence: ..._OLFACTORY_SIGNALING_PATHWAY gene set https://www.gsea-msigdb.org/gsea/msigdb/cards/REACTOME_OLFACTORY_SIGNALING_PATHWAY Systematic name: M4072 fgsea Bioconductor package https://bioconductor.org/packages/release/bioc/html/fgsea.html v1.17.0 org.Hs.eg.db Bioconductor database https://bioconductor.org/packages/release/data/annotation/html/org.Hs.eg.db.html v3.12.0 Other GeoMx Digital Spatial Profil...
- Full pipeline: stage not stated [Bioconductor, R v4.1, fgsea]

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: Analysis of ProSPr data and generation of VCs was done using the software R Bioconductor ( Gentleman et al., 2004 ).
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Evidence: ...Computing 4.0.2 R Core Team https://www.r-project.org R package – Seurat v3.2.2 Github https://github.com/satijalab/seurat R package – DESeq2 v1.30.0 Bioconductor https://bioconductor.org/packages/DESeq2/ R package – Circlize v0.4.11 CRAN https://CRAN.R-project.org/package=circlize R package – ggplot2 v3.3.2 CRAN https://CRAN.R-project.org/package=ggplot2 R package – ComplexHeatmap v2.7.3 Biocondu...
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Splice site m<sup>6</sup>A methylation prevents binding of U2AF35 to inhibit RNA splicing. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.062 | PMCID: PMC8208822 | PMID: 33930289
- Evidence: ...//www.r-project.org Bowtie Langmead et al., 2009 http://bowtie-bio.sourceforge.net/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/DESeq2 Bioconductor Huber et al., 2015 https://www.bioconductor.org/ Salmon Patro et al., 2017 https://combine-lab.github.io/salmon/ MACS2 Zhang et al., 2008 https://github.com/macs3-project/MACS MSPC Jalili et al., 2018 https://genometric.github.io/MSPC/ B...
- Full pipeline: stage not stated [Bioconductor, Cutadapt, DESeq2, MACS2, R]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: A numeric matrix of raw read counts was generated, with genes in rows and samples in columns, and used for differential gene expression analysis with the Bioconductor Limma package ( Ritchie et al., 2015 ) after removing genes with less than 50 total reads across all samples or of less than 200 nucleotides in length.
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: ...011 RRID: SCR_011841 RNA-SeQC DeLuca et al., 2012 RRID: SCR_005120 RSEM Li and Dewey, 2011 RRID: SCR_013027 Scanpy Wolf et al., 2018 RRID: SCR_018139 Bioconductor R Huber et al., 2015 RRID: SCR_001905 Bioconductor packages edgeR Robinson et al., 2010 RRID: SCR_012802 Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be ful...
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: ...pression/software/downloads/latest CITE-seq Count version 1.4.3 Github https://github.com/Hoohm/CITE-seq-Count R package DropletUtils version 1.4.2 R Bioconductor; Lun et al., 2019 https://www.bioconductor.org/packages/release/bioc/html/DropletUtils.html R package Seurat version 3.1.5.9900 Github; Butler et al., 2018 https://github.com/satijalab/seurat R package Harmony version 1.0 Github; Korsuns...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Compromised SARS-CoV-2-specific placental antibody transfer. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.027 | PMCID: PMC7755577 | PMID: 33476549
- Evidence: An orthogonal PLSDA was implemented using the R ‘ropls’ Bioconductor package (orthI = 1; PredI = 1).
- Full pipeline: differential/statistical testing [Cytoscape v3.8.0] -> stage not stated [Bioconductor, CellProfiler, R v4.0.0]

### Dynamic 3D proteomes reveal protein functional alterations at high resolution in situ. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.021 | PMCID: PMC7836100 | PMID: 33357446
- Evidence: ...ttps://www.bioconductor.org/packages/release/bioc/html/MSstats.html proteusLabelFree Marek Gierlinski https://github.com/bartongroup/proteusLabelFree Bioconductor Huber et al., 2015 https://www.bioconductor.org/about/ topGO Adrian Alexa, Jorg Rahnenfuhrer https://bioconductor.org/packages/release/bioc/html/topGO.html viper Mariano J Alvarez http://bioconductor.org/packages/release/bioc/html/viper....
- Full pipeline: differential/statistical testing [SciPy, limma] -> stage not stated [AutoDock Vina v1.1.2, Bioconductor, NAMD v2.13, PyMOL v2.4, Python, R, pheatmap, seaborn]

### Post-gastrulation synthetic embryos generated ex utero from mouse naive ESCs. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.028 | PMCID: PMC9439721 | PMID: 35988542
- Evidence: ...com/single-cell-gene-expression/software/downloads/latest Seurat R package v3.2.2 Satija Lab, USA https://satijalab.org/seurat/ AUCell R package v1.8 Bioconductor project, USA https://bioconductor.org/packages/release/bioc/html/AUCell.html UTAP Bioinformatics unit, Weizmann Institute of Science, Israel https://utap.readthedocs.io/en/latest/ DESeq2.0 Bioconductor project, USA https://bioconductor.o...
- Full pipeline: alignment/mapping [STAR v2.4.2a] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, R, Seurat, pheatmap]

### Cell surface fluctuations regulate early embryonic lineage sorting. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.022 | PMCID: PMC8896887 | PMID: 35196500
- Evidence: Transcriptome analysis Principal component and cluster analyses were performed based on log 2 fragments per kilobase of exon per million mapped fragments (log 2 FPKM) values computed with the Bioconductor packages DESeq2 ( Love et al., 2014 ), Sincell ( Juliá et al., 2015 ) or FactoMineR in addition to custom scripts.
- Full pipeline: alignment/mapping [Bioconductor] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Bioconductor] -> stage not stated [DESeq2, HTSeq, ImageJ]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: ...ge) ( Angerer et al., 2016 ) v 3.0.1 ClusterProfiler (R package) ( Yu et al., 2012 ) v3.10.1 (CRAN) SingleR (R package) ( Aran et al., 2019 ) v1.0.5 (Bioconductor) DirichletReg (R package) ( Maier, 2014 ) v0.6.3.1 (CRAN) AUCell (R package) ( Aibar et al., 2017 ) v1.6.1 (CRAN) Cytobank ( Kotecha et al., 2010 ) https://www.cytobank.org https://doi.org/10.1002/0471142956.cy1017s53 SPADE (Cytobank) ( ...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: In order to assign each cell to a lineage and subsequent cell type, the FlowSOM clustering algorithm was used in iterative rounds with the Bioconductor “FlowSOM” package in R (v.1.16.0, Van Gassen et al., 2015 ).
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: Peaks were called in each sample using MACS2 79 with default parameters, and differential accessibility/binding analysis was conducted using Bioconductor DESeq2 in RStudio.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Evidence: Statistical analysis of protein quantitation was completed with R Bioconductor package artMS (version 1.14.0) 56 and its function artmsQuantification, which is a wrapper around the R Bioconductor package Mass Spectrometry Statistics and Quantification (MSstats) (version 4.4.0) as follows 38 ( table S2 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### Mechanopathology of biofilm-like Mycobacterium tuberculosis cords. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.016 | PMCID: PMC10642369 | PMID: 37865090
- Evidence: ...ect for Scientific Computing Free Software Foundation RRID: SCR_001905 Star PMID: 23104886 RRID: SCR_004463 FastQC Baraham Institute RRID: SCR_014583 Bioconductor Roswell Park Comprehensive Cancer Center RRID: SCR_006442 Other NalgeneTM square PETG media bottles with closure ThermoFisher Cat#: 2019-0030 Lung-on-chip Emulate Cat#: Chip-S1 Chip Coating Reagents Emulate Cat#: ER1, ER2 1.30/1.00 x 15 ...
- Full pipeline: quality control [Bioconductor, FastQC, GSEA, STAR v2.7.10b] -> alignment/mapping [STAR v2.7.10b] -> quantification [R, edgeR] -> stage not stated [ImageJ, MACS2]

### Serotonin reduction in post-acute sequelae of viral infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.013 | PMCID: PMC11227373 | PMID: 37848036
- Version used: **3.8**
- Evidence: ...a Taqman assay Thermo Scientific Mm00558004_m1 Vil1 Taqman assay Thermo Scientific Mm00494146_m1 Software and algorithms Agilent software Agilent N/A Bioconductor v.3.8 Bioconductor https://www.bioconductor.org/ Biorender Biorender https://biorender.com/ Flowjo v10.6.2 BD https://www.flowjo.com/ GSEA Broad institute https://www.gsea-msigdb.org/ ImageJ v2.1.0/1.53c NIH https://imagej.nih.gov/ij/ Ka...
- Full pipeline: read trimming [edgeR] -> quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1, limma] -> stage not stated [Bioconductor v3.8, GSEA, ImageJ v2.1.0, Seurat, kallisto v0.46.0]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Evidence: Enrichment analysis on different genomic elements was calculated using the Bioconductor package regioneR (v1.18.1) with overlapPermTest function 72 .
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Evidence: 40-bp paired-end ATAC-seq FASTQs were aligned to the mm10 genome from the Bsgenome.Mmusculus.UCSC.mm10 Bioconductor package (version 1.4.0) using Rsubread’s align method in paired-end mode with fragments between 1 to 5000 base-pairs considered properly paired.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### The proteomic landscape of genome-wide genetic perturbations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.026 | PMCID: PMC7615649 | PMID: 37080200
- Evidence: All analyses conducted in R, using standard, publicly accessible packages obtained either through GitHub ( https://github.com/ ), the Comprehensive R Archive Network (CRAN, https://cran.r-project.org/ ), or Bioconductor ( https://www.bioconductor.org/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler, limma] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [Bioconductor, ComplexHeatmap, R, WGCNA]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Evidence: Gene ontology (GO) overrepresentation analysis Differentially expressed human proteins from 30 μM arsenite (As(III)) treatment dataset were used for GO term “Biological processes” overrepresentation analysis using clusterProfiler (R Bioconductor).
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Evidence: 72 https://deeptools.readthedocs.io/en/ develop/ BEDtools v2.30.0 Quinlan 73 https://bedtools.readthedocs.io/en/latest/ Seqmonk v1.47.1 Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk/ projects/seqmonk/ SeqPlots v.12.1 Stempor and Ahringer 74 https://bioconductor.org/packages/release/bioc/html/ seqplots.html R v4.1.2 R Project https://www.r-project.org/ Bioconductor Huber et al.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### SARS-CoV-2 replication in airway epithelia requires motile cilia and microvillar reprogramming. (Cell 2023)

- DOI: 10.1016/j.cell.2022.11.030 | PMCID: PMC9715480 | PMID: 36580912
- Evidence: Batch correction was done using ComBat function from the sva package from Bioconductor, and the log 2 -transformation was undone to obtain the counts for differential expression analysis.
- Full pipeline: normalisation [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, GSEA] -> stage not stated [ImageJ, MACS2, R]

### Thyroid hormone remodels cortex to coordinate body-wide metabolism and exploration. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.041 | PMCID: PMC11455614 | PMID: 39178853
- Evidence: Ordered gene set enrichment analysis For each cell subtype analyzed through the above differential expression framework, the background genes used in the DE analysis (genes expressed in >1% of cells of the relevant subtype) were annotated using the gene biotype information in the “EnsDb.Mmusculus.v79” package in R Bioconductor and filtered to include only protein-coding genes.
- Full pipeline: read trimming [Seurat] -> alignment/mapping [Seurat] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, R v4.2.2] -> stage not stated [GSEA, PyTorch]

### BCAA-nitrogen flux in brown fat controls metabolic health independent of thermogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.030 | PMCID: PMC11145561 | PMID: 38653240
- Evidence: .../calrapp.org/ Compound Discoverer 3.3 Thermo Fisher Scientific Cat# OPTON-3106 RStudio R Core team https://www.R-project.org/ heatmaps version 1.26.0 Bioconductor https://bioconductor.org/packages/release/bioc/html/heatmaps.html Biorender Biorender https://www.biorender.com/ MetaboAnalyst 6.0 MetaboAnalyst https://www.metaboanalyst.ca/ Adobe Illustrator 2020 Adobe https://www.adobe.com/products/il...
- Full pipeline: stage not stated [Bioconductor, Monocle]

### Pan-cancer proteogenomics characterization of tumor immunity. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.027 | PMCID: PMC10988632 | PMID: 38359819
- Evidence: Consensus clustering was performed using the R packages ConsensusClusterPlus 110 within the Bioconductor package CancerSubtypes.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, Enrichr] -> differential/statistical testing [GSVA, SciPy] -> machine learning [R] -> visualisation [GSVA] -> stage not stated [Cellpose, scikit-image]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Evidence: Specifically, we retrieved the human GO annotation data from the R/Bioconductor packages org.Hs.eg.db 127 and GO.db 128 and then conducted the overlap analysis between GO terms and KD signature using the hypergeometric test.
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 84 ; RRID: N/A Bioconductor DESeq2 v1.36 Love et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.002 | PMCID: PMC11829167 | PMID: 39814019
- Evidence: These were conducted using GENESIS Bioconductor package in R, which was developed for large-scale genetic analyses in samples with complex structure including relatedness, population structure and ancestry admixture.
- Full pipeline: alignment/mapping [LDSC] -> variant calling [LDSC] -> dimensionality reduction/clustering [LDSC] -> stage not stated [Bioconductor, GCTA, MAGMA v1.08, PLINK v1.9]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **3.19**
- Evidence: 218 https://github.com/bioexcel/biobb_pdb_tools biomaRt (Bioconductor v3.19) Durinck et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: 30th, 2018) and then the R/Bioconductor genbankr (version 1.10.0) was used to distinguish mouse contigs from the contigs of other species.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### Rapid and stable mobilization of CD8<sup>+</sup> T cells by SARS-CoV-2 mRNA vaccine. (Nature 2021)

- DOI: 10.1038/s41586-021-03841-4 | PMCID: PMC8426185 | PMID: 34320609
- Evidence: Dimensional reduction of multiparametric flow cytometry data Dimensionality reduction of multiparametric flow cytometry data was done with R version 4.0.2 using the Bioconductor (release (3.11)) CATALYST package23.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2] -> dimensionality reduction/clustering [Bioconductor, R v4.0.2] -> stage not stated [MACS2]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: Segmentation was performed with circular binary segmentation (alpha = 0.0001 and undo.prune = 0.05) from R Bioconductor DNACopy package 34 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Loop extrusion as a mechanism for formation of DNA damage repair foci. (Nature 2021)

- DOI: 10.1038/s41586-021-03193-z | PMCID: PMC7116834 | PMID: 33597753
- Evidence: Scanned array data were normalized using Tiling Affymetrix Software (TAS) (quantile normalization, scale set to 500) and analyzed as described in 10 , 12 and converted to.wig files using R/Bioconductor software, when necessary, for visualization using the Integrated Genome Browser (bioviz.org).
- Full pipeline: read trimming [R, SAMtools] -> alignment/mapping [R, SAMtools] -> normalisation [Bioconductor, deepTools] -> differential/statistical testing [deepTools] -> visualisation [Bioconductor] -> stage not stated [MACS2, ggplot2]

### Skin-resident innate lymphoid cells converge on a pathogenic effector state. (Nature 2021)

- DOI: 10.1038/s41586-021-03188-w | PMCID: PMC8336632 | PMID: 33536623
- Evidence: Fitting of the LDA model was performed with the CountClust Bioconductor package (v1.12.0) [ 27 ], which is a wrapper for the maptpx package (v1.9.2) [ 62 ].
- Full pipeline: normalisation [SciPy, Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Scanpy, UMAP] -> visualisation [UMAP] -> stage not stated [Bioconductor]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: Differentially expressed genes (DEGs) were detected by DESeq2 package from Bioconductor ( bioconductor.org/packages/release/bioc/html/DESeq2 ) 62 using likelihood ratio test (LRT, adjusted P -value < 0.001) or Wald test.
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### Control of osteoblast regeneration by a train of Erk activity waves. (Nature 2021)

- DOI: 10.1038/s41586-020-03085-8 | PMCID: PMC7864885 | PMID: 33408418
- Evidence: Bioconductor package DESeq2 35 (v 1.26.0) were employed for differential expression (DE) analysis.
- Full pipeline: read trimming [TopHat, Trim Galore v0.4.1] -> alignment/mapping [TopHat, Trim Galore v0.4.1] -> quantification [featureCounts] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> stage not stated [ilastik v1.3.3]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Evidence: Cufflinks was used to generate transcript abundance as fragments per kilobase of transcript per million mapped reads (FPKM), and statistical analysis of FPKM values was calculated using R (Bioconductor).
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Nociceptor neurons affect cancer immunosurveillance. (Nature 2022)

- DOI: 10.1038/s41586-022-05374-w | PMCID: PMC9646485 | PMID: 36323780
- Evidence: Raw read count tables were normalized by the median of ratios method with the DESeq2 package from Bioconductor and then converted to GCT and CLS format.
- Full pipeline: read trimming [STAR v2.5.1b, Trimmomatic v0.35] -> alignment/mapping [STAR v2.5.1b, Trimmomatic v0.35, featureCounts] -> quantification [Bioconductor, RSEM] -> normalisation [Bioconductor, RSEM] -> dimensionality reduction/clustering [R] -> stage not stated [DESeq2 v1.18.1, ImageJ]

### Antibody targeting of E3 ubiquitin ligases for receptor degradation. (Nature 2022)

- DOI: 10.1038/s41586-022-05235-6 | PMCID: PMC9534761 | PMID: 36131013
- Evidence: Quantification and statistical analysis were performed by MSstatsTMT v2.2.7, an open-source R/Bioconductor package 35 .
- Full pipeline: quantification [Bioconductor, R] -> normalisation [R, limma] -> differential/statistical testing [Bioconductor, limma]

### Brainstem ADCYAP1<sup>+</sup> neurons control multiple aspects of sickness behaviour. (Nature 2022)

- DOI: 10.1038/s41586-022-05161-7 | PMCID: PMC9492535 | PMID: 36071158
- Version used: **1.0.6**
- Evidence: The following analysis was based on Orchestrating Single-Cell Analysis from Bioconductor (v1.0.6; https://bioconductor.org/books/release/OSCA/ ) and vignettes from Seurat (v4.0; https://satijalab.org/seurat/ ) 50 .
- Full pipeline: quality control [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor v1.0.6, Seurat v4.0]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: Overlap between differentially expressed genes from the RNA-seq data (mouse) and ChIP–seq data (human) was performed by first transforming the human genes associated with each annotated peak to their corresponding mouse homologues using information available in the Ensembl database through the biomaRt Bioconductor package 60 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Evidence: Differential gene expression testing was performed using an NB GLM implemented in the Bioconductor package edgeR (v3.32.0) 52 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Retrograde movements determine effective stem cell numbers in the intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-04962-0 | PMCID: PMC7614894 | PMID: 35831497
- Version used: **3.14**
- Evidence: Differential expression analysis was performed between groups considering biological replicates of intestinal locations using DeSeq2 (version 1.34 in Bioconductor 3.14) 28 in R (version 4.1.1) (R Core Team 2021).
- Full pipeline: read trimming [STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> differential/statistical testing [Bioconductor v3.14, R v4.1.1] -> stage not stated [ImageJ, NumPy v1.19.5, Python v3.10, TrackMate]

### Structure of the MRAS-SHOC2-PP1C phosphatase complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05086-1 | PMCID: PMC9452295 | PMID: 35830882
- Evidence: Analysis of dependency map data We used the DepMap package (v.1.8) and experiment hub package (v.2.2), available on Bioconductor, to access the datasets from the Broad Institute DepMap cancer dependency study 61 , 62 .
- Full pipeline: structure determination [PHENIX] -> stage not stated [Bioconductor, R]

### Developmental dynamics of two bipotent thymic epithelial progenitor types. (Nature 2022)

- DOI: 10.1038/s41586-022-04752-8 | PMCID: PMC9159946 | PMID: 35614226
- Evidence: To do this, the raw count matrices and metadata describing the nine subtypes of TECs were obtained through the Bioconductor data package MouseThymusAgeing ( https://bioconductor.org ; 10.18129/B9.bioc.MouseThymusAgeing).
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Evidence: Gene expression was quantified using qCount from QuasR package 59 using the ‘TxDb.Mmusculus.UCSC.mm9.knownGene’ database for gene annotation (Bioconductor package: Carlson M and Maintainer BP.
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### Genetic instability from a single S phase after whole-genome duplication. (Nature 2022)

- DOI: 10.1038/s41586-022-04578-4 | PMCID: PMC8986533 | PMID: 35355016
- Evidence: Aneuploid libraries were not used as a reference and blacklists were constructed using the example from Bioconductor as a guideline.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.4] -> normalisation [RSEM] -> stage not stated [Bioconductor, GSEA, ImageJ]

### The cGAS-STING pathway drives type I IFN immunopathology in COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04421-w | PMCID: PMC8891013 | PMID: 35045565
- Evidence: The significant temporal dynamics were defined with the timecourse package in R Bioconductor, which uses a multivariate empirical Bayes model to rank proteins 57 .
- Full pipeline: quantification [ImageJ] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [limma v3.40.6] -> stage not stated [Bioconductor]

### RNA profiles reveal signatures of future health and disease in pregnancy. (Nature 2022)

- DOI: 10.1038/s41586-021-04249-w | PMCID: PMC8770117 | PMID: 34987224
- Evidence: Gene set enrichment analysis Gene set enrichment analysis (GSEA) 11 , 41 was done with the fast GSEA algorithm 42 using Bioconductor’s fgsea package 43 .
- Full pipeline: quality control [MultiQC] -> read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, Picard, R, fgsea]

### Spatial predictors of immunotherapy response in triple-negative breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06498-3 | PMCID: PMC10533410 | PMID: 37674077
- Evidence: A ‘spillover matrix’ quantifying crosstalk was generated using the Bioconductor CATALYST 41 package and subsequently used to correct single-cell measurements.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> quantification [Bioconductor] -> differential/statistical testing [R] -> machine learning [ilastik] -> stage not stated [CellProfiler]

### Epitope editing enables targeted immunotherapy of acute myeloid leukaemia. (Nature 2023)

- DOI: 10.1038/s41586-023-06496-5 | PMCID: PMC10499609 | PMID: 37648862
- Evidence: Deep sequencing data from the GUIDE-seq experiment were analysed using GS-Preprocess ( https://github.com/umasstr/GS-Preprocess ) and Bioconductor Package GUIDEseq (v.1.4.1) 68 .
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [Python] -> visualisation [ggplot2] -> stage not stated [Bioconductor, R]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Evidence: 5 ) (see Supplementary Table 3 ) and gene sets obtained via the msigdbr() function from the R Bioconductor package msigdbr (v.
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Evidence: Except when specifically mentioned, all analyses were performed with R/Bioconductor packages, R v.4.2.2 (2022-11-10 r83330) ( https://cran.r-project.org/ ; http://www.bioconductor.org/ ) in a Linux environment (x86_64-pc-linux-gnu (64-bit)).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### A spatially resolved timeline of the human maternal-fetal interface. (Nature 2023)

- DOI: 10.1038/s41586-023-06298-9 | PMCID: PMC10356615 | PMID: 37468587
- Evidence: To assign decidual cell populations (≥70% cell area in decidua) to a lineage, the clustering algorithm FlowSOM (Bioconductor FlowSOM package in R) 29 was used, which separated cells into 100 clusters based on the expression of 19 canonical lineage-defining markers ( Supplementary Information ).
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [limma, scikit-learn] -> stage not stated [ImageJ, Jupyter, Python, QuPath v0.4.0, R]

### Cooperation between bHLH transcription factors and histones for DNA access. (Nature 2023)

- DOI: 10.1038/s41586-023-06282-3 | PMCID: PMC10338342 | PMID: 37407816
- Evidence: Sequencing fragments were mapped to the W601 sequence and E-box-motif-containing variants (153 bp) using the Bioconductor package QuasR with default settings 67 , which internally use Bowtie for read mapping 68 .
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bioconductor, Bowtie2, ChimeraX, PyMOL] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.6, ImageJ, RELION, SAMtools v1.6]

### Psychedelics reopen the social reward learning critical period. (Nature 2023)

- DOI: 10.1038/s41586-023-06204-3 | PMCID: PMC10284704 | PMID: 37316665
- Evidence: Estimated transcript-level abundances were collapsed to gene-level expression estimates and analysed using the sleuth (v0.30.0) R/Bioconductor package.
- Full pipeline: quantification [Bioconductor] -> stage not stated [kallisto v0.46.2]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Version used: **3.15**
- Evidence: 9d ) were generated using the pathview package (version 1.36.0) in Bioconductor (v.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: The count data matrix was then processed by using limma and edgeR in R/Bioconductor, as described.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Evidence: Statistical analysis of differentially expressed proteins was done using the Bioconductor package limma (v.3.54).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### Fumarate induces vesicular release of mtDNA to drive innate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-05770-w | PMCID: PMC10017517 | PMID: 36890229
- Evidence: Read counting was performed using the Bioconductor package Rsubread (v.1.28.1) ( https://github.com/LTLA/csawUsersGuide ) and gene annotations from GENCODE (release M17).
- Full pipeline: read trimming [Cutadapt v1.10.0] -> alignment/mapping [Cutadapt v1.10.0, STAR v2.6.0c] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2 v1.18.1] -> stage not stated [GSEA, ImageJ]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: Further data processing was performed using the R/Bioconductor environment.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Evidence: Acquired raw data were analysed using the (LIMMA) package of R-Bioconductor after uploading the median signal intensities.
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Evidence: Reads per kilobase per million mapped reads (RPKM) and transcripts per million (TPM) gene expression values were calculated from the trimmed mean of M -values (TMM)-normalized counts per million (CPM) values using the Bioconductor package edgeR (v.3.30.0) 64 and R (v.4.0.0) 65 .
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Dendritic cells direct circadian anti-tumour immune responses. (Nature 2023)

- DOI: 10.1038/s41586-022-05605-0 | PMCID: PMC9891997 | PMID: 36470303
- Evidence: Differential expression analysis was performed using the R/Bioconductor edgeR package.
- Full pipeline: alignment/mapping [STAR v2.7.0] -> quantification [HTSeq v0.9.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [ImageJ]

### NK2R control of energy expenditure and feeding to treat metabolic diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-08207-0 | PMCID: PMC11602716 | PMID: 39537932
- Evidence: The SNPlocs.Hsapiens.dbSNP144.GRCh37 Bioconductor package 85 was used to convert the genomic coordinates of SNPs to rsID for the summary statistics of HbA1c and BMI-adjusted HbA1c.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> stage not stated [GEMMA, Seurat v4.3.0, VEP, data.table v1.14.2, tidyverse v1.3.1]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: GSEA was performed using the Bioconductor package fgsea with the default parameters on genes ranked by log[fold change] 91 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Inhibition of IL-11 signalling extends mammalian healthspan and lifespan. (Nature 2024)

- DOI: 10.1038/s41586-024-07701-9 | PMCID: PMC11291288 | PMID: 39020175
- Evidence: Differentially expressed genes were identified using R v4.2.0 using the Bioconductor package DESeq2 v1.36.0 using the Wald test for comparisons.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.7.9a] -> quantification [ImageJ v1.53t, pheatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.36.0, R v4.2] -> visualisation [pheatmap] -> stage not stated [featureCounts, fgsea v1.22.0]

### dsRNA formation leads to preferential nuclear export and gene expression. (Nature 2024)

- DOI: 10.1038/s41586-024-07576-w | PMCID: PMC11236707 | PMID: 38898279
- Evidence: Data were processed in the R/Bioconductor environment ( www.bioconductor.org , R v.3.6.1) using the DESeq2 package 54 ; v.1.24.0).
- Full pipeline: read trimming [Cutadapt v2.1, TopHat v2.1.1] -> alignment/mapping [Cutadapt v2.1, TopHat v2.1.1] -> quantification [featureCounts] -> stage not stated [BEDTools, Bioconductor, DESeq2]

### MYCT1 controls environmental sensing in human haematopoietic stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07478-x | PMCID: PMC11168926 | PMID: 38839950
- Evidence: Statistical analysis of MaxQuant output data was performed with the artMS Bioconductor package (v.1.4.2), which performs the relative quantification of protein abundance using the MSstats Bioconductor package (default parameters).
- Full pipeline: quantification [Bioconductor] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> stage not stated [AlphaFold, GSEA, R, Seurat v3.1.2]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Version used: **3.14**
- Evidence: All of the analyses were carried out using different packages in R version 4.1.2 and Bioconductor version 3.14.
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: The reference genome package (BSgenome.Mmusculus.UCSC.mm10) was downloaded from Bioconductor ( https://www.bioconductor.org ).
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Evidence: All packages are publicly available at the Comprehensive R Archive Network ( https://cran.r-project.org ), the Bioconductor project ( http://bioconductor.org ) or their respective GitHub pages.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Evidence: To find the functional pathways enriched in each set of regulons, we performed gene ontology enrichment analysis using the EnrichR Bioconductor package (v.3.1) 69 .
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Differential expression analysis was conducted with R Project and the Bioconductor package limmaVoom.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Evidence: Raw counts were corrected for biases due to different library preparations, if present, using the ComBat_seq function from the R Bioconductor package sva v.3.38.0 (ref.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### Anti-TIGIT antibody improves PD-L1 blockade through myeloid and T&lt;sub&gt;reg&lt;/sub&gt; cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07121-9 | PMCID: PMC11139643 | PMID: 38418879
- Evidence: To quantify gene expression levels, the number of reads mapped to the exons of each RefSeq gene was calculated in a strand-specific manner using the functionality provided by the R package Genomic Alignments (Bioconductor) 50 .
- Full pipeline: alignment/mapping [Bioconductor, R] -> quantification [Bioconductor, R] -> normalisation [Harmony v1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [fgsea] -> stage not stated [Seurat]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **3.6**
- Evidence: R (v.3.4.1) 46 and Bioconductor (v.3.6) 47 were used for the RNA-seq analysis.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Version used: **3.11**
- Evidence: All analyses were done in R-4.0.0, using the functionality of Bioconductor v.3.11.
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### Prime editing-installed suppressor tRNAs for disease-agnostic genome editing. (Nature 2025)

- DOI: 10.1038/s41586-025-09732-2 | PMCID: PMC12675287 | PMID: 41261131
- Evidence: Sequences for rhAmpSeq amplicons were extracted using the R Bioconductor BSGenome package (v.1.4.3) using the GRCh37/hg19 (human) reference genomes.
- Full pipeline: read trimming [Bowtie2, DESeq2, STAR, Trim Galore] -> alignment/mapping [Bioconductor, Bowtie2, DESeq2, STAR, Trim Galore] -> differential/statistical testing [DESeq2, STAR, Trim Galore]

### Origins of chromosome instability unveiled by coupled imaging and genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09632-5 | PMCID: PMC12695650 | PMID: 41162705
- Evidence: The read depth signal was segmented using the DNAcopy Bioconductor package.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2] -> variant calling [DELLY, WhatsHap] -> quantification [ImageJ] -> machine learning [XGBoost] -> stage not stated [Bioconductor, Python]

### Sperm sequencing reveals extensive positive selection in the male germline. (Nature 2025)

- DOI: 10.1038/s41586-025-09448-3 | PMCID: PMC12611766 | PMID: 41062690
- Evidence: Code modified from trackViewer (R/Bioconductor package v.1.38.0) was used to generate gene mutation lollipop plots. lme4 (v.1.1-33) was used for linear mixed-effects models. ggplot2 (v.3.4.4) was used for plotting. dNdScv ( https://github.com/im3sanger/dndscv ; version as of commit on 29 September 2023) was used for selection analysis.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [Bioconductor, ggplot2 v3.4.4, lme4] -> visualisation [R] -> stage not stated [BCFtools, Nextflow]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Evidence: In the chimpanzee genome, PRDM9 site density in sites per kb on SST1 regions was calculated using R and Bioconductor.
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Differential expression analysis between MYCN amplification status was performed using the Bioconductor package limma 66 (v.3.40.6).
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Fluctuating DNA methylation tracks cancer evolution at clinical scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09374-4 | PMCID: PMC12443617 | PMID: 40931062
- Evidence: We annotated fCpGs using Illumina manifest and other genomic annotation packages available at Bioconductor including IlluminaHumanMethylation450kanno.ilmn12.hg19 (v0.6.1) and IlluminaHumanMethylationEPICanno.ilm10b2.hg19 (v0.6.0).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Bioconductor, R, SAMtools, Stan, dynesty, ggplot2 v3.5.2, survival (R) v0.4.9]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Evidence: The GSVA method 33 , using the MSigDb Hallmark collection of RNA-seq data, was then used to calculate GSVA scores for E2F targets and G2/M checkpoint pathway using the GSVA Bioconductor package (v.1.50.5).
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Evidence: Read counts were normalized using the trimmed mean of M method implemented in the R Bioconductor package edgeR to determine the abundance of each gene.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Evidence: The rest of the data were read into R using the bsseq Bioconductor package, which was used to obtain methylation average per gene and genomic windows used for chromosome-level methylation.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: To adjust for technical variation, we used the RUVr method 84 implemented in the RUVSeq v.1.18.0 Bioconductor package.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: To classify cell types based on their marker expression levels, the FlowSOM clustering algorithm was used with the Bioconductor ‘FlowSOM’ R package 72 .
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **3.12**
- Evidence: Further analyses were performed using R 4.0.4 (‘Lost Library Book’) and Bioconductor 3.12.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Obtained raw unique molecular identifier (UMI) count matrices of valid barcoded cells for each port were loaded into R (v.4.1.2) for further analyses using Bioconductor packages 66 and Seurat (v.4.0.6) 67 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Version used: **3.15**
- Evidence: The analysis was implemented using R (v4.2.0) 84 and Bioconductor (v3.15) 85 .
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Evidence: The packages are both available from Bioconductor ( http://www.bioconductor.org ) (accessed in October 2022).
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Differential gene expression analysis was performed on filtered estimated read counts using the R Bioconductor package DESeq2 v.1.42.1, using a generalized linear model with a negative binomial distribution.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: Cell clustering analysis of the IR-treated samples was performed with the Seurat R Bioconductor package 69 , using the SC transformed counts generated using the ‘v2’ vst flavour, with Louvain resolution of 0.6 and the first 20 principal components as identified by principal component analysis, for both samples.
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Version used: **3.19**
- Evidence: For GO analysis, we used Bioconductor (v.3.19) to perform GO analyses in R ( https://bioconductor.org/packages/release/bioc/html/motifmatchr ).
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: Differential expression analysis was performed with the DESeq2 (v.1.22) Bioconductor package 40 , using a likelihood ratio test for data from time-course experiments.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: The −log 10 P values were visualized as a heat map created with the ComplexHeatmap Bioconductor package (v.2.16.0, using a custom colour palette shown in the scale) 61 , 62 .
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Evidence: Gene set variation analysis was used to calculate a per-sample activity score for each of the BTMs (excluding unannotated modules labelled ‘TBA’) using R Bioconductor package GSVA v.1.44.1 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Plasticity of the mammalian integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-08794-6 | PMCID: PMC12119373 | PMID: 40140574
- Evidence: 24 were obtained from the National Center for Biotechnology Information Gene Expression Omnibus repository ( GSE128092 ) and prepared the same way as described above, with a difference that the aligned reads were summarized using the featureCounts function of the RSubread (v2.6.4) R/Bioconductor package 54 .
- Full pipeline: quality control [FastQC v0.11.4] -> read trimming [R] -> alignment/mapping [Bioconductor, HTSeq, featureCounts] -> quantification [ImageJ] -> normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [ImageJ] -> stage not stated [DESeq2]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Evidence: The resulting single-cell gene expression data were analyzed within the R/Bioconductor framework ( www.r-project.org and www.bioconductor.org ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Version used: **3.18**
- Evidence: To detect significant differences in protein abundances between conditions, we performed a t -test using the package of Bioconductor (v.3.18) 58 , with a FDR threshold of 0.1.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Neutralizing GDF-15 can overcome anti-PD-1 and anti-PD-L1 resistance in solid tumours. (Nature 2025)

- DOI: 10.1038/s41586-024-08305-z | PMCID: PMC11779642 | PMID: 39663448
- Evidence: Differential gene expression analyses were performed using the R/Bioconductor package limma (linear models for microarray and RNA-sequencing data) between visugromab treatment (day 14) and pretreatment (baseline) by applying a paired moderated t -test.
- Full pipeline: quantification [R] -> differential/statistical testing [Bioconductor, limma]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Constructs Bioconductor ExpressionSet objects from raw count matrices and sample metadata, filters lowly expressed genes based on user-defined count and percentage thresholds, performs RLE normalization, applies log-transformation, and optionally performs scaling or YuGene-transformation 195 with optional subtraction of control-group medians to generate relative expression data; Gene processing.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Evidence: All R/Bioconductor analyses were based on R v4.5.1 (2025-06-13) ( https://cran.r-project.org/ ) using Rstudio software ( https://posit.co/download/rstudio-desktop/ ).
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### Focal white matter lesions drive grey matter inflammation and synapse loss. (Nature 2026)

- DOI: 10.1038/s41586-026-10414-w | PMCID: PMC13293868 | PMID: 42020752
- Evidence: Heat maps were plotted using ComplexHeatmap R package 73 (ComplexHeatmap (Bioconductor; http://bioconductor.org/packages/ComplexHeatmap/ ).
- Full pipeline: read trimming [Snakemake v7.24.0] -> quantification [ImageJ v1.54p] -> dimensionality reduction/clustering [UMAP] -> visualisation [Bioconductor, ComplexHeatmap, UMAP] -> stage not stated [Python, R, Seurat, igraph]

### Template-driven scaffolding of SCF&lt;sup&gt;FBXO42&lt;/sup&gt; regulates PP2A degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10368-z | PMCID: PMC13233325 | PMID: 41986709
- Evidence: The raw counts data were stored in a standard Bioconductor SummarizedExperiment object 50 .
- Full pipeline: quantification [limma] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, Coot, PHENIX, R]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Evidence: Genomic features definitions were based on the Bioconductor TxDb.Hsapiens.UCSC.hg38.knownGene (v3.14.0) annotation, corresponding to the UCSC knownGene track from GENCODE V38, and assembled using the createGeneAnnotation function in the ArchR package.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **3.13**
- Evidence: Subsequent analysis was performed using the statistical computing environment R v.4.1.2 in RStudio v.1.4.17 and Bioconductor v.3.13 (ref.
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Evidence: The top 1,000 outliers from each chromosome at each spatial scale were used in downstream analyses, including a gene ontology enrichment using topGO (v.2.42.0), an R Bioconductor package.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Evidence: Raw signal intensities from the resulting .idat files were calculated using the minfi Bioconductor package v.1.24.0.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: For 13 C-labelled samples, isotopic correction of raw GC–MS peaks for all reported metabolites was performed using the IsoCorrectoR package (v.1.5.1) available as part of the Bioconductor library (BioC 3.8) and implemented in R (CRAN 3.6.1).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: Filtered estimated read counts from RSEM were used for differential expression comparisons using the Wald test implemented in the R Bioconductor package DESeq2 v.1.22.2 based on generalized linear model and negative binomial distribution 70 .
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Evidence: ANOVA calculations were ordinary one-way ANOVA. q values were calculated using the qvalue command from Bioconductor in R Studio and Benjamini–Hochberg-corrected P values were calculated using the p.adjust command with the method being ‘BH’ in R Studio.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Differential expression analysis (DEA) was conducted using the Bioconductor EdgeR package (v.3.6).
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### Gene-drive-capable mosquitoes suppress patient-derived malaria in Tanzania. (Nature 2026)

- DOI: 10.1038/s41586-025-09685-6 | PMCID: PMC12779567 | PMID: 41372414
- Evidence: Pairwise percentage identity values were calculated by aligning each concatenated sequence to the NF54 reference genome using pwalign in Bioconductor, applying the formula: 100 × (number of identical positions)/(aligned positions + internal gap positions).
- Full pipeline: alignment/mapping [BWA, Bioconductor, Cutadapt] -> stage not stated [BCFtools, ImageJ]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: Differential gene expression analysis comparing Post- versus Pre- samples was performed using negative binomial distribution and Benjamini–Hochberg false discovery rate (FDR) with the Bioconductor package DESeq2, applying Wald tests on normalized counts to obtain log 2 (fold change) and P values for each gene.
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Independent mechanisms of inflammation and myeloid bias in VEXAS syndrome. (Nature 2026)

- DOI: 10.1038/s41586-025-09815-0 | PMCID: PMC12851934 | PMID: 41183570
- Evidence: Pseudobulk and single-cell genotyping of the consequence of the Uba1 base edit were performed using the pileup functionality in Rsamtools (as part of Bioconductor) 65 .
- Full pipeline: read trimming [Seurat] -> variant calling [Bioconductor] -> quantification [Seurat]

### Dendritic cell paucity in mismatch repair-proficient colorectal cancer liver metastases limits immune checkpoint blockade efficacy. (PNAS 2021)

- DOI: 10.1073/pnas.2105323118 | PMCID: PMC8609309 | PMID: 34725151
- Evidence: Gene read counts were then generated using the Bioconductor R package GenomicAlignments ( 73 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK] -> quantification [Bioconductor, DESeq2, R] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, GSVA, SnpEff]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Evidence: Peaks and DARs datasets were annotated to the TSS of the nearest gene using ChipSeeker v1.22.1 with org.At.tair.db and TxDb.Athaliana.BioMart.plantsmart28 Bioconductor packages ( 78 – 80 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Substrate discrimination and quality control require each catalytic activity of TRAMP and the nuclear RNA exosome. (PNAS 2021)

- DOI: 10.1073/pnas.2024846118 | PMCID: PMC8040639 | PMID: 33782132
- Evidence: The raw count matrix generated by HTSeq were then processed using the R/Bioconductor package DESeq ( https://www.huber.embl.de/users/anders/DESeq/ ), which was used to both normalize the full dataset and to analyze differential expressions between sample groups.
- Full pipeline: alignment/mapping [HTSeq v0.5.3, Picard] -> quantification [ImageJ] -> normalisation [Bioconductor] -> differential/statistical testing [Bioconductor]

### <i>Drosophila</i> Fezf functions as a transcriptional repressor to direct layer-specific synaptic connectivity in the fly visual system. (PNAS 2021)

- DOI: 10.1073/pnas.2025530118 | PMCID: PMC8020669 | PMID: 33766917
- Evidence: Expression quantification was performed with Salmon ( 37 ) to identify transcript-level abundance estimates and then collapsed down to the gene level using the R Bioconductor package tximport ( 38 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2, MACS2 v2.1.1] -> stage not stated [Fiji, ImageJ]

### Single-molecule nanopore sequencing reveals extreme target copy number heterogeneity in arylomycin-resistant mutants. (PNAS 2021)

- DOI: 10.1073/pnas.2021958118 | PMCID: PMC7817135 | PMID: 33443214
- Evidence: Single-nucleotide variant detection was carried out by using in-house R scripts, which utilized the Bioconductor packages, GenomicRanges ( 31 ), Genomic Alignments ( 31 ), VariantTools, and gmapR.
- Full pipeline: alignment/mapping [Bioconductor] -> stage not stated [R]

### OCT4 induces embryonic pluripotency via STAT3 signaling and metabolic mechanisms. (PNAS 2021)

- DOI: 10.1073/pnas.2008890118 | PMCID: PMC7826362 | PMID: 33452132
- Evidence: Principal component and cluster analyses were performed based on log 2 FPKM values computed with custom scripts, in addition to the Bioconductor packages DESeq ( 88 ) or FactoMineR .
- Full pipeline: alignment/mapping [HTSeq, STAR] -> variant calling [WGCNA] -> quantification [Bioconductor, HTSeq] -> dimensionality reduction/clustering [Bioconductor, WGCNA] -> differential/statistical testing [GSEA, R]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: The read counts for all samples were then normalized using the trimmed mean of M method implemented in the R Bioconductor package edgeR to generate the abundance for each gene ( 75 , 76 ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Metabolome-wide association study on &lt;i&gt;ABCA7&lt;/i&gt; indicates a role of ceramide metabolism in Alzheimer's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2206083119 | PMCID: PMC9618092 | PMID: 36269859
- Evidence: Peak picking was completed using Bioconductor R-package XCMS ( 46 ).
- Full pipeline: stage not stated [Bioconductor, FreeSurfer, PLINK]

### Socioeconomic inequalities in molecular risk for chronic diseases observed in young adulthood. (PNAS 2022)

- DOI: 10.1073/pnas.2103088119 | PMCID: PMC9621370 | PMID: 36252037
- Evidence: All analyses were conducted using R software, especially the Bioconductor suite ( 52 ), unless noted.
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R, limma] -> stage not stated [Bioconductor]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Peaks were imported into the DiffBind package from Bioconductor ( 54 ), and differential peaks were called between even (ChiRP_1) and odd (ChiRP_2) probe sets.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### Dopamine and GPCR-mediated modulation of DN1 clock neurons gates the circadian timing of sleep. (PNAS 2022)

- DOI: 10.1073/pnas.2206066119 | PMCID: PMC9407311 | PMID: 35969763
- Evidence: Differential expression analysis between nSyb neurons and clock neurons was performed using the Bioconductor package edgeR ( 33 ).
- Full pipeline: dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [Bioconductor, Seurat, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [Picard]

### Intestinal tissue-resident T cell activation depends on metabolite availability. (PNAS 2022)

- DOI: 10.1073/pnas.2202144119 | PMCID: PMC9411733 | PMID: 35969785
- Evidence: All normalizations and differential expression analyses were performed in R (version 3.1.0) together with the DESeq2 Bioconductor package and the Negative Binomial Distribution method.
- Full pipeline: read trimming [Cutadapt v1.1] -> alignment/mapping [TopHat] -> normalisation [Bioconductor, DESeq2, R v3.1.0] -> differential/statistical testing [Bioconductor, DESeq2, R v3.1.0]

### Ciliogenesis requires sphingolipid-dependent membrane and axoneme interaction. (PNAS 2022)

- DOI: 10.1073/pnas.2201096119 | PMCID: PMC9351462 | PMID: 35895683
- Evidence: Differential expression analysis for transcriptomes and translatomes was achieved using the Bioconductor package edgeR, based on the negative binomial distributions ( 57 ).
- Full pipeline: quality control [Bowtie2] -> alignment/mapping [Bowtie2, IMOD] -> dimensionality reduction/clustering [seaborn] -> differential/statistical testing [Bioconductor, Python, edgeR] -> visualisation [seaborn] -> stage not stated [ImageJ, MotionCor2]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Evidence: In R (v4.1.2), mapped reads were used to build count matrices using Bioconductor packages GenomicAlignments (v1.26.0) and GenomicFeatures (v1.42.2) ( 49 ).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### Blood-based untargeted metabolomics in relapsing-remitting multiple sclerosis revealed the testable therapeutic target. (PNAS 2022)

- DOI: 10.1073/pnas.2123265119 | PMCID: PMC9231486 | PMID: 35700359
- Evidence: False discovery rates were calculated by the Q value method from the Bioconductor R package and are provided for reference.
- Full pipeline: differential/statistical testing [Bioconductor, R] -> visualisation [Cytoscape]

### Nuclear speckle integrity and function require TAO2 kinase. (PNAS 2022)

- DOI: 10.1073/pnas.2206046119 | PMCID: PMC9231605 | PMID: 35704758
- Version used: **3.11**
- Evidence: All subsequent analysis was performed using R version 4.0.2 and Bioconductor 3.11 ( 47 ) in RStudio (R Core Team, 2020) (RStudio Team, 2020).
- Full pipeline: quality control [STAR] -> read trimming [STAR, Trimmomatic] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor v3.11, R v4.0.2]

### Explosive seed dispersal depends on SPL7 to ensure sufficient copper for localized lignin deposition via laccases. (PNAS 2022)

- DOI: 10.1073/pnas.2202287119 | PMCID: PMC9214497 | PMID: 35666865
- Evidence: Differential gene expression was analyzed using DESeq from Bioconductor ( 40 ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Bioconductor, R]

### APOBEC3A regulates transcription from interferon-stimulated response elements. (PNAS 2022)

- DOI: 10.1073/pnas.2011665119 | PMCID: PMC9171812 | PMID: 35549556
- Evidence: Bioconductor R software (R v4.0.5) was used to generate heatmaps in Fig.
- Full pipeline: read trimming [fastp] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, Bioconductor, R v4.0]

### An antagonistic pleiotropic gene regulates the reproduction and longevity tradeoff. (PNAS 2022)

- DOI: 10.1073/pnas.2120311119 | PMCID: PMC9170148 | PMID: 35482917
- Evidence: Transcriptome and translatome changes were calculated using the Bioconductor package DESeq2 with adjusted P ≤ 0.05.
- Full pipeline: alignment/mapping [HTSeq v0.9.1] -> quantification [HTSeq v0.9.1] -> stage not stated [Bioconductor, DESeq2, ImageJ]

### A saturation mutagenesis screen uncovers resistant and sensitizing secondary <i>KRAS</i> mutations to clinical KRAS<sup>G12C</sup> inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2120512119 | PMCID: PMC9170150 | PMID: 35471904
- Evidence: We used the Bioconductor Summarized Experiment machinery to store count data and keep track of the feature annotation ( 16 ).
- Full pipeline: differential/statistical testing [limma] -> stage not stated [Bioconductor, PHENIX]

### The CHARGE syndrome ortholog CHD-7 regulates TGF-β pathways in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2109508119 | PMCID: PMC9169646 | PMID: 35394881
- Version used: **3.7**
- Evidence: R v3.5.0 (2018-04-23) and Bioconductor v3.7 with BiocInstaller v1.30.0 were used.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.5.4a] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [Bioconductor v3.7, R v3.5]

### Signaling from the RNA sensor RIG-I is regulated by ufmylation. (PNAS 2022)

- DOI: 10.1073/pnas.2119531119 | PMCID: PMC9169834 | PMID: 35394863
- Evidence: Normalization and differential expression was carried out using the DESeq2 ( 70 ) Bioconductor ( 71 ) package with the R statistical programming environment.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [HTSeq]

### A DNA repair-independent role for alkyladenine DNA glycosylase in alkylation-induced unfolded protein response. (PNAS 2022)

- DOI: 10.1073/pnas.2111404119 | PMCID: PMC8892324 | PMID: 35197283
- Evidence: Data were analyzed using R/Bioconductor as described in the SI Appendix .
- Full pipeline: stage not stated [Bioconductor, Enrichr]

### TRIM14 inhibits OPTN-mediated autophagic degradation of KDM4D to epigenetically regulate inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2113454119 | PMCID: PMC8851536 | PMID: 35145029
- Evidence: Peaks were annotated to the gene with the closest transcription start sites by ChIPseeker (v1.28.3) available on Bioconductor.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5] -> dimensionality reduction/clustering [clusterProfiler v4.0.5] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.6, Picard]

### MRP5 and MRP9 play a concerted role in male reproduction and mitochondrial function. (PNAS 2022)

- DOI: 10.1073/pnas.2111617119 | PMCID: PMC8832985 | PMID: 35121660
- Version used: **3.4**
- Evidence: DESeq2 was run using R (version 3.6.1) and Bioconductor (version 3.4) with BioInstaller (version 1.24.0) for volcano plotting and statistical analysis of differential changes utilizing adjusted P value < 0.01 and false discovery rate cutoffs of 0.05.
- Full pipeline: quality control [FastQC v0.11.7] -> differential/statistical testing [Bioconductor v3.4, DESeq2 v1.12.3, R v3.6.1] -> stage not stated [HOMER]

### BRD4-directed super-enhancer organization of transcription repression programs links to chemotherapeutic efficacy in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2109133119 | PMCID: PMC8832982 | PMID: 35105803
- Evidence: These peaks were then annotated by specific genic features using the ChIPseeker R Bioconductor package ( 47 ) with promoter specification centered on ±3,000 bp of the transcription start site ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> alignment/mapping [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [Bioconductor, HOMER, MACS2]

### Electrophysiological measures from human iPSC-derived neurons are associated with schizophrenia clinical status and predict individual cognitive performance. (PNAS 2022)

- DOI: 10.1073/pnas.2109395119 | PMCID: PMC8784142 | PMID: 35017298
- Evidence: Gene set enrichment analyses were performed with the clusterProfiler Bioconductor package ( 57 ), using the hypergeometric test to assess enrichment of marginally significant DEGs (at P < 0.005) that were stratified by case–control directionality, against a background of all expressed genes that had Entrez gene IDs.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> variant calling [SAMtools] -> quantification [featureCounts v1.5.0, kallisto] -> dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [limma]

### Convergent evolution of venom gland transcriptomes across Metazoa. (PNAS 2022)

- DOI: 10.1073/pnas.2111392119 | PMCID: PMC8740685 | PMID: 34983844
- Evidence: We identified orthogroups with similar expression patterns using the isa implemented in the isa2 Bioconductor package ( 20 ) with default parameters.
- Full pipeline: quality control [kallisto] -> read trimming [kallisto] -> alignment/mapping [RAxML] -> quantification [kallisto] -> normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [Bioconductor, InterProScan]

### A dicer-related helicase opposes the age-related pathology from SKN-1 activation in ASI neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2308565120 | PMCID: PMC10756303 | PMID: 38113255
- Evidence: Peak calls were made using MACS2 v2.2.7.1 Peak files were feature annotated using Chipseeker Bioconductor package in R using the annotate Peak function.
- Full pipeline: read trimming [STAR v2.7.6a, Trim Galore] -> alignment/mapping [STAR v2.7.6a] -> quantification [DESeq2, R v3.5.2] -> differential/statistical testing [DESeq2, R v3.5.2] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.7.1, SAMtools v1.10]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Output bam files were converted into bigwig track files to display coverage throughout the genome (in RPM) using the GenomicRanges package ( 45 ) as well as other standard Bioconductor R packages.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### Salicylic acid and RNA interference mediate antiviral immunity of plant stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302069120 | PMCID: PMC10589665 | PMID: 37824524
- Evidence: Visualization of the data was achieved using R and Bioconductor ( 59 ) including the packages tidyverse and ggplot2.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2 v2.3.5] -> visualisation [Bioconductor, ggplot2, tidyverse] -> stage not stated [DESeq2, ImageJ, featureCounts]

### Unexpected metabolic rewiring of CO<sub>2</sub> fixation in H<sub>2</sub>-mediated materials-biology hybrids. (PNAS 2023)

- DOI: 10.1073/pnas.2308373120 | PMCID: PMC10589654 | PMID: 37816063
- Evidence: Statistical analysis of MaxQuant label-free quantitation data was performed with the artMS Bioconductor package which performs the relative quantification of protein abundance using the MSstats Bioconductor package (default parameters).
- Full pipeline: quantification [Bioconductor] -> differential/statistical testing [Bioconductor]

### Cooperative regulation of coupled oncoprotein synthesis and stability in triple-negative breast cancer by EGFR and CDK12/13. (PNAS 2023)

- DOI: 10.1073/pnas.2221448120 | PMCID: PMC10515179 | PMID: 37695916
- Evidence: Pooled samples were matched by barcoded reads, and guide-level counts were computed using bcSeq (v1.12.0) Bioconductor package ( 95 ) in the R (v3.5.1) programming environment.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [RSEM v1.2.25, STAR v2.4.1a] -> quantification [ImageJ, RSEM v1.2.25] -> differential/statistical testing [DESeq2 v1.22.0] -> stage not stated [Bioconductor]

### Systems-level temporal immune-metabolic profile in Crimean-Congo hemorrhagic fever virus infection. (PNAS 2023)

- DOI: 10.1073/pnas.2304722120 | PMCID: PMC10500270 | PMID: 37669378
- Evidence: DGE analysis with adjustment for confounding factors such as age, gender, cell type proportion, and other possible factors was performed using R/Bioconductor package DESeq2 v1.26.0 ( 40 ).
- Full pipeline: normalisation [R, limma v3.50.0] -> differential/statistical testing [R, limma v3.50.0] -> stage not stated [Bioconductor, DESeq2 v1.26.0, GSEA]

### <i>Bcl6</i>, <i>Irf2</i>, and <i>Notch2</i> promote nonclassical monocyte development. (PNAS 2023)

- DOI: 10.1073/pnas.2220853120 | PMCID: PMC10469339 | PMID: 37607223
- Evidence: All gene counts were then imported into the R/Bioconductor package EdgeR and TMM normalization size factors were calculated to adjust for samples for differences in library size.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> normalisation [Bioconductor, edgeR]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Evidence: DESeq2 Bioconductor package v1.40.0 ( 55 ) was used on the RNA-Seq data to conduct differential expression analyses.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### sccomp: Robust differential composition and variability analysis for single-cell data. (PNAS 2023)

- DOI: 10.1073/pnas.2203828120 | PMCID: PMC10438834 | PMID: 37549298
- Evidence: Being a statistical model that fits count data compositionality and group-wise variability while allowing the exclusion of outliers, we anticipate its adoption in other scientific fields. sccomp is available as an R package via Bioconductor and GitHub.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> machine learning [R] -> stage not stated [Seurat, Stan, limma, tidyverse]

### Ancient transcriptional regulators can easily evolve new pair-wise cooperativity. (PNAS 2023)

- DOI: 10.1073/pnas.2302445120 | PMCID: PMC10334809 | PMID: 37399378
- Evidence: Processing of sequence data was carried out in the programming language R using Bioconductor and custom scripts.
- Full pipeline: stage not stated [Bioconductor]

### Lipid biomarkers for algal resistance to viral infection in the ocean. (PNAS 2023)

- DOI: 10.1073/pnas.2217121120 | PMCID: PMC10318983 | PMID: 37364132
- Evidence: Preprocessing of the CDF files was done using the R ( 78 ) packages “xcms” ( 79 ) and “CAMERA” ( 80 ) obtained from the Bioconductor repository.
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [R] -> stage not stated [Bioconductor]

### Steroid receptor coactivator 3 is a key modulator of regulatory T cell-mediated tumor evasion. (PNAS 2023)

- DOI: 10.1073/pnas.2221707120 | PMCID: PMC10266015 | PMID: 37253006
- Evidence: The differential RNA expression profile between SRC-3 KO Treg versus wild-type Treg was analyzed using R, Bioconductor, and orange program.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [Bioconductor] -> stage not stated [GSEA, MACS2]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Downstream analyses and identification of differentially expressed genes used the EdgeR Bioconductor package ( 97 ).
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Consequences of poly(ethylene oxide) and poloxamer P188 on transcription in healthy and stressed myoblasts. (PNAS 2023)

- DOI: 10.1073/pnas.2219885120 | PMCID: PMC10161009 | PMID: 37094151
- Evidence: The Bioconductor package Empirical Analysis of Digital Gene Expression Data in R (edgeR) was utilized because of its ability to determine differential expression of a dataset with a small number of replicates that is expected to have less than 50% of the genes impacted ( 61 – 63 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [GSEA, STRING db]

### Rapid cancer cell perineural invasion utilizes amoeboid migration. (PNAS 2023)

- DOI: 10.1073/pnas.2210735120 | PMCID: PMC10151474 | PMID: 37075074
- Evidence: The expression count matrix from the mapped reads was computed using HTSeq ( http://htseq.readthedocs.io/ ), and the raw count matrix was processed using the R/Bioconductor package DESeq ( https://www.bioconductor.org/packages//2.10/bioc/html/DESeq.html ) to normalize the full data set and analyze differential expression between sample groups.
- Full pipeline: alignment/mapping [Bioconductor, HTSeq] -> normalisation [Bioconductor, HTSeq] -> differential/statistical testing [Bioconductor, HTSeq] -> stage not stated [Enrichr, ImageJ v1.52q]

### Epitranscriptic regulation of <i>HRAS</i> by <i>N</i><sup>6</sup>-methyladenosine drives tumor progression. (PNAS 2023)

- DOI: 10.1073/pnas.2302291120 | PMCID: PMC10083612 | PMID: 36996116
- Evidence: Then the exomePeak R/Bioconductor package (version 3.7) ( 61 ) was used to find the differential m 6 A peaks between the tumor and adjacent samples.
- Full pipeline: alignment/mapping [TopHat v2.2.1] -> differential/statistical testing [Bioconductor]

### Transcription factor bHLH121 regulates root cortical aerenchyma formation in maize. (PNAS 2023)

- DOI: 10.1073/pnas.2219668120 | PMCID: PMC10041174 | PMID: 36927156
- Evidence: Genes were annotated using R Software (version 3.2.4) (R Core Team 2018), Bioconductor ( 76 ), MapMan ( 77 ), and MaizeGDB ( 78 ).
- Full pipeline: alignment/mapping [MUSCLE] -> variant calling [R, lme4] -> differential/statistical testing [R] -> stage not stated [Bioconductor]

### RNA interference is essential to modulating the pathogenesis of mosquito-borne viruses in the yellow fever mosquito &lt;i&gt;Aedes aegypti&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213701120 | PMCID: PMC10089172 | PMID: 36893279
- Evidence: The edgeR Bioconductor software package ( https://bioconductor.org/packages/release/bioc/html/edgeR.html ) was used to determine differential expression between replicate datasets.
- Full pipeline: differential/statistical testing [Bioconductor, edgeR]

### Light-dependent signal transduction in the marine diatom <i>Phaeodactylum tricornutum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216286120 | PMCID: PMC10089185 | PMID: 36897974
- Evidence: Gene counts (unique aligned reads per gene) were used for differential expression (DE) analysis carried out using the DESeq R/Bioconductor package, which infers DE based on the negative binomial distribution.
- Full pipeline: alignment/mapping [Bioconductor] -> differential/statistical testing [Bioconductor] -> stage not stated [BLAST]

### Mitochondrial control of microglial phagocytosis by the translocator protein and hexokinase 2 in Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2209177120 | PMCID: PMC9974442 | PMID: 36787364
- Evidence: Differential enrichment analysis using Bioconductor R package Limma version 3.13 was used to identify candidate interactors (FDR < 10%, fold change > 2) ( 71 ).
- Full pipeline: differential/statistical testing [Bioconductor, R] -> stage not stated [Cytoscape]

### Definition of the contribution of an Osteopontin-producing CD11c<sup>+</sup> microglial subset to Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2218915120 | PMCID: PMC9963365 | PMID: 36730200
- Evidence: Analysis of differentially expressed genes (DEGs) was performed by a negative binomial model implemented in the R package edgeR (Bioconductor) ( 57 , 58 ), comparing OPN-KO.5XFAD to 5XFAD mice using a one-factor design and default parameters.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [MACS2]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Evidence: Where necessary, raw data were reanalyzed by bowtie2 (2.3.5) ( 77 ) alignment to the most recent Cryptococcus neoformans H99 or KN99α genome ( fungibd.org ), count matrices generated with HTSeq (1.99.2) ( 78 ) and RNA-seq analysis with Bioconductor DESeq2 (1.22.2) ( 79 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Sec22b is a critical and nonredundant regulator of plasma cell maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2213056120 | PMCID: PMC9926242 | PMID: 36595686
- Evidence: The Bioconductor edgeR package was used to import raw counts into R statistical software and compute normalized log2 counts per millions of mapped reads using the weighted trimmed mean of M-values as the normalization procedure.
- Full pipeline: read trimming [Bioconductor, edgeR] -> alignment/mapping [Bioconductor, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [GSEA, clusterProfiler, fgsea] -> differential/statistical testing [Bioconductor, R, edgeR, limma]

### The lncRNA LUCAT1 is elevated in inflammatory disease and restrains inflammation by regulating the splicing and stability of NR4A2. (PNAS 2023)

- DOI: 10.1073/pnas.2213715120 | PMCID: PMC9910463 | PMID: 36577072
- Version used: **3.14**
- Evidence: Salmon results files were imported into R using the package tximeta Bioconductor release 3.14 ( 71 ).
- Full pipeline: read trimming [Cutadapt, minimap2 v2.17] -> alignment/mapping [RSEM v1.3.1, STAR v2.6.1, minimap2 v2.17] -> stage not stated [Bioconductor v3.14]

### Bioprosthetic heart valve structural degeneration associated with metabolic syndrome: Mitigation with polyoxazoline modification. (PNAS 2023)

- DOI: 10.1073/pnas.2219054120 | PMCID: PMC9910464 | PMID: 36574676
- Evidence: Proteins with q-values < 0.05 were imported into RStudio and GSEA and visualizations were performed with Bioconductor packages clusterprofiler v4.4 and enrichplot v1.16.1 for dot plots.
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [Cytoscape v3.9.1] -> visualisation [Bioconductor, Cytoscape v3.9.1] -> stage not stated [GSEA]

### Epithelial tubule interconnection driven by HGF-Met signaling in the kidney. (PNAS 2024)

- DOI: 10.1073/pnas.2416887121 | PMCID: PMC11670081 | PMID: 39705305
- Evidence: Each batch was processed independently using the scran Bioconductor package ( 57 ).
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, ImageJ]

### E93 controls adult differentiation by repressing &lt;i&gt;broad&lt;/i&gt; in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2403162121 | PMCID: PMC11665871 | PMID: 39671182
- Evidence: Motifs matches, from Br and E93 binding sites from the FlyFactor Survey database, were identified in promoter regions (1,000 bp upstream and 200 bp downstream the transcription start site of the gene) with the matchMotifs function from the motifmatcher Bioconductor package in R.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [Bioconductor]

### Chronologically inappropriate morphogenesis (&lt;i&gt;Chinmo&lt;/i&gt;) is required for maintenance of larval stages of fall armyworm. (PNAS 2024)

- DOI: 10.1073/pnas.2411286121 | PMCID: PMC11626174 | PMID: 39589873
- Evidence: We utilized the comprehensive JASPAR database ( 60 ), which encompasses motifs from multiple species and is easily accessible through application programming interfaces (APIs) or Bioconductor packages ( 61 , 62 ).
- Full pipeline: quantification [MACS2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, Seurat, Signac]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Evidence: Gene set enrichment analysis (GSEA) ( 55 ), focused on Gene Ontology ( 56 ), was conducted using the R 4.3.1 Bioconductor package clusterProfiler ( 57 ) to elucidate whole transcriptomic patterns between groups.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### Manipulating a host-native microbial strain compensates for low microbial diversity by increasing weight gain in a wild bird population. (PNAS 2024)

- DOI: 10.1073/pnas.2402352121 | PMCID: PMC11513901 | PMID: 39401350
- Evidence: A “Generalized time-reversible with Gamma rate variation maximum likelihood” tree was constructed using a neighbor-joining tree as a starting point with the Phangorn package ( 86 ) following the Bioconductor workflow ( 87 ).
- Full pipeline: visualisation [vegan] -> stage not stated [Bioconductor, DADA2, R, lme4, phyloseq]

### Natural variation in age-related dopamine neuron degeneration is glutathione dependent and linked to life span. (PNAS 2024)

- DOI: 10.1073/pnas.2403450121 | PMCID: PMC11494315 | PMID: 39388265
- Evidence: This was applied to the normalized and imputed metabolomic data using the Bioconductor limma package ( 98 ).
- Full pipeline: normalisation [Bioconductor, limma] -> stage not stated [ImageJ]

### Targeting the MAtrix REgulating MOtif abolishes several hallmarks of cancer, triggering antitumor immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2404485121 | PMCID: PMC11494334 | PMID: 39382998
- Evidence: Differential analyses were performed using the DESEQ2 package from the Bioconductor framework ( 50 ).
- Full pipeline: quality control [FastQC] -> differential/statistical testing [Bioconductor] -> stage not stated [GSEA, ImageJ]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: The differential expression analysis was performed with DESeq2 R Bioconductor package (1.39.2) ( 87 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Light regulates widespread plant alternative polyadenylation through the chloroplast. (PNAS 2024)

- DOI: 10.1073/pnas.2405632121 | PMCID: PMC11348263 | PMID: 39150783
- Evidence: The DESeq method (R Bioconductor) ( 53 ) was used to analyze gene expression changes.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> stage not stated [Bioconductor]

### Polyomavirus ALTOs, but not MTs, downregulate viral early gene expression by activating the NF-κB pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2403133121 | PMCID: PMC11348336 | PMID: 39141346
- Evidence: Differential expression comparisons between relevant sample groups were performed using Bioconductor’s edgeR ( 43 ).
- Full pipeline: alignment/mapping [Clustal Omega, STAR] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [GSEA]

### The neocortical infrastructure for language involves region-specific patterns of laminar gene expression. (PNAS 2024)

- DOI: 10.1073/pnas.2401687121 | PMCID: PMC11348331 | PMID: 39133845
- Evidence: We excluded spots according to spot-wise quality control metrics using the default settings of the perCellQCMetrics and quickPerCellQC functions from the Scran v1.18.7 R Bioconductor package, which considers the log-total UMI count, log-number of detected features, and percentage of counts in specified “control” gene sets (mitochondrial genes, spike-in transcripts) ( 80 ).
- Full pipeline: quality control [Bioconductor] -> alignment/mapping [MAGMA, STAR v2.5.1b, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [ImageJ v1.53t, R]

### m&lt;sup&gt;6&lt;/sup&gt;A modification plays an integral role in mRNA stability and translation during pattern-triggered immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2411100121 | PMCID: PMC11331096 | PMID: 39116132
- Evidence: To calculate the RNA decay rate, the Bioconductor RNAdecay package was utilized to normalize the data, model mRNA decay, and compare genotype effects.
- Full pipeline: read trimming [STAR, Trim Galore] -> alignment/mapping [Bowtie2, STAR, Trim Galore] -> variant calling [Bioconductor] -> normalisation [Bioconductor, DESeq2, HTSeq]

### The DNA damage response of <i>Escherichia coli</i>, revisited: Differential gene expression after replication inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2407832121 | PMCID: PMC11228462 | PMID: 38935560
- Evidence: Differential expression analysis was conducted using the R Bioconductor package, DESeq2 1.42.0 ( 86 ) yielding the log2 fold change, P -values, and median-ratio normalized counts.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, MultiQC] -> alignment/mapping [MultiQC, STAR] -> quantification [edgeR v3.18] -> normalisation [Bioconductor, DESeq2 v1.42.0] -> differential/statistical testing [Bioconductor, DESeq2 v1.42.0] -> stage not stated [R v4.3, ggplot2 v3.5.0]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: The analysis was conducted following the Bioconductor RNA-seq workflow and differential gene expression was analyzed using the R package DESeq2 .
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Psychosocial experiences are associated with human brain mitochondrial biology. (PNAS 2024)

- DOI: 10.1073/pnas.2317673121 | PMCID: PMC11228499 | PMID: 38889126
- Evidence: R/Bioconductor (packages GenomicAlignments and GenomicRanges) was used to calculate the median sequence coverages of the autosomal chromosomes and of the mitochondrial genome.
- Full pipeline: read trimming [edgeR, limma v3.44.3] -> alignment/mapping [edgeR, limma v3.44.3] -> normalisation [edgeR, limma v3.44.3] -> differential/statistical testing [R v4.0.4] -> stage not stated [Bioconductor]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Evidence: Reads aligning to annotated mouse transcripts were counted using SummarizeOverlaps in the GenomicAlignments Bioconductor package ( 49 ), and differential expression analysis was performed using the DESeq2 package ( 50 ).
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles up-regulate and directly transfer adherence factors promoting host cell colonization. (PNAS 2024)

- DOI: 10.1073/pnas.2401159121 | PMCID: PMC11194581 | PMID: 38865261
- Version used: **3.8**
- Evidence: All subsequent analyses were carried out using the statistical computing environment R version 4.3.0 in RStudio version 1.1.456, and Bioconductor version 3.8.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [Galaxy]

### APOBEC2 safeguards skeletal muscle cell fate through binding chromatin and regulating transcription of non-muscle genes during myoblast differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2312330121 | PMCID: PMC11047093 | PMID: 38625936
- Evidence: Paired-end reads were aligned to mm10 genome using the subjunc function in the Bioconductor Rsubread package ( 66 ).
- Full pipeline: alignment/mapping [Bioconductor] -> quantification [ImageJ, R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [DESeq2, MACS2]

### NOVA1 acts as an oncogenic RNA-binding protein to regulate cholesterol homeostasis in human glioblastoma cells. (PNAS 2024)

- DOI: 10.1073/pnas.2314695121 | PMCID: PMC10927500 | PMID: 38416679
- Evidence: Reads were aligned to the hg19 build using STAR ( 42 ) and analyzed by differential analysis of raw sequencing counts using DESeq2 (Bioconductor, https://www.bioconductor.org/packages/release/bioc/html/DESeq2.html ) ( 43 ).
- Full pipeline: alignment/mapping [Bioconductor, DESeq2, STAR] -> differential/statistical testing [Bioconductor, DESeq2, STAR]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Evidence: The Bioconductor environment was used (Biobase v2.48.0) ( 53 ).
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### Cortical &lt;i&gt;miR-709&lt;/i&gt; links glutamatergic signaling to NREM sleep EEG slow waves in an activity-dependent manner. (PNAS 2024)

- DOI: 10.1073/pnas.2220532121 | PMCID: PMC10801902 | PMID: 38207077
- Evidence: Statistical analysis was performed with the R Bioconductor package limma by fitting a linear model and computing moderated t tests, comparing miRNA expression levels in the SD vs. the control group.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [Bioconductor, R, limma] -> stage not stated [WGCNA]

### BRCA1 and ELK-1 regulate neural progenitor cell fate in the optic tectum in response to visual experience in <i>Xenopus laevis</i> tadpoles. (PNAS 2024)

- DOI: 10.1073/pnas.2316542121 | PMCID: PMC10801852 | PMID: 38198524
- Evidence: We used the DE analysis package, DESeq2 (RRID:SCR_015687), and R for graphics (v3.1.2; cran.r-project.org; RRID:SCR_001905) through Bioconductor (RRID:SCR_006442).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, Cufflinks, Cytoscape, ImageJ]

### Dual-targeted ping-pong CAR T cells: Leveraging peripheral expansion to improve solid tumor immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2518996122 | PMCID: PMC12745717 | PMID: 41397127
- Evidence: GSVA results were graphed using the ggplot2 Bioconductor R package.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Bioconductor, GSVA, R, ggplot2]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: Normalization and analysis of the RNA read count matrix were performed using the Bioconductor R package DESeq2 with default settings.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: Differential expression analysis was done from filtered CPM normalized counts (CPM <1 across half of the samples) using DESeq2 ( 30 ) (Bioconductor Release: 3.14) in R version 3.4.1.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Evidence: Differential peak analysis was conducted using the Bioconductor package DiffBind.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: Counts for genes and TEs were generated using featureCounts v2 and normalized for sequencing depth using the TMM method implemented in the limma package of Bioconductor.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Evidence: To identify a universal sleep deprivation response in gene expression of LSD and MSD animals, raw reads from experiment 1 and experiment 2 were batch corrected using ComBat-Seq function in the Bioconductor package sva version 3.42.0 ( 22 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles suppress IFNε-mediated responses driven by its intracellular bacterial symbiont &lt;i&gt;Mycoplasma hominis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2508297122 | PMCID: PMC12232435 | PMID: 40560611
- Version used: **3.8**
- Evidence: All subsequent analyses were carried out using the statistical computing environment R version 4.3.0 in RStudio version 1.1.456, and Bioconductor version 3.8.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [GSEA]

### Transcriptomic and proteomic ramifications of segmental amplification in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2422424122 | PMCID: PMC12107188 | PMID: 40372434
- Evidence: Differential expression analysis was performed in R v4.3.1/RStudio (Posit team; Boston, MA) with the following Bioconductor/R packages: edgeR ( 66 , 67 ), limma ( 68 ), glimma, gplots, RcolorBrewer, and Nonnegative Matrix Factorization.
- Full pipeline: differential/statistical testing [Bioconductor, R v4.3, edgeR, limma]

### Red-light signaling pathway activates desert cyanobacteria to prepare for desiccation tolerance. (PNAS 2025)

- DOI: 10.1073/pnas.2502034122 | PMCID: PMC11962455 | PMID: 40112114
- Evidence: Genes with similar expression profiles were clustered by FCM and analyzed using the Bioconductor Mfuzz package in R.
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [edgeR v3.20.7] -> dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [edgeR v3.20.7] -> stage not stated [AlphaFold, PyMOL]

### Genetic ablation of the TET family in retinal progenitor cells impairs photoreceptor development and leads to blindness. (PNAS 2025)

- DOI: 10.1073/pnas.2420091122 | PMCID: PMC11912455 | PMID: 40053367
- Evidence: By combining the capabilities of methylKit and annotatr Bioconductor packages, we formed a list of genes in which all promoters and first exons were hypermethylated in the retinas of Chx10-TET animals; methylation of at least one promoter or the first exon of these genes should be low in the retinas of TET mice ( Dataset S2 ) ( 22 , 23 ).
- Full pipeline: visualisation [Bismark] -> stage not stated [Bioconductor]

### The RNA-binding protein RBPMS inhibits smooth muscle cell-driven vascular remodeling in atherosclerosis and vascular injury. (PNAS 2025)

- DOI: 10.1073/pnas.2415933122 | PMCID: PMC11892686 | PMID: 39999164
- Evidence: GraphPad Prism 6 and Bioconductor were used for all statistical testing.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Bioconductor]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Evidence: Filtering out lowly expressed genes (13,613 genes were kept), normalization and differential expression analysis were performed with the R/Bioconductor package edgeR v.3.42.4 ( 66 ), and statistical significance was assessed with a general linear model, negative binomial distribution, and quasi-likelihood F test.
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Targeting EPHB2/ABL1 restores antitumor immunity in preclinical models of ependymoma. (PNAS 2025)

- DOI: 10.1073/pnas.2319474122 | PMCID: PMC11789170 | PMID: 39841145
- Evidence: DEGs was performed by R Bioconductor package DESeq2 with a P -value of 0.01 and fold-change of 2 as the cutoff.
- Full pipeline: quantification [HTSeq] -> dimensionality reduction/clustering [R, STRING db, pheatmap] -> stage not stated [Bioconductor, DESeq2, Seurat]

### Impact of sex chromosomes and gonad type in stress susceptibility in corticostriatal brain regions. (PNAS 2026)

- DOI: 10.1073/pnas.2531920123 | PMCID: PMC13229181 | PMID: 42189975
- Evidence: The analysis was produced in R using the RRHO2 package, which is publicly available at Bioconductor ( 75 ).
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.10.3, Metascape] -> stage not stated [Bioconductor, WGCNA]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Differential gene expression was performed using the R Bioconductor package limma ( 49 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Evidence: Read counts were normalized across all samples using the counts function in DESeq2 package v.1.30.1 from Bioconductor ( 70 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: Naïve brain mouse tumors, using the R/Bioconductor package DESeq2 ( 45 ) (v 1.44.0and a statistical cutoff of FDR < 0.05 and FC > 1.5 was applied to obtain differentially regulated genes.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Antagonism of RNA silencing in the yellow fever mosquito, &lt;i&gt;Aedes aegypti&lt;/i&gt;, by the nsP2 protein of the prototype alphavirus. (PNAS 2026)

- DOI: 10.1073/pnas.2521417123 | PMCID: PMC12913014 | PMID: 41662525
- Evidence: For differential expression analysis between replicate datasets, we used the edgeR Bioconductor package ( https://bioconductor.org/packages/release/bioc/html/edgeR.html ).
- Full pipeline: differential/statistical testing [Bioconductor, edgeR]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Evidence: The Bioconductor R package DESeq2 (v.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: For peak calling, we used the R/Bioconductor DEWSeq package to identify significantly enriched sliding windows in OAS1 immunoprecipitated samples over the corresponding size-matched input control samples (adjusted P value < 0.01, log2-fold change > 2).
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Silencing mitochondrial gene expression in living cells. (Science 2025)

- DOI: 10.1126/science.adr3498 | PMCID: PMC7618265 | PMID: 40403134
- Evidence: The downstream analysis was performed in RStudio (R version 4.3.0) using packages from the Bioconductor repository ( 42 , 43 ) and the Tidyverse suite.
- Full pipeline: quantification [ImageJ v1.47] -> normalisation [limma v3.56.2] -> dimensionality reduction/clustering [clusterProfiler v4.8.3, limma v3.56.2] -> differential/statistical testing [DESeq2 v1.40.2, ImageJ v1.47, limma v3.56.2] -> stage not stated [Bioconductor, R v4.3.0, ggplot2]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: Enrichment analysis was run using the Bioconductor annotation data package (org.Hs.eg.db v3.15.0).
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

