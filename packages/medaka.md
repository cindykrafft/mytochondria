# Medaka

- **Category:** genomics
- **Papers in survey:** 13
- **Journals:** PNAS (7), Nature (6)
- **Years:** 2022 (3), 2023 (1), 2024 (4), 2025 (4), 2026 (1)
- **Versions named:** 1.7 (1), 1.5.0 (1), 1.11.3 (1), 1.9.1 (1)
- **Pipeline stages it appears in:** alignment/mapping (1)

## Papers

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: The contigs were polished calling variants with Medaka ( https://github.com/nanoporetech/medaka ).
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Embryonic genome instability upon DNA replication timing program emergence. (Nature 2024)

- DOI: 10.1038/s41586-024-07841-y | PMCID: PMC11410655 | PMID: 39198647
- Evidence: Notably, while the relatively unstructured pre-ZGA 3D genome was conserved in zebrafish and medaka 50 , 51 , somatic-cell-like RT was reported in pre-ZGA zebrafish embryos, despite the extremely short S phase 52 .
- Full pipeline: stage not stated [ImageJ, Medaka]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Evidence: Consensus sequences were generated using Medaka software (v1.4.3) with medaka_haploid_variant and medaka_consensus programs for polishing ( https://github.com/nanoporetech/medaka ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Evidence: Genome assemblies were then polished with both long reads using medaka consensus -m r941_prom_sup_g507 1.8.0 ( https://github.com/nanoporetech/medaka ) and Illumina short reads using HapoG 1.3.3 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Version used: **1.5.0**
- Evidence: Finally, chromosome-level genome assemblies were polished with Medaka (v.1.5.0) to correct possible sequence errors such as indels and mismatches, as follows: (1) first, we mapped the Nanopore reads to the chromosome-level assembly using the minimap2-based mini_align utility; (2) we then used Medaka consensus to obtain consensus sequences, specifying a batch size of 200 (--batch 200 flag) and the ...
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **1.7**
- Evidence: Contigs were polished in the following manner: first, raw contigs were corrected using the ultrafast consensus module Racon (v.1.4.17), followed by two sequential rounds of contig polishing with Medaka (v.1.7).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Marine viral particles reveal an expansive repertoire of phage-parasitizing mobile elements. (PNAS 2022)

- DOI: 10.1073/pnas.2212722119 | PMCID: PMC9618062 | PMID: 36256808
- Evidence: The consensus sequence of each pool of fragments was determined using three passes of racon ( 50 ) with a final pass of medaka ( https://github.com/nanoporetech/medaka ), following the assembly-free viral genome (AFVG) polishing methods as previously described ( 19 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [HMMER, IQ-TREE, Medaka, R v9.4, eggNOG, minimap2]

### A genetically linked pair of NLR immune receptors shows contrasting patterns of evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2116896119 | PMCID: PMC9271155 | PMID: 35771942
- Evidence: To further improve the accuracy of the assembly, Racon software ( https://github.com/lbcb-sci/racon ) was applied twice, and Medaka ( https://github.com/nanoporetech/medaka ) was used to correct misassembly.
- Full pipeline: stage not stated [BWA, IQ-TREE v2.0.3, ImageJ, Medaka]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Evidence: Whole genome assemblies were generated for the CU and PU strains with ONT long reads via Canu v2.1.1 (genome size 20 Mb) ( 67 ), followed by short-read polishing via medaka v0.8.1 (1X) ( https://github.com/nanoporetech/medaka ) and pilon v1.23 (3X) ( 68 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Resolving the 22q11.2 deletion using CTLR-Seq reveals chromosomal rearrangement mechanisms and individual variance in breakpoints. (PNAS 2024)

- DOI: 10.1073/pnas.2322834121 | PMCID: PMC11295037 | PMID: 39042694
- Version used: **1.9.1**
- Evidence: Assemblies were polished using Medaka version 1.9.1 ( https://github.com/nanoporetech/medaka ) and then with Polypolish ( 40 ) for samples where corresponding linked reads were also generated ( Fig.
- Full pipeline: alignment/mapping [BWA, minimap2 v2.18] -> variant calling [Flye] -> stage not stated [Medaka v1.9.1]

### In-patient evolution of a high-persister <i>Escherichia coli</i> strain with reduced in vivo antibiotic susceptibility. (PNAS 2024)

- DOI: 10.1073/pnas.2314514121 | PMCID: PMC10801923 | PMID: 38190524
- Evidence: Briefly, long-read assemblies were created with Flye-v2.9-b1768 ( 62 ) and polished with the long-reads using Racon-v1.4.21 ( 63 ) and Medaka-v1.4.4 (nanoporetech GitHub: https://github.com/nanoporetech/medaka ).
- Full pipeline: stage not stated [Flye, Medaka]

### Synergistic interactions between &lt;i&gt;Candida albicans&lt;/i&gt; and &lt;i&gt;Enterococcus faecalis&lt;/i&gt; promote toxin-dependent host cell damage. (PNAS 2025)

- DOI: 10.1073/pnas.2505310122 | PMCID: PMC12646220 | PMID: 41213026
- Version used: **1.11.3**
- Evidence: The basecalled reads were assembled and polished using Flye (v2.9.3), Medaka (v1.11.3), and Racon (v1.4.20).
- Full pipeline: stage not stated [Flye v2.9.3, Medaka v1.11.3]

### &lt;i&gt;Enterobacter hormaechei&lt;/i&gt; replaces virulence with carbapenem resistance via porin loss. (PNAS 2025)

- DOI: 10.1073/pnas.2414315122 | PMCID: PMC11874173 | PMID: 39977318
- Evidence: 1.4.3 ( https://github.com/nanoporetech/medaka ) using the r941_prom_high_g4011 model.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.10] -> stage not stated [BLAST v2.11.0, Medaka]

