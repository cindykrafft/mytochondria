# featureCounts

- **Category:** genomics
- **Papers in survey:** 331
- **Journals:** PNAS (164), Nature (143), Cell (19), Science (5)
- **Years:** 2021 (28), 2022 (57), 2023 (62), 2024 (67), 2025 (81), 2026 (36)
- **Versions named:** 2.0.1 (32), 2.0.0 (15), 1.5.0 (10), 1.6.3 (9), 1.6.2 (8), 2.0.6 (7), 1.6.4 (7), 1.6.0 (5), 1.6.1 (4), 1.5.2 (3)
- **Pipeline stages it appears in:** alignment/mapping (161), quantification (142), differential/statistical testing (31), read trimming (27), normalisation (21), quality control (14), visualisation (2), dimensionality reduction/clustering (2), registration (1), variant calling (1)

## Papers

### Identification of a therapeutic interfering particle-A single-dose SARS-CoV-2 antiviral intervention with a high barrier to resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.004 | PMCID: PMC8577993 | PMID: 34838159
- Evidence: Transcript level quantification was performed using featureCounts (subread-2.0.2) with default parameters.
- Full pipeline: quantification [DESeq2, featureCounts] -> simulation/modelling [Python] -> visualisation [Matplotlib v3.3.3, seaborn v0.11.0] -> stage not stated [ImageJ, NumPy v1.19.4, SciPy v1.5.4]

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: 1072534 Software and algorithms Galaxy platform Afgan et al., 2016 N/A Deeptools Ramírez et al., 2016 N/A STAR Dobin et al., 2013 N/A FeatureCounts Liao et al., 2014 N/A DESeq2 Love et al., 2014 N/A Morpheus Broad Institute N/A DAVID Huang et al., 2009 N/A Trimmomatic Bolger et al., 2014 N/A Bowtie2 Langmead and Salzberg, 2012 N/A SAM tools Li et al., 2009 N/A MACS2 Zhang et al., 2008 N/A Bedtools...
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: Gene-count summaries were generated with featureCounts ( Liao et al., 2014 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Version used: **2.0.1**
- Evidence: Uniquely mapped reads were counted across genes with a program in Bioconductor R ( Huber et al., 2015 ) package, featureCounts (version 2.0.1) ( Liao et al., 2014 ).
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Evidence: Remaining reads were then aligned to the host genome and reads overlapping genomic features (genes) were quantified using the featureCounts command line utility ( Liao et al., 2014 ).
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Version used: **1.6.2**
- Evidence: Reads that fell inside peaks were counted using featureCounts v1.6.2 ( Liao et al., 2014 ) and differential accessibility analysis was performed using DESeq2 v1.32 ( Love et al., 2014 ).
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ...Btools) ( Bushnell et al., 2017 ) v38.90 HISAT2 ( Kim et al., 2015 ) v2.1.0 FastQC https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ v0.11.9 FeatureCounts ( Liao et al., 2014 ) v2.0.1 Astra Wyatt Technology v8.0 Compass Bruker Daltonics v1.2 TopSpin Bruker BioSpin GmbH V4.1.3 Resource availability Lead contact Further information and requests for resources should be directed to the lead c...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: Reads were aligned to human genome (hg38), Mesocricetus auratus (MesAur1.0) and SARS-CoV-2 (wuhCor1) using Subread ( Liao et al., 2013 ) and the raw read counts were assembled using featureCounts pipeline( Liao et al., 2014 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...., 2016b ) http://galahad.well.ox.ac.uk/XGR Fastcluster ( Mulner, 2013 ) v1.1.25 FastQC ( Andrews, 2010 ) v0.11.9 https://github.com/s-andrews/FastQC featureCounts ( Liao et al., 2014 ) v1.6.4 fgsea ( Korotkevich et al., 2021 ) https://bioconductor.org/packages/release/bioc/html/fgsea.html FlowJo BD Biosciences v10.6 https://www.flowjo.com Fragpipe ( Yu et al., 2021 ) v13.0 GATK variant calling ( ...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: Reads aligning to the two intervals were counted by featureCounts 100 in a strand unspecific manner.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **2.0.1**
- Evidence: The reads were mapped with HISAT2 v2.2.1, 101 the .sam files resulting from each mapping were converted into .bam files and indexed using SAMtools v1.10 102 and the reads mapped against each gene were counted using featureCounts v2.0.1.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: 71 Read counts for each gene annotation were generated with featureCounts 72 and normalized.
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 42 http://amp.pharm.mssm.edu/Enrichr/ featureCounts Liao et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Evidence: Read counts were then assessed using featureCounts function in Subread package (version 2.0.1).
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Version used: **2.0.0**
- Evidence: 121 http://www.htslib.org/ FeatureCounts v2.0.0 Liao et al.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Version used: **1.4.4**
- Evidence: 100 Then the mRNA expression was quantified and summarized at the gene level by featureCounts (v1.4.4) 101 based on Ensembl gene model GRCh37.70.
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### Proximity-specific ribosome profiling reveals the logic of localized mitochondrial translation. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.002 | PMCID: PMC12650760 | PMID: 40876456
- Version used: **1.6.2**
- Evidence: RNA-seq Raw sequencing reads were aligned to the human genome (GRCh38.99) using STAR 2.7.1a 72 and quantified using featureCounts 1.6.2 73 .
- Full pipeline: alignment/mapping [STAR v2.7.1a, TopHat v2.1.1, featureCounts v1.6.2] -> quantification [STAR v2.7.1a, featureCounts v1.6.2]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: 184 Mapped reads were quantified using featureCounts software package 201 and differential expression analysis was performed using DESeq2 software.
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### Citrate clearance is a major function of aconitase 2 in the canonical TCA cycle. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.028 | PMCID: PMC13045649 | PMID: 41763199
- Evidence: A matrix of raw counts was generated using featureCounts/subread (version 2.16.1).
- Full pipeline: differential/statistical testing [DESeq2 v1.46.0] -> stage not stated [GSEA, R v4.3.2, featureCounts, fgsea, ggplot2 v3.5.2]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Version used: **1.4.6**
- Evidence: 68 ) and transcripts per feature were quantified using featureCounts v.1.4.6 (ref.
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Sulfur sequestration promotes multicellularity during nutrient limitation. (Nature 2021)

- DOI: 10.1038/s41586-021-03270-3 | PMCID: PMC7969356 | PMID: 33627869
- Evidence: Sequenced libraries were processed with deepTools 49 , using STAR 50 , for trimming and mapping, and featureCounts 51 to quantify mapped reads.
- Full pipeline: read trimming [Seurat, UMAP, deepTools, featureCounts] -> alignment/mapping [DESeq2, R, Seurat, UMAP, deepTools, featureCounts] -> quantification [DESeq2, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: RNA-Seq reads were then aligned to GRCm38.91 (mm10) with STAR 71 and transcript count was quantified using featureCounts 52 to generate raw count matrix.
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Version used: **2.0.0**
- Evidence: Then the transcriptomes were annotated to GENCODE M23 ( gencodegenes.org ) 60 by FeatureCounts (2.0.0) 61 .
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### Control of osteoblast regeneration by a train of Erk activity waves. (Nature 2021)

- DOI: 10.1038/s41586-020-03085-8 | PMCID: PMC7864885 | PMID: 33408418
- Evidence: Gene-level read counts were obtained using the featureCounts 34 (v1.6.1) by the reads with MAPQ greater than 30.
- Full pipeline: read trimming [TopHat, Trim Galore v0.4.1] -> alignment/mapping [TopHat, Trim Galore v0.4.1] -> quantification [featureCounts] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> stage not stated [ilastik v1.3.3]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **1.6.4**
- Evidence: Gene-level assignment was then performed using featureCounts 1.6.4 57 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Defining HPV-specific B cell responses in patients with head and neck cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-2931-3 | PMCID: PMC9462833 | PMID: 33208941
- Evidence: Alignments were sorted and indexed with samtools 43 , and aligned reads assigned to the Ensembl reference transcriptome release 90 with featureCounts 44 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [R, Seurat v3.1.4]

### Nociceptor neurons affect cancer immunosurveillance. (Nature 2022)

- DOI: 10.1038/s41586-022-05374-w | PMCID: PMC9646485 | PMID: 36323780
- Evidence: Aligned reads were assigned to genic regions using the featureCounts function from subread v.1.6.4 (ref.
- Full pipeline: read trimming [STAR v2.5.1b, Trimmomatic v0.35] -> alignment/mapping [STAR v2.5.1b, Trimmomatic v0.35, featureCounts] -> quantification [Bioconductor, RSEM] -> normalisation [Bioconductor, RSEM] -> dimensionality reduction/clustering [R] -> stage not stated [DESeq2 v1.18.1, ImageJ]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Version used: **1.6.2**
- Evidence: Reads were counted towards human genes (GENCODE v35) and SARS-CoV-2 genes (WA-CDC-WA1/2020 assembly; MN985325.1 ) using featureCounts (v1.6.2).
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: Gene expression was quantified with featureCounts 56 (v1.5.2).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Evidence: Alignment files were individually name-sorted using Samtools v1.11 57 , and then used to create a cell-by-gene count matrix using featureCounts 58 (subread v2.0.1).
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: Gene-level read counts were obtained by running featureCounts 51 , a read count summarization program within the Rsubread package 52 and the inbuilt Rsubread annotation that is a modified version of the NCBI RefSeq mouse (mm10) genome annotation build 38.1.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Truncated FGFR2 is a clinically actionable oncogene in multiple cancers. (Nature 2022)

- DOI: 10.1038/s41586-022-05066-5 | PMCID: PMC9436779 | PMID: 35948633
- Version used: **1.6.2**
- Evidence: Gene- and exon-level expression read counts were quantified by featureCounts (v.1.6.2) 97 on the basis of gene structures defined in GRCh38.
- Full pipeline: read trimming [edgeR v3.26.6] -> alignment/mapping [BWA v0.7.5a, STAR v2.7.2] -> quantification [RSEM v1.3.0, edgeR v3.26.6, featureCounts v1.6.2] -> normalisation [edgeR v3.26.6] -> differential/statistical testing [R, limma v3.52.1]

### Brown-fat-mediated tumour suppression by cold-altered global metabolism. (Nature 2022)

- DOI: 10.1038/s41586-022-05030-3 | PMCID: PMC9365697 | PMID: 35922508
- Version used: **2.0.0**
- Evidence: Aligned reads were summarized using featureCounts (v.2.0.0) based on the Gencode vM19 annotation.
- Full pipeline: alignment/mapping [featureCounts v2.0.0] -> differential/statistical testing [DESeq2 v1.30.0, GSEA v4.1.0] -> stage not stated [ImageJ]

### ADAR1 averts fatal type I interferon induction by ZBP1. (Nature 2022)

- DOI: 10.1038/s41586-022-04878-9 | PMCID: PMC9329096 | PMID: 35859176
- Evidence: Remaining reads were passed to HISAT2 (v2.1.0) 51 for strand-aware alignment, and strand-specific counts of uniquely mapping reads were prepared using featureCounts (within Subread v1.6.4; ref.
- Full pipeline: quality control [Cutadapt v3.4, FastQC v0.11.8] -> read trimming [Cutadapt v3.4, FastQC v0.11.8] -> alignment/mapping [HISAT2 v2.1.0, SAMtools, featureCounts] -> quantification [DESeq2 v1.22.1] -> normalisation [DESeq2 v1.22.1] -> differential/statistical testing [DESeq2 v1.22.1] -> visualisation [DESeq2 v1.22.1] -> stage not stated [QuPath v0.3.2]

### Apoptotic brown adipocytes enhance energy expenditure via extracellular inosine. (Nature 2022)

- DOI: 10.1038/s41586-022-05041-0 | PMCID: PMC9452294 | PMID: 35790189
- Version used: **2.0.1**
- Evidence: FeatureCounts (v.2.0.1, ref.
- Full pipeline: normalisation [DESeq2 v1.32.0] -> stage not stated [MACS2, featureCounts v2.0.1, ggpubr v0.4.0]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Version used: **1.4.5**
- Evidence: Count data were generated by FeatureCounts v.1.4.5-p1 with parameters --minReadOverlap 3 -T 3 -M -O -s 0 using the gencode.v32.annotation.gtf ( https://www.gencodegenes.org/ ) file for annotation 51 .
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **2.0.1**
- Evidence: After 80% read coverage and 95% identity filtering, the BAM files were processed using FeatureCounts (v.2.0.1) 88 (using the parameters featureCounts --primary -O --fraction -t CDS,tRNA -F GTF -g ID -p) to compute the number of inserts per gene.
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: The number of reads mapping to the exons of each gene was counted with featureCounts 82 , using the NCBI RefSeq mm10 gene annotation.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **1.6.4**
- Evidence: The read counts mapping to ABO (exon 1 to 7) were quantified for each sample using featureCounts (v.1.6.4) 79 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Intron-mediated induction of phenotypic heterogeneity. (Nature 2022)

- DOI: 10.1038/s41586-022-04633-0 | PMCID: PMC9068511 | PMID: 35444278
- Evidence: The reads mapping to introns or CDS of intron-containing genes were quantified using featureCounts 53 using custom produced .saf files extracted from the reference .gff annotation file.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, TopHat, featureCounts] -> quantification [featureCounts] -> visualisation [Clustal Omega] -> stage not stated [ImageJ]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: Gene expression was quantified using FeatureCounts 40 using gene models from GENCODE v31.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Evidence: Reads were aligned to the genome using star v2.6.0c and reads in genes were counted with featureCounts (subread v1.6.2) and parameter -s 0.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **2.0.0**
- Evidence: The aligned reads at standard and allele-specific levels were counted separately using Gencode GTF (m9) using featureCounts (v.2.0.0) 61 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Mouse genome rewriting and tailoring of three important disease loci. (Nature 2023)

- DOI: 10.1038/s41586-023-06675-4 | PMCID: PMC10632133 | PMID: 37914927
- Version used: **1.6.3**
- Evidence: The genes–samples counts matrix was generated using featureCounts (v1.6.3), normalized based on their library size factors using DEseq2, and differential expression analysis was performed.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, STAR] -> normalisation [deepTools v3.1.0, featureCounts v1.6.3] -> differential/statistical testing [featureCounts v1.6.3] -> stage not stated [Picard, fastp]

### Glioma synapses recruit mechanisms of adaptive plasticity. (Nature 2023)

- DOI: 10.1038/s41586-023-06678-1 | PMCID: PMC10632140 | PMID: 37914930
- Evidence: Reads were mapped to hg19 annotation using Tophat2 63 (version 2.0.13) and transcript expression was quantified against RefSeq gene annotations using featureCounts 64 (v2.0.3).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [ImageJ v2.1.0, RSEM, featureCounts, kallisto] -> normalisation [RSEM] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.36.0] -> visualisation [ImageJ v2.1.0] -> stage not stated [R v4.1.1]

### Inhibition of fatty acid oxidation enables heart regeneration in adult mice. (Nature 2023)

- DOI: 10.1038/s41586-023-06585-5 | PMCID: PMC10584682 | PMID: 37758950
- Evidence: The number of reads aligning to genes was counted with featureCounts ≥ 1.6.0 from the Subread package 50 .
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [FastQC v0.11.8, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Version used: **2.0.0**
- Evidence: Aligned reads were assigned to small RNA loci and classes using Samtools v.1.10, GNU Awk v.5.1.0 and Subread featureCounts v.2.0.0 ( https://subread.sourceforge.net/ ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Evidence: Mapped reads that fell on genes were counted using featureCounts from Rsubread package 69 .
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Version used: **2.0.1**
- Evidence: Primary alignments were selected using samtools (v.1.7) and reads per genomic feature were counted with featureCounts (v.2.0.1 from Subread package).
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### cGAS-STING drives ageing-related inflammation and neurodegeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-06373-1 | PMCID: PMC10412454 | PMID: 37532932
- Version used: **2.0.1**
- Evidence: For bulk hippocampus, RNA was mapped to the mouse genome assembly GRCm39 (release 109) using STAR aligner (v.2.7.10b), and counts were generated using featureCounts (v.2.0.1).
- Full pipeline: alignment/mapping [HTSeq, STAR, featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.38.2, ImageJ, Seurat]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Version used: **2.0.0**
- Evidence: Features were counted using featureCounts (v.2.0.0) 104 .
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### PLSCR1 is a cell-autonomous defence factor against SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06322-y | PMCID: PMC10371867 | PMID: 37438530
- Evidence: The uniquely mapped reads (cut-off: mapping quality score (MAPQ) > 10) were counted to ENCODE gene annotation (v.24) using FeatureCounts.
- Full pipeline: alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, R] -> simulation/modelling [AlphaFold, GROMACS v2021.3, Python] -> stage not stated [PyMOL, VMD]

### Mast cells link immune sensing to antigen-avoidance behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06188-0 | PMCID: PMC10432277 | PMID: 37438525
- Evidence: Data were mapped using STAR aligner (v.2.5.2b) 68 , and reads were annotated using the FeatureCounts algorithm from the subread package (v.1.5.1) 69 .
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [DESeq2]

### Heritable transcriptional defects from aberrations of nuclear architecture. (Nature 2023)

- DOI: 10.1038/s41586-023-06157-7 | PMCID: PMC10322708 | PMID: 37286600
- Evidence: We first generated feature counts from analysis-ready RNA-seq bam files using featureCounts from Subread 2.0.1 ( https://subread.sourceforge.net ) and then calculated total TPM 47 .
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, GATK v4.1.9.0, STAR v2.7.6a] -> quantification [RSEM, featureCounts] -> stage not stated [ImageJ, MACS2, Python]

### Myelin dysfunction drives amyloid-β deposition in models of Alzheimer's disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06120-6 | PMCID: PMC10247380 | PMID: 37258678
- Version used: **1.6.3**
- Evidence: Gene raw counts of each sample were extracted using featureCounts (v.1.6.3) 71 from aligned profiles for differential gene expression analysis using DESeq2 (v.1.26.0) 72 and converted to TPM value for sample distance calculation and visualization, as well as for gene expression pattern analysis.
- Full pipeline: quality control [STAR v2.5.2b] -> alignment/mapping [DESeq2 v1.26.0, STAR v2.5.2b, featureCounts v1.6.3] -> quantification [DESeq2 v1.26.0, featureCounts v1.6.3] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts v1.6.3] -> visualisation [DESeq2 v1.26.0, featureCounts v1.6.3] -> stage not stated [MACS2, R v4.04, afex v0.28]

### A Pseudomonas aeruginosa small RNA regulates chronic and acute infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06111-7 | PMCID: PMC10247376 | PMID: 37225987
- Evidence: As PA1414 ( sicX ) was originally annotated as a protein-coding gene, we first assigned reads to protein-coding genes with featureCounts Subread v2.0.1 (ref.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.4.2, Cutadapt v3.0] -> alignment/mapping [Bowtie2 v2.4.2, MUSCLE, SAMtools v1.13] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R, featureCounts]

### Glioblastoma remodelling of human neural circuits decreases survival. (Nature 2023)

- DOI: 10.1038/s41586-023-06036-1 | PMCID: PMC10191851 | PMID: 37138086
- Evidence: For differential expression analysis, we extracted exon-level count data from the mapped HISAT2 output using featureCounts 69 .
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [HISAT2, featureCounts] -> normalisation [Python, Seurat v3.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Python, R v3.1, Seurat v3.0.1, featureCounts] -> stage not stated [ImageJ]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Evidence: For these genes, a further filtration was done to eliminate any short (less than 50 amino acids) translated proteins, in-frame stop codons or low (less than 200 reads) expression featureCounts, subread v2.0.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: The number of reads mapped to the 3′ UTR of genes was determined using featureCounts.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: Bulk RNA-seq quantification of gene expression in vitro RNA-seq The featureCounts package 64 was used to count reads in cultured neuron RNA-seq data using a custom filtered annotation file (gencode.v17.annotation.gtf filtered for feature_type=“gene”, gene_type=“protein_coding” and gene_status=“KNOWN”) to obtain read counts along genes for each sample.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: Differential chromatin accessibility analysis Differentially accessible peaks were determined first by counting the number of reads overlapping each called peak region (using a merged peak file from all samples and replicates across the time course) using featureCounts software (from the subread package).
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **1.6.2**
- Evidence: The resulting reads were mapped onto the mouse genome (GRCm38, Ensembl 61 release 81) using HiSAT2 (v.2.1.0) 62 and quantified using featureCounts (v.1.6.2) 63 .
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Undecaprenyl phosphate translocases confer conditional microbial fitness. (Nature 2023)

- DOI: 10.1038/s41586-022-05569-1 | PMCID: PMC9876793 | PMID: 36450355
- Evidence: A read matrix for each sample was then generated with featureCounts from Rsubread (version 2.4.3) 61 .
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.3] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, ImageJ v1.53, InterProScan, featureCounts]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: Raw gene counts were quantified using the featureCounts 86 program of subread v.2.0.1.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Evidence: The full pipeline uses trimmomatic 75 (v0.33) to filter reads, Cutadapt 76 (v1.18) to demultiplex, UMI-tools 77 (v0.5.5) to extract UMIs, bwa 78 (v0.7.17) to align, and featureCounts 79 (v1.6.3) to annotate features.
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: Using featureCounts in Rsubread package in R, we counted all reads over the consensus peak regions, then performed differential accessible peak analysis using DESeq2.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: The featureCounts 106 module from the subread package (v.1.4.3-p1) was used for read quantification, with the argument ‘-s 2’ for strand-specific samples and argument ‘-s 0’ for non-strand-specific samples.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Evidence: Reads were counted for each GENCODE annotated gene using HTSeq (v.0.12.4) 60 and for caRNAs using featureCounts 64 , and then differentially expressed genes were called using DESeq2 package in R 65 with P < 0.05.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Evidence: The mapped reads were counted for each gene using featureCounts 64 version 1.5.2 with “-t exon -p -B -Q 1” options. the transcripts per million (TPM) values of each gene in each sample were calculated.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Version used: **1.6.0**
- Evidence: The aligned RNA-seq BAM files were used to quantify the gene-level read counts using featureCounts (v.1.6.0) 78 ; these counts were then vst-normalized and log 2 -transformed using DESeq2 (v.1.40.2) 69 to obtain values for the expression of all genes and all samples.
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Mitochondrial complex I promotes kidney cancer metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07812-3 | PMCID: PMC11424252 | PMID: 39143213
- Evidence: Features (genes, transcripts and exons) were counted using featureCounts 54 .
- Full pipeline: alignment/mapping [STAR v2.7.3] -> differential/statistical testing [DESeq2 v1.14.1, edgeR] -> stage not stated [HTSeq v0.6.1, ImageJ, R, featureCounts]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Evidence: Read counts were assigned to annotated features using featureCounts 107 .
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: Reads were aligned to the human genome version GRCh38 (downloaded from https://www.ensembl.org/Homo_sapiens/Info/Index ) using STAR 51 , and per-gene read counting was performed using the featureCounts function of the subread package in R 52 .
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **1.6.0**
- Evidence: Gene-level features were quantified using featureCounts v.1.6.0 based on GRCh38 gene annotation.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### Inhibition of IL-11 signalling extends mammalian healthspan and lifespan. (Nature 2024)

- DOI: 10.1038/s41586-024-07701-9 | PMCID: PMC11291288 | PMID: 39020175
- Evidence: The Ensembl release 104 M. musculus GRCm39 GTF was used as annotation to prepare STAR indexes and for FeatureCounts.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.7.9a] -> quantification [ImageJ v1.53t, pheatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.36.0, R v4.2] -> visualisation [pheatmap] -> stage not stated [featureCounts, fgsea v1.22.0]

