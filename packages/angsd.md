# ANGSD

- **Category:** statgen
- **Papers in survey:** 78
- **Journals:** Nature (35), PNAS (34), Cell (8), Science (1)
- **Years:** 2021 (14), 2022 (10), 2023 (11), 2024 (12), 2025 (25), 2026 (6)
- **Versions named:** 0.910 (7), 0.933 (4), 0.930 (3), 0.931 (3), 0.935 (3), 0.921 (3), 0.940 (2), 0.923 (1), 0.917 (1), 0.934 (1)
- **Pipeline stages it appears in:** quality control (33), alignment/mapping (9), variant calling (7), differential/statistical testing (3), quantification (1), structure determination (1)

## Papers

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Version used: **0.921**
- Evidence: 5.1 Patterson et al., 2012 https://github.com/DReichLab/AdmixTools ADMIXTURE Alexander et al., 2009 http://dalexander.github.io/admixture/download.html ANGSD v.
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...http://broadinstitute.github.io/picard http://broadinstitute.github.io/picard MapDamage2.0 Jónsson et al., 2013 https://ginolhac.github.io/mapDamage/ ANGSD Korneliussen et al., 2014 https://github.com/ANGSD/angsd READ Monroy Kuhn et al., 2018 https://bitbucket.org/tguenther/read/src/master/ KING Manichaikul et al., 2010 http://people.virginia.edu/∼wc9c/KING/ PLINK1.9 Purcell et al., 2007 https://w...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### Genome-wide data from medieval German Jews show that the Ashkenazi founder event pre-dated the 14<sup>th</sup> century. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.002 | PMCID: PMC9793425 | PMID: 36455558
- Evidence: We estimated the degree of contamination with contamMix version 1.0–12 ( Fu et al., 2013 ) for the mitochondrial DNA and ANGSD for the X chromosome ( Korneliussen et al., 2014 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BCFtools, BWA v0.7.15] -> quantification [SAMtools] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [BEAST v2.6.6] -> visualisation [ggplot2] -> stage not stated [ADMIXTURE, R]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ... Reference Consortium dataset ( McCarthy et al., 2016 ) accession number EGAD00001002729 on the European Genome-phenome Archive HapMap file for chrX (ANGSD) HapMapChrx.gz ( Rasmussen et al., 2011 ) http://www.popgen.dk/angsd/index.php/ANGSD HapMap phase II b37 genetic map N/A https://github.com/odelaneau/shapeit4/tree/master/maps Human reference sequence hs37d5 ( 1000 Genomes Project Consortium et...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Ancient genomes reveal origin and rapid trans-Eurasian migration of 7<sup>th</sup> century Avar elites. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.007 | PMCID: PMC9042794 | PMID: 35366416
- Version used: **0.910**
- Evidence: ... https://github.com/statgen/bamUtil https://github.com/statgen/bamUtil CircularMapper Peltzer et al., 2016 https://github.com/apeltzer/CircularMapper ANGSD 0.910 Korneliussen et al., 2014 http://www.popgen.dk/angsd/index.php/ANGSD Schmutzi Renaud et al., 2015 https://github.com/grenaud/schmutzi SAMtools 1.3 Li et al., 2009 http://www.htslib.org/doc/samtools.html pileupCaller https://github.com/sts...
- Full pipeline: read trimming [BWA v0.7.12] -> stage not stated [ANGSD v0.910, GATK v3.5, PLINK v1.9, R v4.0, SAMtools v1.3, SHAPEIT]

### A genetic history of the Balkans from Roman frontier to Slavic migrations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.10.018 | PMCID: PMC10752003 | PMID: 38065079
- Evidence: We computed the ratio of X-to-Y chromosome reads, estimated mismatch rates to the consensus mitochondrial sequence, using contamMix-1.0.10 62 and ran X-chromosome contamination estimates using ANGSD 63 in males with sufficient coverage ( Data S2, Table 1 ).
- Full pipeline: quality control [ANGSD] -> stage not stated [BCFtools]

### Long shared haplotypes identify the southern Urals as a primary source for the 10th-century Hungarians. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.002 | PMCID: PMC12711333 | PMID: 41106360
- Version used: **0.921**
- Evidence: Ancient DNA authenticity was verified using contamMix (v1.0.10511)( 110 ) to detect heterogeneity in mitochondrial DNA sequences and ANGSD (0.921–3-g40ac3d6)( 111 ) to detect heterogeneity in X chromosome sequences.
- Full pipeline: dimensionality reduction/clustering [NetworkX] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools, R]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **0.933**
- Evidence: 101 https://github.com/popgenDK/SATC ANGSD v0.933-102-g7d57642 Korneliussen et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### Triangulation supports agricultural spread of the Transeurasian languages. (Nature 2021)

