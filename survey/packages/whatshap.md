# WhatsHap

- **Category:** genomics
- **Papers in survey:** 15
- **Journals:** Nature (10), PNAS (4), Cell (1)
- **Years:** 2022 (3), 2023 (3), 2024 (2), 2025 (6), 2026 (1)
- **Versions named:** 1.1 (2), 1.4 (1), 1.0 (1), 1.5 (1), 1.6 (1), 0.18 (1)
- **Pipeline stages it appears in:** variant calling (5), alignment/mapping (3), differential/statistical testing (1)

## Papers

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Version used: **0.18**
- Evidence: (2012) https://genome.sph.umich.edu/wiki/VerifyBamID WhatsHap v0.18 Martin et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: Alignments were then phased using the PEPPER-Margin-DeepVariant pipeline, after which WhatsHap was used to tag reads in the filtered alignments using phasing information 53 , 54 .
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: To obtain chromosome-scale haplotypes, integrative phasing with WhatsHap 68 was performed, combining local dense phase information derived from long reads with global sparse phase information inferred from Strand-seq alignments.
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Genotyping, sequencing and analysis of 140,000 adults from Mexico City. (Nature 2023)

- DOI: 10.1038/s41586-023-06595-3 | PMCID: PMC10600010 | PMID: 37821707
- Evidence: For the WGS phasing, we used WhatsHap ( https://github.com/whatshap/whatshap ) to extract phase information in the sequence reads and from the subset of available trios and pedigrees, and this information was fed into Shapeit (v.4.2.2; https://odelaneau.github.io/shapeit4 ) through the --use-PS 0.0001 option.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [REGENIE] -> stage not stated [BCFtools, DeepVariant v0.10.0, GATK, WhatsHap]

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Version used: **1.0**
- Evidence: We used WhatsHap (v.1.0) (ref.
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **1.1**
- Evidence: For small variants, the two-pass mode of DeepVariant (v.1.1.0) 107 with WhatsHap (v.1.1) 108 was used to call SNPs and indels from the PacBio HiFi read alignments.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Origins of chromosome instability unveiled by coupled imaging and genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09632-5 | PMCID: PMC12695650 | PMID: 41162705
- Evidence: Haplotype phasing of the ONT reads was performed with WhatsHap to generate read depth plots by haplotype 80 .
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2] -> variant calling [DELLY, WhatsHap] -> quantification [ImageJ] -> machine learning [XGBoost] -> stage not stated [Bioconductor, Python]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Evidence: Read-based phasing was done with WhatsHap 43 at first, followed by population-level phasing with SHAPEIT4 for better accuracy 44 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: Using the NYGC raw genotypes, the phasing was done by WhatsHap 76 (v.2.0) in three different ways: phasing with only the ONT reads (from hereon referred to as long-read phasing), trio phasing and trio phasing with the ONT reads (from hereon referred to as long-read–trio phasing).
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **1.1**
- Evidence: Both switch and Hamming errors were calculated using two variant call format (VCF) files produced by the pipeline calc_switchErr ( https://github.com/tangerzhang/calc_switchErr ), based on the ‘compare’ function of WhatsHap (v.1.1) 70 .
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **1.4**
- Evidence: Haplotype phasing performance was evaluated by comparing SNV haplotypes from Dipcall datasets of PIGA and hifiasm assemblies using WhatsHap (v.1.4) 73 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Evidence: Variants were called with Illumina short reads (more accurate, higher coverage), whereas phasing and haplotagging were performed with PacBio long reads, as recommended in the WhatsHap documentation.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### Frequent horizontal chromosome transfer between asexual fungal insect pathogens. (PNAS 2024)

- DOI: 10.1073/pnas.2316284121 | PMCID: PMC10945790 | PMID: 38442176
- Version used: **1.6**
- Evidence: Phasing of SNPs and small InDels for M. guizhouense was determined using PacBio Hifi reads generated in this study and WhatsHap (version 1.6) ( 65 ). gRSCU was estimated using BioKIT (version 0.1.3).
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.4.4] -> variant calling [BCFtools, Bowtie2 v2.4.4] -> differential/statistical testing [R v3.6.0] -> stage not stated [WhatsHap v1.6]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Version used: **1.5**
- Evidence: Thus, phasing was performed through a combination of read-based phasing using WhatsHap v1.5 ( 84 ) and joint statistical phasing using SHAPEIT4 v1.3 ( 85 ).
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### Repeated polyploidization shapes divergence in floral morphology in &lt;i&gt;Lithophragma bolanderi&lt;/i&gt; (Saxifragaceae). (PNAS 2025)

- DOI: 10.1073/pnas.2505119122 | PMCID: PMC12377753 | PMID: 40802687
- Evidence: Fifth, we estimated parsimony scores for all possible MUL trees using GRAMPA version 1.4 ( 60 ) based on 46 gene trees phased with WhatsHap ( 83 ), to examine whether trees with multimapping of polyploids to both L. bolanderi and L. glabrum , as expected under allopolyploidy, was the most parsimonious explanation.
- Full pipeline: read trimming [GATK v4.1.4.1, fastp] -> alignment/mapping [GATK v4.1.4.1, fastp] -> variant calling [GATK v4.1.4.1, IQ-TREE, VCFtools, fastp] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4] -> stage not stated [BUSCO, WhatsHap]

