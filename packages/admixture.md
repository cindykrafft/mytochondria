# ADMIXTURE

- **Category:** statgen
- **Papers in survey:** 110
- **Journals:** Nature (53), PNAS (50), Cell (5), Science (2)
- **Years:** 2021 (20), 2022 (12), 2023 (14), 2024 (17), 2025 (36), 2026 (11)
- **Versions named:** 1.3.0 (22), 1.3 (6), 1.2 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (44), differential/statistical testing (9), variant calling (5), machine learning (3), quantification (2), visualisation (2), normalisation (1), quality control (1), structure determination (1), alignment/mapping (1)

## Papers

### The genomic history of the Middle East. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.013 | PMCID: PMC8445022 | PMID: 34352227
- Evidence: The samples were chosen based on a previous ADMIXTURE run ( Bergström et al., 2020 ) and outliers were excluded (i.e., Druze that show relatively high African ancestry, or Africans that show relatively high Eurasian ancestry).
- Full pipeline: stage not stated [ADMIXTURE, BCFtools v1.9, GATK v3.7, RAxML v8.2.10, SAMtools]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Evidence: 5.1 Patterson et al., 2012 https://github.com/DReichLab/AdmixTools ADMIXTURE Alexander et al., 2009 http://dalexander.github.io/admixture/download.html ANGSD v.
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...rc/master/ KING Manichaikul et al., 2010 http://people.virginia.edu/∼wc9c/KING/ PLINK1.9 Purcell et al., 2007 https://www.cog-genomics.org/plink/2.0/ ADMIXTURE Alexander et al., 2009 http://dalexander.github.io/admixture/index.html RFMix Maples et al., 2013 https://sites.google.com/site/rfmixlocalancestryinference/ CircularMapper Peltzer et al., 2016 https://github.com/apeltzer/CircularMapper SAMt...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### Genome-wide data from medieval German Jews show that the Ashkenazi founder event pre-dated the 14<sup>th</sup> century. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.002 | PMCID: PMC9793425 | PMID: 36455558
- Evidence: Higher variability in EAJ relative to MAJ was also observed when projecting a much larger MAJ sample ( Figure S2 ) as well as in an ADMIXTURE analysis ( Alexander et al., 2009 ) ( Data S1 , section 5 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BCFtools, BWA v0.7.15] -> quantification [SAMtools] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [BEAST v2.6.6] -> visualisation [ggplot2] -> stage not stated [ADMIXTURE, R]

### Long shared haplotypes identify the southern Urals as a primary source for the 10th-century Hungarians. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.002 | PMCID: PMC12711333 | PMID: 41106360
- Evidence: ADMIXTURE analysis: Before running ADMIXTURE( 87 ) we pruned our dataset with plink (version 3)( 118 ).
- Full pipeline: dimensionality reduction/clustering [NetworkX] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools, R]

### A chickpea genetic variation map based on the sequencing of 3,366 genomes. (Nature 2021)

- DOI: 10.1038/s41586-021-04066-1 | PMCID: PMC8612933 | PMID: 34759320
- Evidence: The SNP dataset was filtered for missing (>0.1) and MAF (<0.01) and used for a detailed search with ADMIXTURE 65 v.1.3.0 between K = 19 and K = 30 to identify the most likely number of admixture components.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BUSCO, PLINK, RAxML, VCFtools]

### The genomic origins of the Bronze Age Tarim Basin mummies. (Nature 2021)

- DOI: 10.1038/s41586-021-04052-7 | PMCID: PMC8580821 | PMID: 34707286
- Version used: **1.3.0**
- Evidence: The unsupervised admixture analysis was performed with ADMIXTURE v.1.3.0 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools v1.7] -> stage not stated [ADMIXTURE v1.3.0, PLINK v1.90]

### The origins and spread of domestic horses from the Western Eurasian steppes. (Nature 2021)

- DOI: 10.1038/s41586-021-04018-9 | PMCID: PMC8550961 | PMID: 34671162
- Evidence: Struct-f4, thus, achieves similar objectives to other clustering methods, such as ADMIXTURE 77 and Ohana 78 , but does not assume Hardy–Weinberg equilibrium.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [Rcpp] -> structure determination [RAxML] -> stage not stated [ANGSD, R]

### Genomic insights into the formation of human populations in East Asia. (Nature 2021)

- DOI: 10.1038/s41586-021-03336-2 | PMCID: PMC7993749 | PMID: 33618348
- Evidence: We manually curated the data using ADMIXTURE 12 and principal component analysis as implemented in EIGENSOFT 10 to identify individuals that were outliers compared with others from their own populations in cases in which a main cluster was identifiable.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [ANGSD, PLINK]

### A genetic history of the pre-contact Caribbean. (Nature 2021)

- DOI: 10.1038/s41586-020-03053-2 | PMCID: PMC7864882 | PMID: 33361817
- Version used: **1.3.0**
- Evidence: Unsupervised analysis of population structure We used the software ADMIXTURE v1.3.0 74 , 75 to perform unsupervised structure analysis on a dataset comprised of autosomal SNPs that overlap between the 1240k and Illumina dataset and pruned in PLINK1.9 76 using --indep-pairwise 200 25 0.4.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard] -> structure determination [BWA v0.7.15] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.3.1, SAMtools]

### The Anglo-Saxon migration and the formation of the early English gene pool. (Nature 2022)