- DOI: 10.1038/s41586-021-04108-8 | PMCID: PMC8612925 | PMID: 34759322
- Version used: **0.910**
- Evidence: Third, we measured the nuclear genome contamination rate in males on the basis of X chromosome data as implemented in ANGSD v.0.910 80 .
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12, SAMtools v1.3] -> simulation/modelling [BEAST v2.6]

### The genomic origins of the Bronze Age Tarim Basin mummies. (Nature 2021)

- DOI: 10.1038/s41586-021-04052-7 | PMCID: PMC8580821 | PMID: 34707286
- Version used: **0.910**
- Evidence: Last, we estimated the nuclear contamination rate on men using ANGSD v.0.910 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools v1.7] -> stage not stated [ADMIXTURE v1.3.0, PLINK v1.90]

### The origins and spread of domestic horses from the Western Eurasian steppes. (Nature 2021)

- DOI: 10.1038/s41586-021-04018-9 | PMCID: PMC8550961 | PMID: 34671162
- Evidence: Minor and major alleles were identified using ANGSD 60 (version 0.933-86-g3fefdc4, htslib: 1.10.2-106-g9c35744) and the following parameters: -baq 0 -doMajorMinor 2 -uniqueOnly 1 -minMapQ 25 -minQ 30 -minind 7 -doCounts 1 -doMaf 1.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [Rcpp] -> structure determination [RAxML] -> stage not stated [ANGSD, R]

### Genomic insights into the formation of human populations in East Asia. (Nature 2021)

- DOI: 10.1038/s41586-021-03336-2 | PMCID: PMC7993749 | PMID: 33618348
- Evidence: We considered data from an individual usable for analysis if it consisted of a minimum 5000 SNPs, if the lower bound of its ANGSD 95% confidence interval is <0.01, and if the upper bound of its contamMix 95% confidence interval is >0.98.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [ANGSD, PLINK]

### Million-year-old DNA sheds light on the genomic history of mammoths. (Nature 2021)

- DOI: 10.1038/s41586-021-03224-9 | PMCID: PMC7116897 | PMID: 33597750
- Version used: **0.921**
- Evidence: Allele sampling To minimize coverage-related biases, all subsequent analyses were based on pseudo-haploidized sequences that were generated by randomly selecting a single high quality base call at each autosomal genomic site using ANGSD v0.921 36 .
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.921, BCFtools, Picard, RepeatMasker v4.0.7, SAMtools v1.10]

### The Anglo-Saxon migration and the formation of the early English gene pool. (Nature 2022)

- DOI: 10.1038/s41586-022-05247-2 | PMCID: PMC9534755 | PMID: 36131019
- Evidence: Contamination estimation We used the Analysis of Next Generation Sequencing Data (ANGSD) package 84 (v0.923) to test for heterozygosity of polymorphic sites on the X chromosome in male individuals, applying a contamination threshold of 5% at the results of method two.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA, Picard] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, SAMtools]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Evidence: We used contamMix to determine evidence of contamination based on polymorphism in mitochondrial DNA 56 , and ANGSD to determine evidence of contamination based on polymorphism on the X chromosome in males 57 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Extensive pedigrees reveal the social organization of a Neolithic community. (Nature 2023)

- DOI: 10.1038/s41586-023-06350-8 | PMCID: PMC10432279 | PMID: 37495691
- Evidence: We used the ANGSD (Analysis of Next Generation Sequencing Data) package to test for heterozygosity of polymorphic sites on the X chromosome in male individuals, applying a contamination threshold of 5% that none of our samples have reached 53 (maximum = 2.41%; Supplementary Table 1 ).
- Full pipeline: quality control [ANGSD] -> read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [QGIS v3.30]

### Early contact between late farming and pastoralist societies in southeastern Europe. (Nature 2023)

- DOI: 10.1038/s41586-023-06334-8 | PMCID: PMC10412445 | PMID: 37468624
- Evidence: The nuclear contamination for males was estimated using ANGSD 79 and ranged from 0.2% to 2%.
- Full pipeline: quality control [ANGSD] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools v1.3]

### Palaeogenomics of Upper Palaeolithic to Neolithic European hunter-gatherers. (Nature 2023)

