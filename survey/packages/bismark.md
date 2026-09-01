# Bismark

- **Category:** genomics
- **Papers in survey:** 43
- **Journals:** PNAS (22), Nature (18), Cell (2), Lancet (1)
- **Years:** 2021 (5), 2022 (6), 2023 (8), 2024 (11), 2025 (12), 2026 (1)
- **Versions named:** 0.22.3 (6), 0.23.0 (2), 0.22.1 (2), 0.24.0 (2), 0.20.0 (1), 0.14.4 (1), 0.22.2 (1), 0.19.1 (1), 0.23.1 (1), 0.14.3 (1)
- **Pipeline stages it appears in:** alignment/mapping (35), read trimming (15), quality control (2), quantification (2), visualisation (1)

## Papers

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **0.16.3**
- Evidence: ...1) NuGEN Technologies https://github.com/nugentechnologies/NuMetRRBS nudup.py (version 2.3) NuGEN Technologies https://github.com/tecangenomics/nudup Bismark (version 0.16.3) Krueger and Andrews, 2011 https://www.bioinformatics.babraham.ac.uk/projects/bismark/ R Package: DSS (version 2.36.0) Park and Wu, 2016 https://bioconductor.org/packages/release/bioc/html/DSS.html R Package: minfi (version 1....
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Evidence: Single-cell and bulk DNA methylation sequencing data analysis Raw fastq reads from both the single-cell and bulk DNA methylation sequencing were first trimmed using TrimGalore (v0.4.3) ( https://github.com/FelixKrueger/TrimGalore ), and cleaned reads were aligned to the human hg19 or mouse mm9 genome (in silico bisulfite converted) using Bismark tool (v0.17.0) 69 .
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Reducing surgical site infections in low-income and middle-income countries (FALCON): a pragmatic, multicentre, stratified, randomised controlled trial. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)01548-8 | PMCID: PMC8586736 | PMID: 34710362
- Evidence: ...a , Hodonou Sogbo , Mireille Dokponou , Benedict Boakye , Richard Ofosu-Akromah , Ataa Kusiwaa , Kofi Yeboah Gyan , Doris Ofosuhene , Samuel Dadzie , Bismark Effah Kontor , Emmanuel Gyimah Amankwa , Godsway Solomon Attepor , Ephraim Kobby , Sheba Kunfah , Jyoti Dhiman , Rajesh Selvakumar , Gurtaj Singh , Anju Susan , Clotilde Fuentes Orozco , Laura Urdapilleta Gomez del Campo , Antonio Ramos De de...
- Full pipeline: stage not stated [Bismark]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: ...rall mCG rate > 0.5; (3) the overall mCH rate < 0.2; (4) the total final reads (combining R1 and R2) > 500,000; and (5) the total mapping rate (using Bismark 55 ) > 0.5.
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Evidence: Then R1 and R2 reads were mapped separately to the mm10 genome using Bismark with Bowtie.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **0.22.2**
- Evidence: Reads were mapped to TAIR10 using Bismark (v.0.22.2) 82 , and methylation was called using MethylDackel (v.0.5.2) ( https://github.com/dpryan79/MethylDackel ), selecting --CHG and --CHH options.
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Version used: **0.22.3**
- Evidence: Reads were aligned to the GRCh38 (hg38) reference genome using Bismark (v.0.22.3) with the ‘--non_directional’ option and default parameters. mtRNA genomic coordinates for the GRCh38 reference genome were obtained from the ENSEMBL database.
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **0.22.3**
- Evidence: BS-seq Pre-processing Raw fastq files were aligned against the ‘N-masked’ genome and deduplicated using Bismark (v.0.22.3) 83 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Widespread somatic L1 retrotransposition in normal colorectal epithelium. (Nature 2023)

- DOI: 10.1038/s41586-023-06046-z | PMCID: PMC10191854 | PMID: 37165195
- Evidence: Trimmed reads were mapped using Bismark 73 to the genome combining human reference genome (GRCh37) modified by the incorporation of L1 consensus sequences at the non-reference L1 source sites, pUC19 and lambda DNA sequences.
- Full pipeline: read trimming [Bismark] -> alignment/mapping [BWA, Bismark, minimap2] -> stage not stated [Cutadapt, DELLY, Picard]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **0.14.4**
- Evidence: The bisulfite-converted DNA sequence aligner Bismark (v.0.14.4) 53 was used to align reads to the UCSC reference genome hg19 build, and PCR deduplication was carried out using NuDup, leveraging NuGEN’s molecular tagging technology (v.2.3; https://github.com/nugentechnologies/nudup ).
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Evidence: Briefly, each read end (R1 or R2) was mapped separately using Bismark with Bowtie1 with read1 as complementary (always G to A converted) and read2 (always C to T converted) as the original strand.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **0.22.3**
- Evidence: Processing of single-cell epigenomic data Genomic reads were first trimmed with Trim Galore 0.4.4 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) in paired-end mode, and then mapped to GRCm38 with Bismark 0.22.3 72 in single-end, non-directional mode.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **0.22.1**
- Evidence: (v.0.6.3) and mapped on the GRCh38.p12 genome using Bismark (v.0.22.1) 81 and Bowtie2 (v.2.3.4.1) with the “-X 2000” option.
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **0.20.0**
- Evidence: Whole-genome bisulfite-seq Raw fastq sequences were quality- and adaptor-trimmed using Trim Galore (0.4.3.1) and reads aligned to mm10 using Bismark (0.20.0), discarding the first 8 bp from the 5′ end and the last 2 bp from the 3′ of a single-end reads.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Evidence: High-quality remaining reads were analysed using the Bismark read mapper methylation caller tool v.0.23.0.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **0.22.3**
- Evidence: The trimmed reads were aligned to hg38 using Bismark (v0.22.3) 50 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **0.23.0**
- Evidence: EM-seq data were first aligned to the S1_h1, S2, R3, R4 combined subgenomes with Bismark (v.0.23.0) with the flag ‘--local’ and duplications were removed by deduplicate_bismark.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: 81 command trim_galore --clip_R1 6 --three_prime_clip_r1 6, mapped using Bismark 82 with the command bismark --non_directional --un --ambiguous --multicore 2 and deduplicated using the command deduplicate_bismark.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: The Megalodon CG methylation calls were compared to previously published Whole-Genome Bisulfite Sequencing remapped to the new reference genomes using Bismark (SRR8346013 and SRR10356110) 21 , 48 .
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **0.23.0**
- Evidence: The resulting WGBS reads were mapped to the JI0074 reference genome using Bismark (v.0.23.0) and PCR duplicates were removed from the aligned reads.
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### The maternal X chromosome affects cognition and brain ageing in female mice. (Nature 2025)

- DOI: 10.1038/s41586-024-08457-y | PMCID: PMC11798838 | PMID: 39843739
- Evidence: Illumina’s base calling software was used to identify sequence reads and aligned to a reference genome using Bismark, an aligner optimized for bisulfite sequence calling ( http://www.bioinformatics.babraham.ac.uk/projects/bismark/ ).
- Full pipeline: quality control [FastQC] -> read trimming [STAR] -> alignment/mapping [Bismark, STAR] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, featureCounts]

### CRISPR-based targeting of DNA methylation in <i>Arabidopsis thaliana</i> by a bacterial CG-specific DNA methyltransferase. (PNAS 2021)

- DOI: 10.1073/pnas.2125016118 | PMCID: PMC8201958 | PMID: 34074795
- Evidence: Raw sequencing reads were aligned to the Arabidopsis genome (TAIR10) using Bismark ( 24 ), which was also used to generate per-position DNA methylation tracks.
- Full pipeline: alignment/mapping [Bismark, HTSeq] -> normalisation [deepTools] -> differential/statistical testing [DESeq2]

### DNA polymerase epsilon interacts with SUVH2/9 to repress the expression of genes associated with meiotic DSB hotspot in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208441119 | PMCID: PMC9564942 | PMID: 36191225
- Version used: **0.22.3**
- Evidence: Briefly, raw reads were treated using Cutadapt version 3.4 ( 71 ) to remove the adapters; the remaining reads were mapped to the genome, deduplicated, and quantified using Bismark version 0.22.3 ( 72 ) with Arabidopsis genome assembly TAIR10 ( https://www.arabidopsis.org ) and the modified parameter “–cutoff 4.” DMRs were called using an R package DMRcaller version 1.22.0 ( 73 ) with the “bins” mo...
- Full pipeline: read trimming [Bismark v0.22.3, Cutadapt, STAR v2.7.9a] -> alignment/mapping [Bismark v0.22.3, Bowtie2, Cutadapt, STAR v2.7.9a] -> quantification [Bismark v0.22.3, Cutadapt, DESeq2 v1.30.1, R, STAR v2.7.9a, featureCounts v2.0.0] -> stage not stated [ImageJ v1.52]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: DNAm was called by Bismark ( 50 ) and smoothed by the R package bsseq (v1.18) ( 51 ).
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### Sympatric speciation of the spiny mouse from Evolution Canyon in Israel substantiated genomically and methylomically. (PNAS 2022)

- DOI: 10.1073/pnas.2121822119 | PMCID: PMC9060526 | PMID: 35320043
- Evidence: Methylation data were extracted by Bismark, and DMRs were calculated by R package of DSS.
- Full pipeline: stage not stated [Bismark, DELLY, GATK, Metascape, R, VCFtools]

### Cell-free DNA profiling informs all major complications of hematopoietic cell transplantation. (PNAS 2022)

- DOI: 10.1073/pnas.2113476118 | PMCID: PMC8795552 | PMID: 35058359
- Evidence: The Bismark alignment tool ( 71 ) was used to align reads to the human genome (version hg19), remove PCR duplicates, and calculate methylation densities.
- Full pipeline: alignment/mapping [BLAST, Bismark] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: Cleaned reads were mapped to the hg38 human reference genome by Bismark with the following options: “–fastq –non_directional –unmapped –nucleotide_coverage.” Reads that mapped to multiple locations were removed and PCR duplicate reads were removed with picard.jar (v-2.4.1).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### The lack of negative association between TE load and subgenome dominance in synthesized <i>Brassica</i> allotetraploids. (PNAS 2023)

- DOI: 10.1073/pnas.2305208120 | PMCID: PMC10589682 | PMID: 37816049
- Evidence: The Bismark tool ( 66 ) was used for processing the bisulfite sequencing data with default parameters (--bowtie2 --score-min L,0,-0.2 --no-discordant --maxins 500 --dovetail --no-mixed --ignore-quals).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [R, SciPy] -> stage not stated [Bismark, Bowtie2, RepeatMasker v4.0.3]

### Tet2 deletion in CD4+ T cells disrupts Th1 lineage commitment in memory cells and enhances T follicular helper cell recall responses to viral rechallenge. (PNAS 2023)

- DOI: 10.1073/pnas.2218324120 | PMCID: PMC10483640 | PMID: 37639586
- Evidence: Alignment to the mm10 reference genome was performed using Bismark ( 34 ) v0.19.0 with options (bismark --multicore 6 --bowtie2 -N 1 $MM10 -1 $FORWARD_READS -2 $REVERSE_READS).
- Full pipeline: quality control [FastQC v0.11.4, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark, Bowtie2, DESeq2 v1.30.1, featureCounts v1.6.3] -> differential/statistical testing [DESeq2 v1.30.1, featureCounts v1.6.3] -> stage not stated [BEDTools]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Version used: **0.22.1**
- Evidence: Bisulfite sequencing data were aligned and analyzed using Bismark (v 0.22.1) to the human genome (hg38).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase. (PNAS 2024)

- DOI: 10.1073/pnas.2423270121 | PMCID: PMC11670102 | PMID: 39689177
- Evidence: Raw paired-end reads were adapter-trimmed using Trim Galore (version 0.6.10) ( 47 ) and then mapped to the hg38 genome and deduplicated using Bismark Bisulfite Mapper (version 0.24.2) ( 48 ).
- Full pipeline: quality control [ArchR, UMAP] -> read trimming [Bismark, Python, Trim Galore v0.6.10, Trimmomatic v0.39] -> alignment/mapping [Bismark, Trim Galore v0.6.10, Trimmomatic v0.39] -> dimensionality reduction/clustering [ArchR, UMAP]

### Genetic variation drives cancer cell adaptation to ECM stiffness. (PNAS 2024)

- DOI: 10.1073/pnas.2403062121 | PMCID: PMC11441511 | PMID: 39302966
- Evidence: The trimmed reads were aligned to the reference genome (hg38) using the Bismark tool (version 0.23.1) ( 62 ).
- Full pipeline: read trimming [Bismark] -> alignment/mapping [Bismark] -> differential/statistical testing [R v4.1.3, edgeR] -> stage not stated [GSEA v4.1.0, ImageJ, Trim Galore]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: Subsequently, the resulting clean reads were aligned to the converted reference genome (Gmax v4, Phytozome) using the Bismark program (v0.20.0) ( 45 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Imprinted X chromosome inactivation in marsupials: The paternal X arrives at the egg with a silent DNA methylation profile. (PNAS 2024)

- DOI: 10.1073/pnas.2412185121 | PMCID: PMC11388282 | PMID: 39190362
- Evidence: Bismark ( 47 ) Genome Preparation (bismark version 0.22.3) was run to generate the requisite files for the Bismark Genome Alignment.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bismark] -> normalisation [R] -> stage not stated [SAMtools]

### An atlas of the tomato epigenome reveals that KRYPTONITE shapes TAD-like boundaries through the control of H3K9ac distribution. (PNAS 2024)

- DOI: 10.1073/pnas.2400737121 | PMCID: PMC11252963 | PMID: 38968127
- Version used: **0.24.0**
- Evidence: Clean reads were mapped onto tomato M82 genome ( 42 ) using Bismark (v0.24.0) ( 59 ) with option -N 1 and nucleotide coverage.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bismark v0.24.0, Bowtie2 v2.3.5] -> differential/statistical testing [BEDTools v2.28.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, R, deepTools v3.5.0]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Version used: **0.19.1**
- Evidence: Bismark (v 0.19.1, Babraham Institute) ( 34 ) mapped the reads to the Arabidopsis reference genome (TAIR10) and Col-Cen-v1.2 assembly ( 23 ).
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Germline variants in &lt;i&gt;UHRF1&lt;/i&gt; are associated with multilocus imprinting disturbance in humans and mice. (PNAS 2025)

- DOI: 10.1073/pnas.2505884122 | PMCID: PMC12403135 | PMID: 40825131
- Evidence: After adapter removal, quality filtering, and further reevaluation by FastQC, data were aligned with human build hg19, PCR duplicates were removed, and methylation information was extracted using the Bismark software ( 65 ).
- Full pipeline: quality control [Bismark, FastQC] -> read trimming [Bismark, FastQC, Trim Galore] -> alignment/mapping [Bismark, GATK v3.7, SAMtools v1.3.1] -> variant calling [GATK v3.7, SAMtools v1.3.1] -> stage not stated [ANNOVAR, VEP]

### Complementary genetic and epigenetic changes facilitate rapid adaptation to multiple global change stressors. (PNAS 2025)

- DOI: 10.1073/pnas.2422782122 | PMCID: PMC12305003 | PMID: 40663607
- Version used: **0.22.3**
- Evidence: Mapping was conducted using Bismark v0.22.3 ( 64 ) and Bowtie2 v2.2.6 with local alignments ( 65 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bismark v0.22.3, Bowtie2 v2.2.6] -> differential/statistical testing [R v3.6.0, edgeR] -> stage not stated [BEDTools, DESeq2]

### Genetic ablation of the TET family in retinal progenitor cells impairs photoreceptor development and leads to blindness. (PNAS 2025)

- DOI: 10.1073/pnas.2420091122 | PMCID: PMC11912455 | PMID: 40053367
- Evidence: We used Integrative Genomics Viewer (IGV) to visualize the bed files that were generated by Bismark Bisulfite Mapper.
- Full pipeline: visualisation [Bismark] -> stage not stated [Bioconductor]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Version used: **0.23.1**
- Evidence: Trimmed reads were aligned to reference genomes using Bismark (v0.23.1) ( 81 ) with bowtie2 (v2.1.0) ( 82 ), and methylation status was determined using the bismark_methylation_extractor (minimum coverage = 2).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### The androgen clock is an epigenetic predictor of long-term male hormone exposure. (PNAS 2025)

- DOI: 10.1073/pnas.2420087121 | PMCID: PMC11760496 | PMID: 39805019
- Version used: **0.14.3**
- Evidence: (version 0.6.7) ( 43 ) followed by mapping and methylation calling with Bismark (version 0.14.3) ( 44 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bismark v0.14.3] -> stage not stated [R]

### Exercise intensity and training alter the innate immune cell type and chromosomal origins of circulating cell-free DNA in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2406954122 | PMCID: PMC11761974 | PMID: 39805013
- Evidence: Sequencing reads were processed using Bismark ( 107 ) with nearly default settings (--maxins 800, --score_min L,0,-0.6), to remove duplicate reads, map to GRCh38 genome, and quantify methylation.
- Full pipeline: quantification [Bismark] -> stage not stated [BEDTools, SAMtools]

### DNA methylation in invertebrate genomes and cell lineage plasticity. (PNAS 2026)

- DOI: 10.1073/pnas.2510416123 | PMCID: PMC13012060 | PMID: 41790947
- Version used: **0.24.0**
- Evidence: Raw reads were quality-checked and trimmed using Trim Galore v0.6.10 (Krueger; GitHub: https://github.com/FelixKrueger/TrimGalore ), then aligned to the respective reference genomes ( P. ochraceus : GCA_010994315.2; A. californica : GCF_000002075.1 assembly AplCal3.0, Broad Institute) using Bismark v0.24.0 ( 88 , 89 ).
- Full pipeline: quality control [Bismark v0.24.0, Trim Galore v0.6.10] -> read trimming [Bismark v0.24.0, Trim Galore v0.6.10] -> alignment/mapping [Bismark v0.24.0, Trim Galore v0.6.10] -> stage not stated [R v4.5, emmeans, phytools]

