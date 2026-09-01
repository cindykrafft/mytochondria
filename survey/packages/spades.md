# SPAdes

- **Category:** genomics
- **Papers in survey:** 74
- **Journals:** PNAS (50), Nature (21), Cell (2), Science (1)
- **Years:** 2021 (10), 2022 (17), 2023 (12), 2024 (18), 2025 (8), 2026 (9)
- **Versions named:** 3.13.0 (6), 3.15.2 (6), 3.15.5 (5), 3.11.1 (4), 3.13.1 (4), 3.15.3 (3), 4.1.0 (2), 3.14.1 (2), 3.10.1 (2), 3.12 (1)
- **Pipeline stages it appears in:** read trimming (18), alignment/mapping (7), normalisation (3), quality control (2), structure determination (2), differential/statistical testing (1), dimensionality reduction/clustering (1), variant calling (1), machine learning (1)

## Papers

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **3.10.0**
- Evidence: ...etagenomics/genome_sets/gut_phage_database/ Classifier scripts This paper https://github.com/cai91/GPD/tree/master/classifier Software and Algorithms SPAdes v.3.10.0 Bankevich et al., 2012 https://github.com/ablab/spades MEGAHIT v1.1.3 Li et al., 2015 https://github.com/voutcn/megahit VirSorter v1.0.5 Roux et al., 2015 https://github.com/simroux/VirSorter VirFinder v1.1 Ren et al., 2017 https://gi...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: SEP identification in hCom2 119 hCom2 reference genomes, sequenced as part of the original hCom2 publication, 59 were either downloaded from RefSeq as assemblies or assembled with SPAdes 75 (–isolate) from their raw DNA sequencing reads, depending on availability.
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Version used: **3.13.0**
- Evidence: Mapped reads were subsequently reassembled using SPAdes v.3.13.0 with mismatch corrector and coverage threshold enabled (--careful --cov-cutoff 60), resulting in the assembly of a single contig (292,647 bp) that was circularized by trimming the identical overlapping ends (127 bp) giving rise to the closed genome (292,520 bp).
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Version used: **3.13.3**
- Evidence: In brief, reads were assembled using Trinity v.2.8.4 ( k -mer = 25), SPAdes v.3.13.3 45 ( k -mer = 55), SPAdes ( k -mer = 75) and Trans-Abyss v.2.0.1 46 ( k -mer = 32).
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Decoupling of respiration rates and abundance in marine prokaryoplankton. (Nature 2022)