### The cortical amygdala consolidates a socially transmitted long-term memory. (Nature 2024)

- DOI: 10.1038/s41586-024-07632-5 | PMCID: PMC11306109 | PMID: 38961294
- Version used: **2.0.0**
- Evidence: We determined gene counts using FeatureCounts (v.2.0.0) 77 .
- Full pipeline: alignment/mapping [STAR v2.7.10a, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Cellpose, R v4.2.2, featureCounts v2.0.0]

### dsRNA formation leads to preferential nuclear export and gene expression. (Nature 2024)

- DOI: 10.1038/s41586-024-07576-w | PMCID: PMC11236707 | PMID: 38898279
- Evidence: Subsequently, abundance measurement of reads overlapping with exons or introns was conducted with featureCounts 51 , subread v.1.5.0-p1, Ensembl (EF4.68) supplemented with the coordinates of UTRs, CUTs, SUTs 22 , 52 , 53 and XUTs 3 , 29 .
- Full pipeline: read trimming [Cutadapt v2.1, TopHat v2.1.1] -> alignment/mapping [Cutadapt v2.1, TopHat v2.1.1] -> quantification [featureCounts] -> stage not stated [BEDTools, Bioconductor, DESeq2]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: Left: z-scored log-transformed normalized gene counts obtained from salmon (bottom left of each cell) and featureCounts (top right of each cell).
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Gene read counts were obtained using the featureCounts program 76 from Rsubread using the GTF annotation file for GRCh38 (v.102).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: (Artificial Intelligence RNA-Seq) software from Sequentia Biotech with the following pipeline: BBDuk (reads trimming; BBDUkguide ), STAR (reads mapping to the mouse genome GRCm38 (ENSEMBL); https://github.com/alexdobin/STAR ), featureCounts (gene expression quantification; https://subread.sourceforge.net/featureCounts.html ) and NOISeq (statistical analysis of differentially expressed genes; http:...
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Adhesive anti-fibrotic interfaces on diverse organs. (Nature 2024)

- DOI: 10.1038/s41586-024-07426-9 | PMCID: PMC11168934 | PMID: 38778109
- Evidence: Gene expression against the mRatBN7.2 transcriptome (Ensembl release 104) 37 was quantified with STAR 38 and featureCounts 39 .
- Full pipeline: quality control [Cutadapt, FastQC] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ v2.1.0]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: Gene counts were generated using featureCounts 62 v.2.0.1 and TPM values for protein-coding genes were calculated as previously described 63 .
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Evidence: The data were quantified using the featureCounts module of Subread v.2.0.1 (ref.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **2.0.1**
- Evidence: Counts were generated using featureCounts (v.2.0.1) 87 (featureCounts -p -t transcript -g transcript_id -O --minOverlap 10) and RPKM was calculated using the calculation reads for a gene/(all reads for the sample/1,000,000) × (1,000/length of gene).
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Transient loss of Polycomb components induces an epigenetic cancer fate. (Nature 2024)

- DOI: 10.1038/s41586-024-07328-w | PMCID: PMC11096130 | PMID: 38658752
- Evidence: Next, aligned reads were counted for each D. melanogaster transcript (dmel_r6.36 annotation) using the featureCounts function from the Rsubread R package (v.2.0.1, isPairedEnd = TRUE) and differential expression analysis was performed using the DESeq2 R package 69 (v.1.26.0, design = ~replicate + condition).
- Full pipeline: quality control [fastp] -> alignment/mapping [DESeq2, SAMtools, featureCounts] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [GATK, Mutect2, R, data.table v1.14.2]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **1.5.0**
- Evidence: To quantify gene expression levels, featureCounts (v.1.5.0-p3) was used to count the reads mapped to each gene, followed by the calculation of fragments per kilobase of transcript sequence per million mapped reads based on gene length and read count.
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: Finally, featureCounts from the Rsubread software package 2.10.5 was used to quantify the raw reads with genes defined from the respective Ensembl releases 50 .
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### A brain-specific angiogenic mechanism enabled by tip cell specialization. (Nature 2024)

- DOI: 10.1038/s41586-024-07283-6 | PMCID: PMC11041701 | PMID: 38570687
- Evidence: The generated BAM files containing the alignment results were sorted according to the mapping position, and raw read counts for each gene were calculated using the FeatureCounts function from the Subread package v.1.4.6-p5.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore v0.4.4] -> alignment/mapping [Bowtie2, SAMtools v1.16.1, TopHat v2.1.1, Trim Galore v0.4.4, featureCounts] -> quantification [featureCounts] -> stage not stated [DESeq2 v1.12, ImageJ v1.53c, Seurat]

### CGRP sensory neurons promote tissue healing via neutrophils and macrophages. (Nature 2024)

- DOI: 10.1038/s41586-024-07237-y | PMCID: PMC11023938 | PMID: 38538784
- Evidence: Reads were quantified using featureCounts producing the raw genes count matrix and various quality control metrics which were summarized in a multiQC report 64 , 65 .
- Full pipeline: quality control [featureCounts] -> alignment/mapping [STAR] -> quantification [featureCounts] -> differential/statistical testing [limma]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Version used: **1.6.3**
- Evidence: Expression quantification was performed using featureCounts (v.1.6.3) 67 against the gtf matching the reference Homo sapiens genome.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### Anoxygenic phototroph of the Chloroflexota uses a type I reaction centre. (Nature 2024)

