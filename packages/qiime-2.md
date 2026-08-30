# QIIME 2

- **Category:** microbiome
- **Papers in survey:** 59
- **Journals:** PNAS (39), Nature (16), Cell (4)
- **Years:** 2021 (11), 2022 (10), 2023 (7), 2024 (14), 2025 (14), 2026 (3)
- **Versions named:** 2020.8 (2), 2018.11 (2), 2020.11 (2), 1.8.0 (2), 2021.2.0 (1), 2019.7 (1), 1.9.1 (1), 2023.2 (1), 2019.10 (1), 2017.4 (1)
- **Pipeline stages it appears in:** read trimming (9), dimensionality reduction/clustering (5), quantification (4), quality control (3), alignment/mapping (2), normalisation (1)

## Papers

### Microbial exposure during early human development primes fetal immune cells. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.039 | PMCID: PMC8240556 | PMID: 34077752
- Version used: **1.8.0**
- Evidence: ....r-project.org UMAP ( McInnes et al., 2018 ) https://github.com/lmcinnes/umap SMuRF 1.0 CRAN https://cran.r-project.org/web/packages/smurf/index.html QIIME 1.8.0 QIIME http://qiime.org/ emperor 1.0 Biocore https://biocore.github.io/emperor/ vegan v2.5.7 CRAN https://cran.r-project.org/web/packages/vegan/index.html Python 2.7.0 Python Software Foundation https://www.python.org/ Python 3.7.0 Python ...
- Full pipeline: alignment/mapping [pandas] -> dimensionality reduction/clustering [QIIME 2 v1.8.0, R v4.4, UMAP] -> stage not stated [ImageJ, Matplotlib v3.2.1, NumPy v1.19.4, Python v2.7.0, seaborn v0.9.0]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **2018.8**
- Evidence: ....10 Zhang et al., 2014 https://cme.h-its.org/exelixis/web/software/pear/ cutadapt version 1.17 Martin, 2011 https://cutadapt.readthedocs.io/en/v1.17/ QIIME 2 version 2018.8 Bolyen et al., 2019 https://qiime2.org/ ITSx version 1.1b1 ( Bengtsson-Palme and Ryberg, 2013 https://microbiology.se/software/itsx/ R version 4.03 R CRAN www.r-project.org phyloseq 1.34.0 McMurdie and Holmes, 2013 https://bioc...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Evidence: ...o.org/records/12615731 Adobe Illustrator Adobe www.adobe.com DESeq2 https://doi.org/10.1186/s13059-014-0550-8 https://doi.org/10.18129/B9.bioc.DESeq2 QIIME I v1.9.188 https://doi.org/10.1038/s41587-019-0209-9 https://qiime2.org/ Dada2 v1.6.089 https://doi.org/10.1038/nmeth.3869 https://doi.org/10.18129/B9.bioc.dada2 Phlyoseq v1.30.090 https://doi.org/10.1371/journal.pone.0061217 https://doi.org/10...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: 177 V16.40.1 NIS-Elements Nikon V6.10.01 Odyssey Western Blot Image Studio LI-COR V6.0 OrthoFinder Emms and Kelly 178 V3.0.1b1 Prism Graph Pad V10.4.2 Progenesis QI Non-Linear Dynamics V3.0 QIIME2 Bolyen et al.
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### Rapid microbial methanogenesis during CO<sub>2</sub> storage in hydrocarbon reservoirs. (Nature 2021)

- DOI: 10.1038/s41586-021-04153-3 | PMCID: PMC8695373 | PMID: 34937895
- Version used: **2017.4**
- Evidence: Microbiome bioinformatics were performed with QIIME 2 2017.4 47 .
- Full pipeline: read trimming [DADA2] -> machine learning [scikit-learn] -> stage not stated [QIIME 2 v2017.4]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: Microbial community analysis of the 16S rRNA gene amplicon data was carried out using the QIIME2 environment with a number of available plugins 51 .
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **2018.11**
- Evidence: Further analyses were performed using QIIME 2 (v.2018.11) 104 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Insulin-regulated serine and lipid metabolism drive peripheral neuropathy. (Nature 2023)