- DOI: 10.1038/s41586-022-05247-2 | PMCID: PMC9534755 | PMID: 36131019
- Evidence: ADMIXTURE analysis We performed model-based clustering analysis using ADMIXTURE 48 (v1.3).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA, Picard] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, SAMtools]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Evidence: To achieve this, we defined three cohorts based on the most common ancestries identified among the participants, using a combination of (1) uniform manifold approximation and projection (UMAP) dimension reduction of 40 genetic principal components provided by UKB, and (2) ADMIXTURE analysis supervised on five reference populations and self-reported ethnicity information.
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### Indigenous Australian genomes show deep structure and rich novel variation. (Nature 2023)

- DOI: 10.1038/s41586-023-06831-w | PMCID: PMC10733150 | PMID: 38093005
- Version used: **1.3**
- Evidence: Ancestry inference Global ancestry proportions were estimated in the NCIG + PNG dataset using ADMIXTURE (v.1.3) 32 after intersecting with the low-coverage 1000 Genomes dataset and thinning for linkage disequilibrium.
- Full pipeline: variant calling [GATK v3.8] -> normalisation [R v5.1] -> dimensionality reduction/clustering [R v5.1, UMAP v0.2.7.0] -> stage not stated [ADMIXTURE v1.3, BCFtools, BEAST v2.6.0, PLINK, ggplot2]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Evidence: ADMIXTURE clustering analysis: Using PLINK2 61 , we first removed SNPs in high linkage disequilibrium using the command –indep-pairwise 50 5 0.5.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: In this study, we obtain proxies for genetic ancestries using ADMIXTURE 20 (see below).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### A pangenome reference of 36 Chinese populations. (Nature 2023)

- DOI: 10.1038/s41586-023-06173-7 | PMCID: PMC10322713 | PMID: 37316654
- Evidence: We randomly selected 10 unrelated high-quality samples from each CPC population, and inferred the genetic ancestry for each sample using ADMIXTURE assuming 2–12 ancestry components (K).
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> variant calling [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BCFtools, QUAST v5.2.0, pheatmap v1.0.12]

### Northwest African Neolithic initiated by migrants from Iberia and Levant. (Nature 2023)

- DOI: 10.1038/s41586-023-06166-6 | PMCID: PMC10266975 | PMID: 37286608
- Evidence: An unsupervised model-based clustering algorithm, implemented in ADMIXTURE v,1.3.0 (ref.
- Full pipeline: variant calling [GATK v3.5.0] -> registration [GATK v3.5.0] -> dimensionality reduction/clustering [ADMIXTURE, QGIS] -> stage not stated [BCFtools, PLINK v1.9, SAMtools]

### A weakly structured stem for human origins in Africa. (Nature 2023)

- DOI: 10.1038/s41586-023-06055-y | PMCID: PMC10208968 | PMID: 37198480
- Evidence: ADMIXTURE and principal component analyses were done on a subset of variants filtered to remove variants in high linkage disequilibrium ( r 2 threshold of 0.1).
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE]

### Entwined African and Asian genetic roots of medieval peoples of the Swahili coast. (Nature 2023)

- DOI: 10.1038/s41586-023-05754-w | PMCID: PMC10060156 | PMID: 36991187
- Evidence: ADMIXTURE clustering analysis We prepared data for the ADMIXTURE 48 plots in Fig.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, R]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **1.3.0**
- Evidence: The population structure analysis was performed with ADMIXTURE v1.3.0 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### The rise and transformation of Bronze Age pastoralists in the Caucasus. (Nature 2024)

- DOI: 10.1038/s41586-024-08113-5 | PMCID: PMC11602729 | PMID: 39478221
- Evidence: The Human Origins dataset with 597,573 SNPs was used for analysis comparing ancient to modern groups, such as PCA and ADMIXTURE, whereas the 1240k dataset of 1,233,013 SNPs was used for comparison between ancient groups in f -statistics and ancestry modelling.
- Full pipeline: quality control [ANGSD, FastQC] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE]

### Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. (Nature 2024)

