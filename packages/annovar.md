# ANNOVAR

- **Category:** genomics
- **Papers in survey:** 43
- **Journals:** PNAS (21), Nature (14), Cell (6), Science (2)
- **Years:** 2021 (7), 2022 (7), 2023 (2), 2024 (7), 2025 (16), 2026 (4)
- **Versions named:** 1.0.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (6), variant calling (4), simulation/modelling (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: The functional effects of variants were annotated by ANNOVAR ( Wang et al., 2010 ; Yang and Wang, 2015 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: Variant annotation was performed using ANNOVAR (version 2016Feb01) ( Wang et al., 2010 ).
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...on et al., 2012 ) https://github.com/DReichLab/AdmixTools ANGSD - version 0.917 ( Rasmussen et al., 2011 ) http://www.popgen.dk/angsd/index.php/ANGSD ANNOVAR ( Wang et al., 2010 ) https://annovar.openbioinformatics.org ATLAS - commits 6bd2482 & 7cfc900 ( Link et al., 2017 ) https://bitbucket.org/wegmannlab/atlas/ ATLAS-Pipeline, commit 6df90e7 Wegmann lab, Ilektra Schulz bitbucket.org/wegmannlab/a...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Evidence: Ascertainment of CHIP carriage status in ARIC CHIP was previously determined using whole exome sequencing data using GATK Mutect2 118 and ANNOVAR 119 as reported by Bick et al.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### Encoding and decoding selectivity and promiscuity in the human chemokine-GPCR interaction network. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.046 | PMCID: PMC12435897 | PMID: 40273912
- Evidence: For these genes, we mapped raw genomic locations from the MC3 call set to desired transcripts using ANNOVAR.
- Full pipeline: alignment/mapping [ANNOVAR, MUSCLE, R] -> stage not stated [Cytoscape, PyMOL, TopHat]

### Global genetic interaction network of a human cell maps conserved principles and informs functional interpretation of gene co-essentiality profiles. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.044 | PMCID: PMC13281610 | PMID: 42049019
- Evidence: Discovered variants were then filtered for exonic variants using ANNOVAR.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, STAR] -> variant calling [GATK] -> visualisation [Cytoscape] -> stage not stated [ANNOVAR, R, SciPy]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: Variants were annotated with ANNOVAR 52 and excluded if present in dbsnp129.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Evidence: SNP and indels were annotated using ANNOVAR 60 .
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: Mutations that were present at an allelic fraction (AF) of less than 1%, had coverage of less than ×25 in both normal and tumour tissue exome data, were present in the gnomAD repository with a population prevalence greater than 1% and identified as lying within repetitive regions by ANNOVAR (version 599af129dbcfd4e85a2da9832c4ae59898e2f3a9) were removed.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Evolutionary histories of breast cancer and related clones. (Nature 2023)

- DOI: 10.1038/s41586-023-06333-9 | PMCID: PMC10432280 | PMID: 37495687
- Evidence: The variants identified by each caller were annotated using ANNOVAR 64 ; the variants that were listed in the 1000 Genomes Project dataset or gnomAD database with a minor allele frequency of more than or equal to 0.001 and variants within segmental duplications reported in the GenomicSuperDups database or repetitive sequences reported in the University of California, Santa Cruz (UCSC) Genome Brows...
- Full pipeline: stage not stated [ANNOVAR, MACS2, Mutect2, R, SAMtools]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Evidence: First, somatic mutations were annotated using ANNOVAR 121 .
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Evidence: Variant functional region was annotated using ANNOVAR (2020Jne07) annotate_variation.pl 85 .
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: The somatic mutation candidates were called using MuTect2 from GATK (v4.0.12) software 40 and annotated with ANNOVAR (v20191024) 41 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Evidence: Detailed functional annotation of the novel SNPs associated with T2D, EHT, HbA1c, SBP and DBP was done using ANNOVAR (release: 2020-06-08) 30 with the table_annovar.pl script.
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### Population-specific polygenic risk scores for people of Han Chinese ancestry. (Nature 2025)

