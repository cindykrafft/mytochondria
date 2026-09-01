# fastp

- **Category:** genomics
- **Papers in survey:** 117
- **Journals:** PNAS (65), Nature (44), Cell (8)
- **Years:** 2021 (4), 2022 (17), 2023 (18), 2024 (23), 2025 (39), 2026 (16)
- **Versions named:** 0.20.0 (9), 0.20.1 (8), 0.23.4 (7), 0.23.2 (6), 0.21.0 (6), 0.19.7 (1), 0.12.4 (1), 0.23.0 (1), 0.19.41 (1), 0.24 (1)
- **Pipeline stages it appears in:** read trimming (77), alignment/mapping (23), quality control (17), quantification (4), differential/statistical testing (2), variant calling (2)

## Papers

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Evidence: Adapters were automatically detected and trimmed using fastp ( Chen et al., 2018 ).
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Version used: **0.21.0**
- Evidence: ... Plasmid: pC-BA.2 HV69-70del S This study N/A Plasmid: pC-BA.2 F486V S This study N/A Plasmid: pC-BA.2 R493Q S This study N/A Software and algorithms fastp v0.21.0 Chen et al., 2018 https://github.com/OpenGene/fastp BWA-MEM v0.7.17 Li and Durbin, 2009 http://bio-bwa.sourceforge.net SAMtools v1.9 Li et al., 2009 http://www.htslib.org snpEff v5.0e Cingolani et al., 2012 http://pcingola.github.io/Snp...
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: 2.17-r941) ( Li, 2018 ), and fastp ( Chen et al., 2018 ) capable of being run on any high performance compute system.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Version used: **0.21.0**
- Evidence: ...lasmid: pC-ACE2 ( Ozono et al., 2021 ) N/A Plasmid: pC-TMPRSS2 ( Ozono et al., 2021 ) N/A Plasmid: pJYDC1 Addgene Cat# 162458 Software and algorithms fastp v0.21.0 ( Chen et al., 2018 ) https://github.com/OpenGene/fastp BWA-MEM v0.7.17 ( Li and Durbin, 2009 ) http://bio-bwa.sourceforge.net SAMtools v1.9 ( Li et al., 2009 ) http://www.htslib.org snpEff v5.0e ( Cingolani et al., 2012 ) http://pcingo...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Evidence: 3′-seq analysis Reads were processed with fastp to remove poly(A) stretches and then mapped to the dm6 genome using STAR v2.6.1b with modified parameters ("--sjdbOverhang 74 --limitBAMsortRAM 60000000000 --alignIntronMax 1").
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### Rapid DNA unwinding accelerates genome editing by engineered CRISPR-Cas9. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.031 | PMCID: PMC11658890 | PMID: 38781968
- Evidence: 52 https://github.com/OpenGene/fastp Logomaker version 0.8 Tareen and Kinney 53 https://logomaker.readthedocs.io/en/latest/ ModelAngelo version 1.0.1 Jamali et al.
- Full pipeline: structure determination [Coot v0.9.8.7] -> stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, PHENIX v1.19.2, Python, Topaz, fastp]

### Evolution of Mycobacterium tuberculosis transcription regulation is associated with increased transmission and drug resistance. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.005 | PMCID: PMC12624571 | PMID: 41033311
- Evidence: Next, it used fastp to infer and remove adapters and duplicate reads.
- Full pipeline: quality control [Bowtie2, Cutadapt] -> read trimming [Bowtie2, Cutadapt, fastp] -> alignment/mapping [Bowtie2, Cutadapt] -> variant calling [BCFtools] -> stage not stated [BLAST, SAMtools, SciPy]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: QUANTIFICATION AND STATISTICAL ANALYSIS ChIP-seq analysis Peak calling: Adaptors for raw reads were trimmed using fastp with default parameters and aligned to the human reference genome hg38 with parameters “–end-to-end –very-sensitive –no-unal –no-mixed –no-discordant -I 100 -X 800” using bowtie2.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### Nanobodies from camelid mice and llamas neutralize SARS-CoV-2 variants. (Nature 2021)

- DOI: 10.1038/s41586-021-03676-z | PMCID: PMC8260353 | PMID: 34098567
- Evidence: Reads with undetermined N nucleotides, low quality sequence or less than 300 nt in length were removed with the fastp program 31 .
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera, fastp]

### Identification of trypsin-degrading commensals in the large intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-05181-3 | PMCID: PMC9477747 | PMID: 36071157
- Version used: **0.20.0**
- Evidence: 65 ) to remove duplicated reads, and fastp v.0.20.0 (ref.
- Full pipeline: read trimming [BWA, Canu v1.8] -> alignment/mapping [BWA, ChimeraX, PyMOL] -> quantification [BWA] -> normalisation [BWA] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold, Prokka, fastp v0.20.0, minimap2 v2.17]

### Non-viral, specifically targeted CAR-T cells achieve high safety and efficacy in B-NHL. (Nature 2022)

- DOI: 10.1038/s41586-022-05140-y | PMCID: PMC9452296 | PMID: 36045296
- Evidence: We applied fastp 49 with default parameter to filter out the adaptor sequence and remove low-quality reads to achieve clean data.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [GSVA, UMAP] -> differential/statistical testing [Seurat] -> stage not stated [GSEA, fastp]

### Post-translational control of beige fat biogenesis by PRDM16 stabilization. (Nature 2022)

- DOI: 10.1038/s41586-022-05067-4 | PMCID: PMC9433319 | PMID: 35978186
- Version used: **0.20.1**
- Evidence: Secondary adapter trimming, NextSeq/Poly(G) tail trimming and read filtering were performed using fastp (v.0.20.1); low-quality reads and reads shorter than 24 nucleotides after trimming were removed from the read pool.
- Full pipeline: read trimming [edgeR, fastp v0.20.1] -> alignment/mapping [Bowtie2 v2.1.0, RSEM v1.2.15] -> quantification [Salmon v1.4.0] -> normalisation [edgeR] -> stage not stated [Enrichr]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **0.19.41**
- Evidence: Raw sequencing data were filtered to remove adapter sequences and low-quality reads using fastp (v.0.19.41) 88 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Attenuated fusogenicity and pathogenicity of SARS-CoV-2 Omicron variant. (Nature 2022)

