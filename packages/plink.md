# PLINK

- **Category:** statgen
- **Papers in survey:** 184
- **Journals:** PNAS (88), Nature (83), Cell (8), Science (5)
- **Years:** 2021 (19), 2022 (31), 2023 (24), 2024 (31), 2025 (49), 2026 (30)
- **Versions named:** 1.9 (47), 1.90b (18), 2.0 (9), 1.90 (9), 2.00a (3), 1.07 (3), 1.9b (2), 1.09 (1), 1.9.20200712 (1), 1.987 (1)
- **Pipeline stages it appears in:** variant calling (30), dimensionality reduction/clustering (22), differential/statistical testing (20), quality control (11), simulation/modelling (3), visualisation (3), quantification (2), alignment/mapping (2), normalisation (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Version used: **1.9**
- Evidence: ...iki/METAL_Documentation GWAMA Mägi et al., 2010 ; Mägi and Morris, 2010 https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-288 PLINK 1.9 Purcell et al., 2007 https://www.cog-genomics.org/plink/1.9/ COJO in GCTA Yang et al., 2011 , 2012 https://cnsgenomics.com/software/gcta/#COJO FUMA Watanabe et al., 2017 https://fuma.ctglab.nl LDHub Zheng et al., 2017 https://github.com/bul...
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Version used: **1.9**
- Evidence: ...tml PhyML v3.1 Guindon et al., 2010 http://www.atgc-montpellier.fr/phyml/ Picard tools v2.9.0 Broad Institute http://broadinstitute.github.io/picard/ PLINK 1.9 Purcell et al., 2007 https://zzz.bwh.harvard.edu/plink/plink2.shtml popHelper Francis, 2017 http://pophelper.com/ Samtools v.
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Version used: **2.0**
- Evidence: We used the PLINK 2.0 toolset to calculate the average proportion of alternative alleles for each individual.
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### Ancient genomes reveal origin and rapid trans-Eurasian migration of 7<sup>th</sup> century Avar elites. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.007 | PMCID: PMC9042794 | PMID: 35366416
- Version used: **1.9**
- Evidence: ...ATES MOSAIC v1.3 Salter-Townshend and Myers, 2019 https://maths.ucd.ie/∼mst/MOSAIC/ RFMix v2.03 Maples et al., 2013 https://github.com/slowkoni/rfmix PLINK v.
- Full pipeline: read trimming [BWA v0.7.12] -> stage not stated [ANGSD v0.910, GATK v3.5, PLINK v1.9, R v4.0, SAMtools v1.3, SHAPEIT]

### Limb development genes underlie variation in human fingerprint patterns. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.008 | PMCID: PMC8740935 | PMID: 34995520
- Version used: **1.9**
- Evidence: ... ; RRID: SCR_013499 R v3.6.1 The R Foundation https://www.r-project.org ; RRID: N/A PLS-PM The R CRAN https://github.com/gastonstat/plspm ; RRID: N/A PLINK v1.9 Purcell et al., 2007 https://www.cog-genomics.org/plink2 ; RRID: N/A SHAPEIT Delaneau et al., 2011 http://www.shapeitforum.com ; RRID: N/A IMPUTE2 Howie et al., 2009 https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ; RRID: SCR_013055 E...
- Full pipeline: stage not stated [Cytoscape, GCTA, IMPUTE2, ImageJ, PLINK v1.9, R v3.6, SHAPEIT]

### Influence of autozygosity on common disease risk across the phenotypic spectrum. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.028 | PMCID: PMC10580289 | PMID: 37757828
- Version used: **1.9**
- Evidence: 64 https://www.kingrelatedness.com/ PLINK 1.9 PLINK Working Group https://www.cog-genomics.org/plink/1.9/ plm Croissant and Millo 65 https://cran.r-project.org/web/packages/plm/index.html R 4.0.2 R Core Team https://www.r-project.org/ Resource availability Lead contact Further materials and requests may be directed to lead contact, Hilary Martin ( hcm@sanger.ac.uk ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [PLINK v1.9, R v4.0]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **1.9**
- Evidence: 112 http://www.popgen.dk/software/index.php/NgsAdmix evalAdmix v0.962 Garcia-Erill and Albrechtsen 113 https://github.com/GenisGE/evalAdmix PLINK v.1.9 Purcell et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.002 | PMCID: PMC11829167 | PMID: 39814019
- Version used: **1.9**
- Evidence: 17,608 SNPs present in all 49 cohorts, followed by the above LD pruning were used for robust relatedness testing across cohorts using PLINK v1.9 55 ; pairs of subjects with PIHAT > 0.2 were identified and one member of each pair removed at random, preferentially retaining cases over controls.
- Full pipeline: alignment/mapping [LDSC] -> variant calling [LDSC] -> dimensionality reduction/clustering [LDSC] -> stage not stated [Bioconductor, GCTA, MAGMA v1.08, PLINK v1.9]

### A chickpea genetic variation map based on the sequencing of 3,366 genomes. (Nature 2021)

- DOI: 10.1038/s41586-021-04066-1 | PMCID: PMC8612933 | PMID: 34759320
- Evidence: We defined two other SNP sets: (i) Set-A: only SNPs with <30% missing call, and biallelic calls, and (ii) Set-B: SNPs with less than 30% missing calls, biallelic calls, and LD-pruned using PLINK 33 v.1.90 (“--indep-pairphase 50 10 0.2” parameter).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BUSCO, PLINK, RAxML, VCFtools]

### The genomic origins of the Bronze Age Tarim Basin mummies. (Nature 2021)

- DOI: 10.1038/s41586-021-04052-7 | PMCID: PMC8580821 | PMID: 34707286
- Version used: **1.90**
- Evidence: For ADMIXTURE, we removed genetic markers with minor allele frequency lower than 1% and pruned for linkage disequilibrium using the -indep-pairwise 200 25 0.2 option in PLINK v.1.90 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools v1.7] -> stage not stated [ADMIXTURE v1.3.0, PLINK v1.90]

### Genome of a middle Holocene hunter-gatherer from Wallacea. (Nature 2021)

- DOI: 10.1038/s41586-021-03823-6 | PMCID: PMC8387238 | PMID: 34433944
- Version used: **1.9**
- Evidence: After file conversion with PLINK v.1.9 67 , we ran TreeMix v.1.12 42 setting the Denisovan genome 39 as the root and utilizing the parameters -k 150 and -global.
- Full pipeline: read trimming [BWA, SAMtools v1.3] -> alignment/mapping [BWA] -> variant calling [SAMtools v1.3] -> differential/statistical testing [ggplot2 v3.3.3] -> visualisation [ggplot2 v3.3.3] -> stage not stated [PLINK v1.9, QGIS]

### Mapping the human genetic architecture of COVID-19. (Nature 2021)

- DOI: 10.1038/s41586-021-03767-x | PMCID: PMC8674144 | PMID: 34237774
- Evidence: The recommended analysis tool was SAIGE, but studies also used other software such as PLINK 40 .
- Full pipeline: differential/statistical testing [LDSC v1.0.1] -> stage not stated [PLINK, R, SAIGE, TwoSampleMR]

### Genomic insights into the formation of human populations in East Asia. (Nature 2021)

- DOI: 10.1038/s41586-021-03336-2 | PMCID: PMC7993749 | PMID: 33618348
- Evidence: We carried out ADMIXTURE analysis in unsupervised mode 12 after pruning for linkage disequilibrium in PLINK 70 with parameters --indep-pairwise 200 25 0.4 which retained 256,427 SNPs.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [ANGSD, PLINK]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: The extent of linkage disequilibrium for the population was determined from SNPs 99 in PLINK 100 .
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: ... https://github.com/bulik/ldsc/ ; MEMO (rareGWAMA), https://github.com/dajiangliu/rareGWAMA/ ; Minimac3, https://genome.sph.umich.edu/wiki/Minimac3 ; PLINK, https://www.cog-genomics.org/plink/ ; R, https://www.r-project.org/ ; RATES, https://github.com/wangc29/RATES ; RVTESTS, https://github.com/zhanxw/rvtests/ ; SAIGE, https://github.com/weizhouUMICH/SAIGE ; SHAPEIT, http://mathgen.stats.ox.ac.uk...
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### A saturated map of common genetic variants associated with human height. (Nature 2022)

- DOI: 10.1038/s41586-022-05275-y | PMCID: PMC9605867 | PMID: 36224396
- Evidence: The resulting list contained 536 genes, of which 462 (Supplementary Table 11) are autosomal on the basis of annotation from PLINK ( https://www.cog-genomics.org/static/bin/plink/glist-hg19 ).
- Full pipeline: dimensionality reduction/clustering [MAGMA] -> differential/statistical testing [LDSC, R] -> stage not stated [GCTA, PLINK]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Version used: **1.90**
- Evidence: For the sex determination, the coverage data for the X and Y chromosomes was compared to the average coverage for the sample autosomes using PLINK v1.90 48 ( www.cog-genomics.org/plink/1.9/ ).
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### The Anglo-Saxon migration and the formation of the early English gene pool. (Nature 2022)

- DOI: 10.1038/s41586-022-05247-2 | PMCID: PMC9534755 | PMID: 36131019
- Evidence: 104 , 105 ) were pruned using PLINK 106 (v1.90b3.29). aDNA data were merged to this dataset, correcting for reference allele and strand flips.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA, Picard] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, SAMtools]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Evidence: Case–control association test We conducted GWAS of COVID-19 by using logistic regression of the imputed dosages of each of the variants on case–control status, using PLINK2 software (v2.00a3LM AVX2 Intel (6 July 2020)).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Grey wolf genomic history reveals a dual ancestry of dogs. (Nature 2022)

