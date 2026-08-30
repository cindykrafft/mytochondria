# tidyverse

- **Category:** general
- **Papers in survey:** 238
- **Journals:** PNAS (104), Nature (102), Cell (24), Science (4), Lancet (3), NEJM (1)
- **Years:** 2021 (24), 2022 (31), 2023 (37), 2024 (53), 2025 (71), 2026 (22)
- **Versions named:** 2.0.0 (12), 1.1.4 (9), 1.3.1 (8), 1.3.0 (8), 1.1.2 (7), 1.0.7 (6), 1.3.2 (3), 1.2.0 (2), 1.1.3 (2), 1.1.0 (2)
- **Pipeline stages it appears in:** visualisation (67), differential/statistical testing (49), dimensionality reduction/clustering (12), normalisation (8), quantification (5), variant calling (2), machine learning (1), quality control (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **1.0.2**
- Evidence: ...kages/release/bioc/html/scran.html R package ggplot2 version 3.3.2 Wickham, 2016 https://cran.r-project.org/web/packages/ggplot2/index.html R package dplyr version 1.0.2 Wickham et al., 2020 https://cran.r-project.org/web/packages/dplyr/index.html R package uwot version 0.1.8 Melville, 2020 https://cran.r-project.org/web/packages/uwot/index.html R package clusterProfiler version 3.14.3 Yu et al., ...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Microglia jointly degrade fibrillar alpha-synuclein cargo by distribution through tunneling nanotubes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.007 | PMCID: PMC8527836 | PMID: 34555357
- Evidence: ... LI-COR Biosciences N/A Imaris Bitplane by Oxford Instruments plc v9.2.1 NIS-elements Nikon AR 4.20.03 Partek Genomics Suite and R Parket Inc. v3.5.0 tidyr CRAN v1.0.2 Other BD FACSCANTOII BD Biosciences equipment HiSeq2500 Illumina equipment Infinite M200 Pro TECAN equipment Leica TCS SP8 STED Leica equipment Nikon Eclipse Ti fluorescence microscope Nikon equipment ODYSSEY CLx Imaging System LI-C...
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> dimensionality reduction/clustering [Cytoscape] -> stage not stated [CellProfiler, Fiji, ImageJ, ggplot2, tidyverse]

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: ...ps://www.scipy.org/ numpy van der Walt et al., 2011 https://numpy.org/ snakemake Köster and Rahmann, 2012 https://snakemake.readthedocs.io/en/stable/ tidyverse Wickham et al., 2017 https://www.tidyverse.org/ rgl CRAN https://cran.r-project.org/web/packages/rgl/index.html vegan CRAN https://cran.r-project.org/web/packages/vegan/vegan.pdf MoBIE This paper https://github.com/mobie/mobie#mobie Resourc...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### High-resolution profiling of pathways of escape for SARS-CoV-2 spike-binding antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.045 | PMCID: PMC8096189 | PMID: 34010620
- Evidence: ...ray http://xarray.pydata.org/en/stable/ SAMtools https://quay.io/biocontainers/samtools:1.3%5fh0592bc0_3 R (version 4.0.2) https://www.R-project.org/ tidyverse https://www.tidyverse.org/ ggpubr https://github.com/kassambara/ggpubr corrr https://github.com/tidymodels/corrr cowplot https://github.com/wilkelab/cowplot/ scales https://github.com/r-lib/scales rstatix https://github.com/kassambara/rstat...
- Full pipeline: stage not stated [Clustal Omega, Nextflow, R v4.0.2, SAMtools, ggpubr, tidyverse, xarray]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: ....42.2) Ritchie et al., 2015 https://www.bioconductor.org/packages/release/bioc/html/limma.html Tidyverse (1.2.1, 1.3.0) ( Wickham, 2019 ) https://www.tidyverse.org ComplexHeatmap (2.2.0) Gu et al., 2016 https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html edgeR (3.26.8, 3.28.1) McCarthy et al., 2012 https://bioconductor.org/packages/release/bioc/html/edgeR.html FGSEA (1.10.1) Se...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...wth https://github.com/mrc-ide/skygrowth N/A SPIn Liu et al., 2015 Version 1.1 IQ-TREE 2 Minh et al., 2020 Version 2.0.6 lubridate https://github.com/tidyverse/lubridate Version 1.7.4 ape Paradis and Schliep, 2019 Version 5.3 brms Bürkner, 2018 Version 2.13.5 drc https://cran.r-project.org/web/packages/drc/drc.pdf Version 3.0-1 entropy https://cran.r-project.org/web/packages/entropy/ Version 1.2.1...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Evidence: ...ackages/SingleR DoubletFinder v2.0.3 McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder ggplot2 Wickham, 2016 https://ggplot2.tidyverse.org Plotly Sievert, 2020 https://plotly-r.com Analysis scripts This paper https://github.com/BosingerLab/RM_Baricitinib_manuscript Docker v 1.12.6 Docker https://www.docker.com/ RStudio v1.1.453 RStudio, Inc. https://rstudio.com/ rocker/rst...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Membrane phosphoinositides regulate GPCR-β-arrestin complex assembly and dynamics. (Cell 2022)

- DOI: 10.1016/j.cell.2022.10.018 | PMCID: PMC10030194 | PMID: 36368322
- Evidence: K means clustering was performed using pre-built functions in the tidyverse package (v 1.3.1) of R.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [tidyverse] -> differential/statistical testing [R]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **1.0.7**
- Evidence: VennDiagram 1.6.20, pheatmap 1.0.12, ggforce 0.3.3, ggpubr 0.4.0, RColorBrewer 1.1-2, proxy 0.4-26, reshape2 1.4.4, stringr 1.4.0, dplyr 1.0.7, purrr 0.3.4, readr 1.4.0, tidyr 1.1.3, tidyverse 1.3.1.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **1.0.6**
- Evidence: Graphics were generated using the ggplot2 3.3.3 ( Wickham, 2009 ), ComplexHeatmap 2.4.3 ( Gu et al., 2016 ), pheatmap 1.0.12 ( Kolde, 2019 ), igraph 1.2.6 ( Csardi and Nepusz, 2006 ), RCy3 2.8.1 ( Gustavsen et al., 2019 ), stringr 1.4.0 ( Wickham, 2019 ), dplyr 1.0.6 ( Wickham et al., 2020 ), and RColorBrewer 1.1-2 ( Neuwirth, 2014 ) R package.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Non-canonical odor coding in the mosquito. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.024 | PMCID: PMC9480278 | PMID: 35985288
- Evidence: (2015) https://satijalab.org/seurat/ ggplot2 Wickham (2016) https://ggplot2.tidyverse.org/ R R Core Team (2021) https://www.r-project.org/ R studio RStudio Team, 2020 https://www.rstudio.com/ FIJI Schindelin et al.
- Full pipeline: normalisation [ComplexHeatmap] -> stage not stated [ImageJ, R, Seurat, ggplot2, scDblFinder, tidyverse]

### Emergence of immune escape at dominant SARS-CoV-2 killer T cell epitope. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.002 | PMCID: PMC9279490 | PMID: 35931021
- Evidence: ...ci.org/rnaturalearth (website) https://cran.r-project.org/package=rnaturalearth N/A Tidyverse Wickham et al., 2019 https://cran.r-project.org/package=tidyverse tidyverse, RRID: SCR_019186 Gotree Frédéric Lemoine, Olivier Gascuel, Gotree/Goalign: toolkit and Go API to facilitate the development of phylogenetic workflows, NAR Genomics and Bioinformatics, Volume 3, Issue 3, September 2021, https://gi...
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT] -> stage not stated [CCP4 v7.1, PyMOL v2.3.4, R v4.0, REFMAC v5.8, tidyverse]

### Germinal center responses to SARS-CoV-2 mRNA vaccines in healthy and immunocompromised individuals. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.027 | PMCID: PMC8808747 | PMID: 35202565
- Evidence: All statistical analysis was performed in R version 4.0.3, using the following packages: ggplot2, Semblance, multicross, crossmatchtest, dplyr, randtests, ggpubr, and merTools.
- Full pipeline: differential/statistical testing [ggplot2, ggpubr, tidyverse] -> stage not stated [R v4.0.3]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: ....org/biomart/martview/3e2c65a5e3f783f8c9e5d648e4b64126 pheatmap R package N/A https://rdrr.io/cran/pheatmap/ ggplot2 ( Wickham 2016 ) https://ggplot2.tidyverse.org Scanpy ( Wolf et al., 2018 ) https://scanpy.readthedocs.io/en/stable/ PyTorch N/A https://pytorch.org TotalVI ( Gayoso et al., 2021 ) https://docs.scvi-tools.org/en/stable/user_guide/models/totalvi.html ScVI ( Lopez et al., 2018 ) https...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Evidence: 92 https://bioconductor.org/packages/release/bioc/html/GenomicFeatures.html ggplot2_3.2.1 N/A https://github.com/tidyverse/ggplot2 dplyr_1.0.8 N/A https://github.com/tidyverse/dplyr seqtk 1.2-r94 N/A https://github.com/lh3/seqtk Tama N/A https://github.com/GenomeRIK/tama Sierra Patrick et al.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### The proteomic landscape of genome-wide genetic perturbations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.026 | PMCID: PMC7615649 | PMID: 37080200
- Evidence: 28 https://github.com/vdemichev/diann-rpackage R Statistical Computing Software The R Foundation https://www.r-project.org/ tidyverse Wickham et al.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler, limma] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [Bioconductor, ComplexHeatmap, R, WGCNA]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: 84 https://ggplot2.tidyverse.org/ clusterProfiler R package Yu et al.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **1.3.1**
- Evidence: ...//jupyter-notebook.readthedocs.io/en/v6.5.2/ R v.3.6.3 The Comprehensive R Archive Network https://cran.r-project.org/ R packages N/A seqinr v.4.2.5, tidyverse, v.1.3.1, knitr v.1.33, ggpubr v.0.4.0, DescTools v.0.99.41, gtools v.3.8.2, gridExtra v.2.3, cowplot v.1.1.1, scales v.1.1.1, grid v.3.6.3, broom v.0.7.6, e1071 v.1.7.6, and table1 v.1.4 Python packages N/A biopython v1.79, matplotlib v3.7...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 47 https://ggplot2.tidyverse.org GseaPreranked Subramanian et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Neurotransmitter classification from electron microscopy images at synaptic sites in Drosophila melanogaster. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.016 | PMCID: PMC11106717 | PMID: 38729112
- Evidence: ...1/zenodo.10593546 Software and algorithms R R Core Team 130 RRID SCR 001905 knitr (R) Xie 131 RRID SCR 018533 ggplot2 (R) Wickham 132 RRID SCR 014601 tidyverse (R) Wickham et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, ggplot2, tidyverse]

### Global, site-resolved analysis of ubiquitylation occupancy and turnover rate reveals systems properties. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.024 | PMCID: PMC11136510 | PMID: 38626770
- Version used: **1.0.5**
- Evidence: ...cientific N/A Xcalibur 4.7.69 Thermo Scientific N/A R version N/A https://cloud.r-project.org/ R Studio v1.4.1106 N/A https://rstudio.com/ R package: dplyr v1.0.5 N/A https://cran.r-project.org/web/packages/dplyr/index.html R package: ggplot2 v3.3.5 N/A http://ggplot2.org/ R package: GGally v2.1.2 N/A https://cran.r-project.org/web/packages/GGally/index.html R package: ComplexHeatmap v2.6.2 Gu et ...
- Full pipeline: stage not stated [AlphaFold, ComplexHeatmap v2.6.2, PyMOL v2.5.0, Python v3.7.1, R, ggplot2 v3.3.5, tidyverse v1.0.5]

### Microglia maintain structural integrity during fetal brain morphogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.012 | PMCID: PMC10869139 | PMID: 38309258
- Evidence: ...eurat 4.3.0.1 N/A https://satijalab.org/seurat/get_started.html ; RRID: SCR_016341 R package: Tidyverse 2.0.0 N/A https://CRAN.R-project.org/ package=tidyverse ; RRID: SCR_019186 R package: Viridis 0.6.4 N/A https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html ; RRID: SCR_016696 R package: Clustree 0.5.0 N/A https://CRAN.R-project.org/package=clustree ; RRID: SCR_016293 ...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Bowtie2, ImageJ, Metascape v3.5.20230501, R, Seurat v4.3.0.1, ggplot2, tidyverse]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Evidence: DataTables, reshape2 and dplyr packages were used for data visualization and data wrangling.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### Phages communicate across species to shape microbial ecosystems. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.004 | PMCID: PMC13220667 | PMID: 41923642
- Evidence: ... 9FKU Oligonucleotides Please see Table S5 N/A Software and algorithms R R Core Team 31 https://www.R-project.org/ ggplot2 Wickham 32 https://ggplot2.tidyverse.org ggpubr Kassambara.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, IQ-TREE, R, ggplot2, ggpubr, tidyverse]

### Characterisation of in-hospital complications associated with COVID-19 using the ISARIC WHO Clinical Characterisation Protocol UK: a prospective, multicentre cohort study. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)00799-6 | PMCID: PMC8285118 | PMID: 34274064
- Evidence: All statistical analyses were done with R (version 3.6.3) using the tidyverse, finalfit, mcgv, survival, stringdist, janitor, and Hmisc packages.
- Full pipeline: differential/statistical testing [R v3.6.3, tidyverse]