- DOI: 10.1038/s41586-024-07180-y | PMCID: PMC10972752 | PMID: 38480893
- Evidence: Following read mapping to MAGs, the counts of metatranscriptome read hits to genes within MAGs were summarized using featureCounts 107 , in v1.6.4 of the Subread package.
- Full pipeline: read trimming [DADA2 v1.10.0] -> alignment/mapping [Clustal Omega v1.2.3, featureCounts] -> stage not stated [HMMER v3.1b, IQ-TREE v1.6.9, QIIME 2 v2019.10]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Evidence: 22 G reads were quantified using featureCounts (Rsubread, R), normalized by the total number of 22 G per replicate, and visualized using the Gviz R package 62 .
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Evidence: Gene counts were quantified using the featureCounts function from the Subread package v.2.0.1 (ref.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### Targeted protein degradation via intramolecular bivalent glues. (Nature 2024)

- DOI: 10.1038/s41586-024-07089-6 | PMCID: PMC10917667 | PMID: 38383787
- Version used: **2.0.1**
- Evidence: In brief, sequencing reads were trimmed using fastx-toolkit (v0.0.14), aligned using Bowtie2 (v2.4.5) and quantified using featureCounts (v2.0.1).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> visualisation [ChimeraX, PyMOL] -> stage not stated [ColabFold, Coot v0.9.8.1, Nextflow, PHENIX v1.20.1]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Version used: **2.0.1**
- Evidence: A count matrix, using all alignments from all profiles against merged peaks, was then created with featureCounts v.2.0.1: featureCounts -F SAF -Q 10 --primary -s 1 -T 12 -a {merged_peaks} -o {merged_peaks.counts.txt} {all_bam_files}.
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### Bile salt hydrolase catalyses formation of amine-conjugated bile acids. (Nature 2024)

- DOI: 10.1038/s41586-023-06990-w | PMCID: PMC10881385 | PMID: 38326609
- Version used: **2.0.1**
- Evidence: 34 ) was used to check for the quality of alignments. featureCounts (v.2.0.1) (ref.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Trimmomatic, fastp v0.12.4] -> alignment/mapping [Bowtie2 v2.2.5, SAMtools v1.10, featureCounts v2.0.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [Prokka]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: A global peak atlas was created by first removing blacklisted regions ( https://www.encodeproject.org/annotations/ENCSR636HFF ) then merging all peaks within 500 bp and counting reads with version 1.6.1 of featureCounts ( http://subread.sourceforge.net ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Evidence: Genomic matches were counted using featureCounts with parameters -F “GTF” -t “exon” -g “gene_id” --minOverlap 20 -M --primary -O --fraction -J -Q 30 -T 4.
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: Read counts for each gene were calculated using featureCounts from the Subread package.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Evidence: Quantification was performed with featureCounts from subread (v.2.0.6) 103 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **2.0.0**
- Evidence: Reads were counted using featureCounts (v.2.0.0) (ref.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Evidence: Reads were aligned to the reference genome (GRCh38) using Rsubread, and gene expression was quantified with featureCounts.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: Sequencing data were aligned using HISAT2 in human reference genome (GRCh38), with reads counting performed by featureCounts.
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Reads were adapter-trimmed (Trim Galore, Nextera-specific settings, minimum overlap 3 bases), aligned to the human reference genome (GRCh38.p14, GENCODE release 47; STAR aligner), and counted (featureCounts, paired-end settings).
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Version used: **2.0.3**
- Evidence: Expression levels of gene features, that is, coding DNA sequences regions from the reference assembly, were quantitated using FeatureCounts (v2.0.3) as raw read counts of the stranded libraries 79 .Differential analysis of quantitated gene features compared with treatment was performed using the software package edgeR on raw sequence counts 80 .
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Microbial iron oxide respiration coupled to sulfide oxidation. (Nature 2025)

- DOI: 10.1038/s41586-025-09467-0 | PMCID: PMC12545173 | PMID: 40866705
- Evidence: FeatureCounts (part of SubRead 2.0.6 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.407, RAxML v8.2.12] -> structure determination [RAxML v8.2.12] -> visualisation [R v4.1] -> stage not stated [AlphaFold v2.3.2, AutoDock Vina v1.1.2, DESeq2 v3.19, HMMER, ImageJ, featureCounts]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: To generate a global peak atlas, blacklisted regions were removed before merging all peaks within a 500-bp region and quantifying reads using featureCounts.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Version used: **2.4**
- Evidence: 63 ) and the mapped reads were assigned with FeatureCounts (v2.4) 64 based on the genome-build GRCm38.p4 annotation and NCBI Refseq gene mode by removing ribosomal genes and non-coding RNA, respectively.
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Evidence: Paired reads were counted for each gene using featureCounts from Subread (v.2.0.1).
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Evidence: FeatureCounts (subread 1.6.3) was applied to count reads mapped to each gene.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Expanding the cytokine receptor alphabet reprograms T cells into diverse states. (Nature 2025)

- DOI: 10.1038/s41586-025-09393-1 | PMCID: PMC12460165 | PMID: 40804519
- Evidence: Gene expression was quantified with featureCounts.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC, MACS2 v3.0.1] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [R v4.4, SCENIC v0.12.1]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Version used: **2.0.1**
- Evidence: Read counts were obtained using featureCounts v.2.0.1.
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### A gut sense for a microbial pattern regulates feeding. (Nature 2025)

- DOI: 10.1038/s41586-025-09301-7 | PMCID: PMC12443592 | PMID: 40702192
- Evidence: STAR was used with the mm10 mouse reference genome to align reads, and count tables were generated using featureCounts.
- Full pipeline: alignment/mapping [featureCounts] -> stage not stated [BigStitcher, DESeq2, ImageJ]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Version used: **1.6.4**
- Evidence: 1b ) using featureCounts (v.1.6.4) 70 (Subread package). rRNA cleavage sites were annotated based on the positions described previously 14 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: The trimmed reads were then aligned to the GRCm38.91 (mm10) reference genome using STAR 56 , and the transcript count was quantified using featureCounts 57 to generate a raw count matrix.
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Evidence: The number of reads for each RIFIN gene was tallied using featureCounts 41 and normalized by dividing it by the total number of mapped reads.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Version used: **1.6.1.0**
- Evidence: Transcriptomes were analysed on the Galaxy platform 59 using Trim Galore! version 0.4.3.1 (developed by Felix Krueger at the Babraham Institute), HISAT2 version 2.1.0 60 and featureCounts version 1.6.1.0 61 . snRNA-seq of thymic tissue The Chromium GEM-X Single Cell 3′ v4 protocol ( CG000731 , Rev B) was followed starting from step 1.1 according to the manufacturer’s guidelines.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **1.5.3**
- Evidence: Gene-level expression was quantified using featureCounts v.1.5.3, using Ensembl gene annotations (release v.113) for both alignment and quantification.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: For transcriptome-wide analysis of RNAs enriched by RIP-seq, aligned reads were assigned to annotated transcriptome features using featureCounts 47 (v2.0.2) with -s 1 for strandedness.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Molecular basis of positional memory in limb regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09036-5 | PMCID: PMC12176643 | PMID: 40399677
- Evidence: We used featureCounts 67 to generate a read counts table.
- Full pipeline: read trimming [HISAT2, Trimmomatic v0.39] -> alignment/mapping [HISAT2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, ggplot2 v3.3.6, pheatmap]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Reads overlapping annotated genes were quantified using the command featureCounts from the R package Rsubread 75 , excluding multi-mapping reads.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Taurine from tumour niche drives glycolysis to promote leukaemogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09018-7 | PMCID: PMC12328231 | PMID: 40369079
- Evidence: The mouse bulk RNA-seq samples were processed otherwise identical to the human bulk RNA-seq with two exceptions: m38 + gencode M27 reference ( https://www.gencodegenes.org/mouse/release_M27.html ) for use within alignment and counting, and ‘-s 0’ being used within subread featureCounts.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> differential/statistical testing [DESeq2 v1.28.1, Enrichr] -> stage not stated [Seurat v4.1.0, tidyverse v1.2.0]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Gene expression counts were computed by means of the FeatureCounts option from the Subread toolkit 55 using gencode v.38 reference.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Evidence: Read counts were mapped to genes using featureCounts.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: Read counts were assigned to genes using featureCounts from the Subread package (v.2.0.1) with options -Q 10 -p -B -C -s 2 -g gene_id -t exon and the respective annotation file (Gencode v.M25).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **1.5.0**
- Evidence: The gene count matrix was generated with FeatureCounts version 1.5.0-p2 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Plasticity of the mammalian integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-08794-6 | PMCID: PMC12119373 | PMID: 40140574
- Evidence: 24 were obtained from the National Center for Biotechnology Information Gene Expression Omnibus repository ( GSE128092 ) and prepared the same way as described above, with a difference that the aligned reads were summarized using the featureCounts function of the RSubread (v2.6.4) R/Bioconductor package 54 .
- Full pipeline: quality control [FastQC v0.11.4] -> read trimming [R] -> alignment/mapping [Bioconductor, HTSeq, featureCounts] -> quantification [ImageJ] -> normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [ImageJ] -> stage not stated [DESeq2]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Evidence: Counts for each gene were calculated with Subread (v.2.0.1) ‘featureCounts’ function 62 , filtering low confidence mapping reads (‘-Q 10’).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Evidence: Barcode sequencing analysis Barcodes from genomic DNA sequencing were quantified using BWA (v0.7.18) and FeatureCounts from Rsubread package (v2.18.0).
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Evidence: Then, the reads with barcode and UMI information were assigned to the transcriptome using featureCounts of package Subread 1.6.4.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Evidence: Expression levels were determined by FeatureCounts from the Subread package (v.2.0.1) 63 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Version used: **2.12.2**
- Evidence: RSubread/FeatureCounts (v.2.12.2) was used to calculate read counts, while differential expression analysis was performed using DESeq2 72 , 73 , with adjusted P < 0.05 used as the significance cut-off.
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### Synthetic lethality of mRNA quality control complexes in cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08398-6 | PMCID: PMC11864970 | PMID: 39910291
- Evidence: Counts were calculated using featureCounts from subread package and subsequently adjusted with TMM normalization and limma-voom transformation.
- Full pipeline: normalisation [featureCounts, limma] -> visualisation [PyMOL v1.7.6.6] -> stage not stated [fgsea]

### C-terminal amides mark proteins for degradation via SCF-FBXO31. (Nature 2025)

- DOI: 10.1038/s41586-024-08475-w | PMCID: PMC11821526 | PMID: 39880951
- Evidence: Reads were aligned with STAR-aligner 76 (v.2.7.10a) and counting was performed using FeatureCounts 77 (v.2.0.6) against a custom transcriptome reference.
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [limma v3.58.1] -> differential/statistical testing [DESeq2, limma v3.58.1] -> visualisation [ChimeraX]

### The maternal X chromosome affects cognition and brain ageing in female mice. (Nature 2025)

- DOI: 10.1038/s41586-024-08457-y | PMCID: PMC11798838 | PMID: 39843739
- Evidence: Unique gene hit counts from exons were calculated using featureCounts in the Subread package v.1.5.2.
- Full pipeline: quality control [FastQC] -> read trimming [STAR] -> alignment/mapping [Bismark, STAR] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, featureCounts]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Version used: **1.6.0**
- Evidence: The trimmed and quality-filtered reads were mapped to the Arabidopsis genome (TAIR10) using STAR (v.2.6.1b) 47 with default parameters and transformed to a count per gene per library using featureCounts (v.1.6.0) 48 .
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: FeatureCounts was then used to estimate gene abundance, with KEGG annotations from gene annotations generated using Mantis 63 , mapping to 17,536 KOs.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Gene expression analysis Gene expression quantification was performed using the featureCounts function of the R subRead package 85 , using a gtf file containing the UCSC genes for mm9 with paired or single-end settings depending on the samples.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: UMI counting and deduplication was performed with umi_tools 55 (v1.0.1) and gene counts were generated from the deduplicated reads using featureCounts (subread v2.0.1) using Gencode v41 basic transcriptome annotation.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Evidence: Reads were aligned to the genome using star v.2.6.0c and reads in genes were counted with featureCounts (subread v.1.6.2) using strand-specific read counting for QuantSeq experiments (-s 1).
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **2.0.8**
- Evidence: The mapped reads were assembled with FeatureCounts (v.2.0.8) 59 , and differential gene expression was analysed using DESeq2 (v.2.11.40.8) 60 based on read counts.
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **2.0.6**
- Evidence: Data preprocessing Processing of generated bulk RNA-seq data Reads from both bulk RNA-seq datasets (ITP and Klotho -KO) were mapped to the mouse genome (GRCm39) with STAR (v2.7.11b) 192 and counted via featureCounts (v2.0.6) 193 .
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **2.0.0**
- Evidence: The featureCounts v.2.0.0 52 was used to generate counts of reads aligned to annotated genes in the Ensembl GRCm38.99 with options ‘-p -O–fraction’.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Evidence: Following alignment, gene-level read counts were quantified from the aligned BAM files using the featureCounts function from the Rsubread package.
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### H&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;2&lt;/sub&gt; repurposes plant O&lt;sub&gt;2&lt;/sub&gt; sensing to regulate post-hypoxia responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10366-1 | PMCID: PMC13216066 | PMID: 42020755
- Evidence: After a quality check using FastQC, we aligned the reads on the A. thaliana full genome (TAIR 10) using Rsubread 74 (v.2.16.1) and counted them using featureCounts 75 (in the Rsubread package).
- Full pipeline: quality control [FastQC, featureCounts] -> alignment/mapping [FastQC, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR] -> stage not stated [ImageJ, R v4.3.1]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **2.0.6**
- Evidence: On the basis of read counts from featureCounts (v2.0.6) 79 , gene expression levels was normalized to transcripts per million (TPM).
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **2.0.1**
- Evidence: PCR duplicates were removed with Picard (v.2.27.4), and gene counts were generated using featureCounts (v.2.0.1).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Version used: **2.0.1**
- Evidence: Within each chunk of an RNA sublibrary, we performed barcode matching, 10 bp UMI parsing from Read2, and adapter trimming for Read1 only, followed by genome alignment with STAR (v2.5.4b) 95 , gene annotation with featureCounts (v2.0.1) 96 , and conversion of the output BAM file to a more storage-efficient TSV format.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Evidence: FeatureCounts was used to obtain a gene expression matrix, using the parameters ‘--fraction -t gene’ on the GENCODE annotation (vM25).
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **1.6.3**
- Evidence: FeatureCounts (v.1.6.3; RRID SCR_012919 ) was used for quantification of gene expression levels, followed by DEseq2 (RRID SCR_000154 ) for differential gene expression analysis.
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Version used: **2.0.1**
- Evidence: Read counts mapped on these regions were quantified using featureCounts (v2.0.1) 59 and a normalized Bigwig file was generated using bamCoverage (deepTools v3.5.3) 57 .
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### Facile induction of immune tolerance by an interleukin-2-TGFβ surrogate agonist. (Nature 2026)

