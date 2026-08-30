# deepTools

- **Category:** genomics
- **Papers in survey:** 167
- **Journals:** PNAS (74), Nature (71), Cell (19), Science (3)
- **Years:** 2021 (16), 2022 (15), 2023 (33), 2024 (39), 2025 (45), 2026 (19)
- **Versions named:** 3.5.1 (19), 3.5.0 (5), 3.3.1 (5), 3.5.4 (3), 3.3.2 (3), 3.5.5 (3), 3.2.1 (3), 3.1.3 (3), 3.5.3 (2), 3.5.2 (2)
- **Pipeline stages it appears in:** normalisation (58), visualisation (36), alignment/mapping (32), quantification (18), read trimming (9), quality control (6), variant calling (1), dimensionality reduction/clustering (1), differential/statistical testing (1)

## Papers

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: Sequenced libraries were processed with deepTools ( Ramírez et al., 2016 ), using STAR ( Dobin et al., 2013 ), for trimming and mapping, and featureCounts ( Liao et al., 2014 ) to quantify mapped reads.
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Version used: **3.1.3**
- Evidence: ...Addgene Cat#31208 Software and Algorithms Bowtie2 v2.2.9 Langmead and Salzberg, 2012 N/A Cutadapt Martin, 2011 N/A DESeq2 v1.32 Love et al., 2014 N/A deeptools v3.1.3 Ramírez et al., 2016 N/A Flowjo 10.6.2 FLOWJO https://www.flowjo.com Graphpad Prism 8 Graphpad software https://www.graphpad.com/scientific-software/prism/ MACS2 Zhang et al., 2008 N/A PoolQ version 3.2.9 Broad Institute https://port...
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: ATAC-seq analysis Raw sequencing fastq files were processed using cutadapt ( Martin, 2011 ) for adapter trimming, Bowtie2 { Langmead, 2012 #2898) for mapping, SAMtools ( Li et al., 2009 ) for filtering, sorting and removing duplicates, and deepTools ( Ramírez et al., 2016 ) for generating coverage tracks.
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: The resultant BAM file was indexed using SAMtools index, and converted to a bigwig file using deepTools bamcoverage.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **3.5.1**
- Evidence: 88 https://github.com/macs3-project/MACS CellRanger 6.1.1 v6.1.1 10X Genomics https://support.10xgenomics.com/cloud-analysis/release-notes BWA 0.7.17 Li and Durbin 89 https://github.com/lh3/bwa Possvm Grau-Bové and Sebé-Pedrós 90 https://github.com/xgrau/possvm-orthology/ deeptools 3.5.1 Ramírez et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Evidence: MACS2 (v2.0.10) 76 was used to call the peaks and deepTools 77 were used to compute the ChIP-seq or Cut and Run signal around prostate PMDs.
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Version used: **3.5.0**
- Evidence: 21 https://github.com/ConesaLab/SQANTI3 IsoAnnotLite 2.7.3 N/A https://isoannot.tappas.org/isoannot-lite/ cDNA_Cupcake v12.5 N/A https://github.com/Magdoll/cDNA_Cupcake deeptools 3.5.0 N/A https://github.com/deeptools/deepTools randomForest N/A https://cran.r-project.org/web/packages/randomForest/index.html MEME Suite 5.5.0 AME N/A https://meme-suite.org/meme/tools/ame MEME Suite 5.5.0 FIMO N/A ht...
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Version used: **3.1.2**
- Evidence: Bigwigs were generated using deeptools (version 3.1.2) with RPKM normalization and presented by Integrative Genomics Viewer (IGV) software.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: 105 To visualize the RNA-seq data in the UCSC genome browser, bigwig files were generated using the bamCoverage command from deepTools ( https://deeptools.readthedocs.io/en/develop/content/tools/bamCoverage.html ).
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Version used: **3.5.1**
- Evidence: 71 https://github.com/taoliu/MACS/tree/ master/MACS2 deepTools v.3.5.1 Ramírez et al.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Version used: **3.5.1**
- Evidence: The coverage files were generated with the ‘normalize to 1× genome coverage’ methods in deepTools (version 3.5.1).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### The fork protection complex promotes parental histone recycling and epigenetic memory. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.017 | PMCID: PMC11383432 | PMID: 39094569
- Evidence: 117 https://deeptools.readthedocs.io/en/develop/ SeqPlots v.12.1 Stempor and Ahringer 118 https://bioconductor.org/packages/release/bioc/html/seqplots.html R and R Studio R Project https://www.r-project.org/ SCAR-Seq Analysis Pipeline Wenger et al.
- Full pipeline: differential/statistical testing [R v4.2.2] -> visualisation [PyMOL v1.2r, ggpubr v0.6.0] -> stage not stated [AlphaFold, Bowtie2 v2.4.2, ChimeraX, MACS2, SAMtools v1.12, deepTools]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Evidence: 123 RRID: SCR_012918 deeptools Ramírez et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **3.2.1**
- Evidence: 108 http://www.htslib.org/ deepTools v3.2.1 Ramirez et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Vertebrate centromeres in mitosis are functionally bipartite structures stabilized by cohesin. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.014 | PMCID: PMC11164432 | PMID: 38744280
- Evidence: 79 http://www.usadellab.org/cms/index.php?page=trimmomatic BWA mem v0.7.16 Heng Li https://github.com/lh3/bwa?tab=readme-ov-file deepTools bamCoverage v3.5 deepTools https://deeptools.readthedocs.io/en/develop/ LAMMPS Plimpton 80 https://github.com/lammps/lammps Huygens Professional (v20.10) Scientific Volume Imaging https://svi.nl/Huygens-Professional capC-MAP software Buckle 81 https://github.co...
- Full pipeline: read trimming [BWA v0.7.16, Cutadapt v1.18, ImageJ, LAMMPS, Trimmomatic v0.36, deepTools] -> stage not stated [Snakemake]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: To assess accessibility differences between lateAD and nonAD, we computed log 2 (fold change) values using bigwigCompare from the deepTools suite (v.3.5.1), comparing lateAD to nonAD profiles within each cell class.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: GI-SINE specific sequence motif identification In order to determine the precise genomic start and end coordinates of B2-SINE based on RNAseq reads, the bamCoverage tool from deepTools suite, version 3.5.1 98 was used.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: ChIP-seq signals (.bigwig and.bedGraph) were derived from the bam files using bamCoverage from the deepTools suite.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### Inflammation switches the chemoattractant requirements for naive lymphocyte entry into lymph nodes. (Cell 2025)

- DOI: 10.1016/j.cell.2024.11.031 | PMCID: PMC11845304 | PMID: 39708807
- Version used: **3.5.4**
- Evidence: The annotation was carried out using PAPST 65 and the heatmap creation utilized deeptools 3.5.4.
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2 v1.4.2, Metascape] -> visualisation [UMAP] -> stage not stated [R v4.2.1, Seurat v4.3.0, deepTools v3.5.4]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: The genomic coverage was calculated using bamCoverage from deeptools 50 (version 3.5.0) with binSize 1.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: For chromatin accessibility of each cell type, we merged all fragments from snATAC-seq cells that were assigned to this cell type in the integration analysis and used ‘deeptools bamcoverage’ to generate CPM-normalized bigwig files.
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: Visualizing cluster signal in peaks The deeptools suite 64 ( https://deeptools.readthedocs.io/en/develop/ ) was used to visualize pileups of cluster-specific ATAC-seq signal (output from MACS2) in DA peak sets.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Evidence: For chromatin accessibility of each subtype, we merged all fragments from snATAC-seq cells that were assigned to this subtype in the integration analysis and used deeptools bamcoverage to generate CPM normalized bigwig files.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **3.4.2**
- Evidence: BigWig files were then generated using deepTools v3.4.2 bamCoverage 60 with the following options: (–ignoreDuplicates–minFragmentLength 0–maxFragmentLength 1000–binSize 50–scaleFactor).
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Sulfur sequestration promotes multicellularity during nutrient limitation. (Nature 2021)

- DOI: 10.1038/s41586-021-03270-3 | PMCID: PMC7969356 | PMID: 33627869
- Evidence: Sequenced libraries were processed with deepTools 49 , using STAR 50 , for trimming and mapping, and featureCounts 51 to quantify mapped reads.
- Full pipeline: read trimming [Seurat, UMAP, deepTools, featureCounts] -> alignment/mapping [DESeq2, R, Seurat, UMAP, deepTools, featureCounts] -> quantification [DESeq2, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R]

### Loop extrusion as a mechanism for formation of DNA damage repair foci. (Nature 2021)

- DOI: 10.1038/s41586-021-03193-z | PMCID: PMC7116834 | PMID: 33597753
- Evidence: For representation of genomic tracks, the data were further smoothed using slidding windows as indicated. bamCompare from deeptools, with the parameters --binSize=50, --operation=log2 and with default normalization (readCount) was used to generate differential tracks.
- Full pipeline: read trimming [R, SAMtools] -> alignment/mapping [R, SAMtools] -> normalisation [Bioconductor, deepTools] -> differential/statistical testing [deepTools] -> visualisation [Bioconductor] -> stage not stated [MACS2, ggplot2]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Metagene plots: Metagene plots were created with the deepTools package using ATAC-seq peak centers and regions extended to +/− 3,000 bp with 10 bp bins.
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **3.1.1**
- Evidence: Bigwig files were generated by normalizing IP bam files to respective inputs using deepTools (v.3.1.1) 70 .
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Reads were filtered by mapping quality 60 (samtools view -q 40) and fragment length 61 (deepTools alignmentSieve --maxFragmentLength 120).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Version used: **3.3.1**
- Evidence: Using deepTools (version 3.3.1) bamCoverage, a coverage file (bigWig format) for each sample was created.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: Bioinformatics data processing and analyses were performed using Bash (v4.2.46), R (v3.6) and Python (v3.8.5) programming languages as well as the following tools: FastQC (Babraham Bioinformatics) (v0.11.7) cutadapt 37 (v1.16), HISAT2 38 (v2.1.0), SAMtools 39 (v1.9), sambamba 40 (v0.6.6) and deepTools 41 (v3.1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: 2g , we used deeptools 91 (v.3.5.1) to profile the boundary probability at transcript ±2 Mb 25-kb bins.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: ...es of cCREs (red) overlapping (ovlp) with rDHSs, cCREs (blue) with no overlaps with rDHSs, and random genomic background (grey) were determined using deepTools 82 . d , The fraction of cCREs captured by different cell subtypes for peak calling.
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Evidence: Bigwig files were created using deepTools bamCoverage (v.3.3.2) 62 , using a size factor calculated from DESeq2 (v.1.26.0) 63 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Mouse genome rewriting and tailoring of three important disease loci. (Nature 2023)

- DOI: 10.1038/s41586-023-06675-4 | PMCID: PMC10632133 | PMID: 37914927
- Version used: **3.1.0**
- Evidence: The read per million (RPM)-normalized BigWig files were generated using deepTools (v.3.1.0).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, STAR] -> normalisation [deepTools v3.1.0, featureCounts v1.6.3] -> differential/statistical testing [featureCounts v1.6.3] -> stage not stated [Picard, fastp]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Evidence: Whole-genome coverage was computed using the bamCoverage command form deeptools to generate bigwig from BAM files (without PCR duplicate suppression).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Version used: **3.1.0**
- Evidence: Coverage signal tracks (bigWigs) of primary alignments were generated using deepTools (v.3.1.0).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### R-loop-dependent promoter-proximal termination ensures genome stability. (Nature 2023)

- DOI: 10.1038/s41586-023-06515-5 | PMCID: PMC10511320 | PMID: 37557913
- Version used: **3.5.1**
- Evidence: Normalized bigwig files were generated with the bamCoverage function from deepTools (v.3.5.1) 63 using scale factors calculated according to Supplementary Note 1 .
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [Picard, SAMtools v1.12] -> quantification [Trim Galore v0.6.6] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [Trim Galore v0.6.6] -> stage not stated [ImageJ, MACS2 v2.2.7.1, R]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: CpG methylation for RLC_Cereba copies was then calculated using the deeptools computeMatrix function and visualized using the deeptools plotProfile function 98 .
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Continuous synthesis of E. coli genome sections and Mb-scale human DNA assembly. (Nature 2023)

- DOI: 10.1038/s41586-023-06268-1 | PMCID: PMC7614783 | PMID: 37380776
- Version used: **3.5.1**
- Evidence: We computed coverage using deeptools (v3.5.1) 48 bamCoverage with the bin size set to 50 nucleotides.
- Full pipeline: read trimming [minimap2] -> alignment/mapping [SAMtools v1.16.1, minimap2] -> variant calling [Mutect2] -> stage not stated [GATK v4.3.0, Python, RepeatMasker, deepTools v3.5.1]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: Normalized bigwig files were generated using the bamCoverage function from deeptools using reads per kilobase of transcript per million mapped reads normalization.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### A druggable copper-signalling pathway that drives inflammation. (Nature 2023)

- DOI: 10.1038/s41586-023-06017-4 | PMCID: PMC10131557 | PMID: 37100912
- Evidence: Bigwig tracks were then generated with deeptools and normalized to 1 million reads to account for differences in sequencing depth.
- Full pipeline: quality control [Nextflow] -> normalisation [R, deepTools, edgeR v3.30.3] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, limma]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: For each sample, the fold change against the input experiment was then computed using the bamComapre command from the deepTools package (v.3.5.1) 100 setting –scaleFactorsMethod readCount, --extendReads, --operation ratio and --binSize 100).
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **3.4.3**
- Evidence: Quality filtered reads were mapped using NextGenMap (v.0.5.5) 119 in paired-end mode, duplicates were removed using samtools (v.1.9) 120 and mapped reads were shifted using deepTools (v.3.4.3) 121 (Supplementary Tables 58 and 60 ).
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### A DNA methylation atlas of normal human cell types. (Nature 2023)