- DOI: 10.1038/s41586-022-04824-9 | PMCID: PMC9279150 | PMID: 35768506
- Version used: **1.90b**
- Evidence: Selection analyses Selection analysis was performed using PLINK (v1.90b5.2) 88 .
- Full pipeline: alignment/mapping [BWA, Clustal Omega v1.2.4, Picard, SAMtools v1.9] -> variant calling [BCFtools, GATK, Picard] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Version used: **2.0**
- Evidence: Principal component analysis was performed using PLINK (v.2.0) 77 using SNPs and indels from TGG1.1-332, and the first four principal components were used as covariates when estimating heritability.
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **1.9**
- Evidence: Individual genotypes were merged into a single VCF file using PLINK (v.1.9) 54 encompassing a total of 39.3 million variants including 31,094,663 SNPs and 8,266,390 INDELs.
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Version used: **1.9**
- Evidence: We then LD-pruned using PLINK v.1.9 with r 2 = 0.1 and in 500-kb windows.
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### Genetic associations of protein-coding variants in human disease. (Nature 2022)

- DOI: 10.1038/s41586-022-04394-w | PMCID: PMC8891017 | PMID: 35197637
- Evidence: We defined independent trait associations through linkage-disequilibrium-based ( r 2 = 0.1) clumping ±500 kb around the lead variants using PLINK 44 , excluding the HLA region (chr6:25.5-34.0Mb) which is treated as one region due to complex and extensive linkage-disequilibrium patterns.
- Full pipeline: differential/statistical testing [SAIGE v0.39] -> stage not stated [PLINK, REGENIE v1.0.6.7]

### Indigenous Australian genomes show deep structure and rich novel variation. (Nature 2023)

