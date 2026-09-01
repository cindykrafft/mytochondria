# SHAPEIT

- **Category:** statgen
- **Papers in survey:** 16
- **Journals:** Nature (9), PNAS (4), Cell (3)
- **Years:** 2021 (1), 2022 (6), 2023 (1), 2024 (2), 2025 (4), 2026 (2)
- **Pipeline stages it appears in:** variant calling (9)

## Papers

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Evidence: (2009) http://www.htslib.org/ SHAPEIT v2.r904 Delaneau et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### Ancient genomes reveal origin and rapid trans-Eurasian migration of 7<sup>th</sup> century Avar elites. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.007 | PMCID: PMC9042794 | PMID: 35366416
- Evidence: ...ools GATK v3.5 DePristo et al., 2011 https://gatk.broadinstitute.org/hc/en-us GeneImp 1.4 Spiliopoulou et al., 2017 https://pm2.phs.ed.ac.uk/geneimp/ SHAPEIT v2.r790 Delaneau et al., 2013 https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.html pMMRCalculator https://github.com/TCLamnidis/pMMRCalculator https://github.com/TCLamnidis/pMMRCalculator HaploGrep2 Kloss-Brandstätter et al.,...
- Full pipeline: read trimming [BWA v0.7.12] -> stage not stated [ANGSD v0.910, GATK v3.5, PLINK v1.9, R v4.0, SAMtools v1.3, SHAPEIT]

### Limb development genes underlie variation in human fingerprint patterns. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.008 | PMCID: PMC8740935 | PMID: 34995520
- Evidence: ...N/A PLS-PM The R CRAN https://github.com/gastonstat/plspm ; RRID: N/A PLINK v1.9 Purcell et al., 2007 https://www.cog-genomics.org/plink2 ; RRID: N/A SHAPEIT Delaneau et al., 2011 http://www.shapeitforum.com ; RRID: N/A IMPUTE2 Howie et al., 2009 https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ; RRID: SCR_013055 EIGENSOFT Price et al., 2006 https://data.broadinstitute.org/alkesgroup/EIGENSOFT...
- Full pipeline: stage not stated [Cytoscape, GCTA, IMPUTE2, ImageJ, PLINK v1.9, R v3.6, SHAPEIT]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: ...project.org/ ; RATES, https://github.com/wangc29/RATES ; RVTESTS, https://github.com/zhanxw/rvtests/ ; SAIGE, https://github.com/weizhouUMICH/SAIGE ; SHAPEIT, http://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.html ; TESLA, https://github.com/funfunchen/rareGWAMA ; VCFtools, https://vcftools.github.io/index.html .
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Evidence: Markers not appearing in both datasets were dropped and the merged panel was phased with SHAPEIT4 (v.4.2.0) 57 using the default parameters plus --sequencing and the default GRCh38 genetic map supplied with SHAPEIT.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### The genetic legacy of the expansion of Bantu-speaking peoples in Africa. (Nature 2024)

- DOI: 10.1038/s41586-023-06770-6 | PMCID: PMC10794141 | PMID: 38030719
- Evidence: For haplotype phasing of the AfricanNeo dataset, we used SHAPEIT v.2.r904 (ref.
- Full pipeline: quality control [PLINK v1.90b] -> variant calling [PLINK v1.90b, SHAPEIT, UMAP] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [Python, R]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Evidence: Genotype data on chromosome 6 were phased using SHAPEIT (v.2, release 900) 49 to obtain haplotype information.
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Evidence: Evaluation For the evaluation of the consensus haplotypes produced from 1kGP and PG-SHAPEIT phased genotypes, PAV was run with one of the consensus haplotypes as a reference and the other one as a query sequence, together with the respective haplotype assemblies for the same individual.
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: Using SHAPEIT 59 and the 1000 Genomes phase 2 reference panel, we computed haplotype blocks.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: SHAPEIT 58 (v.2.r900) was used to infer haplotypes, and imputation was done in IMPUTE2 (v.2.3.2) 59 using a 1,000 genomes reference panel phase 3 (all ancestries).
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Evidence: Phasing was performed using SHAPEIT (v.3) 88 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Evidence: The merged dataset was split by chromosome, rephased using SHAPEIT (v.2; ref.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### False discovery rate control in genome-wide association studies with population structure. (PNAS 2021)

- DOI: 10.1073/pnas.2105841118 | PMCID: PMC8501795 | PMID: 34580220
- Evidence: The haplotype distribution is approximated by an HMM in the style of SHAPEIT ( 43 – 45 ).
- Full pipeline: variant calling [SHAPEIT] -> stage not stated [PLINK]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: In brief, prephasing was first performed with SHAPEIT to infer haplotypes for samples based on autosomal SNPs with an MAF greater than 0.01.
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: Finally, genotypes were phased with SHAPEIT ( 78 ) (git 1.16 to 1.17).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Evidence: We used Beagle (28Sep18.793) ( 120 ) to do the imputation for the variants and used SHAPEIT (v2.r904) ( 121 ) to produce a more accurate set of phased genotypes on the variants.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

