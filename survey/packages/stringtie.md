# StringTie

- **Category:** genomics
- **Papers in survey:** 61
- **Journals:** PNAS (41), Nature (19), Cell (1)
- **Years:** 2021 (6), 2022 (9), 2023 (13), 2024 (12), 2025 (16), 2026 (5)
- **Versions named:** 2.2.1 (7), 1.3.3b (5), 2.2.3 (3), 1.3.4 (2), 1.3.6 (2), 1.3.3 (2), 2.1.5 (1), 1.3.0 (1), 2.0.6 (1), 2.2.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (28), quantification (18), read trimming (4), structure determination (2), quality control (2), normalisation (2), differential/statistical testing (2), variant calling (1)

## Papers

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Version used: **2.2.1**
- Evidence: 123 N/A QT-PISA Krissinel 124 N/A Spectronaut v17.6 https://biognosys.com/software/spectronaut/ N/A StringTie v2.2.1 Perea et al.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Version used: **1.3.6**
- Evidence: The resulting mapping files were parsed by StringTie v.1.3.6 52 and transcripts reconstructed from each aligned sample were merged in a single consensus .gtf file.
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Version used: **1.3.0**
- Evidence: RNA evidence was collected by aligning RNA-sequencing (RNA-seq) reads to the repeat-masked assembly using HISAT2 (v.2.10.2) 57 and assembling them to transcripts with StringTie (v.1.3.0) 58 .
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **1.3.3b**
- Evidence: Potential transcripts were then assembled, using StringTie (v.1.3.3b) (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: First, TA299 and TA10622 RNA-seq data from the six tissues were mapped to their respective reference assemblies using STAR 73 (v.2.7.0f; parameters: --outFilterMismatchNoverReadLmax 0.02) and assembled into transcripts with StringTie 74 (v.2.1.4; parameters : --rf -m 150 -f 0.3 -t).
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Relaxed targeting rules help PIWI proteins silence transposons. (Nature 2023)

- DOI: 10.1038/s41586-023-06257-4 | PMCID: PMC10338343 | PMID: 37344600
- Version used: **1.3.4**
- Evidence: Transcript abundance was calculated using StringTie (v.1.3.4) 66 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> differential/statistical testing [DESeq2 v1.18.1, scikit-learn] -> stage not stated [SciPy v1.8.1]

### Ageing-associated changes in transcriptional elongation influence longevity. (Nature 2023)

- DOI: 10.1038/s41586-023-05922-y | PMCID: PMC10132977 | PMID: 37046086
- Evidence: Quantification of transcript abundance for ITPR1 and AGO3 was obtained by using StringTie 73 .
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.5.1b, Trimmomatic] -> quantification [StringTie] -> differential/statistical testing [DESeq2 v1.8.2, GSEA] -> stage not stated [kallisto v0.42.5]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **1.3.6**
- Evidence: StringTie (v.1.3.6) 66 was used to convert STAR alignments into gene transfer format (GTF) files and Portcullis (v.1.1.2) 67 to generate a curated set of splice junctions.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Version used: **1.3.3**
- Evidence: Next, we assembled models of transcripts expressed using StringTie v.1.3.3 (ref.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: Using evidence derived from expression data, RNA-seq data were first mapped using STAR 84 (v.2.7.8a) and subsequently assembled into transcripts by StringTie 85 (v.2.1.5, parameters -m 150-t -f 0.3).
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Molecular and physiological changes in the SpaceX Inspiration4 civilian crew. (Nature 2024)

- DOI: 10.1038/s41586-024-07648-x | PMCID: PMC11357997 | PMID: 38862026
- Evidence: Transcripts detected in whole blood RNA sequencing were assembled using StringTie 52 . m6A modifications were quantified using m6Anet 53 with a probability threshold of 0.9.
- Full pipeline: quantification [StringTie]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **1.3.3b**
- Evidence: These alignments were used to assemble transcriptomes for each organ using StringTie (v.1.3.3b) and subsequently merged together using Taco 80 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **2.1.5**
- Evidence: All expression data were mapped using STAR (version 2.7.8a) 94 and assembled into transcripts with StringTie (version 2.1.5, parameters -m 150-t -f 0.3) 95 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: 93 ) with the –dta parameter, and genome-based transcriptomes were built for each sample using StringTie 94 .
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: 80 ) (v.2.0.5) and then assembled into transcripts with StringTie 81 (v.2.0).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Stress dynamically modulates neuronal autophagy to gate depression onset. (Nature 2025)