- DOI: 10.1038/s41586-026-10208-0 | PMCID: PMC13190267 | PMID: 41813890
- Evidence: To identify differentially expressed genes from public bulk RNA-seq datasets for computing gene set signature scores, bulk RNA-seq FASTQ files were aligned to the GENCODE VM25 (mm10) reference genome using Rsubread 49 , and gene expression was quantified with featureCounts 50 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, featureCounts, fgsea] -> stage not stated [Metascape, SCENIC]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: The summarized data were then assessed by statistical models (one-way ANOVA with Tukey’s HSD and the Benjamini–Hochberg for multiple gene correction) or STAR, featureCounts and DESeq2.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Version used: **2.0.6**
- Evidence: HISAT2 (v.2.2.1) was used to build the index of the reference genome, and HISAT2 was used to align paired-end clean reads to the reference genome. featureCounts (v.2.0.6) was used to count the reads numbers mapped to each gene.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Consensus peaks set across all Flag antibody samples were created using BEDTools; featureCounts 84 was used to count consensus peaks in each sample; and HOMER was used to annotate peaks relative to gene features and perform motif enrichment analysis.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Albumin orchestrates a natural host defence mechanism against mucormycosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09882-3 | PMCID: PMC12804082 | PMID: 41501454
- Evidence: The reads that mapped to genomic features were calculated using the featureCounts program (v.2.0.3) 69 .
- Full pipeline: alignment/mapping [STAR, featureCounts] -> differential/statistical testing [R v4.3.1] -> visualisation [R v4.3.1] -> stage not stated [Fiji, GSEA, ImageJ, pheatmap]

### A direct role for a mitochondrial targeting sequence in signalling stress. (Nature 2026)

- DOI: 10.1038/s41586-025-09834-x | PMCID: PMC7618714 | PMID: 41372412
- Evidence: Gene-level read counts were quantified using the featureCounts function from the Rsubread package (version 2.23.2) in R (version 4.4.1).
- Full pipeline: quantification [R v4.4.1, featureCounts] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [AlphaFold, BLAST v2.14.0, ImageJ]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **2.0.1**
- Evidence: The resulting reads were trimmed using fastx-toolkit (v.0.0.14) and subsequently aligned (Bowtie2, v.2.4.5) and quantified (featureCounts, v.2.0.1).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **1.6.1**
- Evidence: The mapped reads count of each gene was measured by featureCounts (v.1.6.1).
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **1.6.4**
- Evidence: Sequences were aligned to mouse genome build GRCm38.98 (mm10) using Hisat2 (v2.1.0), and per gene counts were determined using FeatureCounts (v1.6.4).
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Version used: **1.6.4**
- Evidence: The trimmed sequences were aligned to the mouse genome build GRCm38.98 using HISAT2 (v2.1.0), with raw counts per gene subsequently determined using FeatureCounts (v1.6.4).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Raw gene expression counts were summarized with featureCounts 84 using a custom hg38 and plasmid GTF file containing joint annotations.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### SARS-CoV-2 expresses a microRNA-like small RNA able to selectively repress host genes. (PNAS 2021)

- DOI: 10.1073/pnas.2116668118 | PMCID: PMC8719879 | PMID: 34903581
- Evidence: The reads were mapped with bowtie2 ( 66 ) (–very-sensitive-local) to an index containing human and SARS-CoV-2 genomes. miRNAs were counted by using featureCounts ( 67 ) and annotations obtained from miRBase ( 68 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, featureCounts] -> differential/statistical testing [edgeR] -> visualisation [BEDTools]

### Single-cell quantification of a broad RNA spectrum reveals unique noncoding patterns associated with cell types and states. (PNAS 2021)

- DOI: 10.1073/pnas.2113568118 | PMCID: PMC8713755 | PMID: 34911763
- Version used: **1.6.1**
- Evidence: Reads mapping to multiple locations were assigned either to a location with the best mapping score or, in the case of equal multimapping score, to the genomic location randomly chosen as “primary.” Transcripts were counted using featureCounts v1.6.1 ( 51 ) with the following parameters: -M –primary -s 1.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [featureCounts v1.6.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [R, UMAP]

### Hippocampal neurons' cytosolic and membrane-bound ribosomal transcript profiles are differentially regulated by learning and subsequent sleep. (PNAS 2021)

- DOI: 10.1073/pnas.2108534118 | PMCID: PMC8640746 | PMID: 34819370
- Evidence: Reads mapped to unique transcripts were counted with featureCounts ( 86 ).
- Full pipeline: alignment/mapping [featureCounts] -> visualisation [R]

### Monoclonal antibody-mediated neutralization of SARS-CoV-2 in an IRF9-deficient child. (PNAS 2021)

- DOI: 10.1073/pnas.2114390118 | PMCID: PMC8609338 | PMID: 34702736
- Version used: **2.0.2**
- Evidence: The sequencing reads were mapped onto the human reference genome GRCh38 with STAR aligner v2.7, and the mapped reads were then quantified to determine the gene-level read counts, with featureCounts v2.0.2.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.2] -> quantification [DESeq2, STAR, featureCounts v2.0.2] -> normalisation [DESeq2]

### Coordinated bacterial and plant sulfur metabolism in <i>Enterobacter</i> sp. SA187-induced plant salt stress tolerance. (PNAS 2021)

- DOI: 10.1073/pnas.2107417118 | PMCID: PMC8609655 | PMID: 34772809
- Version used: **1.6.5**
- Evidence: Aligned reads were then used to calculate the number of reads per gene using FeatureCounts version 1.6.5 ( 57 ), and FPKM was calculated using Cufflinks version 2.2.1 ( 58 ).
- Full pipeline: quality control [R] -> read trimming [Trimmomatic] -> alignment/mapping [TopHat v2.0.9, featureCounts v1.6.5] -> quantification [Cufflinks v2.2.0, featureCounts v1.6.5] -> differential/statistical testing [Cufflinks v2.2.0] -> stage not stated [ImageJ]

### The translatome of neuronal cell bodies, dendrites, and axons. (PNAS 2021)

- DOI: 10.1073/pnas.2113929118 | PMCID: PMC8639352 | PMID: 34670838
- Version used: **2.0.0**
- Evidence: For both total RNA sequencing and ribosome footprint libraries from the somata and neuropil, the software featureCounts version 2.0.0 ( 69 ) was used to calculate counts per gene from reads that were aligned to the rat genome.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt] -> alignment/mapping [Bowtie2 v2.3.5.1, STAR v2.7.3, featureCounts v2.0.0] -> stage not stated [DESeq2 v1.30.1, Python]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Evidence: FeatureCounts was used to quantify gene-level transcript abundances, which were subsequently converted to transcripts per million ( 78 ).
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### Fever supports CD8<sup>+</sup> effector T cell responses by promoting mitochondrial translation. (PNAS 2021)

- DOI: 10.1073/pnas.2023752118 | PMCID: PMC8237659 | PMID: 34161266
- Evidence: Sequenced libraries were processed with the Galaxy platform and deepTools for quality control ( 37 ), Spliced Transcripts Alignment to a Reference (STAR) ( 38 ) for trimming and mapping, and featureCounts ( 39 ) to quantify mapped reads.
- Full pipeline: quality control [Galaxy, deepTools, featureCounts] -> read trimming [Galaxy, deepTools, featureCounts] -> alignment/mapping [DESeq2, Galaxy, R, deepTools, featureCounts] -> quantification [DESeq2, Galaxy, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [ImageJ, Metascape]

### Molecular design of the γδT cell receptor ectodomain encodes biologically fit ligand recognition in the absence of mechanosensing. (PNAS 2021)

- DOI: 10.1073/pnas.2023050118 | PMCID: PMC8256041 | PMID: 34172580
- Version used: **1.4.4**
- Evidence: The read counts were quantified at the exon level using subRead featureCounts (v1.4.4) software ( 87 ) and differential expression testing was performed using DESeq2 (v1.6.3) software ( 88 ).
- Full pipeline: alignment/mapping [SAMtools, STAR] -> quantification [DESeq2 v1.6.3, featureCounts v1.4.4] -> differential/statistical testing [DESeq2 v1.6.3, featureCounts v1.4.4]

### HIF-1α is a negative regulator of interferon regulatory factors: Implications for interferon production by hypoxic monocytes. (PNAS 2021)

- DOI: 10.1073/pnas.2106017118 | PMCID: PMC8256008 | PMID: 34108245
- Version used: **1.5.2**
- Evidence: Gene-level raw counts were calculated using featureCounts (v1.5.2) and normalized by the Trimmed means of M-values normalization method implemented in the edgeR package ( 64 ).
- Full pipeline: quality control [HISAT2 v2.0.5] -> read trimming [edgeR, featureCounts v1.5.2] -> alignment/mapping [HISAT2 v2.0.5] -> normalisation [edgeR, featureCounts v1.5.2]

### Small noncoding RNA profiling across cellular and biofluid compartments and their implications for multiple sclerosis immunopathology. (PNAS 2021)

- DOI: 10.1073/pnas.2011574118 | PMCID: PMC8092379 | PMID: 33879606
- Evidence: CSF cells total RNA libraries ( n = 17) were preprocessed with TrimGalore, mapped with STAR against hg38, and annotated using featureCounts with Ensemble GRCh38.
- Full pipeline: alignment/mapping [Trim Galore, featureCounts] -> differential/statistical testing [DESeq2, limma] -> stage not stated [BEDTools]

### Single-cell atlas of developing murine adrenal gland reveals relation of Schwann cell precursor signature to neuroblastoma phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2022350118 | PMCID: PMC7865168 | PMID: 33500353
- Version used: **1.5.2**
- Evidence: Read assignment was with featureCounts, version 1.5.2, using a gene annotation based on GENCODE, version M14.
- Full pipeline: normalisation [R, Seurat, limma] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [featureCounts v1.5.2]

### Consequences of aneuploidy in human fibroblasts with trisomy 21. (PNAS 2021)

- DOI: 10.1073/pnas.2014723118 | PMCID: PMC8017964 | PMID: 33526671
- Evidence: Aligned exon fragments with mapping quality higher than 20 were counted toward gene expression with featureCounts_1.5.2 3.
- Full pipeline: alignment/mapping [featureCounts]

### A genome-scale CRISPR screen reveals factors regulating Wnt-dependent renewal of mouse gastric epithelial cells. (PNAS 2021)

- DOI: 10.1073/pnas.2016806118 | PMCID: PMC7848749 | PMID: 33479180
- Version used: **1.6.1**
- Evidence: Reads on annotated genes were counted using featureCounts (v1.6.1).
- Full pipeline: read trimming [Cutadapt v1.16, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.2b] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [featureCounts v1.6.1]

### The harsh microenvironment in early breast cancer selects for a Warburg phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2011342118 | PMCID: PMC7826394 | PMID: 33452133
- Evidence: Finally, we quantified the number of uniquely aligned reads associated with each gene in each sample using the featureCounts ( 47 ).
- Full pipeline: read trimming [R] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Cutadapt, Enrichr]

### Precise spatial structure impacts antimicrobial susceptibility of <i>S. aureus</i> in polymicrobial wound infections. (PNAS 2022)

- DOI: 10.1073/pnas.2212340119 | PMCID: PMC9907066 | PMID: 36520668
- Version used: **2.0.1**
- Evidence: Reads were mapped to P. aeruginosa strain PA14 (accession number GCF_000014625.1) downloaded from the National Center for Biotechnology Information (NCBI) using Bowtie2 version 2.3.5 ( 65 ) and tallied with featureCounts version 2.0.1.
- Full pipeline: read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0]

### Temporal changes in plasma membrane lipid content induce endocytosis to regulate developmental epithelial-to-mesenchymal transition. (PNAS 2022)

- DOI: 10.1073/pnas.2212879119 | PMCID: PMC9907157 | PMID: 36508654
- Evidence: Transcripts were then counted using featureCounts ( 83 ), and differential expression analysis between premigratory and migratory gene expression was carried out using DESeq2 ( 84 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, featureCounts]

### Quality assessment and refinement of chromatin accessibility data using a sequence-based predictive model. (PNAS 2022)

- DOI: 10.1073/pnas.2212810119 | PMCID: PMC9907136 | PMID: 36508674
- Evidence: We used featureCounts ( 48 ) to calculate the fraction of reads in called peaks (FRiP), known promoters, and enhancers.
- Full pipeline: quality control [Jupyter] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [LDSC, MACS2, featureCounts]

### A bacterium from a mountain lake harvests light using both proton-pumping xanthorhodopsins and bacteriochlorophyll-based photosystems. (PNAS 2022)

- DOI: 10.1073/pnas.2211018119 | PMCID: PMC9897461 | PMID: 36469764
- Evidence: FeatureCounts was used to assess the number of reads per gene.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [featureCounts]

### Inflammatory response to retrotransposons drives tumor drug resistance that can be prevented by reverse transcriptase inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2213146119 | PMCID: PMC9894111 | PMID: 36449545
- Evidence: Reads were counted using featureCounts ( 51 ) using the same annotation.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [featureCounts]

### EBF1 is continuously required for stabilizing local chromatin accessibility in pro-B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2210595119 | PMCID: PMC9860308 | PMID: 36409886
- Evidence: The expression level of the annotated genes (GRCm38.p4) was calculated by featureCounts (subread v2.0.0) ( 49 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA, featureCounts]

### ADAR regulates APOL1 via A-to-I RNA editing by inhibition of MDA5 activation in a paradoxical biological circuit. (PNAS 2022)

- DOI: 10.1073/pnas.2210150119 | PMCID: PMC9636950 | PMID: 36282916
- Version used: **2.0.0**
- Evidence: Gene counts were obtained from the nontruncated bam files using featureCounts version 2.0.0 of the Subread package and normalized using the DESeq2 package in R version 4.1.2.
- Full pipeline: quality control [STAR] -> read trimming [STAR] -> alignment/mapping [SAMtools v1.13, STAR] -> quantification [DESeq2, HTSeq] -> normalisation [R v4.1.2, featureCounts v2.0.0] -> stage not stated [Matplotlib, SciPy]

### <i>Arabidopsis</i> AAR2, a conserved splicing factor in eukaryotes, acts in microRNA biogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2208415119 | PMCID: PMC9565372 | PMID: 36191209
- Version used: **1.64**
- Evidence: Mapped reads were counted using featureCounts v1.64 ( 69 ), and differentially expressed genes were analyzed using the R package DESeq2.
- Full pipeline: alignment/mapping [featureCounts v1.64] -> differential/statistical testing [DESeq2, R, featureCounts v1.64]