- DOI: 10.1038/s41586-025-09350-y | PMCID: PMC12675292 | PMID: 41094136
- Evidence: Finally, we used ANNOVAR to annotate the new variants with data from the RefSeqGene database (updated 17 August 2020) 71 , 72 .
- Full pipeline: quantification [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, LDSC] -> differential/statistical testing [LDSC, PLINK, SAIGE] -> stage not stated [ANNOVAR, R]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Evidence: Simulation and annotation of possible human mutations For each gene included in the filtered GENCODE annotation v22, all possible single-nucleotide substitutions were simulated, annotated using ANNOVAR v2018Apr16 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: Data alignment was performed using the BWA, and variants were annotated using ANNOVAR ( https://annovar.openbioinformatics.org/en/latest/ ).
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### Geographic and age variations in mutational processes in colorectal cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09025-8 | PMCID: PMC12221974 | PMID: 40267983
- Evidence: Variant calls were then derived into genotypes for each individual and annotated using ANNOVAR 51 .
- Full pipeline: alignment/mapping [BWA, Bowtie2, fastp] -> variant calling [ANNOVAR] -> quantification [R] -> visualisation [R]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Evidence: Variants were annotated using SnpEff (v.5.1), ANNOVAR and Ensembl Variant Effect Predictor (v.107) and an array of databases for variant allele frequency and effect on the encoded protein, conservation, tissue expression, deleteriousness and disease association.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: Annotation of variants obtained from genome sequencing was performed by ANNOVAR 82 .
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: ANNOVAR ( 84 ) was used to annotate SNPs based on the GFF3 files for the reference genome.
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Accelerated expansion of pathogenic mitochondrial DNA heteroplasmies in Huntington's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2014610118 | PMCID: PMC8325154 | PMID: 34301881
- Evidence: The functional impact of mtDNA variants was determined by using the ANNOVAR pipeline ( 76 ).
- Full pipeline: alignment/mapping [SAMtools v1.6, freebayes v1.1.0] -> registration [SAMtools v1.6, freebayes v1.1.0] -> differential/statistical testing [R v3.5.0, lme4 v1.1] -> stage not stated [ANNOVAR, Picard]

### Prediction of Alzheimer's disease-specific phospholipase c gamma-1 SNV by deep learning-based approach for high-throughput screening. (PNAS 2021)

- DOI: 10.1073/pnas.2011250118 | PMCID: PMC7826347 | PMID: 33397809
- Evidence: VCF files were generated with vcfutils.pl varFilter, and functional annotation of each variant was performed with ANNOVAR (ANNOtate VARiation) software.
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [ANNOVAR, BCFtools v1.3, Cufflinks]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: The mutations, including single nucleotide variants and short insertions/deletions were functionally annotated using ANNOVAR with the corresponding databases for mouse GRCm38/mm10 ( 69 ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Evidence: Annotation of genomic SVs was performed using the package ANNOVAR (v2019Oct24) ( 114 ).
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Heterozygous LRP1 deficiency causes developmental dysplasia of the hip by impairing triradiate chondrocytes differentiation due to inhibition of autophagy. (PNAS 2022)

- DOI: 10.1073/pnas.2203557119 | PMCID: PMC9477389 | PMID: 36067312
- Evidence: Sequence variants were identified via comparisons with the national center for biotechnology information (NCBI) reference sequence NM 005529.5 and annotated by the current version of ANNOVAR (July 16, 2017; https://annovar.openbioinformatics.org/en/latest/ ) with information from Online Mendelian Inheritance in Man (OMIM), Gene Ontology, the Kyoto Encyclopedia of Genes and Genomes (KEGG) Pathway, ...
- Full pipeline: alignment/mapping [BWA v0.59] -> stage not stated [ANNOVAR, GATK, ImageJ]

### Homeostasis limits keratinocyte evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2006487119 | PMCID: PMC9436311 | PMID: 35998218
- Evidence: Each cell contains a base-pair resolution of 72 genes with genomic positional information constructed from the reference hg19 genome using ANNOVAR ( 14 ).
- Full pipeline: stage not stated [ANNOVAR, R]

### Genetics, leadership position, and well-being: An investigation with a large-scale GWAS. (PNAS 2022)

- DOI: 10.1073/pnas.2114271119 | PMCID: PMC8944770 | PMID: 35286190
- Evidence: The functional annotation and gene mapping were performed using ANNOVAR (version 2018Apr16), including types of intronic, exonic, intergenic, 5′-UTR, 3′-UTR, etc.
- Full pipeline: alignment/mapping [ANNOVAR] -> differential/statistical testing [LDSC v1.0.1] -> stage not stated [METAL, PLINK v1.07]

### High-frequency and functional mitochondrial DNA mutations at the single-cell level. (PNAS 2023)

- DOI: 10.1073/pnas.2201518120 | PMCID: PMC9910596 | PMID: 36577067
- Evidence: The functional impact of mtDNA variants was annotated with the ANNOVAR pipeline ( 84 ), and pathogenicity of mtDNA variants was evaluated using CADD ( 63 ), both of which were provided by the STAMP pipeline.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools] -> registration [SAMtools] -> stage not stated [ANNOVAR, ggplot2]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Evidence: We then used the ANNOVAR (v2020Jun08) software ( 86 ) to annotate nonsynonymous SNPs with the parameter “--aamatrixfile grantham matrix.” Deleterious nonsynonymous SNPs (dnsSNPs) were diagnosed by calculating the Grantham score (GS) ( 87 ), a measurement of the physical/chemical properties of amino acid changes.
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### Pathogenic variants in autism gene &lt;i&gt;KATNAL2&lt;/i&gt; cause hydrocephalus and disrupt neuronal connectivity by impairing ciliary microtubule dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2314702121 | PMCID: PMC11228466 | PMID: 38916997
- Evidence: Single-nucleotide variants and small indels were called with GATK HaplotypeCaller ( 62 ) and Freebayes ( 63 ), and annotated in ANNOVAR ( 64 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ANNOVAR, GATK] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [ImageJ] -> visualisation [ComplexHeatmap, ggplot2, pheatmap]

### The impact of age and number of mutations on the size of clonal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2319364121 | PMCID: PMC10895265 | PMID: 38359296
- Evidence: All mutations were annotated by SnpEff (v4.2, https://pcingola.github.io/SnpEff/ ) and ANNOVAR (v2019Dec03, http://www.openbioinformatics.org/annovar/ ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard v2.23.0] -> differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, SnpEff v4.2]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Evidence: The variant call format (VCF) files of somatic mutation were annotated using ANNOVAR ( 44 ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Evidence: Somatic variants from all cells were merged and ANNOVAR ( 54 ) was used for variant annotation.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### Germline variants in &lt;i&gt;UHRF1&lt;/i&gt; are associated with multilocus imprinting disturbance in humans and mice. (PNAS 2025)

- DOI: 10.1073/pnas.2505884122 | PMCID: PMC12403135 | PMID: 40825131
- Evidence: The generated VCF files were manipulated using VCFTools 0.1.13 ( 63 ) and annotated using ANNOVAR and Variant Effect Predictor V109 ( 64 ).
- Full pipeline: quality control [Bismark, FastQC] -> read trimming [Bismark, FastQC, Trim Galore] -> alignment/mapping [Bismark, GATK v3.7, SAMtools v1.3.1] -> variant calling [GATK v3.7, SAMtools v1.3.1] -> stage not stated [ANNOVAR, VEP]

### The fetal hydrops-associated single-residue mutation L322P disrupts mechanical but not chemical activation of the PIEZO1 ion channel. (PNAS 2025)

- DOI: 10.1073/pnas.2503793122 | PMCID: PMC12377734 | PMID: 40789030
- Evidence: ... d) use the Genome Analysis Toolkit (GATK v3.7) ( 47 ) to identify SNVs and indels; e) perform functional annotation of these variant sites using the ANNOVAR software (16 Jul 2016 version).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [ANNOVAR, AlphaFold, BEDTools, GATK v3.7, ImageJ, Picard]

### A recurrent de novo damaging variant in &lt;i&gt;EMP2&lt;/i&gt; causes progressive symmetric erythrokeratoderma. (PNAS 2025)

- DOI: 10.1073/pnas.2509896122 | PMCID: PMC12358830 | PMID: 40758889
- Evidence: The remaining variants were annotated for functional impact, population frequency, and pathogenicity using ANNOVAR.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [QuPath] -> dimensionality reduction/clustering [Monocle, Seurat, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ANNOVAR]

### Genomic analysis of 11,555 probands identifies 60 dominant congenital heart disease genes. (PNAS 2025)

- DOI: 10.1073/pnas.2420343122 | PMCID: PMC12002227 | PMID: 40127276
- Evidence: The union of these variant calls was annotated using ANNOVAR ( 73 ), multiallelic sites were split with BCFtools ( 74 ), and insertion-deletion variants were left-aligned with BCFtools ( SI Appendix ).
- Full pipeline: alignment/mapping [ANNOVAR, BCFtools] -> variant calling [ANNOVAR, BCFtools] -> machine learning [GATK v3.7, freebayes]

### Exome sequencing identifies genes for socioeconomic status in 350,770 individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2414018122 | PMCID: PMC11745334 | PMID: 39772748
- Evidence: Common variants were annotated by ANNOVAR ( 24 ), and those annotated as “exonic” or “exonic;splicing” ( n = 35,670) were included in the single-variant association analysis.
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ANNOVAR, FUMA, PLINK v2.0, SAIGE, Seurat, SnpEff]