- DOI: 10.1038/s41586-022-05580-6 | PMCID: PMC9811898 | PMID: 36599988
- Version used: **3.4.1**
- Evidence: Heatmaps and average plots were prepared using deepTools (v.3.4.1) 61 , with the functions ‘computeMatrix’, ‘plotHeatmap’ and ‘plotProfile’.
- Full pipeline: alignment/mapping [SAMtools v1.9] -> dimensionality reduction/clustering [SciPy v1.6.3] -> differential/statistical testing [HOMER] -> stage not stated [BEDTools v2.26.0, deepTools v3.4.1, scikit-learn]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **3.3.1**
- Evidence: BigWig files were generated using deeptools (v.3.3.1) 92 with the settings ‘-normalizeUsing CPM’.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Evidence: GRO-seq signal was converted to the bigwig format for visualization using deepTools bamCoverage 18 (v.3.3.1) with the following parameters: --binSize 10 --normalizeUsing CPM --effectiveGenomeSize 3209286105 --exactScaling.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Evidence: The ChIP–seq signal was converted to bigwig format for visualization using deepTools bamCoverage 74 (v.3.3.1) with the following parameters: --bs 5 --smoothLength 105 --normalize Using CPM --scaleFactor 10.
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **3.2.1**
- Evidence: Coverage tracks (Bigwig files) were generated from filtered BAM files for individual replicates using deepTools (v.3.2.1, RRID: SCR_016366 ) bamCoverage with parameters –normalizeUsing RPKM –binsize 1.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tissue spaces are reservoirs of antigenic diversity for Trypanosoma brucei. (Nature 2024)

