# QUAST

- **Category:** genomics
- **Papers in survey:** 25
- **Journals:** PNAS (15), Nature (10)
- **Years:** 2022 (2), 2023 (7), 2024 (2), 2025 (11), 2026 (3)
- **Versions named:** 5.0.2 (4), 5.2.0 (3), 5.2.0.2 (1), 5.0 (1), 5.0.0 (1), 4.5.4 (1), 5.0.1 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), differential/statistical testing (2), read trimming (2), quality control (1), variant calling (1), dimensionality reduction/clustering (1)

## Papers

### Switchable chiral transport in charge-ordered kagome metal CsV<sub>3</sub>Sb<sub>5</sub>. (Nature 2022)

- DOI: 10.1038/s41586-022-05127-9 | PMCID: PMC9668744 | PMID: 36224393
- Evidence: M.G.V., C.F. and T.N. acknowledge support from FOR 5249 (QUAST) lead by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation).
- Full pipeline: stage not stated [QUAST, Quantum ESPRESSO]

### A pangenome reference of 36 Chinese populations. (Nature 2023)

- DOI: 10.1038/s41586-023-06173-7 | PMCID: PMC10322713 | PMID: 37316654
- Version used: **5.2.0**
- Evidence: We used QUAST v5.2.0 (ref.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> variant calling [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BCFtools, QUAST v5.2.0, pheatmap v1.0.12]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: Assembly contiguity assessment Assembly contiguity was assessed for each haplotype using QUAST 79 .
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **5.0.2**
- Evidence: For assembly validation and quality control, we used QUAST (v5.0.2) 51 to calculate the assembly metrics, Merqury (v1.3) 52 to estimate the base-call accuracy and k -mer completeness based on 21-mer produced from the short-read WGS data 14 and BUSCO (v5.3.1) 17 with the embryophyta_odb10 database to determine the completeness of each genome assembly.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Version used: **5.0.2**
- Evidence: Subsequently, reads were de novo-assembled using Spades v3.15.3 42 , and the quality of assembly was assessed using QUAST v5.0.2 43 .
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **5.0**
- Evidence: The resulting assembly was evaluated using QUAST (v.5.0) 60 , with a total assembly length of 310,325,892 bp divided in 618 contigs, GC% of 36.82 and N50 of 12,028,351 bp.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: To round off our evaluation, the number of mismatches between the Nipponbare genome assembled in this study and the reference genomes IRGSP-1.0 and T2T-NIP was assessed using QUAST 73 (v.5.0.1).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **5.2.0**
- Evidence: 90 ) and assembly quality was assessed using QUAST v.5.2.0 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Telomere-to-telomere assembly using HERRO-corrected Nanopore Simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10563-y | PMCID: PMC13323052 | PMID: 42045451
- Evidence: These contigs were evaluated against the X and Y chromosomes from HG002 assembly v1.0.1 using QUAST 31 ( Methods , ‘Analysis methods’), achieving genome fractions of 100% and 99.98% for X and Y, respectively, with a total of 7 misassemblies (Extended Data Table 2 ).
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BEDTools, BUSCO, Canu, Flye, QUAST]

### Natural maternal immunity protects neonates from Escherichia coli sepsis. (Nature 2026)

- DOI: 10.1038/s41586-026-10225-z | PMCID: PMC13108393 | PMID: 41813901
- Version used: **5.2.0.2**
- Evidence: Assembly quality was assessed using QUAST (v.5.2.0.2) against the E. coli Nissle 1917 reference genome (GCF_000714595.1) 90 .
- Full pipeline: quality control [FastQC v0.12.1, NanoPlot v1.46.0] -> alignment/mapping [MAFFT v7.526, QUAST v5.2.0.2] -> stage not stated [Python, SPAdes]

### Mechanism of superconductivity in the Hubbard model at intermediate interaction strength. (PNAS 2022)

- DOI: 10.1073/pnas.2205048119 | PMCID: PMC9388079 | PMID: 35947620
- Evidence: A.T. acknowledges financial support from the Austrian Science Fund (FWF) through the Project I 5868 (part of the FOR 5249 [QUAST] of the German Research Foundation, DFG).
- Full pipeline: stage not stated [QUAST]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **5.0.2**
- Evidence: Assembly quality was assessed with QUAST v5.0.2 ( 52 ).
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Monopole-like orbital-momentum locking and the induced orbital transport in topological chiral semimetals. (PNAS 2023)

- DOI: 10.1073/pnas.2305541120 | PMCID: PMC10691347 | PMID: 37983495
- Evidence: M.G.V. and C.F. thank the DFG (German Research Foundation) for 5249 (QUAST).
- Full pipeline: stage not stated [QUAST]

### The emergence and diversification of a zoonotic pathogen from within the microbiota of intensively farmed pigs. (PNAS 2023)

