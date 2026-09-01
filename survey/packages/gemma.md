# GEMMA

- **Category:** statgen
- **Papers in survey:** 38
- **Journals:** PNAS (25), Nature (11), Science (1), Cell (1)
- **Years:** 2021 (4), 2022 (6), 2023 (4), 2024 (8), 2025 (9), 2026 (7)
- **Versions named:** 0.98.5 (4), 0.98.1 (3), 0.98.3 (2), 0.94 (2), 0.93 (1), 0.97 (1), 0.98.4 (1), 0.96 (1)
- **Pipeline stages it appears in:** differential/statistical testing (12), variant calling (3), dimensionality reduction/clustering (2), alignment/mapping (2), normalisation (1), visualisation (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Evidence: We adopted a linear mixed model built in BOLT_LMM (N > 5000) or GEMMA (N < 5000) for the association tests while accounting for the relatedness and population structure (first 20PCs).
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **0.97**
- Evidence: We computed genome-wide kinship ( Θ ) for all pairs of relevant individuals using the SNP genotypes at the above-mentioned 30.2 million DNA variants using either GEMMA (v.0.97) 64 or GCTA (v.1.26) 65 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **0.98.5**
- Evidence: GWAS was performed with GEMMA v0.98.5 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Version used: **0.98.1**
- Evidence: A genome-wide association study was performed in GEMMA (v.0.98.1) 70 using default parameters with a mixed linear model and an estimated kinship matrix.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### NK2R control of energy expenditure and feeding to treat metabolic diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-08207-0 | PMCID: PMC11602716 | PMID: 39537932
- Evidence: Metabolic phenotypes were measured as previously described 88 , and association analyses were performed with a linear mixed model, to account for relatedness and admixture, assuming an additive genetic model and adjusting for age, sex, cohort using GEMMA 89 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> stage not stated [GEMMA, Seurat v4.3.0, VEP, data.table v1.14.2, tidyverse v1.3.1]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **0.93**
- Evidence: GWAS was performed using the R package bugwas (v.0.0.0.9000) 65 , which considers the population structure using PCA, followed by GEMMA (v.0.93) to perform GWAS analysis.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Version used: **0.98.1**
- Evidence: Based on these, we performed GWAS using GEMMA (v0.98.1) 64 with parameters (gemma-0.98.1-linux-static -miss 0.9 –gk -o kinship.txt and gemma-0.98.1-linux-static -miss 0.9 -lmm -k kinship.txt).
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **0.98.1**
- Evidence: Genome-wide association study The multi-location and multi-season phenotypic dataset was used to perform GWASs with the SNP matrix using GEMMA (v.0.98.1) 74 , and employing the following parameters (gemma-0.98.1-linux-static -miss 0.9 –gk -o kinship.txt and gemma-0.98.1-linux-static -miss 0.9 -lmm -k kinship.txt).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Version used: **0.98.5**
- Evidence: Genome-wide association studies Association tests were run using a linear mixed model, with the estimated genetic relationship matrix (GRM) as a random effect, taking population structure and relatedness into account, using GEMMA v.0.98.5 (ref.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Version used: **0.98.5**
- Evidence: Fitting the linear mixed model (LMM) We used GEMMA (v0.98.5) 69 to fit the LMM and estimate the polygenic selection coefficient γ .
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Evidence: Specifically, to control for viral population structure, we constructed a viral genetic relatedness matrix (vGRM) from EBV variants after linkage disequilibrium-based pruning (sliding window of 1,000 SNPs, step of 1 SNP, r 2 < 0.4) using the GEMMA software (v0.98.5) 73 , following the recommended practice and previous work on highly linked genomes 6 , 74 , 75 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **0.98.3**
- Evidence: Dhurrin and cyanide genome-wide association GWAS were performed using a linear mixed model implemented in GEMMA (v.0.98.3) 115 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Genome evolution in an agricultural pest following adoption of transgenic crops. (PNAS 2021)

- DOI: 10.1073/pnas.2020853118 | PMCID: PMC8719884 | PMID: 34930832
- Version used: **0.98.4**
- Evidence: Following read filtering and genome alignment, we applied a Bayesian sparse linear mixed model [BSLMM; GEMMA v.0.98.4 ( 55 , 56 )] to 6,756 to 6,268 filtered SNPs to identify the genomic architecture of Cry resistance.
- Full pipeline: alignment/mapping [GEMMA v0.98.4, R] -> variant calling [BCFtools] -> differential/statistical testing [GEMMA v0.98.4] -> stage not stated [Bowtie2]

### Linked supergenes underlie split sex ratio and social organization in an ant. (PNAS 2021)

- DOI: 10.1073/pnas.2101427118 | PMCID: PMC8609651 | PMID: 34772805
- Version used: **0.94**
- Evidence: We identified regions significantly associated with colony sex ratio in 71 F. glacialis colonies ( n = 138 individuals) by performing a GWAS using a univariate linear mixed model implemented in GEMMA version 0.94 ( 74 ), with significance assessed using a Wald test.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.8] -> variant calling [VCFtools v0.1.13] -> visualisation [R] -> stage not stated [GEMMA v0.94]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Version used: **0.96**
- Evidence: Finally, GWAS was carried out using mixed linear model (MLM) from package GEMMA (version 0.96) ( 60 ) for each trait separately.
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Pan-mitogenomics reveals the genetic basis of cytonuclear conflicts in citrus hybridization, domestication, and diversification. (PNAS 2022)

- DOI: 10.1073/pnas.2206076119 | PMCID: PMC9618123 | PMID: 36260744
- Version used: **0.98.5**
- Evidence: Those filtered variations were used for the GWAS analysis and depended on linear mixed models constructed in GEMMA (v0.98.5) ( 73 ).
- Full pipeline: dimensionality reduction/clustering [PLINK v1.90b, R] -> differential/statistical testing [Python, ggplot2] -> visualisation [PLINK v1.90b, R, ggplot2] -> stage not stated [GEMMA v0.98.5, IQ-TREE v2.0, SnpEff v5.1]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Evidence: GEMMA was used to calculate the percentage of the total skin color variance that can be explained by rs75356281 ( 53 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### Electrical responses from human retinal cone pathways associate with a common genetic polymorphism implicated in myopia. (PNAS 2022)

- DOI: 10.1073/pnas.2119675119 | PMCID: PMC9173800 | PMID: 35594404
- Evidence: Association testing was performed using all of the genotyped subjects and a mixed linear model, which adjusts for intrafamilial relatedness, as implemented in the software GEMMA ( 47 ), where the electrophysiological parameters served as outcomes and allelic dosage at the rs524952 locus as a predictor.
- Full pipeline: variant calling [GEMMA] -> differential/statistical testing [GEMMA]

### Molecular parallelism in signaling function across different sexually selected ornaments in a warbler. (PNAS 2022)

- DOI: 10.1073/pnas.2120482119 | PMCID: PMC8872772 | PMID: 35165176
- Evidence: We scanned the transcriptome for SNPs associated with ornament size using a Bayesian sparse linear mixed model in the GEMMA package ( 20 ).
- Full pipeline: alignment/mapping [R, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.1.0, HISAT2 v2.1.0, ImageJ, SAMtools v1.7]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: G × P G × P associations were based on the SNPs only dataset and estimated using a linear model with GEMMA ( 88 ).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Evidence: GWAS was performed on the LD-pruned SNP (or indel) set using the linear mixed model (LMM) in the program genome-wide efficient mixed model association (GEMMA) ( 74 ) (version 0.98.1).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### Phase variation as a major mechanism of adaptation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301394120 | PMCID: PMC10334774 | PMID: 37399390
- Evidence: We determined the associations using a linear mixed model as implemented in GEMMA ( 71 ), allowing a maximum missingness of 1% (-miss parameter) and a minimum minor allele frequency of 1% (-maf parameter).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BCFtools, GEMMA, IQ-TREE, Picard, Pilon, SAMtools]

### Natural selection of immune and metabolic genes associated with health in two lowland Bolivian populations. (PNAS 2023)

- DOI: 10.1073/pnas.2207544120 | PMCID: PMC9910614 | PMID: 36574663
- Evidence: Association testing was performed using GEMMA ( 100 ), and included age and sex as covariates as well as a relatedness matrix inferred by the program from the filtered, genome-wide genotype dataset.
- Full pipeline: alignment/mapping [R] -> variant calling [GEMMA] -> normalisation [limma] -> stage not stated [ADMIXTURE, GCTA, VCFtools]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: GEMMA was used to produce a centered relationship matrix for the plastid genomes of the 60 progenitor lines and to run a univariate association study ( 60 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Higher oxygen content and transport characterize high-altitude ethnic Tibetan women with the highest lifetime reproductive success. (PNAS 2024)

- DOI: 10.1073/pnas.2403309121 | PMCID: PMC11551319 | PMID: 39432765
- Evidence: The beta value is the effect size of the minor allele. p_LRT is the P value of the likelihood ratio test implemented in GEMMA.
- Full pipeline: differential/statistical testing [GEMMA]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Evidence: Estimates of heritability, genetic correlations, and associations between individual SNPs and each migratory trait were obtained using GEMMA (genome-wide efficient mixed-model association; version 0.98.1; ( 34 )).
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Evidence: Genome-wide Efficient Mixed Model Association [GEMMA ( 87 )] was used to implement a Bayesian Sparse Linear Mixed Model [BSLMM ( 45 )] to explore the genomic architecture underlying FOI separately in devils and DFTD.
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### GWAS for behavioral traits in golden retrievers identifies genes implicated in human temperament, mental health, and cognition. (PNAS 2025)

- DOI: 10.1073/pnas.2421757122 | PMCID: PMC12684936 | PMID: 41284867
- Evidence: We tested for stratification and outliers by creating a centered relatedness matrix using the Genome-wide Efficient Mixed Model Analysis (GEMMA) Software v0.98.1 ( 75 ) which was transformed into distance matrices using the tidyverse package in R.4.2.2 ( 111 ) and visualized them on multidimensional scaling plots.
- Full pipeline: variant calling [PLINK v1.9] -> normalisation [GEMMA, tidyverse] -> dimensionality reduction/clustering [GEMMA, tidyverse] -> differential/statistical testing [MAGMA v1.10] -> visualisation [GEMMA, tidyverse] -> stage not stated [GCTA]

### Morphological and genomic responses to hurricanes arise and persist during a biological invasion. (PNAS 2025)

- DOI: 10.1073/pnas.2517322122 | PMCID: PMC12663987 | PMID: 41248293
- Version used: **0.94**
- Evidence: Briefly, we relied on a standard linear-mixed model implemented in GEMMA v.
- Full pipeline: normalisation [ImageJ] -> stage not stated [GEMMA v0.94, R, lme4]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Version used: **0.98.3**
- Evidence: Specifically, we applied a Bayesian sparse linear mixed model (BSLMM) ( 76 ) implemented in GEMMA (v0.98.3), following an approach similar to Contina et al.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Genomic analyses identify 15 risk loci and reveal &lt;i&gt;HDAC2&lt;/i&gt;, &lt;i&gt;SOX2-OT&lt;/i&gt;, and &lt;i&gt;IGF2BP2&lt;/i&gt; in a naturally occurring canine model of gastric cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2416723122 | PMCID: PMC12146739 | PMID: 40445765
- Evidence: A linear mixed model analysis using GEMMA ( 55 ) further supports six of the moderate effect loci ( Fig.
- Full pipeline: stage not stated [GEMMA, Python]

### Agouti and BMP signaling drive a naturally occurring fate conversion of melanophores to leucophores in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2424180122 | PMCID: PMC11874323 | PMID: 40305763
- Evidence: Zebrafish and other Danio species were reared at ~28 °C (14L:10D) and fed rotifers, Artemia and GEMMA Micro (Skretting).
- Full pipeline: alignment/mapping [Monocle] -> quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GEMMA]

### Natural variations in <i>TT8</i> and its neighboring <i>STK</i> confer yellow seed with elevated oil content in <i>Brassica juncea</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2417264122 | PMCID: PMC11804580 | PMID: 39883846
- Evidence: A total of 4,529,618 SNPs with MAF ≥ 0.05 and missing rate ≤ 0.1 in the population were used for the GWAS using the genome-wide efficient mixed model association program (GEMMA) ( 88 ) under a mixed-linear model.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12] -> differential/statistical testing [GEMMA] -> visualisation [Cytoscape] -> stage not stated [BUSCO, R, VCFtools, WGCNA, minimap2 v2.17]

### Host genetic regulation of rumen 6-hydroxymelatonin reduces methane emissions in dairy cattle. (PNAS 2026)

- DOI: 10.1073/pnas.2604454123 | PMCID: PMC13291679 | PMID: 42258707
- Evidence: For the exposure group, the mixed linear model (MLM) was conducted with 166 samples from all 304 dairy cattle using GEMMA with the command “-r2 0.3” as independence settings.
- Full pipeline: quality control [fastp] -> alignment/mapping [fastp] -> dimensionality reduction/clustering [R] -> differential/statistical testing [GEMMA, TwoSampleMR v0.5.6] -> stage not stated [GCTA, PLINK, VEP, lavaan]

### Genome-wide association mapping and targeted loss of function studies identify &lt;i&gt;Shroom3&lt;/i&gt; as a driver of hyperpolyploidy and ventricular dilation. (PNAS 2026)

- DOI: 10.1073/pnas.2522068123 | PMCID: PMC13229193 | PMID: 42189988
- Evidence: We performed quantitative trait loci (QTL) mapping using genome-wide efficient mixed-model analysis [GEMMA; ( 27 )] to identify the genetic loci associated with the various ploidy classes.
- Full pipeline: alignment/mapping [GEMMA] -> normalisation [clusterProfiler] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Evidence: To account for population structure, we generated a centered kinship matrix using the -gk 1 parameter in GEMMA.
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Plant-fungi interactions in &lt;i&gt;Marchantia polymorpha&lt;/i&gt; are associated with horizontal gene transfer and terpene metabolism. (PNAS 2026)

- DOI: 10.1073/pnas.2532723123 | PMCID: PMC12890914 | PMID: 41637459
- Evidence: This plot and the previous one result from a classical GWAS analysis performed with GEMMA, followed by the use of the local score technique on the SNP P -values, to amplify the signal between SNPs in LD.
- Full pipeline: quality control [Nextflow v21.10.6] -> alignment/mapping [Nextflow v21.10.6] -> differential/statistical testing [R v4.4, edgeR] -> stage not stated [BLAST, GEMMA]

### Introgression dynamics of sex-linked chromosomal inversions shape the Malawi cichlid radiation. (Science 2025)

- DOI: 10.1126/science.adr9961 | PMCID: PMC7617772 | PMID: 40504893
- Evidence: We calculated the fixation index ( F ST ) and the population branch statistic between the benthic clades using ANGSD methods ( 85 ) and performed a genome-wide association (GWA) analysis for clade adherence with GEMMA ( 86 ).
- Full pipeline: quality control [SnpEff] -> alignment/mapping [BCFtools, BWA] -> differential/statistical testing [ANGSD, GEMMA]