- DOI: 10.1038/s41586-024-07881-4 | PMCID: PMC11390480 | PMID: 39261618
- Evidence: Reference data For multidimensional scaling, f -statistics, ADMIXTURE, local ancestry inference and admixture dating, we considered SNP array data from refs.
- Full pipeline: alignment/mapping [GATK, SAMtools] -> normalisation [ADMIXTURE] -> registration [GATK, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [Matplotlib v3.5.3, R, ggplot2 v3.3.2] -> stage not stated [ANGSD v0.930, PLINK v1.9.20200712]

### Sources of gene expression variation in a globally diverse human cohort. (Nature 2024)

- DOI: 10.1038/s41586-024-07708-2 | PMCID: PMC11291278 | PMID: 39020179
- Evidence: Although we emphasize the greater genetic diversity within African populations—a point obscured by ADMIXTURE analysis and principal component analysis (PCA) 16 —these visualizations demonstrate that our study includes data from several non-African ancestry groups that were poorly represented in previous studies (Fig.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ADMIXTURE] -> stage not stated [VEP]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Evidence: Population structure analysis Phylogenetic tree and ADMIXTURE For the Phylogenetic genetic analysis, neighbour-joining tree and maximum likelihood tree were constructed for the genome-wide 4DTv (fourfold degenerate synonymous site) using rapidnj (version 2.3.2) 54 and iqtree (version 1.6.9) 55 , respectively.
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Version used: **1.3.0**
- Evidence: Next, we used unsupervised ADMIXTURE (v.1.3.0) to assess the population structure of modern P. falciparum and P. vivax using a model-based approach 97 .
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Ancient genomes reveal insights into ritual life at Chichén Itzá. (Nature 2024)

- DOI: 10.1038/s41586-024-07509-7 | PMCID: PMC11208145 | PMID: 38867041
- Version used: **1.3.0**
- Evidence: ADMIXTURE analysis We used ADMIXTURE v.1.3.0 (ref.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.7.12] -> stage not stated [ADMIXTURE v1.3.0, SAMtools]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Since all the GWAS summary statistics used in the current work were based on European populations, we used ADMIXTURE tool (v1.3.0) 60 and PCA to infer the unsupervised cluster of individuals with European genetic background within ccRCC cases.
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Evidence: We investigated overall population structure among the dataset individuals using PCA and model-based clustering (ADMIXTURE 94 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### 100 ancient genomes show repeated population turnovers in Neolithic Denmark. (Nature 2024)

- DOI: 10.1038/s41586-023-06862-3 | PMCID: PMC10781617 | PMID: 38200294
- Evidence: Individuals not passing imputation quality control cutoffs mentioned above were included in PCA and ADMIXTURE analyses as pseudo-haploid genotypes.
- Full pipeline: quality control [ADMIXTURE] -> variant calling [ADMIXTURE, BCFtools, PLINK, R, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [PLINK, R]

### Elevated genetic risk for multiple sclerosis emerged in steppe pastoralist populations. (Nature 2024)

- DOI: 10.1038/s41586-023-06618-z | PMCID: PMC10781639 | PMID: 38200296
- Evidence: First, we used model-based clustering (ADMIXTURE) 63 (Supplementary Note 1 and Supplementary Fig.
- Full pipeline: quality control [ANGSD v0.931] -> alignment/mapping [BWA v0.7.17] -> quantification [ANGSD v0.931] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [PLINK, Picard, R, SAMtools v1.10]

### The genetic legacy of the expansion of Bantu-speaking peoples in Africa. (Nature 2024)

- DOI: 10.1038/s41586-023-06770-6 | PMCID: PMC10794141 | PMID: 38030719
- Evidence: In addition, we applied an unsupervised clustering-based approach using ADMIXTURE software v.1.3.0 (ref.
- Full pipeline: quality control [PLINK v1.90b] -> variant calling [PLINK v1.90b, SHAPEIT, UMAP] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [Python, R]

### Ancient DNA from Shimao city records kinship practices in Neolithic China. (Nature 2025)

- DOI: 10.1038/s41586-025-09799-x | PMCID: PMC12711557 | PMID: 41299168
- Evidence: We estimated individual ancestries by model-based maximum likelihood clustering using ADMIXTURE 63 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.5.10] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Version used: **1.3.0**
- Evidence: Genetic ancestry fractions were estimated using ADMIXTURE (v.1.3.0) 48 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### Population-specific polygenic risk scores for people of Han Chinese ancestry. (Nature 2025)

- DOI: 10.1038/s41586-025-09350-y | PMCID: PMC12675292 | PMID: 41094136
- Evidence: The proportion of genetic ancestry was determined by ADMIXTURE 60 , and the projected principal component scores with 1000 Genomes as a reference panel were applied to determine individuals’ ancestry 61 .
- Full pipeline: quantification [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, LDSC] -> differential/statistical testing [LDSC, PLINK, SAIGE] -> stage not stated [ANNOVAR, R]

### A haplotype-based evolutionary history of barley domestication. (Nature 2025)

- DOI: 10.1038/s41586-025-09533-7 | PMCID: PMC12629985 | PMID: 40993384
- Evidence: 24 defined 12 populations using model-based ancestry estimation with ADMIXTURE 43 in a global diversity panel of 19,778 domesticated barley, which had been subjected to GBS 24 .
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [BCFtools v1.15.1, DeepVariant v1.6.0, SnpEff v4.3t, minimap2 v2.24] -> visualisation [R v3.5.1] -> stage not stated [ADMIXTURE, PLINK, SAMtools v1.16.1]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Evidence: We used the FSTruct 116 package to quantify the variability of the Q matrix (which contains the row vectors of ancestry coefficients for each individual) outputted by supervised ADMIXTURE.
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Version used: **1.3.0**
- Evidence: Population differentiation We used ADMIXTURE v.1.3.0 ( https://github.com/NovembreLab/admixture ) to compute admixture for K = 5.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **1.3.0**
- Evidence: ADMIXTURE (version 1.3.0) 78 was run with k ranging from 1 to 9 on a linkage-disequilibrium-pruned SNP matrix with less than 10% missing data.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Whole-genome ancestry of an Old Kingdom Egyptian. (Nature 2025)

- DOI: 10.1038/s41586-025-09195-5 | PMCID: PMC12367555 | PMID: 40604286
- Version used: **1.2**
- Evidence: ADMIXTURE clustering We used a model-based clustering approach from the program ADMIXTURE v.1.2 (ref.
- Full pipeline: quality control [ANGSD v0.933] -> variant calling [BCFtools v1.19] -> dimensionality reduction/clustering [ADMIXTURE v1.2] -> stage not stated [PLINK v1.9]

### Ancient DNA reveals the prehistory of the Uralic and Yeniseian peoples. (Nature 2025)

- DOI: 10.1038/s41586-025-09189-3 | PMCID: PMC12342343 | PMID: 40604287
- Evidence: ADMIXTURE and PCA All relatives and shotgun sequences were excluded from ADMIXTURE analysis.
- Full pipeline: variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [ANGSD v0.923, QGIS v3.40.6, R]

### Sequence diversity lost in early pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-025-09031-w | PMCID: PMC12176622 | PMID: 40399685
- Evidence: Estimation of genetic ancestry Genetic ancestry of parental samples was estimated by running ADMIXTURE 54 v.1.3.0 in supervised mode using 1000 Genomes 55 CEU (Utah Caucasian, European), CHB (Beijing Han, East Asian), ITU (Indian Telugu, South Asian), PEL (Peruvian, Native American) and YRI (Nigerian Yoruba, African) as training populations.
- Full pipeline: alignment/mapping [BWA, Picard, R] -> variant calling [Manta v1.6.0] -> differential/statistical testing [R] -> machine learning [ADMIXTURE] -> stage not stated [PLINK, VEP]

### Picuris Pueblo oral history and genomics reveal continuity in US Southwest. (Nature 2025)

- DOI: 10.1038/s41586-025-08791-9 | PMCID: PMC12137115 | PMID: 40307544
- Evidence: We used ADMIXTURE 63 to investigate ancestry proportions and detect the presence of non-Indigenous American ancestry.
- Full pipeline: quality control [ANGSD v0.931] -> variant calling [BCFtools v1.17] -> stage not stated [ADMIXTURE, BEAST v2.6, Picard v2.25.0, SAMtools v1.3.1]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: ADMIXTURE 82 (version 1.3.0) was employed to analyse the population structure, with K increasing from 2 to 16.
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Punic people were genetically diverse with almost no Levantine ancestors. (Nature 2025)

- DOI: 10.1038/s41586-025-08913-3 | PMCID: PMC12226237 | PMID: 40269169
- Version used: **1.3.0**
- Evidence: Ancestry modeling with ADMIXTURE We ran ADMIXTURE version 1.3.0 55 in unsupervised mode on the 122 individuals from our Phoenician-Punic data set that were sequenced for more than 100,000 SNPs, together with 24 individuals from related populations around the Mediterranean ( Supplementary Table 12 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK, R, SAMtools]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Version used: **1.3.0**
- Evidence: Admixture analysis was conducted with ADMIXTURE (v.1.3.0) 78 for K values from 2 to 10.
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: The tree branches are colour-coded by group, and the external circles denote the geographical distribution of each accession. b , ADMIXTURE clustering of 280 Oryza accessions from K = 2 to K = 7.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Ancient DNA from the Green Sahara reveals ancestral North African lineage. (Nature 2025)

- DOI: 10.1038/s41586-025-08793-7 | PMCID: PMC12043513 | PMID: 40175549
- Evidence: We then ran all the analyses throughout the manuscript (including PCA, f 3 and f 4 statistics, qpAdm, admixture graph, DATES and ADMIXTURE), except for admixfrog and hapROH, which, as individual analyses, use only the higher-coverage data from TKH001.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, MAFFT] -> variant calling [SAMtools v1.3] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> stage not stated [PLINK, tidyverse v1.3.0]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Evidence: Admixture, haplotype masking and fine structure Inuit and European admixture proportions were calculated using the software ADMIXTURE 60 on a subset of variants with MAF > 5%, missingness less than 1% and LD-pruned within 1 Mb removing variants with R 2 > 0.8 using Plink v.1.9.0 (ref.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### A genomic history of the North Pontic Region from the Neolithic to the Bronze Age. (Nature 2025)

- DOI: 10.1038/s41586-024-08372-2 | PMCID: PMC11909631 | PMID: 39910299
- Evidence: We performed a subset of unsupervised ADMIXTURE analysis 71 using a new data processing pipeline focusing on “summary individuals” that prevents the formation of population-specific ancestry components.
- Full pipeline: quality control [ANGSD] -> stage not stated [ADMIXTURE, BCFtools, SAMtools]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Evidence: We then used ADMIXTURE 90 and AdmixturePlotter 91 to calculate the best K for our model (that is, the one with the lowest cross validation error (CVE); K = 5) and the admixture proportions of the components that are maximized in each of the parental populations modelled (Fig.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### The evolutionary history and unique genetic diversity of Indigenous Americans. (Nature 2026)

- DOI: 10.1038/s41586-026-10406-w | PMCID: PMC13149005 | PMID: 42020734
- Evidence: This procedure yielded an linkage-disequilibrium-pruned dataset for downstream analyses that required an independent set of markers (for example, PCA and ADMIXTURE).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK, VEP] -> normalisation [VEP] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK v1.9, R, SnpEff]

### Genomic history of early dogs in Europe. (Nature 2026)

- DOI: 10.1038/s41586-026-10112-7 | PMCID: PMC13017524 | PMID: 41882126
- Version used: **1.3.0**
- Evidence: Ancestry analyses Clustering was performed using ADMIXTURE v.1.3.0 (ref.
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0]

### Dogs were widely distributed across western Eurasia during the Palaeolithic. (Nature 2026)

- DOI: 10.1038/s41586-026-10170-x | PMCID: PMC13017512 | PMID: 41882128
- Version used: **1.3.0**
- Evidence: We performed model-based estimation of population structure using the algorithm implemented in ADMIXTURE v.1.3.0 (ref.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.505] -> differential/statistical testing [BEAST v2.6.7] -> stage not stated [ADMIXTURE v1.3.0]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **1.3.0**
- Evidence: Population genetics We applied ADMIXTURE (v.1.3.0) 99 using default settings to n = 1,984 unique genotypes of non-duplicated sequencing libraries.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Evidence: Ancestry estimation was performed using PLINK v.1.9, and ADMIXTURE 48 v.1.3.0 for unsupervised analysis together with the superpopulations of the 1000 Genomes dataset 49 .
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Version used: **1.3.0**
- Evidence: ADMIXTURE Unsupervised ADMIXTURE (v.1.3.0; ref.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### Homo sapiens-specific evolution unveiled by ancient southern African genomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09811-4 | PMCID: PMC12872451 | PMID: 41339558
- Version used: **1.3.0**
- Evidence: The program ADMIXTURE (v.1.3.0) 76 was used for unsupervised estimation of ancestry components.
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK v1.9, SAMtools, SnpEff]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Evidence: ADMIXTURE clustering analysis We used the ADMIXTURE 105 , 106 (v1.23) software package to perform an unsupervised assessment of genetic structure among the newly-reported individuals, including ancient ( Extended Data Tables 0.2 . and 0.3) and modern 2 Native Americans for reference.
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### Systems biology analysis of human genomes points to key pathways conferring spina bifida risk. (PNAS 2021)

- DOI: 10.1073/pnas.2106844118 | PMCID: PMC8713748 | PMID: 34916285
- Evidence: Next, we calculated the ancestry of each individual in relation to nine gene pools representing distinct geographic regions around the world (e.g., South Africa) ( 75 ) using supervised ADMIXTURE ( 77 ).
- Full pipeline: stage not stated [ADMIXTURE, BEDTools, GATK, R, VEP, WGCNA, scikit-learn]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: Then, ADMIXTURE ( 41 ) was used to estimate the genetic ancestry of 126 samples (the single individual species F. daltoniana and F. iinumae were discarded for this analysis), specifying a range of K = 2 to 14 hypothetical ancestral populations.
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Genome evolution of the psammophyte <i>Pugionium</i> for desert adaptation and further speciation. (PNAS 2021)

- DOI: 10.1073/pnas.2025711118 | PMCID: PMC8545485 | PMID: 34649989
- Evidence: ADMIXTURE and Eigensoft were used for population structure analysis.
- Full pipeline: stage not stated [ADMIXTURE, AUGUSTUS, BUSCO, GATK, RepeatMasker]

### Ancestral polymorphisms shape the adaptive radiation of <i>Metrosideros</i> across the Hawaiian Islands. (PNAS 2021)

- DOI: 10.1073/pnas.2023801118 | PMCID: PMC8449318 | PMID: 34497122
- Evidence: ( D ) Ancestry proportion estimates using the ADMIXTURE algorithm for K = 3, 7, and 14.
- Full pipeline: stage not stated [ADMIXTURE, BUSCO]

### Assisted gene flow using cryopreserved sperm in critically endangered coral. (PNAS 2021)

- DOI: 10.1073/pnas.2110559118 | PMCID: PMC8463791 | PMID: 34493583
- Version used: **1.3**
- Evidence: First, ADMIXTURE version 1.3 ( 47 ) was run with the full set of 19,696 probes designed for resolution of population genomic structure as previously described ( 35 ).
- Full pipeline: stage not stated [ADMIXTURE v1.3, R]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: The ADMIXTURE algorithm models individuals as the products of variable levels of admixture between a collection of K genetic source groups.
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### The genomes of ancient date palms germinated from 2,000 y old seeds. (PNAS 2021)

- DOI: 10.1073/pnas.2025337118 | PMCID: PMC8126781 | PMID: 33941705
- Evidence: We estimated individual ancestries on 1) all accessions and 2) date palms and P. theophrasti only using ADMIXTURE ( 44 ) v.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> variant calling [GATK v3.5] -> stage not stated [ADMIXTURE, Picard, R]

### Genomic stability through time despite decades of exploitation in cod on both sides of the Atlantic. (PNAS 2021)

- DOI: 10.1073/pnas.2025453118 | PMCID: PMC8054022 | PMID: 33827928
- Evidence: ( D ) Model-based ADMIXTURE ancestry components for historical (1907, 1940) and modern (2013, 2014) populations ( k = 2; NGSadmix).
- Full pipeline: alignment/mapping [ANGSD v0.931] -> stage not stated [ADMIXTURE]

### An introgressed gene causes meiotic drive in <i>Neurospora sitophila</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2026605118 | PMCID: PMC8092558 | PMID: 33875604
- Evidence: We searched for a genome-wide signal of introgression using a sliding window phylogenetic approach with Twisst ( 52 ), and evaluated introgression and between-clade gene flow with ADMIXTURE ( 53 ).
- Full pipeline: alignment/mapping [Cufflinks] -> differential/statistical testing [RAxML] -> stage not stated [ADMIXTURE, BLAST, IQ-TREE]

### Multiple migrations to the Philippines during the last 50,000 years. (PNAS 2021)

- DOI: 10.1073/pnas.2026132118 | PMCID: PMC8020671 | PMID: 33753512
- Version used: **1.3**
- Evidence: ADMIXTURE v1.3 ( 44 ) and CLUMPP ( 45 ) were used to analyze population structure, which was subsequently visualized using Pong v1.4.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [PLINK v1.9] -> visualisation [ADMIXTURE v1.3]

### Ancient DNA from Guam and the peopling of the Pacific. (PNAS 2021)

- DOI: 10.1073/pnas.2022112118 | PMCID: PMC7817125 | PMID: 33443177
- Evidence: This dataset was used only for PCA and ADMIXTURE analyses.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, R, data.table, pheatmap, tidyverse]

### The evolution of skin pigmentation-associated variation in West Eurasia. (PNAS 2021)

- DOI: 10.1073/pnas.2009227118 | PMCID: PMC7817156 | PMID: 33443182
- Evidence: ADMIXTURE Analysis on Capture-Shotgun Data.
- Full pipeline: stage not stated [ADMIXTURE, PLINK v1.90b]

### Impact of cultural and genetic structure on food choices along the Silk Road. (PNAS 2022)

- DOI: 10.1073/pnas.2209311119 | PMCID: PMC9704696 | PMID: 36375050
- Evidence: Finally, we pruned the variants for linkage disequilibrium (–indep-pairwise 200 50 0.4), and we evaluated the patterns of shared ancestries among populations with the ADMIXTURE software via a cross-validation approach to infer the best number of ancestral components.
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SciPy, lme4] -> differential/statistical testing [lme4] -> machine learning [ADMIXTURE] -> stage not stated [PLINK v1.9, R, vegan]

### The diverse genetic origins of a Classical period Greek army. (PNAS 2022)

- DOI: 10.1073/pnas.2205272119 | PMCID: PMC9564095 | PMID: 36191217
- Evidence: We performed clustering using unsupervised ADMIXTURE ( 50 ) for k = 2 to k = 15.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.6.1] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Evidence: After pruning the SNPs based on linkage disequilibrium using PLINK, we performed genetic structure clustering of autosomal SNPs using ADMIXTURE ( 98 ) and PCA with smartpca in EIGENSOFT v5.0.2 ( 99 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Revealing the recent demographic history of Europe via haplotype sharing in the UK Biobank. (PNAS 2022)

- DOI: 10.1073/pnas.2119281119 | PMCID: PMC9233301 | PMID: 35696575
- Evidence: To explore the sampled population structure of Europe from 5,500 individuals from the UKBB, we initially performed PCA using PLINK ( 28 , 29 ) and estimated ancestry components using the model-based maximum likelihood method of ADMIXTURE ( 57 ).
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [ADMIXTURE, PLINK, R] -> differential/statistical testing [R, ggplot2, igraph]

### Insights into bear evolution from a Pleistocene polar bear genome. (PNAS 2022)

- DOI: 10.1073/pnas.2200016119 | PMCID: PMC9214488 | PMID: 35666863
- Evidence: ADMIXTURE analysis suggests 2% shared ancestry between the ancient polar bear and brown bears.
- Full pipeline: stage not stated [ADMIXTURE, RAxML]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Version used: **1.3**
- Evidence: This dataset was then used to run ADMIXTURE (v1.3) with a K = 4 based on population history and previously reported admixture analyses ( 48 ).
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### Genomic insights into zokors' phylogeny and speciation in China. (PNAS 2022)

- DOI: 10.1073/pnas.2121819119 | PMCID: PMC9171634 | PMID: 35512099
- Evidence: Population genomic analyses including phylogenetic tree, PCA, and STRUCTURE construction were conducted by Phylip, GCTA, and ADMIXTURE, respectively.
- Full pipeline: alignment/mapping [GATK] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BUSCO, RAxML, VCFtools]

