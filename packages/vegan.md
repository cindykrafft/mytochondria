# vegan

- **Category:** microbiome
- **Papers in survey:** 71
- **Journals:** PNAS (48), Nature (21), Cell (2)
- **Years:** 2021 (3), 2022 (9), 2023 (10), 2024 (13), 2025 (29), 2026 (7)
- **Versions named:** 2.6 (9), 2.5 (4), 2.6.4 (1), 2.7 (1)
- **Pipeline stages it appears in:** differential/statistical testing (14), dimensionality reduction/clustering (7), visualisation (7), quantification (4), normalisation (4), variant calling (1)

## Papers

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **2.5**
- Evidence: 1.38.0), vegan (v.2.5-7), microbiome (v.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Cervicovaginal microbiome and natural history of Chlamydia trachomatis in adolescents and young women. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.011 | PMCID: PMC12035847 | PMID: 39818212
- Evidence: Statistical significance in α-diversity was determined using the Wilcoxon rank sum test using a core function R, while PERMANOVA was used to assess significance and obtain R 2 in β-diversity with the vegan R package.
- Full pipeline: quantification [DADA2] -> dimensionality reduction/clustering [DADA2] -> differential/statistical testing [DADA2, R, vegan] -> machine learning [DADA2] -> stage not stated [ggplot2, phyloseq]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Evidence: Bray–Curtis dissimilarity was used as β -diversity metric and computed using vegdist of the vegan package in R (v.3.5.3).
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### The landscape of genomic structural variation in Indigenous Australians. (Nature 2023)

- DOI: 10.1038/s41586-023-06842-7 | PMCID: PMC10733147 | PMID: 38093003
- Evidence: We then used the vegdist function from the vegan R package to calculate the dissimilarity between individuals based on their variant composition using Bray–Curtis methodology.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools] -> visualisation [ggplot2] -> stage not stated [BEDTools, R, RepeatMasker v4.1.2, ape (R), vegan]

### Distinguishing features of long COVID identified through immune profiling. (Nature 2023)

- DOI: 10.1038/s41586-023-06651-y | PMCID: PMC10620090 | PMID: 37748514
- Evidence: The PERMANOVA test was run using the vegan package in R 63 .
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> visualisation [ComplexHeatmap] -> stage not stated [edgeR, vegan]

### Synergy and oxygen adaptation for development of next-generation probiotics. (Nature 2023)

