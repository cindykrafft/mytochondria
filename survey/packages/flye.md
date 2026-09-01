# Flye

- **Category:** genomics
- **Papers in survey:** 47
- **Journals:** Nature (24), PNAS (22), Cell (1)
- **Years:** 2021 (1), 2022 (6), 2023 (4), 2024 (17), 2025 (10), 2026 (9)
- **Versions named:** 2.9 (9), 2.9.2 (3), 2.9.1 (3), 2.7 (3), 2.8.1 (3), 2.9.3 (2), 2.8.3 (2), 2.9.5 (1), 2.9.0 (1), 2.4.2 (1)
- **Pipeline stages it appears in:** alignment/mapping (2), read trimming (1), variant calling (1)

## Papers

### Genetic manipulation of Patescibacteria provides mechanistic insights into microbial dark matter and the epibiotic lifestyle. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.017 | PMCID: PMC10633639 | PMID: 37683634
- Version used: **2.9**
- Evidence: 62 N/A Filtlong v0.2.1 https://github.com/rrwick/Filtlong N/A Flye v2.9 https://github.com/fenderglass/Flye/releases/tag/2.9 .
- Full pipeline: alignment/mapping [MUSCLE, minimap2] -> dimensionality reduction/clustering [R] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Flye v2.9, HMMER]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: Diploid contig assemblies Trio binning Flye ONT pipeline (asm6 and asm7) Following a trio-based assembly approach 22 , parental Illumina 21-mers were counted in the child, maternal and paternal read sets (full sets, not subset coverage recommendations).
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Version used: **2.7**
- Evidence: Primary assemblies were generated from three assemblers (Flye v.2.7, Hicanu v.2.0 and Hifiasm v.0.13) 50 – 52 and potential misassemblies were corrected using the GALA pipeline 53 ( Supplementary Note ).
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **2.4.2**
- Evidence: PacBio reads were self-corrected using Canu (v.1.7.1) before assembly with Flye (v.2.4.2) 72 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Version used: **2.8.3**
- Evidence: We performed an initial metagenomic assembly of long reads using Flye (v.2.8.3-b1695) 73 with the ‘--meta’ option.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **2.9.2**
- Evidence: Reads were assembled with Flye (v.2.9.2-b1786) 114 in metagenomics mode, with the –nano-hq setting and –read-error set to 0.03 as recommended for ONT Q20+ chemistry.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Version used: **2.9.2**
- Evidence: The reads were assembled with Flye (v2.9.2) 53 with the --pacbio-hifi flag, resulting in 118 contigs of total length 55,743,399 bp with an N50 (the shortest contig of the set of the largest contigs making up 50% of the assembly) of 1,370,944 bp.
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Drosophila are hosts to the first described parasitoid wasp of adult flies. (Nature 2024)