### A generalist-specialist trade-off between switchgrass cytotypes impacts climate adaptation and geographic range. (PNAS 2022)

- DOI: 10.1073/pnas.2118879119 | PMCID: PMC9169841 | PMID: 35377798
- Evidence: We also generated diploid genotypes (three potential genotypes) for all samples to use with ADMIXTURE, which does not accept dosage genotypes.
- Full pipeline: alignment/mapping [BWA] -> variant calling [ADMIXTURE, PLINK v1.9, SAMtools, VCFtools] -> registration [GATK v3.0, Picard] -> stage not stated [R]

### Ancient DNA at the edge of the world: Continental immigration and the persistence of Neolithic male lineages in Bronze Age Orkney. (PNAS 2022)

- DOI: 10.1073/pnas.2108001119 | PMCID: PMC8872714 | PMID: 35131896
- Version used: **1.3**
- Evidence: We investigated population relationships between newly reported samples and other ancient and modern individuals using smartPCA and ADMIXTURE (version 1.3) ( 62 ), with D and f statistics calculated using ADMIXTOOLS ( 63 ) to formally confirm relationships, and quantified admixture using qpAdm ( 34 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK v3.8] -> quantification [ADMIXTURE v1.3] -> registration [GATK v3.8] -> differential/statistical testing [ADMIXTURE v1.3]

