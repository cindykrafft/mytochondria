# SnpEff

- **Category:** genomics
- **Papers in survey:** 80
- **Journals:** PNAS (45), Nature (26), Science (4), Cell (4), Lancet (1)
- **Years:** 2021 (9), 2022 (14), 2023 (15), 2024 (10), 2025 (24), 2026 (8)
- **Versions named:** 5.1 (6), 4.3 (5), 4.3t (5), 5.1d (4), 4.2 (2), 5.0 (2), 4.5 (1), 4.3p (1), 5.0e (1), 5.2 (1)
- **Pipeline stages it appears in:** variant calling (4), quality control (2), alignment/mapping (2), machine learning (1), differential/statistical testing (1)

## Papers

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Evidence: ...2009 http://bio-bwa.sourceforge.net SAMtools v1.9 Li et al., 2009 http://www.htslib.org snpEff v5.0e Cingolani et al., 2012 http://pcingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenetic analysis pipeline) GitHub https://github.com/roblanf/sarscov2phylo Minimap2 v2.17 Li, 2018 https://github.com/lh3/minimap2 trimAl v1.2 Capella-Gutiérrez et al., 2009 http://trimal.cgenomics....
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Evidence: ...p://bio-bwa.sourceforge.net SAMtools v1.9 ( Li et al., 2009 ) http://www.htslib.org snpEff v5.0e ( Cingolani et al., 2012 ) http://pcingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenetic analysis pipeline) GitHub,2022 https://github.com/roblanf/sarscov2phylo Minimap2 v2.17 ( Li, 2018 ) https://github.com/lh3/minimap2 trimAl v1.2 ( Capella-Gutiérrez et al., 2009 ) http://trim...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: For annotation of the variants, we used SnpEff-4.1a 98 tools.
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Evidence: 120 https://pcingola.github.io/SnpEff/ / SLiM 4.0.1 Haller and Messer 121 https://messerlab.org/slim/ GATK v.4.1.7 McKenna et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### Transmission of SARS-CoV-2 delta variant (AY.127) from pet hamsters to humans, leading to onward human-to-human transmission: a case study. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)00326-9 | PMCID: PMC8912929 | PMID: 35279259
- Evidence: Mutation analysis Single nucleotide polymorphisms among the studied consensus sequences were compared to the reference genome (Genbank accession: MN908947.3 ) using ucsc-faToVcf 23 and annotated by SnpEff.
- Full pipeline: alignment/mapping [SnpEff] -> stage not stated [IQ-TREE v2.1.3]

### Exome sequencing and analysis of 454,787 UK Biobank participants. (Nature 2021)

- DOI: 10.1038/s41586-021-04103-z | PMCID: PMC8596853 | PMID: 34662886
- Evidence: In brief, variants were annotated using SnpEff, with the most severe consequence for each variant chosen across all protein-coding transcripts.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [LDSC, REGENIE] -> stage not stated [GCTA v1.91.7, SnpEff]

### Rare variant contribution to human disease in 281,104 UK Biobank exomes. (Nature 2021)

