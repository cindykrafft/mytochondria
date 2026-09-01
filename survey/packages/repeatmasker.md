# RepeatMasker

- **Category:** genomics
- **Papers in survey:** 134
- **Journals:** PNAS (75), Nature (51), Cell (6), Science (2)
- **Years:** 2021 (20), 2022 (24), 2023 (25), 2024 (21), 2025 (37), 2026 (7)
- **Versions named:** 4.1.2 (8), 2.0.1 (8), 4.0.7 (7), 4.1.5 (3), 4.1.1 (3), 4.1.0 (2), 4.1.6 (2), 1.0.11 (2), 4.0.6 (2), 4.0.5 (2)
- **Pipeline stages it appears in:** alignment/mapping (12), quantification (3), structure determination (2), dimensionality reduction/clustering (2), machine learning (2), differential/statistical testing (1), quality control (1)

## Papers

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: From single-cell transcriptomes, quantification of all TEs in the classes LINE, SINE, LTR, DNA, and Retroposon based on RepeatMasker were extracted.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: .../www.drive5.com/muscle/ Geneious Prime 2021.0.3 Biomatters https://www.geneious.com/download/ bwa-mem Li and Durbin, 2009 http://maq.sourceforge.net/ RepeatMasker Institute for Systems Biology http://www.repeatmasker.org/ RSEM (v1.2.22) Li and Dewey, 2011 http://deweylab.github.io/RSEM/ STAR aligner software (2.5.1b) ENCODE https://www.encodeproject.org/software/star/ Prism Graphpad, https://www.g...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **4.0**
- Evidence: 119 https://meme-suite.org/meme/doc/download.html RepeatMasker v4.0 Smit et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: ....com/scientific-software/prism Version 10.0.2 (171) R R Core Team and R Foundation for Statistical Computing, https://www.r-project.org version 4.1.1 RepeatMasker Institute for Systems Biology http://www.repeatmasker.org/ FastQC (v0.11.9) Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk bwa-mem Li and Durbin 93 http://maq.sourceforge.net/ Ensembl (V109) Ensembl www.ensembl.org UCS...
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 90 https://bioconductor.org/packages/release/bioc/html/edgeR.html ; RRID:SCR_012802 RepeatMasker (mm10) RepeatMasker Open-3.0.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **4.0.5**
- Evidence: 36 https://busco.ezlab.org RepeatMasker v4.0.5 Smit et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: Most of the repeats were masked only with WindowMasker 75 , with no annotation available by RepeatMasker 104 . j , Minor repeat types in collapsed repeats.
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Universal nomenclature for oxytocin-vasotocin ligand and receptor families. (Nature 2021)

- DOI: 10.1038/s41586-020-03040-7 | PMCID: PMC8081664 | PMID: 33911268
- Evidence: ...ated for DNA transposable elements), and thus we quantitatively searched for adjacent transposable elements in the human and chimpanzee genomes using RepeatMasker ( http://genome.ucsc.edu/ ) 38 and obtained information for each specific transposable element using Dfam 2.0 12 .
- Full pipeline: alignment/mapping [BLAST, MAFFT] -> stage not stated [RepeatMasker]

### HP1 drives de novo 3D genome reorganization in early Drosophila embryos. (Nature 2021)

- DOI: 10.1038/s41586-021-03460-z | PMCID: PMC8116211 | PMID: 33854237
- Evidence: HP1 peaks and repetitive sequences (UCSC RepeatMasker) are represented below. d , Strong enrichment of HP1 close to the pericentromeric heterochromatin. e , One euchromatic HP1 binding region. f , IGV browser snapshots of different genomic regions showing HP1 binding in euchromatin regions.
- Full pipeline: stage not stated [MACS2, RepeatMasker]

### Million-year-old DNA sheds light on the genomic history of mammoths. (Nature 2021)

- DOI: 10.1038/s41586-021-03224-9 | PMCID: PMC7116897 | PMID: 33597750
- Version used: **4.0.7**
- Evidence: Finally, we masked all sites within repetitive regions as identified with RepeatMasker v.4.0.7 37 , CpG sites, sites with more than two alleles among all individuals, and sites with coverage above the 95th percentile of the genome-wide average to reduce false calls from duplicated genomic regions.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.921, BCFtools, Picard, RepeatMasker v4.0.7, SAMtools v1.10]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: We searched for ‘diagnostic’ 15-mers via Jellyfish 58 in LTR regions of Gypsy, Copia and Pao insertions (identified by RepeatMasker 59 and LTRHarvest 60 ) that distinguished each set of homologous chromosomes (≤1 hit in one homologue and ≥100 in the other).
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Evidence: The entire region is contained within a region annotated as repetitive by RepeatMasker (red interval).
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Platypus and echidna genomes reveal mammalian biology and evolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03039-0 | PMCID: PMC8081666 | PMID: 33408411
- Version used: **4.0.6**
- Evidence: For the homology-based method, we used default repeat library from Repbase (v.21.11) 51 for RepeatMasker (v.4.0.6) 52 , trf (v.4.07) 53 and Proteinmasker (v.4.0.6) 52 to annotate.
- Full pipeline: alignment/mapping [BWA, HISAT2, minimap2 v2.13] -> quantification [ggplot2 v3.2.1] -> normalisation [ggplot2 v3.2.1] -> stage not stated [ImageJ v2.0.0, RepeatMasker v4.0.6]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Version used: **4.1.0**
- Evidence: We performed analyses with common repeat collapses included and excluded, defining common repeat collapses as sequences that were over 75% common repeat elements as identified by RepeatMasker (v4.1.0) and TRF (v4.09).
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Evidence: As annotation files for Velocyto, we used the same mm10 gene annotations used in pre-processing, in addition to the mm10 expressed repeat annotation from the RepeatMasker track of UCSC genome browser.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **1.332**
- Evidence: Identification and annotation of repetitive elements Transposable elements (TEs) were identified by the Extensive De-Novo TE Annotator (EDTA) 59 v.1.9.4, and the non-redundant TE libraries for each accession were passed into RepeatMasker v.1.332 ( http://www.repeatmasker.org ) to mask potential genomic repeats together with simple repeats and satellites, by default parameters.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: Genomic repeats were obtained from RepeatMasker and L1Base 48 , 49 and associations with the RIP-seq peaks were investigated using GAT and BEDTools.
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### The landscape of genomic structural variation in Indigenous Australians. (Nature 2023)

- DOI: 10.1038/s41586-023-06842-7 | PMCID: PMC10733147 | PMID: 38093003
- Version used: **4.1.2**
- Evidence: Each extended allele was then scanned for interspersed mobile elements using RepeatMasker (4.1.2-p1) with the following input parameters: -species human -gff -s -norna -nolow.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools] -> visualisation [ggplot2] -> stage not stated [BEDTools, R, RepeatMasker v4.1.2, ape (R), vegan]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: TE analysis The TE annotation of cCREs was annotated using Homer 45 and UCSC mm10 refGene and RepeatMasker annotation.
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Evidence: For the analysis of repeats, the RepeatMasker annotation was downloaded from https://www.repeatmasker.org/species/anoGam.html , RepeatMasker open-4.0.5-Repeat Library 20140131.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### Continuous synthesis of E. coli genome sections and Mb-scale human DNA assembly. (Nature 2023)

