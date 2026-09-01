# InterProScan

- **Category:** phylogenetics
- **Papers in survey:** 62
- **Journals:** PNAS (42), Nature (18), Cell (2)
- **Years:** 2021 (5), 2022 (12), 2023 (8), 2024 (19), 2025 (12), 2026 (6)
- **Versions named:** 5.34 (2), 5.59 (2), 5.52 (2), 5.66 (1), 5.47 (1), 5.50 (1), 4.65 (1), 5.69 (1), 5.61 (1), 5.0 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (1), alignment/mapping (1)

## Papers

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ...ntinued) pBbS5k-RFP Addgene 35285 pUC-21 Addgene 49787 Plasmid DNA This study See Table S2 Software and algorithms HMMER https://www.hmmer.org v3.3.1 InterProScan ( Jones et al., 2014 ) v5.51-85.0 MAFFT ( Katoh and Standley, 2013 ) v7.475 trimAI ( Capella-Gutiérrez et al., 2009 ) v1.4 IQtree ( Minh et al., 2020 ) v2.0.4 ModelFinder ( Kalyaanamoorthy et al., 2017 ) N/A iTOL https://itol.embl.de ( L...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### Mastigoneme structure reveals insights into the O-linked glycosylation code of native hydroxyproline-rich helices. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.005 | PMCID: PMC11015965 | PMID: 38552624
- Evidence: 64 Domains were identified from the primary sequence using InterProScan.
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, ColabFold, InterProScan]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **5.34**
- Evidence: For gene functional annotation, InterProScan 5.34-73.0 (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Undecaprenyl phosphate translocases confer conditional microbial fitness. (Nature 2023)

- DOI: 10.1038/s41586-022-05569-1 | PMCID: PMC9876793 | PMID: 36450355
- Evidence: To assess domain architecture, we used InterProScan ( https://www.ebi.ac.uk/interpro ) with DUF368 (PF04018) or DedA (PF09335) as queries and manually examined identified domain structures.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.3] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, ImageJ v1.53, InterProScan, featureCounts]

### A transcriptomic hourglass in brown algae. (Nature 2024)

- DOI: 10.1038/s41586-024-08059-8 | PMCID: PMC11540847 | PMID: 39443791
- Version used: **5.61**
- Evidence: Enrichment analyses To explore gene function, GO terms were obtained using InterProScan v5.61-93.0 98 .
- Full pipeline: quantification [OrthoFinder v2.5.4] -> stage not stated [InterProScan v5.61, R]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Evidence: Mutations were annotated using SnpEff 67 and InterProScan 45 .
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Evidence: This was complemented by predicting conserved domains using the InterProScan software package (v5.56-89.0) with the SFLD (v4.0), PANTHER (v17.0), SuperFamily (v1.75), PROSITE (v2022_01), CDD (v3.18), Pfam (v34.0), SMART (v7.1), PRINTS (v42.0), and CATH-Gene3D databases (v4.3.0) 38 .
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Version used: **5.0**
- Evidence: Protein families (Pfams) were annotated using InterProScan (v5.0) against Pfam (v43) database.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### Birth of protein folds and functions in the virome. (Nature 2024)

- DOI: 10.1038/s41586-024-07809-y | PMCID: PMC11410667 | PMID: 39187718
- Evidence: Identification of annotated protein sequence clusters Each protein in the database was searched against the Pfam 23 , CDD 24 , and TIGRFAM 25 databases using InterProScan 22 .
- Full pipeline: alignment/mapping [AlphaFold, BLAST, Clustal Omega v1.2.4] -> dimensionality reduction/clustering [BLAST, InterProScan] -> differential/statistical testing [R v4.0.3] -> structure determination [IQ-TREE v2.3.3] -> stage not stated [ColabFold, Nextflow]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **5.64**
- Evidence: Predicted gene annotations obtained from BRAKER were processed using a combination of NCBI BLAST+ (v2.9.0-2) 67 , AGAT (v1.2.1) ( https://github.com/NBISweden/AGAT ), InterProScan (v5.64-96.0) 68 , 69 , and R (v4.2.0).
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: Highly transcribed genes (top 20%) were further inspected using the InterPro web server 54 v.95.0-97.0 ( https://www.ebi.ac.uk/interpro/result/InterProScan ) and searches against the NCBI-nr database 55 using the NCBI BLAST web server ( https://blast.ncbi.nlm.nih.gov/Blast.cgi ).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Version used: **4.65**
- Evidence: We also transferred the gene ontology (GO) terms associated with the best protein hit in RefSeq to each novel gene (using the same identity and coverage filters as above) and inferred the GO terms of the whole pangenome based on sequence using InterProScan v.4.65-97.0 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Evidence: Methylation genes were obtained using human DNMT1, DNMT3A, TET1 and UHRF1 sequences as input for a BLASTP search against the predicted proteome of P. gotoi , and were subsequently analysed in the InterProScan web server ( https://www.ebi.ac.uk/interpro ).
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Complete biosynthesis of salicylic acid from phenylalanine in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09175-9 | PMCID: PMC12408352 | PMID: 40702181
- Version used: **5.69**
- Evidence: The conserved protein PFAM domains for these putative homologues were identified by InterProScan (v.5.69-101.0) 68 , PF00501 and PF13193 for OSD1 ( Os03g0130100 ), PF00378, PF02737 and PF00725 for AIM1 ( Os02g0274100 ), PF00108 and PF02803 for Os KAT1 ( Os02g0817700 ) and Os KAT2 ( Os10g0457600 ), PF02458 for OSD2 ( Os10g0503300 ), PF00067 for OSD3 ( Os09g0441400 ) and PF07859 for OSD4 ( Os05g0410...
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.526, Picard, RAxML v8.2.12] -> stage not stated [InterProScan v5.69]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: For functional annotation of genes, InterProScan 85 (v.5.56-89.0) was used to predict potential protein domains.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **5.34**
- Evidence: To perform functional gene annotation, we utilized the InterProScan (v.5.34-73.0) 86 program, which identifies potential protein domains and Gene Ontology terms based on sequence signatures.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **5.66**
- Evidence: For novel coding transcripts, gene sequences were predicted with GeneMarkS-T (v.5.1) 108 and further validated using InterProScan (v.5.66) 109 with several databases (for example, CDD, Gene3D, PANTHER, Pfam and PIRSF).
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **5.47**
- Evidence: Repeats were functionally analysed with InterProScan (v.5.47-82.0) 70 , incorporating Pfam 71 and PANTHER 72 databases, and those with significant hits to protein-coding domains were excluded.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Version used: **5.50**
- Evidence: InterPro signatures of the C. flexa predicted proteome were obtained using InterProScan (v.5.50-84.0) 90 , 91 .
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Chemical capture of diazo metabolites reveals biosynthetic hydrazone oxidation. (Nature 2026)

- DOI: 10.1038/s41586-025-10079-x | PMCID: PMC13061610 | PMID: 41639443
- Evidence: InterProScan was used to generate additional metadata for all genes and neighbours.
- Full pipeline: visualisation [Cytoscape] -> stage not stated [AlphaFold, BLAST, InterProScan, Prokka]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: Then, the InterProScan ( 65 ) package was used to annotate the predicted genes using the InterPro database.
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Version used: **5.36**
- Evidence: InterProScan v5.36-75.055 was used to identify protein domains and families.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### PilB from &lt;i&gt;Streptococcus sanguinis&lt;/i&gt; is a bimodular type IV pilin with a direct role in adhesion. (PNAS 2021)

- DOI: 10.1073/pnas.2102092118 | PMCID: PMC8179133 | PMID: 34031252
- Evidence: Prediction of protein domains, their global distribution, and associated architectures was done by using InterProScan ( 29 ) to interrogate the InterPro database.
- Full pipeline: visualisation [PyMOL] -> stage not stated [Coot, InterProScan]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Version used: **5.16**
- Evidence: The motifs and domains in protein sequences were annotated using InterProScan version 5.16-55.0 ( 66 ) via searching public databases.
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### Divergent low-density lipoprotein receptor (LDLR) linked to low VSV G-dependent viral infectivity and unique serum lipid profile in zebra finches. (PNAS 2021)

- DOI: 10.1073/pnas.2025167118 | PMCID: PMC8106303 | PMID: 33903244
- Evidence: To compare the predicted protein sequences and structural domains of LDLR orthologs, we used Clustal with default settings in JalView1.0 and InterProScan.
- Full pipeline: stage not stated [InterProScan]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: InterProScan ( 81 ) was used to annotate proteins with Pfam, TMHMM, SignalP, and GO terms.
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### Multiclonal human origin and global expansion of an endemic bacterial pathogen of livestock. (PNAS 2022)

- DOI: 10.1073/pnas.2211217119 | PMCID: PMC9897428 | PMID: 36469788
- Version used: **5.52**
- Evidence: Functional categories of bovine-enriched accessory genes were predicted using EggNOG-mapper (v2.0) ( 54 ), Bakta (v0.5) ( 57 ) , and InterProScan (v5.52-86.0) ( 55 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36] -> alignment/mapping [phytools] -> differential/statistical testing [BEAST, R] -> simulation/modelling [phytools] -> structure determination [phytools] -> stage not stated [InterProScan v5.52, Prokka v1.13]

### Metabolic novelty originating from horizontal gene transfer is essential for leaf beetle survival. (PNAS 2022)

- DOI: 10.1073/pnas.2205857119 | PMCID: PMC9546569 | PMID: 36161953
- Evidence: The HQ transcripts were annotated using BLAST, Gene Ontology, EggNOG, and InterProScan in OmicsBox v2.0 ( https://www.biobam.com/omicsbox ).
- Full pipeline: stage not stated [BLAST, BUSCO, Flye v2.8.3, InterProScan, R v9.4]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Evidence: Seven RGA-related domains and motifs—including NB-ARC, NBS, LRR, TM, STTK, LysM, CC, and TIR—were searched by InterProScan, hmmscan, and phobius from RGAugury pipeline in annotated genes.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Leafy and weedy seadragon genomes connect genic and repetitive DNA features to the extravagant biology of syngnathid fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2119602119 | PMCID: PMC9245644 | PMID: 35733255
- Evidence: We aligned all RNA-seq data (including new and previously published reads) as described above and supplied .bam files to BRAKER2 ( 33 ) for annotation, followed by filtering with InterProScan ( 34 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [InterProScan, STAR] -> dimensionality reduction/clustering [BLAST] -> stage not stated [BUSCO, Flye, RepeatMasker]

### Phylogenomic and functional characterization of an evolutionary conserved cytochrome P450-based insecticide detoxification mechanism in bees. (PNAS 2022)

- DOI: 10.1073/pnas.2205850119 | PMCID: PMC9245717 | PMID: 35733268
- Evidence: Cytochrome P450 sequences were identified by querying proteins for the conserved cytochrome P450 domain (Pfam: PF00067) using InterProScan ( 54 ) and Blast2GO ( 55 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [InterProScan]

### Screening membraneless organelle participants with machine-learning models that integrate multimodal features. (PNAS 2022)

- DOI: 10.1073/pnas.2115369119 | PMCID: PMC9214545 | PMID: 35687670
- Evidence: ... ( 8 ), ESPritz for IDR detection ( 23 ), SEG for LCR detection ( 24 ), CIDER for hydropathy prediction ( 28 ), DeepCoil for CC detection ( 27 ), and InterProScan for modular domain prediction ( 59 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA, InterProScan, XGBoost]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: Additionally, orthologous groups were identified in these proteins using eggNOG-mapper ( 67 ) to the viral database (default settings) and InterProScan ( 68 ) was used for further functional characterization of the proteins (default settings).
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: ... distachyon , Physcomitrella patens subsp. patens , and Chlamydomonas reinhardtii UniProt Trembl proteins; or 3) proteins with a domain identified by InterProScan ( 59 ) with an e value of 1e-10 or lower.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Convergent evolution of venom gland transcriptomes across Metazoa. (PNAS 2022)

- DOI: 10.1073/pnas.2111392119 | PMCID: PMC8740685 | PMID: 34983844
- Evidence: For the GO annotations in this study, we used the CrowdGOFull model, which utilizes annotations from DeepGOPlus ( 55 ), FunFams ( 56 ), InterProScan ( 57 ), and Wei2GO ( 58 ).
- Full pipeline: quality control [kallisto] -> read trimming [kallisto] -> alignment/mapping [RAxML] -> quantification [kallisto] -> normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [Bioconductor, InterProScan]

### The exceptional form and function of the giant bacterium <i>Ca.</i> Epulopiscium viviparus revolves around its sodium motive force. (PNAS 2023)

- DOI: 10.1073/pnas.2306160120 | PMCID: PMC10756260 | PMID: 38109545
- Evidence: InterProScan was used to identify domains in the giant proteins ( 99 ).
- Full pipeline: quantification [pheatmap] -> stage not stated [Canu v1.1, InterProScan]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Evidence: We also used InterProScan ( 74 ) database to annotate the motifs and domains within gene models.
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### Standing genetic variation fuels rapid evolution of herbicide resistance in blackgrass. (PNAS 2023)

- DOI: 10.1073/pnas.2206808120 | PMCID: PMC10120058 | PMID: 37043536
- Evidence: Transcriptome data supported 87.5% of the annotated genes, and 95% of all genes could be assigned functions with InterProScan ( 28 ).
- Full pipeline: read trimming [BUSCO] -> alignment/mapping [MAFFT v7.407] -> variant calling [MAFFT v7.407] -> visualisation [MAFFT v7.407] -> stage not stated [ADMIXTURE, ANGSD v0.930, GATK v4.1.3.0, InterProScan]

### The <i>Holothuria leucospilota</i> genome elucidates sacrificial organ expulsion and bioadhesive trap enriched with amyloid-patterned proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2213512120 | PMCID: PMC10120082 | PMID: 37036994
- Evidence: Gene functions were annotated based on best-matched hits in SwissProt and Gene motifs and domains were identified by InterProScan.
- Full pipeline: alignment/mapping [BUSCO, BWA, MAFFT, RAxML] -> normalisation [DESeq2] -> visualisation [MAFFT, RAxML] -> stage not stated [AlphaFold, InterProScan]

### On the origin of appetite: GLWamide in jellyfish represents an ancestral satiety neuropeptide. (PNAS 2023)

- DOI: 10.1073/pnas.2221493120 | PMCID: PMC10104569 | PMID: 37011192
- Version used: **5.52**
- Evidence: Protein sequences of all Cladonema contigs were predicted using TransDecoder ( 51 ), and these were annotated using InterProScan 5.52-86.0 (European Bioinformatics Institute (EMBL-EBI)) and the Pfam database.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [R, RSEM] -> dimensionality reduction/clustering [R] -> differential/statistical testing [edgeR] -> stage not stated [InterProScan v5.52]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **5.35**
- Evidence: We used InterProScan (5.35 to 74.0) ( 89 ) to annotate GO for the predicted coding genes.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **5.59**
- Evidence: Protein domains were predicted on those hits using InterProScan v5.59-91.0 and visually examined for manual curation ( Dataset S2 ).
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Order of amino acid recruitment into the genetic code resolved by last universal common ancestor's protein domains. (PNAS 2024)

- DOI: 10.1073/pnas.2410311121 | PMCID: PMC11670089 | PMID: 39665745
- Evidence: We used InterProScan ( 88 ) to identify instances of each Pfam domain ( 24 ).
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [MAFFT] -> stage not stated [InterProScan, R, phytools]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Evidence: Positive hits of the BLOC-2 subunits were further characterized for secondary structure using Ali2D ( 71 ) and domain structure using InterProScan ( 72 ).
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **5.57**
- Evidence: The L. magnus predicted MIC and MAC proteomes from Pogigwasc, MAC proteomes from 13 ciliate species, and translated ORFs >30 a.a. predicted by getorf (EMBOSS v6.6.0.0) from 4 species’ MIC genomes ( SI Appendix , Table S4 ), were annotated with InterProScan v5.57-90.0 ( 116 ).
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### &lt;i&gt;Prevotella&lt;/i&gt; are major contributors of sialidases in the human vaginal microbiome. (PNAS 2024)

- DOI: 10.1073/pnas.2400341121 | PMCID: PMC11388281 | PMID: 39186657
- Evidence: We required all hits to be greater than 250 amino acids in length ( SI Appendix , Supplementary Fasta File B ) and validated hits manually by searching for predicted sialidase domains using InterProScan.
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508, RAxML v8.2.10] -> stage not stated [AlphaFold, InterProScan, Python]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **2.1**
- Evidence: Preliminary annotation of the divergent flavi-like virus was performed using InterProScan v2.1 against the CDD, SuperFamily, and NCBIfam databases as implemented in Geneious Prime v2023.2.1.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Evidence: ( D ) InterProScan domains of the wild type and MSS PAX7, along with the Octapeptide (OP, in orange) that was not predicted by InterProScan.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: ...A. coerulea , N. nucifera , T. sinense , B. sinica , V. vinifera , Solanum lycopersicum , and A. thaliana ], were searched using BLASTP (1e −30 ) and InterProScan ( 117 ) with Chlamydomonas reinhardtii ( 118 ) as the outgroup.
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Machine learning enables identification of an alternative yeast galactose utilization pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2315314121 | PMCID: PMC11067038 | PMID: 38669185
- Evidence: Using the KEGG ( 53 , 54 ) and InterProScan ( 55 ) gene functional annotations generated by the Y1000+ Project ( 6 ), a data matrix was built with presence and absence of each unique KEGG Orthology (KO) and counts of each unique InterPro ID number in each genome.
- Full pipeline: quantification [ggplot2 v3.4.2] -> machine learning [XGBoost v1.7.3, scikit-learn] -> visualisation [ggplot2 v3.4.2] -> stage not stated [HMMER, InterProScan]

### An evolutionarily conserved ubiquitin ligase drives infection and transmission of flaviviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2317978121 | PMCID: PMC11032495 | PMID: 38593069
- Evidence: A. aegypti protein (GCF_002204515.2) was annotated by InterProScan using the iprscan5.py script from the European Bioinformatics Institute.
- Full pipeline: differential/statistical testing [ImageJ] -> stage not stated [InterProScan]

### Targeted hypermutation of putative antigen sensors in multicellular bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316469121 | PMCID: PMC10907252 | PMID: 38354254
- Evidence: Sequences were run through InterProScan ( 83 ), hmmscan in the HMMER Web server ( 84 ) and NCBI Conserved Domains Database ( 85 , 86 ) to predict functional domains.
- Full pipeline: read trimming [MAFFT v7.407] -> alignment/mapping [MAFFT v7.407, SAMtools, minimap2 v2.24] -> visualisation [HMMER] -> stage not stated [InterProScan]

### Flexible B&lt;sub&gt;12&lt;/sub&gt; ecophysiology of &lt;i&gt;Phaeocystis antarctica&lt;/i&gt; due to a fusion B&lt;sub&gt;12&lt;/sub&gt;-independent methionine synthase with widespread homologues. (PNAS 2024)

- DOI: 10.1073/pnas.2204075121 | PMCID: PMC10861871 | PMID: 38306482
- Evidence: A protein domain search using InterProScan revealed that this P. antarctica MetE-fusion is a multi-domain protein consisting of three conserved domains and is distinct from canonical MetEs.
- Full pipeline: alignment/mapping [BLAST] -> stage not stated [InterProScan]

### Jumbo phage-mediated transduction of genomic islands. (PNAS 2025)

- DOI: 10.1073/pnas.2512465122 | PMCID: PMC12595487 | PMID: 41150720
- Evidence: The ORFs were then annotated by Pfam in InterProScan ( 75 ).
- Full pipeline: alignment/mapping [BLAST] -> dimensionality reduction/clustering [R v4.1.2] -> stage not stated [InterProScan, Prokka, eggNOG]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Version used: **5.15**
- Evidence: Functions of the predicted genes were annotated using InterProScan v.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Evolutionarily divergent nidovirus with an exceptionally large genome identified in Pacific oysters undergoing mass mortality. (PNAS 2025)

- DOI: 10.1073/pnas.2426923122 | PMCID: PMC12377751 | PMID: 40758866
- Version used: **5.59**
- Evidence: Annotation of these CDSs, including the identification of conserved domains within the polyprotein, was carried out using NCBI Conserved Domain Search (NCBI CD-Search) and InterProScan version 5.59-91.0 ( 97 ), integrating multiple protein domain databases ( SI Appendix , Extended Materials and Methods ).
- Full pipeline: read trimming [MAFFT, SPAdes v3.15.2, Trimmomatic v0.38] -> alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2.1] -> structure determination [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0.3, InterProScan v5.59]

### An endosymbiotic origin of the crimson pigment from the lac insect. (PNAS 2025)

- DOI: 10.1073/pnas.2501623122 | PMCID: PMC12207437 | PMID: 40523179
- Evidence: Preliminary annotations using antiSMASH ( 31 ) and InterProScan ( 32 ) identified no PKS domains encoded by Wolbachia but revealed several genes for putative type I PKS domains in the KLYLS genome.
- Full pipeline: stage not stated [BLAST, BUSCO, IQ-TREE, InterProScan]

### The great phage escape: Activating and escaping lactococcal antiphage systems. (PNAS 2025)

- DOI: 10.1073/pnas.2426508122 | PMCID: PMC12184496 | PMID: 40498451
- Evidence: Escape mutants of PARIS, type II CBASS, AbiD/F, and AbiB antiphage systems harbored mutations in genes which are located in the early expressed region of the corresponding phage genome, and for which no function could be assigned based on domain searches, structural homology analysis (Dali and Foldseek), and comparative sequence analysis (InterProScan, HHpred, and BLASTn/BLASTp) ( 46 , 60 , 61 ).
- Full pipeline: stage not stated [AlphaFold v2.3.1, BLAST, ChimeraX, InterProScan]

### Convergent expansions of keystone gene families drive metabolic innovation in Saccharomycotina yeasts. (PNAS 2025)

- DOI: 10.1073/pnas.2500165122 | PMCID: PMC12167968 | PMID: 40460114
- Evidence: For the final two families, we used InterProScan ( 54 ) v5.72 to annotate protein domains of each member, from which we derived a consensus prediction of protein function.
- Full pipeline: alignment/mapping [IQ-TREE] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [InterProScan, OrthoFinder]

### A long-distance inhibitory system regulates haustoria numbers in parasitic plants. (PNAS 2025)

- DOI: 10.1073/pnas.2424557122 | PMCID: PMC11874510 | PMID: 39964721
- Evidence: Custom annotations of the Phtheirospermum predicted proteins ( 16 ) were estimated using InterProScan ( 53 ) and used for the gene ontology analysis that was performed using the topGO software ( 54 ).
- Full pipeline: read trimming [fastp, featureCounts] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> stage not stated [InterProScan]

### Origin of eukaryotic plasmalogen biosynthesis by horizontal gene transfer from myxobacteria. (PNAS 2026)

- DOI: 10.1073/pnas.2529738123 | PMCID: PMC13012113 | PMID: 41843685
- Evidence: As in Discoba, FAR and GNPAT occur recurrently in Amoebozoa as FARAT, whose detection was straightforward since PSI-BLAST and InterProScan reliably identified the FAR domain.
- Full pipeline: stage not stated [InterProScan]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Version used: **5.62**
- Evidence: For each protein, we extracted the InterPro protein families and Gene Ontology (GO) terms ( 69 ) using InterProScan v.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