- DOI: 10.1038/s41586-023-05726-0 | PMCID: PMC9977688 | PMID: 36859578
- Version used: **0.934**
- Evidence: We applied ANGSD 0.934 70 and hapCon 71 for libraries from male individuals, and applied contamLD 72 and a newly developed method that analyses contamination in ROH for female and male libraries (see Supplementary Information, section 2 for a detailed description).
- Full pipeline: quality control [ANGSD v0.934] -> read trimming [BWA v0.7.12] -> alignment/mapping [BWA v0.7.12, SAMtools] -> differential/statistical testing [R v3.5]

### Evolution of the germline mutation rate across vertebrates. (Nature 2023)

- DOI: 10.1038/s41586-023-05752-y | PMCID: PMC9995274 | PMID: 36859541
- Evidence: Nucleotide diversity ( π ) was calculated using ANGSD 92 .
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard, SAMtools] -> variant calling [GATK v4.0.7.0] -> stage not stated [ANGSD, BCFtools v1.2, IQ-TREE v2.0.3, R]

### The rise and transformation of Bronze Age pastoralists in the Caucasus. (Nature 2024)

- DOI: 10.1038/s41586-024-08113-5 | PMCID: PMC11602729 | PMID: 39478221
- Evidence: Following this, the ANGSD 67 (v0.935) tool was used to calculate the rate of heterozygosity on the X chromosome to determine contamination in genetically male individuals, applying a contamination threshold of 5% in individuals with at least 100 X-SNP positions covered twice.
- Full pipeline: quality control [ANGSD, FastQC] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE]

### Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. (Nature 2024)

