# ggplot2

- **Category:** general
- **Papers in survey:** 587
- **Journals:** PNAS (290), Nature (236), Cell (46), Science (12), Lancet (2), NEJM (1)
- **Years:** 2021 (57), 2022 (96), 2023 (99), 2024 (121), 2025 (160), 2026 (54)
- **Versions named:** 3.3.5 (23), 3.5.1 (22), 3.4.2 (20), 3.3.3 (17), 3.4.4 (14), 3.3.6 (14), 3.3.2 (14), 3.2.1 (9), 3.5.0 (7), 3.4.3 (6)
- **Pipeline stages it appears in:** visualisation (267), differential/statistical testing (78), dimensionality reduction/clustering (39), normalisation (14), quantification (12), alignment/mapping (5), variant calling (4), structure determination (2), machine learning (1), simulation/modelling (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **3.3.2**
- Evidence: ...b/packages/leiden/index.html R package scran version 1.14.6 Lun et al., 2016 https://bioconductor.org/packages/release/bioc/html/scran.html R package ggplot2 version 3.3.2 Wickham, 2016 https://cran.r-project.org/web/packages/ggplot2/index.html R package dplyr version 1.0.2 Wickham et al., 2020 https://cran.r-project.org/web/packages/dplyr/index.html R package uwot version 0.1.8 Melville, 2020 htt...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### A defective viral genome strategy elicits broad protective immunity against respiratory viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.023 | PMCID: PMC8598942 | PMID: 34852237
- Evidence: The Figures were plot by R, ggplot2 package.
- Full pipeline: differential/statistical testing [Cufflinks, TopHat] -> visualisation [ggplot2] -> stage not stated [ImageJ]

### Microglia jointly degrade fibrillar alpha-synuclein cargo by distribution through tunneling nanotubes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.007 | PMCID: PMC8527836 | PMID: 34555357
- Evidence: Henneberger N/A Software and Algorithms CellProfiler Broad Institute of Harvard and MIT v3.1.8 FACSDIVA™ software Becton Dickinson N/A Fiji ImageJ Wayne Rusband v2.0.0-rc-69/1.52n FlowJo FlowJo, LLC v3.05470 ggplot2 CRAN v3.2.1 Graph Pad Prism GraphPad Software Inc. v7.0e and v8.0 Image Studio, v5.2 LI-COR Biosciences N/A Imaris Bitplane by Oxford Instruments plc v9.2.1 NIS-elements Nikon AR 4.20....
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> dimensionality reduction/clustering [Cytoscape] -> stage not stated [CellProfiler, Fiji, ImageJ, ggplot2, tidyverse]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Version used: **3.3.2**
- Evidence: ...30.0 Bioconductor https://bioconductor.org/packages/DESeq2/ R package – Circlize v0.4.11 CRAN https://CRAN.R-project.org/package=circlize R package – ggplot2 v3.3.2 CRAN https://CRAN.R-project.org/package=ggplot2 R package – ComplexHeatmap v2.7.3 Bioconductor https://bioconductor.org/packages/ComplexHeatmap/ R package – fgsea v1.16.0 Bioconductor https://bioconductor.org/packages/fgsea/ Python Pro...
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Fab-dimerized glycan-reactive antibodies are a structural category of natural antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.042 | PMCID: PMC8135257 | PMID: 34019795
- Evidence: Graphs and plots were generated using the Seurat and ggplot2 R packages and Graphpad Prism version 8.
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, R, Seurat, UMAP] -> stage not stated [PyMOL, RELION, UCSF Chimera, ggplot2]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Evidence: ... Subsampler This paper https://github.com/andersonbrito/subsampler baltic 0.1.5 https://github.com/evogytis/baltic https://github.com/evogytis/baltic ggplot2 CRAN Wickham, 2016 choroplethr CRAN Lamstein et al., 2020 maps CRAN Becker et al., 2018 anytime CRAN https://cran.r-project.org/web/packages/anytime/index.html forcats CRAN https://cran.r-project.org/web/packages/forcats/index.html scales CRA...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### Soluble ACE2-mediated cell entry of SARS-CoV-2 via interaction with proteins related to the renin-angiotensin system. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.053 | PMCID: PMC7923941 | PMID: 33713620
- Evidence: The resulting datasets were subjected to clustering analyses, including principal components analysis (PCA), volcano plot, and heatmap hierarchical clustering analysis, using the stat function in R, ggplot2 function in R, and Complex Heatmap, respectively ( Gu et al., 2016 ; Ito and Murphy, 2013 ).
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> stage not stated [Bowtie2, Cutadapt, DESeq2, HTSeq]

### Osteoclasts recycle via osteomorphs during RANKL-stimulated bone resorption. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.002 | PMCID: PMC7938889 | PMID: 33636130
- Evidence: ...http://bioconductor.org/packages/release/bioc/html/ggbio.html ; RRID: SCR_003313 ggfortify ( Tang et al., 2016 ) https://github.com/sinhrks/ggfortify ggplot2 ( Wickham, 2016 ) https://cran.r-project.org/web/packages/ggplot2/index.html ; RRID: SCR_014601 Imaris Bitplane https://imaris.oxinst.com/packages ; RRID: SCR_007370 NMF ( Gaujoux and Seoighe, 2010 ) https://CRAN.R-project.org/package=NMF MAS...
- Full pipeline: alignment/mapping [STAR v2.4.1] -> normalisation [STAR v2.4.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [RSEM, STAR v2.4.1] -> stage not stated [Cutadapt, ImageJ, MAGMA, ggplot2]

### Maturation and persistence of the anti-SARS-CoV-2 memory B cell response. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.050 | PMCID: PMC7994111 | PMID: 33571429
- Version used: **3.3.2**
- Evidence: Graphics were obtained using the ggplot2 v3.3.2 and circlize v0.4.10 packages.
- Full pipeline: quality control [Seurat v3.2.2] -> alignment/mapping [R v4.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, igraph v1.2.6] -> stage not stated [Docker, ggplot2 v3.3.2]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **3.3.2**
- Evidence: ...age clusterProfiler version 3.16.1 R Bioconductor; Yu et al., 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html R package ggplot2 version 3.3.2 R CRAN https://cran.r-project.org/web/packages/ggplot2/index.html R package pheatmap version 1.0.12 R CRAN https://cran.r-project.org/web/packages/pheatmap/index.html R package ggraph version 2.0.3 R CRAN https://cran.r-project....
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Evidence: ...t al., 2019 https://bioconductor.org/packages/SingleR DoubletFinder v2.0.3 McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder ggplot2 Wickham, 2016 https://ggplot2.tidyverse.org Plotly Sievert, 2020 https://plotly-r.com Analysis scripts This paper https://github.com/BosingerLab/RM_Baricitinib_manuscript Docker v 1.12.6 Docker https://www.docker.com/ RStudio v1.1.453 RStudio...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Genome-wide data from medieval German Jews show that the Ashkenazi founder event pre-dated the 14<sup>th</sup> century. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.002 | PMCID: PMC9793425 | PMID: 36455558
- Evidence: Due to the large MAJ sample size, we plotted the positions of these individuals as a 2-dimensional kernel density plot ( Figure S2A ) using the function stat_density_2days() from the package ggplot2 in R .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BCFtools, BWA v0.7.15] -> quantification [SAMtools] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [BEAST v2.6.6] -> visualisation [ggplot2] -> stage not stated [ADMIXTURE, R]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **3.3.4**
- Evidence: Packages used in analysis include phyloseq 1.34.0, ggplot2 3.3.4, ggbeeswarm 0.6.0, ggrepel 0.9.1.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **3.3.3**
- Evidence: Graphics were generated using the ggplot2 3.3.3 ( Wickham, 2009 ), ComplexHeatmap 2.4.3 ( Gu et al., 2016 ), pheatmap 1.0.12 ( Kolde, 2019 ), igraph 1.2.6 ( Csardi and Nepusz, 2006 ), RCy3 2.8.1 ( Gustavsen et al., 2019 ), stringr 1.4.0 ( Wickham, 2019 ), dplyr 1.0.6 ( Wickham et al., 2020 ), and RColorBrewer 1.1-2 ( Neuwirth, 2014 ) R package.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Non-canonical odor coding in the mosquito. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.024 | PMCID: PMC9480278 | PMID: 35985288
- Evidence: (2015) https://satijalab.org/seurat/ ggplot2 Wickham (2016) https://ggplot2.tidyverse.org/ R R Core Team (2021) https://www.r-project.org/ R studio RStudio Team, 2020 https://www.rstudio.com/ FIJI Schindelin et al.
- Full pipeline: normalisation [ComplexHeatmap] -> stage not stated [ImageJ, R, Seurat, ggplot2, scDblFinder, tidyverse]

### Neutralizing immunity in vaccine breakthrough infections from the SARS-CoV-2 Omicron and Delta variants. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.019 | PMCID: PMC8930394 | PMID: 35429436
- Evidence: Plots were generated using ggplot2 package (version 3.3.5) in R and seaborn package (version 0.11.0) in Python.
- Full pipeline: read trimming [BLAST] -> quantification [Python v3.7.10] -> differential/statistical testing [Python v3.7.10] -> visualisation [Python v3.7.10] -> stage not stated [Pangolin, R v4.0, ggplot2, seaborn]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: (2011) https://software.broadinstitute.org/software/igv/ R version 4.0.5 ggplot2 package The R Foundation https://cran.r-project.org/web/packages/ggplot2/index.html R version 4.0.5 Seurat package The R Foundation https://cran.r-project.org/web/packages/Seurat/index.html Cellranger 5.0.1 10X Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/release-notes...
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.018 | PMCID: PMC8786601 | PMID: 35148837
- Evidence: (2021) DOI: 10.1038/s41586-021-03791-x Software and algorithms R version 4.0.5 base packages The R Foundation https://www.rstudio.com/products/rstudio/download/ R version 4.0.5 ggplot2 package The R Foundation https://cran.r-project.org/web/packages/ggplot2/index.html QuPath version 0.2.3 Bankhead et al.
- Full pipeline: dimensionality reduction/clustering [NumPy v1.19.1, scikit-learn v1.0] -> visualisation [SciPy v1.6.2] -> stage not stated [Matplotlib v3.3.2, QuPath v0.2.3, R v4.0.5, ggplot2, seaborn v0.11.2]

### Germinal center responses to SARS-CoV-2 mRNA vaccines in healthy and immunocompromised individuals. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.027 | PMCID: PMC8808747 | PMID: 35202565
- Evidence: All statistical analysis was performed in R version 4.0.3, using the following packages: ggplot2, Semblance, multicross, crossmatchtest, dplyr, randtests, ggpubr, and merTools.
- Full pipeline: differential/statistical testing [ggplot2, ggpubr, tidyverse] -> stage not stated [R v4.0.3]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: These were drawn using the stat_ellipse method from the R package ggplot2, using default parameters.
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: ...ater.html BioMart N/A https://www.ensembl.org/biomart/martview/3e2c65a5e3f783f8c9e5d648e4b64126 pheatmap R package N/A https://rdrr.io/cran/pheatmap/ ggplot2 ( Wickham 2016 ) https://ggplot2.tidyverse.org Scanpy ( Wolf et al., 2018 ) https://scanpy.readthedocs.io/en/stable/ PyTorch N/A https://pytorch.org TotalVI ( Gayoso et al., 2021 ) https://docs.scvi-tools.org/en/stable/user_guide/models/total...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: Data visualization All the graphical visualization of the data was performed in R with the ggplot2 package with the exception of the heatmaps, which were displayed using the pheatmap library Box plots: Box plots are calculated in the style of Tukey, shortly the center of the box represents the median of the values, the hinges the 25th and 75th percentile and the whiskers are extended no further th...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### SARS-CoV-2 mRNA vaccination elicits a robust and persistent T follicular helper cell response in humans. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.026 | PMCID: PMC8695127 | PMID: 35026152
- Evidence: 0.9.2 https://gephi.org ggplot2 R package v.
- Full pipeline: stage not stated [R, data.table, ggplot2, igraph]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: The R package ggplot2 was used to generate and render each plot (refer to KRT for all software).
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### LRRC37B is a human modifier of voltage-gated sodium channels and axon excitability in cortical neurons. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.028 | PMCID: PMC10754148 | PMID: 38134874
- Evidence: CN-dotplots generated using the R package ggplot2.
- Full pipeline: stage not stated [ImageJ, R, Scanpy, ggplot2]

### The proteomic landscape of synaptic diversity across brain regions and cell types. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.028 | PMCID: PMC10686415 | PMID: 37918396
- Evidence: 90 ggplot2 was used for visualization.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Cytoscape, R v4.2, STRING db, WGCNA]

### Dispersal patterns and influence of air travel during the global expansion of SARS-CoV-2 variants of concern. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.001 | PMCID: PMC10247138 | PMID: 37413988
- Evidence: 43 CRAN ggplot2 R package Wickham 44 CRAN MASS R package N/A https://www.stats.ox.ac.uk/pub/MASS4/ DescTools R package Signorell 45 N/A Resource availability Lead contact Further information and requests for data and resources should be directed to and will be fulfilled by the Lead Contact, Houriiyah Tegally ( houriiyah.tegally@gmail.com ).
- Full pipeline: stage not stated [R, TreeTime, ggplot2]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Evidence: 92 https://bioconductor.org/packages/release/bioc/html/GenomicFeatures.html ggplot2_3.2.1 N/A https://github.com/tidyverse/ggplot2 dplyr_1.0.8 N/A https://github.com/tidyverse/dplyr seqtk 1.2-r94 N/A https://github.com/lh3/seqtk Tama N/A https://github.com/GenomeRIK/tama Sierra Patrick et al.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### Apoptotic cell fragments locally activate tingible body macrophages in the germinal center. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.004 | PMCID: PMC7614509 | PMID: 36868219
- Evidence: Simulations were run for 75 simulated minutes and fragment count data and position data for calibration were exported as.csv and plotted in ggplot2 in R v4.1.2 using bespoke scripts.
- Full pipeline: simulation/modelling [ggplot2] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, GSEA v4.2.3, ImageJ, Python v3.9, QuPath, R v4.1, Seurat, edgeR]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: 110 The odd ratios were then plotted with ggplot2 ( cran.r-project.org/web/packages/ggplot2/index.html ) 107 with the odds ratio displayed on the x-axis, the dot size reflecting the gene count (number of genes present in the top 5% of PC1 contributing genes) and the dot color reflecting the p-value.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: 83 https://doi.org/10.18129/B9.bioc.DEP ggplot2 Wickham et al.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### CSF proteomics identifies early changes in autosomal dominant Alzheimer's disease. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.049 | PMCID: PMC11531390 | PMID: 39332414
- Evidence: ADDITIONAL RESOURCES Data visualization Data visualization plots were mainly generated by ggplot2 R package version 3.4.2.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.0] -> simulation/modelling [GSVA] -> visualisation [ggplot2] -> stage not stated [R v4.1.3, WGCNA]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Evidence: 107 Quantification and statistical analysis Summary of data are presented as mean ±/+ standard error of mean (SEM) using PRISM v9 or “ggplot2” package in R.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 47 https://ggplot2.tidyverse.org GseaPreranked Subramanian et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Neurotransmitter classification from electron microscopy images at synaptic sites in Drosophila melanogaster. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.016 | PMCID: PMC11106717 | PMID: 38729112
- Evidence: ...ctions This paper https://doi.org/10.5281/zenodo.10593546 Software and algorithms R R Core Team 130 RRID SCR 001905 knitr (R) Xie 131 RRID SCR 018533 ggplot2 (R) Wickham 132 RRID SCR 014601 tidyverse (R) Wickham et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, ggplot2, tidyverse]

### Global, site-resolved analysis of ubiquitylation occupancy and turnover rate reveals systems properties. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.024 | PMCID: PMC11136510 | PMID: 38626770
- Version used: **3.3.5**
- Evidence: ...ject.org/ R Studio v1.4.1106 N/A https://rstudio.com/ R package: dplyr v1.0.5 N/A https://cran.r-project.org/web/packages/dplyr/index.html R package: ggplot2 v3.3.5 N/A http://ggplot2.org/ R package: GGally v2.1.2 N/A https://cran.r-project.org/web/packages/GGally/index.html R package: ComplexHeatmap v2.6.2 Gu et al.
- Full pipeline: stage not stated [AlphaFold, ComplexHeatmap v2.6.2, PyMOL v2.5.0, Python v3.7.1, R, ggplot2 v3.3.5, tidyverse v1.0.5]

### Time-series reconstruction of the molecular architecture of human centriole assembly. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.025 | PMCID: PMC11060037 | PMID: 38604175
- Evidence: Determination of regression models As the raw data produce uneven point distributions that render the cluterisation difficult, we have softened the raw data with a smoother using the R environment for statistical computing, 91 exploratory plots made using the ggplot2 graphics system.
- Full pipeline: differential/statistical testing [R, ggplot2] -> stage not stated [ImageJ, UCSF Chimera]

### Microglia maintain structural integrity during fetal brain morphogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.012 | PMCID: PMC10869139 | PMID: 38309258
- Evidence: ...8931 R package: Paletteer 1.5.0 N/A https://CRAN.R-project.org/package=paletteer R package: Ggplot2 3.4.3 N/A https://cran.r-project.org/web/packages/ggplot2/index.html ; RRID: SCR_014601 R package: Sctransform 0.3.5 N/A https://github.com/satijalab/sctransform ; RRID: SCR_022146 R package: GlmGamPoi 1.10.2 N/A https://bioconductor.org/packages/glmGamPoi/ Bowtie 2 N/A http://bowtie-bio.sourceforge...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Bowtie2, ImageJ, Metascape v3.5.20230501, R, Seurat v4.3.0.1, ggplot2, tidyverse]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Evidence: 102 The absolute cell-type enrichment scores are presented as dot plots generated with library ggplot2 ( https://cran.r-project.org/web/packages/ggplot2/index.html ).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Evidence: These structures were rendered and visualized using the r3dmol package while the plots were generated using ggplot2 package in R.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Using the R packages ggpubr and ggplot2, a scatter plot was generated to compare the average expression of each protein across the different experiments.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Design principles of cell-state-specific enhancers in hematopoiesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.017 | PMCID: PMC12173716 | PMID: 40345201
- Evidence: For the plots in Figures 3 B, 3C, and 3F we then summed this quantity over all the sites placed in the GRE to obtain a sum of motif scores and used smoothened conditional means (geom_smooth function from ggplot2) for plotting.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ArchR] -> machine learning [TensorFlow] -> stage not stated [R, ggplot2, kallisto, pheatmap]

### Cervicovaginal microbiome and natural history of Chlamydia trachomatis in adolescents and young women. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.011 | PMCID: PMC12035847 | PMID: 39818212
- Evidence: 49 Alluvial plots, representing mBV state transitions between t −1 and t 0 visits were constructed using the ggplot2 package and the geom_alluvium function.
- Full pipeline: quantification [DADA2] -> dimensionality reduction/clustering [DADA2] -> differential/statistical testing [DADA2, R, vegan] -> machine learning [DADA2] -> stage not stated [ggplot2, phyloseq]

### Phages communicate across species to shape microbial ecosystems. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.004 | PMCID: PMC13220667 | PMID: 41923642
- Evidence: ...2 crystal structure This paper PDB: 9FKU Oligonucleotides Please see Table S5 N/A Software and algorithms R R Core Team 31 https://www.R-project.org/ ggplot2 Wickham 32 https://ggplot2.tidyverse.org ggpubr Kassambara.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, IQ-TREE, R, ggplot2, ggpubr, tidyverse]

### Citrate clearance is a major function of aconitase 2 in the canonical TCA cycle. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.028 | PMCID: PMC13045649 | PMID: 41763199
- Version used: **3.5.2**
- Evidence: GSEA dot plots were graphed using ggplot2 (version 3.5.2) in R.
- Full pipeline: differential/statistical testing [DESeq2 v1.46.0] -> stage not stated [GSEA, R v4.3.2, featureCounts, fgsea, ggplot2 v3.5.2]

### Molecular features of human pathological tau distinguish tauopathy-associated dementias. (Cell 2026)

- DOI: 10.1016/j.cell.2025.12.036 | PMCID: PMC13075643 | PMID: 41616780
- Version used: **3.3.5**
- Evidence: Analyses were performed and figures were created in R (v4.1.0) using RStudio (v1.4.1717) with the packages R.utils (v2.11.0), stringr (v1.4.0), GetoptLong (v1.0.5), reshape2 (v1.4.4), circlize (v0.4.13), ComplexHeatmap (v2.11.1), dendsort (v0.3.4), dendextend (v1.15.2), ggplot2 (v3.3.5), ggpubr (v0.4.0), ggdendro (v0.1.22), ggpmisc (v0.4.5), scales (v1.1.1), and gridExtra (v2.3).
- Full pipeline: visualisation [ComplexHeatmap v2.11.1, ggplot2 v3.3.5, ggpubr v0.4.0] -> stage not stated [R v4.1.0]

### Elective surgery system strengthening: development, measurement, and validation of the surgical preparedness index across 1632 hospitals in 119 countries. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)01846-3 | PMCID: PMC9621702 | PMID: 36328042
- Evidence: Analyses were done with R Studio (version 4.1.1) packages: tidyverse, finalfit, psych, and ggplot2.
- Full pipeline: stage not stated [Canu, ggplot2, tidyverse]

### Past SARS-CoV-2 infection protection against re-infection: a systematic review and meta-analysis. (Lancet 2023)

- DOI: 10.1016/s0140-6736(22)02465-5 | PMCID: PMC9998097 | PMID: 36930674
- Evidence: 27 Tidyverse, data.table, stringi, ggplot2, forestplot, formattable, crosswalk002, metafor, and mrbrt002 packages were used.
- Full pipeline: stage not stated [R v1.4.1103, data.table, ggplot2, metafor]

### Pan-Sarbecovirus Neutralizing Antibodies in BNT162b2-Immunized SARS-CoV-1 Survivors. (NEJM 2021)

- DOI: 10.1056/nejmoa2108453 | PMCID: PMC8422514 | PMID: 34407341
- Evidence: Box plots and scatterplots were generated with the ggplot2 package in R software, version 3.3.2.
- Full pipeline: stage not stated [ggplot2]

### Footprint evidence of early hominin locomotor diversity at Laetoli, Tanzania. (Nature 2021)

- DOI: 10.1038/s41586-021-04187-7 | PMCID: PMC8674131 | PMID: 34853470
- Evidence: Box and whisker plots and bivariate graphs (using ggplot2 54 ) were generated using R (v.
- Full pipeline: quantification [ImageJ v1.47] -> stage not stated [R v4.0.3, ggplot2, tidyverse]

### Late Quaternary dynamics of Arctic biota from ancient environmental genomics. (Nature 2021)

- DOI: 10.1038/s41586-021-04016-x | PMCID: PMC8636272 | PMID: 34671161
- Evidence: 1b ) via the Loess Smooth (span = 4) function in the R package ggplot2 (ref.
- Full pipeline: stage not stated [ComplexHeatmap, R, ggplot2]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Version used: **3.2.1**
- Evidence: Analysis was performed in RStudio using R version 3.5.3, R packages: Seurat 3.1.1, ggplot2 3.2.1 and scrattch.hicat 0.0.22.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **3.3.2**
- Evidence: Correlations between human and marmoset cell subclasses were visualized as boxplots for TFBS activities, expression of transcription factors, and variable genes using the R package ggplot2 v3.3.2 (ref.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Genome of a middle Holocene hunter-gatherer from Wallacea. (Nature 2021)

- DOI: 10.1038/s41586-021-03823-6 | PMCID: PMC8387238 | PMID: 34433944
- Version used: **3.3.3**
- Evidence: The results of f 3 -statistics were plotted in the geographical location of the test group using ggplot2 v.3.3.3 in RStudio v.1.2.1335.
- Full pipeline: read trimming [BWA, SAMtools v1.3] -> alignment/mapping [BWA] -> variant calling [SAMtools v1.3] -> differential/statistical testing [ggplot2 v3.3.3] -> visualisation [ggplot2 v3.3.3] -> stage not stated [PLINK v1.9, QGIS]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: Most of the statistical analysis and data visualization were performed in R using the packages tidyverse, ggplot2, purrr, tibble, dplyr, tidyr, stringr, readr, forcats, scales, grid, reshape2, Rtsne, ggfortify, factoextra, ggpubr, ggforce, ggrepel, RColorBrewer and pheatmap.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: Plots were generated with the R package ‘ggplot2’ (v3.2.1) 65 SciPy (v.1.4.1) 66 and pandas (v1.01) 67 Acoustic Cell Tagmentation Procedure FACS sorted 384 well plates were spun at 1500xg for > 4min.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Lipid signalling enforces functional specialization of T<sub>reg</sub> cells in tumours. (Nature 2021)

- DOI: 10.1038/s41586-021-03235-6 | PMCID: PMC8168716 | PMID: 33627871
- Version used: **2.2.1**
- Evidence: All the plots were generated using R package ggplot2 v.2.2.1.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, limma v3.34.9] -> visualisation [UMAP] -> stage not stated [GSEA, Seurat, ggplot2 v2.2.1]

### Loop extrusion as a mechanism for formation of DNA damage repair foci. (Nature 2021)

- DOI: 10.1038/s41586-021-03193-z | PMCID: PMC7116834 | PMID: 33597753
- Evidence: APA heatmaps were reprocessed using ggplot2 in order to display counts at the same color scale between - DSB and +DSB conditions.
- Full pipeline: read trimming [R, SAMtools] -> alignment/mapping [R, SAMtools] -> normalisation [Bioconductor, deepTools] -> differential/statistical testing [deepTools] -> visualisation [Bioconductor] -> stage not stated [MACS2, ggplot2]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Evidence: 61 ) and plotted as a heatmap using ggplot2 ( Fig.4d ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### SARS-CoV-2 infection is effectively treated and prevented by EIDD-2801. (Nature 2021)

- DOI: 10.1038/s41586-021-03312-w | PMCID: PMC7979515 | PMID: 33561864
- Version used: **3.3.1**
- Evidence: Graphs and summary tables were built in R using ggplot; gene set enrichment was performed using GSEA and GO analysis (tidyverse 1.3.0; PCATools 1.2.0; Sqldf 0.4–11; na.tools 0.3.1; ggbiplot 0.55; ggplot2 3.3.1; dplyr 0.8.4).
- Full pipeline: alignment/mapping [STAR v2.7.5a] -> quantification [STAR v2.7.5a] -> normalisation [DESeq2, R v3.6.3] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [GSEA, ImageJ, ggplot2 v3.3.1, tidyverse v1.3.0]

### Platypus and echidna genomes reveal mammalian biology and evolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03039-0 | PMCID: PMC8081666 | PMID: 33408411
- Version used: **3.2.1**
- Evidence: The normalized sex chromosomes submatrix was extracted for quantification and plotting with ggplot2 (v.3.2.1).
- Full pipeline: alignment/mapping [BWA, HISAT2, minimap2 v2.13] -> quantification [ggplot2 v3.2.1] -> normalisation [ggplot2 v3.2.1] -> stage not stated [ImageJ v2.0.0, RepeatMasker v4.0.6]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **3.3.1**
- Evidence: Visualization: Plotting was performed in figures 1 , 2 , 3 , extended data figures 1 , 2 , and 3 using ggplot2 version 3.3.1 unless otherwise noted.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Defining HPV-specific B cell responses in patients with head and neck cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-2931-3 | PMCID: PMC9462833 | PMID: 33208941
- Evidence: Data were visualised with ggplot2 48 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [R, Seurat v3.1.4]

### Global hotspots of salt marsh change and carbon emissions. (Nature 2022)

- DOI: 10.1038/s41586-022-05355-z | PMCID: PMC9771810 | PMID: 36450979
- Evidence: Maps generated using R package ggplot2 and cowplot.
- Full pipeline: stage not stated [Python v3.8.10, QGIS v3.12.263, R v3.6, ggplot2, tidyverse]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Evidence: Raw data were plotted using ggplot2 in R (v.3.6.0) 48 , 49 .
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Version used: **3.3.3**
- Evidence: We performed the multidimensional analyses in the R development environment (version 3.6.3), equipped with the following packages: tidyverse (version 1.3.0), RColorBrewer (version 1.1.2), ggplot2 (version 3.3.3), ggrepel (version 0.9.1) and stats (version 3.6.3).
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Dysregulated naive B cells and de novo autoreactivity in severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05273-0 | PMCID: PMC9630115 | PMID: 36044993
- Evidence: Custom plotting, such as that for mutation frequency violin plots, was performed using the ggplot2 library for base analysis, followed by postprocessing in Adobe Illustrator.
- Full pipeline: normalisation [pheatmap] -> stage not stated [Docker, R v3.6.2, ggplot2]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: Plots were generated using Scanpy (in Python for dot plots and velocity) and Seurat (in R for UMAP plots), as well ggplot2 for the remainder of the plots (in R for bar plots and proportion scatter plots).
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: All descriptive statistics plots (with the exception of those including phylogenetic trees, which were constructed with ITOL 63 ) were done in R, particularly with the ggplot2 package 64 .
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Version used: **3.2.1**
- Evidence: We analysed the downstream data using R (v.3.5.0), plots generated using the R package ggplot2 (v.3.2.1).
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Evidence: The figure was originally created using sf and ggplot2 R packages based on Global Map Japan version 2.1 Vector data (Geospatial Information Authority of Japan).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **3.3.0**
- Evidence: The box plots were plotted in R (v.4.0.0–v.4.1.2) using ggplot2 (v.3.3.0–v.3.3.5) and defined as follows: the bottom and top hinges correspond to the first and third quartiles (the 25th and 75th percentiles), the top whisker extends from the hinge to the largest value no further than 1.5 × IQR from the hinge (where the IQR is the interquartile range, or distance between the first and third quartil...
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### BA.2.12.1, BA.4 and BA.5 escape antibodies elicited by Omicron infection. (Nature 2022)

- DOI: 10.1038/s41586-022-04980-y | PMCID: PMC9385493 | PMID: 35714668
- Version used: **3.3.3**
- Evidence: All t -SNE plots were generated by R package ggplot2 (v3.3.3).
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.20, RELION v3.1, UCSF Chimera v1.16] -> visualisation [ChimeraX v1.3, R, Seurat] -> stage not stated [Pangolin, ggplot2 v3.3.3, scikit-learn]

### Signatures of copy number alterations in human cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-04738-6 | PMCID: PMC9242861 | PMID: 35705804
- Evidence: Plotting was performed with base R or with packages ggplot2, ggrepel, RColorBrewer, circlize, ComplexHeatmap, colorspace, seriation, dendextend, beanplot and corrplot.
- Full pipeline: normalisation [RSEM] -> stage not stated [Beagle v5.1, ComplexHeatmap, R, ggplot2, survival (R), tidyverse]

### Potentiating adoptive cell therapy using synthetic IL-9 receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04801-2 | PMCID: PMC9283313 | PMID: 35676488
- Evidence: 59 ) R packages, specifically on the TFactS annotated gene set 60 , and visualized using the ggplot2 R package.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> quantification [HTSeq] -> normalisation [pheatmap] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [R, fgsea]

