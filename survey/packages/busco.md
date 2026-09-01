# BUSCO

- **Category:** phylogenetics
- **Papers in survey:** 165
- **Journals:** PNAS (119), Nature (44), Cell (2)
- **Years:** 2021 (17), 2022 (33), 2023 (28), 2024 (29), 2025 (43), 2026 (15)
- **Versions named:** 5.2.2 (11), 3.0.2 (8), 4.0.5 (4), 5.1.2 (4), 5.4.7 (3), 5.3.2 (3), 5.4.3 (2), 5.4.4 (2), 4.0.6 (2), 5.7.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (11), machine learning (3), read trimming (2), variant calling (2), quality control (1), structure determination (1), differential/statistical testing (1)

## Papers

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **5.1.2**
- Evidence: 1.0.13) Parks et al., 2015 https://github.com/Ecogenomics/CheckM EukCC Saary et al., 2020 https://github.com/Finn-Lab/EukCC BUSCO v5.1.2 Simão et al., 2015 https://busco.ezlab.org/ Mfannot N/A https://github.com/BFL-lab/Mfannot PEAR version 0.9.10 Zhang et al., 2014 https://cme.h-its.org/exelixis/web/software/pear/ cutadapt version 1.17 Martin, 2011 https://cutadapt.readthedocs.io/en/v1.17/ QIIME ...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **3.0.1**
- Evidence: 87 http://genome.ucsc.edu BUSCO v3.0.1 Simão et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### A chickpea genetic variation map based on the sequencing of 3,366 genomes. (Nature 2021)

