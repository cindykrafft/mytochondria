# BEDTools

- **Category:** genomics
- **Papers in survey:** 302
- **Journals:** Nature (148), PNAS (126), Cell (17), Science (11)
- **Years:** 2021 (32), 2022 (39), 2023 (58), 2024 (62), 2025 (80), 2026 (31)
- **Versions named:** 2.30.0 (42), 2.29.2 (11), 2.26.0 (9), 2.25.0 (8), 2.27.1 (6), 2.31.0 (5), 2.31.1 (4), 2.28.0 (4), 2.29.0 (3), 2.23.0 (2)
- **Pipeline stages it appears in:** alignment/mapping (53), normalisation (9), visualisation (8), quantification (7), dimensionality reduction/clustering (7), differential/statistical testing (6), quality control (5), variant calling (5), read trimming (4), machine learning (1)

## Papers

### TDP-43 condensation properties specify its RNA-binding and regulatory repertoire. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.018 | PMCID: PMC8445024 | PMID: 34380047
- Evidence: For each experiment, BEDtools ( Quinlan, 2014 ) was used to count the number of reads that mapped to a window 200 nucleotides upstream of the PAS in a strand-aware manner.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools] -> quantification [Cutadapt, DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Fiji, ImageJ, Snakemake v5.31.1] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...4 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ChIP-seq Analysis pipeline This study https://github.com/MarioPujato/NextGenAligner bedtools Quinlan and Hall, 2010 https://github.com/arq5x/bedtools2/releases HOMER Heinz et al., 2010 http://homer.ucsd.edu/homer/ STAR Dobin et al., 2013 https://github.com/alexdobin/STAR HiCUP Wingett et al., 2015 https://www.bioinformatics.babraham...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Evidence: Peaks were assigned to the nearest transcription start site within 100kb for integration with RNA-seq data and overlaps of ChIP-seq and ATAC-seq peaks were determined using bedtools.
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: DMRs were assigned to overlap a promoter if 20% of the DMR or 20% of the promoter overlapped using bedtools ‘intersect’ ( Quinlan and Hall, 2010 ).
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Version used: **2.26.0**
- Evidence: (2021) http://samtools.github.io/bcftools/bcftools.html BWA-MEM v0.7.15 Li (2013) http://bio-bwa.sourceforge.net/ bedtools v2.26.0 Quinlan and Hall (2010) https://github.com/arq5x/bedtools2 CrossMap v0.5.3 Zhao et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...-bwa.sourceforge.net BEDOPS v2.4.40 ( Neph et al., 2012 ) https://bedops.readthedocs.io/en/latest/ Bedtools 2.25.0 ( Quinlan and Hall, 2010 ) https://bedtools.readthedocs.io/en/latest/ ContamMix - version 1.0 ( Fu et al., 2013 ) https://science.umd.edu/biology/plfj/ dadi ( Gutenkunst et al., 2009 ) https://bitbucket.org/gutenkunstlab/dadi fastsimcoal2.7 ( Excoffier et al., 2013 , 2021 ) http://cmp...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: 80 Generation of consensus peak files from multiple biological replicates was performed using bedtools intersect, and analysis of overlapping peaks/peak distances was performed using bedtools intersect and bedtools closest.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: To identify regions with a statistically significant change in NSP9 binding between SND1 knockout and control cell lines, overlapping peak intervals were calculated within each time point by using bedtools intersect .
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Evidence: PicardTools ( https://broadinstitute.github.io/picard ) was used to add read group information and mark duplicates, and baseline coverage histograms were generated using BEDTools genomecov 139 , from which the 5th, 50th, and 95th percentile of coverage for each library, both genome-wide and across chromosome X, were extracted.
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Version used: **2.27.0**
- Evidence: 95 N/A snakemake 7.0.4 N/A https://github.com/snakemake/snakemake bedtools v2.27.0 N/A https://github.com/arq5x/bedtools2 vegan 2.6-2 Oksanen et al.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Version used: **2.30.0**
- Evidence: 72 https://deeptools.readthedocs.io/en/ develop/ BEDtools v2.30.0 Quinlan 73 https://bedtools.readthedocs.io/en/latest/ Seqmonk v1.47.1 Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk/ projects/seqmonk/ SeqPlots v.12.1 Stempor and Ahringer 74 https://bioconductor.org/packages/release/bioc/html/ seqplots.html R v4.1.2 R Project https://www.r-project.org/ Bioconductor Huber et al.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Evidence: 120 RRID: SCR_007322 BEDtools Quinlan and Hall 121 RRID: SCR_006646 SEACR Meers et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Mapping chromatin structure at base-pair resolution unveils a unified model of cis-regulatory element interactions. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.013 | PMCID: PMC7618578 | PMID: 41197626
- Evidence: ...b1113 https://jaspar.genereg.net/ DESeq2 https://doi.org/10.1186/s13059-014-0550-8 http://www.bioconductor.org/packages/release/bioc/html/DESeq2.html bedtools https://doi.org/10.1093/bioinformatics/btq033 https://bedtools.readthedocs.io/en/latest/ Trim_galore Babraham Institute https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ FLASh https://doi.org/10.1093/bioinformatics/btr507 John ...
- Full pipeline: read trimming [Trim Galore] -> quantification [Snakemake] -> differential/statistical testing [Snakemake] -> structure determination [Trim Galore] -> stage not stated [BEDTools, Bowtie2, DESeq2, LAMMPS, MACS2]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Version used: **2.30.0**
- Evidence: Overlap analysis for these bins was conducted using BEDTools (v.2.30.0).
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 85 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ; RRID:SCR_015687 BEDtools suite 2.26.0 Quinlan and Hall 86 https://bedtools.readthedocs.io/en/latest/index.html ; RRID:SCR_006646 Bowtie2 Langmead and Salzberg 87 https://bowtie-bio.sourceforge.net/bowtie2/index.shtml ; RRID:SCR_016368 NGSplot Shen et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **2.29.2**
- Evidence: 116 https://cmpg.unibe.ch/software/fastsimcoal27/ pixy 1.2.7.beta Korunes and Samuk 117 https://pixy.readthedocs.io/en/latest/ bedtools v2.29.2 Quinlan and Hall 118 https://bedtools.readthedocs.io/en/latest/ VEP v108.2 McLaren et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Evidence: We obtained the FASTA file for the hg38 ERVs using BEDTools.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: In brief, the genome was split into equal-sized windows (50 kb), and the number of nucleotides sequenced in each bin was calculated for each GAM sample with bedtools 57 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: The coverage of unique eccDNA fragments at each base of the genome was obtained using bedtools 46 (version 2.29.2) and stored in bigwig file.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: A union peak list for the whole dataset was obtained by merging peak sets from all cell clusters using BEDtools (RRID:SCR_006646) 73 .
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: We used ‘bedtools intersect’ with the ‘-wa -u’ parameter to calculate DMR and ATAC peak overlaps 66 (RRID: SCR_006646).
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Version used: **2.24.0**
- Evidence: Disease intersection DNM enrichment Peak sets were intersected with DNMs from 2,708 probands and 1,876 siblings using bedtools v2.24.0.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Evidence: Non-overlapping chromosome 100-kb bins of the mm10 genome (generated by “bedtools makewindows -w 100000”) were used for clustering analysis and ANN model training, and the gene body regions ±2 kb defined by the mouse GENCODE vm22 were used for cluster annotation and integration with other modalities. sn-m3C-seq-specific steps or read mapping and chromatin contact analysis Methylome sequencing read...
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Initial Upper Palaeolithic humans in Europe had recent Neanderthal ancestry. (Nature 2021)

- DOI: 10.1038/s41586-021-03335-3 | PMCID: PMC8026394 | PMID: 33828320
- Evidence: BAM files of the libraries enriched for the specific subset of the nuclear genome were further intersected with the BED files containing target SNP positions (390k, 840k, 1000k, Archaic admixture, a merged set of SNP Panels 1 and 2 or 1240k, and a merged set of SNP Panels 1, 2 and 3 or 2200k) and regions (Y chromosome) using BEDtools 53 (version: 2.24.0).
- Full pipeline: alignment/mapping [SAMtools] -> differential/statistical testing [R] -> stage not stated [BEDTools]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **2.26.0**
- Evidence: Coverage from all sites was calculated using bedtools (v.2.26.0) genomeCoverageBed 37 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Evidence: The BAM index of mapped reads corresponding to the 16 KIN-CLIP libraries was then converted to BED/bedgraph using the standard command line version of –bedtools (V2.29.1) and –samtools (V1.10) 42 .
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Normalized bigwig files were created using the normalization factors from DESeq2 as previously described 54 and bedtools genomeCoverageBed 55 .
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Evidence: We annotated the mouse genomic DNA reads identified around the integration sites with genes defined in gencode vM24 ( https://www.gencodegenes.org/pages/gencode.html ) using “bedtools intersect” 55 .
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Version used: **2.17.0**
- Evidence: Non-concordant read pairs were then removed from the BAM file using Samtools (version 1.3.1) 63 . bedtools (version 2.17.0) was used to convert BAM files to BED files and to extend each read to 15bp upstream and 22bp downstream from the read 5’-end in a stranded manner 64 , in order to account for steric hindrance of Tn5-DNA contacts 65 .
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### A transcriptional switch controls sex determination in Plasmodium falciparum. (Nature 2022)

- DOI: 10.1038/s41586-022-05509-z | PMCID: PMC9750867 | PMID: 36477538
- Version used: **2.29.1**
- Evidence: The resulting bed files were sorted and merged with bedtools (v.2.29.1) 45 .
- Full pipeline: alignment/mapping [minimap2 v2.17] -> quantification [HTSeq v0.12.4] -> visualisation [R] -> stage not stated [BEDTools v2.29.1, HISAT2 v2.0.0, SAMtools, Seurat v4.0.4, scDblFinder v1.6.0]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **2.28.0**
- Evidence: Windows within 150 bp were merged using BEDtools (v.2.28.0) 72 .
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Evidence: Aligned reads were sorted by read name using SAMtools sort -n{bam}, and all proper reads pairs (that is, reads mapped to the same chromosome and with correct read orientation) were isolated using SAMtools view -bf 0x2 and finally converted to the bed format using bedtools bamtobed -bedpe -mate1 -i{bam}.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: Genomic coordinates of the causative variant were compared with the genomic coordinates of the NUMTs using bedtools 49 .
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Version used: **2.18.1**
- Evidence: Output files were merged with bedtools (v2.18.1) intersect to select the subset of enriched regions found in both replicates.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### Ordered and deterministic cancer genome evolution after p53 loss. (Nature 2022)

- DOI: 10.1038/s41586-022-05082-5 | PMCID: PMC9402436 | PMID: 35978189
- Evidence: Raw fastq data were first mapped to the hybrid genome using bwa and then counts of reads mapping to the two trans-elements (eGFP and mKate) along with genes Clp1 and Trp53 were collected using bedtools coverage.
- Full pipeline: alignment/mapping [BEDTools]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **2.29.2**
- Evidence: To infer the local phylogeny among the 32 representative accessions, considering the diverse nucleotide evolution rate of coding and non-coding regions, we masked coding regions according to the gene prediction in DM using the maskFastaFromBed command embedded in BEDTools (v.2.29.2) (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: TF peaks that overlapped peaks called in the IgG control were removed using bedtools intersect (-v) 63 before downstream analysis.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Somatic mutation rates scale with lifespan across mammals. (Nature 2022)

- DOI: 10.1038/s41586-022-04618-z | PMCID: PMC9021023 | PMID: 35418684
- Evidence: Next, coverage information from individual mtDNA and whole-genome alignment (BAM) files was obtained using the genomecov tool in the bedtools suite (v.2.17.0) 64 .
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.17] -> stage not stated [R]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Version used: **2.27.1**
- Evidence: Reads that span either exon 19–exon 20 junction, exon 20–CE junction, CE–exon 21 junction or exon 20–exon 21 junction were quantified using bedtools (2.27.1) using the command ‘bedtools intersect -split’.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: Counts for specific junctions were tallied by parsing the STAR splice junction output tables using bedtools 44 .
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: ...tQC (Babraham Bioinformatics) (v0.11.7), UMI-tools 42 (v1.1.1), cutadapt 37 (v1.16), HISAT2 (v2.1.0) 38 , SAMtools (v1.9) 39 , deepTools 41 (v3.1.0), BEDTools 43 (v2.30.0), data.table (v1.13.2), GenomicFeatures 44 (v1.38.2), edgeR 45 , 46 (v3.28.1), and GAT 47 (v1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Brain-wide correspondence of neuronal epigenomics and distant projections. (Nature 2023)

- DOI: 10.1038/s41586-023-06823-w | PMCID: PMC10719087 | PMID: 38092919
- Evidence: 1: 100,000–200,000; and so on) using bedtools make-window, and for each single cell, we counted the methylated and total basecalls for all 100-kb bins using ALLCools generate-dataset.
- Full pipeline: stage not stated [BEDTools, SCENIC, Seurat]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: For each non-human species, we used each feature’s orthologous coordinates in hg38 and performed bedtools 82 intersect 82 , counting each human element with an overlapping element as having level 1 conservation between human and that species independent of cell type.
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Version used: **2.26.0**
- Evidence: Files were converted with SAMtools v.1.9 and BEDtools v.2.26.0 to generate bedgraph files 43 .
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### The landscape of genomic structural variation in Indigenous Australians. (Nature 2023)

- DOI: 10.1038/s41586-023-06842-7 | PMCID: PMC10733147 | PMID: 38093003
- Evidence: To identify annotated protein-coding genes within CNV regions, we used bedtools intersect with a requirement for complete gene containment within a given region (parameter -f 1.0).
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools] -> visualisation [ggplot2] -> stage not stated [BEDTools, R, RepeatMasker v4.1.2, ape (R), vegan]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: We then merged the DMRs to obtain a final non-overlapping DMR list (bedtools merge -d 0), which included 2.56 million DMRs.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: A union peak list for the whole dataset was obtained by merging peak sets from all of the cell clusters using BEDtools 91 .
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Evidence: These BAM files were then converted to fastq files using bedtools bamtofastq, and the split allele 1 and allele 2 fastq files were processed using MAPS 80 (downloaded from GitHub on 21 May 2021) as described in the standard analysis.
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: The top 5,000 overlapping FOXP3 ChIP–seq peaks were calculated by bedtools using a 50% reciprocal overlap criterion.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **2.25.0**
- Evidence: The reproducible peaks were further merged between sgNTC-transduced and sg Ikzf1 -transduced, sg Ets1 -transduced or sg Rbpj -transduced T pex or T ex samples if they overlapped by 100 bp and nucleosome-free reads from each sample were counted using bedtools (v.2.25.0).
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: We then used the BEDtools 66 intersect function to compare the peak coordinates of snATAC-seq-specific peaks with these two cell type groups of peaks.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **2.30.0**
- Evidence: Using bedtools (v.2.30.0), the single peak universe was sorted, overlapping peaks were merged, and peaks within blacklisted regions of the mm10 genome were removed.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Version used: **2.29.2**
- Evidence: To identify SOA-bound motifs, the sequences of peaks (±200 bp from the summit) with higher binding (FDR < 0.05) in males (pupa) or SOA(1–1265) were extracted using bedtools (v.2.29.2).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Evidence: Coverage tracks of aligned 18–35 nucleotide reads overlapping in sense with piRNA genes were produced using Bedtools genomeCoverageBed v.2.27.1 ( http://bedtools.readthedocs.io ) and kentUtils bedGraphToBigWig v.385 ( https://github.com/ucscGenomeBrowser/kent ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Version used: **2.30.0**
- Evidence: Exact insert sites were clustered together with bedtools (version 2.30.0) cluster within a 50-bp interval 52 .
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Version used: **2.25.0**
- Evidence: The reproducible peaks were merged between wild-type and FLCN-deficient cDC1s if they overlapped by 100-bp and then were counted from each of the 8 samples by bedtools (version 2.25.0).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Single-cell quantification of ribosome occupancy in early mouse development. (Nature 2023)

- DOI: 10.1038/s41586-023-06228-9 | PMCID: PMC10307641 | PMID: 37344592
- Evidence: These were annotated by their position within the transcript (5′ UTR, CDS and 3′ UTR) and various functional classes as detailed below using bedtools version v2.29.2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ, R v4.0, Seurat]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Version used: **2.25.0**
- Evidence: Counts were obtained for 5-kb bins using bedtools (v.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: The combined minimap2 and VecScreen adaptor hits (when present) were hard-masked in the assemblies using a WDL of the bedtools maskfasta command ( https://dockstore.org/workflows/github.com/human-pangenomics/hpp_production_workflows/MaskAssembly:master?tab=info ). bedtools maskfasta \-fi ${inputFastaFN} \-bed ~{adapterBed} \-fo ~{outputFasta} In the second cleaning step, we used VecScreen to detec...
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Recombination between heterologous human acrocentric chromosomes. (Nature 2023)

- DOI: 10.1038/s41586-023-05976-y | PMCID: PMC10172130 | PMID: 37165241
- Evidence: PHR derivation To obtain the PHRs, we aggregated the final results by considering regions with positional homology entropy greater than 0 and supported by at least 1 contig, merging with BEDtools 63 those that were less than 30 kb away, and removing merged regions shorter than 30 kb.
- Full pipeline: alignment/mapping [Python, igraph] -> stage not stated [BEDTools, PLINK v1.9, R v3.6.3, ggplot2 v3.3.3, tidyverse v1.3.0]

### Mitotic clustering of pulverized chromosomes from micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-05974-0 | PMCID: PMC10307639 | PMID: 37165191
- Evidence: We next intersected the coordinates of the breakpoints and genes using bedtools 62 .
- Full pipeline: alignment/mapping [STAR v2.7.4a] -> quantification [ImageJ] -> normalisation [DESeq2, GSEA v4.3.2, HTSeq v0.6.1p] -> differential/statistical testing [DESeq2, GSEA v4.3.2] -> stage not stated [BEDTools]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: ATAC–seq, percentage of GC, gene models and RNA-seq signal overlaps with compartments were calculated using bedtools intersect 97 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Version used: **2.30.0**
- Evidence: This was done using bedtools (version 2.30.0) in the following way: bedtools subtract -a H3K4me1_file.bed -b H3K27ac_file.bed > interm_file.bed bedtools subtract -a interm_file.bed -b H3K27me3_file.bed > primed_enhancers.bed To produce primed enhancers file bedtools intersect -a H3K4me1_file.bed -b H3K27ac_file.bed > active_enhancers.bed To produce active enhancers file bedtools intersect -a H3K4m...
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Version used: **2.30.0**
- Evidence: The CoREs of the same type coming from both sample comparisons ( C 12 A , C 12 I ) were merged together by stacking overlapping regions together (using the bedtools merge command from bedtools (v.2.30.0) 64 , 65 ), finally creating a consensus set of CoREs concatenating the two sets ( C 12 = [ C 12 A , C 12 I ] ).
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **2.30.0**
- Evidence: To account for any gene models missed by BRAKER prediction but present in the Hedin/2 transcriptome assembly, the gene models from GMAP faba transcriptome alignments and BRAKER were compared using bedtools v2.30.0, retaining only the GMAP genes that did not have an intersection with the BRAKER gene models.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: NPAS4-bound sites (no FOS) were generated using bedtools/2.27.1 intersect bed -v option to generate peaks with no NPAS4 and vice versa. bigWig visualization To generate bigWig files for ATAC-seq, ChIP–seq and CUT&RUN datasets, all aligned bam files for each replicate of a given experimental condition were pooled and converted to the BED format with the bedtools/2.27.1 bamtobed.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Aberrant phase separation and nucleolar dysfunction in rare genetic diseases. (Nature 2023)

- DOI: 10.1038/s41586-022-05682-1 | PMCID: PMC9931588 | PMID: 36755093
- Version used: **2.30.0**
- Evidence: The resulting BED file was then used to filter ClinVar 57 , COSMIC 58 , dbSNP 59 and 1000 Genomes 60 to the designated genomic coordinates of the C-terminal IDR regions using BEDtools (v.2.30.0.) 61 .
- Full pipeline: visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BEDTools v2.30.0, ColabFold, R, VEP, ggplot2]

### mRNA ageing shapes the Cap2 methylome in mammalian mRNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05668-z | PMCID: PMC9891201 | PMID: 36725932
- Version used: **2.28.0**
- Evidence: The 5′ end read coverage (representing a TSN coverage) per each genomic position was obtained using BEDTools v2.28.0 (ref.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> differential/statistical testing [ImageJ v1.53a] -> visualisation [ImageJ v1.53a] -> stage not stated [BEDTools v2.28.0]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.28.0**
- Evidence: Peaks from repetitive regions were filtered using BEDtools (v.2.28.0) 124 at each developmental stage.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### A DNA methylation atlas of normal human cell types. (Nature 2023)

- DOI: 10.1038/s41586-022-05580-6 | PMCID: PMC9811898 | PMID: 36599988
- Version used: **2.26.0**
- Evidence: Overlapping regions were dropped using bedtools (v.2.26.0) 59 .
- Full pipeline: alignment/mapping [SAMtools v1.9] -> dimensionality reduction/clustering [SciPy v1.6.3] -> differential/statistical testing [HOMER] -> stage not stated [BEDTools v2.26.0, deepTools v3.4.1, scikit-learn]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Mapped reads were converted to BAM format using samtools 75 , and bedtools bamtofastq 76 was used to obtain the reads in FASTQ format.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Evidence: We determined the distance between rREs and cCREs with the bedtools closest command (v2.27.1) 56 and compared this distance to that for a simple repeats catalogue 57 .
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Version used: **2.29.2**
- Evidence: Single-copy regions extracted in BED format and their sequences (with the command ‘bedtools complement’) were retrieved using BEDTools (v.2.29.2) 63 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Version used: **2.31.1**
- Evidence: The resulting BAM files were split into isoform specific BAM files using bedtools (version 2.31.1).
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Version used: **2.30.0**
- Evidence: Intersections were performed using bedtools (v.2.30.0) 84 and pybedtools (v.0.9.0) 85 with the following command ‘Malinois/DHS-natural_BED.intersect(ENCODE_cCRE_BED, wa=True, u=True)’ and the number of intersections was reported.
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Version used: **2.31.0**
- Evidence: Peaks identified in at least two biological replicates were merged using bedtools (v.2.31.0) 63 and were used in the following analyses.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **2.30.0**
- Evidence: VMR methylation was correlated with the expression of the closest gene, as determined with bedtools 2.30.0 81 : bedtools closest -D ‘b’ -a regions.bed -b gene_bodies.bed.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### Growth of complete ammonia oxidizers on guanidine. (Nature 2024)

- DOI: 10.1038/s41586-024-07832-z | PMCID: PMC11410670 | PMID: 39143220
- Evidence: Counts for each gene were calculated using bedtools coverage (-counts) using BAM files from bbmap and GFF files downloaded from GenBank for each genome.
- Full pipeline: alignment/mapping [ImageJ v1.54f] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ImageJ v1.54f, PyMOL, phytools] -> stage not stated [AlphaFold, BEDTools, HMMER]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Evidence: 112 ) and the 5′ position of each read (the cloned 5′-monophosphate corresponding to the position of AGO-mediated cleavage) was extracted using BEDtools 116 with CPM normalization.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Version used: **2.3.0**
- Evidence: Segments were defined as overlapping focal events if either the segment interval constituted greater than half of the focal region, or vice versa, using pybedtools and bedtools (v.2.3.0) 89 , 90 .
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### De novo variants in the RNU4-2 snRNA cause a frequent neurodevelopmental syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07773-7 | PMCID: PMC11338827 | PMID: 38991538
- Version used: **2.31.0**
- Evidence: Generating 1,000 random intergenic sequences Using the bedtools (v.2.31.0) subtractBed function 47 we retrieved regions on chromosome 12 that do not overlap with RefSeq transcripts aligned by the National Center for Biotechnology Information.
- Full pipeline: alignment/mapping [BEDTools v2.31.0, STAR] -> quantification [STAR] -> normalisation [STAR] -> stage not stated [Python, R v4.0.2, SAMtools]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Evidence: Average depth of coverage values was calculated using BEDTools genomecov (v.2.30.0), and mitochondrial haplogroups were assigned using mutserve (v.1.3.0) and haplogrep (v.2.1.25).
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Bridge RNAs direct programmable recombination of target and donor DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07552-4 | PMCID: PMC11208160 | PMID: 38926615
- Evidence: Insertion sites that were within 5 bp of each other were merged together using bedtools merge 68 and a representative insertion site was selected.
- Full pipeline: alignment/mapping [BWA, minimap2] -> dimensionality reduction/clustering [HMMER] -> stage not stated [BEDTools, BLAST, Python]

### dsRNA formation leads to preferential nuclear export and gene expression. (Nature 2024)

- DOI: 10.1038/s41586-024-07576-w | PMCID: PMC11236707 | PMID: 38898279
- Evidence: Sense–antisense-pair identification Overlapping sense–antisense pairs were identified using BEDTools intersect (v.2.3.1) 55 , requiring overlaps to occur on the opposite strand with a minimum overlap of 0.5. lncRNAs were considered in analysis as SUTs, XUTs or CUTs only if they do not overlap with other transcripts of the other types on the same strand.
- Full pipeline: read trimming [Cutadapt v2.1, TopHat v2.1.1] -> alignment/mapping [Cutadapt v2.1, TopHat v2.1.1] -> quantification [featureCounts] -> stage not stated [BEDTools, Bioconductor, DESeq2]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **2.30.0**
- Evidence: After confirming concordance, replicates were aggregated and read coverage was calculated for 10 kb consecutive windows with local smoothing: 50 kb windows with a step-length of 10 kb using the central 10 kb window coordinates using bedtools (v2.30.0) multicov.
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Plasmodium nuclear genotyping For libraries that passed nuclear-capture quality control (Supplementary Methods 5 ), we extracted alignments competitively mapped to the P. vivax and/or P. falciparum nuclear chromosome scaffolds and converted them to FASTQ format using BEDtools 90 (v.2.25.0).
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: To compute non-B-DNA density, we used the coverage command in bedtools to count the number of overlaps between each 100-kb window and non-B-DNA motifs.
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Evidence: Overlap of the regions was calculated using the intersect command of BEDTools 83 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Evidence: Alignment sam files were converted to bam files using samtools v.1.9 and bam files were converted to bed files using bedtools v.2.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Evidence: We then used BEDTools intersect (v.2.27.1) 58 to remove regions of the ATAC peak calls that directly overlapped annotated exons.
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: To generate IGV genome browser tracks for ChIP–seq and RNA-seq data, all aligned bam files for each replicate of a given experiment were pooled and converted to BED format with bedtools bamtobed and filtered to be coverted into coverageBED format using bedtools.
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Version used: **2.30.0**
- Evidence: We then performed a Fisher’s exact test, as implemented in bedtools v.2.30.0 (ref.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: To identify the reciprocal translocation breakpoints between chromosomes 4q35.1/11q24.3 and 16q23.3/17q25.3 in the CHM1 genome, we first aligned CHM1 PacBio HiFi reads to the T2T-CHM13 reference genome 4 (v.2.0) using pbmm2 (v.1.1.0) and used BEDtools 64 intersect (v.2.29.0) to define putative translocation regions based on AneuFinder analysis (described above).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Evidence: Additionally, repetitive regions of the genome (95% repetitive, masked with a 24mer and 10 kb regions where greater than 90% of bases were annotated as retrotransposons (from LAI analysis) were also excluded using BEDtools 59 subtract.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Version used: **2.27**
- Evidence: H3K9me3 signal was calculated as read counts per genomic position in the ChIP sample normalized by counts in the corresponding input sample using bedtools v2.27 (ref.
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Version used: **2.29.2**
- Evidence: The yeast genome was split into 100-kb sliding windows with 10-kb step size using bedtools v2.29.2 makewindows 87 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### On the genetic basis of tail-loss evolution in humans and apes. (Nature 2024)

- DOI: 10.1038/s41586-024-07095-8 | PMCID: PMC10901737 | PMID: 38418917
- Version used: **2.30.0**
- Evidence: The homologous regions of the 140 genes, together with 10,000 bp both upstream and downstream sequences, in the 8 species were extracted from Multiz30way alignment using bedtools (v.2.30.0) 52 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BEDTools v2.30.0, STAR v2.7.2a] -> differential/statistical testing [DESeq2 v1.40.2]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Evidence: Bedtools (v.2.28.0) was used to subtract blacklist regions (using bedtools subtract) and to identify peaks called in both replicates (using bedtools intersect).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Structural basis of ribosomal 30S subunit degradation by RNase R. (Nature 2024)

- DOI: 10.1038/s41586-024-07027-6 | PMCID: PMC10901742 | PMID: 38326618
- Evidence: After generating the bam files, bedgraph files were generated using bedtools and visualized using the IGV genome browser.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, MotionCor2] -> visualisation [BEDTools, ImageJ] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION v3.1.3]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: The BEDTools suite version 2.29.2 ( http://bedtools.readthedocs.io ) was used to create normalized read density profiles.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Version used: **2.23.0**
- Evidence: Read depth and coverage were determined using pysam ( https://github.com/pysam-developers/pysam ) and BEDtools (v.2.23.0) 79 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### Emergence of replication timing during early mammalian development. (Nature 2024)

- DOI: 10.1038/s41586-023-06872-1 | PMCID: PMC10781638 | PMID: 38123678
- Evidence: BED files of the read coordinates were generated with the BEDtools 60 (v.2.29.0) command ‘bamtobed’.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.3.5] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [BEDTools, ImageJ v1.53k, R v4.0.0, SAMtools v1.9]

### Targeted design of synthetic enhancers for selected tissues in the Drosophila embryo. (Nature 2024)

- DOI: 10.1038/s41586-023-06905-9 | PMCID: PMC10830412 | PMID: 38086418
- Evidence: Prediction on full Drosophila genome We extracted 1,001 bp sequences tiled across the Drosophila dm6 genome (downloaded from https://hgdownload.soe.ucsc.edu/goldenPath/dm6/bigZips/dm6.fa.gz ) with a stride of 20 bp using bedtools makewindows (parameters -w 1001 -s 20’) and bedtools getfasta 58 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Keras, TensorFlow v1.14.0] -> visualisation [R, UMAP] -> stage not stated [BEDTools, MACS2, ggplot2 v3.2.1]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Version used: **2.30.0**
- Evidence: We selected only the motif instances from Cluster-Buster results and merged (by using BEDTools v.2.30.0; RRID: SCR_006646 ; ref.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Peaks from each sample replicate IgG as well as marker peaks from scATAC–seq fibroblast and endoderm clusters were subtracted for peak calls for each sample using bedtools subtract -A 67 .
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Version used: **2.26.0**
- Evidence: A database of community prophage genomes (high-quality predictions n = 338) and bacterial host genomes ( n = 78, masked for prophage regions using bedtools (v.2.26.0)) was constructed 70 .
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### Somatic mutation and selection at population scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09584-w | PMCID: PMC12611758 | PMID: 41062696
- Evidence: The resulting VCF files were intersected with our panel regions using bedtools 69 and missing genotypes were annotated as REF with bcftools +missing2 (ref.
- Full pipeline: alignment/mapping [MAFFT] -> variant calling [BEDTools, GATK] -> differential/statistical testing [lme4] -> stage not stated [BCFtools, R]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Version used: **2.30.0**
- Evidence: BAM files were converted to FASTQ format using bedtools v.2.30.0 bamtofastq.
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **2.30.0**
- Evidence: The BAM files were converted to BED using bedtools v.2.30.0 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Cas9 senses CRISPR RNA abundance to regulate CRISPR spacer acquisition. (Nature 2025)

- DOI: 10.1038/s41586-025-09577-9 | PMCID: PMC12477760 | PMID: 40902823
- Evidence: Potential dRS3 sites were defined by taking the set of sites showing the best scores observed in the genome for the motif ATTCCCGCCTGCGCGGGAAT, assessed using FIMO 74 and cross-referenced with the end points of the phage integrations using bedtools 62 .
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v0.92] -> read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9, minimap2] -> stage not stated [BEDTools]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: A peak atlas was created by combining the superset of all peaks using the ‘merge’ function in the BEDTools suite (v.2.29.2).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **2.30.0**
- Evidence: Mapping statistics and fraction of reads in peaks, calculated using bedtools (v.2.30.0), are provided in Supplementary Table 12 .
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Elementary 3D organization of active and silenced E. coli genome. (Nature 2025)

- DOI: 10.1038/s41586-025-09396-y | PMCID: PMC12460168 | PMID: 40804527
- Evidence: For a summary of the procedure: The intersection between features A and B ( A ∩ B ) was calculated using bedtools intersect with a fraction overlap threshold of 0.1 (option f = 0.1).
- Full pipeline: alignment/mapping [BWA] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [BEDTools, Conda, HOMER v4.11.1]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: We therefore lifted the GRCh38 callsets to CHM13 using bedtools 73 and the liftOver tool 74 with the GRCh38 to CHM13 chain file.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **2.29.0**
- Evidence: We filtered the alignments to only those contigs that traversed each human centromere, from the p to the q arm, using BEDtools (v.2.29.0) 129 intersect.
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **2.30.0**
- Evidence: All circular sequences were extracted from the assemblies, and BEDTools (version 2.30.0) 61 was used to identify the sequences’ circular starting points.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Range extender mediates long-distance enhancer activity. (Nature 2025)

- DOI: 10.1038/s41586-025-09221-6 | PMCID: PMC12267059 | PMID: 40604280
- Evidence: Reads were then aligned to the original mm10 genome assembly and a modified version of the genome containing the corresponding insertion using bedtools getfasta 81 .
- Full pipeline: alignment/mapping [BEDTools] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER] -> stage not stated [MACS2, R, Signac]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **2.30.0**
- Evidence: Using the BEDtools (v.2.30.0) 115 command getfasta, sequences for each SCO locus were extracted from the R. canina genome assembly and written into a multifasta file.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: We used bedtools intersect (v2.30.0) with the minimum overlap fraction (-f), ranging from 0.2 to 1.0 to calculate the percentage of overlap. snRNA-seq and snATAC-seq integration We integrated our snATAC-seq with a subset of our snRNA-seq data (six high-quality samples that displayed high heterogeneity of cell types) using the addGeneIntegrationMatrix function.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Evidence: Cistrome and GREAT analysis Replicate MACS2 CUT&RUN peak files were merged, then controls (IgG and SP140) were subtracted from the HA–SP140 peak file using bedtools intersect (v.2.28.0) 65 to output a file of SP140 peaks.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: BEDTools 41 was used to identify overlapping regions of significant difference in the H3K27ac CUT&RUN with the ATAC dataset.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: We used bedtools intersect 121 to collect and survey the set of TEs located 1 kb upstream or downstream of the genomic feature category of interest.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Evidence: Isolate genotypes with a read depth lower than 20× at a given position were set to no-call. ‘gatk SortVcf’ was then used to merge the filtered variable and non-variable positions into a single VCF file. ‘bedtools subtract’ was subsequently used to remove masked positions from the reference genome and positions called as heterozygous when considering the isolates as diploid (see the section ‘Filter...
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: BEDtools maskfasta was used to create an N-masked version of the MonDom5 reference genome from the complete set of 25 million variants.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Using BEDTools 113 , we intersected the non-reference insertions with introns, exons, 5′-UTRs and 3′-UTRs from T2T-CHM13.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: Non-primary alignments were removed using samtools view (option -F 0×900) and converted to BED format using bedtools bamtobed 2.27 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **2.30.0**
- Evidence: Reads were then mapped against mm10 with Bowtie2 (2.4.4), and duplicate reads were removed with samtools (1.15.1) rmdup, and bam files were converted to bed files with bedtools (2.30.0) bamtobed.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: After this, we used BEDTools 132 (v.2.30.0) with the parameter ‘-d 30000’ to merge overlap regions that were identified within the top 5% of two values.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Version used: **2.30.0**
- Evidence: We then identified regions of overlap for all interacting TF–TF pairs described in this study using bedtools v.2.30.0 (ref.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **2.25.0**
- Evidence: The reproducible peaks were further merged between samples if they overlapped by at least 100 bp and nucleosome-free reads from each sample were counted using bedtools (v.2.25.0).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: To identify accessible regions, we converted the processed bam files to bed format using bedtools 77 and used awk to add four bases to the start site if the read was on the positive strand and remove five bases from the end site if the read was on the negative strand to correct for tn5 biases.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### In vitro reconstitution of meiotic DNA double-strand-break formation. (Nature 2025)

- DOI: 10.1038/s41586-024-08551-1 | PMCID: PMC11922769 | PMID: 39972125
- Version used: **2.25.0**
- Evidence: BAM files were further converted to BED files using the bedtools (v.2.25.0) ‘bamtobed’ command 42 .
- Full pipeline: alignment/mapping [SAMtools v1.9] -> quantification [ImageJ] -> dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.25.0]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **2.30.0**
- Evidence: Pairwise Jaccard similarities between haplotypes were estimated using BEDTools (v.2.30.0) with the ‘jaccard’ command.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Massively parallel characterization of transcriptional regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08430-9 | PMCID: PMC11903340 | PMID: 39814889
- Evidence: For each replicate, we collapsed overlapping peaks using bedtools merge (parameters “-o collapse -c 2,3,7”).
- Full pipeline: stage not stated [BEDTools]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Evidence: Overlap of various peaks and TSSs was achieved using bedtools intersect (v.2.31) 72 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: For CAGE prediction, we collected the K562 CAGE (CNhs12336) BAM file from FANTOM5 and used bedtools to extract alignment counts in peaks called from ENCODE K562 scATAC-seq data (ENCFF998SLH).
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **2.31.1**
- Evidence: To detect de novo somatic insertions of TEs, clip_disc-local.sorted.bam files were converted to bedfiles using BEDTools (v.2.31.1) 52 with the ‘bamtobed’ function.
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Regions that overlapped with the ENCODE blacklist 72 were removed using the bedtools 73 intersect function (flag --v).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Evidence: Coverage proportions across each investigated gene were calculated with BEDtools 97 and subsequently plotted on a heatmap using ggplot2 of R version 4.2.2 (Extended Data Fig.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### Earliest modern human genomes constrain timing of Neanderthal admixture. (Nature 2025)

- DOI: 10.1038/s41586-024-08420-x | PMCID: PMC11839475 | PMID: 39667410
- Evidence: We also overlapped Neanderthal segments with the intersections of the previously reported Neanderthal and Denisovan desert regions using BEDTools 35 – 37 , 66 .
- Full pipeline: read trimming [BWA v0.5.10] -> alignment/mapping [BWA v0.5.10, Bowtie2, GATK, SAMtools] -> variant calling [GATK] -> visualisation [ggplot2 v3.4.2, tidyverse v1.1.4] -> stage not stated [BEDTools]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Version used: **2.30.0**
- Evidence: Bam files were generated with SAMtools 69 , 70 (v1.9) view -bS -F 0 × 04 and bam-to-bed conversion performed with bedtools (v2.30.0) bamtobed -bedpe.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: Peaks were then extended to 400 bp using BEDtools and non-overlapping peaks between the pseudo-replicates were discarded.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **2.31.1**
- Evidence: For END-seq, peaks were called using MACS (v.1.4.3) 67 with the parameters: -nolambda, -nomodel and -keep-dup = all (keep all redundant reads) and subsequent analysis were done using bedtools (v.2.31.1) 68 and R (v.4.3.2).
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Version used: **2.23.0**
- Evidence: Summary statistics for sequencing depth and coverage were generated using BEDtools (v2.23.0) 76 and pysam ( https://github.com/pysam-developers/pysam ).
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: The sequencing depth at each site was calculated using bedtools 74 , and saturation curves were generated to confirm sufficient sequencing depth.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **2.26.0**
- Evidence: To identify broad H3K4me3 domains, those with a distance shorter than 5 kb were merged using the ‘merge’ function from BEDTools (v.2.26.0), as described previously 24 .
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Telomere-to-telomere assembly using HERRO-corrected Nanopore Simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10563-y | PMCID: PMC13323052 | PMID: 42045451
- Evidence: BEDTools 62 was used for operating with annotation BED files which were used for stratifying analysis by different kinds of regions.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BEDTools, BUSCO, Canu, Flye, QUAST]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Version used: **2.27.1**
- Evidence: Furthermore, a feature count matrix filtering alignments against the t4 isolate reference genome with mapping quality < 10 was generated with bedtools (v.2.27.1) multicov using the command bedtools multicov -p -q 10 -bams {sample1}_sorted.bam {sample2}_sorted.bam.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **2.30.0**
- Evidence: To identify potent MAPK/ERK inhibitor-responsive SOX10 targets, the nearest genes within 10 kb of 5,281 AZD6244-specific SOX10 binding peaks were identified using the closest command from bedtools (v.2.30.0) 75 and intersected with the significantly upregulated DEGs.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Evidence: To create the custom region set, we used bedtools to merge the HDMA global caCREs set with the hg38 genome TSS set.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: Furthermore, we used open-source programmes such as bedtools, GREAT, fastasplitter, HOMER and MEME for various analyses 45 , 46 .
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **2.30.0**
- Evidence: To clean raw assemblies, PacBio adapter sequences were identified using minimap2 (-cxsr -f5000 -N2000 -secondary=yes) and masked with BEDTools (v.2.30.0) 68 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Evidence: The intersection of chicken and mouse H3K27ac and ZBTB18 ChIP–seq peaks was conducted using the ‘IntersectBed’ function within bedtools.
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **2.30.0**
- Evidence: Binary files were next input into 18 chromatin states as described above and genomic annotation was performed in 200-bp resolution, using MakeSegmentation function of ChromHMM and makewindows function of bedtools (v.2.30.0) 84 .
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Cleavage of mRNAs by a minority of pachytene piRNAs improves sperm fitness. (Nature 2026)

- DOI: 10.1038/s41586-026-10102-9 | PMCID: PMC13061629 | PMID: 41639461
- Evidence: RNA PolII density was calculated using BEDTools genomecov (v.2.3.4) 67 – 71 as read coverage normalized by sequencing depth and gene length (parts per million per kb; ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.18.1]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: MACS2 was used to call peaks, filtered using bedtools and converted to bigwigs with UCSC wigtoBigwig 70 , 71 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **2.30.0**
- Evidence: Data were analysed using the nf-core/cutandrun pipeline v.3.2.2 with Nextflow v.24.04.2, using the default parameters and following software dependencies: bedtools (v.2.30.0), bowtie (v.2.4.4), deeptools (v.3.5.1), fastqc (v.0.12.1), picard (v.3.1.0), Python (v.3.9.12), samtools (v.1.17), Genrich (v.0.6.1), TrimGalore (v.0.6.6), ucsc (v.377).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### A prophage-encoded abortive infection protein preserves host and prophage spread. (Nature 2026)

- DOI: 10.1038/s41586-025-10070-6 | PMCID: PMC13043305 | PMID: 41606329
- Version used: **2.27.1**
- Evidence: 50 ) and bedtools v2.27.1 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT] -> structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.27.1, PHENIX, SAMtools v1.1]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **2.30**
- Evidence: Then, SAMtools (v1.19) and bedtools (v2.30) were used to compute the breadth of coverage of each genome.
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: BEDTools 79 and bedGraphToBigWig 80 were used to create normalized bigwig files, which were visualized using Integrated Genomics Viewer 81 .
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: In brief, the genome was split into equal-sized windows, and the number of nucleotides sequenced in each bin was calculated for each GAM sample with bedtools.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Version used: **2.30.0**
- Evidence: To accomplish this, we used the bedtools (v2.30.0) 87 closest module to identify genes that overlap with the variant or have their transcription start site or transcription end site closest to the variant.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **2.27.1**
- Evidence: Intersect function of bedtools (v.2.27.1) was used to identify H3K27ac enhancers corresponding to H3K27ac peaks not overlapping promoters and found in broader H3K36me2 domains.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Version used: **2.30.0**
- Evidence: Read counts were then obtained for 1-kb windows across the reference hg19 genome using bedtools (v.2.30.0).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### Specificity, length and luck drive gene rankings in association studies. (Nature 2026)

- DOI: 10.1038/s41586-025-09703-7 | PMCID: PMC12823407 | PMID: 41193809
- Evidence: Across all files, overlapping peaks were combined using bedtools merge 72 .
- Full pipeline: differential/statistical testing [MAGMA] -> stage not stated [BEDTools, LDSC, REGENIE, VEP]

### Response of an Afro-Palearctic bird migrant to glaciation cycles. (PNAS 2021)

- DOI: 10.1073/pnas.2023836118 | PMCID: PMC8719893 | PMID: 34949638
- Evidence: S6 ), and regions annotated as repeats by RepeatMasker ( 63 ) were masked with BEDtools ( 70 ).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> registration [GATK, Picard] -> differential/statistical testing [R v3.4.2] -> stage not stated [ANGSD, BEDTools, BUSCO, RepeatMasker]