- DOI: 10.1038/s41586-021-03855-y | PMCID: PMC8458098 | PMID: 34375979
- Evidence: On the basis of SnpEff annotations, we defined synonymous variants as those annotated as ‘synonymous_variant’.
- Full pipeline: differential/statistical testing [R] -> stage not stated [REGENIE v2.0.2, SAIGE, SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: These variants were annotated with SNPeff 126 and the weighted sum of three main categories of variants (high, moderate and low; a description of these can be found at https://pcingola.github.io/SnpEff/se_inputoutput/#effect-prediction-details ) for each gene were calculated as SNPeff_score = high × 20 + moderate × 5 + low × 1.
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Rare variant associations with plasma protein levels in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06547-x | PMCID: PMC10567546 | PMID: 37794183
- Evidence: Based on SnpEff annotations, we defined synonymous variants as those annotated as ‘synonymous_variant’.
- Full pipeline: alignment/mapping [GATK, Mutect2 v4.2.2.0] -> variant calling [GATK, Mutect2 v4.2.2.0] -> differential/statistical testing [R] -> stage not stated [SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Long-molecule scars of backup DNA repair in BRCA1- and BRCA2-deficient cancers. (Nature 2023)

- DOI: 10.1038/s41586-023-06461-2 | PMCID: PMC10482687 | PMID: 37587346
- Evidence: The impacts of protein-coding SNVs and indels were also annotated through SnpEff (GRCh37.75 database).
- Full pipeline: alignment/mapping [BWA, Picard] -> variant calling [GATK] -> registration [Picard] -> stage not stated [R, SnpEff]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: SnpSift 109 was used to select EMS-type (G/C to A/T) transitions from the VCF file.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06063-y | PMCID: PMC10171177 | PMID: 37165196
- Version used: **4.3t**
- Evidence: Filtered mutation sets were annotated using SnpEff (v.4.3t).
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [Scanpy] -> stage not stated [Mutect2 v1.1.7, SciPy, SnpEff v4.3t, Strelka v1.0.15]

### Pan-cancer whole-genome comparison of primary and metastatic solid tumours. (Nature 2023)

- DOI: 10.1038/s41586-023-06054-z | PMCID: PMC10247378 | PMID: 37165194
- Version used: **5.1**
- Evidence: Therapeutic actionability of variants To determine the amount of actionable variants observed in each sample, we compared our variants annotated by SnpEff (v5.1) 56 to those derived from three different databases (OncoKB 57 , CIViC 58 and CGI 59 ) that were classified based on a common clinical evidence level ( https://civic.readthedocs.io/en/latest/model/evidence/level.html ) as previously descri...
- Full pipeline: stage not stated [R, SnpEff v5.1]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Evidence: Mutations were annotated using SnpEff 67 and InterProScan 45 .
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Version used: **4.5**
- Evidence: Variants were annotated using SnpEff v.4.5 ( https://snpeff.sourceforge.net/ ).
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Version used: **4.3t**
- Evidence: SnpEff (v4.3t) 18 was used for annotating and predicting the genome structural position and functional effects of identified SNPs and indels.
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Version used: **5.1**
- Evidence: Site frequency spectrum Annotations of SNPs and indels were obtained using SnpEff v.5.1 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### A haplotype-based evolutionary history of barley domestication. (Nature 2025)

- DOI: 10.1038/s41586-025-09533-7 | PMCID: PMC12629985 | PMID: 40993384
- Version used: **4.3t**
- Evidence: The effects of SNPs and indels residing in the genes of those regions were classified with SnpEff (v4.3t) 68 , and variants with high allele frequency differentiation in haplotype1 and haplotype2 were prioritized (Supplementary Table 5 ).
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [BCFtools v1.15.1, DeepVariant v1.6.0, SnpEff v4.3t, minimap2 v2.24] -> visualisation [R v3.5.1] -> stage not stated [ADMIXTURE, PLINK, SAMtools v1.16.1]

### Whole-genome sequencing of 490,640 UK Biobank participants. (Nature 2025)

- DOI: 10.1038/s41586-025-09272-9 | PMCID: PMC12443626 | PMID: 40770095
- Version used: **4.3**
- Evidence: Table 2 Numbers of variants identified in at least one individual stratified by annotation across the DRAGEN single-sample dataset annotated using SnpEff v4.3 against Ensembl Build 38.92 Annotation WGS WES Intersection Union Unique to WES Present WES (%) Unique to WGS Present WGS (%) Coding 12,226,571 11,596,546 11,522,471 12,300,646 74,075 94.28% 704,100 99.40% Splice 1,180,346 1,107,034 1,086,15...
- Full pipeline: stage not stated [SnpEff v4.3]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: Variants were annotated and filtered, and functional impact predictions were made using the SnpEff & SnpSift toolbox.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### In vivo screen of Plasmodium targets for mosquito-based malaria control. (Nature 2025)

- DOI: 10.1038/s41586-025-09039-2 | PMCID: PMC12267055 | PMID: 40399670
- Evidence: Variants were annotated using SnpEff with a custom database built from the 3D7 reference GFF from PlasmoDB (v.13.0).
- Full pipeline: alignment/mapping [GATK v3.5] -> stage not stated [ImageJ, Python v3.5, SnpEff]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: SnpEff 67 (v.4.3t) was used to annotate the SNPs, and functional significance was then categorized on the basis of their positions with respect to genes (intergenic regions, exons, introns, splicing sites, untranslated regions, upstream and downstream regions) and mutation consequences (missense, start codon gain or loss, stop codon gain or loss and splicing mutations).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: Finally, we annotated and predicted the effects of our identified SNPs using SnpEff 106 (v.55.0), to ensure a comprehensive understanding of their potential impact.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Immune evasion through mitochondrial transfer in the tumour microenvironment. (Nature 2025)

- DOI: 10.1038/s41586-024-08439-0 | PMCID: PMC11798832 | PMID: 39843734
- Version used: **5.1d**
- Evidence: The detected variants were annotated using GRCh38.p14 as the reference by SnpEff (v.5.1d) 61 and subjected to additional candidate validation by EAGLE (v.1.1.1) 62 .
- Full pipeline: stage not stated [GATK v4.1.8, Mutect2, SnpEff v5.1d]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Version used: **5.1**
- Evidence: Variants were annotated using SnpEff (v.5.1), ANNOVAR and Ensembl Variant Effect Predictor (v.107) and an array of databases for variant allele frequency and effect on the encoded protein, conservation, tissue expression, deleteriousness and disease association.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: SNP annotation was performed using SnpEff 76 (v.5.2c).
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### The evolutionary history and unique genetic diversity of Indigenous Americans. (Nature 2026)

- DOI: 10.1038/s41586-026-10406-w | PMCID: PMC13149005 | PMID: 42020734
- Evidence: Annotations from dbSNP, ClinVar and more custom annotations were retrieved using SnpSift and VEP plugins.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK, VEP] -> normalisation [VEP] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK v1.9, R, SnpEff]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **5.1d**
- Evidence: Filtered genotypes were imputed with beagle (v5.4) 102 and variant effects annotated with SnpEff (v5.1d) 103 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Mutation impacts were predicted using SnpEff 66 .
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### Homo sapiens-specific evolution unveiled by ancient southern African genomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09811-4 | PMCID: PMC12872451 | PMID: 41339558
- Evidence: Biallelic SNPs (lifted to GRCh38) were annotated with SnpEff 86 for functional effect using the hg38kg genome supported by the program.
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK v1.9, SAMtools, SnpEff]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Version used: **4.3**
- Evidence: Effects of variant categories on ADHD Quality controlled variants were functionally annotated using SnpEff v.4.3 54 , 55 , and SnpSift 54 was used to annotate information derived from dbNSFP 56 .
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Version used: **4.3**
- Evidence: For both the outlier and random replicate window sets, we annotated all SNPs using SnpEff version 4.3 ( 76 ) based on the location of SNPs in the P . major genome.
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### Genomic basis of fishing-associated selection varies with population density. (PNAS 2021)

- DOI: 10.1073/pnas.2020833118 | PMCID: PMC8713780 | PMID: 34903645
- Version used: **4.4**
- Evidence: The total set of SNPs and the outlier SNPs from each density were also used for an analysis of SNP types using SnpEff v4.4 ( 62 ).
- Full pipeline: read trimming [Cutadapt v1.16, Trimmomatic v0.36] -> alignment/mapping [ANGSD, BWA v0.7.17] -> differential/statistical testing [ggplot2] -> stage not stated [Picard v2.18.14, R v3.5, SnpEff v4.4]

### Dendritic cell paucity in mismatch repair-proficient colorectal cancer liver metastases limits immune checkpoint blockade efficacy. (PNAS 2021)

- DOI: 10.1073/pnas.2105323118 | PMCID: PMC8609309 | PMID: 34725151
- Evidence: Functional impact of single-nucleotide polymorphisms (SNPs) and indels was annotated using SnpEff ( 70 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK] -> quantification [Bioconductor, DESeq2, R] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, GSVA, SnpEff]

### SARS-CoV-2 evolution in animals suggests mechanisms for rapid variant selection. (PNAS 2021)

- DOI: 10.1073/pnas.2105253118 | PMCID: PMC8612357 | PMID: 34716263
- Evidence: SnpEff and SnpSift were used to annotate variants and predict their functional effects ( 66 , 67 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> stage not stated [GATK, Nextflow, SnpEff]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Version used: **3.1**
- Evidence: Functional annotation of the identified variants associated genes was performed using SnpEff (version 3.1) ( http://snpeff.sourceforge.net/ ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### The genomics of ecological flexibility, large brains, and long lives in capuchin monkeys revealed with fecalFACS. (PNAS 2021)

- DOI: 10.1073/pnas.2010632118 | PMCID: PMC7896301 | PMID: 33574059
- Evidence: Among the genes present in each window in the top 0.5% and top 0.1% of F ST values, we searched for SNPs with high or moderate effects using SnpEff and identified those SNPs with high F ST values (> 0.75) using VCFtools.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> stage not stated [BCFtools, Picard, SAMtools, SnpEff, VCFtools]

### Pan-mitogenomics reveals the genetic basis of cytonuclear conflicts in citrus hybridization, domestication, and diversification. (PNAS 2022)

- DOI: 10.1073/pnas.2206076119 | PMCID: PMC9618123 | PMID: 36260744
- Version used: **5.1**
- Evidence: Second, the mitochondrial and chloroplast genomic datasets were annotated in SnpEff v5.1 ( 66 ).
- Full pipeline: dimensionality reduction/clustering [PLINK v1.90b, R] -> differential/statistical testing [Python, ggplot2] -> visualisation [PLINK v1.90b, R, ggplot2] -> stage not stated [GEMMA v0.98.5, IQ-TREE v2.0, SnpEff v5.1]

### Genome-wide association identifies a missing hydrolase for tocopherol synthesis in plants. (PNAS 2022)

- DOI: 10.1073/pnas.2113488119 | PMCID: PMC9191347 | PMID: 35639691
- Evidence: To examine potential impacts of associated SNPs those passing FDR were assessed with the functional effect prediction tool SnpEff ( 16 ).
- Full pipeline: differential/statistical testing [SnpEff]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Evidence: The predicted effects of SNPs and indels on protein-coding genes were annotated with SnpEff, and variants annotated as frame_shift, stop_gained, start_lost, splice_acceptor_variant, and splice_donor_variant were designated as LoF variants.
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### <i>duper</i> is a null mutation of Cryptochrome 1 in Syrian hamsters. (PNAS 2022)

- DOI: 10.1073/pnas.2123560119 | PMCID: PMC9170138 | PMID: 35471909
- Evidence: SNPs predicted to cause a HIGH or MODERATE putative impact estimated by SnpEff ( 21 ) were being screened manually using Integrative Genomics Viewer ( 54 ) to exclude potential false-positive variants.
- Full pipeline: stage not stated [BUSCO v4.0.6, Flye v2.7, GATK, SAMtools, SnpEff]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Version used: **4.2**
- Evidence: Variants were then annotated using SnpEff (version 4.2) ( 70 ).
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### Mutational background influences <i>P. aeruginosa</i> ciprofloxacin resistance evolution but preserves collateral sensitivity robustness. (PNAS 2022)

- DOI: 10.1073/pnas.2109370119 | PMCID: PMC9169633 | PMID: 35385351
- Evidence: The impact of SNPs and INDELs was evaluated by using SnpEff ( 73 ), and annotated results were saved in the VCF format.
- Full pipeline: alignment/mapping [SAMtools] -> differential/statistical testing [R] -> stage not stated [GATK, Picard, SnpEff, freebayes]

### An integrative skeletal and paleogenomic analysis of stature variation suggests relatively reduced health for early European farmers. (PNAS 2022)

- DOI: 10.1073/pnas.2106743119 | PMCID: PMC9169634 | PMID: 35389750
- Evidence: Specifically, we compared our imputed genotype data in the full dataset of the high-coverage Loschbour individual (∼16×) ( 115 ) with down-sampled BAM files (using SAMtools -s parameter) ( 128 ) from 3× coverage to 0.3× for chromosome 1 using SnpSift ( 139 ).
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SnpEff] -> registration [GATK] -> stage not stated [PLINK v1.9, Picard]

### Purging of deleterious burden in the endangered Iberian lynx. (PNAS 2022)

- DOI: 10.1073/pnas.2110614119 | PMCID: PMC8931242 | PMID: 35238662
- Version used: **4.3i**
- Evidence: We used SnpEff v4.3i ( 45 ) to annotate variants based on a custom annotation file ( SI Appendix ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> variant calling [GATK v3.7] -> stage not stated [SnpEff v4.3i]

### Engineering and functional analysis of yeast with a monotypic 40S ribosome subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2114445119 | PMCID: PMC8833219 | PMID: 35105807
- Evidence: Finally, SNPs were identified by the HaplotypeCaller program of GATK and annotated with SnpEff ( 48 ) and were further validated by Sanger sequencing.
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> variant calling [GATK v3.5, SnpEff] -> registration [GATK v3.5] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [Picard]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Version used: **4.3a**
- Evidence: Candidate SNPs were identified using SnpEff (version 4.3a) ( 80 ), and SNPs of moderate effect were filtered using Provean ( 21 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### Conservation genetics as a management tool: The five best-supported paradigms to assist the management of threatened species. (PNAS 2022)

- DOI: 10.1073/pnas.2105076119 | PMCID: PMC8740573 | PMID: 34930821
- Evidence: Derived SNPs of coding regions are filtered for and then annotated functionally for their likely impact [e.g., SnpEff ( 87 )] or by assessing each SNP site for conservation across homologous sites of a large database; SNPs at highly conserved sites are assumed to be more deleterious [e.g., SIFT algorithm ( 88 )].
- Full pipeline: stage not stated [SnpEff]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Resulting variants were annotated using SnpEff and SnpSift.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### A suppressor screen &lt;i&gt;in C. elegans&lt;/i&gt; identifies a multiprotein interaction that stabilizes the synaptonemal complex. (PNAS 2023)

- DOI: 10.1073/pnas.2314335120 | PMCID: PMC10723054 | PMID: 38055743
- Evidence: We filtered the ENU induced mutations for homozygous variants that had a read depts of greater than 15 and a quality score greater than or equal to 200 using SnpSift ( 63 ).
- Full pipeline: alignment/mapping [BWA, GATK] -> stage not stated [AlphaFold, SnpEff]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Evidence: The SNPs were annotated using SnpEff ( 73 ) (version4.3).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### Functional genomic diversity is correlated with neutral genomic diversity in populations of an endangered rattlesnake. (PNAS 2023)

- DOI: 10.1073/pnas.2303043120 | PMCID: PMC10614936 | PMID: 37844221
- Version used: **4.3**
- Evidence: We used the reference genome annotation file (.gff) and reference genome (.fasta) to functionally annotate genome-wide SNPs using SnpEff v.4.3 ( 66 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, SnpEff v4.3] -> stage not stated [BUSCO, R]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Version used: **4.3t**
- Evidence: We used SnpEff v.4.3t ( 98 ) to evaluate the genetic load level by categorizing the derived allele mutations in the coding regions of each individual into LOF, missense, and synonymous mutations.
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### Natural genetic variation in the pheromone production of <i>C. elegans</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2221150120 | PMCID: PMC10293855 | PMID: 37339205
- Evidence: SNVs with high or moderate impact inferred from SnpEff are colored purple.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools, PLINK v1.9] -> stage not stated [GCTA, R, SnpEff]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Version used: **5.0**
- Evidence: To identify deleterious mutations, we predicted the functional effects of the polarized SNPs using both SnpEff v5.0 ( 104 ) and the Variant Effect Predictor (VEP) v99.2 ( 105 ).
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Breast cancer patient-derived whole-tumor cell culture model for efficient drug profiling and treatment response prediction. (PNAS 2023)

- DOI: 10.1073/pnas.2209856120 | PMCID: PMC9910599 | PMID: 36574653
- Evidence: The most deleterious variant (based on SnpEff) is presented per gene.
- Full pipeline: alignment/mapping [GATK] -> stage not stated [GSEA, SnpEff]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: Mutations were annotated using SnpEff ( 115 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Version used: **4.3**
- Evidence: First, we annotated synonymous and nonsynonymous mutations within coding regions using SnpEff (v4.3) ( 85 ).
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: To assess whether the putatively adaptive loci were enriched for coding or noncoding regions of the genome, the locations of outlier SNPs were categorized using SnpEff ( 37 ) and the American chestnut genome feature file (Cdentata_673_v1.1.gene_exons.gff3.gz; http://phytozome-next.jgi.doe.gov/ ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Version used: **5.1d**
- Evidence: We used SnpEff (version 5.1d; 91 ) to functionally annotate SNPs in a subset of genes; those in SGCZ on chromosome 5 (46000000-46800000) and those in genes on chromosome 1 (28792449-96508609).
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### The impact of age and number of mutations on the size of clonal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2319364121 | PMCID: PMC10895265 | PMID: 38359296
- Version used: **4.2**
- Evidence: All mutations were annotated by SnpEff (v4.2, https://pcingola.github.io/SnpEff/ ) and ANNOVAR (v2019Dec03, http://www.openbioinformatics.org/annovar/ ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard v2.23.0] -> differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, SnpEff v4.2]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **5.0**
- Evidence: SnpEff v5.0 ( 75 ) and SIFT ( https://sift.bii.a-star.edu.sg/ ) were used to identify high-confidence deleterious mutations.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Joubert syndrome 26 protein enforces compartmentalized motility of a ciliary kinesin. (PNAS 2025)

- DOI: 10.1073/pnas.2504374122 | PMCID: PMC12663925 | PMID: 41264249
- Evidence: Variants were called (freebayes v1.3.6), annotated (SnpEff), and filtered (depth > 5, allele frequency>0.8) to minimize false positives.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [FastQC] -> stage not stated [AlphaFold, ImageJ, SnpEff, freebayes v1.3.6]

### An ADAR2-mimic base editor for efficient C-to-U RNA editing in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2505269122 | PMCID: PMC12625888 | PMID: 41196347
- Version used: **5.2**
- Evidence: Editing sites were annotated with SnpEff (v.5.2).
- Full pipeline: quality control [FastQC v0.12.1, Trim Galore v0.6.10] -> read trimming [FastQC v0.12.1, HISAT2, Trim Galore v0.6.10] -> alignment/mapping [HISAT2] -> stage not stated [SAMtools v1.21, SnpEff v5.2]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: We first built a database for each Panthera species in SnpEff ( 64 ) using an annotated genome for each species.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Evolution of cross-tolerance to metals in yeast. (PNAS 2025)

- DOI: 10.1073/pnas.2505337122 | PMCID: PMC12452953 | PMID: 40928868
- Evidence: After processing and filtering ( SI Appendix , Supplementary Methods ), mutations in protein-coding genes, as identified by SnpEff ( 31 ), were retained (see below for intergenic mutations).
- Full pipeline: stage not stated [SnpEff]

### Factors underlying a latitudinal gradient in the S/G lignin monomer ratio in natural poplar variants. (PNAS 2025)

- DOI: 10.1073/pnas.2503491122 | PMCID: PMC12403099 | PMID: 40833412
- Evidence: SNPs and InDels were called using SAMtools/BCFtools and annotated with SnpEff.
- Full pipeline: dimensionality reduction/clustering [R, WGCNA] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BCFtools, SAMtools, SnpEff]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Version used: **5.1**
- Evidence: Furthermore, to assess mutational load in coding regions, we annotated our autosomal SNP dataset and predicted their functional effects using SnpEff v5.1 ( 48 ).
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### Whole-genome duplication increases genetic diversity and load in outcrossing <i>Arabidopsis arenosa</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2501739122 | PMCID: PMC12337351 | PMID: 40737318
- Version used: **5.1**
- Evidence: For indels and SNPs we used SnpEff (5.1) ( 109 ) to annotate the putative phenotypic effect of each variant.
- Full pipeline: alignment/mapping [minimap2 v2.22] -> variant calling [GATK v3.7, R] -> differential/statistical testing [vegan v2.6] -> stage not stated [SnpEff v5.1]

### Genetic rescue of Florida panthers reduced homozygosity but did not swamp ancestral genotypes. (PNAS 2025)

- DOI: 10.1073/pnas.2410945122 | PMCID: PMC12337334 | PMID: 40720660
- Evidence: To identify LOF variants we used SnpEff ( 39 , 40 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK v4.2, SAMtools] -> variant calling [GATK v4.2] -> normalisation [BEDTools] -> visualisation [BEDTools] -> stage not stated [RepeatMasker, SnpEff, tidyverse]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Evidence: We used SnpEff ( 97 ) to annotate all mutations in coding regions into different impact categories based on predicted changes to protein structure.
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: The identified variants were then annotated using SnpEff (V.5.2C) ( 55 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### The SIK3-N783Y mutation is associated with the human natural short sleep trait. (PNAS 2025)

- DOI: 10.1073/pnas.2500356122 | PMCID: PMC12088394 | PMID: 40324078
- Evidence: ...th the 1,000 Genomes ( 36 ) and ExAC ( 37 ) datasets was less than 10 −4 ; 3) was potentially deleterious because it had a “high” predicted impact in SnpEff( 38 ), or was called as “damaging” by SIFT ( 39 ), or was categorized as either “probably damaging” or “possibly damaging” by HumDiv-trained Polyphen-2 ( 40 ), 4) it did not belong to a gene with a high load of rare deleterious mutations, and ...
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> machine learning [SnpEff] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Cytoscape, ImageJ]

### Exome sequencing identifies genes for socioeconomic status in 350,770 individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2414018122 | PMCID: PMC11745334 | PMID: 39772748
- Evidence: Rare variants were annotated with SnpEff ( 62 ), and the most severe protein consequence was selected for each variant.
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ANNOVAR, FUMA, PLINK v2.0, SAIGE, Seurat, SnpEff]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Version used: **4.3t**
- Evidence: Annotations were performed with SnpEff (4.3t) ( 68 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Genome degradation in plant tissue culture. (PNAS 2026)

- DOI: 10.1073/pnas.2530182123 | PMCID: PMC13123843 | PMID: 42018421
- Version used: **5.1d**
- Evidence: SnpEff v5.1d ( 80 ) was used to evaluate the effect of mutations.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39, minimap2 v2.17] -> alignment/mapping [MUSCLE, R, SAMtools v1.13, minimap2 v2.17] -> variant calling [DeepVariant v1.6.1, minimap2 v2.17] -> stage not stated [SnpEff v5.1d]

### The contribution of historical processes to contemporary extinction risk in placental mammals. (Science 2023)

- DOI: 10.1126/science.abn5856 | PMCID: PMC10184782 | PMID: 37104572
- Version used: **5.0e**
- Evidence: Synonymous, missense and loss-of-function variants were then estimated in the program SnpEff v.5.0e( 64 ).
- Full pipeline: alignment/mapping [BWA v0.7.15] -> variant calling [BWA v0.7.15] -> differential/statistical testing [R] -> stage not stated [GATK, SnpEff v5.0e, scikit-learn v1.0.2]

### Systematic in vitro evolution in &lt;i&gt;Plasmodium falciparum&lt;/i&gt; reveals key determinants of drug resistance. (Science 2024)

- DOI: 10.1126/science.adk9893 | PMCID: PMC11809290 | PMID: 39607932
- Evidence: Functional annotation of variants was carried out using SnpEff ( 14 ) with a custom database built from the 3D7 GFF from PlasmoDB ( https://plasmodb.org/plasmo/app ).
- Full pipeline: alignment/mapping [AlphaFold, GATK v3.5] -> visualisation [Cytoscape v3.9.1] -> stage not stated [DELLY, Picard, SAMtools, SnpEff]

### Functional maps of a genomic locus reveal confinement of an enhancer by its target gene. (Science 2025)

- DOI: 10.1126/science.ads6552 | PMCID: PMC7618358 | PMID: 40966339
- Version used: **4.3p**
- Evidence: To construct the 129S1/CAST genome, mouse strain-specific variants were obtained from the Mouse Genomes Project ( 42 ), homozygous SNPs were filtered using SnpSift v4.3p ( 46 )), and bcftools v1.9 ( 47 ) was used to insert single nucleotide variants into the GRCm38/mm10 mouse genome obtained from the Ensembl database.
- Full pipeline: alignment/mapping [BWA] -> quantification [deepTools v3.0] -> normalisation [deepTools v3.0] -> visualisation [Signac] -> stage not stated [BCFtools v1.9, MACS2, SnpEff v4.3p]

### Introgression dynamics of sex-linked chromosomal inversions shape the Malawi cichlid radiation. (Science 2025)

- DOI: 10.1126/science.adr9961 | PMCID: PMC7617772 | PMID: 40504893
- Evidence: The final VCF file contained 84 million biallelic SNPs that passed stringent quality control, which we annotated with SnpEff ( 81 ).
- Full pipeline: quality control [SnpEff] -> alignment/mapping [BCFtools, BWA] -> differential/statistical testing [ANGSD, GEMMA]