- DOI: 10.1038/s41586-021-04066-1 | PMCID: PMC8612933 | PMID: 34759320
- Evidence: Then, the ‘fabales’ genes were downloaded from the BUSCO 17 database (odb10), which contains 5,366 single-copy orthologues to predict the genes for 195 wild species accessions, CDC Frontier genome 11 and M. truncatula genome 18 (as outgroup) using GeneWise 47 v.2.4.1 with the parameters “-both -sum -genesf”.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BUSCO, PLINK, RAxML, VCFtools]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: Evaluation Detailed methods for other types of evaluation, including BUSCO runs, mis-join and missed-join identification, reliable blocks, collapsed repeats, telomeres, RNA-seq and ATAC–seq mapping, and false gene duplications are in the Supplementary Methods .
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: The gene annotation—which is derived from Illumina RNA sequencing ( n libraries = 88, n conditions = 18, >3 billion reads) and PacBio Iso-Seq ( n conditions = 9, > 4.5 million reads, Supplementary Data 3 )—encompasses 80,278 primary and 49,664 alternative transcripts and is as complete as the genome assembly (BUSCO = 99.4%) (Extended Data Fig.
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Evidence: Completeness of the de novo-assembled transcriptome was assessed with BUSCO v.3 49 using core vertebrate genes and Vertebrata genes (vertebrata_odb9 database) in the gVolante webserver 50 .
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Version used: **3.1.0**
- Evidence: BUSCO analyses Busco completeness for the 41 assemblies was calculated with BUSCO v3.1.0 using the mammalia_odb9 lineage set ( https://busco-archive.ezlab.org/v3/ ) 82 .
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Evidence: The completeness of these assemblies was assessed by BUSCO analysis, which shows an average of 96.2% single-copy Solanales genes completely assembled (Extended Data Fig.
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **4.1.4**
- Evidence: The assembly completeness in genic regions was evaluated using the solanales_odb10 database (for Solanaceae species) of BUSCO v.4.1.4 (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### The mosaic oat genome gives insights into a uniquely healthy cereal crop. (Nature 2022)

- DOI: 10.1038/s41586-022-04732-y | PMCID: PMC9159951 | PMID: 35585233
- Version used: **5.1.2**
- Evidence: 1a and Supplementary Table 1 ), with a BUSCO (v5.1.2; ref.
- Full pipeline: visualisation [WGCNA] -> stage not stated [BUSCO v5.1.2]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Version used: **5.0.0**
- Evidence: Assembly completeness was evaluated using BUSCO (v.5.0.0) 65 with the plant dataset (poales_odb10).
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Evidence: We assessed genome sequence and protein datasets using BUSCO (v.5) 96 .
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: We evaluated the progress of the polishing process with the BUSCO tool (v.3.0.2) that seeks widely represented single-copy gene families in the assembly 65 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **3.0.2b**
- Evidence: 59 ); and (2) BUSCO v3.0.2b 60 analysis with Embryophyta database 9.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Evidence: Merqury (v.1.1) 56 and BUSCO (v.5) 57 were used to assess genome completeness and to evaluate the quality of the assembly (Supplementary Fig.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Version used: **3.0.2**
- Evidence: BUSCO analysis was conducted on the contig assemblies using BUSCO (v.3.0.2) with embryophyta_odb9 dataset 14 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Version used: **5.4.7**
- Evidence: BUSCO (v5.4.7) 54 was used to check the quality of the assembly, using the lineage dataset mucorales_odb10, giving the following result: C (complete): 97.5%, S (single-copy): 5.1%, D (duplicated): 92.4%, F (fragmented): 1.7%, M (missing): 0.8%, n (number of genes): 2,449.
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **5.3.1**
- Evidence: For assembly validation and quality control, we used QUAST (v5.0.2) 51 to calculate the assembly metrics, Merqury (v1.3) 52 to estimate the base-call accuracy and k -mer completeness based on 21-mer produced from the short-read WGS data 14 and BUSCO (v5.3.1) 17 with the embryophyta_odb10 database to determine the completeness of each genome assembly.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **5.5.0**
- Evidence: Assembly completeness was also assessed with BUSCO 5.5.0 (ref.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: Protein-coding genes Our gene annotations (Supplementary Table 32 and Methods ) indicated the presence of a high percentage of BUSCO genes on the X chromosomes (Supplementary Table 33 ), and of most previously known Y chromosome genes (Fig.
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **5.4.4**
- Evidence: The representation of mammalian universal single-copy orthologues in the different genomes was assessed with BUSCO (v.5.4.4) 27 using the curated mammalian v.10 database 19 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Evidence: The primary annotation is highly complete (BUSCO = 99.8% total, 99.3% duplicate completeness) 22 with 194,593 coding sequences (and 105,138 alternative spliced transcripts).
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Evidence: The final BUSCO score (Metazoa) is C:90.0% (S:89.8%, D:0.2%), F:4.0%, M:6.0%, n:954.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Evidence: 1c ), and completeness averaged 99.1% by BUSCO, closely matching the reference score 37 of 99.4% (Extended Data Fig.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Evidence: To assess gene completeness, we used compleasm 56 , a tool based on BUSCO.
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **4.0.5**
- Evidence: We then ran a BUSCO (v.4.0.5) 61 analysis to evaluate the completeness of the genome.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **5.4.1**
- Evidence: The assembly was evaluated with BUSCO (v.5.4.1) with a final score of C:94.3% [S:91.3%, D:3.0%], F:1.3%, M:4.4% (n:954, metazoa_odb10).
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Evidence: We benchmarked the quality of the gene predictions against the BUSCO Poales dataset.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **5.4.0**
- Evidence: We used Benchmarking Universal Single-Copy Orthologues (BUSCO, v.5.4.0) 57 to evaluate the completeness of 35 chromosome-level scaffolds and for each of the four subgenomes.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **5.4.3**
- Evidence: BUSCO v5.4.3 79 with the eudicots_odb10 dataset and assembly-stats v1.0.1 ( https://github.com/sanger-pathogens/assembly-stats ) were used on all assemblies to measure completeness and contiguity.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **5.2.2**
- Evidence: For the initial training of predictors, Funannotate-predict also uses BUSCO (v.5.2.2) 78 for initial Augustus species training.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Version used: **5.1.2**
- Evidence: Completeness was measured with the fraction of conserved orthologues recovered by BUSCO v.5.1.2 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Version used: **5.2.2**
- Evidence: Base quality and sequence-level completeness of the genome assemblies were assessed using Merqury (v.1.3) 23 , and gene set completeness was evaluated using BUSCO (v.5.2.2) 24 .
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: First, we evaluated gene completeness using the embryophyta_odb10 database, using BUSCO 72 (v.5.2.2), and repeat completeness on the basis of the LTR assembly index (LAI) 25 , using LTR_retriever (v.2.9.0) with parameters ‘-maxlenltr 7000’.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Evidence: Moreover, small contigs (<100,000 bp) with >80% of the sequence mapping to a named chromosome that contained one or more duplicated BUSCO genes, but no single BUSCO genes, were also removed using a Python script.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **5.1.1**
- Evidence: First, we used BUSCO v.5.1.1 (Benchmarking Universal Single-Copy Orthologs; odb10 dataset) with arguments: --mode ‘genome’ to compare the percentage of completely detected near-universally conserved mammalian genes across different assemblies 71 .
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **5.4.4**
- Evidence: BUSCO (v.5.4.4) 23 was used to evaluate assembly quality with the embryophyte_odb10 protein database.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: Completeness To evaluate genome completeness, we first used the BUSCO 51 tool with the embryophyta_odb10 database to assess the presence of conserved single-copy orthologous genes.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### Telomere-to-telomere assembly using HERRO-corrected Nanopore Simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10563-y | PMCID: PMC13323052 | PMID: 42045451
- Evidence: Evaluation of gene completeness We evaluated the gene completeness of assemblies using three different methods—asmgene, BUSCO 53 , 54 and compleasm 55 .
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BEDTools, BUSCO, Canu, Flye, QUAST]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **5.7.0**
- Evidence: BUSCO (5.7.0) 62 was also used to validate the completeness of assembly with actinopterygii_odb10 as a database.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Evidence: Similar to many recent upgrades of older genome sequences, repetitive regions in V5 are more extensive (for example, 2.86 times more contiguous centromere 20 blocks), whereas the gene-rich portions are moderately improved (BUSCO genome assembly completeness scores of 98.3% for V3 and 99.7% for V5).
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Limited thermal tolerance in tropical insects and its genomic signature. (Nature 2026)

- DOI: 10.1038/s41586-026-10155-w | PMCID: PMC12999521 | PMID: 41781608
- Evidence: For testing robustness of results, we conducted analyses with data from all genomes, only high-quality genomes (BUSCO > 89.9, N50 > 300 kb), and only for proteins which were covered by all insect species.
- Full pipeline: structure determination [phytools] -> visualisation [phytools] -> stage not stated [AlphaFold, BUSCO, Conda]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Evidence: Second, SNAP 68 , was trained using 194 eukaryotic BUSCO genes (v.2.0) 69 identified in the genome, yielding 15,083 gene models.
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Evidence: Genome completeness was then assessed with BUSCO, which yielded expected results for Hanseniaspora species 71 ( Supplementary Table 1 ).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Version used: **5.4.7**
- Evidence: The quality of canonical proteins from 154 genomes were assessed by BUSCO v.5.4.7 (ref.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: We used benchmarking universal single-copy orthologs (BUSCO 18 ) to assess the completeness of our gene annotations.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Response of an Afro-Palearctic bird migrant to glaciation cycles. (PNAS 2021)

- DOI: 10.1073/pnas.2023836118 | PMCID: PMC8719893 | PMID: 34949638
- Evidence: Genome completeness was measured with BUSCO ( 61 ).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> registration [GATK, Picard] -> differential/statistical testing [R v3.4.2] -> stage not stated [ANGSD, BEDTools, BUSCO, RepeatMasker]

### Adaptive divergence in shoot gravitropism creates hybrid sterility in an Australian wildflower. (PNAS 2021)

- DOI: 10.1073/pnas.2004901118 | PMCID: PMC8617494 | PMID: 34789571
- Evidence: Although 843 MB is much shorter than the expected haploid size of 1.38 GB ( 72 ) of the whole genome, the Benchmarking Universal Single-Copy Orthologs (BUSCO) gene content completeness of 84% (5% fragmented and 11% missing) suggests that this assembly is primarily missing intergenic repetitive DNA sequences, which are notoriously difficult to assemble.
- Full pipeline: alignment/mapping [BLAST] -> variant calling [SAMtools v0.1.16] -> stage not stated [BUSCO, ImageJ, R]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: The completeness of the genome assembly was also evaluated using the BUSCO software ( 22 ).
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Genome evolution of the psammophyte <i>Pugionium</i> for desert adaptation and further speciation. (PNAS 2021)

- DOI: 10.1073/pnas.2025711118 | PMCID: PMC8545485 | PMID: 34649989
- Evidence: Moreover, 97.9 and 97.4% of the 2,326 eudicot-specific BUSCO genes were identified in the genome assemblies of P. cornutum and P. dolabratum , respectively ( SI Appendix , Table S7 ).
- Full pipeline: stage not stated [ADMIXTURE, AUGUSTUS, BUSCO, GATK, RepeatMasker]

### Comparative genomics provides insights into the aquatic adaptations of mammals. (PNAS 2021)

- DOI: 10.1073/pnas.2106080118 | PMCID: PMC8449357 | PMID: 34503999
- Evidence: BUSCO (Benchmarking Universal Single-Copy Orthologs) (version 3.0.2) ( 12 ) was used to assess the quality of the assemblies, revealing an average genome completeness of 90.98% ( SI Appendix , Table S6 ).
- Full pipeline: stage not stated [BUSCO]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **3.0.2**
- Evidence: The assemblies were checked for quality and completeness by calculating standard genome statistics and by checking presence, fragmentation, and duplication of arthropod core genes using CEGMA v2.5 and BUSCO v3.0.2 ( 67 , 68 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### Ancestral polymorphisms shape the adaptive radiation of <i>Metrosideros</i> across the Hawaiian Islands. (PNAS 2021)

- DOI: 10.1073/pnas.2023801118 | PMCID: PMC8449318 | PMID: 34497122
- Evidence: The assembly was evaluated with 2,326 Benchmarking Universal Single-Copy Ortholog (BUSCO) genes from eudicots, and 2,183 genes (93.8%) were present.
- Full pipeline: stage not stated [ADMIXTURE, BUSCO]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Evidence: Estimation of genome recovery was calculated with BUSCO v3 (Benchmarking Universal Single-Copy Orthologs) ( 79 ) using the Eukaryota_odb9 dataset ( Dataset S2 ).
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Three genomes in the algal genus <i>Volvox</i> reveal the fate of a haploid sex-determining region after a transition to homothallism. (PNAS 2021)

- DOI: 10.1073/pnas.2100712118 | PMCID: PMC8166075 | PMID: 34011609
- Evidence: Assembly quality of the three genomes was high based on the presence of the vast majority of benchmarking universal single-copy orthologs (BUSCO) reference genes ( 30 ) (94.9 to 98.1% complete genes) ( SI Appendix , Table S2 ).
- Full pipeline: alignment/mapping [AUGUSTUS] -> stage not stated [BUSCO, Pilon v1.22]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Version used: **3.0.2**
- Evidence: BUSCO (version 3.0.2) ( 68 ) with 1,375 single-copy orthologs was used to assess the completeness of the genome assembly.
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### The giant axolotl genome uncovers the evolution, scaling, and transcriptional control of complex gene loci. (PNAS 2021)

- DOI: 10.1073/pnas.2017176118 | PMCID: PMC8053990 | PMID: 33827918
- Evidence: ...982) ( 2 , 21 ), to the genome to produce gene models representing 35,529 annotated genomic loci with a Benchmarking Universal Single-Copy Orthologs (BUSCO) C-score of 88.4% (vertebrate database) ( 22 ).
- Full pipeline: alignment/mapping [StringTie] -> stage not stated [BLAST, BUSCO]

### The evolution of ancestral and species-specific adaptations in snowfinches at the Qinghai-Tibet Plateau. (PNAS 2021)

- DOI: 10.1073/pnas.2012398118 | PMCID: PMC8020664 | PMID: 33753478
- Evidence: Using benchmarks against universal single-copy orthologs of birds (BUSCO, ref.
- Full pipeline: stage not stated [BUSCO, Metascape, R]

### <i>Trichoderma reesei</i> Rad51 tolerates mismatches in hybrid meiosis with diverse genome sequences. (PNAS 2021)

- DOI: 10.1073/pnas.2007192118 | PMCID: PMC7923544 | PMID: 33593897
- Evidence: Second, the OrthoDB-based BUSCO software program was also used to quantitatively measure the completeness of genome assembly.
- Full pipeline: stage not stated [BUSCO]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: After an initial run with MAKER, BUSCO- v4.1.1 ( 77 – 79 ) was used to assess the completeness and quality of the annotation.
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: Furthermore, we identified 2,272 (87.9%, SI Appendix , Table S5 ) of the conserved vertebrate BUSCO genes, indicating that the N. parkeri assembled genome is of high integrity and accuracy.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Version used: **5.2.2**
- Evidence: Median coverage was calculated for each read set by mapping to the M. oreades reference genome and focusing only on single copy ortholog regions as identified by BUSCO v5.2.2 with the Agaricomycetes_odb10 database ( 99 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Evolution of the ancestral mammalian karyotype and syntenic regions. (PNAS 2022)

- DOI: 10.1073/pnas.2209139119 | PMCID: PMC9550189 | PMID: 36161960
- Version used: **5.2.2**
- Evidence: We evaluated genome completeness of the reconstructed RACFs using the BUSCO (version 5.2.2) software with the mammalian OrthoDB version 10 dataset ( 38 ).
- Full pipeline: structure determination [BUSCO v5.2.2] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.29.0]

### Metabolic novelty originating from horizontal gene transfer is essential for leaf beetle survival. (PNAS 2022)

- DOI: 10.1073/pnas.2205857119 | PMCID: PMC9546569 | PMID: 36161953
- Evidence: The quality of the assembled genome was assessed by BUSCO ver.4 ( 71 ) with insecta_odb10 database, and the final genome assembly covered 92.0% of complete BUSCOs with having 2.4% fragmented and 5.6% missing BUSCOs.
- Full pipeline: stage not stated [BLAST, BUSCO, Flye v2.8.3, InterProScan, R v9.4]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Evidence: Genome completeness was assessed by three methods: 1) Benchmarking universal single-copy orthologs (BUSCO) evaluation, resulting in a BUSCO-estimated pygmy loris genome integrity of 89.06% (complete BUSCOs/total BUSCOs) ( Dataset S1, Table S14 ) ( 57 ); 2) core eukaryotic genes mapping approach (CEGMA) evaluation ( 58 ), whereby assembly completeness was assessed by mapping 248 conserved core euka...
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **3.0.2**
- Evidence: BUSCO (v3.0.2) ( 23 ) was used to evaluate the assembly completeness of three cotton genomes with 1,440 embryophyte genes from the “Embryophyta_odb9” database.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Diploid-dominant life cycles characterize the early evolution of Fungi. (PNAS 2022)

- DOI: 10.1073/pnas.2116841119 | PMCID: PMC9457484 | PMID: 36037379
- Evidence: To conduct genome-scale phylogenomic analyses that excluded paralogous sequences we generated a filtered set of 487 genes derived from the 758 conserved markers comprising the BUSCO fungi_odb10 database ( 71 ).
- Full pipeline: variant calling [GATK, SAMtools v1.5] -> structure determination [phytools] -> stage not stated [BUSCO]

### Comparative genomics of mortal and immortal cnidarians unveils novel keys behind rejuvenation. (PNAS 2022)

- DOI: 10.1073/pnas.2118763119 | PMCID: PMC9459311 | PMID: 36037356
- Evidence: The quality of both assemblies, measured with Benchmarking sets of Universal Single-Copy Orthologs (BUSCO), indicates coverages of 78.88% and 88.78%, respectively ( SI Appendix , section 3.1 and Table S1 ).
- Full pipeline: alignment/mapping [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [AlphaFold v2.1.2, BUSCO, ChimeraX, GSEA, fgsea]

### Signatures of adaptive evolution in platyrrhine primate genomes. (PNAS 2022)

- DOI: 10.1073/pnas.2116681119 | PMCID: PMC9436310 | PMID: 35994669
- Version used: **3.0.2**
- Evidence: We evaluated completeness of the genome assembly by its estimated gene content using CEGMA v2.5 ( 53 ) and BUSCO v3.0.2 ( 52 ) to calculate the proportion of 248 CEGs or 6,192 Euarchontoglires-specific conserved single-copy orthologs, respectively, that were either complete, fragmented, or missing.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BUSCO v3.0.2, RepeatMasker v4.0.7]

### The evolution of synaptic and cognitive capacity: Insights from the nervous system transcriptome of &lt;i&gt;Aplysia&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122301119 | PMCID: PMC9282427 | PMID: 35867761
- Evidence: S4 for examples of improved Reference Protein coverage); this is a more sensitive measure of transcriptome completeness than BUSCO proteins ( Fig.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> differential/statistical testing [RAxML] -> stage not stated [BUSCO]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **3.0.2**
- Evidence: To obtain quantitative measures of the completeness of the genome assembly, we used BUSCO v.3.0.2 ( 73 ) with BLAST+ v.2.2.28+, HMMER v.3.1b2, and AUGUSTUS v.3.3.2.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Leafy and weedy seadragon genomes connect genic and repetitive DNA features to the extravagant biology of syngnathid fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2119602119 | PMCID: PMC9245644 | PMID: 35733255
- Evidence: We evaluated assembly quality and completeness using Quast ( 20 ) and BUSCO ( 21 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [InterProScan, STAR] -> dimensionality reduction/clustering [BLAST] -> stage not stated [BUSCO, Flye, RepeatMasker]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Evidence: Transcriptome completeness and heterogeneity were determined by assessing genome completeness via Benchmarking Universal Single-Copy Orthologs ( 77 ) (BUSCO ver.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### Repeated translocation of a supergene underlying rapid sex chromosome turnover in <i>Takifugu</i> pufferfish. (PNAS 2022)

- DOI: 10.1073/pnas.2121469119 | PMCID: PMC9191631 | PMID: 35658077
- Evidence: A Benchmarking Universal Single-Copy Orthologs (BUSCO) search against the 4,584 single-copy orthologs for Actinopterygii suggested that the assembly was missing only 2.3% of the core genes ( SI Appendix , Table S12 ).
- Full pipeline: alignment/mapping [BWA, minimap2] -> stage not stated [BUSCO, RAxML v0.8]

### Gene-rich X chromosomes implicate intragenomic conflict in the evolution of bizarre genetic systems. (PNAS 2022)

- DOI: 10.1073/pnas.2122580119 | PMCID: PMC9191650 | PMID: 35653559
- Evidence: We assessed the quality of all genomes using BUSCO ( 47 ), to determine the proportion of single copy orthologs expected to be present in either insects (insecta_odb10 for fungus gnat species) or arthropods (for springtails) in the genome assemblies ( SI Appendix , Fig.
- Full pipeline: stage not stated [BUSCO, SPAdes v3.13.1]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: The quality of the genome assemblies, including the ones previously published by our group, was checked by BUSCO ( 38 ) and CEGMA ( 39 ) analyses ( SI Appendix , Table S1 ).
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Genomic insights into zokors' phylogeny and speciation in China. (PNAS 2022)

- DOI: 10.1073/pnas.2121819119 | PMCID: PMC9171634 | PMID: 35512099
- Evidence: ...e length, bp 227,920,291 The genome assembly covered 3,967 (∼97.0%) of the 4,104 total orthologs in the Benchmarking Universal Single-Copy Orthologs (BUSCO) database, indicating completeness of the genome ( SI Appendix , Figs.
- Full pipeline: alignment/mapping [GATK] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BUSCO, RAxML, VCFtools]

### <i>duper</i> is a null mutation of Cryptochrome 1 in Syrian hamsters. (PNAS 2022)

- DOI: 10.1073/pnas.2123560119 | PMCID: PMC9170138 | PMID: 35471909
- Version used: **4.0.6**
- Evidence: The resulting assembly of error-corrected contigs was assessed for completeness using lineage-specific single-copy orthologs (mammalia_odb10) with BUSCO v4.0.6 ( 19 ).
- Full pipeline: stage not stated [BUSCO v4.0.6, Flye v2.7, GATK, SAMtools, SnpEff]

### Genomic adaptations for arboreal locomotion in Asian flying treefrogs. (PNAS 2022)

- DOI: 10.1073/pnas.2116342119 | PMCID: PMC9060438 | PMID: 35286217
- Evidence: We assessed assembly quality using benchmarking of universal single-copy orthologs (BUSCO v3) ( 16 ) and retrieved 83.33% and 87.94% complete BUSCO genes for the R. kio and R. dugritei genomes, respectively ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> differential/statistical testing [DESeq2 v1.30.0, featureCounts] -> stage not stated [BUSCO]

### <i>PRDM9</i> losses in vertebrates are coupled to those of paralogs <i>ZCWPW1</i> and <i>ZCWPW2</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2114401119 | PMCID: PMC8892340 | PMID: 35217607
- Evidence: Of these, we filtered out 32 species that were missing 10 or more BUSCO core genes (out of a total of 255 genes) ( 54 ), reasoning that their genomes were sufficiently incomplete that they may be missing orthologs by chance ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [BLAST, Clustal Omega] -> stage not stated [BUSCO, R]

### An in-frame deletion mutation in the degron tail of auxin coreceptor <i>IAA2</i> confers resistance to the herbicide 2,4-D in <i>Sisymbrium orientale</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2105819119 | PMCID: PMC8892348 | PMID: 35217601
- Evidence: GSE159202 ) (BUSCO score of 98.4%, Eukaryota ODB10).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [SAMtools] -> differential/statistical testing [R v3.3, edgeR] -> stage not stated [BCFtools, BUSCO]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: The BUSCO score ( 58 ) was used to check for the completeness of the gene sets in the assembly.
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: Annotation completeness was assessed using Benchmarking Universal Single-Copy Orthologs (BUSCO) with the poales_odb10.2019–11-20 database of 4,896 conserved genes.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Domoic acid biosynthesis in the red alga <i>Chondria armata</i> suggests a complex evolutionary history for toxin production. (PNAS 2022)

- DOI: 10.1073/pnas.2117407119 | PMCID: PMC8833176 | PMID: 35110408
- Version used: **4.0.5**
- Evidence: Genome contiguity and completeness was assessed with the eukaryota benchmarking universal single-copy orthologs (BUSCO v4.0.5) database ( 22 ).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [AlphaFold, BLAST, BUSCO v4.0.5]

### Sequence locally, think globally: The Darwin Tree of Life Project. (PNAS 2022)

- DOI: 10.1073/pnas.2115642118 | PMCID: PMC8797607 | PMID: 35042805
- Evidence: The outer circle (black) shows estimated genome size and the middle ring (purple) the BUSCO (Eukaryota ortholog set) completeness of preliminary assemblies.
- Full pipeline: stage not stated [BUSCO]

### Green plant genomes: What we know in an era of rapidly expanding opportunities. (PNAS 2022)

- DOI: 10.1073/pnas.2115640118 | PMCID: PMC8795535 | PMID: 35042803
- Evidence: Gene space completeness as evaluated by single-copy benchmarks, including universal single-copy orthologues (BUSCO), core gene families (CoreGFs), or the online platform for plant comparative genomes PLAZA, should be considered in light of species composition of the source databases and methodologies ( 72 ).
- Full pipeline: stage not stated [BUSCO]

### Standards recommendations for the Earth BioGenome Project. (PNAS 2022)

- DOI: 10.1073/pnas.2115639118 | PMCID: PMC8795494 | PMID: 35042802
- Evidence: ...teness, more than 90% of the sequence assigned to candidate chromosomal sequences, more than 90% single copy conserved genes [e.g., as inferred using BUSCO ( 18 )] complete and single copy, and more than 90% of transcripts from the same species mappable.
- Full pipeline: stage not stated [BUSCO]

### Scattered differentiation of unlinked loci across the genome underlines ecological divergence of the selfing grass &lt;i&gt;Brachypodium stacei&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2304848120 | PMCID: PMC10636366 | PMID: 37903254
- Evidence: Then, 98.6% of the BUSCO ortholog and homeolog genes could be completely predicted in Bsta-ECI, which were slightly higher than those in the previous assembly ( SI Appendix , Fig.
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BUSCO, HISAT2, IQ-TREE v1.6.12]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Evidence: To further evaluate the completeness of L. chinensis genome, the genome assembly was checked with benchmarking universal single-copy orthologs (BUSCO) ( 53 ) from the Embryophyta lineage and the LTR Assembly Index (LAI) ( 54 ).
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### Functional genomic diversity is correlated with neutral genomic diversity in populations of an endangered rattlesnake. (PNAS 2023)

- DOI: 10.1073/pnas.2303043120 | PMCID: PMC10614936 | PMID: 37844221
- Evidence: BUSCO completeness was calculated as 91.1% complete, with 4.4% fragmented and 4.5% missing BUSCOs.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, SnpEff v4.3] -> stage not stated [BUSCO, R]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Version used: **5.4.2b**
- Evidence: Next, genome completeness was assessed by BUSCO v5.4.2b ( 22 ).
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Evidence: The quality of the gene models was assessed with two metrics: the AED in MAKER 3.01.03 ( 75 ) and the BUSCO score (v5.1.2) ( 79 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Version used: **5.2.2**
- Evidence: The quality and completeness of the pangenome were assessed using QUAST v5.0.2 ( 78 ) and BUSCO v5.2.2 ( 79 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Evidence: Genome completeness was assessed using the Sordariomyceta odb9 set of BUSCO (v3) ( 38 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### Complex evolutionary processes maintain an ancient chromosomal inversion. (PNAS 2023)

- DOI: 10.1073/pnas.2300673120 | PMCID: PMC10288594 | PMID: 37311002
- Version used: **4.0.5**
- Evidence: Based on BUSCO version 4.0.5 with the eukaryota_odb10 database (70 species, 255 BUSCOs), the assembly included 216 complete BUSCOs (212 single copy and four duplicated; 84.7%), 15 fragmented BUSCOs (5.9%) and 24 missing BUSCOs (9.4%).
- Full pipeline: alignment/mapping [RepeatMasker v4.0.7, SAMtools v1.5] -> variant calling [BCFtools v1.6] -> stage not stated [BEAST v2.6.6, BUSCO v4.0.5, R v4.0.2]

### Disruption of the standard kinetochore in holocentric <i>Cuscuta</i> species. (PNAS 2023)

- DOI: 10.1073/pnas.2300877120 | PMCID: PMC10214151 | PMID: 37192159
- Evidence: Completeness and contiguity of assemblies were evaluated using BUSCO [v5.2.2; ( 51 )] and QUAST [v5.0.2; ( 52 )].
- Full pipeline: alignment/mapping [SAMtools, STAR] -> structure determination [StringTie] -> stage not stated [BLAST, BUSCO, OrthoFinder, QUAST]

### Allelic resolution of insect and spider silk genes reveals hidden genetic diversity. (PNAS 2023)

- DOI: 10.1073/pnas.2221528120 | PMCID: PMC10161007 | PMID: 37094147
- Evidence: Comparison of genome and gene sequences from organisms used in this study Order Species Contig N50 (Mbp) BUSCO % complete Gene No. of amino acids allele 1 No. of amino acids allele 2 % complete repeat indels (CRI) Study Trichoptera Arctopsyche grandis 9.4 98.9 H-fibroin 6,375 5,696 97.6 Present study Trichoptera Atopsyche davidsoni 14.1 98.8 H-fibroin 7,878 6,992 94.1 Ríos-Touma et al.
- Full pipeline: stage not stated [BUSCO]

### Genomic and structural basis for evolution of tropane alkaloid biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2302448120 | PMCID: PMC10151470 | PMID: 37068250
- Evidence: The assembly quality of these two genomes was high based on benchmarking universal single-copy orthologs (BUSCO) analysis (93.40 to 94.49% complete BUSCO genes), core eukaryotic gene-mapping approach analysis (94.76 to 96.77% core eukaryotic genes), and short-read mapping analysis (98.88 to 99.83% map rates) ( SI Appendix , Tables S2–S4 ).
- Full pipeline: alignment/mapping [BUSCO, MAFFT] -> dimensionality reduction/clustering [OrthoFinder] -> visualisation [PyMOL v2.4] -> stage not stated [AlphaFold, AutoDock Vina v1.1.2, IQ-TREE]

### Standing genetic variation fuels rapid evolution of herbicide resistance in blackgrass. (PNAS 2023)

- DOI: 10.1073/pnas.2206808120 | PMCID: PMC10120058 | PMID: 37043536
- Evidence: ...size 3,529,081,863 bp Chromosome N50 554,019,051 bp Largest chromosome 807,086,175 bp Number of protein-coding genes 50,029 Mean gene length 2,789 bp BUSCO score C:94.6% [S:82.0%, D:12.6%], F:0.9%, M:4.5% TE content Class I [LTR: 63.8%, non-LTR: 0.1%] Class II [TIR: 10.9%, Helitron: 8.2%] Other repeated regions: 2.15% Contig metrics are shown before deduplication.
- Full pipeline: read trimming [BUSCO] -> alignment/mapping [MAFFT v7.407] -> variant calling [MAFFT v7.407] -> visualisation [MAFFT v7.407] -> stage not stated [ADMIXTURE, ANGSD v0.930, GATK v4.1.3.0, InterProScan]

### The <i>Holothuria leucospilota</i> genome elucidates sacrificial organ expulsion and bioadhesive trap enriched with amyloid-patterned proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2213512120 | PMCID: PMC10120082 | PMID: 37036994
- Evidence: It encompasses 2,312 scaffolds with contig N50 and scaffold N50 sizes of 55.5 Mb and 56.1 Mb ( Dataset S1 E ), respectively, and features 97.63% high-quality read alignments ( Dataset S1 F ) and 96.3% BUSCO completeness ( Dataset S1 G ), indicating a significant improvement to all previously reported echinoderm genomes (contig N50: 0.01 to 0.19 Mb; scaffold N50: 0.07 to 1.52 Mb) ( 16 – 19 ).
- Full pipeline: alignment/mapping [BUSCO, BWA, MAFFT, RAxML] -> normalisation [DESeq2] -> visualisation [MAFFT, RAxML] -> stage not stated [AlphaFold, InterProScan]

### The expansion of agriculture has shaped the recent evolutionary history of a specialized squash pollinator. (PNAS 2023)

- DOI: 10.1073/pnas.2208116120 | PMCID: PMC10104555 | PMID: 37011184
- Version used: **4.0.6**
- Evidence: Assembly completeness was 97.9% (5870 of 5991 BUSCOs), assessed via BUSCO v4.0.6 using the Hymenoptera reference set ( 41 ).
- Full pipeline: alignment/mapping [AUGUSTUS] -> variant calling [GATK] -> stage not stated [BUSCO v4.0.6, GSEA, R]

### The genomics of linkage drag in inbred lines of sunflower. (PNAS 2023)

- DOI: 10.1073/pnas.2205783119 | PMCID: PMC10083583 | PMID: 36972449
- Version used: **5.1.2**
- Evidence: Details of the annotation processes, along with assessment results generated with BUSCO v5.1.2 (-m prot -l embryophyta_odb10) software ( 79 ), are provided in Dataset S3 .
- Full pipeline: alignment/mapping [GATK] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.1.2, Snakemake, VCFtools]

### Euglenozoan kleptoplasty illuminates the early evolution of photoendosymbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2220100120 | PMCID: PMC10041101 | PMID: 36927158
- Evidence: The completeness of the transcriptomes was estimated with Benchmarking Universal Single-Copy Orthologs (BUSCO) v.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [IQ-TREE, MAFFT] -> differential/statistical testing [IQ-TREE] -> stage not stated [BUSCO, SPAdes v3.10.1]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Evidence: The new haploid amphioxus genomes have an assembled size ranging from 382 to 491 Mb, and an over 200-fold contig N50 length (between 6.4 Mb and 14.2 Mb) compared to the published genomes ( 4 , 17 , 22 ), an over 97% genome completeness (measured by BUSCO (Benchmarking Universal Single-Copy Orthologs)) and a reduced level of false duplications ( SI Appendix , Table S1 and Fig.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Version used: **5.3.2**
- Evidence: ( 19 ) were assembled using SPAdes v.3.13 ( 57 ) with reference to the L. edodes W1-26 genome ( 13 ) and assessed using BUSCO 5.3.2 with the OrthoDB v10 Basidiomycota database ( SI Appendix ).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **4.0.5**
- Evidence: We performed the Augustus (3.4.0) ( 71 ) gene model training through the BUSCO (4.0.5) ( 72 ) pipeline and predicted the gene models using the trained profile.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Divergent sensory and immune gene evolution in sea turtles with contrasting demographic and life histories. (PNAS 2023)

- DOI: 10.1073/pnas.2201076120 | PMCID: PMC9962930 | PMID: 36749728
- Evidence: BUSCO analysis ( 115 ) and QV value estimations ( 116 ) were conducted to assess the overall completeness, duplication, and relative quality of the assemblies.
- Full pipeline: alignment/mapping [BCFtools, SAMtools] -> variant calling [BCFtools, GATK, SAMtools] -> stage not stated [ANGSD, BUSCO, OrthoFinder, PLINK]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **5.4.3**
- Evidence: BUSCO v5.4.3 identified 389 single-copy fungal orthologs from fungi_odb10 database that were present in ≥90% of the species.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Origins of genome-editing excisases as illuminated by the somatic genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213887120 | PMCID: PMC9942806 | PMID: 36669098
- Evidence: As judged by high BUSCO scores (<2% missing orthologs), it is also relatively complete ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [RepeatMasker v2.0.1] -> stage not stated [BUSCO, Flye v2.7, HMMER, OrthoFinder, eggNOG]

### Two-speed genome evolution drives pathogenicity in fungal pathogens of animals. (PNAS 2023)

- DOI: 10.1073/pnas.2212633120 | PMCID: PMC9926174 | PMID: 36595674
- Evidence: Our updated gene annotation also revealed slightly higher numbers of predicted protein-coding genes ( n = 10,867 with a combined length of 16.38 Mb) and was slightly more complete (94.1% complete Benchmarking Universal Single-Copy Orthologs (BUSCO) for core conserved fungal genes) compared to the v.1 assembly (complete BUSCO = 93%).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, RAxML] -> stage not stated [BUSCO, Canu v1.8, GATK, HMMER, RepeatMasker v4.0.5]

### Proteomic analysis of the sponge Aggregation Factor implicates an ancient toolkit for allorecognition and adhesion in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2409125121 | PMCID: PMC11670116 | PMID: 39693348
- Evidence: The final assembly had a BUSCO v3 completeness score of 89.6% and a BUSCO v4 completeness score of 85.1%.
- Full pipeline: read trimming [PyMOL, Trimmomatic] -> stage not stated [AlphaFold, BUSCO, HMMER]

### Fitness consequences of structural variation inferred from a House Finch pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2409943121 | PMCID: PMC11588099 | PMID: 39531493
- Evidence: We generated two de novo haplotype genome assemblies per sample using Hifiasm ( 59 ) and assessed them with assembly-stats and BUSCO scores ( Dataset S2 ).
- Full pipeline: variant calling [BUSCO, hifiasm] -> stage not stated [BCFtools, PLINK, RepeatMasker]

### Homeotic and nonhomeotic patterns in the tetrapod vertebral formula. (PNAS 2024)

- DOI: 10.1073/pnas.2411421121 | PMCID: PMC11588047 | PMID: 39527744
- Evidence: We include the list of annotated and unannotated genomes used in our study in an electronic repository ( 42 ), as well as several measures of the genome quality (coverage), contiguity (scaffold N50), and RefSeq annotation completeness when available (BUSCO score).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [BLAST, BUSCO, SciPy, phytools]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Version used: **5.2.2**
- Evidence: Transcriptome quality was assessed with BUSCO v.
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### The &lt;i&gt;ivory&lt;/i&gt; lncRNA regulates seasonal color patterns in buckeye butterflies. (PNAS 2024)

- DOI: 10.1073/pnas.2403426121 | PMCID: PMC11474026 | PMID: 39352931
- Version used: **5.4.7**
- Evidence: Assessment of completeness was performed with BUSCO v5.4.7 with complete BUSCO score of 97.9 % ( SI Appendix , Table S11 ).
- Full pipeline: alignment/mapping [HISAT2, MACS2] -> differential/statistical testing [DESeq2] -> stage not stated [AUGUSTUS, BUSCO v5.4.7]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Version used: **5.2.2**
- Evidence: Gene space completeness was assessed using BUSCO version 5.2.2 ( 70 ) and the odb10 database for Brassicales, employing default parameters.
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Evidence: 94% completeness was estimated by BUSCO (Alveolata marker set) from the predicted proteome ( SI Appendix , Fig.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### Revisiting the four Hexapoda classes: Protura as the sister group to all other hexapods. (PNAS 2024)

- DOI: 10.1073/pnas.2408775121 | PMCID: PMC11441524 | PMID: 39298489
- Evidence: ...mic and transcriptomic data for 42 other hexapod species from NCBI ( SI Appendix for details) with high Benchmarking Universal Single-Copy Orthologs (BUSCO) completeness values plus nine aquatic “crustacean” clades (outgroups) recovered as close relatives of hexapods in previous studies ( 18 , 20 – 22 , 60 ).
- Full pipeline: stage not stated [BUSCO]

### Amoebozoan testate amoebae illuminate the diversity of heterotrophs and the complexity of ecosystems throughout geological time. (PNAS 2024)

- DOI: 10.1073/pnas.2319628121 | PMCID: PMC11287125 | PMID: 39012821
- Version used: **5.3.2**
- Evidence: Finally, we assessed the completeness of all newly sequenced transcriptomes using BUSCO v.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RAxML v8.2.12] -> stage not stated [BUSCO v5.3.2, IQ-TREE]

### A wound-induced differentiation trajectory for neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2322864121 | PMCID: PMC11260127 | PMID: 38976727
- Version used: **3.0.2**
- Evidence: BUSCO completeness was measured using BUSCO v3.0.2 and the “eukaryota_odb9” dataset, with 90.7% of genes represented in the assembly (88.1% single copy, 2.6% duplicates).
- Full pipeline: read trimming [RAxML v8.2.4] -> alignment/mapping [MUSCLE v3.8.31, RAxML v8.2.4] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [BUSCO v3.0.2, Pilon v1.23]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: BUSCO ( 68 ) was used to assess the completeness of the assembled genome by comparison against embryophyta_odb10 in genome mode.
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Haplotype-resolved genome assembly and implementation of VitExpress, an open interactive transcriptomic platform for grapevine. (PNAS 2024)

- DOI: 10.1073/pnas.2403750121 | PMCID: PMC11161759 | PMID: 38805269
- Evidence: Assembly metrics and BUSCO genome score for each primary assembly CH_REF UB_REF PN_T2T PNv4 Contigs Number 57 62 189 2,646 N50 contig length 25.4 Mb 19 Mb 26.8 Mb 445 Kb L50 contig count 9 10 9 321 Scaffolds Total size of scaffolds * 499.9 (496.1) Mb 494.6 (491) Mb 504.6 (494.9) Mb 474.7 (462.2) Mb Longest scaffold 37.9 Mb 38.8 Mb 36.7 Mb 34.9 Mb Median scaffold 25.1 Mb 25.7 Mb 25.9 Mb 24.2 Mb N50...
- Full pipeline: stage not stated [BUSCO]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Evidence: 94.2% of avian orthologs present in the inland vs. coastal reference genome following a BUSCO analysis).
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### What one genus of showy moths can say about migration, adaptation, and wing pattern. (PNAS 2024)

- DOI: 10.1073/pnas.2319726121 | PMCID: PMC11047066 | PMID: 38630713
- Evidence: We mapped Lepidoptera universal single-copy orthologs (USCO) from the BUSCO database ( 31 ) to U. ornatrix proteins, retaining those with coverage ≥ 70%.
- Full pipeline: alignment/mapping [AlphaFold, BUSCO, HMMER, IQ-TREE v1.6.12, MAFFT] -> stage not stated [scikit-learn]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: ( B ) We found broad agreement with the previously published genome for C. viridis ( 23 ) on the basis of locations of BUSCO loci.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Subgenome-aware analyses reveal the genomic consequences of ancient allopolyploid hybridizations throughout the cotton family. (PNAS 2024)

- DOI: 10.1073/pnas.2313921121 | PMCID: PMC11009661 | PMID: 38568968
- Evidence: We predicted 53,515 protein-coding genes, and the BUSCO genome completeness score was 99.61% ( SI Appendix , Table S6 ).
- Full pipeline: stage not stated [BUSCO, IQ-TREE]

### Taking a color photo: A homozygous 25-bp deletion in <i>Bace2</i> may cause brown-and-white coat color in giant pandas. (PNAS 2024)

- DOI: 10.1073/pnas.2317430121 | PMCID: PMC10945837 | PMID: 38437540
- Evidence: The BUSCO ( 13 ) complete score was 96%.
- Full pipeline: variant calling [GATK] -> stage not stated [BUSCO]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Evidence: Genome quality was evaluated using BUSCO and Merqury.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### Extraordinary preservation of gene collinearity over three hundred million years revealed in homosporous lycophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2312607121 | PMCID: PMC10823260 | PMID: 38236735
- Evidence: Both proteomes had high completeness scores from Benchmarking Universal Single-Copy Ortholog (BUSCO) with the “viridiplantae_odb10” database, indicating high annotation quality (90.4% for H. asiatica ; 97.5% for D. complanatum ) ( Dataset S4 ).
- Full pipeline: stage not stated [ANGSD v0.935, BUSCO, DESeq2 v3.17, RAxML v8.2.12]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Evidence: BUSCO scores ranged from 30.7% (Psilocybe_fuliginosa_NY-1901148) to 95.4% (Psilocybe_stuntzii_WTU-F-011520).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Evidence: Benchmarking Universal Single-Copy Orthologs (BUSCO) (v4.1.2) ( 63 ) was used to evaluate the completeness of the gene sets in our draft genome.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### The olfactory bulb endocast as a proxy for mammalian olfaction. (PNAS 2025)

- DOI: 10.1073/pnas.2510575122 | PMCID: PMC12718348 | PMID: 41359846
- Evidence: Upon investigation, the Tasmanian tiger genome ranks 15th lowest in BUSCO score among the 64 genomes examined ( Dataset S1 ), yet still shows a relatively high score of 89%.
- Full pipeline: stage not stated [BUSCO, ggplot2, phytools]

### Spatial variation in the mutation rate within the plant shoot apical meristem. (PNAS 2025)

- DOI: 10.1073/pnas.2514507122 | PMCID: PMC12646271 | PMID: 41213012
- Evidence: To assess the effect of the reference genome, we used Red Polenta long reads from PacBio and standard tools ( SI Appendix , Methods ) to produce a high continuity assembly (N50=45.4 Mb, 98.3% completeness of Solanales BUSCO genes, SI Appendix , Methods and Table S3 and Fig.
- Full pipeline: alignment/mapping [BUSCO] -> variant calling [hifiasm] -> stage not stated [RepeatMasker]

### Homology-mediated transformation of frog-killing fungus &lt;i&gt;Batrachochytrium dendrobatidis&lt;/i&gt; illuminates chytrid development and pathogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507572122 | PMCID: PMC12595416 | PMID: 41150711
- Version used: **5.2.2**
- Evidence: Assembly completeness was evaluated with BUSCO v5.2.2 ( 38 ) using the fungi_odb10 and eukaryota_odb10 datasets, reporting completeness scores of 88 to 89% and 94 to 95%, respectively.
- Full pipeline: alignment/mapping [SAMtools v1.14, minimap2 v2.28] -> stage not stated [BLAST, BUSCO v5.2.2, QUAST v5.0.0, R v4.0.2]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Version used: **5.2.2**
- Evidence: Transcriptome completeness was evaluated with BUSCO v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Evidence: While this B. franklini genome had BUSCO scores indicating a fairly complete genome (hymenoptera_odb10: 96.1% complete, 0.25% duplicate, 1.5% fragmented, 3.91% missing), the genome is fragmented compared to contemporary whole-genome sequencing results from fresh material of related Bombus , with a N50 length of 235 kb across a total of 31.7 k contigs and the longest contig being 1.7 Mb ( SI Append...
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### &lt;i&gt;WUSCHEL-D1&lt;/i&gt; upregulation enhances grain number by inducing formation of multiovary-producing florets in wheat. (PNAS 2025)

- DOI: 10.1073/pnas.2510889122 | PMCID: PMC12557809 | PMID: 41086219
- Evidence: We recovered 99.4% of the Poales single copy BUSCO core genes with 96.6% coming from complete and duplicated BUSCOs indicating high completeness ( SI Appendix , Table S1 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [minimap2] -> stage not stated [BUSCO, Python, hifiasm]

### Phylogenomics redefines the evolutionary history of mosquitoes. (PNAS 2025)

- DOI: 10.1073/pnas.2519291122 | PMCID: PMC12557814 | PMID: 41052354
- Evidence: We extracted BUSCO and UCE loci from mosquito and outgroup species with publicly available reference genomes, whole genome sequencing or transcriptome datasets ( Dataset S1 ).
- Full pipeline: alignment/mapping [BUSCO] -> differential/statistical testing [R, ggplot2] -> stage not stated [BEAST, IQ-TREE v2.2, TreeTime]

### The genome of the vining fern &lt;i&gt;Lygodium microphyllum&lt;/i&gt; highlights genomic and functional differences between life phases of an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2504773122 | PMCID: PMC12501142 | PMID: 40996792
- Evidence: The genome assembly was highly complete, with 98.11% single and duplicated intact BUSCO genes (Viridiplantae ODB10, n = 425).
- Full pipeline: differential/statistical testing [DESeq2 v1.44.0] -> stage not stated [BUSCO, hifiasm v0.19.9]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: Transcriptome-based analyses identified 19,457 protein-coding genes with homologous proteins in the Bargibant’s seahorse genome, and this accounts for 93.4% of the complete BUSCO set across vertebrates ( SI Appendix , Tables S1–S7 ).
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Evolution of developmental bias explains divergent patterns of phenotypic evolution in two nematode clades. (PNAS 2025)

- DOI: 10.1073/pnas.2507529122 | PMCID: PMC12403097 | PMID: 40828025
- Version used: **5.2.2**
- Evidence: S3 ), we used BUSCO 5.2.2( 62 ) to analyze the genomes of 23 nematode clade V species and a clade IV outgroup (first sheet of Dataset S2 ).
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MAFFT v7.49] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.2.2, emmeans v1.10.3, ggplot2 v3.5.1]

### Repeated polyploidization shapes divergence in floral morphology in &lt;i&gt;Lithophragma bolanderi&lt;/i&gt; (Saxifragaceae). (PNAS 2025)

- DOI: 10.1073/pnas.2505119122 | PMCID: PMC12377753 | PMID: 40802687
- Evidence: The resulting assembly had an N50 of 196,527 and a BUSCO score of 92.7 and was annotated using the BRAKER2 ( 75 ) pipeline resulting in a protein set with a BUSCO score of 90% (details in SI Appendix , Supporting Text S3.2 ).
- Full pipeline: read trimming [GATK v4.1.4.1, fastp] -> alignment/mapping [GATK v4.1.4.1, fastp] -> variant calling [GATK v4.1.4.1, IQ-TREE, VCFtools, fastp] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4] -> stage not stated [BUSCO, WhatsHap]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **5.3.2**
- Evidence: Final assembly completeness and quality was assessed with the k-mer tool Merqury v1.3 ( 99 ) and BUSCO v5.3.2 ( 100 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### Yeast adapts to diverse ecological niches driven by genomics and metabolic reprogramming. (PNAS 2025)

- DOI: 10.1073/pnas.2502044122 | PMCID: PMC12358858 | PMID: 40763020
- Evidence: Assessment of pangenome completeness using the BUSCO method and the saccharomycetes_odb10 database ( D ).
- Full pipeline: dimensionality reduction/clustering [eggNOG] -> stage not stated [BUSCO]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Version used: **5.7.1**
- Evidence: Synteny analysis was performed using orthologous genes identified with BUSCO version 5.7.1 with the lineage database lepidoptera_odb10 and otherwise default options ( 121 ), including two outgroup genomes, Melitaea cinxia ( 122 ) and D. plexippus ( 123 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Genomic origins and evolution of neo-sex chromosomes in Pacific Island birds. (PNAS 2025)

- DOI: 10.1073/pnas.2503746122 | PMCID: PMC12337287 | PMID: 40720643
- Version used: **5.2.2**
- Evidence: All genomes and assembly stages were also assessed for completeness using BUSCO (v5.2.2; ref.
- Full pipeline: read trimming [Trim Galore v0.6.2, hifiasm] -> alignment/mapping [Trim Galore v0.6.2, hifiasm] -> stage not stated [BUSCO v5.2.2, R, RepeatMasker v4.1.2, SAMtools v1.11, minimap2 v2.26]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Version used: **3.0.2**
- Evidence: For the de novo genome assembly, we first used Trimmomatic ( 67 ) to remove adapters and low-quality sequences and then assembled the data using ALLPATHS-LG r.52485 ( 68 ) with the option “HAPLOIDIFY = True.” The quality of the assembly was evaluated with QUAST v4.5.4 ( 69 ) and BUSCO v3.0.2 ( 70 ) using the “mammalia_odb9” dataset.
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### Diploidization in a wild rice allopolyploid is both episodic and gradual. (PNAS 2025)

- DOI: 10.1073/pnas.2424854122 | PMCID: PMC12232711 | PMID: 40569381
- Evidence: The high completeness and continuity of three genome assemblies were evidenced by mapping of next-generation sequencing (NGS) clean reads (≥99.4%), Benchmarking Universal Single-Copy Orthologs (BUSCO) (≥95.83%), and Long Terminal Repeat Assembly Index (LAI) scores (LAI = 18.17 to 27.62) ( 39 ) ( SI Appendix, Supplementary text ).
- Full pipeline: alignment/mapping [BUSCO] -> dimensionality reduction/clustering [ADMIXTURE]

### An endosymbiotic origin of the crimson pigment from the lac insect. (PNAS 2025)

- DOI: 10.1073/pnas.2501623122 | PMCID: PMC12207437 | PMID: 40523179
- Evidence: The KLYLS genome measured 23.27 Mbp (7,546 protein-coding genes, 59.01% GC content, protein BUSCO score 95.3%, SI Appendix , Tables S4 and S5 ).
- Full pipeline: stage not stated [BLAST, BUSCO, IQ-TREE, InterProScan]

### Transgenerational epigenetic effect of kings' aging on offspring's caste fate mediated by sperm DNA methylation in termites. (PNAS 2025)

- DOI: 10.1073/pnas.2509506122 | PMCID: PMC12184646 | PMID: 40512787
- Evidence: The completeness of the Insecta benchmarking universal single-copy orthologs (BUSCO) ( 29 ) for whole-genome assembly was 94.1% (93.3% complete; 0.8% fragmented).
- Full pipeline: stage not stated [BUSCO, R]

### Cross-species modeling of plant genomes at single-nucleotide resolution using a pretrained DNA language model. (PNAS 2025)

- DOI: 10.1073/pnas.2421738122 | PMCID: PMC12184517 | PMID: 40489624
- Evidence: Given the relatively poor annotation in other species compared to Arabidopsis , we used the BUSCO tool ( 66 ) to identify 3,236 orthologous genes specific to monocotyledons in O. sativa , S. bicolor, and Z. mays and 2,326 orthologous genes specific to eudicotyledons in G. hirsutum and G. max to generate reliable testing datasets in other species.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [XGBoost] -> visualisation [UMAP] -> stage not stated [BEDTools, BUSCO, VEP]

### Phylogenomics reveals the slow-burning fuse of diatom evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2500153122 | PMCID: PMC12146733 | PMID: 40440071
- Evidence: Transcriptome quality and completeness was estimated with BUSCO ( 60 ).
- Full pipeline: stage not stated [BUSCO, IQ-TREE]

### Genomic map of the functionally extinct northern white rhinoceros (&lt;i&gt;Ceratotherium simum cottoni&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2401207122 | PMCID: PMC12107126 | PMID: 40359041
- Evidence: ( E ) Benchmark Universal Single Copy Ortholog (BUSCO) scores for the genome assembly and annotation using three datasets: eukaryota (255 genes), Vertebrata (3,354 genes), and Laurasiatheria (12,234 genes).
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BUSCO, Pilon]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Version used: **5.0**
- Evidence: Genome completeness was assessed using BUSCO v5.0 with the embryophyta_odb9 dataset ( 27 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Accurate, scalable, and fully automated inference of species trees from raw genome assemblies using ROADIES. (PNAS 2025)

- DOI: 10.1073/pnas.2500553122 | PMCID: PMC12088440 | PMID: 40314967
- Evidence: ( 40 ), was generated using 250 single-copy BUSCO genes (using Amino acid sequences) and running MAFFT, RAxML-NG, and ASTRAL-MP (in summary mode) sequentially.
- Full pipeline: stage not stated [BUSCO, MAFFT, RAxML, Snakemake]

### Cryptic genetic variation in brain gene expression precedes the evolution of cannibalism in spadefoot toad tadpoles. (PNAS 2025)

- DOI: 10.1073/pnas.2418431122 | PMCID: PMC12088425 | PMID: 40294283
- Evidence: We assessed the completeness of the transcriptomes using the BUSCO tetrapod dataset (5,310 orthologs) ( SI Appendix , Table S4 ).
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [BUSCO, DESeq2, survival (R)]

### Genomic divergence across the tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2319389122 | PMCID: PMC11912424 | PMID: 40014554
- Evidence: Additionally, we downloaded the 67 eukaryotic “odb10” datasets from the Benchmarking Universal Single-Copy Orthologs (BUSCO) website (busco.ezlab.org), which specifies the SCOs common to members of selected taxonomic group ( 56 , 57 ).
- Full pipeline: stage not stated [BLAST, BUSCO, SAMtools v1.15.1]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Evidence: The three haplotype-resolved genome assemblies were anchored to 38 chromosomes and highly contiguous, with scaffold N50 sizes ranging from 25.1 to 26.3 Mb and Benchmarking Universal Single-Copy Orthologs (BUSCO) completeness scores of 97.3 to 98.5% ( SI Appendix, Table S3 ).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Natural variations in <i>TT8</i> and its neighboring <i>STK</i> confer yellow seed with elevated oil content in <i>Brassica juncea</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2417264122 | PMCID: PMC11804580 | PMID: 39883846
- Evidence: To our knowledge, the PM genome is the first T2T assembly of B. juncea , which covered over 99.9% of HiFi reads and identified 99.7% of genes in the BUSCO ( 28 ) dataset ( Dataset S5 ).
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12] -> differential/statistical testing [GEMMA] -> visualisation [Cytoscape] -> stage not stated [BUSCO, R, VCFtools, WGCNA, minimap2 v2.17]

### Evolution of genome-wide barriers to gene flow during complex speciation in rattlesnakes. (PNAS 2026)

- DOI: 10.1073/pnas.2609058123 | PMCID: PMC13214041 | PMID: 42166239
- Evidence: The total assembly is 1.6 Gbp in length and is highly contiguous and complete, with a contig N50 of 93.16 Mbp, scaffold N50 of 206.8 Mbp, and 98.43% BUSCO completeness ( SI Appendix , Table S1 ).
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [BUSCO]

### Genomic diversity and the domestication history of cotton (&lt;i&gt;Gossypium hirsutum&lt;/i&gt;). (PNAS 2026)

- DOI: 10.1073/pnas.2607107123 | PMCID: PMC13213997 | PMID: 42150059
- Evidence: BUSCO (Benchmarking Universal Single-Copy Orthologs) ( 29 ) analysis suggested 99.3% completeness with 97.1% being duplicated, as expected for a polyploid.
- Full pipeline: stage not stated [BUSCO]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: The resulting BUSCO score to the eudicots_odb10 set was C: 97.9% (S:1.4%, D:96.5%), F:0.2%, M:1.9%, n:2,326.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Phylogenomic synteny reveals paleohexaploid-derived genomic blocks across Asteraceae. (PNAS 2026)

- DOI: 10.1073/pnas.2426851123 | PMCID: PMC12912976 | PMID: 41666000
- Evidence: As our main objective was to build a synteny-phylogenomic framework for Asteraceae, we applied several criteria for selecting genomes for comparative analysis: 1) chromosome level assembly; 2) high BUSCO and OMArk scores; and 3) maximized phylogenetic representation.
- Full pipeline: stage not stated [BUSCO]

### Incomplete lineage sorting shaped mixed traits during a colobine primate radiation. (PNAS 2026)

- DOI: 10.1073/pnas.2524833123 | PMCID: PMC12867756 | PMID: 41576102
- Evidence: The results from BUSCO analyses ( 40 ) showed that genome completeness was 96%, indicating reliable quality ( SI Appendix , Table S9 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold v2.3.1] -> stage not stated [BUSCO, RAxML v8.2.9]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Evidence: We obtained the assembly metrics using QUAST software v.5.2.0 ( 61 ), and used BUSCO software v.5.4.3 to assess assembly completeness ( 62 ).
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