### MCM complexes are barriers that restrict cohesin-mediated loop extrusion. (Nature 2022)

- DOI: 10.1038/s41586-022-04730-0 | PMCID: PMC9159944 | PMID: 35585235
- Evidence: All plots were compiled with ggplot2 in R.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R] -> stage not stated [Fiji, ImageJ, NumPy, Python, SciPy, ggplot2]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Evidence: All remaining plots were drawn using ggplot2.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### Ostrich eggshell beads reveal 50,000-year-old social network in Africa. (Nature 2022)

- DOI: 10.1038/s41586-021-04227-2 | PMCID: PMC8755535 | PMID: 34931044
- Evidence: All PCA figures were made using ‘ggplot2’ packages 53 .
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [R v4.0.1] -> visualisation [ggplot2] -> stage not stated [ImageJ]

### Omicron escapes the majority of existing SARS-CoV-2 neutralizing antibodies. (Nature 2022)

- DOI: 10.1038/s41586-021-04385-3 | PMCID: PMC8866119 | PMID: 35016194
- Version used: **3.3.3**
- Evidence: Two-dimensional t -SNE plots are generated by ggplot2 (v.3.3.3), and heat maps are generated by the ComplexHeatmap package (v.2.6.2).
- Full pipeline: normalisation [MACS2, R] -> dimensionality reduction/clustering [ComplexHeatmap, R, ggplot2 v3.3.3] -> stage not stated [Python]

### Indigenous Australian genomes show deep structure and rich novel variation. (Nature 2023)

- DOI: 10.1038/s41586-023-06831-w | PMCID: PMC10733150 | PMID: 38093005
- Evidence: Maps Maps were obtained from Google Maps using the ‘get_googlemap’ function of the ‘ggmap’ package in R 80 , and points were superimposed using ggplot2 (ref.
- Full pipeline: variant calling [GATK v3.8] -> normalisation [R v5.1] -> dimensionality reduction/clustering [R v5.1, UMAP v0.2.7.0] -> stage not stated [ADMIXTURE v1.3, BCFtools, BEAST v2.6.0, PLINK, ggplot2]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Evidence: The locations of mRNA molecules were plotted as a scatterplot using the ggplot function from the ggplot2 package with the Z -planes collapsed into one.
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### The landscape of genomic structural variation in Indigenous Australians. (Nature 2023)

- DOI: 10.1038/s41586-023-06842-7 | PMCID: PMC10733147 | PMID: 38093003
- Evidence: Allele sequences were visualized in sequence bar charts, in which each tile represented a nucleotide (A, C, G and T), using R package ggplot2.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools] -> visualisation [ggplot2] -> stage not stated [BEDTools, R, RepeatMasker v4.1.2, ape (R), vegan]

### Evolution of neuronal cell classes and types in the vertebrate retina. (Nature 2023)

- DOI: 10.1038/s41586-023-06638-9 | PMCID: PMC10719112 | PMID: 38092908
- Version used: **3.4.2**
- Evidence: ...des several packages used for statistical calculations and data visualizations including MASS v7.3.60, pvclust v2.2.0, reshape2 v1.4.4, stats v4.3.0, ggplot2 v3.4.2, dendextend v1.17.1 and ggdendro v0.1.23 We describe the analysis steps here at a high level.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat v4.3.0, ggplot2 v3.4.2] -> visualisation [Seurat v4.3.0, UMAP, ggplot2 v3.4.2]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **3.3.2**
- Evidence: The MAplots, box plots, violin plots and donut plots were produced using ggplot2 (v.3.3.2; https://ggplot2.tidyverse.org ) and heat maps of gene expression changes were produced using pheatmap (v.1.0.12; https://cran.r-project.org/web/packages/pheatmap/index.html ) in R (v.4.0.3).
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Version used: **3.4.3**
- Evidence: Map Plotting: Map in Figure 1A was made using the open-source R packages maps (version 3.4.1), sf (version 1.14) 74 , rnaturalearth (version 0.3.4) 75 , ggplot2 (version 3.4.3) 76 , and ggrepel (version 0.9.3) 77 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **3.3.5**
- Evidence: To visualize the distribution of cells with a specific perturbation (at the gene level) on the UMAP, contour density plots were generated using the ggplot2 (v.3.3.5) R package.
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Version used: **3.3.5**
- Evidence: Density plots were created using the stat_2d_density_filled function in ggplot2 v3.3.5.
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### High-resolution maps show that rubber causes substantial deforestation. (Nature 2023)

- DOI: 10.1038/s41586-023-06642-z | PMCID: PMC10632130 | PMID: 37853124
- Evidence: The figure was produced using R library ‘ggplot2’.
- Full pipeline: stage not stated [ggplot2]

### Antiviral type III CRISPR signalling via conjugation of ATP and SAM. (Nature 2023)

- DOI: 10.1038/s41586-023-06620-5 | PMCID: PMC10600005 | PMID: 37853119
- Evidence: The tree was visualized in R 4.1.1 and RStudio 2021.9.0.351 ( http://www.rstudio.com/ ) using ggtree 47 and ggplot2 48 .
- Full pipeline: visualisation [R v4.1, ggplot2] -> stage not stated [AlphaFold, Snakemake v7.22.0]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: Our pipeline used the R packages matrixStats, dplyr and ggplot2.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Unraveling the functional dark matter through global metagenomics. (Nature 2023)

- DOI: 10.1038/s41586-023-06583-7 | PMCID: PMC10584684 | PMID: 37821698
- Evidence: Plot distributions were computed using R and the R/ggplot2 45 package.
- Full pipeline: alignment/mapping [Clustal Omega, Python] -> dimensionality reduction/clustering [Clustal Omega] -> differential/statistical testing [R] -> stage not stated [AlphaFold, HMMER v3.1, ggplot2]

### A continuous fish fossil record reveals key insights into adaptive radiation. (Nature 2023)

- DOI: 10.1038/s41586-023-06603-6 | PMCID: PMC10567567 | PMID: 37794187
- Version used: **3.4.2**
- Evidence: 51 ) with packages rstatix v.0.7.2, ggplot2 v.3.4.2, tidypaleo v.0.1.3, patchwork 1.1.2, scales v.1.2.1, ggtext v.0.1.2 and dplyr v.1.1.2.
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [ggplot2 v3.4.2, tidyverse v1.1.2]

### Assembloid CRISPR screens reveal impact of disease genes in human neurodevelopment. (Nature 2023)

- DOI: 10.1038/s41586-023-06564-w | PMCID: PMC10567561 | PMID: 37758944
- Evidence: Data smoothing was performed using the geom_smooth() (as implemented in the ggplot2 package v.3.3.6) function in R with default parameters.
- Full pipeline: normalisation [ComplexHeatmap, R, Seurat] -> visualisation [ComplexHeatmap] -> stage not stated [Fiji v1.0, ImageJ v1.0, ggplot2]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Evidence: This enrichment was plotted against the −log 10 -transformed P value (Welch’s t -test) using the ggplot2 package in the R environment.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Evidence: The smoothened enrichment scores were visualized on the UMAP embedding using the ggplot2 (ref.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Polθ is phosphorylated by PLK1 to repair double-strand breaks in mitosis. (Nature 2023)

- DOI: 10.1038/s41586-023-06506-6 | PMCID: PMC10499603 | PMID: 37674080
- Evidence: Data were plotted in R using ggplot2.
- Full pipeline: visualisation [ggplot2] -> stage not stated [AlphaFold]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Version used: **3.4.2**
- Evidence: ...; rhdf5 v.2.44.0; DelayedArray v.0.26.3; S4Arrays v.1.0.4; patchwork v.1.1.2; reticulate v.1.28; Matrix v.1.5-4.1; cowplot v.1.1.1; ggExtra v.0.10.0; ggplot2 v.3.4.2; dplyr v.1.1.2; wesanderson v.0.3.6; RColorBrewer v.1.1-3; Seurat v.4.9.9.9042; SeuratObject v.4.9.9.9084; bmrm v.4.4; SummarizedExperiment v.1.30.1; Biobase v.2.60.0; GenomicRanges v.1.52.0; GenomeInfoDb v.1.36.0; IRanges v.2.34.0; S...
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Epitope editing enables targeted immunotherapy of acute myeloid leukaemia. (Nature 2023)

- DOI: 10.1038/s41586-023-06496-5 | PMCID: PMC10499609 | PMID: 37648862
- Evidence: The figures were generated using the R package ggplot2 62 .
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [Python] -> visualisation [ggplot2] -> stage not stated [Bioconductor, R]

### Native diversity buffers against severity of non-native tree invasions. (Nature 2023)

- DOI: 10.1038/s41586-023-06440-7 | PMCID: PMC10533391 | PMID: 37612513
- Evidence: 4.2.2) 115 using lme4 116 , lmerTest 117 , and betareg 118 , while visualizations for these models used ggplot2 119 ; tidyverse 95 was used throughout as well.
- Full pipeline: visualisation [ggplot2, lme4] -> stage not stated [QGIS, R, tidyverse]

### Global methane emissions from rivers and streams. (Nature 2023)

- DOI: 10.1038/s41586-023-06344-6 | PMCID: PMC10511311 | PMID: 37587344
- Version used: **3.3.5**
- Evidence: Packages used were dplyr (v.1.0.7) for data wrangling 53 , ggplot2 (v.3.3.5) for visualization 54 , lubridate (v.1.7.10) for temporal data 55 , corr (v.0.4.3) to assess correlations in the data 56 , ggtext (v.0.1.1) for labelling figures 57 , ggpubr (v.0.4.0) 58 and patchwork (v.1.1.1) 59 for composing multipaneled figures, sf (v.1.0.3) for spatial analysis of vector data 60 , terra (v.1.4.11) for...
- Full pipeline: machine learning [XGBoost] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4.0, tidyverse v1.0.7] -> stage not stated [R v0.3.2]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Version used: **3.3.3**
- Evidence: The final list of 167 regulons excluded non ‘_extended’ duplicates when ‘_extended’ versions were present. scRNA-seq data visualization Dot plots were created by R package ggplot2 (v.3.3.3).
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Evidence: All charts and visualization plots were generated with ggplot2 and dittoSeq 73 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Version used: **3.3.6**
- Evidence: Additional visualizations were based on functions from Nebulosa (v.1.6.0), Scillus (v.0.5.0) and ggplot2 (v.3.3.6).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: Mapped k -mers in each .bam file ( T. monococcum and T. urartu ) were analysed for the coverage in genomic windows of 1 Mb using mosdepth 112 and visualized in R (v.4.0.4) using ggplot2.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Enrichments were performed using Fisher’s exact tests and the resultant −log 10 [ P ] values were scaled and visualized using ggplot2.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Evidence: The ggplot2 package (v.3.4.2) was used to create boxplots, pie charts and scatterplots.
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### A cytosolic surveillance mechanism activates the mitochondrial UPR. (Nature 2023)

- DOI: 10.1038/s41586-023-06142-0 | PMCID: PMC10284689 | PMID: 37286597
- Version used: **3.3.3**
- Evidence: All plots were created using the R packages ggplot2 (v.3.3.3), gplots (v.3.1.1) and RColorBrewer (v.1.1-2).
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.7.1] -> stage not stated [DESeq2 v1.18.1, ImageJ v1.53, ggplot2 v3.3.3]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Version used: **3.3.5**
- Evidence: R plots used native plotting capabilities of the aforementioned packages together with ggplot2 (v.3.3.5), ggpubr (v.0.4.0) and ComplexHeatmap 42 (v.2.6.2) packages.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Uridine-derived ribose fuels glucose-restricted pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06073-w | PMCID: PMC10232363 | PMID: 37198494
- Version used: **3.3.5**
- Evidence: For data analysis and visualization in R, packages (with versions) used include dplyr (0.8.3), ggplot2 (3.3.5), gplots (3.0.1, heatmap.2 function), ComplexHeatmap (2.3.5), tidyverse (1.3.0) and VennDiagram (1.6.20).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5.2, limma] -> visualisation [ComplexHeatmap, ggplot2 v3.3.5, tidyverse v0.8.3] -> stage not stated [GSEA v4.0.3]

### In situ architecture of the ER-mitochondria encounter structure. (Nature 2023)

- DOI: 10.1038/s41586-023-06050-3 | PMCID: PMC7614606 | PMID: 37165187
- Evidence: For figure panels, the data was plotted using ggplot2 61 and raincloud plots 62 within R, and GraphPad Prism.
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ] -> simulation/modelling [NAMD] -> structure determination [IMOD] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, R, VMD]

### Recombination between heterologous human acrocentric chromosomes. (Nature 2023)

- DOI: 10.1038/s41586-023-05976-y | PMCID: PMC10172130 | PMID: 37165241
- Version used: **3.3.3**
- Evidence: We displayed the untangling results for each acrocentric chromosome with the R development environment (version 3.6.3), equipped with the following packages: tidyverse (version 1.3.0), RColorBrewer (version 1.1.2), ggplot2 (version 3.3.3) and ggrepel (version 0.9.1).
- Full pipeline: alignment/mapping [Python, igraph] -> stage not stated [BEDTools, PLINK v1.9, R v3.6.3, ggplot2 v3.3.3, tidyverse v1.3.0]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **3.3.5**
- Evidence: For general visualisation purposes, R packages ggplot2 (v3.3.5) 69 , ggpubr (v0.4) 70 , ggrepel (v0.9.2) 71 , ggbeeswarm (v.0.6.0) 72 , scales (v1.2.1.) 73 , ggforce (v0.4.1) 74 , and cowplot (v1.1.1) 75 were used.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **3.2.1**
- Evidence: Unless stated otherwise, plots were generated in the R environment (v.3.6.3), using ggplot2 (v.3.2.1) 64 , ggpubr (v.0.4.0), cowplot (v.1.0.0), scales(v.1.0.0) and ggrepel (v.0.8.1).
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Autoregulation of GPCR signalling through the third intracellular loop. (Nature 2023)

- DOI: 10.1038/s41586-023-05789-z | PMCID: PMC10033409 | PMID: 36890236
- Evidence: Figures were generated in RStudio (version 2022.12.0) using the ggplot2 package 62 .
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [ggplot2] -> stage not stated [VMD v1.9.3]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: Plots of differential gene expression were visualized using the ggplot2 package in R with significant genes ( P value < 0.05, |log2FC| ≥ 1).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Telomere-to-mitochondria signalling by ZBP1 mediates replicative crisis. (Nature 2023)

- DOI: 10.1038/s41586-023-05710-8 | PMCID: PMC9946831 | PMID: 36755096
- Version used: **3.3.2**
- Evidence: Graphical packages (Gviz v.1.28.3, rtracklayer v.1.44.2, gridExtra v.2.3, ggplot2 v.3.3.2) were used to visualize data.
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> normalisation [HOMER v4.10] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v3.6.1, ggplot2 v3.3.2] -> stage not stated [CellProfiler v4.2.1, ComplexHeatmap, ImageJ]

### Aberrant phase separation and nucleolar dysfunction in rare genetic diseases. (Nature 2023)

- DOI: 10.1038/s41586-022-05682-1 | PMCID: PMC9931588 | PMID: 36755093
- Evidence: Data wrangling was performed in base R, and plots were generated using the ggplot2 package.
- Full pipeline: visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BEDTools v2.30.0, ColabFold, R, VEP, ggplot2]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **3.3.3**
- Evidence: Statistical analysis Statistical analyses and graphical representations were performed in R using packages vegan (version 2.5–7), phyloseq (v1.28.0) 126 , QuantPsyc (v1.5), ggplot2 (v3.3.3), ggpubr (v0.4.0) and corrplot (v0.84).
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Version used: **3.2.1**
- Evidence: Plots were created using ggplot2 v.3.2.1, tidyverse v.1.3.0, dplyr v.0.8.5, cowplot v.1.0.0 and pheatmap v.1.0.12.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Imprinted SARS-CoV-2 humoral immunity induces convergent Omicron RBD evolution. (Nature 2023)

- DOI: 10.1038/s41586-022-05644-7 | PMCID: PMC9931576 | PMID: 36535326
- Version used: **3.3.3**
- Evidence: Figures were generated by R package ggplot2 (v3.3.3).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [R, ggplot2 v3.3.3, scikit-learn] -> stage not stated [SciPy]

### Microglia regulate central nervous system myelin growth and integrity. (Nature 2023)

- DOI: 10.1038/s41586-022-05534-y | PMCID: PMC9812791 | PMID: 36517604
- Version used: **3.3.5**
- Evidence: ShinyCell v.2.1.0 was used to produce an interactive application, and org.Mm.eg.db v.3.13.0 was used to annotate genes. ggplot2 v.3.3.5 was used to perform custom plots, here v.1.0.1 was used to ensure reproducible paths, and Matrix v.1.3.4 was used for handling sparse matrices.
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [Seurat v4.1.0] -> stage not stated [QuPath v0.3.0, ggplot2 v3.3.5]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: Plots were generated with the R package ggplot2 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Soil microbiomes show consistent and predictable responses to extreme events. (Nature 2024)

