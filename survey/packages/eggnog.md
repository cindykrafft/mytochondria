# eggNOG

- **Category:** phylogenetics
- **Papers in survey:** 47
- **Journals:** PNAS (31), Nature (14), Cell (2)
- **Years:** 2021 (5), 2022 (12), 2023 (3), 2024 (10), 2025 (13), 2026 (4)
- **Versions named:** 5.0 (2), 4.5.1 (2), 4.5 (2), 5.0.2 (1), 5.0.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (6), dimensionality reduction/clustering (4)

## Papers

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: ...ulgaris : ( i ) Pfam domain architectures using Pfamscan and the Pfam database ( Punta et al., 2012 ) (version 33.0); ( ii ) Gene Ontologies from the eggNOG database ( Huerta-Cepas et al., 2016a ) (version 5.0), using eggNOG-mapper ( Huerta-Cepas et al., 2017 ); and ( iii ) gene names from the corresponding best pairwise alignments among predicted proteins from the human genome (version GRCh38, an...
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **5.0**
- Evidence: ...3869 https://doi.org/10.18129/B9.bioc.dada2 Phlyoseq v1.30.090 https://doi.org/10.1371/journal.pone.0061217 https://doi.org/10.18129/B9.bioc.phyloseq eggNOG 5.0 https://doi.org/10.1093/nar/gky1085 https://github.com/eggnogdb/eggnog-mapper MUSCLE v5.1 https://doi.org/10.1038/s41467-022-34630-w https://www.drive5.com/muscle/ raxmlGUI 2.0 https://doi.org/10.1111/2041-210X.13512 https://antonellilab.g...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: Classification of functional categories was performed using the eggNOG-mapper v.1 web service 68 with mapping mode DIAMOND and standard settings.
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### Visualizing translation dynamics at atomic detail inside a bacterial cell. (Nature 2022)

- DOI: 10.1038/s41586-022-05255-2 | PMCID: PMC9534751 | PMID: 36171285
- Evidence: ...nd RefSeq genome annotation for the M. pneumoniae strain M129 (ATCC 29342) were downloaded from NCBI; (ii) protein sequences were also annotated with eggNOG-mapper to obtain COG (Clusters of Orthologous Groups) IDs 8 , 68 ; (iii) for the annotated ribosomal proteins, the corresponding COG multiple sequence alignments from representative bacterial species were downloaded from the eggNOG database 69...
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> structure determination [Coot, PHENIX, Python v3.7.7] -> visualisation [ChimeraX] -> stage not stated [RELION v3.0]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: Cluster of Orthologous Groups functional categories (functional categories) and KEGG Orthology Groups (KOs) 59 were annotated to euk_db sequences with eggNOG-mapper 60 v1.0.3-3-g3e22728, using DIAMOND for the alignments of euk_db sequences against the eggNOG database (the functional category ‘S: unknown function’ was ignored as it does not include functional information).
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **5.0**
- Evidence: The predicted genes were annotated by identifying universal single-copy marker genes (uscMGs) with fetchMGs (v.1.2) 66 , assigning orthologous groups with emapper (v.2.0.1) 67 based on eggNOG (v.5.0) 68 and performing queries against the KEGG database (release 2020-02-10) 69 .
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Evidence: These functional annotations were integrated into a Trinotate database, which retrieved Gene Ontology (GO), eggNOG and Kyoto Encyclopedia of Genes and Genomes (KEGG) terms for each transcript.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Evidence: The assembly was gene-called with BRAKER (v3.0.6) 55 – 62 , using the —fungus flag, and then functionally annotated with eggNOG-mapper (v2.1.12) 63 using the option --target_taxa Fungi.
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: Additional information about gene functions was sourced from the RAST web server 49 ( https://rast.nmpdr.org/ ) and through DIAMOND 50 v.2.0.8 similarity searches against the KEGG 51 v.58 and eggNOG 52 v.4.5 databases using the utility script ‘sqm_annot.pl’ from the SqueezeMeta metagenomics pipeline 53 v.1.6.2.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Evidence: We collected gene ontology terms and functional classification information by applying eggNOG (ref.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Functional and evolutionary significance of unknown genes from uncultivated taxa. (Nature 2024)

- DOI: 10.1038/s41586-023-06955-z | PMCID: PMC10849945 | PMID: 38109938
- Evidence: 24 ) using eggNOG-mapper v.2 (ref.
- Full pipeline: alignment/mapping [BLAST, Clustal Omega, DIAMOND] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [R] -> structure determination [Clustal Omega] -> stage not stated [ColabFold, HMMER, eggNOG]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Evidence: To bin host proteins into functional groups, we used the COG functional category assignments for Synechococcus sp. strain WH8109 proteins in the eggNOG database (v.5.0) 79 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Among primary transcripts, likely contaminants were determined by identifying transcripts predicted on contigs where fewer than 90% of predictions were annotated as either ‘viridiplantae’ or ‘eukaryote’ according to eggNOG-mapper (v2.1.12) 95 , and were removed.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: Further functional annotation was performed using eggNOG-mapper (version emapper-2.1.10) 80 based on eggNOG orthology data 81 and a DIAMOND search algorithm 82 .
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **5.0.2**
- Evidence: The representative genes were annotated by assigning them to orthologous groups with emapper (v.2.1.7) 125 based on eggNOG (v.5.0.2) 126 and by performing queries against the KEGG database (release v.2022-04) 127 .
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### Pesticide residues alter taxonomic and functional biodiversity in soils. (Nature 2026)

- DOI: 10.1038/s41586-025-09991-z | PMCID: PMC12965876 | PMID: 41606316
- Evidence: Functional gene identification and annotation of metagenome sequencing reads were performed using eggNOG-mapper v.2.1.2 77 with eggNOG orthology database v.5.0.2 78 .
- Full pipeline: normalisation [R] -> stage not stated [DADA2, eggNOG, fastp v0.23.4, vegan]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Evidence: We annotated all features containing open reading frames (ORFs) using eggNOG-mapper v2 ( 70 ) with eggNOG database v5.0 ( 71 ).
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### GRINS: Genetic elements that recode assembly-line polyketide synthases and accelerate their diversification. (PNAS 2021)

- DOI: 10.1073/pnas.2100751118 | PMCID: PMC8256042 | PMID: 34162709
- Version used: **4.5**
- Evidence: We used Prodigal through antiSMASH (–genefinding-tool prodigal) in order to obtain CDS predictions, and we annotated all the resulting CDS sequences with the eggNOG mapper utility from the eggNOG4.5 database ( 29 ).
- Full pipeline: structure determination [RAxML] -> stage not stated [eggNOG v4.5]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Version used: **4.5**
- Evidence: Predicted genes were functionally annotated using 1) CAZy database from dbCAN v6 ( 90 ) and HMMER 3.1b2 ( 91 ), 2) KEGG [Release 2015-10-12; ( 92 , 93 )], and 3) eggNOG v4.5 ( 94 ), both using BLAST 2.2.28+.
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Marine viral particles reveal an expansive repertoire of phage-parasitizing mobile elements. (PNAS 2022)