### SARS-CoV-2 expresses a microRNA-like small RNA able to selectively repress host genes. (PNAS 2021)

- DOI: 10.1073/pnas.2116668118 | PMCID: PMC8719879 | PMID: 34903581
- Evidence: Track visualization was performed using an IGV browser ( 70 ) of generated with BEDtools ( 71 ) bed files.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, featureCounts] -> differential/statistical testing [edgeR] -> visualisation [BEDTools]

### Systems biology analysis of human genomes points to key pathways conferring spina bifida risk. (PNAS 2021)

- DOI: 10.1073/pnas.2106844118 | PMCID: PMC8713748 | PMID: 34916285
- Evidence: First, BEDTools ( 94 ) was employed to identify those rare noncoding SNVs that fell within regulatory regions.
- Full pipeline: stage not stated [ADMIXTURE, BEDTools, GATK, R, VEP, WGCNA, scikit-learn]

### Early-life midazolam exposure persistently changes chromatin accessibility to impair adult hippocampal neurogenesis and cognition. (PNAS 2021)

- DOI: 10.1073/pnas.2107596118 | PMCID: PMC8463898 | PMID: 34526402
- Evidence: Egr1 binding loci that overlapped with open chromatin regions were calculated using BEDTools.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2, SAMtools v0.1.19]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **2.26.0**
- Evidence: ... genome with coverage <10 (the coverage threshold for genotype filtration) were excluded from further analysis (changed to N; coverage estimated with bedtools version 2.26.0 from individual bam-files after removing overhanging N’s at read ends using GATK SplitNCigarReads with the option–process-secondary-alignments).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### The p53 transcriptional response across tumor types reveals core and senescence-specific signatures modulated by long noncoding RNAs. (PNAS 2021)

