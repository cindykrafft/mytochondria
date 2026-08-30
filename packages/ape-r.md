# ape (R)

- **Category:** phylogenetics
- **Papers in survey:** 19
- **Journals:** Nature (13), PNAS (6)
- **Years:** 2021 (1), 2022 (3), 2023 (2), 2024 (5), 2025 (4), 2026 (4)
- **Versions named:** 5.8 (3), 5.6 (3), 5.5 (1), 5.7 (1), 5.7.1 (1), 5.0 (1), 5.3 (1)
- **Pipeline stages it appears in:** visualisation (4), alignment/mapping (2), structure determination (2), differential/statistical testing (1)

## Papers

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Version used: **5.6**
- Evidence: DNA samples that did not have matched RNA-seq samples were then removed from the trees (with drop.tip from ape R package v.5.6-1, ref.
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### The landscape of genomic structural variation in Indigenous Australians. (Nature 2023)

- DOI: 10.1038/s41586-023-06842-7 | PMCID: PMC10733147 | PMID: 38093003
- Evidence: Subsequently, we performed a PCOA on the dissimilarity matrix using the pcoa function from the ape R package.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools] -> visualisation [ggplot2] -> stage not stated [BEDTools, R, RepeatMasker v4.1.2, ape (R), vegan]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Version used: **5.3**
- Evidence: The neighbour-joining trees were constructed using the ape R package v.5.3.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Thresholds for adding degraded tropical forest to the conservation estate. (Nature 2024)

- DOI: 10.1038/s41586-024-07657-w | PMCID: PMC11269177 | PMID: 39020163
- Version used: **5.0**
- Evidence: Methods All data manipulation, data analysis and construction of figures were conducted in the R v.4.02 computing environment 46 , using the packages ape (v.5.0) 47 , betareg (v.3.1-4) 48 , dplyr (v.1.1.4) 49 , lme4 (v.1.1-35.1) 50 , lmtest (v.0.9-40) 51 , lubridate (v.1.9.3) 52 , MASS (v.7.3-60.0.1) 53 , openxlsx (v.4.2.5.2) 54 , paletteer (v.1.6.0) 55 , pastecs (v.1.4.2) 56 , png (v.0.1-8) 57 , ...
- Full pipeline: visualisation [ape (R) v5.0, lme4 v1.1, tidyverse v1.1.4]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **5.6**
- Evidence: Duplication and deletion information was extracted from the CNV calls and then used to reconstruct the neighbour-joining tree with the R package ape (v.5.6-2).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Version used: **5.6**
- Evidence: We then carried out a principal coordinate analysis based on M SV using the pcoa() function of the R package ape (v.5.6-2), with the negative eigenvalues corrected with Cailliez’s method 53 .
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **5.8**
- Evidence: We used the R package ape (v.5.8) 46 to calculate the cophenetic distances between species; the phylogeny was reconstructed using a multilocus alignment obtained from whole bacterial genomes using phylophlan (v.3.0) 47 .
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **5.7.1**
- Evidence: We jackknifed loci one at a time to test for the support of both Pd -1 and Pd -2 clades monophyly using the ‘is.monophyletic’ function in ape (v.5.7.1) 60 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Fine-scale patterns of SARS-CoV-2 spread from identical pathogen sequences. (Nature 2025)

- DOI: 10.1038/s41586-025-08637-4 | PMCID: PMC11964829 | PMID: 40044856
- Evidence: Pairwise genetic distances We compute pairwise genetic distances between Washington state sequences with the ape R package 50 using Hamming distances.
- Full pipeline: dimensionality reduction/clustering [vegan] -> differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [Nextstrain, R, ape (R), igraph]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **5.8**
- Evidence: The R package ape (v.5.8) was used to construct and visualize the lineage trees.
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **5.5**
- Evidence: 68 ) in RStudio (v.4.2) using the following packages: ape (v.5.5), vegan (v.2.6.4), DESeq2 (v.1.32.0), matrixStats (v.0.61.0), cowplot (v.1.1.1), broom (v.0.7.8), dplyr (v.1.0.7), tidyr (v.1.1.3) and tidyverse (v.2.0.0).
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **5.7**
- Evidence: These were visualized by a Principal Coordinate Analysis (PCoA) (package ape (v.5.7-1) 122 in R) and the statistical significance was tested using PERMANOVA.
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Version used: **5.8**
- Evidence: We used these matrices to compute neighbor-joining trees using the ape R package (v5.8) 96 , rooting them at USA_Ancient_Beringian.SG .
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### Estimating maximal microbial growth rates from cultures, metagenomes, and single cells via codon usage patterns. (PNAS 2021)

- DOI: 10.1073/pnas.2016810118 | PMCID: PMC8000110 | PMID: 33723043
- Evidence: S15 B , we sampled 10,000 tips from our tree and calculated all pairwise distances between tips using the cophenetic.phylo() function in the ape R package ( 105 ).
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [RAxML] -> visualisation [ggplot2, ggpubr] -> stage not stated [R, ape (R)]

### Wildlife susceptibility to infectious diseases at global scales. (PNAS 2022)

- DOI: 10.1073/pnas.2122851119 | PMCID: PMC9436312 | PMID: 35994656
- Evidence: In the case of mammals we used Upham tree ( 94 ) and calculated a phylogenetic distance matrix with the ape R package ( 95 ) given in million years among tips of the tree.
- Full pipeline: differential/statistical testing [R] -> stage not stated [ape (R), ggplot2, phytools]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Evidence: We plotted the nuclear and mitochondrial phylogenetic trees face to face with links using the cophyloplot function in the ape R package [v.5.5 ( 89 )].
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### Estimating the reproduction number and transmission heterogeneity from the size distribution of clusters of identical pathogen sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2305299121 | PMCID: PMC11009662 | PMID: 38568971
- Evidence: For each dataset, we computed a pairwise distance matrix between aligned sequences using the ape R package ( 51 ).
- Full pipeline: alignment/mapping [R, ape (R)] -> dimensionality reduction/clustering [igraph] -> stage not stated [Nextstrain]

### Significant shifts in latitudinal optima of North American birds. (PNAS 2024)

- DOI: 10.1073/pnas.2307525121 | PMCID: PMC11009622 | PMID: 38557189
- Evidence: The phylogenetic correlation matrix was calculated assuming a Brownian-motion model of evolution [( 104 ); function vcv ], and with branch lengths computed using the method of Grafen [( 106 ); function compute.brlen ] in the ape R package ( 107 ).
- Full pipeline: stage not stated [R, ape (R), metafor, phytools]

### Quantifying compositional variability in microbial communities with FAVA. (PNAS 2025)

- DOI: 10.1073/pnas.2413211122 | PMCID: PMC11929398 | PMID: 40063791
- Evidence: We performed this computation with the “cophenetic.phylo” function in the ape R package ( 56 ).
- Full pipeline: quantification [QIIME 2] -> stage not stated [R, ape (R)]