### DNA polymerase epsilon interacts with SUVH2/9 to repress the expression of genes associated with meiotic DSB hotspot in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208441119 | PMCID: PMC9564942 | PMID: 36191225
- Version used: **2.0.0**
- Evidence: ...and TEs (fold change ≥2 and P < 0.01) were identified by the R package DESeq2 version 1.30.1 ( 69 ) based on the gene expression matrix quantified by featureCounts version 2.0.0 ( 70 ).
- Full pipeline: read trimming [Bismark v0.22.3, Cutadapt, STAR v2.7.9a] -> alignment/mapping [Bismark v0.22.3, Bowtie2, Cutadapt, STAR v2.7.9a] -> quantification [Bismark v0.22.3, Cutadapt, DESeq2 v1.30.1, R, STAR v2.7.9a, featureCounts v2.0.0] -> stage not stated [ImageJ v1.52]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Evidence: Then, according to the mapped reads, the read counts and TPMs (transcripts per million) were used to indicate expression level using featureCounts software ( 90 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### Reduced Satb1 expression predisposes CD4<sup>+</sup> T conventional cells to Treg suppression and promotes transplant survival. (PNAS 2022)

- DOI: 10.1073/pnas.2205062119 | PMCID: PMC9546564 | PMID: 36161903
- Evidence: Aligned sequences were quantified (featureCounts) ( 55 ) followed by normalization with the trimmed mean of m-values method ( 56 – 59 ).
- Full pipeline: read trimming [featureCounts] -> alignment/mapping [STAR v2.5.3a, featureCounts] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [R v3.4.1] -> differential/statistical testing [edgeR]

### Biosensors for inflammation as a strategy to engineer regulatory T cells for cell therapy. (PNAS 2022)

- DOI: 10.1073/pnas.2208436119 | PMCID: PMC9546553 | PMID: 36161919
- Evidence: Mapping was performed using STAR, and gene counts are based on featureCounts.
- Full pipeline: quality control [DESeq2] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [fgsea, ggplot2]

### Mafba and Mafbb regulate microglial colonization of zebrafish brain via controlling chemotaxis receptor expression. (PNAS 2022)

- DOI: 10.1073/pnas.2203273119 | PMCID: PMC9522419 | PMID: 36122226
- Evidence: Read counts per gene were calculated by FeatureCounts (Rsubread_2.6.1).
- Full pipeline: alignment/mapping [STAR] -> quantification [featureCounts] -> stage not stated [ImageJ]

### Truncated Tau caused by intron retention is enriched in Alzheimer's disease cortex and exhibits altered biochemical properties. (PNAS 2022)

- DOI: 10.1073/pnas.2204179119 | PMCID: PMC9477417 | PMID: 36067305
- Version used: **2.0.1**
- Evidence: Counts for Tau gene were generated using featureCounts (v.2.0.1.) and differential expression was calculated by DESeq2 (v.1.30.1).
- Full pipeline: normalisation [ggplot2, tidyverse] -> differential/statistical testing [DESeq2, featureCounts v2.0.1]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Reads were aligned to the hg38 genome in STAR ( 41 ) v2.6.1 and quantified with featureCounts ( 42 ) v1.6.3.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### Adrenergic receptor signaling induced by Klf15, a regulator of regeneration enhancer, promotes kidney reconstruction. (PNAS 2022)

- DOI: 10.1073/pnas.2204338119 | PMCID: PMC9388080 | PMID: 35939709
- Version used: **2.0.1**
- Evidence: Peaks in independent samples were merged and fragments per peak in each sample were counted using featureCounts (2.0.1) and edgeR (3.32.1) software packages to detect differential ATAC-seq peaks (RRID: SCR_012919) (RRID:SCR_012802) ( 19 , 39 ).
- Full pipeline: differential/statistical testing [MACS2 v2.2.6, edgeR v3.32.1, featureCounts v2.0.1] -> stage not stated [BEDTools v2.30.0, HOMER]

### Seed DNA damage responses promote germination and growth in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2202172119 | PMCID: PMC9335332 | PMID: 35858436
- Evidence: The read counts for genes in the GTF file were generated with featureCounts() function of Rsubread package ( 49 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [SAMtools] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Voltage-gated sodium channel &lt;i&gt;scn8a&lt;/i&gt; is required for innervation and regeneration of amputated adult zebrafish fins. (PNAS 2022)

- DOI: 10.1073/pnas.2200342119 | PMCID: PMC9282381 | PMID: 35867745
- Evidence: Differentially regulated transcripts were identified using featureCounts and DESeq2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [ImageJ]

### Transcriptome profiling of kisspeptin neurons from the mouse arcuate nucleus reveals new mechanisms in estrogenic control of fertility. (PNAS 2022)

- DOI: 10.1073/pnas.2113749119 | PMCID: PMC9271166 | PMID: 35763574
- Evidence: Gene level quantification of read counts was performed by featureCounts, and 89.1% of mapped reads were assigned to genes.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts]

### APOBEC3A regulates transcription from interferon-stimulated response elements. (PNAS 2022)

- DOI: 10.1073/pnas.2011665119 | PMCID: PMC9171812 | PMID: 35549556
- Evidence: Gene expression was quantified with featureCounts ( 54 ) according to the hg38 RefSeq gene annotations ( 55 , 56 ) obtained from the University of California, Santa Cruz genome Browser ( 57 ).
- Full pipeline: read trimming [fastp] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, Bioconductor, R v4.0]

### Enzymes degraded under high light maintain proteostasis by transcriptional regulation in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121362119 | PMCID: PMC9171785 | PMID: 35549553
- Evidence: Aligned reads were summarized to gene-level loci using the Araport11 annotation ( 76 ) using featureCounts (-s 2 for reverse stranded libraries) ( 77 ).
- Full pipeline: quality control [FastQC v0.11.7] -> alignment/mapping [SAMtools v1.3.1, featureCounts] -> differential/statistical testing [edgeR] -> stage not stated [Trim Galore]

### An approach for evaluating the effects of dietary fiber polysaccharides on the human gut microbiome and plasma proteome. (PNAS 2022)

- DOI: 10.1073/pnas.2123411119 | PMCID: PMC9171781 | PMID: 35533274
- Evidence: Count data were generated from alignments (featureCounts; Subread v.
- Full pipeline: read trimming [Cutadapt, DADA2 v1.13.0] -> alignment/mapping [Picard, featureCounts] -> stage not stated [Bowtie2]

### Genomewide CRISPR knockout screen identified PLAC8 as an essential factor for SADS-CoVs infection. (PNAS 2022)

- DOI: 10.1073/pnas.2118126119 | PMCID: PMC9170153 | PMID: 35476513
- Evidence: Features were counted using featureCounts as part of Subread version 2.0.1 with the parameters -T 4 -s 2 -d 25 -p -P -B -M -O.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [STAR v2.7.7a] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [R v4.0.3] -> stage not stated [Cytoscape, SAMtools v1.12, featureCounts]

### Agonists of prostaglandin E<sub>2</sub> receptors as potential first in class treatment for nephronophthisis and related ciliopathies. (PNAS 2022)

- DOI: 10.1073/pnas.2115960119 | PMCID: PMC9170064 | PMID: 35482924
- Evidence: FASTQ files were mapped to the ENSEMBL [Human(GRCh38/hg38)/Mouse GRCm38/mm10] reference using Hisat2 and counted by featureCounts from the Subread R package ( http://www.r-project.org/ ).
- Full pipeline: alignment/mapping [R, featureCounts] -> quantification [ImageJ] -> stage not stated [Metascape, PHENIX]

### MicroRNA-29a attenuates CD8 T cell exhaustion and induces memory-like CD8 T cells during chronic infection. (PNAS 2022)

- DOI: 10.1073/pnas.2106083119 | PMCID: PMC9169946 | PMID: 35446623
- Version used: **1.5.0**
- Evidence: The mapped data were assigned genomic features with featureCounts, version1.5.0 ( 57 ).
- Full pipeline: quality control [FastQC v11.5] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [STAR v2.5.0, featureCounts v1.5.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, limma]

### &lt;i&gt;Wolbachia&lt;/i&gt; depletion blocks transmission of lymphatic filariasis by preventing chitinase-dependent parasite exsheathment. (PNAS 2022)

- DOI: 10.1073/pnas.2120003119 | PMCID: PMC9169722 | PMID: 35377795
- Version used: **1.5.0**
- Evidence: The aligned RNA sequence expression data were quantified using the program FeatureCounts (v1.5.0-p3) ( 62 ) and used as input into the program edgeR (v3.30.3) ( 63 ) for differential gene expression analysis.
- Full pipeline: alignment/mapping [edgeR v3.30.3, featureCounts v1.5.0] -> quantification [edgeR v3.30.3, featureCounts v1.5.0] -> differential/statistical testing [edgeR v3.30.3, featureCounts v1.5.0]

### Layered evolution of gene expression in "superfast" muscles for courtship. (PNAS 2022)

- DOI: 10.1073/pnas.2119671119 | PMCID: PMC9168950 | PMID: 35363565
- Version used: **2.0.1**
- Evidence: Read pairs were counted per gene using full gene coordinate boundaries using featureCounts (v2.0.1) ( 46 ).
- Full pipeline: alignment/mapping [BCFtools, BWA, RAxML, STAR v2.7.3a] -> differential/statistical testing [limma] -> stage not stated [featureCounts v2.0.1]

### Hemogenic and aortic endothelium arise from a common hemogenic angioblast precursor and are specified by the Etv2 dosage. (PNAS 2022)

- DOI: 10.1073/pnas.2119051119 | PMCID: PMC9060440 | PMID: 35333649
- Evidence: Aligned reads were converted to counts for each gene using featureCounts (Rsubread_2.6.1).
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, R v4.0.2, Seurat]

### Prevention of the foreign body response to implantable medical devices by inflammasome inhibition. (PNAS 2022)

- DOI: 10.1073/pnas.2115857119 | PMCID: PMC8944905 | PMID: 35298334
- Version used: **1.5.0**
- Evidence: Additional QC was performed with featureCounts (v1.5.0-p2) ( 52 ) and Qualimap (v2.2) ( 53 ).
- Full pipeline: quality control [MultiQC v0.9, featureCounts v1.5.0] -> alignment/mapping [MultiQC v0.9, STAR] -> quantification [DESeq2, HTSeq, R v3.4] -> normalisation [DESeq2, R v3.4] -> dimensionality reduction/clustering [MultiQC v0.9] -> differential/statistical testing [DESeq2, R v3.4] -> stage not stated [ImageJ]

### Genomic adaptations for arboreal locomotion in Asian flying treefrogs. (PNAS 2022)

- DOI: 10.1073/pnas.2116342119 | PMCID: PMC9060438 | PMID: 35286217
- Evidence: Counts of each sample were calculated using featureCounts in the Rsubread package ( 60 ), and differential expression analysis used DESeq2 v1.30.0 ( 61 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> differential/statistical testing [DESeq2 v1.30.0, featureCounts] -> stage not stated [BUSCO]

### A multiomic study uncovers a bZIP23-PER1A-mediated detoxification pathway to enhance seed vigor in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2026355119 | PMCID: PMC8892333 | PMID: 35217598
- Evidence: The featureCounts was employed to summarize the reads.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [Cytoscape v3.6] -> stage not stated [R, featureCounts]

### Molecular parallelism in signaling function across different sexually selected ornaments in a warbler. (PNAS 2022)

- DOI: 10.1073/pnas.2120482119 | PMCID: PMC8872772 | PMID: 35165176
- Evidence: We used the BAM files from the HISAT2 alignment and the GTF file from MAKER to construct a gene count file [using the featureCounts command in the R package Rsubread ( 50 ); SI Appendix ].
- Full pipeline: alignment/mapping [R, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.1.0, HISAT2 v2.1.0, ImageJ, SAMtools v1.7]

### Genetic analysis of cancer drivers reveals cohesin and CTCF as suppressors of PD-L1. (PNAS 2022)

- DOI: 10.1073/pnas.2120540119 | PMCID: PMC8851563 | PMID: 35149558
- Evidence: Reads mapping to genes were quantified with featureCounts from the R package Subread (version 2.0.1).
- Full pipeline: alignment/mapping [R, STAR v2.4.2a, featureCounts] -> quantification [DESeq2, GSEA, R, featureCounts]

### Genomic and transcriptomic analyses of the subterranean termite <i>Reticulitermes speratus</i>: Gene duplication facilitates social evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2110361119 | PMCID: PMC8785959 | PMID: 35042774
- Evidence: Transcript abundances were estimated using featureCounts and normalized with the trimmed mean of M-values algorithm in edgeR.
- Full pipeline: read trimming [edgeR, featureCounts] -> alignment/mapping [TopHat v2.1.0] -> quantification [edgeR, featureCounts] -> normalisation [edgeR, featureCounts]

### Electrophysiological measures from human iPSC-derived neurons are associated with schizophrenia clinical status and predict individual cognitive performance. (PNAS 2022)

- DOI: 10.1073/pnas.2109395119 | PMCID: PMC8784142 | PMID: 35017298
- Version used: **1.5.0**
- Evidence: Genes and exons were quantified with featureCounts v1.5.0-p3 ( 54 ) to a custom concatenated hg38+rn6 gtf file within each sample.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> variant calling [SAMtools] -> quantification [featureCounts v1.5.0, kallisto] -> dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [limma]

### SF3B1 mutant-induced missplicing of MAP3K7 causes anemia in myelodysplastic syndromes. (PNAS 2022)

- DOI: 10.1073/pnas.2111703119 | PMCID: PMC8740767 | PMID: 34930825
- Evidence: To generate mRNA expression matrix for transcriptome analysis, we used featureCounts ( 52 ) from package ‘Subread’ to call read counts from STAR realigned bam files.
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ, featureCounts] -> normalisation [ImageJ] -> registration [featureCounts] -> differential/statistical testing [ImageJ]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Evidence: Read counts were generated with the Rsubread package function featureCounts in R ( 89 , 90 ). edgeR was used to construct principal component analysis plots of libraries ( 32 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Evidence: Trimmed reads that were at least 22 bp were mapped to the concatenated genomes of 27 P. gingivalis strains ( Dataset S1 ) using Bowtie2 v2.3.5 with default parameters ( 50 ). featureCounts (subread-2.0.1) was used to assign reads to protein-coding genes with the flags -s 0 (unstranded) and -O (allowMultiOverlap) in R 4.0.2 ( 53 , 54 ) so that each read was assigned to a single locus or to neighbor...
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Evidence: Different combination of read aligning (i.e., Spliced Transcripts Alignment to a Reference, STAR) and counting methods (featureCounts) did not materially alter the number of shared DEGs.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### Adaptive DNA amplification of synthetic gene circuit opens a way to overcome cancer chemoresistance. (PNAS 2023)

- DOI: 10.1073/pnas.2303114120 | PMCID: PMC10710087 | PMID: 38019857
- Evidence: The gene annotation was downloaded from the NCBI website, and read counts were obtained using FeatureCounts.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.6.1d] -> quantification [featureCounts] -> stage not stated [Fiji, ImageJ, R v4.1, fastp v0.20.1]

### &lt;i&gt;INDETERMINATE1&lt;/i&gt;-mediated expression of &lt;i&gt;FT&lt;/i&gt; family genes is required for proper timing of flowering in &lt;i&gt;Brachypodium distachyon&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312052120 | PMCID: PMC10655584 | PMID: 37934817
- Version used: **1.6.2**
- Evidence: Then, FeatureCounts v1.6.2 was used for counting reads for each annotated gene ( 86 ).
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, SAMtools v1.9] -> stage not stated [Galaxy, featureCounts v1.6.2, tidyverse]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Version used: **2.0.0**
- Evidence: Sorted BAM files were finally used as input for featureCounts (v.2.0.0) ( 45 ) in order to count the mapped reads to the gene coordinates reported in the GTF annotation file downloaded from GENCODE (v.41).
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Activity-induced MeCP2 phosphorylation regulates retinogeniculate synapse refinement. (PNAS 2023)

