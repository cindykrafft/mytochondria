# Nextstrain

- **Category:** phylogenetics
- **Papers in survey:** 40
- **Journals:** Nature (15), PNAS (15), Cell (5), NEJM (3), Science (1), Lancet (1)
- **Years:** 2021 (10), 2022 (6), 2023 (10), 2024 (7), 2025 (5), 2026 (2)
- **Versions named:** 1.0.0 (2), 3.12.036 (1), 1.0.3 (1), 21.0.1 (1), 0.15 (1), 2.14.1 (1), 2.9.1 (1), 3.0.3 (1)
- **Pipeline stages it appears in:** alignment/mapping (7), visualisation (2), machine learning (1), structure determination (1), quantification (1), quality control (1), dimensionality reduction/clustering (1)

## Papers

### Transmission, infectivity, and neutralization of a spike L452R SARS-CoV-2 variant. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.025 | PMCID: PMC8057738 | PMID: 33991487
- Evidence: ...r v7.388 Katoh and Standley, 2013 , https://mafft.cbrc.jp/alignment/software/ N/A Geneious v11.1.5 Kearse et al., 2012 , https://www.geneious.com N/A Nextstrain/Augur pipeline v3.0.0 https://github.com/nextstrain/augur N/A PANGOLIN v.2.3.8 Rambaut et al., 2020a , https://github.com/cov-lineages/pangolin N/A GraphPad Prism v9.1.0 (216) GraphPad Software, https://www.graphpad.com/ N/A BEAST v2.63 Bo...
- Full pipeline: alignment/mapping [BLAST, MAFFT, Nextstrain] -> stage not stated [IQ-TREE v1.6, Python v3.7.9, R v4.0, SciPy]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Evidence: .../github.com/artic-network/rampart ARTIC Network Bioinformatic protocol ARTIC Network https://artic.network/ncov-2019/ncov2019-bioinformatics-sop.html Nextstrain https://nextstrain.org/ Hadfield et al., 2018 Huff model N/A Huff, 1963 , 2003 Subsampler This paper https://github.com/andersonbrito/subsampler baltic 0.1.5 https://github.com/evogytis/baltic https://github.com/evogytis/baltic ggplot2 CRA...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### SARS-CoV-2 breakthrough infections elicit potent, broad, and durable neutralizing antibody responses. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.011 | PMCID: PMC8769922 | PMID: 35123650
- Version used: **1.0.0**
- Evidence: Sequence quality was determined using Nextclade version 1.0.0-alpha.8 ( https://clades.nextstrain.org/ ).
- Full pipeline: stage not stated [Nextstrain v1.0.0, Pangolin]

### Transmission from vaccinated individuals in a large SARS-CoV-2 Delta variant outbreak. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.027 | PMCID: PMC8695126 | PMID: 35051367
- Version used: **3.0.3**
- Evidence: ...b.io/lofreq/ viral-ngs 2.1.28 Broad Institute https://dockstore.org/workflows/github.com/broadinstitute/viral-pipelines/sarscov2_illumina_full:master Nextstrain v3.0.3 Hadfield et al., 2018 https://dockstore.org/workflows/github.com/broadinstitute/viral-pipelines/sarscov2_nextstrain_aligned_input:master FastTree version 2.1.11 Price et al., 2009 and 2010 http://www.microbesonline.org/fasttree/ bal...
- Full pipeline: dimensionality reduction/clustering [Matplotlib] -> differential/statistical testing [SciPy] -> visualisation [Matplotlib] -> stage not stated [Nextstrain v3.0.3, R]

### A pseudovirus system enables deep mutational scanning of the full SARS-CoV-2 spike. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.001 | PMCID: PMC9922669 | PMID: 36868218
- Evidence: ...1/UShER_SARS-CoV-2/2022/09/26/public-2022-09-26.all.masked.nextclade.pangolin.pb.gz We then used matUtils25 to separate the tree by the pre-annotated Nextstrain clades, and extract the number of unique occurrences of each nucleotide mutation along the tree branches for each clade.
- Full pipeline: stage not stated [Jupyter, Nextstrain, Python, Snakemake]

### Characterisation of SARS-CoV-2 variants in Beijing during 2022: an epidemiological and phylogenetic analysis. (Lancet 2023)

- DOI: 10.1016/s0140-6736(23)00129-0 | PMCID: PMC9949854 | PMID: 36773619
- Version used: **2.9.1**
- Evidence: Phylogenetic and phylodynamic analysis The evaluation of the quality of genomes, genomic alignment, clade, and Pango lineage assignment, and the genetic variation annotations of SARS-CoV-2 genomes were performed by Nextclade version 2.9.1.
- Full pipeline: alignment/mapping [Nextstrain v2.9.1] -> structure determination [IQ-TREE v2.0.3]

### Efficacy of NVX-CoV2373 Covid-19 Vaccine against the B.1.351 Variant. (NEJM 2021)

- DOI: 10.1056/nejmoa2103055 | PMCID: PMC8091623 | PMID: 33951374
- Evidence: D) Per protocol efficacy endpoint accrual relative to distribution of variant as reported in Nextstrain.org .
- Full pipeline: stage not stated [Nextstrain]