- DOI: 10.1038/s41586-022-05505-3 | PMCID: PMC9771814 | PMID: 36477536
- Version used: **3.0.0**
- Evidence: The remaining reads were digitally normalized using kmernorm v.1.05 ( http://sourceforge.net/projects/kmernorm ) using the settings -k 21 -t 30 -c 3 and then assembled with SPAdes (v.3.0.0) 61 using the following settings: --careful --sc --phred-offset 33.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [Bowtie2] -> normalisation [SPAdes v3.0.0] -> stage not stated [Prokka]

### Prolonged viral suppression with anti-HIV-1 antibody therapy. (Nature 2022)

- DOI: 10.1038/s41586-022-04597-1 | PMCID: PMC9177424 | PMID: 35418681
- Version used: **3.13.0**
- Evidence: A k-mer-based assembler, SPAdes v3.13.0 52 is used to assemble the HIV-1 sequences.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [MAFFT v7.487] -> stage not stated [SPAdes v3.13.0]

### Phage anti-CBASS and anti-Pycsar nucleases subvert bacterial immunity. (Nature 2022)

- DOI: 10.1038/s41586-022-04716-y | PMCID: PMC9117128 | PMID: 35395152
- Evidence: The trimmed reads from each phage genome were assembled into scaffolds using SPAdes genome assembler version 3.14.0 (ref.
- Full pipeline: read trimming [Cutadapt v2.8, SPAdes] -> visualisation [PyMOL v2.3.0] -> stage not stated [BLAST, IQ-TREE, PHENIX]

### Emergence of methicillin resistance predates the clinical use of antibiotics. (Nature 2022)

- DOI: 10.1038/s41586-021-04265-w | PMCID: PMC8810379 | PMID: 34987223
- Version used: **3.15**
- Evidence: Sequence analyses Draft genomes were de novo assembled using SPAdes (v.3.15) 46 .
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> simulation/modelling [R] -> stage not stated [SPAdes v3.15]

### Synergy and oxygen adaptation for development of next-generation probiotics. (Nature 2023)

- DOI: 10.1038/s41586-023-06378-w | PMCID: PMC10412450 | PMID: 37532933
- Version used: **3.13.0**
- Evidence: The dependency programs include SPAdes v3.13.0, racon v1.4.1, bowtie2 v2.3.5.1, and pilon v1.23.
- Full pipeline: alignment/mapping [Kraken2] -> quantification [Bracken] -> differential/statistical testing [R, vegan] -> stage not stated [Bowtie2 v2.3.5.1, Prokka v1.14.5, SPAdes v3.13.0]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Evidence: For each dataset, recruited Asgard reads were independently assembled using SPAdes 71 and IDBA-UD 72 and further binned using CONCOCT, using a minimum contig length of 1,000 bp.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Version used: **3.15.2**
- Evidence: The trimmed reads were co-assembled using SPAdes (v.3.15.2) 64 with the k -mer length varying from 21 to 111 and the ‘--meta’ option.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Evidence: Samples from the Yamaoka laboratory were sequenced at Novogene Co., Ltd., Beijing, China with the Illumina NOVA PE150 platform and assembled using the SPAdes genome assembler v.3.15.3 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### A virally encoded tRNA neutralizes the PARIS antiviral defence system. (Nature 2024)

- DOI: 10.1038/s41586-024-07874-3 | PMCID: PMC11464382 | PMID: 39111359
- Evidence: Genome assemblies were performed with SPAdes implemented in Unicycler 59 .
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HMMER v3.3.2, MUSCLE v5.1] -> structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.7, SPAdes]

### An enterococcal phage-derived enzyme suppresses graft-versus-host disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07667-8 | PMCID: PMC11291292 | PMID: 38987594
- Version used: **3.13.0**
- Evidence: Third, correction of sequencing errors on the basis of the Hamming graph and Bayesian subclustering were performed using BayesHammer software (as bundled with SPAdes v.3.13.0) (spades.py –only-error-correction) 67 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> dimensionality reduction/clustering [SPAdes v3.13.0] -> differential/statistical testing [SPAdes v3.13.0] -> stage not stated [BLAST, Cutadapt, QIIME 2 v2018.11, R, SAMtools, ggplot2 v3.3.6]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: Subsequently, mapped long and short reads were assembled together using SPAdes 45 v.3.15.3 (‘--isolate -k 21,33,55,77,99,111’, mapped long reads were supplied using ‘-s’ and scaffolds of the previous iteration were supplied using ‘--trusted-contigs’) and the assembled scaffolds were filtered to retain only scaffolds of at least 1 kb.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Version used: **3.12**
- Evidence: Trimmed reads of parent strains were used to generate draft genomes by performing de novo assembly using SPAdes (v.3.12) 42 with MismatchCorrector activated (--careful parameter) and annotation with Prokka (v.1.14.0) 43 using the NCBI A. baumannii assembly (ASM975968v1; GCA_009759685.1 ) as the reference.
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: This toolkit implements Bowtie 2 63 to initially find reads mapped to a plant chloroplast database and SPAdes 64 for de novo assembly and iterative extension.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Deep origin of eukaryotes outside Heimdallarchaeia within Asgardarchaeota. (Nature 2025)

- DOI: 10.1038/s41586-025-08955-7 | PMCID: PMC12222021 | PMID: 40335687
- Evidence: The resulting clean reads were single-sample de novo assembled using SPAdes 50 (v.3.15.3) with the parameters: ‘-k 21,33,55,77,99 -meta’.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT] -> stage not stated [Bowtie2, HMMER, IQ-TREE, SAMtools, SPAdes]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **4.1.0**
- Evidence: Virulence genes, antibiotic resistance and mobile genetic elements V. cholerae genome assembly was carried out using SPAdes v.4.1.0.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Natural maternal immunity protects neonates from Escherichia coli sepsis. (Nature 2026)