- DOI: 10.1073/pnas.2307773120 | PMCID: PMC10666105 | PMID: 37963246
- Version used: **5.0.1**
- Evidence: All assemblies were evaluated using QUAST v.5.0.1 ( 53 ) and we mapped reads back to de novo assemblies to investigate polymorphism (indicative of mixed cultures) using Bowtie2 v1.2.2 ( 54 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v1.2.2, QUAST v5.0.1] -> stage not stated [Canu v1.9, Prokka v1.14.5, R]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Version used: **5.0.2**
- Evidence: The quality and completeness of the pangenome were assessed using QUAST v5.0.2 ( 78 ) and BUSCO v5.2.2 ( 79 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### Disruption of the standard kinetochore in holocentric <i>Cuscuta</i> species. (PNAS 2023)

- DOI: 10.1073/pnas.2300877120 | PMCID: PMC10214151 | PMID: 37192159
- Evidence: Completeness and contiguity of assemblies were evaluated using BUSCO [v5.2.2; ( 51 )] and QUAST [v5.0.2; ( 52 )].
- Full pipeline: alignment/mapping [SAMtools, STAR] -> structure determination [StringTie] -> stage not stated [BLAST, BUSCO, OrthoFinder, QUAST]

### Hund's flat band in a frustrated spinel oxide. (PNAS 2025)

- DOI: 10.1073/pnas.2518213122 | PMCID: PMC12626020 | PMID: 41196354
- Evidence: M.V., M.C., and G.S., acknowledge support from the DFG (German Science Foundation) through FOR 5249 QUAST (Project-ID 449872909), EXC2147 ct.qmat (Project-ID 390858490), and SFB 1170 ToCoTronics (Project-ID 258499086), respectively.
- Full pipeline: stage not stated [QUAST, Quantum ESPRESSO]

### Homology-mediated transformation of frog-killing fungus &lt;i&gt;Batrachochytrium dendrobatidis&lt;/i&gt; illuminates chytrid development and pathogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507572122 | PMCID: PMC12595416 | PMID: 41150711
- Version used: **5.0.0**
- Evidence: Assembly quality was assessed using QUAST v5.0.0 ( 37 ) with default parameters, reporting total assembly size (range: 26 to 34 Mb), number of contigs (75 to 403), N50 (1.2 to 1.8 Mb), L50 ( 5 – 8 ), and largest contig (3.6 to 6.1 Mb).
- Full pipeline: alignment/mapping [SAMtools v1.14, minimap2 v2.28] -> stage not stated [BLAST, BUSCO v5.2.2, QUAST v5.0.0, R v4.0.2]

### Symbiotic solutions for colony nutrition: Conserved nitrogen recycling within the bacterial pouch of &lt;i&gt;Tetraponera&lt;/i&gt; ants. (PNAS 2025)

- DOI: 10.1073/pnas.2514882122 | PMCID: PMC12595465 | PMID: 41150726
- Evidence: Assembly statistics were calculated with QUAST-5.0.2 ( 73 ) ( SI Appendix , Table S8 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic] -> read trimming [FastQC v0.11.9, Trimmomatic] -> differential/statistical testing [QUAST] -> stage not stated [BLAST, Flye v2.9, RAxML v8.2.12]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Evidence: To assess the quality and contiguity of the assembled B. franklini genome, we used QUAST and the BlobToolKit package v 2.6.1 ( 44 ) with the Benchmark of Single-Copy Orthologs [BUSCOs; ( 75 )] for Hymenoptera.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Nano-biochar regulates phage-host interactions, reducing antibiotic resistance genes in vermicomposting systems. (PNAS 2025)

- DOI: 10.1073/pnas.2511986122 | PMCID: PMC12403132 | PMID: 40838886
- Evidence: Raw reads were trimmed and quality filtered using Fastp ( 45 ) to generate high quality clean reads from which contigs were assembled using MEGAHIT ( 46 ), with subsequent quality assessment performed using QUAST ( 58 ).
- Full pipeline: read trimming [QUAST] -> dimensionality reduction/clustering [BLAST] -> stage not stated [IQ-TREE, R, eggNOG]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **5.2.0**
- Evidence: Assembly statistics were extracted with QUAST v5.2.0 ( 98 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Version used: **4.5.4**
- Evidence: For the de novo genome assembly, we first used Trimmomatic ( 67 ) to remove adapters and low-quality sequences and then assembled the data using ALLPATHS-LG r.52485 ( 68 ) with the option “HAPLOIDIFY = True.” The quality of the assembly was evaluated with QUAST v4.5.4 ( 69 ) and BUSCO v3.0.2 ( 70 ) using the “mammalia_odb9” dataset.
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### Direct control of electron spin at an intrinsically chiral surface for highly efficient oxygen reduction reaction. (PNAS 2025)

- DOI: 10.1073/pnas.2413609122 | PMCID: PMC11892581 | PMID: 39999173
- Evidence: 742068), the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) through SFB 1143 (project ID 24731007), QUAST (project ID FOR 5249), the Würzburg-Dresden Cluster of Excellence on Complexity and Topology in Quantum Matter—ct.qmat (EXC 2147, project ID 390858490), and EXQIRAL (No.
- Full pipeline: dimensionality reduction/clustering [QUAST]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Evidence: We obtained the assembly metrics using QUAST software v.5.2.0 ( 61 ), and used BUSCO software v.5.4.3 to assess assembly completeness ( 62 ).
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

