# hifiasm

- **Category:** genomics
- **Papers in survey:** 34
- **Journals:** Nature (24), PNAS (10)
- **Years:** 2022 (2), 2023 (7), 2024 (6), 2025 (14), 2026 (5)
- **Versions named:** 0.13 (3), 0.11 (2), 0.16.1 (2), 0.15.3 (1), 0.14.1 (1), 15.1 (1), 0.19.9 (1), 0.16.0 (1)
- **Pipeline stages it appears in:** variant calling (6), alignment/mapping (2), read trimming (1)

## Papers

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: Trio phasing hifiasm contig pipeline (asm9) Hifiasm finds alignments between HiFi reads and corrects sequencing errors observed in alignments 31 .
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Evidence: Genomes of the 44 HiFi sequenced accessions were assembled by hifiasm 54 ( https://github.com/chhylp123/hifiasm ), using default parameters.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Version used: **15.1**
- Evidence: Genome assembly PacBio HiFi reads were assembled using hifiasm (v.15.1) 61 with the default parameters ( https://github.com/chhylp123/hifiasm/ ) to generate primary contig assemblies.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Version used: **0.16.1**
- Evidence: The genome of B. microptera was assembled using wtdbg (v.2.4) 73 , and the sponge genomes were assembled using hifiasm (v.0.16.1-r375) 74 .
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### Increased mutation and gene conversion within human segmental duplications. (Nature 2023)

- DOI: 10.1038/s41586-023-05895-y | PMCID: PMC10172114 | PMID: 37165237
- Evidence: HPRC haplotypes were assembled using PacBio HiFi with hifiasm 3 , 54 creating contiguous long-read assemblies.
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [hifiasm] -> stage not stated [RepeatMasker v4.1.2]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: Only the sample HG002 was re-assembled with Trio-Hifiasm (v.0.14.1), which is explained in more detail in the next subsection. hifiasm -o ${SAMPLE_NAME} -t 48 -1 pat.yak -2 mat.yak hifi.fq.gz Hifiasm produces one graph per haplotype in GFA format.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **0.11**
- Evidence: Methods Genome assembly and validation PacBio HiFi reads were assembled using hifiasm v0.11-r302 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Version used: **0.11**
- Evidence: Genome sequence assembly and validation PacBio HiFi reads were assembled using hifiasm (v.0.11-r302) 59 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **0.16.1**
- Evidence: For Ae. tauschii , HiFi reads were assembled using hifiasm (v0.16.1) 50 with parameters “-l0 -u -f38” optimized for homozygous and large genomes (-l0 -f38) and to minimize misassemblies by disabling the post-join contigs step (-u), favouring accuracy over contiguity.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: Software for bioinformatics analyses Further software that was used during the analysis of the sequencing data that is described in the Supplementary Information : hifiasm-meta 69 v.0.2-r043 for the assembly of long-read metagenomes; CompareM v.0.1.2 ( https://github.com/dparks1134/CompareM ) for the calculation of average amino acid identity between Ca .
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: Targeted sequence assembly and validation of centromeric regions To generate complete assemblies of centromeric regions from the CHM1, HG00733, chimpanzee, orangutan and macaque genomes, we first assembled each genome from PacBio HiFi data ( Supplementary Table 1 ) using hifiasm 24 (v.0.16.1).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Evidence: We additionally created hifiasm (ultra-long; v.0.19.6) 10 assemblies ( Supplementary Methods ), which were used to complement our analysis of the most challenging regions (centromeres and Yq12).
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **0.13**
- Evidence: Diploid genome assembly HiFi reads were assembled with hifiasm (0.13-r308) 46 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: First, a phased primary assembly was obtained by running Hifiasm 55 using 50 Gb of PacBio HiFi reads in combination with Dovetail Omni-C reads with the following command: hifiasm -o out.phased.asm.hic --h1 hic.R1.fastq.gz --h2 hic.R2.fastq.gz hifi.reads.fastq.gz.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Generation of phased genome assemblies Phased genome assemblies were generated using two different algorithms, namely Verkko (v.1.3.1 and v.1.4.1) 16 and hifiasm (UL) with ONT support (v.0.19.5) 17 .
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Evidence: Initial genome assemblies were generated with hifiasm 21 (v.0.7) with default settings, and contigs with low sequencing support were purged.
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: The final assembly of the chloroplast genome was then performed using hifiasm 61 (v.0.16.0) with default parameters.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Evidence: Sequencing reads from each sample were assembled using hifiasm 64 and the exact parameters and software version varied between the samples based on the level of estimated heterozygosity and are reported in Supplementary Table 2 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **0.13**
- Evidence: For six species ( Aselliscus stoliczkanus , Hipposideros larvatus , Rhinolophus affinis , R. perniger lanosus , R. yonghoiseni and R. trifoliatus ), we created contig assemblies using hifiasm v.0.13 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Evidence: We then assembled haplotype-resolved assemblies with the HiFi reads and Hi-C reads using hifiasm ( https://github.com/chhylp123/hifiasm ) (v.0.16) 67 with default parameters.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: Genome assemblies Contig-level assembly Approximately 30× HiFi reads, combined with ONT-UL reads exceeding 100 kb, were processed using the hifiasm 46 (v.0.19.1-r559) program using its default settings.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **0.15.3**
- Evidence: Diploid genome assembly using the high-coverage dataset High-coverage HiFi assemblies were generated using hifiasm (v.0.15.3) 12 , incorporating Hi-C data for haplotype phasing 65 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Efficient near-telomere-to-telomere assembly of nanopore simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10105-6 | PMCID: PMC13070018 | PMID: 41639459
- Evidence: Methods Overview of hifiasm (ONT) The existing hifiasm assembly toolkit consists of three approaches: the original hifiasm 6 , hifiasm (Hi-C) 8 and hifiasm (UL) 1 , each designed for specific purposes.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [hifiasm]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Version used: **0.14.1**
- Evidence: PacBio HiFi PacBio HiFi reads were assembled using hifiasm (v.0.14.1) 56 and the TRITEX pipeline 45 was used for pseudomolecule construction.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Version used: **0.13**
- Evidence: The Siphonodentalium genome was assembled de novo based on HiFi reads using hifiasm v0.13 ( 71 ) with the option -l 3 to exclude redundant haplotigs.
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **0.16.0**
- Evidence: For PacBio HiFi reads, hifiasm (0.16.0-r369) ( 54 ) with default parameter was used to assemble the primary contigs (hifi_pri).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Fitness consequences of structural variation inferred from a House Finch pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2409943121 | PMCID: PMC11588099 | PMID: 39531493
- Evidence: Two haplotypes per sample were assembled with hifiasm ( 59 ) ( Fig.
- Full pipeline: variant calling [BUSCO, hifiasm] -> stage not stated [BCFtools, PLINK, RepeatMasker]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: HiFi reads from both flowcells were assembled using hifiasm ( 74 ) v0.13 (r308), followed by purge_dups ( 75 ) v1.2.5.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Spatial variation in the mutation rate within the plant shoot apical meristem. (PNAS 2025)

- DOI: 10.1073/pnas.2514507122 | PMCID: PMC12646271 | PMID: 41213012
- Evidence: For the Red Polenta genome assembly, we used 35× per haplotype coverage PacBio HiFi sequencing to construct a primary assembly with hifiasm ( 55 ).
- Full pipeline: alignment/mapping [BUSCO] -> variant calling [hifiasm] -> stage not stated [RepeatMasker]

### &lt;i&gt;WUSCHEL-D1&lt;/i&gt; upregulation enhances grain number by inducing formation of multiovary-producing florets in wheat. (PNAS 2025)

- DOI: 10.1073/pnas.2510889122 | PMCID: PMC12557809 | PMID: 41086219
- Evidence: For the development of the MOV genome, we generated 212.64 Gbp of sequencing reads (~14× coverage) and assembled them using hifiasm to produce an assembly of 14.48 Gbp with a scaffold N50 of 15.7 Mbp.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [minimap2] -> stage not stated [BUSCO, Python, hifiasm]

### The genome of the vining fern &lt;i&gt;Lygodium microphyllum&lt;/i&gt; highlights genomic and functional differences between life phases of an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2504773122 | PMCID: PMC12501142 | PMID: 40996792
- Version used: **0.19.9**
- Evidence: A contig-level assembly was generated with error-corrected Nanopore reads >5 kb using HERRO v0.1.0 ( 87 ) and hifiasm v0.19.9 ( 88 ).
- Full pipeline: differential/statistical testing [DESeq2 v1.44.0] -> stage not stated [BUSCO, hifiasm v0.19.9]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: The genome was assembled de novo into contigs using FALCON, string graphs, and hifiasm with optimized parameters.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Genomic origins and evolution of neo-sex chromosomes in Pacific Island birds. (PNAS 2025)

- DOI: 10.1073/pnas.2503746122 | PMCID: PMC12337287 | PMID: 40720643
- Evidence: For each Myzomela species, we mapped trimmed (TrimGalore v.0.6.2; Q30) short-read data from a single male ( M. cardinalis: CA114, M. tristrami TA590) and a single female ( M. cardinalis: CA886, genome strain, M. tristrami: TA662, genome strain) to the raw hifiasm assemblies using bwa (v0.7.17; ref.
- Full pipeline: read trimming [Trim Galore v0.6.2, hifiasm] -> alignment/mapping [Trim Galore v0.6.2, hifiasm] -> stage not stated [BUSCO v5.2.2, R, RepeatMasker v4.1.2, SAMtools v1.11, minimap2 v2.26]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: These reads were combined with 1,073,209,059 PE Hi-C reads and assembled using the hifiasm assembly software in the joined hifi + Hi-C mode ( 56 ).
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