- DOI: 10.1038/s41586-023-06831-w | PMCID: PMC10733150 | PMID: 38093005
- Evidence: Genomic variation To assess variant sharing, the NCIG + PNG (masked) dataset was merged with the high-coverage 1000 Genomes dataset 18 (both underwent equivalent data processing, including variant quality score recalibration filtering at 99.8), taking the union of sites using the PLINK ‘--bmerge’ command 64 and removing sites that became triallelic using the ‘--exclude’ command.
- Full pipeline: variant calling [GATK v3.8] -> normalisation [R v5.1] -> dimensionality reduction/clustering [R v5.1, UMAP v0.2.7.0] -> stage not stated [ADMIXTURE v1.3, BCFtools, BEAST v2.6.0, PLINK, ggplot2]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Evidence: ADMIXTURE clustering analysis: Using PLINK2 61 , we first removed SNPs in high linkage disequilibrium using the command –indep-pairwise 50 5 0.5.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Plasma proteomic associations with genetics and health in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06592-6 | PMCID: PMC10567551 | PMID: 37794186
- Evidence: We defined primary associations through clumping ±1 Mb around the significant variants using PLINK 60 , excluding the HLA region (chromosome 6: 25.5–34.0 Mb), which is treated as one locus owing to complex and extensive LD patterns.
- Full pipeline: machine learning [R] -> stage not stated [PLINK, REGENIE v2.2.1, VEP]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Version used: **1.9**
- Evidence: Once the data had been merged, we performed principal component analysis (PCA) using PLINK (v.1.9) 57 and ensured that the three study populations (that is, AFB, EUB and ASH) overlapped with the corresponding 1KG populations, to exclude batch effects between genotyping platforms (Supplementary Fig.
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: Population diversity and structure We assessed the genetic relationships between accessions with PCA using all SNPs (121,459,674) with PLINK 110 (v.1.90).
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Northwest African Neolithic initiated by migrants from Iberia and Levant. (Nature 2023)

- DOI: 10.1038/s41586-023-06166-6 | PMCID: PMC10266975 | PMID: 37286608
- Version used: **1.9**
- Evidence: Individual heterozygosity was calculated from the number of variable positions divided by that of sequenced SNPs, using the –het command in PLINK 1.9 (ref.
- Full pipeline: variant calling [GATK v3.5.0] -> registration [GATK v3.5.0] -> dimensionality reduction/clustering [ADMIXTURE, QGIS] -> stage not stated [BCFtools, PLINK v1.9, SAMtools]

### Polygenic scoring accuracy varies across the genetic ancestry continuum. (Nature 2023)

- DOI: 10.1038/s41586-023-06079-4 | PMCID: PMC10284707 | PMID: 37198491
- Evidence: First, we filter the ATLAS-typed genotypes with plink2 by Mendel error rate (plink --me 1 1 –set-me-missing), founders (--filter-founders), minor allele frequency (–maf 0.15), genotype missing call rate (--geno 0.05) and Hardy–Weinberg equilibrium test P value (–hwe 0.001).
- Full pipeline: variant calling [PLINK] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [R]

### Recombination between heterologous human acrocentric chromosomes. (Nature 2023)

- DOI: 10.1038/s41586-023-05976-y | PMCID: PMC10172130 | PMID: 37165241
- Version used: **1.9**
- Evidence: We estimated linkage disequilibrium between pairs of markers within 70 kb by using PLINK v1.9 66 upon specification of haploid sets and retaining all values of r 2 > 0 (plot_ld_1.R).
- Full pipeline: alignment/mapping [Python, igraph] -> stage not stated [BEDTools, PLINK v1.9, R v3.6.3, ggplot2 v3.3.3, tidyverse v1.3.0]

### Entwined African and Asian genetic roots of medieval peoples of the Swahili coast. (Nature 2023)

- DOI: 10.1038/s41586-023-05754-w | PMCID: PMC10060156 | PMID: 36991187
- Evidence: 1 using PLINK2 49 .
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, R]

### Examining the role of common variants in rare neurodevelopmental conditions. (Nature 2024)

- DOI: 10.1038/s41586-024-08217-y | PMCID: PMC11634775 | PMID: 39567701
- Evidence: To define relatedness, we used a file generated by GEL consisting of a pairwise kinship matrix produced using the PLINK2 (refs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GCTA, LDSC] -> stage not stated [PLINK, VEP]

### Releasing a sugar brake generates sweeter tomato without yield penalty. (Nature 2024)

- DOI: 10.1038/s41586-024-08186-2 | PMCID: PMC11578880 | PMID: 39537922
- Evidence: We performed the genome-wide ROH analysis on the basis of the variation map using the PLINK program (version 1.90b6.21) 77 with the following parameters: --homozyg-kb 1,000 --homozyg-snp 10 --homozyg-window-het 3.
- Full pipeline: alignment/mapping [MAFFT v7.525] -> quantification [ImageJ] -> visualisation [ggplot2 v3.4.4] -> stage not stated [IQ-TREE, PLINK, Python, VCFtools v0.1.16]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **1.9**
- Evidence: PCA PCA on the whole dataset was performed using SNPs extracted from the global alignment file, following linkage disequilibrium pruning to remove linked SNPs (window size, 50 base pairs; step size, ten variants; r 2 threshold, 0.1), using the software PLINK (v.1.9) 60 .
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. (Nature 2024)

- DOI: 10.1038/s41586-024-07881-4 | PMCID: PMC11390480 | PMID: 39261618
- Version used: **1.9.20200712**
- Evidence: ROH We used hapROH 46 and PLINK v1.9.20200712 47 to detect ROH.
- Full pipeline: alignment/mapping [GATK, SAMtools] -> normalisation [ADMIXTURE] -> registration [GATK, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [Matplotlib v3.5.3, R, ggplot2 v3.3.2] -> stage not stated [ANGSD v0.930, PLINK v1.9.20200712]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **1.9**
- Evidence: The PCA for ethnic heterogeneity was done using PLINK (v.1.9) on whole-exome sequencing and whole-genome sequence data, with the 1000 Genomes Project phase 3 public database as a reference, using more than 15,000 exonic variants with a MAF of more than 0.01 and a call rate greater than 0.99.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### Position-dependent function of human sequence-specific transcription factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07662-z | PMCID: PMC11269187 | PMID: 39020164
- Version used: **2.00a**
- Evidence: The resulting VCF was converted into PLINK format using plink2 (v.2.00a2.3LM) 82 , retaining only SNPs with less than 50% of genotype calls missing, and a minor allele frequency greater than 0.05.
- Full pipeline: read trimming [Cutadapt v3.4, fastp] -> alignment/mapping [STAR v2.7.10a, fastp] -> variant calling [PLINK v2.00a] -> normalisation [DESeq2] -> stage not stated [BCFtools, HOMER]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Version used: **1.90**
- Evidence: The LD and haploblocks were calculated by PLINK (version 1.90 beta) 40 , 41 , the haplotype clustering was performed by HAPPE 14 .
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Version used: **1.90**
- Evidence: After converting genotype data to binary format, we used PLINK (v.1.90; http://pngu.mgh.harvard.edu/purcell/plink/ ) to filter variants with a minor allele frequency below 1% (--make-bed, --maf) and prune variants with a correlation threshold above 0.4 using a 200-bp sliding window and a step size of 25 (--indep-pairwise 200 25 0.4) 98 .
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Version used: **1.9b**
- Evidence: After basic quality control using PLINK (v1.9b, www.cog-genomics.org/plink/1.9/ ), 333 variants were removed due to missing genotype rate > 5%, 1,236 variants failed Hardy–Weinberg equilibrium test ( P values < 10 −8 ), and 18,702 variants had MAF < 1% in our cohort.
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Genome-wide characterization of circulating metabolic biomarkers. (Nature 2024)

- DOI: 10.1038/s41586-024-07148-y | PMCID: PMC10990933 | PMID: 38448586
- Version used: **2.0**
- Evidence: Associations between SNPs and metabolic traits were tested using PLINK 2.0.
- Full pipeline: differential/statistical testing [R] -> stage not stated [GCTA, PLINK v2.0, SAIGE, TwoSampleMR v0.5.1]

### Genetic drivers of heterogeneity in type 2 diabetes pathophysiology. (Nature 2024)

- DOI: 10.1038/s41586-024-07019-6 | PMCID: PMC10937372 | PMID: 38374256
- Version used: **1.9**
- Evidence: Clumps were formed around index variants, which were selected using a greedy algorithm in PLINK v.1.9 (ref.
- Full pipeline: differential/statistical testing [R] -> stage not stated [PLINK v1.9]

### 100 ancient genomes show repeated population turnovers in Neolithic Denmark. (Nature 2024)

- DOI: 10.1038/s41586-023-06862-3 | PMCID: PMC10781617 | PMID: 38200294
- Evidence: We computed D-statistics from genotypes in PLINK format using the qpdstat function implemented in the ADMIXTOOLS 2 R package 79 .
- Full pipeline: quality control [ADMIXTURE] -> variant calling [ADMIXTURE, BCFtools, PLINK, R, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [PLINK, R]

### Elevated genetic risk for multiple sclerosis emerged in steppe pastoralist populations. (Nature 2024)

- DOI: 10.1038/s41586-023-06618-z | PMCID: PMC10781639 | PMID: 38200296
- Evidence: We used PLINK 62 , excluding SNPs with MAF < 0.05 in the imputed panel.
- Full pipeline: quality control [ANGSD v0.931] -> alignment/mapping [BWA v0.7.17] -> quantification [ANGSD v0.931] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [PLINK, Picard, R, SAMtools v1.10]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Evidence: GWAS and meta-analysis The manipulation of human genotype datasets was conducted using PLINK (version alpha 2.1).
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### GDF15 linked to maternal risk of nausea and vomiting during pregnancy. (Nature 2024)

- DOI: 10.1038/s41586-023-06921-9 | PMCID: PMC10808057 | PMID: 38092039
- Version used: **1.90b**
- Evidence: 19: 18388612:C:G (GRCh38) and Pearson’s R was determined using the PLINK v.1.90b6.26/Swiss Army knife App via the UKB Research Access Platform, with the following parameters ‘--ld-window-r2 0 --ld-window 10000 --keep-allele-order --snp chr19:18388612:C:G --window 1000’.
- Full pipeline: alignment/mapping [GATK] -> variant calling [BCFtools, SAMtools] -> quantification [BCFtools, SAMtools, lme4] -> registration [Picard] -> stage not stated [PLINK v1.90b, R]

### The genetic legacy of the expansion of Bantu-speaking peoples in Africa. (Nature 2024)

- DOI: 10.1038/s41586-023-06770-6 | PMCID: PMC10794141 | PMID: 38030719
- Version used: **1.90b**
- Evidence: After merging all newly genotyped data and quality control steps using PLINK v.1.90b6.4 (ref.
- Full pipeline: quality control [PLINK v1.90b] -> variant calling [PLINK v1.90b, SHAPEIT, UMAP] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [Python, R]

### Ancient DNA from Shimao city records kinship practices in Neolithic China. (Nature 2025)

- DOI: 10.1038/s41586-025-09799-x | PMCID: PMC12711557 | PMID: 41299168
- Evidence: Before the admixture analysis, we pruned genotypes with high linkage disequilibrium ( r 2 > 0.4) using PLINK (version v.1.90) 65 and the parameters ‘-indep-pairwise 200 25 0.4’ were applied for SNP filtering, leaving 597,573 SNPs.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.5.10] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Version used: **2.0**
- Evidence: For computational efficiency, PCA and the top 10 PCs were generated using the fastPCA version (--pca approx) in PLINK 2.0.
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### Population-specific polygenic risk scores for people of Han Chinese ancestry. (Nature 2025)

- DOI: 10.1038/s41586-025-09350-y | PMCID: PMC12675292 | PMID: 41094136
- Evidence: In the GWAS set, we selected an unrelated subset ( n = 248,754) to perform GWAS using a generalized linear model with PLINK2, and we conducted 1:10 age, sex-matching for the traits with imbalanced case/control ratio (less than 1/20).
- Full pipeline: quantification [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, LDSC] -> differential/statistical testing [LDSC, PLINK, SAIGE] -> stage not stated [ANNOVAR, R]

### Polygenic and developmental profiles of autism differ by age at diagnosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09542-6 | PMCID: PMC12571882 | PMID: 41034588
- Evidence: The GWAS was done for unrelated individuals of European ancestry, with the first ten genetic PCs included as covariates using logistic regression as provided in PLINK.
- Full pipeline: differential/statistical testing [PLINK, lme4 v1.1.27.1] -> stage not stated [GCTA, LDSC, lavaan v0.6]

### A haplotype-based evolutionary history of barley domestication. (Nature 2025)

- DOI: 10.1038/s41586-025-09533-7 | PMCID: PMC12629985 | PMID: 40993384
- Evidence: Before running ADMIXTURE, the SNP set was thinned with PLINK 45 (v1.9) using the parameters ‘--indep-pairwise 50 10 0.1’.
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [BCFtools v1.15.1, DeepVariant v1.6.0, SnpEff v4.3t, minimap2 v2.24] -> visualisation [R v3.5.1] -> stage not stated [ADMIXTURE, PLINK, SAMtools v1.16.1]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Evidence: Population structure analysis To estimate the population ancestry proportions of hybrids, we selected M. ibericus and M. structor individuals from variant files (same variant filtering as for SNP heterozygosity computing) and then produced a bed file using PLINK 86 (v.1.90b6.21) before using fastStructure 16 (v.1.0) with k = 2.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Evidence: Variants with minor allele frequency of 0.01 were removed and PLINK was used for linkage disequilibrium (LD) pruning with a window size of 200, a step size of 5 and an R 2 threshold of 0.5.
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Version used: **1.90b**
- Evidence: The directly genotyped dataset was used with additional quality control filters using PLINK (v.1.90b6.21, https://www.cog-genomics.org/plink/1.9/ ) 47 that included: autosomes, minor allele frequency ≥ 5%, not present in high linkage disequilibrium (LD) regions and LD pruning using a R 2 threshold of 0.2 with a window size of 50 markers and a step size of 5 markers.
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Parent-of-origin effects on complex traits in up to 236,781 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-09357-5 | PMCID: PMC12527933 | PMID: 40770099
- Version used: **1.90b**
- Evidence: Methods UK Biobank genotype processing We used the UK Biobank Axiom Array data provided in PLINK format 39 and converted it to variant call format (VCF) using PLINK (v1.90b5) 40 .
- Full pipeline: quality control [BCFtools v1.8] -> variant calling [PLINK v1.90b] -> dimensionality reduction/clustering [igraph] -> stage not stated [R, REGENIE v3.2.9]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **1.90b**
- Evidence: A distance matrix was calculated with PLINK (v1.90b6.9) 76 using the parameters ‘--distance 1-ibs flat-missing square’ and transformed into a neighbour-joining tree with FASTME (version 2.1.5) 77 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Whole-genome ancestry of an Old Kingdom Egyptian. (Nature 2025)

- DOI: 10.1038/s41586-025-09195-5 | PMCID: PMC12367555 | PMID: 40604286
- Version used: **1.9**
- Evidence: The remaining 111,208 positions were subsequently pruned for SNPs in strong linkage disequilibrium using PLINK v.1.9 (ref.
- Full pipeline: quality control [ANGSD v0.933] -> variant calling [BCFtools v1.19] -> dimensionality reduction/clustering [ADMIXTURE v1.2] -> stage not stated [PLINK v1.9]

### Ancient DNA reveals the prehistory of the Uralic and Yeniseian peoples. (Nature 2025)

- DOI: 10.1038/s41586-025-09189-3 | PMCID: PMC12342343 | PMID: 40604287
- Evidence: Genotype files in PLINK format for the 229 modern individuals for whom we newly report SNP array can be found at secondary accession ERZ26790638.
- Full pipeline: variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [ANGSD v0.923, QGIS v3.40.6, R]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Version used: **2.0**
- Evidence: This dataset can be accessed via the Resources section on the PLINK 2.0 website ( Resources — PLINK 2.0 (cog-genomics.org) ).
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Sequence diversity lost in early pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-025-09031-w | PMCID: PMC12176622 | PMID: 40399685
- Evidence: Markers were pruned for pairs in strong linkage disequilibrium by excluding long-range high-linkage-disequilibrium regions 56 and running PLINK 57 v.1.90b6.15 --indep-pairwise 200 25 0.4.
- Full pipeline: alignment/mapping [BWA, Picard, R] -> variant calling [Manta v1.6.0] -> differential/statistical testing [R] -> machine learning [ADMIXTURE] -> stage not stated [PLINK, VEP]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: Initially, SNPs were pruned on the basis of linkage disequilibrium (LD) using PLINK 69 , with a window size of 10 kb, a window step of one SNP, and an r 2 threshold of 0.8.
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Punic people were genetically diverse with almost no Levantine ancestors. (Nature 2025)

- DOI: 10.1038/s41586-025-08913-3 | PMCID: PMC12226237 | PMID: 40269169
- Evidence: This pruning was done by applying PLINK V1.9 57 with options --indep-pairwise 200 25 0.4 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK, R, SAMtools]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: To determine the phylogenetic relationships of three populations, including wild rice and cultivated rice (Supplementary Tables 14 , 16 and 17 ), we first converted the SNP VCF files into tfam format using PLINK 116 (v.1.90b6.9 64-bit).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Translational genomics of osteoarthritis in 1,962,069 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-08771-z | PMCID: PMC12119359 | PMID: 40205036
- Evidence: (1) For each phenotype, we performed clumping using PLINK 56 together with a significance threshold of P ≤ 1.3 × 10 −8 , 2 Mb window around each index variants and linkage disequilibrium (LD) threshold of 0.1.
- Full pipeline: quality control [BCFtools v1.13, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [Enrichr, GCTA, PLINK]

### Ancient DNA from the Green Sahara reveals ancestral North African lineage. (Nature 2025)

- DOI: 10.1038/s41586-025-08793-7 | PMCID: PMC12043513 | PMID: 40175549
- Evidence: Modern and ancient groups were subsetted from the HO-based dataset, converted to PLINK format, and transposed to pseudohaploid format to reduce artificial drift.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, MAFFT] -> variant calling [SAMtools v1.3] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> stage not stated [PLINK, tidyverse v1.3.0]

### Spatially resolved mapping of cells associated with human complex traits. (Nature 2025)

- DOI: 10.1038/s41586-025-08757-x | PMCID: PMC12095064 | PMID: 40108460
- Evidence: We used PLINK (V1.90) 69 to associate SNPs with the simulated phenotypes with the first ten principal components, derived from SNPs, fitted as covariates.
- Full pipeline: alignment/mapping [R] -> variant calling [GCTA] -> normalisation [Scanpy] -> dimensionality reduction/clustering [PLINK, Seurat, clusterProfiler] -> differential/statistical testing [MAGMA] -> simulation/modelling [PLINK] -> stage not stated [LDSC]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Version used: **1.9**
- Evidence: Quality control was performed by checking the exome metrics summarizing the target-base coverage, genotypic sex (PLINK v.1.9), relationship inference (KING v.2.2.7) and contamination (Picard v.2.25.6).
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: We used the CAVIAR 84 to quantify the causal posterior probability (CPP) for each associated k -mer within the interval by integrating GWAS z -scores with a local LD correlation matrix calculated using PLINK2 using the --r-unphased square option 85 .
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### The evolutionary history and unique genetic diversity of Indigenous Americans. (Nature 2026)

- DOI: 10.1038/s41586-026-10406-w | PMCID: PMC13149005 | PMID: 42020734
- Version used: **1.9**
- Evidence: Using PLINK v.1.9 (ref.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK, VEP] -> normalisation [VEP] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK v1.9, R, SnpEff]

### Dynamics of genetic and somatic trade-offs in ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10407-9 | PMCID: PMC13253337 | PMID: 42020758
- Evidence: ...librium-based principal components (principal component instrumental variables) 116 that were evaluated using the 1000 Genomes Project panel 117 with PLINK 118 v1.90b6.21.
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.3.4.1] -> variant calling [BCFtools, R v4.0] -> dimensionality reduction/clustering [PLINK, TwoSampleMR v0.6.2, clusterProfiler] -> stage not stated [SAMtools v1.6]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Evidence: Initially, we clumped SNPs with PLINK using a P-value <10 −3 , r 2 <0.05, and a 500 kb window.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Version used: **1.9**
- Evidence: Genotype quality control was performed using PLINK (v1.9) 60 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Population-scale repeat expansions elucidate disease risk and brain atrophy. (Nature 2026)

- DOI: 10.1038/s41586-026-10345-6 | PMCID: PMC13190288 | PMID: 41951733
- Evidence: IBD estimates were calculated among individuals within the same ancestral superclass that was determined in ancestry predictions as mentioned above using PLINK with a minimum PI_HAT cut-off of 0.1875 to capture out to second-degree relationships, which generates ancestry–version IBD estimates.
- Full pipeline: variant calling [R, REGENIE v3.2] -> registration [FSL v6.0.7.8] -> differential/statistical testing [REGENIE v3.2] -> stage not stated [FreeSurfer v7.3.2, PLINK, dcm2niix]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Evidence: The remaining SNVs were further pruned to remove sites in LD using PLINK2 (ref.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **1.90b**
- Evidence: To generate an approximately independent set of markers, we removed variants with MAF < 0.05, more than 50% missingness, and applied LD-based pruning with a window size of 50 SNPs, step size of 5 SNPs and a r 2 threshold of 0.5 in PLINK (v.1.90b6.12) 100 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Evidence: For compatibility with regenie step 2, the provided dosages were converted to plink2 pgen-files.
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Version used: **1.9**
- Evidence: Ancestry estimation was performed using PLINK v.1.9, and ADMIXTURE 48 v.1.3.0 for unsupervised analysis together with the superpopulations of the 1000 Genomes dataset 49 .
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### Phenome-wide analysis of copy number variants in 470,727 UK Biobank genomes. (Nature 2026)

- DOI: 10.1038/s41586-025-10087-x | PMCID: PMC13083251 | PMID: 41639462
- Evidence: We used PLINK 58 to compute Hardy–Weinberg statistics for each CNV.
- Full pipeline: dimensionality reduction/clustering [REGENIE v3.5] -> differential/statistical testing [PLINK] -> stage not stated [R]

### A cross-population compendium of gene-environment interactions. (Nature 2026)

- DOI: 10.1038/s41586-025-10054-6 | PMCID: PMC12999510 | PMID: 41606330
- Version used: **2.00a**
- Evidence: ...esearch/tree/master/enformer ), shapeit4 v.4.1.2 ( https://odelaneau.github.io/shapeit4/ ), minimac4 v.1.0.1 ( https://github.com/statgen/Minimac4 ), plink2 v.2.00a6LM ( https://www.cog-genomics.org/plink/2.0/ ), king v.2.2.5 ( https://www.kingrelatedness.com/ ), FINEMAP v.1.4.2 ( http://www.christianbenner.com/ ), GenomeStudio v.2.0.5 ( https://support.illumina.com/downloads/genomestudio-2-0.html...
- Full pipeline: variant calling [IMPUTE2] -> dimensionality reduction/clustering [R, Seurat v4.3.0.1, UMAP] -> differential/statistical testing [MAGMA] -> stage not stated [BCFtools, LDSC v1.0.0, PLINK v2.00a]

### Human and bacterial genetic variation shape oral microbiomes and health. (Nature 2026)

- DOI: 10.1038/s41586-025-10037-7 | PMCID: PMC12979206 | PMID: 41606319
- Version used: **2.00a**
- Evidence: We performed a series of QC steps on the joint call set, starting by converting half-calls to missing and then excluding variants with >10% missingness using plink2 (v.2.00a3.6LM).
- Full pipeline: quality control [DeepVariant v1.3.0, PLINK v2.00a] -> alignment/mapping [DeepVariant v1.3.0] -> variant calling [DeepVariant v1.3.0] -> differential/statistical testing [LDSC, R] -> visualisation [ChimeraX v1.9] -> stage not stated [AlphaFold, Bowtie2, MetaPhlAn v4.0.6, SAMtools v1.15.1]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **1.09**
- Evidence: Sample identity was verified using the identity by descent algorithm from PLINK (v.1.09) 114 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Evidence: We pruned these variant sets using PLINK2 (--indep-pairwise 1000 100 0.8) as input to REGENIE’s step1 analyses.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Version used: **1.90b**
- Evidence: To identify independently associated GWAS variants, we used PLINK (v1.90b5.3) 86 with the –clump flag, a P value threshold of 5 × 10 −8 , a linkage disequilibrium threshold of r 2 = 0.01 and a physical distance threshold of 10 Mb.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### Mapping the genetic landscape across 14 psychiatric disorders. (Nature 2026)

- DOI: 10.1038/s41586-025-09820-3 | PMCID: PMC12779569 | PMID: 41372416
- Version used: **1.9**
- Evidence: Significant loci were identified using the clumping functionality in PLINK v.1.9 with an r 2 threshold of 0.1 and a 3,000 kb window.
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [MAGMA, PLINK v1.9, R]

### Homo sapiens-specific evolution unveiled by ancient southern African genomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09811-4 | PMCID: PMC12872451 | PMID: 41339558
- Version used: **1.9**
- Evidence: The final genome-wide dataset was filtered using PLINK v.1.9 ( www.cog-genomics.org/plink/1.9 ) for a minimum allele frequency of 10% and linkage-disequilibrium pruned using command --indep-pairwise 50 5 0.4.
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK v1.9, SAMtools, SnpEff]

### Estimation and mapping of the missing heritability of human phenotypes. (Nature 2026)

- DOI: 10.1038/s41586-025-09720-6 | PMCID: PMC12851931 | PMID: 41225014
- Evidence: In total, 325,484 common variants and 2,435,866 rare variants were retained and 30 genotypic principal components for each bin (that is, 8 × 30 = 240 principal components in total) were computed in the set of unrelated samples using the randomized matrix algorithm implemented in PLINK2 (ref.
- Full pipeline: variant calling [PLINK] -> dimensionality reduction/clustering [PLINK] -> differential/statistical testing [LDSC] -> stage not stated [R, REGENIE]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Version used: **1.9**
- Evidence: Input data was prepared using PLINK (v 1.9) 108 .
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: MDS analysis was preformed using PLINK 59 ( www.cog-genomics.org/plink/1.9/ ) with –maf=0.05 and a maximum of 70% missing data.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Invasion genomics uncover contrasting scenarios of genetic diversity in a widespread marine invader. (PNAS 2021)

- DOI: 10.1073/pnas.2116211118 | PMCID: PMC8713979 | PMID: 34911766
- Version used: **1.90b**
- Evidence: Genetic diversity and population structure analyses were conducted using filtered SNP datasets following linkage disequilibrium-based variant pruning implemented in PLINK version 1.90b3.42 ( 54 ), which produces a pruned subset of markers in approximate linkage equilibrium.
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7.15, Trimmomatic v0.36] -> alignment/mapping [BWA v0.7.15, Picard v2.6.0] -> variant calling [BCFtools v1.9] -> stage not stated [PLINK v1.90b, VCFtools v0.1.14]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: SNPs with LD were pruned (–indep-pairwise 50 10 0.0575) using PLINK software ( 85 ).
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### False discovery rate control in genome-wide association studies with population structure. (PNAS 2021)

- DOI: 10.1073/pnas.2105841118 | PMCID: PMC8501795 | PMID: 34580220
- Evidence: To eliminate the redundancy in the findings, variants associated with the phenotype and highly correlated with one another are “clumped” into distinct groups, utilizing procedures such as that implemented in PLINK ( 26 ).
- Full pipeline: variant calling [SHAPEIT] -> stage not stated [PLINK]

### A model and test for coordinated polygenic epistasis in complex traits. (PNAS 2021)

- DOI: 10.1073/pnas.1922305118 | PMCID: PMC8053945 | PMID: 33833052
- Evidence: For binary traits, we used logistic regression and a computationally efficient approximate Firth correction ( 90 , 91 ) using “cc-residualize no-firth” in plink2.
- Full pipeline: differential/statistical testing [PLINK]

### The impact of identity by descent on fitness and disease in dogs. (PNAS 2021)

- DOI: 10.1073/pnas.2019116118 | PMCID: PMC8072400 | PMID: 33853941
- Evidence: The Fitak et al. data ( 9 ) were lifted over to CanFam3.1, then merged with Hayward et al. data ( 10 ) using PLINK ( 49 ).
- Full pipeline: stage not stated [BEDTools, PLINK, R]

### Multiple migrations to the Philippines during the last 50,000 years. (PNAS 2021)

- DOI: 10.1073/pnas.2026132118 | PMCID: PMC8020671 | PMID: 33753512
- Version used: **1.9**
- Evidence: Measures of basic statistics and measures of genetic diversity, including runs of homozygosity and inbreeding coefficient, were computed using the–het,–homozyg, and–ibc functions of PLINK v1.9 ( 40 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [PLINK v1.9] -> visualisation [ADMIXTURE v1.3]

### Placental genomic risk scores and early neurodevelopmental outcomes. (PNAS 2021)

- DOI: 10.1073/pnas.2019789118 | PMCID: PMC7896349 | PMID: 33558239
- Version used: **1.07**
- Evidence: Quality control was performed using PLINK (version 1.07) ( 44 ) as reported elsewhere ( 11 ).
- Full pipeline: quality control [PLINK v1.07] -> alignment/mapping [SPM] -> differential/statistical testing [SPM, limma] -> stage not stated [R]

### Ancient DNA from Guam and the peopling of the Pacific. (PNAS 2021)

- DOI: 10.1073/pnas.2022112118 | PMCID: PMC7817125 | PMID: 33443177
- Evidence: Pruning of SNPs in linkage disequilibrium (LD) was done using the PLINK tool ( 87 ) with the following settings: –indep- pairwise 200 25 0.4 ( 88 ).
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, R, data.table, pheatmap, tidyverse]

### Sunlight exposure exerts immunomodulatory effects to reduce multiple sclerosis severity. (PNAS 2021)

- DOI: 10.1073/pnas.2018457118 | PMCID: PMC7817192 | PMID: 33376202
- Version used: **1.90**
- Evidence: Briefly, genotyping was performed using an Illumina OmniExpress chip and QC was performed in PLINK v1.90.
- Full pipeline: quality control [PLINK v1.90] -> variant calling [PLINK v1.90] -> differential/statistical testing [R v3.6, lme4] -> visualisation [ggplot2] -> stage not stated [edgeR, kallisto]

### The evolution of skin pigmentation-associated variation in West Eurasia. (PNAS 2021)

- DOI: 10.1073/pnas.2009227118 | PMCID: PMC7817156 | PMID: 33443182
- Version used: **1.90b**
- Evidence: To identify genome-wide significant and independent SNPs, we performed clumping using PLINK v1.90b6.6 ( 89 ) with 1000 Genomes GBR as an LD reference panel (--clump-p1 5 × 10 −8 --clump-r2 0.05 --clump-kb 250), and followed up with clumping based on physical distance to exclude SNPs within 100 kb of each other.
- Full pipeline: stage not stated [ADMIXTURE, PLINK v1.90b]

### A global analysis of matches and mismatches between human genetic and linguistic histories. (PNAS 2022)

- DOI: 10.1073/pnas.2122084119 | PMCID: PMC9704691 | PMID: 36399547
- Evidence: Dataset screening and F ST distances are calculated with PLINK ( 45 ).
- Full pipeline: differential/statistical testing [R] -> visualisation [R] -> stage not stated [PLINK]

### Impact of cultural and genetic structure on food choices along the Silk Road. (PNAS 2022)

- DOI: 10.1073/pnas.2209311119 | PMCID: PMC9704696 | PMID: 36375050
- Version used: **1.9**
- Evidence: We removed related individuals by excluding one of each individual pair showing an identity by descent value higher than 0.25 with PLINK 1.9 ( 75 ).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SciPy, lme4] -> differential/statistical testing [lme4] -> machine learning [ADMIXTURE] -> stage not stated [PLINK v1.9, R, vegan]

### Metabolome-wide association study on &lt;i&gt;ABCA7&lt;/i&gt; indicates a role of ceramide metabolism in Alzheimer's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2206083119 | PMCID: PMC9618092 | PMID: 36269859
- Evidence: GWAS was performed using PLINK2 ( 59 ).
- Full pipeline: stage not stated [Bioconductor, FreeSurfer, PLINK]

### Pan-mitogenomics reveals the genetic basis of cytonuclear conflicts in citrus hybridization, domestication, and diversification. (PNAS 2022)

- DOI: 10.1073/pnas.2206076119 | PMCID: PMC9618123 | PMID: 36260744
- Version used: **1.90b**
- Evidence: Also, we conducted the PCA for cytoplasmic genomes by using PLINK v1.90b6.21 ( 64 ) and plotted the results with the R package.
- Full pipeline: dimensionality reduction/clustering [PLINK v1.90b, R] -> differential/statistical testing [Python, ggplot2] -> visualisation [PLINK v1.90b, R, ggplot2] -> stage not stated [GEMMA v0.98.5, IQ-TREE v2.0, SnpEff v5.1]

### The diverse genetic origins of a Classical period Greek army. (PNAS 2022)

- DOI: 10.1073/pnas.2205272119 | PMCID: PMC9564095 | PMID: 36191217
- Evidence: We pruned SNPs in linkage disequilibrium with one another with PLINK using the parameter –indep-pairwise 200 25 0.4.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.6.1] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Version used: **1.07**
- Evidence: Genetic association of the tag variant rs75356281 with M values (back of the hand, underarm, and buttock) was conducted by utilizing PLINK v1.07 ( 83 ) with age, sex, and altitude taken as covariates.
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### Using neuroimaging genomics to investigate the evolution of human brain structure. (PNAS 2022)

- DOI: 10.1073/pnas.2200638119 | PMCID: PMC9546597 | PMID: 36161899
- Evidence: To identify genome-wide significant loci associated with any of our neuroimaging traits, we performed clumping with PLINK ( 72 ), and selected SNPs that are in LD ( r 2 > 0.6) with clumped GWAS SNPs.
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [LDSC] -> stage not stated [FreeSurfer, PLINK, R, ggplot2]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **1.9**
- Evidence: A neighbor-joining tree was constructed using the APE ( 96 ) package from the pair-wise identical-by-state distance matrix calculated using PLINK 1.9 ( 97 ) and based on autosomal SNPs.
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### A quantile integral linear model to quantify genetic effects on phenotypic variability. (PNAS 2022)

- DOI: 10.1073/pnas.2212959119 | PMCID: PMC9522331 | PMID: 36122202
- Evidence: To determine the number of independent significant vQTLs, we clumped the summary statistics for each method in PLINK2 ( 45 ) (–clump option with parameters –clump-p1 5.0e-8 –clump-p2 5.0e-8 –clump-r2 0.01 and –clump-kb 5000) by using the analytic sample in UK Biobank as the LD reference panel.
- Full pipeline: quantification [LDSC] -> differential/statistical testing [LDSC, PLINK]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: SNPs were pruned using P- value informed clumping in PLINK ( 62 ), with a cutoff of r 2 = 0.1 within a 500-kb window.
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### Comparative genomics uncovers the evolutionary history, demography, and molecular adaptations of South American canids. (PNAS 2022)

- DOI: 10.1073/pnas.2205986119 | PMCID: PMC9407222 | PMID: 35969758
- Evidence: We examined genome-wide site heterozygosity and quantified the extent of ROH in SA canids using PLINK ( 113 ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [PLINK] -> stage not stated [R]

### Microbiome-associated human genetic variants impact phenome-wide disease risk. (PNAS 2022)

- DOI: 10.1073/pnas.2200551119 | PMCID: PMC9245617 | PMID: 35749358
- Evidence: Haplotype blocks were extracted using PLINK ( 125 ) version 1.9b_5.2 using the standard “blocks” command.
- Full pipeline: variant calling [PLINK] -> visualisation [ComplexHeatmap v2.12] -> stage not stated [R, SAIGE, VEP]

### Revealing the recent demographic history of Europe via haplotype sharing in the UK Biobank. (PNAS 2022)

- DOI: 10.1073/pnas.2119281119 | PMCID: PMC9233301 | PMID: 35696575
- Evidence: With this dataset, we performed initial PCA using PLINK ( 28 , 29 ) to identify ancestry outliers.
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [ADMIXTURE, PLINK, R] -> differential/statistical testing [R, ggplot2, igraph]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Version used: **1.9**
- Evidence: A dataset of common biallelic SNPs was generated using PLINK (v1.9) with variant filtering criteria of an in-cohort minor allele frequency (MAF) ≥ 0.05, genotype missingness less than 5%, and Hardy–Weinberg P value cutoff of 1E-06.
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### Population interconnectivity over the past 120,000 years explains distribution and diversity of Central African hunter-gatherers. (PNAS 2022)

- DOI: 10.1073/pnas.2113936119 | PMCID: PMC9173804 | PMID: 35580185
- Evidence: The data were then pruned for MAF <0.05 with PLINK ( 68 ).
- Full pipeline: stage not stated [PLINK]

### An integrative skeletal and paleogenomic analysis of stature variation suggests relatively reduced health for early European farmers. (PNAS 2022)

- DOI: 10.1073/pnas.2106743119 | PMCID: PMC9169634 | PMID: 35389750
- Version used: **1.9**
- Evidence: For our data, polygenic height scores were estimated using PLINK 1.9 ( 142 ) with clumping of independent SNPs.
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SnpEff] -> registration [GATK] -> stage not stated [PLINK v1.9, Picard]

### A generalist-specialist trade-off between switchgrass cytotypes impacts climate adaptation and geographic range. (PNAS 2022)

- DOI: 10.1073/pnas.2118879119 | PMCID: PMC9169841 | PMID: 35377798
- Version used: **1.9**
- Evidence: For LD analysis, r 2 was calculated in PLINK v1.9 ( 93 ) and VCFtools ( 85 ) between hiF st SNPs across all samples and within each of the three gene pools using diploid-only genotypes.
- Full pipeline: alignment/mapping [BWA] -> variant calling [ADMIXTURE, PLINK v1.9, SAMtools, VCFtools] -> registration [GATK v3.0, Picard] -> stage not stated [R]

### Genetics, leadership position, and well-being: An investigation with a large-scale GWAS. (PNAS 2022)

- DOI: 10.1073/pnas.2114271119 | PMCID: PMC8944770 | PMID: 35286190
- Version used: **1.07**
- Evidence: Independent significant variants and their surrounding genomic loci were identified using LD clumping in PLINK version 1.07 ( https://zzz.bwh.harvard.edu/plink/download.shtml ).
- Full pipeline: alignment/mapping [ANNOVAR] -> differential/statistical testing [LDSC v1.0.1] -> stage not stated [METAL, PLINK v1.07]

### Leveraging cell-type-specific regulatory networks to interpret genetic variants in abdominal aortic aneurysm. (PNAS 2022)

- DOI: 10.1073/pnas.2115601119 | PMCID: PMC8740683 | PMID: 34930827
- Version used: **1.9**
- Evidence: For 268 AAA patients and 133 healthy controls, we applied PLINK 1.9 ( 24 ) to obtain the frequency for each allele.
- Full pipeline: stage not stated [PLINK v1.9]

### Genomic loci influence patterns of structural covariance in the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2300842120 | PMCID: PMC10756284 | PMID: 38127979
- Evidence: In GWAS, we performed a linear regression for each PSC and included the same covariates as in the heritability estimates using PLINK ( 63 ).
- Full pipeline: differential/statistical testing [FUMA, MAGMA, PLINK] -> stage not stated [GCTA, GSEA, LDSC]

### The impact of COVID-19 on a college freshman sample reveals genetic and nongenetic forms of susceptibility and resilience to stress. (PNAS 2023)

- DOI: 10.1073/pnas.2305779120 | PMCID: PMC10710019 | PMID: 38011555
- Evidence: Briefly, we followed previously published methods and workflows for quality checking and LD-based pruning in PLINK: The sample call rate was 95%, the SNP call rate was 99%, the Minor Allele Frequency was 0.005, the Hardy–Weinberg equilibrium was 0.00001, and the LD-based pruning window size was 50 with a step size of 5 ( 10 ).
- Full pipeline: quality control [PLINK] -> variant calling [PLINK] -> differential/statistical testing [R v4.2] -> stage not stated [IMPUTE2]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Evidence: LD pruning was performed with PLINK ( 75 ) (version 1.9) using a window size of 10 kb and an r 2 threshold of 0.5.
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### Increased homozygosity due to endogamy results in fitness consequences in a human population. (PNAS 2023)

- DOI: 10.1073/pnas.2309552120 | PMCID: PMC10614605 | PMID: 37847737
- Evidence: ( 33 ), which included using PLINK to filter for missingness greater than 5%, a minor allele frequency less than or equal to 1%, and a Hardy–Weinberg equilibrium exact test with a P -value below 0.0001.
- Full pipeline: differential/statistical testing [brms] -> stage not stated [PLINK]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Version used: **2.0**
- Evidence: Kinship coefficients were estimated with the “--make-king-table” command in PLINK v.2.0 ( 68 ), whose output reflects the proportion of SNPs with identical states (IBS0, identity by state zero) between individuals.
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Version used: **1.90**
- Evidence: To ensure that loci were independent, linkage disequilibrium (r 2 ) among SNP was calculated using PLINK (v1.90) ( 80 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### Natural genetic variation in the pheromone production of <i>C. elegans</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2221150120 | PMCID: PMC10293855 | PMID: 37339205
- Version used: **1.9**
- Evidence: We used BCFtools ( 45 ) to filter variants below a 5% minor allele frequency and variants with missing genotypes and used PLINK v1.9 ( 46 , 47 ) to prune genotypes using LD.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools, PLINK v1.9] -> stage not stated [GCTA, R, SnpEff]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Version used: **1.9**
- Evidence: ROH were called with a minimum length of 500 kb and a minimum of 50 SNPs using the --homozyg function in PLINK v1.9 ( 101 ) and the following parameters: --homozyg-window-snp 50 --homozyg-snp 50 --homozyg-kb 500 --homozyg-gap 1000 --homozyg-density 50 --homozyg-window-missing 5 and --homozyg-window-het 3.
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Evidence: After converting the BGEN format to PLINK binary format, additional standard quality check procedures were carried out, including removal of single nucleotide polymorphisms (SNPs) with low imputation quality scores, filtering out individuals with more than 10% missingness, SNPs with more than 5% missingness, and SNPs failing the Hardy-Weinberg equilibrium test at P = 1*10 −6 .
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Evidence: Variant tables in VCF format were processed with PLINK ( 76 ) using option --aec, and PCA results were plotted in R using ggplot2 ( 77 ).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Divergent sensory and immune gene evolution in sea turtles with contrasting demographic and life histories. (PNAS 2023)

- DOI: 10.1073/pnas.2201076120 | PMCID: PMC9962930 | PMID: 36749728
- Evidence: ANGSD was parameterized to output files configured for use as input for the PLINK ROH analysis ( 129 ).
- Full pipeline: alignment/mapping [BCFtools, SAMtools] -> variant calling [BCFtools, GATK, SAMtools] -> stage not stated [ANGSD, BUSCO, OrthoFinder, PLINK]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: To convert from vcf to bed and ped formats, we used PLINK ( 93 ) and VCFtools ( 91 ).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### Community-engaged ancient DNA project reveals diverse origins of 18th-century African descendants in Charleston, South Carolina. (PNAS 2023)

- DOI: 10.1073/pnas.2201620120 | PMCID: PMC9934026 | PMID: 36623185
- Evidence: The Human Origins Panel ( 62 ), 1000 Genomes Panel ( 35 ), and a custom panel of African reference populations ( 63 – 65 ) were assembled and filtered for variant calling using PLINK ( 66 ) ( Dataset S5 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.9] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9]

### The genetic origins and impacts of historical Papuan migrations into Wallacea. (PNAS 2024)

- DOI: 10.1073/pnas.2412355121 | PMCID: PMC11670103 | PMID: 39689173
- Version used: **1.987**
- Evidence: This final set of 848 individuals was filtered for SNPs missing in more than 5% of the combined samples, or having a minor allele frequency less than 1% across all samples, using PLINK v.1.987; ( 76 ), resulting in a set of 3.77 M SNPs available for further analysis.
- Full pipeline: read trimming [BWA v0.7.17, fastp] -> alignment/mapping [BWA v0.7.17, GATK, SAMtools v1.9] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE, R] -> stage not stated [PLINK v1.987]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: Distance matrices were calculated for each of the three genomes using PLINK ( 101 ), and the ape package in R was used to produce neighbor-joining trees ( 102 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Genetic and linguistic comparisons reveal complex sex-biased transmission of language features. (PNAS 2024)

- DOI: 10.1073/pnas.2322881121 | PMCID: PMC11621847 | PMID: 39556737
- Version used: **2.0**
- Evidence: We used PLINK 2.0 to find biallelic SNPs with call rates of at least 1% and with a Hardy–Weinberg equilibrium exact test P -value less than 10 −7 (using the midp and keep-fewhet options) and only kept those individuals with sex identified in the associated metadata ( 64 ).
- Full pipeline: stage not stated [PLINK v2.0, R]

### Fitness consequences of structural variation inferred from a House Finch pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2409943121 | PMCID: PMC11588099 | PMID: 39531493
- Evidence: Runs of homozygosity were identified using PLINK ( 119 ) with SNPs from the PGGB VCF.
- Full pipeline: variant calling [BUSCO, hifiasm] -> stage not stated [BCFtools, PLINK, RepeatMasker]

### Controlling for polygenic genetic confounding in epidemiologic association studies. (PNAS 2024)

- DOI: 10.1073/pnas.2408715121 | PMCID: PMC11536117 | PMID: 39432782
- Evidence: SNPs with nonzero effects were randomly selected across the genome and genetic components (i.e., PGS without measurement error) were calculated using PLINK ( 91 ).
- Full pipeline: differential/statistical testing [LDSC] -> stage not stated [PLINK]

### Unraveling the genomic diversity and admixture history of captive tigers in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2402924121 | PMCID: PMC11441546 | PMID: 39298482
- Evidence: In order to select individuals to build the reference panel and accurately split individuals into groups for kinship estimation, we conducted PCA to ensure that all individuals in the unimputed dataset were clustering according to subspecies using PLINK v2 ( 71 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.4.1] -> variant calling [BWA v0.7.17, GATK v4.1.4.1] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.6, VCFtools, VEP]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Version used: **1.9**
- Evidence: For PCA, we used the PLINK (v1.9) ( 65 ) software to convert the VCF files into PLINK files.
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Version used: **1.9**
- Evidence: This analysis was computationally intractable with the full dataset, so we applied LD-pruning to the ≈11.5 million SNP dataset using PLINK v1.9 to remove SNPs with R 2 values >0.5 within 50 SNP sliding windows (step size 10 SNPs), resulting in a reduced dataset of 2,934,239 SNPs ( 16 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Version used: **1.90**
- Evidence: We conducted PCA on SVs using PLINK (v1.90) ( 88 ) to assess the genetic relationship between the Tibetan sheep and low-altitude Hu sheep.
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Detecting inbreeding depression in structured populations. (PNAS 2024)

- DOI: 10.1073/pnas.2315780121 | PMCID: PMC11087799 | PMID: 38687793
- Evidence: We identified runs of homozygosity (ROHs) with PLINK ( 17 ) and default parameters.
- Full pipeline: stage not stated [GCTA, PLINK, lme4]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Version used: **1.9b**
- Evidence: We performed LD-pruning using PLINK (version 1.9b5; --geno 0.10 –indep-pairwise 200 20 0.2 –maf 0.05) and ran BSLMMs for each migratory trait.
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### Posttranscriptional regulation of <i>FAN1</i> by miR-124-3p at rs3512 underlies onset-delaying genetic modification in Huntington's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2322924121 | PMCID: PMC11032436 | PMID: 38607933
- Evidence: In order to identify a set of SNPs that tag the effects of frequent onset-delaying modifier effect of FAN1 , we calculated the LD of SNPs (in the chr15:31000000-31400000 region) with the lead SNP (i.e., rs35811129) using the PLINK program ( https://zzz.bwh.harvard.edu/plink/ld.shtml ).
- Full pipeline: alignment/mapping [R] -> stage not stated [PLINK]

### Genomic ancestry and social dynamics of the last hunter-gatherers of Atlantic France. (PNAS 2024)

- DOI: 10.1073/pnas.2310545121 | PMCID: PMC10927518 | PMID: 38408241
- Evidence: Runs of homozygosity were estimated for a diploid dataset, for which ancient sample VCF files were subset to transversion sites enriched in the Yoruba population of the 1000 Genome Panel (KGP), phase 3 data, with the --homozyg command in PLINK ( 65 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [PLINK, SAMtools]

### Computationally efficient whole-genome quantile regression at biobank scale. (PNAS 2025)

- DOI: 10.1073/pnas.2513007122 | PMCID: PMC12718364 | PMID: 41380003
- Evidence: Specifically, we selected individuals of white British ancestry with available genotype data and applied quality-control filters using PLINK2 ( 24 , 25 ).
- Full pipeline: variant calling [PLINK]

### A 120-y time series of genomes reveals the consequences of closed breeding in German Shepherd Dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421755122 | PMCID: PMC12684887 | PMID: 41284896
- Version used: **1.90b**
- Evidence: We calculated estimates of both damage-corrected heterozygosity and conditional heterozygosity at transversion sites ascertained in a coyote (see SI Appendix ), as well as the frequency and size of ROH using PLINK v.1.90b6.21 ( 58 ).
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.5.3, SAMtools v1.9] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.1.4, PLINK v1.90b]

### GWAS for behavioral traits in golden retrievers identifies genes implicated in human temperament, mental health, and cognition. (PNAS 2025)

- DOI: 10.1073/pnas.2421757122 | PMCID: PMC12684936 | PMID: 41284867
- Version used: **1.9**
- Evidence: PLINK v1.9 software ( 110 ) was used to filter out markers with >5% genotype calls missing, which deviated from Hardy–Weinberg equilibrium ( P < 1e−6), or with minor allele frequency <5%, and individuals with >5% genotype calls missing.
- Full pipeline: variant calling [PLINK v1.9] -> normalisation [GEMMA, tidyverse] -> dimensionality reduction/clustering [GEMMA, tidyverse] -> differential/statistical testing [MAGMA v1.10] -> visualisation [GEMMA, tidyverse] -> stage not stated [GCTA]

### The impacts of European arrival on Australian dingoes. (PNAS 2025)

- DOI: 10.1073/pnas.2421749122 | PMCID: PMC12684890 | PMID: 41284893
- Version used: **1.90b**
- Evidence: We also calculated runs of homozygosity in PLINK v.1.90b6.21 following established methods ( 83 ), which were used to estimate both the fraction of each individual’s genome in ROH (F ROH ), and the frequency distribution of autozygous segments across Australian and New Guinean populations (e.g., ref.
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [SAMtools v1.9] -> differential/statistical testing [ADMIXTURE v1.3.0] -> stage not stated [BCFtools v1.9, BEDTools, IQ-TREE v2.1.4, PLINK v1.90b, R, VCFtools]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Version used: **1.90b**
- Evidence: We developed a reproducible and scalable Nextflow workflow for heritability estimation and GWAS using PLINK (v1.90b6.21 and v2.00a5LM) ( 92 ) and Genome-wide Complex Trait Analysis (GCTA v1.94.1) ( 109 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### Imputation of ancient canid genomes reveals inbreeding history over the past 10,000 years. (PNAS 2025)

- DOI: 10.1073/pnas.2416980122 | PMCID: PMC12684900 | PMID: 41284898
- Version used: **1.9**
- Evidence: ROH were estimated on the downsampled imputed samples using PLINK v1.9 ( 67 ) and on the downsampled nonimputed samples using ROHan v1.0 ( 68 ).
- Full pipeline: stage not stated [PLINK v1.9, R]

### Anthropocene genetic diversity loss in the marine tropics. (PNAS 2025)

- DOI: 10.1073/pnas.2513012122 | PMCID: PMC12646237 | PMID: 41231948
- Version used: **1.9**
- Evidence: PCA was performed using PLINK v.1.9 ( 73 ).
- Full pipeline: quality control [VCFtools v0.1.14] -> alignment/mapping [SAMtools v1.9, SPAdes v3.15.3] -> dimensionality reduction/clustering [ADMIXTURE v1.3, PLINK v1.9] -> stage not stated [freebayes v1.3.1]

### Machine-learning models based on histological images from healthy donors identify imageQTLs and predict chronological age. (PNAS 2025)

- DOI: 10.1073/pnas.2423469122 | PMCID: PMC12646272 | PMID: 41218125
- Version used: **2.0**
- Evidence: For this analysis, we employed a genome-wide association study approach, using the general linear models implemented in PLINK v2.0 ( 48 ).
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [PLINK v2.0] -> stage not stated [DESeq2, GSEA, QuPath v0.4.3]

### The genetic lottery goes to school: Better schools compensate for the effects of students' genetic differences. (PNAS 2025)

- DOI: 10.1073/pnas.2511715122 | PMCID: PMC12582282 | PMID: 41134622
- Evidence: PGI EA were computed based on these weights with the –score command in plink2 ( 48 ).
- Full pipeline: dimensionality reduction/clustering [R v4.2] -> stage not stated [PLINK]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Evidence: Using vcftools and PLINK, we calculated several statistics that were used to assess the quality of mapped sequences and identify individuals that sequenced poorly, including individual depth of coverage, the fraction of missing sites per individual, and transition:transversion ratios.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Evolutionary histories of functional mutations during the domestication and spread of &lt;i&gt;japonica&lt;/i&gt; rice in Asia. (PNAS 2025)

- DOI: 10.1073/pnas.2514614122 | PMCID: PMC12582302 | PMID: 41115193
- Version used: **1.90**
- Evidence: Next, we transformed vcf files into bed format files and filtered out any SNP with a genotyping rate lower than 80%, using PLINK v1.90 ( 114 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, Nextflow v20.10.0] -> variant calling [PLINK v1.90] -> dimensionality reduction/clustering [R v4.3] -> stage not stated [VCFtools v1.6]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: We conducted PCA using PLINK2 ( 93 ), admixture analyses using Admixture ( 44 ), and constructed a phylogenetic tree using IQtree ( 94 ).
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: We checked for individual relatedness using PLINK 1.
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Version used: **1.90b**
- Evidence: To visualize population structure, we performed PCAs in PLINK v1.90b5.3 ( 70 ) after pruning linked sites with an R 2 >0.1.
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### A genomic test of sex-biased dispersal in white sharks. (PNAS 2025)

- DOI: 10.1073/pnas.2507931122 | PMCID: PMC12358869 | PMID: 40758892
- Evidence: We used the window-based approach implemented in plink2 ( https://www.cog-genomics.org/plink/2.0 ) ( 51 ).
- Full pipeline: read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> variant calling [GATK v4.0] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools v1.9, PLINK]

### Population structure limits the use of genomic data for predicting phenotypes and managing genetic resources in forest trees. (PNAS 2025)

- DOI: 10.1073/pnas.2425691122 | PMCID: PMC12232740 | PMID: 40560610
- Version used: **1.90b**
- Evidence: 0.1.14 ( 122 ) and PLINK v.1.90b4.4 ( 123 ) to filter SNPs based on “strict” and “liberal” criteria, and then simulated a set of 51,820 “RAD-Seq” markers ( SI Appendix , Table S4 and Materials and Methods ).
- Full pipeline: variant calling [R] -> differential/statistical testing [R] -> simulation/modelling [PLINK v1.90b] -> stage not stated [GCTA, VCFtools v0.1.14]

### Participation bias in the estimation of heritability and genetic correlation. (PNAS 2025)

- DOI: 10.1073/pnas.2425530122 | PMCID: PMC12207467 | PMID: 40540605
- Version used: **1.90**
- Evidence: We used PLINK 1.90 to derive GWAS summary statistics ( 26 ).
- Full pipeline: variant calling [R] -> differential/statistical testing [PLINK v1.90] -> stage not stated [LDSC]

### Longitudinal sequencing reveals polygenic and epistatic nature of genomic response to selection. (PNAS 2025)

- DOI: 10.1073/pnas.2410452122 | PMCID: PMC12207516 | PMID: 40531879
- Evidence: To do this, we applied a clustering procedure akin to the LD clumping algorithm implemented in PLINK ( 64 ).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA, Picard] -> variant calling [DESeq2] -> dimensionality reduction/clustering [PLINK] -> stage not stated [R, emmeans]

### Natural dispersal is better than translocation for reducing risks of inbreeding depression in eastern black rhinoceros (&lt;i&gt;Diceros bicornis michaeli&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2414412122 | PMCID: PMC12167989 | PMID: 40460127
- Version used: **1.9**
- Evidence: The filtered set of SNPs were input to PLINK v1.9 ( 61 ) and the option—genome was selected to estimate pairwise relatedness (PI_HAT).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [SAMtools] -> variant calling [BCFtools] -> differential/statistical testing [emmeans] -> stage not stated [ADMIXTURE, PLINK v1.9, R, VCFtools]

### Study design and the sampling of deleterious rare variants in biobank-scale datasets. (PNAS 2025)

- DOI: 10.1073/pnas.2425196122 | PMCID: PMC12167998 | PMID: 40460117
- Version used: **1.90b**
- Evidence: For each weighted subsample, we compute the SFS for putative LoF sites on chromosome 1 (32,320 variants) as well as equal-sized random subsets of synonymous and missense variants (subsets generated using PLINK v1.90b6.26; variant annotation provided by UKB).
- Full pipeline: stage not stated [PLINK v1.90b]

### Ancient DNA suggests a historical demographic decline and genetic erosion in the Atlantic bluefin tuna. (PNAS 2025)

- DOI: 10.1073/pnas.2409302122 | PMCID: PMC12130816 | PMID: 40392844
- Version used: **1.90b**
- Evidence: SNPs were pruned (–indep-pairwise 50 5 0.2) for linkage disequilibrium using PLINK v1.90b6.21 ( 115 ) following ( 116 ).
- Full pipeline: read trimming [BWA, SAMtools v1.7, Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools v1.7] -> registration [GATK v3.7] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b, Picard, VCFtools v0.1.16]

### Genomics highlight an underestimation of phenology sensitivity to the urban heat island effect. (PNAS 2025)

- DOI: 10.1073/pnas.2408564122 | PMCID: PMC11962471 | PMID: 40100635
- Evidence: Using PLINK, we pruned the VCF for linkage disequilibrium, filtered for minor allele frequency greater than 0.1 and specified biallelic sites before calculating the eigenmodes of the SNP marker data matrix ( 43 , 44 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [PLINK, R]

### MUC5AC filaments illuminate the structural diversification of respiratory and intestinal mucins. (PNAS 2025)

- DOI: 10.1073/pnas.2419717122 | PMCID: PMC11912381 | PMID: 40035770
- Version used: **1.9**
- Evidence: The three common variants (V52F, S221R, and R1201W) were analyzed for correlation (r2) with the three common haplogroups of MUC5AC alleles (H1, H2, and H3) using PLINK v1.9.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX v1.3, PLINK v1.9, PyMOL]

### Empowering genome-wide association studies via a visualizable test based on the regional association score. (PNAS 2025)

- DOI: 10.1073/pnas.2419721122 | PMCID: PMC11892588 | PMID: 39999171
- Evidence: We include covariates such as age, sex, and the top 10 principle components from the genotype data, processed with the software PLINK ( 37 ).
- Full pipeline: variant calling [PLINK]

### Exome sequencing identifies genes for socioeconomic status in 350,770 individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2414018122 | PMCID: PMC11745334 | PMID: 39772748
- Version used: **2.0**
- Evidence: The top 10 within-ancestral PCs were calculated by PLINK version 2.0 using an initially defined set of high-quality independent autosomal variants (MAF > 0.1%, missingness < 1%, HWE P -value > 1.0 × 10 −6 , and two rounds of pruning using –indep-pairwise 200 100 0.1 and --indep-pairwise 200 100 0.05).
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ANNOVAR, FUMA, PLINK v2.0, SAIGE, Seurat, SnpEff]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Version used: **1.9**
- Evidence: High-quality 4DTv SNPs (36,028) were used for maximum-likelihood phylogenetic tree construction (IQ-TREE) (v1.6.12) ( 69 ), PCA (PLINK, v1.9), and population structure analysis (ADMIXTURE, K = 2–10, v1.23) ( 70 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Host genetic regulation of rumen 6-hydroxymelatonin reduces methane emissions in dairy cattle. (PNAS 2026)

- DOI: 10.1073/pnas.2604454123 | PMCID: PMC13291679 | PMID: 42258707
- Evidence: The MLM was established to identify significant SNPs for 6-hydroxylmelatonin, a kinship matrix was established as the random effect using GEMMA ( 21 ), and the population structure was established as the fixed effect using PLINK.
- Full pipeline: quality control [fastp] -> alignment/mapping [fastp] -> dimensionality reduction/clustering [R] -> differential/statistical testing [GEMMA, TwoSampleMR v0.5.6] -> stage not stated [GCTA, PLINK, VEP, lavaan]

### Observational epidemiological studies can mitigate genetic confounding with a genetic relatedness matrix. (PNAS 2026)

- DOI: 10.1073/pnas.2533909123 | PMCID: PMC13167772 | PMID: 42090255
- Evidence: To compute PENGUIN-corrected estimates in simulated data, we first generated GWAS summary statistics for biallelic variants with minor allele frequency greater than 0.01 using plink2 ( 72 ).
- Full pipeline: variant calling [LDSC] -> differential/statistical testing [PLINK] -> simulation/modelling [LDSC, PLINK] -> stage not stated [GCTA]

### An inverse correlation between structural linguistic and human genetic diversity. (PNAS 2026)

- DOI: 10.1073/pnas.2526762123 | PMCID: PMC13142977 | PMID: 42066044
- Version used: **1.9**
- Evidence: F was calculated with PLINK v 1.9 ( 43 ) on the autosomal chromosomes for each individual in the dataset as the observed ( H O ) minus expected ( H E ) homozygous genotypes, divided by the number of nonmissing genotypes (i.e., the number of nonmissing SNPs) minus the expected number of homozygotes: F = H O - H E N NM - H E .
- Full pipeline: variant calling [PLINK v1.9] -> stage not stated [R, Stan, brms]

### Unveiling the glymphatic system's role in brain aging: A comprehensive biomarker and modifiable intervention target. (PNAS 2026)

- DOI: 10.1073/pnas.2516601123 | PMCID: PMC13142974 | PMID: 42044335
- Evidence: We conducted quality control on imputed genotypes from white British of European ancestry using PLINK as described previously ( 64 , 65 ).
- Full pipeline: quality control [PLINK] -> alignment/mapping [ANNOVAR] -> variant calling [PLINK] -> differential/statistical testing [FUMA, LightGBM, Metascape] -> machine learning [XGBoost]

### Large future genetic diversity losses are predicted from conservation indicators even with habitat protection. (PNAS 2026)

- DOI: 10.1073/pnas.2514371123 | PMCID: PMC13037886 | PMID: 41886371
- Version used: **1.9**
- Evidence: All datasets were transformed into PLINK files using PLINK v1.9 ( 53 ).
- Full pipeline: variant calling [R v0.0.3] -> stage not stated [ADMIXTURE, PLINK v1.9, SciPy]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Evidence: We estimated pairwise linkage disequilibrium using PLINK (version v1.90b6.26) ( 63 ) with the following parameters: --ld-window-kb 1000, --ld-window 99999, --ld-window-r2 0.
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Deep evolutionary conservation of a sex-determining locus without sequence homology. (PNAS 2026)

- DOI: 10.1073/pnas.2522417123 | PMCID: PMC12799146 | PMID: 41490485
- Version used: **1.9**
- Evidence: We confirmed male diploidy by comparing genome-wide heterozygosity levels with those of diploid females, and we inferred runs of homozygosity in diploid individuals using PLINK v1.9.
- Full pipeline: alignment/mapping [BWA v0.7.18, freebayes v1.0.2] -> variant calling [BWA v0.7.18, IQ-TREE v2.3.6, SPAdes v3.15.2, freebayes v1.0.2] -> dimensionality reduction/clustering [BWA v0.7.18, freebayes v1.0.2] -> structure determination [IQ-TREE v2.3.6] -> stage not stated [BCFtools v1.21, PLINK v1.9, R v4.4, VCFtools v0.1.16]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Version used: **1.9**
- Evidence: The PCA for ethnic heterogeneity was performed with PLINK (v1.9) on WES and WGS data, with the 1000 Genomes Project phase 3 public database as a reference, using >15,000 exonic variants with a MAF > 0.01 and a call rate > 0.99.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Somatic mosaicism in schizophrenia brains reveals prenatal mutational processes. (Science 2024)

- DOI: 10.1126/science.adq1456 | PMCID: PMC11490355 | PMID: 39388546
- Evidence: After LD-based pruning of common variants using PLINK2 ( 60 ), PLINK2’s implementation of KING ( 61 ) was used to estimate relatedness; related samples and samples with cryptic relationships were removed with a kinship coefficient cut-off of ≥ 0.0884.
- Full pipeline: alignment/mapping [GATK] -> normalisation [DESeq2] -> stage not stated [PLINK, R]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Evidence: The plink2 and Nexus databases were used to search a database composed of the subunit sequences ( 95 , 96 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Canine genome-wide association study identifies &lt;i&gt;DENND1B&lt;/i&gt; as an obesity gene in dogs and humans. (Science 2025)

- DOI: 10.1126/science.ads2145 | PMCID: PMC7618706 | PMID: 40048553
- Version used: **1.9**
- Evidence: A stringent, conservative significance threshold ( p = 8.31x10 -7 ) was determined by Bonferroni correction, using the number of independent SNP in the analysis (determined by LD pruning of the data set using a cut-off of r 2 < 0.7 in PLINK v.1.9) ( 61 ).
- Full pipeline: differential/statistical testing [GCTA, PLINK v1.9]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Version used: **1.9**
- Evidence: PLINK (v1.9) was used to perform logistic regression with Firth correction to assess associations with CHIP for the most significant sentinel SNP at 24 loci previously reported ( 11 ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

