# Canu

- **Category:** genomics
- **Papers in survey:** 29
- **Journals:** PNAS (17), Nature (9), Science (1), Lancet (1), Cell (1)
- **Years:** 2021 (4), 2022 (7), 2023 (8), 2024 (2), 2025 (3), 2026 (5)
- **Versions named:** 2.1.1 (5), 1.8 (3), 1.6 (3), 2.2 (2), 2.0 (1), 1.7.1 (1), 2.1 (1), 1.1 (1), 1.9 (1), 1.3 (1)
- **Pipeline stages it appears in:** alignment/mapping (2), read trimming (2), variant calling (2), structure determination (1)

## Papers

### Two-component spike nanoparticle vaccine protects macaques from SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.035 | PMCID: PMC7834972 | PMID: 33577765
- Evidence: N/A GraphPad Prism v8 GraphPad N/A XCalibur Version v4.2 Thermo Fisher N/A Orbitrap Fusion Tune application v3.1 Thermo Fisher N/A Flowjo v10 Flowjo N/A UCSF ChimeraX Goddard et al., 2018 N/A GraphPad Prism v7 GraphPad N/A Canu Koren et al., 2017 https://github.com/marbl/canu Minimap2 Li, 2018 https://github.com/lh3/minimap2 Varscan Koboldt et al., 2012 http://varscan.sourceforge.net/ Longshot Edg...
- Full pipeline: stage not stated [Canu, ChimeraX, minimap2]

### Elective surgery system strengthening: development, measurement, and validation of the surgical preparedness index across 1632 hospitals in 119 countries. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)01846-3 | PMCID: PMC9621702 | PMID: 36328042
- Evidence: ...nzo Dario Mandato , Lorenzo Aguzzoli , Jlenia Sarnari , Gabriela E Nita , Nicolò Fabbri , Michele Rubbini , Roberta Tutino , Mauro Podda , Gian Luigi Canu , Enrico Peiretti , Sokol Trungu , Mario D'Oria , Andrea Lauretta , Matteo Marro , Francesco Guerrera , Mauro Santarelli , Stefano Salizzoni , Oreste Iocca , Pasquale Di Maio , Teresa Perra , Alberto Porcu , Antonio M Scanu , Giovanni Pirozzolo ...
- Full pipeline: stage not stated [Canu, ggplot2, tidyverse]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: Canu 77 1.5+67 was used to generate the combined PacBio CLR and Oxford Nanopore ONT assembly.
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Version used: **2.0**
- Evidence: The ONT recommended subset reads were then assigned using splitHaplotigs in Canu v2.0 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Identification of trypsin-degrading commensals in the large intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-05181-3 | PMCID: PMC9477747 | PMID: 36071157
- Version used: **1.8**
- Evidence: Error correction of the trimmed reads was conducted by Canu (v.1.8) with additional options (corOutCoverage = 10,000, corMinCoverage = 0, corMhapSensitivity = high) after internal control removal and adapter trimming by Sequel.
- Full pipeline: read trimming [BWA, Canu v1.8] -> alignment/mapping [BWA, ChimeraX, PyMOL] -> quantification [BWA] -> normalisation [BWA] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold, Prokka, fastp v0.20.0, minimap2 v2.17]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **1.7.1**
- Evidence: PacBio reads were self-corrected using Canu (v.1.7.1) before assembly with Flye (v.2.4.2) 72 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **2.1.1**
- Evidence: Aligned reads were converted to FASTQ format with SAMtools (version 1.16.1) 59 and assembled with Canu (version 2.1.1) 60 in the PacBio HiFi mode with expected genome sizes ranging from 120 kb to 400 kb in 10-kb increments.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **2.2**
- Evidence: For Megaderma spasma , we ran Canu v.2.2 in -nanopore mode and created the primary contig sets using purge-dups as above.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Telomere-to-telomere assembly using HERRO-corrected Nanopore Simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10563-y | PMCID: PMC13323052 | PMID: 42045451
- Evidence: These include Canu 8 plus purge_dups 9 , FALCON-Unzip 10 , Flye 11 plus HapDup 12 , 13 , Shasta 14 and PECAT 15 .
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BEDTools, BUSCO, Canu, Flye, QUAST]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Version used: **2.1.1**
- Evidence: The HiFi reads for the mouse-derived strains were assembled using both Canu v.2.1.1 and Flye v.2.9 with the following parameters: Canu (-pacbio-hifi, genomeSize = 2.5 M, minReadLength = 2200) and Flye (-g 2.5 m, --min-overlap 2200, --pacbio-hifi).
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **2.2**
- Evidence: We then generated de novo genome assemblies using Canu (v.2.2; genomeSize = 10 maxInputCoverage = 100).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: Briefly, the PacBio raw reads were corrected by Canu ( 51 ) with the following parameters: minReadLength >3,000 and minOverlapLength >500.
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### Long-read assembly of a Great Dane genome highlights the contribution of GC-rich sequence and mobile elements to canine genomes. (PNAS 2021)

