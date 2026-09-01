# Pilon

- **Category:** genomics
- **Papers in survey:** 31
- **Journals:** PNAS (20), Nature (10), Cell (1)
- **Years:** 2021 (7), 2022 (7), 2023 (5), 2024 (6), 2025 (5), 2026 (1)
- **Versions named:** 1.23 (9), 1.22 (4), 1.24 (2), 1.18 (2)
- **Pipeline stages it appears in:** alignment/mapping (4), read trimming (1), structure determination (1)

## Papers

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Evidence: ...i-lab/scirpy BLASTp v2.12.0+ Altschul et al., 1997 https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins Lifelines v0.26.0 (Python package) Davidson-Pilon, 2021 https://github.com/CamDavidsonPilon/lifelines scikit-learn v0.24.2 (Python package) Pedregosa et al., 2011 https://github.com/scikit-learn/scikit-learn IgBLAST Ye et al., 2013 https://www.ncbi.nlm.nih.gov/igblast/ Immunarch v0.6.5 (R pack...
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Version used: **1.23**
- Evidence: 68 ), and subsequently used for polishing using Pilon v.1.23 (ref.
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: Short-read polishing Illumina polishing benchmarking was performed using Longranger 83 2.1.3 and Pilon 84 1.21 with --fix bases, local option (Supplementary Table 5 ).
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **1.23**
- Evidence: 55 ), and then two rounds of Pilon v.1.23 (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **1.23**
- Evidence: Errors in the primary assembly were first corrected using PacBio subreads using racon (v.1.4.10) 73 , and Illumina paired-end reads were then mapped to the contigs using bwa-mem 74 to polish the contigs using Pilon (v.1.23, Broad Institute) 75 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Polishing and validation of the Loki-B35 genome was performed using four rounds of Pilon 79 as part of the validation pipeline of metagenomic assemblies proposed previously 80 .
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **1.23**
- Evidence: Then, the polished genome sequences were error-corrected using the short insert size reads by Pilon (v.1.23) 57 with default settings.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Version used: **1.23**
- Evidence: The alignment was used for assembly polishing first with ONT reads with Racon (v.1.4.16) 50 and then by ten rounds of polishing using trimmed, unmapped Illumina reads by Pilon (v.1.23) 51 .
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: Illumina short reads and PacBio long reads (CLRs) were provided to OPERA-MS and assembled using the built-in OPERA-MS genome database and the default settings (the latter includes polishing of output MAGs with Pilon 39 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Evidence: The genomes of Lek174 and Lek79 were sequenced using MinION (Oxford Nanopore Technologies) and MiSeq, and their genomic contigs were generated from the obtained long reads and short reads using Flye 42 , BWA 43 , 44 and Pilon 45 programs.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **1.23**
- Evidence: Finally, we performed three rounds of contig polishing with Pilon (v.1.23) using publicly available Illumina sequencing datasets from each species (Sequence Read Archive (SRA) accession numbers SRX5619117, SRX5619118 and SRX5619119).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Version used: **1.22**
- Evidence: The draft genome was polished with Pilon v1.22 ( 56 ) using the Illumina reads under the default settings.
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### A squalene-hopene cyclase in <i>Schizosaccharomyces japonicus</i> represents a eukaryotic adaptation to sterol-limited anaerobic environments. (PNAS 2021)

- DOI: 10.1073/pnas.2105225118 | PMCID: PMC8364164 | PMID: 34353908
- Version used: **1.18**
- Evidence: Flye contigs were polished using Pilon version 1.18 ( 88 ).
- Full pipeline: read trimming [RAxML v0.8.1] -> alignment/mapping [HMMER, MAFFT v7.402, RAxML v0.8.1] -> stage not stated [Flye v2.7.1, Pilon v1.18]

### Nuclear envelope budding is a response to cellular stress. (PNAS 2021)

- DOI: 10.1073/pnas.2020997118 | PMCID: PMC8325156 | PMID: 34290138
- Evidence: We thank Marc Pilon for providing the C. elegans worms and for contributing intellectually to the manuscript writing.
- Full pipeline: structure determination [IMOD] -> stage not stated [Pilon]

### Three genomes in the algal genus <i>Volvox</i> reveal the fate of a haploid sex-determining region after a transition to homothallism. (PNAS 2021)

- DOI: 10.1073/pnas.2100712118 | PMCID: PMC8166075 | PMID: 34011609
- Version used: **1.22**
- Evidence: The Illumina data were then used to improve the assembly sequence with Pilon v.1.22 software tool, ultimately giving a set of nuclear genome sequence ( SI Appendix , Table S2 ).
- Full pipeline: alignment/mapping [AUGUSTUS] -> stage not stated [BUSCO, Pilon v1.22]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: The primary assembly was polished by Illumina short reads using Pilon with default parameters ( 25 ).
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: We refined the primary assembly by using both PacBio long-read data and BGISEQ short-read data with Pilon ( 53 ).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Spatial scale of tuberculosis transmission in Lima, Peru. (PNAS 2022)

- DOI: 10.1073/pnas.2207022119 | PMCID: PMC9659349 | PMID: 36322726
- Evidence: We mapped the paired-end raw sequencing data to the H37Rv reference genome using the BWA-MEM (Burroughs Wheeler Aligner-Maximal Exact Match) algorithm ( 11 ) and used SAMtools and Pilon to identify the single-nucleotide polymorphisms (SNPs) and the insertions and deletions using a coverage-based approach ( 12 , 13 ).
- Full pipeline: alignment/mapping [BWA, Pilon, SAMtools]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **1.22**
- Evidence: 2000 and polished the assembly with Pilon v1.22 (parameters “–mindepth 10 –changes –threads 4 –fix bases.”) ( 55 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **1.18**
- Evidence: Finally, Pilon (v1.18) ( 74 ) were used to perform a second round of error correction with Illumina PE reads (insertion size = 350 bp).
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Sex-linked gene traffic underlies the acquisition of sexually dimorphic UV color vision in <i>Heliconius</i> butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2301411120 | PMCID: PMC10438391 | PMID: 37552755
- Evidence: This assembly was polished twice with Arrow from SMRT Analysis (v5.1.0) ( 47 ) and then twice with Pilon ( 48 ) using 1,203 million 150 bp PE reads ( SI Appendix , Table S4 ).
- Full pipeline: quality control [Bowtie2 v2.2.7, Kraken2] -> alignment/mapping [BEDTools, Bowtie2 v2.2.7, MUSCLE] -> differential/statistical testing [R] -> stage not stated [Canu v1.6, Pilon, StringTie]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **1.22**
- Evidence: Accuracy of draft assemblies was improved with Medaka v1.5.0 or Nanopolish v0.11.2, and further polished with Pilon v1.22 ( 71 ) using Illumina paired end reads.
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### Phase variation as a major mechanism of adaptation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301394120 | PMCID: PMC10334774 | PMID: 37399390
- Evidence: We used Pilon (settings: --variant) on the resulting BAM files to generate VCF files that contained calls for all reference positions corresponding to H37Rv from pileup ( 61 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BCFtools, GEMMA, IQ-TREE, Picard, Pilon, SAMtools]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Version used: **1.23**
- Evidence: Variants were called using Pilon v1.23 ( 37 ).
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Version used: **1.24**
- Evidence: Contigs were then polished to improve the single-base accuracy in a single round of polishing with Medaka [version1.5.0; ( 65 )] using the ONT long reads, followed by a second round of polishing incorporating paired-end Illumina HiSeq data with Pilon (version 1.24) ( 66 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### A wound-induced differentiation trajectory for neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2322864121 | PMCID: PMC11260127 | PMID: 38976727
- Version used: **1.23**
- Evidence: Basecalling was performed using the gpu version of Guppy (v6.0.1), assembled using Shasta (v0.1.0), and polished using previously published short reads ( 54 ) using Pilon (v1.23).
- Full pipeline: read trimming [RAxML v8.2.4] -> alignment/mapping [MUSCLE v3.8.31, RAxML v8.2.4] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [BUSCO v3.0.2, Pilon v1.23]

### Global diversity of enterococci and description of 18 previously unknown species. (PNAS 2024)

- DOI: 10.1073/pnas.2310852121 | PMCID: PMC10927581 | PMID: 38416678
- Version used: **1.23**
- Evidence: The assembly was polished by aligning Illumina reads to assembly contigs using bwa mem (v0.7.4) ( 52 ) and then Pilon (v1.23) ( 53 ) was run with the --fix bases parameter.
- Full pipeline: alignment/mapping [IQ-TREE v1.7, MAFFT, Pilon v1.23] -> dimensionality reduction/clustering [HMMER, OrthoFinder v2.3.3]

### Chemokine/cytokine-releasing biomaterials induce in situ tertiary lymphoid-like structures and enhance antitumor immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2409560122 | PMCID: PMC12625823 | PMID: 41183186
- Evidence: Shari Pilon-Thomas for providing human TIL, Dr.
- Full pipeline: stage not stated [Pilon]

### Amazonian and Andean tree communities are not tracking current climate warming. (PNAS 2025)

- DOI: 10.1073/pnas.2425619122 | PMCID: PMC12402989 | PMID: 40828017
- Evidence: In Bolivia, the elevational gradient encompasses mature forests ranging from 200 m to 3,400 m in the Madidi region, including the protected areas of Madidi National Park (13.80° S, 67.63° W), Apolobamba (14.99° S, 68.82° W), and the Pilon-Lajas Biosphere Reserve (15.00° S, 67.33° W).
- Full pipeline: stage not stated [Pilon]

### Genomic map of the functionally extinct northern white rhinoceros (&lt;i&gt;Ceratotherium simum cottoni&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2401207122 | PMCID: PMC12107126 | PMID: 40359041
- Evidence: The scaffolds were then polished using Racon ( 26 ) and Pilon ( 27 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BUSCO, Pilon]

### A selfish supergene causes meiotic drive through both sexes in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421185122 | PMCID: PMC12054836 | PMID: 40267129
- Version used: **1.24**
- Evidence: Initial assemblies were performed with Flye v2.9 ( 51 ), consensus sequences were built with Racon v1.4.20 ( 52 ), and three rounds of polishing were done with the appropriate Illumina reads using Pilon v1.24 ( 53 ).
- Full pipeline: alignment/mapping [BEDTools, MAFFT] -> stage not stated [Flye v2.9, Pilon v1.24, R v4.3.0, phytools]