- DOI: 10.1073/pnas.2025539118 | PMCID: PMC8346867 | PMID: 34326251
- Evidence: Messenger RNA (mRNA)-seq reads were counted that overlapped exons or intronic parts using custom scripts and bedtools multicov using the -split option.
- Full pipeline: alignment/mapping [StringTie, TopHat] -> normalisation [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2]

### Cell-free reconstitution reveals the molecular mechanisms for the initiation of secondary siRNA biogenesis in plants. (PNAS 2021)

- DOI: 10.1073/pnas.2102889118 | PMCID: PMC8346886 | PMID: 34330830
- Evidence: Sequence Alignment Map (SAM) files were converted to BAM files using SAMtools ( 60 ) and then to BED files with BEDTools ( 61 ).
- Full pipeline: alignment/mapping [BEDTools, Cutadapt, SAMtools, ggplot2]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: To do that, we generated a bed file of edit distances to the reference of the mapped reads with bedtools bamtobed -tag NM, and we calculated the −Δ% in R.
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Dynamic chromatin regulatory landscape of human CAR T cell exhaustion. (PNAS 2021)

- DOI: 10.1073/pnas.2104758118 | PMCID: PMC8325267 | PMID: 34285077
- Evidence: A union peak set was compiled by extending peak summits to 500 bp, merging all summits, running bedtools cluster, selecting summits with the highest MACS2 score, and filtering by the ENCODE hg19 blacklist.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [BEDTools, DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2, Picard, R]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Version used: **2.25.0**
- Evidence: The alignment results were converted to bed format and CENH3-ChIP-seq enrichment was calculated with bedtools v2.25.0 ( 101 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### The evolution and changing ecology of the African hominid oral microbiome. (PNAS 2021)

- DOI: 10.1073/pnas.2021655118 | PMCID: PMC8157933 | PMID: 33972424
- Evidence: We used bedtools ( 101 ) to calculate the breadth and depth coverage of a set of known virulence factors for these two taxa.
- Full pipeline: alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [BEAST, R] -> stage not stated [BEDTools]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Evidence: We convert the viral read BAM files into Bed files using the bamToBed utility in BEDTools ( 73 ).
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### Small noncoding RNA profiling across cellular and biofluid compartments and their implications for multiple sclerosis immunopathology. (PNAS 2021)

- DOI: 10.1073/pnas.2011574118 | PMCID: PMC8092379 | PMID: 33879606
- Evidence: To investigate length distribution of sncRNAs, sequences in the final preprocessed BAM files were filtered based on requiring 50% reciprocal overlap with selected biotypes using the BEDTools intersect function.
- Full pipeline: alignment/mapping [Trim Galore, featureCounts] -> differential/statistical testing [DESeq2, limma] -> stage not stated [BEDTools]

### The impact of identity by descent on fitness and disease in dogs. (PNAS 2021)

- DOI: 10.1073/pnas.2019116118 | PMCID: PMC8072400 | PMID: 33853941
- Evidence: To find the number of genes expected to contain at least one exon without an ROH, the ROH in each individual were permuted to a new location on the same chromosome using BEDTools shuffle ( 57 ).
- Full pipeline: stage not stated [BEDTools, PLINK, R]

### Accurate SNV detection in single cells by transposon-based whole-genome amplification of complementary strands. (PNAS 2021)

- DOI: 10.1073/pnas.2013106118 | PMCID: PMC7923680 | PMID: 33593904
- Evidence: Overlapping regions of the downloaded browser extensible data (BED) files of exonic and transcribed regions were merged with BEDTools ( 40 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2 v2.12] -> stage not stated [BEDTools]

### DNA methylation-linked chromatin accessibility affects genomic architecture in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023347118 | PMCID: PMC7865151 | PMID: 33495321
- Version used: **2.26.0**
- Evidence: ATAC-seq peaks were called by HMMRATAC (version 1.2.9) with minimum length of 50 bp for each replicate, and consensus set of peaks of each replicates were merged by bedtools (version 2.26.0) intersect while allowing 10 base pairs of distance ( 28 , 48 ).
- Full pipeline: read trimming [Cutadapt v2.5, SAMtools] -> alignment/mapping [Bowtie2, Cutadapt v2.5, RSEM] -> quantification [Bowtie2, RSEM] -> differential/statistical testing [R v3.30.0, edgeR v3.30.0] -> visualisation [pheatmap] -> stage not stated [BEDTools v2.26.0]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Evidence: In order to identify the enriched motifs, the 60 nt upstream sequences of each polyA site extracted by bedtools getfasta ( 51 ) were submitted to MEME ( 52 ) to discover motifs ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Identification and functional validation of super-enhancers in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2215328119 | PMCID: PMC9860255 | PMID: 36409894
- Evidence: The genomic positions of three types of ACRs were determined by comparing the genomic coordinates of the ACRs to TAIR 10 gene annotation using BEDTools ( 73 ).
- Full pipeline: alignment/mapping [BWA, SAMtools, minimap2] -> stage not stated [BCFtools, BEDTools, R v4.0.4]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Version used: **2.29.0**
- Evidence: The output was processed to calculate distributions along chromosomes on windows of 50 kb and steps of 10 kb using the utilities makewindows and coverage of BEDTools v2.29.0 ( 87 , 88 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Version used: **2.29.2**
- Evidence: The read number for each species in the union set of DHSs was determined by using BEDTools v.2.29.2 ( 97 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### Ectopic expression of meiotic cohesin generates chromosome instability in cancer cell line. (PNAS 2022)

- DOI: 10.1073/pnas.2204071119 | PMCID: PMC9549395 | PMID: 36179046
- Evidence: Second, peaks from the two biological replicates were intersected with each other with bedtools ( 132 ), with –d 10 parameter or with Genome Integrator (UCSC utilities), to generate a set of conserved peaks.
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, clusterProfiler] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [BEDTools, MACS2 v2.2, RepeatMasker]

### Leveraging orthology within maize and Arabidopsis QTL to identify genes affecting natural variation in gravitropism. (PNAS 2022)

- DOI: 10.1073/pnas.2212199119 | PMCID: PMC9546580 | PMID: 36161933
- Evidence: The loci containing genes At3g24140, At4g15130, At5g17290, and At5g17310 plus 1 kb downstream and upstream were retrieved with ‘bedtools getfasta’ version 2.27.1 ( 54 ) and ‘blastn’ version 2.2.29 ( 46 ) commands.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [MAFFT] -> stage not stated [BEDTools, BLAST]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: After peak calling with MACS2, we count the fragments which intersect with at least one peak as the number of fragments in peaks using bedtools for each cell.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Evolution of the ancestral mammalian karyotype and syntenic regions. (PNAS 2022)

- DOI: 10.1073/pnas.2209139119 | PMCID: PMC9550189 | PMID: 36161960
- Version used: **2.29.0**
- Evidence: For subsequent analyses of sequence features in msHSBs and EBRs, the human genome was divided into 10- and 100-kbp windows using BEDTools (version 2.29.0) ( 83 ).
- Full pipeline: structure determination [BUSCO v5.2.2] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.29.0]

### Rpd3 regulates single-copy origins independently of the rDNA array by opposing Fkh1-mediated origin stimulation. (PNAS 2022)

- DOI: 10.1073/pnas.2212134119 | PMCID: PMC9546531 | PMID: 36161938
- Version used: **2.25.0**
- Evidence: Overlapping origins between the different datasets were determined by bedtools 2.25.0 using intersect function; from these results, the union of origins identified in WT and rpd3Δ cells was determined for use as the total origins list of 306 only for the following purpose: Rpd3-repressed origins were called by applying a two-sample, two-tailed t test ( P < 0.001) comparing WT and rpd3Δ QBU signals...
- Full pipeline: stage not stated [BEDTools v2.25.0, MACS2 v1.4.2]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Evidence: For inversions, we also only considered candidates supported by at least two methods by using bedtools ( 113 ).
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Different classes of genomic inserts contribute to human antibody diversity. (PNAS 2022)

- DOI: 10.1073/pnas.2205470119 | PMCID: PMC9457163 | PMID: 36037353
- Evidence: Genome coverage was calculated using BEDTools ( https://bedtools.readthedocs.io/en/latest/index.html , v2.27.1) ( 68 ) and a dedicated python script using pysam ( https://github.com/pysam-developers/pysam ) was written to identify potential inserts.
- Full pipeline: quality control [FastQC] -> read trimming [R, Trim Galore, Trimmomatic] -> alignment/mapping [R, Trimmomatic] -> stage not stated [BEDTools, MACS2, ggplot2]

### False-positive IRESes from &lt;i&gt;Hoxa9&lt;/i&gt; and other genes resulting from errors in mammalian 5' UTR annotations. (PNAS 2022)

- DOI: 10.1073/pnas.2122170119 | PMCID: PMC9456764 | PMID: 36037358
- Evidence: Reads were summed and assigned to annotated refTSS peaks via bedtools intersect to define refTSS strength.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [scikit-learn] -> stage not stated [BEDTools, Cutadapt]

### Nucleotide excision repair removes thymidine analog 5-ethynyl-2'-deoxyuridine from the mammalian genome. (PNAS 2022)

- DOI: 10.1073/pnas.2210176119 | PMCID: PMC9436350 | PMID: 35994676
- Evidence: The output .sam files were converted into .bam files by using SAMtools ( 47 ) and then were converted into .bed files using bedtools ( 48 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> stage not stated [BEDTools, SAMtools]

### Adrenergic receptor signaling induced by Klf15, a regulator of regeneration enhancer, promotes kidney reconstruction. (PNAS 2022)

- DOI: 10.1073/pnas.2204338119 | PMCID: PMC9388080 | PMID: 35939709
- Version used: **2.30.0**
- Evidence: Unique and overlapping peaks were computed using BEDTools (2.30.0) (RRID:SCR_006646) ( 41 ).
- Full pipeline: differential/statistical testing [MACS2 v2.2.6, edgeR v3.32.1, featureCounts v2.0.1] -> stage not stated [BEDTools v2.30.0, HOMER]

### Historical contingencies and phage induction diversify bacterioplankton communities at the microscale. (PNAS 2022)

- DOI: 10.1073/pnas.2117748119 | PMCID: PMC9335236 | PMID: 35862452
- Version used: **2.27.0**
- Evidence: Based on read mapping to MAGs, per-base coverage values for all binned contigs were computed with BEDTools v2.27.0 ( 64 ) and were used to calculate contig-wide average coverage values.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BEDTools v2.27.0]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Version used: **2.29.2**
- Evidence: First, bedtools (v2.29.2) was used to subset ATACseq peaks that overlapped with an H3K27ac peak while removing those overlapping with H3K27me3 peaks.
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### The evening complex integrates photoperiod signals to control flowering in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2122582119 | PMCID: PMC9245669 | PMID: 35733265
- Version used: **2.30.0**
- Evidence: Graphpad Prism 8.0.2; Geneious Prime 2020.2.2; HISAT2 version 2.2.1; StringTie version 2.1.1; bwa version: 0.7.17-r1188; macs2 version 2.2.7.1; deeptools version 3.5.0; homer version 4.11; samtools version 1.11; bedtools version 2.30.0; R version 4.1.0; Custom code for using R packages are deposited at https://github.com/yl-lu/Rice_EC .
- Full pipeline: alignment/mapping [HISAT2] -> quantification [StringTie, deepTools] -> normalisation [deepTools] -> stage not stated [BEDTools v2.30.0, BWA, MACS2, R, SAMtools v1.11]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Evidence: Overlapping windows of the same repeat type were merged into larger regions using bedtools merge (v2.25.0) ( 49 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: The alignment files were filtered for mapping quality >5, and intervals less than 50 base pairs apart were merged with bedtools.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### APOBEC3A regulates transcription from interferon-stimulated response elements. (PNAS 2022)

- DOI: 10.1073/pnas.2011665119 | PMCID: PMC9171812 | PMID: 35549556
- Evidence: We then used BEDTools ( 49 ) ‘closest’ to filter on genes with TTTC motif pairs located upstream of or within annotated human genes (GENCODEV36) ( 50 ).
- Full pipeline: read trimming [fastp] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, Bioconductor, R v4.0]

### Stone Age <i>Yersinia pestis</i> genomes shed light on the early evolution, diversity, and ecology of plague. (PNAS 2022)

- DOI: 10.1073/pnas.2116722119 | PMCID: PMC9169917 | PMID: 35412864
- Version used: **2.25.0**
- Evidence: The output bam files were then used to calculate the percent of the gene covered using bedtools v2.25.0 ( 96 ) and prepared the data for R using Generate_bed_files.sh.
- Full pipeline: variant calling [GATK, Picard] -> differential/statistical testing [GATK, Picard] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.25.0, RAxML v0.9.0, ggpubr]

### Species-specific KRAB-ZFPs function as repressors of retroviruses by targeting PBS regions. (PNAS 2022)

- DOI: 10.1073/pnas.2119415119 | PMCID: PMC8931336 | PMID: 35259018
- Evidence: In addition, by calculating the density of ChIP-seq reads for H3K9me3 and H3K27ac at different distances from ZFP961 peaks using BEDTools, we found that KO of Zfp961 mainly affected the levels of histone marks closest to ZFP961 binding sites (distance from ZFP961 peaks <1 kb) ( SI Appendix , Fig.
- Full pipeline: stage not stated [BEDTools, RepeatMasker]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: The final BAM files were converted to BEDgraph files, using BEDtools-2.14.3 ( 32 ).
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### Spatiotemporal analysis identifies ABF2 and ABF3 as key hubs of endodermal response to nitrate. (PNAS 2022)

- DOI: 10.1073/pnas.2107879119 | PMCID: PMC8794810 | PMID: 35046022
- Evidence: The resulting peaks were annotated to genes using BEDtools considering 2 kb upstream of the transcription start site.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEDTools, ImageJ, MACS2, R]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Version used: **2.30.0**
- Evidence: H3K27Ac peaks that overlap H3K4me1 peaks were retained and merged with the nearest peaks if the distance between two peaks is ≤2 kb using bedtools 2.30.0 ( 50 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### Generation of de novo miRNAs from template switching during DNA replication. (PNAS 2023)

- DOI: 10.1073/pnas.2310752120 | PMCID: PMC10710096 | PMID: 38019864
- Version used: **2.26.0**
- Evidence: Using the Ensembl v.105 ( 50 ) genome annotation (gff3) for humans, the coordinates of coding genes, noncoding RNA genes, pseudogenes, coding exons, noncoding exons, and UTR3/UTR5 regions were extracted and, within each subclass, overlapping regions were merged using BEDTools v.2.26.0 ( 56 ).
- Full pipeline: stage not stated [BEDTools v2.26.0, Matplotlib v3.5.1, Python, R, ggplot2, seaborn v0.11.2]

### TGF-β broadly modifies rather than specifically suppresses reactivated memory CD8 T cells in a dose-dependent manner. (PNAS 2023)

- DOI: 10.1073/pnas.2313228120 | PMCID: PMC10691214 | PMID: 37988468
- Evidence: Peaks with a MACS2 ( 60 ) computed q value of less than 0.0001 in at least one replicate were merged with bedtools ( 61 ) function intersect and processed to uniform peaks of 500 bp width with the functions getPeaks and resize from R package chromVAR ( 62 ).
- Full pipeline: normalisation [limma] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2, R]

### Dual thermal ecotypes coexist within a nearly genetically identical population of the unicellular marine cyanobacterium &lt;i&gt;Synechococcus&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2315701120 | PMCID: PMC10665897 | PMID: 37972069
- Version used: **2.30**
- Evidence: Read filtering was done with bbduk (bbmap, v.38.90), and all reads mapped to the available reference genome for LA31 GCF_018502385.1 ( 25 ) using bowtie2 v.2.4.3 ( 61 ), and separated from non- Synechococcus reads using samtools v.1.11 ( 62 ) and BEDtools v.2.30 ( 63 ).
- Full pipeline: read trimming [minimap2 v2.17] -> alignment/mapping [BEDTools v2.30, Bowtie2 v2.4.3, SAMtools v1.11, minimap2 v2.17] -> normalisation [SPAdes v3.15.2] -> stage not stated [R]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We identified windows overlapping genes based on Ensembl gene coordinates (mm10) and the BEDTools “intersect” tool ( 92 ).
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: Binary Alignment Map (BAM) files were converted to Browser Extensible Data (BED) format using bedtools bamtobed function.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Tet2 deletion in CD4+ T cells disrupts Th1 lineage commitment in memory cells and enhances T follicular helper cell recall responses to viral rechallenge. (PNAS 2023)

- DOI: 10.1073/pnas.2218324120 | PMCID: PMC10483640 | PMID: 37639586
- Evidence: Genome coverage was assessed using the bedtools ( 35 ) genomecov software v2.25.0.
- Full pipeline: quality control [FastQC v0.11.4, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark, Bowtie2, DESeq2 v1.30.1, featureCounts v1.6.3] -> differential/statistical testing [DESeq2 v1.30.1, featureCounts v1.6.3] -> stage not stated [BEDTools]

### Sex-linked gene traffic underlies the acquisition of sexually dimorphic UV color vision in <i>Heliconius</i> butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2301411120 | PMCID: PMC10438391 | PMID: 37552755
- Evidence: Alignments were sorted, and male and female Illumina read coverage ( SI Appendix , Table S4 ) of each contig was measured using Bedtools (bedtools coverage -mean) ( 69 ), and contigs showing at least twofold higher coverage for female reads than male reads were designated as putative W-linked contigs.
- Full pipeline: quality control [Bowtie2 v2.2.7, Kraken2] -> alignment/mapping [BEDTools, Bowtie2 v2.2.7, MUSCLE] -> differential/statistical testing [R] -> stage not stated [Canu v1.6, Pilon, StringTie]

### Using evolutionary constraint to define novel candidate driver genes in medulloblastoma. (PNAS 2023)

- DOI: 10.1073/pnas.2300984120 | PMCID: PMC10438395 | PMID: 37549291
- Version used: **2.29.2**
- Evidence: The GC contents were calculated with BEDTools (v2.29.2).
- Full pipeline: stage not stated [BEDTools v2.29.2, GATK v4.1.4]

### Replitrons: A major group of eukaryotic transposons encoding HUH endonuclease. (PNAS 2023)

- DOI: 10.1073/pnas.2301424120 | PMCID: PMC10288648 | PMID: 37307447
- Evidence: For each genome, the coordinates of hits with e-values <0.01 were extracted and converted to DNA sequences using BEDTools “getfasta” ( 62 ).
- Full pipeline: alignment/mapping [MAFFT v7.471] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BEDTools, IQ-TREE v2.0.3]