- DOI: 10.1073/pnas.2212722119 | PMCID: PMC9618062 | PMID: 36256808
- Evidence: Genes predicted using prodigal ( 53 ) were annotated independently with both EggNOG ( 54 ) using eggNOG-mapper v2 ( 55 ) and VOGdb using hmmsearch ( 56 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [HMMER, IQ-TREE, Medaka, R v9.4, eggNOG, minimap2]

### Microbiome composition modulates secondary metabolism in a multispecies bacterial community. (PNAS 2022)

- DOI: 10.1073/pnas.2212930119 | PMCID: PMC9586298 | PMID: 36215464
- Evidence: Open reading frames were annotated with prokka v1.14.6 ( 56 ), and further classified into COG categories with eggNOG (evolutionary genealogy of genes: non-supervised orthologous groups) mapper v2.0.8.post2-80-g6e57065 ( 57 ).
- Full pipeline: alignment/mapping [HTSeq, SAMtools v1.9, fastp v0.20.0] -> quantification [HTSeq, SAMtools v1.9] -> differential/statistical testing [R v4.2] -> stage not stated [Bowtie2 v2.4.2, edgeR, eggNOG]

### Metatranscriptomics captures dynamic shifts in mycorrhizal coordination in boreal forests. (PNAS 2022)

- DOI: 10.1073/pnas.2118852119 | PMCID: PMC9245616 | PMID: 35727987
- Evidence: Functional annotations were assigned using eggnog-mapper ( 112 ) and the eggNOG database.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> differential/statistical testing [DESeq2] -> stage not stated [eggNOG]

### Multikingdom interactions govern the microbiome in subterranean cultural heritage sites. (PNAS 2022)

- DOI: 10.1073/pnas.2121141119 | PMCID: PMC9169738 | PMID: 35344401
- Evidence: ... Prodigal (prokaryotic dynamic programming gene-finding algorithm) v2.6.3 ( 53 ), and the protein-coding genes were assigned to the NCBI nr database, eggNOG (evolutionary genealogy of genes: nonsupervised orthologous groups), and KEGG ( https://www.kegg.jp/ ) databases for functional annotation with an e -value threshold of 10 −5 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> stage not stated [R, eggNOG]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: Additionally, orthologous groups were identified in these proteins using eggNOG-mapper ( 67 ) to the viral database (default settings) and InterProScan ( 68 ) was used for further functional characterization of the proteins (default settings).
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Phosphonate production by marine microbes: Exploring new sources and potential function. (PNAS 2022)

- DOI: 10.1073/pnas.2113386119 | PMCID: PMC8931226 | PMID: 35254902
- Version used: **4.5.1**
- Evidence: We annotated the 16 Prochlorococcus and 22 SAR11/ Pelagibacterales genomes containing verified pepM sequences with eggNOG 4.5.1 ( 108 ) using eggNOG-Mapper version 1.0.3–3-g3e22728 ( 109 ).
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler v3.8] -> stage not stated [HMMER v3.1b, eggNOG v4.5.1]

### Kin selection for cooperation in natural bacterial populations. (PNAS 2022)

- DOI: 10.1073/pnas.2119070119 | PMCID: PMC8892524 | PMID: 35193981
- Evidence: For further investigation into properties that may differ between cooperative and private genes, we used eggNOG functional annotations ( 57 ).
- Full pipeline: visualisation [R, ggplot2] -> stage not stated [eggNOG]

### Acquisition of the arginine deiminase system benefits epiparasitic Saccharibacteria and their host bacteria in a mammalian niche environment. (PNAS 2022)

- DOI: 10.1073/pnas.2114909119 | PMCID: PMC8764695 | PMID: 34992141
- Evidence: The existing NCBI PGAP annotations were combined with eggNOG, Pfam, and TIGRFAM annotations to manually identify the arcABC operons.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE, RAxML v8.2.11] -> visualisation [MUSCLE] -> stage not stated [Python, eggNOG]