- DOI: 10.1038/s41586-025-08807-4 | PMCID: PMC12058529 | PMID: 40205038
- Evidence: After the final transcriptome was generated, StringTie and ballgown were used to estimate the expression levels of all transcripts and determine mRNA expression abundance by calculating the FPKM value.
- Full pipeline: quantification [StringTie] -> differential/statistical testing [DESeq2]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **2.2.1**
- Evidence: First, we aligned RNA-seq reads to assembled haplotypes using HISAT2 (v.2.2.1) 76 with the “--dta” parameter and then assembled by StringTie (v.2.2.1) 77 with the “--rf” parameter.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **2.2.3**
- Evidence: RNA-seq reads were mapped to the genome using HISAT2, and the resulting alignments were assembled into transcripts with StringTie (v2.2.3) using a reference-guided approach.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **2.2.1**
- Evidence: We then aligned RNA-seq reads to the assemblies using HISAT2 (v.2,2.1) 104 , and performed transcriptome assembly with StringTie (v.2.2.1) 105 , using Liftoff annotations as guidance.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Cleavage of mRNAs by a minority of pachytene piRNAs improves sperm fitness. (Nature 2026)

- DOI: 10.1038/s41586-026-10102-9 | PMCID: PMC13061629 | PMID: 41639461
- Version used: **1.3.4**
- Evidence: Transcript abundance was calculated with StringTie (v1.3.4) 64 using mm10/rmsk and gene annotation from Ensembl.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.18.1]

### The <i>Clp1</i> R140H mutation alters tRNA metabolism and mRNA 3' processing in mouse models of pontocerebellar hypoplasia. (PNAS 2021)