### Digital microfluidics-based digital counting of single-cell copy number variation (dd-scCNV Seq). (PNAS 2023)

- DOI: 10.1073/pnas.2221934120 | PMCID: PMC10193948 | PMID: 37155890
- Evidence: To compare the performance of MDA and dd-scCNV Seq, duplicates-removed and duplicates-retained reads on chr4 were extracted using bedtools ( 24 ).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.38] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.9] -> differential/statistical testing [SAMtools v1.9] -> stage not stated [BEDTools]

### Vertebrate-tropism of a cressdnavirus lineage implicated by poxvirus gene capture. (PNAS 2023)

- DOI: 10.1073/pnas.2303844120 | PMCID: PMC10193959 | PMID: 37155884
- Evidence: Strictly overlapping alignments are merged with BEDTools ( 65 ) to generate a minimum–maximum coordinate range for each feature, which is extracted as a nucleotide FASTA.
- Full pipeline: read trimming [IQ-TREE v2.2.0, MAFFT v7.487] -> alignment/mapping [AlphaFold v2.1.1, BEDTools, BLAST v2.0.15, IQ-TREE v2.2.0, MAFFT v7.487] -> visualisation [AlphaFold v2.1.1]

### The PLOD2/succinate axis regulates the epithelial-mesenchymal plasticity and cancer cell stemness. (PNAS 2023)

