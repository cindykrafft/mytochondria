# data.table

- **Category:** general
- **Papers in survey:** 34
- **Journals:** Nature (21), PNAS (9), Cell (2), Science (1), Lancet (1)
- **Years:** 2021 (5), 2022 (2), 2023 (9), 2024 (7), 2025 (9), 2026 (2)
- **Versions named:** 1.14.2 (4), 1.14.8 (3), 1.12.8 (2), 1.14.6 (1), 1.13.2 (1), 1.13.3 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (2), visualisation (1), simulation/modelling (1), normalisation (1), differential/statistical testing (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Evidence: Data analysis was done using custom scripts and with the following packages: rawDiag ( Trachsel et al., 2018 ) and data.table ( Dowle and Srinivasan, 2019 ).
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### SARS-CoV-2 mRNA vaccination elicits a robust and persistent T follicular helper cell response in humans. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.026 | PMCID: PMC8695127 | PMID: 35026152
- Evidence: 3.0.3 Shugay et al., 2014 https://github.com/milaboratory/mixcr data.table R package v.
- Full pipeline: stage not stated [R, data.table, ggplot2, igraph]

### Past SARS-CoV-2 infection protection against re-infection: a systematic review and meta-analysis. (Lancet 2023)

- DOI: 10.1016/s0140-6736(22)02465-5 | PMCID: PMC9998097 | PMID: 36930674
- Evidence: 27 Tidyverse, data.table, stringi, ggplot2, forestplot, formattable, crosswalk002, metafor, and mrbrt002 packages were used.
- Full pipeline: stage not stated [R v1.4.1103, data.table, ggplot2, metafor]

### Rare variant contribution to human disease in 281,104 UK Biobank exomes. (Nature 2021)

- DOI: 10.1038/s41586-021-03855-y | PMCID: PMC8458098 | PMID: 34375979
- Version used: **1.12.8**
- Evidence: R libraries data.table (v1.12.8; https://CRAN.R-project.org/package=data.table ), MASS (7.3-51.6; https://www.stats.ox.ac.uk/pub/MASS4/ ), tidyr (1.1.0; https://CRAN.R-project.org/package=tidyr ) and dplyr (1.0.0; https://CRAN.R-project.org/package=dplyr ) were also used.
- Full pipeline: differential/statistical testing [R] -> stage not stated [REGENIE v2.0.2, SAIGE, SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Version used: **1.13.2**
- Evidence: ...atics) (v0.11.7), UMI-tools 42 (v1.1.1), cutadapt 37 (v1.16), HISAT2 (v2.1.0) 38 , SAMtools (v1.9) 39 , deepTools 41 (v3.1.0), BEDTools 43 (v2.30.0), data.table (v1.13.2), GenomicFeatures 44 (v1.38.2), edgeR 45 , 46 (v3.28.1), and GAT 47 (v1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Rare variant associations with plasma protein levels in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06547-x | PMCID: PMC10567546 | PMID: 37794183
- Version used: **1.12.8**
- Evidence: R libraries data.table (v.1.12.8; https://CRAN.R-project.org/package=data.table ), MASS (7.3-51.6; https://www.stats.ox.ac.uk/pub/MASS4/ ), tidyr (1.1.0; https://CRAN.R-project.org/package=tidyr ) and dplyr (1.0.0; https://CRAN.R-project.org/package=dplyr ) were also used.
- Full pipeline: alignment/mapping [GATK, Mutect2 v4.2.2.0] -> variant calling [GATK, Mutect2 v4.2.2.0] -> differential/statistical testing [R] -> stage not stated [SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Evidence: For each base, information for cell barcode and UMI was obtained by setting the --output-extra option, and subsequently collapsed using R and the data.table package.
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **1.14.6**
- Evidence: For I/O operations and general data manipulations, the R packages tidyverse (v1.3.2) 61 , data.table (v1.14.6) 62 , readxl (v1.4.1) 63 , fst (0.9.8) 64 , and qusage (v2.28.0) 65 – 67 were used.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Antibodies against endogenous retroviruses promote lung cancer immunotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05771-9 | PMCID: PMC10115647 | PMID: 37046094
- Version used: **1.14.2**
- Evidence: The packages dplyr (v.1.0.7), data.table (v.1.14.2), tidyverse (v.1.3.1) and rjson (v.0.2.20) were used for data handling in R.
- Full pipeline: quantification [Salmon v0.12.0] -> differential/statistical testing [lme4 v1.1.27.1] -> stage not stated [QuPath v0.3, R, RepeatMasker, data.table v1.14.2, survival (R) v3.2.13, tidyverse v1.0.7]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: The method was implemented in R, making use of the package data.table.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### NK2R control of energy expenditure and feeding to treat metabolic diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-08207-0 | PMCID: PMC11602716 | PMID: 39537932
- Version used: **1.14.2**
- Evidence: Data were loaded and manipulated using data.table (1.14.2) and tidyverse (1.3.1).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> stage not stated [GEMMA, Seurat v4.3.0, VEP, data.table v1.14.2, tidyverse v1.3.1]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Evidence: The mutations within a VAF quantile bin were classified as either overlapping or not overlapping with the genomic span of the most highly expressed genes (stratum 6) using the R data.table foverlaps function 94 .
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Natural proteome diversity links aneuploidy tolerance to protein turnover. (Nature 2024)

- DOI: 10.1038/s41586-024-07442-9 | PMCID: PMC11153158 | PMID: 38778096
- Evidence: First, the evidence.txt was loaded with the fread function from the data.table package, filtered for lysine-containing peptides and cleaned from potential contaminants and remaining reverse hits.
- Full pipeline: read trimming [edgeR] -> quantification [R, edgeR] -> normalisation [edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold, GSEA, STRING db, data.table]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Handling of geospatial and other data was conducted using the R packages lme4, matrixStats, Matrix, geojsonio, raster, rgeos, sf, sp, tmaptools, patchwork, leaflet, data.table, dplyr, haven, Hmisc, openxlsx, rgdal, scales, stringr, tidyr, tibble, xlsx, rfPermute, randomForest, forcats, and in python using the packages pandas, numpy, scipy, statsmodels, firthlogist, patsy and jupyter 68 – 97 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Transient loss of Polycomb components induces an epigenetic cancer fate. (Nature 2024)

- DOI: 10.1038/s41586-024-07328-w | PMCID: PMC11096130 | PMID: 38658752
- Version used: **1.14.2**
- Evidence: Computations on genomic coordinate files and downstream computations were conducted using the data.table R package (data.table: Extension of ‘data.frame’. https://r-datatable.com , https://Rdatatable.gitlab.io/data.table , https://github.com/Rdatatable/data.table , v.1.14.2).
- Full pipeline: quality control [fastp] -> alignment/mapping [DESeq2, SAMtools, featureCounts] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [GATK, Mutect2, R, data.table v1.14.2]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.14.8**
- Evidence: R (v.4.1.3): cluster (v.2.1.2) 138 , ComplexHeatmap (v.2.10.0) 139 , 140 , data.table (v.1.14.8) 141 , DescTools (v.0.99.48) 142 , dplyr (v.1.1.2) 143 , gdata (v.2.19.0) 144 , ggforce (v.0.4.1) 145 , ggplot2 (v.3.4.2) 146 , ggpmisc (v.0.5.3) 147 , ggpointdensity (v.0.1.0) 148 , ggpubr (v.0.5.0) 149 , ggrastr (v.1.0.2) 150 , ggrepel (v.0.9.3) 151 , grid (v.4.1.3) 152 , gridExtra (v.2.3) 153 , gtabl...
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Box and whisker plots were generated by first converting gene names into region bed files using the R packages biomaRt, data.table, dplyr and GenomicRanges.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Additional R packages used include Presto, DESeq2, dplyr, ply, ape, cowplot, Matrix, variancePartition, MAST, HGNChelper, openxlsx, RColorBrewer, gridExtra, ggpubr, ComplexHeatmap, tidyverse, tibble, biomaRt, data.table, glmGamPoi, SeuratWrappers, patchwork, magrittr, s2, gplots, stringr, ggnewscale, ggbreak, coin and dunn.test.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **1.14.2**
- Evidence: The session used the following libraries: cluster (2.1.2), celldex (1.4.0), data.table (1.14.2), enrichplot (1.14.1), ggpubr (0.4.0), GO.db (3.14.0), clusterProfiler (4.2.2), genesorteR (0.4.3), RColorBrewer (1.1-2), slingshot (2.2.0), TrajectoryUtils (1.2.0), princurve (2.1.6), scRNAseq (2.8.0), pathview (1.34.0), limma (3.50.0), dynamicTreeCut (1.63-1), dendextend (1.15.2), pheatmap (1.0.12), cl...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: A custom R script with ggplot2 74 and data.table packages 92 was used to plot the distribution of frequencies of different SNP ratio classes.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Clonal driver neoantigen loss under EGFR TKI and immune selection pressures. (Nature 2025)

- DOI: 10.1038/s41586-025-08586-y | PMCID: PMC11946900 | PMID: 39972134
- Version used: **1.14.8**
- Evidence: Analysis was conducted in R using the dplyr (v.1.1.4), immunarch (v.0.9.1), data.table (v.1.14.8), RColorBrewer (v.1.1-3), viridis (v.0.6.5) and ggplot2 (v.3.5.1) packages.
- Full pipeline: stage not stated [data.table v1.14.8, ggplot2 v3.5.1, tidyverse v1.1.4]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Positive and negative matrices were converted to data frames and then combined using rbindlist() from the package data.table ( https://github.com/Rdatatable/data.table ) by alternating lines according to the row number in the data frame such that, for every line of positive-strand scores on a sequence, the next line is corresponding scores for the motif reverse complement on that same sequence.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **1.14.8**
- Evidence: Postprocessing and data visualization were performed in R (v.4.4.1) using data.table (v.1.14.8), ggplot2 (v.3.4.2), pheatmap (v.1.0.12) and ComplexHeatmap (v.2.16.0).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: Data were read with either data.table 161 v.1.15.4 or readxl 162 v.1.4.3.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: The implementation relies significantly upon the R packages data.table ( 52 ), ggplot2 ( 53 ), ggspatial ( 54 ), rnaturalearth ( 55 ), and pheatmap ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Ancient DNA from Guam and the peopling of the Pacific. (PNAS 2021)

- DOI: 10.1073/pnas.2022112118 | PMCID: PMC7817125 | PMID: 33443177
- Evidence: We used the tidyverse ( 98 ), data.table ( https://CRAN.R-project.org/package=data.table ), Hmisc ( https://CRAN.R-project.org/package=Hmisc ), and pheatmap ( https://CRAN.R-project.org/package=pheatmap ) packages.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, R, data.table, pheatmap, tidyverse]

### A simple mechanism for collective decision-making in the absence of payoff information. (PNAS 2023)

- DOI: 10.1073/pnas.2216217120 | PMCID: PMC10629567 | PMID: 37428910
- Evidence: ...9 ) (version 1.2.0), dplyr ( 80 ) (version 1.0.10), readr ( 81 ) (version 2.1.2), ggeffects ( 82 ) (version 1.1.3), survminer ( 83 ) (version 0.4.9), data.table ( 84 ) (version 1.14.2), viridis ( 85 ) (version 0.6.2), scales ( 86 ) (version 1.2.1), and survival ( 87 ) (version 3.4-0).
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.2.1, data.table, survival (R), tidyverse]

### Genetic factors predict hybrid formation in the British flora. (PNAS 2023)

- DOI: 10.1073/pnas.2220261120 | PMCID: PMC10120012 | PMID: 37040419
- Evidence: All other data manipulation took place in R version 3.6.1 using base R and packages data.table ( 55 ) and dplyr ( 56 ).
- Full pipeline: visualisation [R] -> stage not stated [IQ-TREE, Python, data.table, ggplot2, tidyverse]

### Oceanographic connectivity explains the intra-specific diversity of mangrove forests at global scales. (PNAS 2023)

- DOI: 10.1073/pnas.2209637120 | PMCID: PMC10083552 | PMID: 36996109
- Evidence: All analyses were performed in R (R Development Core Team, 2018) using the R packages “bigmemory,” “data.table,” “dismo,” “doparallel,” “geosphere,” “gstat,” “igraph,” “raster,” and “vegan.” The source code for biophysical modeling is available in Supplementary Information 5 ( 60 ).
- Full pipeline: stage not stated [R, data.table, igraph]

### A mutant fitness assay identifies bacterial interactions in a model ocean hot spot. (PNAS 2023)

- DOI: 10.1073/pnas.2217200120 | PMCID: PMC10041152 | PMID: 36920927
- Evidence: All plots and statistical analyses were performed in R v4.0.1 ( 84 ) using the packages tidyverse ( 85 ) and data.table ( 86 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R v4.0, data.table, tidyverse]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: ...rary(sqldf), library(hopach), library(edgeR), library(limma), library(GOstats), library(GO.db), library(org.Hs.eg.db), library(org.Mm.eg.db), library(data.table), library(circlize), library(gridExtra), library(ggplot2), library(dplyr)})) # Set new working directory setwd(“”) # Load significant genes dataset Significant_Genes <- read.csv(“Significant_Genes.txt”, sep=””) # Load normalized expression...
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### Chlorophyll trends are negative for lakes but positive for estuarine-coastal waters. (PNAS 2025)

- DOI: 10.1073/pnas.2502289122 | PMCID: PMC12280897 | PMID: 40623175
- Evidence: Aside from the default packages loaded with R base, we mainly used data.table ( 42 ), wql ( 43 ), a fork of our archived wq package, for trend calculations, and ggplot2 ( 44 ) for graphics.
- Full pipeline: stage not stated [data.table, ggplot2]

### A combined experimental and computational analysis of mantATP turnover in skinned muscle fibers. (PNAS 2025)

- DOI: 10.1073/pnas.2502652122 | PMCID: PMC12107101 | PMID: 40372438
- Evidence: Data were further processed using R (V 4.2.2), with the libraries: tidyverse, diann, data.table, magrittr, FactoMineR, factoextra and ggplot2, gprofiler, ggplot2.
- Full pipeline: stage not stated [data.table, ggplot2, tidyverse]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **1.13.3**
- Evidence: Analyses in R (4.0.2) ( 60 ) were conducted using the following main packages: brms (2.13.9) ( 58 , 59 ), rstanarm (2.21.1) ( 91 ), rstan (2.21.2) ( 92 ), data.table (1.13.3) ( 93 ), and ggplot2 (3.3.2) ( 94 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