### Scattered differentiation of unlinked loci across the genome underlines ecological divergence of the selfing grass &lt;i&gt;Brachypodium stacei&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2304848120 | PMCID: PMC10636366 | PMID: 37903254
- Version used: **1.3.0**
- Evidence: Population structure was analyzed using ADMIXTURE (v1.3.0).
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BUSCO, HISAT2, IQ-TREE v1.6.12]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Evidence: Population genetic structure was assessed with sNMF, which is more statistically robust to departures from population genetic model assumptions and computationally efficient than likelihood-based approaches such as STRUCTURE and ADMIXTURE ( 88 ), to estimate the number of discrete genetic clusters (K) ( 89 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Standing genetic variation fuels rapid evolution of herbicide resistance in blackgrass. (PNAS 2023)

- DOI: 10.1073/pnas.2206808120 | PMCID: PMC10120058 | PMID: 37043536
- Evidence: The identification of ancestry groups was performed with ADMIXTURE ( 73 ) ( Fig.
- Full pipeline: read trimming [BUSCO] -> alignment/mapping [MAFFT v7.407] -> variant calling [MAFFT v7.407] -> visualisation [MAFFT v7.407] -> stage not stated [ADMIXTURE, ANGSD v0.930, GATK v4.1.3.0, InterProScan]

### Community-engaged ancient DNA project reveals diverse origins of 18th-century African descendants in Charleston, South Carolina. (PNAS 2023)

- DOI: 10.1073/pnas.2201620120 | PMCID: PMC9934026 | PMID: 36623185
- Evidence: Principal Component and ADMIXTURE Analyses.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.9] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9]