- DOI: 10.1038/s41586-022-04462-1 | PMCID: PMC8942852 | PMID: 35104835
- Version used: **0.21.0**
- Evidence: Sequencing reads were trimmed using fastp v0.21.0 46 and subsequently mapped to the viral genome sequences of a lineage B isolate (strain Wuhan-Hu-1; GISAID ID: EPI_ISL_402125; GenBank accession no.
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [fastp v0.21.0] -> variant calling [SAMtools v1.9] -> differential/statistical testing [Stan v2.28.1] -> simulation/modelling [Stan v2.28.1] -> stage not stated [BWA v0.7.17, ImageJ, R v3.6]

### Enhanced fusogenicity and pathogenicity of SARS-CoV-2 Delta P681R mutation. (Nature 2022)

- DOI: 10.1038/s41586-021-04266-9 | PMCID: PMC8828475 | PMID: 34823256
- Version used: **0.21.0**
- Evidence: Sequencing reads were trimmed using fastp (v.0.21.0) 39 and subsequently mapped to the viral genome sequences of a lineage A isolate (strain WK-521; GISIAD ID: EPI_ISL_408667) 29 or a GFP -inserted WK-521 (ref.
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [MAFFT, fastp v0.21.0] -> variant calling [SAMtools v1.9] -> stage not stated [BWA v0.7.17, IQ-TREE, ImageJ v2.2.0]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Version used: **0.23.0**
- Evidence: Subsequently, reads were trimmed to remove adaptors using fastp v.0.23.0 with standard parameters.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### Mouse genome rewriting and tailoring of three important disease loci. (Nature 2023)

- DOI: 10.1038/s41586-023-06675-4 | PMCID: PMC10632133 | PMID: 37914927
- Evidence: Amplicon reads pairs with more than 75% of G bases were removed, and poor-quality reads were filtered out using fastp 48 with options “-A -G -q 30 -u 15”.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, STAR] -> normalisation [deepTools v3.1.0, featureCounts v1.6.3] -> differential/statistical testing [featureCounts v1.6.3] -> stage not stated [Picard, fastp]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Evidence: 10 ): adapters were trimmed using fastp with default parameters 62 , and mapped to hg19 using HISAT2 with the options–no-mixed–dta–rna-strandness RF -k 2 63 .
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: Adapters and primers were trimmed using fastp 68 .
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: The raw reads were trimmed using fastp to remove low-quality bases from reads (quality <20) and adapter sequences.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### Tree islands enhance biodiversity and functioning in oil palm landscapes. (Nature 2023)