- DOI: 10.1073/pnas.2110730118 | PMCID: PMC8488643 | PMID: 34548404
- Evidence: We first compared our RNA-seq data to the Gencode reference transcriptome, using StringTie to assemble a customized transcriptome such that the 3′ ends observed in our RNA-seq data were reflected in our reference transcriptome ( Fig.
- Full pipeline: stage not stated [StringTie]

### The p53 transcriptional response across tumor types reveals core and senescence-specific signatures modulated by long noncoding RNAs. (PNAS 2021)

- DOI: 10.1073/pnas.2025539118 | PMCID: PMC8346867 | PMID: 34326251
- Evidence: RNA-seq reads were mapped to mm10 with TopHat ( 43 ) to Gencode transcript annotation (M9), and transcripts were annotated with StringTie ( 44 ).
- Full pipeline: alignment/mapping [StringTie, TopHat] -> normalisation [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2]

### The DME demethylase regulates sporophyte gene expression, cell proliferation, differentiation, and meristem resurrection. (PNAS 2021)

- DOI: 10.1073/pnas.2026806118 | PMCID: PMC8307533 | PMID: 34266952
- Version used: **2.1.3**
- Evidence: Reads were assembled into transcripts using StringTie (v2.1.3) ( 78 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0] -> visualisation [R, ggplot2] -> stage not stated [DESeq2, StringTie v2.1.3]

### The giant axolotl genome uncovers the evolution, scaling, and transcriptional control of complex gene loci. (PNAS 2021)

- DOI: 10.1073/pnas.2017176118 | PMCID: PMC8053990 | PMID: 33827918
- Evidence: Iso-Seq reads were separately aligned, and the gene models from both sets were combined using StringTie–merge.
- Full pipeline: alignment/mapping [StringTie] -> stage not stated [BLAST, BUSCO]

### Incipient genome erosion and metabolic streamlining for antibiotic production in a defensive symbiont. (PNAS 2021)

- DOI: 10.1073/pnas.2023047118 | PMCID: PMC8092579 | PMID: 33883280
- Version used: **1.3.3**
- Evidence: Sequenced reads were quality checked and trimmed using the Trimommatic implementation in KBase (v1.2.14, https://www.kbase.us ) ( 88 ), the alignment of the reads to the reference genome was performed with Bowtie 2 (v2.3.2) ( 89 ), and aligned reads were assembled using StringTie (v1.3.3) ( 90 ).
- Full pipeline: quality control [Bowtie2 v2.3.2, StringTie v1.3.3] -> read trimming [Bowtie2 v2.3.2, StringTie v1.3.3] -> alignment/mapping [Bowtie2 v2.3.2, StringTie v1.3.3] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [BLAST, ggplot2, ggpubr]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: Then, StringTie ( 68 ) (-f 0.3 -j 3 -c 5 -g 100 -s 10000 -p 8) was used to calculate transcript expression levels.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### The evolution of synaptic and cognitive capacity: Insights from the nervous system transcriptome of &lt;i&gt;Aplysia&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122301119 | PMCID: PMC9282427 | PMID: 35867761
- Evidence: These filtered reads were then assembled using three different approaches: de novo with Trinity; genome-guided de novo, also with Trinity; and pure genome-guided assembly with StringTie.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> differential/statistical testing [RAxML] -> stage not stated [BUSCO]

### The evening complex integrates photoperiod signals to control flowering in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2122582119 | PMCID: PMC9245669 | PMID: 35733265
- Evidence: Transcripts per million (TPM) values for genes were calculated by StringTie with default settings directed by gene annotation file IRGSP-1.0 ( 64 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [StringTie, deepTools] -> normalisation [deepTools] -> stage not stated [BEDTools v2.30.0, BWA, MACS2, R, SAMtools v1.11]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: Finally, the assembly was completed using StringTie ( 42 ) with default settings.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: They were used as inputs in StringTie ( 41 ) to create the initial transcriptome assembly with 71,042 transcripts, which was used to annotate the genome using Maker v.3 ( 42 ), resulting in 18,196 genes with 29,389 transcripts.
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: ...after bowtie2 ( 55 ) alignment and Salmon ( 56 ) quantification or 2) at least one TPM in the gtf file obtained after a minimap2 ( 57 ) alignment and StringTie ( 58 ) quantification of IsoSeq3 polished long reads.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: The transcripts in each sample were assembled and quantified using StringTie ( 58 ).
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Evidence: The RNAseq data were also mapped to the genome using HISAT2 ( 70 ) and the reads were assembled into transcripts using StringTie ( 71 ), and then, TransDecoder ( 66 ) was subsequently used to perform ORFs prediction with the assembled transcripts.
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### Sex-linked gene traffic underlies the acquisition of sexually dimorphic UV color vision in <i>Heliconius</i> butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2301411120 | PMCID: PMC10438391 | PMID: 37552755
- Evidence: The transcripts were annotated and merged using StringTie ( 60 ).
- Full pipeline: quality control [Bowtie2 v2.2.7, Kraken2] -> alignment/mapping [BEDTools, Bowtie2 v2.2.7, MUSCLE] -> differential/statistical testing [R] -> stage not stated [Canu v1.6, Pilon, StringTie]

### Host hydrocarbons protect symbiont transmission from a radical host defense. (PNAS 2023)

- DOI: 10.1073/pnas.2302721120 | PMCID: PMC10400980 | PMID: 37487102
- Version used: **1.3.3b**
- Evidence: The retained reads were mapped to either the S. coelicolor or S. philanthi genome ( 50 ) using Bowtie2 (v.2.3.2) and StringTie (v.1.3.3b) implemented in KBase ( 98 ) using default settings. rRNA sequences were removed from the dataset before differential gene expression was analyzed using DESeq2 (v.1.22.2) ( 99 ) in RStudio (v1.1.453 with R v3.5.0).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> differential/statistical testing [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> visualisation [ggplot2]

### NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2308750120 | PMCID: PMC10401007 | PMID: 37487068
- Evidence: Assembly and quantification were performed using StringTie ( 44 ) (Galaxy Version 2.1.1).
- Full pipeline: alignment/mapping [Bowtie2, STAR] -> quantification [StringTie] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Galaxy, ImageJ, MACS2]

### Disruption of the standard kinetochore in holocentric <i>Cuscuta</i> species. (PNAS 2023)

- DOI: 10.1073/pnas.2300877120 | PMCID: PMC10214151 | PMID: 37192159
- Evidence: Whole-length transcripts and genes were then reconstructed using the StringTie program [v2.1.7; ( 58 )] with parameters -c 2 -f 0.05.
- Full pipeline: alignment/mapping [SAMtools, STAR] -> structure determination [StringTie] -> stage not stated [BLAST, BUSCO, OrthoFinder, QUAST]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **1.3.3b**
- Evidence: Then we generated reference-guided and de novo assembled transcript sequences using Cupcake (5.8) with Iso-Seq reads, and StringTie (1.3.3b) ( 77 ) (-m 300 -j 5 -c 8) and Cufflinks (2.2.1) ( 78 ) (–multi-read-correct –max-intron-length 30000) and Trinity (2.6.6) ( 79 ) (--min_glue 10 --path_reinforcement_distance 30 --min_contig_length 400 --jaccard_clip) with RNA-seq reads.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **2.1.1**
- Evidence: We further used the HISAT2 (2.1.0) ( 69 )-StringTie (2.1.1) ( 70 ) pipeline to assemble the transcripts through a genome-guided method.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Glutamate-GABA imbalance mediated by miR-8-5p and its STTM regulates phase-related behavior of locusts. (PNAS 2023)

- DOI: 10.1073/pnas.2215660120 | PMCID: PMC9910461 | PMID: 36574679
- Evidence: StringTie software was used to calculate the fragments per kilobase million values of genes.
- Full pipeline: alignment/mapping [HISAT2] -> stage not stated [ImageJ, StringTie, edgeR]

### ERRα and ERRγ coordinate expression of genes associated with Alzheimer's disease, inhibiting &lt;i&gt;DKK1&lt;/i&gt; to suppress tau phosphorylation. (PNAS 2024)

- DOI: 10.1073/pnas.2406854121 | PMCID: PMC11406303 | PMID: 39231208
- Evidence: Transcripts per million (TPM) values were calculated with StringTie.
- Full pipeline: alignment/mapping [MACS2 v2.2.7.1, STAR v2.7.10a] -> quantification [StringTie]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: Raw reads were trimmed with Trimmomatic, reads were mapped using STAR, and FPKM tables were generated using StringTie.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### Identification and characterization of a small-molecule metallophore involved in lanthanide metabolism. (PNAS 2024)

- DOI: 10.1073/pnas.2322096121 | PMCID: PMC11317620 | PMID: 39078674
- Evidence: Using KBase ( 50 ), reads were aligned with HISTAT2, transcripts were assembled with StringTie, and DEGs were identified using DESeq2.
- Full pipeline: alignment/mapping [DESeq2, StringTie] -> dimensionality reduction/clustering [BLAST, HMMER]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Version used: **2.0**
- Evidence: Read counts were normalized to Transcripts Per Kilobase Million (TPM) by StringTie (version 2.0) ( 46 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### Premeiotic 24-nt phasiRNAs are present in the <i>Zea</i> genus and unique in biogenesis mechanism and molecular function. (PNAS 2024)

- DOI: 10.1073/pnas.2402285121 | PMCID: PMC11127045 | PMID: 38739785
- Version used: **2.1.7**
- Evidence: Briefly, StringTie v2.1.7 ( 33 ) and Scallop v0.10.4 ( 34 ) were separately used with default parameters to perform de novo transcriptome assembly, and the resulting transcriptome annotations were merged using the merge function of StringTie.
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MUSCLE, edgeR v4.0.2, featureCounts v1.6.3] -> normalisation [edgeR v4.0.2, featureCounts v1.6.3] -> stage not stated [BEDTools v2.29.2, StringTie v2.1.7]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Version used: **2.2.1**
- Evidence: For each sample, genome-guided transcriptome assembly was performed using StringTie v2.2.1 ( 86 ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### Enhanced weathering in the US Corn Belt delivers carbon removal with agronomic benefits. (PNAS 2024)

- DOI: 10.1073/pnas.2319436121 | PMCID: PMC10907306 | PMID: 38386712
- Evidence: Unaligned reads were discarded and aligned reads were assembled using StringTie ( 67 ) with an average read length of 150 bp and a minimum assembled transcript length of 200 bp.
- Full pipeline: alignment/mapping [HISAT2, StringTie] -> differential/statistical testing [DESeq2]

### DIDO is necessary for the adipogenesis that promotes diet-induced obesity. (PNAS 2024)

- DOI: 10.1073/pnas.2300096121 | PMCID: PMC10801893 | PMID: 38194457
- Evidence: Relative expression of transcripts was quantified with StringTie, converted to transcripts per million (TPM) reads, and kept for later analysis when TPM > 0 in all samples.
- Full pipeline: alignment/mapping [BWA, Picard] -> quantification [StringTie] -> stage not stated [DESeq2]

### Anellovirus protein encoded by &lt;i&gt;ORF2/3&lt;/i&gt; functions as the viral replication initiation protein. (PNAS 2025)

- DOI: 10.1073/pnas.2516306122 | PMCID: PMC12772153 | PMID: 41433061
- Version used: **2.2.3**
- Evidence: We used the resulting alignments form the RNA-seq pipeline to quantify the host and nrVL4619 transcript isoforms using StringTie v2.2.3 ( 80 ), in units of Transcripts per Million Mapped (TPM), then extracted the nrVL4619 transcripts using samtools v1.20 ( 81 ) to quantify the relative TPM values of the nrVL4619 transcripts exclusively.
- Full pipeline: alignment/mapping [SAMtools v1.20, StringTie v2.2.3] -> quantification [SAMtools v1.20, StringTie v2.2.3] -> stage not stated [AlphaFold, Conda, fastp v0.23.4]

### Ace2 safeguards embryonic hematopoietic stem and progenitor cell production by restraining Nlrp3-mediated pyroptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2515641122 | PMCID: PMC12704739 | PMID: 41348733
- Version used: **1.3.3b**
- Evidence: FPKM and read count for each gene were calculated using StringTie (version 1.3.3b) ( 67 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.1.0] -> quantification [StringTie v1.3.3b] -> dimensionality reduction/clustering [clusterProfiler v4.6.1] -> differential/statistical testing [DESeq2 v1.10.1, R v3.2.3] -> stage not stated [GSEA, ImageJ]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **2.2.3**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Ubiquitin-mediated degradation restricts spatiotemporal accumulation of the cytoplasmic male sterility protein WA352 to anthers in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2504381122 | PMCID: PMC12557538 | PMID: 41100672
- Evidence: The clean reads were first aligned to the rice (ZS97) reference genome ( http://rice.hzau.edu.cn/rice_rs2/ ) ( 46 ) using HISAT2; then StringTie was used to assemble transcripts and calculate the fragments per kilobase of transcript per million mapped reads (FPKM) for estimating gene expression levels ( 47 ).
- Full pipeline: alignment/mapping [HISAT2, StringTie] -> quantification [HISAT2, StringTie] -> stage not stated [AlphaFold, ColabFold]

### Genetic dissection of nonconventional introns reveals codominant noncanonical splicing code in &lt;i&gt;Euglena&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509937122 | PMCID: PMC12501133 | PMID: 40986342
- Evidence: Based on mapped reads with a mapping quality score (MQ) ≥ 1, exon–intron structures were predicted using StringTie-v1.3.0 ( 44 ) with the parameters: “-f = 0.5, -g = 20, -c = 5”.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BLAST, HMMER, ImageJ]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: A transcriptome-wide gene count matrix was then created using the script prepDE.py3 provided on the StringTie website ( https://ccb.jhu.edu/software/stringtie ).
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### Mutations in the circadian cycle drive adaptive plasticity in cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2506928122 | PMCID: PMC12435244 | PMID: 40901874
- Version used: **2.2.1**
- Evidence: In parallel, normalized expression values were calculated using StringTie (v2.2.1) ( 67 ) in Transcripts Per Million (TPMs).
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [StringTie v2.2.1, featureCounts v2.0.1] -> normalisation [StringTie v2.2.1] -> differential/statistical testing [DESeq2 v1.34.0, R v4.2.1]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Version used: **2.2.1**
- Evidence: Genome-mapped reads underwent de novo reference-guided transcript assembly using two assemblers: StringTie v2.2.1 (-c 1.5, -f 0.2, -s 20, and -m 150) ( 44 , 45 ) and Scallop v0.10.5 (--min_transcript_length_increase 35) ( 46 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### Antlers on does: An unexpected role of macrophages in deer biology. (PNAS 2025)

- DOI: 10.1073/pnas.2424448122 | PMCID: PMC12184406 | PMID: 40512783
- Evidence: After cleaning the raw data, and using the deer reference genome, we utilized the workflows of HISAT2, StringTie, and DESeq2 ( 33 ) to analyze differentially expressed genes (DEGs) with |log 2 FoldChange| ≥ 2 and Benjamini–Hochberg P -value < 0.001 between two groups.
- Full pipeline: alignment/mapping [DESeq2, HISAT2, StringTie] -> quantification [ImageJ] -> normalisation [ImageJ] -> differential/statistical testing [DESeq2, HISAT2, StringTie] -> stage not stated [GSEA, Seurat]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: Transcriptomic data were aligned using HISAT2 and assembled with StringTie ( 34 , 35 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Plastic responses to past environments shape adaptation to novel selection pressures. (PNAS 2025)

- DOI: 10.1073/pnas.2409541122 | PMCID: PMC11804578 | PMID: 39883835
- Version used: **2.2.0**
- Evidence: The transcriptome was then assembled against the reference genome annotation ( 62 ) using StringTie v2.2.0 ( 63 ).
- Full pipeline: read trimming [STAR v2.7.10a] -> alignment/mapping [STAR v2.7.10a, StringTie v2.2.0] -> stage not stated [R]

### Dynamic diversification of lignan metabolism in sesame via coordinated oxygenation and glucosylation across germination. (PNAS 2026)

- DOI: 10.1073/pnas.2605774123 | PMCID: PMC13250549 | PMID: 42247565
- Version used: **2.2.1**
- Evidence: Transcript abundance was quantified as transcripts per million (TPM) using StringTie version 2.2.1 ( 69 ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.0] -> quantification [StringTie v2.2.1]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Version used: **2.0.6**
- Evidence: StringTie (v2.0.6) was run first both with a reference genome to assemble the RNA-Seq alignments into potential transcripts and in genome-guided mode.
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