- DOI: 10.1038/s41586-024-07881-4 | PMCID: PMC11390480 | PMID: 39261618
- Version used: **0.930**
- Evidence: In addition, we computed type-specific error rates using ANGSD v0.930 83 (Supplementary Figs.
- Full pipeline: alignment/mapping [GATK, SAMtools] -> normalisation [ADMIXTURE] -> registration [GATK, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [Matplotlib v3.5.3, R, ggplot2 v3.3.2] -> stage not stated [ANGSD v0.930, PLINK v1.9.20200712]

### Ancient genomes reveal insights into ritual life at Chichén Itzá. (Nature 2024)

- DOI: 10.1038/s41586-024-07509-7 | PMCID: PMC11208145 | PMID: 38867041
- Evidence: Analysis of next generation sequencing data(ANGSD) was used to estimate nuclear contamination, as males are expected to be homozygous at each X chromosome position 145 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.7.12] -> stage not stated [ADMIXTURE v1.3.0, SAMtools]

### Widespread horse-based mobility arose around 2200 BCE in Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-024-07597-5 | PMCID: PMC11269178 | PMID: 38843826
- Version used: **0.917**
- Evidence: 2 , entailing data pseudo-haploidization with ANGSD (v.0.917) 63 for those sites covered by two reads or more (base quality scores greater than or equal to 30), and disregarding sites uncovered in 30% or more of the samples.
- Full pipeline: stage not stated [ANGSD v0.917, Bowtie2]

### Network of large pedigrees reveals social practices of Avar communities. (Nature 2024)

- DOI: 10.1038/s41586-024-07312-4 | PMCID: PMC11078744 | PMID: 38658749
- Version used: **0.910**
- Evidence: Exogenous human autosomal DNA contamination was estimated in male individuals by assessing X-chromosome heterozygosity levels using ANGSD v.0.910 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [BCFtools v1.3, Cytoscape v3.9.1, Picard, igraph]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Evidence: Three methods were used to estimate DNA contamination: two based on mitochondrial sequences 81 , 82 and one method investigating X-chromosomal data in males (ANGSD, Supplementary Note 1 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### Elevated genetic risk for multiple sclerosis emerged in steppe pastoralist populations. (Nature 2024)

- DOI: 10.1038/s41586-023-06618-z | PMCID: PMC10781639 | PMID: 38200296
- Version used: **0.931**
- Evidence: Additionally, we applied ANGSD (v0.931) 58 to estimate nuclear contamination by quantifying heterozygosity on the X chromosome in males.
- Full pipeline: quality control [ANGSD v0.931] -> alignment/mapping [BWA v0.7.17] -> quantification [ANGSD v0.931] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [PLINK, Picard, R, SAMtools v1.10]

### Ancient DNA from Shimao city records kinship practices in Neolithic China. (Nature 2025)

- DOI: 10.1038/s41586-025-09799-x | PMCID: PMC12711557 | PMID: 41299168
- Evidence: Contamination rates for men were also estimated using ANGSD 56 , leveraging the fact that men have one copy of the X chromosome, and verified using HapCon 57 , to improve the performance of low-coverage data.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.5.10] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Evidence: Contamination estimation We used the ANGSD (Analysis of Next Generation Sequencing Data) package 98 (v.0.923) to test for heterozygosity of polymorphic sites on the X chromosome in male individuals, applying a contamination threshold of 5% at the results of method 1.
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### Phylogenetically informative proteins from an Early Miocene rhinocerotid. (Nature 2025)

- DOI: 10.1038/s41586-025-09231-4 | PMCID: PMC12267063 | PMID: 40634620
- Evidence: We used ANGSD 63 to generate consensus sequences from BAM files corresponding to chromosomes that include genes of interest.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [ANGSD]

### Whole-genome ancestry of an Old Kingdom Egyptian. (Nature 2025)

- DOI: 10.1038/s41586-025-09195-5 | PMCID: PMC12367555 | PMID: 40604286
- Version used: **0.933**
- Evidence: 110 ); (2) present-day mitochondrial DNA-based contamination using schmutzi (commit be61017) 111 ; and (3) chromosome X contamination on libraries assigned as male using ANGSD v.0.933 (ref.
- Full pipeline: quality control [ANGSD v0.933] -> variant calling [BCFtools v1.19] -> dimensionality reduction/clustering [ADMIXTURE v1.2] -> stage not stated [PLINK v1.9]

### Ancient DNA reveals the prehistory of the Uralic and Yeniseian peoples. (Nature 2025)

- DOI: 10.1038/s41586-025-09189-3 | PMCID: PMC12342343 | PMID: 40604287
- Version used: **0.923**
- Evidence: We flagged as “questionable” males with evidence of high polymorphism on the X chromosome (lower bound of the 95% confidence interval for mismatch rate >1%), or as “critical” (if >5%), estimated using ANGSD v0.923 72 .
- Full pipeline: variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [ANGSD v0.923, QGIS v3.40.6, R]

### Ancient DNA reveals a two-clanned matrilineal community in Neolithic China. (Nature 2025)

- DOI: 10.1038/s41586-025-09103-x | PMCID: PMC12310535 | PMID: 40468069
- Version used: **0.910**
- Evidence: Additionally, the nuclear genome contamination rate in male individuals was determined by analysing X chromosome data with ANGSD v0.910 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [R]

### Picuris Pueblo oral history and genomics reveal continuity in US Southwest. (Nature 2025)

- DOI: 10.1038/s41586-025-08791-9 | PMCID: PMC12137115 | PMID: 40307544
- Version used: **0.931**
- Evidence: 104 ), and present-day contamination using ContamMix 52 and ANGSD v.0.931 (ref.
- Full pipeline: quality control [ANGSD v0.931] -> variant calling [BCFtools v1.17] -> stage not stated [ADMIXTURE, BEAST v2.6, Picard v2.25.0, SAMtools v1.3.1]

### Punic people were genetically diverse with almost no Levantine ancestors. (Nature 2025)

- DOI: 10.1038/s41586-025-08913-3 | PMCID: PMC12226237 | PMID: 40269169
- Evidence: To estimate a 95% confidence interval for contamination on the X chromosome in males (who should have no variation on the non-pseudoautosomal regions of the X chromosome in the absence of contamination), we used ANGSD 51 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK, R, SAMtools]

### High continuity of forager ancestry in the Neolithic period of the eastern Maghreb. (Nature 2025)

- DOI: 10.1038/s41586-025-08699-4 | PMCID: PMC12094895 | PMID: 40074896
- Evidence: 1.0.1051 [ 81 ], and (2) for the X chromosome (in males only), we evaluated mismatch rates using ANGSD [ 82 ].
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [ANGSD]

### A genomic history of the North Pontic Region from the Neolithic to the Bronze Age. (Nature 2025)

- DOI: 10.1038/s41586-024-08372-2 | PMCID: PMC11909631 | PMID: 39910299
- Evidence: To assess ancient DNA authenticity, we used both contamMix-1.0.1051 56 to search for heterogeneity in mitochondrial DNA sequences which are expected to be non-variable in uncontaminated individuals, and ANGSD 57 to search for heterogeneity in X chromosome sequences which should be non-variable in contaminated male individuals 57 .
- Full pipeline: quality control [ANGSD] -> stage not stated [ADMIXTURE, BCFtools, SAMtools]

### The genetic origin of the Indo-Europeans. (Nature 2025)

- DOI: 10.1038/s41586-024-08531-5 | PMCID: PMC11922553 | PMID: 39910300
- Evidence: We assessed ancient DNA authenticity by using contamMix-1.0.1051 82 to search for heterogeneity in mitochondrial DNA sequences which are expected to be non-variable in uncontaminated individuals, and also ANGSD to test for heterogeneity in X chromosome sequences which are expected to be homozygous in males.
- Full pipeline: quality control [ANGSD] -> stage not stated [BCFtools, SAMtools]