### Global variation in postoperative mortality and complications after cancer surgery: a multicentre, prospective cohort study in 82 countries. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)00001-5 | PMCID: PMC7846817 | PMID: 33485461
- Evidence: All analyses were done using R (version 3.6.3), using the finalfit, tidyverse, and lme4.
- Full pipeline: stage not stated [R v3.6.3, lme4, tidyverse]

### Elective surgery system strengthening: development, measurement, and validation of the surgical preparedness index across 1632 hospitals in 119 countries. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)01846-3 | PMCID: PMC9621702 | PMID: 36328042
- Evidence: Analyses were done with R Studio (version 4.1.1) packages: tidyverse, finalfit, psych, and ggplot2.
- Full pipeline: stage not stated [Canu, ggplot2, tidyverse]

### Fourth Dose of BNT162b2 mRNA Covid-19 Vaccine in a Nationwide Setting. (NEJM 2022)

- DOI: 10.1056/nejmoa2201688 | PMCID: PMC9020581 | PMID: 35417631
- Evidence: Analyses were performed with the use of R software, version 4.1.0, and the additional freely available R software packages “tidyverse,” version 1.3.1, and “survminer,” version 0.4.9.
- Full pipeline: stage not stated [survival (R), tidyverse]

### Footprint evidence of early hominin locomotor diversity at Laetoli, Tanzania. (Nature 2021)

- DOI: 10.1038/s41586-021-04187-7 | PMCID: PMC8674131 | PMID: 34853470
- Evidence: 3.6.1), with custom scripts and functions from the dplyr 55 , ggplot2 54 and reshape2 56 packages.
- Full pipeline: quantification [ImageJ v1.47] -> stage not stated [R v4.0.3, ggplot2, tidyverse]

### Rare variant contribution to human disease in 281,104 UK Biobank exomes. (Nature 2021)