- DOI: 10.1038/s41586-022-05637-6 | PMCID: PMC9891999 | PMID: 36697822
- Version used: **2020.11**
- Evidence: Downstream analyses were performed in QIIME 2 version 2020.11 58 .
- Full pipeline: read trimming [fastp, minimap2 v2.17] -> alignment/mapping [Bowtie2 v2.4.2] -> quantification [ImageJ v1.53e] -> stage not stated [QIIME 2 v2020.11, Stan]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Raw reads were processed using cutadapt 56 to remove primer sequences followed by the sequence analyses using the QIIME2 pipeline 57 .
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Version used: **2020.8**
- Evidence: Raw data quality was assessed using FastQC v0.11.5 and raw data were imported in QIIME2 v2020.8 for downstream analysis 28 .
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### An enterococcal phage-derived enzyme suppresses graft-versus-host disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07667-8 | PMCID: PMC11291292 | PMID: 38987594
- Version used: **2018.11**
- Evidence: 16S rRNA gene analysis was performed using QIIME2 (v.2018.11; https://qiime2.org ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> dimensionality reduction/clustering [SPAdes v3.13.0] -> differential/statistical testing [SPAdes v3.13.0] -> stage not stated [BLAST, Cutadapt, QIIME 2 v2018.11, R, SAMtools, ggplot2 v3.3.6]

### In situ targeted base editing of bacteria in the mouse gut. (Nature 2024)

- DOI: 10.1038/s41586-024-07681-w | PMCID: PMC11338833 | PMID: 38987595
- Evidence: Sequences were clustered into operational taxonomic units at a 97% similarity threshold with Uparse 81 v.7.0.1001 and annotated with taxonomy information using QIIME 82 v.1.9.1 and the Silva database.
- Full pipeline: alignment/mapping [MAFFT, Python] -> dimensionality reduction/clustering [QIIME 2] -> stage not stated [Cutadapt v3.3, Matplotlib, fastp, seaborn]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Evidence: Sequencing data quality control, read mapping, and amplicon sequence variant (ASV) generation was completed using QIIME 67 – 69 .
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### Anoxygenic phototroph of the Chloroflexota uses a type I reaction centre. (Nature 2024)

- DOI: 10.1038/s41586-024-07180-y | PMCID: PMC10972752 | PMID: 38480893
- Version used: **2019.10**
- Evidence: Sequence data analysis was performed for V4–V5 region samples using QIIME2 (v2019.10) 72 via the AXIOME3 pipeline 73 , commit 1ec1ea6 ( https://github.com/neufeld/axiome3 ), with default parameters.
- Full pipeline: read trimming [DADA2 v1.10.0] -> alignment/mapping [Clustal Omega v1.2.3, featureCounts] -> stage not stated [HMMER v3.1b, IQ-TREE v1.6.9, QIIME 2 v2019.10]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Version used: **2019.7**
- Evidence: ITS1 sequences were trimmed using ITSxpress (v1.7.4) 67 in QIIME 2 (v2019.7).
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Version used: **1.9.1**
- Evidence: The bioinformatics pipeline QIIME (v.1.9.1) was used as the informatics environment for all relevant processing of raw sequencing data and the determination of relative bacterial abundances.
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **2023.2**
- Evidence: Paired-end 16S rRNA gene sequences were demultiplexed and imported into QIIME2 (release 2023.2) for processing 64 .
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: Abundance tables were analysed using the QIIME2 software package.
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Version used: **2020.8**
- Evidence: Amplicon sequences were processed using Quantitative Insights into Microbial EcologyQ 2 (QIIME2, 2020.8) 55 workflow.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **2021.2.0**
- Evidence: QIIME 2 (v.2021.2.0) was used to process 16S sequencing reads 69 .
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Closed microbial communities self-organize to persistently cycle carbon. (PNAS 2021)

- DOI: 10.1073/pnas.2013564118 | PMCID: PMC8609437 | PMID: 34740965
- Evidence: Data were analyzed using QIIME and DADA2 pipelines.
- Full pipeline: stage not stated [DADA2, Python, QIIME 2]

### No evidence for colonization of oral bacteria in the distal gut in healthy adults. (PNAS 2021)

- DOI: 10.1073/pnas.2114152118 | PMCID: PMC8594488 | PMID: 34610963
- Evidence: Adaptor trimming was done in Quantitative Insights Into Microbial Ecology (QIIME) 2 using SHI7 ( 11 ), and the resulting demultiplexed fastq files were used as input to Divisive Amplicon Denoising Algorithm (DADA)2 ( 12 ).
- Full pipeline: read trimming [QIIME 2] -> alignment/mapping [BLAST] -> differential/statistical testing [R v3.4] -> stage not stated [DADA2, phyloseq]

### Human variation in gingival inflammation. (PNAS 2021)

- DOI: 10.1073/pnas.2012578118 | PMCID: PMC8271746 | PMID: 34193520
- Version used: **2018.2**
- Evidence: Analysis of merged 300-bp paired-end reads (average length 450 bp) was performed as previously described ( 57 , 58 ) using the Quantitative Insights into Microbial Ecology (QIIME2, version 2018.2) ( 59 ) following the Divisive Amplicon Denoising Algorithm 2 (DADA2) pipeline workflow ( 36 , 60 ) to generate ASVs.
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [DADA2, QIIME 2 v2018.2, R, phyloseq]

### An ecophysiological explanation for manganese enrichment in rock varnish. (PNAS 2021)

- DOI: 10.1073/pnas.2025188118 | PMCID: PMC8237629 | PMID: 34161271
- Evidence: 16S amplicon sequence reads from 61 varnish samples and 19 soil samples were processed using QIIME2 ( 69 ) to generate feature tables containing the frequencies of each unique sequence variant per sample.
- Full pipeline: read trimming [Trimmomatic] -> stage not stated [DADA2, ImageJ, QIIME 2, R]

### Carbonate-hosted microbial communities are prolific and pervasive methane oxidizers at geologically diverse marine methane seep sites. (PNAS 2021)

- DOI: 10.1073/pnas.2006857118 | PMCID: PMC8237665 | PMID: 34161255
- Evidence: The most abundant sequences in each cluster were selected as the representative sequences, which were then assigned taxonomy in QIIME using assign_taxonomy.py and the chimera-screened database called SILVA v128 SSURef.
- Full pipeline: dimensionality reduction/clustering [QIIME 2]

### Physical mixing in coastal waters controls and decouples nitrification via biomass dilution. (PNAS 2021)

- DOI: 10.1073/pnas.2004877118 | PMCID: PMC8106330 | PMID: 33903227
- Evidence: Illumina sequences of the 16S rRNA gene were processed using a QIIME 2–based workflow ( 70 ) as described in SI Appendix , SI Materials and Methods .
- Full pipeline: stage not stated [QIIME 2]

### The evolution and changing ecology of the African hominid oral microbiome. (PNAS 2021)

- DOI: 10.1073/pnas.2021655118 | PMCID: PMC8157933 | PMID: 33972424
- Evidence: We compared this method to results obtained using SourceTracker ( 28 )—which was performed on 16S-mapped reads filtered from shotgun data using EAGER (with comparative present-day modern human and environmental metagenomes as sources), followed by closed-reference clustering using QIIME ( 92 )—and found concordance between the two methods ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [BEAST, R] -> stage not stated [BEDTools]

### Legume-microbiome interactions unlock mineral nutrients in regrowing tropical forests. (PNAS 2021)

- DOI: 10.1073/pnas.2022241118 | PMCID: PMC7980381 | PMID: 33836596
- Evidence: ( C ) The QIIME 16S rRNA-based relative abundance of Acidobacteriia exhibits a negative correlation with soil pH (Pearson correlation test r = − 0.513, *** P = 0.0004, F = 15.00, DFd = 42).
- Full pipeline: quantification [QIIME 2]

### Type IV pili trigger episymbiotic association of Saccharibacteria with its bacterial host. (PNAS 2022)

- DOI: 10.1073/pnas.2215990119 | PMCID: PMC9894109 | PMID: 36454763
- Evidence: Samples were distinguished according to barcodes and primers, while clean reads were further processed using QIIME2 ( 38 ).
- Full pipeline: read trimming [fastp v0.20.0] -> stage not stated [ImageJ, Python, QIIME 2]

### Reactive granulopoiesis depends on T-cell production of IL-17A and neutropenia-associated alteration of gut microbiota. (PNAS 2022)

- DOI: 10.1073/pnas.2211230119 | PMCID: PMC9860329 | PMID: 36409919
- Evidence: Demultiplexed pair-end fastq files obtained from Miseq were analyzed by QIIME2 pipeline ver.2019.7 ( 60 ).
- Full pipeline: read trimming [QIIME 2] -> alignment/mapping [MAFFT] -> stage not stated [DADA2]

### Spatial turnover of soil viral populations and genotypes overlain by cohesive responses to moisture in grasslands. (PNAS 2022)

- DOI: 10.1073/pnas.2209132119 | PMCID: PMC9659419 | PMID: 36322723
- Evidence: OTU clustering was performed at a 97% sequence identity threshold with the QIIME ( 92 ) implementation of UCLUST v1.2.22 ( 91 ) following the open reference protocol against the SILVA database v132 ( 86 ).
- Full pipeline: read trimming [Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.4.2, SAMtools v1.11] -> quantification [DESeq2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [DESeq2, R v3.6] -> stage not stated [ggplot2, igraph]

### Active antibiotic resistome in soils unraveled by single-cell isotope probing and targeted metagenomics. (PNAS 2022)

- DOI: 10.1073/pnas.2201473119 | PMCID: PMC9546533 | PMID: 36161886
- Evidence: The raw data of 16S rRNA genes were assembled, quality-filtered, and analyzed in the QIIME ( 60 ).
- Full pipeline: visualisation [OrthoFinder v2.2.6] -> stage not stated [QIIME 2]

### &lt;i&gt;Lactobacillus crispatus&lt;/i&gt; Limits Bladder Uropathogenic &lt;i&gt;E. coli&lt;/i&gt; Infection by Triggering a Host Type I Interferon Response. (PNAS 2022)

- DOI: 10.1073/pnas.2117904119 | PMCID: PMC9388105 | PMID: 35939684
- Evidence: QIIME 2 microbiome analysis package was used to perform the bioinformatic analysis.
- Full pipeline: stage not stated [QIIME 2]

### A 3D-printed transepidermal microprojection array for human skin microbiome sampling. (PNAS 2022)

- DOI: 10.1073/pnas.2203556119 | PMCID: PMC9335308 | PMID: 35867832
- Evidence: Assigned paired-end reads of each sample were merged to raw tags by using Fast Length Adjustment of SHort reads (FLASH) (version 1.2.7), and the merged raw tags were filtered and developed into clean tags according to Quantitative Insights Into Microbial Ecology (QIIME) (version 1.7.0).
- Full pipeline: stage not stated [QIIME 2]

### The gut microbiome influences host diet selection behavior. (PNAS 2022)

- DOI: 10.1073/pnas.2117537119 | PMCID: PMC9169907 | PMID: 35439064
- Version used: **2020.4**
- Evidence: A total of 1,398,994 raw Illumina sequencing reads (mean of 22,206 per sample ( n = 63) ± 1,111 SE) were paired and quality filtered via the DADA2 pipeline ( 61 ) in QIIME2 (version 2020.4) ( 62 ) using default parameters.
- Full pipeline: visualisation [R] -> stage not stated [DADA2, QIIME 2 v2020.4]

### Top-down and bottom-up cohesiveness in microbial community coalescence. (PNAS 2022)

- DOI: 10.1073/pnas.2111261119 | PMCID: PMC8832967 | PMID: 35105804
- Version used: **1.9.0**
- Evidence: The sequencing reads were demultiplexed on QIIME 1.9.0 ( 40 ).
- Full pipeline: read trimming [QIIME 2 v1.9.0] -> stage not stated [DADA2]

### Microbiota configuration determines nutritional immune optimization. (PNAS 2023)

- DOI: 10.1073/pnas.2304905120 | PMCID: PMC10710091 | PMID: 38011570
- Version used: **2020.2**
- Evidence: 16S data were analyzed using QIIME 2 (v2020.2).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Bowtie2 v2.4.2, HOMER, HUMAnN v3.0, QIIME 2 v2020.2]

### Cooperation and cheating orchestrate Vibrio assemblages and polymicrobial synergy in oysters infected with OsHV-1 virus. (PNAS 2023)

- DOI: 10.1073/pnas.2305195120 | PMCID: PMC10556616 | PMID: 37751557
- Evidence: All bioinformatics processes used the next-generation microbiome bioinformatics platform QIIME 2 ( 67 ) (version 2020.2) and grouped sequences in ASV (Amplicon Sequence Variants) using DADA2 v1.14 ( 68 ).
- Full pipeline: quantification [DESeq2 v1.36.0] -> differential/statistical testing [phyloseq] -> structure determination [RAxML] -> stage not stated [DADA2 v1.14, QIIME 2]

### Multigenerational adversity impacts on human gut microbiome composition and socioemotional functioning in early childhood. (PNAS 2023)

- DOI: 10.1073/pnas.2213768120 | PMCID: PMC10372691 | PMID: 37463211
- Version used: **2.0**
- Evidence: QIIME v2.0 ( 62 ) was used to normalize microbiome data using rarefaction (depth = 5,777), which accounts for uneven sequencing depth between samples ( 63 and SI Appendix , Fig.
- Full pipeline: normalisation [QIIME 2 v2.0]

### Ecoevolutionary processes structure milk microbiomes across the mammalian tree of life. (PNAS 2023)

- DOI: 10.1073/pnas.2218900120 | PMCID: PMC10334807 | PMID: 37399384
- Evidence: We built a phylogenetic tree using FastTree ( 63 ) in QIIME2 ( 64 ), and combined data files for further analysis using the phyloseq package ( 65 ).
- Full pipeline: stage not stated [QIIME 2, R v4.0.3, lavaan, phyloseq]

### Diversity of plant DNA in stool is linked to dietary quality, age, and household income. (PNAS 2023)

- DOI: 10.1073/pnas.2304441120 | PMCID: PMC10319039 | PMID: 37368926
- Evidence: We subsequently converted the pipeline to use existing infrastructure for amplicon marker gene analysis maintained in QIIME2 ( 72 ), with paired-end adapter and primer trimming performed with cutadapt v.
- Full pipeline: read trimming [QIIME 2] -> stage not stated [Cutadapt v3.4, DADA2 v1.10.0, phyloseq v1.32.0]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Version used: **2024.2**
- Evidence: Illumina sequence reads were demultiplexed based on barcode sequences using iSeq software and processed in QIIME 2, version 2024.2 ( 93 ).
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### The telencephalon is a neuronal substrate for systemic inflammatory responses in teleosts via polyamine metabolism. (PNAS 2024)

- DOI: 10.1073/pnas.2404781121 | PMCID: PMC11441480 | PMID: 39284055
- Evidence: Using QIIME2, we computed various alpha diversity indices, including Shannon diversity, Chao1 richness, Pielou's evenness index, and Faith’s phylogenetic diversity (PD).
- Full pipeline: read trimming [DADA2] -> stage not stated [QIIME 2]

### The microbiota-dependent tryptophan metabolite alleviates high-fat diet-induced insulin resistance through the hepatic AhR/TSC2/mTORC1 axis. (PNAS 2024)

- DOI: 10.1073/pnas.2400385121 | PMCID: PMC11363250 | PMID: 39167602
- Version used: **1.8.0**
- Evidence: All these indices in our samples were calculated with QIIME (version 1.8.0).
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [QIIME 2 v1.8.0]

### Synergistic material-microbe interface toward deeper anaerobic defluorination. (PNAS 2024)

- DOI: 10.1073/pnas.2400525121 | PMCID: PMC11295042 | PMID: 39042683
- Version used: **2022.2**
- Evidence: Sequences were analyzed on the microbiome bioinformatics platform QIIME 2 v2022.2 ( https://qiime2.org/ ).
- Full pipeline: quality control [DADA2] -> stage not stated [QIIME 2 v2022.2]

### Climate mismatches with ectomycorrhizal fungi contribute to migration lag in North American tree range shifts. (PNAS 2024)

- DOI: 10.1073/pnas.2308811121 | PMCID: PMC11161776 | PMID: 38805274
- Evidence: 29 , which involved processing and denoising Illumina reads with DADA2 ( 62 ) and 454 pyrosequencing reads with QIIME and USEARCH ( 63 ).
- Full pipeline: stage not stated [DADA2, QIIME 2, R]

### 3D intrusions transport active surface microbial assemblages to the dark ocean. (PNAS 2024)

- DOI: 10.1073/pnas.2319937121 | PMCID: PMC11087786 | PMID: 38696469
- Evidence: Taxonomies were assigned to each ASV using classify-sklearn by QIIME2 ( 75 ) searching against the SILVA database release 138 ( 76 ).
- Full pipeline: read trimming [Cutadapt v1.13] -> stage not stated [QIIME 2, scikit-learn]

### Positive associations fuel soil biodiversity and ecological networks worldwide. (PNAS 2024)

- DOI: 10.1073/pnas.2308769121 | PMCID: PMC10861899 | PMID: 38285947
- Evidence: Bioinformatics processing was performed for raw sequences by combining QIIME ( 43 ), USEARCH ( 44 ), and UNOISE ( 45 ).
- Full pipeline: dimensionality reduction/clustering [igraph] -> stage not stated [QIIME 2, vegan]

### Constraining the oxygen requirements for modern microbial eukaryote diversity. (PNAS 2024)

- DOI: 10.1073/pnas.2303754120 | PMCID: PMC10786294 | PMID: 38165897
- Evidence: Sequences from prefilter and Sterivex filters were processed individually using the Quantitative Insights Into Microbial Ecology 2 (QIIME 2) software package ( 61 ).
- Full pipeline: dimensionality reduction/clustering [DADA2] -> differential/statistical testing [R] -> machine learning [scikit-learn] -> visualisation [ggplot2, tidyverse] -> stage not stated [QIIME 2]

### Soil microbial life history strategies covary with ecosystem multifunctionality across aridity gradients. (PNAS 2025)

- DOI: 10.1073/pnas.2511071122 | PMCID: PMC12541398 | PMID: 41066109
- Evidence: Raw sequencing reads were subsequently demultiplexed, quality-filtered, and processed using QIIME2 ( 54 ) to generate Amplicon Sequence Variants (ASVs) at 100% sequence identity.
- Full pipeline: read trimming [QIIME 2] -> dimensionality reduction/clustering [R]

### Ecosystem consequences of a nitrogen-fixing proto-organelle. (PNAS 2025)

- DOI: 10.1073/pnas.2503108122 | PMCID: PMC12452926 | PMID: 40920925
- Evidence: Sequences were denoised and demultiplexed using DADA2 in QIIME2 ( 57 ).
- Full pipeline: read trimming [DADA2, QIIME 2] -> stage not stated [R]

### Human land use promotes range expansion of soil protists from temperate to subtropical regions in China. (PNAS 2025)

- DOI: 10.1073/pnas.2413220122 | PMCID: PMC12318147 | PMID: 40694336
- Version used: **1.90**
- Evidence: The Quantitative Insights Into Microbial Ecology (QIIME v1.90) pipeline was used to generate high-quality processed and analyzed sequences ( 51 ).
- Full pipeline: differential/statistical testing [R v3.6.2, emmeans, lme4] -> stage not stated [QIIME 2 v1.90, vegan]

### Gut sulfide metabolism modulates behavior and brain bioenergetics. (PNAS 2025)

- DOI: 10.1073/pnas.2503677122 | PMCID: PMC12207524 | PMID: 40526718
- Evidence: Analysis of 16S sequencing was performed using QIIME2 ( 63 ).
- Full pipeline: alignment/mapping [DADA2] -> stage not stated [QIIME 2]

### Exposure and health risks of livestock air resistomes. (PNAS 2025)

- DOI: 10.1073/pnas.2403866122 | PMCID: PMC12067279 | PMID: 40294268
- Version used: **2020.11**
- Evidence: All 16S rRNA gene sequences were processed by QIIME2 (v2020.11), and OTUs were generated at 97% similarity.
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [Bracken, Kraken2, QIIME 2 v2020.11]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **2023.7**
- Evidence: Merging of paired-end reads, data quality filtering, and denoising was performed using QIIME2 v2023.7 ( 35 ) and the DADA2 plugin ( 36 ) to generate amplicon sequence variants (ASVs).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Eukaryotic phytoplankton drive a decrease in primary production in response to elevated CO&lt;sub&gt;2&lt;/sub&gt; in the tropical and subtropical oceans. (PNAS 2025)

- DOI: 10.1073/pnas.2423680122 | PMCID: PMC11929437 | PMID: 40063804
- Evidence: Quality control of the sequencing reads, identification of the amplicon sequencing variants (ASV, defined by 99% sequence similarity), and primary taxonomic affiliation based on SILVA SSU (version 138) were all conducted by QIIME2 workflow ( 76 ) and the R package DADA2 ( 77 ).
- Full pipeline: quality control [DADA2, QIIME 2, R] -> stage not stated [CDO, vegan]

### Quantifying compositional variability in microbial communities with FAVA. (PNAS 2025)

- DOI: 10.1073/pnas.2413211122 | PMCID: PMC11929398 | PMID: 40063791
- Evidence: Matrices of such abundances are central to software widely used for the analysis of microbiome data, such as Phyloseq ( 30 ) and QIIME2 ( 31 ).
- Full pipeline: quantification [QIIME 2] -> stage not stated [R, ape (R)]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Evidence: ASVs were generated using DADA2 ( 68 ), implemented within the QIIME 2 ( 69 ) suite (version 2022-2).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Industrialization increases the estrogen-recycling capacity of the gut microbiome. (PNAS 2026)

- DOI: 10.1073/pnas.2523589123 | PMCID: PMC13099636 | PMID: 41973926
- Evidence: Sequences from each dataset were imported into QIIME 2 (amplicon version 2023.9.1) ( 70 ), where they underwent pair joining (for paired-end reads only), denoising, quality filtering, and taxonomic assignment.
- Full pipeline: differential/statistical testing [R v4.2.1] -> stage not stated [QIIME 2]