### Ancient DNA reveals reproductive barrier despite shared Avar-period culture. (Nature 2025)

- DOI: 10.1038/s41586-024-08418-5 | PMCID: PMC11864967 | PMID: 39814885
- Version used: **0.910**
- Evidence: We used Schmutzi (v.0.7.12) for estimating contamination level on mitochondria 61 and ANGSD (v.0.910) for estimating contamination on X chromosomes 62 .
- Full pipeline: quality control [ANGSD v0.910] -> read trimming [SAMtools] -> stage not stated [Picard]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Version used: **0.935**
- Evidence: ANGSD v.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Version used: **0.940**
- Evidence: Estimation of human DNA contamination and damage patterns were performed at a library level, using contamMix 77 , ANGSD (v.0.940) 78 , and mapDamage2.0 79 .
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Lasting Lower Rhine-Meuse forager ancestry shaped Bell Beaker expansion. (Nature 2026)

- DOI: 10.1038/s41586-026-10111-8 | PMCID: PMC12978843 | PMID: 41673154
- Evidence: We estimated mismatch rates to the consensus mitochondrial sequence using contamMix-1.0.1051 68 , and X-chromosome contamination estimates using ANGSD 69 in males with sufficient coverage.
- Full pipeline: quality control [ANGSD] -> variant calling [BCFtools, SAMtools]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Version used: **0.930**
- Evidence: Pseudo-haploid genotypes were called using ANGSD (v.0.930; ref.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Evidence: Contamination evidence based on mtDNA polymorphism was determined using contamMix 90 , while hapConX 91 and ANGSD 92 were used to assess contamination evidence based on X-chromosome polymorphism in males ( Extended Data Tables 0.1 . and 0.2 ).
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### Response of an Afro-Palearctic bird migrant to glaciation cycles. (PNAS 2021)

- DOI: 10.1073/pnas.2023836118 | PMCID: PMC8719893 | PMID: 34949638
- Evidence: Consensus sequences for the resequenced individuals were obtained by choosing the most common base per position (-doFasta 2 in ANGSD, 68).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> registration [GATK, Picard] -> differential/statistical testing [R v3.4.2] -> stage not stated [ANGSD, BEDTools, BUSCO, RepeatMasker]

### Genomic evidence for inbreeding depression and purging of deleterious genetic variation in Indian tigers. (PNAS 2021)

- DOI: 10.1073/pnas.2023018118 | PMCID: PMC8670471 | PMID: 34848534
- Evidence: Next, we converted the mapped reads into a haploid FASTA consensus sequence, excluding all sites with depth above one (as such sites contain at least one mismapped read) using ANGSD (http://www.popgen.dk/angsd/index.php/ANGSD) - dofasta.
- Full pipeline: alignment/mapping [ANGSD, GATK] -> registration [GATK] -> stage not stated [Picard, Strelka, VCFtools, VEP]

### Genomic basis of fishing-associated selection varies with population density. (PNAS 2021)

- DOI: 10.1073/pnas.2020833118 | PMCID: PMC8713780 | PMID: 34903645
- Evidence: The following site filtering options were used in ANGSD: -SNP_pval 1e-6 -remove_bads 1 (removal of bad mapped reads), -setMinDepth 48 (minimum sum of depth across individuals), -setMaxDepth 600 (maximum sum of depth across individuals), -minInd 48 (minimum number of individuals), -minQ 20 (minimum read quality), -minMapQ 20 (minimum mapping quality), and -minMaf 0.05 (minimum minor allele frequenc...
- Full pipeline: read trimming [Cutadapt v1.16, Trimmomatic v0.36] -> alignment/mapping [ANGSD, BWA v0.7.17] -> differential/statistical testing [ggplot2] -> stage not stated [Picard v2.18.14, R v3.5, SnpEff v4.4]

### Modern Siberian dog ancestry was shaped by several thousand years of Eurasian-wide trade and human dispersal. (PNAS 2021)

- DOI: 10.1073/pnas.2100338118 | PMCID: PMC8488619 | PMID: 34544854
- Evidence: Each sample was aligned to the CanFam3.1 reference dog genome ( 27 ) using the Burrows-Wheeler Alignment Backtrack algorithm (BWA aln) ( 28 , 29 ), subsequently pseudohaploid calling was performed on the samples and a panel of publicly available canid samples with ANGSD ( 30 ) to be used for downstream analyses.
- Full pipeline: alignment/mapping [ANGSD, BWA] -> stage not stated [R]

### Herded and hunted goat genomes from the dawn of domestication in the Zagros Mountains. (PNAS 2021)

- DOI: 10.1073/pnas.2100901118 | PMCID: PMC8237664 | PMID: 34099576
- Evidence: D statistics ( 39 ), IBS, heterozygosity and error estimation, population branch statistic, and F ST outlier analyses were performed using the ANGSD toolkit ( 75 ) with transversion variants only.
- Full pipeline: alignment/mapping [MUSCLE] -> registration [MUSCLE] -> differential/statistical testing [ANGSD] -> stage not stated [BCFtools v1.5, BEAST]

### Genomic stability through time despite decades of exploitation in cod on both sides of the Atlantic. (PNAS 2021)

- DOI: 10.1073/pnas.2025453118 | PMCID: PMC8054022 | PMID: 33827928
- Version used: **0.931**
- Evidence: Reads were mapped to the chromosome-scale gadMor2 Atlantic cod genome assembly ( 25 ), and SNP allele frequencies were estimated using ANGSD 0.931 with custom filtering to avoid mapping errors and historical DNA damage patterns ( SI Appendix , Materials and Methods ) ( 50 ).
- Full pipeline: alignment/mapping [ANGSD v0.931] -> stage not stated [ADMIXTURE]

### Ecological adaptation in European eels is based on phenotypic plasticity. (PNAS 2021)

- DOI: 10.1073/pnas.2022620118 | PMCID: PMC7848574 | PMID: 33479174
- Version used: **0.933**
- Evidence: We used ANGSD v0.933 ( 24 ) to estimate genotype likelihoods for all analyses, because our low sequencing coverage approach prohibits calling genotypes.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> variant calling [ANGSD v0.933] -> dimensionality reduction/clustering [R v3.6.1] -> differential/statistical testing [R v3.6.1]

### The diverse genetic origins of a Classical period Greek army. (PNAS 2022)

- DOI: 10.1073/pnas.2205272119 | PMCID: PMC9564095 | PMID: 36191217
- Evidence: We used contamMix to test for contamination based on polymorphism in the mtDNA ( 116 ), applying an mtDNA contamination threshold of 5%, and ANGSD to test for contamination based on polymorphism on the X chromosome in males ( 117 ), applying an X-chromosomal contamination threshold of 2%.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.6.1] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Version used: **0.935**
- Evidence: To account for uncertainty in genotyping, the site frequency spectrum (SFS), genetic diversity, and Tajima’s D were calculated using the probabilistic framework implemented in ANGSD (version 0.935) ( 66 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **0.929**
- Evidence: We estimated population differentiation ( F ST ) for all pairwise population comparisons using the program ANGSD v.0.929-21-g4c6d001 ( 82 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Ancient DNA gives new insights into a Norman Neolithic monumental cemetery dedicated to male elites. (PNAS 2022)

- DOI: 10.1073/pnas.2120786119 | PMCID: PMC9170172 | PMID: 35446690
- Evidence: We used the ANGSD package to test for the heterozygosity of polymorphic sites on the X chromosome in male individuals, applying a contamination threshold of 5% ( 34 ) ( Dataset S1 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.7.12] -> stage not stated [SAMtools v1.3.1]

### Ancient and modern genomics of the Ohlone Indigenous population of California. (PNAS 2022)

- DOI: 10.1073/pnas.2111533119 | PMCID: PMC9060455 | PMID: 35312358
- Evidence: First, we estimated genotype likelihoods in the ancient and modern samples with ANGSD ( 67 ).
- Full pipeline: variant calling [ANGSD]

### Natural disaster and immunological aging in a nonhuman primate. (PNAS 2022)

- DOI: 10.1073/pnas.2121663119 | PMCID: PMC8872742 | PMID: 35131902
- Evidence: Kinship was estimated using ANGSD and ngsRelate ( 79 ) from mapped 3′seq bam files.
- Full pipeline: alignment/mapping [ANGSD, kallisto] -> quantification [limma] -> normalisation [limma] -> differential/statistical testing [R v4.0.2] -> stage not stated [HOMER, Seurat]

### Descent, marriage, and residence practices of a 3,800-year-old pastoral community in Central Eurasia. (PNAS 2023)

- DOI: 10.1073/pnas.2303574120 | PMCID: PMC10483636 | PMID: 37603728
- Evidence: Potential contamination rates were estimated based on MT-reads using contamMix-1.0.9 ( 55 ) and with ContamLD ( 56 ) in combination with ANGSD ( 115 ) for reads aligned to the autosomes and the X chromosome in males, respectively.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [ANGSD] -> registration [GATK v3.6]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Evidence: Genotype likelihoods were first estimated from bam files in ANGSD ( 98 ) using the GATK model (-GL 2), inferring major and minor alleles (-doMajorMinor 1) and outputting only polymorphic sites (-SNP_pval 1 e-6 ) with data in at least 60% of individuals (-minInd 30).
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Standing genetic variation fuels rapid evolution of herbicide resistance in blackgrass. (PNAS 2023)

- DOI: 10.1073/pnas.2206808120 | PMCID: PMC10120058 | PMID: 37043536
- Version used: **0.930**
- Evidence: Watterson thetas θ W were estimated with ANGSD v0.930 ( 74 ) exclusively from the ddRAD-sequenced portion of the A. myosuroides assembly.
- Full pipeline: read trimming [BUSCO] -> alignment/mapping [MAFFT v7.407] -> variant calling [MAFFT v7.407] -> visualisation [MAFFT v7.407] -> stage not stated [ADMIXTURE, ANGSD v0.930, GATK v4.1.3.0, InterProScan]

### Estimating human mobility in Holocene Western Eurasia with large-scale ancient genomic data. (PNAS 2023)

- DOI: 10.1073/pnas.2218375120 | PMCID: PMC9992830 | PMID: 36821583
- Evidence: For quality filtering, we kept only samples with 25,000 or more recovered autosomal SNPs on this array, determinable molecular sex and—for male individuals—an X-chromosome contamination value determined with ANGSD ( 78 ) < 0.1.
- Full pipeline: quality control [ANGSD] -> stage not stated [R, ggpubr, igraph, tidyverse]

### Divergent sensory and immune gene evolution in sea turtles with contrasting demographic and life histories. (PNAS 2023)

- DOI: 10.1073/pnas.2201076120 | PMCID: PMC9962930 | PMID: 36749728
- Evidence: ROHs were identified by generating a SNP-list using the analysis of next generation sequencing data [ANGSD; ( 128 )] pipeline.
- Full pipeline: alignment/mapping [BCFtools, SAMtools] -> variant calling [BCFtools, GATK, SAMtools] -> stage not stated [ANGSD, BUSCO, OrthoFinder, PLINK]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Version used: **0.939**
- Evidence: Likelihoods for the three possible genotypes in each biallelic site were then calculated from the BAM files in ANGSD 0.939 ( 77 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Elucidating the sustainability of 700 y of Inuvialuit beluga whale hunting in the Mackenzie River Delta, Northwest Territories, Canada. (PNAS 2024)

- DOI: 10.1073/pnas.2405993121 | PMCID: PMC11348011 | PMID: 39136992
- Evidence: We used ANGSD v/0.935 ( 86 ) to identify variable sites in the nuclear dataset.
- Full pipeline: alignment/mapping [BWA, MAFFT, RepeatMasker, SAMtools] -> registration [GATK, Picard] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ANGSD]

### Capturing the fusion of two ancestries and kinship structures in Merovingian Flanders. (PNAS 2024)

- DOI: 10.1073/pnas.2406734121 | PMCID: PMC11228521 | PMID: 38913897
- Evidence: For male individuals, contamination was also estimated on the basis of chromosome X heterozygosity using the two contamination estimation methods implemented in ANGSD ( 42 ). mapDamage2.0 ( 48 ) was used to estimate the frequency of C to T transitions in the 5′ end of the DNA fragments.
- Full pipeline: quality control [ANGSD, MultiQC] -> dimensionality reduction/clustering [UMAP]

### Extraordinary preservation of gene collinearity over three hundred million years revealed in homosporous lycophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2312607121 | PMCID: PMC10823260 | PMID: 38236735
- Version used: **0.935**
- Evidence: Genome-wide heterozygosity was estimated using ANGSD v0.935 ( 64 ) based on a Site Frequency Spectrum (SFS).
- Full pipeline: stage not stated [ANGSD v0.935, BUSCO, DESeq2 v3.17, RAxML v8.2.12]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Evidence: To disentangle whether phylogenetic discordance among Felis taxa has resulted from introgression or incomplete lineage sorting (ILS) as was previously reported ( 10 ), we conducted a series of tests using different software [Dsuite ( 11 ), QuIBL ( 12 ), and ANGSD ( 13 )] with independent algorithms based on input data of sequences or phylogenetic trees.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### A new late Neanderthal from Crimea reveals long-distance connections across Eurasia. (PNAS 2025)

- DOI: 10.1073/pnas.2518974122 | PMCID: PMC12625898 | PMID: 41144685
- Evidence: A consensus sequence was called with ANGSD –doFasta ( SI Appendix , section E ) and multiple sequence alignment including a collection of present-day humans, Neanderthals, and Pan troglodytes was performed via the MEGA11 in-built MUSCLE algorithm ( 84 , 85 ).
- Full pipeline: alignment/mapping [ANGSD, Python] -> stage not stated [GATK, SAMtools v1.20]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: Finally, we conducted a GWAS on color morph using the score test (-doAsso2) function in ANGSD ( 72 ), which relies on genotype likelihoods rather than called genotypes–a more appropriate approach for low-coverage data compared to methods based on genotype frequencies.
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Evidence: We used ANGSD -doIBS ( 83 ), which selects one allele per site for each sample based on a randomly sampled high-quality sequencing read.
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### The importance of small-island populations for the long-term survival of endangered large-bodied insular mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422690122 | PMCID: PMC12232422 | PMID: 40553499
- Evidence: To assess the efficiency of purifying selection across different populations, we first built unfolded site frequency spectra (SFS) using ANGSD ( 28 ), based on alleles that have been assigned different impact ratings by the Variant Effect Predictor ( 29 ), i.e., low, modifier, moderate, and high ( Fig.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [ANGSD, QGIS, R, VEP]

### Archaeogenomic insights into commensalism and regional variation in pig management in Neolithic northwest Europe. (PNAS 2025)

- DOI: 10.1073/pnas.2410235122 | PMCID: PMC11962444 | PMID: 40096601
- Evidence: D -statistics, Fst outlier analysis, and mitochondrial phylogeny reconstruction were performed using the ANGSD toolkit ( 109 ), restricted to transversions.
- Full pipeline: variant calling [ADMIXTURE] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ANGSD] -> structure determination [ADMIXTURE, ANGSD] -> stage not stated [RAxML]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Version used: **0.933**
- Evidence: For each locus, a consensus sequence in Fasta format was generated using ANGSD v.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Evidence: First, we calculated local covariance matrices for each window using ANGSD ( 97 ) and PCAngsd ( 98 ).
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Ancient genomes reveal trans-Eurasian connections between the European Huns and the Xiongnu Empire. (PNAS 2025)

- DOI: 10.1073/pnas.2418485122 | PMCID: PMC11892651 | PMID: 39993190
- Version used: **0.910**
- Evidence: We performed DNA contamination analyses with ANGSD v0.910 ( 83 ) for the autosomal contamination levels (applicable only for males) and with Schmutzi ( 84 ) for the mitochondrial DNA contamination in both males and females.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [Cytoscape v3.9.1, Picard]

### Family relations of Moche elite burials on the North Coast of Peru (~500 CE): Analyses of the Señora de Cao and relatives. (PNAS 2025)

- DOI: 10.1073/pnas.2416321121 | PMCID: PMC11725780 | PMID: 39715432
- Evidence: We used recommended parameters in Contammix ( 53 ) to estimate mitochondrial contamination rates and estimated contamination on the X-chromosome for all biologically male individuals using ANGSD ( 54 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.6.1]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **0.940**
- Evidence: A consensus fasta file was generated with ANGSD v0.940 ( 55 ) with parameter -doFasta 2 (most common base), with filters for mapping quality (-minmapQ 30), base quality (-minQ 30), and minimum coverage per site of 10× (-setMinDepth 10).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### The Japanese Archipelago sheltered cave lions, not tigers, during the Late Pleistocene. (PNAS 2026)

- DOI: 10.1073/pnas.2523901123 | PMCID: PMC12890994 | PMID: 41587328
- Evidence: Mitochondrial genomes were assembled from mapped reads using ANGSD ( 81 ).
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [ANGSD, BWA v0.7.17, SAMtools v1.11] -> stage not stated [MAFFT v7.505, Python]

### Introgression dynamics of sex-linked chromosomal inversions shape the Malawi cichlid radiation. (Science 2025)

- DOI: 10.1126/science.adr9961 | PMCID: PMC7617772 | PMID: 40504893
- Evidence: We calculated the fixation index ( F ST ) and the population branch statistic between the benthic clades using ANGSD methods ( 85 ) and performed a genome-wide association (GWA) analysis for clade adherence with GEMMA ( 86 ).
- Full pipeline: quality control [SnpEff] -> alignment/mapping [BCFtools, BWA] -> differential/statistical testing [ANGSD, GEMMA]