- DOI: 10.1073/pnas.2310344120 | PMCID: PMC10623012 | PMID: 37871205
- Evidence: Reads were counted in the full gene body (TSS to TTS of longest isoform, in order to include intronic reads) using Subread featureCounts.
- Full pipeline: read trimming [Bowtie2 v2.2.9, STAR v2.5.2b, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.9, STAR v2.5.2b] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.34.0, R v3.34.1, edgeR v3.34.1] -> stage not stated [SAMtools v0.1.19, featureCounts]

### Salicylic acid and RNA interference mediate antiviral immunity of plant stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302069120 | PMCID: PMC10589665 | PMID: 37824524
- Evidence: The annotation of small RNAs to genes was done by using featureCounts ( 53 ) with Araport 11 annotation.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2 v2.3.5] -> visualisation [Bioconductor, ggplot2, tidyverse] -> stage not stated [DESeq2, ImageJ, featureCounts]

### Downregulation of apoptotic repressor <i>AVEN</i> exacerbates cardiac injury after myocardial infarction. (PNAS 2023)

- DOI: 10.1073/pnas.2302482120 | PMCID: PMC10589712 | PMID: 37816050
- Evidence: Raw data reads quality was checked by Fastqc and then aligned to the human reference genome sequence (UCSC hg19 assembly) using STAR ( 50 ), and the uniquely mapped reads were assigned to genomic features using featureCounts ( 51 ).
- Full pipeline: quality control [featureCounts] -> alignment/mapping [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### The lack of negative association between TE load and subgenome dominance in synthesized <i>Brassica</i> allotetraploids. (PNAS 2023)

- DOI: 10.1073/pnas.2305208120 | PMCID: PMC10589682 | PMID: 37816049
- Evidence: RNA-seq fragments were aligned to the reference genomes using Hisat2 ( 63 ) with parameters “--max-intronlen 20000 -k 5”, and the fragment counts for each annotated gene were calculated by FeatureCounts ( 64 ) with parameters “-p -D 1000 -Q 5”.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [R, SciPy] -> stage not stated [Bismark, Bowtie2, RepeatMasker v4.0.3]

### Engineered bone marrow as a clinically relevant ex vivo model for primary bone cancer research and drug screening. (PNAS 2023)

- DOI: 10.1073/pnas.2302101120 | PMCID: PMC10523456 | PMID: 37729195
- Evidence: Subsequently, reads were mapped to the mouse genome (mm10) using STAR ( 66 ), and gene-level read counts were determined using “featureCounts” from Rsubread package ( 67 ).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [limma]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: The cleaned reads were aligned to the Drosophila reference genome (dm6) using the STAR aligner, and the number of reads mapped to each annotated gene was counted using featureCounts.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Mouse models of <i>SYNGAP1</i>-related intellectual disability. (PNAS 2023)

- DOI: 10.1073/pnas.2308891120 | PMCID: PMC10500186 | PMID: 37669379
- Evidence: FeatureCounts ( 57 ) was used to generate counts of reads aligning to known genes, which were then used in quality control measures.
- Full pipeline: quality control [FastQC, MultiQC, STAR, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [GSEA, R]

### Tet2 deletion in CD4+ T cells disrupts Th1 lineage commitment in memory cells and enhances T follicular helper cell recall responses to viral rechallenge. (PNAS 2023)

- DOI: 10.1073/pnas.2218324120 | PMCID: PMC10483640 | PMID: 37639586
- Version used: **1.6.3**
- Evidence: Briefly, mapped reads were assigned to annotated genes using featureCounts version 1.6.3, and differentially expressed genes were identified using DESeq2 version 1.30.1 with a 5% false discovery rate ( 33 ).
- Full pipeline: quality control [FastQC v0.11.4, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark, Bowtie2, DESeq2 v1.30.1, featureCounts v1.6.3] -> differential/statistical testing [DESeq2 v1.30.1, featureCounts v1.6.3] -> stage not stated [BEDTools]

### SARS-CoV-2 mouse adaptation selects virulence mutations that cause TNF-driven age-dependent severe disease with human correlates. (PNAS 2023)

- DOI: 10.1073/pnas.2301689120 | PMCID: PMC10410703 | PMID: 37523564
- Evidence: Reads were aligned to the reference genome using the Rsubread align function, and gene counts were quantified from the resultant BAM files using Subread featureCounts ( 43 ) (v2.0.3) and the Mus musculus GRCm39.106 reference GTF file ( http://ftp.ensembl.org/pub/release-106/gtf/mus_musculus/ ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.12] -> alignment/mapping [featureCounts, minimap2 v2.2.4] -> quantification [featureCounts] -> machine learning [StarDist] -> stage not stated [R v4.2, edgeR, limma]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **2.0.1**
- Evidence: Read count matrices were obtained with featureCounts v2.0.1 and differential expression assessed with DESeq2 v1.36.0 ( 78 ) using a FDR < 0.05 and log2 FC > ± 1.0.
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### IL-7R licenses a population of epigenetically poised memory CD8<sup>+</sup> T cells with superior antitumor efficacy that are critical for melanoma memory. (PNAS 2023)

- DOI: 10.1073/pnas.2304319120 | PMCID: PMC10372654 | PMID: 37459511
- Evidence: Filtered reads were aligned to referen genome mm10 using STAR aligner and quantified using featureCounts.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, STAR, featureCounts] -> alignment/mapping [STAR, featureCounts] -> quantification [STAR, featureCounts] -> differential/statistical testing [DESeq2, R v4.0] -> stage not stated [RSEM]

### Ancient vertebrate dermal armor evolved from trunk neural crest. (PNAS 2023)

- DOI: 10.1073/pnas.2221120120 | PMCID: PMC10372632 | PMID: 37459514
- Evidence: Transcript counts were calculated using featureCounts ( 58 ), and DGE analysis was performed using DESeq2 ( 59 ).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega v1.2.3] -> visualisation [ComplexHeatmap] -> stage not stated [DESeq2, featureCounts]

### NOS inhibition reverses TLR2-induced chondrocyte dysfunction and attenuates age-related osteoarthritis. (PNAS 2023)

- DOI: 10.1073/pnas.2207993120 | PMCID: PMC10629581 | PMID: 37428931
- Evidence: Read counts were determined with featureCounts ( 73 ).
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [featureCounts] -> stage not stated [GSEA, MACS2]

### Adaptive structural and functional evolution of the placenta protects fetal growth in high-elevation deer mice. (PNAS 2023)

- DOI: 10.1073/pnas.2218049120 | PMCID: PMC10288601 | PMID: 37307471
- Evidence: Read counts were determined using featureCounts in Subread ( 97 ), allowing for fractional counting of mapping reads.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [ImageJ v2.0.0, featureCounts] -> stage not stated [R v4.0, WGCNA, emmeans, lme4]

### Mechanoepigenetic regulation of extracellular matrix homeostasis via Yap and Taz. (PNAS 2023)

- DOI: 10.1073/pnas.2211947120 | PMCID: PMC10235980 | PMID: 37216538
- Evidence: FeatureCounts was used to generate count files ( 63 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2, Picard, SAMtools, deepTools, featureCounts]

### Paf1 complex subunit Rtf1 stimulates H2B ubiquitylation by interacting with the highly conserved N-terminal helix of Rad6. (PNAS 2023)

- DOI: 10.1073/pnas.2220041120 | PMCID: PMC10235976 | PMID: 37216505
- Evidence: Transcript counts were extracted from the BAM files using featureCounts ( 72 ).
- Full pipeline: alignment/mapping [DESeq2, STAR v2.7.5a] -> quantification [DESeq2] -> stage not stated [AlphaFold, ComplexHeatmap, featureCounts]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: The genes in X. tropicalis and X. laevis were counted separately using featureCounts ( 53 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### IRIS: Discovery of cancer immunotherapy targets arising from pre-mRNA alternative splicing. (PNAS 2023)

- DOI: 10.1073/pnas.2221116120 | PMCID: PMC10214192 | PMID: 37192158
- Version used: **2.0.1**
- Evidence: Splicing factor ( 36 ) gene expression levels were quantified by FeatureCounts v2.0.1 ( 60 ), followed by DESeq2 v1.26.0 ( 61 ) normalization.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [Cufflinks v2.2.1, DESeq2 v1.26.0, featureCounts v2.0.1] -> normalisation [DESeq2 v1.26.0, featureCounts v2.0.1]

### CDYL reinforces male gonadal sex determination through epigenetically repressing <i>Wnt4</i> transcription in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2221499120 | PMCID: PMC10193937 | PMID: 37155872
- Version used: **1.6.4**
- Evidence: DNAFORM using raw counts obtained with featureCounts (v1.6.4) (a software program in the Subread package).
- Full pipeline: alignment/mapping [STAR] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat] -> stage not stated [MACS2, featureCounts v1.6.4]

### Nonpathological inflammation drives the development of an avian flight adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2219757120 | PMCID: PMC10175837 | PMID: 37126698
- Evidence: The bioinformatic analysis was performed on a Linux platform utilizing a custom bioinformatics pipeline that included STAR (version 2.70f) alignment of reads, the SUBREAD featureCounts program (version 2.0.0) to produce count tables, and DESeq2 R software package (1.26.0; R version 2.6.3) for differential expression analysis.
- Full pipeline: quality control [FastQC] -> alignment/mapping [DESeq2, R v2.70f, STAR v2.70f, featureCounts] -> quantification [ImageJ] -> differential/statistical testing [DESeq2, R v2.70f, STAR v2.70f, featureCounts]

### Application of a quantitative framework to improve the accuracy of a bacterial infection model. (PNAS 2023)

- DOI: 10.1073/pnas.2221542120 | PMCID: PMC10175807 | PMID: 37126703
- Version used: **2.0.1**
- Evidence: The reads that did not map to the decoy genomes were then mapped to P. aeruginosa PAO1 (Accession number GCF_000006765.1) using bowtie2. featureCounts v2.0.1 was used to assign mapped reads to PAO1 genes with the flags -s 1 (stranded) and -O (allowMultiOverlap) so that each read was assigned to a single locus or to neighboring genes ( 53 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.10] -> read trimming [Bowtie2 v2.3.5, Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> normalisation [DESeq2 v1.28.1, R] -> stage not stated [BLAST]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Reads were aligned to hg38 using a Bpipe ( 92 ) RNA-Seq pipeline that incorporated FastQC quality control, adaptor trimming with Trimmomatic v.0.35 ( 93 ), mapping with STAR 2.7.3a ( 94 ), summarizing reads over genes with featureCounts ( 95 ), and MultiQC ( 96 ) to summarize the analyses.
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Derepression of Y-linked multicopy protamine-like genes interferes with sperm nuclear compaction in <i>D. melanogaster</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220576120 | PMCID: PMC10120018 | PMID: 37036962
- Evidence: ...ignIntronMax 25000,” indexed with all FlyBase genes (FB2020_06 Dmel Release 6.37) and the option “—sjdbOverhang 100.” Gene counts were obtained using featureCounts ( 49 ); v 2.0.1, with “-M –fraction -p -s 2.” After summing gene counts for technical replicates, differential expression was assayed using DESeq2 v1.26.0 ( 50 ), with lfcShrink(type=”ashr”)).
- Full pipeline: alignment/mapping [BEDTools, STAR v2.7.1a] -> quantification [BEDTools] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts] -> stage not stated [ImageJ]

### Mutant β<sub>1</sub>-adrenergic receptor improves REM sleep and ameliorates tau accumulation in a mouse model of tauopathy. (PNAS 2023)

- DOI: 10.1073/pnas.2221686120 | PMCID: PMC10104526 | PMID: 37014857
- Version used: **1.5.0**
- Evidence: Quantification of gene expression was analyzed by featureCounts (version 1.5.0-p3).
- Full pipeline: quantification [featureCounts v1.5.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### Experimental evidence for the functional importance and adaptive advantage of A-to-I RNA editing in fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2219029120 | PMCID: PMC10041177 | PMID: 36917661
- Evidence: The number of reads aligned to each gene (count data) was calculated using featureCounts ( 70 ) and normalized by Transcripts Per Million (TPM).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [R v4.1, featureCounts] -> normalisation [featureCounts] -> visualisation [AlphaFold, R v4.1, UCSF Chimera v1.16] -> stage not stated [BLAST]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Version used: **1.6.3**
- Evidence: The number of fragments (a pair-read was counted as one fragment) was counted using featureCounts v1.6.3 software ( 54 ).
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### KMT2D acetylation by CREBBP reveals a cooperative functional interaction at enhancers in normal and malignant germinal center B cells. (PNAS 2023)

- DOI: 10.1073/pnas.2218330120 | PMCID: PMC10089214 | PMID: 36893259
- Version used: **1.6.3**
- Evidence: Genome-mapped reads were aligned to exons on the mm10 transcriptome reference ( 62 ) based on the information in the genomic BAM files using featureCounts (v1.6.3) ( 63 ) to produce abundance tables.
- Full pipeline: alignment/mapping [HISAT2, featureCounts v1.6.3] -> quantification [ImageJ, featureCounts v1.6.3] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v4.2, SciPy] -> stage not stated [GSEA, HOMER]

### Neuron-specific transcriptomic signatures indicate neuroinflammation and altered neuronal activity in ASD temporal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2206758120 | PMCID: PMC10013873 | PMID: 36862688
- Version used: **1.6.4**
- Evidence: Gene-level quantifications were calculated using featureCounts (v1.6.4).
- Full pipeline: quantification [featureCounts v1.6.4] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [DESeq2 v1.22.2, GSEA, WGCNA]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **1.5.2**
- Evidence: RNA-seq data of multiple Bf developmental stages were downloaded from NCBI SRA (PRJDB3785) for estimating the Hox gene expression level using HISAT2 (2.0.4) and featureCounts (v1.5.2).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Version used: **1.5.1**
- Evidence: For RNA-seq analyses, read counts were obtained with subread’s featureCounts v1.5.1 ( 70 ) from the bam files of input samples.
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **1.6.2**
- Evidence: To quantify the expression level, we counted the mapped reads using featureCounts (1.6.2) ( 81 ) with options “-M -C” and calculated the TPM (transcripts per million) values.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Time of day determines postexercise metabolism in mouse adipose tissue. (PNAS 2023)

