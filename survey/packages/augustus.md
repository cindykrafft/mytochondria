# AUGUSTUS

- **Category:** genomics
- **Papers in survey:** 29
- **Journals:** PNAS (20), Nature (9)
- **Years:** 2021 (6), 2022 (4), 2023 (5), 2024 (6), 2025 (5), 2026 (3)
- **Versions named:** 3.2.3 (3), 3.1.0 (2), 3.4.0 (2), 3.3.3 (2), 3.3 (2), 3.3.2 (1), 2.5.5 (1)
- **Pipeline stages it appears in:** machine learning (7), alignment/mapping (6), structure determination (1)

## Papers

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Version used: **3.3.3**
- Evidence: Ab initio gene prediction was performed using SNAP (v.2006-07-28) 60 and AUGUSTUS (v.3.3.3) 61 .
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **3.4.0**
- Evidence: 62 ) was then run to use the transcript assemblies as hints to generate predicted gene models from AUGUSTUS (v.3.4.0) ( https://github.com/Gaius-Augustus/Augustus ) and to train the hidden Markov model (HMM) of GeneMark-ET (v.3.67_lic) (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **3.2.3**
- Evidence: On the basis of the results of homology prediction, the genes with complete integrity of structure were preserved to train the gene model analysis which was then used with AUGUSTUS v.3.2.3 (ref.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Version used: **3.1.0**
- Evidence: ... of protein/translated open reading frames (ORFs) and EXONERATE (v.2.4.0) 64 , PASA assembly ORFs (in-house homology constrained ORF finder) and from AUGUSTUS (v.3.1.0) 65 trained by the high confidence PASA assembly ORFs and with intron hints from short read alignments.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: For ab initio prediction, four different programs were used: FGENESH+ 75 (v.3.1.1), SNAP 76 (v.2006-07-28), GeneMark-ES 77 (v.4.68_lic) and AUGUSTUS 78 (v.3.3.2).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **3.4.0**
- Evidence: Subsequently, we used the BRAKER2 (v.2.1.5) 78 program to train the ab initio prediction model from AUGUSTUS (v.3.4.0) 79 ( https://github.com/Gaius-Augustus/Augustus ) and collected high-quality RNA-seq hints using the Hidden Markov Model (HMM) from GeneMark-ET (v.3.67) 80 with the parameter “--nocleanup --softmasking”.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: These refined structures were then used to guide the iterative training of gene models in AUGUSTUS 62 (v.3.3.3), a process that continued until the highest predictive scores were achieved.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **3.1.0**
- Evidence: Gene models were predicted using FGENESH+ (v.3.1.0) 74 , FGENESH_EST, EXONERATE, PASA assembly ORFs and AUGUSTUS (v.3.1.0) 75 trained on high-confidence PASA assembly open reading frames with intron hints from RNA sequencing alignments.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Genome modelling and design across all domains of life with Evo 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10176-5 | PMCID: PMC13128491 | PMID: 41781614
- Evidence: Performance was compared to SegmentNT-30 kb multispecies (asterisks indicate species in SegmentNT training data), ab initio AUGUSTUS, and to baseline nucleotide content and conservation metrics.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HMMER, Pangolin] -> machine learning [AUGUSTUS, UMAP] -> stage not stated [AlphaFold, BLAST, HOMER]

### Genome evolution of the psammophyte <i>Pugionium</i> for desert adaptation and further speciation. (PNAS 2021)

- DOI: 10.1073/pnas.2025711118 | PMCID: PMC8545485 | PMID: 34649989
- Evidence: Genes were predicted using AUGUSTUS, GlimmerHMM, PASA, Exonerate, and EVidenceModeler.
- Full pipeline: stage not stated [ADMIXTURE, AUGUSTUS, BUSCO, GATK, RepeatMasker]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Version used: **2.5.5**
- Evidence: Afterward, genes were ab initio predicted using AUGUSTUS v2.5.5 ( 75 ) and FGENESH v8.0.0a (SoftBerry) with maize and monocot matrices, respectively.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Version used: **3.2.3**
- Evidence: For each coassembly, protein-coding genes were predicted de novo with AUGUSTUS 3.2.3 ( 87 , 88 ) using the identified BUSCO v3 proteins as training set ( 89 ).
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Three genomes in the algal genus <i>Volvox</i> reveal the fate of a haploid sex-determining region after a transition to homothallism. (PNAS 2021)

- DOI: 10.1073/pnas.2100712118 | PMCID: PMC8166075 | PMID: 34011609
- Evidence: Other gene models on SDR and SDLR/short SDLR contigs and on autosomal/autosome-like regions were constructed manually after predicted by AUGUSTUS ( 41 ) with the C. reinhardtii parameter and by RNA sequencing mapping ( SI Appendix , Supplementary Information Text 4 ).
- Full pipeline: alignment/mapping [AUGUSTUS] -> stage not stated [BUSCO, Pilon v1.22]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: De novo assembled transcripts were used as training data in ab initio prediction software SNAP ( 64 ) and AUGUSTUS ( 65 ).
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### Anaerobic gut fungi are an untapped reservoir of natural products. (PNAS 2021)

- DOI: 10.1073/pnas.2019855118 | PMCID: PMC8106346 | PMID: 33906945
- Evidence: In the case of incomplete models, we used the BRAKER1 pipeline ( 77 ), which combines usage of RNA-seq read alignments with GeneMark-ET and AUGUSTUS gene finding to extend the gene models to completeness.
- Full pipeline: alignment/mapping [AUGUSTUS, MAFFT] -> dimensionality reduction/clustering [BLAST] -> visualisation [Cytoscape] -> stage not stated [OrthoFinder, RAxML]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **3.3.2**
- Evidence: To obtain quantitative measures of the completeness of the genome assembly, we used BUSCO v.3.0.2 ( 73 ) with BLAST+ v.2.2.28+, HMMER v.3.1b2, and AUGUSTUS v.3.3.2.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: AUGUSTUS ( 51 ) and GENSCAN ( 52 ) were used to construct models for de novo prediction.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **3.3.3**
- Evidence: In between each run of MAKER, the gene models were used to train the ab initio gene predictors SNAP (version 2006-07-28) ( 76 ) and AUGUSTUS 3.3.3 ( 77 ), which were used in the MAKER pipeline. tRNA genes were predicted with tRNAscan-SE 1.3.1 ( 78 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Evidence: An ab initio gene prediction was performed by AUGUSTUS ( 85 ) and GeneMark-EP ( 86 ) with the protein sequences as extrinsic evidence.
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### The expansion of agriculture has shaped the recent evolutionary history of a specialized squash pollinator. (PNAS 2023)

- DOI: 10.1073/pnas.2208116120 | PMCID: PMC10104555 | PMID: 37011184
- Evidence: ...d genome assemblies for the Colorado and Mexico populations of E. pruinosa , used CACTUS ( 61 ) to align these to the reference genome, and then used AUGUSTUS-CGP ( 71 ) to lift over the reference annotation to the new assemblies, thus ensuring that gene models for the nonreference populations formed complete coding sequences (e.g., accounting for indels and changes in splice sites or start/stop c...
- Full pipeline: alignment/mapping [AUGUSTUS] -> variant calling [GATK] -> stage not stated [BUSCO v4.0.6, GSEA, R]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **3.3**
- Evidence: The MAKER gene annotation was then used to train SNAP (2013–11–29) ( 85 ) (maker2zff -c 0.99 -e 0.99 -o 0.99 -l 800 -x 0.01) and AUGUSTUS (3.3) ( 86 ) for ab initio predictions.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Evidence: The tiny introns of Blepharisma are difficult to model with existing gene prediction software, hence RNA-seq data were mapped to the MAC genome to identify introns empirically, before using Intronarrator, a wrapper around AUGUSTUS ( 89 ) with similar parameters as for the Blepharisma MAC genome ( SI Appendix , SI Methods “Gene prediction and domain annotation” ).
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### The &lt;i&gt;ivory&lt;/i&gt; lncRNA regulates seasonal color patterns in buckeye butterflies. (PNAS 2024)

- DOI: 10.1073/pnas.2403426121 | PMCID: PMC11474026 | PMID: 39352931
- Evidence: Briefly, BRAKER3 incorporates transcript selector algorithm TSEBRA with AUGUSTUS predictions through BRAKER1 and BRAKER2 pipelines.
- Full pipeline: alignment/mapping [HISAT2, MACS2] -> differential/statistical testing [DESeq2] -> stage not stated [AUGUSTUS, BUSCO v5.4.7]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: For ab initio annotation, high-quality genic models were predicted using PASA, SNAP ( 85 ), GeneMark ( 86 ), and AUGUSTUS ( 87 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Short macrocyclic peptides in sponge genomes. (PNAS 2024)

- DOI: 10.1073/pnas.2314383121 | PMCID: PMC10945851 | PMID: 38442178
- Version used: **3.3**
- Evidence: The animal genes were predicted using AUGUSTUS 3.3 ( 51 ) with the transcriptome assembly as training data.
- Full pipeline: machine learning [AUGUSTUS v3.3] -> stage not stated [BLAST, Flye]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **3.2.3**
- Evidence: The homology-based annotated genes were then used for de novo prediction using AUGUSTUS (v3.2.3) ( 69 ) and SNAP (v2017-03-01) ( 70 ).
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: The BRAKER2 pipeline, incorporating GeneMark-EP and AUGUSTUS, was used for ab initio gene prediction ( 33 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Genomic signatures associated with the evolutionary loss of egg yolk in parasitoid wasps. (PNAS 2025)

- DOI: 10.1073/pnas.2422292122 | PMCID: PMC12036997 | PMID: 40232796
- Evidence: Thirteen Vg protein sequences of 11 species and two VgR protein sequences from UniProt ( 98 ) or NCBI database as query reference ( SI Appendix, Table S15, S16 ), and AUGUSTUS web interface ( 99 ) or FGENESH+ service online ( 100 ) were utilized for chimeric sequences reannotation.
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> quantification [RSEM] -> structure determination [IQ-TREE, OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, HMMER]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Evidence: We then annotated the genome for protein-coding genes using BRAKER2 —a fully automated pipeline that uses the tools GENEMARK-ES/ET ( 134 ) and AUGUSTUS ( 135 ) for gene structure prediction ( 136 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