### Unveiling the glymphatic system's role in brain aging: A comprehensive biomarker and modifiable intervention target. (PNAS 2026)

- DOI: 10.1073/pnas.2516601123 | PMCID: PMC13142974 | PMID: 42044335
- Evidence: Four approaches were employed for functional annotation and gene mapping, including ANNOVAR ( 67 ), positional mapping, eQTL mapping ( 68 ), and chromatin interaction mapping ( 69 ).
- Full pipeline: quality control [PLINK] -> alignment/mapping [ANNOVAR] -> variant calling [PLINK] -> differential/statistical testing [FUMA, LightGBM, Metascape] -> machine learning [XGBoost]

### Rhesus macaques with an &lt;i&gt;OPA1&lt;/i&gt; mutation demonstrate features of autosomal dominant optic atrophy. (PNAS 2026)

- DOI: 10.1073/pnas.2509165123 | PMCID: PMC13099570 | PMID: 41984835
- Evidence: The protein-altering effects of the variants in human coordinate were annotated with ANNOVAR (v.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [ANNOVAR, GATK, ImageJ]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Evidence: Gene regions were annotated by ANNOVAR ( 56 ) using the database GRCh37 refGene ( 57 ).
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Aberrant basal cell clonal dynamics shape early lung carcinogenesis. (Science 2025)

- DOI: 10.1126/science.ads9145 | PMCID: PMC7617789 | PMID: 40310937
- Version used: **1.0.0**
- Evidence: The somatic callers were annotated against database sources including COSMIC (v.75, https://cancer.sanger.ac.uk/cosmic ) ( 64 ), RefSeq and other in silico prediction tools using ANNOVAR v1.0.0 ( 65 ).
- Full pipeline: alignment/mapping [SAMtools] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.24.0] -> visualisation [R, UMAP, ggplot2] -> stage not stated [ANNOVAR v1.0.0, Seurat v5.0.1, Slingshot]