- DOI: 10.1073/pnas.2214942120 | PMCID: PMC10194013 | PMID: 37155842
- Evidence: BEDtools coverage function was used to count the reads density for each bin in the gene.
- Full pipeline: stage not stated [BEDTools, SAMtools]

### TRAF4-mediated nonproteolytic ubiquitination of androgen receptor promotes castration-resistant prostate cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2218229120 | PMCID: PMC10193960 | PMID: 37155905
- Evidence: Venn diagrams of peaks were generated using bedtools ( 79 ).
- Full pipeline: normalisation [HOMER] -> stage not stated [BEDTools, GSEA, MACS2 v2.1.0]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Evidence: We used seqkit ( 45 ) for sequence data manipulations (extraction, conversion, translation), bedtools ( 46 ) to compute GC contents along sequences, and MMseqs2 (easy-search -s 7.5 --greedy-best-hits 1) to align MCP loci to known virophage and PLV hallmark proteins.
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Derepression of Y-linked multicopy protamine-like genes interferes with sperm nuclear compaction in <i>D. melanogaster</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220576120 | PMCID: PMC10120018 | PMID: 37036962
- Evidence: RNA coverage across genes at nucleotide resolution was quantified with “bedtools coverage” ( 51 ) and scaled by the total number of reads mapped to genes.
- Full pipeline: alignment/mapping [BEDTools, STAR v2.7.1a] -> quantification [BEDTools] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts] -> stage not stated [ImageJ]

