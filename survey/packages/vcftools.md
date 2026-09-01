# VCFtools

- **Category:** genomics
- **Papers in survey:** 112
- **Journals:** PNAS (82), Nature (28), Cell (2)
- **Years:** 2021 (13), 2022 (19), 2023 (19), 2024 (23), 2025 (29), 2026 (9)
- **Versions named:** 0.1.16 (24), 0.1.13 (8), 0.1.14 (6), 0.1.15 (4), 0.1.17 (3), 0.1.12b (2), 0.1.12 (2), 1.6 (1)
- **Pipeline stages it appears in:** variant calling (21), alignment/mapping (5), differential/statistical testing (4), dimensionality reduction/clustering (4), normalisation (3), quantification (2), quality control (2)

## Papers

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...er/CircularMapper SAMtools Li et al., 2009 http://samtools.sourceforge.net/ BCFtools Li et al., 2009 http://samtools.github.io/bcftools/bcftools.html VCFtools Danecek et al., 2011 http://vcftools.sourceforge.net/ HaploGrep2 Weissensteiner et al., 2016 https://github.com/seppinho/haplogrep-cmd GATK McKenna et al., 2010 https://gatk.broadinstitute.org/hc/en-us BEAST Bouckaert et al., 2019 http://bea...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Version used: **0.1.12**
- Evidence: (2016) https://useast.ensembl.org/info/docs/tools/vep/index.html VCFtools v0.1.12 Danecek et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### A chickpea genetic variation map based on the sequencing of 3,366 genomes. (Nature 2021)

- DOI: 10.1038/s41586-021-04066-1 | PMCID: PMC8612933 | PMID: 34759320
- Evidence: Nucleotide diversity ( π ) was calculated from a 100-kb sliding window with a 10-kb step using VCFtools 36 v.0.1.13.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BUSCO, PLINK, RAxML, VCFtools]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: F ST calculations were accomplished via vcftools 91 .
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: ...weizhouUMICH/SAIGE ; SHAPEIT, http://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.html ; TESLA, https://github.com/funfunchen/rareGWAMA ; VCFtools, https://vcftools.github.io/index.html .
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### Island-specific evolution of a sex-primed autosome in a sexual planarian. (Nature 2022)

- DOI: 10.1038/s41586-022-04757-3 | PMCID: PMC9177419 | PMID: 35650439
- Version used: **0.1.14**
- Evidence: All variants were filtered with VCFtools (version 0.1.14) 48 to remove insertions and deletions and to select biallelic SNVs.
- Full pipeline: variant calling [GATK v4.1.4.1] -> quantification [kallisto v0.44.0] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [ImageJ, RAxML v0.9.0, VCFtools v0.1.14]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Version used: **0.1.16**
- Evidence: VCFtools (0.1.16) were used to filter for sites that are in intron 20–21.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### Mutation bias reflects natural selection in Arabidopsis thaliana. (Nature 2022)