- DOI: 10.1073/pnas.2218510120 | PMCID: PMC9974500 | PMID: 36780527
- Version used: **1.6.0**
- Evidence: Reads were mapped to Ensembl mm10 release 92 using STAR (2.5.3a), and transcripts counted with FeatureCounts (1.6.0).
- Full pipeline: alignment/mapping [featureCounts v1.6.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [R]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **2.0.1**
- Evidence: Long RNA data were quantified by featureCounts v2.0.1 from the Subread package, modifying strandness to the forward or reverse strand as needed to generate sense or antisense counts, respectively.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Version used: **2.0.1**
- Evidence: IES features were counted with featureCounts v2.0.1 ( 87 ).
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Evidence: Aligned read counts were extracted using the featureCounts command in Subread v2.0.1 ( 79 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Reads overlapping Ensembl gene models (Salmo_salar-GCA_905237065.2) were quantified using R (version 4.2) package “Rsubread” ( 65 ) and the function “featureCounts”, specifying the parameters “count ChimericFragments=FALSE, countReadPairs=TRUE, countMultiMappingReads=TRUE, fraction=TRUE,” and “primaryOnly=TRUE”.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### Characterization of the enzyme for 5-hydroxymethyluridine production and its role in silencing transposable elements in dinoflagellates. (PNAS 2024)

- DOI: 10.1073/pnas.2400906121 | PMCID: PMC11572971 | PMID: 39508766
- Version used: **1.5.3**
- Evidence: The featureCounts (v1.5.3) tool with the “-M --fraction” setting was used to weight counts for multimapped reads.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.2.5, HOMER, STAR v2.7.10a] -> quantification [HOMER] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [deepTools v3.5.5, featureCounts v1.5.3]

### Free-swimming bacteria transcriptionally respond to shear flow. (PNAS 2024)

- DOI: 10.1073/pnas.2406688121 | PMCID: PMC11494325 | PMID: 39383001
- Evidence: Quality control and adapter trimming were performed with Illumina’s software bcl-convert, read mapping was performed with HISAT2 ( 40 ), and read quantification was performed using Subread’s featureCounts ( 41 ) functionality.
- Full pipeline: quality control [HISAT2, featureCounts] -> read trimming [HISAT2, edgeR, featureCounts] -> alignment/mapping [HISAT2, featureCounts] -> quantification [HISAT2, edgeR, featureCounts] -> normalisation [edgeR] -> stage not stated [ImageJ]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Evidence: 51 ) for read counts computed using featureCounts ( 52 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### Local adaptation, plasticity, and evolved resistance to hypoxic cold stress in high-altitude deer mice. (PNAS 2024)

- DOI: 10.1073/pnas.2412526121 | PMCID: PMC11474095 | PMID: 39352929
- Version used: **2.0.3**
- Evidence: We implemented featureCounts v2.0.3 ( 71 ) to count numbers of reads aligning to annotated genes (i.e., counts were performed at the gene level; n = 32,828); featureCounts was run using default parameters, with the exception that we counted reads overlapping with more than one feature (-O flag), meaning that each overlapping feature receives a count of 1 from a read.
- Full pipeline: alignment/mapping [featureCounts v2.0.3] -> normalisation [edgeR] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [R, lme4] -> stage not stated [WGCNA]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **2.0.1**
- Evidence: Read counts for each gene were obtained using featureCounts (v2.0.1) ( 66 ), and UMI duplications were removed using UMI-tools.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Transdifferentiation occurs without resetting development-specific DNA methylation, a key determinant of full-function cell identity. (PNAS 2024)

- DOI: 10.1073/pnas.2411352121 | PMCID: PMC11441492 | PMID: 39292740
- Evidence: Read counting was performed using featureCounts (V 1.6.2) with mm10 gtf annotation.
- Full pipeline: read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, SAMtools, Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, R]

### Machine learning reveals the transcriptional regulatory network and circadian dynamics of &lt;i&gt;Synechococcus elongatus&lt;/i&gt; PCC 7942. (PNAS 2024)

- DOI: 10.1073/pnas.2410492121 | PMCID: PMC11420160 | PMID: 39269777
- Evidence: RSEQC was used to infer read direction before generating read counts using featureCounts ( 54 , 55 ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore, featureCounts] -> read trimming [FastQC, Trim Galore] -> quantification [MultiQC, featureCounts] -> dimensionality reduction/clustering [STRING db] -> stage not stated [scikit-learn]

### Plasma cell-free RNA signatures of inflammatory syndromes in children. (PNAS 2024)

- DOI: 10.1073/pnas.2403897121 | PMCID: PMC11406294 | PMID: 39240972
- Evidence: Total counts were calculated using featureCounts 30 (v2.0.0).
- Full pipeline: quality control [SAMtools v1.14] -> alignment/mapping [SAMtools v1.14] -> quantification [DESeq2, R] -> machine learning [Snakemake] -> stage not stated [featureCounts]

### Oxysterol binding protein regulates the resolution of TLR-induced cytokine production in macrophages. (PNAS 2024)

- DOI: 10.1073/pnas.2406492121 | PMCID: PMC11331125 | PMID: 39361877
- Evidence: Feature counts were extracted using the featureCounts software ( 50 ), distributed as part of the Subread package v1.5.2.
- Full pipeline: quality control [FastQC v0.11.5] -> quantification [ImageJ, limma] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [R, edgeR v3.26.8, limma] -> stage not stated [GSEA, MACS2 v2.1.0, featureCounts]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: The STAR-mapped BAM files and our custom gene annotation file were used to generate both transcript-level and exon-level count tables using FeatureCounts ( 73 ) (featureCounts -M -t exon).
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### UPF1 deficiency enhances mitochondrial ROS which promotes an immunosuppressive microenvironment in pancreatic ductal adenocarcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2401996121 | PMCID: PMC11331118 | PMID: 40591563
- Evidence: Briefly, raw reads were fed into “rna-star” module of Seq-N-Slide which employs Trimmomatic for adaptor trimming and low-quality base removal, STAR for alignment to reference genomes (mm10), fastq_screen for contaminant detection, Picard for base distribution and 5′/3′ biases, and featureCounts to generate genes-samples count matrices.
- Full pipeline: read trimming [Picard, STAR, Trimmomatic, featureCounts] -> alignment/mapping [Picard, STAR, Trimmomatic, featureCounts] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2]

### Improvement of a mouse infection model to capture &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt; chronic physiology in cystic fibrosis. (PNAS 2024)

- DOI: 10.1073/pnas.2406234121 | PMCID: PMC11331117 | PMID: 39102545
- Version used: **2.0.1**
- Evidence: Reads were assigned to PAO1 coding sequences in FeatureCounts (v2.0.1) ( 34 ), with reads assigned to overlapping meta-features (if applicable) and strandedness specified (strandedness information is provided in Dataset S1 ).
- Full pipeline: quality control [Bowtie2 v2.4.2, FastQC v0.11.9] -> read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.4.2, FastQC v0.11.9] -> stage not stated [featureCounts v2.0.1]

### Convergent evolution in toxin detection and resistance provides evidence for conserved bacterial-fungal interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2304382121 | PMCID: PMC11317636 | PMID: 39088389
- Evidence: Read summarization was performed using featureCounts ( 63 ).
- Full pipeline: read trimming [Bowtie2 v2.4.2] -> alignment/mapping [Bowtie2 v2.4.2, Clustal Omega] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, PyMOL, featureCounts]

### Cone photoreceptor differentiation regulated by thyroid hormone transporter MCT8 in the retinal pigment epithelium. (PNAS 2024)

- DOI: 10.1073/pnas.2402560121 | PMCID: PMC11287251 | PMID: 39018199
- Evidence: Reads were counted by FeatureCounts (subread v2.0.6) and normalized as counts per million mapped reads (cpm).
- Full pipeline: alignment/mapping [STAR v2.7.10b, featureCounts] -> quantification [kallisto v0.46.0] -> normalisation [featureCounts] -> stage not stated [ImageJ]

### Life stage-specific poly(A) site selection regulated by <i>Trypanosoma brucei</i> DRBD18. (PNAS 2024)

- DOI: 10.1073/pnas.2403188121 | PMCID: PMC11260167 | PMID: 38990950
- Evidence: Per gene quantifications were calculated using the subread function FeatureCounts, using the strand-specific parameter enabled.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, R, Seurat]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Evidence: Unnormalized raw read counts of genes were obtained from bam files using the featureCounts function from the Subread package (version 1.6.2) ( 48 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### The role of mitochondria in sex- and age-specific gene expression in a species without sex chromosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2321267121 | PMCID: PMC11181141 | PMID: 38838014
- Evidence: The featureCounts program in the Subread package release 1.6.4 ( 92 ) was used to estimate the count values for all annotated genes with the parameters (-d 200 -D 500 -s 1 -B -C -p).
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.38] -> read trimming [FastQC v0.11.8, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.7.2] -> stage not stated [WGCNA, featureCounts]

### Innate acting memory Th1 cells modulate heterologous diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2312837121 | PMCID: PMC11181110 | PMID: 38838013
- Evidence: Count tables were generated with featureCounts ( 62 ) (version 1.22.2) using the options ‘-t exon -g gene_id’ and the GTF file of the GRCm38 build (version 101) as reference.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [R v4.0.2, featureCounts, ggplot2, pheatmap v1.0.12]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Version used: **2.0.0**
- Evidence: Next, featureCounts (v2.0.0) was used to count reads in exons and generate a read count table.
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### Premeiotic 24-nt phasiRNAs are present in the <i>Zea</i> genus and unique in biogenesis mechanism and molecular function. (PNAS 2024)

- DOI: 10.1073/pnas.2402285121 | PMCID: PMC11127045 | PMID: 38739785
- Version used: **1.6.3**
- Evidence: Reads mapped to PHAS loci or miRNAs were counted using featureCounts v1.6.3 ( 48 ) with parameter -M and normalized to CPM using edgeR v4.0.2 ( 49 ).
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MUSCLE, edgeR v4.0.2, featureCounts v1.6.3] -> normalisation [edgeR v4.0.2, featureCounts v1.6.3] -> stage not stated [BEDTools v2.29.2, StringTie v2.1.7]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: Count tables were obtained using the featureCounts tool.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### Normalizing granuloma vasculature and matrix improves drug delivery and reduces bacterial burden in tuberculosis-infected rabbits. (PNAS 2024)

- DOI: 10.1073/pnas.2321336121 | PMCID: PMC10998582 | PMID: 38530888
- Version used: **1.5.0**
- Evidence: Raw gene counts were then obtained using featureCounts v.1.5.0-p3 ( 54 ), while disregarding reads aligned to multiple genes.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> normalisation [DESeq2 v1.42.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.0] -> stage not stated [ImageJ]

### Sexual stage-specific A-to-I mRNA editing is mediated by tRNA-editing enzymes in fungi. (PNAS 2024)

- DOI: 10.1073/pnas.2319235121 | PMCID: PMC10962958 | PMID: 38466838
- Evidence: With the inputs of these transcription initiation and termination sites, reads mapping to the FgTAD2 -L and FgTAD2 -S isoforms were counted and normalized to compute their transcripts per million (TPM) with FeatureCounts ( 30 ).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [featureCounts] -> stage not stated [AlphaFold, Picard]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: The resulting processed reads were aligned to the reference M. abscessus ATCC 19977 genome (Genome accession: NC_010397 ) using STAR2.7.1 and aligned reads were counted using featureCounts ( 61 , 62 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Evidence: The aligned reads were quantified by featureCounts from SubRead v.1.5.1.
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### A metabolic cell death program downstream of SARM1 couples NAD&lt;sup&gt;+&lt;/sup&gt; depletion to BAX activation and APAF1 degradation. (PNAS 2025)

- DOI: 10.1073/pnas.2522444122 | PMCID: PMC12718333 | PMID: 41364765
- Evidence: ...lt_1.sam > result_2.sam.” Finally, the number of Gene trap insertions in each gene was quantified based on the human genome annotation file using the featureCounts tool: “featureCounts -T 8 -t gene -g gene_name -a Homo_sapiens.GRCh38.101.gtf -o result.txt result_2.sam.” The results from all steps were subsequently compiled and analyzed using Excel to provide a comprehensive overview of the sequenc...
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, Trimmomatic] -> quantification [featureCounts] -> stage not stated [RSEM]

### Distinguishing subtypes of endothelial cells in the mouse aorta. (PNAS 2025)

- DOI: 10.1073/pnas.2525755122 | PMCID: PMC12704785 | PMID: 41343672
- Evidence: Samtools software (version 1.16.1) was used to filter out the duplicated reads, and the Subread package (version 1.4.6-p5) was used to summarize the gene counts with the featureCounts function.
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat] -> stage not stated [R, SAMtools, featureCounts]

### Core microRNAs regulate neural crest delamination and condensation in the developing trigeminal ganglion. (PNAS 2025)

- DOI: 10.1073/pnas.2517668122 | PMCID: PMC12704738 | PMID: 41329730
- Evidence: Read quantification was performed with featureCounts using a microRNA annotation file from miRBase ( 39 ), corresponding to the Galgal5 genome assembly.
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [ComplexHeatmap v2.6.2] -> stage not stated [ImageJ v1.53, STRING db]

### Lamprey &lt;i&gt;FOXN1&lt;/i&gt; rescues the block of thymic epithelial cell development in the mouse &lt;i&gt;Foxn1&lt;/i&gt;-deficient thymic rudiment. (PNAS 2025)

- DOI: 10.1073/pnas.2520664122 | PMCID: PMC12685072 | PMID: 41289399
- Version used: **1.6.1**
- Evidence: Gene-level counts were generated with featureCounts v1.6.1 ( 56 ).
- Full pipeline: read trimming [Cutadapt v4.9, STAR v2.7.11b] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, STAR v2.7.11b] -> differential/statistical testing [emmeans, limma] -> visualisation [STAR v2.7.11b] -> stage not stated [featureCounts v1.6.1]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Version used: **2.0.6**
- Evidence: The number of reads mapped to each gene was counted using featureCounts v2.0.6 with a reference gene model (XL_9.1 _ v1.8.3.2.primaryTranscripts.gff3; Xenbase) ( 32 , 78 ) and compared using edgeR v4.1.25 ( 82 ) to detect DEGs (FDR < 0.05) between groups.
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Evidence: Gene-level quantification was performed with featureCounts (subread v2.0.6).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **2.0.6**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Neuronal plasticity at puberty in mouse hypothalamic &lt;i&gt;Kiss1&lt;/i&gt; neurons that control fertility. (PNAS 2025)

