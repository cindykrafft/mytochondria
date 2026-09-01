# GCTA

- **Category:** statgen
- **Papers in survey:** 44
- **Journals:** Nature (20), PNAS (20), Cell (3), Science (1)
- **Years:** 2021 (5), 2022 (10), 2023 (6), 2024 (8), 2025 (12), 2026 (3)
- **Versions named:** 1.25.3 (1), 1.9.3 (1), 1.26 (1), 1.91.7 (1), 1.94.1 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (6), variant calling (3), differential/statistical testing (3), machine learning (1), simulation/modelling (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Evidence: .../bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-288 PLINK 1.9 Purcell et al., 2007 https://www.cog-genomics.org/plink/1.9/ COJO in GCTA Yang et al., 2011 , 2012 https://cnsgenomics.com/software/gcta/#COJO FUMA Watanabe et al., 2017 https://fuma.ctglab.nl LDHub Zheng et al., 2017 https://github.com/bulik/ldsc PRsice2 Choi and O’Reilly, 2019 ; Choi et al., 2020 https://www.prsice....
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### Limb development genes underlie variation in human fingerprint patterns. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.008 | PMCID: PMC8740935 | PMID: 34995520
- Evidence: ... and Eskin, 2011 http://genetics.cs.ucla.edu/meta/ ; RRID: N/A PAINTOR v2.1 Kichaev et al., 2014 https://github.com/gkichaev/PAINTOR_V3.0 ; RRID: N/A GCTA-GREML Lee et al., 2012 ; Yang et al., 2011 https://yanglab.westlake.edu.cn/software/gcta/ ; RRID: N/A LocusZoom Pruim et al., 2010 https://genome.sph.umich.edu/wiki/LocusZoom ; RRID: SCR_009257 GREAT v4.0.4 McLean et al., 2010 http://great.stanf...
- Full pipeline: stage not stated [Cytoscape, GCTA, IMPUTE2, ImageJ, PLINK v1.9, R v3.6, SHAPEIT]

### Trans-ancestry genome-wide study of depression identifies 697 associations implicating cell types and pharmacotherapies. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.002 | PMCID: PMC11829167 | PMID: 39814019
- Evidence: Using conditional-and-joint GCTA-COJO 12 analysis with threshold p ≤ 5 × 10 −8 within 10 Mb windows for the combined meta-analysis, we identified 697 significant independent single-nucleotide polymorphisms (SNPs) in 635 genomic regions.
- Full pipeline: alignment/mapping [LDSC] -> variant calling [LDSC] -> dimensionality reduction/clustering [LDSC] -> stage not stated [Bioconductor, GCTA, MAGMA v1.08, PLINK v1.9]

### Exome sequencing and analysis of 454,787 UK Biobank participants. (Nature 2021)

- DOI: 10.1038/s41586-021-04103-z | PMCID: PMC8596853 | PMID: 34662886
- Version used: **1.91.7**
- Evidence: We then identified independent signals (in the autosomes and the X chromosome) using the approximate conditional analysis implemented in GCTA v.1.91.7 46 .
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [LDSC, REGENIE] -> stage not stated [GCTA v1.91.7, SnpEff]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: URLs for software use BCFtools, http://samtools.github.io/bcftools/ ; BOLT-LMM, https://data.broadinstitute.org/alkesgroup/BOLT-LMM/ ; cov-LDSC, https://github.com/immunogenomics/cov-ldsc ; EAGLE, https://alkesgroup.broadinstitute.org/Eagle/ ; GCTA, http://cnsgenomics.com/software/gcta/ ; IMPUTE2, https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ; LDpred, https://github.com/bvilhjal/ldpred/ ; ...
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### A saturated map of common genetic variants associated with human height. (Nature 2022)

- DOI: 10.1038/s41586-022-05275-y | PMCID: PMC9605867 | PMID: 36224396
- Evidence: Quasi-independent associations were obtained after performing approximate conditional and joint (COJO) multiple-SNP analyses 6 , as implemented in GCTA 7 ( Methods ).
- Full pipeline: dimensionality reduction/clustering [MAGMA] -> differential/statistical testing [LDSC, R] -> stage not stated [GCTA, PLINK]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: ...s in our dataset, (3) we further filtered for MAF > 0.05 in 1KGP3 (as well as in our data), (4) we calculated the first 20 principal components using GCTA 54 , (5) we projected the individual data onto the 1KGP3 principal component loadings, (6) we trained a random forest model to predict ancestries based on (i) first 8 1KGP3 principal components, (ii) set Ntrees = 400, (iii) train and predict on ...
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### Stroke genetics informs drug discovery and risk prediction across ancestries. (Nature 2022)

- DOI: 10.1038/s41586-022-05165-3 | PMCID: PMC9524349 | PMID: 36180795
- Evidence: We applied the conditional and joint analysis approach 7 implemented in the Genome-wide Complex Trait Analysis software 52 (GCTA-COJO) to identify potentially independent signals within the same genomic region.
- Full pipeline: quality control [R] -> differential/statistical testing [LDSC] -> stage not stated [GCTA, MAGMA, SAIGE, Seurat, TwoSampleMR]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Evidence: Genome-wide association study For the MLM, we used the leave-one-chromosome-out method and the mixed model implemented in GCTA 39 .
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Genetic and chemotherapeutic influences on germline hypermutation. (Nature 2022)

- DOI: 10.1038/s41586-022-04712-2 | PMCID: PMC9117138 | PMID: 35545669
- Evidence: To remove cryptic relatedness, we removed individuals with an estimated relatedness of >0.025 (using GCTA grm-cutoff, 0.025).
- Full pipeline: differential/statistical testing [R v4.0.1] -> stage not stated [GCTA]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **1.26**
- Evidence: We computed genome-wide kinship ( Θ ) for all pairs of relevant individuals using the SNP genotypes at the above-mentioned 30.2 million DNA variants using either GEMMA (v.0.97) 64 or GCTA (v.1.26) 65 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Evidence: We established the independence of signals using GCTA-cojo, and we validated this with conditional analysis using individual-level data with SAIGE ( Methods , Supplementary Table 6 ).
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Version used: **1.25.3**
- Evidence: (1) We performed association testing using linear mixed models as implemented in GCTA (v.1.25.3), including a genetic relatedness matrix (GRM) as a random effect 55 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Version used: **1.9.3**
- Evidence: To perform the conditional analysis, we used the GCTA (v.1.9.3) --cojo-slct function 25 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Examining the role of common variants in rare neurodevelopmental conditions. (Nature 2024)

- DOI: 10.1038/s41586-024-08217-y | PMCID: PMC11634775 | PMID: 39567701
- Evidence: Code availability We used publicly available software: LDpred ( https://github.com/bvilhjal/ldpred ), LDSC ( https://github.com/bulik/ldsc ), GCTA-LDMS ( https://yanglab.westlake.edu.cn/software/gcta/#GREMLinWGSorimputeddata ), PCGC regression ( https://dougspeed.com/pcgc-regression/ ) and GenomicSEM ( https://github.com/PerlineDemange/non-cognitive/blob/master/GenomicSEM/Genetic%20correlations/Wi...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GCTA, LDSC] -> stage not stated [PLINK, VEP]

### Genome-wide characterization of circulating metabolic biomarkers. (Nature 2024)

- DOI: 10.1038/s41586-024-07148-y | PMCID: PMC10990933 | PMID: 38448586
- Evidence: Heritability and variance explained We used GCTA-GREML 71 v.
- Full pipeline: differential/statistical testing [R] -> stage not stated [GCTA, PLINK v2.0, SAIGE, TwoSampleMR v0.5.1]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Evidence: For the PCA including only imputed diploid samples, we used GCTA (ref.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Evidence: Heritability estimation We estimated SV heritability using the GREML software from the GCTA toolbox (v.1.94.1).
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Polygenic and developmental profiles of autism differ by age at diagnosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09542-6 | PMCID: PMC12571882 | PMID: 41034588
- Evidence: Heritability, genetic correlation, and genomicSEM Heritability analyses for age at autism diagnosis were conducted using a single-component genome-wide complex trait analysis with a genomic-relatedness-based restricted maximum likelihood approach (GCTA-GREML v1.94.1) 91 , 92 in unrelated autistic individuals using the quality-controlled genetic data in SPARK.
- Full pipeline: differential/statistical testing [PLINK, lme4 v1.1.27.1] -> stage not stated [GCTA, LDSC, lavaan v0.6]

### Translational genomics of osteoarthritis in 1,962,069 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-08771-z | PMCID: PMC12119359 | PMID: 40205036
- Evidence: (2) For each index variant in a given clump, we performed an approximate stepwise model-selection procedure implemented by COJO in GCTA 57 to establish whether index variants were independent ( Supplementary Note ).
- Full pipeline: quality control [BCFtools v1.13, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [Enrichr, GCTA, PLINK]

### Spatially resolved mapping of cells associated with human complex traits. (Nature 2025)

- DOI: 10.1038/s41586-025-08757-x | PMCID: PMC12095064 | PMID: 40108460
- Evidence: We used GCTA (V1.94.1) 66 to generate quantitative traits based on real genotype data of a set of selected causal variants.
- Full pipeline: alignment/mapping [R] -> variant calling [GCTA] -> normalisation [Scanpy] -> dimensionality reduction/clustering [PLINK, Seurat, clusterProfiler] -> differential/statistical testing [MAGMA] -> simulation/modelling [PLINK] -> stage not stated [LDSC]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Evidence: Quasi-independent genome-wide significant ( P < 5 × 10 −8 ) signals were initially selected in 1-Mb windows and secondary signals within these loci were further selected by conditional analysis in GCTA 68 , using a linkage disequilibrium reference derived from the UK Biobank study.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Evidence: We first assessed the contribution of different variant types to cis -heritability (the variance explained by all genetic variants in a 1 Mb window around the transcription start site (TSS)) of gene expression phenotypes using a multicomponent GREML model in GCTA 53 – 55 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: The PCA was performed with population-scale LD filtered SNPs using GCTA ( 86 ).
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Handedness and its genetic influences are associated with structural asymmetries of the cerebral cortex in 31,864 individuals. (PNAS 2021)

- DOI: 10.1073/pnas.2113095118 | PMCID: PMC8617418 | PMID: 34785596
- Evidence: From the imputed SNP genotype data released by the UK Biobank (March 2018), 9,516,135 autosomal variants with minor allele frequencies > 1%, INFO (imputation quality) score > 0.7 and Hardy–Weinberg equilibrium P > 1 × 10 −7 were used to build a genetic relationship matrix using the Genome-wide Complex Trait Analysis (GCTA) software ( 77 ) (version 1.93.0beta).
- Full pipeline: variant calling [GCTA] -> structure determination [FreeSurfer v6.0]

### Genome-wide shifts in climate-related variation underpin responses to selective breeding in a widespread conifer. (PNAS 2021)

- DOI: 10.1073/pnas.2016900118 | PMCID: PMC7958292 | PMID: 33649218
- Evidence: GPA (also known as GWAS) analyses of 32,449 SNPs in 929 natural seedlings were implemented using the mlma function in GCTA ( 44 ) and the seedling phenotypic residual values of each trait ( SI Appendix , section C.2 ).
- Full pipeline: stage not stated [GCTA]

### Genomic insights into zokors' phylogeny and speciation in China. (PNAS 2022)

- DOI: 10.1073/pnas.2121819119 | PMCID: PMC9171634 | PMID: 35512099
- Evidence: Population genomic analyses including phylogenetic tree, PCA, and STRUCTURE construction were conducted by Phylip, GCTA, and ADMIXTURE, respectively.
- Full pipeline: alignment/mapping [GATK] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BUSCO, RAxML, VCFtools]

### Genomic loci influence patterns of structural covariance in the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2300842120 | PMCID: PMC10756284 | PMID: 38127979
- Evidence: (B): Heritability estimates and genome-wide association analysis: We estimated the SNP-based heritability explained by all autosomal genetic variants using GCTA-GREML ( 62 ).
- Full pipeline: differential/statistical testing [FUMA, MAGMA, PLINK] -> stage not stated [GCTA, GSEA, LDSC]

### Natural genetic variation in the pheromone production of <i>C. elegans</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2221150120 | PMCID: PMC10293855 | PMID: 37339205
- Evidence: The additive kinship matrix was generated from the 30,065 markers using the make-grm and make-grm-inbred functions from GCTA ( 48 ).
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools, PLINK v1.9] -> stage not stated [GCTA, R, SnpEff]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Evidence: We used fastGWA implemented in GCTA ( 67 ), a mixed linear model-based tool, that controls for population stratification by principal components and takes into account relatedness using a sparse genetic relationship matrix.
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### Natural selection of immune and metabolic genes associated with health in two lowland Bolivian populations. (PNAS 2023)

- DOI: 10.1073/pnas.2207544120 | PMCID: PMC9910614 | PMID: 36574663
- Evidence: Using our dataset, we estimate a heritability of 0.193 (SE = 0.046) and 0.162 (SE = 0.049) for eosinophil percentages and total counts, respectively [using GCTA ( 70 ), n = 1227].
- Full pipeline: alignment/mapping [R] -> variant calling [GEMMA] -> normalisation [limma] -> stage not stated [ADMIXTURE, GCTA, VCFtools]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Evidence: Then, PCA was carried out using the genome-wide complex trait analysis (GCTA) (v1.92.2) ( 66 ) with default parameters.
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### Fast and scalable ensemble learning method for versatile polygenic risk prediction. (PNAS 2024)

- DOI: 10.1073/pnas.2403210121 | PMCID: PMC11331062 | PMID: 39110727
- Evidence: For simulation setting, we generated 10 simulation replicates of a continuous phenotype using GCTA ( 40 ) based on a linear additive model with total heritability around 0.4.
- Full pipeline: differential/statistical testing [LDSC] -> simulation/modelling [GCTA] -> machine learning [R]

### Detecting inbreeding depression in structured populations. (PNAS 2024)

- DOI: 10.1073/pnas.2315780121 | PMCID: PMC11087799 | PMID: 38687793
- Evidence: We could not use GCTA software to run the mixed model for this GRM because its leading eigenvalue is negative which the Choleski decomposition algorithm used for matrix inversion in GCTA cannot handle (it requires a positive definite matrix), while the Schur decomposition algorithm used in gaston can.
- Full pipeline: stage not stated [GCTA, PLINK, lme4]

### Heritability within groups is uninformative about differences among groups: Cases from behavioral, evolutionary, and statistical genetics. (PNAS 2024)

- DOI: 10.1073/pnas.2319496121 | PMCID: PMC10962975 | PMID: 38470926
- Evidence: The estimator works on principles similar to SNP heritability estimators ( 35 ), such as implemented in GCTA ( 36 ).
- Full pipeline: stage not stated [GCTA]

### GWAS for behavioral traits in golden retrievers identifies genes implicated in human temperament, mental health, and cognition. (PNAS 2025)

- DOI: 10.1073/pnas.2421757122 | PMCID: PMC12684936 | PMID: 41284867
- Evidence: Heritability was estimated using the genome-based restricted maximum likelihood (GREML) approach, implemented through GCTA software (v.1.93.2) ( 76 ) specifically employing the GREML-LDMS approach to adjust for the influence of LD and minor allele frequency (MAF) on the estimated SNP heritability.
- Full pipeline: variant calling [PLINK v1.9] -> normalisation [GEMMA, tidyverse] -> dimensionality reduction/clustering [GEMMA, tidyverse] -> differential/statistical testing [MAGMA v1.10] -> visualisation [GEMMA, tidyverse] -> stage not stated [GCTA]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Version used: **1.94.1**
- Evidence: We developed a reproducible and scalable Nextflow workflow for heritability estimation and GWAS using PLINK (v1.90b6.21 and v2.00a5LM) ( 92 ) and Genome-wide Complex Trait Analysis (GCTA v1.94.1) ( 109 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### Integrating extensive functional annotations and multiomics of cattle enhances climate resilience prediction and mapping. (PNAS 2025)

- DOI: 10.1073/pnas.2514736122 | PMCID: PMC12704747 | PMID: 41284851
- Evidence: The linear mixed model analysis used GCTA ( 66 ).
- Full pipeline: machine learning [R] -> stage not stated [GCTA, VEP]

### Population structure limits the use of genomic data for predicting phenotypes and managing genetic resources in forest trees. (PNAS 2025)

- DOI: 10.1073/pnas.2425691122 | PMCID: PMC12232740 | PMID: 40560610
- Evidence: Genomic relationship matrices (GRMs) were calculated using the kin.blup function of rrBLUP or the -- make-grm-alg 1 option of GCTA ( 131 ).
- Full pipeline: variant calling [R] -> differential/statistical testing [R] -> simulation/modelling [PLINK v1.90b] -> stage not stated [GCTA, VCFtools v0.1.14]

### A periplasmic protein modulates the proteolysis of peptidoglycan hydrolases to maintain cell wall homeostasis in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418854122 | PMCID: PMC11789061 | PMID: 39841140
- Evidence: To construct a library of mutant bipP alleles for the identification of hyperactive bipP , bipP was mutagenized by error-prone PCR using pWJ229 as a template with the primer pair 5′-GCTA TCTAGA TTTAAGAAGGAGATATACATATGCAGGGCACAAAAATTCGAC-3′ and 5′-CCTTAAAGCGCATGAACTCC-3′, employing Pfu(D215A D473G) polymerase ( 41 ).
- Full pipeline: structure determination [UCSF Chimera] -> stage not stated [AlphaFold, GCTA]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Evidence: To estimate heritability and phenotypic variance, we used GCTA —a tool developed to estimate these parameters for complex traits based on genome-wide SNPs ( 166 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

### Host genetic regulation of rumen 6-hydroxymelatonin reduces methane emissions in dairy cattle. (PNAS 2026)

- DOI: 10.1073/pnas.2604454123 | PMCID: PMC13291679 | PMID: 42258707
- Evidence: S1 A ) by GCTA ( 14 ) ( https://yanglab.westlake.edu.cn/software/gcta ), and using the population structure ( SI Appendix , Fig.
- Full pipeline: quality control [fastp] -> alignment/mapping [fastp] -> dimensionality reduction/clustering [R] -> differential/statistical testing [GEMMA, TwoSampleMR v0.5.6] -> stage not stated [GCTA, PLINK, VEP, lavaan]

### Observational epidemiological studies can mitigate genetic confounding with a genetic relatedness matrix. (PNAS 2026)

- DOI: 10.1073/pnas.2533909123 | PMCID: PMC13167772 | PMID: 42090255
- Evidence: Unless specified otherwise, the GRM was constructed with an algorithm corresponding to the assumption that all variants contribute equally to heritability (GCTA flag --make-grm-alg 0).
- Full pipeline: variant calling [LDSC] -> differential/statistical testing [PLINK] -> simulation/modelling [LDSC, PLINK] -> stage not stated [GCTA]

### Canine genome-wide association study identifies &lt;i&gt;DENND1B&lt;/i&gt; as an obesity gene in dogs and humans. (Science 2025)

- DOI: 10.1126/science.ads2145 | PMCID: PMC7618706 | PMID: 40048553
- Evidence: Significant factors in the regression (sex, neuter status and a sex:neuter interaction term) were included as covariates in the GWAS which applied a linear mixed effects model (GCTA MLMA-LOCO) to identify variants associated with BCS ( 60 ).
- Full pipeline: differential/statistical testing [GCTA, PLINK v1.9]

