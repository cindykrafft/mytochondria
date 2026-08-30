# OrthoFinder

- **Category:** phylogenetics
- **Papers in survey:** 73
- **Journals:** PNAS (51), Nature (19), Cell (3)
- **Years:** 2021 (3), 2022 (9), 2023 (16), 2024 (14), 2025 (22), 2026 (9)
- **Versions named:** 2.5.4 (12), 2.5.5 (8), 2.2.7 (4), 2.5.2 (3), 2.4.0 (2), 2.3.8 (2), 2.3.7 (1), 2.3.3 (1), 2.3.12 (1), 2.2.6 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (10), alignment/mapping (7), structure determination (3), visualisation (2), read trimming (1), differential/statistical testing (1), quantification (1), quality control (1)

## Papers

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **2.5.4**
- Evidence: 27 http://homer.ucsd.edu/homer/ OrthoFinder v2.5.4 Emms and Kelly 100 https://github.com/davidemms/OrthoFinder BLASTp v2.7.1+ Altschul et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Evidence: 116 https://alphafold.ebi.ac.uk/download Orthofinder v2.5.4 Emms and Kelly 117 https://github.com/davidemms/OrthoFinder MatLab (version: 2021b) The MathWorks Inc.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: 177 V16.40.1 NIS-Elements Nikon V6.10.01 Odyssey Western Blot Image Studio LI-COR V6.0 OrthoFinder Emms and Kelly 178 V3.0.1b1 Prism Graph Pad V10.4.2 Progenesis QI Non-Linear Dynamics V3.0 QIIME2 Bolyen et al.
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: On the basis of the alignments, proteins were clustered into orthogroups (OGs) with OrthoFinder 37 v2.7 [-I 2].
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **2.5.2**
- Evidence: 66 ) results of 2,701,787 peptide sequences of protein-coding genes, annotated from 44 potato accessions and the DM v.6.1 reference genome 11 , were input into OrthoFinder (v.2.5.2) (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Version used: **2.3.7**
- Evidence: Orthologue Inference Orthologues were inferred between species by finding reciprocal-best BLASTp 97 hits between the proteins in the genomes, or with OrthoFinder (v.2.3.7) 98 .
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: The inner tree is a clustering of ‘ Mirusviricota ’ and other genomes based on the occurrence of all gene clusters (OrthoFinder method, Bray-Curtis distance).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.2.7**
- Evidence: To reconstruct gene families, we used OrthoFinder (v.2.2.7) 82 using MMSeqs2 (ref.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Exaptation of ancestral cell-identity networks enables C&lt;sub&gt;4&lt;/sub&gt; photosynthesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08204-3 | PMCID: PMC11618092 | PMID: 39567684
- Evidence: Differentially accessible peaks between cell types were identified using the FindMarkers() command (adjusted P value < 0.05, per cent threshold > 0.3), before being associated with the nearest gene (±2,000 bp from transcription start site) Orthology analyses We determined gene orthologues between rice and sorghum using OrthoFinder 57 .
- Full pipeline: dimensionality reduction/clustering [Seurat, Signac, UMAP] -> differential/statistical testing [OrthoFinder] -> stage not stated [DESeq2, MACS2]

### A transcriptomic hourglass in brown algae. (Nature 2024)

- DOI: 10.1038/s41586-024-08059-8 | PMCID: PMC11540847 | PMID: 39443791
- Version used: **2.5.4**
- Evidence: To compare expression levels between species, we compared the expression levels (abundance) of orthogroups (sets of orthologues and paralogues) using OrthoFinder v2.5.4 95 , treating genes as isoforms and orthogroups as genes when importing the RNA-seq data using tximport v1.26.1 86 .
- Full pipeline: quantification [OrthoFinder v2.5.4] -> stage not stated [InterProScan v5.61, R]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Evidence: We used OrthoFinder 70 (v2.5.4) with default parameters to perform gene family analysis.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: The confirmed proteomes were subsequently analysed using OrthoFinder 81 to identify common single-copy orthologues.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **2.5.4**
- Evidence: We used OrthoFinder (v2.5.4) 90 to group repeats for deduplication.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **2.5.4**
- Evidence: For synteny analysis for each gene family, we used OrthoFinder (v.2.5.4) to identify orthologous clusters among pea and related legumes (for example, Vicia sativa , Medicago truncatula , Cicer arietinum , Lotus japonicus , Vigna radiata , Phaseolus vulgaris and Glycine max ), and visualized collinearity blocks with JCVI (v.1.2.7).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Version used: **2.5.5**
- Evidence: A gene-level pan-genome was constructed using all genes in the 40 haploid genomes, which were first clustered with OrthoFinder (v.2.5.5) 28 , diamond (v.2.0.13) 84 and Blast (v.2.12.0+) 85 .
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: The alignment results were then input into OrthoFinder 115 (v.2.5.4) to find orthogroups and orthologues.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Evidence: Gene expansion contraction analysis To analyse gene expansions and contractions, we processed the ultrametric species tree and gene family counts from OrthoFinder using CAFE5 (ref.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **2.5.4**
- Evidence: The gene families were inferred using the OrthoFinder (v.2.5.4) 92 program, which utilizes the Markov cluster algorithm.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Biosynthesis of cinchona alkaloids. (Nature 2026)

- DOI: 10.1038/s41586-026-10227-x | PMCID: PMC13149305 | PMID: 41851462
- Evidence: 14 . e , Comparison of cross-species transcriptomes using the OrthoFinder algorithm (with A. thaliana included in the analysis to exclude broadly conserved plant genes).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [OrthoFinder]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **2.5.5**
- Evidence: Comparative genomics Gene families were calculated with OrthoFinder (v.2.5.5) 81 and parsed with GENESPACE (v.1.3.1) 82 to create saturation curves.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Evidence: A side script provided by OrthoFinder ( primary_transcript.py ) and Cd-hit v.4.8.1 (ref.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Version used: **2.5.5**
- Evidence: Construction of the oat core, shell and cloud genomes Phylogenetic HOGs based on the primary protein sequences from 30 oat lines with consolidated gene predictions were calculated using OrthoFinder v.2.5.5 20 with standard parameters (see ‘Annotation of protein-coding genes’ for details; Leggett, Williams and AC Morgan were not part of this orthologous framework, because their gene content was not...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Adaptations in metabolism and protein translation give rise to the Crabtree effect in yeast. (PNAS 2021)

- DOI: 10.1073/pnas.2112836118 | PMCID: PMC8713813 | PMID: 34903663
- Evidence: Ortholog Prediction with OrthoFinder and GO Annotation.
- Full pipeline: stage not stated [OrthoFinder, R]

### Anaerobic gut fungi are an untapped reservoir of natural products. (PNAS 2021)

- DOI: 10.1073/pnas.2019855118 | PMCID: PMC8106346 | PMID: 33906945
- Evidence: PKS genes predicted by antiSMASH ( 19 ) and SMURF ( 25 ) for A. robustus , C. churrovis , N . californiae , and P. finnis were grouped into families by OrthoFinder ( 56 ) with default parameters.
- Full pipeline: alignment/mapping [AUGUSTUS, MAFFT] -> dimensionality reduction/clustering [BLAST] -> visualisation [Cytoscape] -> stage not stated [OrthoFinder, RAxML]

### An ancient, conserved gene regulatory network led to the rise of oral venom systems. (PNAS 2021)

- DOI: 10.1073/pnas.2021311118 | PMCID: PMC8040605 | PMID: 33782124
- Evidence: In addition to using the orthologs defined by NCBI, we carried out phylogenetic ortholog estimation using OrthoFinder (OF) ( 28 ).
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM, kallisto] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [edgeR] -> stage not stated [OrthoFinder, R, WGCNA]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: Orthologous protein families were annotated with OrthoFinder ( 83 ).
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Version used: **2.3.8**
- Evidence: The OrthoFinder v.2.3.8 ( 103 ) program was used to analyze the proteome of Gr, Ga, and the two subgenomes of Gh.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### Active antibiotic resistome in soils unraveled by single-cell isotope probing and targeted metagenomics. (PNAS 2022)

- DOI: 10.1073/pnas.2201473119 | PMCID: PMC9546533 | PMID: 36161886
- Version used: **2.2.6**
- Evidence: OrthoFinder v2.2.6 was used to infer rooted gene trees for all orthogroups ( 58 ), and the maximum likelihood tree was constructed using FastTree v2.1.10 ( 59 ), visualized with TreeDyn.
- Full pipeline: visualisation [OrthoFinder v2.2.6] -> stage not stated [QIIME 2]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **2.2.7**
- Evidence: OrthoFinder (v2.2.7) ( 101 ) was used to detect orthogroups of homologous genes from all genomes using default parameters.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Sulfur and methane oxidation by a single microorganism. (PNAS 2022)

- DOI: 10.1073/pnas.2114799119 | PMCID: PMC9371685 | PMID: 35914169
- Evidence: A homology-based search for functional genes was performed by using BLAST ( 124 ), OrthoFinder ( 125 ), and manual examination (details are in Materials and Methods ).
- Full pipeline: stage not stated [OrthoFinder, Prokka]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: Predicted protein sequences of A. subjunquillea , A. molliuscula , L. venenata , G. marginata , and G. sulciceps were clustered in orthogroups using OrthoFinder ( 56 ) with default settings.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Version used: **2.3.8**
- Evidence: We clustered proteins from 23 species into orthogroups using OrthoFinder (v2.3.8) ( 26 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Version used: **2.5.4**
- Evidence: Single-copy orthologous sequences from these five species were then extracted using OrthoFinder v.2.5.4 ( 72 ).
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### Cell type-specific cytonuclear coevolution in three allopolyploid plant species. (PNAS 2023)

- DOI: 10.1073/pnas.2310881120 | PMCID: PMC10556624 | PMID: 37748065
- Evidence: OrthoFinder and pSONIC were employed to partition expression of duplicate genes into their respective homoeologs.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, UMAP] -> structure determination [Monocle] -> visualisation [UMAP] -> stage not stated [OrthoFinder]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Version used: **2.4.0**
- Evidence: Homologous groups of sequences (“homogroups”) among those species were identified using OrthoFinder v2.4.0 ( 80 ) with an inflation parameter of 2.1.
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **2.5.4**
- Evidence: For species-tree reconstruction, single-copy orthologs were identified across Malassezia spp. and the outgroup U. maydis with OrthoFinder v2.5.4 ( 72 ) and aligned with MAFFT v7.310 ( 73 ).
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### Pumping iron: A multi-omics analysis of two extremophilic algae reveals iron economy management. (PNAS 2023)

- DOI: 10.1073/pnas.2305495120 | PMCID: PMC10372677 | PMID: 37459532
- Version used: **2.5.2**
- Evidence: Orthological and paralogical relationships between proteins and estimation of gene duplication events were determined by OrthoFinder (v2.5.2, available at https://github.com/davidemms/OrthoFinder ) using default parameters ( 52 ).
- Full pipeline: alignment/mapping [BLAST] -> visualisation [PyMOL v1.7.4] -> stage not stated [ColabFold, Cytoscape v3.4, OrthoFinder v2.5.2]

### Disruption of the standard kinetochore in holocentric <i>Cuscuta</i> species. (PNAS 2023)

- DOI: 10.1073/pnas.2300877120 | PMCID: PMC10214151 | PMID: 37192159
- Evidence: Predicted protein sequences from C. europaea and C. epithymum were compared with published proteomes of C. campestris , C. australis , and Ipomoea nil using program OrthoFinder [v2.5.2; ( 59 )] to identify orthologs and orthogroups.
- Full pipeline: alignment/mapping [SAMtools, STAR] -> structure determination [StringTie] -> stage not stated [BLAST, BUSCO, OrthoFinder, QUAST]

### Genomic and structural basis for evolution of tropane alkaloid biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2302448120 | PMCID: PMC10151470 | PMID: 37068250
- Evidence: Orthologous gene families were clustered from proteins of 11 plants from different families by OrthoFinder ( 37 ).
- Full pipeline: alignment/mapping [BUSCO, MAFFT] -> dimensionality reduction/clustering [OrthoFinder] -> visualisation [PyMOL v2.4] -> stage not stated [AlphaFold, AutoDock Vina v1.1.2, IQ-TREE]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **2.2.7**
- Evidence: We ran OrthoFinder (2.2.7) ( 96 ) to group the orthologous genes, diamond (0.9.21) for protein alignment.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Evidence: Phylogenetic datasets of single-copy orthologs were constructed using OrthoFinder ( 30 ) with the flags -M msa -S blast -T iqtree (unless stated otherwise).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Transcriptome age of individual cell types in <i>Caenorhabditis elegans</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216351120 | PMCID: PMC9992843 | PMID: 36812209
- Version used: **2.5.4**
- Evidence: We then applied OrthoFinder v2.5.4 with default parameters ( 48 ) to construct orthogroups.
- Full pipeline: stage not stated [OrthoFinder v2.5.4]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **2.5.2**
- Evidence: We used OrthoFinder (2.5.2) ( 83 ) to group homologous genes from chicken, zebra finch ( Taeniopygia guttata ) ( 7 ), human, spotted gar ( Lepisosteus oculatus ) ( 84 ), white-spotted bamboo shark ( Chiloscyllium plagiosum ) ( 85 ), and amphioxus ( Branchiostoma belcheri , Bb) ( 15 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Divergent sensory and immune gene evolution in sea turtles with contrasting demographic and life histories. (PNAS 2023)

- DOI: 10.1073/pnas.2201076120 | PMCID: PMC9962930 | PMID: 36749728
- Evidence: We used a dataset containing 8 species of turtle, 4 nonturtle reptiles, 3 mammals, and 1 amphibian using OrthoFinder ( 124 , 125 ).
- Full pipeline: alignment/mapping [BCFtools, SAMtools] -> variant calling [BCFtools, GATK, SAMtools] -> stage not stated [ANGSD, BUSCO, OrthoFinder, PLINK]

### Origins of genome-editing excisases as illuminated by the somatic genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213887120 | PMCID: PMC9942806 | PMID: 36669098
- Evidence: Two orthogroups classified by OrthoFinder are shown.
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [RepeatMasker v2.0.1] -> stage not stated [BUSCO, Flye v2.7, HMMER, OrthoFinder, eggNOG]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Evidence: ...ed, which spanned the Dipteran tree ( B. coprophila , P. hygida , Aedes aegypti , Anopheles gambiae , and Drosophila melanogaster ), as determined by OrthoFinder ( 54 ).
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### Investigating the &lt;i&gt;cis-&lt;/i&gt;regulatory basis of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; photosynthesis in grasses at single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2402781121 | PMCID: PMC11459142 | PMID: 39312655
- Evidence: In order to identify core C 4 enzymes across these species, we used OrthoFinder, named and numbered the enzyme models based off of their relatedness to Z. mays copies of known core C 4 genes ( 31 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.16.1, minimap2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt v4.5, OrthoFinder, scDblFinder]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: The OrthoFinder program (v2.2.6) was employed to categorize ortholog groups for each family ( 42 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: Then OGs within all P . × acerifolia chromosomes were identified using OrthoFinder ( 96 ), with Nelumbo nucifera (all chromosomes) serving as the outgroup.
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### UDP-glycosyltransferases act as key determinants of host plant range in generalist and specialist <i>Spodoptera</i> species. (PNAS 2024)

- DOI: 10.1073/pnas.2402045121 | PMCID: PMC11087754 | PMID: 38683998
- Evidence: To gain insight into the evolution of the UGT33 and UGT40 family genes during the speciation of the five Spodoptera species, OrthoFinder ( 22 ) and NOTUNG ( 23 ) were used to characterize gene gain/loss events of the UGT genes at each node of the phylogenetic tree.
- Full pipeline: stage not stated [OrthoFinder]

### The metabolic domestication syndrome of budding yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2313354121 | PMCID: PMC10945815 | PMID: 38457520
- Version used: **2.4.0**
- Evidence: Next, we used OrthoFinder (version 2.4.0) ( 70 ) to cluster homologous genes across all genomes.
- Full pipeline: alignment/mapping [MAFFT v7.471] -> dimensionality reduction/clustering [OrthoFinder v2.4.0] -> stage not stated [RAxML]

### Rubisco is evolving for improved catalytic efficiency and CO<sub>2</sub> assimilation in plants. (PNAS 2024)

- DOI: 10.1073/pnas.2321050121 | PMCID: PMC10945770 | PMID: 38442173
- Evidence: The complete set of translated proteomes for species in each respective taxonomic group were subject to orthogroup inference using OrthoFinder V2.5.2 ( 128 , 129 ) software run with default settings and with the DIAMOND ultra-sensitive mode ( 130 , 131 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE, OrthoFinder]

### Global diversity of enterococci and description of 18 previously unknown species. (PNAS 2024)

- DOI: 10.1073/pnas.2310852121 | PMCID: PMC10927581 | PMID: 38416678
- Version used: **2.3.3**
- Evidence: We identified orthologous clusters of genes across our complete set of 103 genomes using OrthoFinder v2.3.3 (with default parameters) ( 68 ), which is optimized for highly diverse datasets.
- Full pipeline: alignment/mapping [IQ-TREE v1.7, MAFFT, Pilon v1.23] -> dimensionality reduction/clustering [HMMER, OrthoFinder v2.3.3]

### Genomes, fossils, and the concurrent rise of modern birds and flowering plants in the Late Cretaceous. (PNAS 2024)

- DOI: 10.1073/pnas.2319696121 | PMCID: PMC10895254 | PMID: 38346181
- Version used: **2.3.12**
- Evidence: To identify orthologous CDS sequences across species, we applied the cDNA sequences of the chicken as a query against the cDNA sequences of the remaining 124 species using the program OrthoFinder (v2.3.12) with an E-value cutoff of 1e−10 ( 51 ).
- Full pipeline: stage not stated [BLAST, OrthoFinder v2.3.12, R, RAxML]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Version used: **2.5.4**
- Evidence: Orthologs were identified with OrthoFinder v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Language models reveal a complex sequence basis for adaptive convergent evolution of protein functions. (PNAS 2025)

- DOI: 10.1073/pnas.2418254122 | PMCID: PMC12501123 | PMID: 40986350
- Version used: **2.5.5**
- Evidence: OrthoFinder v2.5.5 ( 74 ) was used to derive orthogroups of genes.
- Full pipeline: alignment/mapping [MAFFT v7.505] -> differential/statistical testing [IQ-TREE v2.2.5] -> structure determination [IQ-TREE v2.2.5] -> stage not stated [BLAST, OrthoFinder v2.5.5, R]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Version used: **2.2.7**
- Evidence: OrthoFinder (v.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Heritable symbiont producing nonribosomal peptide confers extreme heat sensitivity and antifungal protection on its host. (PNAS 2025)

- DOI: 10.1073/pnas.2509873122 | PMCID: PMC12232616 | PMID: 40569380
- Version used: **2.5.5**
- Evidence: Orthologous proteins were assigned using OrthoFinder (v2.5.5) ( 54 ) and 269 shared single-copy orthologs were aligned using MAFFT (v7.520).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [MAFFT v7.520, OrthoFinder v2.5.5] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [R, survival (R)]

### Homoploid hybridization adds clarity to the origins of octoploid strawberries. (PNAS 2025)

- DOI: 10.1073/pnas.2502814122 | PMCID: PMC12207424 | PMID: 40531871
- Evidence: The orthologs were identified in ten diploid assemblies and four subgenomes in both F. chiloensis and F. virginiana using OrthoFinder ( 72 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [GATK, IQ-TREE, OrthoFinder, SAMtools]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Version used: **2.5.4**
- Evidence: For comparisons among paralogs, OrthoFinder v2.5.4 ( 60 , 61 ) was used to compare the somatically retained gene set to the germline-specific gene set ( SI Appendix , Table S1 ), in order to identify groups of paralogous genes that share a common ancestor with groups of one or more somatic genes.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### Convergent expansions of keystone gene families drive metabolic innovation in Saccharomycotina yeasts. (PNAS 2025)

- DOI: 10.1073/pnas.2500165122 | PMCID: PMC12167968 | PMID: 40460114
- Evidence: OrthoFinder ( 51 ) v3.0 was run under default parameters on the 1,154 genomes, resulting in 72,381 gene families ( 18 ) which were then filtered to 14,785 to include only gene families with at least 10 taxa represented.
- Full pipeline: alignment/mapping [IQ-TREE] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [InterProScan, OrthoFinder]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Version used: **2.5.5**
- Evidence: Chromosomal-level synteny was performed using GENESPACE v1.3.1 ( 81 ) with OrthoFinder v2.5.5 ( 82 ) and MCScanX v1.0.0 ( 83 ).
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: Single-copy orthogroups were identified using OrthoFinder ( 45 ), and protein sequences were extracted via in-house scripts.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Genomic signatures associated with the evolutionary loss of egg yolk in parasitoid wasps. (PNAS 2025)

- DOI: 10.1073/pnas.2422292122 | PMCID: PMC12036997 | PMID: 40232796
- Evidence: Orthology and species trees were reconstructed with OrthoFinder ( 120 ), STAG ( 121 ), and IQ-TREE ( 122 ), with divergence times estimated using r8s-v1.81 ( 123 ) and fossil-calibrated nodes ( 124 ).
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> quantification [RSEM] -> structure determination [IQ-TREE, OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, HMMER]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **2.5.5**
- Evidence: Gene families were identified using OrthoFinder v2.5.5 ( 81 ) for 89 representative MAGs at the species level with ≥80% completeness and ≤10% contamination.
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Subfunctionalization and epigenetic regulation of a biosynthetic gene cluster in &lt;i&gt;Solanaceae&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2420164122 | PMCID: PMC11874288 | PMID: 39977312
- Version used: **2.5.4**
- Evidence: OrthoFinder (v2.5.4) ( 43 ) was used to infer orthogroups containing P. grisea withanolide BGC genes.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> quantification [DESeq2] -> normalisation [DESeq2] -> visualisation [Python v3.9] -> stage not stated [IQ-TREE v2.1.4, OrthoFinder v2.5.4]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Evidence: Single-copy orthologs were identified using OrthoFinder ( 76 ), with M. rotundifolia as outgroup.
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **2.5.5**
- Evidence: A total of 1,106 single-copy orthogroups were identified using OrthoFinder version 2.5.5, and the protein sequences were extracted with seqkit v2.2.032, independently aligned by MAFFT v7.47133, and filtered through trimAl v1.434 with default parameters.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Metabolic enhancement contributed by horizontal gene transfer is essential for dietary specialization in leaf beetles. (PNAS 2025)

- DOI: 10.1073/pnas.2415717122 | PMCID: PMC11725898 | PMID: 39793087
- Version used: **2.5.4**
- Evidence: OrthoFinder v2.5.4 was employed to examine orthologs and homologs, using “-M msa -T fasttree” parameters ( 52 ).
- Full pipeline: alignment/mapping [Clustal Omega, SAMtools v1.17] -> stage not stated [IQ-TREE v2.2.2.6, OrthoFinder v2.5.4, RepeatMasker v2.0.4, eggNOG, fastp v0.23.4]

### Animals have expanded the evolutionary legacy of unicellular ancestors in blood cells. (PNAS 2026)

- DOI: 10.1073/pnas.2528110123 | PMCID: PMC13250551 | PMID: 42207871
- Evidence: Then, we identified homologs in the proteome data using OrthoFinder ( 79 ).
- Full pipeline: stage not stated [OrthoFinder]

### A multiplant transcriptomic atlas reveals conserved and lineage-specific defense architectures in response to &lt;i&gt;Botrytis cinerea&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2601719123 | PMCID: PMC13167747 | PMID: 42090259
- Evidence: We therefore identified all orthologues of these genes in all our host species using OrthoFinder.
- Full pipeline: stage not stated [OrthoFinder]

### Insights into cephalochordate genome and gene evolution from the early-diverging amphioxus &lt;i&gt;Asymmetron lucayanum&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2521280123 | PMCID: PMC13012124 | PMID: 41860958
- Evidence: We used OrthoFinder ( 79 ) to identify orthologous groups shared by the five cephalochordates as well as other representative bilaterians ( SI Appendix , Table S9 ).
- Full pipeline: variant calling [Canu] -> stage not stated [OrthoFinder]

### Evolution of sensory systems underlies the emergence of predatory feeding behaviors in nematodes. (PNAS 2026)

- DOI: 10.1073/pnas.2514172123 | PMCID: PMC12867699 | PMID: 41604260
- Evidence: Orthologous were determined using OrthoFinder ( 66 ).
- Full pipeline: stage not stated [OrthoFinder]