- DOI: 10.1038/s41586-026-10225-z | PMCID: PMC13108393 | PMID: 41813901
- Evidence: Hybrid de novo assembly was performed using Unicycler (v.0.5.1), which utilizes SPAdes for initial short-read assembly followed by long-read scaffolding and polishing with Racon (v.1.5.0) 87 – 89 .
- Full pipeline: quality control [FastQC v0.12.1, NanoPlot v1.46.0] -> alignment/mapping [MAFFT v7.526, QUAST v5.2.0.2] -> stage not stated [Python, SPAdes]

### Capturing dynamic phage-pathogen coevolution by clinical surveillance. (Nature 2026)

- DOI: 10.1038/s41586-026-10136-z | PMCID: PMC12987554 | PMID: 41813903
- Evidence: Genomes were assembled using SPAdes 36 , and for escape phages selected on PLE11(+) V. cholerae , genomes were analysed using BreSeq (v.0.33) 37 .
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [BLAST, ColabFold, IQ-TREE v2.2.0, SPAdes, fastp v0.23.2]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **4.1.0**
- Evidence: First, we generated a de novo genome assembly using the SPAdes (v.4.1.0) assembler.
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **3.13.0**
- Evidence: The complete mitochondrial genome of the squirrel was de novo assembled from quality-filtered reads using SPAdes v.3.13.0 (ref.
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **3.10.1**
- Evidence: These normalized overlap read libraries were assembled into contigs using SPAdes v3.10.1, a multi k-mer assembler ( 62 ), with options -m 400–careful -k 21, 33, 55, 77, 99, 111, 127.
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Version used: **3.13.1**
- Evidence: Individual read libraries were assembled using SPAdes v3.13.1 ( 54 , 55 ); parameters used are in SI Appendix , SI Methods .
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Evidence: Each SAG was de novo assembled using SPAdes (St.
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Adaptive differentiation and rapid evolution of a soil bacterium along a climate gradient. (PNAS 2021)

- DOI: 10.1073/pnas.2101254118 | PMCID: PMC8106337 | PMID: 33906949
- Evidence: Briefly, we quality filtered the metagenomic reads with BBDuk and assembled all raw reads using the SPAdes genome assembler ( 69 ) with a “careful” iterative k-step ranging from k = 31 to 91.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> stage not stated [BLAST, SPAdes]

### The cyanobacterium <i>Prochlorococcus</i> has divergent light-harvesting antennae and may have evolved in a low-oxygen ocean. (PNAS 2021)

- DOI: 10.1073/pnas.2025638118 | PMCID: PMC7980375 | PMID: 33707213
- Version used: **3.5**
- Evidence: Artifactual sequences were filtered off the raw data and draft SAGs were assembled using SPAdes 3.5.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, IQ-TREE, SPAdes v3.5]

### A conserved long noncoding RNA, GAPLINC, modulates the immune response during endotoxic shock. (PNAS 2021)

- DOI: 10.1073/pnas.2016648118 | PMCID: PMC7896317 | PMID: 33568531
- Evidence: De novo transcript assembly was performed using SPAdes.
- Full pipeline: alignment/mapping [minimap2] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> stage not stated [SPAdes]

### Microbial dynamics of elevated carbon flux in the open ocean's abyss. (PNAS 2021)

- DOI: 10.1073/pnas.2018269118 | PMCID: PMC7848738 | PMID: 33479184
- Evidence: The dereplicated MAGs were further refined by reassembling the mapped quality trimmed reads with SPAdes ( 73 ) using the –careful and –trusted-contigs setting.
- Full pipeline: read trimming [SPAdes] -> alignment/mapping [SPAdes] -> structure determination [SPAdes, ggplot2, pheatmap] -> visualisation [Cytoscape, ggplot2, pheatmap] -> stage not stated [BWA v0.7.15, R, WGCNA]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Version used: **3.11.1**
- Evidence: Merged and unmerged reads from FLASh were used as input for genome assembly with SPAdes v3.11.1 ( 63 ) with default settings.
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### Multiclonal human origin and global expansion of an endemic bacterial pathogen of livestock. (PNAS 2022)

- DOI: 10.1073/pnas.2211217119 | PMCID: PMC9897428 | PMID: 36469788
- Version used: **3.11.1**
- Evidence: Short read sequences were adapter trimmed using Trimmomatic v0.36 ( 35 ) and de novo assembled using SPAdes v3.11.1 ( 36 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36] -> alignment/mapping [phytools] -> differential/statistical testing [BEAST, R] -> simulation/modelling [phytools] -> structure determination [phytools] -> stage not stated [InterProScan v5.52, Prokka v1.13]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: The reads were trimmed and quality controlled using Trimmomatic ( 75 ) and then assembled using SPAdes ( 76 ) and annotated via Prokka ( 77 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Recurrent emergence of <i>Klebsiella pneumoniae</i> carbapenem resistance mediated by an inhibitory <i>ompK36</i> mRNA secondary structure. (PNAS 2022)

- DOI: 10.1073/pnas.2203593119 | PMCID: PMC9499542 | PMID: 36095213
- Version used: **3.9.0**
- Evidence: Assemblies were generated for all isolates with available raw sequence data using SPAdes v3.9.0 ( 35 ) and annotated with Prokka v1.14.5 ( 36 ).
- Full pipeline: alignment/mapping [BCFtools v0.1.19, BLAST v2.6.0, MUSCLE v3.8, SAMtools] -> stage not stated [Prokka v1.14.5, SPAdes v3.9.0]

### Isolation of a virus causing a chronic infection in the archaeal model organism &lt;i&gt;Haloferax volcanii&lt;/i&gt; reveals antiviral activities of a provirus. (PNAS 2022)

- DOI: 10.1073/pnas.2205037119 | PMCID: PMC9436352 | PMID: 35994644
- Version used: **3.13.1**
- Evidence: Subsequent assembly of high-quality reads was performed with assembler SPAdes v3.13.1 from ref.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BLAST] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [SPAdes v3.13.1]

### A gut microbial peptide and molecular mimicry in the pathogenesis of type 1 diabetes. (PNAS 2022)

- DOI: 10.1073/pnas.2120028119 | PMCID: PMC9351354 | PMID: 35878027
- Evidence: Data Availability Because the DIABIMMUNE study metagenomics sequencing reads were not ideal for a peptide search, we first assembled the reads using SPAdes ( 11 ), and they are available at https://github.com/ablab/spades .
- Full pipeline: stage not stated [SPAdes]

### Plant genetic effects on microbial hubs impact host fitness in repeated field trials. (PNAS 2022)

- DOI: 10.1073/pnas.2201285119 | PMCID: PMC9335298 | PMID: 35867817
- Evidence: Reads were assembled using SPAdes (using the settings --isolate -k 21,33,55,77) and annotated with the software Prokka designed for rapid prokaryotic genome annotation ( 67 , 68 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [Python] -> normalisation [Python] -> stage not stated [Prokka, R, SPAdes, igraph, lme4]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Evidence: Processed reads from transcriptomes of the two samples per species were assembled into transcript contigs in SPAdes ( 73 ) ver.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### Gene-rich X chromosomes implicate intragenomic conflict in the evolution of bizarre genetic systems. (PNAS 2022)

- DOI: 10.1073/pnas.2122580119 | PMCID: PMC9191650 | PMID: 35653559
- Version used: **3.13.1**
- Evidence: The genome of springtail A. fusca was assembled using SPAdes v3.13.1 ( 44 ).
- Full pipeline: stage not stated [BUSCO, SPAdes v3.13.1]

### Recombination resolves the cost of horizontal gene transfer in experimental populations of <i>Helicobacter pylori</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2119010119 | PMCID: PMC8944584 | PMID: 35298339
- Evidence: The binned reads from the alignment of the donors to the reference genome were assembled into scaffolds via the de novo assembly software package SPAdes ( 70 ).
- Full pipeline: alignment/mapping [SAMtools, SPAdes] -> dimensionality reduction/clustering [R] -> stage not stated [Prokka]

### Diverse methylotrophic methanogenic archaea cause high methane emissions from seagrass meadows. (PNAS 2022)

- DOI: 10.1073/pnas.2106628119 | PMCID: PMC8892325 | PMID: 35165204
- Evidence: Additionally, full-length 16S rRNA gene sequences taxonomically assigned to Bathyarchaeia were assembled from metagenomic 16S rRNA gene sequences using SPAdes assembler version 3.11.1 ( 65 ) as implemented in phyloFlash.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [MAFFT] -> stage not stated [HMMER, IQ-TREE, QGIS, SPAdes]

### <i>Bacteroides thetaiotaomicron</i> uses a widespread extracellular DNase to promote bile-dependent biofilm formation. (PNAS 2022)

- DOI: 10.1073/pnas.2111228119 | PMCID: PMC8851478 | PMID: 35145026
- Version used: **3.13.0**
- Evidence: Illumina whole-genome sequencing was performed by the Plateforme de Microbiologie Mutualisée (P2M) of Institut Pasteur and the genomes were assembled using SPAdes v3.13.0 ( 50 ) and when necessary were reassembled using Unicycler ( 51 ).
- Full pipeline: stage not stated [BLAST, SPAdes v3.13.0]

### Longitudinal clonal dynamics of HIV-1 latent reservoirs measured by combination quadruplex polymerase chain reaction and sequencing. (PNAS 2022)

- DOI: 10.1073/pnas.2117630119 | PMCID: PMC8794825 | PMID: 35042816
- Version used: **3.13.1**
- Evidence: After the overlapping reads are merged by BBMerge, we use a k-mer–based assembler, SPAdes v3.13.1, to reconstruct the HIV-1 sequences.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [RAxML v8.2.11] -> structure determination [SPAdes v3.13.1]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **3.15.2**
- Evidence: PF and TC genomes were de novo assembled with SPAdes v3.15.2 ( 51 ) in --isolate mode and with the --cov-cutoff flag set to auto.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Dual thermal ecotypes coexist within a nearly genetically identical population of the unicellular marine cyanobacterium &lt;i&gt;Synechococcus&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2315701120 | PMCID: PMC10665897 | PMID: 37972069
- Version used: **3.15.2**
- Evidence: Synechococcus reads were normalized to 60× coverage using bbnorm (bbmap, v.38.90) and assembled with SPAdes v.3.15.2 ( 64 ).
- Full pipeline: read trimming [minimap2 v2.17] -> alignment/mapping [BEDTools v2.30, Bowtie2 v2.4.3, SAMtools v1.11, minimap2 v2.17] -> normalisation [SPAdes v3.15.2] -> stage not stated [R]

### Diversity of rhodopsin cyclases in zoospore-forming fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2310600120 | PMCID: PMC10622942 | PMID: 37871207
- Version used: **3.15.5**
- Evidence: Genome assemblies of low-covering genomic data were either received from the NCBI database or raw sequencing data stored by JGI or in the Sequence Read Archive (NCBI) and were trimmed using BBduk and assembled by SPAdes (3.15.5) ( 24 ).
- Full pipeline: read trimming [IQ-TREE, SPAdes v3.15.5] -> alignment/mapping [IQ-TREE] -> simulation/modelling [GROMACS v2019.3] -> visualisation [Matplotlib v3.4.3, PyMOL v2.4.1] -> stage not stated [AlphaFold, MDAnalysis v2.4.3]

### Loss of Pde1 function acts as an evolutionary gateway to penicillin resistance in <i>Streptococcus pneumoniae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2308029120 | PMCID: PMC10576035 | PMID: 37796984
- Version used: **3.15.5**
- Evidence: For the determination of sequence types of clinical isolates, the Illumina short reads were assembled into draft assemblies using SPAdes (version 3.15.5, 2) and the ST was determined using the command line MLST (unpublished software https://github.com/tseemann/mlst ) which scans contigs for the seven MLST genes found in the pubMLST scheme ( 33 ).
- Full pipeline: alignment/mapping [Clustal Omega, HMMER v3.2.1] -> stage not stated [Python, SPAdes v3.15.5]

### The genomic landscape of swine influenza A viruses in Southeast Asia. (PNAS 2023)

- DOI: 10.1073/pnas.2301926120 | PMCID: PMC10438389 | PMID: 37552753
- Version used: **3.15.3**
- Evidence: For each sample, reads were de novo assembled using SPAdes v3.15.3 ( 51 ), and individual gene segment was determined by BLASTn v2.2.18 ( 52 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.39] -> read trimming [FastQC, Trimmomatic v0.39] -> structure determination [BEAST v10.4, RAxML v1.1.0] -> stage not stated [BLAST v2.2.18, SPAdes v3.15.3]

### Epidemiological connectivity between humans and animals across an urban landscape. (PNAS 2023)

- DOI: 10.1073/pnas.2218860120 | PMCID: PMC10629570 | PMID: 37450494
- Version used: **3.6**
- Evidence: De novo assembly was performed using SPAdes v3.6 ( 66 ) (parameters: --careful, -t 1, --phred-offset 33).
- Full pipeline: differential/statistical testing [R v3.3] -> stage not stated [SPAdes v3.6]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Version used: **3.11.1**
- Evidence: Reads were then assembled de novo using SPAdes v3.11.1 ( 34 ).
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Euglenozoan kleptoplasty illuminates the early evolution of photoendosymbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2220100120 | PMCID: PMC10041101 | PMID: 36927158
- Version used: **3.10.1**
- Evidence: The plastid genomes were pre-assembled with SPAdes v3.10.1 ( 42 ), and the plastid genes were identified in the assembled contigs using the BLASTX algorithm ( 43 ) and extracted.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [IQ-TREE, MAFFT] -> differential/statistical testing [IQ-TREE] -> stage not stated [BUSCO, SPAdes v3.10.1]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Version used: **3.12.0**
- Evidence: Genomes were sequenced using Illumina and PacBio technologies and assembled with Falcon 0.7.3 and 1.8.8 (PacBio) and SPAdes 3.12.0 and 3.13.0 or Velvet 1.2.07 (Illumina).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Photosynthetic demands on translational machinery drive retention of redundant tRNA metabolism in plant organelles. (PNAS 2024)

- DOI: 10.1073/pnas.2421485121 | PMCID: PMC11670086 | PMID: 39693336
- Version used: **3.15.4**
- Evidence: SPAdes v.3.15.4 ( 108 ) was then used to assemble trimmed reads de novo. tRNA Analysis.
- Full pipeline: read trimming [MAFFT v7.525, RAxML v8.2.12, SPAdes v3.15.4] -> alignment/mapping [MAFFT v7.525, RAxML v8.2.12] -> visualisation [Python]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Version used: **3.14.1**
- Evidence: After mass control, all reads of soil samples were assembled through k ~ mers of 21, 33, 55, 77, 99, and 127 under SPAdes v3.14.1 and “-meta” mode ( 77 ).
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Adaptive evolution of carbapenem-resistant hypervirulent &lt;i&gt;Klebsiella pneumoniae&lt;/i&gt; in the urinary tract of a single patient. (PNAS 2024)

- DOI: 10.1073/pnas.2400446121 | PMCID: PMC11363291 | PMID: 39150777
- Evidence: In addition, genomic characteristics were analyzed using various software and databases: SPAdes-v3.13.0 (genome hybrid assembly), Unicycler-v0.4.7 (genome hybrid assembly), Prokka (annotation), ARDB (drug resistance gene profiles), VFDB (virulence gene profiles), PlasmidFinder (plasmid replicon typing), Kleborate 0.4.0 (O antigen, K antigen, and multilocus sequence typing), Parsnp (Phylogenetic an...
- Full pipeline: stage not stated [Prokka, SPAdes]

### Lining the small intestine with mycobacteriophages protects from &lt;i&gt;Mycobacterium avium&lt;/i&gt; subsp. &lt;i&gt;paratuberculosis&lt;/i&gt; and eliminates fecal shedding. (PNAS 2024)

- DOI: 10.1073/pnas.2318627121 | PMCID: PMC11331133 | PMID: 39102547
- Version used: **3.15.5**
- Evidence: Filtered reads were de novo assembled using SPAdes v3.15.5 with default parameters on careful mode ( 46 ).
- Full pipeline: quality control [FastQC v0.12.1, Trimmomatic] -> read trimming [FastQC v0.12.1, SPAdes v3.15.5, Trimmomatic]

### Targeted whole-genome recovery of single viral species in a complex environmental sample. (PNAS 2024)

- DOI: 10.1073/pnas.2404727121 | PMCID: PMC11295033 | PMID: 39052829
- Evidence: The remaining reads are assembled into contigs with an open-sourced de novo genome assembler, SPAdes ( 32 ).
- Full pipeline: stage not stated [SPAdes]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **3.15.5**
- Evidence: The assembly of the contig was compared against assemblies generated using SPAdes v3.15.5 ( 24 ) and Trinity v2.8.6 ( 25 ).
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Version used: **3.15.3**
- Evidence: We assembled UCE reference contigs in SPAdes v3.15.3 ( 80 ) from sample LSUMNS B7901.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### The evolutionary genomics of adaptation to stress in wild rhizobium bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2311127121 | PMCID: PMC10990125 | PMID: 38507447
- Version used: **3.14.1**
- Evidence: Genomic reads from Illumina sequencing were de novo assembled with SPAdes (v.
- Full pipeline: quality control [Prokka v1.13.3] -> read trimming [MUSCLE] -> alignment/mapping [MAFFT v7.475, MUSCLE] -> differential/statistical testing [lme4 v1.1] -> visualisation [R] -> stage not stated [RAxML, SPAdes v3.14.1]

### Genome copy number predicts extreme evolutionary rate variation in plant mitochondrial DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2317240121 | PMCID: PMC10927533 | PMID: 38427600
- Evidence: Raw reads for each of the 60 species were first assembled using SPAdes-3.15.2 with settings -k 21,33,55,77,99 -t 64 to generate putative contigs from nuclear and mitochondrial genomes ( 76 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.5, SAMtools] -> differential/statistical testing [R v4.2.2] -> visualisation [ggplot2] -> stage not stated [RAxML, SPAdes]

### Isolation, characterization, and circulation sphere of a filovirus in fruit bats. (PNAS 2024)

- DOI: 10.1073/pnas.2313789121 | PMCID: PMC10873641 | PMID: 38335257
- Evidence: The reads were quality checked using fastp version 0.20.0, and the resultants were de novo assembled using SPAdes genome assembler version 3.14.1 in meta mode.
- Full pipeline: quality control [SPAdes, fastp v0.20.0] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> quantification [ImageJ] -> visualisation [ImageJ, PyMOL v2.4.0] -> stage not stated [BLAST v0.9.35]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Version used: **3.15.2**
- Evidence: Raw sequencing reads were trimmed and quality filtered using fastP version 0.20.1 ( 67 ) and then assembled using the paired-end assembly in SPAdes version 3.15.2 ( 68 ) with kmer values alternating every other digit between 21 and 127, inclusive.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### Anthropocene genetic diversity loss in the marine tropics. (PNAS 2025)

- DOI: 10.1073/pnas.2513012122 | PMCID: PMC12646237 | PMID: 41231948
- Version used: **3.15.3**
- Evidence: For E . laterofenestra , reads were mapped to a de novo whole genome assembly created with shotgun sequencing and assembled by SPAdes v.3.15.3 ( 67 ) following the pire_ssl_data_processing GitHub repository ( 68 ).
- Full pipeline: quality control [VCFtools v0.1.14] -> alignment/mapping [SAMtools v1.9, SPAdes v3.15.3] -> dimensionality reduction/clustering [ADMIXTURE v1.3, PLINK v1.9] -> stage not stated [freebayes v1.3.1]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Evidence: Following the recommendations for de novo assembly using SPAdes ( 43 ), we downsampled the filtered Illumina data from GNS104 by specifying a target depth of 75× with bbnorm (Bushnell; sourceforge.net/projects/bbmap/).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Inverse stable isotope probing-metabolomics (InverSIP) identifies an iron acquisition system in a methane-oxidizing bacterial community. (PNAS 2025)

- DOI: 10.1073/pnas.2507323122 | PMCID: PMC12435222 | PMID: 40901884
- Version used: **4.0.0**
- Evidence: Raw metagenomic reads were trimmed using Trimmomatic ( 51 ) and were assembled using the --meta mode of SPAdes v4.0.0 ( 52 ).
- Full pipeline: read trimming [SPAdes v4.0.0, Trimmomatic] -> alignment/mapping [Python]

### Evolutionarily divergent nidovirus with an exceptionally large genome identified in Pacific oysters undergoing mass mortality. (PNAS 2025)

- DOI: 10.1073/pnas.2426923122 | PMCID: PMC12377751 | PMID: 40758866
- Version used: **3.15.2**
- Evidence: Raw reads for RNA-Seq samples were quality-controlled and trimmed using Trimmomatic v.0.38 ( 94 ), followed by de novo assembly using SPAdes v.3.15.2 ( 95 ) and MEGAHIT v.1.2.9 ( 96 ), respectively ( SI Appendix , Extended Materials and Methods ).
- Full pipeline: read trimming [MAFFT, SPAdes v3.15.2, Trimmomatic v0.38] -> alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2.1] -> structure determination [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0.3, InterProScan v5.59]

### Allelic variations and gene cluster modularity act as nonlinear bottlenecks for cholera emergence. (PNAS 2025)

- DOI: 10.1073/pnas.2417915122 | PMCID: PMC12146696 | PMID: 40434643
- Version used: **3.11.1**
- Evidence: Reads were trimmed using Trimmomatic v0.36 ( 77 ) and assembled de novo with SPAdes version 3.11.1 ( 78 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36]

### Ancient origin and high diversity of zymocin-like killer toxins in the budding yeast subphylum. (PNAS 2025)

- DOI: 10.1073/pnas.2419860122 | PMCID: PMC11848437 | PMID: 39928860
- Version used: **3.14**
- Evidence: The SRA datasets were downloaded using SRA Explorer ( https://sra-explorer.info/ ), trimmed using Skewer v0.2.2 ( 49 ), and assembled using SPAdes v3.14 ( 31 ).
- Full pipeline: read trimming [SPAdes v3.14] -> alignment/mapping [STAR] -> stage not stated [Cytoscape]

### Pneumococcal membrane particles promote serotype-independent cellular and humoral immunity and protect against pneumococcal colonization. (PNAS 2026)

- DOI: 10.1073/pnas.2537226123 | PMCID: PMC13214003 | PMID: 42154558
- Version used: **3.15.5**
- Evidence: Strains were sequenced using Illumina paired-end reads and de novo assembled using SPAdes v3.15.5 ( 41 ).
- Full pipeline: alignment/mapping [BCFtools, BWA v0.7.19, SAMtools v1.22] -> stage not stated [SPAdes v3.15.5]

### Smooth-to-rough morphotype switching, a mechanism of phage resistance in &lt;i&gt;&lt;i&gt;Mycobacterium&lt;/i&gt; abscessus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2531197123 | PMCID: PMC12993973 | PMID: 41811441
- Evidence: Reads were cleaned and trimmed, SPAdes ( 54 ) and Unicycler ( 55 ) were used for the de novo assembly.
- Full pipeline: read trimming [SPAdes] -> stage not stated [AlphaFold, BLAST]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Evidence: Filtered reads were assembled de novo into contigs using SPAdes genome assembler v3.13.1 ( https://github.com/ablab/spades ) with default parameters.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

### Deep evolutionary conservation of a sex-determining locus without sequence homology. (PNAS 2026)

- DOI: 10.1073/pnas.2522417123 | PMCID: PMC12799146 | PMID: 41490485
- Version used: **3.15.2**
- Evidence: To control for haplotype bias, we assembled the seven L. humile sex haplotypes de novo from published male Illumina reads ( 15 ) using SPAdes v3.15.2 (“ --isolate -k 21,33,55,77,99 ”) ( 62 ).
- Full pipeline: alignment/mapping [BWA v0.7.18, freebayes v1.0.2] -> variant calling [BWA v0.7.18, IQ-TREE v2.3.6, SPAdes v3.15.2, freebayes v1.0.2] -> dimensionality reduction/clustering [BWA v0.7.18, freebayes v1.0.2] -> structure determination [IQ-TREE v2.3.6] -> stage not stated [BCFtools v1.21, PLINK v1.9, R v4.4, VCFtools v0.1.16]

### Diverse phage communities are maintained stably on a clonal bacterial host. (Science 2024)

- DOI: 10.1126/science.adk1183 | PMCID: PMC7617280 | PMID: 39666794
- Version used: **3.15.0**
- Evidence: Full genome-sized contigs were then assembled using SPAdes version 3.15.0 ( 49 ) with default parameters, but using only the first 400,000 lines of the fasta files, since excessive coverage leads to problems with assembly ( 50 ).
- Full pipeline: differential/statistical testing [tidyverse v2.0.0] -> visualisation [R] -> stage not stated [BLAST, SPAdes v3.15.0]