- DOI: 10.1038/s41586-021-03855-y | PMCID: PMC8458098 | PMID: 34375979
- Version used: **1.1.0**
- Evidence: R libraries data.table (v1.12.8; https://CRAN.R-project.org/package=data.table ), MASS (7.3-51.6; https://www.stats.ox.ac.uk/pub/MASS4/ ), tidyr (1.1.0; https://CRAN.R-project.org/package=tidyr ) and dplyr (1.0.0; https://CRAN.R-project.org/package=dplyr ) were also used.
- Full pipeline: differential/statistical testing [R] -> stage not stated [REGENIE v2.0.2, SAIGE, SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: Most of the statistical analysis and data visualization were performed in R using the packages tidyverse, ggplot2, purrr, tibble, dplyr, tidyr, stringr, readr, forcats, scales, grid, reshape2, Rtsne, ggfortify, factoextra, ggpubr, ggforce, ggrepel, RColorBrewer and pheatmap.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### SARS-CoV-2 infection is effectively treated and prevented by EIDD-2801. (Nature 2021)

- DOI: 10.1038/s41586-021-03312-w | PMCID: PMC7979515 | PMID: 33561864
- Version used: **1.3.0**
- Evidence: Graphs and summary tables were built in R using ggplot; gene set enrichment was performed using GSEA and GO analysis (tidyverse 1.3.0; PCATools 1.2.0; Sqldf 0.4–11; na.tools 0.3.1; ggbiplot 0.55; ggplot2 3.3.1; dplyr 0.8.4).
- Full pipeline: alignment/mapping [STAR v2.7.5a] -> quantification [STAR v2.7.5a] -> normalisation [DESeq2, R v3.6.3] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [GSEA, ImageJ, ggplot2 v3.3.1, tidyverse v1.3.0]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **1.3.0**
- Evidence: Statistical analysis: Statistical analysis was performed using base R version 3.6.3 with tidyverse version 1.3.0 69 and Python 3.6.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Global hotspots of salt marsh change and carbon emissions. (Nature 2022)

- DOI: 10.1038/s41586-022-05355-z | PMCID: PMC9771810 | PMID: 36450979
- Evidence: Hurricane track and intensity data (HURDAT2) were acquired from National Weather Service and processed using the R package ‘tidyverse’ 75 , 76 .
- Full pipeline: stage not stated [Python v3.8.10, QGIS v3.12.263, R v3.6, ggplot2, tidyverse]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Version used: **1.3.0**
- Evidence: We performed the multidimensional analyses in the R development environment (version 3.6.3), equipped with the following packages: tidyverse (version 1.3.0), RColorBrewer (version 1.1.2), ggplot2 (version 3.3.3), ggrepel (version 0.9.1) and stats (version 3.6.3).
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: ... https://cole-trapnell-lab.github.io/monocle3 ), Seurat version 3 ( https://github.com/satijalab/seurat ) and ggplot2 version 3.3.5 ( https://ggplot2.tidyverse.org/ ).
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: Additional analyses were performed using a series of R packages (tidyverse, Seurat, infercnv and hdf5r) and Python and BASH scripts as follows.
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### Signatures of copy number alterations in human cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-04738-6 | PMCID: PMC9242861 | PMID: 35705804
- Evidence: Data handling was performed with GenomicRanges, tidyr, stringr, parallel and gtools.
- Full pipeline: normalisation [RSEM] -> stage not stated [Beagle v5.1, ComplexHeatmap, R, ggplot2, survival (R), tidyverse]

### Enhanced fitness of SARS-CoV-2 variant of concern Alpha but not Beta. (Nature 2022)

- DOI: 10.1038/s41586-021-04342-0 | PMCID: PMC8828469 | PMID: 34937050
- Evidence: Statistical analysis Statistical analysis was performed using GraphPad Prism 8 or R 35 (version 4.1), using the packages tidyverse 36 (v1.3.1), ggpubr (v0.4.0) and rstatix (v.0.7.0).
- Full pipeline: differential/statistical testing [ggpubr v0.4.0, tidyverse]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Evidence: The MAplots, box plots, violin plots and donut plots were produced using ggplot2 (v.3.3.2; https://ggplot2.tidyverse.org ) and heat maps of gene expression changes were produced using pheatmap (v.1.0.12; https://cran.r-project.org/web/packages/pheatmap/index.html ) in R (v.4.0.3).
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Evidence: GenomicRanges, plyranges, tidyverse, patchwork, ggforce, ggside and ggtext were used to read, manipulate and visualize genomic data in R and produce figures.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: Our pipeline used the R packages matrixStats, dplyr and ggplot2.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Rare variant associations with plasma protein levels in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06547-x | PMCID: PMC10567546 | PMID: 37794183
- Version used: **1.1.0**
- Evidence: R libraries data.table (v.1.12.8; https://CRAN.R-project.org/package=data.table ), MASS (7.3-51.6; https://www.stats.ox.ac.uk/pub/MASS4/ ), tidyr (1.1.0; https://CRAN.R-project.org/package=tidyr ) and dplyr (1.0.0; https://CRAN.R-project.org/package=dplyr ) were also used.
- Full pipeline: alignment/mapping [GATK, Mutect2 v4.2.2.0] -> variant calling [GATK, Mutect2 v4.2.2.0] -> differential/statistical testing [R] -> stage not stated [SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### A continuous fish fossil record reveals key insights into adaptive radiation. (Nature 2023)

- DOI: 10.1038/s41586-023-06603-6 | PMCID: PMC10567567 | PMID: 37794187
- Version used: **1.1.2**
- Evidence: 51 ) with packages rstatix v.0.7.2, ggplot2 v.3.4.2, tidypaleo v.0.1.3, patchwork 1.1.2, scales v.1.2.1, ggtext v.0.1.2 and dplyr v.1.1.2.
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [ggplot2 v3.4.2, tidyverse v1.1.2]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Version used: **1.1.2**
- Evidence: ... DelayedArray v.0.26.3; S4Arrays v.1.0.4; patchwork v.1.1.2; reticulate v.1.28; Matrix v.1.5-4.1; cowplot v.1.1.1; ggExtra v.0.10.0; ggplot2 v.3.4.2; dplyr v.1.1.2; wesanderson v.0.3.6; RColorBrewer v.1.1-3; Seurat v.4.9.9.9042; SeuratObject v.4.9.9.9084; bmrm v.4.4; SummarizedExperiment v.1.30.1; Biobase v.2.60.0; GenomicRanges v.1.52.0; GenomeInfoDb v.1.36.0; IRanges v.2.34.0; S4Vectors v.0.38.1...
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Native diversity buffers against severity of non-native tree invasions. (Nature 2023)

- DOI: 10.1038/s41586-023-06440-7 | PMCID: PMC10533391 | PMID: 37612513
- Evidence: Metrics were calculated in R using packages ape 94 , tidyverse 95 , abdiv 96 , doParallel 97 , foreach 98 and pez 99 .
- Full pipeline: visualisation [ggplot2, lme4] -> stage not stated [QGIS, R, tidyverse]

### Global methane emissions from rivers and streams. (Nature 2023)

- DOI: 10.1038/s41586-023-06344-6 | PMCID: PMC10511311 | PMID: 37587344
- Version used: **1.0.7**
- Evidence: Packages used were dplyr (v.1.0.7) for data wrangling 53 , ggplot2 (v.3.3.5) for visualization 54 , lubridate (v.1.7.10) for temporal data 55 , corr (v.0.4.3) to assess correlations in the data 56 , ggtext (v.0.1.1) for labelling figures 57 , ggpubr (v.0.4.0) 58 and patchwork (v.1.1.1) 59 for composing multipaneled figures, sf (v.1.0.3) for spatial analysis of vector data 60 , terra (v.1.4.11) for...
- Full pipeline: machine learning [XGBoost] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4.0, tidyverse v1.0.7] -> stage not stated [R v0.3.2]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Evidence: Using Seurat objects with scRNA-seq expression data and metadata (including cell type annotations and XV-seq mutation calls joined based on cell barcodes), we performed all downstream single-cell analyses in R with extensive use of the tidyverse 63 .
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Uridine-derived ribose fuels glucose-restricted pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06073-w | PMCID: PMC10232363 | PMID: 37198494
- Version used: **0.8.3**
- Evidence: For data analysis and visualization in R, packages (with versions) used include dplyr (0.8.3), ggplot2 (3.3.5), gplots (3.0.1, heatmap.2 function), ComplexHeatmap (2.3.5), tidyverse (1.3.0) and VennDiagram (1.6.20).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5.2, limma] -> visualisation [ComplexHeatmap, ggplot2 v3.3.5, tidyverse v0.8.3] -> stage not stated [GSEA v4.0.3]

### Recombination between heterologous human acrocentric chromosomes. (Nature 2023)

- DOI: 10.1038/s41586-023-05976-y | PMCID: PMC10172130 | PMID: 37165241
- Version used: **1.3.0**
- Evidence: We displayed the untangling results for each acrocentric chromosome with the R development environment (version 3.6.3), equipped with the following packages: tidyverse (version 1.3.0), RColorBrewer (version 1.1.2), ggplot2 (version 3.3.3) and ggrepel (version 0.9.1).
- Full pipeline: alignment/mapping [Python, igraph] -> stage not stated [BEDTools, PLINK v1.9, R v3.6.3, ggplot2 v3.3.3, tidyverse v1.3.0]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **1.3.2**
- Evidence: For I/O operations and general data manipulations, the R packages tidyverse (v1.3.2) 61 , data.table (v1.14.6) 62 , readxl (v1.4.1) 63 , fst (0.9.8) 64 , and qusage (v2.28.0) 65 – 67 were used.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Antibodies against endogenous retroviruses promote lung cancer immunotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05771-9 | PMCID: PMC10115647 | PMID: 37046094
- Version used: **1.0.7**
- Evidence: The packages dplyr (v.1.0.7), data.table (v.1.14.2), tidyverse (v.1.3.1) and rjson (v.0.2.20) were used for data handling in R.
- Full pipeline: quantification [Salmon v0.12.0] -> differential/statistical testing [lme4 v1.1.27.1] -> stage not stated [QuPath v0.3, R, RepeatMasker, data.table v1.14.2, survival (R) v3.2.13, tidyverse v1.0.7]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Version used: **1.3.0**
- Evidence: Plots were created using ggplot2 v.3.2.1, tidyverse v.1.3.0, dplyr v.0.8.5, cowplot v.1.0.0 and pheatmap v.1.0.12.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Soil microbiomes show consistent and predictable responses to extreme events. (Nature 2024)

- DOI: 10.1038/s41586-024-08185-3 | PMCID: PMC11655354 | PMID: 39604724
- Evidence: 75 ) and tidyverse:2.0 (ref.
- Full pipeline: read trimming [Cutadapt v1.2.1] -> quantification [vegan] -> differential/statistical testing [R, ggplot2 v3.3] -> visualisation [vegan] -> stage not stated [BLAST v2.13, DADA2 v1.24, lme4 v3.1, tidyverse]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **1.1.4**
- Evidence: CITE-seq quality control and denoising CITE-seq data were processed using the R packages Seurat 58 (v.4.3.0), SeuratObject (v.4.1.4), SeuratDisk (v.0.0.0.9021), SingleCellExperiment (v.1.24.0), Matrix (v.1.6-4), matrixStats (v.1.2.0), dplyr (v.1.1.4), tidyr (v.1.3.1), reshape2 (v.1.4.4), BiocNeighbors (v.1.20.2), BiocParallel (v.1.36.0), stringr (V.1.5.1), reticulate (v.1.35.0) and sceasy (v.0.0.7...
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: The first two principal components were illustrated by ggplot2 ( https://ggplot2.tidyverse.org ).
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### NK2R control of energy expenditure and feeding to treat metabolic diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-08207-0 | PMCID: PMC11602716 | PMID: 39537932
- Version used: **1.3.1**
- Evidence: Data were loaded and manipulated using data.table (1.14.2) and tidyverse (1.3.1).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> stage not stated [GEMMA, Seurat v4.3.0, VEP, data.table v1.14.2, tidyverse v1.3.1]

### Migrating is not enough for modern planktonic foraminifera in a changing ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-08191-5 | PMCID: PMC11634771 | PMID: 39537925
- Evidence: For handling string manipulations and pattern matching, stringr was utilized 66 . dplyr allowed for robust data transformation and filtering 67 , while vegan was used to conduct the ecological multivariate data analyses 68 .
- Full pipeline: stage not stated [ggplot2, ggpubr, pheatmap, tidyverse]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Evidence: The following libraries and software version have been used for IS analysis and statistics: Prism (v.10); R v.4.0.3 (package dependencies linked to this version include ISAnalytics, scales, dplyr, rstatix for wilcox_test, splines, Rcapture, vegan, psych, cluster, DescTools, fpc, pca, factorextra, ggplot).
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### Rifaximin prophylaxis causes resistance to the last-resort antibiotic daptomycin. (Nature 2024)

- DOI: 10.1038/s41586-024-08095-4 | PMCID: PMC11602712 | PMID: 39443798
- Version used: **1.3.1**
- Evidence: Data visualization and statistics All figures were generated in R (v.4.0.3, https://www.r-project.org/ ) using tidyverse (v.1.3.1), patchwork (v.1.1.1), ggnewscale (v.0.4.5) and maps (v.3.4.2).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2, HTSeq, MAFFT] -> quantification [Bowtie2, HTSeq] -> differential/statistical testing [tidyverse v1.3.1] -> visualisation [R v4.0.3, tidyverse v1.3.1] -> stage not stated [IQ-TREE v2.1.2, Kraken2]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **1.3.2**
- Evidence: The analysis and plotting (for this section and the following) were done using R v.4.3.1 and python v.3.10.6, as well as the R packages ggplot2 v.3.3.6 and tidyverse v.1.3.2 and python library numpy v.1.23.2.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Final plots were drawn and formatted using the tidyverse packages 51 .
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Genetic links between ovarian ageing, cancer risk and de novo mutation rates. (Nature 2024)

- DOI: 10.1038/s41586-024-07931-x | PMCID: PMC11410666 | PMID: 39261734
- Evidence: Software packages for R—tidyverse ( https://www.tidyverse.org/ ), pheatmap, ( https://CRAN.R-project.org/package=pheatmap ) and reshape2 ( https://github.com/hadley/reshape )—were used in processing and visualising the data.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> differential/statistical testing [REGENIE v2.2.4, statsmodels] -> visualisation [pheatmap, tidyverse] -> stage not stated [R v4.1.2]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **1.3.1**
- Evidence: Data exploration and visualization was done in R/tidyverse 1.3.1.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### ILC2-derived LIF licences progress from tissue to systemic immunity. (Nature 2024)

- DOI: 10.1038/s41586-024-07746-w | PMCID: PMC11338826 | PMID: 39112698
- Evidence: Using R programming language, the dplyr package was utilized to filter the CellTalkDB database by the cytokine and cytokine receptor gene lists to remove non-cytokine-related ligand–receptor pairs.
- Full pipeline: read trimming [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [tidyverse]

### DNA-sensing inflammasomes cause recurrent atherosclerotic stroke. (Nature 2024)

- DOI: 10.1038/s41586-024-07803-4 | PMCID: PMC11390481 | PMID: 39112714
- Evidence: Principal components were picked by their percentage of explained variance (62.73% (PC1) and 21.05% (PC2)) and visualized using the ‘ggplot2’ package (version 3.4.3; https://ggplot2.tidyverse.org ).
- Full pipeline: dimensionality reduction/clustering [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [ImageJ]

### Molecular mimicry in multisystem inflammatory syndrome in children. (Nature 2024)

- DOI: 10.1038/s41586-024-07722-4 | PMCID: PMC11324515 | PMID: 39112696
- Version used: **1.1.4**
- Evidence: Further analysis was performed using the R language for statistical computing, with merging and subsetting of data performed using the dplyr v1.1.4 package.
- Full pipeline: differential/statistical testing [Python, SciPy, scikit-learn, tidyverse v1.1.4] -> machine learning [scikit-learn] -> stage not stated [Scanpy v1.10.0, Seurat, igraph v2.0.3]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Evidence: Mutational density by deciles of all 22 metrics were calculated using the R package dplyr 122 .
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Evidence: R packages used were limma ( https://bioconductor.org/packages/limma ), MSnbase ( https://bioconductor.org/packages/MSnbase ), tidyverse ( https://tidyverse.tidyverse.org ), biobroom ( https://bioconductor.org/packages/biobroom ), ggrepel ( https://cran.r-project.org/web/packages/ggrepel/vignettes/ggrepel.html ) and ClusterProfiler ( https://bioconductor.org/packages/clusterProfiler/ ).
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### Thresholds for adding degraded tropical forest to the conservation estate. (Nature 2024)

- DOI: 10.1038/s41586-024-07657-w | PMCID: PMC11269177 | PMID: 39020163
- Version used: **1.1.4**
- Evidence: Methods All data manipulation, data analysis and construction of figures were conducted in the R v.4.02 computing environment 46 , using the packages ape (v.5.0) 47 , betareg (v.3.1-4) 48 , dplyr (v.1.1.4) 49 , lme4 (v.1.1-35.1) 50 , lmtest (v.0.9-40) 51 , lubridate (v.1.9.3) 52 , MASS (v.7.3-60.0.1) 53 , openxlsx (v.4.2.5.2) 54 , paletteer (v.1.6.0) 55 , pastecs (v.1.4.2) 56 , png (v.0.1-8) 57 , ...
- Full pipeline: visualisation [ape (R) v5.0, lme4 v1.1, tidyverse v1.1.4]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Ties (typically, fold changes with value zero) were assigned to the same lowest rank (see min_rank function from R package dplyr).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Brainstem Dbh&lt;sup&gt;+&lt;/sup&gt; neurons control allergen-induced airway hyperreactivity. (Nature 2024)

- DOI: 10.1038/s41586-024-07608-5 | PMCID: PMC11254774 | PMID: 38987587
- Evidence: We plotted a density UMAP using geom_density_2d and stat_density_2d ( https://ggplot2.tidyverse.org/reference/geom_density_2d.html ) from ggplot2 (v3.3.2) 44 for visual identification of high-density regions that represent potential unique cell populations.
- Full pipeline: quality control [R, Seurat v4.0, UMAP] -> normalisation [R, Seurat v4.0, UMAP, scDblFinder v2.0] -> dimensionality reduction/clustering [R, Seurat v4.0, UMAP, ggplot2 v3.3.2, tidyverse] -> differential/statistical testing [R, Seurat v4.0, UMAP] -> visualisation [ggplot2 v3.3.2, tidyverse]

### Global shortfalls in documented actions to conserve biodiversity. (Nature 2024)

- DOI: 10.1038/s41586-024-07498-7 | PMCID: PMC11168922 | PMID: 38839953
- Evidence: R Packages Data wrangling: dplyr 66 , pdftools 67 , purrr 68 , reticulate 69 , tidyr 70 .
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2] -> stage not stated [R v4.3.2, tidyverse]

### Senescent glia link mitochondrial dysfunction and lipid accumulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07516-8 | PMCID: PMC11168935 | PMID: 38839958
- Evidence: Statistical analysis Statistical analysis and data visualization were performed in the R Environment using RStudio with base R and packages as indicated including with tidyverse (dplyr, ggplot2), ggrepel, cowplot, ggsurvplot.
- Full pipeline: alignment/mapping [DESeq2, HISAT2 v2.1.0, HTSeq v0.9.1, SAMtools] -> differential/statistical testing [DESeq2, HTSeq v0.9.1, edgeR, ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse]

### The sex of organ geometry. (Nature 2024)

- DOI: 10.1038/s41586-024-07463-4 | PMCID: PMC11168936 | PMID: 38811741
- Evidence: All statistical analyses were carried out using R including use of ‘dplyr’ package (v.1.0.10).
- Full pipeline: dimensionality reduction/clustering [R v3.6.0] -> differential/statistical testing [tidyverse] -> visualisation [ggplot2]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Handling of geospatial and other data was conducted using the R packages lme4, matrixStats, Matrix, geojsonio, raster, rgeos, sf, sp, tmaptools, patchwork, leaflet, data.table, dplyr, haven, Hmisc, openxlsx, rgdal, scales, stringr, tidyr, tibble, xlsx, rfPermute, randomForest, forcats, and in python using the packages pandas, numpy, scipy, statsmodels, firthlogist, patsy and jupyter 68 – 97 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Version used: **1.1.3**
- Evidence: Coverage plots were generated using ggplot2 (3.4.4) on data organized using the readr (2.1.4), dplyr (1.1.3), tidyr (1.3.0) and stringr (1.5.0) packages 58 .
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### Revealing uncertainty in the status of biodiversity change. (Nature 2024)

- DOI: 10.1038/s41586-024-07236-z | PMCID: PMC11041640 | PMID: 38538788
- Evidence: We compiled the data using the following R packages: tidyverse 49 , countrycode 50 , janitor 51 , here 52 and arrow 53 .
- Full pipeline: visualisation [ggplot2] -> stage not stated [R, tidyverse]

### The evolution of menopause in toothed whales. (Nature 2024)

- DOI: 10.1038/s41586-024-07159-9 | PMCID: PMC10954554 | PMID: 38480878
- Evidence: All data management, analysis and plotting were performed in R with the tidyverse, rstan cmdstanr and ape packages 64 – 67 .
- Full pipeline: stage not stated [tidyverse]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.1.2**
- Evidence: R (v.4.1.3): cluster (v.2.1.2) 138 , ComplexHeatmap (v.2.10.0) 139 , 140 , data.table (v.1.14.8) 141 , DescTools (v.0.99.48) 142 , dplyr (v.1.1.2) 143 , gdata (v.2.19.0) 144 , ggforce (v.0.4.1) 145 , ggplot2 (v.3.4.2) 146 , ggpmisc (v.0.5.3) 147 , ggpointdensity (v.0.1.0) 148 , ggpubr (v.0.5.0) 149 , ggrastr (v.1.0.2) 150 , ggrepel (v.0.9.3) 151 , grid (v.4.1.3) 152 , gridExtra (v.2.3) 153 , gtabl...
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Mutualisms weaken the latitudinal diversity gradient among oceanic islands. (Nature 2024)

- DOI: 10.1038/s41586-024-07110-y | PMCID: PMC10937366 | PMID: 38418873
- Version used: **1.3.2**
- Evidence: 4.3.2) using the following packages: mgcv (v1.8.41), gridExtra (v2.3), betareg (v3.1.4), MASS (v7.3.58.1), lme4 (v1.1.31), lmerTest (v3.1.3), lsmeans (v2.30.0), ggeffects (v1.1.4), spdep (v1.2.7), ggplot2 (v3.4.0), ncf (v1.3.2), ape (v5.6.2), sjPlot (v2.8.12), gridExtra (v2.3), MuMIn (v1.47.1), maps (v3.4.1), sf (v1.0.9), car (v3.1.1), viridis (v0.6.2), tidyverse (v1.3.2) and GIFT (v1.3.0).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, ggplot2 v3.4.0, tidyverse v1.3.2]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Evidence: The results were processed using tidyverse package (v2.0.0) in R 94 .
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Box and whisker plots were generated by first converting gene names into region bed files using the R packages biomaRt, data.table, dplyr and GenomicRanges.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **2.0**
- Evidence: ...RNA-seq, whole-exome sequencing, immunohistochemistry and IMC data, which were conducted using R (v4.2.3) using R-studio build 513 with the packages: tidyverse (v2.0), ggplot2 (v3.4.2), ggpubr (v0.6.0) and pheatmap (v1.0.12).
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Evidence: Astrocyte Fos count analyses across groups for each brain region were run with R v.4.3.2 on RStudio v.2023.12.1.402 and relied on the tidyverse, car, dunn.test and dplyr packages and base R functions aov(), TukeyHSD() and p.adjust().
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### The Panoptes system uses decoy cyclic nucleotides to defend against phage. (Nature 2025)

- DOI: 10.1038/s41586-025-09557-z | PMCID: PMC12657218 | PMID: 41034579
- Evidence: Data processing (knitr and dplyr libraries), statistical analysis (stats and Rmpfr libraries) and visualization (VennDiagram library) were performed using the R language.
- Full pipeline: differential/statistical testing [tidyverse] -> structure determination [Coot v1.1.17] -> visualisation [PyMOL, tidyverse] -> stage not stated [AlphaFold, ColabFold v1.5.5, PHENIX]

### Doughnut of social and planetary boundaries monitors a world out of balance. (Nature 2025)

- DOI: 10.1038/s41586-025-09385-1 | PMCID: PMC12488500 | PMID: 41034533
- Evidence: We used the tidyverse suite of packages (v2.0.0) for organizing, manipulating and visualizing the data.
- Full pipeline: differential/statistical testing [ggpubr] -> visualisation [ggpubr, tidyverse]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Version used: **1.3.1**
- Evidence: Bubble plots of protein expression were generated using the R package tidyverse (v.1.3.1) 71 based on z score-normalized protein expression values.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### A neuronal architecture underlying autonomic dysreflexia. (Nature 2025)

- DOI: 10.1038/s41586-025-09487-w | PMCID: PMC12571909 | PMID: 40963010
- Evidence: All statistical analysis was performed in R using the base package ‘stats’, with primary implementation through the ‘tidyverse’ and ‘broom’ packages.
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain, QuPath v0.4.3]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: The application was written and developed with the Shiny R package, and data visualizations were made possible with the following packages: shiny, tidyverse, ggpubr, visNetwork, png, dqshiny, DT, gsubfn, shinyjs, glue, shinydashboard and plotly.
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Evidence: 70 ), dplyr 71 , ape 72 and RColorBrewer 73 .
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Additional R packages used include Presto, DESeq2, dplyr, ply, ape, cowplot, Matrix, variancePartition, MAST, HGNChelper, openxlsx, RColorBrewer, gridExtra, ggpubr, ComplexHeatmap, tidyverse, tibble, biomaRt, data.table, glmGamPoi, SeuratWrappers, patchwork, magrittr, s2, gplots, stringr, ggnewscale, ggbreak, coin and dunn.test.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Version used: **1.0.9**
- Evidence: ...1), rgdal (v.1.5-32), spatstat (v.2.3-4), maptools (v.1.1-4), gstat (v.2.0-9), sp (v.1.5-0), labdsv (v.2.0-1), rcarbon (v.1.5.1), magrittr (v.2.0.3), dplyr (v.1.0.9), reshape 2 (v.1.4.4), and tidyverse (v.1.3.2).
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **1.1.2**
- Evidence: ... matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R packages: ggplot2 (v.3.4.4), gplots (v.3.1.3), readr (v.2.1.4), dplyr (v.1.1.2), reshape2 (v.1.4.4), patchwork (v.1.1.3), RColorBrewer (v.1.1.3), ggrepel (v.0.9.4), aplot (v.0.1.10), ggdendro (v.0.1.23), Matrix (v.1.6.4), here (v.1.0.1), pheatmap (v.1.0.12), tidyr (v.1.3.0), cowplot (v.1.1.1) and circlize’ (v.0.4...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Eye structure shapes neuron function in Drosophila motion vision. (Nature 2025)

- DOI: 10.1038/s41586-025-09276-5 | PMCID: PMC12488493 | PMID: 40702177
- Version used: **2.0.0**
- Evidence: Our data analysis used these software packages: MATLAB (MathWorks), R 82 , RStudio (Posit Software) and the primary R packages natverse (v.0.2.4) 83 , tidyverse (v.2.0.0) 84 and np (v0.67-17) 78 .
- Full pipeline: stage not stated [tidyverse v2.0.0]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Evidence: Top genes were extracted with dplyr.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: Data visualization was performed using the ggplot2 74 , patchwork 134 , tidyr 135 and dplyr 136 packages (Supplementary Fig.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Rapid emergence of a maths gender gap in first grade. (Nature 2025)

- DOI: 10.1038/s41586-025-09126-4 | PMCID: PMC7618463 | PMID: 40500443
- Evidence: R packages used included rstatix, FactoMineR, dplyr, tidyverse, broom, ggplot2, jtools, LambertW, cohens_d, reshape2, lmerTest, knitr, rmarkdown, MatchIt, remotes, rcpp, glmertree, BayesFactor, mice and tableone, all for R v.4.3.2.
- Full pipeline: stage not stated [R, ggplot2, lme4, tidyverse]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Ideogram methods Ideograms for each pair of chromosomes for the 78 chromosome-level, haplotype-phased genomes were created using ggplot2 [ https://ggplot2.tidyverse.org ] in R ( www.R-project.org ) (Fig.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Version used: **1.1.4**
- Evidence: ...01905); R package ggplot2 (3.5.1, RRID:SCR_014601); R package RColorBrewer (1.1.3, SCR_016697); R package ggrepel (0.9.5, RRID:SCR_016223); R package dplyr (1.1.4); R package FactoMineR (2.11, RRID:SCR_014602); R package pheatmap (1.0.12, RRID:SCR_016418); R package factoextra (1.0.7, RRID:SCR_016692); R package pROC (1.18.5); R package reshape2 (1.4.4); R package igraph (2.1.2); R package tidyr (...
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Taurine from tumour niche drives glycolysis to promote leukaemogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09018-7 | PMCID: PMC12328231 | PMID: 40369079
- Version used: **1.2.0**
- Evidence: Moreover, dplyr v.1.2.0 and tidyverse v.1.3.2 were used extensively for data piping and transformation.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> differential/statistical testing [DESeq2 v1.28.1, Enrichr] -> stage not stated [Seurat v4.1.0, tidyverse v1.2.0]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Version used: **2.0.0**
- Evidence: ...0.2) were used for morphology analysis; Numpy (1.23.5), pandas (1.5.3), SciPy (1.10.1), statsmodels (0.13.5), scikit-learn (1.2.1), PyTorch (1.12.1), tidyverse (2.0.0), glmmTMB (1.1.10), performance (0.12.2) and emmeans (1.10.3) were used for model training and statistical analysis; Matplotlib (3.7.0), seaborn (0.12.2), HoloViews (1.15.4), Ipyvolume (0.5.2) and Neuroglancer ( https://github.com/se...
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Recurrent humid phases in Arabia over the past 8 million years. (Nature 2025)

- DOI: 10.1038/s41586-025-08859-6 | PMCID: PMC12018461 | PMID: 40205061
- Evidence: Statistical tests To determine whether the isotopic composition of the carbonate and fluid inclusions statistically differed in δ 18 O mean and variance, one-way analysis of variance and post hoc Tukey tests were performed using the ‘dplyr’ package in the R software.
- Full pipeline: differential/statistical testing [tidyverse]

### Ancient DNA from the Green Sahara reveals ancestral North African lineage. (Nature 2025)

- DOI: 10.1038/s41586-025-08793-7 | PMCID: PMC12043513 | PMID: 40175549
- Version used: **1.3.0**
- Evidence: The following R packages were used cowplot (v.1.1.2), ggplot (v.3.4.2), ggh4x (v.0.2.3), ggnewscale (v.0.4.8), janno (v.1.0.0), magrittr (v.2.0.3), maps (v.3.4.1), patchwork (v.1.1.2), purrr (v.1.0.1), RColorBrewer (v.1.1.3), readxl (v.1.4.1), tidyr (v.1.3.0) and tidyverse (v.1.3.2).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, MAFFT] -> variant calling [SAMtools v1.3] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> stage not stated [PLINK, tidyverse v1.3.0]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Evidence: Nchart was generated with ggplot2 ( https://ggplot2.tidyverse.org/ ) using adaptation of N-chart ( https://github.com/MariaNattestad/Nchart ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **1.1.2**
- Evidence: R libraries used: BiocManager v.1.30.22, circlize v.0.4.15, ComplexHeatmap v.2.16.0, drawProteins v.1.20.0, dplyr v.1.1.2, ggplot2 v.3.4.4, ggnewscale v.0.4.10, ggrepel v.0.9.4, PerformanceAnalytics v.2.0.4, RColorBrewer v.1.1-3, stringr v.1.5.1, tidyr v.1.3.0, tidyverse v.2.0.0, ggplot2 v.3.4.4.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### Clonal driver neoantigen loss under EGFR TKI and immune selection pressures. (Nature 2025)

- DOI: 10.1038/s41586-025-08586-y | PMCID: PMC11946900 | PMID: 39972134
- Version used: **1.1.4**
- Evidence: Analysis was conducted in R using the dplyr (v.1.1.4), immunarch (v.0.9.1), data.table (v.1.14.8), RColorBrewer (v.1.1-3), viridis (v.0.6.5) and ggplot2 (v.3.5.1) packages.
- Full pipeline: stage not stated [data.table v1.14.8, ggplot2 v3.5.1, tidyverse v1.1.4]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Evidence: Further analysis and visualization were done in R 74 using tidyverse 75 and ggpubr 76 .
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Version used: **1.1.3**
- Evidence: ...treeio v.1.26.0, ggh4x v.0.2.6, scales v.1.2.1, edgeR v.4.0.16, limma v.3.58.1, ggtree v.3.10.1, lubridate v.1.9.3, forcats v.1.0.0, stringr v.1.5.0, dplyr v.1.1.3, purrr v.1.0.2, readr v.2.1.4, tidyr v.1.3.0, tibble v.3.2.1, ggplot2 v.3.4.4, tidyverse v.2.0.0, SeuratObject v.4.1.4, Seurat v.4.4.0, RcppAnnoy v.0.0.22, cellranger v.4-5, spaceranger v.2 and bolt-lmm v.2.3.6.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **2.0.0**
- Evidence: 122 ) and tidyverse v.2.0.0 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Global meta-analysis shows action is needed to halt genetic diversity loss. (Nature 2025)

- DOI: 10.1038/s41586-024-08458-x | PMCID: PMC11839457 | PMID: 39880948
- Version used: **0.8.0**
- Evidence: We then performed full text mining in R v.3.5.2 39 , using the packages pdfsearch v.0.2.3 40 , dplyr v.0.8.0 41 , and stringi v.1.3.1 42 to remove records that did not contain population genetic keywords (Supplementary Information 2.2 ).
- Full pipeline: visualisation [R] -> stage not stated [ggplot2 v3.4.3, tidyverse v0.8.0]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Evidence: Data visualization The R package ggplot2 was used for figure generation ( https://ggplot2.tidyverse.org ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **2.0.0**
- Evidence: Genes with P adj < 0.05 were deemed to be significant and Z scores were computed in R using tidyverse (v.2.0.0). heatmap.2 in R was used to visualize the cycle genes (gplots v.3.1.3.1) across the zeitgeber.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **1.1.4**
- Evidence: The number of insertion sites were plotted using the packages of ggplot2 (v.3.4.4) 53 , readr (v.2.1.5) 54 and dplyr (v.1.1.4) 55 in R software (v.4.3.2) 56 .
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Earliest modern human genomes constrain timing of Neanderthal admixture. (Nature 2025)

- DOI: 10.1038/s41586-024-08420-x | PMCID: PMC11839475 | PMID: 39667410
- Version used: **1.1.4**
- Evidence: We used Rstudio (v.2022.12.0+353, http://www.rstudio.com/ ) and the following packages for data visualization: cowplot (v.1.1.2), ggplot2 (v.3.4.2, https://ggplot2.tidyverse.org ), tidyr (v.1.3.0, https://github.com/tidyverse/tidyr ), dplyr (v.1.1.4, https://github.com/tidyverse/dplyr ), magrittr (v.2.0.3, https://github.com/tidyverse/magrittr ), scales (v.1.3.0, https://github.com/r-lib/scales ) ...
- Full pipeline: read trimming [BWA v0.5.10] -> alignment/mapping [BWA v0.5.10, Bowtie2, GATK, SAMtools] -> variant calling [GATK] -> visualisation [ggplot2 v3.4.2, tidyverse v1.1.4] -> stage not stated [BEDTools]

### The oestrous cycle stage affects mammary tumour sensitivity to chemotherapy. (Nature 2025)

- DOI: 10.1038/s41586-024-08276-1 | PMCID: PMC11666466 | PMID: 39633046
- Evidence: 68 ) and packages from tidyverse 69 , including dplyr, tidyr and ggplot2, and were analysed as follows.
- Full pipeline: quantification [Fiji v1.49k, QuPath v0.4.4] -> dimensionality reduction/clustering [ImageJ] -> differential/statistical testing [R v4.4.2] -> machine learning [QuPath v0.4.4] -> stage not stated [ggplot2, tidyverse]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Version used: **1.2.0**
- Evidence: All data analysis and visualization was done in R (v4.2.1) with the following packages: stats (v.4.1.1), vegan (v.2.6), ggplot2 (v.3.3.6), ComplexUpset (v.2.8.0), tidyr (v.1.2.0), dplyr (v.1.0.9), corrplot (v.0.92), pheatmap (v.1.0.12), RColorBrewer (v.1.1-3), pls (v.2.8), edgeR (v.3.16).
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Evidence: Statistical methods The data from IHC, flow cytometry (tumour biopsies and blood), secretome and plasma were processed with the dplyr package (1.1.4) for later use.
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Evidence: Most visualizations are based on ggplot2 ( https://ggplot2.tidyverse.org/ ).
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### Polyclonal selection of immune checkpoint mutations in thyroid autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10493-9 | PMCID: PMC13233322 | PMID: 41981327
- Evidence: R packages used include: tidyverse 83 (v.2), GenomicRanges 84 (v.1.62.1), dndscv 22 (v.0.0.1.0), scales 85 (v.1.4.0), patchwork 86 (v.1.3.2), viridis 87 (v.0.6.5), RColorBrewer 88 (v.1.1-3), lattice 89 (v.0.22-6), latticeExtra 90 (v.0.6-31), vcfR 91 (v.1.15.0), MASS 92 (v.7.3-65), jsonlite 93 (v.2.0.0), ggforce 94 (v.0.5.0), stringi 95 (v.1.8.7), gtools 96 (v.3.9.5), drc 69 (v.3.0-1), pander 97 (v...
- Full pipeline: alignment/mapping [BWA, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [R, Seurat, ggpubr, tidyverse]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **1.0.7**
- Evidence: 68 ) in RStudio (v.4.2) using the following packages: ape (v.5.5), vegan (v.2.6.4), DESeq2 (v.1.32.0), matrixStats (v.0.61.0), cowplot (v.1.1.1), broom (v.0.7.8), dplyr (v.1.0.7), tidyr (v.1.1.3) and tidyverse (v.2.0.0).
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Version used: **2.0.0**
- Evidence: The quantified area was normalized to the mean area of the first 20 frames before the light-to-dark transition and plotted using tidyverse (v.2.0.0) in R (v.4.1.1) and RStudio (v.2021.9.0.351).
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Fossil isotope evidence for trophic simplification on modern Caribbean reefs. (Nature 2026)

- DOI: 10.1038/s41586-025-10077-z | PMCID: PMC13017509 | PMID: 41673163
- Version used: **1.3.1**
- Evidence: All data analysis was conducted using R software (v.4.1.2), via the tidyverse (v.1.3.1), boot (v.1.3-28), rlist (v.0.4.6.2), onewaytests (v.2.7), rstatix (v.0.7.0), forcats (v.0.5.1) and tidyr (v.1.3.1) packages.
- Full pipeline: differential/statistical testing [R] -> stage not stated [tidyverse v1.3.1]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: Heatmap visualization of ATAC-seq data was performed using pheatmap. scRNA-seq metadata analysis Analysis was performed primarily in R (v.3.6.1) using the package Seurat 68 , 79 (v.3.1), with the package tidyverse 80 (v.1.2.1) used to organize data and the package ggplot2 (v.3.2.1) to generate figures. scRNA-seq data from GSE10898 , GSE99254 , GSE98638 , GSE199565 and GSE181785 were filtered to ke...
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: Quantification and statistical analysis Data were plotted in R (version 4.4.2 (2024-06-14)) using the ggplot2, tidyr, dplyr, ggpubr and Hmisc toolkits (versions ggplot2_3.5.1, tidyr_1.3.1, dplyr_1.1.4, ggpubr_0.6.0, Hmisc_5.2.1), Python (version 3.12.9) using the pandas, scipy, scikit-learn, matplotlib and seaborn packages (versions pandas_2.2.3, scipy_1.14.1, scikit-learn_1.5.2, matplotlib_3.9.2,...
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Nutrient requirements of organ-specific metastasis in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09898-9 | PMCID: PMC12851942 | PMID: 41501456
- Version used: **1.1.2**
- Evidence: The analysis was conducted using R studio (v4.3.1), using the dplyr (v1.1.2) and ggplot2 (v3.4.3) packages for data processing and visualization, the boot package (v2019.6.0) for bootstrap confidence interval calculations, and the reshape2 package (v1.4.4) for data reshaping.
- Full pipeline: visualisation [ggplot2 v3.4.3, tidyverse v1.1.2]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: ...e samples and 107,826 (106,760 after filtering) species-representative OTUs using usearch 87 v.11 with downstream analysis done in R 78 v.4.4.1 using tidyverse 93 v.2.0.0.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **2.0.0**
- Evidence: Data visualization was performed using ggplot2 (v.3.5.1), which is part of the tidyverse (v.2.0.0) suite of tools 81 .
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Evidence: Map plotting Figure 1a was generated in R 111 v.4.3.2 with open-source packages dplyr 112 v1.1.4 , ggforce 113 v0.4.2 , ggnewscale 114 v0.4.10 , ggplot2 115 v3.4.4 , ggspatial 116 v1.1.9 , ggstar 117 v1.0.4 , ggrepel 118 v0.9.5 , paletteer 119 v1.3 , raster 120 v3.6-26 , rnaturalearth 121 v1.0.1 , sf 122 , 123 v1.0-15 , tidyterra v0.5.2 124 and terra 125 v1.7- 71, using Natural Earth ( https://www...
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **1.1.2**
- Evidence: Plots were produced using the ggplot2 R package (v.3.5.1), and data input and processing were performed with dplyr v.1.1.2, tidyr v.1.3.0, readxl v.1.4.3, readr v.2.1.4 and magrittr v.2.0.3.
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Microchromosomes are building blocks of bird, reptile, and mammal chromosomes. (PNAS 2021)

- DOI: 10.1073/pnas.2112494118 | PMCID: PMC8609325 | PMID: 34725164
- Evidence: Homology and statistics were plotted in R using the tidyverse package (v1.3.0) with custom scripts available at the GitHub repository.
- Full pipeline: differential/statistical testing [tidyverse] -> visualisation [tidyverse]

### Emergent RNA-RNA interactions can promote stability in a facultative phototrophic endosymbiosis. (PNAS 2021)

- DOI: 10.1073/pnas.2108874118 | PMCID: PMC8463893 | PMID: 34521754
- Evidence: Size distributions of sRNA abundance for each sample were plotted using the R programming language packages tidyverse, grid.extra, and ggplot2 in R Studio. eDicer Methods for Identifying Putative RNA–RNA Interactions.
- Full pipeline: quality control [FastQC] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2] -> quantification [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [BLAST]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: Pairwise Wilcoxon rank sum tests were done in R with dplyr and the Benjamini–Hochberg P -value adjustment method ( Dataset S13 ).
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Single-nuclear transcriptomics reveals diversity of proximal tubule cell states in a dynamic response to acute kidney injury. (PNAS 2021)

- DOI: 10.1073/pnas.2026684118 | PMCID: PMC8271768 | PMID: 34183416
- Version used: **1.0.2**
- Evidence: The R packages Seurat v.3.2.2 ( 18 ), ggplot2 v.3.3.2, Matrix v.2.3-18, and dplyr v.1.0.2 were used for preprocessing, data analysis, and visualization in R Studio (R version 3.6.3).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Monocle v0.2.3.0, SCENIC v1.1.2, STAR, UMAP] -> visualisation [Monocle v0.2.3.0, R v3.6.3, Seurat v3.2.2, ggplot2 v3.3.2, tidyverse v1.0.2]

### Killed whole-genome reduced-bacteria surface-expressed coronavirus fusion peptide vaccines protect against disease in a porcine model. (PNAS 2021)

- DOI: 10.1073/pnas.2025622118 | PMCID: PMC8106328 | PMID: 33858942
- Evidence: Statistical analysis was done using R (v1.3.1093) with the Rstudio environment with included packages and the tidyverse and stats packages, with visualizations using ggplot2.
- Full pipeline: differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [ImageJ]

### People have shaped most of terrestrial nature for at least 12,000 years. (PNAS 2021)

- DOI: 10.1073/pnas.2023483118 | PMCID: PMC8092386 | PMID: 33875599
- Evidence: Raster data in 5 arc minutes and other formats were converted to the DGG system using R [v.3.6.3 ( 68 )] with the packages ddgridR [v.2.0.4 ( 69 )], exactextractr [v.0.4.0 ( 70 )], sf [v.0.9–5 ( 71 )], and tidyverse [v.1.3.0 ( 72 )].
- Full pipeline: differential/statistical testing [R v3.6.3] -> stage not stated [tidyverse]

### Comparing treatment strategies to reduce antibiotic resistance in an in vitro epidemiological setting. (PNAS 2021)

- DOI: 10.1073/pnas.2023467118 | PMCID: PMC8020770 | PMID: 33766914
- Evidence: All statistical analyses were performed in R 4.0.2 ( 31 ) using the packages tidyverse ( 32 ), multcomp ( 33 ), and multcompView ( 34 ).
- Full pipeline: differential/statistical testing [R v4.0, tidyverse]

### High-salt diet suppresses autoimmune demyelination by regulating the blood-brain barrier permeability. (PNAS 2021)

- DOI: 10.1073/pnas.2025944118 | PMCID: PMC7999868 | PMID: 33723078
- Evidence: Subsequent data filtering and visualizations were performed in the R environment using the tidyverse packages and pheatmap.
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [DESeq2 v1.26.1, kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.1, clusterProfiler v3.14.3, limma] -> visualisation [pheatmap, tidyverse]

### Bayesian estimation of SARS-CoV-2 prevalence in Indiana by random testing. (PNAS 2021)

- DOI: 10.1073/pnas.2013906118 | PMCID: PMC7865174 | PMID: 33441450
- Evidence: Data management was performed with the package dplyr ( 30 ), and maps were generated through the packages maps ( 31 ) and sp ( 32 ).
- Full pipeline: differential/statistical testing [Stan] -> stage not stated [tidyverse]

### Ancient DNA from Guam and the peopling of the Pacific. (PNAS 2021)

- DOI: 10.1073/pnas.2022112118 | PMCID: PMC7817125 | PMID: 33443177
- Evidence: We used the tidyverse ( 98 ), data.table ( https://CRAN.R-project.org/package=data.table ), Hmisc ( https://CRAN.R-project.org/package=Hmisc ), and pheatmap ( https://CRAN.R-project.org/package=pheatmap ) packages.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, R, data.table, pheatmap, tidyverse]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: We made plots using ggplot2, cowplot, and pheatmap ( 110 – 113 ) and made extensive use of the tidyverse suite of R packages for data analysis ( 114 ).
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### Testing hypotheses of a coevolutionary key innovation reveals a complex suite of traits involved in defusing the mustard oil bomb. (PNAS 2022)

- DOI: 10.1073/pnas.2208447119 | PMCID: PMC9907077 | PMID: 36508662
- Evidence: Output from this software was plotted in R ( 53 ), using the tidyverse package ( 63 ).
- Full pipeline: alignment/mapping [SAMtools] -> visualisation [tidyverse] -> stage not stated [R]

### Teeth, prenatal growth rates, and the evolution of human-like pregnancy in later <i>Homo</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2200689119 | PMCID: PMC9564099 | PMID: 36191229
- Evidence: All plots were made with the ggplot2 package ( 111 ), and averages and log-transformed values were calculated with the dplyr package ( 112 ).
- Full pipeline: differential/statistical testing [R v4.1.2] -> visualisation [R v4.1.2] -> stage not stated [ggplot2, tidyverse]

### A single helix repression domain is functional across diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2206986119 | PMCID: PMC9564828 | PMID: 36191192
- Evidence: Data from at least two independent replicates were combined and plotted in R ( https://ggplot2.tidyverse.org/ ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> normalisation [ImageJ] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### Truncated Tau caused by intron retention is enriched in Alzheimer's disease cortex and exhibits altered biochemical properties. (PNAS 2022)

- DOI: 10.1073/pnas.2204179119 | PMCID: PMC9477417 | PMID: 36067305
- Evidence: Normalized IR ratio from individual human subject determined from DESeq2 was used to generate dot plot with “ggplot” function in “ggplot2” package ( https://ggplot2.tidyverse.org ).
- Full pipeline: normalisation [ggplot2, tidyverse] -> differential/statistical testing [DESeq2, featureCounts v2.0.1]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; sine oculis/SIX-type homeobox genes act as homeotic switches to define neuronal subtype identities. (PNAS 2022)

- DOI: 10.1073/pnas.2206817119 | PMCID: PMC9478639 | PMID: 36067313
- Evidence: We used the R tidyverse package collection and the ggplot2 graph library.
- Full pipeline: stage not stated [ImageJ, ggplot2, tidyverse]

### The glioblastoma multiforme tumor site promotes the commitment of tumor-infiltrating lymphocytes to the T&lt;sub&gt;H&lt;/sub&gt;17 lineage in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2206208119 | PMCID: PMC9407554 | PMID: 35969754
- Version used: **1.0.7**
- Evidence: Data from RNA-seq were processed in R version 4.1.0 (2021-05-18) using DESeq2 (v1.32.0), openxlsx (v4.2.4), ggplot2 (v3.3.5), and dplyr (v1.0.7).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2 v1.32.0, GSEA, GSVA, R v4.1.0, ggplot2 v3.3.5, tidyverse v1.0.7]

### Number neurons in the nidopallium of young domestic chicks. (PNAS 2022)

- DOI: 10.1073/pnas.2201039119 | PMCID: PMC9371667 | PMID: 35917348
- Evidence: All statistical analyses and visualization of the data were performed in R ( 65 ) with packages “tidyverse,” “ggplot2,” and “PMCMRplus” and in MATLAB using custom-made scripts and the Curve Fitting Toolbox.
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> visualisation [R, ggplot2, tidyverse] -> stage not stated [PsychoPy]

### Comparing human and chimpanzee temporal lobe neuroanatomy reveals modifications to human language hubs beyond the frontotemporal arcuate fasciculus. (PNAS 2022)

- DOI: 10.1073/pnas.2118295119 | PMCID: PMC9282369 | PMID: 35787056
- Evidence: The analyses were performed using R studio (version 3.5.3; R Core Team 2019) and tidyverse ( 95 ), broom ( 96 ), and purrr ( 97 ) packages.
- Full pipeline: alignment/mapping [SPM] -> registration [FSL v5.0.10, SPM] -> differential/statistical testing [SPM] -> stage not stated [R, tidyverse]

### Emergent effects of global change on consumption depend on consumers and their resources in marine systems. (PNAS 2022)

- DOI: 10.1073/pnas.2108878119 | PMCID: PMC9173678 | PMID: 35446691
- Version used: **1.3.0**
- Evidence: All data manipulation and analyses were conducted using the statistical software, R (version 3.6.2) ( 60 ), with the associated packages tidyverse (version 1.3.0) ( 61 ) and metafor (version 2.4–0) ( 62 ).
- Full pipeline: differential/statistical testing [R v3.6.2, metafor v2.4, tidyverse v1.3.0]

### Infrastructure inequality is a characteristic of urbanization. (PNAS 2022)

- DOI: 10.1073/pnas.2119890119 | PMCID: PMC9169802 | PMID: 35377809
- Evidence: We analyzed the data in R ( https://www.r-project.org/ ) using ggplot2, sf, rgdal, Hmisc, spdep, spatialreg, raster, tmap, and dplyr packages and in python ( https://www.python.org/ ) programming languages using numpy, scipy, pandas, geopandas, osgeo, scikit-image, matplotlib, and rasterio packages.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, scikit-image, tidyverse]

### A widely distributed phosphate-insensitive phosphatase presents a route for rapid organophosphorus remineralization in the biosphere. (PNAS 2022)

- DOI: 10.1073/pnas.2118122119 | PMCID: PMC8812569 | PMID: 35082153
- Evidence: All statistical analyses and data visualizations were performed using the ggplot2, ggfortify, tidyr, plyr, serration, and rcolorbrewer packages in Rstudio (1.2.5033).
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [BLAST] -> differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [HMMER, IQ-TREE]

### Impact of ADAR-induced editing of minor viral RNA populations on replication and transmission of SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2112663119 | PMCID: PMC8833170 | PMID: 35064076
- Evidence: Data handling, statistical analyses, and graphical representation were performed in R, version 4.0.3 (packages tidyverse, naniar, tableone and ggplot2) ( 36 , 37 ) and in MS Excel.
- Full pipeline: differential/statistical testing [ggplot2, tidyverse] -> stage not stated [Python]

### Ship traffic connects Antarctica's fragile coasts to worldwide ecosystems. (PNAS 2022)

- DOI: 10.1073/pnas.2110303118 | PMCID: PMC8784123 | PMID: 35012982
- Evidence: Figures were created in R ( 86 ) using the packages “tidyverse” ( 87 ), “sf” ( 88 ), “tidygraph” ( 103 ), “ggraph” ( 107 ), “nngeo” ( 108 ), “raster” ( 109 ),“rnaturalearth” ( 106 ),“igraph” ( 101 ), “ggrepel” ( 110 ), and “cowplot” ( 89 ).
- Full pipeline: visualisation [igraph, tidyverse] -> stage not stated [R]

### THESEUS1 modulates cell wall stiffness and abscisic acid production in <i>Arabidopsis thaliana</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2119258119 | PMCID: PMC8740707 | PMID: 34949719
- Evidence: Statistical analyses were performed in R ( 66 ) using the packages ggplot2 ( 67 ), dplyr ( 68 ), multcomp ( 69 ), and lsmeans ( 70 ).
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [Fiji, ImageJ]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Version used: **1.3.0**
- Evidence: Accuracy scores were calculated and graphed using rlog-normalized read counts for the 1,500 P. gingivalis core genes ( Dataset S1 C ) in R version 4.0.2 with the following packages: tidyverse version 1.3.0, cowplot version 1.0.0, readr version 1.3.1, dplyr version 1.0.2, tidyr version 1.1.2, tibble version 3.0.3, purrr version 0.3.4, ggsunburst version 0.3.0, zeallot version 0.1.0, ggplot2 version...
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **1.3.1**
- Evidence: Packages ggplot2 v3.3.6, ggpubr v0.4.0 pheatmap v1.0.12, RColorBrewer v1.1-3, ggsignif v0.6.3, and tidyverse v1.3.1 were used for data manipulation and representation.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Proteome-wide tagging with an H&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;2&lt;/sub&gt; biosensor reveals highly localized and dynamic redox microenvironments. (PNAS 2023)

- DOI: 10.1073/pnas.2314043120 | PMCID: PMC10691247 | PMID: 37991942
- Evidence: Data handling, processing, and cleaning were done using R packages of the tidyverse collection ( 29 ): janitor, here, writexl, and readxl.
- Full pipeline: stage not stated [ggplot2, ggpubr, tidyverse]

### &lt;i&gt;INDETERMINATE1&lt;/i&gt;-mediated expression of &lt;i&gt;FT&lt;/i&gt; family genes is required for proper timing of flowering in &lt;i&gt;Brachypodium distachyon&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312052120 | PMCID: PMC10655584 | PMID: 37934817
- Evidence: To identify the candidate variants, BSA-sequencing data of phyC-1 were used as a control to subtract background variants by using the dplyr package in R [ https://CRAN.R-project.org/package=dplyr , ( 36 )].
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, SAMtools v1.9] -> stage not stated [Galaxy, featureCounts v1.6.2, tidyverse]

### Salicylic acid and RNA interference mediate antiviral immunity of plant stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302069120 | PMCID: PMC10589665 | PMID: 37824524
- Evidence: Visualization of the data was done by using the packages tidyverse ( 55 ) and ggplot2 ( 56 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2 v2.3.5] -> visualisation [Bioconductor, ggplot2, tidyverse] -> stage not stated [DESeq2, ImageJ, featureCounts]

### Resistance to host antimicrobial peptides mediates resilience of gut commensals during infection and aging in <i>Drosophila</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2305649120 | PMCID: PMC10483595 | PMID: 37639605
- Evidence: The R packages ggplot2, dplyr, and tidyverse were used for data visualization.
- Full pipeline: differential/statistical testing [R v4.2] -> visualisation [ggplot2, tidyverse] -> stage not stated [survival (R)]

### Synaptic and cellular endocannabinoid signaling mechanisms regulate stress-induced plasticity of nucleus accumbens somatostatin neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2300585120 | PMCID: PMC10450650 | PMID: 37590414
- Evidence: Briefly, R statistical software with the “tidyverse” package was used to convert X/Y position into speed of movement for the fiber and the tail during each frame.
- Full pipeline: differential/statistical testing [R, tidyverse] -> stage not stated [DeepLabCut]

### sccomp: Robust differential composition and variability analysis for single-cell data. (PNAS 2023)

- DOI: 10.1073/pnas.2203828120 | PMCID: PMC10438834 | PMID: 37549298
- Evidence: Data wrangling was done through tidyverse ( 61 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> machine learning [R] -> stage not stated [Seurat, Stan, limma, tidyverse]

### Optogenetic clustering and membrane translocation of the BcLOV4 photoreceptor. (PNAS 2023)

- DOI: 10.1073/pnas.2221615120 | PMCID: PMC10410727 | PMID: 37527339
- Evidence: The obtained values were exported into R (version 4.2.2) for data analysis using the dplyr ( 52 ) and ggplot2 ( 53 ) packages.
- Full pipeline: stage not stated [CellProfiler, ImageJ, R v4.2.2, ggplot2, tidyverse]

### MicroRNA-335-5p suppresses voltage-gated sodium channel expression and may be a target for seizure control. (PNAS 2023)

- DOI: 10.1073/pnas.2216658120 | PMCID: PMC10372546 | PMID: 37463203
- Evidence: All analyses were performed in RStudio (Rversion 4.1.3) ( 76 ) using the httr, dplyr, tidyr, and plyr packages ( 77 ).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [ComplexHeatmap, DESeq2, R, tidyverse]

### A simple mechanism for collective decision-making in the absence of payoff information. (PNAS 2023)

- DOI: 10.1073/pnas.2216217120 | PMCID: PMC10629567 | PMID: 37428910
- Evidence: ...( 74 ) (version 1.1.4), lme4 ( 75 ) (version 1.1-30), lmerTest ( 76 ) (version 3.1-3), DHARMa ( 77 ) (version 0.4.5), ggplot2 ( 78 ) (version 3.3.6), tidyr ( 79 ) (version 1.2.0), dplyr ( 80 ) (version 1.0.10), readr ( 81 ) (version 2.1.2), ggeffects ( 82 ) (version 1.1.3), survminer ( 83 ) (version 0.4.9), data.table ( 84 ) (version 1.14.2), viridis ( 85 ) (version 0.6.2), scales ( 86 ) (version ...
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.2.1, data.table, survival (R), tidyverse]

### Demographic consequences of phenological asynchrony for North American songbirds. (PNAS 2023)

- DOI: 10.1073/pnas.2221961120 | PMCID: PMC10334763 | PMID: 37399376
- Evidence: We used R package “MCMCvis” ( 92 ) to summarize, visualize, and manipulate all Bayesian model output and the “tidyverse” packages ( 93 ) for additional data manipulation.
- Full pipeline: differential/statistical testing [R, tidyverse] -> visualisation [tidyverse] -> stage not stated [Stan, phytools]

### Functional calcium-responsive parathyroid glands generated using single-step blastocyst complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2216564120 | PMCID: PMC10334775 | PMID: 37379351
- Evidence: Volcano plots were generated using ggplot2 and dplyr in R v4.1.2.
- Full pipeline: normalisation [DESeq2, R v4.1, ggplot2] -> dimensionality reduction/clustering [UMAP] -> visualisation [DESeq2, R v4.1, ggplot2] -> stage not stated [Seurat v4.2.1, tidyverse]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: RNA-seq analyses were performed using Seq2Pathway, fgsea, tidyverse, and dplyr software packages.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Graphical visualizations used the gplots, tidyverse, and ggplot2 packages.
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Genetic factors predict hybrid formation in the British flora. (PNAS 2023)

- DOI: 10.1073/pnas.2220261120 | PMCID: PMC10120012 | PMID: 37040419
- Evidence: All other data manipulation took place in R version 3.6.1 using base R and packages data.table ( 55 ) and dplyr ( 56 ).
- Full pipeline: visualisation [R] -> stage not stated [IQ-TREE, Python, data.table, ggplot2, tidyverse]

### Genomics-driven breeding for local adaptation of durum wheat is enhanced by farmers' traditional knowledge. (PNAS 2023)

- DOI: 10.1073/pnas.2205774119 | PMCID: PMC10083613 | PMID: 36972461
- Evidence: Data, Materials, and Software Availability Data management relied on R/tidyverse ( 65 ) and R/rgdal ( 66 ).
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [R, ggplot2, tidyverse]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Evidence: After initial fMRI preprocessing, additional steps to create the fMRI features for predictive models and reshape data were conducted using custom code in python 3.7.7 using the packages pandas ( 138 ) and numpy ( 139 ) and R 4.0.2 using the package collections tidyverse ( 140 ) and tidymodels ( 141 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### A mutant fitness assay identifies bacterial interactions in a model ocean hot spot. (PNAS 2023)

- DOI: 10.1073/pnas.2217200120 | PMCID: PMC10041152 | PMID: 36920927
- Evidence: All plots and statistical analyses were performed in R v4.0.1 ( 84 ) using the packages tidyverse ( 85 ) and data.table ( 86 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R v4.0, data.table, tidyverse]

### Estimating human mobility in Holocene Western Eurasia with large-scale ancient genomic data. (PNAS 2023)

- DOI: 10.1073/pnas.2218375120 | PMCID: PMC9992830 | PMID: 36821583
- Evidence: ...ma ( 98 ), latex2exp ( 99 ), lemon ( 100 ), progress ( 101 ), rnaturalearth ( 102 ), sf ( 103 ), smartsnp ( 104 ), viridis ( 105 ), and, finally, the tidyverse and the many packages within it ref.
- Full pipeline: quality control [ANGSD] -> stage not stated [R, ggpubr, igraph, tidyverse]

### Enhanced pathogenicity of Th17 cells due to natalizumab treatment: Implications for MS disease rebound. (PNAS 2023)

- DOI: 10.1073/pnas.2209944120 | PMCID: PMC9910615 | PMID: 36574650
- Evidence: Gene rankings were based on custom R-code and the R-package dplyr ( 54 ).
- Full pipeline: stage not stated [GSEA, fgsea, tidyverse]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Version used: **2.0.0**
- Evidence: Normalization and differential expression analysis was performed using DESeq2 v1.40.2 ( 80 ) defaults using R ( 81 ), RStudio v2023.9.0.463, and tidyverse v2.0.0 ( 82 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### The global spread of Oriental Horses in the past 1,500 years through the lens of the Y chromosome. (PNAS 2024)

- DOI: 10.1073/pnas.2414408121 | PMCID: PMC11626155 | PMID: 39556761
- Evidence: ( 66 ) and the tidyverse collection of packages ( 67 ).
- Full pipeline: stage not stated [tidyverse]

### Modeling extrahepatic hepatitis E virus infection in induced human primary neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2411434121 | PMCID: PMC11588080 | PMID: 39546567
- Evidence: Data visualization was done in the statistical programming language R with in-house scripts using the libraries tidyverse, tidytSingleCellExperiment, Seurat ggplot2, GO-plot, ComplexHeatmap, and venn.
- Full pipeline: differential/statistical testing [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> visualisation [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> stage not stated [CellProfiler, ImageJ]

### Proteins required for stereocilia elongation during mammalian hair cell development ensure precise and steady heights during adult life. (PNAS 2024)

- DOI: 10.1073/pnas.2405455121 | PMCID: PMC11459194 | PMID: 39320919
- Evidence: Analyses and visualizations were done in R 3.6.2 with tidyverse, ggpubr, and rstatix packages.
- Full pipeline: visualisation [R v3.6, ggpubr, tidyverse] -> stage not stated [ImageJ]

### Innate face-selectivity in the brain of young domestic chicks. (PNAS 2024)

- DOI: 10.1073/pnas.2410404121 | PMCID: PMC11459190 | PMID: 39316055
- Evidence: All statistical analyses and visualization of the data was performed in R ( 68 ) with packages “tidyverse,” multcomp, “ggplot2,” and “PMCMRplus” and in MATLAB using custom-made scripts.
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> visualisation [R, ggplot2, tidyverse] -> stage not stated [Kilosort v2.0]

### Charting the future of high forest low deforestation jurisdictions. (PNAS 2024)

- DOI: 10.1073/pnas.2306496121 | PMCID: PMC11406276 | PMID: 39226355
- Evidence: Statistical modeling and calculations were performed in R version 4.0.2, using the statistical and modeling packages “dplyr” v1.1.2, “MASS” v7.3-51.6, “smotefamily” v1.3.1, “ranger” v0.16.0, the visualization packages “ggplot2” v3.4.2 and “cowplot” v1.1.1, and the parallelization packages “foreach” v1.5.0 and “doParallel” v1.0.15.
- Full pipeline: differential/statistical testing [R v4.0.2, ggplot2, tidyverse] -> visualisation [R v4.0.2, ggplot2, tidyverse]

### A quantitative model of temperature-dependent diapause progression. (PNAS 2024)

- DOI: 10.1073/pnas.2407057121 | PMCID: PMC11388385 | PMID: 39196619
- Evidence: Other important R packages were tidyverse ( 60 ), lubridate ( 61 ), and bayestestR ( 62 ).
- Full pipeline: differential/statistical testing [R, Stan, brms] -> stage not stated [tidyverse]

### Maternal manipulation of offspring size can trigger the evolution of eusociality in promiscuous species. (PNAS 2024)

- DOI: 10.1073/pnas.2402179121 | PMCID: PMC11331107 | PMID: 39110731
- Version used: **2.0.0**
- Evidence: All data analysis and plotting were conducted in R v4.2.1 ( 77 ) using the R-packages tidyverse v2.0.0 ( 78 ), cowplot v1.1.1 ( 79 ), stringr v1.5.0 ( 80 ), and MetBrewer v.0.2.0 ( 81 ).
- Full pipeline: differential/statistical testing [brms v2.20.4, emmeans v1.8.8] -> stage not stated [R v4.2, tidyverse v2.0.0]

### Global expansion of marine protected areas and the redistribution of fishing effort. (PNAS 2024)

- DOI: 10.1073/pnas.2400592121 | PMCID: PMC11260147 | PMID: 38980905
- Evidence: We use the tidyverse suite of packages for all data wrangling tasks ( 69 ), and the tidymodels suite of packages for the general machine learning framework ( 70 ).
- Full pipeline: stage not stated [R, tidyverse]

### Relative decline in density of Northern Hemisphere tree species in warm and arid regions of their climate niches. (PNAS 2024)

- DOI: 10.1073/pnas.2314899121 | PMCID: PMC11252807 | PMID: 38954552
- Evidence: Changes in density across species’ climatic niches were visualized with terra and tidyverse R packages ( 65 , 66 ), and all analyses were performed using R Statistical Software [v4.2.0; ( 62 )].
- Full pipeline: differential/statistical testing [tidyverse] -> visualisation [tidyverse] -> stage not stated [R, lme4]

### Detecting recollection: Human evaluators can successfully assess the veracity of others' memories. (PNAS 2024)

- DOI: 10.1073/pnas.2310979121 | PMCID: PMC11145205 | PMID: 38781212
- Evidence: All statistical analyses were performed using R version 4.2.1 ( 62 ) with data wrangling, summaries, and pairwise tests performed using the tidyverse ( 63 ) and rstatix packages ( 64 ).
- Full pipeline: differential/statistical testing [R v4.2.1, tidyverse]

### The impact of age and number of mutations on the size of clonal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2319364121 | PMCID: PMC10895265 | PMID: 38359296
- Evidence: Statistical analyses were performed using the R statistical software (version 4.3.1), with visual plots drawn with the help of R packages “ggplot2” ( https://github.com/tidyverse/ggplot2 ) and “PICH” ( https://github.com/hfang-bristol/PICH ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard v2.23.0] -> differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, SnpEff v4.2]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: All data preprocessing was performed with the tidyverse ecosystem of R packages ( 48 ), and the statistical analysis was carried out using R software ( 49 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### Macroscale controls determine the recovery of river ecosystem productivity following flood disturbances. (PNAS 2024)

- DOI: 10.1073/pnas.2307065121 | PMCID: PMC10835108 | PMID: 38266048
- Evidence: Additional R packages used to extract, visualize, and analyze data include the tidyverse ( 79 ), here ( 80 ), shinystan ( 81 ), ggbreak ( 82 ), and patchwork ( 83 ) packages.
- Full pipeline: differential/statistical testing [brms] -> visualisation [tidyverse] -> stage not stated [R]

### Constraining the oxygen requirements for modern microbial eukaryote diversity. (PNAS 2024)

- DOI: 10.1073/pnas.2303754120 | PMCID: PMC10786294 | PMID: 38165897
- Evidence: Both O 2 and H 2 S values were visualized across depth and time using tidyverse and ggplot2 in R.
- Full pipeline: dimensionality reduction/clustering [DADA2] -> differential/statistical testing [R] -> machine learning [scikit-learn] -> visualisation [ggplot2, tidyverse] -> stage not stated [QIIME 2]

### Elevated risk of infectious diseases in adulthood after prenatal or early postnatal exposure to the Great Chinese Famine. (PNAS 2025)

- DOI: 10.1073/pnas.2513421122 | PMCID: PMC12685027 | PMID: 41284860
- Version used: **2.0.0**
- Evidence: All analyses were conducted using R 4.3.1, with packages tidyverse 2.0.0 ( 62 ) for data processing, INLA 23.04.24 ( 63 ) for fitting BAPC models, mgcv 1.8.42 ( 64 ) for fitting GAMs, metafor 4.0.0 ( 65 ) for fitting meta-regression models, foreach 1.5.2 ( 66 ) and doSNOW 1.0.20 ( 67 ) for parallel computation, and ggplot2 3.4.1 ( 68 ), tmap 3.3.3 ( 69 ), cowplot 1.1.1 ( 70 ), and ggsci 3.0.0 ( 71...
- Full pipeline: differential/statistical testing [R v4.3, ggplot2 v3.4.1, metafor v4.0.0, tidyverse v2.0.0] -> visualisation [ggplot2 v3.4.1]

### GWAS for behavioral traits in golden retrievers identifies genes implicated in human temperament, mental health, and cognition. (PNAS 2025)

- DOI: 10.1073/pnas.2421757122 | PMCID: PMC12684936 | PMID: 41284867
- Evidence: We tested for stratification and outliers by creating a centered relatedness matrix using the Genome-wide Efficient Mixed Model Analysis (GEMMA) Software v0.98.1 ( 75 ) which was transformed into distance matrices using the tidyverse package in R.4.2.2 ( 111 ) and visualized them on multidimensional scaling plots.
- Full pipeline: variant calling [PLINK v1.9] -> normalisation [GEMMA, tidyverse] -> dimensionality reduction/clustering [GEMMA, tidyverse] -> differential/statistical testing [MAGMA v1.10] -> visualisation [GEMMA, tidyverse] -> stage not stated [GCTA]

### The telomeric valine-arginine dipeptide repeat protein changes state to diffuse staining in mitosis and represses in vitro translation. (PNAS 2025)

- DOI: 10.1073/pnas.2520441122 | PMCID: PMC12663981 | PMID: 41269794
- Evidence: 4 was made using tidyverse, ggplot2 ( 56 ), and janitor ( 57 ) packages in R version 4.3.1.
- Full pipeline: stage not stated [ImageJ, R v4.3.1, ggplot2, tidyverse]

### p53 regulates the expression of histone modifiers to restrict stemness and maintain differentiated luminal identity in breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2522646122 | PMCID: PMC12595495 | PMID: 41160600
- Evidence: Box plots were generated with R, using ggplot2 and rstatix packages ( https://ggplot2.tidyverse.org . and https://rpkgs.datanovia.com/rstatix/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ggplot2, survival (R), tidyverse]

### Decreased hippocampal neurite density in late-middle-aged adults following prenatal exposure to higher levels of maternal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2420188122 | PMCID: PMC12595415 | PMID: 41144670
- Evidence: All analyses were conducted in R version 4.2.1 using a combination of base R and tidyverse functions ( 139 , 140 ).
- Full pipeline: stage not stated [FSL, FreeSurfer, MRtrix3, R v4.2.1, tidyverse]

### Morphological specializations of mosquito CO&lt;sub&gt;2&lt;/sub&gt;-sensing olfactory receptor neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2514666122 | PMCID: PMC12582328 | PMID: 41129220
- Evidence: Model implementation was conducted via the “cmdstanr” package in R (R package version 0.8.1, https://www.R-project.org/ ; https://discourse.mc-stan.org ; https://mc-stan.org/cmdstanr/ ), and data analysis and visualization were performed using the “tidyverse” suite ( 68 ).
- Full pipeline: alignment/mapping [IMOD] -> machine learning [R] -> visualisation [tidyverse] -> stage not stated [ImageJ, SciPy, Stan]

### Transpupillary in vivo two-photon imaging reveals enhanced surveillance of retinal microglia in diabetic mice. (PNAS 2025)

- DOI: 10.1073/pnas.2426241122 | PMCID: PMC12541322 | PMID: 41060759
- Evidence: All statistical analyses were performed using Excel software (Microsoft, Redmond, WA), MATLAB using built-in functions, and R (version 4.4.2; using the “tidyverse”, “multcomp”, “rstatix”, “nlme”, “emmeans”, and “PMCMRplus” packages).
- Full pipeline: differential/statistical testing [R v4.4.2, emmeans, tidyverse] -> stage not stated [ImageJ v1.54f]

### Disulfide cross-linked redox-sensitive peptide condensates are efficient cell delivery vehicles of molecular cargo. (PNAS 2025)

- DOI: 10.1073/pnas.2515427122 | PMCID: PMC12541440 | PMID: 41060763
- Evidence: The tidyverse, ggsci, and scales packages were utilized for data wrangling, visualization, and statistical analysis ( 5 , 6 ).
- Full pipeline: differential/statistical testing [tidyverse] -> visualisation [tidyverse] -> stage not stated [ImageJ, R v4.1.2]

### Founders predict trait evolution and population performance after evolutionary rescue in the red flour beetle. (PNAS 2025)

- DOI: 10.1073/pnas.2506244122 | PMCID: PMC12435296 | PMID: 40906810
- Evidence: Packages used for analysis and visualization were ggplot2, gridExtra, paletteer, dplyr, tidyr, forcats, hrbrthemes, viridis, corrplot, RColorBrewer, survival, sjstats, segmented, broom, ggpubr, MASS, and vegan.
- Full pipeline: visualisation [ggplot2, ggpubr, tidyverse] -> stage not stated [R v3.4.4]

### The rise of diversity terminology in biomedical research. (PNAS 2025)

- DOI: 10.1073/pnas.2401805122 | PMCID: PMC12403007 | PMID: 40828015
- Evidence: After constructing the three dictionaries, we used the tidyverse and tidytext packages written in the R programming language to conduct several preprocessing steps that standardized our text data ( 77 , 78 ), including converting text to lower case, removing special characters and numbers, recoding select compound and hyphenated terms, and then classifying each term into the H1, H2, and H3 categor...
- Full pipeline: stage not stated [tidyverse]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: ..., library(GO.db), library(org.Hs.eg.db), library(org.Mm.eg.db), library(data.table), library(circlize), library(gridExtra), library(ggplot2), library(dplyr)})) # Set new working directory setwd(“”) # Load significant genes dataset Significant_Genes <- read.csv(“Significant_Genes.txt”, sep=””) # Load normalized expression values norm_vals <- read.delim(“norm_vals.xls”) # Merge data based on the “sy...
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### Asymmetric development and function of paired sperm-storage organs in &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2512096122 | PMCID: PMC12403100 | PMID: 40828028
- Version used: **2.0.0**
- Evidence: Statistical analysis was performed in R v4.4.1 with the following packages: tidyverse v2.0.0, lme4 v1.1–35.5, and emmeans v1.10.6.
- Full pipeline: differential/statistical testing [R v4.4, emmeans v1.10.6, lme4 v1.1, tidyverse v2.0.0]

### A universal of speech timing: Intonation units form low-frequency rhythms. (PNAS 2025)

- DOI: 10.1073/pnas.2425166122 | PMCID: PMC12403009 | PMID: 40828013
- Evidence: To this end, we used the identify_outliers function in the R package rstatix ( 140 ) and the anti_join function in the package dplyr ( 141 ).
- Full pipeline: stage not stated [R, tidyverse]

### Cognitive bridge between geometric and numerical learning in monkeys. (PNAS 2025)

- DOI: 10.1073/pnas.2502101122 | PMCID: PMC12403012 | PMID: 40825124
- Evidence: All data processing, analyses, and visualizations were performed in R using libraries dplyr , tidyr , ggplot2 , and lme4 .
- Full pipeline: visualisation [ggplot2, lme4, tidyverse]

### Split-YFP-coupled interaction-dependent TurboID identifies new functions of basal cell polarity in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2502445122 | PMCID: PMC12358837 | PMID: 40768356
- Evidence: The complete LFQ data are provided as Dataset S3 , and the detailed R scripts for candidate enrichment analysis are as below: library(“dplyr”) library(“DEP”) library(SummarizedExperiment) data<-read.csv(“MS6226-MS5931_PD data/MQ data.csv,”stringsAsFactors=FALSE) des<-read.csv(“Design.csv”,stringsAsFactors=FALSE) data_unique <- make_unique(data, “Gene.names,” “Protein.
- Full pipeline: dimensionality reduction/clustering [STRING db] -> stage not stated [ImageJ, tidyverse]

### Evolution and evolvability of rifampicin resistance across the bacterial tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2424307122 | PMCID: PMC12337354 | PMID: 40737327
- Version used: **2.0.0**
- Evidence: Data wrangling and visualization were performed using packages tidyverse v2.0.0 ( 73 ), ggnewscale v0.4.10 ( 74 ), GGally v2.2.1 ( 75 ), ggpubr v0.6.0 ( 76 ), ggh4x v0.2.8 ( 77 ), RColorBrewer v1.1-3 ( 78 ), patchwork v1.2.0 ( 79 ), NGLvieweR ( 80 ), and htmlwidgets ( 81 ).
- Full pipeline: visualisation [ggpubr v0.6.0, tidyverse v2.0.0] -> stage not stated [R v4.4.1]

### Indigenous territories and protected areas are crucial for ecosystem connectivity in the Amazon basin. (PNAS 2025)

- DOI: 10.1073/pnas.2418189122 | PMCID: PMC12337320 | PMID: 40720645
- Version used: **1.3.1**
- Evidence: Additional R packages used for data curation were terra v.1.8.5 ( 112 ), tidyverse v.1.3.1 ( 113 ); ggplot2 v.3.5.1 ( 114 ) was used for data visualization.
- Full pipeline: visualisation [ggplot2 v3.5.1, tidyverse v1.3.1] -> stage not stated [QGIS, emmeans, lme4]

### Genetic rescue of Florida panthers reduced homozygosity but did not swamp ancestral genotypes. (PNAS 2025)

- DOI: 10.1073/pnas.2410945122 | PMCID: PMC12337334 | PMID: 40720660
- Evidence: Using dplyr library ( 54 ) and custom scripts in R, we averaged their ancestry to obtain a mean value of ancestry proportion per window.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK v4.2, SAMtools] -> variant calling [GATK v4.2] -> normalisation [BEDTools] -> visualisation [BEDTools] -> stage not stated [RepeatMasker, SnpEff, tidyverse]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Evidence: Data manipulations in R were performed with the tidyverse package ( 99 ).
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Methane-powered sea spiders: Diverse, epibiotic methanotrophs serve as a source of nutrition for deep-sea methane seep &lt;i&gt;Sericosura&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2501422122 | PMCID: PMC12232434 | PMID: 40523202
- Evidence: Percent stacked bar charts were made with R packages dplyr ( 48 ) and tidyverse ( 49 ) in order to depict microbiome data [v4.3.1 ( 50 )].
- Full pipeline: quality control [FastQC v1.13] -> read trimming [DADA2] -> stage not stated [tidyverse]

### Mapping encounters between Antarctic krill fishing vessels and air-breathing krill predators using acoustic data from the fishery. (PNAS 2025)

- DOI: 10.1073/pnas.2417203122 | PMCID: PMC12207417 | PMID: 40523191
- Evidence: All subsequent analysis was done in R ( 60 ) with help of the terra ( 61 ), tidyterra ( 62 ), tidyverse ( 63 ), and scico ( 64 ) packages.
- Full pipeline: stage not stated [R, tidyverse]

### Independent transitions to fully planktonic life cycles shaped the global distribution of medusozoans in the epipelagic zone. (PNAS 2025)

- DOI: 10.1073/pnas.2415979122 | PMCID: PMC12146771 | PMID: 40440075
- Evidence: Data analysis and statistical tests were performed using R [v4.4.1; ( 72 )] with the packages vegan [v2.6-6.1; ( 73 )], tidyverse [v2.0.0; ( 74 )], and custom scripts (available in Zenodo).
- Full pipeline: alignment/mapping [BLAST, phytools] -> differential/statistical testing [tidyverse, vegan] -> stage not stated [R, igraph]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Evidence: Violin plots were created in R Studio using the package ggplot2 v3.5.1 ( https://ggplot2.tidyverse.org ).
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### A combined experimental and computational analysis of mantATP turnover in skinned muscle fibers. (PNAS 2025)

- DOI: 10.1073/pnas.2502652122 | PMCID: PMC12107101 | PMID: 40372438
- Evidence: Data were further processed using R (V 4.2.2), with the libraries: tidyverse, diann, data.table, magrittr, FactoMineR, factoextra and ggplot2, gprofiler, ggplot2.
- Full pipeline: stage not stated [data.table, ggplot2, tidyverse]

### Distinguishing species boundaries from geographic variation. (PNAS 2025)

- DOI: 10.1073/pnas.2423688122 | PMCID: PMC12088384 | PMID: 40324080
- Evidence: We also used Plink 1.9 ( 81 ) to calculate missing data proportions and processed results using the vcfR ( 82 ) and tidyverse ( 83 ) packages in R.
- Full pipeline: visualisation [ggplot2] -> stage not stated [ADMIXTURE v1.3.0, R, RAxML, VCFtools v0.1.13, tidyverse, vegan]

### Ultrasound-activated cilia for biofilm control in indwelling medical devices. (PNAS 2025)

- DOI: 10.1073/pnas.2418938122 | PMCID: PMC12067268 | PMID: 40294275
- Version used: **1.0.7**
- Evidence: Images were imported into R (version 4.2.2) for further statistical analysis and visualization using packages such as ggplot2 (v3.3.5), dplyr (v1.0.7), and viridis (v0.6.2).
- Full pipeline: differential/statistical testing [R v4.2.2, ggplot2 v3.3.5, tidyverse v1.0.7] -> visualisation [R v4.2.2, ggplot2 v3.3.5, tidyverse v1.0.7] -> stage not stated [ImageJ]

### In situ cavitation bubble manometry reveals a lack of light-activated guard cell turgor modulation in bryophytes. (PNAS 2025)

- DOI: 10.1073/pnas.2419887122 | PMCID: PMC12002306 | PMID: 40138347
- Evidence: We compared the mean bubble dissolution times between cell types (epidermal vs. guard cells) and treatments (light vs dark acclimated) using standard t tests and ANOVA using the dplyr package in R.
- Full pipeline: stage not stated [ImageJ, tidyverse]

### iPSCs engrafted in allogeneic hosts without immunosuppression induce donor-specific tolerance to secondary allografts. (PNAS 2025)

- DOI: 10.1073/pnas.2413398122 | PMCID: PMC11929385 | PMID: 40073064
- Evidence: The results were visualized using R (v4.0.1) and the Seurat, ggplot2, and dplyr packages. scRNA-seq Analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2, tidyverse] -> stage not stated [R, Seurat v4.0.1]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Evidence: Heatmaps of expression data were generated by the ggplot2 R package ( https://ggplot2.tidyverse.org ) using Z -normalized FPKM.
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### Mycorrhiza increases plant diversity and soil carbon storage in grasslands. (PNAS 2025)

- DOI: 10.1073/pnas.2412556122 | PMCID: PMC11848320 | PMID: 39937867
- Version used: **1.1.4**
- Evidence: All statistical analyses except SEM were conducted in R, and the following packages: argicolae v.1.3-5, lme4 v.1.1-30, ggtext v.0.1.1, ggplot2 v.3.3.5, ggpubr v.0.4.0, tidyr v.1.1.4, and vegan v.2.5-7 were used.
- Full pipeline: differential/statistical testing [ggplot2 v3.3.5, ggpubr v0.4.0, lme4 v1.1, tidyverse v1.1.4]

### Prey depletion, interspecific competition, and the energetics of hunting in endangered African wild dogs, &lt;i&gt;Lycaon pictus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2414772122 | PMCID: PMC11831116 | PMID: 39869818
- Evidence: ...umption that observations were independent (first confirming that the lag one autocorrelation was strong, and all other lags were weak.) We then used dplyr to aggregate the data from minutes to days, calculating total distance moved, the number of hunting efforts and kills, mean prey biomass and mean lion utilization for each day.
- Full pipeline: quantification [R] -> stage not stated [JAGS, tidyverse]

### Life history is a key driver of temporal fluctuations in tropical tree abundances. (PNAS 2025)

- DOI: 10.1073/pnas.2422348122 | PMCID: PMC11789054 | PMID: 39854224
- Version used: **1.0.10**
- Evidence: Code samples used to generate results and figures used R version 4.2.2 with reshape2 version 1.4.4, dplyr version 1.0.10, and tidyr version 1.2.1., and are available in a Zenodo archive ( 110 ).
- Full pipeline: stage not stated [R v4.2.2, tidyverse v1.0.10]

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

### Atlantic to Pacific: Outbreak of bivalve transmissible neoplasia detected in hybridizing soft-shell clams and eDNA in Puget Sound. (PNAS 2026)

- DOI: 10.1073/pnas.2611852123 | PMCID: PMC13320677 | PMID: 42335235
- Evidence: Maps were generated using R packages ggplot ( 40 ), ggmap ( 41 ), and dplyr ( 42 ).
- Full pipeline: alignment/mapping [BLAST] -> stage not stated [tidyverse]

### Mating-dependent lifespan cost of sterol depletion in male &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2533735123 | PMCID: PMC13250600 | PMID: 42228537
- Evidence: Data wrangling was carried out using dplyr ( 33 ) and tidyverse ( 34 ), and figures were made using ggplot2 ( 35 ).
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2, tidyverse] -> stage not stated [emmeans]

### Egress thresholds and wildfire fatalities. (PNAS 2026)

- DOI: 10.1073/pnas.2535081123 | PMCID: PMC13250580 | PMID: 42224582
- Evidence: R analyses relied on the following packages: tidyverse, sf, rnaturalearth, rnaturalearthdata, RColorBrewer, scales, tidycensus, ggpubr, biscale, dplyr, ggplot2, and minpack.lm.
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, R v4.4.0, ggplot2, ggpubr, tidyverse]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: The analysis was implemented in R, using the dplyr and emmeans packages to compute genotype means, mean differences, SE, CI, and P -values, ensuring statistical inference.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Version used: **1.1.4**
- Evidence: Data manipulation and preprocessing were performed using dplyr (v 1.1.4) and tidyverse (v 2.0.0) in R.
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: These datasets were then classified into bins using the tidyverse and plotted as histograms with ggplot2 ( 46 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### A systematic map of methods for assessing societal benefits of Earth science information. (PNAS 2026)

- DOI: 10.1073/pnas.2524370123 | PMCID: PMC12890935 | PMID: 41650232
- Evidence: All analysis and figures were generated using R statistical software version 4.4.1 ( 77 ) and the tidyverse metapackage version 2.0.0 ( 78 ).
- Full pipeline: differential/statistical testing [tidyverse] -> visualisation [tidyverse] -> stage not stated [R]

### Plant diversity influences plant volatile emission with varying effects at the species and community levels. (PNAS 2026)

- DOI: 10.1073/pnas.2518326123 | PMCID: PMC12818445 | PMID: 41538247
- Evidence: All statistical analyses and data visualization were conducted in R version 4.5.1 ( 82 ) using the rBExIS, dplyr , tidyverse , tibble, and janitor for data retrieval, cleaning, and formatting ( 83 – 86 ).
- Full pipeline: differential/statistical testing [R v4.5.1, lme4, tidyverse] -> visualisation [ComplexHeatmap, R v4.5.1, ggplot2, pheatmap, tidyverse] -> stage not stated [mothur, phyloseq]

### Molecular determinants of ligand efficacy and potency in GPCR signaling. (Science 2023)

- DOI: 10.1126/science.adh1859 | PMCID: PMC7615523 | PMID: 38127743
- Evidence: The following packages were used: tidyverse (especially dplyr, ggplot2, purrr, tibble, tidyr, forcats, stringr), plotly, MASS, reshape, reshape2, ggrepel, patchwork, ggpubr, bio3d ( 53 ), openxlsx.
- Full pipeline: stage not stated [GROMACS, MDTraj, PyMOL v2.5.2, R v4.0, ggplot2, ggpubr, tidyverse]

### Diverse phage communities are maintained stably on a clonal bacterial host. (Science 2024)

- DOI: 10.1126/science.adk1183 | PMCID: PMC7617280 | PMID: 39666794
- Version used: **2.0.0**
- Evidence: We conducted statistical tests using R version 4.2.0 (2022-04-22) ( 61 ) and using tidyverse version 2.0.0 ( 62 ).
- Full pipeline: differential/statistical testing [tidyverse v2.0.0] -> visualisation [R] -> stage not stated [BLAST, SPAdes v3.15.0]

### The immunopathological landscape of human pre-TCRα deficiency: From rare to common variants. (Science 2024)

- DOI: 10.1126/science.adh4059 | PMCID: PMC10958617 | PMID: 38422122
- Evidence: Statistical analyses and figures were produced with RStudio (version 2023.03.1 Build 446, Posit Software, rstudio.com ), using R Statistical Software (version 4.3.0, R Core Team 2023, R-project.org ) and the tidyverse package (version 2.0.0, Posit Software, tidyverse.org ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, SAMtools v1.14] -> differential/statistical testing [R, tidyverse] -> visualisation [R, tidyverse] -> stage not stated [MACS2, Seurat v4.0.4, kallisto v0.46.1]

### Mitochondria protect against an intracellular pathogen by restricting access to folate. (Science 2025)

- DOI: 10.1126/science.adr6326 | PMCID: PMC12483063 | PMID: 40811546
- Evidence: Exploratory data analysis and visualization was done using tidyverse in R ( 56 , 57 ).
- Full pipeline: differential/statistical testing [limma] -> visualisation [R, tidyverse]