- DOI: 10.1038/s41586-023-06086-5 | PMCID: PMC10247383 | PMID: 37225981
- Version used: **0.20.0**
- Evidence: Paired-end sequences were quality filtered with fastp (v.0.20.0) 69 and merged with PEAR v.0.9.11 (ref.
- Full pipeline: stage not stated [BLAST v2.7.1, Cutadapt v2.5, R, fastp v0.20.0]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Version used: **0.20.0**
- Evidence: Subsequently, fastp (v.0.20.0, flags: --length_required 36; --cut_window_size 4; --cut_mean_quality 10; --average_qual 20 (ref.
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Version used: **0.20.1**
- Evidence: Sequence reads were processed with fastp (v0.20.1) to remove sequences of sequencing adapters and low-quality (Phred quality score below 15) sequences from the 3′ end of the sequence reads.
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### Insulin-regulated serine and lipid metabolism drive peripheral neuropathy. (Nature 2023)

- DOI: 10.1038/s41586-022-05637-6 | PMCID: PMC9891999 | PMID: 36697822
- Evidence: In summary, the raw reads were adapter filtered using the auto-detect parameters in fastp version 20 54 and host (mouse) filtered using minimap2 version 2.17 55 .
- Full pipeline: read trimming [fastp, minimap2 v2.17] -> alignment/mapping [Bowtie2 v2.4.2] -> quantification [ImageJ v1.53e] -> stage not stated [QIIME 2 v2020.11, Stan]

### Probing plant signal processing optogenetically by two channelrhodopsins. (Nature 2024)

- DOI: 10.1038/s41586-024-07884-1 | PMCID: PMC11424491 | PMID: 39198644
- Evidence: Data processing (fastp) and mapping to the N. tabacum genome (kallisto) 75 was carried out using Amalgkit ( https://github.com/kfuku52/amalgkit ).
- Full pipeline: alignment/mapping [fastp, kallisto] -> normalisation [DESeq2] -> stage not stated [PyMOL, R, pheatmap]

### Position-dependent function of human sequence-specific transcription factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07662-z | PMCID: PMC11269187 | PMID: 39020164
- Evidence: We then trimmed adapter sequences from reads using fastp and aligned them to the masked genome using STAR using the default parameters.
- Full pipeline: read trimming [Cutadapt v3.4, fastp] -> alignment/mapping [STAR v2.7.10a, fastp] -> variant calling [PLINK v2.00a] -> normalisation [DESeq2] -> stage not stated [BCFtools, HOMER]

### In situ targeted base editing of bacteria in the mouse gut. (Nature 2024)

- DOI: 10.1038/s41586-024-07681-w | PMCID: PMC11338833 | PMID: 38987595
- Evidence: 73 ); --minimum-length parameter set to 20), merged (FLASH 77 v.1.2.11, parameters --min-overlap 10 --max-mismatch-density 0.2) and filtered by quality (fastp 78 v.0.23.1; parameters -q 19 -u 15).
- Full pipeline: alignment/mapping [MAFFT, Python] -> dimensionality reduction/clustering [QIIME 2] -> stage not stated [Cutadapt v3.3, Matplotlib, fastp, seaborn]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Evidence: The raw data was filtered using the following parameters (fastp 42 v0.20.0: -f 9 -F 9 -l 80 -g); adapter sequences were removed; reads of N number ≥5 and reads where the base quality ≤15 exceeds 40% were discarded; 9 bp in the front of reads were trimmed of and reads with a length ≥80 bp were retained; After removing these low-quality and adapter-containing reads, an average of ~185.14 Gb of clean...
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Version used: **0.20.1**
- Evidence: For libraries sequenced on the NextSeq500, polyg trimming with fastp (v.0.20.1) was enabled using the nf-core/eager flag --complexity_filter_poly_g; we also trimmed 2 bp from the 5′ and 3′ ends of reads from UDG-half-treated libraries 85 .
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Transient loss of Polycomb components induces an epigenetic cancer fate. (Nature 2024)

- DOI: 10.1038/s41586-024-07328-w | PMCID: PMC11096130 | PMID: 38658752
- Evidence: Briefly, base calling was performed using Illumina pipeline CASAVA v.1.8.2, and subjected to quality control using fastp with the following parameters: -g -q 5 -u 50 -n 15 -l 150 --min_trim_length 10 --overlap_diff_limit 1--overlap_diff_percent_limit 10.
- Full pipeline: quality control [fastp] -> alignment/mapping [DESeq2, SAMtools, featureCounts] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [GATK, Mutect2, R, data.table v1.14.2]

### Bile salt hydrolase catalyses formation of amine-conjugated bile acids. (Nature 2024)

- DOI: 10.1038/s41586-023-06990-w | PMCID: PMC10881385 | PMID: 38326609
- Version used: **0.12.4**
- Evidence: Obtained demultiplexed reads were checked for quality and filtered using fastp (v.0.12.4) (ref.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Trimmomatic, fastp v0.12.4] -> alignment/mapping [Bowtie2 v2.2.5, SAMtools v1.10, featureCounts v2.0.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [Prokka]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: To ensure comparability, both public and newly generated data underwent processing through an optimized fork of the community-curated Nextflow rnaseq pipeline (v.3.15.1) 56 – 58 , which was executed in the following order: Read preprocessing Adapters, low-quality base pairs, and poly(A) and poly(G) tails were trimmed using the fastp 59 program (v.0.23.4).
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **0.23.2**
- Evidence: Read mapping To map the short-read sequencing data onto the reference genome, Illumina reads of the 390 samples (326 whole-genome sequencing, 64 RNA sequencing) were trimmed and filtered using fastp v.0.23.2 (ref.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: In brief, raw FASTQ files provided by the sequencing facility were assessed for quality with FastQC 67 , followed by trimming of adapter sequences and removal of low-quality reads with fastp 68 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **0.23.4**
- Evidence: In brief, the pipeline used fastp (v.0.23.4) 71 for adapter trimming and complexity filtering and Bowtie (v.2.5.2) 72 for the removal of eukaryotic contaminant reads, including the human genome (references retrieved from Zenodo: 10.5281/zenodo.4629921).
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Version used: **0.23.2**
- Evidence: For this purpose, paired-end reads were processed using fastp (v.0.23.2 or v.0.24.0) 71 with the following settings: --trim_tail1 1 --trim_tail2 1 --cut_right --cut_right_window_size 4 --cut_right_mean_quality 15 --qualified_quality_phred 15 --unqualified_percent_limit 40 --trim_poly_x --poly_x_min_len 10 --n_base_limit 0 --length_required 75.
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Short-read Illumina data was trimmed with fastp 94 .
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: RNA-seq analysis was performed using the SUSHI framework 75 , which encompassed the following steps: read quality was inspected using FastQC, and sequencing adaptors were removed using fastp 76 ; pseudoalignment and transcriptomic counts of the RNA-seq reads was performed using the Kallisto Bioconductor R package 77 with the GENCODE human genome build GRCh38.p13 (release 37) 78 ; differential expr...
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: To annotate M. leidyi genome we first downloaded developmental Illumina RNA-seq samples ( GSE93977 ), trimmed them with fastp and built a de novo Trinity assembly, which was mapped to the genome using gmap 92 .
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Geographic and age variations in mutational processes in colorectal cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09025-8 | PMCID: PMC12221974 | PMID: 40267983
- Evidence: Prior to alignment, poor quality reads were filtered using fastp 75 , and the remaining human reads were removed by excluding those that mapped to GRCh38, T2T-CHM13v2.0, and the 47 pangenomes 76 .
- Full pipeline: alignment/mapping [BWA, Bowtie2, fastp] -> variant calling [ANNOVAR] -> quantification [R] -> visualisation [R]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: For calculating gene-expression levels, low-quality RNA-seq reads were first removed using fastp 86 (v.0.23.0) with parameters ‘-l 30’.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Version used: **0.19.7**
- Evidence: Trimming of the first 8 bases and adaptors and quality filtering were performed using fastp (v.0.19.7) 46 with the parameters -x -f 8 -q 30 -b 50.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **0.20.0**
- Evidence: The RNA-seq reads were filtered using fastp (v.0.20.0) 51 to remove Illumina adaptor sequences, and to eliminate low-quality bases with the ‘-3 -q 15 -l 15’ options.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Evidence: Raw reads were trimmed and filtered using fastp 64 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Version used: **0.23.2**
- Evidence: ...llowing for 1 bp mismatch for each of the three rounds of 8 bp barcodes that make up a single-cell barcode, followed by Nextera adapter trimming with fastp (v0.23.2) 93 , genome alignment with Bowtie2 (v2.5.0) 94 , and conversion of the output BAM file to a more storage-efficient fragment file.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **0.23.4**
- Evidence: FASTQ files were trimmed using fastp v.0.23.4, moving a sliding window from the 5′ and 3′ ends of the reads and trimming bases with a mean quality below 20.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Capturing dynamic phage-pathogen coevolution by clinical surveillance. (Nature 2026)

- DOI: 10.1038/s41586-026-10136-z | PMCID: PMC12987554 | PMID: 41813903
- Version used: **0.23.2**
- Evidence: Briefly, fastp v.0.23.2 (ref.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [BLAST, ColabFold, IQ-TREE v2.2.0, SPAdes, fastp v0.23.2]

### Pesticide residues alter taxonomic and functional biodiversity in soils. (Nature 2026)

- DOI: 10.1038/s41586-025-09991-z | PMCID: PMC12965876 | PMID: 41606316
- Version used: **0.23.4**
- Evidence: Raw metagenomic sequencing reads underwent initial quality processing using fastp v.0.23.4 75 for quality filtering and error correction.
- Full pipeline: normalisation [R] -> stage not stated [DADA2, eggNOG, fastp v0.23.4, vegan]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Version used: **0.20.0**
- Evidence: Samples were demultiplexed, quality checked, filtered and aligned with genome build GRCm38 using pre-established pipelines implemented in snakePipes 64 with STARsolo v.2.7.4a 65 , deeptools v.3.3.2, seqtk v.1.3, pigz v.2.3.4, snpsplit v.0.3.4, samtools v.1.10, fastqc v.0.11.9, cutadapt v.2.8, trim-galore v.0.6.5, multiqc v.1.8, fastp v.0.20.0, umi_tools v.1.0.1 and star v.2.7.4a.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Evidence: RNA sequencing data processing and analysis Raw data (raw reads) of fastq format were first processed through fastp software.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Genomic sequencing reads were quality trimmed using fastp 61 and aligned to the S. pombe ASM294v2.30 reference sequence 62 with the BWA aligner 63 using default parameters.
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: The raw reads were trimmed for barcodes, quality filtered and deduplicated with fastp 83 v.0.23.2 with the following options: --detect_adapter_for_pe --correction --cut_right --cut_right_window_size 4 --cut_right_mean_quality 20 --average_qual 30 --length_required 100 --dedup --dup_calc_accuracy 6.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Evidence: Raw data (raw reads) of FASTQ format were firstly processed through fastp.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### Estimating maximal microbial growth rates from cultures, metagenomes, and single cells via codon usage patterns. (PNAS 2021)

- DOI: 10.1073/pnas.2016810118 | PMCID: PMC8000110 | PMID: 33723043
- Version used: **0.21.0**
- Evidence: Adapters and low-quality reads were trimmed using fastp v0.21.0 ( 87 ) with default parameters, and only reads longer than 30 base pairs (bp) were kept for further analysis.
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [RAxML] -> visualisation [ggplot2, ggpubr] -> stage not stated [R, ape (R)]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: Reads used for genome assembly were quality and adapter trimmed using fastp ( 66 ) using default parameters for single end reads, and the “--detect_adapter_for_pe” flag for paired end reads.
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### Type IV pili trigger episymbiotic association of Saccharibacteria with its bacterial host. (PNAS 2022)

- DOI: 10.1073/pnas.2215990119 | PMCID: PMC9894109 | PMID: 36454763
- Version used: **0.20.0**
- Evidence: Raw 16S rRNA gene sequencing reads were demultiplexed, quality-filtered by fastp (version 0.20.0) and merged with FLASH (version 1.2.7).
- Full pipeline: read trimming [fastp v0.20.0] -> stage not stated [ImageJ, Python, QIIME 2]

### Microbiome composition modulates secondary metabolism in a multispecies bacterial community. (PNAS 2022)

- DOI: 10.1073/pnas.2212930119 | PMCID: PMC9586298 | PMID: 36215464
- Version used: **0.20.0**
- Evidence: Briefly, reads were preprocessed with fastp v0.20.0 ( 59 ) and split to their respective source (i.e., either Bc , Fj , or Pk ) with bbsplit ( 60 ), discarding ambiguously mapped reads.
- Full pipeline: alignment/mapping [HTSeq, SAMtools v1.9, fastp v0.20.0] -> quantification [HTSeq, SAMtools v1.9] -> differential/statistical testing [R v4.2] -> stage not stated [Bowtie2 v2.4.2, edgeR, eggNOG]

### Ectopic expression of meiotic cohesin generates chromosome instability in cancer cell line. (PNAS 2022)

- DOI: 10.1073/pnas.2204071119 | PMCID: PMC9549395 | PMID: 36179046
- Evidence: As a routine approach, the ChIP-on-ChEP-seq data (delivered as paired reads) from crab-eating macaque were first cleaned by trimming of adapters and removing low-quality reads using fastp ( 128 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, clusterProfiler] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [BEDTools, MACS2 v2.2, RepeatMasker]

### Three distinct <i>Atoh1</i> enhancers cooperate for sound receptor hair cell development. (PNAS 2022)

- DOI: 10.1073/pnas.2119850119 | PMCID: PMC9371730 | PMID: 35925886
- Evidence: For both ATAC-seq and CUT&RUN analyses, raw reads were first trimmed by using fastp with default parameters ( 67 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools]

### APOBEC3A regulates transcription from interferon-stimulated response elements. (PNAS 2022)

- DOI: 10.1073/pnas.2011665119 | PMCID: PMC9171812 | PMID: 35549556
- Evidence: Read quality assessment and trimming was performed using fastp ( 52 ).
- Full pipeline: read trimming [fastp] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, Bioconductor, R v4.0]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: Briefly, FASTQ files were trimmed to remove low-quality reads using fastp ( 64 ) (version 0.12.5, arguments –cut_by_quality3, –cut_window_size = 10, –cut_mean_quality = 20, –length_required = 50, –correction) and aligned to the most likely inferred ancestor of the MTBC ( 24 ) using the BWA-MEM algorithm ( 65 ).
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### BRD4-directed super-enhancer organization of transcription repression programs links to chemotherapeutic efficacy in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2109133119 | PMCID: PMC8832982 | PMID: 35105803
- Evidence: The quality of raw data was examined by FastQC, and sequencing adapter and low-quality reads, including those with more than five “N” bases and mean Phred quality score less than 15, were removed through fastp.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> alignment/mapping [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [Bioconductor, HOMER, MACS2]

### Adaptive DNA amplification of synthetic gene circuit opens a way to overcome cancer chemoresistance. (PNAS 2023)

- DOI: 10.1073/pnas.2303114120 | PMCID: PMC10710087 | PMID: 38019857
- Version used: **0.20.1**
- Evidence: The low-quality reads (containing at least one ambiguous base, or average quality <20) were then removed using fastp v0.20.1.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.6.1d] -> quantification [featureCounts] -> stage not stated [Fiji, ImageJ, R v4.1, fastp v0.20.1]

### Changes in parrot diversity after human arrival to the Caribbean. (PNAS 2023)

- DOI: 10.1073/pnas.2301128120 | PMCID: PMC10576146 | PMID: 37748079
- Evidence: Adaptor removal, quality trimming, deduplication, and pairing of the MiSeq and NovaSeq reads were performed in fastp ( 67 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [BWA v0.7.13, IQ-TREE v2.1.2, SAMtools v1.10] -> stage not stated [BCFtools v1.12, MAFFT v7.455, R v4.1]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We filtered raw reads below a Phred quality score of 15 and trimmed adapter sequences using fastp ( 75 ).
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: For each sample, reads were trimmed using fastp to generate trimmed.fastq.gz files.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Sakuranetin protects rice from brown planthopper attack by depleting its beneficial endosymbionts. (PNAS 2023)

- DOI: 10.1073/pnas.2305007120 | PMCID: PMC10266023 | PMID: 37256931
- Evidence: After demultiplexing, the sequencing was quality filtered with fastp ( https://github.com/OpenGene/fastp ) and merged with FLASH ( https://ccb.jhu.edu/software/FLASH/index.shtml ) ( 42 , 43 ).
- Full pipeline: read trimming [fastp]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: Raw fastq reads were trimmed by fastp and aligned to the fusion genome using Burrows-Wheeler Aligner (BWA) ( 42 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Host-specific plasmid evolution explains the variable spread of clinical antibiotic-resistance plasmids. (PNAS 2023)

- DOI: 10.1073/pnas.2212147120 | PMCID: PMC10104558 | PMID: 37023131
- Evidence: We used fastp for quality control, adapter trimming, and quality filtering of reads acquired by Illumina sequencing ( 73 ).
- Full pipeline: quality control [fastp] -> read trimming [fastp] -> stage not stated [R]

### Cross-species predictive modeling reveals conserved drought responses between maize and sorghum. (PNAS 2023)

- DOI: 10.1073/pnas.2216894120 | PMCID: PMC10013860 | PMID: 36848555
- Version used: **0.23.2**
- Evidence: We trimmed sequence adapters and quality checked the raw FASTQ files using the program fastp (v0.23.2) ( 43 ).
- Full pipeline: quality control [fastp v0.23.2] -> read trimming [fastp v0.23.2] -> variant calling [DESeq2 v1.36.0] -> normalisation [scikit-learn] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [scikit-learn] -> stage not stated [R]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Evidence: Raw fastq files were trimmed using fastp ( 112 ) with default settings.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### The genetic origins and impacts of historical Papuan migrations into Wallacea. (PNAS 2024)

- DOI: 10.1073/pnas.2412355121 | PMCID: PMC11670103 | PMID: 39689173
- Evidence: For all samples, raw sequence reads were processed with fastp to remove adapters and trim poly-G and poly-X tails, with additional trimming of terminal nucleotides (5’ end = 20nt; 3’ end = 5nt) using a mean quality threshold of 20 ( 63 ).
- Full pipeline: read trimming [BWA v0.7.17, fastp] -> alignment/mapping [BWA v0.7.17, GATK, SAMtools v1.9] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE, R] -> stage not stated [PLINK v1.987]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: RNA-seq reads were trimmed using “fastp” ( 63 ) version 0.20.1 and options “p trim_front1=2 trim_front2=2 detect_adapter_for_pe”.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### Conserved moonlighting protein pyruvate dehydrogenase induces robust protection against &lt;i&gt;Staphylococcus aureus&lt;/i&gt; infection. (PNAS 2024)

- DOI: 10.1073/pnas.2321939121 | PMCID: PMC11388329 | PMID: 39186649
- Version used: **0.20.1**
- Evidence: Filtration of sequence adapters and low-quality bases was carried out with the help of fastp (v0.20.1) ( 50 ).
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [Clustal Omega] -> differential/statistical testing [DESeq2 v1.30.1]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: Raw fastq sequencing reads were trimmed of poor quality and adapter sequences using FASTP ( 71 ) (fastp–qualified_quality_phred 30).
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### Transfection of entomopathogenic <i>Metarhizium</i> species with a mycovirus confers hypervirulence against two lepidopteran pests. (PNAS 2024)

- DOI: 10.1073/pnas.2320572121 | PMCID: PMC11214047 | PMID: 38885380
- Evidence: Raw data in the FASTQ format were processed using the open-source software fastp (HaploX Biotechnology, Shenzhen, China) ( 64 ); clean reads were obtained by removing reads containing adapter, ploy-N, and low-quality reads from raw data.
- Full pipeline: read trimming [fastp] -> alignment/mapping [ggplot2] -> quantification [ggplot2] -> dimensionality reduction/clustering [clusterProfiler, ggplot2] -> stage not stated [BLAST, DESeq2, R, pheatmap]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Evidence: Raw NGS reads were processed by filtering sequence length <50 and base number >6 with fastp software (version 0.20.0).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: A total of 98 Gb of trimmed genomic data were generated using fastp ( 63 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### TMPRSS2-mediated SARS-CoV-2 uptake boosts innate immune activation, enhances cytopathology, and drives convergent virus evolution. (PNAS 2024)

- DOI: 10.1073/pnas.2407437121 | PMCID: PMC11161796 | PMID: 38814864
- Evidence: Raw Fastq files were quality- and adapter-trimmed with fastp ( 40 ).
- Full pipeline: read trimming [fastp] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Evidence: ChIP-Seq raw data (fastQ files) were analyzed with fastp for quality control checks ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Timeless noncoding DNA contains cell-type preferential enhancers important for proper Drosophila circadian regulation. (PNAS 2024)

- DOI: 10.1073/pnas.2321338121 | PMCID: PMC11009632 | PMID: 38568969
- Evidence: ATAC-Seq files were adaptor-trimmed using fastp.
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, MACS2] -> stage not stated [BEDTools, Cellpose, DESeq2, SAMtools]

### IL-27 regulates the differentiation of follicular helper NKT cells via metabolic adaptation of mitochondria. (PNAS 2024)

- DOI: 10.1073/pnas.2313964121 | PMCID: PMC10907256 | PMID: 38394242
- Evidence: Adaptor sequences were trimmed from the raw RNA-seq reads with fastp ( 47 ).
- Full pipeline: read trimming [fastp] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ, MACS2]

### Isolation, characterization, and circulation sphere of a filovirus in fruit bats. (PNAS 2024)

- DOI: 10.1073/pnas.2313789121 | PMCID: PMC10873641 | PMID: 38335257
- Version used: **0.20.0**
- Evidence: The reads were quality checked using fastp version 0.20.0, and the resultants were de novo assembled using SPAdes genome assembler version 3.14.1 in meta mode.
- Full pipeline: quality control [SPAdes, fastp v0.20.0] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> quantification [ImageJ] -> visualisation [ImageJ, PyMOL v2.4.0] -> stage not stated [BLAST v0.9.35]

### Phase separation of YAP-MAML2 differentially regulates the transcriptome. (PNAS 2024)

- DOI: 10.1073/pnas.2310430121 | PMCID: PMC10873646 | PMID: 38315854
- Evidence: The raw data were processed with fastp.
- Full pipeline: dimensionality reduction/clustering [ImageJ] -> stage not stated [edgeR, fastp]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **0.20.1**
- Evidence: All PacBio sequences provided by Maryland Genomics (University of Maryland, institute for genome sciences) were conducted by fastqc (v0.11.9) with default parameters and fastp (v0.20.1) with the parameters of “-5 -W 5 -M 30 -q 30 -z 1 -n 5” and then were corrected by NEXTDENOVO (v2.4.0) ( https://github.com/Nextomics/NextDenovo ) with default parameters and assembled using Flye (v2.8.1-b1676) ( 62...
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Anellovirus protein encoded by &lt;i&gt;ORF2/3&lt;/i&gt; functions as the viral replication initiation protein. (PNAS 2025)

- DOI: 10.1073/pnas.2516306122 | PMCID: PMC12772153 | PMID: 41433061
- Version used: **0.23.4**
- Evidence: We used the “star_salmon” workflow and chose fastp v0.23.4 for read quality filtering, while otherwise retaining the default settings and software versions used in nf-core/rnaseq v3.17.0.
- Full pipeline: alignment/mapping [SAMtools v1.20, StringTie v2.2.3] -> quantification [SAMtools v1.20, StringTie v2.2.3] -> stage not stated [AlphaFold, Conda, fastp v0.23.4]

### Nanorate sequencing reveals the &lt;i&gt;Arabidopsis&lt;/i&gt; somatic mutation landscape. (PNAS 2025)

- DOI: 10.1073/pnas.2514194122 | PMCID: PMC12685076 | PMID: 41296725
- Evidence: Sequencing reads ( 101 ) were trimmed and filtered with fastp using default parameters ( 102 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2] -> stage not stated [MACS2, SAMtools, SciPy, Snakemake]

### The immunoproteasome regulates ILC2 responses by modulating mitochondrial capacity. (PNAS 2025)

- DOI: 10.1073/pnas.2518190122 | PMCID: PMC12663963 | PMID: 41264257
- Evidence: Read quality was assessed and adapters trimmed using fastp.
- Full pipeline: read trimming [fastp] -> quantification [ImageJ] -> differential/statistical testing [R, edgeR] -> stage not stated [QuPath]

### Single-cell metabolome and RNA-seq multiplexing on single plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512828122 | PMCID: PMC12582292 | PMID: 41134629
- Evidence: Adapter sequences or poly-A tail from fastq files were trimmed based on fastp, aligned onto genome by STAR (v2.7.10a), and quantified by RSEM (v.1.3.1).
- Full pipeline: read trimming [RSEM v1.3.1, STAR v2.7.10a, fastp] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.10a, fastp] -> quantification [RSEM v1.3.1, STAR v2.7.10a, fastp] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [Cytoscape] -> stage not stated [ImageJ, Seurat v5.0.1]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **0.23.4**
- Evidence: Raw reads were processed using fastp (v0.23.4; poly-G trimming enabled, minimum length 150 bp, quality/N-content filtering) and assessed for quality (FastQC v0.12.1, MultiQC v1.23).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **1.0.1**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Combined pesticide pollution enhances the dissemination of the phage-encoded antibiotic resistome in the soil under nitrogen deposition. (PNAS 2025)

- DOI: 10.1073/pnas.2516722122 | PMCID: PMC12519213 | PMID: 41042849
- Version used: **0.22.08**
- Evidence: Raw reads from the metagenomes were trimmed using fastp (v0.22.08) ( 77 ) and contigs were independently assembled using MEGAHIT (v1.2.9) ( 78 ).
- Full pipeline: read trimming [fastp v0.22.08] -> alignment/mapping [BLAST] -> visualisation [Cytoscape v3.10.0] -> stage not stated [HMMER v3.1b, R v4.0.3, eggNOG, vegan]

### Duplication of a conserved mitochondrial enzyme gene arms parasitoid wasps with venom cytotoxicity and oogenesis regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2512820122 | PMCID: PMC12501140 | PMID: 40996803
- Evidence: Quality control of the RNA-seq data was performed by fastp ( 68 ) v0.23.4, and then the gene expression level (transcripts per kilobase million, TPM) was calculated by salmon ( 69 ) v0.12.0.
- Full pipeline: quality control [fastp] -> alignment/mapping [MAFFT] -> quantification [fastp] -> structure determination [phytools] -> stage not stated [AlphaFold, BLAST, HMMER]

### The balance between microbial arsenic methylation and demethylation in paddy soils underpins global arsenic risk and straighthead disease in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2508311122 | PMCID: PMC12478174 | PMID: 40966281
- Evidence: Quality control was performed with fastp ( 58 ) (v0.21.0), yielding ~8.07 billion reads (average ~79 million/sample).
- Full pipeline: quality control [fastp] -> differential/statistical testing [pheatmap] -> visualisation [pheatmap] -> stage not stated [BLAST]

### A 65-kb deletion survey identifies a distal &lt;i&gt;cis-&lt;/i&gt;regulatory region for red-light induction of &lt;i&gt;Ghd7&lt;/i&gt;, a key rice floral repressor. (PNAS 2025)

- DOI: 10.1073/pnas.2423119122 | PMCID: PMC12377723 | PMID: 40811470
- Version used: **0.23.4**
- Evidence: Quality control and adapter trimming were performed using fastp (version 0.23.4) with the following parameters: --detect_adapter_for_pe --cut_front --cut_tail --cut_window_size 4 --cut_mean_quality 20 -l 36 -u 30.
- Full pipeline: quality control [FastQC v0.12.1, fastp v0.23.4] -> read trimming [FastQC v0.12.1, fastp v0.23.4] -> alignment/mapping [HISAT2 v2.2.1, minimap2] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [SAMtools v1.19, featureCounts]

### Repeated polyploidization shapes divergence in floral morphology in &lt;i&gt;Lithophragma bolanderi&lt;/i&gt; (Saxifragaceae). (PNAS 2025)

- DOI: 10.1073/pnas.2505119122 | PMCID: PMC12377753 | PMID: 40802687
- Evidence: We mapped reads trimmed with fastp ( 76 ) of both species to the reference genome of L. bolanderi with bwa version 0.7.18 ( 77 ), identified and filtered duplicated reads, and called SNPs with GATK version 4.1.4.1 by using Haplotypecaller to call variants per individual, for their specific ploidy levels, and then aggregate variants using GenotypeGVCFs ( 78 , 79 ).
- Full pipeline: read trimming [GATK v4.1.4.1, fastp] -> alignment/mapping [GATK v4.1.4.1, fastp] -> variant calling [GATK v4.1.4.1, IQ-TREE, VCFtools, fastp] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4] -> stage not stated [BUSCO, WhatsHap]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Evidence: Raw reads were trimmed and paired with fastp (--qualified_quality_phred 20, --unqualified_percent_limit 20) for a final total of 402 million read pairs from axenic E. clementina ( 86 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### Measuring the selective packaging of RNA molecules by viral coat proteins in cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505190122 | PMCID: PMC12377776 | PMID: 40789029
- Version used: **0.23.2**
- Evidence: Briefly, we filtered the RNAseq reads for overall quality using fastp (v0.23.2) ( 76 ) with the following parameters: minimum read length of 15 (-l 15), sliding window size of 8 (-w 8), quality threshold of 15 (-q 15), maximum unqualified base percentage of 40% (-u 40), maximum number of ambiguous bases of 5 (-n 5), and adapter trimming (-a CTGTCTCTTATACACATCT).
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1] -> structure determination [PHENIX]

### Neuronal processes contain the essential components for the late steps of ribosome biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2502424122 | PMCID: PMC12337303 | PMID: 40743395
- Evidence: The reads underwent cleaning to remove adapters and low-quality segments using [fastp]( https://github.com/OpenGene/fastp ).
- Full pipeline: quality control [DESeq2] -> read trimming [fastp] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Ciprofloxacin-driven purifying selection on viral genomes accelerates soil N&lt;sub&gt;2&lt;/sub&gt;O production. (PNAS 2025)

- DOI: 10.1073/pnas.2503199122 | PMCID: PMC12304974 | PMID: 40668828
- Evidence: After trimming and filtering low-quality reads using fastp, a total of 270 GB clean reads (approximately 30 GB per soil sample) were obtained and deposited in the NCBI Short Read Archive database.
- Full pipeline: read trimming [fastp] -> visualisation [Cytoscape v3.7.2] -> stage not stated [BLAST v2.12.0, R v4.3.1, eggNOG, ggplot2, pheatmap]

### Multiorgan transcriptomics in mice identifies immunoglobulin heavy constant mu (&lt;i&gt;Ighm&lt;/i&gt;) as a tissue-level aging biomarker. (PNAS 2025)

- DOI: 10.1073/pnas.2423142122 | PMCID: PMC12280941 | PMID: 40643973
- Version used: **0.23.1**
- Evidence: Adapter sequences were trimmed, and low-quality reads (those in which more than 50% of the bases have a Qphred quality score of ≤20) were filtered out using fastp (v 0.23.1) ( 27 ).
- Full pipeline: read trimming [fastp v0.23.1] -> alignment/mapping [STAR v2.7.11b] -> quantification [ImageJ] -> dimensionality reduction/clustering [edgeR v4.2.1] -> visualisation [edgeR v4.2.1] -> stage not stated [DESeq2, R v4.4.1]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Version used: **0.20.1**
- Evidence: The low-quality metagenomic reads were then processed with fastp (version 0.20.1) 3).
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Macroevolutionary changes in natural selection on codon usage reflect evolution of the tRNA pool across a budding yeast subphylum. (PNAS 2025)

- DOI: 10.1073/pnas.2419889122 | PMCID: PMC12260425 | PMID: 40591602
- Evidence: Briefly, adapters for each sequence were trimmed using fastp ( 52 ), and genes were quantified using kallisto ( 53 ).
- Full pipeline: read trimming [fastp, kallisto] -> quantification [fastp, kallisto] -> visualisation [ComplexHeatmap] -> stage not stated [R]

### Population sequencing for phylogenetic diversity and transmission analyses. (PNAS 2025)

- DOI: 10.1073/pnas.2424797122 | PMCID: PMC12167970 | PMID: 40460116
- Version used: **0.20.1**
- Evidence: The reads from the single colonies underwent quality control using fastp v0.20.1 ( 35 ) using default parameters and the SNPs were called using NASP v1.2.0 ( 36 ) which mapped the reads to the reference (accession NC_007795 ) using BWA-MEM v0.7.17 ( 37 ) and called the SNPs using the GATK v3.8 UnifiedGenotyper ( 26 , 38 ) method.
- Full pipeline: quality control [BWA v0.7.17, GATK, fastp v0.20.1] -> alignment/mapping [BWA v0.7.17, GATK, fastp v0.20.1] -> variant calling [BWA v0.7.17, fastp v0.20.1]

### RNA sequencing analysis of viromes of &lt;i&gt;Aedes albopictus&lt;/i&gt; and &lt;i&gt;Aedes vexans&lt;/i&gt; collected from NEON sites. (PNAS 2025)

- DOI: 10.1073/pnas.2403591122 | PMCID: PMC12107137 | PMID: 40354533
- Version used: **0.21.1**
- Evidence: Reads were preprocessed and trimmed using fastp v0.21.1 ( 40 ) and assembled into contigs using MEGAHIT v1.2.9 ( 41 ) with default options.
- Full pipeline: read trimming [BWA, fastp v0.21.1] -> alignment/mapping [BLAST, BWA, Kraken2, SAMtools] -> stage not stated [Bowtie2, R]

### Global modulation of gene expression and transcriptome size in aneuploid combinations of maize. (PNAS 2025)

- DOI: 10.1073/pnas.2426749122 | PMCID: PMC12067209 | PMID: 40310457
- Evidence: The raw reads were trimmed, and low-quality reads were filtered out by fastp using default parameters ( 55 , 56 ).
- Full pipeline: read trimming [fastp]

### Unified molecular approach for spatial epigenome, transcriptome, and cell lineages. (PNAS 2025)

- DOI: 10.1073/pnas.2424070122 | PMCID: PMC12037033 | PMID: 40249782
- Evidence: Reads were trimmed to a maximum length of 75 bp and adapter sequences were removed using “fastp.” Hisat2 was used to align fastq files to the mm10 or hg38 reference genome using parameters “--no-spliced-alignment --very-sensitive -X 2000.” The CB and UB tags were added to the hisat2 ATAC-seq alignments using the read name table created from spaceranger as well as a custom python script utilizing t...
- Full pipeline: quality control [ArchR, Seurat] -> read trimming [fastp] -> alignment/mapping [HISAT2, Seurat, fastp] -> quantification [ArchR] -> dimensionality reduction/clustering [ArchR] -> visualisation [ggplot2]

### Biallelic variants in the conserved ribosomal protein chaperone gene &lt;i&gt;PDCD2&lt;/i&gt; are associated with hydrops fetalis and early pregnancy loss. (PNAS 2025)

- DOI: 10.1073/pnas.2426078122 | PMCID: PMC12012559 | PMID: 40208938
- Version used: **0.21.0**
- Evidence: Libraries were sequenced on an Illumina platform (CeGaT). fastp (v0.21.0) was used to remove artificial and low quality (Phred quality score below 15) sequences ( 53 ).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> stage not stated [GATK, VEP v103.0, fastp v0.21.0]

### A long-distance inhibitory system regulates haustoria numbers in parasitic plants. (PNAS 2025)

- DOI: 10.1073/pnas.2424557122 | PMCID: PMC11874510 | PMID: 39964721
- Evidence: Briefly, the adapter and low-quality sequences were removed using the fastp software with default parameters ( 48 ).
- Full pipeline: read trimming [fastp, featureCounts] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> stage not stated [InterProScan]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **0.20.0**
- Evidence: Raw reads were filtered using fastp (version 0.20.0) with default parameters.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Metabolic enhancement contributed by horizontal gene transfer is essential for dietary specialization in leaf beetles. (PNAS 2025)

- DOI: 10.1073/pnas.2415717122 | PMCID: PMC11725898 | PMID: 39793087
- Version used: **0.23.4**
- Evidence: In brief, the high-quality sequencing raw reads were filtered using fastp v0.23.4 ( 42 ).
- Full pipeline: alignment/mapping [Clustal Omega, SAMtools v1.17] -> stage not stated [IQ-TREE v2.2.2.6, OrthoFinder v2.5.4, RepeatMasker v2.0.4, eggNOG, fastp v0.23.4]

### Host genetic regulation of rumen 6-hydroxymelatonin reduces methane emissions in dairy cattle. (PNAS 2026)

- DOI: 10.1073/pnas.2604454123 | PMCID: PMC13291679 | PMID: 42258707
- Evidence: The metagenomic reads after quality control with fastp were aligned to the reference database provided by SGV-Finder, which is based on the proGenomes database ( http://progenomes1.embl.de/ ) ( 23 ) using GEM mapper.
- Full pipeline: quality control [fastp] -> alignment/mapping [fastp] -> dimensionality reduction/clustering [R] -> differential/statistical testing [GEMMA, TwoSampleMR v0.5.6] -> stage not stated [GCTA, PLINK, VEP, lavaan]

### Ancient DNA from shells reveals delayed genomic erosion and rapid immune adaptation in the critically endangered black abalone. (PNAS 2026)

- DOI: 10.1073/pnas.2600483123 | PMCID: PMC13229213 | PMID: 42207912
- Evidence: We adapter-trimmed and merged overlapping reads from all shell libraries using fastp with default parameters ( 90 ).
- Full pipeline: read trimming [fastp] -> variant calling [SAMtools] -> stage not stated [GATK, IQ-TREE, R]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **0.24**
- Evidence: Raw reads were trimmed and merged using fastp v0.24 ( 50 ), requiring a minimal overlap of 15 base pairs (bp) and a maximum number of mismatches of 1 (--overlap_len_require 15 --overlap_diff_limit 1).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### Fibro-adipogenic progenitor cells from murine SMA muscles are intrinsically adipogenic. (PNAS 2026)

- DOI: 10.1073/pnas.2525423123 | PMCID: PMC13037897 | PMID: 41886383
- Evidence: Reads were acquired from the NovaSeq 6000 platform and were cleaned up using fastp ( 72 ) to remove adaptor sequencing and low quality reads with phred score <20.
- Full pipeline: quality control [featureCounts] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ, fastp]

### Domestication drives repeated evolution of sexual-asexual life cycle trade-offs in yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2526682123 | PMCID: PMC12798947 | PMID: 41505518
- Version used: **0.24.2**
- Evidence: Raw reads were processed using fastp (0.24.2) ( 48 ) to remove adapters and discard reads shorter than 40 nucleotides or with an average Phread quality score below 25.
- Full pipeline: read trimming [fastp v0.24.2] -> alignment/mapping [SAMtools v1.21] -> stage not stated [BCFtools v1.21, R, VCFtools]

### Dietary folic acid prevents peripheral neuropathy in mouse models of neural tube defects and type 2 diabetes. (PNAS 2026)

- DOI: 10.1073/pnas.2528095123 | PMCID: PMC12773702 | PMID: 41481435
- Version used: **0.20**
- Evidence: Adapter trimming and quality filtering were performed with fastp v0.20 ( 65 ).
- Full pipeline: read trimming [fastp v0.20, kallisto v0.46.1] -> alignment/mapping [kallisto v0.46.1] -> quantification [kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [R v3.42.2, edgeR v3.42.2] -> stage not stated [ImageJ]