- DOI: 10.1038/s41586-024-08151-z | PMCID: PMC11634766 | PMID: 39478231
- Evidence: Read coverage was calculated using deepTools 70 (v.3.5.5) to convert BAM alignment files to bigWig coverage tracks.
- Full pipeline: alignment/mapping [deepTools] -> visualisation [R] -> stage not stated [Cutadapt, ImageJ v1.53, SAMtools]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: BAM files were converted to normalized bigWig files for visualization and plotting using deepTools 48 bamCoverage v.3.5.0 with the following parameters: -bs 1 --normalizeUsing BPM.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **2.0.0**
- Evidence: 2.31.0) 84 and used to scale bigwig files equivalently in deepTools (v.2.0.0) 85 .
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Evidence: For data visualization, alignment files were converted to a strand-specific bigwig format using deepTools 111 .
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Bigwig files were created using the deepTools bamCoverage function.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **3.5.0**
- Evidence: BigWig files were generated from the BAM files using bamcoverage for raw count with the “--normalizeUsing CPM -bs 25” or bamcompare for IP/Input command with the “--pseudocount 1 -bs 1000” option of deepTools (v.3.5.0) 87 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **3.5.4**
- Evidence: Read coverage was estimated using deepTools (v.3.5.4) 63 with bamCoverage and a bin size of 10 bp and normalization by bins per million mapped reads.
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: Alignments were normalized and filtered with deepTools 73 (v.3.4.3) bamCompare with the following parameters: bamCompare -b1 {ChIP.bam} -b2 {bulk_nucleosomal. bam} --operation ratio --binSize 1000 --minMappingQuality 1 -o {out. bw}.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Version used: **3.3.1**
- Evidence: Quality control plots were made using deeptools v3.3.1 (ref.
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Version used: **3.5.0**
- Evidence: Coverage tracks were produced in bigWig format using bamCoverage (deepTools v3.5.0) 80 with bin size 10 and smooth length 100, normalized using RPGC to an effective genome size of 12,000,000 for sacCer3 and 2652783500 for mm10, and visualized using IGV v2.12.3 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Evidence: We used the stats function of deeptools/pyBigWig package (RRID: SCR_024807 ) 72 to calculate mean γ-KC accessibility values for each bin.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **3.2.1**
- Evidence: Coverage tracks were generated from Binary Alignment Map files using deepTools (v.3.2.1) bamCoverage with parameters –normalizeUsingRPKM –binsize 10 (ref.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Exported bed files were used as input to deeptools multiBigWig summary, yielding coverage intensity matrix file sin.npz format, which were then read into R using numpy and reticulate.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: Sequencing depth in peaks were normalized as reads per kilobase of transcript per million mapped reads (RPKM) using the bamCoverage function in deepTools.
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Evidence: Moreover, when comparing the changes in chromatin accessibility caused by genotypes across samples or between different cell types, read counts were scaled and normalized using the deepTools package (v.2.0) bamCoverage function and re-scaled to reads per genomic content as the base unit 71 .
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Tornado plots were generated with deepTools 80 (v.3.5.1) functions (computeMatrix and plotHeatmap), with genes annotated from the indicated pathway sets.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Evidence: CPM normalized bigwigs were made using deepTools bamCoverage v.3.0.1.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Using deepTools 78 , the computeMatrix function in scale-regions mode was used to calculate the methylation score, using the parameters --binSize 50 --averageTypeBins mean -a 1000 -b 1000.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: Using deeptools alignmentSieve aligned reads were filtered and shifted with -ATACshift, which corresponds to mate reads being shifted +4 and −5 bp for positive and negative strands, respectively.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **3.5.1**
- Evidence: For heatmaps and PCAs, matrices were generated with deeptools (3.5.1) computeMatrix, and heatmaps and PCAs were generated with deeptools plotHeatmap and ggplot2 (3.4.2), respectively.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Histone H1 deamidation facilitates chromatin relaxation for DNA repair. (Nature 2025)

- DOI: 10.1038/s41586-025-08835-0 | PMCID: PMC12074999 | PMID: 40240600
- Version used: **3.5.5**
- Evidence: The generation of metagene profiles and heatmaps, which display the signals of each histone modification and open chromatin at DSBs, was accomplished using the computeMatrix and plotHeatmap functions of deepTools (v3.5.5).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.4, SAMtools] -> stage not stated [AlphaFold, ImageJ, Picard, PyMOL, deepTools v3.5.5]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Evidence: Coverage files (Bigwig files) were generated for each single cell using deepTools 52 (v.3.5.4) bamCoverage function with ‘--normalizeUsing RPKM’ and ‘--minMappingQuality 10’ options.
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Evidence: Identification of sequencing coverage Sequencing read coverage per 50-bp bin was calculated using deeptools ‘bamCoverage’ (v3.5.1) 60 with default values.
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Version used: **3.5.1**
- Evidence: Correlation analysis for TACIT data For correlation analysis between different experiments, we calculated the normalized mean scores in 5-kb bins of the genome by using the multiBigwigSummary function in deepTools (v.3.5.1) 57 .
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: To generate a reference matrix of coverage for the regions spanning 1,000 bps upstream and downstream of the centres of the specific peaks, we utilized the deeptools computeMatrix function.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Evidence: Enrichment was calculated as log 2 [ChIP/input] using deepTools bamCompare (v3.5.2) 86 , averaged for replicates and aligned to +1 nucleosome as for nucleosome occupancy.
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **3.5.1**
- Evidence: Genome coverage tracks (bigwig files) were produced using the deepTools (v.3.5.1) bamCoverage function with the options --binSize 10 --smoothLength 30 --normalizeUsing None --scaleFactor # (derived from E. coli spike in) and using an ENCODE hg19 or mm10 blacklist file (10.1038/s41598-019-45839-z, v2 for both) to discard regions with consistently non-specific signal 69 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Engineered extrachromosomal oncogene amplifications promote tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08318-8 | PMCID: PMC11754114 | PMID: 39695225
- Version used: **3.5.3**
- Evidence: To compare ATAC-seq signals between ecDNA amplicons and corresponding chromosomal regions, bamCoverage in deeptools (v.3.5.3) was used to calculate read counts with 10 kb bin size, and MACS (v.3.0.0b1) was used for peak calling.
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, R, STAR] -> quantification [MACS2 v3.0.0b, deepTools v3.5.3] -> differential/statistical testing [DESeq2, R, STAR] -> stage not stated [CNVkit v0.9.10, fgsea]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **3.5.1**
- Evidence: The samples were normalized using the bamCoverage function from deepTools (v3.5.1) to visualize the signal in IGV (v2.7.0).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Evidence: Bigwig files were produced using the deepTools package (v3.5.1), using an ENCODE hg19 or mm10 v2 blacklist file to discard regions with consistently non-specific signal, and scaled using E. coli spike-in controls to normalize sequencing depth.
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **3.5.1**
- Evidence: For visualization of CATCH-seq using the Integrative Genomics Viewer (v.2.16.1) 59 , genome coverage tracks were generated using bamCoverage from deepTools (v.3.5.1) 60 with the parameters ‘–binSize 50–scaleFactor 1–normalizeUsing RPKM–numberOfProcessors 28–extendReads 200–ignoreDuplicates–smoothLength 100’.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **3.5.1**
- Evidence: Normalized ATAC signal coverage bigWig files for genome track visualization were generated using deepTools (v.3.5.1) 55 .
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Version used: **3.5.3**
- Evidence: A normalized Bigwig file was generated using bamCoverage (deepTools v3.5.3) 57 and visualized on Integrative Genomics Viewer (v2.19.1) 58 .
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **3.5.2**
- Evidence: In addition, Cse4-mNG nucleosome dyads were determined with deepTools (v.3.5.2) using the function bamCoverage–Mnase.
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **3.5.1**
- Evidence: Data were analysed using the nf-core/cutandrun pipeline v.3.2.2 with Nextflow v.24.04.2, using the default parameters and following software dependencies: bedtools (v.2.30.0), bowtie (v.2.4.4), deeptools (v.3.5.1), fastqc (v.0.12.1), picard (v.3.1.0), Python (v.3.9.12), samtools (v.1.17), Genrich (v.0.6.1), TrimGalore (v.0.6.6), ucsc (v.377).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **3.5.4**
- Evidence: Read coverage was computed using multiBamSummary (deepTools, v.3.5.4) in bins of 1 kb.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Version used: **3.3.2**
- Evidence: Samples were demultiplexed, quality checked, filtered and aligned with genome build GRCm38 using pre-established pipelines implemented in snakePipes 64 with STARsolo v.2.7.4a 65 , deeptools v.3.3.2, seqtk v.1.3, pigz v.2.3.4, snpsplit v.0.3.4, samtools v.1.10, fastqc v.0.11.9, cutadapt v.2.8, trim-galore v.0.6.5, multiqc v.1.8, fastp v.0.20.0, umi_tools v.1.0.1 and star v.2.7.4a.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: Chromatin dataset processing CUT&Run datasets were processed by trimming adaptors using cutadapt, locally mapping the reads using bowtie2, filtering for quality, removing duplicates and ENCODE blacklisted regions (ENCFF419RSJ) using samtools, and computing the coverage using deeptools.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: For visualization purposes, Reads Per Genomic Content (RPGC) normalization (1× coverage) signal was averaged among the replicates per each condition using deeptools bigwigCompare.
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **3.5.5**
- Evidence: Genomic enrichment of CUT&Tag signals for each histone modification was analysed using deeptools (v.3.5.5) and visualized using IGV (v.2.13.0).
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Version used: **3.5.1**
- Evidence: To plot heatmaps of protein binding in retention elements, we used the ‘computeMatrix’ function in deepTools (v.3.5.1) with the ‘scale-regions’ mode, specified each ‘bigWig’ file using “--scoreFileName”, and a.bed file containing hg38 retention element coordinates using “--regionsFileName”, along with the following parameters: “--regionBodyLength 5000 --beforeRegionStartLength 5000 --afterRegionSt...
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Version used: **3.5.0**
- Evidence: Signal visualization files and images were generated using deepTools v.3.5.0 ( 81 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Version used: **3.3.2**
- Evidence: Reads per kilobase and million mapped read (RPKM)-normalized bigWig files were generated with bamCoverage from deepTools v3.3.2.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### Fever supports CD8<sup>+</sup> effector T cell responses by promoting mitochondrial translation. (PNAS 2021)

- DOI: 10.1073/pnas.2023752118 | PMCID: PMC8237659 | PMID: 34161266
- Evidence: Sequenced libraries were processed with the Galaxy platform and deepTools for quality control ( 37 ), Spliced Transcripts Alignment to a Reference (STAR) ( 38 ) for trimming and mapping, and featureCounts ( 39 ) to quantify mapped reads.
- Full pipeline: quality control [Galaxy, deepTools, featureCounts] -> read trimming [Galaxy, deepTools, featureCounts] -> alignment/mapping [DESeq2, Galaxy, R, deepTools, featureCounts] -> quantification [DESeq2, Galaxy, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [ImageJ, Metascape]

### CRISPR-based targeting of DNA methylation in <i>Arabidopsis thaliana</i> by a bacterial CG-specific DNA methyltransferase. (PNAS 2021)

- DOI: 10.1073/pnas.2125016118 | PMCID: PMC8201958 | PMID: 34074795
- Evidence: Coverage tracks were generated using bamCoverage [deepTools, options–binSize 1–normalizeUsing CPM ( 28 )], and replicates were then pooled using bigWigMerge from the University of California Santa Cruz (UCSC) toolkit ( 29 ).
- Full pipeline: alignment/mapping [Bismark, HTSeq] -> normalisation [deepTools] -> differential/statistical testing [DESeq2]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Evidence: To generate genome coverage file, we used the bamCoverage from the deepTools suite ( 72 ) (version 3.5.0) to convert the STAR generated Aligned.sortedByCoord.out.bam file to a bigwig file binned at 10 bp, using command: bamCoverage -b Aligned.sortedByCoord.out.bam -o Aligned.sortedByCoord.out.bw–binSize 10.
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### The Myc-associated zinc finger protein (MAZ) works together with CTCF to control cohesin positioning and genome organization. (PNAS 2021)

- DOI: 10.1073/pnas.2023127118 | PMCID: PMC7896315 | PMID: 33558242
- Evidence: Heat map was generated with deepTools.
- Full pipeline: stage not stated [R, deepTools]

### Transcriptional control of cone photoreceptor diversity by a thyroid hormone receptor. (PNAS 2022)

- DOI: 10.1073/pnas.2209884119 | PMCID: PMC9894165 | PMID: 36454759
- Evidence: Libraries were normalized to reads per genomic coverage using deepTools bamCoverage, and peaks visualized on gene maps by Integrative Genomic Viewer (v2.8.12).
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [deepTools] -> differential/statistical testing [DESeq2, MACS2 v2.2.7.1, edgeR] -> visualisation [deepTools]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Version used: **3.1.3**
- Evidence: For visualization, the filtered, sorted, and indexed BAM files were converted to the bigwig format by using the bamCoverage function in deepTools v.3.1.3 ( 102 ) with a bin size of 10 bp and RPKM normalization.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### Polycomb group (PcG) proteins prevent the assembly of abnormal synaptonemal complex structures during meiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2204701119 | PMCID: PMC9586294 | PMID: 36215502
- Evidence: Coverage plots were performed with the wiggleplotr R package using bigWig files obtained from the RNA-seq alignments transformed with the deepTools bamcoverage tool with CPM normalization ( 75 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR, deepTools] -> normalisation [R, deepTools, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [MACS2]

### Winter warming post floral initiation delays flowering via bud dormancy activation and affects yield in a winter annual crop. (PNAS 2022)

- DOI: 10.1073/pnas.2204355119 | PMCID: PMC9522361 | PMID: 36122201
- Version used: **2.3**
- Evidence: Then, the peaks of anti-H3K4me3 were normalized and visualized by bamCoverage of deepTools v2.3 and Integrative Genomics Viewer (IGV) v2.12.0, respectively ( 40 , 41 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HISAT2 v2.2.1] -> normalisation [deepTools v2.3] -> visualisation [deepTools v2.3] -> stage not stated [HOMER, Picard, R, WGCNA]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **3.2.0**
- Evidence: Integrated Genome Browser–compatible files were made using samtools (v1.9), sort and index, deepTools (v3.2.0), and bamCompare ( 44 , 45 ).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### The ZCCHC14/TENT4 complex is required for hepatitis A virus RNA synthesis. (PNAS 2022)

- DOI: 10.1073/pnas.2204511119 | PMCID: PMC9282228 | PMID: 35867748
- Evidence: Peaks enriched for reads mapping to HAV RNA were analyzed with deeptools/3.2.0.
- Full pipeline: alignment/mapping [HOMER v4.11, deepTools]

### The evening complex integrates photoperiod signals to control flowering in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2122582119 | PMCID: PMC9245669 | PMID: 35733265
- Evidence: BigWig files for IGV tracks were generated using deepTools function bamCoverage and normalized using RPKM.
- Full pipeline: alignment/mapping [HISAT2] -> quantification [StringTie, deepTools] -> normalisation [deepTools] -> stage not stated [BEDTools v2.30.0, BWA, MACS2, R, SAMtools v1.11]

### Zinc finger protein 280C contributes to colorectal tumorigenesis by maintaining epigenetic repression at H3K27me3-marked loci. (PNAS 2022)

- DOI: 10.1073/pnas.2120633119 | PMCID: PMC9295756 | PMID: 35605119
- Version used: **3.1.3**
- Evidence: For a ChIP signal heatmap and profile curve in given genomic intervals, a score matrix was first calculated using computeMatrix in deeptools (version 3.1.3) at a bin size of 10 bp, then plotHeatmap and plotProfiles in deeptools were used for visualization.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, MACS2 v2.1.6] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> visualisation [deepTools v3.1.3] -> stage not stated [GSEA]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: Spearman correlation analysis between the 3-h pupal tissues was performed using deepTools ( 52 ).
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Evidence: Normalized read coverage tracks were generated using the USeq package Sam2Useq application ( 45 ) and deepTools ( 46 ).
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Version used: **3.5.1**
- Evidence: Heatmaps and metaplots were generated using deepTools 3.5.1 ( 51 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Version used: **2.0**
- Evidence: BigWig files were generated from the aligned SAM or BED-file formats using Samtools, Bedtools ( 53 ), and deepTools 2.0 ( https://deeptools.readthedocs.io/en/develop/index.html ).
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: The average methylation levels within 10-kb windows were calculated by deepTools ( 45 ) multiBigwigSummary.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### TGF-β broadly modifies rather than specifically suppresses reactivated memory CD8 T cells in a dose-dependent manner. (PNAS 2023)

- DOI: 10.1073/pnas.2313228120 | PMCID: PMC10691214 | PMID: 37988468
- Evidence: Genome-wide visualization of ATAC-seq coverage was computed with deeptools ( 65 ) function coveragebam, using scale factors computed based on the number of reads within the total peak set.
- Full pipeline: normalisation [limma] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2, R]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: Peaks were called with MACS2 callpeak tool with default settings and plots were generated using deepTools plotHeatmap.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Mechanoepigenetic regulation of extracellular matrix homeostasis via Yap and Taz. (PNAS 2023)

- DOI: 10.1073/pnas.2211947120 | PMCID: PMC10235980 | PMID: 37216538
- Evidence: To generate BigWig files, deepTools BamCoverage was used with default settings and a bin size of 10 bp ( 69 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2, Picard, SAMtools, deepTools, featureCounts]

### Osteolectin increases bone elongation and body length by promoting growth plate chondrocyte proliferation. (PNAS 2023)

- DOI: 10.1073/pnas.2220159120 | PMCID: PMC10235998 | PMID: 37216542
- Version used: **3.5.1**
- Evidence: In wild-type samples, 72% of raw reads with a >10 MAPQ score were processed by deepTools 3.5.1 to generate bigwig files, and IGV version 2.11.9 was used to browse them and generate panel Fig.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bowtie2 v4.1, Trim Galore v0.6.4] -> alignment/mapping [Bowtie2 v4.1, SAMtools v1.12, Trim Galore v0.6.4] -> stage not stated [deepTools v3.5.1]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Version used: **3.5**
- Evidence: To assess the reproducibility of replicates, the read coverage of genomic regions was calculated for filtered BAM files using the deeptools v3.5 multiBamSummary bins command with a bin size of 10 kb.
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Evidence: For visualization, bam files of both IP and input samples were collapsed for PCR duplicates using SAMtools, and IP samples were normalized to their corresponding inputs and to their library size using deeptools’ v3.2.1 ( 73 ) bamCompare.
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### Molecular basis of locus-specific H3K9 methylation catalyzed by SUVH6 in plants. (PNAS 2023)

- DOI: 10.1073/pnas.2211155120 | PMCID: PMC9910501 | PMID: 36580600
- Evidence: The methylation levels were plotted by deepTools with bin size = 10bp.
- Full pipeline: visualisation [deepTools]

### Non-B-form DNA tends to form in centromeric regions and has undergone changes in polyploid oat subgenomes. (PNAS 2023)

- DOI: 10.1073/pnas.2211683120 | PMCID: PMC9910436 | PMID: 36574697
- Evidence: For visualization, the alignment BAM files were converted to normalized coverage files with 50-bp bins with deepTools ( 68 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA, Trimmomatic v0.36] -> alignment/mapping [BWA, MACS2, SAMtools v1.3.1, deepTools] -> normalisation [deepTools] -> visualisation [deepTools]

### Histone methyltransferase SETDB1 safeguards mouse fetal hematopoiesis by suppressing activation of cryptic enhancers. (PNAS 2024)

- DOI: 10.1073/pnas.2409656121 | PMCID: PMC11670114 | PMID: 39689172
- Evidence: Coverage heatmaps were generated using deeptools ( 65 ).
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, RSEM, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [RSEM, pheatmap] -> stage not stated [BEDTools, GSEA, MACS2, deepTools]

### Long-range &lt;i&gt;Atoh1&lt;/i&gt; enhancers maintain competency for hair cell regeneration in the inner ear. (PNAS 2024)

- DOI: 10.1073/pnas.2418098121 | PMCID: PMC11665905 | PMID: 39671177
- Evidence: Bioinformatic analysis used cellranger, Seurat ( 60 ), Signac ( 61 ), deepTools ( 62 ), DESeq2 ( 63 ), DiffBind ( 64 ), and Homer ( 55 ).
- Full pipeline: stage not stated [DESeq2, Seurat, Signac, deepTools]

### An E2 ubiquitin-conjugating enzyme links diubiquitinated H2B to H3K27M oncohistone function. (PNAS 2024)

- DOI: 10.1073/pnas.2416614121 | PMCID: PMC11621828 | PMID: 39560642
- Version used: **3.3.1**
- Evidence: Spike-in-normalized bigwig track files were created using bamCoverage from deepTools v3.3.1, with settings --binSize=20 --smoothLength=60 --normalizeUsing BPM --scaleFactor $scale_factor, where $scale_factor = the ratio of total reads/spike-in reads.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [deepTools v3.3.1] -> stage not stated [ChimeraX, SAMtools v1.8]

### Characterization of the enzyme for 5-hydroxymethyluridine production and its role in silencing transposable elements in dinoflagellates. (PNAS 2024)

- DOI: 10.1073/pnas.2400906121 | PMCID: PMC11572971 | PMID: 39508766
- Version used: **3.5.5**
- Evidence: Spearman’s correlations between samples were analyzed based on output from deepTools (version 3.5.5).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.2.5, HOMER, STAR v2.7.10a] -> quantification [HOMER] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [deepTools v3.5.5, featureCounts v1.5.3]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: We measured coverage using the “bamCoverage” function in the deepTools software package ( 61 , 113 ) and recorded it as counts per million reads (CPM) in the entire genome using the “exactScaling” option.
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### AMBRA1 controls the translation of immune-specific genes in T lymphocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2416722121 | PMCID: PMC11536168 | PMID: 39436665
- Evidence: To create bigwig files, BAM files were first indexed with samtools using default settings, and bigwig files were generated with the bamCoverage function from deepTools.
- Full pipeline: quantification [HTSeq] -> normalisation [pheatmap] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, SAMtools, deepTools]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Evidence: Density signals were calculated using the deeptools bamCoverage ( 47 ) and visualized with the Integrative Genomics Viewer ( 48 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **3.5.1**
- Evidence: To generate bigwig files, merged (AR or IgG) or individual (H3K4me3) BAM files were converted to counts per million (CPM)-normalized bigwig files using deepTools (v3.5.1) ( 75 ) bamCoverage (--binSize 100 --normalizeUsing CPM).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: For an in-depth examination of DNA methylation patterns in all three sequence contexts (CG, CHH, and CHG), relevant genomic data were extracted and visualized utilizing ViewBS and deeptools programs.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: For visualization, BAM files were converted into bigwig files using deeptools bamCoverage ( 69 ) (bamCoverage ––outFileFormat bigwig ––binSize 1 ––normalizeUsing None ––minMappingQuality 1).
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### An atlas of the tomato epigenome reveals that KRYPTONITE shapes TAD-like boundaries through the control of H3K9ac distribution. (PNAS 2024)

- DOI: 10.1073/pnas.2400737121 | PMCID: PMC11252963 | PMID: 38968127
- Version used: **3.5.0**
- Evidence: Read density was assessed using the bamCoverage function of deeptools v3.5.0 ( 49 ) software with default parameters.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bismark v0.24.0, Bowtie2 v2.3.5] -> differential/statistical testing [BEDTools v2.28.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, R, deepTools v3.5.0]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Evidence: Aligned mouse bam files were normalized to Counts per Million (CPM) and input reads were subtracted from IP reads using deepTools bamCompare ( 51 ).
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### CRISPRi screens identify the lncRNA, <i>LOUP</i>, as a multifunctional locus regulating macrophage differentiation and inflammatory signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2322524121 | PMCID: PMC11145268 | PMID: 38781216
- Evidence: Replicates were merged, and alignments were converted to BigWig tracks with the bamCoverage (--binsize 1) module from deepTools ( 58 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, deepTools] -> stage not stated [AlphaFold, DESeq2]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Evidence: For quantitative analysis of ChIP-Seq signals across the genome, Bam files from biological replicates underwent normalization to Input and conversion into bigwig files using bamCompare of deepTools package.
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: Processed files were aligned to the mm10 assembly with hisat2 ( 32 ) and converted to bigwig files with deepTools ( 33 ) bamCoverage function.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Version used: **3.5.1**
- Evidence: Occupancy and log2 fold change heatmaps were generated using deepTools v.3.5.1 ( 93 ).
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: Subsequent analyses for visualization of ChIP-seq were done using samtools ( 60 ), deeptools ( 61 ), and SparK ( 62 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### COP1 controls light-dependent chromatin remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2312853121 | PMCID: PMC10895365 | PMID: 38349881
- Evidence: Mapped reads were normalized using deepTools and visualized using IGV.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, deepTools] -> normalisation [deepTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [ImageJ, MACS2]

### Minimal requirements for the epigenetic inheritance of engineered silent chromatin domains. (PNAS 2024)

- DOI: 10.1073/pnas.2318455121 | PMCID: PMC10801849 | PMID: 38198529
- Version used: **3.5.2**
- Evidence: Data were normalized to counts per million using the bamCoverage module of deepTools 3.5.2 and visualized in IGV 2.16.0.
- Full pipeline: normalisation [deepTools v3.5.2] -> visualisation [deepTools v3.5.2]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Version used: **3.0.2**
- Evidence: To compute DNA methylation levels across 1 kb upstream and downstream of CEN178 centers, deepTools (v 3.0.2) ( 36 ) was used with the computeMatrix reference-point option.
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Version used: **3.4.3**
- Evidence: Coverage was calculated from BAM files using the bamCoverage tool in deepTools (v3.4.3) ( 65 ), with normalization set to reads per genomic content.
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### Genome-wide strand-specific UV mutagenesis in &lt;i&gt;&lt;i&gt;Escherichia coli&lt;/i&gt;&lt;/i&gt; is directed by the Mfd translocase. (PNAS 2025)

- DOI: 10.1073/pnas.2523368122 | PMCID: PMC12646321 | PMID: 41231941
- Evidence: Strand-specific genome-wide coverage profiles were generated using deepTools ( 30 ) bamCoverage, with CPM (counts per million) normalization and a bin size of 1 bp.
- Full pipeline: read trimming [STAR v2.7, Trimmomatic] -> alignment/mapping [SAMtools, STAR v2.7] -> normalisation [deepTools] -> stage not stated [Conda, Snakemake]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **3.4.1**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Sperm and offspring production in a nonobstructive azoospermia mouse model via testicular mRNA delivery using lipid nanoparticles. (PNAS 2025)

- DOI: 10.1073/pnas.2516573122 | PMCID: PMC12557808 | PMID: 41082659
- Evidence: To assess potential large-scale genomic alterations such as insertions or deletions, genome-wide read depth profiles were generated using bamCompare from the deepTools suite (v3.4.3).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt v3.2] -> alignment/mapping [Bowtie2 v2.3.5.1, Cutadapt v3.2, SAMtools v1.20] -> stage not stated [deepTools]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Evidence: Postalignment processing was performed using Picard, MarkDuplicates, SAMtools, and deepTools.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: Uniquely mapped reads were kept for downstream analysis using Samtools-1.9 and Sambamba-6.7 ( 51 , 52 ), bigwig files were calculated using deepTools-3.1.1 ( 53 ) with a bin size of 50 bp, before visualization in IGV-2.12.3 ( 54 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: Matrixes were generated using deeptools 2 ( 56 ): computeMatrix with the L1s coordinates ( SI Appendix , Table S1 ) (-R) and various Bigwigs (-S)”; and the following options -bs 50 –sortRegions keep –sortUsing mean –averageTypeBins mean –outFileSortedRegions”.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Version used: **2.5.3**
- Evidence: Genome browser snapshots were generated using the R v4.0.3 environment and Rseb (v0.3.1) ( https://github.com/sebastian-gregoricchio/Rseb ) ( 58 ), while tornado plots have been produced using deepTools (v2.5.3).
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **3.3.1**
- Evidence: Mapped RNA-seq data from polyA enrichment and rRNA depletion experiments were normalized with deeptools v3.3.1 bamCoverage (--normalizeUsing BPM -p max -bs 100) ( 132 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: Bigwig tracks were generated using bamcoverage from the deeptools package and peaks were called using MACS2 ( 60 ) with the –broadpeak option.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### SCoTCH-seq reveals that 5-hydroxymethylcytosine encodes regulatory information across DNA strands. (PNAS 2025)

- DOI: 10.1073/pnas.2512204122 | PMCID: PMC12337322 | PMID: 40743391
- Evidence: Profiles of CpG states at each enhancer type were generated using deepTools ( 52 ) (200-bp bin size).
- Full pipeline: read trimming [Cutadapt v4.6, Picard v3.1.1, SAMtools v1.19.2] -> stage not stated [BEDTools v2.31.0, Snakemake v7.3.8, deepTools]

### Foxn3 is required to suppress aberrant ciliogenesis in nonphotoreceptor retinal neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2500871122 | PMCID: PMC12304973 | PMID: 40663603
- Evidence: Peak calling, identification of peak positions and distributions, and motif analysis were performed using the HOMER software suite ( http://homer.ucsd.edu/homer/index.html ) and deepTools ( 75 , 76 ).
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [HOMER, Seurat, deepTools, scDblFinder]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: Heatmaps and profile plots were generated by deepTools.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: To visualize deep-sequencing data, we used samtools, deeptools ( 67 ), and SparK ( https://github.com/harbourlab/SparK ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: Signal tracks were generated using the deeptools bamCoverage ( 63 ) (Version 3.5.1) and viewed on WashU Epigenome Browser.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Perturbing nuclear glycosylation in the mouse preimplantation embryo slows down embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2410520122 | PMCID: PMC12012502 | PMID: 40203037
- Version used: **3.0.2**
- Evidence: Bigwig files were obtained with deeptools v3.0.2, normalizing to bins per million.
- Full pipeline: read trimming [STAR v2.7.8a] -> alignment/mapping [STAR v2.7.8a] -> normalisation [DESeq2, deepTools v3.0.2] -> stage not stated [GSEA, ImageJ, featureCounts]

### Downregulation of Nesprin1 by Runx2 deficiency is critical for the development of skeletal laminopathy-like pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2320138122 | PMCID: PMC12012476 | PMID: 40208950
- Evidence: Metagene plots were generated from BAM files using deepTools’ bamCompare function.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP, scVelo] -> stage not stated [Galaxy, ImageJ, Python, Scanpy, deepTools]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Evidence: Signal tracks were generated using bamCoverage (version 3.5.1, deeptools) function and visualized by WashU Epigenome Browser website.
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Version used: **3.3.2**
- Evidence: BigWig files for visualization were created by deepTools (version 3.3.2) ( 82 ) with a 10 bp bin size, viewed via Integrative Genomics Viewer ( 83 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Evidence: DNA methylation patterns across contexts (CG, CHG, CHH) were visualized with deepTools ( 85 ).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Plant BCL-DOMAIN HOMOLOG proteins play a conserved role in SWI/SNF complex stability. (PNAS 2025)

- DOI: 10.1073/pnas.2413346122 | PMCID: PMC11761322 | PMID: 39823297
- Version used: **3.5.1**
- Evidence: Heatmaps and metaplots were produced using the computeMatrix and plotHeatmap or plotProfile commands from deeptools v3.5.1 ( 49 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, deepTools v3.5.1, ggplot2]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: Bigwigs were created for visualization using deepTools ( 58 ) (version 3.5.1-0) with the options −e and −RPCG.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2534844123 | PMCID: PMC13099603 | PMID: 41984841
- Evidence: Normalized coverage and ChIP/Input enrichment tracks were generated with deepTools (bamCoverage and bamCompare) using read count normalization.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, Trim Galore] -> quantification [deepTools] -> normalisation [deepTools] -> differential/statistical testing [DESeq2 v1.28.1, R] -> stage not stated [GSEA, SAMtools]

### Versatile SMAD2 and SMAD3 epitope-tagged mouse models for genomic profiling of TGFβ signaling: Uncovering GDF9-SMAD2/3 targets. (PNAS 2026)

- DOI: 10.1073/pnas.2600071123 | PMCID: PMC13056123 | PMID: 41911462
- Version used: **2.4.2**
- Evidence: Peak heatmaps and the density plots were generated using deepTools 2.4.2.
- Full pipeline: quality control [Bowtie2] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2, STAR v2.7.11b, featureCounts v2.1.1] -> quantification [STAR v2.7.11b] -> stage not stated [DESeq2 v1.48.2, HOMER v4.11, deepTools v2.4.2]

### KLF2 overrides the resident memory CD8 T cell differentiation program, in opposition to KLF3. (PNAS 2026)

- DOI: 10.1073/pnas.2533700123 | PMCID: PMC13037849 | PMID: 41871244
- Version used: **3.3.0**
- Evidence: Peaks were annotated using HOMER (v4.9.1), and heatmaps were generated with deepTools (v3.3.0).
- Full pipeline: quality control [FastQC v0.12.1, featureCounts v2.0.6] -> read trimming [FastQC v0.12.1, featureCounts v2.0.6] -> alignment/mapping [FastQC v0.12.1, featureCounts v2.0.6] -> differential/statistical testing [GSEA] -> stage not stated [HOMER v4.9.1, deepTools v3.3.0]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Version used: **3.5.1**
- Evidence: Coverage bigWig tracks were generated from alignment files using the bamCoverage function in deeptools v3.5.1 ( 56 ) with scale factors calculated by deeptools multiBamSummary.
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### EPOP and MTF2 activate PRC2 activity through DNA-sequence specificity. (PNAS 2026)

- DOI: 10.1073/pnas.2527303123 | PMCID: PMC12890814 | PMID: 41650228
- Evidence: Regions in mm10 genome blacklist was removed using bedtools and bigwig files were generated using deeptools and parameters: --binSize 50 --normalizeUsing RPKM --ignoreDuplicates --ignoreForNormalization chrX --extendReads 250 for visualization in IGV.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [BEDTools, deepTools] -> normalisation [BEDTools, deepTools] -> visualisation [BEDTools, deepTools] -> stage not stated [ImageJ, MACS2, SAMtools]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Evidence: Coverage bigwig files were generated with deepTools bamCoverage (v3.5.1) ( 113 ) with the following options:–normalizeUsing RPKM –extendReads –ignoreDuplicates.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Functional maps of a genomic locus reveal confinement of an enhancer by its target gene. (Science 2025)

- DOI: 10.1126/science.ads6552 | PMCID: PMC7618358 | PMID: 40966339
- Version used: **3.0**
- Evidence: The coverage files (bigwig files) were generated with RPKM normalization using deepTools (version 3.0).
- Full pipeline: alignment/mapping [BWA] -> quantification [deepTools v3.0] -> normalisation [deepTools v3.0] -> visualisation [Signac] -> stage not stated [BCFtools v1.9, MACS2, SnpEff v4.3p]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Version used: **3.5.6**
- Evidence: To generate profile plots and heatmaps, we used deepTools v3.5.6 with the following procedure.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