- DOI: 10.1073/pnas.2512855122 | PMCID: PMC12582290 | PMID: 41118223
- Evidence: Read assignment to genes, read summarization, and gene-level quantification were performed by featureCounts (Subread v 2.0.2).
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: Using featureCounts ( 29 ), reads were assigned to exonic regions and counted.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Version used: **2.0.6**
- Evidence: Gencode v38 gene annotations were provided to STAR to improve the accuracy of mapping. featureCounts (v2.0.6) was used to count the number of mapped reads to each gene ( 57 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: Raw RNA-seq reads were trimmed using cutadapt-1.9.1 ( 44 ) and mapped to Arabidopsis thaliana TAIR10 reference genome using STAR-2.5.a ( 45 ), featureCounts ( 46 ) was used to count the numbers of reads mapped to each gene.
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Mutations in the circadian cycle drive adaptive plasticity in cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2506928122 | PMCID: PMC12435244 | PMID: 40901874
- Version used: **2.0.1**
- Evidence: Individual sample gene expression levels were quantified with featureCounts (v2.0.1) ( 65 ).
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [StringTie v2.2.1, featureCounts v2.0.1] -> normalisation [StringTie v2.2.1] -> differential/statistical testing [DESeq2 v1.34.0, R v4.2.1]

### Lysosomal reduced thiols are essential for mouse embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2427125122 | PMCID: PMC12435214 | PMID: 40892915
- Evidence: Gene-level quantification was performed using featureCounts from the Subread package, assigning uniquely mapped reads to annotated genes.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Shared metabolism between a bacterial and fungal species that reside in the human gut. (PNAS 2025)

- DOI: 10.1073/pnas.2504785122 | PMCID: PMC12415286 | PMID: 40854125
- Version used: **2.0.1**
- Evidence: Read counts for each species were then extracted using Subread FeatureCounts (2.0.1) using the appropriate genome version specific GFF file ( 65 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.14] -> quantification [featureCounts v2.0.1] -> normalisation [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: Counts for genes and TEs were generated using featureCounts v2 and normalized for sequencing depth using the TMM method implemented in the limma package of Bioconductor.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### A 65-kb deletion survey identifies a distal &lt;i&gt;cis-&lt;/i&gt;regulatory region for red-light induction of &lt;i&gt;Ghd7&lt;/i&gt;, a key rice floral repressor. (PNAS 2025)

- DOI: 10.1073/pnas.2423119122 | PMCID: PMC12377723 | PMID: 40811470
- Evidence: Read assignment to transcript features was performed using FeatureCounts from the Subread package (version 2.0.6).
- Full pipeline: quality control [FastQC v0.12.1, fastp v0.23.4] -> read trimming [FastQC v0.12.1, fastp v0.23.4] -> alignment/mapping [HISAT2 v2.2.1, minimap2] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [SAMtools v1.19, featureCounts]

### Transcription termination promotes splicing efficiency and fidelity in a compact genome. (PNAS 2025)

- DOI: 10.1073/pnas.2507187122 | PMCID: PMC12358841 | PMID: 40763012
- Evidence: For read counts, we calculated the number of reads mapping to each gene using featureCounts as part of the Rsubread package (version 2.12.3) allowing for multiple overlaps.
- Full pipeline: alignment/mapping [featureCounts, minimap2] -> quantification [DESeq2, featureCounts] -> normalisation [DESeq2] -> stage not stated [BEDTools, SAMtools]

### Lysosomal glucocerebrosidase is needed for ciliary Hedgehog signaling: A convergent pathway contributing to Parkinson's disease. (PNAS 2025)

- DOI: 10.1073/pnas.2504774122 | PMCID: PMC12337309 | PMID: 40737317
- Evidence: Hisat2 v2.0.5 was used to align clean reads to the mm39 mouse reference genome, and raw count of each sample was evaluated by featureCounts ( 45 ) v1.5.0-p3.
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [CellProfiler]

### Deficiency in transmitter release triggers homeostatic transcriptional changes that increase presynaptic excitability. (PNAS 2025)

- DOI: 10.1073/pnas.2322714122 | PMCID: PMC12337328 | PMID: 40729383
- Evidence: Mapping was performed with HISAT2 (ver 2.1.0) ( 81 ), and the counts matrix was generated with the featureCounts function from the Subread package (ver 1.6.4) ( 82 ).
- Full pipeline: quality control [FastQC v0.11.7, Trimmomatic v0.38] -> read trimming [FastQC v0.11.7, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0, featureCounts] -> normalisation [DESeq2 v1.26.0] -> visualisation [ggplot2 v3.2.1] -> stage not stated [R v4.1.0]

### HIF1α mediates circadian regulation of skeletal muscle metabolism and substrate preference in response to time-of-day exercise. (PNAS 2025)

- DOI: 10.1073/pnas.2504080122 | PMCID: PMC12280960 | PMID: 40627397
- Evidence: Reads were aligned to the mouse genome assembly (mm10) using STAR aligner ( 45 ), and transcripts counted using featureCounts ( 46 ).
- Full pipeline: alignment/mapping [STAR, featureCounts] -> quantification [Python] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [emmeans]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Transcript counts were calculated using featureCounts (Subread) and differential gene expression analysis was performed using DESeq2 ( 62 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### SARS-CoV-2 nsp15 enhances viral virulence by subverting host antiviral defenses. (PNAS 2025)

- DOI: 10.1073/pnas.2426528122 | PMCID: PMC12184426 | PMID: 40504150
- Evidence: Raw gene counts were generated with FeatureCounts ( 55 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [pheatmap] -> stage not stated [ImageJ, featureCounts]

### Spatiotemporal regulation of target mRNA cleavage by 21-nt phasiRNAs in maize anthers. (PNAS 2025)

- DOI: 10.1073/pnas.2422647122 | PMCID: PMC12184425 | PMID: 40498447
- Version used: **2.0.1**
- Evidence: Gene expression levels were quantified using FeatureCounts v2.0.1 with raw counts ( 36 ).
- Full pipeline: quantification [featureCounts v2.0.1] -> stage not stated [edgeR]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Evidence: Unique gene hit counts were obtained using featureCounts from the Subread package v1.5.2, counting only unique reads within exon regions.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Version used: **1.5.0**
- Evidence: The number of reads mapped to each gene was quantified using featureCounts (v1.5.0-p3).
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### Perturbing nuclear glycosylation in the mouse preimplantation embryo slows down embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2410520122 | PMCID: PMC12012502 | PMID: 40203037
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability The datasets generated in this study are available at Biostudies under the accession E-MTAB-12981 (73) , together with the table of gene counts (featureCounts output) for all samples that passed the filtering steps (last column of SI Appendix , Table S3 ).
- Full pipeline: read trimming [STAR v2.7.8a] -> alignment/mapping [STAR v2.7.8a] -> normalisation [DESeq2, deepTools v3.0.2] -> stage not stated [GSEA, ImageJ, featureCounts]

### A conserved ARF-DNA interface underlies auxin-triggered transcriptional response. (PNAS 2025)

- DOI: 10.1073/pnas.2501915122 | PMCID: PMC12002309 | PMID: 40168121
- Evidence: Cleaned reads were mapped to the M. polymorpha genome (v6.1, https://marchantia.info/ ) using Hisat2 for paired-end reads ( 46 ), followed by counting reads per gene with FeatureCounts using default parameters ( 47 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [featureCounts] -> quantification [ilastik v1.3.3] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, HMMER, PyMOL]

### Diel partitioning in microbial phosphorus acquisition in the Sargasso Sea. (PNAS 2025)

- DOI: 10.1073/pnas.2410268122 | PMCID: PMC11929403 | PMID: 40085655
- Evidence: For the cellular community, trimmed filtered reads were mapped to the combined assembly using BBMap v38.84 ( 41 ) using default parameters and tabulated using featureCounts ( 43 ).
- Full pipeline: read trimming [featureCounts] -> alignment/mapping [BLAST, eggNOG, featureCounts] -> stage not stated [DESeq2]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Version used: **2.0.0**
- Evidence: Reads mapped to genes were counted with featureCounts (version 2.0.0) ( 78 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Evidence: Gene-level read counts were obtained using featureCounts (Subread v2.0.6) with reverse-strand settings (-s 2).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Version used: **1.5.0**
- Evidence: Reads were counted for exons of annotated genes using featureCounts (v1.5.0-p3) in paired-end mode.
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### A long-distance inhibitory system regulates haustoria numbers in parasitic plants. (PNAS 2025)

- DOI: 10.1073/pnas.2424557122 | PMCID: PMC11874510 | PMID: 39964721
- Evidence: The quality-filtered reads were mapped to the Phtheirospermum genome ( 16 ) using STAR ( 49 ) and the read count was calculated using FeatureCounts ( 50 ).
- Full pipeline: read trimming [fastp, featureCounts] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> stage not stated [InterProScan]

### Extensive location bias of the GPCR-dependent translatome via site-selective activation of mTOR. (PNAS 2025)

- DOI: 10.1073/pnas.2414738122 | PMCID: PMC11874449 | PMID: 39964727
- Evidence: FeatureCounts (Subread version 1.6.3) was used to align and quantify coding sequences, with RPF reads being narrowed to reads of length 26 to 34 nucleotides.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v3.16] -> stage not stated [Cytoscape, R]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Version used: **2.0.1**
- Evidence: Gene counts were extracted with FeatureCounts (v2.0.1) ( 80 ), and expression levels were normalized to FPKM values using custom R scripts.
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Coding relationship links RNA G-quadruplexes and protein RGG motifs in RNA-binding protein autoregulation. (PNAS 2025)

- DOI: 10.1073/pnas.2413721122 | PMCID: PMC11789052 | PMID: 39847338
- Evidence: In order to filter the transcripts for those that were at all available in the experiment and use them as a background in subsequent analysis, the sequencing reads of the rG4-seq data, which were used for the analysis with rG4-seeker, were quantified using featureCounts ( 69 ) and genes with a CPM ≥ 1 in at least two samples and under Li + and K + or K + + PDS conditions were retained.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [featureCounts, kallisto v0.50.1]

### Codon bias, nucleotide selection, and genome size predict in situ bacterial growth rate and transcription in rewetted soil. (PNAS 2025)

- DOI: 10.1073/pnas.2413032122 | PMCID: PMC11761963 | PMID: 39805015
- Evidence: Counts of reads mapping to DRAM-annotated genes were identified using featureCounts ( 74 ).
- Full pipeline: alignment/mapping [DESeq2, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [R v4.2.1, ggplot2, tidyverse] -> visualisation [R v4.2.1, ggplot2, tidyverse] -> stage not stated [NumPy, Python v3.8.2]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Evidence: Uniquely mapped sequencing reads were assigned to mm10 refGene genes using featureCounts (from subread).
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Version used: **2.0.1**
- Evidence: RNA-seq data from NCBI SRA were filtered ( Dataset S15 ), and then aligned to TM-1 genome via HISAT2 (v2.2.1) ( 77 ), and gene expression quantified by featureCounts (v2.0.1) ( 78 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: To determine DARs, featureCounts ( 60 ) version 2.0.2 was used to generate a counts table of reads from each sample mapping to the merged set of all IDR-called peaks.
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Version used: **1.6.3**
- Evidence: The mapped SAM files were then put through subread featureCounts version 1.6.3 ( 62 ) to count mapped transcripts for each library, in pair-ended mode using the parameters -O for overlapping models allowed and -Q 40 for a minimum mapping quality of 40.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Versatile SMAD2 and SMAD3 epitope-tagged mouse models for genomic profiling of TGFβ signaling: Uncovering GDF9-SMAD2/3 targets. (PNAS 2026)

- DOI: 10.1073/pnas.2600071123 | PMCID: PMC13056123 | PMID: 41911462
- Version used: **2.1.1**
- Evidence: Aligned reads were assigned to genes with featureCounts v2.1.1.
- Full pipeline: quality control [Bowtie2] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2, STAR v2.7.11b, featureCounts v2.1.1] -> quantification [STAR v2.7.11b] -> stage not stated [DESeq2 v1.48.2, HOMER v4.11, deepTools v2.4.2]

### Fibro-adipogenic progenitor cells from murine SMA muscles are intrinsically adipogenic. (PNAS 2026)

- DOI: 10.1073/pnas.2525423123 | PMCID: PMC13037897 | PMID: 41886383
- Evidence: After QC, reads were aligned to the reference genome of Mus musculus GRC39 using Salmon alignment tool ( 73 , 74 ) and gene quantification was completed using featureCounts ( 75 ).
- Full pipeline: quality control [featureCounts] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ, fastp]

### KLF2 overrides the resident memory CD8 T cell differentiation program, in opposition to KLF3. (PNAS 2026)

- DOI: 10.1073/pnas.2533700123 | PMCID: PMC13037849 | PMID: 41871244
- Version used: **2.0.6**
- Evidence: FastQC v0.12.1 ( 65 ) was used to generate sequence quality reports for raw and trimmed reads. featureCounts v2.0.6 ( 66 ) was used to count mapped reads to genes.
- Full pipeline: quality control [FastQC v0.12.1, featureCounts v2.0.6] -> read trimming [FastQC v0.12.1, featureCounts v2.0.6] -> alignment/mapping [FastQC v0.12.1, featureCounts v2.0.6] -> differential/statistical testing [GSEA] -> stage not stated [HOMER v4.9.1, deepTools v3.3.0]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: The aligned files were then indexed with SAMtools (v1.19.2), and gene expression levels were quantified using featureCounts.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Germline fate determination by a single ARGONAUTE protein in &lt;i&gt;Ectocarpus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2518712123 | PMCID: PMC12867755 | PMID: 41604268
- Evidence: Gene expression quantification was performed using featureCounts ( 92 ), which counted the number of reads mapped to each gene.
- Full pipeline: quality control [Trimmomatic] -> read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT, STAR, featureCounts] -> quantification [DESeq2, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Version used: **2.0.1**
- Evidence: Anonymized BAM files were downloaded from the Allen Brain Atlas API and were counted using featureCounts (v2.0.1) and GRCh37.p5 reference genome.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Version used: **1.6.0**
- Evidence: Reads were quantified with featureCounts v1.6.0 to generate gene-level feature counts from the read alignment, based on GENCODE GRCh37.p13 gene annotation.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Version used: **1.6.2**
- Evidence: Raw sequencing reads were aligned to the mouse genome (mm39) using STAR 2.7.1a and quantified using featureCounts 1.6.2 ( 111 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: Sequences were mapped to the GRCm38/mm10 reference genome with RSubread, and gene features were quantified with featureCounts.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Poxvirus attack of antiviral defense pathways unleashes an effector-triggered NF-κB response. (Science 2026)

- DOI: 10.1126/science.adw4937 | PMCID: PMC13041778 | PMID: 41678605
- Evidence: Fragment counts were quantified using featureCounts from the Subread (2.0.3) package, and differential gene expression analysis was conducted using DESeq2 (1.42.1).
- Full pipeline: quality control [Cutadapt v1.18, FastQC] -> read trimming [Cutadapt v1.18, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.42.1, featureCounts] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, R]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: The number of reads aligning to genes were counted with featureCounts with the following parameters - B -C -s 0 -t exon , where only reads mapping at least partially inside exons were admitted, and these reads were aggregated per gene.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

