# VarScan

- **Category:** genomics
- **Papers in survey:** 13
- **Journals:** PNAS (9), Nature (3), Cell (1)
- **Years:** 2021 (1), 2022 (3), 2023 (4), 2024 (4), 2025 (1)
- **Versions named:** 2.3.8 (2), 2.4.3 (1), 2.4.2 (1), 2.3.9 (1), 2.4.1 (1)
- **Pipeline stages it appears in:** variant calling (4), differential/statistical testing (2), alignment/mapping (2)

## Papers

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Version used: **2.4.1**
- Evidence: ...t/ Picard 1.81 N/A http://broadinstitute.github.io/picard/ Mutect v1.1.7 Cibulskis et al., 2013 https://software.broadinstitute.org/cancer/cga/mutect VarScan v2.4.1 Koboldt et al., 2012 http://varscan.sourceforge.net/ Annovar Wang et al., 2010 http://annovar.openbioinformatics.org/en/latest/ R package ‘Copynumber’ Nilsen et al., 2012 http://bioconductor.org/packages/release/bioc/html/copynumber.ht...
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Version used: **2.3.8**
- Evidence: Somatic mutation calling using bulk data Somatic mutations were called from WES using the Somaticwrapper pipeline v.1.6 ( https://github.com/ding-lab/somaticwrapper ), which includes four different callers, that is, Strelka (v.2.9.10) 56 , MUTECT (v.1.1.7) 57 , VarScan (v.2.3.8) 58 and Pindel (v.0.2.5) 59 .
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Version used: **2.3.8**
- Evidence: Mutation calling using WES Somatic mutations were called from WES data using the Somaticwrapper pipeline (v.2.2; https://github.com/ding-lab/somaticwrapper ), which includes four different callers: Strelka (v.2.9.10) 54 , MUTECT (v.1.1.7) 55 , VarScan (v.2.3.8) 56 and Pindel (v.0.2.5) 57 .
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Version used: **2.4.3**
- Evidence: After generating a text pileup output for the BAM files with the mpileup tool from Samtools version 1.7 90 , SNPs were called using VarScan version 2.4.3 91 (using parameters: -p-value 0.01, -min-reads2 1, -min-coverage 1, -min-freq-for-hom, 0.4 -min-var-freq 0.05, -output-vcf 1).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Experimental evolution reveals the synergistic genomic mechanisms of adaptation to ocean warming and acidification in a marine copepod. (PNAS 2022)

- DOI: 10.1073/pnas.2201521119 | PMCID: PMC9499500 | PMID: 36095205
- Evidence: Variants were called using VarScan 2 ( 75 ) with a minimum variant frequency of 0.01, P value of 0.1, minimum alternate reads 2, and minimum coverage of 30×, resulting in 10,368,816 sites.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [VarScan] -> stage not stated [MrBayes]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: Variant calling was performed using SAMtools ( 67 ), VarScan ( 68 ), and GATK ( 69 ).
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### Global genomic instability caused by reduced expression of DNA polymerase ε in yeast. (PNAS 2022)

- DOI: 10.1073/pnas.2119588119 | PMCID: PMC8944251 | PMID: 35290114
- Version used: **2.3.9**
- Evidence: VarScan 2.3.9 software was then used to detect de novo base substitutions and in/dels ( 66 ).
- Full pipeline: stage not stated [VarScan v2.3.9]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Version used: **2.4.2**
- Evidence: For sequencing of TET2, data were aligned using bowtie2 (v 2.4.1) to the human genome (hg38), and the variant allele frequency analyzed using VarScan (v 2.4.2) with base quality >15, minimum variant allele frequency > 0.01 and P -value for calling variants >0.01.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### Noncanonical HPV carcinogenesis drives radiosensitization of head and neck tumors. (PNAS 2023)

- DOI: 10.1073/pnas.2216532120 | PMCID: PMC10410762 | PMID: 37523561
- Evidence: ( 64 ) Variant calls were downloaded using the R TCGAbiolinks package; ( 65 ) calls performed with VarScan ( 66 ) were used for all analyses.
- Full pipeline: variant calling [VarScan] -> differential/statistical testing [GSEA, WGCNA] -> stage not stated [CNVkit, R]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Evidence: A pileup format was created using SAMtools ( 29 ), then variants were called using VarScan ( 30 ).
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: Binary alignment map (BAM) files were generated using SAMtools, and Variant Call Format (VCF) files were generated using VarScan ( 101 , 102 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: Variant calling was performed using VarScan ( 57 ) and annotated using SNPeff ( 58 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### Mitotic recombination events and single-base mutations induced by ultraviolet light in G1-arrested yeast cells. (PNAS 2025)

- DOI: 10.1073/pnas.2518046122 | PMCID: PMC12557804 | PMID: 41091767
- Evidence: VarScan ( 41 ) was subsequently used to identify mutations based on read depth across the genome.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [VarScan]