- DOI: 10.1038/s41586-024-08185-3 | PMCID: PMC11655354 | PMID: 39604724
- Version used: **3.3**
- Evidence: Statistical analyses All statistical analyses were performed in R software v.4.2 or above 59 , and most plots were generated using ggplot2 v.3.3 (ref.
- Full pipeline: read trimming [Cutadapt v1.2.1] -> quantification [vegan] -> differential/statistical testing [R, ggplot2 v3.3] -> visualisation [vegan] -> stage not stated [BLAST v2.13, DADA2 v1.24, lme4 v3.1, tidyverse]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **3.5.0**
- Evidence: Data were visualized using ggplot2 (v.3.5.0), ggrastr (v.1.0.2), ggridges (v.0.5.6) and RColorBrewer (v.1.1-3).
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: The distance to the closest pangenome accession was plotted with the R package ggplot2 to determine the threshold for similarity (Extended Data Fig.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Migrating is not enough for modern planktonic foraminifera in a changing ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-08191-5 | PMCID: PMC11634771 | PMID: 39537925
- Evidence: The viridis package supplied colourblind-friendly colour palettes 74 , and tidyr enabled easier data cleaning and wrangling 75 . ggplot2 and ggpubr were used to create high-quality graphics 76 , 77 , with reshape2 and reshape facilitating the reshaping of the data structures 78 .
- Full pipeline: stage not stated [ggplot2, ggpubr, pheatmap, tidyverse]

### Releasing a sugar brake generates sweeter tomato without yield penalty. (Nature 2024)

- DOI: 10.1038/s41586-024-08186-2 | PMCID: PMC11578880 | PMID: 39537922
- Version used: **3.4.4**
- Evidence: To visualize these patterns, we used ggplot2 (version 3.4.4) 78 to plot ROH length and number distributions across wild (PIM) and cultivated (BIG) populations.
- Full pipeline: alignment/mapping [MAFFT v7.525] -> quantification [ImageJ] -> visualisation [ggplot2 v3.4.4] -> stage not stated [IQ-TREE, PLINK, Python, VCFtools v0.1.16]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **3.4.3**
- Evidence: Barplots were prepared with ggplot2 (v.3.4.3).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Version used: **3.3.6**
- Evidence: A curated list of aggregated interactions were plotted for visualization using ggplot2 (v.3.3.6).
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **3.3.6**
- Evidence: The analysis and plotting (for this section and the following) were done using R v.4.3.1 and python v.3.10.6, as well as the R packages ggplot2 v.3.3.6 and tidyverse v.1.3.2 and python library numpy v.1.23.2.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: Data are visualized using ggplot2.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: Volcano plots were generated using the ggplot2 package in R and heat maps were generated using ComplexHeatmap package in R.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Statistical information Data were plotted in R (v.2022.07.01 and 554 running R v.4.0.3 (2020-10-10)) using the dplyr, ggplot2, tidyr, cowplot, reshape2, ggrepel, ggpubr, scales and RColorBrewer packages (versions dplyr_1.0.4, ggplot2_3.3.3, tidyr_1.1.2, cowplot_1.1.1, scales_1.1.1, reshape2_1.4.4, ggrepel_0.9.1, ggpubr_0.4.0, scales_1.1.1, RColorBrewer_1.1-2) or Microsoft Excel for Mac (v.16).
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. (Nature 2024)

- DOI: 10.1038/s41586-024-07881-4 | PMCID: PMC11390480 | PMID: 39261618
- Version used: **3.3.2**
- Evidence: All maps were plotted using the ggplot2 v3.3.2 102 R package.
- Full pipeline: alignment/mapping [GATK, SAMtools] -> normalisation [ADMIXTURE] -> registration [GATK, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [Matplotlib v3.5.3, R, ggplot2 v3.3.2] -> stage not stated [ANGSD v0.930, PLINK v1.9.20200712]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Evidence: The resulting dataset was imported in R to compute summary statistics comparing linkage disequilibrium across each major continental region, or superpopulations, and we used ggplot2 to visualize the results.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Version used: **3.5.1**
- Evidence: Bar, box, violin and heat map plots were created using the R package ggplot2 (v3.5.1).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### Mechanisms that clear mutations drive field cancerization in mammary tissue. (Nature 2024)

- DOI: 10.1038/s41586-024-07882-3 | PMCID: PMC11374684 | PMID: 39232148
- Evidence: Data visualization was executed using the ggplot2 package in R, with specific emphasis on certain chromosomes.
- Full pipeline: alignment/mapping [BWA, Cutadapt] -> dimensionality reduction/clustering [Python] -> simulation/modelling [Python] -> visualisation [ImageJ, ggplot2] -> stage not stated [QuPath]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **3.4.2**
- Evidence: The remaining plots were produced with ggplot2 (v3.4.2) 98 and the Python seaborn library (v0.11.2) 78 .
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: All summary plots were generated in R, mostly using the ggplot2 package 60 .
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### DNA-sensing inflammasomes cause recurrent atherosclerotic stroke. (Nature 2024)

- DOI: 10.1038/s41586-024-07803-4 | PMCID: PMC11390481 | PMID: 39112714
- Evidence: Principal components were picked by their percentage of explained variance (62.73% (PC1) and 21.05% (PC2)) and visualized using the ‘ggplot2’ package (version 3.4.3; https://ggplot2.tidyverse.org ).
- Full pipeline: dimensionality reduction/clustering [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [ImageJ]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Evidence: The ggplot2 R package was used to generate graphics.
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Results were visualized using MAGeCKFlute 60 and ggplot2 62 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: The ridgeline plot showing the distribution of PC1 score for each neuronal cell type was generated using the ggplot2 package in R.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: Statistics and plots were generated by ggplot2 in R and GraphPad Prism 8.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Other plots were made using the ggplot2 library in R and seaborn library in Python.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Brainstem Dbh&lt;sup&gt;+&lt;/sup&gt; neurons control allergen-induced airway hyperreactivity. (Nature 2024)

- DOI: 10.1038/s41586-024-07608-5 | PMCID: PMC11254774 | PMID: 38987587
- Version used: **3.3.2**
- Evidence: We plotted a density UMAP using geom_density_2d and stat_density_2d ( https://ggplot2.tidyverse.org/reference/geom_density_2d.html ) from ggplot2 (v3.3.2) 44 for visual identification of high-density regions that represent potential unique cell populations.
- Full pipeline: quality control [R, Seurat v4.0, UMAP] -> normalisation [R, Seurat v4.0, UMAP, scDblFinder v2.0] -> dimensionality reduction/clustering [R, Seurat v4.0, UMAP, ggplot2 v3.3.2, tidyverse] -> differential/statistical testing [R, Seurat v4.0, UMAP] -> visualisation [ggplot2 v3.3.2, tidyverse]

### An enterococcal phage-derived enzyme suppresses graft-versus-host disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07667-8 | PMCID: PMC11291292 | PMID: 38987594
- Version used: **3.3.6**
- Evidence: A volcano plot was drawn using the ggplot2 (v.3.3.6) R package.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> dimensionality reduction/clustering [SPAdes v3.13.0] -> differential/statistical testing [SPAdes v3.13.0] -> stage not stated [BLAST, Cutadapt, QIIME 2 v2018.11, R, SAMtools, ggplot2 v3.3.6]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Evidence: DEGs were visualized as volcano plot using ggplot2 R package v.3.3.2.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### Transposase-assisted target-site integration for efficient plant genome engineering. (Nature 2024)

- DOI: 10.1038/s41586-024-07613-8 | PMCID: PMC11254759 | PMID: 38926583
- Evidence: Data for forward and reverse orientation of mPing insertion were merged and R package ggplot2 was used for the data display.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [R, ggplot2]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Data presentation The following R packages were used to create figures: GenomicRanges 109 , EnhancedVolcano 110 , ggplot2 (ref.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Global shortfalls in documented actions to conserve biodiversity. (Nature 2024)

- DOI: 10.1038/s41586-024-07498-7 | PMCID: PMC11168922 | PMID: 38839953
- Evidence: Data visualization: cowplot 72 , DiagrammeR 73 , DiagrammeRsvg 74 , egg 75 , ggplot2 76 , ggnewscale 77 , ggtext 78 , gridExtra 79 , png 80 , RColorBrewer 81 , rphylopic 82 , rsvg 83 , scales 84 .
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2] -> stage not stated [R v4.3.2, tidyverse]

### Senescent glia link mitochondrial dysfunction and lipid accumulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07516-8 | PMCID: PMC11168935 | PMID: 38839958
- Evidence: Statistical analysis Statistical analysis and data visualization were performed in the R Environment using RStudio with base R and packages as indicated including with tidyverse (dplyr, ggplot2), ggrepel, cowplot, ggsurvplot.
- Full pipeline: alignment/mapping [DESeq2, HISAT2 v2.1.0, HTSeq v0.9.1, SAMtools] -> differential/statistical testing [DESeq2, HTSeq v0.9.1, edgeR, ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse]

### The sex of organ geometry. (Nature 2024)

- DOI: 10.1038/s41586-024-07463-4 | PMCID: PMC11168936 | PMID: 38811741
- Evidence: Boxplots and line graphs were plotted in R using the ‘ggplot2’ package (v.3.4.0).
- Full pipeline: dimensionality reduction/clustering [R v3.6.0] -> differential/statistical testing [tidyverse] -> visualisation [ggplot2]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Evidence: The curve fitting analysis was performed using the geom_smooth function with “method = “gam”” option from the ggplot2 package in R.
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### The intrinsic substrate specificity of the human tyrosine kinome. (Nature 2024)

- DOI: 10.1038/s41586-024-07407-y | PMCID: PMC11136658 | PMID: 38720073
- Evidence: These values were log-transformed and plotted in v.4.2.3 of R 65 using v.3.4.2 of the package ggplot2 66 .
- Full pipeline: visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python v3.7.6, SciPy]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **3.4.2**
- Evidence: Volcano plots were visualized using the ggplot2 R package ggplot2 (v.3.4.2), and PCA was conducted using the prcomp function in R and visualized using the R packages ggplot2 and ggrepel (v.0.9.3).
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: Results were extracted from edgeR as tables and used for generating volcano or box plots in ggplot2 in RStudio.
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### Environmental drivers of increased ecosystem respiration in a warming tundra. (Nature 2024)

- DOI: 10.1038/s41586-024-07274-7 | PMCID: PMC11062900 | PMID: 38632407
- Evidence: 1 were made with R (packages ggplot2 and country code) and for the maps in Fig.
- Full pipeline: stage not stated [R, ggplot2, metafor]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Version used: **3.3.5**
- Evidence: The top enriched terms were visualized with dot plots using R package ggplot2 (v3.3.5).
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: We used the stv_row.bed file to visualize the organization of the α-satellite HOR arrays with R 68 (v.1.1.383) and the ggplot2 package 66 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Version used: **3.4.1**
- Evidence: Screen results were plotted using R (4.2.2) and ggplot2 (3.4.1).
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### Revealing uncertainty in the status of biodiversity change. (Nature 2024)

- DOI: 10.1038/s41586-024-07236-z | PMCID: PMC11041640 | PMID: 38538788
- Evidence: Figures were produced using the following R packages: ggplot2 54 , ggtree 55 and ape 45 .
- Full pipeline: visualisation [ggplot2] -> stage not stated [R, tidyverse]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **3.4.2**
- Evidence: R (v.4.1.3): cluster (v.2.1.2) 138 , ComplexHeatmap (v.2.10.0) 139 , 140 , data.table (v.1.14.8) 141 , DescTools (v.0.99.48) 142 , dplyr (v.1.1.2) 143 , gdata (v.2.19.0) 144 , ggforce (v.0.4.1) 145 , ggplot2 (v.3.4.2) 146 , ggpmisc (v.0.5.3) 147 , ggpointdensity (v.0.1.0) 148 , ggpubr (v.0.5.0) 149 , ggrastr (v.1.0.2) 150 , ggrepel (v.0.9.3) 151 , grid (v.4.1.3) 152 , gridExtra (v.2.3) 153 , gtabl...
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Version used: **3.2.0**
- Evidence: Differences in Bhattacharyya distances between patient groups were tested using Wilcoxon rank-sum tests, and boxplots were generated using the geom_boxplot function from the R package ggplot2 (v.3.2.0).
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Mutualisms weaken the latitudinal diversity gradient among oceanic islands. (Nature 2024)

- DOI: 10.1038/s41586-024-07110-y | PMCID: PMC10937366 | PMID: 38418873
- Version used: **3.4.0**
- Evidence: 4.3.2) using the following packages: mgcv (v1.8.41), gridExtra (v2.3), betareg (v3.1.4), MASS (v7.3.58.1), lme4 (v1.1.31), lmerTest (v3.1.3), lsmeans (v2.30.0), ggeffects (v1.1.4), spdep (v1.2.7), ggplot2 (v3.4.0), ncf (v1.3.2), ape (v5.6.2), sjPlot (v2.8.12), gridExtra (v2.3), MuMIn (v1.47.1), maps (v3.4.1), sf (v1.0.9), car (v3.1.1), viridis (v0.6.2), tidyverse (v1.3.2) and GIFT (v1.3.0).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, ggplot2 v3.4.0, tidyverse v1.3.2]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **2.2.1**
- Evidence: Figure 2 was created using ggplot2 (v.2.2.1) 50 .
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Smoking changes adaptive immunity with persistent effects. (Nature 2024)

- DOI: 10.1038/s41586-023-06968-8 | PMCID: PMC10881394 | PMID: 38355791
- Version used: **3.2.1**
- Evidence: P values of association tests were represented using ggplot2 3.2.1 in R 3.6.0.
- Full pipeline: differential/statistical testing [ggplot2 v3.2.1] -> stage not stated [R v4.2]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Evidence: The line of gene expression was plotted by the geom_smooth function in ggplot2.
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Evidence: Expression data of characteristic genes in KC and TAM clusters were extracted and presented in violin plots using the ggplot2 package (v.3.4.1).
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Translation selectively destroys non-functional transcription complexes. (Nature 2024)

- DOI: 10.1038/s41586-023-07014-3 | PMCID: PMC10881389 | PMID: 38326611
- Evidence: Plots were generated using ggplot2 and statistical analyses shown were performed using stat_compare_means (Student’s t -test) in RStudio (v.2022.07.2).
- Full pipeline: differential/statistical testing [ggplot2] -> structure determination [ChimeraX, Coot] -> stage not stated [RELION]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Evidence: TreeAnnotator v2.6.7 was used to compute MCC trees and the results were visualized using ggplot2 124 , ggtree 125 and custom scripts.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Targeted design of synthetic enhancers for selected tissues in the Drosophila embryo. (Nature 2024)

- DOI: 10.1038/s41586-023-06905-9 | PMCID: PMC10830412 | PMID: 38086418
- Version used: **3.2.1**
- Evidence: 66 )) and using the R package ggplot2 (v.3.2.1 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Keras, TensorFlow v1.14.0] -> visualisation [R, UMAP] -> stage not stated [BEDTools, MACS2, ggplot2 v3.2.1]

### N&lt;sup&gt;1&lt;/sup&gt;-methylpseudouridylation of mRNA causes +1 ribosomal frameshifting. (Nature 2024)

- DOI: 10.1038/s41586-023-06800-3 | PMCID: PMC10764286 | PMID: 38057663
- Version used: **3.4.2**
- Evidence: Donor genotypes for the BNT162b2-vaccinated individuals were visualized in a presence–absence heatmap in R (version 4.3.0) using ggplot2 (version 3.4.2).
- Full pipeline: alignment/mapping [STAR v2.7.4a] -> variant calling [R v4.3.0, ggplot2 v3.4.2] -> visualisation [R v4.3.0, ggplot2 v3.4.2]

### Repeated Omicron exposures override ancestral SARS-CoV-2 immune imprinting. (Nature 2024)

- DOI: 10.1038/s41586-023-06753-7 | PMCID: PMC10764275 | PMID: 37993710
- Version used: **3.3.3**
- Evidence: Figures were generated by R package ggplot2 (v3.3.3).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy, igraph]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **3.3.5**
- Evidence: To visualize both microglia and T cells in a combined PCA space, the first two principal components (PC1 and PC2) were plotted using ggplot2 (v.3.3.5) with fixed axis scaling to preserve relative distances.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **3.4.2**
- Evidence: ...me sequencing, immunohistochemistry and IMC data, which were conducted using R (v4.2.3) using R-studio build 513 with the packages: tidyverse (v2.0), ggplot2 (v3.4.2), ggpubr (v0.6.0) and pheatmap (v1.0.12).
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### A vaccine central in A(H5) influenza antigenic space confers broad immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09626-3 | PMCID: PMC12657240 | PMID: 41094140
- Version used: **3.5.1**
- Evidence: Data visualization and statistics Data were visualized with Racmacs (v.1.2.3) 80 , r3js (v.0.0.2) 83 and/or ggplot2 (v.3.5.1) 87 in R v.4.4.3 (used throughout).
- Full pipeline: read trimming [MAFFT v7.515] -> alignment/mapping [MAFFT v7.515] -> differential/statistical testing [ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [R v4.4.3]

### New fossils reveal the hand of Paranthropus boisei. (Nature 2025)

- DOI: 10.1038/s41586-025-09594-8 | PMCID: PMC12657221 | PMID: 41094139
- Version used: **3.4.1**
- Evidence: The PC scores were plotted using the function ggplot() in the R package ggplot2 (v.3.4.1) 71 .
- Full pipeline: visualisation [ggplot2 v3.4.1] -> stage not stated [ImageJ, R]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Version used: **3.5.1**
- Evidence: Genome maps were visualized using the R gggenomes (v.0.9.9.9000) package, and genome read coverage was visualized using R ggplot2 (v.3.5.1).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### Sperm sequencing reveals extensive positive selection in the male germline. (Nature 2025)

- DOI: 10.1038/s41586-025-09448-3 | PMCID: PMC12611766 | PMID: 41062690
- Version used: **3.4.4**
- Evidence: Code modified from trackViewer (R/Bioconductor package v.1.38.0) was used to generate gene mutation lollipop plots. lme4 (v.1.1-33) was used for linear mixed-effects models. ggplot2 (v.3.4.4) was used for plotting. dNdScv ( https://github.com/im3sanger/dndscv ; version as of commit on 29 September 2023) was used for selection analysis.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [Bioconductor, ggplot2 v3.4.4, lme4] -> visualisation [R] -> stage not stated [BCFtools, Nextflow]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Regression between adenosine-ending codon and protein levels were calculated with the R function stat_cor (package ggpubr) to compute Pearson’s r and geom_smooth (package ggplot2) using ‘linear model’ to display the regression line.
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Version used: **3.4.2**
- Evidence: The following packages were used: CellRanger v.6.0.1, singleCellTK v.2.8.0, Seurat v.4.3.0, scater v.1.24.0, harmony v.0.1.1, RColorBrewer v.1.1.3, ComplexHeatmap v.2.14.0, ArchR v.1.0.2, muscat v.1.12.1, readr v.2.1.4, ggplot2 v.3.4.2, ggsignif v.0.6.4, ggpubr v.0.6.0, magrittr v.2.0.3, scCoda v.0.1.9 Python package, celda v.1.19.1 and hdWGCNA v.0.4.5.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **3.4.4**
- Evidence: UMAP coordinates and hox13 normalized expression of endoderm cells were exported to a file and plotted using ggplot2 v.3.4.4.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Fluctuating DNA methylation tracks cancer evolution at clinical scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09374-4 | PMCID: PMC12443617 | PMID: 40931062
- Version used: **3.5.2**
- Evidence: Plots were generated using ggplot2 (v3.5.2).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Bioconductor, R, SAMtools, Stan, dynesty, ggplot2 v3.5.2, survival (R) v0.4.9]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Evidence: Figures were produced using the packages ggplot2 (ref.
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Version used: **3.3.6**
- Evidence: The following R packages were used: Rsamtools (v.2.12.0), vegan (v.2.6-2), factoextra (v.1.0.7), ggplot2 (v.3.3.6), ggExtra (v.0.10.0), ggforce (v.0.3.3), rnaturalearth (v.0.1.0), sf (v.1.0.-8), raster (v.3.5-21), rgdal (v.1.5-32), spatstat (v.2.3-4), maptools (v.1.1-4), gstat (v.2.0-9), sp (v.1.5-0), labdsv (v.2.0-1), rcarbon (v.1.5.1), magrittr (v.2.0.3), dplyr (v.1.0.9), reshape 2 (v.1.4.4), an...
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: Next, principal components analysis (visualized using ggplot2) was performed on highly variable data.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### STING induces ZBP1-mediated necroptosis independently of TNFR1 and FADD. (Nature 2025)

- DOI: 10.1038/s41586-025-09536-4 | PMCID: PMC12629989 | PMID: 40834903
- Version used: **3.5.1**
- Evidence: Volcano plots were generated using ggplot2 (v.3.5.1) and heat maps were created using heatmap.2 (gplots, v.3.2.0) with row-wise scaling on the DEseq2-normalized expression data.
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [Fiji, ImageJ, RSEM, STAR] -> normalisation [ggplot2 v3.5.1] -> differential/statistical testing [DESeq2 v1.44.0, RSEM, STAR] -> stage not stated [GSEA, Metascape]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: Data visualization was done using the ggplot2 package in R 81 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Evidence: Using the ggplot2 package (v.3.5.0) 76 , average log 2 (FC) values of human and mouse genes were plotted.
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **3.4.4**
- Evidence: ...numpy (v.1.19.3), anndata (v.0.7.4), scanpy (v.1.6.0), matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R packages: ggplot2 (v.3.4.4), gplots (v.3.1.3), readr (v.2.1.4), dplyr (v.1.1.2), reshape2 (v.1.4.4), patchwork (v.1.1.3), RColorBrewer (v.1.1.3), ggrepel (v.0.9.4), aplot (v.0.1.10), ggdendro (v.0.1.23), Matrix (v.1.6.4), here (v.1.0.1), pheatmap (v.1.0.12), t...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: Plots were produced using the Seurat 57 , ggplot2 63 , ggpubr 64 and pheatmap 65 R packages.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Evidence: We used the resulting RepeatMasker and HumAS-AMMER stv_row.bed files to visualize the organization of the α-satellite HOR arrays with R (v.1.1.383) 131 and the ggplot2 package 132 .
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **3.3.3**
- Evidence: The session used the following libraries: limma (3.46.0), edgeR (3.32.1), tximport (1.18.0), edgeR (3.32.1), sva (3.38.0), RColorBrewer (1.1-2), pheatmap (1.0.12), biomaRt (2.46.3), ggplot2 (3.3.3), gplots (3.1.1), ggfortify (0.4.11), NMF (0.23.0), cluster (2.1.1), fpc (2.2-9), plyr (1.8.6), dplyr (1.0.5), pvclust (2.2-0), ggrepel (0.9.1), amap (0.8-18), gProfileR (0.7.0), xtable (1.8-4), ggpubr (...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **3.5.1**
- Evidence: The package ggplot2 (v.3.5.1) was used for visualization.
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Version used: **3.4.2**
- Evidence: The results from above analyses were visualized using the R package ggplot2 (v.3.4.2).
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: A bubble map displaying the mean counts of chromosome pairs within different subsections was drawn with ggplot2 74 .
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Version used: **3.5.1**
- Evidence: The volcano and correlation plots depicting the results were generated using the R package ggplot2 v.3.5.1 (ref.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Version used: **3.5.0**
- Evidence: Volcano plots were generated with ggplot2 v.3.5.0 R package.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Rapid emergence of a maths gender gap in first grade. (Nature 2025)

- DOI: 10.1038/s41586-025-09126-4 | PMCID: PMC7618463 | PMID: 40500443
- Evidence: R packages used included rstatix, FactoMineR, dplyr, tidyverse, broom, ggplot2, jtools, LambertW, cohens_d, reshape2, lmerTest, knitr, rmarkdown, MatchIt, remotes, rcpp, glmertree, BayesFactor, mice and tableone, all for R v.4.3.2.
- Full pipeline: stage not stated [R, ggplot2, lme4, tidyverse]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Evidence: Figures were generated using GraphPad PRISM9 and with R package ggplot2.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **3.3.5**
- Evidence: The R package ComplexHeatmap (v.2.11.1) was used to generate heat maps, and visualization was facilitated using ggplot2 (v.3.3.5), ggpubr (v.0.6.0), ggrepel (v.0.9.2), Statannot (v.0.6.0), Circlize (v.0.4.16), GseaVis (v.0.0.5), Enrichplot (v.1.22.0), GridExtra (v.2.3.0), Pheatmap(v.1.0.12) and DEGreport (v.1.38.5) R packages.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Evidence: Dot plots were generated with the R package ‘ggplot2’ 68 .
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: Transcriptome-wide comparisons were visualized as MA plots, using ggplot2 to plot “baseMean” (mean normalized counts across all conditions) against log 2 (enrichment).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Ideogram methods Ideograms for each pair of chromosomes for the 78 chromosome-level, haplotype-phased genomes were created using ggplot2 [ https://ggplot2.tidyverse.org ] in R ( www.R-project.org ) (Fig.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Version used: **3.5.1**
- Evidence: Software and resources The following software, packages and resources were additionally used for analysis and visualization: Rstudio (2023.06.0 Build 421 with R 4.2.1, RRID:SCR_001905); R package ggplot2 (3.5.1, RRID:SCR_014601); R package RColorBrewer (1.1.3, SCR_016697); R package ggrepel (0.9.5, RRID:SCR_016223); R package dplyr (1.1.4); R package FactoMineR (2.11, RRID:SCR_014602); R package p...
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **3.5.0**
- Evidence: Maps and plotting Unless otherwise stated, figures were produced in R using functions from base R 52 and ggplot2 (v.3.5.0) 118 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Molecular basis of positional memory in limb regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09036-5 | PMCID: PMC12176643 | PMID: 40399677
- Version used: **3.3.6**
- Evidence: Volcano plots were generated using ggplot2 v.3.3.6 (ref.
- Full pipeline: read trimming [HISAT2, Trimmomatic v0.39] -> alignment/mapping [HISAT2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, ggplot2 v3.3.6, pheatmap]

### Clonal tracing with somatic epimutations reveals dynamics of blood ageing. (Nature 2025)

- DOI: 10.1038/s41586-025-09041-8 | PMCID: PMC12240852 | PMID: 40399669
- Evidence: Data visualization Plots were generated using the R packages ggplot2 (ref.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, Seurat]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Line plots showing mean and standard error of gene and repeat expression were generated using ggplot2.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Targeting the SHOC2-RAS interaction in RAS-mutant cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-08931-1 | PMCID: PMC12137120 | PMID: 40335703
- Version used: **3.3.6**
- Evidence: Figures and fgsea analysis were created with R v.4.1.0 using the R packages fgsea v.1.18.0, ggplot2 v.3.3.6, cowplot v.1.1.1 and ggpubr v.0.4.0.
- Full pipeline: differential/statistical testing [DESeq2, edgeR] -> stage not stated [Picard, R, fgsea, ggplot2 v3.3.6, ggpubr v0.4.0]

### Global evolution of inflammatory bowel disease across epidemiologic stages. (Nature 2025)

- DOI: 10.1038/s41586-025-08940-0 | PMCID: PMC12158780 | PMID: 40307548
- Evidence: 3 were created in R using the ggplot2 package.
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [ggplot2]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: Visualizations were generated using Seurat 45 , ComplexHeatmap 47 and ggplot2 (ref.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Microbial metabolite drives ageing-related clonal haematopoiesis via ALPK1. (Nature 2025)

- DOI: 10.1038/s41586-025-08938-8 | PMCID: PMC12137129 | PMID: 40269158
- Evidence: All graphs and analysis were generated using GraphPad Prism 9.0 software or using the package ggplot2 from R.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [HISAT2] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, FastQC v0.11.8, R] -> stage not stated [MACS2, ggplot2, phyloseq]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Version used: **3.4.4**
- Evidence: Plots were generated using ggplot2 (v.3.4.4).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **3.4.2**
- Evidence: For heatmaps and PCAs, matrices were generated with deeptools (3.5.1) computeMatrix, and heatmaps and PCAs were generated with deeptools plotHeatmap and ggplot2 (3.4.2), respectively.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: Heat plots of 1-DST matrices were made with the ggplot2 package in R (v.4.1.3).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: The results of the analyses were visualized with ggplot2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **3.3.6**
- Evidence: Exact sequence variant counts were converted to relative abundance, which was plotted in R v.4.2.0 with ggplot2 v.3.3.6.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### The P-loop NTPase RUVBL2 is a conserved clock component across eukaryotes. (Nature 2025)

- DOI: 10.1038/s41586-025-08797-3 | PMCID: PMC12178907 | PMID: 40140583
- Version used: **3.4.2**
- Evidence: The differential analysis was done using the limma package (v.3.54.2) 58 , and the resulting volcano plots were created in R using ggplot2 (v.3.4.2). siRNA assay U2OS cells with the Per2-dLuc reporter were seeded at 8 × 10 5 cells in 35-mm dishes.
- Full pipeline: differential/statistical testing [ggplot2 v3.4.2, limma] -> stage not stated [ImageJ v1.53c]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Evidence: The log 2 FC values and MAGeCK RRA scores of the mitochondria-associated genes in this secondary genetic interaction screen were visualized as a volcano plot by ggplot2 R package (v.3.3.5), with the top 1 and 2 significantly enriched (based on MAGeCK RRA score) mitochondria-associated gene candidates ( Casp9 and Bak1 ) annotated.
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: This was done by plotting cells positive for Cyp2f2 on one image using ggplot2 in R, and cells positive for Cyp2e1 on another ggplot2 image.
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Evidence: Nchart was generated with ggplot2 ( https://ggplot2.tidyverse.org/ ) using adaptation of N-chart ( https://github.com/MariaNattestad/Nchart ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **3.4.4**
- Evidence: R libraries used: BiocManager v.1.30.22, circlize v.0.4.15, ComplexHeatmap v.2.16.0, drawProteins v.1.20.0, dplyr v.1.1.2, ggplot2 v.3.4.4, ggnewscale v.0.4.10, ggrepel v.0.9.4, PerformanceAnalytics v.2.0.4, RColorBrewer v.1.1-3, stringr v.1.5.1, tidyr v.1.3.0, tidyverse v.2.0.0, ggplot2 v.3.4.4.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Plots were generated using the ggplot2 R package (RRID:SCR_014601). sexDEG analysis To determine DEGs between sexes, we performed sample-pseudobulk-based DESeq2 (RRID:SCR_015687) differential expression testing for each cell type.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Vulnerability of amphibians to global warming. (Nature 2025)

- DOI: 10.1038/s41586-025-08665-0 | PMCID: PMC11946914 | PMID: 40044855
- Evidence: Maps, phylogenetic trees and data visualizations were generated using the R packages rnaturalearthhires 65 , ggtree 66 and ggplot2 67 .
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [R, brms] -> visualisation [ggplot2] -> stage not stated [lme4 v1.1, metafor]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: We plotted the dot plots with the position of the dots representing the subtracted GSVA enrichment values, and the size of the dot representing the prevalence using ggplot2.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Version used: **3.3.6**
- Evidence: Visualization of data by a combination of the ComplexHeatmap (v.2.4.3 and v.2.14.0) 74 , ggplot2 (v.3.3.6 and v.3.5.1) 75 , cowplot (v.1.1.1; https://CRAN.R-project.org/package=cowplot ) and viridis 76 packages.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Clonal driver neoantigen loss under EGFR TKI and immune selection pressures. (Nature 2025)

- DOI: 10.1038/s41586-025-08586-y | PMCID: PMC11946900 | PMID: 39972134
- Version used: **3.5.1**
- Evidence: Analysis was conducted in R using the dplyr (v.1.1.4), immunarch (v.0.9.1), data.table (v.1.14.8), RColorBrewer (v.1.1-3), viridis (v.0.6.5) and ggplot2 (v.3.5.1) packages.
- Full pipeline: stage not stated [data.table v1.14.8, ggplot2 v3.5.1, tidyverse v1.1.4]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Version used: **3.5.0**
- Evidence: Related volcano plots were created using the R package ggplot2 (v.3.5.0).
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **3.5.1**
- Evidence: Volcano plots were created using the R package ggplot2 (v.3.5.1).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Version used: **3.4.4**
- Evidence: ....1, ggtree v.3.10.1, lubridate v.1.9.3, forcats v.1.0.0, stringr v.1.5.0, dplyr v.1.1.3, purrr v.1.0.2, readr v.2.1.4, tidyr v.1.3.0, tibble v.3.2.1, ggplot2 v.3.4.4, tidyverse v.2.0.0, SeuratObject v.4.1.4, Seurat v.4.4.0, RcppAnnoy v.0.0.22, cellranger v.4-5, spaceranger v.2 and bolt-lmm v.2.3.6.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **3.4.2**
- Evidence: Plots were generated in R using the packages ggplot2 v.3.4.2 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Global meta-analysis shows action is needed to halt genetic diversity loss. (Nature 2025)

- DOI: 10.1038/s41586-024-08458-x | PMCID: PMC11839457 | PMID: 39880948
- Version used: **3.4.3**
- Evidence: Publication trends and the characteristics of studies included in our final dataset were summarized visually using the R packages ggplot2 v.3.4.3 49 , treemapify v.2.5.5 50 and ggridges v.0.5.4 51 .
- Full pipeline: visualisation [R] -> stage not stated [ggplot2 v3.4.3, tidyverse v0.8.0]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Evidence: PCA based on haplotypes (12 chromosomes) was performed using Plink (v.1.90) 99 on the VCF file with the parameter “--pca 5”; the results were visualized using the R package ggplot2 100 .
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Evidence: Data visualization The R package ggplot2 was used for figure generation ( https://ggplot2.tidyverse.org ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: The circus plots were graphed by using the circlize package, and the rest of the graphs were visualized using ggplot2 and Seurat.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: GO enrichment plots were created using ggplot2 (ref.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: The most abundant pathways were included in PCoA using geom_text from the package ggplot2 (ref.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **3.4.4**
- Evidence: The number of insertion sites were plotted using the packages of ggplot2 (v.3.4.4) 53 , readr (v.2.1.5) 54 and dplyr (v.1.1.4) 55 in R software (v.4.3.2) 56 .
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: For comparison of MYC peaks within closed and open chromatin across all reprogramming systems, intersection over union or the Jaccard index was measured using the bedtools jaccard function and ggplot2 was used to generate the resulting heat map 73 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Evidence: Coverage proportions across each investigated gene were calculated with BEDtools 97 and subsequently plotted on a heatmap using ggplot2 of R version 4.2.2 (Extended Data Fig.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### Earliest modern human genomes constrain timing of Neanderthal admixture. (Nature 2025)

- DOI: 10.1038/s41586-024-08420-x | PMCID: PMC11839475 | PMID: 39667410
- Version used: **3.4.2**
- Evidence: We used Rstudio (v.2022.12.0+353, http://www.rstudio.com/ ) and the following packages for data visualization: cowplot (v.1.1.2), ggplot2 (v.3.4.2, https://ggplot2.tidyverse.org ), tidyr (v.1.3.0, https://github.com/tidyverse/tidyr ), dplyr (v.1.1.4, https://github.com/tidyverse/dplyr ), magrittr (v.2.0.3, https://github.com/tidyverse/magrittr ), scales (v.1.3.0, https://github.com/r-lib/scales ) ...
- Full pipeline: read trimming [BWA v0.5.10] -> alignment/mapping [BWA v0.5.10, Bowtie2, GATK, SAMtools] -> variant calling [GATK] -> visualisation [ggplot2 v3.4.2, tidyverse v1.1.4] -> stage not stated [BEDTools]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Version used: **3.4.1**
- Evidence: Visualization was performed in R using ggplot2 (v3.4.1).
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Macrophages excite muscle spindles with glutamate to bolster locomotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08272-5 | PMCID: PMC11735391 | PMID: 39633045
- Evidence: Graphs and dotplots were made using GraphPad Prism v.9.4.0 or using ggplot2-v.3.3.6 in R, respectively.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [DESeq2, ImageJ, ggplot2, scDblFinder]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Evidence: The plots were generated using the DimPlot and VlnPlot functions from Seurat as well as the ggplot2 and pheatmap R libraries.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### The oestrous cycle stage affects mammary tumour sensitivity to chemotherapy. (Nature 2025)

- DOI: 10.1038/s41586-024-08276-1 | PMCID: PMC11666466 | PMID: 39633046
- Evidence: 68 ) and packages from tidyverse 69 , including dplyr, tidyr and ggplot2, and were analysed as follows.
- Full pipeline: quantification [Fiji v1.49k, QuPath v0.4.4] -> dimensionality reduction/clustering [ImageJ] -> differential/statistical testing [R v4.4.2] -> machine learning [QuPath v0.4.4] -> stage not stated [ggplot2, tidyverse]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Version used: **3.3.6**
- Evidence: All data analysis and visualization was done in R (v4.2.1) with the following packages: stats (v.4.1.1), vegan (v.2.6), ggplot2 (v.3.3.6), ComplexUpset (v.2.8.0), tidyr (v.1.2.0), dplyr (v.1.0.9), corrplot (v.0.92), pheatmap (v.1.0.12), RColorBrewer (v.1.1-3), pls (v.2.8), edgeR (v.3.16).
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Evolving antibody response to SARS-CoV-2 antigenic shift from XBB to JN.1. (Nature 2025)

- DOI: 10.1038/s41586-024-08315-x | PMCID: PMC11754117 | PMID: 39510125
- Version used: **3.3.3**
- Evidence: To visualize the dataset in two dimensions, uniform manifold approximation and projection was performed on the basis of the k -nearest-neighbour graph using umap-learn module (v.0.5.2), and figures were generated using R package ggplot2 (v.3.3.3).
- Full pipeline: dimensionality reduction/clustering [R, UMAP, ggplot2 v3.3.3, igraph] -> differential/statistical testing [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Evidence: Gene expression patterns were visualized using custom dot plots generated with ggplot2, where average normalized expression values were calculated using the AverageExpression function from the normalized RNA assay slot, and percent expression was computed as the fraction of cells within each identity with expression greater than zero.
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Amplified Arctic iceberg traffic reshapes benthic biodiversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10630-4 | PMCID: PMC13293891 | PMID: 42271066
- Evidence: Statistical analyses were conducted in the R environment using the packages vegan, pairwiseAdonis and ggplot2.
- Full pipeline: differential/statistical testing [ggplot2] -> stage not stated [ImageJ]

### Technology mediation in child sexual exploitation and abuse in Africa and Asia. (Nature 2026)

- DOI: 10.1038/s41586-026-10525-4 | PMCID: PMC13253325 | PMID: 42203864
- Evidence: All graphs were created using ggplot2 96 and ggdist 97 .
- Full pipeline: differential/statistical testing [R] -> stage not stated [brms, ggplot2]

### Genome-wide sweeps create ecological units in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-026-10476-w | PMCID: PMC13322978 | PMID: 42092154
- Version used: **3.5.1**
- Evidence: Statistical analysis Statistical analyses and graphical representations were performed in R (v.4.2.1) 80 using base R statistical functions and ggplot2 (v.3.5.1) 81 , ggpubr (v.0.6.0) 82 , ggtree (v.3.4.4) 83 , ggtreeExtra (v.1.6.1) 84 and ComplexHeatmap (v.2.12.1) 85 .
- Full pipeline: alignment/mapping [MetaPhlAn v4.0.6] -> differential/statistical testing [ComplexHeatmap v2.12.1, ggplot2 v3.5.1, ggpubr v0.6.0] -> stage not stated [Prokka v1.14.6, R, SciPy]

### Higher-order interactions enhance the latitudinal tree diversity gradient. (Nature 2026)

- DOI: 10.1038/s41586-026-10434-6 | PMCID: PMC13171435 | PMID: 42056517
- Version used: **4.0.0**
- Evidence: 2 was generated using R packages ggplot2 (v.4.0.0) and ggrepel (v.0.9.6).
- Full pipeline: stage not stated [ggplot2 v4.0.0]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Version used: **3.4.4**
- Evidence: Paired box plots and box plots were generated using the packages ggpubr (0.6.0) and ggplot2 (3.4.4).
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Evidence: Most visualizations are based on ggplot2 ( https://ggplot2.tidyverse.org/ ).
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### A pro-carcinogenic bacterial toxin binds claudin-4 to cleave E-cadherin. (Nature 2026)

- DOI: 10.1038/s41586-026-10375-0 | PMCID: PMC13253352 | PMID: 42020735
- Version used: **3.4.4**
- Evidence: 2d were generated using ggplot2 version 3.4.4 in R version 4.2.2.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ, R v4.2.2, ggplot2 v3.4.4]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **3.5.1**
- Evidence: Statistics and reproducibility Statistical analysis was performed as noted in the figure legends using R (R base (v.4.2.0 or later), ggplot2 (v.3.5.1), ggpubr (v.0.6.0) Seurat (v.5.0.1)) and GraphPad Prism (v.10.4.1).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Version used: **3.5.1**
- Evidence: The filtered number of DEGs ( P < 0.05 and log 2 [FC] > 0.1) in each cluster was recorded as a .csv file and then visualized using ggplot2 v.3.5.1.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Version used: **3.4.4**
- Evidence: All statistical analyses were performed using the R statistical environment (v.4.3.2), with R packages survival (v.3.5-7) and ggplot2 (v.3.4.4). scRNA-seq analysis of human PFA-EPN data Published PFA-EPN cohorts In addition to our newly generated scRNA-seq PFA database, we added published scRNA-seq PFA 10X Genomics samples from EGAS00001003170 (ref.
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: Spatial clustering was visualized by applying a 2D Gaussian kernel density estimator to the extracted coordinates using the stat_density_2d_filled() function from the ggplot2 package 81 in R (v4.3.1).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: The results were plotted as bar graphs with the ggplot2 package in R (v.4.2).
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Version used: **3.5.0**
- Evidence: We visualized results using ggplot2 (v.3.5.0).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **4.3.2**
- Evidence: Plots were generated with Python (v.3.9.7), R (v.3.6.1) and Rstudio (v.4.2.2), using ggplot2 (v.4.3.2), pheatmap (v.1.0.12), radarchart (v.0.7.5) and euler (v.6.1.1).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### CLCC1 governs ER bilayer equilibration to maintain lipid homeostasis. (Nature 2026)

- DOI: 10.1038/s41586-026-10161-y | PMCID: PMC13061606 | PMID: 41741642
- Evidence: The significant GO terms of the cellular component were visualized using the ggplot2 R package (v.3.4.4).
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [R] -> structure determination [IMOD] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX v1.7.1, Fiji, ImageJ]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **3.4.2**
- Evidence: UpSet plots were generated using the R packages UpSetR (v.1.4.0) 141 and ComplexUpset (v.1.3.3) 142 , 143 , boxplots and violin plots using ggplot2 (v.3.4.2) 144 , heatmaps using ComplexHeatmap (v.2.14.0) 145 and maps using leaflet (v.2.1.2) 146 .
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **3.4.2**
- Evidence: Postprocessing and data visualization were performed in R (v.4.4.1) using data.table (v.1.14.8), ggplot2 (v.3.4.2), pheatmap (v.1.0.12) and ComplexHeatmap (v.2.16.0).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Rising atmospheric CO&lt;sub&gt;2&lt;/sub&gt; reduces nitrogen availability in boreal forests. (Nature 2026)

- DOI: 10.1038/s41586-025-10039-5 | PMCID: PMC12916481 | PMID: 41709006
- Evidence: To enhance the visual differentiation of overlapping data points, the geom jitter function (ggplot2; ref.
- Full pipeline: normalisation [emmeans] -> stage not stated [R, ggplot2]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: UMAP plots were generated by calculating UMAP embeddings using Seurat and then plotting them as scatter plots using ggplot2.
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **3.5.1**
- Evidence: All statistics on TCGA-derived data were performed in R, and data visualization was done with ggplot2 (v.3.5.1) 80 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: 5d were acquired using the provided download function. scRNA-seq data analysis All plots and visualizations were performed using Seurat 76 v.4.1.1, ggpubr v.0.4.0 or ggplot2 (ref.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: Quantification and statistical analysis Data were plotted in R (version 4.4.2 (2024-06-14)) using the ggplot2, tidyr, dplyr, ggpubr and Hmisc toolkits (versions ggplot2_3.5.1, tidyr_1.3.1, dplyr_1.1.4, ggpubr_0.6.0, Hmisc_5.2.1), Python (version 3.12.9) using the pandas, scipy, scikit-learn, matplotlib and seaborn packages (versions pandas_2.2.3, scipy_1.14.1, scikit-learn_1.5.2, matplotlib_3.9.2,...
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Nutrient requirements of organ-specific metastasis in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09898-9 | PMCID: PMC12851942 | PMID: 41501456
- Version used: **3.4.3**
- Evidence: The analysis was conducted using R studio (v4.3.1), using the dplyr (v1.1.2) and ggplot2 (v3.4.3) packages for data processing and visualization, the boot package (v2019.6.0) for bootstrap confidence interval calculations, and the reshape2 package (v1.4.4) for data reshaping.
- Full pipeline: visualisation [ggplot2 v3.4.3, tidyverse v1.1.2]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: Density UMAP visualization was performed using the ggplot2 stat_density_2d() function. scRNA-seq and V(D)J-seq analyses of B16-OVA TILs B16-OVA were explanted at day +12 post-injection so that tumour sizes remained comparable between treatment groups.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### Decay of driver mutations shapes the landscape of intestinal transformation. (Nature 2026)

- DOI: 10.1038/s41586-025-09762-w | PMCID: PMC12804087 | PMID: 41339549
- Evidence: For data visualization, oncoprint (waterfall), copy-number frequency and copy-number spectral plots were designed using the GenVisR 97 package (v.1.34.0), while all other plots were designed using the ggplot2 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, R] -> quantification [QuPath] -> visualisation [ggplot2] -> stage not stated [VEP]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **3.5.1**
- Evidence: Data visualization was performed using ggplot2 (v.3.5.1), which is part of the tidyverse (v.2.0.0) suite of tools 81 .
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **3.5.1**
- Evidence: Boxplots were created using ggplot2 (v3.5.1 or v3.5.2) and ggbeeswarm (v0.7.2) with statistical annotation created by ggpubr (v0.6.0), method = ‘t-test’.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: Data were visualized using a combination of ggplot2 63 and cowplot 64 packages in R.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Cytosolic acetyl-coenzyme A is a signalling metabolite to control mitophagy. (Nature 2026)

- DOI: 10.1038/s41586-025-09745-x | PMCID: PMC12823391 | PMID: 41225001
- Evidence: Volcano plots for genome-wide and mitochondria-targeted analyses of the CRISPR screening were generated using the R package ggplot2.
- Full pipeline: quantification [Metascape] -> stage not stated [R, ggplot2]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Evidence: Both analyses were conducted in R using the packages vegan, car and ggplot2.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: All visualizations were generated using ggplot2 with coord_polar() for circular layout. cNMF factors derived from meta-analysis were then applied to Xenium in situ 5100-plex dataset, calculating activity scores for each cell in the spatial dataset.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Evidence: Map plotting Figure 1a was generated in R 111 v.4.3.2 with open-source packages dplyr 112 v1.1.4 , ggforce 113 v0.4.2 , ggnewscale 114 v0.4.10 , ggplot2 115 v3.4.4 , ggspatial 116 v1.1.9 , ggstar 117 v1.0.4 , ggrepel 118 v0.9.5 , paletteer 119 v1.3 , raster 120 v3.6-26 , rnaturalearth 121 v1.0.1 , sf 122 , 123 v1.0-15 , tidyterra v0.5.2 124 and terra 125 v1.7- 71, using Natural Earth ( https://www...
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: Results were plotted in R using the ggplot2 package.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **3.5.1**
- Evidence: Volcano plots were produced with custom code using ggplot2 (v.3.5.1).
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Measuring the buffering capacity of gene silencing in &lt;i&gt;Saccharomyces cerevisiae&lt;/i&gt;. (PNAS 2021)

- DOI: 10.1073/pnas.2111841118 | PMCID: PMC8670432 | PMID: 34857629
- Evidence: Data for ∼100 cells per time point were collected, compiled into a spreadsheet, and graphed using R software with ggplot2 package.
- Full pipeline: stage not stated [ImageJ, ggplot2]

### Genomic basis of fishing-associated selection varies with population density. (PNAS 2021)

- DOI: 10.1073/pnas.2020833118 | PMCID: PMC8713780 | PMID: 34903645
- Evidence: Statistical analyses were performed using Statistica 7 (Statsoft), and all visuals were created using ggplot2 in R v3.5.3.
- Full pipeline: read trimming [Cutadapt v1.16, Trimmomatic v0.36] -> alignment/mapping [ANGSD, BWA v0.7.17] -> differential/statistical testing [ggplot2] -> stage not stated [Picard v2.18.14, R v3.5, SnpEff v4.4]

### N6-methyladenosine (m<sup>6</sup>A) depletion regulates pluripotency exit by activating signaling pathways in embryonic stem cells. (PNAS 2021)

- DOI: 10.1073/pnas.2105192118 | PMCID: PMC8713808 | PMID: 34921114
- Evidence: Data processing and visualization of staining quantifications were done with RStudio (R version 3.6) and the ggplot2 package.
- Full pipeline: quantification [R v3.6, ggplot2] -> visualisation [R v3.6, ggplot2]

### Defective cytokinin signaling reprograms lipid and flavonoid gene-to-metabolite networks to mitigate high salinity in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2105021118 | PMCID: PMC8640937 | PMID: 34815339
- Evidence: A genotype–genotype correlation analysis based on Pcc was carried out using the “ggplot2” package in R v3.5.1.
- Full pipeline: alignment/mapping [clusterProfiler] -> variant calling [ggplot2] -> dimensionality reduction/clustering [R v3.5, clusterProfiler] -> visualisation [Cytoscape, igraph]

### Phytoplankton exudates and lysates support distinct microbial consortia with specialized metabolic and ecophysiological traits. (PNAS 2021)

- DOI: 10.1073/pnas.2101178118 | PMCID: PMC8521717 | PMID: 34620710
- Evidence: PCoAs were performed in R (version 3.4.0) using the function “ rca() ” from the package “vegan” ( 88 ), and resulting components were plotted with the package “ggplot2” ( 89 ).
- Full pipeline: alignment/mapping [Bowtie2] -> visualisation [R v3.4.0, ggplot2] -> stage not stated [SciPy]

### Emergent RNA-RNA interactions can promote stability in a facultative phototrophic endosymbiosis. (PNAS 2021)

- DOI: 10.1073/pnas.2108874118 | PMCID: PMC8463893 | PMID: 34521754
- Evidence: Size distributions of sRNA abundance for each sample were plotted using the R programming language packages tidyverse, grid.extra, and ggplot2 in R Studio. eDicer Methods for Identifying Putative RNA–RNA Interactions.
- Full pipeline: quality control [FastQC] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2] -> quantification [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [BLAST]

### Extracellular matrix protein N-glycosylation mediates immune self-tolerance in &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2021)

- DOI: 10.1073/pnas.2017460118 | PMCID: PMC8488588 | PMID: 34544850
- Evidence: Graphs were produced using the ggplot2 package ( 152 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [ggplot2]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Evidence: The packages of ggplot2, maptoos, and maps in R (v3.6.1) were used to mark the archaeological site locations of samples from the second plague pandemic.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself. (PNAS 2021)

- DOI: 10.1073/pnas.2100542118 | PMCID: PMC8449404 | PMID: 34507984
- Evidence: The probability density of expression values was plotted after determining the smoothed kernel density estimate by the ggplot2 R library.
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [R v3.6.3] -> visualisation [ComplexHeatmap, ggplot2, ggpubr] -> stage not stated [Clustal Omega v1.2]

### Trade-offs among transport, support, and storage in xylem from shrubs in a semiarid chaparral environment tested with structural equation modeling. (PNAS 2021)

- DOI: 10.1073/pnas.2104336118 | PMCID: PMC8379947 | PMID: 34389676
- Evidence: This was done using boxplots and violin plots (R package ggplot2) and by partitioning the variance of the measured traits among species nested within each site, across the different sites, and within each species (intraspecific; R package lme4 for mixed-effect models).
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.0.5, lavaan v0.6]

### Pro-inflammatory T helper 17 directly harms oligodendrocytes in neuroinflammation. (PNAS 2021)

- DOI: 10.1073/pnas.2025813118 | PMCID: PMC8403833 | PMID: 34417310
- Evidence: All data were analyzed using GraphPad Prism 6 (GraphPad Software) or R ( 88 ) using the ggplot2 package ( 89 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ggplot2]

### Cell-free reconstitution reveals the molecular mechanisms for the initiation of secondary siRNA biogenesis in plants. (PNAS 2021)

- DOI: 10.1073/pnas.2102889118 | PMCID: PMC8346886 | PMID: 34330830
- Evidence: Processed data were transferred to R, and length distribution and the 5′-end position for each siRNA were mapped onto the TAS3 mRNA using the ggplot2 package.
- Full pipeline: alignment/mapping [BEDTools, Cutadapt, SAMtools, ggplot2]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: The implementation relies significantly upon the R packages data.table ( 52 ), ggplot2 ( 53 ), ggspatial ( 54 ), rnaturalearth ( 55 ), and pheatmap ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Elucidation of an anaerobic pathway for metabolism of l-carnitine-derived γ-butyrobetaine to trimethylamine in human gut bacteria. (PNAS 2021)

- DOI: 10.1073/pnas.2101498118 | PMCID: PMC8364193 | PMID: 34362844
- Evidence: Plots and statistical analyses were performed using the ggplot2 package v3.3.2 ( 70 ) and R v3.6.0 ( 71 ).
- Full pipeline: alignment/mapping [MAFFT v7.455] -> dimensionality reduction/clustering [MAFFT v7.455] -> differential/statistical testing [R v3.6, ggplot2] -> visualisation [IQ-TREE v1.6.12] -> stage not stated [Prokka]

### Single-nuclear transcriptomics reveals diversity of proximal tubule cell states in a dynamic response to acute kidney injury. (PNAS 2021)

- DOI: 10.1073/pnas.2026684118 | PMCID: PMC8271768 | PMID: 34183416
- Version used: **3.3.2**
- Evidence: The R packages Seurat v.3.2.2 ( 18 ), ggplot2 v.3.3.2, Matrix v.2.3-18, and dplyr v.1.0.2 were used for preprocessing, data analysis, and visualization in R Studio (R version 3.6.3).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Monocle v0.2.3.0, SCENIC v1.1.2, STAR, UMAP] -> visualisation [Monocle v0.2.3.0, R v3.6.3, Seurat v3.2.2, ggplot2 v3.3.2, tidyverse v1.0.2]

### The DME demethylase regulates sporophyte gene expression, cell proliferation, differentiation, and meristem resurrection. (PNAS 2021)

- DOI: 10.1073/pnas.2026806118 | PMCID: PMC8307533 | PMID: 34266952
- Evidence: Volcano plots were plotted to visualize distribution of DEGs, using the R package ggplot2 ( 81 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0] -> visualisation [R, ggplot2] -> stage not stated [DESeq2, StringTie v2.1.3]

### Dopaminergic brainstem disconnection is common to pharmacological and pathological consciousness perturbation. (PNAS 2021)

- DOI: 10.1073/pnas.2026289118 | PMCID: PMC8325270 | PMID: 34301891
- Evidence: All correlations were performed using RStudio with ggplot2 for DoC patients and for propofol experiments with the rmcorr toolbox ( 65 ) using analysis of covariance to account for nonindependence among the repeated observations (awake, mild and moderate sedation, and recovery) by statistically adjusting for interindividual variability.
- Full pipeline: differential/statistical testing [ggplot2] -> stage not stated [CONN toolbox]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Evidence: The reads were counted in the regions of 1 kb along each sequence and the results were plotted by ggplot2 in R ( 72 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### Photosynthesis-independent production of reactive oxygen species in the rice bundle sheath during high light is mediated by NADPH oxidase. (PNAS 2021)

- DOI: 10.1073/pnas.2022702118 | PMCID: PMC8237631 | PMID: 34155141
- Evidence: Plots were generated with custom scripts in RStudio using the package ggplot2.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> quantification [ImageJ, Trimmomatic] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [ggplot2]

### LRRC8A-containing chloride channel is crucial for cell volume recovery and survival under hypertonic conditions. (PNAS 2021)

- DOI: 10.1073/pnas.2025013118 | PMCID: PMC8201826 | PMID: 34083438
- Version used: **3.1.0**
- Evidence: Statistical analyses of data generated with the genetic screening were performed using bash and R scripts; visualizations were done using the ggplot2 (v3.1.0) ( 63 ) and ggrepel (v0.8.0) ( 64 ) R packages.
- Full pipeline: differential/statistical testing [ggplot2 v3.1.0] -> visualisation [ggplot2 v3.1.0] -> stage not stated [GSEA]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Evidence: PCA data were replotted with the package ggplot2 ( 60 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Killed whole-genome reduced-bacteria surface-expressed coronavirus fusion peptide vaccines protect against disease in a porcine model. (PNAS 2021)

- DOI: 10.1073/pnas.2025622118 | PMCID: PMC8106328 | PMID: 33858942
- Evidence: Statistical analysis was done using R (v1.3.1093) with the Rstudio environment with included packages and the tidyverse and stats packages, with visualizations using ggplot2.
- Full pipeline: differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [ImageJ]

### Global inequality remotely sensed. (PNAS 2021)

- DOI: 10.1073/pnas.1919913118 | PMCID: PMC8106331 | PMID: 33903226
- Evidence: The analysis was carried out in R ( https://www.r-project.org ) using the packages raster, rasterVis, sp, rgdal, ggplot2, and mixtools and Python ( https://www.python.org/ ) using numpy, matplotlib, scipy, and statsmodels.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, statsmodels]

### Phylogenomic and ecological analyses reveal the spatiotemporal evolution of global pines. (PNAS 2021)

- DOI: 10.1073/pnas.2022302118 | PMCID: PMC8157994 | PMID: 33941644
- Evidence: The bar plots were implemented in the “ggplot2” package ( 97 ) using R (v.3.6.2) ( 84 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> dimensionality reduction/clustering [phytools v0.7] -> stage not stated [IQ-TREE v2.0, R v3.6.2, ggplot2]

### Signatures of immune dysfunction in HIV and HCV infection share features with chronic inflammation in aging and persist after viral reduction or elimination. (PNAS 2021)

- DOI: 10.1073/pnas.2022928118 | PMCID: PMC8040665 | PMID: 33811141
- Evidence: S2 were generated in R using the ggplot2 library, while the Venn diagram of functional categories was rendered with http://bioinformatics.psb.ugent.be/webtools/Venn .
- Full pipeline: normalisation [R] -> differential/statistical testing [R] -> visualisation [ggplot2]

### Incipient genome erosion and metabolic streamlining for antibiotic production in a defensive symbiont. (PNAS 2021)

- DOI: 10.1073/pnas.2023047118 | PMCID: PMC8092579 | PMID: 33883280
- Evidence: All other graphs were created using ggplot2 and ggpubr ( 97 ).
- Full pipeline: quality control [Bowtie2 v2.3.2, StringTie v1.3.3] -> read trimming [Bowtie2 v2.3.2, StringTie v1.3.3] -> alignment/mapping [Bowtie2 v2.3.2, StringTie v1.3.3] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [BLAST, ggplot2, ggpubr]

### TBK1 recruitment to STING activates both IRF3 and NF-κB that mediate immune defense against tumors and viral infections. (PNAS 2021)

- DOI: 10.1073/pnas.2100225118 | PMCID: PMC8040795 | PMID: 33785602
- Evidence: Bar plots were generated using the R package ggplot2. qRT-PCR.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [R v4.0.2, ggplot2]

### Estimating maximal microbial growth rates from cultures, metagenomes, and single cells via codon usage patterns. (PNAS 2021)

- DOI: 10.1073/pnas.2016810118 | PMCID: PMC8000110 | PMID: 33723043
- Evidence: All figures were made using R packages ggplot2 and ggpubr ( 81 , 82 ).
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [RAxML] -> visualisation [ggplot2, ggpubr] -> stage not stated [R, ape (R)]

### Sunlight exposure exerts immunomodulatory effects to reduce multiple sclerosis severity. (PNAS 2021)

- DOI: 10.1073/pnas.2018457118 | PMCID: PMC7817192 | PMID: 33376202
- Evidence: The remaining data were manipulated and plotted using the R packages tidyR , ggplot2 , and RColorBrewer .
- Full pipeline: quality control [PLINK v1.90] -> variant calling [PLINK v1.90] -> differential/statistical testing [R v3.6, lme4] -> visualisation [ggplot2] -> stage not stated [edgeR, kallisto]

### Microbial dynamics of elevated carbon flux in the open ocean's abyss. (PNAS 2021)

- DOI: 10.1073/pnas.2018269118 | PMCID: PMC7848738 | PMID: 33479184
- Evidence: Figures were generated using pheatmap ( 85 ) and ggplot2 ( 86 ) packages in R ( 79 ) and further refined using Adobe Illustrator.
- Full pipeline: read trimming [SPAdes] -> alignment/mapping [SPAdes] -> structure determination [SPAdes, ggplot2, pheatmap] -> visualisation [Cytoscape, ggplot2, pheatmap] -> stage not stated [BWA v0.7.15, R, WGCNA]

### Glacial meltwater determines the balance between autotrophic and heterotrophic processes in a Greenland fjord. (PNAS 2022)

- DOI: 10.1073/pnas.2207024119 | PMCID: PMC9907075 | PMID: 36534802
- Evidence: A correlation matrix based on data collected at the 10 sampling stations was created using the reshape2 ( 36 ) and ggplot2 ( 37 ) packages in the R program ( 38 ).
- Full pipeline: stage not stated [ggplot2]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: We made plots using ggplot2, cowplot, and pheatmap ( 110 – 113 ) and made extensive use of the tidyverse suite of R packages for data analysis ( 114 ).
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### The restart effect in social dilemmas shows humans are self-interested not altruistic. (PNAS 2022)

- DOI: 10.1073/pnas.2210082119 | PMCID: PMC9894210 | PMID: 36459646
- Evidence: We conducted analyses in RStudio ( 66 ), inputted the data with the zTree package ( 67 ), tested LMM significance with lmerTest ( 68 ), and made the data figures with ggplot2 ( 69 ).
- Full pipeline: stage not stated [ggplot2, lme4]

### Individuals prefer to harm their own group rather than help an opposing group. (PNAS 2022)

- DOI: 10.1073/pnas.2215633119 | PMCID: PMC9894232 | PMID: 36442089
- Version used: **3.3.5**
- Evidence: Data were analyzed using R, version 4.1.2, and the package ggplot2, version 3.3.5 ( 33 ).
- Full pipeline: stage not stated [ggplot2 v3.3.5]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: NMDS was performed using the Bray–Curtis dissimilarity matrix ( 51 ) between groups and visualized by using the ggplot2 package ( 52 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Functional genomics of OCTN2 variants informs protein-specific variant effect predictor for Carnitine Transporter Deficiency. (PNAS 2022)

- DOI: 10.1073/pnas.2210247119 | PMCID: PMC9674959 | PMID: 36343260
- Version used: **3.3.5**
- Evidence: Plots were generated using R package ggplot2 version 3.3.5.
- Full pipeline: differential/statistical testing [R v3.6.3] -> stage not stated [AlphaFold, ggplot2 v3.3.5]

### Why &lt;i&gt;Wolbachia&lt;/i&gt;-induced cytoplasmic incompatibility is so common. (PNAS 2022)

- DOI: 10.1073/pnas.2211637119 | PMCID: PMC9704703 | PMID: 36343219
- Evidence: Wolbachia population infection data with latitude and longitude were plotted in R using the package ggplot2 and Google Maps API.
- Full pipeline: visualisation [ggplot2] -> stage not stated [R]

### Spatial turnover of soil viral populations and genotypes overlain by cohesive responses to moisture in grasslands. (PNAS 2022)

- DOI: 10.1073/pnas.2209132119 | PMCID: PMC9659419 | PMID: 36322723
- Evidence: All plots were generated with ggplot2 ( 99 ).
- Full pipeline: read trimming [Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.4.2, SAMtools v1.11] -> quantification [DESeq2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [DESeq2, R v3.6] -> stage not stated [ggplot2, igraph]

### Pan-mitogenomics reveals the genetic basis of cytonuclear conflicts in citrus hybridization, domestication, and diversification. (PNAS 2022)

- DOI: 10.1073/pnas.2206076119 | PMCID: PMC9618123 | PMID: 36260744
- Evidence: The kinship matrix was computed in GEMMA with the parameter “-gk 2.” The regression analysis was performed based on the kinship matrix with the parameter “-lmm 4.” The output (adjusted P value) was plotted with R package ggplot2 ( 74 ).
- Full pipeline: dimensionality reduction/clustering [PLINK v1.90b, R] -> differential/statistical testing [Python, ggplot2] -> visualisation [PLINK v1.90b, R, ggplot2] -> stage not stated [GEMMA v0.98.5, IQ-TREE v2.0, SnpEff v5.1]

### Stunted children display ectopic small intestinal colonization by oral bacteria, which cause lipid malabsorption in experimental models. (PNAS 2022)

- DOI: 10.1073/pnas.2209589119 | PMCID: PMC9573096 | PMID: 36197997
- Evidence: Statistical analyses and visualizations of the microbial data were conducted in R version 3.4.1 using Phyloseq ( 52 ), vegan ( 53 ), DeSeq2 ( 54 ), and ggplot2 ( 55 ) packages.
- Full pipeline: differential/statistical testing [R v3.4.1, ggplot2] -> visualisation [R v3.4.1, ggplot2]

### Teeth, prenatal growth rates, and the evolution of human-like pregnancy in later <i>Homo</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2200689119 | PMCID: PMC9564099 | PMID: 36191229
- Evidence: All plots were made with the ggplot2 package ( 111 ), and averages and log-transformed values were calculated with the dplyr package ( 112 ).
- Full pipeline: differential/statistical testing [R v4.1.2] -> visualisation [R v4.1.2] -> stage not stated [ggplot2, tidyverse]

### A single helix repression domain is functional across diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2206986119 | PMCID: PMC9564828 | PMID: 36191192
- Evidence: Data from at least two independent replicates were combined and plotted in R ( https://ggplot2.tidyverse.org/ ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> normalisation [ImageJ] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### Biosensors for inflammation as a strategy to engineer regulatory T cells for cell therapy. (PNAS 2022)

- DOI: 10.1073/pnas.2208436119 | PMCID: PMC9546553 | PMID: 36161919
- Evidence: Plots were created with ggplot2 and EnhancedVolcano ( 51 ).
- Full pipeline: quality control [DESeq2] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [fgsea, ggplot2]

### Evolution of the ancestral mammalian karyotype and syntenic regions. (PNAS 2022)

- DOI: 10.1073/pnas.2209139119 | PMCID: PMC9550189 | PMID: 36161960
- Evidence: Results were visualized using the ggplot2 ( 78 ) R package.
- Full pipeline: structure determination [BUSCO v5.2.2] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.29.0]

### Using neuroimaging genomics to investigate the evolution of human brain structure. (PNAS 2022)

- DOI: 10.1073/pnas.2200638119 | PMCID: PMC9546597 | PMID: 36161899
- Evidence: Plots were generated using R packages plotly and ggplot2.
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [LDSC] -> stage not stated [FreeSurfer, PLINK, R, ggplot2]

### Late Pleistocene megafauna extinction leads to missing pieces of ecological space in a North American mammal community. (PNAS 2022)

- DOI: 10.1073/pnas.2115015119 | PMCID: PMC9522422 | PMID: 36122233
- Evidence: Plots were created using base R or package ggplot2 ( 101 ).
- Full pipeline: stage not stated [ImageJ, ggplot2]

### Truncated Tau caused by intron retention is enriched in Alzheimer's disease cortex and exhibits altered biochemical properties. (PNAS 2022)

- DOI: 10.1073/pnas.2204179119 | PMCID: PMC9477417 | PMID: 36067305
- Evidence: Normalized IR ratio from individual human subject determined from DESeq2 was used to generate dot plot with “ggplot” function in “ggplot2” package ( https://ggplot2.tidyverse.org ).
- Full pipeline: normalisation [ggplot2, tidyverse] -> differential/statistical testing [DESeq2, featureCounts v2.0.1]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; sine oculis/SIX-type homeobox genes act as homeotic switches to define neuronal subtype identities. (PNAS 2022)

- DOI: 10.1073/pnas.2206817119 | PMCID: PMC9478639 | PMID: 36067313
- Evidence: We used the R tidyverse package collection and the ggplot2 graph library.
- Full pipeline: stage not stated [ImageJ, ggplot2, tidyverse]

### Different classes of genomic inserts contribute to human antibody diversity. (PNAS 2022)

- DOI: 10.1073/pnas.2205470119 | PMCID: PMC9457163 | PMID: 36037353
- Evidence: Plots were created using ggplot2 and gridExtra packages in R 3.6.2 ( 73 ).
- Full pipeline: quality control [FastQC] -> read trimming [R, Trim Galore, Trimmomatic] -> alignment/mapping [R, Trimmomatic] -> stage not stated [BEDTools, MACS2, ggplot2]

### Strategic intergroup alliances increase access to a contested resource in male bottlenose dolphins. (PNAS 2022)

- DOI: 10.1073/pnas.2121723119 | PMCID: PMC9457541 | PMID: 36037370
- Evidence: We used the DHARMa package ( 70 ) to assess model fit, and we used the effects ( 69 ) and ggplot2 ( 71 ) packages in R to plot model estimates over the raw data.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, ggplot2]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Evidence: Data plots were generated using the R package ggplot2 ( 72 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### Wildlife susceptibility to infectious diseases at global scales. (PNAS 2022)

- DOI: 10.1073/pnas.2122851119 | PMCID: PMC9436312 | PMID: 35994656
- Evidence: To calculate this ellipsoid we used the dataEllipse function of the R package car ( 91 ) implemented in the stat_elipse function of the ggplot2 package ( 92 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [ape (R), ggplot2, phytools]

### Blocking CHOP-dependent TXNIP shuttling to mitochondria attenuates albuminuria and mitigates kidney injury in nephrotic syndrome. (PNAS 2022)

- DOI: 10.1073/pnas.2116505119 | PMCID: PMC9436335 | PMID: 35994650
- Evidence: Control” and “Proteinuria” were filtered for P < 0.05 and fold change > 1.5, and the graph was visualized using ggplot2.
- Full pipeline: visualisation [ggplot2]

### Targeting of microvillus protein Eps8 by the NleH effector kinases from enteropathogenic &lt;i&gt;E. coli&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2204332119 | PMCID: PMC9407544 | PMID: 35976880
- Evidence: For LFQ comparisons, missing values were imputed with a standard derivation of 0.3σ and a downshift of 2.5σ in Perseus, with resulting data visualized with ggplot2 within R.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ggplot2]

### The glioblastoma multiforme tumor site promotes the commitment of tumor-infiltrating lymphocytes to the T&lt;sub&gt;H&lt;/sub&gt;17 lineage in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2206208119 | PMCID: PMC9407554 | PMID: 35969754
- Version used: **3.3.5**
- Evidence: Data from RNA-seq were processed in R version 4.1.0 (2021-05-18) using DESeq2 (v1.32.0), openxlsx (v4.2.4), ggplot2 (v3.3.5), and dplyr (v1.0.7).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2 v1.32.0, GSEA, GSVA, R v4.1.0, ggplot2 v3.3.5, tidyverse v1.0.7]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Evidence: We collected the geographic coordinates of the samples and mapped the minimal inferred ranges of the study species using the geom_sf function from the R ggplot2 package (v.3.3.2; R Core Team, 2020).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### The evolution of mating preferences for genetic attractiveness and quality in the presence of sensory bias. (PNAS 2022)

- DOI: 10.1073/pnas.2206262119 | PMCID: PMC9388091 | PMID: 35939704
- Evidence: We then smoothed these estimates with respect to generation using LOESS regression (R package ggplot2) ( 55 ).
- Full pipeline: differential/statistical testing [R, ggplot2]

### Number neurons in the nidopallium of young domestic chicks. (PNAS 2022)

- DOI: 10.1073/pnas.2201039119 | PMCID: PMC9371667 | PMID: 35917348
- Evidence: All statistical analyses and visualization of the data were performed in R ( 65 ) with packages “tidyverse,” “ggplot2,” and “PMCMRplus” and in MATLAB using custom-made scripts and the Curve Fitting Toolbox.
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> visualisation [R, ggplot2, tidyverse] -> stage not stated [PsychoPy]

### P38α MAPK is a gatekeeper of uterine progesterone responsiveness at peri-implantation via Ube3c-mediated PGR degradation. (PNAS 2022)

- DOI: 10.1073/pnas.2206000119 | PMCID: PMC9371708 | PMID: 35914132
- Evidence: The visualization of RNA-Seq data were done by ggplot2 package in R.
- Full pipeline: alignment/mapping [edgeR v3.9] -> quantification [edgeR v3.9] -> normalisation [edgeR v3.9] -> differential/statistical testing [edgeR v3.9] -> visualisation [ggplot2]

### High-dimensional immune profiling identifies a biomarker to monitor dimethyl fumarate response in multiple sclerosis. (PNAS 2022)

- DOI: 10.1073/pnas.2205042119 | PMCID: PMC9351505 | PMID: 35881799
- Evidence: All plots were drawn using ggplot2.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ggplot2]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; induces a muted host response in human blood that blunts the recruitment of neutrophils. (PNAS 2022)

- DOI: 10.1073/pnas.2123017119 | PMCID: PMC9351360 | PMID: 35881802
- Evidence: Visualization was performed by using R packages ggplot2 ( 65 ), ComplexHeatmap ( 66 ), and ggVennDiagram ( 67 ).
- Full pipeline: alignment/mapping [Bowtie2 v3.1, HTSeq] -> differential/statistical testing [DESeq2, R v3.5.1] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [limma]

### Infants infer potential social partners by observing the interactions of their parent with unknown others. (PNAS 2022)

- DOI: 10.1073/pnas.2121390119 | PMCID: PMC9371719 | PMID: 35878009
- Evidence: ( B : Infants’ reaching for the imitated puppet (study 1, stacked bars) and proportion of time looking at the imitated puppet (studies 2 and 3, box plots; white dots are means, black bars are medians; connected dots are a single infant’s data; boxplots made with ggplot2 ( 27 ).
- Full pipeline: stage not stated [ggplot2]

### Organellar transcripts dominate the cellular mRNA pool across plants of varying ploidy levels. (PNAS 2022)

- DOI: 10.1073/pnas.2204187119 | PMCID: PMC9335225 | PMID: 35858449
- Evidence: Data visualizations were generated with the ggplot2 and ggridges packages.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R v3.5, emmeans] -> visualisation [ggplot2] -> stage not stated [lme4]

### Motor learning without movement. (PNAS 2022)

- DOI: 10.1073/pnas.2204379119 | PMCID: PMC9335319 | PMID: 35858450
- Evidence: Statistical tests were conducted in R (version 4.0.3): packages rstatix ( 71 ), coin ( 72 ), MuMIn ( 73 ), lmerTest ( 74 ), lme4 ( 75 ), r2glmm ( 76 ), emmeans ( 77 ), effsize ( 78 ), effectsize ( 79 ), magrittr ( 80 ), ggplot2 ( 81 ), ggpubr ( 82 ), and ggeffects ( 83 ).
- Full pipeline: differential/statistical testing [R v4.0.3, emmeans, ggplot2, ggpubr, lme4] -> stage not stated [Python v3.8.5]

### Developmental constraints enforce altruism and avert the tragedy of the commons in a social microbe. (PNAS 2022)

- DOI: 10.1073/pnas.2111233119 | PMCID: PMC9303850 | PMID: 35858311
- Evidence: All other figures were plotted using the package ggplot2 in R.
- Full pipeline: visualisation [ggplot2]

### Generalizing Bayesian phylogenetics to infer shared evolutionary events. (PNAS 2022)

- DOI: 10.1073/pnas.2121036119 | PMCID: PMC9304017 | PMID: 35858351
- Evidence: Created using ggplot2 [v3.3.5 ( 53 )], ggtree [v3.1.0 ( 54 )], treeio [v1.17.0 ( 55 )], deeptime [v0.0.6 ( 56 )], cowplot [v1.1.1 ( 57 )], and ggrepel [v0.9.1 ( 58 )].
- Full pipeline: stage not stated [ggplot2]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **3.3.5**
- Evidence: GOs were determined using Enrichr, and significant GO terms with P values of <0.01 were selected for visualization using ggplot2 (v3.3.5) and GOplot (v1.0.2).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### STING activation promotes robust immune response and NK cell-mediated tumor regression in glioblastoma models. (PNAS 2022)

- DOI: 10.1073/pnas.2111003119 | PMCID: PMC9282249 | PMID: 35787058
- Evidence: A volcano plot showing log 2 fold change and –log 10 (adjusted P value) was then generated from the differential expression analysis in ggplot2.
- Full pipeline: alignment/mapping [STAR] -> quantification [QuPath] -> differential/statistical testing [DESeq2, R, ggplot2] -> stage not stated [Enrichr, ImageJ]

### Early human B cell signatures of the primary antibody response to mRNA vaccination. (PNAS 2022)

- DOI: 10.1073/pnas.2204607119 | PMCID: PMC9282446 | PMID: 35759653
- Version used: **3.3.3**
- Evidence: Densities of antibody concentrations at endpoint (v2D28) were estimated via a Gaussian kernel with bandwidth automatically selected through biased cross-validation by the stat_density function from ggplot2 (3.3.3) with bw = “bcv”.
- Full pipeline: dimensionality reduction/clustering [R v4.0.2, UMAP] -> differential/statistical testing [lme4 v1.1.26] -> machine learning [ggplot2 v3.3.3]

### Revealing the recent demographic history of Europe via haplotype sharing in the UK Biobank. (PNAS 2022)

- DOI: 10.1073/pnas.2119281119 | PMCID: PMC9233301 | PMID: 35696575
- Evidence: Plots were generated using the ggplot2 package ( 65 ) in the R statistical computing language ( 59 ).
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [ADMIXTURE, PLINK, R] -> differential/statistical testing [R, ggplot2, igraph]

### Hot and dry conditions predict shorter nestling telomeres in an endangered songbird: Implications for population persistence. (PNAS 2022)

- DOI: 10.1073/pnas.2122944119 | PMCID: PMC9231487 | PMID: 35696588
- Evidence: Statistical analyses were conducted in R version 3.5.1 ( 77 ) and graphically presented using the packages ggplot2 and ggtern ( 78 , 79 ).
- Full pipeline: differential/statistical testing [R v3.5.1, ggplot2, lme4]

### SpyChIP identifies cell type-specific transcription factor occupancy from complex tissues. (PNAS 2022)

- DOI: 10.1073/pnas.2122900119 | PMCID: PMC9231492 | PMID: 35696584
- Evidence: Heatmaps were generated using deeptools2 ( 19 ) (also on usegalaxy.eu), and scatter plots were generated using the R package ggplot2. de novo motif searches were performed using Homer ( 20 ), and all parameters were default except -size 80.
- Full pipeline: alignment/mapping [Bowtie2, MACS2] -> stage not stated [R, ggplot2]

### Vagus nerve stimulation promotes resolution of inflammation by a mechanism that involves Alox15 and requires the α7nAChR subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2023285119 | PMCID: PMC9295760 | PMID: 35622894
- Evidence: R package ggplot2 was used for visualization of ODE and linear models (H.
- Full pipeline: normalisation [Cytoscape] -> differential/statistical testing [R, ggplot2] -> visualisation [R, ggplot2]

### Stabilizing microbial communities by looped mass transfer. (PNAS 2022)

- DOI: 10.1073/pnas.2117814119 | PMCID: PMC9169928 | PMID: 35446625
- Version used: **3.3.0**
- Evidence: The graphical work was supported by the R package ggplot2 v3.3.0 ( 89 ).
- Full pipeline: stage not stated [R v3.6, ggplot2 v3.3.0]

### Estimating bonobo (<i>Pan</i><i>paniscus</i>) and chimpanzee (<i>Pan</i><i>troglodytes</i>) evolutionary history from nucleotide site patterns. (PNAS 2022)

- DOI: 10.1073/pnas.2200858119 | PMCID: PMC9170072 | PMID: 35452306
- Version used: **3.3.3**
- Evidence: Many figures were generated in R using ggplot2, version 3.3.3 ( 87 ).
- Full pipeline: visualisation [ggplot2 v3.3.3] -> stage not stated [BCFtools, Conda, Jupyter, Snakemake]

### Gradual domestication of root traits in the earliest maize from Tehuacán. (PNAS 2022)

- DOI: 10.1073/pnas.2110245119 | PMCID: PMC9169935 | PMID: 35446704
- Evidence: Graphs were created with the ggplot2 package ( 43 , 44 ).
- Full pipeline: stage not stated [ggplot2]

### MoSBi: Automated signature mining for molecular stratification and subtyping. (PNAS 2022)

- DOI: 10.1073/pnas.2118210119 | PMCID: PMC9169782 | PMID: 35412913
- Evidence: All other visualizations use the “ggplot2” library in R.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [Cytoscape, Docker, R]

### Stone Age <i>Yersinia pestis</i> genomes shed light on the early evolution, diversity, and ecology of plague. (PNAS 2022)

- DOI: 10.1073/pnas.2116722119 | PMCID: PMC9169917 | PMID: 35412864
- Evidence: The results were plotted in R ( 43 ) using the ggplot2 package ( 39 ).
- Full pipeline: variant calling [GATK, Picard] -> differential/statistical testing [GATK, Picard] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.25.0, RAxML v0.9.0, ggpubr]

### Infrastructure inequality is a characteristic of urbanization. (PNAS 2022)

- DOI: 10.1073/pnas.2119890119 | PMCID: PMC9169802 | PMID: 35377809
- Evidence: We analyzed the data in R ( https://www.r-project.org/ ) using ggplot2, sf, rgdal, Hmisc, spdep, spatialreg, raster, tmap, and dplyr packages and in python ( https://www.python.org/ ) programming languages using numpy, scipy, pandas, geopandas, osgeo, scikit-image, matplotlib, and rasterio packages.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, scikit-image, tidyverse]

### Neutrophil and natural killer cell imbalances prevent muscle stem cell-mediated regeneration following murine volumetric muscle loss. (PNAS 2022)

- DOI: 10.1073/pnas.2111445119 | PMCID: PMC9169656 | PMID: 35377804
- Evidence: Seurat and ggplot2 were used for data visualization.
- Full pipeline: dimensionality reduction/clustering [UMAP, scVelo] -> simulation/modelling [scVelo] -> visualisation [ggplot2] -> stage not stated [ImageJ, Seurat, velocyto]

### Early evolution of diurnal habits in owls (Aves, Strigiformes) documented by a new and exquisitely preserved Miocene owl fossil from China. (PNAS 2022)

- DOI: 10.1073/pnas.2119217119 | PMCID: PMC9169863 | PMID: 35344399
- Evidence: 3 , using the package ggplot2 [R package ( 57 )] with the average reconstruction of the orbit and eye dimensions.
- Full pipeline: structure determination [R, ggplot2] -> stage not stated [MrBayes, phytools]

### A vasculature niche orchestrates stromal cell phenotype through PDGF signaling: Importance in human fibrotic disease. (PNAS 2022)

- DOI: 10.1073/pnas.2120336119 | PMCID: PMC9060460 | PMID: 35320046
- Evidence: Visualization was performed using the R packages ggplot2 and igraph ( 15 , 19 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [CellPhoneDB, R, Seurat]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: All statistical analyses were performed and visualized in R ( http://www.R-project.org ) using the ggplot2 ( 80 ), genoPlotR ( 81 ), phyloseq ( 82 ), dunn.test ( 83 ), and vegan ( 84 ) packages.
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Triglyceride breakdown from lipid droplets regulates the inflammatory response in macrophages. (PNAS 2022)

- DOI: 10.1073/pnas.2114739119 | PMCID: PMC8944848 | PMID: 35302892
- Evidence: Analysis and visualization for the Olink data were performed with the R language (CRAN; RRID: SCR_003005; https://www.r-project.org ) using the packages ggbiplot (PCA) and ggplot2 (volcano plots).
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> visualisation [ggplot2] -> stage not stated [CellProfiler]

### Parkinson's disease and multiple system atrophy patient iPSC-derived oligodendrocytes exhibit alpha-synuclein-induced changes in maturation and immune reactive properties. (PNAS 2022)

- DOI: 10.1073/pnas.2111405119 | PMCID: PMC8944747 | PMID: 35294277
- Version used: **3.3.0**
- Evidence: Volcano plots of log P value against log fold change were done using ggplot2 version 3.3.0 ( 80 ).
- Full pipeline: differential/statistical testing [ggplot2 v3.3.0] -> stage not stated [ComplexHeatmap v2.4.3, Cytoscape, GSEA]

### Landscape of surfaceome and endocytome in human glioma is divergent and depends on cellular spatial organization. (PNAS 2022)

- DOI: 10.1073/pnas.2114456119 | PMCID: PMC8892282 | PMID: 35217608
- Evidence: Bioinformatics analyses were conducted in R version 4.0.4 and figures were generated using the packages ggplot2, RColorBrewer, viridis, VennDiagram, venneuler (in combination with http://bioinformatics.psb.ugent.be/cgi-bin/liste/Venn/calculate_venn.htpl to perform six-group overlap comparison), and pheatmap (clustering method used was “ward.D2”).
- Full pipeline: dimensionality reduction/clustering [R v4.0.4, ggplot2, pheatmap] -> visualisation [R v4.0.4, ggplot2, pheatmap] -> stage not stated [GSEA]

### Kin selection for cooperation in natural bacterial populations. (PNAS 2022)

- DOI: 10.1073/pnas.2119070119 | PMCID: PMC8892524 | PMID: 35193981
- Evidence: Results figures were all produced using the ggplot2 package in R ( 96 ).
- Full pipeline: visualisation [R, ggplot2] -> stage not stated [eggNOG]

### A widely distributed phosphate-insensitive phosphatase presents a route for rapid organophosphorus remineralization in the biosphere. (PNAS 2022)

- DOI: 10.1073/pnas.2118122119 | PMCID: PMC8812569 | PMID: 35082153
- Evidence: All statistical analyses and data visualizations were performed using the ggplot2, ggfortify, tidyr, plyr, serration, and rcolorbrewer packages in Rstudio (1.2.5033).
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [BLAST] -> differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [HMMER, IQ-TREE]

### Impact of ADAR-induced editing of minor viral RNA populations on replication and transmission of SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2112663119 | PMCID: PMC8833170 | PMID: 35064076
- Evidence: Data handling, statistical analyses, and graphical representation were performed in R, version 4.0.3 (packages tidyverse, naniar, tableone and ggplot2) ( 36 , 37 ) and in MS Excel.
- Full pipeline: differential/statistical testing [ggplot2, tidyverse] -> stage not stated [Python]

### In vitro cell cycle oscillations exhibit a robust and hysteretic response to changes in cytoplasmic density. (PNAS 2022)

- DOI: 10.1073/pnas.2109547119 | PMCID: PMC8832984 | PMID: 35101974
- Evidence: Package ggplot2 in Rstudio 1.2.5019 was installed and utilized.
- Full pipeline: differential/statistical testing [Python v3.7.10, scikit-learn v0.22.2] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [ggplot2]

### Kelp-forest dynamics controlled by substrate complexity. (PNAS 2022)

- DOI: 10.1073/pnas.2103483119 | PMCID: PMC8872774 | PMID: 35181602
- Evidence: Stability landscapes were represented as kernel density plots using the geom_density function of ggplot2 ( 71 ) with the default bandwidth (adjust = 1.0 ) for all but the two WestEnd sites (adjust = 0.8 , to better visualize the algal-only state); other bandwidths produced qualitatively similar results.
- Full pipeline: normalisation [vegan v2.5] -> dimensionality reduction/clustering [vegan v2.5] -> visualisation [ggplot2] -> stage not stated [R]

### Transmission potential of human schistosomes can be driven by resource competition among snail intermediate hosts. (PNAS 2022)

- DOI: 10.1073/pnas.2116512119 | PMCID: PMC8833218 | PMID: 35121663
- Evidence: We produced all figures using the ggplot2 and cowplot packages ( 57 , 58 ).
- Full pipeline: stage not stated [ImageJ, ggplot2]

### THESEUS1 modulates cell wall stiffness and abscisic acid production in <i>Arabidopsis thaliana</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2119258119 | PMCID: PMC8740707 | PMID: 34949719
- Evidence: Regression curves were fitted for each graph using smooth conditional medias (from ggplot2 R package) calculated using local polynomial regression fitting (LOESS) method.
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [Fiji, ImageJ]

### Template switching in DNA replication can create and maintain RNA hairpins. (PNAS 2022)

- DOI: 10.1073/pnas.2107005119 | PMCID: PMC8794818 | PMID: 35046021
- Evidence: Mutation types in the stems (base pair in parent vs. child) were counted separately for instantaneous and two-step CMs, and the counts were visualized as a heat map using the R package ggplot2.
- Full pipeline: read trimming [MAFFT v7.310] -> alignment/mapping [BLAST v2.6.0, MAFFT v7.310] -> dimensionality reduction/clustering [MAFFT v7.310] -> visualisation [R, ggplot2] -> stage not stated [IQ-TREE v1.6.1]

### B cell-derived IL-27 promotes control of persistent LCMV infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116741119 | PMCID: PMC8784116 | PMID: 35022243
- Evidence: Packages ggplot2 and ComplexHeatmap were used for additional plotting.
- Full pipeline: read trimming [Seurat v4.0.3] -> dimensionality reduction/clustering [Seurat v4.0.3, UMAP] -> differential/statistical testing [Seurat v4.0.3] -> stage not stated [ComplexHeatmap, R v4.1.0, ggplot2]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Evidence: Homozygous SNP variants were plotted using the R package ggplot2 ( 79 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Version used: **3.3.2**
- Evidence: ... version 1.3.1, dplyr version 1.0.2, tidyr version 1.1.2, tibble version 3.0.3, purrr version 0.3.4, ggsunburst version 0.3.0, zeallot version 0.1.0, ggplot2 version 3.3.2, and reshape version 0.8.8 ( 61 – 71 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **3.3.6**
- Evidence: Packages ggplot2 v3.3.6, ggpubr v0.4.0 pheatmap v1.0.12, RColorBrewer v1.1-3, ggsignif v0.6.3, and tidyverse v1.3.1 were used for data manipulation and representation.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Generation of de novo miRNAs from template switching during DNA replication. (PNAS 2023)

- DOI: 10.1073/pnas.2310752120 | PMCID: PMC10710096 | PMID: 38019864
- Evidence: Boxplots were drawn from the results using the R package ggplot2 ( 57 ).
- Full pipeline: stage not stated [BEDTools v2.26.0, Matplotlib v3.5.1, Python, R, ggplot2, seaborn v0.11.2]

### Proteome-wide tagging with an H&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;2&lt;/sub&gt; biosensor reveals highly localized and dynamic redox microenvironments. (PNAS 2023)

- DOI: 10.1073/pnas.2314043120 | PMCID: PMC10691247 | PMID: 37991942
- Evidence: Packages used for reading, tidying, and analysis of data included ggplot2 from the tidyverse ( 29 ).
- Full pipeline: stage not stated [ggplot2, ggpubr, tidyverse]

### Salicylic acid and RNA interference mediate antiviral immunity of plant stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302069120 | PMCID: PMC10589665 | PMID: 37824524
- Evidence: Visualization of the data was done by using the packages tidyverse ( 55 ) and ggplot2 ( 56 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2 v2.3.5] -> visualisation [Bioconductor, ggplot2, tidyverse] -> stage not stated [DESeq2, ImageJ, featureCounts]

### Context-dependent function of the transcriptional regulator Rap1 in gene silencing and activation in <i>Saccharomyces cerevisiae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2304343120 | PMCID: PMC10556627 | PMID: 37769255
- Evidence: All displays of ChIP-seq normalized coverage over a defined region were displayed using a custom Rscript and ggplot2 available on the associated GitHub.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [ggplot2] -> stage not stated [MACS2]

### Engineered bone marrow as a clinically relevant ex vivo model for primary bone cancer research and drug screening. (PNAS 2023)

- DOI: 10.1073/pnas.2302101120 | PMCID: PMC10523456 | PMID: 37729195
- Evidence: PCA plot and heatmaps were generated using R packages ggfortify and ggplot2, respectively.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [limma]

### Resistance to host antimicrobial peptides mediates resilience of gut commensals during infection and aging in <i>Drosophila</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2305649120 | PMCID: PMC10483595 | PMID: 37639605
- Evidence: The R packages ggplot2, dplyr, and tidyverse were used for data visualization.
- Full pipeline: differential/statistical testing [R v4.2] -> visualisation [ggplot2, tidyverse] -> stage not stated [survival (R)]

### Explanations for latitudinal diversity gradients must invoke rate variation. (PNAS 2023)

- DOI: 10.1073/pnas.2306220120 | PMCID: PMC10433455 | PMID: 37535654
- Evidence: Maps were constructed in R v.4.2.1 using the sf package ( 42 ) and ggplot2 ( 43 ).
- Full pipeline: stage not stated [ggplot2]

### Optogenetic clustering and membrane translocation of the BcLOV4 photoreceptor. (PNAS 2023)

- DOI: 10.1073/pnas.2221615120 | PMCID: PMC10410727 | PMID: 37527339
- Evidence: The obtained values were exported into R (version 4.2.2) for data analysis using the dplyr ( 52 ) and ggplot2 ( 53 ) packages.
- Full pipeline: stage not stated [CellProfiler, ImageJ, R v4.2.2, ggplot2, tidyverse]

### Engineered calprotectin-sensing probiotics for IBD surveillance in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2221121120 | PMCID: PMC10410751 | PMID: 37523538
- Version used: **3.3.0**
- Evidence: Plots were made in R (v4.0.3) using ggplot2 (v3.3.0), pheatmap (v1.0.12).
- Full pipeline: alignment/mapping [STAR v2.7.5] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [R v4.0.3, ggplot2 v3.3.0, pheatmap v1.0.12]

### Host hydrocarbons protect symbiont transmission from a radical host defense. (PNAS 2023)

- DOI: 10.1073/pnas.2302721120 | PMCID: PMC10400980 | PMID: 37487102
- Evidence: For subsequent visualization of the data in ggplot2, LFC shrinkage was applied using the “apeglm” shrinkage estimator.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> differential/statistical testing [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> visualisation [ggplot2]

### Threatened North African seagrass meadows have supported green turtle populations for millennia. (PNAS 2023)

- DOI: 10.1073/pnas.2220747120 | PMCID: PMC10372671 | PMID: 37459551
- Evidence: RStudio ( 73 ), specifically ggplot2 ( 74 ), was used for plotting ZooMS and stable isotope data.
- Full pipeline: stage not stated [ggplot2]

### A simple mechanism for collective decision-making in the absence of payoff information. (PNAS 2023)

- DOI: 10.1073/pnas.2216217120 | PMCID: PMC10629567 | PMID: 37428910
- Evidence: All data manipulation and statistical analyses were performed in R ( 73 ) (version 4.2.1) using the packages glmmTMB ( 74 ) (version 1.1.4), lme4 ( 75 ) (version 1.1-30), lmerTest ( 76 ) (version 3.1-3), DHARMa ( 77 ) (version 0.4.5), ggplot2 ( 78 ) (version 3.3.6), tidyr ( 79 ) (version 1.2.0), dplyr ( 80 ) (version 1.0.10), readr ( 81 ) (version 2.1.2), ggeffects ( 82 ) (version 1.1.3), survmine...
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.2.1, data.table, survival (R), tidyverse]

### Functional calcium-responsive parathyroid glands generated using single-step blastocyst complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2216564120 | PMCID: PMC10334775 | PMID: 37379351
- Evidence: Normalization and DEG analysis were performed using DESeq2 in Galaxy and visualized using ggplot2 in R v4.1.2.
- Full pipeline: normalisation [DESeq2, R v4.1, ggplot2] -> dimensionality reduction/clustering [UMAP] -> visualisation [DESeq2, R v4.1, ggplot2] -> stage not stated [Seurat v4.2.1, tidyverse]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Version used: **3.3.6**
- Evidence: Plots were generated using matplotlib v3.3.2, seaborn v0.11.0, and ggplot2 v3.3.6.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: Heatmaps were produced using the pheatmap R package ( https://github.com/raivokolde/pheatmap ), lattice ( http://lattice.r-forge.r-project.org/ ) or ggplot2 ( https://ggplot2.tidyverse.org ) packages.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: Scatter plots, bar plots, and density plots were created using the R package ggplot2 ( 65 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Chitin utilization by marine picocyanobacteria and the evolution of a planktonic lifestyle. (PNAS 2023)

- DOI: 10.1073/pnas.2213271120 | PMCID: PMC10194020 | PMID: 37159478
- Evidence: Gene expression results were visualized with ggplot2 ( 72 ).
- Full pipeline: alignment/mapping [HTSeq, MAFFT] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2] -> stage not stated [BLAST]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Graphical visualizations used the gplots, tidyverse, and ggplot2 packages.
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Switch-like compaction of poly(ADP-ribose) upon cation binding. (PNAS 2023)

- DOI: 10.1073/pnas.2215068120 | PMCID: PMC10175808 | PMID: 37126687
- Evidence: Then, the data were plotted using the ggplot2 package in RStudio ( 71 ).
- Full pipeline: visualisation [PyMOL, ggplot2]

### Climate change, tree demography, and thermophilization in western US forests. (PNAS 2023)

- DOI: 10.1073/pnas.2301754120 | PMCID: PMC10161004 | PMID: 37094127
- Evidence: We used R software for all data processing, analysis, and visualization, including the following packages: raster ( 44 ), R-INLA ( 45 ), mgcv ( 35 ), ggplot2 ( 46 ), patchwork ( 47 ), ncdf4 ( 48 ), foreach ( 49 ), doParallel ( 50 ), rgdal ( 51 ), spData ( 52 ), sf ( 53 ), adehabitatHR ( 54 ), rgeos ( 55 ), usdm ( 56 ), and rcartocolor ( 57 ).
- Full pipeline: visualisation [ggplot2] -> stage not stated [R]

### Ancient DNA from a lost Negev Highlands desert grape reveals a Late Antiquity wine lineage. (PNAS 2023)

- DOI: 10.1073/pnas.2213563120 | PMCID: PMC10151551 | PMID: 37068234
- Evidence: The results were plotted using the R packages factoextra and ggplot2.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.5] -> variant calling [GATK, VCFtools] -> dimensionality reduction/clustering [pheatmap] -> visualisation [ggplot2]

### Genetic factors predict hybrid formation in the British flora. (PNAS 2023)

- DOI: 10.1073/pnas.2220261120 | PMCID: PMC10120012 | PMID: 37040419
- Evidence: Other plots were generated with the R package ggplot2 ( 53 ) and lattice ( 54 ).
- Full pipeline: visualisation [R] -> stage not stated [IQ-TREE, Python, data.table, ggplot2, tidyverse]

### NeuronMotif: Deciphering cis-regulatory codes by layer-wise demixing of deep neural networks. (PNAS 2023)

- DOI: 10.1073/pnas.2216698120 | PMCID: PMC10104575 | PMID: 37023129
- Evidence: We used R to count the cutting frequency of the genomes sequences and visualize the footprinting by ggplot2 package ( SI Appendix ).
- Full pipeline: visualisation [ggplot2] -> stage not stated [Python]

### Large-scale analysis of structural brain asymmetries in schizophrenia via the ENIGMA consortium. (PNAS 2023)

- DOI: 10.1073/pnas.2213880120 | PMCID: PMC10083554 | PMID: 36976765
- Evidence: Figure was generated in R using package ggplot2 ( 69 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [FreeSurfer, ggplot2, metafor v3.0]

### Genomics-driven breeding for local adaptation of durum wheat is enhanced by farmers' traditional knowledge. (PNAS 2023)

- DOI: 10.1073/pnas.2205774119 | PMCID: PMC10083613 | PMID: 36972461
- Evidence: Plotting made use of R/ggplot2 ( 67 ), R/raster ( 68 ), and R/patchwork ( 69 ).
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [R, ggplot2, tidyverse]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Version used: **3.2.1**
- Evidence: Log (CPM) and visualization were performed using ggplot2 (3.2.1), RColorBrewer (v1.1.2), tibble (2.1.3), pheatmap (v1.0.12), stats (v3.5.1), and gplots (v3.0.1.2).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### Species-specific CD4<sup>+</sup> T cells enable prediction of mucosal immune phenotypes from microbiota composition. (PNAS 2023)

- DOI: 10.1073/pnas.2215914120 | PMCID: PMC10041165 | PMID: 36917674
- Evidence: Heatmaps were constructed using either ComplexHeatmap ( 42 ) or ggplot2.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ComplexHeatmap, ggplot2]

### Nasal administration of anti-CD3 mAb (Foralumab) downregulates <i>NKG7</i> and increases <i>TGFB1</i> and <i>GIMAP7</i> expression in T cells in subjects with COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2220272120 | PMCID: PMC10243127 | PMID: 36881624
- Version used: **3.3.6**
- Evidence: All plots were generated using tools within scRepertoire, ggplot2 (v3.3.6), and dittoSeq (v1.4.4).
- Full pipeline: read trimming [Seurat v4.1.1] -> alignment/mapping [STAR] -> quantification [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [Seurat v4.1.1] -> stage not stated [ggplot2 v3.3.6]

### Diverse yeast antiviral systems prevent lethal pathogenesis caused by the L-A mycovirus. (PNAS 2023)

- DOI: 10.1073/pnas.2208695120 | PMCID: PMC10089162 | PMID: 36888656
- Evidence: The data were plotted using R studio ggplot2.
- Full pipeline: visualisation [ggplot2] -> stage not stated [ImageJ]

### HIV post-treatment controllers have distinct immunological and virological features. (PNAS 2023)

- DOI: 10.1073/pnas.2218960120 | PMCID: PMC10089217 | PMID: 36877848
- Evidence: Statistical analyses were performed with R (4.1.0) and Stata (13.0, College Station, TX), and figures were plotted with the R “ggplot2” package unless otherwise specified.
- Full pipeline: differential/statistical testing [ggplot2] -> visualisation [ggplot2]

### Oligomerization of a plant helper NLR requires cell-surface and intracellular immune receptor activation. (PNAS 2023)

- DOI: 10.1073/pnas.2210406120 | PMCID: PMC10089156 | PMID: 36877846
- Version used: **3.3.2**
- Evidence: Data generated with ggplot2 (3.3.2) package in R.
- Full pipeline: stage not stated [ImageJ, ggplot2 v3.3.2]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Evidence: Variant tables in VCF format were processed with PLINK ( 76 ) using option --aec, and PCA results were plotted in R using ggplot2 ( 77 ).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Version used: **3.3.5**
- Evidence: Resulting enriched GO terms were visualized with a custom script using ggplot2 v3.3.5 ( 76 ) displaying the adjusted p value (padj) for the GO term, the number of genes from the list that belong to said term, and the percentage of the total genes in the GO term that are present in the list.
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### Polyamines and linear DNA mediate bacterial threat assessment of bacteriophage infection. (PNAS 2023)

- DOI: 10.1073/pnas.2216430120 | PMCID: PMC9992862 | PMID: 36802441
- Evidence: RNA-seq analysis results were plotted with ggplot2 and pheatmap packages in R.
- Full pipeline: normalisation [edgeR v3.34.1] -> differential/statistical testing [edgeR v3.34.1] -> visualisation [ggplot2, pheatmap]

### Elevated dementia risk, cognitive decline, and hippocampal atrophy in multisite chronic pain. (PNAS 2023)

- DOI: 10.1073/pnas.2215192120 | PMCID: PMC9992778 | PMID: 36802440
- Evidence: GAMs were modeled with the “mgcv” package ( 85 ), and visualizations were performed with the “ggplot2” package ( 86 ).
- Full pipeline: visualisation [ggplot2] -> stage not stated [FreeSurfer, R v4.1, lavaan]

### Type III interferon drives thymic B cell activation and regulatory T cell generation. (PNAS 2023)

- DOI: 10.1073/pnas.2220120120 | PMCID: PMC9992806 | PMID: 36802427
- Evidence: 4.0.5), including packages EdgeR, ggplot2 and pheatmap.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R v4.0.0, Seurat, edgeR v3.24.3, ggplot2, pheatmap]

### Spatial organization of lysosomal exocytosis relies on membrane tension gradients. (PNAS 2023)

- DOI: 10.1073/pnas.2207425120 | PMCID: PMC9974462 | PMID: 36800388
- Evidence: All statistical analyses were made with R [R Core Team (2021)] with the help of the following packages: spatsat ( 50 ), raster, viridis, ggplot2, dunn.test, ape ( 82 ), imager, pracma, circular, ggpur, evmix ( 83 ), splancs, OpenImageR, minpack.lm.
- Full pipeline: differential/statistical testing [R, ggplot2] -> stage not stated [ImageJ]

### Discovery of a rapidly evolving yeast defense factor, &lt;i&gt;KTD1&lt;/i&gt;, against the secreted killer toxin K28. (PNAS 2023)

- DOI: 10.1073/pnas.2217194120 | PMCID: PMC9974470 | PMID: 36800387
- Version used: **3.3.5**
- Evidence: Growth curves were generated using the geom_smooth function in the R package ggplot2 (version 3.3.5) ( 69 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ggpubr] -> visualisation [AlphaFold v2.0.0, PyMOL v2.3.0] -> stage not stated [BLAST, R, ggplot2 v3.3.5]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Evidence: Figures were made using base R (R version 4.1.0) and the R packages ComplexHeatmap ( 130 ), igraph ( 131 ), eulerr ( 132 ), and ggplot2 ( 133 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### A sex-biased imbalance between Tfr, Tph, and atypical B cells determines antibody responses in COVID-19 patients. (PNAS 2023)

- DOI: 10.1073/pnas.2217902120 | PMCID: PMC9942838 | PMID: 36669118
- Version used: **3.3.3**
- Evidence: Analysis of data was primarily performed as in “CyTOF workflow: differential discovery in high-throughput high-dimensional cytometry datasets” version 4 ( 70 ) as implemented in the CATALYST R package (1.14.0) with packages cowplot (v1.1.1), flowCore (2.2.0), diffcyt (1.10.0), scater (1.18.3), SingleCellExperiment (1.12.0), and ggplot2 (3.3.3).
- Full pipeline: quantification [edgeR] -> dimensionality reduction/clustering [UMAP, edgeR, ggplot2 v3.3.3] -> differential/statistical testing [edgeR, ggplot2 v3.3.3] -> stage not stated [R v4.0.3]

### Population trends and the transition to agriculture: Global processes as seen from North America. (PNAS 2023)

- DOI: 10.1073/pnas.2209478119 | PMCID: PMC9942849 | PMID: 36649404
- Version used: **3.3.6**
- Evidence: Loess curves were fitted to skeletal and archaeobotanical data using R 4.2.0 ( 77 ) and ggplot2 3.3.6 ( 78 ).
- Full pipeline: stage not stated [R v4.2, ggplot2 v3.3.6]

### Spontaneous cortical dynamics from the first years to the golden years. (PNAS 2023)

- DOI: 10.1073/pnas.2212776120 | PMCID: PMC9942851 | PMID: 36652485
- Evidence: Data from peak vertices were used to display the corresponding effects using ggplot2 ( 56 ).
- Full pipeline: stage not stated [SPM, ggplot2]

### Community-engaged ancient DNA project reveals diverse origins of 18th-century African descendants in Charleston, South Carolina. (PNAS 2023)

- DOI: 10.1073/pnas.2201620120 | PMCID: PMC9934026 | PMID: 36623185
- Evidence: The results were visualized using the ggplot2 package ( 55 ) in RStudio v4.0 ( 56 ). aDNA Methods and Sequencing.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.9] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9]

### Antibiotic perseverance increases the risk of resistance development. (PNAS 2023)

- DOI: 10.1073/pnas.2216216120 | PMCID: PMC9926169 | PMID: 36595701
- Version used: **3.3.3**
- Evidence: All other data analyses were performed with R 4.0.3 ( 35 ), and the results were plotted using the R package ggplot2 3.3.3 ( 36 ).
- Full pipeline: visualisation [R v4.0, ggplot2 v3.3.3]

### High-frequency and functional mitochondrial DNA mutations at the single-cell level. (PNAS 2023)

- DOI: 10.1073/pnas.2201518120 | PMCID: PMC9910596 | PMID: 36577067
- Evidence: Base R plotting and ggplot2 were used for figure generation.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools] -> registration [SAMtools] -> stage not stated [ANNOVAR, ggplot2]

### Zscan4 mediates ubiquitination and degradation of the corepressor complex to promote chromatin accessibility in 2C-like cells. (PNAS 2024)

- DOI: 10.1073/pnas.2407490121 | PMCID: PMC11670194 | PMID: 39705314
- Evidence: Graphs were generated using GraphPad Prism or R package ggplot2 or other R packages described in the method details.
- Full pipeline: stage not stated [AlphaFold, R, ggplot2]

### Metabolites limiting predator growth wane with prey biodiversity. (PNAS 2024)

- DOI: 10.1073/pnas.2410210121 | PMCID: PMC11670093 | PMID: 39689178
- Evidence: All statistical analyses were performed in the R software (version 4.1.2; http://www.r-project.org/ ), and all figures except the phylogenetic tree were created using the ggplot2 package.
- Full pipeline: differential/statistical testing [ggplot2] -> stage not stated [lme4]

### Increased perfluorooctanoic acid accumulation facilitates the migration and invasion of lung cancer cells via remodeling cell mechanics. (PNAS 2024)

- DOI: 10.1073/pnas.2408575121 | PMCID: PMC11665856 | PMID: 39665760
- Evidence: Spearman’s rank correlation coefficients were calculated and plotted using Rstudio with the ggplot2 package.
- Full pipeline: differential/statistical testing [R] -> visualisation [ggplot2] -> stage not stated [GSEA]

### Climate warming drives population trajectories of freshwater fish. (PNAS 2024)

- DOI: 10.1073/pnas.2410355121 | PMCID: PMC11665863 | PMID: 39652750
- Version used: **3.5.1**
- Evidence: All analyses were conducted in R v.4.4.0 ( 81 ), with figures generated using ggplot2 v.3.5.1 ( 82 ) and statistical tests of linear models undertaken with lmerTest v.3.1-3 ( 83 ).
- Full pipeline: quantification [R v0.3.5] -> differential/statistical testing [ggplot2 v3.5.1] -> stage not stated [lme4 v1.1]

### Permafrost instability negates the positive impact of warming temperatures on boreal radial growth. (PNAS 2024)

- DOI: 10.1073/pnas.2411721121 | PMCID: PMC11648870 | PMID: 39621910
- Evidence: All graphs were created using ggplot2 ( 98 ) or base R ( 97 ).
- Full pipeline: stage not stated [R, ggplot2]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Version used: **3.3.2**
- Evidence: Figures where made using ggplot2 (version 3.3.2) and GGally (version 2.0.0).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Genetic risk factors for Mesoamerican nephropathy. (PNAS 2024)

- DOI: 10.1073/pnas.2404848121 | PMCID: PMC11626114 | PMID: 39585978
- Evidence: All data were plotted in ggplot2 using R.
- Full pipeline: variant calling [Beagle, Picard] -> visualisation [ggplot2] -> stage not stated [METAL]

### Comprehensive deletion scan of anti-CRISPR AcrIIA4 reveals essential and dispensable domains for Cas9 inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2413743121 | PMCID: PMC11621469 | PMID: 39570312
- Evidence: All statistical measurements and visualizations were done with custom R scripts (Versions 4.2.2 and 4.3.2) and R package ggplot2 (Versions 3.4.3 and 3.5.0) through RStudio.
- Full pipeline: differential/statistical testing [R, ggplot2] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, ChimeraX, ColabFold v1.5.5]

### Modeling extrahepatic hepatitis E virus infection in induced human primary neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2411434121 | PMCID: PMC11588080 | PMID: 39546567
- Evidence: Data visualization was done in the statistical programming language R with in-house scripts using the libraries tidyverse, tidytSingleCellExperiment, Seurat ggplot2, GO-plot, ComplexHeatmap, and venn.
- Full pipeline: differential/statistical testing [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> visualisation [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> stage not stated [CellProfiler, ImageJ]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: Median CPM and related parameters were calculated for both regions for sets of samples and plotted using the R package ggplot2 ( 114 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### Quorum sensing orchestrates parallel cell death pathways in &lt;i&gt;Vibrio cholerae&lt;/i&gt; via Type 6 secretion-dependent and -independent mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2412642121 | PMCID: PMC11573629 | PMID: 39499633
- Evidence: The obtained intensity values were used to construct kymograph profiles quantifying the space-time development of live and dead cells within the colony using the R and the ggplot2 visualization packages.
- Full pipeline: quantification [ggplot2] -> visualisation [ggplot2] -> stage not stated [ImageJ]

### Reproduction has immediate effects on female mortality, but no discernible lasting physiological impacts: A test of the disposable soma theory. (PNAS 2024)

- DOI: 10.1073/pnas.2408682121 | PMCID: PMC11494338 | PMID: 39374394
- Evidence: The ggplot2 R package was used for data analysis and visualization ( 68 ).
- Full pipeline: visualisation [R, ggplot2]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: Fst distributions were plotted with ggplot2 package ( 83 ) using 1 kb nonoverlapping (step size 1,000 bp) sliding windows.
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Innate face-selectivity in the brain of young domestic chicks. (PNAS 2024)

- DOI: 10.1073/pnas.2410404121 | PMCID: PMC11459190 | PMID: 39316055
- Evidence: All statistical analyses and visualization of the data was performed in R ( 68 ) with packages “tidyverse,” multcomp, “ggplot2,” and “PMCMRplus” and in MATLAB using custom-made scripts.
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> visualisation [R, ggplot2, tidyverse] -> stage not stated [Kilosort v2.0]

### Manipulation of natural transformation by AbaR-type islands promotes fixation of antibiotic resistance in &lt;i&gt;Acinetobacter baumannii&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2409843121 | PMCID: PMC11441513 | PMID: 39288183
- Evidence: Finally, we represent the insertion sites of the different AbaRs for each bacterial strain, by grouping the strains according to the number of AbaRs they carried (analysis and graphical representation: R4.3.1 and ggplot2).
- Full pipeline: stage not stated [ggplot2]

### Charting the future of high forest low deforestation jurisdictions. (PNAS 2024)

- DOI: 10.1073/pnas.2306496121 | PMCID: PMC11406276 | PMID: 39226355
- Evidence: Statistical modeling and calculations were performed in R version 4.0.2, using the statistical and modeling packages “dplyr” v1.1.2, “MASS” v7.3-51.6, “smotefamily” v1.3.1, “ranger” v0.16.0, the visualization packages “ggplot2” v3.4.2 and “cowplot” v1.1.1, and the parallelization packages “foreach” v1.5.0 and “doParallel” v1.0.15.
- Full pipeline: differential/statistical testing [R v4.0.2, ggplot2, tidyverse] -> visualisation [R v4.0.2, ggplot2, tidyverse]

### SlCPK27 cross-links SlHY5 and SlPIF4 in brassinosteroid-dependent photo- and thermo-morphogenesis in tomato. (PNAS 2024)

- DOI: 10.1073/pnas.2403040121 | PMCID: PMC11388283 | PMID: 39190354
- Evidence: GO analysis was performed using Shiny GO ( 42 ), and the results were plotted using ggplot2 with R ( 43 ).
- Full pipeline: visualisation [ggplot2] -> stage not stated [ImageJ]

### Diffusion barriers imposed by tissue topology shape Hedgehog morphogen gradients. (PNAS 2024)

- DOI: 10.1073/pnas.2400677121 | PMCID: PMC11388384 | PMID: 39190357
- Evidence: Data were plotted using ggplot2 in R.
- Full pipeline: simulation/modelling [R] -> visualisation [ggplot2] -> stage not stated [TrackMate]

### Parallel ecological and evolutionary responses to selection in a natural bacterial community. (PNAS 2024)

- DOI: 10.1073/pnas.2403577121 | PMCID: PMC11388356 | PMID: 39190353
- Evidence: All plots were produced using the “ggplot2” package ( 89 ).
- Full pipeline: quantification [DESeq2, R] -> stage not stated [emmeans, ggplot2, lme4, vegan]

### Alloreactive memory CD4 T cells promote transplant rejection by engaging DCs to induce innate inflammation and CD8 T cell priming. (PNAS 2024)

- DOI: 10.1073/pnas.2401658121 | PMCID: PMC11348247 | PMID: 39136987
- Evidence: Heatmaps, dotplots, and PCA plots were generated using Complex Heatmap ( 10.1093/bioinformatics/btw313 ) and ggplot2 (ISBN: 978-3-319-24277-4) R packages.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2, limma] -> differential/statistical testing [DESeq2, R] -> visualisation [limma] -> stage not stated [fgsea]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Evidence: UMAPs were colored by marker staining or according to the manually identified population using ggplot2 ( 48 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### Parallel vector memories in the brain of a bee as foundation for flexible navigation. (PNAS 2024)

- DOI: 10.1073/pnas.2402509121 | PMCID: PMC11287249 | PMID: 39008670
- Evidence: From these measures, search densities were visualized using R (v4.0.2, R Core Development Team) with the “autoimage,” “ggforce,” “ggplot2,” and “gridExtra” plugins.
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2] -> stage not stated [ImageJ v2.3.0]

### Mitochondrial antioxidants abate SARS-COV-2 pathology in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2321972121 | PMCID: PMC11287122 | PMID: 39008677
- Evidence: Also in R, volcano plots were generated using the “EnhancedVolcano” (version 1.16.0) package, and Heatmaps were generated using the “ComplexHeatmap”( 29 ) (version 2.15.1), and “ggplot2” (version 3.4.1) packages.
- Full pipeline: quantification [DESeq2, R v4.2.2] -> normalisation [DESeq2, R v4.2.2] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ComplexHeatmap, GSEA v4.3.2, ggplot2]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Evidence: Final results were plotted using ggplot2 ( 80 ) and R ( 81 ) v4.3.0. qpWave and Sample Clustering.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Evidence: The plots were generated using the DimPlot, FeaturePlot, and VlnPlot functions from Seurat, as well as the ggplot2 and pheatmap R libraries.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### Bioengineering a plant NLR immune receptor with a robust binding interface toward a conserved fungal pathogen effector. (PNAS 2024)

- DOI: 10.1073/pnas.2402872121 | PMCID: PMC11252911 | PMID: 38968126
- Evidence: ( https://www.r-project.org/ ) and the graphic package ggplot2 ( 71 ).
- Full pipeline: structure determination [REFMAC] -> visualisation [ChimeraX, R v4.0] -> stage not stated [ggplot2]

### The DNA damage response of <i>Escherichia coli</i>, revisited: Differential gene expression after replication inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2407832121 | PMCID: PMC11228462 | PMID: 38935560
- Version used: **3.5.0**
- Evidence: Graphs were generated in R 4.3.1 using ggplot2 3.5.0.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, MultiQC] -> alignment/mapping [MultiQC, STAR] -> quantification [edgeR v3.18] -> normalisation [Bioconductor, DESeq2 v1.42.0] -> differential/statistical testing [Bioconductor, DESeq2 v1.42.0] -> stage not stated [R v4.3, ggplot2 v3.5.0]

### Altered circadian rhythm, sleep, and &lt;i&gt;rhodopsin 7&lt;/i&gt;-dependent shade preference during diapause in &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400964121 | PMCID: PMC11228485 | PMID: 38917005
- Evidence: Plotting was performed using either the “ggplot2” R library or Matlab 2021a.
- Full pipeline: differential/statistical testing [R v4.1.0] -> stage not stated [ggplot2]

### Pathogenic variants in autism gene &lt;i&gt;KATNAL2&lt;/i&gt; cause hydrocephalus and disrupt neuronal connectivity by impairing ciliary microtubule dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2314702121 | PMCID: PMC11228466 | PMID: 38916997
- Evidence: Visualization of the heatmap was by ComplexHeatmap and pheatmap packages, and bar graphs were created with ggplot2 ( 57 , 58 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ANNOVAR, GATK] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [ImageJ] -> visualisation [ComplexHeatmap, ggplot2, pheatmap]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Evidence: Deeptools, Integrative genomics browser (IGV), GraphPad Prism, and ggplot2 (Rstudio) were utilized for data visualization ( 51 , 59 ).
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### Transfection of entomopathogenic <i>Metarhizium</i> species with a mycovirus confers hypervirulence against two lepidopteran pests. (PNAS 2024)

- DOI: 10.1073/pnas.2320572121 | PMCID: PMC11214047 | PMID: 38885380
- Evidence: Pearson correlation coefficient ( r ) and principal component analysis (PCA) were performed using ggplot2 packages in R based on the fragments per kilobase per million mapped fragments (FPKM) of all genes in each RNA-seq sample.
- Full pipeline: read trimming [fastp] -> alignment/mapping [ggplot2] -> quantification [ggplot2] -> dimensionality reduction/clustering [clusterProfiler, ggplot2] -> stage not stated [BLAST, DESeq2, R, pheatmap]

### Single-tissue proteomics in <i>Caenorhabditis elegans</i> reveals proteins resident in intestinal lysosome-related organelles. (PNAS 2024)

- DOI: 10.1073/pnas.2322588121 | PMCID: PMC11194598 | PMID: 38861598
- Evidence: The stacked bar plot and volcano plot were generated using the ggplot2 package v.3.4.4 ( 99 ).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, R, clusterProfiler] -> stage not stated [ggplot2]

### Temporal control of RNAi reveals both robust and labile feedback loops in the segmentation clock of the red flour beetle. (PNAS 2024)

- DOI: 10.1073/pnas.2318229121 | PMCID: PMC11194489 | PMID: 38865277
- Evidence: Outliers were determined for the plots using R package ggplot2 , considering data above 1.5 *IQR of the 75th percentile or below 1.5 *IQR of the 25th percentile as outliers.
- Full pipeline: stage not stated [R, ggplot2]

### Historical redlining is associated with disparities in wildlife biodiversity in four California cities. (PNAS 2024)

- DOI: 10.1073/pnas.2321441121 | PMCID: PMC11194601 | PMID: 38861597
- Evidence: All statistical analyses were completed in R v.4.1.0 ( 95 ) and all plots were made using the ggplot2 package ( 96 ).
- Full pipeline: differential/statistical testing [R, ggplot2] -> stage not stated [vegan]

### Juvenile social play predicts adult reproductive success in male bottlenose dolphins. (PNAS 2024)

- DOI: 10.1073/pnas.2305948121 | PMCID: PMC11194510 | PMID: 38857400
- Evidence: All plots were made using the R package ggplot2 ( 83 ) and model effects were plotted using the effects package ( 84 , 85 ).
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2] -> stage not stated [R]

### Innate acting memory Th1 cells modulate heterologous diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2312837121 | PMCID: PMC11181110 | PMID: 38838013
- Evidence: To plot the results, the packages ggplot2 ( 66 ) (version 3.3.3), pheatmap (version 1.0.12), UpSetR ( 67 ) (version 1.4.0), and VennDiagaram (version 1.6.20) were used.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [R v4.0.2, featureCounts, ggplot2, pheatmap v1.0.12]

### Nitrogen and sulfur for phosphorus: Lipidome adaptation of anaerobic sulfate-reducing bacteria in phosphorus-deprived conditions. (PNAS 2024)

- DOI: 10.1073/pnas.2400711121 | PMCID: PMC11181052 | PMID: 38833476
- Evidence: 2 E ) was performed using the “ggplot2” and “pheatmap” packages in R, version 4.3.2.
- Full pipeline: visualisation [Cytoscape v3.9.1] -> stage not stated [ggplot2, pheatmap]

### Macrophage transplantation rescues RNASET2-deficient leukodystrophy by replacing deficient microglia in a zebrafish model. (PNAS 2024)

- DOI: 10.1073/pnas.2321496121 | PMCID: PMC11126979 | PMID: 38753517
- Version used: **3.4.4**
- Evidence: The ranked list of genes was then used for a GSEA using the package fgsea v1.28.0 and the results were plotted using the package ggplot2 v3.4.4. in R v4.3.2.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [R v4.3, fgsea v1.28.0, ggplot2 v3.4.4] -> stage not stated [HTSeq v2.0]

### Clocking out and letting go to unleash green biotech applications in a photosynthetic host. (PNAS 2024)

- DOI: 10.1073/pnas.2318690121 | PMCID: PMC11127020 | PMID: 38739791
- Evidence: 4.2.2 ( 43 ), using the ggplot2 ( 44 ), ggthemes ( 45 ), and gganimate ( 46 ) packages ( Datasets S1 and S2 ).
- Full pipeline: alignment/mapping [SAMtools v1.11.0] -> quantification [DESeq2 v1.36.0] -> normalisation [R] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HISAT2 v2.2.1, ggplot2, pheatmap v1.0.12]

### Real-time emulation of future global warming reveals realistic impacts on the phenological response and quality deterioration in rice. (PNAS 2024)

- DOI: 10.1073/pnas.2316497121 | PMCID: PMC11126993 | PMID: 38739807
- Evidence: The graphs representing trait values were visualized using the R package “ggplot2” (ver.
- Full pipeline: quantification [ComplexHeatmap] -> visualisation [R, ggplot2] -> stage not stated [DESeq2]

### DELLA proteins recruit the Mediator complex subunit MED15 to coactivate transcription in land plants. (PNAS 2024)

- DOI: 10.1073/pnas.2319163121 | PMCID: PMC11087773 | PMID: 38696472
- Evidence: R code for ggplot2-based plotting can be found in the Mendeley Data link (DOI: 10.17632/j474wymh93.1 ).
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9] -> alignment/mapping [Cutadapt, FastQC v0.11.9, HISAT2, HTSeq, MAFFT v7.0] -> quantification [Cutadapt, DESeq2 v1.24.0, FastQC v0.11.9, HISAT2, HTSeq] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [ggplot2]

### Localizing somatic symptoms associated with childhood maltreatment. (PNAS 2024)

- DOI: 10.1073/pnas.2318128121 | PMCID: PMC11087768 | PMID: 38687795
- Evidence: All analyses were performed in R v4.3.3 and all visualizations were produced using ggplot2 and patchwork .
- Full pipeline: visualisation [R v4.3, ggplot2]

### Frequent nonhomologous replacement of replicative helicase loaders by viruses in <i>Vibrionaceae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2317954121 | PMCID: PMC11087808 | PMID: 38683976
- Evidence: The altered residues in the DnaB MSA were visualized using ggplot2 in R, with V. cholerae DnaB as the positional reference ( 20 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.212] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, eggNOG]

### Machine learning enables identification of an alternative yeast galactose utilization pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2315314121 | PMCID: PMC11067038 | PMID: 38669185
- Version used: **3.4.2**
- Evidence: All extracellular galactose quantification data visualization was performed using R (v4.1.2) in the RStudio platform (v2022.07.01+554) and with the package ggplot2 (v3.4.2) ( 65 , 66 ).
- Full pipeline: quantification [ggplot2 v3.4.2] -> machine learning [XGBoost v1.7.3, scikit-learn] -> visualisation [ggplot2 v3.4.2] -> stage not stated [HMMER, InterProScan]

### Genomes of historical specimens reveal multiple invasions of LTR retrotransposons in <i>Drosophila melanogaster</i> during the 19th century. (PNAS 2024)

- DOI: 10.1073/pnas.2313866121 | PMCID: PMC11009621 | PMID: 38564639
- Evidence: We merged fragmented matches using a Python script ( rm - d e f r a g m e n t e r . p y –dist 100) and visualized the joint distribution of the insert size and the divergence using hexagonal heatmaps [ggplot2 ( 74 )].
- Full pipeline: alignment/mapping [BEDTools, MUSCLE v3.8.1551] -> visualisation [Python, ggplot2] -> stage not stated [Cutadapt, RepeatMasker]

### Reconstitution of a biofilm adhesin system from a sulfate-reducing bacterium in <i>Pseudomonas fluorescens</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2320410121 | PMCID: PMC10990149 | PMID: 38498718
- Version used: **3.4.2**
- Evidence: Linear models were built in R (v.4.3.0) and visualized using ggplot2 (v.3.4.2).
- Full pipeline: differential/statistical testing [R v4.3.0, ggplot2 v3.4.2] -> visualisation [R v4.3.0, ggplot2 v3.4.2] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL]

### The effects of mnemonic variability and spacing on memory over multiple timescales. (PNAS 2024)

- DOI: 10.1073/pnas.2311077121 | PMCID: PMC10962934 | PMID: 38470923
- Evidence: We used R packages including lme4, eemeans, rstatix, sjPlot, and ggplot2.
- Full pipeline: stage not stated [ggplot2, lme4]

### Genome copy number predicts extreme evolutionary rate variation in plant mitochondrial DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2317240121 | PMCID: PMC10927533 | PMID: 38427600
- Evidence: Figures were made using ggplot2 ( 92 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.5, SAMtools] -> differential/statistical testing [R v4.2.2] -> visualisation [ggplot2] -> stage not stated [RAxML, SPAdes]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Version used: **3.3.5**
- Evidence: Plots were obtained with ggplot2 v3.3.5.
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### Single-cell profiling of African swine fever virus disease in the pig spleen reveals viral and host dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2312150121 | PMCID: PMC10927503 | PMID: 38412127
- Evidence: The results were visualized using the ggplot2 R package (v3.3.5).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, ggplot2] -> stage not stated [GSVA v1.44.3, Seurat]

### The impact of age and number of mutations on the size of clonal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2319364121 | PMCID: PMC10895265 | PMID: 38359296
- Evidence: Statistical analyses were performed using the R statistical software (version 4.3.1), with visual plots drawn with the help of R packages “ggplot2” ( https://github.com/tidyverse/ggplot2 ) and “PICH” ( https://github.com/hfang-bristol/PICH ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard v2.23.0] -> differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, SnpEff v4.2]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: All visualizations were prepared using the ggplot2 package ( 47 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### Specialized proresolving mediator resolvin E1 corrects the altered cystic fibrosis nasal epithelium cilia beating dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2313089121 | PMCID: PMC10835060 | PMID: 38252817
- Evidence: Ellipses were drawn using stat_ellipse function (package ggplot2) and calculated using multivariate Student distribution and 95% CI.
- Full pipeline: dimensionality reduction/clustering [vegan] -> stage not stated [ggplot2]

### High-resolution map of the Fc functions mediated by COVID-19-neutralizing antibodies. (PNAS 2024)

- DOI: 10.1073/pnas.2314730121 | PMCID: PMC10801854 | PMID: 38198525
- Version used: **3.3.5**
- Evidence: The figure was assembled with ggplot2 v3.3.5.
- Full pipeline: stage not stated [ggplot2 v3.3.5]

### Fossil evidence sheds light on sexual selection during the early evolution of birds. (PNAS 2024)

- DOI: 10.1073/pnas.2309825120 | PMCID: PMC10801838 | PMID: 38190528
- Evidence: Figures were plotted using R package Cairo V 1.6-0 and R package ggplot2 V 3.4.1 Materials and Measurements.
- Full pipeline: visualisation [ggplot2] -> stage not stated [R]

### Constraining the oxygen requirements for modern microbial eukaryote diversity. (PNAS 2024)

- DOI: 10.1073/pnas.2303754120 | PMCID: PMC10786294 | PMID: 38165897
- Evidence: Both O 2 and H 2 S values were visualized across depth and time using tidyverse and ggplot2 in R.
- Full pipeline: dimensionality reduction/clustering [DADA2] -> differential/statistical testing [R] -> machine learning [scikit-learn] -> visualisation [ggplot2, tidyverse] -> stage not stated [QIIME 2]

### Social anxiety disorder-associated gut microbiota increases social fear. (PNAS 2024)

- DOI: 10.1073/pnas.2308706120 | PMCID: PMC10769841 | PMID: 38147649
- Evidence: Plotting was handled using ggplot2 and the Python implementation of plotly ( https://plotly.com/ ).
- Full pipeline: differential/statistical testing [Python, SciPy v1.9.3, lme4] -> stage not stated [R v4.2.2, ggplot2]

### Dual-targeted ping-pong CAR T cells: Leveraging peripheral expansion to improve solid tumor immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2518996122 | PMCID: PMC12745717 | PMID: 41397127
- Evidence: GSVA results were graphed using the ggplot2 Bioconductor R package.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Bioconductor, GSVA, R, ggplot2]

### Localized nutrient colimitation of phytoplankton growth rates across the subtropical South Pacific Ocean. (PNAS 2025)

- DOI: 10.1073/pnas.2526930122 | PMCID: PMC12718367 | PMID: 41370344
- Evidence: Statistical analyses and visualizations were performed using R version 4.3.2 ( 36 ), with specific functions from the “agricolae,” “ggplot2,” and “vegan” packages.
- Full pipeline: differential/statistical testing [R v4.3.2, ggplot2] -> visualisation [R v4.3.2, ggplot2] -> stage not stated [vegan]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Evidence: Visualizations of the correlation matrix were performed using the ggplot2 package.
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Intracellular &lt;i&gt;Acinetobacter baumannii&lt;/i&gt; acts as a transient reservoir in lung infection via a "persist and resist" strategy. (PNAS 2025)

- DOI: 10.1073/pnas.2511369122 | PMCID: PMC12718349 | PMID: 41364768
- Evidence: For host and bacterial comparisons, data visualization was undertaken using ggplot2 in R ( 70 ).
- Full pipeline: visualisation [R, ggplot2] -> stage not stated [GSEA]

### Globally aggregated biodiversity data impact predictive and descriptive research. (PNAS 2025)

- DOI: 10.1073/pnas.2519119122 | PMCID: PMC12718365 | PMID: 41364761
- Evidence: We utilized the extracted metadata to generate figures that show geographic distribution of authorship and data origin over time ( ggplot2, 54 ) in R ( 55 ).
- Full pipeline: stage not stated [R, ggplot2]

### The olfactory bulb endocast as a proxy for mammalian olfaction. (PNAS 2025)

- DOI: 10.1073/pnas.2510575122 | PMCID: PMC12718348 | PMID: 41359846
- Evidence: All the analyses and plots were performed with R ( 62 ) and the following packages: APE ( 63 ), phytools ( 64 ), and ggplot2 ( 65 ).
- Full pipeline: stage not stated [BUSCO, ggplot2, phytools]

### LHPP expression in triple-negative breast cancer promotes tumor growth and metastasis by modulating the tumor microenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2505653122 | PMCID: PMC12704765 | PMID: 41343666
- Evidence: Principal component analysis (PCA), volcano plots, heatmaps, and Gene Set Enrichment analysis were done by using the packages ggplot2 ( 50 ), Pheatmap ( 51 ), Enhanced Volcano ( 52 ), and Cluster Profiler ( 53 ), respectively in R studio.
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: The resulting regulon activity matrix was imported into R for visualization, where the reshape2 package ( 61 ) was used to transform data into a suitable format, ComplexHeatmap ( 62 ) was used to generate clustered heatmaps, and ggplot2 facilitated violin plots, boxplots, and correlation analyses.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Elevated risk of infectious diseases in adulthood after prenatal or early postnatal exposure to the Great Chinese Famine. (PNAS 2025)

- DOI: 10.1073/pnas.2513421122 | PMCID: PMC12685027 | PMID: 41284860
- Version used: **3.4.1**
- Evidence: ...or fitting GAMs, metafor 4.0.0 ( 65 ) for fitting meta-regression models, foreach 1.5.2 ( 66 ) and doSNOW 1.0.20 ( 67 ) for parallel computation, and ggplot2 3.4.1 ( 68 ), tmap 3.3.3 ( 69 ), cowplot 1.1.1 ( 70 ), and ggsci 3.0.0 ( 71 ) for visualization.
- Full pipeline: differential/statistical testing [R v4.3, ggplot2 v3.4.1, metafor v4.0.0, tidyverse v2.0.0] -> visualisation [ggplot2 v3.4.1]

### &lt;i&gt;Rroid2&lt;/i&gt; regulates effector-to-memory CD8&lt;sup&gt;+&lt;/sup&gt; T cell differentiation during infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2503450122 | PMCID: PMC12684896 | PMID: 41284876
- Evidence: Visualization was generated with ggplot2 package, heatmaps were created with ComplexHeatmap package ( 63 ), volcano plots with the EnhancedVolcano Package ( 64 ) and GSEA with decoupleR ( 27 ).
- Full pipeline: alignment/mapping [Cufflinks, STAR, TopHat] -> quantification [Cufflinks] -> differential/statistical testing [DESeq2] -> visualisation [ComplexHeatmap, GSEA, ggplot2] -> stage not stated [R]

### The telomeric valine-arginine dipeptide repeat protein changes state to diffuse staining in mitosis and represses in vitro translation. (PNAS 2025)

- DOI: 10.1073/pnas.2520441122 | PMCID: PMC12663981 | PMID: 41269794
- Evidence: 4 was made using tidyverse, ggplot2 ( 56 ), and janitor ( 57 ) packages in R version 4.3.1.
- Full pipeline: stage not stated [ImageJ, R v4.3.1, ggplot2, tidyverse]

### An AINTEGUMENTA phosphoswitch controls bilateral stem cell activity during secondary growth. (PNAS 2025)

- DOI: 10.1073/pnas.2510538122 | PMCID: PMC12663975 | PMID: 41264254
- Version used: **3.4.3**
- Evidence: All box plots were generated using ggplot2 (version 3.4.3).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> quantification [R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3, emmeans] -> stage not stated [Galaxy, ggplot2 v3.4.3]

### Mobile species' responses to surrounding land use generate trade-offs and synergies among nature's contributions to people. (PNAS 2025)

- DOI: 10.1073/pnas.2505401122 | PMCID: PMC12625974 | PMID: 41183197
- Version used: **3.4.1**
- Evidence: Our data were processed using the sf package v1.0.5 ( 48 ) and visualized using the ggplot2 v3.4.1 ( 49 ) and bayesplot v1.10.0 packages ( 50 ).
- Full pipeline: differential/statistical testing [R v4.0] -> visualisation [ggplot2 v3.4.1]

### Metabolic adaptation of glucose-deprived macrophages involves partial gluconeogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2419568122 | PMCID: PMC12595420 | PMID: 41160607
- Evidence: Heatmaps of scaled expression data, based on hierarchical clustering, were generated using the R package “ggplot2” (R version 4.3.1) ( 38 ).
- Full pipeline: normalisation [ggplot2] -> dimensionality reduction/clustering [ggplot2] -> visualisation [ComplexHeatmap, R] -> stage not stated [Seurat v5.1.0]

### p53 regulates the expression of histone modifiers to restrict stemness and maintain differentiated luminal identity in breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2522646122 | PMCID: PMC12595495 | PMID: 41160600
- Evidence: Box plots were generated with R, using ggplot2 and rstatix packages ( https://ggplot2.tidyverse.org . and https://rpkgs.datanovia.com/rstatix/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ggplot2, survival (R), tidyverse]

### A functional clock in only two dorsal clock neurons is sufficient to restore the basal circadian activity pattern of &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2506164122 | PMCID: PMC12595503 | PMID: 41150714
- Evidence: Data were analyzed in R (v 4.0.5) using RStudio (v 1.3.1093) with the Rethomics framework ( 86 ) and visualized using the ggplot2 package (v 3.3.3) ( 87 ).
- Full pipeline: visualisation [R v4.0.5, ggplot2]

### Discarded cigarette butts as overlooked reservoirs and amplifiers of antibiotic resistance genes and pathogens in urban green spaces. (PNAS 2025)

- DOI: 10.1073/pnas.2525377122 | PMCID: PMC12595418 | PMID: 41144667
- Version used: **4.6**
- Evidence: Total standardized effects were calculated to illustrate the relative importance of each factor, and results were visualized using ggplot2 .
- Full pipeline: differential/statistical testing [R v4.3.3, vegan] -> visualisation [ggplot2 v4.6, vegan] -> stage not stated [DADA2, scikit-learn]

### Spatial gene expression analysis reveals pathological niches in Japanese encephalitis virus neuroinvasion. (PNAS 2025)

- DOI: 10.1073/pnas.2515006122 | PMCID: PMC12582308 | PMID: 41129224
- Version used: **3.5.1**
- Evidence: Averaged expression level and ratio of cell expressing each gene were obtained from Seurat object and visualized as dot plot by R package ggplot2 (v3.5.1) ( 41 ).
- Full pipeline: visualisation [ggplot2 v3.5.1] -> stage not stated [R, Seurat v5.0.3]

### Joint disruption of &lt;i&gt;Ret&lt;/i&gt; and &lt;i&gt;Ednrb&lt;/i&gt; transcription shifts cell fate trajectories in the enteric nervous system in Hirschsprung disease. (PNAS 2025)

- DOI: 10.1073/pnas.2507062122 | PMCID: PMC12582274 | PMID: 41118220
- Evidence: GO and Cnet plots were produced with the clusterprofiler R package, ( 42 ) and additional plots were produced using ggplot2 ( 43 ) with custom scripts.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [clusterProfiler] -> stage not stated [Seurat]

### Invariant HVC size in female canaries singing under testosterone: Unlocking function through neural differentiation, not growth. (PNAS 2025)

- DOI: 10.1073/pnas.2426847122 | PMCID: PMC12582222 | PMID: 41115194
- Evidence: The graphic visualization of the significant terms ( P .adjust < 0.00001) was performed using the ggplot function of the ggplot2 R package ( 58 ) (R Session info, SI Appendix ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, ggplot2] -> stage not stated [ImageJ, R, Seurat v5.0.1]

### Microbial oxidation significantly reduces methane export from global groundwaters. (PNAS 2025)

- DOI: 10.1073/pnas.2508773122 | PMCID: PMC12557531 | PMID: 41082667
- Version used: **3.5.0**
- Evidence: Data were visualized using R packages ggplot2 v.3.5.0 ( 134 ) and scales v.1.3.0 ( 135 ).
- Full pipeline: differential/statistical testing [R v4.3.3] -> visualisation [ggplot2 v3.5.0]

### Heterochronic shifts in a timing-keeping microRNA are associated with multiple instances of neoteny in plants. (PNAS 2025)

- DOI: 10.1073/pnas.2510697122 | PMCID: PMC12541458 | PMID: 41060751
- Evidence: R Statistical Software [v4.4.1; ( 48 )] and ggplot2 were used for plotting qPCR data with the geom smooth() function for all curves ( 55 ), and linear models and tests were fitted using the base functions lm(), aov(), and TukeyHSD().
- Full pipeline: differential/statistical testing [ggplot2] -> structure determination [phytools v1.9.1] -> stage not stated [RAxML v8.2]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Evidence: Visualization used ggplot2 and ggbreak ( 61 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: We used ggplot2 in R to create boxplots of heterozygosity results.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Phylogenomics redefines the evolutionary history of mosquitoes. (PNAS 2025)

- DOI: 10.1073/pnas.2519291122 | PMCID: PMC12557814 | PMID: 41052354
- Evidence: For correlative statistics, plots were made using ggplot2 ( 80 ) and linear regression models were applied with the R package ggpmisc ( 81 ).
- Full pipeline: alignment/mapping [BUSCO] -> differential/statistical testing [R, ggplot2] -> stage not stated [BEAST, IQ-TREE v2.2, TreeTime]

### Meta-analysis finds large variation but no general patterns in the relationship between climate and parasitism in terrestrial animals. (PNAS 2025)

- DOI: 10.1073/pnas.2508970122 | PMCID: PMC12519196 | PMID: 41021800
- Evidence: We generated figures using the packages “ggplot2” version 3.4.2 ( 67 ) and “orchaRd” version 2.0 ( 68 ).
- Full pipeline: stage not stated [R v4.2.0, ggplot2, metafor]

### Muscle-specific increased expression of &lt;i&gt;JAG1&lt;/i&gt; improves the skeletal muscle phenotype in dystrophin-deficient mice. (PNAS 2025)

- DOI: 10.1073/pnas.2506437122 | PMCID: PMC12501121 | PMID: 40986346
- Evidence: Data analyses and visualization were performed using RStudio (R version 4.3.3) and the ggplot2 package.
- Full pipeline: visualisation [R v4.3.3, ggplot2] -> stage not stated [GSEA, ImageJ]

### Wild, scenic, and toxic: Recent degradation of an iconic Arctic watershed with permafrost thaw. (PNAS 2025)

- DOI: 10.1073/pnas.2425644122 | PMCID: PMC12452937 | PMID: 40920934
- Evidence: All data processing was carried out in R ( 46 ) and all figures were prepared using the ggplot2 package ( 47 ) in R.
- Full pipeline: visualisation [R, ggplot2]

### Founders predict trait evolution and population performance after evolutionary rescue in the red flour beetle. (PNAS 2025)

- DOI: 10.1073/pnas.2506244122 | PMCID: PMC12435296 | PMID: 40906810
- Evidence: Packages used for analysis and visualization were ggplot2, gridExtra, paletteer, dplyr, tidyr, forcats, hrbrthemes, viridis, corrplot, RColorBrewer, survival, sjstats, segmented, broom, ggpubr, MASS, and vegan.
- Full pipeline: visualisation [ggplot2, ggpubr, tidyverse] -> stage not stated [R v3.4.4]

### Mass support for conserving 30% of the Earth by 2030: Experimental evidence from five continents. (PNAS 2025)

- DOI: 10.1073/pnas.2503355122 | PMCID: PMC12415196 | PMID: 40857320
- Evidence: Visualizations were created using R packages ggplot2 ( 57 ), cjoint ( 35 ), cowplot ( 58 ), and jtools ( 59 ).
- Full pipeline: differential/statistical testing [R] -> visualisation [ggplot2]

### Coordinated actions of NLR-assembled and glutamate receptor-like calcium channels in plant effector-triggered immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2508018122 | PMCID: PMC12415192 | PMID: 40844808
- Version used: **3.4.2**
- Evidence: Boxplots and Ribbon plots were generated with the ggplot2 (3.4.2) package.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT v7.505] -> stage not stated [ComplexHeatmap, DESeq2 v1.38.0, R, ggplot2 v3.4.2]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: ..., library(GOstats), library(GO.db), library(org.Hs.eg.db), library(org.Mm.eg.db), library(data.table), library(circlize), library(gridExtra), library(ggplot2), library(dplyr)})) # Set new working directory setwd(“”) # Load significant genes dataset Significant_Genes <- read.csv(“Significant_Genes.txt”, sep=””) # Load normalized expression values norm_vals <- read.delim(“norm_vals.xls”) # Merge dat...
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### Evolution of developmental bias explains divergent patterns of phenotypic evolution in two nematode clades. (PNAS 2025)

- DOI: 10.1073/pnas.2507529122 | PMCID: PMC12403097 | PMID: 40828025
- Version used: **3.5.1**
- Evidence: All plots were made using the R package ggplot2 (v.
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MAFFT v7.49] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.2.2, emmeans v1.10.3, ggplot2 v3.5.1]

### Cognitive bridge between geometric and numerical learning in monkeys. (PNAS 2025)

- DOI: 10.1073/pnas.2502101122 | PMCID: PMC12403012 | PMID: 40825124
- Evidence: All data processing, analyses, and visualizations were performed in R using libraries dplyr , tidyr , ggplot2 , and lme4 .
- Full pipeline: visualisation [ggplot2, lme4, tidyverse]

### Dural ectopic lymphatic structures accumulate during aging and exhibit dysregulation in neurodegenerative diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2425081122 | PMCID: PMC12377736 | PMID: 40794835
- Evidence: Results were visualized with the ggplot2 and patchwork packages.
- Full pipeline: differential/statistical testing [R] -> visualisation [ggplot2] -> stage not stated [PHENIX]

### Circulating cell-free RNA signatures for the characterization and diagnosis of myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2025)

- DOI: 10.1073/pnas.2507345122 | PMCID: PMC12377778 | PMID: 40789036
- Version used: **3.3.5**
- Evidence: Data wrangling and visualization were performed using Python (3.9.1), Pandas (1.3.0) matplotlibvenn (0.11.6), R (v4.1.0), Tidyverse (v1.3.1), and ggplot2 (v3.3.5).
- Full pipeline: quantification [Bracken] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> machine learning [DESeq2 v1.34.0] -> visualisation [ggplot2 v3.3.5] -> stage not stated [Kraken2, Snakemake]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Evidence: The resulting read coverage data were analyzed using bedtools genomecov ( 49 ) and we visualized the read coverage using the R package ggplot2 ( 54 ) generating a bar graph to illustrate the distribution of nanoPARE, mRNA, and sRNA reads in these regions.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: Graphs were created in R using the ggplot2 package ( 56 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### Deficiency in transmitter release triggers homeostatic transcriptional changes that increase presynaptic excitability. (PNAS 2025)

- DOI: 10.1073/pnas.2322714122 | PMCID: PMC12337328 | PMID: 40729383
- Version used: **3.2.1**
- Evidence: Visualization of DE analysis was performed with custom scripts built upon ggplot2 (ver 3.2.1) ( 85 ). qRT-PCR.
- Full pipeline: quality control [FastQC v0.11.7, Trimmomatic v0.38] -> read trimming [FastQC v0.11.7, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0, featureCounts] -> normalisation [DESeq2 v1.26.0] -> visualisation [ggplot2 v3.2.1] -> stage not stated [R v4.1.0]

### Indigenous territories and protected areas are crucial for ecosystem connectivity in the Amazon basin. (PNAS 2025)

- DOI: 10.1073/pnas.2418189122 | PMCID: PMC12337320 | PMID: 40720645
- Version used: **3.5.1**
- Evidence: Additional R packages used for data curation were terra v.1.8.5 ( 112 ), tidyverse v.1.3.1 ( 113 ); ggplot2 v.3.5.1 ( 114 ) was used for data visualization.
- Full pipeline: visualisation [ggplot2 v3.5.1, tidyverse v1.3.1] -> stage not stated [QGIS, emmeans, lme4]

### Ciprofloxacin-driven purifying selection on viral genomes accelerates soil N&lt;sub&gt;2&lt;/sub&gt;O production. (PNAS 2025)

- DOI: 10.1073/pnas.2503199122 | PMCID: PMC12304974 | PMID: 40668828
- Evidence: Heat maps, bar plots, box plots, bar stacking plots, and density plots were drawn using the “ggplot2” and “pheatmap” packages in R.
- Full pipeline: read trimming [fastp] -> visualisation [Cytoscape v3.7.2] -> stage not stated [BLAST v2.12.0, R v4.3.1, eggNOG, ggplot2, pheatmap]

### Thalamic CGRP neurons define a spinothalamic pathway for affective pain. (PNAS 2025)

- DOI: 10.1073/pnas.2505889122 | PMCID: PMC12280894 | PMID: 40632570
- Evidence: Fold changes were calculated from TPM values (estimated counts, >20) between HA-tag and HA negative controls., The ggplot2 package from R was utilized to visualize fold changes.
- Full pipeline: quality control [FastQC] -> quantification [RSEM v1.2.28, ggplot2] -> visualisation [ggplot2]

### The WWP1-JARID1B axis sustains acute myeloid leukemia chemoresistance. (PNAS 2025)

- DOI: 10.1073/pnas.2421159122 | PMCID: PMC12280953 | PMID: 40627385
- Evidence: Values were represented as volcano plot using ggplot2 package.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2, Enrichr] -> stage not stated [ggplot2]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: The ggplot2 and pheatmap packages were applied to generate volcano plots and heatmaps, respectively.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### Chlorophyll trends are negative for lakes but positive for estuarine-coastal waters. (PNAS 2025)

- DOI: 10.1073/pnas.2502289122 | PMCID: PMC12280897 | PMID: 40623175
- Evidence: Aside from the default packages loaded with R base, we mainly used data.table ( 42 ), wql ( 43 ), a fork of our archived wq package, for trend calculations, and ggplot2 ( 44 ) for graphics.
- Full pipeline: stage not stated [data.table, ggplot2]

### Deep origins, distinct adaptations, and species-level status indicated for a glacial relict seal. (PNAS 2025)

- DOI: 10.1073/pnas.2503368122 | PMCID: PMC12207470 | PMID: 40493204
- Evidence: A PCA was performed on the thinned data (1.8M sites) with smartpca (v.16000)( 95 ) and the results were visualized with R ( 96 ) using the ggplot2 ( 97 ) package.
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, RAxML v8.2.12, VCFtools]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Evidence: Graphs were prepared using RStudio and the ggplot2 package by plotting signals from 10 to 900 s after treatment, prior to assembly using the InkScape software.
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Version used: **3.5.1**
- Evidence: Violin plots were created in R Studio using the package ggplot2 v3.5.1 ( https://ggplot2.tidyverse.org ).
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### A combined experimental and computational analysis of mantATP turnover in skinned muscle fibers. (PNAS 2025)

- DOI: 10.1073/pnas.2502652122 | PMCID: PMC12107101 | PMID: 40372438
- Evidence: Data were further processed using R (V 4.2.2), with the libraries: tidyverse, diann, data.table, magrittr, FactoMineR, factoextra and ggplot2, gprofiler, ggplot2.
- Full pipeline: stage not stated [data.table, ggplot2, tidyverse]

### UTX (KDM6A) promotes differentiation noncatalytically in somatic self-renewing epithelia. (PNAS 2025)

- DOI: 10.1073/pnas.2422971122 | PMCID: PMC12107135 | PMID: 40372430
- Evidence: As described previously, figures were made in R using ggplot2 ( 63 ).
- Full pipeline: quantification [ImageJ] -> visualisation [ggplot2]

### Acute chromatin decompaction stiffens the nucleus as revealed by nanopillar-induced nuclear deformation in cells. (PNAS 2025)

- DOI: 10.1073/pnas.2416659122 | PMCID: PMC12088434 | PMID: 40343993
- Evidence: Line graphs and bar plots were generated using Origin and ggplot2 package (v3.4.0) for R.
- Full pipeline: stage not stated [CellProfiler, ggplot2]

### The oncoprotein SET promotes serine-derived one-carbon metabolism by regulating SHMT2 enzymatic activity. (PNAS 2025)

- DOI: 10.1073/pnas.2412854122 | PMCID: PMC12088392 | PMID: 40339130
- Evidence: The R packages of ggplot2 and ggpubr were used for data visualization.
- Full pipeline: visualisation [ggplot2, ggpubr]

### Improved synapsis dynamics accompany meiotic stability in &lt;i&gt;Arabidopsis arenosa&lt;/i&gt; autotetraploids. (PNAS 2025)

- DOI: 10.1073/pnas.2420115122 | PMCID: PMC12088413 | PMID: 40333759
- Evidence: All statistical analyses were performed using Rstudio with the version 4.4.0 of R, and plots were made using ggplot2 ( 74 ).
- Full pipeline: differential/statistical testing [emmeans, ggplot2] -> stage not stated [ImageJ, R]

### Lateral jaw motion in fish expands the functional repertoire of vertebrates and underpins the success of a dominant herbivore lineage. (PNAS 2025)

- DOI: 10.1073/pnas.2418982122 | PMCID: PMC12088409 | PMID: 40324084
- Evidence: Plots were produced using the ggplot2 R package ( 73 ).
- Full pipeline: alignment/mapping [phytools] -> structure determination [phytools] -> stage not stated [ImageJ, R, ggplot2]

### The SIK3-N783Y mutation is associated with the human natural short sleep trait. (PNAS 2025)

- DOI: 10.1073/pnas.2500356122 | PMCID: PMC12088394 | PMID: 40324078
- Evidence: The results were imported into the ggplot2 R package for visualization.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> machine learning [SnpEff] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Cytoscape, ImageJ]

### Distinguishing species boundaries from geographic variation. (PNAS 2025)

- DOI: 10.1073/pnas.2423688122 | PMCID: PMC12088384 | PMID: 40324080
- Evidence: S5 , Top panels) and results were visualized using the tidyverse and ggplot2 packages in R ( SI Appendix , Fig.
- Full pipeline: visualisation [ggplot2] -> stage not stated [ADMIXTURE v1.3.0, R, RAxML, VCFtools v0.1.13, tidyverse, vegan]

### Dynamic interplay between niche variation and flight adaptability drove a hundred million years' dispersion in iconic lacewings. (PNAS 2025)

- DOI: 10.1073/pnas.2414549122 | PMCID: PMC12087969 | PMID: 40314968
- Evidence: Logistic regression was then performed in the R package “ggplot2” ( 98 ) using 10,000 iterations generated by the hidden Markov model.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7, ggplot2] -> stage not stated [NCO, R, phytools]

### Ultrasound-activated cilia for biofilm control in indwelling medical devices. (PNAS 2025)

- DOI: 10.1073/pnas.2418938122 | PMCID: PMC12067268 | PMID: 40294275
- Version used: **3.3.5**
- Evidence: Images were imported into R (version 4.2.2) for further statistical analysis and visualization using packages such as ggplot2 (v3.3.5), dplyr (v1.0.7), and viridis (v0.6.2).
- Full pipeline: differential/statistical testing [R v4.2.2, ggplot2 v3.3.5, tidyverse v1.0.7] -> visualisation [R v4.2.2, ggplot2 v3.3.5, tidyverse v1.0.7] -> stage not stated [ImageJ]

### Unified molecular approach for spatial epigenome, transcriptome, and cell lineages. (PNAS 2025)

- DOI: 10.1073/pnas.2424070122 | PMCID: PMC12037033 | PMID: 40249782
- Evidence: Visualizations were created in R using the package ggplot2.
- Full pipeline: quality control [ArchR, Seurat] -> read trimming [fastp] -> alignment/mapping [HISAT2, Seurat, fastp] -> quantification [ArchR] -> dimensionality reduction/clustering [ArchR] -> visualisation [ggplot2]

### &lt;i&gt;LMX1B&lt;/i&gt; missense-perturbation of regulatory element footprints disrupts serotonergic forebrain axon arborization. (PNAS 2025)

- DOI: 10.1073/pnas.2411716122 | PMCID: PMC12002326 | PMID: 40168115
- Version used: **3.4.4**
- Evidence: Heatmap and volcano plots were generated using ggplot2 v3.4.4 in R v4.3.2 ( 61 ).
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [MACS2, R v4.3, ggplot2 v3.4.4]

### Validating new limits for human thermoregulation. (PNAS 2025)

- DOI: 10.1073/pnas.2421281122 | PMCID: PMC12002229 | PMID: 40163728
- Evidence: Data visualizations were created with “ ggplot2 ” ( 57 ).
- Full pipeline: differential/statistical testing [lme4] -> simulation/modelling [R] -> visualisation [ggplot2] -> stage not stated [survival (R)]

### Modulation of host gene expression by the zinc finger antiviral protein. (PNAS 2025)

- DOI: 10.1073/pnas.2420819122 | PMCID: PMC12002351 | PMID: 40146858
- Evidence: Data were plotted using the ggplot2 package for R ( https://cran.r-project.org/web/packages/ggplot2/index.html ).
- Full pipeline: alignment/mapping [DESeq2, STAR] -> differential/statistical testing [DESeq2, STAR] -> visualisation [ggplot2] -> stage not stated [Cytoscape]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Evidence: GO enrichment and KEGG analysis was conducted using metascape (version 3.5), and visualized in ggplot2 ( Datasets S1–S4 ).
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### iPSCs engrafted in allogeneic hosts without immunosuppression induce donor-specific tolerance to secondary allografts. (PNAS 2025)

- DOI: 10.1073/pnas.2413398122 | PMCID: PMC11929385 | PMID: 40073064
- Evidence: The results were visualized using R (v4.0.1) and the Seurat, ggplot2, and dplyr packages. scRNA-seq Analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2, tidyverse] -> stage not stated [R, Seurat v4.0.1]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Evidence: Heatmaps of expression data were generated by the ggplot2 R package ( https://ggplot2.tidyverse.org ) using Z -normalized FPKM.
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### A global estimate of multiecosystem photosynthesis losses under microplastic pollution. (PNAS 2025)

- DOI: 10.1073/pnas.2423957122 | PMCID: PMC11929485 | PMID: 40063820
- Evidence: The meta-analysis was conducted with RStudio in R version 4.0.3 with the “meta”, “metafor”, “lme4”, “nlme”, “ggplot2,” and “multcomp” packages.
- Full pipeline: stage not stated [Python v3.8.8, R v4.0.3, ggplot2, lme4, metafor, scikit-learn v1.2.2]

### The SUbventral-Gland Regulator (SUGR-1) of nematode virulence. (PNAS 2025)

- DOI: 10.1073/pnas.2415861122 | PMCID: PMC11929438 | PMID: 40063806
- Version used: **3.4.2**
- Evidence: Plots were generated using the ggplot2 v3.4.2 package ( 68 ) and figures made in Inkscape v1.1.
- Full pipeline: quality control [FastQC v0.11.9, HTSeq v0.12.4] -> read trimming [FastQC v0.11.9] -> alignment/mapping [STAR v2.7.9a] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [AlphaFold] -> stage not stated [HOMER, ImageJ, R v4.2.1, ggplot2 v3.4.2]

### Early evidence of avocado domestication from El Gigante Rockshelter, Honduras. (PNAS 2025)

- DOI: 10.1073/pnas.2417072122 | PMCID: PMC11912431 | PMID: 40030019
- Evidence: The R packages ggstatsplot ( 90 ) and ggplot2 ( 91 ) were used to analyze the data and visualize the results.
- Full pipeline: differential/statistical testing [R] -> visualisation [ggplot2]

### Specific microbial ratio in the gut microbiome is associated with multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2413953122 | PMCID: PMC11912405 | PMID: 40030030
- Evidence: The top 20 species contributing to differentially abundant topics were visualized using ggplot2 .
- Full pipeline: differential/statistical testing [ggplot2, vegan] -> visualisation [ggplot2] -> stage not stated [R v4.1]

### The modern pattern of insect herbivory predates the advent of angiosperms by 60 My. (PNAS 2025)

- DOI: 10.1073/pnas.2412036122 | PMCID: PMC11892599 | PMID: 39964701
- Evidence: Visualization of DT functional breadth is provided by the “ggplot2” and “gghalves” packages ( 87 , 88 ).
- Full pipeline: differential/statistical testing [R v4.3.3] -> visualisation [ggplot2]

### Mycorrhiza increases plant diversity and soil carbon storage in grasslands. (PNAS 2025)

- DOI: 10.1073/pnas.2412556122 | PMCID: PMC11848320 | PMID: 39937867
- Version used: **3.3.5**
- Evidence: All statistical analyses except SEM were conducted in R, and the following packages: argicolae v.1.3-5, lme4 v.1.1-30, ggtext v.0.1.1, ggplot2 v.3.3.5, ggpubr v.0.4.0, tidyr v.1.1.4, and vegan v.2.5-7 were used.
- Full pipeline: differential/statistical testing [ggplot2 v3.3.5, ggpubr v0.4.0, lme4 v1.1, tidyverse v1.1.4]

### Dispersal of influenza virus populations within the respiratory tract shapes their evolutionary potential. (PNAS 2025)

- DOI: 10.1073/pnas.2419985122 | PMCID: PMC11789087 | PMID: 39835898
- Evidence: All figures were made using RStudio and the package ggplot2 and aesthetically modified using Inkscape v.1.3.2 ( https://inkscape.org ).
- Full pipeline: differential/statistical testing [Python] -> visualisation [ggplot2] -> stage not stated [R v4.1.3, vegan v2.6]

### Plant BCL-DOMAIN HOMOLOG proteins play a conserved role in SWI/SNF complex stability. (PNAS 2025)

- DOI: 10.1073/pnas.2413346122 | PMCID: PMC11761322 | PMID: 39823297
- Evidence: Plots of RNA-seq data and IP-MS volcano plots were drawn using ggplot2.
- Full pipeline: stage not stated [AlphaFold, ColabFold, deepTools v3.5.1, ggplot2]

### Codon bias, nucleotide selection, and genome size predict in situ bacterial growth rate and transcription in rewetted soil. (PNAS 2025)

- DOI: 10.1073/pnas.2413032122 | PMCID: PMC11761963 | PMID: 39805015
- Evidence: All statistical analyses were conducted in R version 4.2.1 ( 82 ) using the tidyverse package ( 83 ) and visualized with ggplot2 ( 84 ).
- Full pipeline: alignment/mapping [DESeq2, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [R v4.2.1, ggplot2, tidyverse] -> visualisation [R v4.2.1, ggplot2, tidyverse] -> stage not stated [NumPy, Python v3.8.2]

### Multiplicity of type 6 secretion system toxins limits the evolution of resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2416700122 | PMCID: PMC11745330 | PMID: 39786933
- Evidence: Data were analyzed and visualized using RStudio version 2023.12.1 + 402, using the packages readxl , ggplot2 , cowplot , dplyr , tidyr and multcomp , and using the Matlab redblue package (© 2009, Adam Auton).
- Full pipeline: visualisation [ggplot2, tidyverse]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: The generated signal files were visualized in R 3.4.2, using the ggplot2 ( https://ggplot2.tidyverse.org ) and ggbio ( 12 ). qPCR validation of mito-DRIP.
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### A receptor kinase complex refines cambium activity in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2532481123 | PMCID: PMC13321232 | PMID: 42330278
- Version used: **3.4.4**
- Evidence: GO (gene ontology) analyses were performed using PANTHER ( 46 ) and the results were plotted using ggplot2(v3.4.4).
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [ggplot2 v3.4.4] -> stage not stated [pheatmap v1.0.12]

### Mating-dependent lifespan cost of sterol depletion in male &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2533735123 | PMCID: PMC13250600 | PMID: 42228537
- Evidence: Data wrangling was carried out using dplyr ( 33 ) and tidyverse ( 34 ), and figures were made using ggplot2 ( 35 ).
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2, tidyverse] -> stage not stated [emmeans]

### Egress thresholds and wildfire fatalities. (PNAS 2026)

- DOI: 10.1073/pnas.2535081123 | PMCID: PMC13250580 | PMID: 42224582
- Evidence: R analyses relied on the following packages: tidyverse, sf, rnaturalearth, rnaturalearthdata, RColorBrewer, scales, tidycensus, ggpubr, biscale, dplyr, ggplot2, and minpack.lm.
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, R v4.4.0, ggplot2, ggpubr, tidyverse]

### PMF proteins mediate mitochondrial fusion in Arabidopsis. (PNAS 2026)

- DOI: 10.1073/pnas.2601242123 | PMCID: PMC13123921 | PMID: 42018423
- Evidence: All statistical analysis was performed in Microsoft Excel Version 18.89.1 or in RStudio Version 2024.04.2 + 764 with R packages ggplot2 and pheatmap.
- Full pipeline: differential/statistical testing [ggplot2, pheatmap] -> stage not stated [AlphaFold, ImageJ]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Counts of peak intersections were then plotted in R using ggplot2 as pie charts.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### Mild SARS-CoV-2 maternal infection in mice induces transient offspring neurodevelopmental aberrance. (PNAS 2026)

- DOI: 10.1073/pnas.2518294123 | PMCID: PMC13012083 | PMID: 41849379
- Version used: **3.5.2**
- Evidence: Visualizations of bulk RNA-sequencing results were created with custom scripts using the ggplot2 (version 3.5.2) library.
- Full pipeline: quality control [FastQC v0.11.9] -> dimensionality reduction/clustering [clusterProfiler v4.10.0] -> differential/statistical testing [limma v3.58.1] -> visualisation [ggplot2 v3.5.2] -> stage not stated [R v4.3.2]

### Reactivation of the silenced &lt;i&gt;BASP1&lt;/i&gt; gene suppresses oncogenic WNT signaling in human colorectal cancer cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524159123 | PMCID: PMC12974518 | PMID: 41785318
- Evidence: Post processing, statistics (Dixon’s Q test, Wilcoxon rank-sum test) and data visualization were carried out in R and RStudio using R package rstatix ( https://cran.r-project.org/web/packages/rstatix/index.html ) and ggplot2 ( https://cran.r-project.org/web/packages/ggplot2/index.html ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [R, ggplot2] -> visualisation [R, ggplot2] -> stage not stated [GSEA]

### Head-to-head comparison of brain-derived pTau217 and total pTau217 for brain amyloid and tau pathology classification. (PNAS 2026)

- DOI: 10.1073/pnas.2536792123 | PMCID: PMC12974465 | PMID: 41770931
- Evidence: We generated all plots using the ggplot() function in the ggplot2 package (v3.5.1) ( 43 ).
- Full pipeline: differential/statistical testing [R v4.4.2] -> stage not stated [ggplot2]

### Stress and resilience in northern European marine ecosystems. (PNAS 2026)

- DOI: 10.1073/pnas.2527939123 | PMCID: PMC12933128 | PMID: 41719339
- Evidence: All analyses were carried out in R version 3.6.0 ( 52 ) using the following R packages: “factoextra” ( 53 ) (Version 1.0.5), “ggplot2” ( 54 ) (Version 3.2-0), “ggrepel” ( 55 ) (Version 0.8.1) and “gridExtra” ( 56 ) (Version 2.3).
- Full pipeline: stage not stated [R v3.6.0, ggplot2]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: All figures were made in R, using ggplot2 ( 49 ).
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Plant diversity influences plant volatile emission with varying effects at the species and community levels. (PNAS 2026)

- DOI: 10.1073/pnas.2518326123 | PMCID: PMC12818445 | PMID: 41538247
- Evidence: For data visualization, we used ggplot2 , ggeffects , ComplexHeatmap , and pheatmap ( 96 – 99 ).
- Full pipeline: differential/statistical testing [R v4.5.1, lme4, tidyverse] -> visualisation [ComplexHeatmap, R v4.5.1, ggplot2, pheatmap, tidyverse] -> stage not stated [mothur, phyloseq]

### Income insufficiency impacts early brain development in infants facing increased psychosocial adversity: A network-based approach. (PNAS 2026)

- DOI: 10.1073/pnas.2513598123 | PMCID: PMC12799155 | PMID: 41490482
- Evidence: The following packages were used: EGAnet package [v2.1.0 ( 21 )]; bootnet package [v1.6 ( 24 )]; ggplot2 [v3.5.1 ( 59 )]; lmer [v3.1-3 ( 60 )]; mirt [v1.43 ( 61 )]; easyRasch package [v0.3.3 ( 62 )].
- Full pipeline: stage not stated [Python v3.6.8, ggplot2]

### CHAMP1 complex promotes heterochromatin assembly and reduces replication stress. (PNAS 2026)

- DOI: 10.1073/pnas.2525144122 | PMCID: PMC12773717 | PMID: 41481470
- Evidence: The ggplot2 R package was used to create the volcano plot of the linear regression results.
- Full pipeline: quantification [ImageJ, limma] -> differential/statistical testing [R, ggplot2, limma] -> visualisation [ImageJ, survival (R) v0.5.0]

### Acclimation to high and low diurnal light is flexible in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2523996123 | PMCID: PMC12773772 | PMID: 41481448
- Version used: **3.5.1**
- Evidence: Line plots of mean gene expression and the 95% CI across the experimental replicates were generated in the R package ggplot2 (v3.5.1) using the mean_cl_boot function.
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [R, clusterProfiler v4.12.0] -> differential/statistical testing [clusterProfiler v4.12.0] -> stage not stated [ggplot2 v3.5.1]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **3.3.2**
- Evidence: Analyses in R (4.0.2) ( 60 ) were conducted using the following main packages: brms (2.13.9) ( 58 , 59 ), rstanarm (2.21.1) ( 91 ), rstan (2.21.2) ( 92 ), data.table (1.13.3) ( 93 ), and ggplot2 (3.3.2) ( 94 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### Molecular determinants of ligand efficacy and potency in GPCR signaling. (Science 2023)

- DOI: 10.1126/science.adh1859 | PMCID: PMC7615523 | PMID: 38127743
- Evidence: The following packages were used: tidyverse (especially dplyr, ggplot2, purrr, tibble, tidyr, forcats, stringr), plotly, MASS, reshape, reshape2, ggrepel, patchwork, ggpubr, bio3d ( 53 ), openxlsx.
- Full pipeline: stage not stated [GROMACS, MDTraj, PyMOL v2.5.2, R v4.0, ggplot2, ggpubr, tidyverse]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: Beeswarm plots were generated using the ggplot2 library (v3.4.2).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### SPL13 controls a root apical meristem phase change by triggering oriented cell divisions. (Science 2024)

- DOI: 10.1126/science.ado4298 | PMCID: PMC7616863 | PMID: 39541454
- Version used: **3.4.3**
- Evidence: All box plots were generated using ggplot2 (version 3.4.3).
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [R v3.5.1, edgeR, ggplot2 v3.4.3]

### Metagenomic editing of commensal bacteria in vivo using CRISPR-associated transposases. (Science 2025)

- DOI: 10.1126/science.adx7604 | PMCID: PMC12969935 | PMID: 41231980
- Evidence: Relative abundance of ASVs in bulk samples is defined as reads count of ASVs normalized by total number of mapped reads and plotted with ggplot2 using custom R scripts.
- Full pipeline: alignment/mapping [BLAST, Bowtie2, ggplot2] -> quantification [ggplot2] -> normalisation [ggplot2, seaborn] -> visualisation [ggplot2, seaborn] -> stage not stated [Python]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: GSEA analysis and corresponding heatmaps and figures were created using R package fgsea (vfgsea_1.24.0), ComplexHeatmap, and ggplot2 for signatures from MSigDB’s hallmark MTORC1 and custom AR signatures based on our data ( 53 – 55 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Evidence: The distributions were plotted using ggplot2( 76 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Intestinal mast cell-derived leukotrienes mediate the anaphylactic response to ingested antigens. (Science 2025)

- DOI: 10.1126/science.adp0246 | PMCID: PMC12513082 | PMID: 40773543
- Evidence: An additional dataset of mast cells from the gut, peritoneal cavity, and skin was downloaded from Tauber et al ( 59 ) and processed as their descriptions All plots in this analysis were generated by the Seurat visualization methods, the ggplot2, and the EnhancedVolcano packages.
- Full pipeline: quality control [R v4.3.3, Seurat] -> alignment/mapping [kallisto v0.45.0] -> quantification [kallisto v0.45.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [Monocle, ggplot2] -> stage not stated [QuPath]

### Silencing mitochondrial gene expression in living cells. (Science 2025)

- DOI: 10.1126/science.adr3498 | PMCID: PMC7618265 | PMID: 40403134
- Evidence: Graphical representations were generated through the ggplot2 package (version 3.5.1).
- Full pipeline: quantification [ImageJ v1.47] -> normalisation [limma v3.56.2] -> dimensionality reduction/clustering [clusterProfiler v4.8.3, limma v3.56.2] -> differential/statistical testing [DESeq2 v1.40.2, ImageJ v1.47, limma v3.56.2] -> stage not stated [Bioconductor, R v4.3.0, ggplot2]

### Aberrant basal cell clonal dynamics shape early lung carcinogenesis. (Science 2025)

- DOI: 10.1126/science.ads9145 | PMCID: PMC7617789 | PMID: 40310937
- Evidence: Phylogenetic trees were visualized using the R package ggplot2.
- Full pipeline: alignment/mapping [SAMtools] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.24.0] -> visualisation [R, UMAP, ggplot2] -> stage not stated [ANNOVAR v1.0.0, Seurat v5.0.1, Slingshot]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Version used: **3.5.2**
- Evidence: PCAs were calculated using the prcomp R function and visualized using ggplot2 (v3.5.2).
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Ontogeny of the spinal cord dorsal horn. (Science 2026)

- DOI: 10.1126/science.adx5781 | PMCID: PMC12879194 | PMID: 41505538
- Evidence: Contours were plotted in ggplot2 using geom_contour_filled and drawn to fit the densest 50, 25, 15, 5 and 2.5% of points.
- Full pipeline: quality control [R v4.4.1, Seurat] -> dimensionality reduction/clustering [AnnData, R v4.4.1, Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [ggplot2] -> stage not stated [ImageJ]