### Natural selection of immune and metabolic genes associated with health in two lowland Bolivian populations. (PNAS 2023)

- DOI: 10.1073/pnas.2207544120 | PMCID: PMC9910614 | PMID: 36574663
- Evidence: First, we used the program ADMIXTURE ( 51 ) to estimate the proportion of the genome originating from K populations for each individual, with K being specified a priori.
- Full pipeline: alignment/mapping [R] -> variant calling [GEMMA] -> normalisation [limma] -> stage not stated [ADMIXTURE, GCTA, VCFtools]

### The genetic origins and impacts of historical Papuan migrations into Wallacea. (PNAS 2024)

- DOI: 10.1073/pnas.2412355121 | PMCID: PMC11670103 | PMID: 39689173
- Evidence: Principal component and ADMIXTURE analyses were performed on the global dataset of 844 modern genomes using a subset of 238,615 unlinked SNPs, with variant pruning performed following Laziridis et al.
- Full pipeline: read trimming [BWA v0.7.17, fastp] -> alignment/mapping [BWA v0.7.17, GATK, SAMtools v1.9] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE, R] -> stage not stated [PLINK v1.987]

### Unraveling the genomic diversity and admixture history of captive tigers in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2402924121 | PMCID: PMC11441546 | PMID: 39298482
- Evidence: Using both imputed and unimputed individuals, we investigated population structure and ancestry of the Generic tigers using a combination of principal component analysis (PCA) and supervised ADMIXTURE (see SI Appendix, Supplementary Notes for ancestry confirmation of single-subspecies individuals).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.4.1] -> variant calling [BWA v0.7.17, GATK v4.1.4.1] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.6, VCFtools, VEP]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Version used: **1.3.0**
- Evidence: Population structure was analyzed by the model-based clustering method ADMIXTURE (v1.3.0) ( 70 ), with cluster numbers (K) ranging from 2 to 10.
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### The role of emerging elites in the formation and development of communities after the fall of the Roman Empire. (PNAS 2024)