- DOI: 10.1073/pnas.2016274118 | PMCID: PMC7980453 | PMID: 33836575
- Version used: **1.3**
- Evidence: Primary contigs were supplemented with contigs obtained from a local assembly of reads aligning to gaps between contigs on CanFam3.1 using Canu v1.3 ( 42 ).
- Full pipeline: alignment/mapping [Canu v1.3, Cufflinks v2.2.1, minimap2 v2.9] -> stage not stated [RepeatMasker v4.0.7, kallisto v0.46.0]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: Noting that some telomeres were missing, we created additional assemblies using Canu v2 ( 86 ) with all reads from all strains of the two nuclear genotypes, which successfully reconstructed most telomeres.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Evidence: We next used Canu ( 53 ) to assemble the genome with the PacBio reads and obtained a 2.89-Gb genome with a contig N50 of 1.51 Mb.
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Multiple genetic paths including massive gene amplification allow <i>Mycobacterium tuberculosis</i> to overcome loss of ESX-3 secretion system substrates. (PNAS 2022)

- DOI: 10.1073/pnas.2112608119 | PMCID: PMC8872769 | PMID: 35193958
- Version used: **1.8**
- Evidence: ( A ) Nanopore sequencing of Δ esxGH ::361-EV M18 generated two contigs after Canu (v1.8) assembly, which were polished and stitched together to create a single linear contig on BioMatters Geneious R11 software by merging of overlapping sequences as described in SI Appendix , SI Materials and Methods .
- Full pipeline: stage not stated [Canu v1.8]

### The exceptional form and function of the giant bacterium <i>Ca.</i> Epulopiscium viviparus revolves around its sodium motive force. (PNAS 2023)

- DOI: 10.1073/pnas.2306160120 | PMCID: PMC10756260 | PMID: 38109545
- Version used: **1.1**
- Evidence: PacBio reads were either self-corrected using Canu 1.1 ( 91 ), or corrected with quality-controlled Illumina reads, using LoRDEC ( 92 ).
- Full pipeline: quantification [pheatmap] -> stage not stated [Canu v1.1, InterProScan]

### The emergence and diversification of a zoonotic pathogen from within the microbiota of intensively farmed pigs. (PNAS 2023)

- DOI: 10.1073/pnas.2307773120 | PMCID: PMC10666105 | PMID: 37963246
- Version used: **1.9**
- Evidence: Hybrid assemblies, using filtered PacBio and Illumina reads, and preliminary assemblies of long-read data assembled with Canu v1.9 ( 55 ) were generated with Unicycler v0.4.7 using the normal mode and default settings ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v1.2.2, QUAST v5.0.1] -> stage not stated [Canu v1.9, Prokka v1.14.5, R]