### Vaccine Breakthrough Infections with SARS-CoV-2 Variants. (NEJM 2021)

- DOI: 10.1056/nejmoa2105000 | PMCID: PMC8117968 | PMID: 33882219
- Evidence: The SARS-CoV-2 genome was assembled with MEGAHIT with default parameters, and the longest sequence (30,005 nucleotides) was analyzed with Nextclade software ( https://clades.nextstrain.org/ ) in order to assign the clade and call mutations.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Nextstrain]

### Convalescent Plasma for Covid-19-Induced ARDS in Mechanically Ventilated Patients. (NEJM 2023)

- DOI: 10.1056/nejmoa2209502 | PMCID: PMC10755833 | PMID: 37889107
- Evidence: 13 Neutralizing antibody titers were determined with SARS-CoV-2 Nextstrain clade 20B (Wuhan-like, B.1.1), isolated from a Belgian patient, in 96-well plates containing confluent Vero E6 cells (ATCC CRL-1586) 17 and were reported as 50% virus neutralization titer (NT50).
- Full pipeline: stage not stated [Nextstrain]

### SARS-CoV-2 B.1.617.2 Delta variant replication and immune evasion. (Nature 2021)

- DOI: 10.1038/s41586-021-03944-y | PMCID: PMC8566220 | PMID: 34488225
- Version used: **0.15**
- Evidence: Following this, all sequences were passed through Nextclade v0.15 ( https://clades.nextstrain.org/ ) to determine the number of gap regions.
- Full pipeline: stage not stated [IQ-TREE v2.1.4, Nextstrain v0.15, Pangolin v3.1.5, PyMOL, R v4.1]

### Emergence and expansion of SARS-CoV-2 B.1.526 after identification in New York. (Nature 2021)

- DOI: 10.1038/s41586-021-03908-2 | PMCID: PMC8481122 | PMID: 34428777
- Evidence: 2a ) was conducted using the Nextstrain 32 workflow at https://github.com/nextstrain/ncov , which aligns sequences against the Wuhan Hu-1 reference using nextalign ( https://github.com/nextstrain/nextclade ), constructs a maximum-likelihood phylogenetic tree via IQ-TREE 33 , estimates molecular clock branch lengths via TreeTime 34 and reconstructs nucleotide and amino acid changes (also via TreeTi...
- Full pipeline: alignment/mapping [Nextstrain] -> structure determination [IQ-TREE, Nextstrain, TreeTime] -> stage not stated [Pangolin]

### SARS-CoV-2 evolution during treatment of chronic infection. (Nature 2021)

- DOI: 10.1038/s41586-021-03291-y | PMCID: PMC7610568 | PMID: 33545711
- Evidence: Major SARS-CoV-2 clade memberships were assigned to all sequences using both the Nextclade server v0.9 ( https://clades.nextstrain.org/ ) and Phylogenetic Assignment Of Named Global Outbreak Lineages (pangolin) 32 .
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [MAFFT v7.475] -> stage not stated [BCFtools, IQ-TREE v2.1.2, Nextstrain, Picard, SAMtools v1.11]

### The neurons that restore walking after paralysis. (Nature 2022)

- DOI: 10.1038/s41586-022-05385-7 | PMCID: PMC9668750 | PMID: 36352232
- Evidence: We focused our analysis on VE-1 neurons, as these were prioritized by Augur with the highest median AUC across all six comparisons.
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat, velocyto] -> normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.3, fgsea] -> simulation/modelling [Python v2.7] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Evidence: Preliminary maximum-likelihood phylogenies identified the Omicron BA.1 sequences as a monophyletic clade rooted within the B.1.1 lineage (Nextstrain clade 20B), with no clear basal progenitor (Fig.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### A molnupiravir-associated mutational signature in global SARS-CoV-2 genomes. (Nature 2023)

- DOI: 10.1038/s41586-023-06649-6 | PMCID: PMC10651478 | PMID: 37748513
- Evidence: We used Taxonium 48 , the UShER web interface 47 , Nextstrain 51 and Nextclade 52 extensively in investigating individual branches of interest.
- Full pipeline: alignment/mapping [IQ-TREE, TreeTime, minimap2] -> dimensionality reduction/clustering [IQ-TREE, TreeTime] -> structure determination [IQ-TREE, TreeTime] -> stage not stated [Nextstrain]

### Transcriptional linkage analysis with in vivo AAV-Perturb-seq. (Nature 2023)

- DOI: 10.1038/s41586-023-06570-y | PMCID: PMC10567566 | PMID: 37730998
- Version used: **1.0.0**
- Evidence: Augur scoring analysis The Augur (v.1.0.0) R package 53 was created to identify cell types that exhibit a high degree of transcriptional changes when comparing control and perturbed cells (Extended Data Fig.
- Full pipeline: normalisation [Seurat v3.0] -> dimensionality reduction/clustering [Seurat v3.0, UMAP] -> differential/statistical testing [R v3.36.0, edgeR] -> stage not stated [Enrichr v2.1, GSEA, Nextstrain v1.0.0, fgsea v3.17]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Version used: **21.0.1**
- Evidence: Phylogenetic analyses were performed by using the Augur v21.0.1 tool kit 61 procedures implemented in Nextstrain 62 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### Prevalence of persistent SARS-CoV-2 in a large community surveillance study. (Nature 2024)

- DOI: 10.1038/s41586-024-07029-4 | PMCID: PMC10901734 | PMID: 38383783
- Evidence: To map between Pangolin lineages and Nextstrain clades, we assumed B.1.1.7 ≡ 20I, B.1.617.2 ≡ {21A,21I,21J}, BA.1 ≡ 21K and BA.2 ≡ {21L,22C,22D}.
- Full pipeline: stage not stated [IQ-TREE v1.6.12, Nextstrain, Pangolin]

### A neuronal architecture underlying autonomic dysreflexia. (Nature 2025)

- DOI: 10.1038/s41586-025-09487-w | PMCID: PMC12571909 | PMID: 40963010
- Evidence: Cell-type prioritization with Augur To identify neuronal subpopulations perturbed during natural repair, we implemented our machine-learning method Augur 19 , 21 .
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain, QuPath v0.4.3]

### Genomics reveals zoonotic and sustained human mpox spread in West Africa. (Nature 2025)

- DOI: 10.1038/s41586-025-09128-2 | PMCID: PMC12310364 | PMID: 40388983
- Evidence: We classified our sequences into lineages using the nomenclature developed previously 18 using Nextclade 38 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> structure determination [IQ-TREE v2.0] -> stage not stated [Nextstrain]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Version used: **1.0.3**
- Evidence: Augur classifier analysis To identify which cell types have a notable change in expression between the control and mutant conditions, we used the package Augur v.1.0.3 (RRID:SCR_023964) 87 , which performs cross-validated random-forest classifier analysis of single-cell datasets.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Fine-scale patterns of SARS-CoV-2 spread from identical pathogen sequences. (Nature 2025)

- DOI: 10.1038/s41586-025-08637-4 | PMCID: PMC11964829 | PMID: 40044856
- Evidence: Consensus sequences are extracted from the GISAID EpiCoV database 46 , 47 and curated using the Nextstrain nCoV ingest pipeline 48 .
- Full pipeline: dimensionality reduction/clustering [vegan] -> differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [Nextstrain, R, ape (R), igraph]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **3.12.036**
- Evidence: After evaluating the Côte d’Ivoire sequences through Nextclade v.3.12.036 (ref.
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### Ecology and spread of the North American H5N1 epizootic. (Nature 2026)

- DOI: 10.1038/s41586-025-09737-x | PMCID: PMC12779553 | PMID: 41225000
- Evidence: Several of the analyses presented have also been publicly made available using a maximum-likelihood framework through the Nextstrain pipeline and a narrative of this work can be found online ( https://nextstrain.org/community/narratives/moncla-lab/nextstrain-narrative-hpai-north-america@main/HPAI-in-North-America ).
- Full pipeline: alignment/mapping [MAFFT v7.5.20] -> differential/statistical testing [BEAST v1.10.4] -> structure determination [BEAST v1.10.4] -> stage not stated [Nextstrain]

### Mass spectrometric identification of immunogenic SARS-CoV-2 epitopes and cognate TCRs. (PNAS 2021)

- DOI: 10.1073/pnas.2111815118 | PMCID: PMC8609653 | PMID: 34725257
- Evidence: The Nextstrain project ( https://nextstrain.org ), an open-source project that provides a continually updated view of publicly available data alongside powerful analytic and visualization tools to aid epidemiological understanding and improve outbreak response, provides a means to analyze genetic diversity across the SARS-CoV-2 genome.
- Full pipeline: visualisation [Nextstrain]

### The origin and early spread of SARS-CoV-2 in Europe. (PNAS 2021)

- DOI: 10.1073/pnas.2012008118 | PMCID: PMC7936359 | PMID: 33571105
- Evidence: We prepared a sequence alignment from data publicly available on GISAID ( https://www.gisaid.org/ ) on 1 April 2020 using the Nextstrain pipeline for SARS-CoV-2 ( 10 ).
- Full pipeline: alignment/mapping [Nextstrain] -> stage not stated [BEAST]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Evidence: Augur, a tool prioritizing a population’s responsiveness to experimental perturbations ( 45 ), reported a similar global responsiveness for all clusters ( SI Appendix , Fig.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### Epistatic models predict mutable sites in SARS-CoV-2 proteins and epitopes. (PNAS 2022)

- DOI: 10.1073/pnas.2113118119 | PMCID: PMC8795541 | PMID: 35022216
- Evidence: According to Nextstrain ( 10 ) global analysis (May 2021, 3,883 genomes), no mutational event has occurred for 58% of the entire proteome, while only 14% has experienced more than two events.
- Full pipeline: stage not stated [HMMER, Jupyter, Nextstrain, R]

### Targeting spike glycans to inhibit SARS-CoV2 viral entry. (PNAS 2023)

- DOI: 10.1073/pnas.2301518120 | PMCID: PMC10515186 | PMID: 37695910
- Evidence: ( A ) World-wide prevalence of ancestral SARS-CoV-2 (gray) and Alpha (indigo), Beta (purple), Gamma (blue), Delta (teal), and Omicron BA.1 (orange) variants of concern in 2021 [Data from Nextstrain database ( 40 )].
- Full pipeline: stage not stated [Nextstrain]

### Phylogeographic reconstruction of the emergence and spread of Powassan virus in the northeastern United States. (PNAS 2023)

- DOI: 10.1073/pnas.2218012120 | PMCID: PMC10120011 | PMID: 37040418
- Evidence: We created Nextstrain pages to visualize the Powassan genomic data with builds for all available genomes ( 14 ), and a more specific build for genomes available from the northeastern United States ( 15 ).
- Full pipeline: alignment/mapping [Bowtie2] -> visualisation [Nextstrain] -> stage not stated [IQ-TREE v1.6.12, R]

### Divalent siRNAs are bioavailable in the lung and efficiently block SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2219523120 | PMCID: PMC10089225 | PMID: 36893269
- Evidence: Phylogenetic tree construction to identify related coronavirus species was performed with the Augur package. siRNA sequences were selected based on standard rules of optimal GC content and minimization of off-targets with seed region homology.
- Full pipeline: stage not stated [Nextstrain]

### White-tailed deer (<i>Odocoileus virginianus</i>) may serve as a wildlife reservoir for nearly extinct SARS-CoV-2 variants of concern. (PNAS 2023)

- DOI: 10.1073/pnas.2215067120 | PMCID: PMC9963525 | PMID: 36719912
- Evidence: Phylogenetic analysis of both datasets was performed by using procedures implemented in Nextstrain ( 36 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.453, QGIS] -> dimensionality reduction/clustering [QGIS] -> visualisation [IQ-TREE, QGIS] -> stage not stated [Nextstrain, Pangolin v4.0.6]

### Correlated substitutions reveal SARS-like coronaviruses recombine frequently with a diverse set of structured gene pools. (PNAS 2023)

- DOI: 10.1073/pnas.2206945119 | PMCID: PMC9945976 | PMID: 36693089
- Evidence: We used the 191 WGS used in the current Nextstrain build for SL-CoVs ( 52 – 54 ) and aligned these to the NCBI reference genome for SARS-CoV-2 (see Materials and Methods for details).
- Full pipeline: alignment/mapping [Nextstrain, minimap2] -> stage not stated [TreeTime]

### Estimation of SARS-CoV-2 fitness gains from genomic surveillance data without prior lineage classification. (PNAS 2024)

- DOI: 10.1073/pnas.2314262121 | PMCID: PMC11194495 | PMID: 38861609
- Evidence: This takes into consideration the abundance and expansion of named lineages established by the scientific nomenclature system such as those used by Nextstrain ( 7 ) and Pango-lineage ( 8 ), as well as their phenotypic and public health impact.
- Full pipeline: quantification [Nextstrain] -> stage not stated [MAFFT]

### Estimating the reproduction number and transmission heterogeneity from the size distribution of clusters of identical pathogen sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2305299121 | PMCID: PMC11009662 | PMID: 38568971
- Evidence: Instead, we grouped sequences by Pango lineage assigned with Nextclade ( 34 ) and generated a pairwise genetic distance matrix for each Pango lineage.
- Full pipeline: alignment/mapping [R, ape (R)] -> dimensionality reduction/clustering [igraph] -> stage not stated [Nextstrain]

### Incipient functional SARS-CoV-2 diversification identified through neural network haplotype maps. (PNAS 2024)

- DOI: 10.1073/pnas.2317851121 | PMCID: PMC10927536 | PMID: 38416684
- Evidence: ( A ) Successive COVID-19 waves in the world from January 2020 until September 2023 (source Nextstrain, https://nextstrain.org/ncov/gisaid/global ).
- Full pipeline: alignment/mapping [MAFFT v7.453] -> structure determination [TreeTime v0.7.6] -> stage not stated [Nextstrain]

### Idea engines: Unifying innovation & obsolescence from markets & genetic evolution to science. (PNAS 2024)

- DOI: 10.1073/pnas.2312468120 | PMCID: PMC10861874 | PMID: 38306477
- Evidence: We obtain the SARS-CoV-2 clade data from the Nextstrain project downloaded on August 10, 2022. # We use the inferred phylogenetic trees based in the GISAID sequence repository that contains millions of global samples of SARS-CoV-2 strains.
- Full pipeline: stage not stated [Nextstrain]

### Estimates of early outbreak-specific SARS-CoV-2 epidemiological parameters from genomic data. (PNAS 2024)

- DOI: 10.1073/pnas.2308125121 | PMCID: PMC10786264 | PMID: 38175864
- Evidence: Sequence quality control, alignment, and tree building were all performed using the Nextstrain pipeline adapted to SARS-CoV-2 ( 33 ).
- Full pipeline: quality control [Nextstrain] -> alignment/mapping [BEAST, IQ-TREE, Nextstrain] -> differential/statistical testing [BEAST]

### SARS-CoV-2 mutant spectrum complexity is an epidemiologically evolvable trait. (PNAS 2025)

- DOI: 10.1073/pnas.2515706122 | PMCID: PMC12501184 | PMID: 40991435
- Version used: **2.14.1**
- Evidence: Each consensus sequence was assigned to a specific clade using the Nextclade v2.14.1 ( https://clades.nextstrain.org/ ) ( 20 ), Pango Lineages ( https://cov-lineages.org/ ) ( 21 ), and Wuhan-Hu-1 ( NC_045512.2 ) as reference genome.
- Full pipeline: alignment/mapping [MAFFT v7.453, Nextstrain v2.14.1]

### SARS-CoV-2 immune evasion by the B.1.427/B.1.429 variant of concern. (Science 2021)

- DOI: 10.1126/science.abi7994 | PMCID: PMC9835956 | PMID: 34210893
- Evidence: The two lineages B.1.427 and B.1.429 (belonging to clade 20C according to Nextstrain designation) share the same S mutations (S13I in the signal peptide, W152C in the NTD, and L452R in the RBD) but harbor different mutations in other SARS-CoV-2 genes ( 42 ).
- Full pipeline: stage not stated [Nextstrain]