- DOI: 10.1073/pnas.2317868121 | PMCID: PMC11388374 | PMID: 39159385
- Evidence: We note that the unsupervised ADMIXTURE analysis on the penecontemporaneous reference samples showed similar regional and subregional power to discriminate populations as the 1000G data ( 25 ), despite the lower sequence quality of the former (refer to Supplementary Section S4 and SI Appendix , Fig.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [SAMtools] -> variant calling [VCFtools] -> normalisation [VCFtools] -> stage not stated [ADMIXTURE, Picard]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: We performed a supervised ADMIXTURE analysis to infer the ancestry of each backcross sample attributable to the three seed zones and C. mollissima ( 43 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Solving the 250-year-old mystery of the origin and global spread of the German cockroach, <i>Blattella germanica</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2401185121 | PMCID: PMC11145273 | PMID: 38768340
- Evidence: ( C ) Bar plot ( Top ), split into region-specific bar plots mapped to sampling sites, derived from maximum likelihood estimation of ancestry (ADMIXTURE) at the optimal number of ancestral clusters (K = 6).
- Full pipeline: alignment/mapping [ADMIXTURE] -> dimensionality reduction/clustering [ADMIXTURE]

### A 120-y time series of genomes reveals the consequences of closed breeding in German Shepherd Dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421755122 | PMCID: PMC12684887 | PMID: 41284896
- Version used: **1.3.0**
- Evidence: S10 ; ( 65 ); ADMIXTURE v.1.3.0 SI Appendix , Fig.
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.5.3, SAMtools v1.9] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.1.4, PLINK v1.90b]

### Gray wolves in an anthropogenic context on a small island in prehistoric Scandinavia. (PNAS 2025)

- DOI: 10.1073/pnas.2421759122 | PMCID: PMC12684923 | PMID: 41284891
- Evidence: The model-based clustering method ADMIXTURE ( 17 ) estimates that both individuals entirely carried wolf-like ancestry ( Fig.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE]

### The impacts of European arrival on Australian dingoes. (PNAS 2025)