### Detection of rare mutations, copy number alterations, and methylation in the same template DNA molecules. (PNAS 2023)

- DOI: 10.1073/pnas.2220704120 | PMCID: PMC10104560 | PMID: 37014860
- Evidence: The intercept function in BEDtools ( 33 ) was then used to identify the fraction of methylation in the targeted regions ( SI Appendix , Table S6 ).
- Full pipeline: stage not stated [BEDTools]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Evidence: We used the R package Quadron ( 93 ) to predict the G-quadruplexes (G4) throughout the genome with default settings, then calculated the length of G4 elements over 20 kb sliding windows along the chromosomes using bedtools coverage.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Genome-wide maps of rare and atypical UV photoproducts reveal distinct patterns of damage formation and mutagenesis in yeast chromatin. (PNAS 2023)

- DOI: 10.1073/pnas.2216907120 | PMCID: PMC10013872 | PMID: 36853943
- Evidence: The resulting alignment files were processed with SAMtools ( 51 ) and BEDtools ( 52 ), and custom Perl scripts were used to identify the dinucleotide sequence immediately upstream of the 5′ end of each sequencing read.
- Full pipeline: alignment/mapping [BEDTools, Bowtie2, SAMtools] -> visualisation [PyMOL]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Evidence: We counted the reads with BEDTools genomecov (2.29.2) ( 66 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Resurrection genomics provides molecular and phenotypic evidence of rapid adaptation to salinization in a keystone aquatic species. (PNAS 2023)

- DOI: 10.1073/pnas.2217276120 | PMCID: PMC9963159 | PMID: 36730191
- Evidence: We extracted the genes surrounding F st outliers ( P ≤ 0.05 after correction) in 10 Kb windows using the D. pulicaria RefSeq annotation (release 100, SC_F0-13Bv2) using bedtools ( 91 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools, BEDTools, SAMtools, VEP]

### Rhizogenic <i>Agrobacterium</i> protein RolB interacts with the TOPLESS repressor proteins to reprogram plant immunity and development. (PNAS 2023)

- DOI: 10.1073/pnas.2210300120 | PMCID: PMC9934019 | PMID: 36634142
- Evidence: The resulting GFF3 file with the coordinates of aligned features was filtered for overlaps (75% alignment coverage) with the ITAG4.0 genome annotation file using BEDTools ( 66 ) (version 2.2.28) to generate a gene identifier mapping table between gene models overlapping with at least 90% of their length. qPCR.
- Full pipeline: alignment/mapping [BEDTools]

### Histone methyltransferase SETDB1 safeguards mouse fetal hematopoiesis by suppressing activation of cryptic enhancers. (PNAS 2024)

- DOI: 10.1073/pnas.2409656121 | PMCID: PMC11670114 | PMID: 39689172
- Evidence: The unified Peak list was filtered for promoter-associated peaks (distance to TSS < 1,000 bp) with bedtools.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, RSEM, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [RSEM, pheatmap] -> stage not stated [BEDTools, GSEA, MACS2, deepTools]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Evidence: Genomic DNA sequencing coverage bigWigs from each dataset for visualization in IGV ( 51 ) were obtained using BEDtools ( 52 ) and UCSC Kent Utilities ( 53 ).
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Custom R code and “bedtools intersect” ( 75 ) were used to filter out peaks overlapping 1 kilo base windows with top 1% of sequencing coverage of control (tagmentation) libraries in order to exclude problematic genome regions.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **2.30.0**
- Evidence: Filtered BAM file was converted to BED with BEDTools version 2.30.0 ( 58 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### The reconstruction of evolutionary dynamics of processed pseudogenes indicates deep silencing of "retrobiome" in naked mole rat. (PNAS 2024)

- DOI: 10.1073/pnas.2313581121 | PMCID: PMC11551321 | PMID: 39467133
- Evidence: As additional illustration, we aligned sequencing reads for specific transcripts sequences of selected genes and calculated per-bp coverage using bedtools genomecov tool ( https://pubmed.ncbi.nlm.nih.gov/20110278/ ).
- Full pipeline: alignment/mapping [BEDTools] -> stage not stated [BLAST]

### Dynamics of transcription-coupled repair of cyclobutane pyrimidine dimers and (6-4) photoproducts in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416877121 | PMCID: PMC11536166 | PMID: 39441633
- Evidence: These strand-separated bed files were converted to bedgraph format using “bedtools genomecov” with parameters -bg -scale N (where N denotes the total number of reads).
- Full pipeline: read trimming [Cutadapt v3.4, STAR] -> alignment/mapping [Bowtie2 v2.4.5, STAR] -> stage not stated [BEDTools, Snakemake]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Evidence: We generated a union set of H3K27ac peaks by taking the top 40,000 peaks of each sample, removing ENCODE blacklisted peaks, and merging all remaining peaks using bedtools merge ( 50 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **2.27.1**
- Evidence: The filtered feature table was merged and used to mask the assembly with the merge and maskfasta commands in bedtools v2.27.1 ( 97 ).
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: Reads count information was extracted from the BAM files for each RNA-seq sample using the “multicov” function within the BEDTools program ( 47 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: Next, we removed blacklisted genes with BEDTools (Version 2.18) intersect -a ( 49 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### An atlas of the tomato epigenome reveals that KRYPTONITE shapes TAD-like boundaries through the control of H3K9ac distribution. (PNAS 2024)

- DOI: 10.1073/pnas.2400737121 | PMCID: PMC11252963 | PMID: 38968127
- Version used: **2.28.0**
- Evidence: Annotation of each histone modification with interaction was performed with bedtools (v 2.28.0) intersect ( 57 ) at a threshold of P value 0.01 and interaction zscore > 200.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bismark v0.24.0, Bowtie2 v2.3.5] -> differential/statistical testing [BEDTools v2.28.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, R, deepTools v3.5.0]

### Membrane association of active genes organizes the chloroplast nucleoid structure. (PNAS 2024)

- DOI: 10.1073/pnas.2309244121 | PMCID: PMC11252823 | PMID: 38968115
- Version used: **2.30.0**
- Evidence: Read counts on defined genomic regions (annotated genes or bins) were determined using samtools v.1.13 ( 60 ) and bedtools v.2.30.0 ( 61 ).
- Full pipeline: read trimming [Bowtie2 v2.4.4, Cutadapt v3.5] -> alignment/mapping [Bowtie2 v2.4.4, Cutadapt v3.5] -> quantification [BEDTools v2.30.0, SAMtools v1.13]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Evidence: BEDTools intersect ( 57 ) was used to assign peaks to gene bodies, promoters, or intergenic regions.
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### High prevalence of PRDM9-independent recombination hotspots in placental mammals. (PNAS 2024)

- DOI: 10.1073/pnas.2401973121 | PMCID: PMC11161765 | PMID: 38809707
- Evidence: We also computed the distance between the midpoint of the window and the closest midpoint of a hotspot using bedtools closest ( 77 ).
- Full pipeline: stage not stated [BEDTools]

### Premeiotic 24-nt phasiRNAs are present in the <i>Zea</i> genus and unique in biogenesis mechanism and molecular function. (PNAS 2024)

- DOI: 10.1073/pnas.2402285121 | PMCID: PMC11127045 | PMID: 38739785
- Version used: **2.29.2**
- Evidence: Overlap among the three types of PHAS loci or between PHAS loci and various genomic features were determined using the intersect function of BEDtools v2.29.2 ( 40 ) with parameters -e -f 0.5 -F 0.5. miRNA Loci Identification and Analyses.
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MUSCLE, edgeR v4.0.2, featureCounts v1.6.3] -> normalisation [edgeR v4.0.2, featureCounts v1.6.3] -> stage not stated [BEDTools v2.29.2, StringTie v2.1.7]

### DNA polymerase delta governs parental histone transfer to DNA replication lagging strand. (PNAS 2024)

- DOI: 10.1073/pnas.2400610121 | PMCID: PMC11098083 | PMID: 38713623
- Evidence: BEDTools ( 51 ) and self-developed Perl programs were used to calculate the genome-wide read coverage.
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [BEDTools]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Evidence: The overlapping sites between the MAZ-binding sites and STAT1-binding sites or repetitive elements were identified using bedtools intersect.
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Evidence: Similarly, to assess the expression levels of both long- and small-RNA and compare them to those of noncoding and repetitive elements, the coordinates of all reads mapped to the reference genome were intersected to those of the noncoding and repetitive elements using BEDtools ( 90 ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### Timeless noncoding DNA contains cell-type preferential enhancers important for proper Drosophila circadian regulation. (PNAS 2024)

- DOI: 10.1073/pnas.2321338121 | PMCID: PMC11009632 | PMID: 38568969
- Evidence: Peaks called from MACS2 were intersected between replicates using bedtools, and peaks across conditions were merged and converted into a reference annotation in SAF format ( 63 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, MACS2] -> stage not stated [BEDTools, Cellpose, DESeq2, SAMtools]

### Genomes of historical specimens reveal multiple invasions of LTR retrotransposons in <i>Drosophila melanogaster</i> during the 19th century. (PNAS 2024)

- DOI: 10.1073/pnas.2313866121 | PMCID: PMC11009621 | PMID: 38564639
- Evidence: We extracted the sequences of mostly full-length insertions (based on a length threshold; for Blood and 412: 6,000 to 8,000bp; for Opus: 5,000 to 8,000bp; for the I-element: 4,000 to 6,000) with bedtools ( 78 ) (v2.30.0) and performed multiple sequence alignment using MUSCLE (v3.8.1551) ( 52 ).
- Full pipeline: alignment/mapping [BEDTools, MUSCLE v3.8.1551] -> visualisation [Python, ggplot2] -> stage not stated [Cutadapt, RepeatMasker]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Evidence: We filtered candidate leaf mutations discarding previously identified heterozygous sites and all candidate mutations from all cambium comparisons using BEDTools subtract (v2.29.2).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### Comparative chemical genomics in <i>Babesia</i> species identifies the alkaline phosphatase PhoD as a determinant of antiparasitic resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2312987121 | PMCID: PMC10907312 | PMID: 38377214
- Evidence: Alignments were sorted and subsequently merged into VCF files using SAMtools ( 112 ), BEDtools ( 113 ), and VCFtools ( 114 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BEDTools, BWA, Clustal Omega, PyMOL v2.3.2, SAMtools, VCFtools] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold]

### Mutations of the circadian clock genes &lt;i&gt;Cry&lt;/i&gt;, &lt;i&gt;Per,&lt;/i&gt; or &lt;i&gt;Bmal1&lt;/i&gt; have different effects on the transcribed and nontranscribed strands of cycling genes. (PNAS 2024)

- DOI: 10.1073/pnas.2316731121 | PMCID: PMC10895256 | PMID: 38359290
- Evidence: Analysis of Data from XR-seq Aligned reads were strand-specifically assigned to genes using bedtools ( 50 ) with command line options bedtools intersect -c -a -b.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2] -> stage not stated [STRING db]

### High UV damage and low repair, but not cytosine deamination, stimulate mutation hotspots at ETS binding sites in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2310854121 | PMCID: PMC10823218 | PMID: 38241433
- Evidence: To analyze mutation density along transcribed genes, we used bedtools ( 44 ) and intersected the mutation data with annotated human genes downloaded from Gencode (GRCh37, release 44 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, Python] -> simulation/modelling [GROMACS, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [BEDTools, SAMtools]

### Sm complex assembly and 5' cap trimethylation promote selective processing of snRNAs by the 3' exonuclease TOE1. (PNAS 2024)

- DOI: 10.1073/pnas.2315259121 | PMCID: PMC10801842 | PMID: 38194449
- Evidence: Briefly, reads were first mapped to the human hg38 genome (STAR --outFilterMultimapNmax 1000 --alignIntronMin 9999999 --outFilterMultimapScoreRange --outFilterMismatchNoverLmax 0.2) and reads mapping to small RNA genes were extracted using bedtools ( 66 ) and samtools ( 67 ).
- Full pipeline: alignment/mapping [BEDTools, SAMtools, STAR v2.7.8a] -> stage not stated [ImageJ]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Version used: **2.30.0**
- Evidence: Signal bedgraph files were generated using bedtools (v2.30.0) ( 53 ) and converted into bigwig files using bedGraphToBigWig (v4) tool.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### The impacts of European arrival on Australian dingoes. (PNAS 2025)

- DOI: 10.1073/pnas.2421749122 | PMCID: PMC12684890 | PMID: 41284893
- Evidence: We then used BEDTools intersect v2.30.0 ( 86 ) and the CanFam3.1 annotation to identify genes within these regions.
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [SAMtools v1.9] -> differential/statistical testing [ADMIXTURE v1.3.0] -> stage not stated [BCFtools v1.9, BEDTools, IQ-TREE v2.1.4, PLINK v1.90b, R, VCFtools]

### Roles of transposable elements and DNA methylation in the formation of CpG islands and CpG-depleted regulatory elements. (PNAS 2025)

- DOI: 10.1073/pnas.2502963122 | PMCID: PMC12582260 | PMID: 41134632
- Evidence: Interval positioning and overlap measurements were computed with bedtools V2.31 and/or R implemented GenomicRanges V1.58.0.
- Full pipeline: stage not stated [BEDTools, RepeatMasker]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **2.31.0**
- Evidence: After conversion of file formats with SAMtools(v.1.17) ( 52 ) and bedtools (v.2.31.0) ( 53 ), peak identification was executed with Macs2 (v.2.2.7.1) ( 54 ).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Evidence: 1 B ) using bedtools closest (v2.30.0) ( 79 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: These 12 peak sets were union-merged by the above categories using bedtools mergeBed (v2.29.0) and default parameters, resulting in four category-specific peak sets.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Pseudouridine prevalence in Kaposi's sarcoma-associated herpesvirus transcriptome reveals an essential mechanism for viral replication. (PNAS 2025)

- DOI: 10.1073/pnas.2508523122 | PMCID: PMC12478172 | PMID: 40961145
- Evidence: A combination of KSHV 2.0 ( 22 ) and more recently annotated novel transcripts and ORFs ( 59 ) were used for assigning Ψ sites to KSHV annotated features through bedtools (intersect -s -split -loj) ( 60 ) followed by ad-hoc PERL script for filtering and summarizing of results ( Dataset S1 ).
- Full pipeline: stage not stated [BEDTools]

### Convergent evolution of &lt;i&gt;NFP&lt;/i&gt;-facilitated root nodule symbiosis. (PNAS 2025)

- DOI: 10.1073/pnas.2424902122 | PMCID: PMC12452920 | PMID: 40924454
- Evidence: We used a custom script that retrieved the top hit for each locus identified using BLASTp ( 56 ) and retrieved the top hit from the genome sequence using BEDTools ( 57 ).
- Full pipeline: stage not stated [BEDTools, BLAST, MAFFT, RAxML]

### Fragmentation signatures in cancer patients resemble those of patients with vascular or autoimmune diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2426890122 | PMCID: PMC12402995 | PMID: 40833414
- Evidence: Binary Alignment Map (BAM) files were converted to bed format using bedtools ( 89 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2, SAMtools] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy v1.13.1] -> stage not stated [Picard]

### Minimizing and quantifying uncertainty in AI-informed decisions: Applications in medicine. (PNAS 2025)

- DOI: 10.1073/pnas.2424203122 | PMCID: PMC12402999 | PMID: 40833408
- Evidence: The full nucleotide of each fragment and the 10 bases upstream and downstream of the fragment was then extracted from the hg19 reference genome using bedtools nuc ( 84 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2] -> differential/statistical testing [scikit-learn] -> stage not stated [Picard, RepeatMasker, SAMtools]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Version used: **2.27.168**
- Evidence: Bigwig coverage tracks with the sum of replicate samples were generated using bedtools 2.27.168 ( 60 ) and deeptools 3.3.169 ( 56 ), and heatmap representations of the coverage signal were performed using computeMatrix function and plotHeatmap from deeptools 3.3.1.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **2.30.0**
- Evidence: Using bedtools v2.30.0 intersect, the source regions were overlapped with endosymbiont gene regions ( 133 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### The fetal hydrops-associated single-residue mutation L322P disrupts mechanical but not chemical activation of the PIEZO1 ion channel. (PNAS 2025)

- DOI: 10.1073/pnas.2503793122 | PMCID: PMC12377734 | PMID: 40789030
- Evidence: Read depth was calculated by BEDTools, and copy number changes were detected by comparing with normal control samples.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [ANNOVAR, AlphaFold, BEDTools, GATK v3.7, ImageJ, Picard]

### Transcription termination promotes splicing efficiency and fidelity in a compact genome. (PNAS 2025)

- DOI: 10.1073/pnas.2507187122 | PMCID: PMC12358841 | PMID: 40763012
- Evidence: Resulting bam files were coordinate sorted and converted to bed files using SAMtools ( 35 ) and Bedtools ( https://bedtools.readthedocs.io/en/latest/ ) for downstream analyses.
- Full pipeline: alignment/mapping [featureCounts, minimap2] -> quantification [DESeq2, featureCounts] -> normalisation [DESeq2] -> stage not stated [BEDTools, SAMtools]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Evidence: Coordinates of these PHAS loci were extended using bedtools slop with a -b value of 1,000 and used to extract putative precursor sequences using bedtools getfasta ( 49 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: After confirming a high correlation between replicates, replicate peaks were combined using the merge function in BEDTools ( 61 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### SCoTCH-seq reveals that 5-hydroxymethylcytosine encodes regulatory information across DNA strands. (PNAS 2025)

- DOI: 10.1073/pnas.2512204122 | PMCID: PMC12337322 | PMID: 40743391
- Version used: **2.31.0**
- Evidence: ( 28 )] were identified with BEDTools (v2.31.0) ( 51 ), and mean levels of each CpG state (or grouped, corresponding CpG states) at each enhancer were calculated.
- Full pipeline: read trimming [Cutadapt v4.6, Picard v3.1.1, SAMtools v1.19.2] -> stage not stated [BEDTools v2.31.0, Snakemake v7.3.8, deepTools]

### Synthesis of large single-transcript pathways from oligonucleotide pools: Design of STARBURST, an autobioluminescent reporter. (PNAS 2025)

- DOI: 10.1073/pnas.2508109122 | PMCID: PMC12337302 | PMID: 40729380
- Evidence: Briefly, it uses minibar ( 46 ) to demultiplex reads, chopper ( 47 ) to remove low-quality reads, minimap2 ( 48 ) to map reads to reference sequences, and samtools ( 49 ), bcftools ( 49 ), bedtools ( 50 ), racon ( 51 ), medaka ( 52 ), seqtk ( 53 ), emboss ( 54 ), and parallel ( 55 ) to generate consensus sequences, annotate variants, and output summaries.
- Full pipeline: read trimming [BCFtools, BEDTools, SAMtools, minimap2]

### Genetic rescue of Florida panthers reduced homozygosity but did not swamp ancestral genotypes. (PNAS 2025)

- DOI: 10.1073/pnas.2410945122 | PMCID: PMC12337334 | PMID: 40720660
- Evidence: For sex chromosomes, we picked 5 PTFP males and 5 PTFP females and plotted the normalized read coverage along the scaffolds using windows (bedtools makewindows -w 100000 -s 10000).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK v4.2, SAMtools] -> variant calling [GATK v4.2] -> normalisation [BEDTools] -> visualisation [BEDTools] -> stage not stated [RepeatMasker, SnpEff, tidyverse]

### Complementary genetic and epigenetic changes facilitate rapid adaptation to multiple global change stressors. (PNAS 2025)

- DOI: 10.1073/pnas.2422782122 | PMCID: PMC12305003 | PMID: 40663607
- Evidence: F ST was estimated on a per-site level using the R package poolfstat ( 71 ), mean F ST relative to the ambient line was calculated in 1.5 kb windows, and the intersection between methylation sites and F ST windows was identified using BEDTools ( 72 ), keeping only windows with at least 5 SNPs and 5 methylation sites.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bismark v0.22.3, Bowtie2 v2.2.6] -> differential/statistical testing [R v3.6.0, edgeR] -> stage not stated [BEDTools, DESeq2]

### Tandem ssDNA in neutrophil extracellular traps binds thrombin and regulates immunothrombosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418191122 | PMCID: PMC12260427 | PMID: 40608679
- Version used: **2.30.0**
- Evidence: Overlap of peaks were identified by bedtools (v2.30.0) ( 77 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.6] -> stage not stated [BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Evidence: We then used bedtools intersect to find all the fixed derived mutations in the annotated VCF and used SnpSift ( 97 ) to produce a text file with the position, predicted impact (high, moderate, low, or modifier), and gene name.
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: The ENCODE Blacklist genome regions were also deleted by using BEDtools ( 64 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Version used: **2.30.0**
- Evidence: Depth of coverage for female long reads aligned to the male reference assembly was calculated using the genomecov function of bedtools v.2.30.0 ( 69 ).
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **2.30.0**
- Evidence: The pipeline was run under the GenoToul configuration available here: https://github.com/nf-core/configs/blob/master/docs/genotoul.md and used the following software and languages: bedtools v2.30.0 ( 81 ), R v4.0.3, v4.1.1, and v4.2.1 ( 82 ), DESEQ2 v1.28.0 ( 83 ); dupradar v1.28.0 ( 84 ), fastqc v 0.12.1 ( 85 ), fq v0.9.1 https://github.com/stjude-rust-labs/fq , gffread v0.12.1 ( 86 ), perl v5.26...
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Cross-species modeling of plant genomes at single-nucleotide resolution using a pretrained DNA language model. (PNAS 2025)

- DOI: 10.1073/pnas.2421738122 | PMCID: PMC12184517 | PMID: 40489624
- Evidence: Based on the repeat-masked annotation, each genome was softmasked with bedtools ( 60 ) and subsequently divided into genomic windows of 512 bp with a step size of 256 bp.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [XGBoost] -> visualisation [UMAP] -> stage not stated [BEDTools, BUSCO, VEP]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Version used: **2.30.0**
- Evidence: 68 . a region of the genome containing the locus and 50 kb of flanking sequence was extracted using BEDtools v2.30.0 and SAMtools v1.18 ( 69 , 70 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### A selfish supergene causes meiotic drive through both sexes in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421185122 | PMCID: PMC12054836 | PMID: 40267129
- Evidence: After mapping nanopore reads to their respective genomes, we used the genomeCoverageBed (flags: -d -ibam) command from bedtools ( 54 ) to obtain read depth at every position.
- Full pipeline: alignment/mapping [BEDTools, MAFFT] -> stage not stated [Flye v2.9, Pilon v1.24, R v4.3.0, phytools]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Version used: **2.30.0**
- Evidence: TE insertion calls from both programs were combined with BEDOPS (v2.4.39) ( 65 ) and merged if they overlapped or were within 20 bp using BEDTools (v2.30.0) ( 66 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### Structural variant and nucleosome occupancy dynamics postchemotherapy in a HER2+ breast cancer organoid model. (PNAS 2025)

- DOI: 10.1073/pnas.2415475122 | PMCID: PMC11892646 | PMID: 39993200
- Evidence: Peak calling was performed using MACS2 ( 55 ) for each of the cell lines and combined into the consensus peaks using bedtools to define cis-regulatory regions (CREs) ( 56 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [BEDTools, MACS2]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Evidence: For this purpose, we first assigned each TE to its closest gene when it was within 2 kb (the distance to either 5′ or 3′ end of gene with ≥ 0 kb and <2 kb) using command “bedtools closest -wo -a gene.bed -b TE.bed”, and thus genes were separated in four classes: hemizygous genes with nearby TEs, hemizygous genes without nearby TEs, diploid genes with nearby TEs, diploid genes without nearby TEs.
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Exercise intensity and training alter the innate immune cell type and chromosomal origins of circulating cell-free DNA in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2406954122 | PMCID: PMC11761974 | PMID: 39805013
- Evidence: Then, bedtools was used to make a bedgraph file tabulating special bed regions and reads in each of the NuMT regions relevant for each participant.
- Full pipeline: quantification [Bismark] -> stage not stated [BEDTools, SAMtools]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Evidence: The workflow used bedtools ( 58 ) (v2.30.0), bioconductor-summarized experiment (v1.20.0), bioconductor-tximeta (v1.8.0), gffread ( 59 ) (v0.12.1), picard (v2.25.7), salmon ( 60 ) (v1.5.2), samtools ( 61 ) (v1.13), star ( 62 ) (v2.6.1d), stringtie ( 63 ) (v2.1.7), Trimgalore (v0.6.7, GitHub—FelixKrueger/TrimGalore: A wrapper around Cutadapt and FastQC to consistently apply adapter and quality trim...
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Version used: **2.27.1**
- Evidence: Peak sets were merged, subtracted, overlapped, etc. using the appropriate bedtools (version 2.27.1) functions ( 59 ).
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **2.29.2**
- Evidence: Finally, BED files filtered for repetitive regions and CpG sites were generated with BEDtools v2.29.2 ( 69 ).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Cohesion site overlap comparisons were performed using bedtools, first sorting bed files, widening regions +/-250 bp via bedtools slop, merging overlapping peak regions, and then intersecting with regions of interest.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Version used: **2.31.1**
- Evidence: These subconsensus peak sets were then combined using the merge function of BEDTools v2.31.1 ( 58 ) to obtain a final consensus peak set that captured all potential peak locations, which was used for downstream analysis.
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### EPOP and MTF2 activate PRC2 activity through DNA-sequence specificity. (PNAS 2026)

- DOI: 10.1073/pnas.2527303123 | PMCID: PMC12890814 | PMID: 41650228
- Evidence: Regions in mm10 genome blacklist was removed using bedtools and bigwig files were generated using deeptools and parameters: --binSize 50 --normalizeUsing RPKM --ignoreDuplicates --ignoreForNormalization chrX --extendReads 250 for visualization in IGV.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [BEDTools, deepTools] -> normalisation [BEDTools, deepTools] -> visualisation [BEDTools, deepTools] -> stage not stated [ImageJ, MACS2, SAMtools]

### Antagonistic regulation of nitrogen and drought signaling mediated by NIN-like protein 7 transcription factor in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2509904122 | PMCID: PMC12773779 | PMID: 41481473
- Evidence: Peak annotation was performed using BEDTools ( 77 ), defining putative target genes as those within 1 kb upstream of the transcription start site (TSS).
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [Bowtie2] -> quantification [kallisto] -> normalisation [DESeq2] -> stage not stated [BEDTools, MACS2]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: Uniquely aligned reads were then used to extract the cross-link truncation site (position 1 relative to the 5′-end of the read start) using bedtools and htseq-clip/extract and quantified using htseq-clip/count.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Creation of de novo cryptic splicing for ALS and FTD precision medicine. (Science 2024)

- DOI: 10.1126/science.adk2539 | PMCID: PMC7616720 | PMID: 39361759
- Evidence: Counts for specific junctions were tallied by parsing the STAR splice junction output tables using bedtools.
- Full pipeline: alignment/mapping [STAR v2.7.0f, minimap2 v2.1] -> quantification [ImageJ, STAR v2.7.0f] -> stage not stated [BEDTools, CellProfiler, R, Snakemake v5.5.4]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **2.30.0**
- Evidence: We filtered IDR output to only select peaks with an IDR score <= 0.05 (transformed IDR value >=540), concatenated the IDR-filtered peak files for WT and either the HSA-6mut or the ΔTRRAP EP400 mutant in a single .bed file by bedops –everything (v2.4.41) ( 115 ), and finally sorted and merged the concatenated files with bedtools (v2.30.0) ( 116 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Version used: **2.31.0**
- Evidence: Reads were filtered based on reciprocal 90% coverage with the target locus using the bedtools v.2.31.0 intersect (-wo -f 0.9 -r) command.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Evidence: Peak calling analysis was performed using Macs2 (v2.1.2) and the target genes were defined by the closest gene from each peak (bedtools closest).
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Evidence: We generated 1000 permutation sets for each mutation type in each cell using SCAN2 by running “scan2 config --analysis permtool” with original mutation calls (--permtool-muts), the human reference genome GRCh37 with decoy (--permtool-bedtools-genome-file), and 1000 permutations (--permtool-n-permutations), followed by “scan2 permtool”.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Peak calling was performed using MACS2, filtered using bedtools, and converted to bigwigs with UCSC wigtoBigwig( 60 , 61 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Evidence: Repetitive elements in the ENCODE blacklist( 74 ) were excluded using bedtools intersect (v2.30.0)( 75 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Version used: **2.29.2**
- Evidence: For mESC samples, bedtools (v2.29.2) intersect was used with the -loj -wa -wb -filenames -sorted options to extract those alignments overlapping with a known variant between the BL6 and CAST alleles from the Sanger Mouse Genome database ( 40 , 70 ).
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Other alignments mapping to scaffolds or blacklist (downloaded from https://mitra.stanford.edu/kundaje/akundaje/release/blacklists/mm10-mouse/mm10.blacklist.bed.gz ) were removed using bedtools intersect.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: These regions were then overlapped with peak annotations in species B using bedtools intersect (v.2.28) ( 89 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