### Sex-linked gene traffic underlies the acquisition of sexually dimorphic UV color vision in <i>Heliconius</i> butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2301411120 | PMCID: PMC10438391 | PMID: 37552755
- Version used: **1.6**
- Evidence: We generated two initial assemblies, one with Falcon ( 45 ) and the other with Canu (v1.6) ( 46 ).
- Full pipeline: quality control [Bowtie2 v2.2.7, Kraken2] -> alignment/mapping [BEDTools, Bowtie2 v2.2.7, MUSCLE] -> differential/statistical testing [R] -> stage not stated [Canu v1.6, Pilon, StringTie]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **2.1.1**
- Evidence: Due to the heterozygous nature of the wild individual, we assembled the sequences with Canu 2.1.1 ( 60 ) using the options “corOutCoverage=200 correctedErrorRate=0.16 batOptions=-dg 3 -db 3 -dr 1 -ca 500 -cp 50”.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **2.1.1**
- Evidence: Basecalled reads passing filtering were demultiplexed and assembled with Canu v2.1.1 ( 70 ).
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **1.6**
- Evidence: These partitioned reads were used for assembling the four haploid assemblies (one Bb, one Bj and two Bf) by Canu (1.6) ( 70 ) (“corOutCoverage=200 correctedErrorRate=0.15”) and Falcon (“pa_daligner_option= -k18 -e0.7 -l2000 -h480 -w8 -s100, ovlp_daligner_option=-k24 -e.93 -l2000 -h600 -s100”).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Version used: **2.1.1**
- Evidence: Whole genome assemblies were generated for the CU and PU strains with ONT long reads via Canu v2.1.1 (genome size 20 Mb) ( 67 ), followed by short-read polishing via medaka v0.8.1 (1X) ( https://github.com/nanoporetech/medaka ) and pilon v1.23 (3X) ( 68 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Two-speed genome evolution drives pathogenicity in fungal pathogens of animals. (PNAS 2023)

- DOI: 10.1073/pnas.2212633120 | PMCID: PMC9926174 | PMID: 36595674
- Version used: **1.8**
- Evidence: Canu v.1.8 ( 87 ) was used to assemble reads ≥ 100 kb (~13× coverage) with stopOnLowCoverage = 0.5, genomeSize = 0.6 g and minReadLength = 500.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, RAxML] -> stage not stated [BUSCO, Canu v1.8, GATK, HMMER, RepeatMasker v4.0.5]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: The CTL array structure was confirmed by comparison with other assemblies of these data generated with Canu ( 44 ), Peregrine ( 45 ), and alternative versions of hifiasm ( SI Appendix , Table S3 ), where the break was fully resolved ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### The extent of introgression between incipient <i>Clarkia</i> species is determined by temporal environmental variation and mating system. (PNAS 2024)

- DOI: 10.1073/pnas.2316008121 | PMCID: PMC10963018 | PMID: 38466849
- Version used: **2.1**
- Evidence: We used Canu (v.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, Picard, SAMtools] -> variant calling [GATK v3.8.0] -> stage not stated [BCFtools, Canu v2.1, RAxML v8.2.11]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **1.6**
- Evidence: PacBio reads were reassembled with Microbial Assembly (smrtlink10), HGAP4, and Canu (version 1.6) software.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Insights into cephalochordate genome and gene evolution from the early-diverging amphioxus &lt;i&gt;Asymmetron lucayanum&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2521280123 | PMCID: PMC13012124 | PMID: 41860958
- Evidence: De novo genome assembly was primarily performed by Canu ( 76 ) with additional haplotype decoupling and chromosome-level elevation.
- Full pipeline: variant calling [Canu] -> stage not stated [OrthoFinder]

### Recurrent acquisition of nuclease-protease pairs in antiviral immunity. (Science 2026)

- DOI: 10.1126/science.aea8769 | PMCID: PMC12799240 | PMID: 41231971
- Evidence: To test Canu activity, we challenged E. coli heterologously expressing Kae CanABC.
- Full pipeline: stage not stated [AlphaFold, Canu]

