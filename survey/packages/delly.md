# DELLY

- **Category:** genomics
- **Papers in survey:** 15
- **Journals:** Nature (10), PNAS (4), Science (1)
- **Years:** 2022 (2), 2023 (2), 2024 (4), 2025 (4), 2026 (3)
- **Versions named:** 0.8.7 (2), 0.7.6 (1), 1.1.6 (1), 0.8.6 (1), 0.8.3 (1), 0.9.1 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), variant calling (1)

## Papers

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Version used: **0.8.6**
- Evidence: 14 ) for SNVs and short indels (less than 50 nt in length; Supplementary Table 2 ) and Delly (v.0.8.6) (ref.
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### Widespread somatic L1 retrotransposition in normal colorectal epithelium. (Nature 2023)

- DOI: 10.1038/s41586-023-06046-z | PMCID: PMC10191854 | PMID: 37165195
- Evidence: We called structural variations using DELLY 64 with matched blood samples and phylogenetically distant clones to retain both early embryonic and somatic mutations.
- Full pipeline: read trimming [Bismark] -> alignment/mapping [BWA, Bismark, minimap2] -> stage not stated [Cutadapt, DELLY, Picard]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Evidence: We identified somatic rearrangements using a graph-based consensus approach comprising Delly 64 , Lumpy 65 and Manta 66 while also considering support from CNAs (Supplementary Fig.
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Evidence: On-target, single-copy integrations are validated using DELLY 77 call copy number variations, and bamintersect 17 to identify unexpectedly mapping read pairs.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### Origins of chromosome instability unveiled by coupled imaging and genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09632-5 | PMCID: PMC12695650 | PMID: 41162705
- Evidence: Structural variant calling was performed with Sniffles 78 and Delly 79 , and calls were curated manually to exclude false positives.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2] -> variant calling [DELLY, WhatsHap] -> quantification [ImageJ] -> machine learning [XGBoost] -> stage not stated [Bioconductor, Python]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: SV discovery using linear references We used Sniffles 71 v.2.0.7 and an LRS-optimized version of DELLY 72 (v.1.1.7) to discover SVs using linear reference genomes.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **1.1.6**
- Evidence: For PacBio HiFi callsets, we ran PBSV ( https://github.com/PacificBiosciences/pbsv ; v.2.9.0), Sniffles (v.2.0.7) 84 , Delly (v.1.1.6) 85 , cuteSV (v.2.0.3) 86 , DeBreak (v.1.0.2) 87 , SVIM (v.2.0.0) 88 , DeepVariant (v.1.5.0) 75 and Clair3 (v.1.0.4) 89 .
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **0.8.7**
- Evidence: Different categories of structural variants (SVs: duplication, inversion, translocation and large-scale deletion or insertion) were detected on the basis of read mapping (read depth and read pair relationships) on PCR-duplicate-marked bam files using Delly (v 0.8.7) with default parameters; a summary of SVs identified is given in Supplementary Table 11 .
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **0.8.7**
- Evidence: Large chromosomal changes, resulting from iPS cell chromosomal instability, were identified using DELLY (v.0.8.7) 118 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Whole-genome landscapes of 1,364 breast cancers. (Nature 2026)

- DOI: 10.1038/s41586-025-09812-3 | PMCID: PMC12851938 | PMID: 41339552
- Version used: **0.7.6**
- Evidence: Tumour purity, ploidy, and segmented CNV profiles were estimated with Sequenza (v.3.0.0) 62 and somatic structural variations were identified using Delly (v.0.7.6) 63 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9] -> stage not stated [DELLY v0.7.6, GATK v4.0, GSEA, Mutect2, R, VEP]

### Expansion of a retrovirus lineage in the koala genome. (PNAS 2022)

- DOI: 10.1073/pnas.2201844119 | PMCID: PMC9231498 | PMID: 35696585
- Evidence: Deletions were called in the resequenced individuals with DELLY ( 17 ) and LUMPY ( 18 ).
- Full pipeline: alignment/mapping [BWA, Picard v2.23.4, RepeatMasker, SAMtools v1.12] -> stage not stated [DELLY, R]

### Sympatric speciation of the spiny mouse from Evolution Canyon in Israel substantiated genomically and methylomically. (PNAS 2022)

- DOI: 10.1073/pnas.2121822119 | PMCID: PMC9060526 | PMID: 35320043
- Evidence: SV was called by Delly, Lumpy, and Manta.
- Full pipeline: stage not stated [Bismark, DELLY, GATK, Metascape, R, VCFtools]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Version used: **0.9.1**
- Evidence: The sorted BAM file served as input for Delly (v0.9.1) ( 71 ), Smoove (v0.2.8) ( 72 ), and manta (v1.6.0) ( 73 ) to detect SVs in shorter reads.
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Version used: **0.8.3**
- Evidence: We used Delly (version 0.8.3) ( 73 ) to identify the breakpoint positions at the tandem duplications.
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Systematic in vitro evolution in &lt;i&gt;Plasmodium falciparum&lt;/i&gt; reveals key determinants of drug resistance. (Science 2024)

- DOI: 10.1126/science.adk9893 | PMCID: PMC11809290 | PMID: 39607932
- Evidence: ...icance of difference in copy ratio vectors, discordant read-pair support for tandem duplications, and overlap with an independent CNV calling method, DELLY ( 18 ).
- Full pipeline: alignment/mapping [AlphaFold, GATK v3.5] -> visualisation [Cytoscape v3.9.1] -> stage not stated [DELLY, Picard, SAMtools, SnpEff]