### Insight into the symbiotic lifestyle of DPANN archaea revealed by cultivation and genome analyses. (PNAS 2022)

- DOI: 10.1073/pnas.2115449119 | PMCID: PMC8784108 | PMID: 35022241
- Version used: **4.5.1**
- Evidence: 1.1.0) ( 50 ), Kyoto Encyclopedia of Genes and Genomes pathway tools ( 51 ), eggNOG (ver.
- Full pipeline: stage not stated [HMMER, Prokka v1.13, RAxML, eggNOG v4.5.1]

### Integrated genomic and functional analyses of human skin-associated &lt;i&gt;Staphylococcus&lt;/i&gt; reveal extensive inter- and intra-species diversity. (PNAS 2023)

- DOI: 10.1073/pnas.2310585120 | PMCID: PMC10666031 | PMID: 37956283
- Evidence: Genomes were annotated using prokka v1.14.6 ( 53 ), followed by functional analysis by eggNOG-mapper v2 (web version) and an in-house script to map completeness of Kyoto Encyclopedia of Genes and Genomes (KEGG) pathways ( 54 ).
- Full pipeline: alignment/mapping [RAxML v1.1.0] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [DADA2, R v4.2, eggNOG, phyloseq]

### Origins of genome-editing excisases as illuminated by the somatic genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213887120 | PMCID: PMC9942806 | PMID: 36669098
- Evidence: MAC and MIC-limited genes were predicted with “Intronarrator” ( https://github.com/Swart-lab/Intronarrator ) and functionally annotated using HMMER3 (hmmscan) ( 58 ), Pannzer2 ( 59 ), and eggNOG ( 60 ).
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [RepeatMasker v2.0.1] -> stage not stated [BUSCO, Flye v2.7, HMMER, OrthoFinder, eggNOG]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Version used: **5.0.0**
- Evidence: Bacterial functional annotations: Protein coding sequences were compared with the KEGG database, Non-supervised Orthologous Groups (eggNOG v5.0.0), and Virus Orthologous Group (VOG, http://vogdb.org ).
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Identification and characterization of the lipoprotein &lt;i&gt;N&lt;/i&gt;-acyltransferase in &lt;i&gt;Bacteroides&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2410909121 | PMCID: PMC11573676 | PMID: 39495918
- Evidence: Functional analysis was performed using eggNOG-mapper (PMID: 30418610).
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [CellProfiler, eggNOG]

### Frequent nonhomologous replacement of replicative helicase loaders by viruses in <i>Vibrionaceae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2317954121 | PMCID: PMC11087808 | PMID: 38683976
- Evidence: The functions of the contrapositive genes were first annotated using eggNOG-mapper2 ( 65 ), KofamScan ( 28 ), and PfamScan ( 66 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.212] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, eggNOG]

### Evolution of homologous recombination rates across bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316302121 | PMCID: PMC11067023 | PMID: 38657048
- Evidence: We tested correlations between inferred r/m and the proportion of various gene functions inferred from COG (clusters of orthologous genes) and CAzy (Carbohydrate-Active Enzymes) categories identified with eggNOG across each reference genome for all bacterial species in this study ( 20 – 22 ).
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> differential/statistical testing [R] -> simulation/modelling [R] -> stage not stated [HMMER, RAxML]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Evidence: The predicted protein-coding genes were annotated with NCBI non-redundant (NR), UniProt (UniProt and TrEMBL), and eggNOG-mapper databases using diamond command with default parameters.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Jumbo phage-mediated transduction of genomic islands. (PNAS 2025)

- DOI: 10.1073/pnas.2512465122 | PMCID: PMC12595487 | PMID: 41150720
- Evidence: Those 136 genomes were then subject to gene prediction by Prodigal (v2.6.3) ( 77 ) and functional annotation by eggNOG-mapper (v2) ( 78 ).
- Full pipeline: alignment/mapping [BLAST] -> dimensionality reduction/clustering [R v4.1.2] -> stage not stated [InterProScan, Prokka, eggNOG]

### Combined pesticide pollution enhances the dissemination of the phage-encoded antibiotic resistome in the soil under nitrogen deposition. (PNAS 2025)

- DOI: 10.1073/pnas.2516722122 | PMCID: PMC12519213 | PMID: 41042849
- Evidence: Functional annotation of related genes was performed using DIAMOND against the KEGG ( 92 ), CAZy ( 93 ), and eggNOG databases ( 94 ).
- Full pipeline: read trimming [fastp v0.22.08] -> alignment/mapping [BLAST] -> visualisation [Cytoscape v3.10.0] -> stage not stated [HMMER v3.1b, R v4.0.3, eggNOG, vegan]

### Nano-biochar regulates phage-host interactions, reducing antibiotic resistance genes in vermicomposting systems. (PNAS 2025)

- DOI: 10.1073/pnas.2511986122 | PMCID: PMC12403132 | PMID: 40838886
- Evidence: Functional annotation of MAGs was performed by comparing DIAMOND to the KEGG, eggNOG, and CAZy databases (e-value ≤ 0.001) ( 45 ).
- Full pipeline: read trimming [QUAST] -> dimensionality reduction/clustering [BLAST] -> stage not stated [IQ-TREE, R, eggNOG]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Evidence: Functional annotation was performed with eggNOG-mapper ( 114 , 115 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Evidence: Functional annotations were generated using eggNOG-mapper (v 2.1.12).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### Yeast adapts to diverse ecological niches driven by genomics and metabolic reprogramming. (PNAS 2025)

- DOI: 10.1073/pnas.2502044122 | PMCID: PMC12358858 | PMID: 40763020
- Evidence: ( 20 ) Yeast-pan 8 9,232 2,974 6,258 This study To illustrate the metabolic functions encoded in the pangenome, we performed a functional annotation for all 3 pangenomes using the eggNOG tool ( 28 ), as well as a functional enrichment analysis based on the annotation from Clusters of Orthologous Groups (COGs).
- Full pipeline: dimensionality reduction/clustering [eggNOG] -> stage not stated [BUSCO]

### Mobile gene clusters and coexpressed plant-rhizobium pathways drive partner quality variation in symbiosis. (PNAS 2025)

- DOI: 10.1073/pnas.2411831122 | PMCID: PMC12337268 | PMID: 40729388
- Evidence: The COG annotation of reference Sinorhizobium genes was obtained from eggNOG-mapper ( 134 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [WGCNA, edgeR, eggNOG]

### Ciprofloxacin-driven purifying selection on viral genomes accelerates soil N&lt;sub&gt;2&lt;/sub&gt;O production. (PNAS 2025)

- DOI: 10.1073/pnas.2503199122 | PMCID: PMC12304974 | PMID: 40668828
- Evidence: VIBRANT v1.2.1 was also performed to annotate the nonredundant functional proteins within viral contigs referencing the KEGG, CARD, Pfam, and eggNOG databases.
- Full pipeline: read trimming [fastp] -> visualisation [Cytoscape v3.7.2] -> stage not stated [BLAST v2.12.0, R v4.3.1, eggNOG, ggplot2, pheatmap]

### Diel partitioning in microbial phosphorus acquisition in the Sargasso Sea. (PNAS 2025)

- DOI: 10.1073/pnas.2410268122 | PMCID: PMC11929403 | PMID: 40085655
- Evidence: The ORF protein sequences were annotated using eggNOG-mapper v2.1.4 [with DIAMOND blastp alignment ( 44 )] for functional annotation, and aligned to the PhyloDB database ( https://github.com/allenlab/PhyloDB ) using the software package EUKulele ( 45 ) for taxonomic annotation.
- Full pipeline: read trimming [featureCounts] -> alignment/mapping [BLAST, eggNOG, featureCounts] -> stage not stated [DESeq2]

### Increasing pesticide diversity impairs soil microbial functions. (PNAS 2025)

- DOI: 10.1073/pnas.2419917122 | PMCID: PMC11745395 | PMID: 39786931
- Evidence: In this study, four CAT databases (life history traits, eggNOG categories, CAZy types, and KEGG pathways) were created according to prescribed protocol ( 49 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.2.3, eggNOG, igraph]

### Metabolic enhancement contributed by horizontal gene transfer is essential for dietary specialization in leaf beetles. (PNAS 2025)

- DOI: 10.1073/pnas.2415717122 | PMCID: PMC11725898 | PMID: 39793087
- Evidence: The functional annotation of protein-coding genes was assessed using eggNOG-mapper version 2 ( http://eggnog-mapper.embl.de/ ).
- Full pipeline: alignment/mapping [Clustal Omega, SAMtools v1.17] -> stage not stated [IQ-TREE v2.2.2.6, OrthoFinder v2.5.4, RepeatMasker v2.0.4, eggNOG, fastp v0.23.4]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Evidence: To complement NCBI’s annotations, we predicted open reading frames (ORFs) from the assemblies using Prodigal v.2.6.3 ( 64 ) and annotated using DIAMOND v.2.1.8 ( 65 ) in eggNOG-mapper v.2.1.11 ( 66 ).
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