- DOI: 10.1038/s41586-024-07919-7 | PMCID: PMC11424482 | PMID: 39261731
- Version used: **2.9.1**
- Evidence: Reads 1 kb and longer were retained using seqtk 56 and assembled with Flye 2.9.1 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.49] -> visualisation [R] -> stage not stated [Flye v2.9.1]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **2.9**
- Evidence: Reads longer than 1 kb were assembled into contigs using Flye 2.9-b1768 (ref.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: Disconnected nodes due to HiFi coverage gaps were joined and gap-filled using localized, ONT-based Flye 73 assemblies.
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### A distinct Fusobacterium nucleatum clade dominates the colorectal cancer niche. (Nature 2024)

- DOI: 10.1038/s41586-024-07182-w | PMCID: PMC11006615 | PMID: 38509359
- Evidence: Additional assembly was carried out using Flye assembler v.2.8 as needed ( https://github.com/fenderglass/Flye ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v2.4.5] -> machine learning [DADA2] -> stage not stated [BLAST, Flye]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Evidence: We used assembled Illumina reads to correct raw Nanopore reads, which were assembled using Flye Assembler 54 .
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: The Flye 70 assembler (v.2.8.1) was used to assemble the genomes, with the HiFi-error set to 0.003, min-overlap set at 2000 and other options kept as the default.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Version used: **2.9**
- Evidence: 77 ); (2) Flye v.2.9 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Version used: **2.9.5**
- Evidence: The resulting reads were assembled using Flye (v.2.9.5) and specifying the parameters --genome-size 3 m --asm-coverage 40.
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Evidence: The genomes of Lek174 and Lek79 were sequenced using MinION (Oxford Nanopore Technologies) and MiSeq, and their genomic contigs were generated from the obtained long reads and short reads using Flye 42 , BWA 43 , 44 and Pilon 45 programs.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **2.9**
- Evidence: These were then parsed into Flye (v.2.9) 25 with the --nano-hq flag.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Version used: **2.9.0**
- Evidence: 74 ), Flye v.2.9.0 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Telomere-to-telomere assembly using HERRO-corrected Nanopore Simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10563-y | PMCID: PMC13323052 | PMID: 42045451
- Evidence: These include Canu 8 plus purge_dups 9 , FALCON-Unzip 10 , Flye 11 plus HapDup 12 , 13 , Shasta 14 and PECAT 15 .
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BEDTools, BUSCO, Canu, Flye, QUAST]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: Multi-contig genomes were stitched together using 2 kb ‘N’ spacers in the order output by Flye.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Version used: **2.9**
- Evidence: The HiFi reads for the mouse-derived strains were assembled using both Canu v.2.1.1 and Flye v.2.9 with the following parameters: Canu (-pacbio-hifi, genomeSize = 2.5 M, minReadLength = 2200) and Flye (-g 2.5 m, --min-overlap 2200, --pacbio-hifi).
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **2.9.3**
- Evidence: Retaining reads with a minimum length of 1 kbp that aligned to the reference with at least 95% identity across at least 200 bp, we assembled the reads with Flye (v.2.9.3) 134 (with the options -- pacbio-hifi and -- scaffold ) to generate new MAGs and repeated the read mapping and assembly step to generate two MAGs of one (MAG48; GCA_977880245 ), two (MAG13; GCA_977880235 ) and seven (MAG20; GCA_97...
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **2.9.2**
- Evidence: Oxford Nanopore reads were quality trimmed using BBDuk Trimmer v.1.0 with the following settings: qtrim=rl trimq=6 minlength=50 ordered=t qin=33 (BBMap—Bushnell B.— sourceforge.net/projects/bbmap ) and de novo assembled using Flye v.2.9.2 (ref.
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: For MFD09848.bin.1.115 (NCBI: GCA_974504955.1 ), reads mapping to contigs of the Nitrososphaerota phylum were extracted with the Samtools view -q 20 -m 1000 command and assembled using Flye 143 (v.2.9.3) with the following settings: --nano-hq, --meta, --extra-params min_read_cov_cutoff = 12.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Evidence: 41 ), an alternative assembler to Flye.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### A squalene-hopene cyclase in <i>Schizosaccharomyces japonicus</i> represents a eukaryotic adaptation to sterol-limited anaerobic environments. (PNAS 2021)

- DOI: 10.1073/pnas.2105225118 | PMCID: PMC8364164 | PMID: 34353908
- Version used: **2.7.1**
- Evidence: Genome assembly was performed using Flye version 2.7.1-b167359 ( 87 ).
- Full pipeline: read trimming [RAxML v0.8.1] -> alignment/mapping [HMMER, MAFFT v7.402, RAxML v0.8.1] -> stage not stated [Flye v2.7.1, Pilon v1.18]

### Metabolic novelty originating from horizontal gene transfer is essential for leaf beetle survival. (PNAS 2022)

- DOI: 10.1073/pnas.2205857119 | PMCID: PMC9546569 | PMID: 36161953
- Version used: **2.8.3**
- Evidence: The draft genome was assembled using Flye 2.8.3 ( 68 ) with setting minimum overlap as 10 kb and with “-meta” option.
- Full pipeline: stage not stated [BLAST, BUSCO, Flye v2.8.3, InterProScan, R v9.4]

### Leafy and weedy seadragon genomes connect genic and repetitive DNA features to the extravagant biology of syngnathid fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2119602119 | PMCID: PMC9245644 | PMID: 35733255
- Evidence: We assembled both genomes with Flye ( 14 ), using all PacBio data excluding “scraps” and an estimated genome size of 600 Mb, followed by two rounds of polishing with the tool arrow ( 15 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [InterProScan, STAR] -> dimensionality reduction/clustering [BLAST] -> stage not stated [BUSCO, Flye, RepeatMasker]

### <i>duper</i> is a null mutation of Cryptochrome 1 in Syrian hamsters. (PNAS 2022)

- DOI: 10.1073/pnas.2123560119 | PMCID: PMC9170138 | PMID: 35471909
- Version used: **2.7**
- Evidence: Flye v2.7 ( 49 ) was used to generate a de novo assembly of the filtered nanopore reads requiring a minimum of 8 Kb overlap among reads.
- Full pipeline: stage not stated [BUSCO v4.0.6, Flye v2.7, GATK, SAMtools, SnpEff]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Version used: **2.9**
- Evidence: These reads were assembled using Flye v2.9 ( 58 ) (settings --nana-hq --meta -g 100m --read-error 0.03 --iterations 3).
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Origins of genome-editing excisases as illuminated by the somatic genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213887120 | PMCID: PMC9942806 | PMID: 36669098
- Version used: **2.7**
- Evidence: The MAC-enriched fraction was sequenced using PacBio HiFi reads and the MAC genome assembled with Flye (version 2.7-b1585) ( 19 ).
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [RepeatMasker v2.0.1] -> stage not stated [BUSCO, Flye v2.7, HMMER, OrthoFinder, eggNOG]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: Base called fastq files were assembled using Flye [version 2.9; ( 63 )] at a depth of 38×, assuming a 557 megabase genome [Kmer-based genome size estimates were performed with FindGSE ( 64 )] into a pseudohaploid primary assembly.
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **2.8.1**
- Evidence: Analysis of an initial assembly with Flye v2.8.1 ( 91 ) (option: --pacbio-hifi) showed that the genome was probably diploid; therefore, CCS reads were assembled again with the diploid-aware assembler Falcon (Bioconda package pb-falcon 2.2.4 installed with package pb-assembly v0.0.8) ( 92 ) using a relatively low identity threshold of 0.96 for collapsing heterozygosity (option: overlap_filtering_se...
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### Resolving the 22q11.2 deletion using CTLR-Seq reveals chromosomal rearrangement mechanisms and individual variance in breakpoints. (PNAS 2024)

- DOI: 10.1073/pnas.2322834121 | PMCID: PMC11295037 | PMID: 39042694
- Evidence: First, on-target nanopore reads longer than 40 kb (base called in super accuracy mode using Dorado) were extracted and assembled using Flye versions 2.6 and 2.9 ( 35 ) (––keep-haplotypes, –nano-hq, or –nano-corr).
- Full pipeline: alignment/mapping [BWA, minimap2 v2.18] -> variant calling [Flye] -> stage not stated [Medaka v1.9.1]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Version used: **2.9.1**
- Evidence: A de novo genome assembly at the contig level was created using Flye (v2.9.1) ( 83 ) with parameter --nano-raw, this including reads overlap, repeat classification and polisher module.
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Endogenous virophages are active and mitigate giant virus infection in the marine protist <i>Cafeteria burkhardae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2314606121 | PMCID: PMC10945749 | PMID: 38446847
- Version used: **2.9.1**
- Evidence: A draft assembly was generated with Flye v2.9.1 ( 53 ) from reads longer than 4 kb with default settings.
- Full pipeline: alignment/mapping [minimap2 v2.22] -> stage not stated [BLAST, Flye v2.9.1, SAMtools]

### Short macrocyclic peptides in sponge genomes. (PNAS 2024)

- DOI: 10.1073/pnas.2314383121 | PMCID: PMC10945851 | PMID: 38442178
- Evidence: The raw long reads from nanopore were corrected using Ratatosk ( 49 ) using the short Illumina reads, and then assembled using Flye ( 50 ).
- Full pipeline: machine learning [AUGUSTUS v3.3] -> stage not stated [BLAST, Flye]

### Environmental radiation exposure at Chornobyl has not systematically affected the genomes or chemical mutagen tolerance phenotypes of local worms. (PNAS 2024)

- DOI: 10.1073/pnas.2314793121 | PMCID: PMC10945782 | PMID: 38442158
- Version used: **2.8.1**
- Evidence: Contigs were assembled with Flye v2.8.1 (flye –nano-raw –genome-size 60m –iterations 1 –meta) ( 46 ) and then cleaned with Oxford Nanopore’s Medaka (medaka_consensus -m r941_in_high_g360) and Racon v 1.4.19 ( 47 ) using default settings.
- Full pipeline: alignment/mapping [GATK v4.3.0.0, R, SAMtools v1.11, VCFtools v0.1.16, minimap2] -> variant calling [GATK v4.3.0.0] -> stage not stated [BCFtools v1.14, Flye v2.8.1, ImageJ]

### In-patient evolution of a high-persister <i>Escherichia coli</i> strain with reduced in vivo antibiotic susceptibility. (PNAS 2024)

- DOI: 10.1073/pnas.2314514121 | PMCID: PMC10801923 | PMID: 38190524
- Evidence: Briefly, long-read assemblies were created with Flye-v2.9-b1768 ( 62 ) and polished with the long-reads using Racon-v1.4.21 ( 63 ) and Medaka-v1.4.4 (nanoporetech GitHub: https://github.com/nanoporetech/medaka ).
- Full pipeline: stage not stated [Flye, Medaka]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **2.8.1**
- Evidence: ... 30 -z 1 -n 5” and then were corrected by NEXTDENOVO (v2.4.0) ( https://github.com/Nextomics/NextDenovo ) with default parameters and assembled using Flye (v2.8.1-b1676) ( 62 ) with parameters “--nano-raw --iterations 2.” Assembled contigs were further polished by NextPolish (v1.3.1) ( https://github.com/Nextomics ) with minimap2_options parameter “-x map-ont” for three rounds using Illumina reads...
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Synergistic interactions between &lt;i&gt;Candida albicans&lt;/i&gt; and &lt;i&gt;Enterococcus faecalis&lt;/i&gt; promote toxin-dependent host cell damage. (PNAS 2025)

- DOI: 10.1073/pnas.2505310122 | PMCID: PMC12646220 | PMID: 41213026
- Version used: **2.9.3**
- Evidence: The basecalled reads were assembled and polished using Flye (v2.9.3), Medaka (v1.11.3), and Racon (v1.4.20).
- Full pipeline: stage not stated [Flye v2.9.3, Medaka v1.11.3]

### Symbiotic solutions for colony nutrition: Conserved nitrogen recycling within the bacterial pouch of &lt;i&gt;Tetraponera&lt;/i&gt; ants. (PNAS 2025)

- DOI: 10.1073/pnas.2514882122 | PMCID: PMC12595465 | PMID: 41150726
- Version used: **2.9**
- Evidence: PacBio HiFi reads were quality-filtered using Filtlong v0.2.0 ( https://github.com/rrwick/Filtlong ) with a minimum read length of 1,000 bp and then assembled with Flye v2.9 ( 72 ) using a minimum overlap of 1,000 bp.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic] -> read trimming [FastQC v0.11.9, Trimmomatic] -> differential/statistical testing [QUAST] -> stage not stated [BLAST, Flye v2.9, RAxML v8.2.12]

### Functional genetic elements of a butterfly mimicry supergene. (PNAS 2025)

- DOI: 10.1073/pnas.2509864122 | PMCID: PMC12541413 | PMID: 41060750
- Evidence: Reads were then assembled using Flye ( 55 ) then polished using Medaka.
- Full pipeline: stage not stated [Flye, HOMER v4.11, MACS2]

### Phage-based delivery of CRISPR-associated transposases for targeted bacterial editing. (PNAS 2025)

- DOI: 10.1073/pnas.2504853122 | PMCID: PMC12318184 | PMID: 40711918
- Evidence: Briefly, the overnight culture was pelleted, genomic DNA was extracted and sequenced with ONT long-reads, sequencing reads were assembled with Flye, and the assembly was annotated using Bakta ( 54 , 55 ) (Plasmidsaurus).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Flye]

### A selfish supergene causes meiotic drive through both sexes in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421185122 | PMCID: PMC12054836 | PMID: 40267129
- Version used: **2.9**
- Evidence: Initial assemblies were performed with Flye v2.9 ( 51 ), consensus sequences were built with Racon v1.4.20 ( 52 ), and three rounds of polishing were done with the appropriate Illumina reads using Pilon v1.24 ( 53 ).
- Full pipeline: alignment/mapping [BEDTools, MAFFT] -> stage not stated [Flye v2.9, Pilon v1.24, R v4.3.0, phytools]

### &lt;i&gt;Chlamydomonas&lt;/i&gt; chloroplast genes tolerate compression of the genetic code to just 51 codons. (PNAS 2026)

- DOI: 10.1073/pnas.2506263123 | PMCID: PMC12799115 | PMID: 41493811
- Evidence: Assemblies were performed with the Flye assembler.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [Flye]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Version used: **2.9**
- Evidence: ...ction factor of 4 specified with -r 4 and window size of 64 specified with -w 64 ( https://github.com/cschin/peregrine-2021?tab=readme-ov-file ), and Flye v.2.9-b1774 ( 60 ).
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

