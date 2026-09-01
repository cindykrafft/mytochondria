# Trim Galore

- **Category:** genomics
- **Papers in survey:** 169
- **Journals:** PNAS (79), Nature (74), Cell (12), Science (4)
- **Years:** 2021 (19), 2022 (16), 2023 (26), 2024 (39), 2025 (40), 2026 (29)
- **Versions named:** 0.6.6 (16), 0.6.7 (13), 0.6.10 (8), 0.4.1 (5), 0.4.5 (4), 0.6.5 (4), 0.5.0 (4), 0.6.1 (3), 10.5281 (2), 0.6.4 (2)
- **Pipeline stages it appears in:** read trimming (128), alignment/mapping (42), quality control (41), differential/statistical testing (4), quantification (3), structure determination (1), dimensionality reduction/clustering (1)

## Papers

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **0.5.0**
- Evidence: ...www.graphpad.com/ FlowJo FlowJo 10 https://www.flowjo.com/ Fiji/ImageJ Open Source https://imagej.net/Fiji BioRender BioRender https://biorender.com/ TrimGalore (version 0.5.0) Martin, 2011 https://github.com/FelixKrueger/TrimGalore kallisto (version 0.44.0) Bray et al. , 2016 https://pachterlab.github.io/kallisto/ R Package: tximport (version 1.8.0) Soneson et al., 2015 https://bioconductor.org/p...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Evidence: ...oh and Standley, 2013 iVar 1.2.1 https://github.com/andersen-lab/ivar Grubaugh et al., 2019 Samtools http://samtools.sourceforge.net/ Li et al., 2009 TrimGalore https://github.com/FelixKrueger/TrimGalore https://github.com/FelixKrueger/TrimGalore RAMPART ARTIC Network https://github.com/artic-network/rampart ARTIC Network Bioinformatic protocol ARTIC Network https://artic.network/ncov-2019/ncov201...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Version used: **0.4.2**
- Evidence: Adaptor sequences were removed using Trim Galore (version 0.4.2) ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ), a wrapper script that runs cutadapt (version 1.9.1) to remove the detected adaptor sequence from the reads.
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### An early cell shape transition drives evolutionary expansion of the human forebrain. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.050 | PMCID: PMC8054913 | PMID: 33765444
- Evidence: ...ord Instruments https://imaris.oxinst.com/ MaMuT v0.27.0 Wolff et al., 2018 https://imagej.net/MaMuT PRAGUI MRC LMB https://github.com/lmb-seq/PRAGUI Trim Galore! v0.6.3 Krueger, 2012 https://github.com/FelixKrueger/TrimGalore/releases Cutadapt v2.4 Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ FASTQC v0.11.5 Andrews, 2010 https://github.com/s-andrews/FastQC HISAT2 v2.0.0-beta Kim et al....
- Full pipeline: quality control [Cutadapt v2.4, FastQC, HISAT2 v2.0.0, HTSeq v0.11.2, Trim Galore] -> stage not stated [R v3.5]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: Analysis of single cell RNA sequencing data All sequencing data was assessed to detect sequencing failures using FASTQC and lower quality reads were filtered or trimmed using TrimGalore.
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...et al., 2019 ) https://odelaneau.github.io/shapeit4/ Snakemake - version 4.0 ( Köster and Rahmann, 2012 ) https://snakemake.readthedocs.io/en/stable/ Trim Galore! - version 0.4.3 Babraham Bioinformatics www.bioinformatics.babraham.ac.uk/projects/trim_galore/ Yjasc_3752_ry_compute.py, version 0.4 ( Skoglund et al., 2013 ) https://ars.els-cdn.com/content/image/1-s2.0-S0305440313002495-mmc1.zip Yleaf...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...sva R ( Johnson et al., 2007 ; Leek et al., 2012 ) v3.36.0 Swissprot human Proteome database + SARSCov2 https://www.uniprot.org/ retrieved 17/07/2020 TrimGalore Krueger v0.6.2 https://github.com/FelixKrueger/TrimGalore ttest2 MATLAB https://uk.mathworks.com/help/stats/ttest2.heml UMAP McInnes, Healy, Melville arXiv:1802.03426v2 Velocyto ( La Manno et al., 2018 ) http://velocyto.org/ Vireo ( Huang ...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Version used: **0.4.3**
- Evidence: Single-cell and bulk RNA-seq data analysis Raw fastq reads generated from HiSeq X sequencer were first cleaned using TrimGalore (v0.4.3) ( https://github.com/FelixKrueger/TrimGalore ) to remove the adapter-polluted reads and reads with low sequencing quality.
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Evidence: 10005903 Software and algorithms Trim Galore! v0.0.6 Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk/ projects/trim_galore/ Bowtie2 v2.4.2 Langmead and Salzberg 69 https://github.com/BenLangmead/bowtie2 SAMtools v1.12 Li et al.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: Reads were trimmed of adapters and low quality bases with Trim Galore ( github.com/FelixKrueger/TrimGalore ) and aligned to the P. copri DSM 18205 reference genome (GCF_020735445.1) with the Burrows Wheeler Aligner (default bwa-mem).
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **0.4.1**
- Evidence: This paper https://github.com/SinghLabUCSF/Diapause-multiomics Picard Tools v2.22.1 Broad Institute https://broadinstitute.github.io/picard/ SnapGene v7.0 Dotmatic https://www.snapgene.com/ TrimGalore v0.4.1 Felix Krueger https://www.bioinformatics.babraham.ac.uk/projects/trimgalore/ Fiji v2.0.0-rc-68/1.52h FijiTeam https://fiji.sc/ Ingenuity Pathway Analysis (IPA) QIAGEN https://digitalinsights.q...
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Mapping chromatin structure at base-pair resolution unveils a unified model of cis-regulatory element interactions. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.013 | PMCID: PMC7618578 | PMID: 41197626
- Evidence: 87 Adapter sequences were removed using Trim Galore (Babraham Institiute, v0.3.1), enabling the reconstruction of full-length sequences for >90% of reads.
- Full pipeline: read trimming [Trim Galore] -> quantification [Snakemake] -> differential/statistical testing [Snakemake] -> structure determination [Trim Galore] -> stage not stated [BEDTools, Bowtie2, DESeq2, LAMMPS, MACS2]

### SARS-CoV-2 evolution during treatment of chronic infection. (Nature 2021)

- DOI: 10.1038/s41586-021-03291-y | PMCID: PMC7610568 | PMID: 33545711
- Version used: **0.6.6**
- Evidence: For short-read sequencing, FASTQs were downloaded, poor-quality reads were identified and removed, and both Illumina and PHiX adapters were removed using TrimGalore v0.6.6 25 .
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [MAFFT v7.475] -> stage not stated [BCFtools, IQ-TREE v2.1.2, Nextstrain, Picard, SAMtools v1.11]

### Control of osteoblast regeneration by a train of Erk activity waves. (Nature 2021)

- DOI: 10.1038/s41586-020-03085-8 | PMCID: PMC7864885 | PMID: 33408418
- Version used: **0.4.1**
- Evidence: Gene expression analyses by RNA-Seq Reads were trimmed by Trim Galore (0.4.1, with -q 15 --paired) and then mapped with TopHat 33 (v 2.1.1, with parameters --b2-very-sensitive --no-coverage-search and supplying the UCSC danRer10 refSeq annotation).
- Full pipeline: read trimming [TopHat, Trim Galore v0.4.1] -> alignment/mapping [TopHat, Trim Galore v0.4.1] -> quantification [featureCounts] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> stage not stated [ilastik v1.3.3]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Version used: **0.6.2**
- Evidence: Fastq files were generated with bcl2fastq2 version 2.20 and trimmed using TrimGalore version 0.6.2 to remove low-quality bases, unpaired sequences, and adaptor sequences.
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **0.4.1**
- Evidence: Bisulfite-seq analysis Downloaded sequencing reads 81 were processed using TrimGalore (v.0.4.1) ( https://github.com/FelixKrueger/TrimGalore ) with default parameters.
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Evidence: Raw sequencing fastq files were trimmed with ‘TrimGalore!’ of the adapter, retaining only reads with a minimum length of 25 nt.
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### Prolonged viral suppression with anti-HIV-1 antibody therapy. (Nature 2022)

- DOI: 10.1038/s41586-022-04597-1 | PMCID: PMC9177424 | PMID: 35418681
- Evidence: After, a quality-control check is carried out by Trim Galore package v0.6.4 ( https://github.com/FelixKrueger/TrimGalore ) to trim Illumina adapters and low-quality bases.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [MAFFT v7.487] -> stage not stated [SPAdes v3.13.0]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **0.6.5**
- Evidence: Adapters and low-quality bases (<Q20) were removed using TrimGalore (v.0.6.5) ( https://github.com/FelixKrueger/TrimGalore ) with the parameters ‘-q 20 --trim-n’.
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: Analytical methods WES reads alignment FASTQ files were preprocessed using trimGalore v.0.6.7 (with the parameter --length 36 and all of the other parameters set to default; https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Pervasive downstream RNA hairpins dynamically dictate start-codon selection. (Nature 2023)

- DOI: 10.1038/s41586-023-06500-y | PMCID: PMC10499604 | PMID: 37674078
- Version used: **0.6.6**
- Evidence: Specifically, raw reads were trimmed using Trim Galore v.0.6.6, a wrapper tool of Cutadapt 53 and FastQC 54 .
- Full pipeline: quality control [Cutadapt, FastQC, MultiQC v1.9, Trim Galore v0.6.6] -> read trimming [Bowtie2 v2.4.2, Cutadapt, FastQC, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [AlphaFold, STAR v2.7.8a]

### R-loop-dependent promoter-proximal termination ensures genome stability. (Nature 2023)

- DOI: 10.1038/s41586-023-06515-5 | PMCID: PMC10511320 | PMID: 37557913
- Version used: **0.6.6**
- Evidence: Quantification and statistical analysis ChIP–Rx analysis Raw ChIP–Rx reads were trimmed using Trim Galore v.0.6.6 (Babraham Institute) in paired-end mode.
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [Picard, SAMtools v1.12] -> quantification [Trim Galore v0.6.6] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [Trim Galore v0.6.6] -> stage not stated [ImageJ, MACS2 v2.2.7.1, R]

### GDF15 promotes weight loss by enhancing energy expenditure in muscle. (Nature 2023)

- DOI: 10.1038/s41586-023-06249-4 | PMCID: PMC10322716 | PMID: 37380764
- Evidence: Trim Galore was used to automate quality and adapter trimming as well as quality control.
- Full pipeline: quality control [MultiQC, Trim Galore] -> read trimming [Trim Galore] -> quantification [DESeq2] -> stage not stated [R, TwoSampleMR]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Evidence: FastQC (v.0.11.2) 51 was used for quality control, and Trim Galore!
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: Metagenomics data analysis Pre-processing pipeline An initial quality control step was performed by trimming adapters and low-quality ends from the reads (Trim Galore!
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### Adeno-associated virus 2 infection in children with non-A-E hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05948-2 | PMCID: PMC7617659 | PMID: 36996873
- Evidence: Illumina adapters were trimmed using Trim Galore ( https://github.com/FelixKrueger/TrimGalore ) and then mapped to the human genome using BWA-MEM ( https://github.com/lh3/bwa ).
- Full pipeline: read trimming [BWA, IQ-TREE, Trim Galore] -> alignment/mapping [BWA, IQ-TREE, MAFFT, Trim Galore] -> quantification [QuPath v0.3.2] -> differential/statistical testing [R]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **0.6.6**
- Evidence: Shortly, metagenomic reads were quality-controlled and reads of low quality (quality score <Q20), fragmented short reads (<75 bp), and reads with >2 ambiguous nucleotides were removed with Trim Galore (v0.6.6).
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **0.5.0**
- Evidence: Trim Galore (v.0.5.0) 60 was used to trim sequencing reads, eliminating the remains of Illumina adaptors and discarding reads that were shorter than 20 bp.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Version used: **0.6.6**
- Evidence: Raw reads were trimmed using TrimGalore v.0.6.6 ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Evidence: Adaptor sequences were removed from raw fastq files using Trim Galore at default settings, followed by alignment to the hg38 reference genome using Map with BWA-MEM to generate the BAM files.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Version used: **0.6.4**
- Evidence: In brief, scCircle-seq sequencing reads were 3′ trimmed for quality using Trim Galore (v.0.6.4) 68 , and adapter sequences with reads shorter than 20 nucleotides were removed.
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: Trim Galore!
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: WES data processing FASTQ files were preprocessed using trimGalore (v.0.6.7; with parameters: --length 36 and all other parameters set to default; https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Rifaximin prophylaxis causes resistance to the last-resort antibiotic daptomycin. (Nature 2024)

- DOI: 10.1038/s41586-024-08095-4 | PMCID: PMC11602712 | PMID: 39443798
- Evidence: Raw paired-end reads were quality trimmed using TrimGalore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) (v.0.6.2).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2, HTSeq, MAFFT] -> quantification [Bowtie2, HTSeq] -> differential/statistical testing [tidyverse v1.3.1] -> visualisation [R v4.0.3, tidyverse v1.3.1] -> stage not stated [IQ-TREE v2.1.2, Kraken2]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Version used: **10.5281**
- Evidence: The pipeline performed adapter trimming with Trim Galore (10.5281/zenodo.5127898) and reference-genome alignment with Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **0.4.4**
- Evidence: Processing of single-cell epigenomic data Genomic reads were first trimmed with Trim Galore 0.4.4 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) in paired-end mode, and then mapped to GRCm38 with Bismark 0.22.3 72 in single-end, non-directional mode.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### ILC2-derived LIF licences progress from tissue to systemic immunity. (Nature 2024)

- DOI: 10.1038/s41586-024-07746-w | PMCID: PMC11338826 | PMID: 39112698
- Version used: **0.50**
- Evidence: Sequence data were trimmed to remove adaptors and sequences with a quality score below 30 using Trim Galore (v.0.50, Babraham Bioinformatics) and then aligned to the mouse genome (GRCm38) using STAR (v.2.6.0a); differential expression was calculated using DESeq2 (v.1.18.1).
- Full pipeline: read trimming [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [tidyverse]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Version used: **0.4.0**
- Evidence: Raw reads were trimmed by TrimGalore v.0.4.0 (Babraham Bioinformatics), mapped to mm10 by TopHat v.2.0.13 and analysed by DESeq2.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Reads were trimmed using Trim Galore (Phred score 24) and filtered to remove reads <20 bp.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Nuclear position and local acetyl-CoA production regulate chromatin state. (Nature 2024)

- DOI: 10.1038/s41586-024-07471-4 | PMCID: PMC11168921 | PMID: 38839952
- Evidence: Adapter sequences were trimmed using Trim Galore!
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [MACS2]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **0.4.1**
- Evidence: In brief, reads were processed using Trim Galore (v.0.4.1) or Cutadapt (v.1.9.1) to remove adaptor sequences.
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **0.4.3.1**
- Evidence: RNA-seq quality control and data preparation Raw reads were quality trimmed using Trim Galore (0.4.3.1, -phred33 --quality 20 --stringency 1 -e 0.1 --length 20).
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: In brief, we performed quality control of the fastq files using FastQC and trimmed the filtered reads with Trim Galore software.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### A brain-specific angiogenic mechanism enabled by tip cell specialization. (Nature 2024)

- DOI: 10.1038/s41586-024-07283-6 | PMCID: PMC11041701 | PMID: 38570687
- Version used: **0.4.4**
- Evidence: Adapter sequences were removed using Trim Galore v.0.4.4 before read mapping and doublets were removed using Samtools v.1.16.1 software.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore v0.4.4] -> alignment/mapping [Bowtie2, SAMtools v1.16.1, TopHat v2.1.1, Trim Galore v0.4.4, featureCounts] -> quantification [featureCounts] -> stage not stated [DESeq2 v1.12, ImageJ v1.53c, Seurat]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Version used: **0.6.6**
- Evidence: Read quality was controlled with Fastqc v.0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), and low-quality reads and the adapters were removed using Trim Galore v.0.6.6 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) according to the following parameters: --quality 20, --length 25, --paired.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **0.6.7**
- Evidence: The EM-seq dataset was adapter-timmed by Trim Galore v0.6.7 with the default parameters.
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Evidence: Demultiplexed reads were filtered based on the reverse transcription (RT) index and hairpin ligation adapter index (Levenshtein edit distance (ED) < 2, including insertions and deletions) and adapter-clipped using trim_galore v0.6.5 ( https://github.com/FelixKrueger/TrimGalore ) with default settings.
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: Sequencing reads were trimmed and filtered for quality and adapter content using version 0.4.5 of TrimGalore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore ) and running version 1.15 of cutadapt and version 0.11.5 of FastQC.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: Reads were demultiplexed (bcl2fastq, Illumina), trimmed to remove low-quality bases and processed to remove read-through adapter sequences (Trim Galore 31 , v.0.6.4).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Evidence: Adaptors were trimmed by trimgalore (v.0.6.7; RRID: SCR_011847 ; https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Prime editing-installed suppressor tRNAs for disease-agnostic genome editing. (Nature 2025)

- DOI: 10.1038/s41586-025-09732-2 | PMCID: PMC12675287 | PMID: 41261131
- Evidence: Fastq reads were trimmed of adapter sequences using Trim Galore, aligned to the human genome using STAR, and differential expression analysis was performed using DESeq2 and custom R scripts.
- Full pipeline: read trimming [Bowtie2, DESeq2, STAR, Trim Galore] -> alignment/mapping [Bioconductor, Bowtie2, DESeq2, STAR, Trim Galore] -> differential/statistical testing [DESeq2, STAR, Trim Galore]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: Bioinformatics analysis of iMgl RNA sequencing Raw sequencing reads were first quality checked and trimmed using Trim Galore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ v.0.6.4, a wrapper program implementing Cutadapt v.2.9 ( https://journal.embnet.org/index.php/embnetjournal/article/view/200 ) and FastQC v.0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ )...
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **0.4.1**
- Evidence: Sequencing analysis and mutation calling were performed as described 45 , using the following tools: Python v.2.7.18, TrimGalore v.0.4.1, BWA v.0.7.13, Samtools v.1.9, Picard v.1.119, GenomeAnalysisTK v.3.5, Bcftools v.1.9, and tabix v.0.2.6.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Evidence: CUT&Tag and CUT&RUN bioinformatic analysis CUT&Tag and CUT&RUN sequencing reads were trimmed using the trim-galore tool (v.0.6.10, https://github.com/FelixKrueger/TrimGalore ), which included adapter removal.
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Reads were adapter-trimmed (Trim Galore, Nextera-specific settings, minimum overlap 3 bases), aligned to the human reference genome (GRCh38.p14, GENCODE release 47; STAR aligner), and counted (featureCounts, paired-end settings).
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Version used: **0.6.7**
- Evidence: Sequencing reads were trimmed and filtered for quality control using TrimGalore (v.0.6.7) with a quality setting of 15, Cutadapt 76 (v.4.0) and FastQC v.0.12.1.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Evidence: Fastq files were quality controlled using FastQC v.0.73 and trimmed with Trim Galore! v.0.6.7.
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: Alignment We used Trim Galore to remove adapters and FastQC to generate QC reports before running alignment.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Evidence: Transcriptomes were analysed on the Galaxy platform 59 using Trim Galore! version 0.4.3.1 (developed by Felix Krueger at the Babraham Institute), HISAT2 version 2.1.0 60 and featureCounts version 1.6.1.0 61 . snRNA-seq of thymic tissue The Chromium GEM-X Single Cell 3′ v4 protocol ( CG000731 , Rev B) was followed starting from step 1.1 according to the manufacturer’s guidelines.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Version used: **0.6.10**
- Evidence: Bulk RNA-seq analysis Raw RNA-seq data were filtered and trimmed using TrimGalore v.0.6.10 (10.5281/zenodo.7598955) with the default settings.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Single-cell BS-seq data were trimmed using the TrimGalore!
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Regulation of PV interneuron plasticity by neuropeptide-encoding genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08933-z | PMCID: PMC12222018 | PMID: 40307547
- Evidence: Specifically, sequencing reads were quality-controlled by FastQC (available at https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and quality-trimmed by Trim Galore (available at https://zenodo.org/record/5127899#.Y8fdOi-l3UI ).
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> stage not stated [Nextflow v21.03.0, edgeR]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **0.6.6**
- Evidence: Adapters were trimmed using Trim Galore (0.6.6), and paired-end alignment was performed using Bowtie2 (2.4.4).
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: Bulk ATAC-seq analysis The Nextera transposase adaptors were removed from the fastq files by trimming them with the --phred33 --paired --fastqc options using trim_galore 75 ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **0.6.7**
- Evidence: Metagenomic read preprocessing and taxonomy profiling Metagenomic reads were deduplicated using HTStream SuperDeduper v.1.3.3 with default parameters, trimmed using TrimGalore v.0.6.7 with a minimum quality score of 30 and a minimum read length of 60.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **0.6.10**
- Evidence: The resulting reads were quality controlled using FastQC v.0.11.8 and Trim Galore v.0.6.10, and mapped to M. truncatula v5 genome (MtrunA17r5.0-ANR) using STAR v.2.5.a.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Evidence: The resulting reads were trimmed for adaptors and low-quality base calls using Trim Galore!
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **0.6.7**
- Evidence: To process the raw data, Trim Galore (v0.6.7) was used with the following parameters: ‘--quality 20 --fastqc --length 20 --stringency 1’.
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Version used: **0.4.5**
- Evidence: Adaptors and low-quality bases were removed with TrimGalore (v0.4.5).
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Evidence: Sequencing reads were trimmed to remove adapter sequences and low-quality bases using Trim Galore! v0.6.10.
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: Analyses of RNA-seq data Raw RNA-seq reads were trimmed with Trim Galore, available at https://github.com/FelixKrueger/TrimGalore/ , using the command trim_galore --quality 30 --length 60 --paired {sample}1.fq.gz {sample}_2.fq.gz --retain_unpaired.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Evidence: Briefly, FASTQ files underwent quality control (FastQC v.0.12.1), adaptors were trimmed (Trim Galore! v.0.6.7), reads were aligned to the GRCh38 human reference transcriptome (STAR v.2.7.9a) and a gene expression matrix was generated (Salmon v.1.10.1).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### An enteric neuron ionotropic receptor regulates salt stress resistance. (Nature 2026)

- DOI: 10.1038/s41586-026-10348-3 | PMCID: PMC13293861 | PMID: 41922765
- Version used: **10.5281**
- Evidence: Sequencing reads were adapter trimmed using Trim Galore (10.5281/zenodo.7598955), mapped to the WBcel235 C. elegans genome, and counted using STAR 71 with alignMatesGapMax 2500.
- Full pipeline: read trimming [Trim Galore v10.5281] -> alignment/mapping [IMOD, Trim Galore v10.5281] -> structure determination [IMOD] -> stage not stated [Python]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Evidence: RNA-seq analysis Quality control and adaptor sequences were removed from fastq file using Trim Galore!
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **0.6.5**
- Evidence: Specifically, FastQC (v.0.11.9; https://www.bioinformatics.babraham.ac.uk/projects/fastqc ) was used for quality control of the FastQ data followed by adapter trimming using Trim Galore (v.0.6.5) ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **0.6.6**
- Evidence: In brief, metagenomic reads were quality-controlled and reads of low quality (quality score <Q20), short reads (<75 bp) and reads with >2 ambiguous nucleotides were removed with Trim Galore (v0.6.6).
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Version used: **0.6.7**
- Evidence: Analysis of EM-Seq data was done as described previously using the Trim Galore (0.6.7), cutadapt (1.18) and Bismarck (v0.23.0) software packages 19 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### CFAP20 salvages arrested RNAPII from the path of co-directional replisomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09943-7 | PMCID: PMC12935552 | PMID: 41535461
- Version used: **0.6.5**
- Evidence: Sequences were trimmed using TrimGalore (v.0.6.5) and aligned to hg38 using STAR (v.2.7.7a) with the genome file GCA_000001405.15_GRCh38.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.7a, Trim Galore v0.6.5] -> alignment/mapping [BWA v0.7.17, STAR v2.7.7a, Trim Galore v0.6.5] -> quantification [AlphaFold] -> stage not stated [HOMER, SAMtools v1.11]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Analysis of bulk RNA-seq of stimulated fibroblasts Raw FASTQ reads were processed using FastQC 70 , Trim Galore ( https://github.com/FelixKrueger/TrimGalore ) and SortMeRNA 71 to remove low-quality reads, adaptors and ribosomal RNA.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Version used: **0.5.0**
- Evidence: Specifically, we trimmed the adapter sequence with TrimGalore (v0.5.0) 72 , aligned to the hg19 reference with Bowtie2 (v2.3.4.1) 73 , filtered duplicates with MACS3 (v3.0.3) 74 and called narrow peaks with the MACS3 (v3.0.3) hmmratac command.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Evidence: Paired-end RNA sequencing reads were trimmed to remove adaptor sequences using TrimGalore!
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Version used: **0.6**
- Evidence: Adapters with low-quality ends were trimmed from FASTQ files using Trim Galore (v.0.6) and quality analysis performed using FastQC (v.0.11.2).
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **0.6.6**
- Evidence: Demultiplexed paired-end FASTQ files were converted to unaligned BAM format using Picard’s FastqToSam tool (v.3.0.0) and trimmed using Trim Galore (v.0.6.6) in paired-end mode with Nextera adapter trimming enabled.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **0.6.7**
- Evidence: In short, reads were deduplicated using HTStream SuperDeduper (v.1.3.3), and low-quality bases were trimmed using TrimGalore (v.0.6.7).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Evidence: In brief, unique molecular identifiers were appended to each paired-end read using umi_tools extract 54 and trimmed using trim_galore ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: Sequences were subsequently trimmed to remove adaptor sequences and low-quality base calls, defined by a Phred score of less than 20, using the Trim Galore tool (v0.6.4).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Quantitative assessment reveals the dominance of duplicated sequences in germline-derived extrachromosomal circular DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2102842118 | PMCID: PMC8617514 | PMID: 34789574
- Version used: **0.6.1**
- Evidence: The sequencing reads were trimmed using Trim Galore (v.0.6.1) and Cut Adapt (v2.3) to remove adapters and subsequently aligned to the University of Santa Cruz (UCSC) hg38 human reference genome or mm10 mouse reference genome using Bowtie 2 (v2.3.5).
- Full pipeline: read trimming [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> alignment/mapping [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> stage not stated [RepeatMasker, SAMtools]

### Emergent RNA-RNA interactions can promote stability in a facultative phototrophic endosymbiosis. (PNAS 2021)

- DOI: 10.1073/pnas.2108874118 | PMCID: PMC8463893 | PMID: 34521754
- Evidence: The raw paired-end reads from the RNA-seq libraries were trimmed using Trim Galore in order to remove barcodes (4-nt from each 3′- and 5′-end) and sRNA adaptors, with additional settings of a phred-score quality threshold of 20 and minimum length of 16-nt.
- Full pipeline: quality control [FastQC] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2] -> quantification [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [BLAST]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **0.6.5**
- Evidence: RNA-seq reads were adapter- and quality-trimmed using TrimGalore v0.6.5 with default options (Phred quality threshold 20; adapter auto-detection) ( 83 , 84 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### High frequency of an otherwise rare phenotype in a small and isolated tiger population. (PNAS 2021)

- DOI: 10.1073/pnas.2025273118 | PMCID: PMC8488692 | PMID: 34518374
- Evidence: Identifying the Causal Mutation We trimmed the whole-genome sequences using TrimGalore ( 97 ) for a quality threshold of 30 on the phred33 scale with a stringency value of 3.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [BCFtools, BWA] -> variant calling [GATK, VCFtools] -> stage not stated [Picard]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Evidence: Raw reads were preprocessed and quality filtered using Trim Galore!
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Evidence: Adapter sequences and low-quality reads were removed from raw reads with trimGalore v0.6.4 ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Amino acids activate mTORC1 to release roe deer embryos from decelerated proliferation during diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2100500118 | PMCID: PMC8536382 | PMID: 34452997
- Evidence: Adaptors were clipped, sequences shorter than 50 bp were removed, and a low-quality end score of 30 was applied with the Trim Galore! tool.
- Full pipeline: quality control [FastQC, MultiQC] -> differential/statistical testing [FastQC, MultiQC, R] -> stage not stated [Galaxy, Trim Galore]

### Transposon-mediated insertional mutagenesis unmasks recessive insecticide resistance in the aphid <i>Myzus persicae</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100559118 | PMCID: PMC8201860 | PMID: 34074777
- Version used: **0.4.5**
- Evidence: The quality of the reads obtained was assessed using FASTQC version 0.11.5 ( 48 ) and adaptor sequences and low-quality base calls removed using TrimGalore 0.4.5 ( 49 ).
- Full pipeline: quality control [FastQC, Trim Galore v0.4.5] -> read trimming [FastQC] -> alignment/mapping [HISAT2 v2.1.0, HTSeq] -> differential/statistical testing [edgeR v3.9] -> stage not stated [MUSCLE v3.8]

### Small noncoding RNA profiling across cellular and biofluid compartments and their implications for multiple sclerosis immunopathology. (PNAS 2021)

- DOI: 10.1073/pnas.2011574118 | PMCID: PMC8092379 | PMID: 33879606
- Evidence: CSF cells total RNA libraries ( n = 17) were preprocessed with TrimGalore, mapped with STAR against hg38, and annotated using featureCounts with Ensemble GRCh38.
- Full pipeline: alignment/mapping [Trim Galore, featureCounts] -> differential/statistical testing [DESeq2, limma] -> stage not stated [BEDTools]

### Primate innate immune responses to bacterial and viral pathogens reveals an evolutionary trade-off between strength and specificity. (PNAS 2021)

- DOI: 10.1073/pnas.2015855118 | PMCID: PMC8020666 | PMID: 33771921
- Version used: **0.2.7**
- Evidence: Following sequencing, we trimmed Illumina adapter sequence from the ends of the reads and removed bases with quality scores <20 using Trim Galore (version 0.2.7).
- Full pipeline: read trimming [Trim Galore v0.2.7] -> alignment/mapping [HTSeq] -> normalisation [limma] -> differential/statistical testing [R v3.6.2, limma] -> stage not stated [Cytoscape v3.7.2]

### A genome-scale CRISPR screen reveals factors regulating Wnt-dependent renewal of mouse gastric epithelial cells. (PNAS 2021)

- DOI: 10.1073/pnas.2016806118 | PMCID: PMC7848749 | PMID: 33479180
- Evidence: Sequence reads were trimmed and quality-filtered using Trim Galore!
- Full pipeline: read trimming [Cutadapt v1.16, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.2b] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [featureCounts v1.6.1]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Version used: **0.6.1**
- Evidence: Reads were filtered and trimmed using Trim Galore version 0.6.1 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Siponimod ameliorates metabolic oligodendrocyte injury via the sphingosine-1 phosphate receptor 5. (PNAS 2022)

- DOI: 10.1073/pnas.2204509119 | PMCID: PMC9546621 | PMID: 36161894
- Version used: **0.6.6**
- Evidence: Adapter and quality trimming was performed using TrimGalore v.0.6.6 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ).
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [STAR v2.6.1d]

### Different classes of genomic inserts contribute to human antibody diversity. (PNAS 2022)

- DOI: 10.1073/pnas.2205470119 | PMCID: PMC9457163 | PMID: 36037353
- Evidence: For suppression of PCR bioinformatics analysis, 300-nt paired-end (PE) reads were trimmed to remove adapters and poor-quality base calls using Trim Galore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ , v0.4.3, parameters –nextera –paired -q 20 –length 100).
- Full pipeline: quality control [FastQC] -> read trimming [R, Trim Galore, Trimmomatic] -> alignment/mapping [R, Trimmomatic] -> stage not stated [BEDTools, MACS2, ggplot2]

### Orchestrated translation specializes dinoflagellate metabolism three times per day. (PNAS 2022)

- DOI: 10.1073/pnas.2122335119 | PMCID: PMC9335273 | PMID: 35858433
- Evidence: The sequences in fastq format produced by the sequencing reaction were trimmed in Galaxy to remove the adapters using TrimGalore ( SI Appendix , Fig.
- Full pipeline: read trimming [Trim Galore] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [R]

### In situ structure of intestinal apical surface reveals nanobristles on microvilli. (PNAS 2022)

- DOI: 10.1073/pnas.2122249119 | PMCID: PMC9214534 | PMID: 35666862
- Evidence: According to the results of FastQC, adaptors or low-quality nucleotides were trimmed by Trim Galore (version [v] 0.5.2) using default parameters.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [IMOD, STAR v2.6.0c] -> stage not stated [ImageJ, MotionCor2, UCSF Chimera]

### Enzymes degraded under high light maintain proteostasis by transcriptional regulation in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121362119 | PMCID: PMC9171785 | PMID: 35549553
- Evidence: Trim Galore!
- Full pipeline: quality control [FastQC v0.11.7] -> alignment/mapping [SAMtools v1.3.1, featureCounts] -> differential/statistical testing [edgeR] -> stage not stated [Trim Galore]

### Signaling from the RNA sensor RIG-I is regulated by ufmylation. (PNAS 2022)

- DOI: 10.1073/pnas.2119531119 | PMCID: PMC9169834 | PMID: 35394863
- Evidence: RNA-seq data were processed using the TrimGalore toolkit ( 65 ), which employs Cutadapt ( 66 ) to trim low-quality bases and Illumina sequencing adapters from the 3′ end of the reads.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [HTSeq]

### A multiomic study uncovers a bZIP23-PER1A-mediated detoxification pathway to enhance seed vigor in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2026355119 | PMCID: PMC8892333 | PMID: 35217598
- Evidence: Reads were trimmed using Trim Galore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) and mapped to the Nipponbare reference using the Hierarchical Indexing for Spliced Alignment of Transcripts program.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [Cytoscape v3.6] -> stage not stated [R, featureCounts]

### Loss of TET reprograms Wnt signaling through impaired demethylation to promote lung cancer development. (PNAS 2022)

- DOI: 10.1073/pnas.2107599119 | PMCID: PMC8832965 | PMID: 35110400
- Version used: **0.5.0**
- Evidence: First, the raw pair-end RNA-seq FASTQ (a format file that is mostly used to store short-read data from high-throughput sequencing) data were trimmed to remove low-quality bases and adaptor sequences by Trim Galore (v0.5.0) with default settings.
- Full pipeline: read trimming [Trim Galore v0.5.0] -> stage not stated [DESeq2, Picard v2.21.2, RepeatMasker, SAMtools v1.4]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: Trim Galore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) was used to remove low-quality bases and to trim adaptor sequences.
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### Longitudinal clonal dynamics of HIV-1 latent reservoirs measured by combination quadruplex polymerase chain reaction and sequencing. (PNAS 2022)

- DOI: 10.1073/pnas.2117630119 | PMCID: PMC8794825 | PMID: 35042816
- Evidence: A quality-control check was performed with Trim Galore package v0.6.4 ( https://github.com/FelixKrueger/TrimGalore ) to trim Illumina adapters and low-quality bases.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [RAxML v8.2.11] -> structure determination [SPAdes v3.13.1]

### A dicer-related helicase opposes the age-related pathology from SKN-1 activation in ASI neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2308565120 | PMCID: PMC10756303 | PMID: 38113255
- Evidence: Quality trimming and Adapter sequences were trimmed from raw paired end reads using Trim Galore package v 0.6.4.
- Full pipeline: read trimming [STAR v2.7.6a, Trim Galore] -> alignment/mapping [STAR v2.7.6a] -> quantification [DESeq2, R v3.5.2] -> differential/statistical testing [DESeq2, R v3.5.2] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.7.1, SAMtools v1.10]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **0.6.6**
- Evidence: All Illumina reads were trimmed with a quality threshold of 20 and reads shorter than 50 bp and adapters were removed using Trim Galore v0.6.6 ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: Low-quality bases, short length, and adaptor sequences in all single-cell BS-seq and bulk BS-seq data were trimmed off using TrimGalore-0.4.5 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ , parameters: –fastqc –paired –phred33 –retain_unpaired –clip_R1 9 –clip_R2 9).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Version used: **0.6.6**
- Evidence: Raw sequencing reads in FASTQ format were quality trimmed, and adapters were removed using Trim Galore (v.0.6.6) ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Endothelial deletion of EPH receptor A4 alters single-cell profile and Tie2/Akap12 signaling to preserve blood-brain barrier integrity. (PNAS 2023)

- DOI: 10.1073/pnas.2204700120 | PMCID: PMC10576133 | PMID: 37796990
- Evidence: Using TrimGalore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ), reads which passed a mean quality filter of 30 and with lengths greater than 30 were retained for downstream analysis.
- Full pipeline: quality control [FastQC, Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Trim Galore, scDblFinder]

### Structure of pre-miR-31 reveals an active role in Dicer-TRBP complex processing. (PNAS 2023)

- DOI: 10.1073/pnas.2300527120 | PMCID: PMC10523476 | PMID: 37725636
- Evidence: The resulting sequencing reads were adapter trimmed using Trim Galore and aligned using bowtie2 (“bowtie2–local–no-unal–no-discordant–no-mixed–phred33 40 -L 12”).
- Full pipeline: read trimming [Bowtie2, Trim Galore] -> alignment/mapping [Bowtie2, Trim Galore] -> quantification [ImageJ]

### Tet2 deletion in CD4+ T cells disrupts Th1 lineage commitment in memory cells and enhances T follicular helper cell recall responses to viral rechallenge. (PNAS 2023)

- DOI: 10.1073/pnas.2218324120 | PMCID: PMC10483640 | PMID: 37639586
- Evidence: Adapters were trimmed from the sequencing reads using Trim Galore! v0.4.4 using options (trim_galore -o $OUTDIR --fastqc --paired $FORWARD_READS $REVERSE_READS).
- Full pipeline: quality control [FastQC v0.11.4, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark, Bowtie2, DESeq2 v1.30.1, featureCounts v1.6.3] -> differential/statistical testing [DESeq2 v1.30.1, featureCounts v1.6.3] -> stage not stated [BEDTools]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **0.6.7**
- Evidence: To compare the transcriptomic profiles of A on B off and “solo” transformants relative to WT, 50-base single-end Illumina reads were filtered and trimmed with Trim Galore v0.6.7 and mapped with STAR v.2.7.4a to a reference genome combining the M. furfur CBS14141 nuclear genome and the a1 - NEO - b4 transgene sequence.
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Version used: **0.6.7**
- Evidence: For the second run, RNA-seq data from 102 libraries were downloaded from the NCBI ( SI Appendix , Table S3 ), trimmed using TrimGalore v0.6.7 ( 87 ) and aligned against the unaligned pangenome using hisat2 v2.2.1 ( 88 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Version used: **0.6.6**
- Evidence: Raw reads of poor quality were trimmed or filtered, using the Trim Galore (v0.6.6) program ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore ).
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### Osteolectin increases bone elongation and body length by promoting growth plate chondrocyte proliferation. (PNAS 2023)

- DOI: 10.1073/pnas.2220159120 | PMCID: PMC10235998 | PMID: 37216542
- Version used: **0.6.4**
- Evidence: Raw reads were trimmed using TrimGalore 0.6.4 and mapped to the Ensembl GRCh38 mouse reference genome version 100 using Bowtie 2.4.1.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bowtie2 v4.1, Trim Galore v0.6.4] -> alignment/mapping [Bowtie2 v4.1, SAMtools v1.12, Trim Galore v0.6.4] -> stage not stated [deepTools v3.5.1]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Evidence: FASTQ dataset quality was assessed by FASTQC v0.11.9 and reads processed by TrimGalore!
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Genome editing in plants using the compact editor CasΦ. (PNAS 2023)

- DOI: 10.1073/pnas.2216822120 | PMCID: PMC9942878 | PMID: 36652483
- Evidence: Reads were first quality and adaptor trimmed using Trim Galore and then mapped to the target genomic region by the BWA aligner (v0.7.17, BWA-MEM algorithm).
- Full pipeline: read trimming [BWA v0.7.17, Trim Galore] -> alignment/mapping [BWA v0.7.17, Trim Galore] -> stage not stated [GATK v4.2.0.0, R, Strelka v2.9.2]

### Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase. (PNAS 2024)

- DOI: 10.1073/pnas.2423270121 | PMCID: PMC11670102 | PMID: 39689177
- Version used: **0.6.10**
- Evidence: Raw paired-end reads were adapter-trimmed using Trim Galore (version 0.6.10) ( 47 ) and then mapped to the hg38 genome and deduplicated using Bismark Bisulfite Mapper (version 0.24.2) ( 48 ).
- Full pipeline: quality control [ArchR, UMAP] -> read trimming [Bismark, Python, Trim Galore v0.6.10, Trimmomatic v0.39] -> alignment/mapping [Bismark, Trim Galore v0.6.10, Trimmomatic v0.39] -> dimensionality reduction/clustering [ArchR, UMAP]

### Characterization of the enzyme for 5-hydroxymethyluridine production and its role in silencing transposable elements in dinoflagellates. (PNAS 2024)

- DOI: 10.1073/pnas.2400906121 | PMCID: PMC11572971 | PMID: 39508766
- Version used: **0.6.7**
- Evidence: The bioinformatic analyses were conducted as follows: Raw DIP-seq and 5hmU-chemical-seq data were first processed using TrimGalore (version 0.6.7) to remove adapters and low-quality bases (--quality 25 --stringency 3).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.2.5, HOMER, STAR v2.7.10a] -> quantification [HOMER] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [deepTools v3.5.5, featureCounts v1.5.3]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: Low-quality reads and sequencing adapters from raw data were removed with Trim Galore! software ( https://github.com/FelixKrueger/TrimGalore ) .
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Spaceflight-induced contractile and mitochondrial dysfunction in an automated heart-on-a-chip platform. (PNAS 2024)

- DOI: 10.1073/pnas.2404644121 | PMCID: PMC11459163 | PMID: 39312653
- Evidence: The sequencing data were preprocessed using Trim Galore ( 85 ) to remove the adapter regions and reads with mean base Phred scores below 30.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [ImageJ]

### Genetic variation drives cancer cell adaptation to ECM stiffness. (PNAS 2024)

- DOI: 10.1073/pnas.2403062121 | PMCID: PMC11441511 | PMID: 39302966
- Evidence: The TrimGalore package was used to filter out reads with a phred33 quality score below 30 ( 61 ).
- Full pipeline: read trimming [Bismark] -> alignment/mapping [Bismark] -> differential/statistical testing [R v4.1.3, edgeR] -> stage not stated [GSEA v4.1.0, ImageJ, Trim Galore]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **0.6.7**
- Evidence: ...fastq --bc-pattern=NNNNNNNNNNCCCCCCCCC.” Adaptor and low-quality sequences were removed, and reads with a length less than 20 bp were discarded using TrimGalore (v0.6.7; http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Transdifferentiation occurs without resetting development-specific DNA methylation, a key determinant of full-function cell identity. (PNAS 2024)

- DOI: 10.1073/pnas.2411352121 | PMCID: PMC11441492 | PMID: 39292740
- Evidence: Low-quality bases and sequencing adaptors of raw fastq files RNA-seq containing single-end 61 bp-long reads were trimmed using Trim Galore (V 0.6.0, https://github.com/FelixKrueger/TrimGalore ) and then mapped to the mm10 reference genome using HISAT2 (V 2.1.0) with default parameters.
- Full pipeline: read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, SAMtools, Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, R]

### Machine learning reveals the transcriptional regulatory network and circadian dynamics of &lt;i&gt;Synechococcus elongatus&lt;/i&gt; PCC 7942. (PNAS 2024)

- DOI: 10.1073/pnas.2410492121 | PMCID: PMC11420160 | PMID: 39269777
- Evidence: Next, Trim Galore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) was applied with default options for read trimming, followed by FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore, featureCounts] -> read trimming [FastQC, Trim Galore] -> quantification [MultiQC, featureCounts] -> dimensionality reduction/clustering [STRING db] -> stage not stated [scikit-learn]

### Alloreactive memory CD4 T cells promote transplant rejection by engaging DCs to induce innate inflammation and CD8 T cell priming. (PNAS 2024)

- DOI: 10.1073/pnas.2401658121 | PMCID: PMC11348247 | PMID: 39136987
- Evidence: Briefly, adapter sequences and low-quality reads were filtered and trimmed using FastQ and Trim Galore Filtered reads were mapped to the mouse GRCm39 reference genome using STAR ( 10.1093/bioinformatics/bts635 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2, limma] -> differential/statistical testing [DESeq2, R] -> visualisation [limma] -> stage not stated [fgsea]

### m&lt;sup&gt;6&lt;/sup&gt;A modification plays an integral role in mRNA stability and translation during pattern-triggered immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2411100121 | PMCID: PMC11331096 | PMID: 39116132
- Evidence: Raw reads were trimmed to remove adaptors and poly(A) sequences by using Trim Galore ( 52 ), and then mapped to the Arabidopsis genome TAIR10 by using the STAR RNA sequencing aligner ( 53 ).
- Full pipeline: read trimming [STAR, Trim Galore] -> alignment/mapping [Bowtie2, STAR, Trim Galore] -> variant calling [Bioconductor] -> normalisation [Bioconductor, DESeq2, HTSeq]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: We performed adapter and quality trimming using Trim Galore! v0.6.6 ( 79 ) with settings –length 50 -q 10 –stringency 1 -e 0.1.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: Sequenced fastq files were qualified and trimmed with TrimGalore.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Evidence: Raw read quality was assessed using FastQC ( 79 ), and reads were trimmed with TrimGalore!
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### Coordination of rhythmic RNA synthesis and degradation orchestrates 24- and 12-h RNA expression patterns in mouse fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2314690121 | PMCID: PMC10873638 | PMID: 38315868
- Evidence: We further used TrimGalore ( 76 ) to remove adapter sequences and remove reads of low quality (<Q20), which we found to be about 0.2% per file.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, STAR v2.7.7a] -> quantification [HOMER] -> visualisation [SAMtools v1.11] -> stage not stated [DESeq2 v1.32.0, R]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Version used: **0.6.7**
- Evidence: Reads were filtered and Illumina adaptors removed using Trim Galore (v 0.6.7, Babraham Institute).
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Core microRNAs regulate neural crest delamination and condensation in the developing trigeminal ganglion. (PNAS 2025)

- DOI: 10.1073/pnas.2517668122 | PMCID: PMC12704738 | PMID: 41329730
- Evidence: Adapter trimming and low-quality reads filtering was performed with TrimGalore using default parameters (v0.6.10; https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [ComplexHeatmap v2.6.2] -> stage not stated [ImageJ v1.53, STRING db]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Version used: **0.4.5**
- Evidence: Sequences were quality trimmed and filtered using Trim Galore (v0.4.5) and cutadapt (v1.15), then trimmed reads were filtered for rRNA by the SortMeRNA ( 91 ) program, and de novo assembled into transcripts using the Trinity program ( 92 ) (v2.8.4).
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### An ADAR2-mimic base editor for efficient C-to-U RNA editing in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2505269122 | PMCID: PMC12625888 | PMID: 41196347
- Version used: **0.6.10**
- Evidence: The quality control of sequencing data was conducted by using FastQC (v.0.12.1), and quality trimming was conducted by Trim Galore (v.0.6.10).
- Full pipeline: quality control [FastQC v0.12.1, Trim Galore v0.6.10] -> read trimming [FastQC v0.12.1, HISAT2, Trim Galore v0.6.10] -> alignment/mapping [HISAT2] -> stage not stated [SAMtools v1.21, SnpEff v5.2]

### Global profiling of polyketide synthases in facultative multicellular eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2515852122 | PMCID: PMC12625978 | PMID: 41191498
- Evidence: 3.12.0) automatically performs quality control using FastQC, followed by read trimming with Trim Galore.
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> machine learning [Cellpose] -> visualisation [R, clusterProfiler] -> stage not stated [TrackMate]

### Genetic dissection of nonconventional introns reveals codominant noncanonical splicing code in &lt;i&gt;Euglena&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509937122 | PMCID: PMC12501133 | PMID: 40986342
- Evidence: For the assembly of short reads, Illumina reads were first trimmed to remove low-quality bases using Trim Galore ( https://github.com/FelixKrueger/TrimGalore ) with default parameters.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BLAST, HMMER, ImageJ]

### Aphid herbivory on macrophytes drives adaptive evolution in an aquatic community via indirect effects. (PNAS 2025)

- DOI: 10.1073/pnas.2502742122 | PMCID: PMC12403121 | PMID: 40838887
- Version used: **0.6.1**
- Evidence: Raw data were quality-checked and trimmed using TrimGalore v0.6.1 ( 29 ), and reads were mapped toward the D. magna reference genome ( 30 ) using BWA ( 31 ) and SAMtools ( 32 ).
- Full pipeline: quality control [BWA, SAMtools, Trim Galore v0.6.1] -> read trimming [BWA, SAMtools, Trim Galore v0.6.1] -> alignment/mapping [BWA, SAMtools, Trim Galore v0.6.1] -> differential/statistical testing [lme4]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Version used: **0.4.5**
- Evidence: We performed quality control and removed adapter sequences in reads using FastQC v0.11.7 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and Trim Galore v0.4.5 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ), respectively.
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### Germline variants in &lt;i&gt;UHRF1&lt;/i&gt; are associated with multilocus imprinting disturbance in humans and mice. (PNAS 2025)

- DOI: 10.1073/pnas.2505884122 | PMCID: PMC12403135 | PMID: 40825131
- Evidence: Then, adapter removal and low base quality filtering were performed with Trim_galore (--paired -a AGATCGGAAGAGC -a2 AAATCAAAAAAAC -q 20) ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: quality control [Bismark, FastQC] -> read trimming [Bismark, FastQC, Trim Galore] -> alignment/mapping [Bismark, GATK v3.7, SAMtools v1.3.1] -> variant calling [GATK v3.7, SAMtools v1.3.1] -> stage not stated [ANNOVAR, VEP]

### Genomic origins and evolution of neo-sex chromosomes in Pacific Island birds. (PNAS 2025)

- DOI: 10.1073/pnas.2503746122 | PMCID: PMC12337287 | PMID: 40720643
- Version used: **0.6.2**
- Evidence: For each Myzomela species, we mapped trimmed (TrimGalore v.0.6.2; Q30) short-read data from a single male ( M. cardinalis: CA114, M. tristrami TA590) and a single female ( M. cardinalis: CA886, genome strain, M. tristrami: TA662, genome strain) to the raw hifiasm assemblies using bwa (v0.7.17; ref.
- Full pipeline: read trimming [Trim Galore v0.6.2, hifiasm] -> alignment/mapping [Trim Galore v0.6.2, hifiasm] -> stage not stated [BUSCO v5.2.2, R, RepeatMasker v4.1.2, SAMtools v1.11, minimap2 v2.26]

### Gibberellin-deactivating GA2OX enzymes act as a hub for auxin-gibberellin cross talk in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; root growth regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2425574122 | PMCID: PMC12318176 | PMID: 40694327
- Evidence: Rough reads were quality-filtered using Rcorrector and Trim Galore scripts ( 62 ).
- Full pipeline: quality control [R] -> differential/statistical testing [R] -> visualisation [R] -> stage not stated [ImageJ, Trim Galore]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: RNA sequencing raw data were subject to quality control and filtration to obtain clean data using Trim Galore.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **0.6.7**
- Evidence: RNASeq raw reads from all described conditions were mapped against the genome of M. paleacea ( 18 ) and counted using the Nextflow v23.10.0 ( 77 ) pipeline NF-CORE/RNASeq v3.14 ( 78 ) with the options star_salmon to align and quantify reads, as well as “-nextseq 30 -length 50” as extra parameters of TrimGalore v0.6.7 ( 79 ) to remove reads with quality lower than 30 or a length lower than 50 bp.
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: High-throughput sequencing data were quality filtered using Trim Galore (Version 0.6.7).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Natural dispersal is better than translocation for reducing risks of inbreeding depression in eastern black rhinoceros (&lt;i&gt;Diceros bicornis michaeli&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2414412122 | PMCID: PMC12167989 | PMID: 40460127
- Evidence: The raw FASTQ reads obtained from the Illumina platform were end trimmed using default settings of Trim Galore for Illumina ( https://github.com/FelixKrueger/TrimGalore ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [SAMtools] -> variant calling [BCFtools] -> differential/statistical testing [emmeans] -> stage not stated [ADMIXTURE, PLINK v1.9, R, VCFtools]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Version used: **0.6.6**
- Evidence: Trimmed, paired-end, 150-bp reads were generated using Trim Galore (version 0.6.6, https://github.com/FelixKrueger/TrimGalore ) and aligned to the TAIR10 reference genome using HISAT2 (version 2.2.1, https://daehwankimlab.github.io/hisat2 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### The NAE1-mediated neddylation operates as an essential post-translational modification checkpoint for effector CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424061122 | PMCID: PMC11912420 | PMID: 40030035
- Version used: **0.6.10**
- Evidence: The resulting raw reads were trimmed by Trim Galore v0.6.10 and aligned to reference genome mm10 with HISAT2 V2.2.1 in combination with Samtools V1.2.
- Full pipeline: read trimming [HISAT2, SAMtools, Trim Galore v0.6.10] -> alignment/mapping [HISAT2, SAMtools, Trim Galore v0.6.10] -> stage not stated [DESeq2, GSEA, pheatmap]

### Abscisic acid signaling gates salt-induced responses of plant roots. (PNAS 2025)

- DOI: 10.1073/pnas.2406373122 | PMCID: PMC11831169 | PMID: 39908104
- Evidence: First read quality was analyzed with FastQC ( 56 ) and MultiQC ( 57 ) packages in Python 2.7, followed by trimming of low quality reads with Trim Galore!
- Full pipeline: quality control [FastQC, MultiQC, Python v2.7, Trim Galore] -> read trimming [FastQC, MultiQC, Python v2.7, Trim Galore] -> alignment/mapping [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, R] -> stage not stated [OpenCV v4.5.1.48]

### The androgen clock is an epigenetic predictor of long-term male hormone exposure. (PNAS 2025)

- DOI: 10.1073/pnas.2420087121 | PMCID: PMC11760496 | PMID: 39805019
- Evidence: Raw sequencing data were trimmed using Trim Galore!
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bismark v0.14.3] -> stage not stated [R]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Evidence: ...(v2.25.7), salmon ( 60 ) (v1.5.2), samtools ( 61 ) (v1.13), star ( 62 ) (v2.6.1d), stringtie ( 63 ) (v2.1.7), Trimgalore (v0.6.7, GitHub—FelixKrueger/TrimGalore: A wrapper around Cutadapt and FastQC to consistently apply adapter and quality trimming to FastQ files, with extra functionality for RRBS data), cutadapt ( 64 ) (v3.4) and ucsc (v377).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### Virus-induced transgene- and tissue culture-free heritable genome editing in tomato. (PNAS 2026)

- DOI: 10.1073/pnas.2530029123 | PMCID: PMC13250589 | PMID: 42241111
- Evidence: Single-end reads were processed by adapter trimming with Trim Galore using default parameters, and the resulting reads were aligned to the target genomic region with BWA (v0.7.17) employing the BWA-MEM algorithm.
- Full pipeline: read trimming [BWA v0.7.17, Trim Galore] -> alignment/mapping [BWA v0.7.17, Trim Galore] -> stage not stated [R]

### WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2534844123 | PMCID: PMC13099603 | PMID: 41984841
- Evidence: For ChIP-seq analysis, raw single-end reads were trimmed with Trim Galore! and aligned to the human reference genome (hg38) using HISAT2, retaining only uniquely mapped reads with mapping quality ≥10.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, Trim Galore] -> quantification [deepTools] -> normalisation [deepTools] -> differential/statistical testing [DESeq2 v1.28.1, R] -> stage not stated [GSEA, SAMtools]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Evidence: Quality control was applied to ChIP raw sequencing data using FastQC v0.11.9 ( 49 ), followed by trimming adaptors and low-quality reads with Trim Galore! v0.6.7 ( 50 ).
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Version used: **0.6.10**
- Evidence: Paired-end reads were quality-filtered using Trim Galore v.0.6.10 ( 60 ) to trim, remove adapter content, and to ensure a minimum PHRED score of 30 and length of at least 120 bp.
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### DNA methylation in invertebrate genomes and cell lineage plasticity. (PNAS 2026)

- DOI: 10.1073/pnas.2510416123 | PMCID: PMC13012060 | PMID: 41790947
- Version used: **0.6.10**
- Evidence: Raw reads were quality-checked and trimmed using Trim Galore v0.6.10 (Krueger; GitHub: https://github.com/FelixKrueger/TrimGalore ), then aligned to the respective reference genomes ( P. ochraceus : GCA_010994315.2; A. californica : GCF_000002075.1 assembly AplCal3.0, Broad Institute) using Bismark v0.24.0 ( 88 , 89 ).
- Full pipeline: quality control [Bismark v0.24.0, Trim Galore v0.6.10] -> read trimming [Bismark v0.24.0, Trim Galore v0.6.10] -> alignment/mapping [Bismark v0.24.0, Trim Galore v0.6.10] -> stage not stated [R v4.5, emmeans, phytools]

### Med14 phosphorylation shapes genomic response to GLP-1 agonists. (PNAS 2026)

- DOI: 10.1073/pnas.2536772123 | PMCID: PMC12974444 | PMID: 41779793
- Evidence: Reads were trimmed with Trim Galore, aligned to the rn6 reference genome using bwa mem.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, Trim Galore] -> quantification [HOMER] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2]

### A host-derived volatile primes context-dependent foraging behavior in parasitic nematodes via a lysosome-associated neural pathway. (PNAS 2026)

- DOI: 10.1073/pnas.2520778123 | PMCID: PMC12933127 | PMID: 41706887
- Evidence: Raw reads were quality-trimmed using Trim Galore! v0.11.8 and validated using FASTQC v0.11.8.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HISAT2 v2.1.0, Picard] -> quantification [HTSeq] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [AlphaFold, PyMOL v3.1]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Version used: **0.6.6**
- Evidence: Raw Illumina sequencing reads were quality-filtered using TrimGalore v0.6.6 ( https://github.com/FelixKrueger/TrimGalore ), trimming low-quality bases from both ends with a minimum Phred quality score threshold of 20.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Version used: **0.6.10**
- Evidence: We used RNA-seq data to annotate the protein-coding genes with the FunGAP pipeline ( 68 ) after trimming sequencing adapters with TrimGalore v.0.6.10 ( https://github.com/FelixKrueger/TrimGalore ), and filtering to retain only reads with a Phred quality score >30 and length of ≥50 bp.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

### Antagonistic regulation of nitrogen and drought signaling mediated by NIN-like protein 7 transcription factor in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2509904122 | PMCID: PMC12773779 | PMID: 41481473
- Evidence: For the results of TARGET sequencing, raw sequences were trimmed and quality filtered using cutadapt ( 64 ) via the TrimGalore package ( github.com/FelixKrueger/TrimGalore ) with default settings.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [Bowtie2] -> quantification [kallisto] -> normalisation [DESeq2] -> stage not stated [BEDTools, MACS2]

### Base editing rescue of spinal muscular atrophy in cells and in mice. (Science 2023)

- DOI: 10.1126/science.adg6518 | PMCID: PMC10270003 | PMID: 36996170
- Version used: **0.6.7**
- Evidence: Trim Galore v0.6.7 in paired-end mode with default parameters to remove low-quality bases, adapter sequences, and unpaired sequences.
- Full pipeline: read trimming [STAR v2.7.10a, Trim Galore v0.6.7, kallisto] -> alignment/mapping [STAR v2.7.10a, kallisto] -> quantification [STAR v2.7.10a, kallisto] -> structure determination [STAR v2.7.10a, kallisto]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Version used: **0.50**
- Evidence: Sequence data were trimmed to remove adaptors and sequences with a quality score below 30 using Trim Galore (version 0.50, Babraham Bioinformatics) and then aligned to the mouse genome (GRCm38) using STAR (version 2.6.0a), and differential expression was calculated using DESeq2 (version 1.18.1) ( 77 ).
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Evidence: Reads were adaptor- and quality-trimmed using Trim Galore!( 69 ) (v0.6.5) and aligned to the GATK Genome Reference Consortium Human Build 38 (GRCh38)( 70 ) using bwa-mem (v0.7.17)( 71 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **0.6.6**
- Evidence: Adapter trimming, low-quality sequence removal, and quality control were performed using Cutadapt and FastQC, respectively, both of which are incorporated within Trim Galore (v0.6.6) ( 99 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

