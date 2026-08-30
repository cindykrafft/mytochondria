# DeepVariant

- **Category:** genomics
- **Papers in survey:** 18
- **Journals:** Nature (16), PNAS (2)
- **Years:** 2022 (3), 2023 (2), 2024 (1), 2025 (7), 2026 (5)
- **Versions named:** 1.4.0 (2), 1.3.0 (2), 1.6.0 (2), 1.6 (1), 0.4 (1), 0.10.0 (1), 1.0.0 (1), 1.6.1 (1)
- **Pipeline stages it appears in:** variant calling (9), alignment/mapping (7), machine learning (2), quality control (1)

## Papers

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: Alignments were then phased using the PEPPER-Margin-DeepVariant pipeline, after which WhatsHap was used to tag reads in the filtered alignments using phasing information 53 , 54 .
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: The HiFi reads were then mapped to scaffolds using minimap2 and heterozygous SNPs called using DeepVariant 66 .
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Version used: **1.0.0**
- Evidence: DeepVariant (v.1.0.0) with the pretrained PacBio mode (--model_type PACBIO) was then used for variant calling of each accession, and all individual variants were merged using glnexus_cli from DeepVariant (v.0.9.0).
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Genotyping, sequencing and analysis of 140,000 adults from Mexico City. (Nature 2023)

- DOI: 10.1038/s41586-023-06595-3 | PMCID: PMC10600010 | PMID: 37821707
- Version used: **0.10.0**
- Evidence: Single-sample variants were called using DeepVariant (v.0.10.0) with default WGS parameters or custom exome parameters 35 , generating a gVCF for each input OQFE CRAM file.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [REGENIE] -> stage not stated [BCFtools, DeepVariant v0.10.0, GATK, WhatsHap]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **1.3.0**
- Evidence: We used DeepVariant (v.1.3.0) with the parameter --model_type=“PACBIO” to call variants on these alignments.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **0.4**
- Evidence: 87 ), and these alignments were passed to the PEPPER-Margin-DeepVariant 0.4 pipeline 88 to polish the initial consensus.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Evidence: Variants were called jointly with DeepVariant 42 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### A haplotype-based evolutionary history of barley domestication. (Nature 2025)

- DOI: 10.1038/s41586-025-09533-7 | PMCID: PMC12629985 | PMID: 40993384
- Version used: **1.6.0**
- Evidence: Variant calling was performed with DeepVariant (v1.6.0) 52 to generate GVCF files for each sample, followed by joint genotyping using GLnexus (v1.3.1) 53 , 54 to obtain a SNP matrix across the 13 samples.
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [BCFtools v1.15.1, DeepVariant v1.6.0, SnpEff v4.3t, minimap2 v2.24] -> visualisation [R v3.5.1] -> stage not stated [ADMIXTURE, PLINK, SAMtools v1.16.1]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **1.6**
- Evidence: Assembly quality was assessed by computing quality value estimates with Merqury and DeepVariant (v.1.6) 75 as previously described 8 .
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **1.6.0**
- Evidence: DeepVariant (v1.6.0) 80 with the pretrained PacBio mode (--model_type PACBIO) was then used for variant calling of each accession, and all individual variants were merged using glnexus_cli (v1.4.1) 81 with the DeepVariant config file.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Detection of meiotic recombination breakpoints using inheritance vectors DeepVariant calls (see the ‘Read-based variant calling’ section) from HiFi sequencing data from G1, G2 and G3 pedigree members allow us to identify the haplotype of origin for heterozygous loci in G3 and infer the occurrence of a recombination along the chromosome when the haplotype of origin changes between loci.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Version used: **1.4.0**
- Evidence: Variant calling was performed using DeepVariant (v.1.4.0) 74 .
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Evidence: To perform a polishing round, we mapped all CCS reads to the scaffolded, gap-closed assemblies using pbmm2 ( https://github.com/PacificBiosciences/pbmm2 ) with arguments: --preset CCS -N 1 and called variants using DeepVariant ( https://github.com/google/deepvariant/ ).
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **1.4.0**
- Evidence: Benchmark small variant callsets were constructed by combining variant calls obtained independently using GATK, DeepVariant (v.1.4.0) 71 and Dipcall from high-coverage short-read, long-read and hifiasm assemblies.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### The DNA virome varies with human genes and environments. (Nature 2026)

- DOI: 10.1038/s41586-026-10288-y | PMCID: PMC13215884 | PMID: 41882355
- Evidence: For AoU and SPARK, we analysed genotypes previously called from WGS using DRAGEN (AoU 24 ) and DeepVariant (SPARK 25 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [DeepVariant] -> differential/statistical testing [LDSC] -> stage not stated [R]

### Human and bacterial genetic variation shape oral microbiomes and health. (Nature 2026)

- DOI: 10.1038/s41586-025-10037-7 | PMCID: PMC12979206 | PMID: 41606319
- Version used: **1.3.0**
- Evidence: Genotyping and quality control of human genetic variants in SPARK Variant calling in SPARK was previously performed using DeepVariant (v.1.3.0) to produce sample-level VCFs from reads aligned to GRCh38 followed by GLnexus (v.1.4.1) to call variants jointly across the cohort.
- Full pipeline: quality control [DeepVariant v1.3.0, PLINK v2.00a] -> alignment/mapping [DeepVariant v1.3.0] -> variant calling [DeepVariant v1.3.0] -> differential/statistical testing [LDSC, R] -> visualisation [ChimeraX v1.9] -> stage not stated [AlphaFold, Bowtie2, MetaPhlAn v4.0.6, SAMtools v1.15.1]

### Genome degradation in plant tissue culture. (PNAS 2026)

- DOI: 10.1073/pnas.2530182123 | PMCID: PMC13123843 | PMID: 42018421
- Version used: **1.6.1**
- Evidence: SBS and InDels were called against the primary and concatenated genome assemblies using DeepVariant v1.6.1 ( 79 ) with the model type “WGS” to generate variant call format (VCF) and genomic variant call format (GVCF) files.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39, minimap2 v2.17] -> alignment/mapping [MUSCLE, R, SAMtools v1.13, minimap2 v2.17] -> variant calling [DeepVariant v1.6.1, minimap2 v2.17] -> stage not stated [SnpEff v5.1d]

### Methylation-associated mutagenesis underlies variation in the mutation spectrum across eukaryotes. (PNAS 2026)

- DOI: 10.1073/pnas.2516368123 | PMCID: PMC12994199 | PMID: 41824497
- Evidence: For Ornithorhynchus anatinus (Platypus), we aligned 49 individual genomes (in FASTQ format) and called variants using DeepVariant ( 143 ) with its standard protocol.
- Full pipeline: alignment/mapping [DeepVariant] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [RepeatMasker]