- DOI: 10.1038/s41586-023-06378-w | PMCID: PMC10412450 | PMID: 37532933
- Evidence: Differences in composition were tested by a permutational multivariate ANOVA using the adonis2 function with 10,000 permutations in the vegan package in R ( https://github.com/vegandevs/vegan/ ).
- Full pipeline: alignment/mapping [Kraken2] -> quantification [Bracken] -> differential/statistical testing [R, vegan] -> stage not stated [Bowtie2 v2.3.5.1, Prokka v1.14.5, SPAdes v3.13.0]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **2.5**
- Evidence: To compare species-level similarity to strain-sharing rates, beta diversity metrics (Aitchison distance, Bray–Curtis dissimilarity, and Jaccard binary distance) computed with the vegan R package (v2.5–7) were converted to similarity indices (1 − (distance or dissimilarity)).
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Soil microbiomes show consistent and predictable responses to extreme events. (Nature 2024)

- DOI: 10.1038/s41586-024-08185-3 | PMCID: PMC11655354 | PMID: 39604724
- Evidence: For visualization of the relative importance of the effect of treatment, country, site and sampling time on taxonomic and functional gene abundance data, as well as measures of soil functioning, we ran NMDS analysis using the function metaMDS in the vegan package 77 , Bray–Curtis dissimilarity, followed by partial RDA, to visualize the relationships between disturbance treatments and community com...
- Full pipeline: read trimming [Cutadapt v1.2.1] -> quantification [vegan] -> differential/statistical testing [R, ggplot2 v3.3] -> visualisation [vegan] -> stage not stated [BLAST v2.13, DADA2 v1.24, lme4 v3.1, tidyverse]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Version used: **2.6**
- Evidence: Population genetic structure of F. prausnitzii We calculated an SV-based between-sample microbial genetic dissimilarity based on Canberra distance for each microbial species separately using the vegdist() function of the R package vegan (v.2.6-2) to generate species-specific genetic distance matrices ( M SV ).
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Version used: **2.6**
- Evidence: The following R packages were used: Rsamtools (v.2.12.0), vegan (v.2.6-2), factoextra (v.1.0.7), ggplot2 (v.3.3.6), ggExtra (v.0.10.0), ggforce (v.0.3.3), rnaturalearth (v.0.1.0), sf (v.1.0.-8), raster (v.3.5-21), rgdal (v.1.5-32), spatstat (v.2.3-4), maptools (v.1.1-4), gstat (v.2.0-9), sp (v.1.5-0), labdsv (v.2.0-1), rcarbon (v.1.5.1), magrittr (v.2.0.3), dplyr (v.1.0.9), reshape 2 (v.1.4.4), an...
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **2.6**
- Evidence: Assessment of drug treatment on the composition of synthetic communities in vitro To assess changes in microbial diversity after drug treatment, we calculated the species richness and Shannon’s index using the R package vegan (v.2.6-8) 65 .
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### A cryptic role for reciprocal helping in a cooperatively breeding bird. (Nature 2025)

- DOI: 10.1038/s41586-025-08958-4 | PMCID: PMC12158779 | PMID: 40335688
- Evidence: The first test was a Mantel test (vegan R package 75 ) for the Pearson’s correlation between adjusted helping scores given and received within each group (Extended Data Fig.
- Full pipeline: normalisation [R, brms] -> differential/statistical testing [R, brms] -> stage not stated [vegan]

### Global impoverishment of natural vegetation revealed by dark diversity. (Nature 2025)

- DOI: 10.1038/s41586-025-08814-5 | PMCID: PMC12095060 | PMID: 40175550
- Evidence: The contribution of each source of variation was calculated using hierarchical variation partitioning (function varpart in the vegan package 59 in R).
- Full pipeline: quantification [R] -> stage not stated [vegan]

### Fine-scale patterns of SARS-CoV-2 spread from identical pathogen sequences. (Nature 2025)

- DOI: 10.1038/s41586-025-08637-4 | PMCID: PMC11964829 | PMID: 40044856
- Evidence: As the NMDS algorithm requires a measure of similarity between counties, we define the similarity s A , B between counties A and B as: s A , B = e − R R A , B 0 We perform two-dimensional NMDS using the vegan R package 57 .
- Full pipeline: dimensionality reduction/clustering [vegan] -> differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [Nextstrain, R, ape (R), igraph]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **2.6**
- Evidence: Microbial diversity, composition and site differences To measure prokaryotic alpha-diversity, species counts were rarefied to 5,000 using the rrarefy function available through the vegan R package v.2.6-4 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: We used the functions dbrda and varpart of the vegan package and forward.sel of the package packfor 88 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Version used: **2.6**
- Evidence: All data analysis and visualization was done in R (v4.2.1) with the following packages: stats (v.4.1.1), vegan (v.2.6), ggplot2 (v.3.3.6), ComplexUpset (v.2.8.0), tidyr (v.1.2.0), dplyr (v.1.0.9), corrplot (v.0.92), pheatmap (v.1.0.12), RColorBrewer (v.1.1-3), pls (v.2.8), edgeR (v.3.16).
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Gut microbiome strain-sharing within isolated village social networks. (Nature 2025)

- DOI: 10.1038/s41586-024-08222-1 | PMCID: PMC11666459 | PMID: 39567691
- Version used: **2.6**
- Evidence: Beta diversity indices were calculated using the vegdist function from the vegan R package (v.2.6-2) 49 .
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> visualisation [igraph v1.3.5] -> stage not stated [MetaPhlAn, R, vegan v2.6]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **2.6.4**
- Evidence: 68 ) in RStudio (v.4.2) using the following packages: ape (v.5.5), vegan (v.2.6.4), DESeq2 (v.1.32.0), matrixStats (v.0.61.0), cowplot (v.1.1.1), broom (v.0.7.8), dplyr (v.1.0.7), tidyr (v.1.1.3) and tidyverse (v.2.0.0).
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Pesticide residues alter taxonomic and functional biodiversity in soils. (Nature 2026)

- DOI: 10.1038/s41586-025-09991-z | PMCID: PMC12965876 | PMID: 41606316
- Evidence: For this, we adapted the varpart function from the vegan R package 90 , comparing the r 2 values of sub-models (GLMs) where the target variable was explained by one driver type alone, combinations of two, or three drivers, or all drivers together (full model), and thereby isolating unique and shared contributions to explained variance (see all R scripts with names containing ‘Variation partitionin...
- Full pipeline: normalisation [R] -> stage not stated [DADA2, eggNOG, fastp v0.23.4, vegan]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Evidence: To test whether the distribution of distances calculated between pairs of individuals within categories (sex, region and archaeological stages) was significantly different from random permutations of individuals across categories, we used ANOSIM (anosim from the vegan package 108 in R 109 ) and a permutational multivariate analysis of variance (adonis2 from the vegan package 108 in R 109 ) (Fig.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### Protected area management has significant spillover effects on vegetation. (Nature 2026)

- DOI: 10.1038/s41586-025-09837-8 | PMCID: PMC12916312 | PMID: 41372406
- Evidence: Variance partitioning, which offers an approach for comparing matrices of predictor variables to a matrix of response variables, was implemented using the vegan package 78 .
- Full pipeline: stage not stated [QGIS, R, vegan]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Evidence: Pairwise dissimilarities among species were computed using the Jaccard distance in vegan R package.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Evidence: Significance of temperature, genotype, and time-point were tested by PERMANOVA using the adonis function from the vegan package (Package version 2.5–6) ( 61 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Antigenic cartography reveals complexities of genetic determinants that lead to antigenic differences among pandemic GII.4 noroviruses. (PNAS 2021)

- DOI: 10.1073/pnas.2015874118 | PMCID: PMC7980451 | PMID: 33836574
- Evidence: The Pearson correlation coefficient ( r ) between antigenic distance and amino acid differences from GII.4 VLPs was calculated using Mantel method implemented in vegan package in R v3.6.0.
- Full pipeline: stage not stated [R v3.6, vegan]

### Heat stress destabilizes symbiotic nutrient cycling in corals. (PNAS 2021)

- DOI: 10.1073/pnas.2022653118 | PMCID: PMC7865147 | PMID: 33500354
- Version used: **2.5**
- Evidence: Differences in expression profiles were analyzed with permutational multivariate analysis of variance with treatment and colony as explanatory variables as implemented in the vegan R package v.2.5-6 ( 99 ).
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [FastQC v0.11.5, Trimmomatic v0.39] -> alignment/mapping [Salmon v1.0.0] -> quantification [Salmon v1.0.0, lme4] -> differential/statistical testing [R, vegan v2.5] -> stage not stated [ImageJ]

### Impact of cultural and genetic structure on food choices along the Silk Road. (PNAS 2022)

- DOI: 10.1073/pnas.2209311119 | PMCID: PMC9704696 | PMID: 36375050
- Evidence: In detail, we computed the correlations in a symmetric Procrustes rotation by using the “ protest ” function within the vegan R package ( 70 ) on the first two dimensions of each dataset obtained through the different techniques, and we reported the mean value across the six combinations of techniques.
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SciPy, lme4] -> differential/statistical testing [lme4] -> machine learning [ADMIXTURE] -> stage not stated [PLINK v1.9, R, vegan]

### LOCOM: A logistic regression model for testing differential abundance in compositional microbiome data with false discovery rate control. (PNAS 2022)

- DOI: 10.1073/pnas.2122788119 | PMCID: PMC9335309 | PMID: 35867822
- Evidence: For testing the global hypothesis, we compared LOCOM to PERMANOVA (the adonis2 function in the vegan R package) based on the Aitchison distance, which is referred to as PERMANOVA-half and PERMANOVA-one corresponding to adding pseudocount 0.5 and 1, respectively, to all cells.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, vegan]

### Trade and foreign fishing mediate global marine nutrient supply. (PNAS 2022)

- DOI: 10.1073/pnas.2120817119 | PMCID: PMC9295801 | PMID: 35605118
- Evidence: The location diversity for foreign fishing (DivFF) was estimated using the Shannon Weaver index in the vegan package in R ( 57 ) and averaged across the seven nutrients used in the earlier analyses ( SI Appendix , Table S4 ).
- Full pipeline: visualisation [R] -> stage not stated [vegan]

### Dissecting the difference in tree species richness between Africa and South America. (PNAS 2022)

- DOI: 10.1073/pnas.2112336119 | PMCID: PMC9168492 | PMID: 35349336
- Evidence: We performed the NMDS analyses by applying the metaMDS function from the vegan package in the R software.
- Full pipeline: dimensionality reduction/clustering [R] -> stage not stated [vegan]

### Distinguishing the molecular diversity, nutrient content, and energetic potential of exometabolomes produced by macroalgae and reef-building corals. (PNAS 2022)

- DOI: 10.1073/pnas.2110283119 | PMCID: PMC8812564 | PMID: 35101918
- Evidence: Results of permutational ANOVA via the adonis function in the vegan package in R are presented at top.
- Full pipeline: differential/statistical testing [vegan] -> visualisation [Cytoscape v3.7]

### Vertical stratification of the air microbiome in the lower troposphere. (PNAS 2022)

- DOI: 10.1073/pnas.2117293119 | PMCID: PMC8851546 | PMID: 35131944
- Evidence: To visualize multivariate patterns in microbial communities, Bray–Curtis dissimilarity distances among centroids for each sample series were calculated in the vegan package ( 37 ) in R v.4.0.2.
- Full pipeline: quality control [Bowtie2 v2.4.1] -> read trimming [Bowtie2 v2.4.1, Cutadapt v1.8.1] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> visualisation [vegan]

### Kelp-forest dynamics controlled by substrate complexity. (PNAS 2022)

- DOI: 10.1073/pnas.2103483119 | PMCID: PMC8872774 | PMID: 35181602
- Version used: **2.5**
- Evidence: Nonmetric multidimensional scaling was performed on this dissimilarity matrix using the vegan package (v.2.5-4) ( 68 ) in R v.3.5.3 ( 69 ) and exhibited a stress of 0.18.
- Full pipeline: normalisation [vegan v2.5] -> dimensionality reduction/clustering [vegan v2.5] -> visualisation [ggplot2] -> stage not stated [R]

### Urbanization and edge effects interact to drive mutualism breakdown and the rise of unstable pathogenic communities in forest soil. (PNAS 2023)

- DOI: 10.1073/pnas.2307519120 | PMCID: PMC10483667 | PMID: 37643216
- Evidence: Shannon’s alpha diversity for the whole fungal and bacterial community was calculated by the vegan package ( 70 ) in R.
- Full pipeline: quality control [R] -> stage not stated [igraph, lme4, vegan]

### Intersubject similarity in neural representations underlies shared episodic memory content. (PNAS 2023)

- DOI: 10.1073/pnas.2308951120 | PMCID: PMC10466090 | PMID: 37603733
- Evidence: We used the Mantel test ( 63 ) implemented in the vegan package ( 56 ) ( https://CRAN.R-project.org/package=vegan ) to examine the relationship between cross-participant neural similarity and their SMC.
- Full pipeline: alignment/mapping [BrainNet Viewer] -> normalisation [ANTs, fMRIPrep v1.4.1] -> registration [fMRIPrep v1.4.1] -> stage not stated [vegan]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Evidence: Statistical analyses were conducted on a total of 166 libraries using the R programming environment using the vegan package ( 35 ).
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Decomposition decreases molecular diversity and ecosystem similarity of soil organic matter. (PNAS 2023)

- DOI: 10.1073/pnas.2303335120 | PMCID: PMC10288640 | PMID: 37307452
- Evidence: Vectors of environmental variables were determined using the vegan package in Rstudio.
- Full pipeline: differential/statistical testing [R, emmeans] -> stage not stated [vegan]

### Species invasions shift microbial phenology in a two-decade freshwater time series. (PNAS 2023)

- DOI: 10.1073/pnas.2211796120 | PMCID: PMC10089161 | PMID: 36881623
- Evidence: We performed NMDS and confirmed the significance of our season choices by calculating the ANOSIM significance using the vegan R package ( 12 ).
- Full pipeline: stage not stated [R, vegan]

### Recovery of a marine keystone predator transforms terrestrial predator-prey dynamics. (PNAS 2023)

- DOI: 10.1073/pnas.2209037120 | PMCID: PMC9945949 | PMID: 36689656
- Version used: **2.6**
- Evidence: We performed PERMANOVA analyses using the adonis2 function in the vegan (v.
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [vegan v2.6]

### Soil viral-host interactions regulate microplastic-dependent carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2413245121 | PMCID: PMC11551317 | PMID: 39467127
- Evidence: The alpha diversity indexes of the microbes in each sample were determined using the “diversity” function in vegan package in R (v4.0.3).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BLAST, Bowtie2, HMMER] -> quantification [Bowtie2] -> stage not stated [DESeq2, R v4.0.3, vegan]

### Manipulating a host-native microbial strain compensates for low microbial diversity by increasing weight gain in a wild bird population. (PNAS 2024)

- DOI: 10.1073/pnas.2402352121 | PMCID: PMC11513901 | PMID: 39401350
- Evidence: Sample completeness curves were plotted using the rarecurve function from the vegan package ( 83 ).
- Full pipeline: visualisation [vegan] -> stage not stated [Bioconductor, DADA2, R, lme4, phyloseq]

### Parallel ecological and evolutionary responses to selection in a natural bacterial community. (PNAS 2024)

- DOI: 10.1073/pnas.2403577121 | PMCID: PMC11388356 | PMID: 39190353
- Evidence: We confirmed homogeneity of variance using the “ betadisper ” function in the vegan package to estimate group differences in dispersion and treated all copper × SBW25 combinations as levels of a single factor in a 1-way AVOVA on dispersion.
- Full pipeline: quantification [DESeq2, R] -> stage not stated [emmeans, ggplot2, lme4, vegan]

### Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2303439121 | PMCID: PMC11317588 | PMID: 39093948
- Evidence: Hierarchical clustering analysis was performed using the vegan package ( 53 ) to identify associations between differentially abundant ASVs and metabolites with significant Spearman correlations (r > ± 0.7, P < 0.05).
- Full pipeline: quantification [ImageJ v2.0.0] -> dimensionality reduction/clustering [vegan] -> differential/statistical testing [DESeq2, R v3.6.0, phyloseq, vegan] -> visualisation [Cytoscape, R v3.6.0, igraph, phyloseq] -> stage not stated [DADA2]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: For the RDA analysis, we used the vegan R package ( 32 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Evidence: The vegan package in R ( 49 ) was used to calculate Simpson’s alpha diversity index and perform MDS.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### Historical redlining is associated with disparities in wildlife biodiversity in four California cities. (PNAS 2024)

- DOI: 10.1073/pnas.2321441121 | PMCID: PMC11194601 | PMID: 38861597
- Evidence: We calculated beta diversity by using a presence–absence (Jaccard’s) metric in the adonis function via the vegan package ( 97 ), which generates values between 0, representing complete dissimilar species assemblages, and 1, representing completely similar assemblages.
- Full pipeline: differential/statistical testing [R, ggplot2] -> stage not stated [vegan]

### Climate change is poised to alter mountain stream ecosystem processes via organismal phenological shifts. (PNAS 2024)

- DOI: 10.1073/pnas.2310513121 | PMCID: PMC10998557 | PMID: 38498724
- Evidence: For our second prediction regarding stream invertebrate phenology and production, we first used permutational multivariate ANOVA (PERMANOVA) tests based on 999 permutations with the function adonis2 in the vegan R package in order to quantify benthic and emergent community change over time and across treatments ( 78 ).
- Full pipeline: quantification [R, vegan] -> differential/statistical testing [R, vegan]

### Deforestation impacts soil biodiversity and ecosystem services worldwide. (PNAS 2024)

- DOI: 10.1073/pnas.2318475121 | PMCID: PMC10990143 | PMID: 38466879
- Evidence: The Euclidean distances within the native forest (procedure control; D c ) and deforested (converted ecosystem) treatment (D t ) of each paired site were calculated using the R vegan package ( SI Appendix , Fig.
- Full pipeline: differential/statistical testing [R v4.1.2, metafor] -> stage not stated [vegan]

### Positive associations fuel soil biodiversity and ecological networks worldwide. (PNAS 2024)

- DOI: 10.1073/pnas.2308769121 | PMCID: PMC10861899 | PMID: 38285947
- Evidence: Nestedness was determined using the nestednodf function in the vegan package.
- Full pipeline: dimensionality reduction/clustering [igraph] -> stage not stated [QIIME 2, vegan]

### Specialized proresolving mediator resolvin E1 corrects the altered cystic fibrosis nasal epithelium cilia beating dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2313089121 | PMCID: PMC10835060 | PMID: 38252817
- Evidence: The centroids of the PCA “clusters” and data dispersion were compared using the PERMANOVA test ( 82 ) and PERMDISP test ( 83 ), respectively, from the vegan package on R.
- Full pipeline: dimensionality reduction/clustering [vegan] -> stage not stated [ggplot2]

### Wild food portfolios: Access to diverse foods stabilizes harvest in wild food systems. (PNAS 2025)

- DOI: 10.1073/pnas.2525571122 | PMCID: PMC12772149 | PMID: 41452987
- Evidence: We calculated harvest diversity as Shannon-Weiner diversity index using the vegan package ( 75 ) in R, where per capita harvest biomass was used as an indicator of relative abundance.
- Full pipeline: quantification [vegan] -> stage not stated [R, igraph]

### Localized nutrient colimitation of phytoplankton growth rates across the subtropical South Pacific Ocean. (PNAS 2025)

- DOI: 10.1073/pnas.2526930122 | PMCID: PMC12718367 | PMID: 41370344
- Evidence: Vector fitting was applied to assess the relationship between environmental variables and the ordination space using the envfit function from the vegan package.
- Full pipeline: differential/statistical testing [R v4.3.2, ggplot2] -> visualisation [R v4.3.2, ggplot2] -> stage not stated [vegan]

### Precipitation increase promotes soil organic carbon formation and stability via the mycorrhizal fungal pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2519072122 | PMCID: PMC12685053 | PMID: 41289393
- Evidence: The first axis of the PCoA was used to represent bacterial community composition, utilizing the “pcoa” function in the vegan package.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, metafor, pheatmap, vegan]

### A quantitative risk assessment framework for mortality due to macroplastic ingestion in seabirds, marine mammals, and sea turtles. (PNAS 2025)

- DOI: 10.1073/pnas.2415492122 | PMCID: PMC12684891 | PMID: 41248313
- Evidence: These were both done using the vegan package in R Version 4.4.1, with a Bray–Curtis dissimilarity used as the distance measure for the NMDS.
- Full pipeline: stage not stated [vegan]

### Discarded cigarette butts as overlooked reservoirs and amplifiers of antibiotic resistance genes and pathogens in urban green spaces. (PNAS 2025)

- DOI: 10.1073/pnas.2525377122 | PMCID: PMC12595418 | PMID: 41144667
- Evidence: Community variation was visualized by Principal Coordinate Analysis based on Bray–Curtis dissimilarity, and compositional differences among sample types were evaluated using permutational multivariate ANOVA with 999 permutations (adonis function, vegan package).
- Full pipeline: differential/statistical testing [R v4.3.3, vegan] -> visualisation [ggplot2 v4.6, vegan] -> stage not stated [DADA2, scikit-learn]

### Combined pesticide pollution enhances the dissemination of the phage-encoded antibiotic resistome in the soil under nitrogen deposition. (PNAS 2025)

- DOI: 10.1073/pnas.2516722122 | PMCID: PMC12519213 | PMID: 41042849
- Evidence: The alpha diversity index of the virome was calculated using the “diversity” function in the vegan package in R (v4.0.3).
- Full pipeline: read trimming [fastp v0.22.08] -> alignment/mapping [BLAST] -> visualisation [Cytoscape v3.10.0] -> stage not stated [HMMER v3.1b, R v4.0.3, eggNOG, vegan]

### Soil eDNA reflects regionally dominant species rather than local composition of tropical tree communities. (PNAS 2025)

- DOI: 10.1073/pnas.2505772122 | PMCID: PMC12403143 | PMID: 40828011
- Evidence: ( E ) Pearson correlation (with 95% CI) between stem OTU and DNA OTU richness across spatial scales using data rarefied based on the number of reads for eDNA and number of individual trees for census data using the ‘rarefy’ function in the vegan R package ( 25 ).
- Full pipeline: read trimming [BLAST, DADA2] -> alignment/mapping [BLAST, DADA2] -> stage not stated [R, vegan]

### Increased microbial carbon use efficiency upon abrupt permafrost thaw. (PNAS 2025)

- DOI: 10.1073/pnas.2419206122 | PMCID: PMC12377653 | PMID: 40794832
- Evidence: The examined biotic factors included microbial biomass, F/B, enzyme activities, alpha diversity calculated by the vegan package ( 72 ), and dominant bacterial and fungal taxa.
- Full pipeline: stage not stated [vegan]

### Whole-genome duplication increases genetic diversity and load in outcrossing <i>Arabidopsis arenosa</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2501739122 | PMCID: PMC12337351 | PMID: 40737318
- Version used: **2.6**
- Evidence: To assess whether the deleterious distribution of fitness effects (DFE) differed between diploid and tetraploid populations, we performed a PERMANOVA (Permutational Multivariate ANOVA) using the adonis function from the vegan R package ver.
- Full pipeline: alignment/mapping [minimap2 v2.22] -> variant calling [GATK v3.7, R] -> differential/statistical testing [vegan v2.6] -> stage not stated [SnpEff v5.1]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Evidence: The data were plotted in R ( 120 ) using the vegan package ( https://doi.org/10.32614/CRAN.package.vegan ) for nonmetric multidimensional scaling with “monoMDS,” specifying a global model, square root transformation, and Wisconsin double standardization (autotransform=TRUE).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Suturing fragmented landscapes: Mosaic hybrid zones in plants may facilitate ecosystem resiliency. (PNAS 2025)

- DOI: 10.1073/pnas.2410941122 | PMCID: PMC12337288 | PMID: 40720662
- Evidence: Variance partitioning and RDA were performed using the functions varpart() and rda() in the vegan package.
- Full pipeline: machine learning [R] -> stage not stated [VCFtools v0.1.16, vegan]

### Human land use promotes range expansion of soil protists from temperate to subtropical regions in China. (PNAS 2025)

- DOI: 10.1073/pnas.2413220122 | PMCID: PMC12318147 | PMID: 40694336
- Evidence: The distance to the community centroid in different human land-use systems was calculated using the function betadisper in the vegan package ( 56 ).
- Full pipeline: differential/statistical testing [R v3.6.2, emmeans, lme4] -> stage not stated [QIIME 2 v1.90, vegan]

### Optimistic people are all alike: Shared neural representations supporting episodic future thinking among optimistic individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2511101122 | PMCID: PMC12318172 | PMID: 40690674
- Evidence: Finally, we used the Mantel test ( 50 ) implemented by the vegan package ( 51 ) to examine the relationship between each ROI’s neural dissimilarity matrix and model dissimilarity matrices.
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [R, vegan]

### Elevated CO<sub>2</sub> alters relative belowground carbon investment for nutrient acquisition in a mature temperate forest. (PNAS 2025)

- DOI: 10.1073/pnas.2503595122 | PMCID: PMC12304975 | PMID: 40663611
- Evidence: Differences were visualized by PCA using the vegan package ( 59 ).
- Full pipeline: dimensionality reduction/clustering [vegan] -> differential/statistical testing [R v4.4, afex] -> visualisation [R v4.4, vegan]

### Independent transitions to fully planktonic life cycles shaped the global distribution of medusozoans in the epipelagic zone. (PNAS 2025)

- DOI: 10.1073/pnas.2415979122 | PMCID: PMC12146771 | PMID: 40440075
- Evidence: Environmental data were centered prior to the analysis and then selected by stepwise model selection using permutation with the ordistep function from the vegan package (options: 1,000 steps).
- Full pipeline: alignment/mapping [BLAST, phytools] -> differential/statistical testing [tidyverse, vegan] -> stage not stated [R, igraph]

### Distinguishing species boundaries from geographic variation. (PNAS 2025)

- DOI: 10.1073/pnas.2423688122 | PMCID: PMC12088384 | PMID: 40324080
- Evidence: We log-transformed our geographic distances and performed the Mantel test using the vegan package ( 90 ) with the Pearson correlation method.
- Full pipeline: visualisation [ggplot2] -> stage not stated [ADMIXTURE v1.3.0, R, RAxML, VCFtools v0.1.13, tidyverse, vegan]

### Eukaryotic phytoplankton drive a decrease in primary production in response to elevated CO&lt;sub&gt;2&lt;/sub&gt; in the tropical and subtropical oceans. (PNAS 2025)

- DOI: 10.1073/pnas.2423680122 | PMCID: PMC11929437 | PMID: 40063804
- Evidence: The PERMANOVA test was conducted using the adonis2 in vegan package ( 81 ) and RVAideMemoire package ( 82 ) in R to compare the difference in eukaryotic phytoplankton community under ambient and acidified conditions for each CO 2 enrichment experiment.
- Full pipeline: quality control [DADA2, QIIME 2, R] -> stage not stated [CDO, vegan]

### Specific microbial ratio in the gut microbiome is associated with multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2413953122 | PMCID: PMC11912405 | PMID: 40030030
- Evidence: P -values represent statistical significance using the Wilcoxon test in ( A – E ). adonis2 test from the vegan package in R was used for significance testing in ( F ).
- Full pipeline: differential/statistical testing [ggplot2, vegan] -> visualisation [ggplot2] -> stage not stated [R v4.1]

### Dispersal of influenza virus populations within the respiratory tract shapes their evolutionary potential. (PNAS 2025)

- DOI: 10.1073/pnas.2419985122 | PMCID: PMC11789087 | PMID: 39835898
- Version used: **2.6**
- Evidence: Calculation of Bray–Curtis and Raup–Crick dissimilarity indexes was done using the vegan package version 2.6-4 in R.
- Full pipeline: differential/statistical testing [Python] -> visualisation [ggplot2] -> stage not stated [R v4.1.3, vegan v2.6]

### A defined community of core gut microbiota members promotes cognitive performance in honey bees. (PNAS 2026)

- DOI: 10.1073/pnas.2608600123 | PMCID: PMC13214017 | PMID: 42160337
- Evidence: To assess differences in gut metabolic profiles across treatment groups, metabolite concentration data were standardized using z-score scaling and a permutational multivariate ANOVA [PERMANOVA; “adonis2” function from the vegan package ( 52 )] using Euclidean distance and 999 permutations was performed.
- Full pipeline: normalisation [vegan] -> differential/statistical testing [vegan] -> stage not stated [lme4]

### Interspecies interaction controls &lt;i&gt;Escherichia coli&lt;/i&gt; growth in human gut microbiome samples. (PNAS 2026)

- DOI: 10.1073/pnas.2527793123 | PMCID: PMC13123830 | PMID: 42018414
- Version used: **2.7**
- Evidence: We assessed beta diversity using the ASV abundance matrix and performed ordination via nonmetric multidimensional scaling (NMDS) with metaMDS from the vegan package (v.
- Full pipeline: quantification [vegan v2.7] -> normalisation [vegan v2.7] -> dimensionality reduction/clustering [vegan v2.7] -> visualisation [phyloseq v1.46] -> stage not stated [DADA2 v3.18, Matplotlib, Python, SciPy, emmeans]