- DOI: 10.1038/s41586-023-06268-1 | PMCID: PMC7614783 | PMID: 37380776
- Evidence: Other features were compiled from the RepeatMasker and regulation UCSC annotation tracks.
- Full pipeline: read trimming [minimap2] -> alignment/mapping [SAMtools v1.16.1, minimap2] -> variant calling [Mutect2] -> stage not stated [GATK v4.3.0, Python, RepeatMasker, deepTools v3.5.1]

### ERα-associated translocations underlie oncogene amplifications in breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06057-w | PMCID: PMC10307628 | PMID: 37198482
- Version used: **4.1.2**
- Evidence: 54 ) (v2.12.0), annotated with RepeatMasker (v4.1.2-p1) and Kraken2 (ref.
- Full pipeline: alignment/mapping [MACS2] -> registration [BWA v0.7.15, Picard v2.8.0, SAMtools v1.3.1] -> stage not stated [GSEA, Kraken2, RepeatMasker v4.1.2]

### Increased mutation and gene conversion within human segmental duplications. (Nature 2023)

- DOI: 10.1038/s41586-023-05895-y | PMCID: PMC10172114 | PMID: 37165237
- Version used: **4.1.2**
- Evidence: RepeatMasker v4.1.2 was used to annotate SNVs with additional repeat classes beyond SDs 53 .
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [hifiasm] -> stage not stated [RepeatMasker v4.1.2]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **4.1.2**
- Evidence: Repeat masking Repeat masking on each assembly was iteratively performed using RepeatMasker (v.4.1.2-p1).
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Antibodies against endogenous retroviruses promote lung cancer immunotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05771-9 | PMCID: PMC10115647 | PMID: 37046094
- Evidence: In brief, hidden Markov models (HMMs) representing known human repeat families (Dfam 2.0 library v.150923) were used to annotate GRCh38 using RepeatMasker, configured with nhmmer.
- Full pipeline: quantification [Salmon v0.12.0] -> differential/statistical testing [lme4 v1.1.27.1] -> stage not stated [QuPath v0.3, R, RepeatMasker, data.table v1.14.2, survival (R) v3.2.13, tidyverse v1.0.7]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **2.0.1**
- Evidence: Repetitive DNA annotation De novo repeat finding was done on Hedin/2 pseudomolecules with RepeatModeler v2.0.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.0.1**
- Evidence: Annotation of repeats and transposable elements RepeatModeler (v.2.0.1) 58 and RepBase were used to construct a de novo repeat library for O. fusiformis , which was then filtered for bona fide genes using the predicted proteome of C. teleta .
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: ...ersensitivity sites (ENCFF823HYK) Replication timing ( https://github.com/skandlab/MutSpot/tree/master/features/Ch38 ), fragile sites (HGNC 2021) and RepeatMasker long interspersed nuclear element, short interspersed nuclear element, long terminal repeat, simple repeat and DNA transposon annotations from UCSC 101 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **4.1.2**
- Evidence: Repeat annotation was performed using RepeatMasker (v4.1.2-p1) 71 and the Ensembl nrTEplantsJune2020 repetitive elements database 72 using the RMBlast engine.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: Duplications and structural variants Segmental duplications The segmental duplication content in humans and non-human primates was identified using SEDEF (v1.1) 80 based on the analysis of genome assemblies soft-masked with TRF v.4.0.9 81 , RepeatMasker 82 , and Windowmasker (v2.2.22) 83 .
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **2.0**
- Evidence: On the basis of Repbase, RepeatModeler (v.2.0) 62 ( http://www.repeatmasker.org/RepeatModeler/ ) and LTR_FINDER (v.1.07) 63 ( http://tlife.fudan.edu.cn/ltr_finder/ ) were also used to identify repetitive sequences in baobab genomes.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: In the third analysis, we first identified the location of the α-satellite HOR array(s) in each genome assembly using RepeatMasker 65 (v.4.1.0) followed by HumAS-HMMER ( https://github.com/fedorrik/HumAS-HMMER_for_AnVIL ) and subsequently extracted regions enriched with ‘live’ α-satellite HORs (denoted with an ‘L’ in the HumAS-HMMER BED file).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Evidence: Repetitive sequences were defined using de novo by RepeatModeler (v.open1.0.11) 66 and known repeat sequences in RepBase.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **1.0.11**
- Evidence: Finally, we constructed a database of repetitive elements using RepeatModeler (v.1.0.11) and used it for masking repetitive sequences with RepeatMasker (v.4.0.7).
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Identification of constrained sequence elements across 239 primate genomes. (Nature 2024)

- DOI: 10.1038/s41586-023-06798-8 | PMCID: PMC10808062 | PMID: 38030727
- Version used: **4.1.2**
- Evidence: We identified and soft-masked common genomic repeats within the assemblies using RepeatMasker (version 4.1.2-p1; http://www.repeatmasker.org ), utilizing the primates repeat catalogue as query.
- Full pipeline: alignment/mapping [SAIGE, minimap2] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [RepeatMasker v4.1.2, VEP]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: The sequence composition of identified endogenous Z-RNAs was analysed by matching them against the RepeatMasker annotation retrieved from the UCSC Table Browser 67 .
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: Identification of ZNF729–FH-bound repetitive DNA was performed by intersecting ZNF729–FH peaks with RepeatMasker (RRID: SCR_012954 ) 78 using Bedtools 79 intersect with -f 0.3.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Version used: **4.1.5**
- Evidence: For a region to be defined as an SST1 array, the following criteria were applied: monomeric unit within the array had to be at least 500 bp in length, there had to be at least two monomers, and the monomers had to overlap with RepeatMasker (v.4.1.5, http://repeatmasker.org/ ) SST1 annotations.
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Resulting reads were mapped, using default parameters, with HISAT2 71 using a GRCm38, release 101 genome and index and were removed if they mapped to rRNA or tRNA according to GRCm38 RepeatMasker definitions from UCSC.
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **4.1.0**
- Evidence: Repeat families were reconstructed using RepeatModeller (2.0.1) and subsequently used to annotate repetitive regions and compute repeat divergence in the genome with RepeatMasker (4.1.0) (Extended Data Fig.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: Repeat data were acquired from the RepeatMasker track and the SD annotations of the CHM13 reference (obtained from https://github.com/marbl/CHM13 ); an inversion was classified as repeat-mediated if it was bracketed by repeats in reverse orientation relative to each other, detected through dotplot analysis.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **4.1.6**
- Evidence: One detection pipeline, L1ME-AID (v.1.0.0-beta; L1 Mediated Annotation and Insertion Detector; see Code availability), leverages a local RepeatMasker (v.4.1.6) 91 installation with the Dfam (v.3.8) database 92 to annotate the freeze4 PAV-merged SV insertion callsets (T2T-CHM13 and GRCh38).
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: R. canina short-read data (SRA: ERR1662939 ) were subjected to clustering analysis using the RepeatExplorer2 pipeline, and the output library of repeats was subsequently used to annotate the genome with the implemented RepeatMasker 124 .
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: We first curated a repeat library using RepeatModeler 89 on a small number of high-quality Cannabis assemblies and pre-existing repeat libraries.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Evidence: Repeat annotation We annotated repeat content of each genome with RepeatModeler and RepeatMasker tools.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Genomic coordinates of the transposable elements, specifically L1, MIR and ERV1, were obtained from the mondom5 RepeatMasker GTF file, selecting for those in the ‘forward’ orientation.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: For H. sapiens , we used RepeatMasker (v.open-4-0-3) annotation of GRCh38 genome released by UCSC.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Version used: **4.1.6**
- Evidence: ...v.4.09.1) was run with parameters: '2 7 7 80 10 50 10 -d -h-ngs', recommended for young (in this context, non-deteriorated) repeats as implemented in RepeatMasker (v.4.1.6).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: This pangenome TE library was then used to reannotate whole-genome TEs in our study’s 149 assemblies, as well as in 28 rice assemblies from a previously published pangenome of 33 cultivated rice accessions 16 (excluding Oryza barthii , Oryza glaberrima , aus , basmati and WSSM) using RepeatMasker ( http://repeatmasker.org ) (v.4.1.2).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Evidence: The locations of annotated repeats (RepeatMasker) were downloaded from the UCSC Genome browser 18 , 64 .
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Evidence: Annotation of transposable elements To annotate transposable elements (TEs) in the newly sequenced bats, we first generated a de novo repeat library for each genome assembly using a novel pipeline consisting of RepeatModeler, RepeatClassifier, custom scripts ( https://github.com/davidaray/bioinfo_tools/blob/master/extract_align.py , RepeatAfterMe (RAM) ( https://zenodo.org/record/7076442 ) and the...
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Evidence: For the remaining transposon elements, RepeatModeler 73 was used to search for a second round.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Evidence: The UCSC database 69 was used to obtain the RepeatMasker annotations and TSS, transcription end site, exons and intron positions (RefSeq annotation table).
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: RepeatMasker ( http://www.repeatmasker.org ) and RepeatModeler2 (ref.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **4.1.5**
- Evidence: RepeatMasker (v4.1.5; http://www.repeatmasker.org ) was used to soft mask the repetitive sequence before protein-coding gene prediction.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **4.1.1**
- Evidence: For repeat annotation, we used Tandem Repeats Finder (v.4.09) 100 (parameters: 2 7 7 80 10 50 15 -l 25 -h) to identify TRs and used RepeatMasker (v.4.1.1) 101 with RMBlast to annotate other types of repeat elements, such as LINEs, SINEs and long terminal repeats.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Evidence: A species-specific repeat library was built from BTx623 V3 using RepeatModeler (v.open1.0.11) 69 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Response of an Afro-Palearctic bird migrant to glaciation cycles. (PNAS 2021)

- DOI: 10.1073/pnas.2023836118 | PMCID: PMC8719893 | PMID: 34949638
- Evidence: The homology-based repeat annotation was done by RepeatMasker version open-4.0.7 ( 63 ) (with parameters “-nolow -no_is -norna -engine ncbi -parallel 1”) at the DNA level based on the Repbase library (version: 20170127).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> registration [GATK, Picard] -> differential/statistical testing [R v3.4.2] -> stage not stated [ANGSD, BEDTools, BUSCO, RepeatMasker]

### Quantitative assessment reveals the dominance of duplicated sequences in germline-derived extrachromosomal circular DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2102842118 | PMCID: PMC8617514 | PMID: 34789574
- Evidence: To gauge the SDs and repetitive DNA contents, repetitive elements in RepeatMasker and SDs (genomicSuperDups) from the UCSC Genome Browser ( http://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/ for hg38 and http://hgdownload.soe.ucsc.edu/goldenPath/mm10/database/ for mm10) were intersected with the gDNA and nscDNA sequencing reads.
- Full pipeline: read trimming [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> alignment/mapping [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> stage not stated [RepeatMasker, SAMtools]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: For repeat detection, four software packages—RepeatModeler ( 66 ) ( www.repeatmasker.org/RepeatModeler/ ), RepeatScout ( 67 ), Piler ( 68 ), and LTR-Finder ( 69 )—were used to build a de novo repeat library based on our assembly with the default settings.
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Genome evolution of the psammophyte <i>Pugionium</i> for desert adaptation and further speciation. (PNAS 2021)

- DOI: 10.1073/pnas.2025711118 | PMCID: PMC8545485 | PMID: 34649989
- Evidence: Transposable elements were identified using Tandem Repeats Finder, RepeatMasker, RepeatModeler, and LTR_Finder.
- Full pipeline: stage not stated [ADMIXTURE, AUGUSTUS, BUSCO, GATK, RepeatMasker]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **4.0.7**
- Evidence: For this, repetitive genomic regions are first masked using RepeatMasker v4.0.7 ( 70 ) as implemented in MAKER.
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### Pericentromeric noncoding RNA changes DNA binding of CTCF and inflammatory gene expression in senescence and cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2025647118 | PMCID: PMC8536346 | PMID: 34426493
- Evidence: 1 B ) were annotated to 652 transcripts using databases, including GRCh37/hg19 (coding genes and some noncoding regions) and RepeatMasker (repetitive elements).
- Full pipeline: stage not stated [ImageJ, RepeatMasker]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: Furthermore, we screened the Anaerolineaceae bacterium oral taxon 439 reference genome for repetitive regions with RepeatScout ( 79 ) and Tandem Repeat Finder ( 80 ) and annotated them with RepeatMasker ( http://www.repeatmasker.org ).
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Version used: **4.0.7**
- Evidence: First, RepeatMasker v4.0.7 ( 73 ) was used to mask repetitive sequences using maize transposable elements ( 74 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### A catalog of tens of thousands of viruses from human metagenomes reveals hidden associations with chronic diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2023202118 | PMCID: PMC8201803 | PMID: 34083435
- Evidence: The final database of “virus core” sequences was processed by RepeatMasker to remove low-complexity regions which recruit reads nonspecifically ( 99 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2, NumPy, SAMtools, SciPy] -> machine learning [scikit-learn] -> stage not stated [Cytoscape, RepeatMasker]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Evidence: Repetitive regions were masked, along with transfer ribonucleic acid (tRNA) sequences, using RepeatMasker ( 82 ) and tRNAscan-SE-1.3 ( 83 ).
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: The de novo prediction was carried out using RepeatModeler ( 57 ) to construct a repeat library with default parameters.
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### Multiple independent recombinations led to hermaphroditism in grapevine. (PNAS 2021)

- DOI: 10.1073/pnas.2023548118 | PMCID: PMC8053984 | PMID: 33837155
- Evidence: RepeatMasker v.open-4.0.6 ( 34 ) was used with a custom Vitis vinifera ssp. vinifera repeat library ( 35 ) to identify repetitive and transposable elements.
- Full pipeline: variant calling [RAxML v8.2.4] -> differential/statistical testing [BEAST v2.5.2] -> stage not stated [RepeatMasker]

### Long-read assembly of a Great Dane genome highlights the contribution of GC-rich sequence and mobile elements to canine genomes. (PNAS 2021)

- DOI: 10.1073/pnas.2016274118 | PMCID: PMC7980453 | PMID: 33836575
- Version used: **4.0.7**
- Evidence: Common repeats in both the CanFam3.1 and Zoey assemblies were identified using RepeatMasker version 4.0.7 with option “–species dog,” using the rmblastn (version 2.2.27+) search engine and a combined repeat database consisting of the Dfam_Consensus-20170127 and RepBase-20170127 releases.
- Full pipeline: alignment/mapping [Canu v1.3, Cufflinks v2.2.1, minimap2 v2.9] -> stage not stated [RepeatMasker v4.0.7, kallisto v0.46.0]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: Repeat families were predicted for each genome using RepeatModeler-v1.0.11 ( 74 ).
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### Correlated gene modules uncovered by high-precision single-cell transcriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2206938119 | PMCID: PMC9907105 | PMID: 36508663
- Evidence: For each gene, a list of UMIs was obtained for all reads mapped to that gene, excluding regions masked by RepeatMasker.
- Full pipeline: read trimming [STAR v2.5.2] -> alignment/mapping [RepeatMasker, STAR v2.5.2] -> dimensionality reduction/clustering [R, SciPy] -> stage not stated [PyTorch, STRING db, Seurat v3.9.9.9024, WGCNA]

### Transposable elements drive intron gain in diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2209766119 | PMCID: PMC9860276 | PMID: 36417430
- Evidence: We also searched for matches among predicted repetitive elements found using RepeatModeler ( 50 ).
- Full pipeline: alignment/mapping [MAFFT, SAMtools] -> differential/statistical testing [R, lme4] -> stage not stated [Python, RepeatMasker, phytools]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Version used: **4.08**
- Evidence: We annotated the repetitive sequences in the N. parkeri genome in RepeatMasker (version 4.08) and RepeatProteinMask (version 4.08) ( 56 ) based on the RepBase TE library ( https://www.girinst.org/repbase/ ).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Version used: **4.0.7**
- Evidence: To annotate their repetitive content, we applied RepeatMasker v4.0.7 ( www.repeatmasker.org/ ) with the Maror2 repeat library ( 49 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Ectopic expression of meiotic cohesin generates chromosome instability in cancer cell line. (PNAS 2022)

- DOI: 10.1073/pnas.2204071119 | PMCID: PMC9549395 | PMID: 36179046
- Evidence: First, the summits of high-confidence peaks were intersected with RepeatMasker (RM) and Tandem Repeat Finder (TRF) datasets and the peaks with summits falling into genomic repeats were excluded.
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, clusterProfiler] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [BEDTools, MACS2 v2.2, RepeatMasker]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **4.0.6**
- Evidence: We next used RepeatMasker v4.0.6 ( 66 ) to predict repeat sequences based on the established repeat sequence database, yielding ∼1.54 Gb of repeat sequence.
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **3.3.0**
- Evidence: We integrated this TE library with a known repeat library (Repbase v15.02, homolog-based) and used these with RepeatMasker (v3.3.0) to predict TEs.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Signatures of adaptive evolution in platyrrhine primate genomes. (PNAS 2022)

- DOI: 10.1073/pnas.2116681119 | PMCID: PMC9436310 | PMID: 35994669
- Version used: **4.0.7**
- Evidence: To assess the repeat content of the robust capuchin genome, we first performed a homology-based repeat annotation of our genome assembly using known elements with RepeatMasker v4.0.7 ( 117 ), followed by de novo repeat identification using the library of unknown repeats generated with RepeatModeler v1.0.11 ( 118 ), and finally we used ProcessRepeats from RepeatMasker to summarize all annotated rep...
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BUSCO v3.0.2, RepeatMasker v4.0.7]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Evidence: We annotated repetitive elements using a combination of RepeatModeler ( 68 ) and RepeatMasker v. open-4.0.8 ( 69 ) using Peromyscus - and rodent-specific repeat libraries.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### The landscape of submicroscopic structural variants at the &lt;i&gt;OPN1LW/OPN1MW&lt;/i&gt; gene cluster on Xq28 underlying blue cone monochromacy. (PNAS 2022)

- DOI: 10.1073/pnas.2115538119 | PMCID: PMC9271157 | PMID: 35759666
- Evidence: We used RepeatMasker for the identification of repetitive sequences and performed a BLAST2seq analysis of the upstream and downstream breakpoint sequences for the detection of sequence homologies.
- Full pipeline: stage not stated [RepeatMasker]

### Leafy and weedy seadragon genomes connect genic and repetitive DNA features to the extravagant biology of syngnathid fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2119602119 | PMCID: PMC9245644 | PMID: 35733255
- Evidence: Assemblies were soft-masked for repeats and areas of low complexity with RepeatMasker ( 31 ) using custom repeat libraries made by combining a teleost library extracted from RepeatModeler2 ( 32 ) with species-specific repeat libraries produced by running RepeatModeler.
- Full pipeline: read trimming [STAR] -> alignment/mapping [InterProScan, STAR] -> dimensionality reduction/clustering [BLAST] -> stage not stated [BUSCO, Flye, RepeatMasker]

### Expansion of a retrovirus lineage in the koala genome. (PNAS 2022)

- DOI: 10.1073/pnas.2201844119 | PMCID: PMC9231498 | PMID: 35696585
- Evidence: This library was formed from sequences included in the phylogenic analysis (above), with koala ERVs restricted to those that had both LTRs (100 pCi ERV sequences) and all hard-masked for simple repeats and low-complexity regions by RepeatMasker ( 36 ) to limit false-positive mapping.
- Full pipeline: alignment/mapping [BWA, Picard v2.23.4, RepeatMasker, SAMtools v1.12] -> stage not stated [DELLY, R]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: Repeated sequences were identified using RepeatMasker ( 46 ), RepeatProteinMasker ( 47 ), and Tandem Repeats Finder ( 48 ).
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Triple-helix potential of the mouse genome. (PNAS 2022)

- DOI: 10.1073/pnas.2203967119 | PMCID: PMC9171763 | PMID: 35503911
- Evidence: Black ticks below the plot show annotated TC repeats (RepeatMasker) on the top or bottom strand.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.1] -> differential/statistical testing [R v3.3.1] -> stage not stated [RepeatMasker]

### Species-specific KRAB-ZFPs function as repressors of retroviruses by targeting PBS regions. (PNAS 2022)

- DOI: 10.1073/pnas.2119415119 | PMCID: PMC8931336 | PMID: 35259018
- Evidence: ...q (MACS) ( 19 )] located with strong enrichment at PBS-Lys–containing ERV subgroup K (ERVK) repeats (according to University of California Santa Cruz RepeatMasker nomenclature) ( Fig.
- Full pipeline: stage not stated [BEDTools, RepeatMasker]

### Loss of TET reprograms Wnt signaling through impaired demethylation to promote lung cancer development. (PNAS 2022)

- DOI: 10.1073/pnas.2107599119 | PMCID: PMC8832965 | PMID: 35110400
- Evidence: The annotated information of exon, intron, intergenic, and CGI (CpG island) was downloaded from the University of California Santa Cruz (UCSC) Genome Browser (mm10), and all repetitive elements were annotated by using RepeatMasker (mm10).
- Full pipeline: read trimming [Trim Galore v0.5.0] -> stage not stated [DESeq2, Picard v2.21.2, RepeatMasker, SAMtools v1.4]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: ....0 ( 7 )] sequences as protein evidence; and a de novo repeats library obtained using LTR_Finder ( 47 ), LTRharvest ( 48 ), LTR retriever ( 49 ), and RepeatModeler ( 50 ) as inputs.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: The mm10 mouse genome and hg38 human genome annotated by RepeatMasker were downloaded from the UCSC genome browser.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### Massive invasion of organellar DNA drives nuclear genome evolution in &lt;i&gt;Toxoplasma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2308569120 | PMCID: PMC10636329 | PMID: 37917792
- Evidence: RepeatMasker was used to identify organellar DNA sequences in nuclear genome sequences. mtDNA and ptDNA sequences were used as the repeat library to mask the corresponding nuclear genomes to identify NUMTs and NUPTs, respectively.
- Full pipeline: stage not stated [RepeatMasker]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Evidence: The L. chinensis –specific de novo repeat library was identified and modeled by RepeatModeler ( 56 ), which can automatically execute two core de novo repeat finding programs, RECON and RepeatScout ( 57 ).
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### The lack of negative association between TE load and subgenome dominance in synthesized <i>Brassica</i> allotetraploids. (PNAS 2023)

- DOI: 10.1073/pnas.2305208120 | PMCID: PMC10589682 | PMID: 37816049
- Version used: **4.0.3**
- Evidence: The repeat annotation of B. rapa and B. oleracea were obtained using tools of RepeatModuler and RepeatMasker (version 4.0.3) ( 68 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [R, SciPy] -> stage not stated [Bismark, Bowtie2, RepeatMasker v4.0.3]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **2.0.1**
- Evidence: A de novo repeat library was constructed using RepeatModeler 2.0.1 ( 65 ), which incorporated RECON 1.08 ( 66 ), RepeatScout 1.0.6 ( 67 ), and TRF 4.0.9 ( 68 ) for identification and classification of repeat families.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Version used: **4.1.1**
- Evidence: The repeats in the unaligned sequences of the pangenome were soft-masked using RepeatMasker v4.1.1 ( 82 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Evidence: A custom repeat library was produced using RepeatModeler open-1.0.11 ( http://www.repeatmasker.org ) on five high-quality Ethiopian genomes and Fol4287.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### Complex evolutionary processes maintain an ancient chromosomal inversion. (PNAS 2023)

- DOI: 10.1073/pnas.2300673120 | PMCID: PMC10288594 | PMID: 37311002
- Version used: **4.0.7**
- Evidence: Repetitive genomic regions were masked prior to genome alignment using RepeatMasker (version 4.0.7) and a Timema repeat library from ( 32 ).
- Full pipeline: alignment/mapping [RepeatMasker v4.0.7, SAMtools v1.5] -> variant calling [BCFtools v1.6] -> stage not stated [BEAST v2.6.6, BUSCO v4.0.5, R v4.0.2]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **1.0.10**
- Evidence: We used RepeatModeler (1.0.10) ( 81 ), Tandem Repeat Finder (409) ( 82 ) (“2 7 7 80 10 50 500 -d -l 6”) and MITE_Hunter ( 83 ) (“-I 86 -n 8 -c 8”) for annotating and classifying the repeat families.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **4.1.2**
- Evidence: Repeats were masked with RepeatMasker (4.1.2) using an avian repeat library ( 78 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **4.1.3**
- Evidence: Both raw structural repeat and curated TE libraries were used by RepeatMasker v4.1.3 to produce annotation files.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Version used: **2.0.1**
- Evidence: Interspersed repeats were annotated in the combined MAC + IES assembly with RepeatModeler v2.0.1 ( 90 ), with manual curation of repeat families rnd-1_family-0 (corresponding to BogoMITE element) and rnd-1_family-73 (containing the BstTc1 transposon) ( SI Appendix , SI Methods “Repeat annotation and clustering” ) ( 91 ).
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### Origins of genome-editing excisases as illuminated by the somatic genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213887120 | PMCID: PMC9942806 | PMID: 36669098
- Version used: **2.0.1**
- Evidence: Repeat elements in the MAC and MIC-limited genomes were predicted using RepeatModeler v2.0.1 ( 61 ) and classified using RepeatClassifier v2.0.1.
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [RepeatMasker v2.0.1] -> stage not stated [BUSCO, Flye v2.7, HMMER, OrthoFinder, eggNOG]

### Two-speed genome evolution drives pathogenicity in fungal pathogens of animals. (PNAS 2023)

- DOI: 10.1073/pnas.2212633120 | PMCID: PMC9926174 | PMID: 36595674
- Version used: **4.0.5**
- Evidence: Repeat content was identified using Repeatmodeller v.2.0.1( 94 ) with rmblast v.2.10.0+ and Tandem Repeat Finder v.4.09 ( 95 ), RepeatScout v.1.06 ( 96 ) and RepeatMasker v.4.0.5 ( 97 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, RAxML] -> stage not stated [BUSCO, Canu v1.8, GATK, HMMER, RepeatMasker v4.0.5]

### Fitness consequences of structural variation inferred from a House Finch pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2409943121 | PMCID: PMC11588099 | PMID: 39531493
- Evidence: Repetitive elements and SDs were identified with RepeatMasker ( 63 ) and BISER ( 62 ), respectively ( SI Appendix , Methods ).
- Full pipeline: variant calling [BUSCO, hifiasm] -> stage not stated [BCFtools, PLINK, RepeatMasker]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: The resulting reads were mapped, using default parameters, with HISAT2 ( 72 ) using a GRCh38, release 84 genome and index and were removed if they mapped to rRNA or tRNA according to GRCh38 RepeatMasker definitions from UCSC.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **2.0.1**
- Evidence: Interspersed repeat element families were predicted from the MIC genome assembly with RepeatModeler v2.0.1 (default settings, random number seed 12345) with the following dependencies: rmblast v2.10.0+ ( http://www.repeatmasker.org/RMBlast.html ), TRF 4.09 ( 95 ), RECON ( 98 ), RepeatScout 1.0.6 ( 99 ), RepeatMasker v4.1.1 ( http://www.repeatmasker.org/RMDownload.html ).
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### Elucidating the sustainability of 700 y of Inuvialuit beluga whale hunting in the Mackenzie River Delta, Northwest Territories, Canada. (PNAS 2024)

- DOI: 10.1073/pnas.2405993121 | PMCID: PMC11348011 | PMID: 39136992
- Evidence: Repetitive regions conserved in the cetartiodactyla group were identified in the beluga whale reference genome using RepeatMasker ( 83 ).
- Full pipeline: alignment/mapping [BWA, MAFFT, RepeatMasker, SAMtools] -> registration [GATK, Picard] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ANGSD]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: However, in this instance, the gene annotation file was expanded to incorporate TE annotations sourced from the UCSC RepeatMasker track for the hg38 genome ( 75 , 76 ).
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: Repeat elements were identified using RepeatModeler ( 73 ) and RepeatMasker ( 74 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Genomes of historical specimens reveal multiple invasions of LTR retrotransposons in <i>Drosophila melanogaster</i> during the 19th century. (PNAS 2024)

- DOI: 10.1073/pnas.2313866121 | PMCID: PMC11009621 | PMID: 38564639
- Evidence: To identify TE insertions in the high-quality assemblies of the D. melanogaster strains [Canton-S, Iso1, Pi2, and Dgrp-732 ( 39 – 41 )], we used RepeatMasker [open-4.0.7; -no-is -s -nolow; ( 73 )] providing the consensus sequences of TEs ( 37 ) as custom library.
- Full pipeline: alignment/mapping [BEDTools, MUSCLE v3.8.1551] -> visualisation [Python, ggplot2] -> stage not stated [Cutadapt, RepeatMasker]

### Morc1 reestablishes H3K9me3 heterochromatin on piRNA-targeted transposons in gonocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2317095121 | PMCID: PMC10990106 | PMID: 38502704
- Evidence: RepeatMasker (open-0.4.5, mm10) was used to annotate TEs in the mouse genome (mm10).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Picard] -> quantification [DESeq2] -> normalisation [DESeq2] -> stage not stated [RepeatMasker]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Version used: **2.0.3**
- Evidence: This consolidated database is used for TE detection in each genome prior to soft masking using RepeatMasker (v2.0.3).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **1.0.11**
- Evidence: RepeatModeler (v1.0.11, http://www.repeatmasker.org/RepeatModeler/ ) with the parameters of “-database species -LTRStruct” was applied to construct the de novo repeat custom library, which was used to predict repeats by Repeatmasker.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Spatial variation in the mutation rate within the plant shoot apical meristem. (PNAS 2025)

- DOI: 10.1073/pnas.2514507122 | PMCID: PMC12646271 | PMID: 41213012
- Evidence: We then used the Extensive De-Novo TE Annotator ( 56 ) and RepeatMasker to soft-mask repeats in the primary assembly.
- Full pipeline: alignment/mapping [BUSCO] -> variant calling [hifiasm] -> stage not stated [RepeatMasker]

### Roles of transposable elements and DNA methylation in the formation of CpG islands and CpG-depleted regulatory elements. (PNAS 2025)

- DOI: 10.1073/pnas.2502963122 | PMCID: PMC12582260 | PMID: 41134632
- Evidence: TE annotations were downloaded from RepeatMasker: hg38 – Dec.
- Full pipeline: stage not stated [BEDTools, RepeatMasker]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: RepeatMasker and RepeatProteinMask (v.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Minimizing and quantifying uncertainty in AI-informed decisions: Applications in medicine. (PNAS 2025)

- DOI: 10.1073/pnas.2424203122 | PMCID: PMC12402999 | PMID: 40833408
- Evidence: BED files for ENCODE V3 candidate cis-regulatory elements and UCSC RepeatMasker repetitive elements were downloaded from the UCSC Genome Browser ( 85 , 86 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2] -> differential/statistical testing [scikit-learn] -> stage not stated [Picard, RepeatMasker, SAMtools]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Evidence: The final nuclear assembly of E. clementina and the publicly released ( 45 ) nuclear sequence of E. pelagica (GCA_946965045.2) were used as input to the RepeatModeler2 and RepeatMasker pipelines (see SI Appendix for details).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### CRISPR-Cas9 screening reveals microproteins regulating adipocyte proliferation and lipid metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2506534122 | PMCID: PMC12358916 | PMID: 40773238
- Evidence: For example, in our Adipocyte smORF library of 1,695 predicted smORFs, 418 (~24%) overlap with DNA repeat regions as defined by the RepeatMasker track on the UCSC Genome Browser.
- Full pipeline: alignment/mapping [STAR] -> stage not stated [BLAST, RepeatMasker]

### RNA polymerase III transcription-associated polyadenylation promotes the accumulation of noncoding retrotransposons during infection. (PNAS 2025)

- DOI: 10.1073/pnas.2507186122 | PMCID: PMC12358842 | PMID: 40768347
- Evidence: For CPSF30 ChIP-seq data in NIH3T3 cells, coverage profiles were generated for all (RPKM≥5) or highly expressed (RPKM ≥ 5,000) B2 SINE and tRNA genes in RepeatMasker ( 54 ) that overlap with called peaks.
- Full pipeline: alignment/mapping [MACS2] -> quantification [PyTorch, RepeatMasker]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Version used: **4.1.5**
- Evidence: Sequence alignments were produced for all loci, masking repetitive elements annotated in the reference genome using RepeatMasker v4.1.5 ( http://repeatmasker.org/ ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Genomic origins and evolution of neo-sex chromosomes in Pacific Island birds. (PNAS 2025)

- DOI: 10.1073/pnas.2503746122 | PMCID: PMC12337287 | PMID: 40720643
- Version used: **4.1.2**
- Evidence: To determine neo-sex chromosome rearrangement structures, we masked for repeats (using RepeatMasker v4.1.2 and our custom Myzomela repeat library; see below) and genes (using our gene annotations and a custom Perl script).
- Full pipeline: read trimming [Trim Galore v0.6.2, hifiasm] -> alignment/mapping [Trim Galore v0.6.2, hifiasm] -> stage not stated [BUSCO v5.2.2, R, RepeatMasker v4.1.2, SAMtools v1.11, minimap2 v2.26]

### Genetic rescue of Florida panthers reduced homozygosity but did not swamp ancestral genotypes. (PNAS 2025)

- DOI: 10.1073/pnas.2410945122 | PMCID: PMC12337334 | PMID: 40720660
- Evidence: We excluded repeat regions masked by NCBI (identified by Window Masker and additionally masked repetitive sequences identified with RepeatMasker.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK v4.2, SAMtools] -> variant calling [GATK v4.2] -> normalisation [BEDTools] -> visualisation [BEDTools] -> stage not stated [RepeatMasker, SnpEff, tidyverse]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Evidence: We first used RepeatMasker and RepeatModeler to identify repetitive regions in the de novo assembly of L. lemmus ( 76 , 77 ).
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### Horizontal transmission of functionally diverse transposons is a major source of new introns. (PNAS 2025)

- DOI: 10.1073/pnas.2414761122 | PMCID: PMC12130899 | PMID: 40402243
- Evidence: We constructed consensus sequences and calculated Kimura divergence from the consensus for introner copies using RepeatModeler’s utility tool, Refiner ( 73 ).
- Full pipeline: alignment/mapping [BLAST, MAFFT] -> normalisation [TreeTime] -> structure determination [RepeatMasker]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: Additional repetitive sequences were identified via RepeatModeler ( 31 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Version used: **4.1.1**
- Evidence: We identified TEs using EDTA ( 104 ) and used RepeatMasker v4.1.1 ( 105 ) to obtain a summary of various TE families within this region relative to the rest of chromosome 4.
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Reenacting a mouse genetic evolutionary arms race in yeast reveals that SLXL1/SLX compete with SLY1/2 for binding to Spindlins. (PNAS 2025)

- DOI: 10.1073/pnas.2421446122 | PMCID: PMC11848428 | PMID: 39928872
- Evidence: Briefly, to estimate Slx and Slxl1 copy numbers, short-read sequencing data from M. spretus (SRA:ERR9880927) ( 43 ) and M. caroli (SRA:ERR133992) were mapped to their respective female genome assemblies (GCA_921997135.2, GCA_900094665.2) ( 44 , 45 ) in which RepeatMasker ( 46 ), Tandem Repeat Finder ( 47 ), and 50-mers with an occurrence >50 were masked.
- Full pipeline: alignment/mapping [RepeatMasker] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Evidence: TE annotation utilized RepeatModeler/RepeatMasker (RM) ( 68 ) and EDTA pipelines ( 69 ).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Version used: **2.0.1**
- Evidence: We first identified and masked repetitive elements in our reference genome assembly using RepeatModeler v2.0.1 with a custom repeat library ( 132 ) and RepeatMasker 4.1.6.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

### Metabolic enhancement contributed by horizontal gene transfer is essential for dietary specialization in leaf beetles. (PNAS 2025)

- DOI: 10.1073/pnas.2415717122 | PMCID: PMC11725898 | PMID: 39793087
- Version used: **2.0.4**
- Evidence: In detail, a repeat library, focusing on insect specialization, was initially created using RepeatModeler v2.0.4 ( 47 ) and RepeatMasker v4.1.5 ( 48 ) for the annotation of repeat sequences.
- Full pipeline: alignment/mapping [Clustal Omega, SAMtools v1.17] -> stage not stated [IQ-TREE v2.2.2.6, OrthoFinder v2.5.4, RepeatMasker v2.0.4, eggNOG, fastp v0.23.4]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **2.0.1**
- Evidence: RepeatModeler v2.0.1 ( 66 ) and RepeatMasker v4.0.9 ( 67 ) were used to identify and mask repeat regions in the reference genome.
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### Methylation-associated mutagenesis underlies variation in the mutation spectrum across eukaryotes. (PNAS 2026)

- DOI: 10.1073/pnas.2516368123 | PMCID: PMC12994199 | PMID: 41824497
- Evidence: Corresponding reference assemblies for each species were downloaded from NCBI or publication repository, along with coding and RepeatMasker annotations.
- Full pipeline: alignment/mapping [DeepVariant] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [RepeatMasker]

### Meiotic DNA breaks drive multifaceted mutagenesis in the human germ line. (Science 2023)

- DOI: 10.1126/science.adh2531 | PMCID: PMC7615360 | PMID: 38033082
- Evidence: Repetitive DNA The repeat context of indel breakpoints was identified using the RepeatMasker track for Build 38 downloaded from the UCSC Genome Browser at https://genome.ucsc.edu/cgi-bin/hgTables .
- Full pipeline: stage not stated [RepeatMasker]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: To quantify repeats per read, reads were analyzed with RepeatMasker.
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