- DOI: 10.1073/pnas.2421749122 | PMCID: PMC12684890 | PMID: 41284893
- Version used: **1.3.0**
- Evidence: To test for gene flow between European dog breeds (X) and dingoes (Y), we used both ADMIXTURE v.1.3.0 ( 78 ), and D-statistics of the form: D(Coyote, X; Y, NullarborPlain13_372) and D(Coyote, NullarborPlain13_372; X, Australian breed), with ancestry proportions calculated using F4-ratio estimation ( 79 ).
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [SAMtools v1.9] -> differential/statistical testing [ADMIXTURE v1.3.0] -> stage not stated [BCFtools v1.9, BEDTools, IQ-TREE v2.1.4, PLINK v1.90b, R, VCFtools]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Evidence: Breed ancestry estimates for each dog were generated using ADMIXTURE ( 113 ), as previously described ( 16 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### Anthropocene genetic diversity loss in the marine tropics. (PNAS 2025)

- DOI: 10.1073/pnas.2513012122 | PMCID: PMC12646237 | PMID: 41231948
- Version used: **1.3**
- Evidence: We analyzed population structure with PCA and ADMIXTURE v.1.3 ( 31 ).
- Full pipeline: quality control [VCFtools v0.1.14] -> alignment/mapping [SAMtools v1.9, SPAdes v3.15.3] -> dimensionality reduction/clustering [ADMIXTURE v1.3, PLINK v1.9] -> stage not stated [freebayes v1.3.1]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Evidence: By using f4 statistics instead of individual allele frequencies, Struct-f4 reduces biases caused by the amount of genetic drift exclusive to single populations, which affects clustering methods that assume Hardy–Weinberg equilibrium, such as ADMIXTURE and STRUCTURE ( 23 , 71 ).
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Evidence: Genome Scans, ADMIXTURE, TriangulaR.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### The power of coalescent methods for inferring recent and ancient gene flow in endangered Bactrian camels. (PNAS 2025)

- DOI: 10.1073/pnas.2410949122 | PMCID: PMC12337305 | PMID: 40720656
- Evidence: A number of methods, including the D -statistic ( 15 ), ADMIXTURE ( 16 ), TREEMIX ( 17 ), and G-PHOCS ( 18 ) were used to infer gene flow.
- Full pipeline: differential/statistical testing [ADMIXTURE]

### A population genetic analysis of the nematode &lt;i&gt;Strongyloides stercoralis&lt;/i&gt; in Asia shows that human infection is not a zoonosis from dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2424630122 | PMCID: PMC12304889 | PMID: 40663613
- Evidence: We looked for evidence of admixture among the iL3s, with ADMIXTURE best supporting k = 8 groups, three of which are specific for human-derived iL3s (though including a single dog-derived iL3s, as the NJ tree, above), and four for dog-derived iL3s ( Fig.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, Bowtie2] -> stage not stated [ADMIXTURE]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Version used: **1.3.0**
- Evidence: The proportion of European and African genetic ancestry for each skin donor was estimated using the supervised clustering algorithm in ADMIXTURE (v1.3.0) ( 28 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### Diploidization in a wild rice allopolyploid is both episodic and gradual. (PNAS 2025)

- DOI: 10.1073/pnas.2424854122 | PMCID: PMC12232711 | PMID: 40569381
- Evidence: To investigate the phylogenetic relationships and population genetic structure of O. minuta and its progenitors, we analyzed all 210 genomes using neighbor-joining (NJ), principal component analysis (PCA), and ADMIXTURE.
- Full pipeline: alignment/mapping [BUSCO] -> dimensionality reduction/clustering [ADMIXTURE]

### Natural dispersal is better than translocation for reducing risks of inbreeding depression in eastern black rhinoceros (&lt;i&gt;Diceros bicornis michaeli&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2414412122 | PMCID: PMC12167989 | PMID: 40460127
- Evidence: ADMIXTURE ( 62 ) was used to estimate population structure for complexity (K) values from 1 to 5 using default settings as explained in the manual.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [SAMtools] -> variant calling [BCFtools] -> differential/statistical testing [emmeans] -> stage not stated [ADMIXTURE, PLINK v1.9, R, VCFtools]

### Distinguishing species boundaries from geographic variation. (PNAS 2025)

- DOI: 10.1073/pnas.2423688122 | PMCID: PMC12088384 | PMID: 40324080
- Version used: **1.3.0**
- Evidence: We ran ADMIXTURE v.1.3.0 ( 37 ) on each of our four separate, filtered assemblies on a range of K values which varied depending on the assembly and with five replicates per run.
- Full pipeline: visualisation [ggplot2] -> stage not stated [ADMIXTURE v1.3.0, R, RAxML, VCFtools v0.1.13, tidyverse, vegan]

### Horizontal transfer of nuclear DNA in transmissible cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2424634122 | PMCID: PMC12067285 | PMID: 40261943
- Version used: **1.3.0**
- Evidence: We used the ADMIXTURE v1.3.0 software ( 24 ) to infer streams of individual ancestries in the populations represented in our data.
- Full pipeline: variant calling [DESeq2] -> quantification [R] -> normalisation [DESeq2] -> differential/statistical testing [R] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.2.5]

### Archaeogenomic insights into commensalism and regional variation in pig management in Neolithic northwest Europe. (PNAS 2025)

- DOI: 10.1073/pnas.2410235122 | PMCID: PMC11962444 | PMID: 40096601
- Evidence: Pseudohaploid genotypes were used for autosomal phylogenetic reconstruction [using plink 1.9 ( 104 ) and PHYLIP ( 105 )], a projection PCA using smartPCA ( 106 ), an admixture analysis using ADMIXTURE ( 107 ), and an admixture graph analysis using ADMIXTOOLS2 qpGraph ( 108 ).
- Full pipeline: variant calling [ADMIXTURE] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ANGSD] -> structure determination [ADMIXTURE, ANGSD] -> stage not stated [RAxML]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Evidence: High-quality 4DTv SNPs (36,028) were used for maximum-likelihood phylogenetic tree construction (IQ-TREE) (v1.6.12) ( 69 ), PCA (PLINK, v1.9), and population structure analysis (ADMIXTURE, K = 2–10, v1.23) ( 70 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Evolution of genome-wide barriers to gene flow during complex speciation in rattlesnakes. (PNAS 2026)

- DOI: 10.1073/pnas.2609058123 | PMCID: PMC13214041 | PMID: 42166239
- Evidence: Analyses of population structure (ADMIXTURE and PCA; SI Appendix , Figs.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [BUSCO]

### Large future genetic diversity losses are predicted from conservation indicators even with habitat protection. (PNAS 2026)

- DOI: 10.1073/pnas.2514371123 | PMCID: PMC13037886 | PMID: 41886371
- Evidence: We estimated F ST by running ADMIXTURE ( 36 ) on the same 29 species with genomic data, yielding a mean F ST = 0.26, range = [0.01 to 0.7].
- Full pipeline: variant calling [R v0.0.3] -> stage not stated [ADMIXTURE, PLINK v1.9, SciPy]

### The genetic legacy of African Americans from Catoctin Furnace. (Science 2023)

- DOI: 10.1126/science.ade4995 | PMCID: PMC10958645 | PMID: 37535739
- Evidence: Further, we compared the results of ADMIXTURE ( Fig.
- Full pipeline: stage not stated [ADMIXTURE]

### Moisture-responsive root-branching pathways identified in diverse maize breeding germplasm. (Science 2025)

- DOI: 10.1126/science.ads5999 | PMCID: PMC11956805 | PMID: 39913586
- Evidence: Ancestry components of n = 231 inbred lines calculated by ADMIXTURE (k=3).
- Full pipeline: stage not stated [ADMIXTURE]