- DOI: 10.1038/s41586-021-04269-6 | PMCID: PMC8810380 | PMID: 35022609
- Evidence: We therefore calculated the minor allele frequency (vcftools --freq) and their mean for every polymorphic position in the genome of 1,135 natural A. thaliana accessions 35 in relation to TSSs and TTSs across the entire genome.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v2.3, SAMtools] -> alignment/mapping [BWA v0.7.17, Bowtie2, Cutadapt v2.3, MACS2, R, SAMtools] -> variant calling [BWA v0.7.17, Cutadapt v2.3, GATK, SAMtools] -> differential/statistical testing [R] -> stage not stated [VCFtools]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: A computational pipeline using vcftools, python, linux and R was used to compute mutation burden in different classes of variants, and at different derived allele frequency thresholds.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: After quality control using VCFtools 108 (v.0.1.17), the raw SNPs were filtered using GATK 107 (v.4.1.8.0) and VCFtools 108 (v.0.1.17) as follows: SNP clusters, defined as three or more SNPs located within 10 bp; low and high average SNP depth (4 ≤ DP ≥ 15); and SNPs located in the unanchored chromosome were removed.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Version used: **0.1.17**
- Evidence: Relatedness To analyse relatedness among the 235 individuals in the ATCP cohort, we used VCFtools (v.0.1.17) with the ‘relatedness2’ option 48 (Supplementary Table 1 ), which is based on the KING software package 49 .
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Version used: **0.1.12b**
- Evidence: Poly(A) RNA was paired-end sequenced at the Oxford Genome Centre using the Illumina HiSeq-4000 machines. vcftools (v0.1.12b) was applied on genetic variation data in the form of variant call format (VCF) files to filter out indels and SNPs with a minor allele frequency of less than 0.04.
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Reducing brassinosteroid signalling enhances grain yield in semi-dwarf wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06023-6 | PMCID: PMC10156601 | PMID: 37100915
- Version used: **0.1.13**
- Evidence: Wheat accessions including 28 wild emmer accessions, 93 domesticated tetraploid wheat accessions and 289 hexaploid wheat accessions (Supplementary Table 7 ) were used for the nucleotide diversity analysis of the Rht-B1 , EamA-B , ZnF-B gene cassette and its flanking regions using VCFtools (v0.1.13) with >100-kilobase sliding windows in 100-kilobase steps.
- Full pipeline: alignment/mapping [TopHat] -> differential/statistical testing [DESeq2, R] -> stage not stated [ImageJ, VCFtools v0.1.13]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: The data were converted to 0, 1 and 2 format using VCFtools 122 and samples were clustered using the pheatmap package ( https://cran.r-project.org/web/packages/pheatmap/pheatmap.pdf ) from R statistical environment 57 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Releasing a sugar brake generates sweeter tomato without yield penalty. (Nature 2024)

- DOI: 10.1038/s41586-024-08186-2 | PMCID: PMC11578880 | PMID: 39537922
- Version used: **0.1.16**
- Evidence: Tajima’s D value was analysed by VCFtools (version 0.1.16), and the F ST value was calculated using the Python script popgenWindows.py as described previously 72 , 73 .
- Full pipeline: alignment/mapping [MAFFT v7.525] -> quantification [ImageJ] -> visualisation [ggplot2 v3.4.4] -> stage not stated [IQ-TREE, PLINK, Python, VCFtools v0.1.16]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **0.1.17**
- Evidence: Variants present in at least 99% of genomes were finally extracted using VCFtools v.0.1.17, generating a total of 866,840 core SNPs.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Version used: **0.1.16**
- Evidence: The resulting output was saved in variant call format (vcf), keeping only biallelic SNPs (-m2 -M2 -v snps), and additionally filtered with vcftools (v.0.1.16) 71 with -keep and -recode options for lists of individuals grouped by continental region in which we were able to estimate diploid copy numbers.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **0.1.16**
- Evidence: We calculated π over 10-kb windows of the genome using VCFtools (v0.1.16) 82 (parameter --window-pi 10000).
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **0.1.16**
- Evidence: We also used VCFtools (v0.1.16) 119 to calculate Weir and Cockerham’s F ST in 10-kb windows to assess signals of selection based on changes in allele frequency between populations.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: Using the complete variant call sets, we quantified the nucleotide diversity of each subspecies with VCFtools.
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **0.1.16**
- Evidence: We filtered SNPs using vcftools (v.0.1.16) 71 , keeping only variants with a genotype quality of more than 10 (--minGQ 10).
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: We then used VCFtools 68 to calculate a relatedness statistic of the long-read sequenced samples compared with the short-read sequenced samples using the ‘--relatedness2’ option.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Filtering of the pangenome graph-based VCF file to compare with the linear reference-based VCF file was performed with VCFtools 66 (example command: vcftools --remove-indels --minGQ 20 --maf 0.25 --max-missing 0.3 --min-alleles 2 --max-alleles 2 --stdout --recode --gzvcf merged.sorted.a.PASS.normed_no_dups.vcf.gz > merged.sorted.a.PASS.normed_no_dups.more_filter_missing0.3.vcf.gz).
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Evidence: The index of genetic differentiation ( F ST ; Weir and Cockerham’s method) between the two clades was calculated using a modified version of vcftools ( https://github.com/jydu/vcftools ) to allow the computation of statistics with haploid data.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **0.1.13**
- Evidence: Genetic differentiation ( F st ) and nucleotide diversity (π) were calculated with VCFtools (version 0.1.13).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: 52 for the 44 individuals using BCFtools, and then sites with ≥5% of missing calls, that is, missing in more than 3 out of 58 samples, were removed using VCFtools 103 (v.0.1.16).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: Identification of genomic selective sweep To detect selective sweeps associated with artificial selection during domestication, we calculated π wild / π cultivated and F ST using VCFtools 119 (v.0.1.16) with a 100-kb sliding window and a 10-kb step.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: To detect interpopulation selective signals, F ST values and XP-CLR scores were calculated using VCFtools 83 (v.0.1.16) and XP-CLR ( https://github.com/hardingnj/xpclr ), respectively.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Version used: **0.1.13**
- Evidence: Variants were identified based on the multiple sequence alignment, and variants with high levels of missing data (more than 10%) or a MAF below 5% were removed using VCFtools (v0.1.13) 105 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Reduced cyclin D3 expression in erythroid cells protects against malaria. (Nature 2026)

- DOI: 10.1038/s41586-026-10110-9 | PMCID: PMC12999499 | PMID: 41708853
- Version used: **0.1.12b**
- Evidence: To estimate the F ST statistic, the Weir–Cockerham formula implemented in VCFtools v.0.1.12b ( https://vcftools.github.io/index.html ) was used to compare SardiNIA with 1KG EUR samples.
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [ImageJ] -> differential/statistical testing [VCFtools v0.1.12b] -> stage not stated [MACS2]

### Genomic evidence for inbreeding depression and purging of deleterious genetic variation in Indian tigers. (PNAS 2021)

- DOI: 10.1073/pnas.2023018118 | PMCID: PMC8670471 | PMID: 34848534
- Evidence: The variants were filtered with VCFtools ( 91 ) to retain biallelic sites with a minimum minor allele count of 3 and remove indels and loci with mean depth across individuals below the 2.5th percentile and above the 97.5th percentile across all loci.
- Full pipeline: alignment/mapping [ANGSD, GATK] -> registration [GATK] -> stage not stated [Picard, Strelka, VCFtools, VEP]

### Invasion genomics uncover contrasting scenarios of genetic diversity in a widespread marine invader. (PNAS 2021)

- DOI: 10.1073/pnas.2116211118 | PMCID: PMC8713979 | PMID: 34911766
- Version used: **0.1.14**
- Evidence: Finally, variants were filtered using vcftools v0.1.14 ( 53 ) so that only biallelic SNPs with a Phred quality score above 13 were retained.
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7.15, Trimmomatic v0.36] -> alignment/mapping [BWA v0.7.15, Picard v2.6.0] -> variant calling [BCFtools v1.9] -> stage not stated [PLINK v1.90b, VCFtools v0.1.14]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Version used: **0.1.13**
- Evidence: We calculated nucleotide diversity (π) and heterozygosity ( H ) for each species or population in VCFtools version 0.1.13 ( 69 ).
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### Linked supergenes underlie split sex ratio and social organization in an ant. (PNAS 2021)

- DOI: 10.1073/pnas.2101427118 | PMCID: PMC8609651 | PMID: 34772805
- Version used: **0.1.13**
- Evidence: We called variants using Samtools mpileup version 1.8 ( 72 ) and filtered the genotypes for missing data (20% per locus, −max-missing 0.8), minor allele count (−mac 2), and minimum depth (−minDP 1) with VCFtools version 0.1.13 ( 73 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.8] -> variant calling [VCFtools v0.1.13] -> visualisation [R] -> stage not stated [GEMMA v0.94]

### Relict inland mangrove ecosystem reveals Last Interglacial sea levels. (PNAS 2021)

- DOI: 10.1073/pnas.2024518118 | PMCID: PMC8522267 | PMID: 34607943
- Version used: **0.1.14**
- Evidence: Processed data from iPyrad were filtered using VCFtools v0.1.14 ( 32 ) following the approach outlined below.
- Full pipeline: differential/statistical testing [BEAST] -> simulation/modelling [BEAST] -> stage not stated [Python, VCFtools v0.1.14]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **0.1.15**
- Evidence: For calculating multidimensional scaling (MDS) plots and AMOVA, first genotypes with a coverage <10 were removed from gvcf-files using vcftools v0.1.15 ( 89 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### High frequency of an otherwise rare phenotype in a small and isolated tiger population. (PNAS 2021)

- DOI: 10.1073/pnas.2025273118 | PMCID: PMC8488692 | PMID: 34518374
- Evidence: We removed loci with missing data for more than 10% of samples and samples with genotype calls at less than 50 loci during the filtering using VCFtools ( 105 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [BCFtools, BWA] -> variant calling [GATK, VCFtools] -> stage not stated [Picard]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Version used: **0.1.17**
- Evidence: To evaluate the degree of genetic isolation among pepper species, we estimated Weir and Cockeram’s weighted Fst for all pairwise combinations of species using VCFtools version 0.1.17 ( 46 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: We first filtered the vcf file of each sample with vcftools and the list of SNPs used in the phylogenetic tree (options –positions and –recode of vcftools).
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### The genomics of ecological flexibility, large brains, and long lives in capuchin monkeys revealed with fecalFACS. (PNAS 2021)

- DOI: 10.1073/pnas.2010632118 | PMCID: PMC7896301 | PMID: 33574059
- Evidence: Among the genes present in each window in the top 0.5% and top 0.1% of F ST values, we searched for SNPs with high or moderate effects using SnpEff and identified those SNPs with high F ST values (> 0.75) using VCFtools.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> stage not stated [BCFtools, Picard, SAMtools, SnpEff, VCFtools]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: Variants in repetitive regions and with more than two alleles were filtered out from the resulting file using VCFtools ( 78 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Population dynamics of Baltic herring since the Viking Age revealed by ancient DNA and genomics. (PNAS 2022)

- DOI: 10.1073/pnas.2208703119 | PMCID: PMC9659336 | PMID: 36282902
- Version used: **0.1.16**
- Evidence: Genetic diversity (π) was estimated in 100-kb windows along the nuclear genome using VCFtools v0.1.16 ( 54 ) for each of the four Baltic populations: WBASs, CBASs, CBSSs, and GSSs, with two or three samples representing each population.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [GATK, IQ-TREE v1.6.12, VCFtools v0.1.16]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **0.1.12**
- Evidence: We used vcftools v0.1.12 ( 102 ) to calculate average F ST and θπ with 50-kb sliding windows and a step size of 25 kb.
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Evidence: VCFtools ( 57 ) was used to remove all filtered positions and monomorphic alleles across the entire dataset.
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Version used: **0.1.16**
- Evidence: Finally, using VCFtools (v.0.1.16), we removed indels and sites with a phred-scaled quality score <30 or missing individuals >0.5 ( 73 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### Uncovering the enigmatic evolution of bears in greater depth: The hybrid origin of the Asiatic black bear. (PNAS 2022)

- DOI: 10.1073/pnas.2120307119 | PMCID: PMC9351369 | PMID: 35858381
- Version used: **0.1.14**
- Evidence: South Group) using VCFtools version 0.1.14 ( 60 ).
- Full pipeline: read trimming [BWA v0.78] -> alignment/mapping [BWA v0.78, MAFFT v7.486, SAMtools v0.1.18] -> registration [GATK v3.7] -> structure determination [RAxML v8.2.11] -> stage not stated [Picard v1.87, VCFtools v0.1.14]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **0.1.15**
- Evidence: Finally, we combined the sequence-capture dataset with the WGS dataset using vcf-merge [vcftools v.0.1.15 ( 80 )].
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Genomic insights into zokors' phylogeny and speciation in China. (PNAS 2022)

- DOI: 10.1073/pnas.2121819119 | PMCID: PMC9171634 | PMID: 35512099
- Evidence: Genetic differentiation parameters, such as F ST and π, were calculated by VCFtools.
- Full pipeline: alignment/mapping [GATK] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BUSCO, RAxML, VCFtools]

### Neo-sex chromosome evolution shapes sex-dependent asymmetrical introgression barrier. (PNAS 2022)

- DOI: 10.1073/pnas.2119382119 | PMCID: PMC9171612 | PMID: 35512091
- Evidence: D. nasuta specific alleles, we calculated allele frequency within each species with VCFtools ( 33 ) and selected the sites with allele frequency difference greater than 0.3.
- Full pipeline: alignment/mapping [GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [VCFtools]

### A generalist-specialist trade-off between switchgrass cytotypes impacts climate adaptation and geographic range. (PNAS 2022)

- DOI: 10.1073/pnas.2118879119 | PMCID: PMC9169841 | PMID: 35377798
- Evidence: For LD analysis, r 2 was calculated in PLINK v1.9 ( 93 ) and VCFtools ( 85 ) between hiF st SNPs across all samples and within each of the three gene pools using diploid-only genotypes.
- Full pipeline: alignment/mapping [BWA] -> variant calling [ADMIXTURE, PLINK v1.9, SAMtools, VCFtools] -> registration [GATK v3.0, Picard] -> stage not stated [R]

### Sympatric speciation of the spiny mouse from Evolution Canyon in Israel substantiated genomically and methylomically. (PNAS 2022)

- DOI: 10.1073/pnas.2121822119 | PMCID: PMC9060526 | PMID: 35320043
- Evidence: SNP was called for each individual using GATK, and genetic diversity was calculated by VCFtools.
- Full pipeline: stage not stated [Bismark, DELLY, GATK, Metascape, R, VCFtools]

### <i>TIC236</i> gain-of-function mutations unveil the link between plastid division and plastid protein import. (PNAS 2022)

- DOI: 10.1073/pnas.2123353119 | PMCID: PMC8931380 | PMID: 35275795
- Evidence: Poor-quality SNPs with a mapping quality < 60 or with a depth < 3 or >200 were filtered out using vcftools ( 37 ).
- Full pipeline: read trimming [Cutadapt v1.3, R, edgeR] -> alignment/mapping [BWA, TopHat, VCFtools] -> normalisation [R, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [SAMtools]

### Stabilizing selection on Atlantic cod supergenes through a millennium of extensive exploitation. (PNAS 2022)

- DOI: 10.1073/pnas.2114904119 | PMCID: PMC8872764 | PMID: 35165196
- Evidence: Deviations from Hardy–Weinberg expectations for the three supergenes were tested with the -hardy option in the vcftools ( 84 ) software package v0.1.13.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R] -> stage not stated [VCFtools]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: The SNPs only dataset was also filtered for a minor allele count ≥ 2 and reduced to biallelic SNPs only using VCFtools ( 77 ) (git 1.14).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Version used: **0.1.13**
- Evidence: Then, SNPs with allele frequencies below 20% and a depth distribution of all sites below 2.5% or above 97.5% were filtered using VCFtools v.0.1.13 ( 65 ).
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We used VCFtools ( 90 ) to calculate Weir and Cockerham Fst at each variant position.
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **0.1.16**
- Evidence: Variant calling was performed in Platypus ( 86 ) and variants were filtered with proportion of missing data of 0.2 and MAF of 0.01 using VCFtools 0.1.16 ( 87 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Version used: **0.1.15**
- Evidence: SNPs within a VCF file containing collection-wide SNP data were filtered with VCFtools (v0.1.15) ( 79 ) to remove positions with a minor allele frequency < 5% and missing data > 10%.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Evidence: Indels, which are phylogenetically uninformative, were removed using vcftools ( 31 ).
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Large-scale functional screen identifies genetic variants with splicing effects in modern and archaic humans. (PNAS 2023)

- DOI: 10.1073/pnas.2218308120 | PMCID: PMC10214146 | PMID: 37192163
- Version used: **0.1.16**
- Evidence: LD between pairs of 1KGP SNPs was calculated using vcftools (v0.1.16) ( 110 ) using the parameters: --hap-r2 --maf 0.01 --ld-window-bp 1000000 --min-r2 0.2 --max-missing 1.
- Full pipeline: stage not stated [VCFtools v0.1.16, VEP]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Evidence: To obtain a high-quality set of variants, we then used VCFtools ( 95 ) to remove loci with a quality score less than 30, a mean depth of coverage less than 5 or greater than 20, a genotyping rate less than 95%, and a minor allele count less than 1.
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Ancient DNA from a lost Negev Highlands desert grape reveals a Late Antiquity wine lineage. (PNAS 2023)

- DOI: 10.1073/pnas.2213563120 | PMCID: PMC10151551 | PMID: 37068234
- Evidence: For each dataset, we used VCFtools ( 70 ) to assert that each locus had genotype call in at least 75% of the samples, and each of the samples had genotype calls in at least 60% of the loci with the minimal read depth of five (for nonpanel samples).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.5] -> variant calling [GATK, VCFtools] -> dimensionality reduction/clustering [pheatmap] -> visualisation [ggplot2]

### The genomics of linkage drag in inbred lines of sunflower. (PNAS 2023)

- DOI: 10.1073/pnas.2205783119 | PMCID: PMC10083583 | PMID: 36972449
- Evidence: The densities of SNPs and small InDels were calculated by using vcftools ( 89 ) in nonoverlapping 500-kb windows.
- Full pipeline: alignment/mapping [GATK] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.1.2, Snakemake, VCFtools]

### Aneuploidy and gene dosage regulate filamentation and host colonization by &lt;i&gt;Candida albicans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2218163120 | PMCID: PMC10089209 | PMID: 36893271
- Evidence: To identify changes in heterozygosity, the number of heterozygous positions was calculated per 1 kbp window using vcftools ( 64 ) and the genotypes assigned with GATK.
- Full pipeline: alignment/mapping [Picard, SAMtools, minimap2 v2.17] -> variant calling [VCFtools, minimap2 v2.17] -> differential/statistical testing [R] -> visualisation [Cutadapt] -> stage not stated [GATK, ImageJ, RAxML v8.2.12]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **0.1.16**
- Evidence: The nucleotide diversity was estimated in 100 kb windows using VCFtools (0.1.16) ( 91 , 92 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Evidence: Linkage disequilibrium analysis was conducted using LDkit v1.0 ( 75 ), and SNPs were filtered using VCFtools including “--thin 5,000 --remove-filtered-all --max-missing-count 6 --maf 0.03 --recode --recode-INFO-all” to eliminate low-occurrence SNPs and subsample at a spacing of 5,000 bp to avoid linkage.
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: We further filtered variants using VCFtools ( 91 ) (v0.1.15) for a minimum quality of 25 and for a maximum of 25% missing samples per site.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### Natural selection of immune and metabolic genes associated with health in two lowland Bolivian populations. (PNAS 2023)

- DOI: 10.1073/pnas.2207544120 | PMCID: PMC9910614 | PMID: 36574663
- Evidence: Derived/ancestral state was added using the fill-aa tool from VCFtools ( 91 ).
- Full pipeline: alignment/mapping [R] -> variant calling [GEMMA] -> normalisation [limma] -> stage not stated [ADMIXTURE, GCTA, VCFtools]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Evidence: Finally, we filtered raw VCF files with VCFtools ( 117 ) to retain only biallelic SNPs genotyped in at least 70% of the individuals, SNPs with quality value above 30 (--minQ 30), genotype quality above 20 (--minGQ 20) and minimum read depth above 5 (--minDP 5).
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: VCF files were filtered based on gene ID and mutation impact using VCFtools ( 116 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### Unraveling the genomic diversity and admixture history of captive tigers in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2402924121 | PMCID: PMC11441546 | PMID: 39298482
- Evidence: Observed homozygous sites were counted in each subspecies using VCFtools ( 74 ) using the “--het” flag and heterozygous sites were calculated by subtracting the (O)HOM (observed homozygosity) column from the NSITES (the total sites queried) column.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.4.1] -> variant calling [BWA v0.7.17, GATK v4.1.4.1] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.6, VCFtools, VEP]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Version used: **0.1.16**
- Evidence: We calculated the F ST between populations by using the vcftools (v0.1.16) ( 71 ) software with the following parameters: “vcftools --gzvcf vcf.gz --weir-fst-pop pop1.list --weir-fst-pop pop2.list --fst-window-size 50000 --fst-window-step 10000 --out result.” We also used vcftools to calculate the genome-wide π with the following parameters: “vcftools --gzvcf vcf.gz --window-pi 500000 -out result....
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### The role of emerging elites in the formation and development of communities after the fall of the Roman Empire. (PNAS 2024)

- DOI: 10.1073/pnas.2317868121 | PMCID: PMC11388374 | PMID: 39159385
- Evidence: Beagle PL files containing phred-scaled genotype likelihoods were generated using vcftools ( 70 ) for all individuals at 1,076,939 autosomal sites for use by fastNGSadmix.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [SAMtools] -> variant calling [VCFtools] -> normalisation [VCFtools] -> stage not stated [ADMIXTURE, Picard]

### Competing adaptations maintain nonadaptive variation in a wild cricket population. (PNAS 2024)

- DOI: 10.1073/pnas.2317879121 | PMCID: PMC11317585 | PMID: 39088392
- Evidence: To investigate this incongruity, we performed an F ST scan [10 kb window, 10 kb step size, using Weir and Cockham’s F ST implemented in vcftools ( 40 )] between samples inferred to be homozygous for inverted haplotypes in Kauai.CG and Hawaii.UH, but which expressed opposite phenotypes.
- Full pipeline: variant calling [VCFtools] -> stage not stated [R v4.0, lme4]

### The RPD3L deacetylation complex is required for facultative heterochromatin repression in &lt;i&gt;Neurospora crassa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2404770121 | PMCID: PMC11317574 | PMID: 39074265
- Evidence: Mapping of the critical mutations was performed as previously described ( 53 , 54 ) using FreeBayes and VCFtools ( 26 , 27 ).
- Full pipeline: alignment/mapping [VCFtools, freebayes] -> normalisation [R] -> dimensionality reduction/clustering [UMAP]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Version used: **0.1.16**
- Evidence: We identified genomic variants and retrieved the genomic interval where the MSS locus is located as previously described ( 26 ) using VCFtools v0.1.16 ( 58 ) and Platypus v0.8.1 ( 59 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Evidence: We performed SNPs filtering using VCFtools ( 77 ) with the following criteria to obtain higher quality SNP sets: (1) Filter out the loci where more than 80% of individuals have missing genotype data (--max-missing 0.8).
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: The heterozygosities (π) among P. × acerifolia subgenomes A, B, and C were calculated by VCFtools with the parameters “--window-pi 500000, --window-pi-step 500000” ( 116 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Version used: **0.1.16**
- Evidence: From genotyped variants, we used GATK4 and VCFtools v0.1.16 ( 76 ) to filter variant calls for missing data, coverage, and quality.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Evidence: We estimated LD (r 2 ) between these significant SNPs and the remaining SNPs on the same chromosome using vcftools (–geno-r2-positions).
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### Cross-pollination in seed-blended refuge and selection for Vip3A resistance in a lepidopteran pest as detected by genomic monitoring. (PNAS 2024)

- DOI: 10.1073/pnas.2319838121 | PMCID: PMC10990109 | PMID: 38513093
- Evidence: Genome-wide divergence and window-specific divergence for these treatment pairs were calculated using Weir and Cockerham's weighted F ST ( 59 ) for 10-, 20-, and 40-kb windows with 1-kb steps in VCFtools.
- Full pipeline: variant calling [BCFtools] -> stage not stated [ImageJ, R, VCFtools]

### Environmental radiation exposure at Chornobyl has not systematically affected the genomes or chemical mutagen tolerance phenotypes of local worms. (PNAS 2024)

- DOI: 10.1073/pnas.2314793121 | PMCID: PMC10945782 | PMID: 38442158
- Version used: **0.1.16**
- Evidence: Pi (genetic diversity) was calculated using VCFtools v.0.1.16 (–window-pi 10000) on the VCF of all Chornobyl or all non-Chornobyl samples, aligned to the CEW1 reference genome, subsampled to achieve comparable sequencing depth, and filtered for only for sites with a read depth of at least 5 for all samples.
- Full pipeline: alignment/mapping [GATK v4.3.0.0, R, SAMtools v1.11, VCFtools v0.1.16, minimap2] -> variant calling [GATK v4.3.0.0] -> stage not stated [BCFtools v1.14, Flye v2.8.1, ImageJ]

### Comparative chemical genomics in <i>Babesia</i> species identifies the alkaline phosphatase PhoD as a determinant of antiparasitic resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2312987121 | PMCID: PMC10907312 | PMID: 38377214
- Evidence: Alignments were sorted and subsequently merged into VCF files using SAMtools ( 112 ), BEDtools ( 113 ), and VCFtools ( 114 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BEDTools, BWA, Clustal Omega, PyMOL v2.3.2, SAMtools, VCFtools] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **0.1.16**
- Evidence: Then, a sliding-window approach of 50-kb sliding windows (step = 25 kb) was applied to the genome-wide SNPs in the VCF file to quantify genetic differentiation ( F ST ) using the VCFtools (v0.1.16) ( 79 ) with the parameters “-window-pi 50000 -window-pi-step 25000.” We then calculated F ST values and the top 1% and 5% of regions were identified as significant selection regions.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### The impacts of European arrival on Australian dingoes. (PNAS 2025)

- DOI: 10.1073/pnas.2421749122 | PMCID: PMC12684890 | PMID: 41284893
- Evidence: Finally, we performed a sliding window Fst scan ( 85 ) in vcftools to detect differences between pre- and postcontact imputed dingoes, checking for overlap with regions of excess European ancestry.
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [SAMtools v1.9] -> differential/statistical testing [ADMIXTURE v1.3.0] -> stage not stated [BCFtools v1.9, BEDTools, IQ-TREE v2.1.4, PLINK v1.90b, R, VCFtools]

### Anthropocene genetic diversity loss in the marine tropics. (PNAS 2025)

- DOI: 10.1073/pnas.2513012122 | PMCID: PMC12646237 | PMID: 41231948
- Version used: **0.1.14**
- Evidence: For information on additional filtering with VCFtools v.0.1.14 ( 72 ) and the identification and removal of cryptic species or contaminated individuals see the SI Appendix , Supporting Methods .
- Full pipeline: quality control [VCFtools v0.1.14] -> alignment/mapping [SAMtools v1.9, SPAdes v3.15.3] -> dimensionality reduction/clustering [ADMIXTURE v1.3, PLINK v1.9] -> stage not stated [freebayes v1.3.1]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Version used: **0.1.16**
- Evidence: Using vcftools v0.1.16-1 ( 80 ), we filtered this initial set of SNPs to those biallelic SNPs that had minimum depth of coverage (minDP) of 10, minimum genotype quality (minGQ) of 30, and were observed at least twice in the dataset (“--mac 2”).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Evolutionary histories of functional mutations during the domestication and spread of &lt;i&gt;japonica&lt;/i&gt; rice in Asia. (PNAS 2025)

- DOI: 10.1073/pnas.2514614122 | PMCID: PMC12582302 | PMID: 41115193
- Version used: **1.6**
- Evidence: ...rate = 4.5 × 10 −8 ( 121 ) adjusted for selfing with the formula r [1 − σ/(2 − σ)], where σ is the selfing rate ( 122 , 123 ). π was calculated using vcftools (v1.6) ( 124 ) and adjusted for masked regions.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, Nextflow v20.10.0] -> variant calling [PLINK v1.90] -> dimensionality reduction/clustering [R v4.3] -> stage not stated [VCFtools v1.6]

### A species interaction kick-starts ecological speciation in allopatry. (PNAS 2025)

- DOI: 10.1073/pnas.2506625122 | PMCID: PMC12557528 | PMID: 41082661
- Evidence: Raw variants were then filtered using bcftools and vcftools to retain only biallelic autosomal SNPs, thus excluding variants on the known sex chromosomes chrY and chrXIX, as well as those on chrM (mitochondrial genome) and chrUn (unassembled scaffolds).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [BCFtools, GATK, SAMtools, VCFtools, lme4]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: We further characterized population divides identified in Admixture and PCA by calculating the number of shared versus private SNPs among groups using BCFtools ( 95 ), pairwise F ST using VCFtools, and the rate of rare variant sharing among groups using VCFtools and PLINK.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Structure of a polymorphic repeat at the &lt;i&gt;CACNA1C&lt;/i&gt; schizophrenia locus. (PNAS 2025)

- DOI: 10.1073/pnas.2415650122 | PMCID: PMC12452837 | PMID: 40932769
- Evidence: LD was calculated between each SNP-VR pair using “vcftools ––hap–r2.” Supplementary Material Appendix 01 (PDF) Dataset S01 (TXT) Dataset S02 (TXT) Dataset S03 (TXT) Dataset S04 (TXT) Dataset S05 (TXT) Dataset S06 (TXT) Dataset S07 (TXT) Dataset S08 (TXT) Dataset S09 (TXT) Dataset S10 (TXT) Data, Materials, and Software Availability All study data are included in the article and/or supporting infor...
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [R, VCFtools]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Version used: **0.1.15**
- Evidence: We applied multiple filters for coverage, missingness, quality, relatedness, and minimum allele count with VCFtools v.0.1.15 ( 69 ) for downstream analyses ( SI Appendix , Methods and Dataset S1H ).
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### Repeated polyploidization shapes divergence in floral morphology in &lt;i&gt;Lithophragma bolanderi&lt;/i&gt; (Saxifragaceae). (PNAS 2025)

- DOI: 10.1073/pnas.2505119122 | PMCID: PMC12377753 | PMID: 40802687
- Evidence: Sixth, we called variants for cpDNA using GATK HaplotypeCaller with ploidy of 1 and produced individual consensus fasta files using VCFtools ( 84 ) ( SI Appendix , Supporting Text S3.8 and Fig.
- Full pipeline: read trimming [GATK v4.1.4.1, fastp] -> alignment/mapping [GATK v4.1.4.1, fastp] -> variant calling [GATK v4.1.4.1, IQ-TREE, VCFtools, fastp] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4] -> stage not stated [BUSCO, WhatsHap]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Version used: **0.1.16**
- Evidence: VCFtools (v0.1.16) ( 102 ) was used for filtering.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Suturing fragmented landscapes: Mosaic hybrid zones in plants may facilitate ecosystem resiliency. (PNAS 2025)

- DOI: 10.1073/pnas.2410941122 | PMCID: PMC12337288 | PMID: 40720662
- Version used: **0.1.16**
- Evidence: Filtering was completed for all study systems using vcftools v0.1.16 ( 75 ) under similar thresholds for missing data, quality, minor allele frequency, read depth, and observed heterozygosity ( SI Appendix , Table S3 ).
- Full pipeline: machine learning [R] -> stage not stated [VCFtools v0.1.16, vegan]

### Population structure limits the use of genomic data for predicting phenotypes and managing genetic resources in forest trees. (PNAS 2025)

- DOI: 10.1073/pnas.2425691122 | PMCID: PMC12232740 | PMID: 40560610
- Version used: **0.1.14**
- Evidence: For the final analyses, we used VCFtools v.
- Full pipeline: variant calling [R] -> differential/statistical testing [R] -> simulation/modelling [PLINK v1.90b] -> stage not stated [GCTA, VCFtools v0.1.14]

### An ancient origin of the naked grains of maize. (PNAS 2025)

- DOI: 10.1073/pnas.2503748122 | PMCID: PMC12207465 | PMID: 40526715
- Version used: **0.1.13**
- Evidence: We used vcftools v.0.1.13 ( 89 ) to remove nonbiallelic alleles (–min-alleles 2 to max-alleles 2), genotypes with genotype quality scores below 20 (–minGQ 20), and sites with missing data for more than 75% of samples (–max-missing 0.75).
- Full pipeline: alignment/mapping [BCFtools v1.13] -> variant calling [R v4.4.2, SAMtools v1.13, VCFtools v0.1.13] -> dimensionality reduction/clustering [R v4.4.2] -> visualisation [R v4.4.2]

### Improving polygenic prediction from whole-genome sequencing data by leveraging predicted epigenomic features. (PNAS 2025)

- DOI: 10.1073/pnas.2419202122 | PMCID: PMC12184400 | PMID: 40504151
- Evidence: Using vcftools ( 43 ), we filter out all insertions and deletions, retaining only the SNPs.
- Full pipeline: alignment/mapping [HOMER] -> stage not stated [VCFtools]

### Deep origins, distinct adaptations, and species-level status indicated for a glacial relict seal. (PNAS 2025)

- DOI: 10.1073/pnas.2503368122 | PMCID: PMC12207470 | PMID: 40493204
- Evidence: The VCF data were converted to FASTA sequences using the vcf-to-tab tool from the VCFtools package ( 89 ) and the script from https://github.com/JinfengChen/vcf-tab-to-fasta modified to work on haploid data.
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, RAxML v8.2.12, VCFtools]

### Natural dispersal is better than translocation for reducing risks of inbreeding depression in eastern black rhinoceros (&lt;i&gt;Diceros bicornis michaeli&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2414412122 | PMCID: PMC12167989 | PMID: 40460127
- Evidence: They were filtered using vcftools ( 57 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [SAMtools] -> variant calling [BCFtools] -> differential/statistical testing [emmeans] -> stage not stated [ADMIXTURE, PLINK v1.9, R, VCFtools]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: Variants were called and filtered using BCFtools (V.1.10.2) ( 53 ) and VCFtools (V.0.1.16) ( 54 ) respectively.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### Ancient DNA suggests a historical demographic decline and genetic erosion in the Atlantic bluefin tuna. (PNAS 2025)

- DOI: 10.1073/pnas.2409302122 | PMCID: PMC12130816 | PMID: 40392844
- Version used: **0.1.16**
- Evidence: 1.6 with settings filter --i “FS>60.0 || SOR>4 || MQ<30 || QD<2.0 || AC==0 || AC==AN.” Then, we removed indels and retained only, biallelic SNPs using VCFtools v.0.1.16 ( 110 ) with settings --remove-indels --min-alleles 2 --max-alleles 2.
- Full pipeline: read trimming [BWA, SAMtools v1.7, Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools v1.7] -> registration [GATK v3.7] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b, Picard, VCFtools v0.1.16]

### Distinguishing species boundaries from geographic variation. (PNAS 2025)

- DOI: 10.1073/pnas.2423688122 | PMCID: PMC12088384 | PMID: 40324080
- Version used: **0.1.13**
- Evidence: From each of our four separate assemblies, we removed individuals that had fewer than 10,000 SNPs and we removed sites that were missing in more than 75% of individuals using vcftools v.0.1.13 ( 85 ).
- Full pipeline: visualisation [ggplot2] -> stage not stated [ADMIXTURE v1.3.0, R, RAxML, VCFtools v0.1.13, tidyverse, vegan]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Evidence: F ST distributions were calculated in VCFtools ( 95 ) using 10,000 putatively neutral and independently segregating LD-pruned SNPs, randomly sampled from outside both genic regions and known structural variants ( 15 ).
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Natural variations in <i>TT8</i> and its neighboring <i>STK</i> confer yellow seed with elevated oil content in <i>Brassica juncea</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2417264122 | PMCID: PMC11804580 | PMID: 39883846
- Evidence: Fixation indices ( F st values) were calculated by VCFtools with parameters and settings “--fst-window-size 10,000 --fst-window-step 5,000” ( 90 ).
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12] -> differential/statistical testing [GEMMA] -> visualisation [Cytoscape] -> stage not stated [BUSCO, R, VCFtools, WGCNA, minimap2 v2.17]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Version used: **0.1.16**
- Evidence: We then identified SNPs in our samples using bcftools v1.18 ( 139 ) and filtered variants using vcftools v0.1.16 ( 140 ) with the following parameters: minor allele frequency of 0.05, minimum depth of 10×, minimum average quality of 40, and a maximum variant missing of 0.995.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Version used: **0.1.16**
- Evidence: Nucleotide diversity (π), F ST , and LD decay were calculated using VCFtools (v0.1.16, https://vcftools.github.io/index.html ) ( 71 ) and PopLDdecay (v3.27) ( 72 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Ultrarapid MC1R protein and associated plumage color evolution in the domestic chicken. (PNAS 2026)

- DOI: 10.1073/pnas.2605288123 | PMCID: PMC13273276 | PMID: 42268884
- Version used: **0.1.16**
- Evidence: Low-quality SNPs were hard-filtered following our previous work ( 51 , 52 ) using “QUAL < 30.0 || QD < 2.0 || MQ < 40.0 || FS > 60.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0 || SOR > 3.0.” Sites with a missingness rate >0.10 and variants with minor allele frequency < 0.1% were further filtered using VCFtools (version 0.1.16) ( 53 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [BWA v0.7.17] -> registration [GATK v3.7] -> stage not stated [Picard v2.18.6, PyMOL, SAMtools v1.9, VCFtools v0.1.16]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Evidence: For the natural populations, we used VCFtools ( 61 ) to include only biallelic variants where samples have a read depth (DP) greater than three and genotype quality (GQ) above 20.
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### D-amino acid aminotransferase1 regulates grain chalkiness in rice by modulating endoplasmic reticulum stress response. (PNAS 2026)

- DOI: 10.1073/pnas.2519395123 | PMCID: PMC12974485 | PMID: 41790945
- Evidence: Nucleotide diversity (π) and fixation index ( Fst ) for OsDAAT1 and its flanking regions (about 2 Mb) were calculated for each rice group by VCFtools software ( http://vcftool.github.io/ ) using a 100 kb window with a step size of 5 kb.
- Full pipeline: stage not stated [VCFtools]

### Domestication drives repeated evolution of sexual-asexual life cycle trade-offs in yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2526682123 | PMCID: PMC12798947 | PMID: 41505518
- Evidence: We retrieved the vcf annotations at the HO locus (chromosome 4, 46271 to 48031) from the full vcf file of 3,039 sequenced isolates using vcftools ( 43 ).
- Full pipeline: read trimming [fastp v0.24.2] -> alignment/mapping [SAMtools v1.21] -> stage not stated [BCFtools v1.21, R, VCFtools]

### Deep evolutionary conservation of a sex-determining locus without sequence homology. (PNAS 2026)

- DOI: 10.1073/pnas.2522417123 | PMCID: PMC12799146 | PMID: 41490485
- Version used: **0.1.16**
- Evidence: Low-quality variants were filtered using VCFtools v.0.1.16 (“ --minQ 20 ”) ( 52 ).
- Full pipeline: alignment/mapping [BWA v0.7.18, freebayes v1.0.2] -> variant calling [BWA v0.7.18, IQ-TREE v2.3.6, SPAdes v3.15.2, freebayes v1.0.2] -> dimensionality reduction/clustering [BWA v0.7.18, freebayes v1.0.2] -> structure determination [IQ-TREE v2.3.6] -> stage not stated [BCFtools v1.21, PLINK v1.9, R v4.4, VCFtools v0.1.16]

