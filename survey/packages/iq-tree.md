# IQ-TREE

- **Category:** phylogenetics
- **Papers in survey:** 258
- **Journals:** PNAS (156), Nature (82), Cell (13), Science (4), Lancet (3)
- **Years:** 2021 (30), 2022 (36), 2023 (47), 2024 (43), 2025 (76), 2026 (26)
- **Versions named:** 1.6.12 (25), 2.0.3 (11), 2.1.2 (9), 2.1.4 (8), 2.0.6 (7), 2.0 (6), 2.2.0 (5), 2.1.3 (5), 2.2.0.3 (5), 2.1.1 (4)
- **Pipeline stages it appears in:** alignment/mapping (77), structure determination (40), read trimming (13), differential/statistical testing (12), visualisation (11), dimensionality reduction/clustering (2), variant calling (2)

## Papers

### Generation and transmission of interlineage recombinants in the SARS-CoV-2 pandemic. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.014 | PMCID: PMC8367733 | PMID: 34499854
- Version used: **2.1**
- Evidence: We reconstructed the phylogenetic relationships for each with IQTREE v2.1 ( Minh et al., 2020 ), using the HKY model of nucleotide substitution, conducting 1000 ultrafast bootstrap replicates ( Minh et al., 2013 ; Hoang et al., 2018 ), and rooting the tree on the reference sequence, which is basal to all B lineage sequences.
- Full pipeline: alignment/mapping [Pangolin, minimap2] -> variant calling [Python] -> structure determination [IQ-TREE v2.1] -> stage not stated [SAMtools, TreeTime]

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Evidence: Site-specific evolutionary rates, measured in units of expected number of substitutions per site, were inferred using the empirical Bayes method in IQ-TREE (–rate) from subfamily-specific (ESCRT-III and PspA/Vipp1) sequence alignments.
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: The trimmed alignments were used to obtain gene trees with IQ-TREE ( Nguyen et al., 2015 ), using up to 10,000 refinement iterations and a convergence threshold of 0.99.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### Transmission, infectivity, and neutralization of a spike L452R SARS-CoV-2 variant. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.025 | PMCID: PMC8057738 | PMID: 33991487
- Version used: **1.6**
- Evidence: Phylogenetic analysis High-quality SARS-CoV-2 genomes (n = 2,519, 2,172 generated in the current study and 347 used as representative global genomes) were downloaded from the Global Initiative on Sharing of All Influenza Data (GISAID) database and processed using the Nextstrain bioinformatics pipeline Augur using IQTREE v1.6.
- Full pipeline: alignment/mapping [BLAST, MAFFT, Nextstrain] -> stage not stated [IQ-TREE v1.6, Python v3.7.9, R v4.0, SciPy]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...l Computing R Foundation for Statistical Computing Version 4.0.3 Skygrowth https://github.com/mrc-ide/skygrowth N/A SPIn Liu et al., 2015 Version 1.1 IQ-TREE 2 Minh et al., 2020 Version 2.0.6 lubridate https://github.com/tidyverse/lubridate Version 1.7.4 ape Paradis and Schliep, 2019 Version 5.3 brms Bürkner, 2018 Version 2.13.5 drc https://cran.r-project.org/web/packages/drc/drc.pdf Version 3.0-1...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Evaluating the Effects of SARS-CoV-2 Spike Mutation D614G on Transmissibility and Pathogenicity. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.020 | PMCID: PMC7674007 | PMID: 33275900
- Evidence: We estimated the tree using IQ-TREE 2 v.
- Full pipeline: differential/statistical testing [R v3.6] -> stage not stated [BEAST, IQ-TREE, Nextflow, brms v2.13.5]

### Emergence of immune escape at dominant SARS-CoV-2 killer T cell epitope. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.002 | PMCID: PMC9279490 | PMID: 35931021
- Evidence: ... 3, September 2021, https://github.com/evolbioinfo/gotree N/A MAFFT Katoh et al., 2002 http://mafft.cbrc.jp/alignment/server/ MAFFT, RRID: SCR_011811 IQ-TREE Nguyen et al., 2015 . https://doi.org/10.1093/molbev/msu300 http://iqtree.org IQ-TREE, RRID: SCR_017254 MixCR v3.0.13 Bolotin et al., 2015 https://github.com/milaboratory/mixcr MiXCR, RRID: SCR_018725 VDJviz Bagaev et al., 2016 . https://vdjv...
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT] -> stage not stated [CCP4 v7.1, PyMOL v2.3.4, R v4.0, REFMAC v5.8, tidyverse]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **2.1**
- Evidence: 83 N/A Software and algorithms IQ-TREE 2.1 Minh et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### A bat MERS-like coronavirus circulates in pangolins and utilizes human DPP4 and host proteases for cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.019 | PMCID: PMC9933427 | PMID: 36803605
- Version used: **1.6.1**
- Evidence: 44 https://github.com/lh3/bwa BioEdit (v7.1.3.0) software.informer http://www.mbio.ncsu.edu/BioEdit/bioedit.html figtree (v1.4.3) Andrew Rambaut http://tree.bio.ed.ac.uk/software/Figtree/ IQ-TREE (v1.6.1) Barbetti et al.
- Full pipeline: stage not stated [BWA v0.7.12, Cutadapt v1.18, IQ-TREE v1.6.1, ImageJ, Pangolin]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: ...quences were concatenated with a curated set of SF1/SF2 core helicase domains, 12 aligned using ClustalOmega (default parameters), phylogenized using IQ-TREE (-bb 1000, -m MFP (optimal model: LG+R8)), bootstraps inferred using UFBoot2 and visualized using iTOL.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Version used: **1.6.12**
- Evidence: 112 N/A HMMER v3.2.1 Wheeler and Eddy 113 N/A IQ-TREE v1.6.12 Nguyen et al.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### Multiple independent acquisitions of ACE2 usage in MERS-related coronaviruses. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.031 | PMCID: PMC12360793 | PMID: 39922191
- Evidence: Phylogenetic trees were generated using the maximal likelihood method in IQ-TREE ( http://igtree.cibiv.univie.ac.at/ ) (1000 Bootstraps) and refined with iTOL (v6) ( https://itol.embl.de/ ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [RELION] -> structure determination [IQ-TREE, RELION, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX, Topaz]

### Phages communicate across species to shape microbial ecosystems. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.004 | PMCID: PMC13220667 | PMID: 41923642
- Evidence: Swiss Institute of Bioinformatics (SIB) https://web.expasy.org/decrease_redundancy/ Ugene Unipro LLC https://ugene.net/ IQ-TREE Trifinopoulos et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, IQ-TREE, R, ggplot2, ggpubr, tidyverse]

### Efficacy of ChAdOx1 nCoV-19 (AZD1222) vaccine against SARS-CoV-2 variant of concern 202012/01 (B.1.1.7): an exploratory analysis of a randomised controlled trial. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)00628-0 | PMCID: PMC8009612 | PMID: 33798499
- Version used: **1.6.12**
- Evidence: 38 Phylogenetic reconstruction was performed on the alignment consisting of consensus sequences rooted with the Wuhan-Hu-1 reference sequence (RefSeq NC_045512 ), using IQ-TREE version 1.6.12, 39 with the generalised time reversible + FreeRate model and 1000 bootstrap replicates.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.402] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [Pangolin v2.1.7]

### Transmission of SARS-CoV-2 delta variant (AY.127) from pet hamsters to humans, leading to onward human-to-human transmission: a case study. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)00326-9 | PMCID: PMC8912929 | PMID: 35279259
- Version used: **2.1.3**
- Evidence: The maximum likelihood phylogenies were estimated using IQ-TREE (v.2.1.3), 20 employing the TIM2+F+I nucleotide substitution model (best-fit model searched by IQ-TREE) with Wuhan-Hu-1 genome (GenBank: MN908947.3 ) as the outgroup.
- Full pipeline: alignment/mapping [SnpEff] -> stage not stated [IQ-TREE v2.1.3]

### Characterisation of SARS-CoV-2 variants in Beijing during 2022: an epidemiological and phylogenetic analysis. (Lancet 2023)

- DOI: 10.1016/s0140-6736(23)00129-0 | PMCID: PMC9949854 | PMID: 36773619
- Version used: **2.0.3**
- Evidence: IQ-TREE version 2.0.3 20 was used to reconstruct phylogenetic trees for both datasets with 1000 ultrafast bootstrap replicates.
- Full pipeline: alignment/mapping [Nextstrain v2.9.1] -> structure determination [IQ-TREE v2.0.3]

### Independent infections of porcine deltacoronavirus among Haitian children. (Nature 2021)

- DOI: 10.1038/s41586-021-04111-z | PMCID: PMC8636265 | PMID: 34789872
- Version used: **2.0.6**
- Evidence: 2 ), as implemented in IQTREE v.2.0.6 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.407] -> dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [IQ-TREE v2.0.6]

### SARS-CoV-2 B.1.617.2 Delta variant replication and immune evasion. (Nature 2021)

- DOI: 10.1038/s41586-021-03944-y | PMCID: PMC8566220 | PMID: 34488225
- Version used: **2.1.4**
- Evidence: Phylogenies were inferred using maximum likelihood in IQTREE v2.1.4 (ref.
- Full pipeline: stage not stated [IQ-TREE v2.1.4, Nextstrain v0.15, Pangolin v3.1.5, PyMOL, R v4.1]

### Emergence and expansion of SARS-CoV-2 B.1.526 after identification in New York. (Nature 2021)

- DOI: 10.1038/s41586-021-03908-2 | PMCID: PMC8481122 | PMID: 34428777
- Evidence: ...s against the Wuhan Hu-1 reference using nextalign ( https://github.com/nextstrain/nextclade ), constructs a maximum-likelihood phylogenetic tree via IQ-TREE 33 , estimates molecular clock branch lengths via TreeTime 34 and reconstructs nucleotide and amino acid changes (also via TreeTime).
- Full pipeline: alignment/mapping [Nextstrain] -> structure determination [IQ-TREE, Nextstrain, TreeTime] -> stage not stated [Pangolin]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **1.6.11**
- Evidence: The resulting FASTA files containing multiple sequence alignments of the submitted genomes (align/<prefix>.[bac120/ar122].user_msa.fasta) were used for maximum likelihood phylogenetic tree inference using IQ-TREE (v.1.6.11) 89 with the following parameters: -nt AUTO -m LG.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: A phylogenetic tree was calculated using IQ-TREE webserver ( http://iqtree.cibiv.univie.ac.at ) running IQ-TREE 81 1.6.11 with default settings and automatic substitution model selection (best-fit model: TIM2+F+I+G4).
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### SARS-CoV-2 evolution during treatment of chronic infection. (Nature 2021)

- DOI: 10.1038/s41586-021-03291-y | PMCID: PMC7610568 | PMID: 33545711
- Version used: **2.1.2**
- Evidence: Maximum likelihood phylogenetic trees were produced using the above curated dataset using IQ-TREE v2.1.2 33 .
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [MAFFT v7.475] -> stage not stated [BCFtools, IQ-TREE v2.1.2, Nextstrain, Picard, SAMtools v1.11]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Evidence: Orthology was ensured by manual inspection of maximum likelihood gene trees (IQ-TREE) and alignments (MAFFT ginsi) for loci showing high branch-length disparity, and five individual sequences were removed.
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Prokaryotic viperins produce diverse antiviral molecules. (Nature 2021)

- DOI: 10.1038/s41586-020-2762-2 | PMCID: PMC7610908 | PMID: 32937646
- Evidence: The tree was computed with IQ-TREE 19 multicore version v.1.6.5 (option –m TESTNEW in IQ-TREE).
- Full pipeline: stage not stated [HMMER v3.2.1, IQ-TREE]

### Borgs are giant genetic elements with potential to expand metabolic capacity. (Nature 2022)

- DOI: 10.1038/s41586-022-05256-1 | PMCID: PMC9605863 | PMID: 36261517
- Version used: **1.6.6**
- Evidence: The final set of genes was aligned using MAFFT v.7.407, and a phylogenetic tree was inferred using IQTREE v.1.6.6 using automatic model selection 49 and visualized using iTOL 50 .
- Full pipeline: alignment/mapping [BLAST, IQ-TREE v1.6.6, MAFFT, SciPy] -> quantification [SciPy] -> visualisation [BLAST, IQ-TREE v1.6.6, MAFFT] -> stage not stated [HMMER]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: We manually curated the 69 OGs that survived to this filter by performing individual phylogenies for each one, using MAFFT 40 v7.123b [-einsi] for sequence alignment, trimAl 41 v1.4.rev15 [-gappyout] for alignment trimming and IQ-TREE 42 v1.6.7 for maximum-likelihood (ML) phylogenetic inference, using ModelFinder 43 for model selection.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **2.0.3**
- Evidence: The tree was constructed with IQTREE (v.2.0.3) (default parameters and -bb 1000) 80 on an alignment (MUSCLE, v.3.8.1551) 81 of 39 concatenated ribosomal proteins identified by Anvi’o, with positions trimmed for coverage in at least 50% of the genomes 82 and using Planctomycecota as the outgroup based on the GTDB tree topology.
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **2.0.6**
- Evidence: Fourfold degenerate SNPs with base quality ≥ 40 and mapping quality ≥ 30 were fed into IQ-TREE v.2.0.6 (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Phage anti-CBASS and anti-Pycsar nucleases subvert bacterial immunity. (Nature 2022)

- DOI: 10.1038/s41586-022-04716-y | PMCID: PMC9117128 | PMID: 35395152
- Evidence: Maximum-likelihood trees were generated using the IQ-TREE web server with ultrafast bootstrapping and 1,000 iterations 44 .
- Full pipeline: read trimming [Cutadapt v2.8, SPAdes] -> visualisation [PyMOL v2.3.0] -> stage not stated [BLAST, IQ-TREE, PHENIX]

### Enhanced fusogenicity and pathogenicity of SARS-CoV-2 Delta P681R mutation. (Nature 2022)

- DOI: 10.1038/s41586-021-04266-9 | PMCID: PMC8828475 | PMID: 34823256
- Evidence: A maximum likelihood tree was generated using IQ-TREE 2 v.2.1.3 with 1,000 bootstraps 35 .
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [MAFFT, fastp v0.21.0] -> variant calling [SAMtools v1.9] -> stage not stated [BWA v0.7.17, IQ-TREE, ImageJ v2.2.0]

### A molnupiravir-associated mutational signature in global SARS-CoV-2 genomes. (Nature 2023)

- DOI: 10.1038/s41586-023-06649-6 | PMCID: PMC10651478 | PMID: 37748513
- Evidence: We took the 20 sequences in the cluster, and the three closest outgroup sequences, we aligned using Nextclade 52 , calculated a tree using IQ-TREE 54 and reconstructed the mutation-annotated tree using TreeTime 55 .
- Full pipeline: alignment/mapping [IQ-TREE, TreeTime, minimap2] -> dimensionality reduction/clustering [IQ-TREE, TreeTime] -> structure determination [IQ-TREE, TreeTime] -> stage not stated [Nextstrain]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Version used: **2.0**
- Evidence: ModelFinder 84 was run as implemented in IQ-TREE (v.2.0-rc2) to identify the best model among all combinations of the LG, WAG, JTT and Q.pfam models, as well as their corresponding mixture models by adding +C20, +C40 and +C60, and the additional mixture models LG4M, LG4X, UL2 and UL3, with rate heterogeneity (none, +R4 and +G4) and frequency parameters (none, +F).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer. (Nature 2023)

- DOI: 10.1038/s41586-023-05945-5 | PMCID: PMC10232371 | PMID: 37259003
- Version used: **2.2.0.3**
- Evidence: The model used for phylogeny construction was selected using ModelFinder in IQ-TREE (v2.2.0.3) 46 , 47 with --mset set to beast2.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> structure determination [Coot] -> visualisation [Cytoscape v3.9.1, PyMOL, R v4.1.0] -> stage not stated [IQ-TREE v2.2.0.3]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: We carried out a phylogenetic reconstruction using the best-fitting model according to the Bayesian information criterion from the ModelFinder 50 Plus option with IQ-TREE 51 v1.6.2.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Version used: **2.1.1**
- Evidence: Phylogeny was estimated using IQTREE (v.2.1.1) assuming a C60+R model and divergence times estimated using Phylobayes (v.4.1e) 86 assuming a CAT+GTR substitution, and a CIR clock model, soft constraints and a birth-death prior on divergence time.
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: Samples were aligned along with known reference strains from GenBank using MAFFT 65 (version v7.271), and the trees were built with IQ-TREE 66 (multicore version 1.6.12) with 1,000 rapid bootstraps and approximate likelihood-ratio test support.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### Adeno-associated virus 2 infection in children with non-A-E hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05948-2 | PMCID: PMC7617659 | PMID: 36996873
- Evidence: The terminal ends of this alignment were trimmed off, and IQ-TREE 2 was used (TIM+F+R3 model) to infer a phylogenetic tree.
- Full pipeline: read trimming [BWA, IQ-TREE, Trim Galore] -> alignment/mapping [BWA, IQ-TREE, MAFFT, Trim Galore] -> quantification [QuPath v0.3.2] -> differential/statistical testing [R]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Version used: **1.6.1**
- Evidence: Nucleotide and amino acid phylogenetic trees were inferred using a maximum-likelihood method with ultrafast bootstrap approximation as implemented in IQ-TREE (version 1.6.1) 31 using 1,000 bootstrap replicates.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### From primordial clocks to circadian oscillators. (Nature 2023)

- DOI: 10.1038/s41586-023-05836-9 | PMCID: PMC10076222 | PMID: 36949197
- Version used: **1.6**
- Evidence: The multiple sequence alignment was then used as input for the phylogenetic tree calculation with IQ-TREE (v.1.6.beta5), using the LG-substitution matrix 45 with the freeRate model (using 10 categories; LG+R10) 46 , 47 .
- Full pipeline: alignment/mapping [IQ-TREE v1.6, MAFFT, RAxML v8.2.9] -> simulation/modelling [UCSF Chimera v1.15] -> structure determination [Coot v0.9.81, PHENIX v1.20.1] -> visualisation [PyMOL v2.6.0]

### Evolution of the germline mutation rate across vertebrates. (Nature 2023)

- DOI: 10.1038/s41586-023-05752-y | PMCID: PMC9995274 | PMID: 36859541
- Version used: **2.0.3**
- Evidence: A phylogenetic tree was built using IQ-TREE version 2.0.3 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard, SAMtools] -> variant calling [GATK v4.0.7.0] -> stage not stated [ANGSD, BCFtools v1.2, IQ-TREE v2.0.3, R]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.0.3**
- Evidence: 2c,d and Supplementary Tables 11 and 12 ) with a WAG amino acid replacement matrix 93 to account for transition rates, the FreeRate heterogeneity model (R4) 94 to describe sites evolution rates, and an optimization of amino acid frequencies using maximum likelihood using IQ-TREE (v.2.0.3) 95 .
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Phylogenomic reconstructions were performed with IQ-TREE 2 (ref.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Releasing a sugar brake generates sweeter tomato without yield penalty. (Nature 2024)

- DOI: 10.1038/s41586-024-08186-2 | PMCID: PMC11578880 | PMID: 39537922
- Evidence: Subsequently, the phylogeny was used to examine the population structure on the basis of the genome-wide SNPs using the IQTREE program (version 2.1.4) 70 .
- Full pipeline: alignment/mapping [MAFFT v7.525] -> quantification [ImageJ] -> visualisation [ggplot2 v3.4.4] -> stage not stated [IQ-TREE, PLINK, Python, VCFtools v0.1.16]

### Design of customized coronavirus receptors. (Nature 2024)

- DOI: 10.1038/s41586-024-08121-5 | PMCID: PMC12187079 | PMID: 39478224
- Version used: **2.0.6**
- Evidence: Phylogenetic trees were constructed by IQ-TREE (v2.0.6) with the WAG substitution model (1,000 Bootstraps) and rendered with iTOL (v6) ( http://itol.embl.de ).
- Full pipeline: differential/statistical testing [RELION] -> structure determination [RELION] -> visualisation [ChimeraX, IQ-TREE v2.0.6] -> stage not stated [PHENIX v1.21, UCSF Chimera]

### Rifaximin prophylaxis causes resistance to the last-resort antibiotic daptomycin. (Nature 2024)

- DOI: 10.1038/s41586-024-08095-4 | PMCID: PMC11602712 | PMID: 39443798
- Version used: **2.1.2**
- Evidence: A maximum-likelihood phylogenetic tree was inferred using IQ-TREE (v.2.1.2) 39 with a general time-reversible (GTR + G4) substitution model, including invariable sites as a constant pattern and 1,000 bootstrap replicates.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2, HTSeq, MAFFT] -> quantification [Bowtie2, HTSeq] -> differential/statistical testing [tidyverse v1.3.1] -> visualisation [R v4.0.3, tidyverse v1.3.1] -> stage not stated [IQ-TREE v2.1.2, Kraken2]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Evidence: All maximum likelihood phylogenetic trees were estimated using IQ-TREE 2 (v2.1.0) 78 .
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Version used: **2.2.2.3**
- Evidence: We used IQ-TREE (v2.2.2.3) 76 to construct a maximum likelihood tree with Neanderthal and Denisova sequences as the outgroup, using an estimated 650 kyr human–Neanderthal split time for time calibration 27 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Birth of protein folds and functions in the virome. (Nature 2024)

- DOI: 10.1038/s41586-024-07809-y | PMCID: PMC11410667 | PMID: 39187718
- Version used: **2.3.3**
- Evidence: Phylogenetic trees were reconstructed using IQTREE v2.3.3 59 with -m TEST -B 1000 options for model testing and bootstrapping.
- Full pipeline: alignment/mapping [AlphaFold, BLAST, Clustal Omega v1.2.4] -> dimensionality reduction/clustering [BLAST, InterProScan] -> differential/statistical testing [R v4.0.3] -> structure determination [IQ-TREE v2.3.3] -> stage not stated [ColabFold, Nextflow]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Version used: **1.6.12**
- Evidence: In brief, multiple sequence alignments were performed using MAFFT (v7.515) 63 ; maximum likelihood trees were inferred using IQ-TREE (v1.6.12) 64 , and the initial tree was refined using sequence metadata through the augur refine subcommand.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: 75 ) for calculating ultrafast bootstraps during the construction of maximum likelihood trees with IQ-TREE 76 v.2.2.0.3 and v.2.2.2.7.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Phylogenomics and the rise of the angiosperms. (Nature 2024)

- DOI: 10.1038/s41586-024-07324-0 | PMCID: PMC11111409 | PMID: 38658746
- Version used: **2.2.0**
- Evidence: After removing sites with more than 90% missing data with Phyutility 66 , gene trees were estimated using IQ-TREE v.2.2.0-beta 67 , keeping identical sequences in the analysis (--keep-ident), setting the substitution model to GTR + G and estimating branch support with 1,000 ultrafast bootstrap replicates 68 .
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT v7.480] -> stage not stated [IQ-TREE v2.2.0, R]

### DNA glycosylases provide antiviral defence in prokaryotes. (Nature 2024)

- DOI: 10.1038/s41586-024-07329-9 | PMCID: PMC11078745 | PMID: 38632404
- Version used: **1.6.12**
- Evidence: A tree was built with the alignment output file via IQ-TREE 1.6.12 58 using the LG4M model with 1,000 bootstrap alignments.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MUSCLE, Python] -> normalisation [Python] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, ColabFold]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: We used IQ-TREE 81 (v.2.1.2) to reconstruct the maximum-likelihood phylogeny with model selection and 1,000 bootstraps.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Complexity of avian evolution revealed by family-level genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07323-1 | PMCID: PMC11111414 | PMID: 38560995
- Evidence: To identify and collapse poorly supported branches before running ASTRAL we used IQTREE 62 v.1.6.12 to perform parametric approximate likelihood ratio tests (aLRT), which are rapid tests of the three possible nearest-neighbour resolutions around a branch 63 and are more computationally efficient than bootstrapping.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE, RAxML]

### Anoxygenic phototroph of the Chloroflexota uses a type I reaction centre. (Nature 2024)

- DOI: 10.1038/s41586-024-07180-y | PMCID: PMC10972752 | PMID: 38480893
- Version used: **1.6.9**
- Evidence: Genomes of representative members of the Chloroflexota phylum were collected as described in the Supplementary Methods , and we used this genome set to construct a species tree via GToTree (v1.4.11) 90 and IQ-TREE (v1.6.9) 91 .
- Full pipeline: read trimming [DADA2 v1.10.0] -> alignment/mapping [Clustal Omega v1.2.3, featureCounts] -> stage not stated [HMMER v3.1b, IQ-TREE v1.6.9, QIIME 2 v2019.10]

### Prevalence of persistent SARS-CoV-2 in a large community surveillance study. (Nature 2024)

- DOI: 10.1038/s41586-024-07029-4 | PMCID: PMC10901734 | PMID: 38383783
- Version used: **1.6.12**
- Evidence: Maximum likelihood phylogenetic trees were constructed using IQ-TREE (v1.6.12) 56 using the GTR+gamma substitution model and ultrafast bootstrap 57 .
- Full pipeline: stage not stated [IQ-TREE v1.6.12, Nextstrain, Pangolin]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Version used: **1.6.10**
- Evidence: In brief, the process involved the following steps: Using IQ-TREE version 1.6.10, a maximum-likelihood tree was created for the multiple genome alignment 98 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **2.1.1**
- Evidence: Phylogenetic trees were reconstructed for each alignment using IQ-TREE (v.2.1.1) with a LGX+R model 89 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: The resulting alignment was trimmed (microseq 53 R package (v.2.1.4)) and then used to construct a maximum-likelihood phylogenetic tree (IQ-TREE 54 (v.1.6.12)).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Evidence: We calculated a phylogenetic tree using IQ-TREE 86 with the LG + I + G substitution model.
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Florigen activation complex forms via multifaceted assembly in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-025-09704-6 | PMCID: PMC12711580 | PMID: 41225013
- Version used: **1.5.5**
- Evidence: A maximum likelihood algorithm implemented in IQ-TREE v.1.5.5 76 with the Jones–Taylor–Thornton model of evolution under GAMMA rate distribution with bootstrapping criterion (up to a maximum of 1,000 bootstraps) was used for phylogenetic analysis.
- Full pipeline: alignment/mapping [MAFFT] -> quantification [Cellpose v2.2.3] -> stage not stated [AlphaFold, ColabFold, IQ-TREE v1.5.5]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Version used: **2.1.2**
- Evidence: Genes were predicted with Prodigal (v.2.6.3) 84 and maximum-likelihood phylogeny was reconstructed with Phylophlan (v.3.0.2) 85 , Diamond (v.2.1.8) 86 , MAFFT (v.7.475) 87 , trimAl (v.1.4.1) 88 and IQ-TREE (v.2.1.2) 89 ) based on concatenated alignments of protein sequences of nine core genes: primase-helicase, exonuclease, portal protein (head-to-tail adaptor), head assembly protein, major capsid...
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### Assessing phylogenetic confidence at pandemic scales. (Nature 2025)

- DOI: 10.1038/s41586-025-09567-x | PMCID: PMC12611777 | PMID: 41193798
- Version used: **2.1.3**
- Evidence: Other branch support methods All other branch support measures considered here were calculated using IQ-TREE v.2.1.3 40 with options –seqtype DNA –seed 1 -m GTR+F+G4 –quiet -nt 1.
- Full pipeline: stage not stated [IQ-TREE v2.1.3, Pangolin, RAxML]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **2.07**
- Evidence: We inferred a phylogenetic tree using IQ-TREE (v.2.07) 80 with a GTR + I + F + G4 model (general time reversible model with proportion of invariant sites, empirical base frequencies and a gamma distribution with four rate categories) and 1,000 ultrafast bootstraps (-bb 1000).
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **2.1.1**
- Evidence: We constructed sequence alignments for all families including more than 6 genes, more than 3 species and fewer than 400 sequences in total using MAFFT (v.7.471) 78 filtered with CLIPKIT (v.1.1.6, -m gappy) 79 and an initial tree reconstructed with IQ-TREE (v.2.1.1) assuming the LG + R model 80 .
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Deciphering phenylalanine-derived salicylic acid biosynthesis in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09280-9 | PMCID: PMC12408371 | PMID: 40702180
- Evidence: A maximum likelihood phylogenetic tree was constructed using IQ-TREE 70 v2.3.0 with the “LG + F + G4” model and 1,000 ultrafast bootstrap replicates 71 .
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> visualisation [Cytoscape] -> stage not stated [IQ-TREE, ImageJ v1.42q]

### Feline infectious peritonitis epizootic caused by a recombinant coronavirus. (Nature 2025)

- DOI: 10.1038/s41586-025-09340-0 | PMCID: PMC12408369 | PMID: 40633571
- Evidence: Maximum-likelihood trees were constructed using IQ-TREE 62 (v.2.0.5).
- Full pipeline: alignment/mapping [Clustal Omega, minimap2] -> stage not stated [IQ-TREE]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **2.2.0**
- Evidence: A phylogenetic tree was constructed from the alignments with IQ-TREE (version 2.2.0-beta) 65 using the parameters -m MFP -bb 1000 -bnni -redo -o wheat.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Version used: **2.2.2**
- Evidence: A maximum-likelihood phylogenetic tree was inferred using IQ-TREE (v.2.2.2) with automatic model selection (-m MFP) and 1,000 ultrafast bootstrap replicates (-bb 1000).
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Electron flow in hydrogenotrophic methanogens under nickel limitation. (Nature 2025)

- DOI: 10.1038/s41586-025-09229-y | PMCID: PMC12350162 | PMID: 40604290
- Evidence: The maximum-likelihood tree is based on a MUSCLE alignment and was generated using IQ-TREE with LG + I + G4 model of evolution.
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold v3.0, MotionCor2, RELION]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: The alignment was performed with MAFFT 70 , and the phylogenetic tree was calculated using IQ-TREE 71 with the following settings: -m MFP --con-tree --burnin 250 -B 1000 -T 36 --wbtl.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **1.6.12**
- Evidence: ... (2) aligned each gene matrix with MAFFT (v.7.505), using the options ‘--localpair --maxiterate 1000’; and (3) inferred maximum-likelihood trees with IQ-TREE (v.1.6.12) with the options ‘-MFP -bb 1000’.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Genomics reveals zoonotic and sustained human mpox spread in West Africa. (Nature 2025)

- DOI: 10.1038/s41586-025-09128-2 | PMCID: PMC12310364 | PMID: 40388983
- Version used: **2.0**
- Evidence: We reconstructed the complete MPXV phylogeny with IQ-TREE v2.0, under the Jukes–Cantor substitution model 37 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> structure determination [IQ-TREE v2.0] -> stage not stated [Nextstrain]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: Within Broccoli, we used the maximum-likelihood gene tree inference algorithm (based on IQ-TREE 121 ) and set a k -mer length of 10,000 to avoid the removal of paralogous sequences from the analysis.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Deep origin of eukaryotes outside Heimdallarchaeia within Asgardarchaeota. (Nature 2025)

- DOI: 10.1038/s41586-025-08955-7 | PMCID: PMC12222021 | PMID: 40335687
- Evidence: IQ-TREE 70 (v.2.2.2.6) was used to infer phylogenetic trees under the LG + C60 + F + G + PMSF model.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT] -> stage not stated [Bowtie2, HMMER, IQ-TREE, SAMtools, SPAdes]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **2.1.2**
- Evidence: Phylogenetic trees were constructed by IQ-TREE (v.2.1.2) with 1,000 ultrafast bootstrap replicates.
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Version used: **2.1.2**
- Evidence: Phylogenetic relationships were analysed in 100-kb windows by constructing maximum likelihood trees with IQ-TREE (v.2.1.2) 76 under the general-time-reversible (GTR) model with 1,000 bootstrap replicates.
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: Subsequent phylogenetic analysis was performed using IQ-TREE 96 (v.1.6.12), incorporating a bootstrap value of 1,000 for robustness.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Structure of the ATP-driven methyl-coenzyme M reductase activation complex. (Nature 2025)

- DOI: 10.1038/s41586-025-08890-7 | PMCID: PMC12176620 | PMID: 40240609
- Evidence: Gene trees were inferred using IQ-TREE 72 .
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [Coot v0.9.8.92, PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX v1.6.1] -> stage not stated [AlphaFold, IQ-TREE, UCSF Chimera v1.17.3]

### Drivers of avian genomic change revealed by evolutionary rate decomposition. (Nature 2025)

- DOI: 10.1038/s41586-025-08777-7 | PMCID: PMC12119353 | PMID: 40108459
- Version used: **2.1.2**
- Evidence: Phylogenetic branch lengths from intergenic regions were estimated using the best-fitting model from the GTR + F + R 57 family in IQ-TREE (v2.1.2) 58 .
- Full pipeline: dimensionality reduction/clustering [BLAST, clusterProfiler] -> differential/statistical testing [brms] -> structure determination [phytools] -> visualisation [phytools] -> stage not stated [IQ-TREE v2.1.2, R]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **2.1.3**
- Evidence: 87 , 88 ), and a concatenated approach, as implemented in IQTREE v.2.1.3 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **2.0.6**
- Evidence: Separately for each chromosome pair, all single-copy orthologous protein sequences were merged into a single FASTA file, which was then fed into IQ-TREE (v.2.0.6) 93 using the maximum-likelihood method.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **2.2.3**
- Evidence: IQ-TREE (v.2.2.3) was used to construct the phylogenetic tree with the maximum likelihood approach.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Version used: **2.0.3**
- Evidence: The alignment was trimmed with ClipKIT 61 and used to reconstruct a phylogeny with IQ-TREE v2.0.3 (-m MFP -T 8 -B 1000) 62 , using a maximum-likelihood approach.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **2.0.3**
- Evidence: The alignments were concatenated into a super matrix, and a phylogenetic tree was subsequently constructed using IQ-TREE (v2.0.3) 52 with the parameters -m TEST, -seqtype DNA, and -bb 10000.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Version used: **2.3.4**
- Evidence: Maximum-likelihood phylogenetic reconstruction was performed using IQTREE (v.2.3.4) 52 with 1,000 ultrafast bootstrap replicates (UFBoot) and 1,000 SH-like approximate likelihood ratio tests 53 (Supplementary Fig.
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Evidence: The maximum likelihood of the phylogenetic relationship was inferred using IQ-TREE 2 (v2.2.0) 106 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **1.6.12**
- Evidence: Maximum likelihood phylogenetic trees for (1) global 7PET and (2) sBD1 and (3) BD2 within the systematic 2014–2018 surveillance study were created using IQ-TREE v.1.6.12 using the HKY+F+I substitution model 49 .
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Dogs were widely distributed across western Eurasia during the Palaeolithic. (Nature 2026)

- DOI: 10.1038/s41586-026-10170-x | PMCID: PMC13017512 | PMID: 41882128
- Version used: **2.1.4**
- Evidence: From this alignment (15,457 sites excluding the control region) we constructed a maximum-likelihood tree in IQ-TREE v.2.1.4 (ref.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.505] -> differential/statistical testing [BEAST v2.6.7] -> stage not stated [ADMIXTURE v1.3.0]

### Capturing dynamic phage-pathogen coevolution by clinical surveillance. (Nature 2026)

- DOI: 10.1038/s41586-026-10136-z | PMCID: PMC12987554 | PMID: 41813903
- Version used: **2.2.0**
- Evidence: Phylogenetic analysis was performed using IQ-TREE v.2.2.0 (ref.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [BLAST, ColabFold, IQ-TREE v2.2.0, SPAdes, fastp v0.23.2]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Evidence: The resulting VCF files were converted to PHYLIP format as input for IQ-TREE using the vcfR package 83 in R (v.4.1.1).
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Evidence: We then estimated the shape parameter α by maximum likelihood, using the program IQ-TREE 3 (v.3.0.1) 85 .
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **2.1.4b**
- Evidence: We used this alignment to reconstruct a maximum-likelihood phylogeny using IQ-TREE v.2.1.4b 50 , 51 .
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Version used: **1.6.12**
- Evidence: We prepared multi-FASTA alignments combining those markers together across all individuals and reconstructed maximum likelihood phylogenies in IQ-TREE (v.1.6.12; ref.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Version used: **2.3.6**
- Evidence: The trimmed alignment generated using ClipKIT 60 was then used to reconstruct a phylogeny using IQ-TREE (v.2.3.6) (-m MFP -T 8 -B 1000) 60 , 61 with a maximum-likelihood approach.
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: IQ-TREE 152 v.2.2.0.3 was used to generate phylogenetic trees of protein sequences, using the ultrafast bootstrap approximation option and 1,000 iterations.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Evidence: We used IQ-TREE multicore (v.2.2.0.3) 64 with options -B 1000 -alrt 1000 --boot-trees --wbtl -m LG + G4 -mwopt --threads-max 24 -T AUTO to build an ML tree using the LG model 65 with 4 rate categories (LG + G4) with 1,000 ultrafast bootstraps 66 .
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Version used: **2.2.2.6**
- Evidence: Finally, the concatenated supermatrix was used to build the phylogeny with IQ-TREE v.2.2.2.6 (ref.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: Phylogenetic trees based on ML were conducted by IQ-TREE ( 78 ) with the JTT+F+R3 model and 1,000 bootstraps.
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### The evolution of social parasitism in <i>Formica</i> ants revealed by a global phylogeny. (PNAS 2021)

- DOI: 10.1073/pnas.2026029118 | PMCID: PMC8463886 | PMID: 34535549
- Evidence: To infer the maximum-likelihood phylogeny, we used ModelFinder ( 112 ) as implemented in IQ-TREE ( 113 ) to select the best model for each UCE locus under the Akaike information criterion (AICc).
- Full pipeline: alignment/mapping [R] -> stage not stated [IQ-TREE]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Version used: **1.6.5**
- Evidence: A FASTA file, concatenated of all SNP sites, was used to generate a maximum likelihood tree with 1,000 fast bootstrap replicates using IQ-TREE (v1.6.5) ( 42 ) with the option -m MFP+ASC to infer the best substitution model and account for ascertainment bias correction.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: We then generated a dendrogrammatic representation of the population’s structure in a maximum likelihood (ML) framework, using IQ-TREE ( 48 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Elucidation of an anaerobic pathway for metabolism of l-carnitine-derived γ-butyrobetaine to trimethylamine in human gut bacteria. (PNAS 2021)

- DOI: 10.1073/pnas.2101498118 | PMCID: PMC8364193 | PMID: 34362844
- Version used: **1.6.12**
- Evidence: A maximum-likelihood phylogenetic tree was constructed using IQ-TREE v1.6.12 ( 65 ) with the LG+F0+G12 model and visualized using FigTree v1.4.4 ( 66 ).
- Full pipeline: alignment/mapping [MAFFT v7.455] -> dimensionality reduction/clustering [MAFFT v7.455] -> differential/statistical testing [R v3.6, ggplot2] -> visualisation [IQ-TREE v1.6.12] -> stage not stated [Prokka]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: The SNP alignment was used to reconstruct a maximum-likelihood phylogenetic tree with IQ-TREE ( 82 ), using ModelFinder ( 83 ) (−m MFP, ModelFinder Plus as default behavior in IQ-TREE) to choose the appropriate substitution model.
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Ongoing global and regional adaptive evolution of SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2104241118 | PMCID: PMC8307621 | PMID: 34292871
- Evidence: Tree topology was iteratively established using both FastTree ( 82 ) and IQ-TREE ( 83 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Evidence: This concatenated amino acid alignment was then submitted to the W-IQ-TREE server ( 65 ) using default settings ( SI Appendix , SI Methods ) and the resulting maximum likelihood tree was visualized using the Interactive Tree Of Life (iTOL) v5 ( 66 ).
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### &lt;i&gt;Helicobacter pylori&lt;/i&gt;'s historical journey through Siberia and the Americas. (PNAS 2021)

- DOI: 10.1073/pnas.2015523118 | PMCID: PMC8237685 | PMID: 34161258
- Evidence: We therefore reconstructed a recombination-aware phylogeny by identifying and removing a variation that was assigned to a homologous recombination by Gubbins ( 35 ) and reconstructed maximum likelihood phylogenetic trees using the best substitution model for our dataset (K3P + ASC + R5) in IQ-TREE ( 62 ), with branch support determined by 1,000 μLtrafast bootstrap replicates ( 63 ).
- Full pipeline: structure determination [IQ-TREE]

### Evolution of bacterial steroid biosynthesis and its impact on eukaryogenesis. (PNAS 2021)

- DOI: 10.1073/pnas.2101276118 | PMCID: PMC8237579 | PMID: 34131078
- Version used: **2.1.06**
- Evidence: Phylogenetic trees were constructed by maximum likelihood inference using Randomized Axelerated Maximum Likelihood (RAxML) version 8.2.11 and IQ-TREE version 2.1.06 ( 48 ) and by Bayesian inference using MrBayes version 3.2.6 ( 49 ) and PhyloBayes version 4.1c ( 50 ) (see SI Appendix , Methods for details).
- Full pipeline: differential/statistical testing [IQ-TREE v2.1.06, MrBayes v3.2.6, RAxML]

### Phylogenomic and ecological analyses reveal the spatiotemporal evolution of global pines. (PNAS 2021)

- DOI: 10.1073/pnas.2022302118 | PMCID: PMC8157994 | PMID: 33941644
- Version used: **2.0**
- Evidence: For the concatenation analysis, the OGs were concatenated by FASconCAT-G (v.1.04) ( 68 ) and used for the maximum likelihood (ML) analysis by IQ-TREE v.2.0-rc1 ( 69 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> dimensionality reduction/clustering [phytools v0.7] -> stage not stated [IQ-TREE v2.0, R v3.6.2, ggplot2]

### An introgressed gene causes meiotic drive in <i>Neurospora sitophila</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2026605118 | PMCID: PMC8092558 | PMID: 33875604
- Evidence: Hits longer than 100 bp were extracted and a phylogeny was inferred using IQ-TREE ( 50 ).
- Full pipeline: alignment/mapping [Cufflinks] -> differential/statistical testing [RAxML] -> stage not stated [ADMIXTURE, BLAST, IQ-TREE]

### The cyanobacterium <i>Prochlorococcus</i> has divergent light-harvesting antennae and may have evolved in a low-oxygen ocean. (PNAS 2021)

- DOI: 10.1073/pnas.2025638118 | PMCID: PMC7980375 | PMID: 33707213
- Evidence: Maximum-likelihood phylogenetic and phylogenomic inferences were performed using IQ-TREE ( 52 ) version 1.6.12.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, IQ-TREE, SPAdes v3.5]

### Evolved increases in hemoglobin-oxygen affinity and the Bohr effect coincided with the aquatic specialization of penguins. (PNAS 2021)

- DOI: 10.1073/pnas.2023936118 | PMCID: PMC8020755 | PMID: 33753505
- Evidence: In brief, the best-fitting codon substitution model and initial tree search were estimated using IQ-TREE with the options -st CODON, -m TESTNEW, -allnni, and -bnni ( 43 , 44 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [IQ-TREE, PyMOL]

### The squalene route to C30 carotenoid biosynthesis and the origins of carotenoid biosynthetic pathways. (PNAS 2022)

- DOI: 10.1073/pnas.2210081119 | PMCID: PMC9907078 | PMID: 36534808
- Evidence: These final alignments were used for phylogenetic reconstructions using IQ-TREE ( 54 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE, MAFFT] -> structure determination [IQ-TREE] -> stage not stated [BLAST]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Evidence: The subsets identified by the SWSC-EN algorithm were then used as input to identify the best partitioning scheme using ModelFinder ( 89 ) as implemented in IQ-TREE multicore v2.0.6 ( 90 ).
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### FtsEX-independent control of RipA-mediated cell separation in <i>Corynebacteriales</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214599119 | PMCID: PMC9897464 | PMID: 36469781
- Version used: **2.0.6**
- Evidence: We used the maximum-likelihood phylogeny reconstruction tool IQ-TREE (v2.0.6) ( 49 ), with the LG + F + R7 model (–m MFP) and ultrafast bootstraps (–B 1000).
- Full pipeline: structure determination [IQ-TREE v2.0.6, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CCP4, ColabFold, HMMER]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Version used: **1.6.8**
- Evidence: The cleaned alignment was given to IQ-TREE v1.6.8 ( 95 , 96 ) to infer a maximum-likelihood tree with extended model selection (–m MFP) and 100 standard bootstrap pseudoreplicates.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Population dynamics of Baltic herring since the Viking Age revealed by ancient DNA and genomics. (PNAS 2022)

- DOI: 10.1073/pnas.2208703119 | PMCID: PMC9659336 | PMID: 36282902
- Version used: **1.6.12**
- Evidence: A maximum-likelihood phylogenetic tree was then built with IQ-TREE v1.6.12 ( 52 , 53 ) using the mitogenome dataset including all modern and ancient samples to verify that the archaeological samples are Atlantic or Baltic herring.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [GATK, IQ-TREE v1.6.12, VCFtools v0.1.16]

### Pan-mitogenomics reveals the genetic basis of cytonuclear conflicts in citrus hybridization, domestication, and diversification. (PNAS 2022)

- DOI: 10.1073/pnas.2206076119 | PMCID: PMC9618123 | PMID: 36260744
- Version used: **2.0**
- Evidence: The LD pruned dataset (∼0.225 million variations) was used to construct the nuclear phylogenetic tree in IQ-TREE version 2.0 with 1,000 μLtrafast bootstrap replicates that yield support values for each node with the GTR + I+G model ( 61 ).
- Full pipeline: dimensionality reduction/clustering [PLINK v1.90b, R] -> differential/statistical testing [Python, ggplot2] -> visualisation [PLINK v1.90b, R, ggplot2] -> stage not stated [GEMMA v0.98.5, IQ-TREE v2.0, SnpEff v5.1]

### Marine viral particles reveal an expansive repertoire of phage-parasitizing mobile elements. (PNAS 2022)

- DOI: 10.1073/pnas.2212722119 | PMCID: PMC9618062 | PMID: 36256808
- Evidence: Trees were inferred from MSAs using IQ-TREE ( 64 ) with the partitioned LG + GAMMA model ( 65 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [HMMER, IQ-TREE, Medaka, R v9.4, eggNOG, minimap2]

### Deep-branching acetogens in serpentinized subsurface fluids of Oman. (PNAS 2022)

- DOI: 10.1073/pnas.2206845119 | PMCID: PMC9586279 | PMID: 36215489
- Version used: **1.6.11**
- Evidence: The concatenated alignment was then subjected to maximum likelihood (ML) phylogenetic analysis using IQ-TREE (v.1.6.11) ( 48 ) after identifying the optimal amino acid substitution model (LG+F+I+R4) among 168 possible models via the Bayesian information criterion, as implemented in the model testing “TEST” function of IQ-TREE.
- Full pipeline: read trimming [Clustal Omega v1.2.4] -> alignment/mapping [BLAST, Bowtie2, Clustal Omega v1.2.4, IQ-TREE v1.6.11] -> quantification [Bowtie2] -> differential/statistical testing [IQ-TREE v1.6.11] -> stage not stated [Prokka v1.14.5]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Evidence: All maximum-likelihood (ML) analyses were conducted with IQ-TREE (versions 1.7.8 and 2.0.4), with branch support calculated from 1,000 iterations of the ultrafast bootstrap algorithm ( 75 – 78 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### The durability of natural infection and vaccine-induced immunity against future infection by SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2204336119 | PMCID: PMC9351502 | PMID: 35858382
- Version used: **2.0.6**
- Evidence: We analyzed the concatenated alignment of the S , M , and ORF1b genes to reconstruct maximum-likelihood molecular phylogenies using IQ-TREE v2.0.6 ( 24 ) and RAxML v7.2.8 ( 25 ), with 1,000 nonparametric bootstrap replicates to assess node support.
- Full pipeline: alignment/mapping [IQ-TREE v2.0.6, RAxML v7.2.8] -> normalisation [TreeTime v0.7.6] -> structure determination [IQ-TREE v2.0.6, RAxML v7.2.8]

### The impact of paleoclimatic changes on body size evolution in marine fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2122486119 | PMCID: PMC9308125 | PMID: 35858316
- Version used: **1.6.12**
- Evidence: We inferred phylogenetic trees and associated support values in an ML framework in IQTREE v.1.6.12 ( 71 ) ( Dataset S4 ).
- Full pipeline: alignment/mapping [phytools] -> structure determination [phytools] -> stage not stated [IQ-TREE v1.6.12, MrBayes v3.2.7a, R v4.0.2]

### A genetically linked pair of NLR immune receptors shows contrasting patterns of evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2116896119 | PMCID: PMC9271155 | PMID: 35771942
- Version used: **2.0.3**
- Evidence: A maximum-likelihood tree was constructed with IQ-TREE v2.0.3 ( 77 ) using 1,000 ultrafast bootstrap replicates ( 78 ).
- Full pipeline: stage not stated [BWA, IQ-TREE v2.0.3, ImageJ, Medaka]

### Anti-bat ultrasound production in moths is globally and phylogenetically widespread. (PNAS 2022)

- DOI: 10.1073/pnas.2117485119 | PMCID: PMC9231501 | PMID: 35704762
- Version used: **1.6.2**
- Evidence: ( 12 ), and a maximum-likelihood analysis was performed in IQ-TREE v.1.6.2 ( 73 ), using ModelFinder to determine the best-fit substitution models for each partition ( 74 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, R] -> dimensionality reduction/clustering [UMAP] -> structure determination [R] -> stage not stated [IQ-TREE v1.6.2, scikit-learn]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Evidence: 7; parameter: ‘linsi’), and the phylogenetic trees were reconstructed in IQTREE ( 80 ) (ver.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **1.6.12**
- Evidence: The combined set of all HLI/Hli sequences was aligned using MAFFT (v7.453; --localpair --maxiterate 1000), and a maximum-likelihood phylogenetic tree was inferred using IQ-TREE (v1.6.12; -m MFP -bb 2000 -alrt 2000 -bnni) ( 54 ), allowing the program to choose the best evolutionary model for the alignment ( 55 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### Human pathogenic RNA viruses establish noncompeting lineages by occupying independent niches. (PNAS 2022)

- DOI: 10.1073/pnas.2121335119 | PMCID: PMC9191635 | PMID: 35639694
- Evidence: With the exception of SARS-CoV-2 and H3N2, tree topology was optimized using IQ-TREE ( 27 ) with the evolutionary model fixed to GTR+F+G4 and the minimum branch length decreased from the default 10e-6 to 10e-7 (options: -m GTR+F+G4 -st DNA -blmin 0.0000001).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE]

### Revisiting the recombinant history of HIV-1 group M with dynamic network community detection. (PNAS 2022)

- DOI: 10.1073/pnas.2108815119 | PMCID: PMC9171507 | PMID: 35500121
- Version used: **1.3.11.1**
- Evidence: From this alignment, we used IQ-TREE (version 1.3.11.1) ( 54 ) to reconstruct a maximum-likelihood tree relating the subtype reference sequences used in the previous method.
- Full pipeline: alignment/mapping [IQ-TREE v1.3.11.1, R] -> structure determination [IQ-TREE v1.3.11.1] -> stage not stated [Python, igraph]

### A novel regulatory gene promotes novel cell fate by suppressing ancestral fate in the sea anemone <i>Nematostella vectensis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2113701119 | PMCID: PMC9172639 | PMID: 35500123
- Evidence: To generate the phylogeny, we first used the model-finder function (-MF) with IQTREE to determine the best substitution model (VT+R8) and then generated a single tree and applied 500 bootstraps using fast bootstrapping.
- Full pipeline: differential/statistical testing [R] -> stage not stated [IQ-TREE]

### Species divergence in gut-restricted bacteria of social bees. (PNAS 2022)

- DOI: 10.1073/pnas.2115013119 | PMCID: PMC9170019 | PMID: 35467987
- Evidence: We aligned and concatenated nucleotide sequences of core genes and constructed the phylogenetic trees using IQ-TREE ( 55 ).
- Full pipeline: alignment/mapping [IQ-TREE]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: With these selected samples, a maximum likelihood phylogeny was constructed using IQTREE ( 73 ) (version 1.6.10) with the general time reversible (GTR) model of evolution, taking into account the invariant sites, and with an ultrafast bootstrap ( 74 ) of 1,000 replicates.
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: Model prediction and tree creation were obtained using IQ-TREE ( 87 , 88 ) (bootstrap values with 1,000 replicates).
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Diverse methylotrophic methanogenic archaea cause high methane emissions from seagrass meadows. (PNAS 2022)

- DOI: 10.1073/pnas.2106628119 | PMCID: PMC8892325 | PMID: 35165204
- Evidence: A Maximum likelihood tree from 214 McrA protein sequences was calculated with IQ-TREE multicore version 1.6.11 ( 75 ) using model LG+F+I+G4 and 1,000 bootstrap iterations.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [MAFFT] -> stage not stated [HMMER, IQ-TREE, QGIS, SPAdes]

### Auxin methylation by <i>IAMT1</i>, duplicated in the legume lineage, promotes root nodule development in <i>Lotus japonicus</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116549119 | PMCID: PMC8915983 | PMID: 35235457
- Evidence: Phylogenetic trees were estimated by the maximum-likelihood method and constructed using the trimmed amino acid sequence and IQ-TREE ( 62 ).
- Full pipeline: read trimming [IQ-TREE]

### A widely distributed phosphate-insensitive phosphatase presents a route for rapid organophosphorus remineralization in the biosphere. (PNAS 2022)

- DOI: 10.1073/pnas.2118122119 | PMCID: PMC8812569 | PMID: 35082153
- Evidence: Tree topology and branch lengths were calculated by maximum likelihood using the Blosum62+F+G4 model of evolution for amino acid sequences based on 875 sites (595 parsimony informative) in IQ-TREE software.
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [BLAST] -> differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [HMMER, IQ-TREE]

### A peptide toxin in ant venom mimics vertebrate EGF-like hormones to cause long-lasting hypersensitivity in mammals. (PNAS 2022)

- DOI: 10.1073/pnas.2112630119 | PMCID: PMC8851504 | PMID: 35131940
- Version used: **2.0.6**
- Evidence: We selected the most appropriate evolutionary model (JTTDCMut+G4) using ModelFinder ( 51 ) before we used IQ-TREE v2.0.6 ( 52 ) to reconstruct the molecular phylogeny by maximum likelihood, estimating branch support values by ultrafast bootstrap using 10,000 replicates ( 53 ).
- Full pipeline: alignment/mapping [MAFFT v7.304b, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE v2.0.6] -> stage not stated [BLAST]

### Template switching in DNA replication can create and maintain RNA hairpins. (PNAS 2022)

- DOI: 10.1073/pnas.2107005119 | PMCID: PMC8794818 | PMID: 35046021
- Version used: **1.6.1**
- Evidence: ML trees were computed with IQ-TREE (version 1.6.1) ( 50 ) using automated model selection ( 51 ) and tree finder, and resulting trees were midpoint rooted using the ete3 python library ( 52 ).
- Full pipeline: read trimming [MAFFT v7.310] -> alignment/mapping [BLAST v2.6.0, MAFFT v7.310] -> dimensionality reduction/clustering [MAFFT v7.310] -> visualisation [R, ggplot2] -> stage not stated [IQ-TREE v1.6.1]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: Maximum likelihood reconstruction was performed with IQ-TREE ( 99 ) based on a concatenation approach with edge-linked partition model and 1,000 ultrafast bootstrap replicates (git 19.7).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **1.6.12**
- Evidence: IQ-TREE v1.6.12 ( 76 ) was used to infer two phylogenetic trees from the concatenated alignments (the first including all capsulated strains and the second including only E. coli strains, both with the E. cloacae outgroup) with best evolutionary model selection and 1,000 ultrafast bootstrap.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### &lt;i&gt;GRASSY TILLERS1&lt;/i&gt; (&lt;i&gt;GT1&lt;/i&gt;) and &lt;i&gt;SIX-ROWED SPIKE1&lt;/i&gt; (&lt;i&gt;VRS1&lt;/i&gt;) homologs share conserved roles in growth repression. (PNAS 2023)

- DOI: 10.1073/pnas.2311961120 | PMCID: PMC10742383 | PMID: 38096411
- Evidence: A model selection test was performed, and a tree was constructed in IQ-TREE 2 ( 67 ) and visualized using the R package ggtree ( 68 ).
- Full pipeline: read trimming [STAR v2.7.9a, Trimmomatic] -> alignment/mapping [HTSeq, MAFFT, STAR v2.7.9a, Trimmomatic] -> differential/statistical testing [DESeq2] -> visualisation [IQ-TREE, R]

### Massive intein content in &lt;i&gt;Anaeramoeba&lt;/i&gt; reveals aspects of intein mobility in eukaryotes. (PNAS 2023)

- DOI: 10.1073/pnas.2306381120 | PMCID: PMC10710043 | PMID: 38019867
- Evidence: Unless specified otherwise, intein sequences were aligned with mafft ( 52 ) v7.407 using default parameters, sites were selected with bmge ( 53 ) v1.12 with the -m BLOSUM30 parameter, and IQ-TREE ( 54 ) v1.6.3 was used to reconstruct phylogenies with 1,000 ultrafast bootstrap replicates ( 55 ) under the C20+G4 mixture model.
- Full pipeline: alignment/mapping [IQ-TREE, MUSCLE] -> structure determination [IQ-TREE] -> visualisation [Cytoscape] -> stage not stated [BLAST]

### Evidence for an ancient aquatic origin of the RNA viral order &lt;i&gt;Articulavirales&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2310529120 | PMCID: PMC10636315 | PMID: 37906647
- Version used: **1.6.12**
- Evidence: In this case, sequences were aligned in MAFFT v7.490 ( 33 ), and the phylogenetic tree was inferred using the maximum likelihood approach in IQ-TREE v1.6.12 ( 31 ) with ModelFinder, which selected LG+F+R10 as the best-fit model.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.490, MUSCLE v5.1] -> quantification [RSEM v1.3.0] -> visualisation [R v4.1] -> stage not stated [BLAST v2.0.9]

### Scattered differentiation of unlinked loci across the genome underlines ecological divergence of the selfing grass &lt;i&gt;Brachypodium stacei&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2304848120 | PMCID: PMC10636366 | PMID: 37903254
- Version used: **1.6.12**
- Evidence: Phylogeny trees were constructed with IQ-TREE (v 1.6.12).
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BUSCO, HISAT2, IQ-TREE v1.6.12]

### Diversity of rhodopsin cyclases in zoospore-forming fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2310600120 | PMCID: PMC10622942 | PMID: 37871207
- Evidence: ...Cs from Q. haematococci ), aligned with Mafft and trimmed using TrimAI (-gt 0.95) ( 25 ), and the maximum likelihood (ML) tree was obtained using the IQ-TREE web server ( http://iqtree.cibiv.univie.ac.at/ ) under the LG+F+R6 substitution model derived from the automatic model finding option ( 26 ) with 1,000 ultrafast bootstrap replicates.
- Full pipeline: read trimming [IQ-TREE, SPAdes v3.15.5] -> alignment/mapping [IQ-TREE] -> simulation/modelling [GROMACS v2019.3] -> visualisation [Matplotlib v3.4.3, PyMOL v2.4.1] -> stage not stated [AlphaFold, MDAnalysis v2.4.3]

### Identification of a carbonic anhydrase-Rubisco complex within the alpha-carboxysome. (PNAS 2023)

- DOI: 10.1073/pnas.2308600120 | PMCID: PMC10614612 | PMID: 37862384
- Evidence: Tree was built using IQ-TREE web server ( 54 ) and visualized using iTOL ( 55 ).
- Full pipeline: alignment/mapping [MUSCLE, RELION v3.1] -> quantification [ImageJ] -> registration [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, IQ-TREE, PyMOL] -> stage not stated [CTFFIND v4.1]

### Reinventing metabolic pathways: Independent evolution of benzoxazinoids in flowering plants. (PNAS 2023)

- DOI: 10.1073/pnas.2307981120 | PMCID: PMC10589660 | PMID: 37812727
- Evidence: The resulting alignments were used to infer Maximul Likelihood phylogenies using IQ-TREE web server ( http://iqtree.cibiv.univie.ac.at/ ) ( 58 ) with automatic substitution model and bootstrap value of 1,000.
- Full pipeline: alignment/mapping [IQ-TREE] -> differential/statistical testing [IQ-TREE]

### Changes in parrot diversity after human arrival to the Caribbean. (PNAS 2023)

- DOI: 10.1073/pnas.2301128120 | PMCID: PMC10576146 | PMID: 37748079
- Version used: **2.1.2**
- Evidence: To assess extant species relationships, IQTREE 2.1.2 ( 82 ) was used to obtain a phylogeny from the 42-sample ( Amazona taxa, Graydidascalus brachyurus , Alipiopsitta xanthops , SI Appendix , Table S3 ) concatenated UCE alignment with 1,000 rapid bootstrap replicates.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BWA v0.7.13, IQ-TREE v2.1.2, SAMtools v1.10] -> stage not stated [BCFtools v1.12, MAFFT v7.455, R v4.1]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Evidence: For IQ-TREE analyses, the best-fitting partition model found by ModelFinder ( 89 ) and the LG+C60+F+G model were used.
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **2.1.3**
- Evidence: A maximum likelihood tree was constructed using a concatenation with gene-based partitioning approach in IQ-TREE v2.1.3 ( 74 ) with 1,000 ultrafast bootstraps replicates, and a gene-based coalescence tree was obtained with ASTRAL-MP v5.15.2 ( 75 ).
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### Origin of the OAS-RNase L innate immune pathway before the rise of jawed vertebrates via molecular tinkering. (PNAS 2023)

- DOI: 10.1073/pnas.2304687120 | PMCID: PMC10400998 | PMID: 37487089
- Version used: **2.0**
- Evidence: Phylogenetic analyses of OAS homologs and RNase L homologs were performed based on NTase domains and full-length RNase L homologs, respectively, using a maximum likelihood method implemented in IQ-TREE (v2.0) ( 52 ).
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> structure determination [MAFFT] -> stage not stated [AlphaFold, HMMER, IQ-TREE v2.0]

### Predicting the effect of mutations to investigate recent events of selection across 60,472 <i>Escherichia coli</i> strains. (PNAS 2023)

- DOI: 10.1073/pnas.2304177120 | PMCID: PMC10401003 | PMID: 37487088
- Version used: **2.0.3**
- Evidence: Ancestral states were inferred using IQ-TREE v.2.0.3 ( 50 ) with a codon GY model ( 51 ).
- Full pipeline: stage not stated [IQ-TREE v2.0.3, Prokka v1.13.3]

### Genomic and geographical structure of human cytomegalovirus. (PNAS 2023)

- DOI: 10.1073/pnas.2221797120 | PMCID: PMC10372631 | PMID: 37459519
- Evidence: 2 were constructed from nucleic acid sequences in IQ-TREE ( 87 ).
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> registration [MAFFT, MUSCLE] -> stage not stated [IQ-TREE, Python, R]

### A periplasmic phospholipase that maintains outer membrane lipid asymmetry in <i>Pseudomonas aeruginosa</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302546120 | PMCID: PMC10374164 | PMID: 37463202
- Version used: **1.6.12**
- Evidence: The maximum-likelihood tree was generated in IQ-TREE v1.6.12 using the best-fit model LG+F+I+G4 ( 76 , 77 ).
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.490, PyMOL] -> stage not stated [AlphaFold, IQ-TREE v1.6.12]

### Cambrian lobopodians shed light on the origin of the tardigrade body plan. (PNAS 2023)

- DOI: 10.1073/pnas.2211251120 | PMCID: PMC10334802 | PMID: 37399417
- Evidence: The maximum likelihood tree search was conducted in IQ-TREE ( 58 ) using the MK model (Jukes-Cantor type model for morphological data), and support was assessed using the ultrafast phylogenetic bootstrap replication method from 10,000 replicates ( 59 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.6] -> stage not stated [IQ-TREE]

### Phase variation as a major mechanism of adaptation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301394120 | PMCID: PMC10334774 | PMID: 37399390
- Evidence: We constructed the phylogenetic trees with IQ-TREE ( 63 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BCFtools, GEMMA, IQ-TREE, Picard, Pilon, SAMtools]

### Replitrons: A major group of eukaryotic transposons encoding HUH endonuclease. (PNAS 2023)

- DOI: 10.1073/pnas.2301424120 | PMCID: PMC10288648 | PMID: 37307447
- Version used: **2.0.3**
- Evidence: A maximum likelihood phylogeny was produced using IQ-TREE v2.0.3 ( 72 ), performed with model selection (-MFP) ( 73 ) and ultrafast bootstrapping (-bb 1000) ( 74 ).
- Full pipeline: alignment/mapping [MAFFT v7.471] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BEDTools, IQ-TREE v2.0.3]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Version used: **1.6.12**
- Evidence: A recombination-free SNP alignment generated by Gubbins was then used to build a phylogeny for each subspecies using IQ-TREE v1.6.12 ( 45 ), using the ModelFinder Plus (-mfp) option and 1,000 bootstrap replicates.
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Vertebrate-tropism of a cressdnavirus lineage implicated by poxvirus gene capture. (PNAS 2023)

- DOI: 10.1073/pnas.2303844120 | PMCID: PMC10193959 | PMID: 37155884
- Version used: **2.2.0**
- Evidence: For phylogenetic analyses, regions of apvRep proteins gained by gene fusion were manually trimmed prior to alignment with cressdnavirus references using MAFFT v7.487 ( 74 ), and analysis with IQ-TREE v2.2.0 ( 75 ).
- Full pipeline: read trimming [IQ-TREE v2.2.0, MAFFT v7.487] -> alignment/mapping [AlphaFold v2.1.1, BEDTools, BLAST v2.0.15, IQ-TREE v2.2.0, MAFFT v7.487] -> visualisation [AlphaFold v2.1.1]

### The cell envelope of <i>Thermotogae</i> suggests a mechanism for outer membrane biogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2303275120 | PMCID: PMC10160955 | PMID: 37094164
- Version used: **2.1.4**
- Evidence: The tree was constructed using IQ-TREE v2.1.4 with 1,000 ultrafast bootstraps and the substitution model LG+F+R6, as determined by ModelFinder ( 71 , 72 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [AlphaFold, ChimeraX, HMMER, IQ-TREE v2.1.4, ImageJ, RoseTTAFold]

### Genomic and structural basis for evolution of tropane alkaloid biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2302448120 | PMCID: PMC10151470 | PMID: 37068250
- Evidence: The resulting sequences were used to construct the maximum likelihood tree by IQ-TREE ( 40 ) using the best-fit model JTT+F+R4 according to BIC.
- Full pipeline: alignment/mapping [BUSCO, MAFFT] -> dimensionality reduction/clustering [OrthoFinder] -> visualisation [PyMOL v2.4] -> stage not stated [AlphaFold, AutoDock Vina v1.1.2, IQ-TREE]

### Genetic factors predict hybrid formation in the British flora. (PNAS 2023)

- DOI: 10.1073/pnas.2220261120 | PMCID: PMC10120012 | PMID: 37040419
- Evidence: Phylogenetic inferences were made using IQ-TREE ( 45 ) in an analysis with three partitions allowing models of molecular evolution to differ between loci and including a multifurcating constraint tree based on Angiosperm Phylogeny Group IV relationships ( 46 ) generated with Phylomatic ( 47 ).
- Full pipeline: visualisation [R] -> stage not stated [IQ-TREE, Python, data.table, ggplot2, tidyverse]

### Evolution of insect innate immunity through domestication of bacterial toxins. (PNAS 2023)

- DOI: 10.1073/pnas.2218334120 | PMCID: PMC10120054 | PMID: 37036995
- Evidence: Sequences were aligned in MAFFT v7.450 ( 40 , 41 ), and protein topologies were inferred using maximum likelihood as implemented in W-IQ-TREE ( http://iqtree.cibiv.univie.ac.at/ ) ( 42 ) using the best-fit model as assessed by BIC in ModelFinder.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.450] -> stage not stated [AlphaFold v2.1.0]

### Phylogeographic reconstruction of the emergence and spread of Powassan virus in the northeastern United States. (PNAS 2023)

- DOI: 10.1073/pnas.2218012120 | PMCID: PMC10120011 | PMID: 37040418
- Version used: **1.6.12**
- Evidence: We sequenced 279 Powassan virus genomes and estimated a maximum-likelihood tree using IQ-TREE version 1.6.12 with ultrafast bootstrap approximation (1,000 replicates) ( 58 ) to determine phylogenetic relationships between publicly available and newly sequenced Lineage I and II genomes.
- Full pipeline: alignment/mapping [Bowtie2] -> visualisation [Nextstrain] -> stage not stated [IQ-TREE v1.6.12, R]

### Bacterial origin of a key innovation in the evolution of the vertebrate eye. (PNAS 2023)

- DOI: 10.1073/pnas.2214815120 | PMCID: PMC10120077 | PMID: 37036996
- Evidence: Maximum likelihood phylogenetic analyses were performed using IQ-TREE ( 40 ) or RAxML ( 41 ) as indicated in Table 1 and Dataset S5 .
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, BLAST, IQ-TREE, RAxML]

### <i>Starships</i> are active eukaryotic transposable elements mobilized by a new family of tyrosine recombinases. (PNAS 2023)

- DOI: 10.1073/pnas.2214521120 | PMCID: PMC10104507 | PMID: 37023132
- Version used: **2.0.3**
- Evidence: The phylogeny was constructed using IQ-TREE version 2.0.3 with automatic model selection (JTT+R5) and 1,000 ultrafast bootstraps.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega, MAFFT, MrBayes] -> differential/statistical testing [Clustal Omega, MrBayes] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.0.3]

### Euglenozoan kleptoplasty illuminates the early evolution of photoendosymbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2220100120 | PMCID: PMC10041101 | PMID: 36927158
- Evidence: Maximum likelihood (ML) trees were constructed for the remaining 179 protein alignments using the IQ-TREE software v1.6.12 ( 58 ), with the evolution model automatically selected with the -m TEST parameter, and statistical support from 1,000 rapid bootstrapping replicates ( 59 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [IQ-TREE, MAFFT] -> differential/statistical testing [IQ-TREE] -> stage not stated [BUSCO, SPAdes v3.10.1]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **2.0**
- Evidence: We used IQ-TREE (2.0-rc1, TVMe+R3) ( 101 ), to construct the phylogenomic tree, and ran bootstrapping for 100 times.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Version used: **2.0.3**
- Evidence: Phylogenetic analyses of leggt and lecsl genes or Pfam domains were performed using IQ-TREE v2.0.3 (-B 1000) ( 35 ) following aligning with MAFFT v7.487 (--auto) ( 62 ) and trimming using ClipKIT v1.3.0 ( 63 ).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **2.2.0.3**
- Evidence: These single-copy gene protein sequences were aligned using MAFFT v7.475, alignments trimmed by TrimAl v1.4.rev15, and used to infer a phylogenomic species tree using IQ-TREE v2.2.0.3.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### White-tailed deer (<i>Odocoileus virginianus</i>) may serve as a wildlife reservoir for nearly extinct SARS-CoV-2 variants of concern. (PNAS 2023)

- DOI: 10.1073/pnas.2215067120 | PMCID: PMC9963525 | PMID: 36719912
- Evidence: Briefly, multiple sequence alignment was performed using Nextalign; maximum likelihood tree was inferred using IQ-TREE through Augur tool kit and data visualization through Auspice.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.453, QGIS] -> dimensionality reduction/clustering [QGIS] -> visualisation [IQ-TREE, QGIS] -> stage not stated [Nextstrain, Pangolin v4.0.6]

### Emergent collective behavior evolves more rapidly than individual behavior among acorn ant species. (PNAS 2024)

- DOI: 10.1073/pnas.2420078121 | PMCID: PMC11621464 | PMID: 39576350
- Version used: **2.1.2**
- Evidence: We used the resulting datablocks as input for partitioning in IQTREE v2.1.2 ( 66 ), using the command -m TESTNEWMERGEONLY.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R] -> stage not stated [IQ-TREE v2.1.2, phytools]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Evidence: Maximum likelihood trees were inferred with 1,000 ultrafast bootstraps in IQ-TREE 2 under the best-performing model inferred by ModelFinder using BIC ( 67 – 69 ) including a selection of mixture models (C10, C20, C40, and C60).
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### The origin of methyl group in methanogen-mediated mercury methylation: From the Wolfe cycle. (PNAS 2024)

- DOI: 10.1073/pnas.2416761121 | PMCID: PMC11494345 | PMID: 39382993
- Evidence: Maximum-likelihood trees were constructed with IQ-TREE ( 55 ) using the following command: “-m LG+C60+F+G, -bb 1000” and edited using iTOL ( 56 ).
- Full pipeline: stage not stated [IQ-TREE]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Version used: **1.6.12**
- Evidence: Afterward, we constructed a ML phylogeny for the giant panda individuals using IQ-TREE (v1.6.12) ( 68 ) with the recommended nucleotide substitution model “GTR+F+G4” calculated by jModelTest (v2.1.10) ( 69 ).
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **1.6.12**
- Evidence: All phylogenetic trees were inferred using the maximum likelihood method available in IQ-TREE v1.6.12 ( 71 ) with 1,000 ultrafast bootstraps.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Amoebozoan testate amoebae illuminate the diversity of heterotrophs and the complexity of ecosystems throughout geological time. (PNAS 2024)

- DOI: 10.1073/pnas.2319628121 | PMCID: PMC11287125 | PMID: 39012821
- Evidence: We assessed the topological support for the resulting tree by 100 Real nonparametric Bootstrap replicates in IQ-TREE (IQ-TREE v.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RAxML v8.2.12] -> stage not stated [BUSCO v5.3.2, IQ-TREE]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Evidence: We used the TN93 substitution model, which was the best-fitting model according to the Bayesian Information Criterion in ModelFinder ( 92 ) as implemented in IQTREE ( 93 ) v1.6.2.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### Illuminating the coevolution of photosynthesis and Bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322120121 | PMCID: PMC11194577 | PMID: 38875151
- Version used: **2.1.3**
- Evidence: ...ufA, and 0.6 for PRK and the RuBisCO large subunit), and the final alignment was used as the input maximum-likelihood estimation of the phylogeny via IQ-TREE v2.1.3 with one of the C10 to C60 profile mixture models (LG+CX0+G+F) estimated as optimal by ModelFinder ( 96 – 99 ) (see figure captions for details).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE v2.1.3, MAFFT] -> stage not stated [AlphaFold, BEAST v2.6.6, Prokka v1.14]

### Natural variation of immune epitopes reveals intrabacterial antagonism. (PNAS 2024)

- DOI: 10.1073/pnas.2319499121 | PMCID: PMC11161748 | PMID: 38814867
- Evidence: Phylogenetic trees for bacteria relatedness were built using GToTree, and protein trees were built using MAFFT for sequence alignment and IQ-TREE tree building.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT]

### Premeiotic 24-nt phasiRNAs are present in the <i>Zea</i> genus and unique in biogenesis mechanism and molecular function. (PNAS 2024)

- DOI: 10.1073/pnas.2402285121 | PMCID: PMC11127045 | PMID: 38739785
- Version used: **2.2.0.3**
- Evidence: The resulting sequences were aligned using MUSCLE ( 43 ), and phylogenetic trees were built using IQ-TREE v2.2.0.3 ( 44 ) to assign/curate names of MIR2118 and MIR2275 loci based on orthology.
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MUSCLE, edgeR v4.0.2, featureCounts v1.6.3] -> normalisation [edgeR v4.0.2, featureCounts v1.6.3] -> stage not stated [BEDTools v2.29.2, StringTie v2.1.7]

### A distinct, high-affinity, alkaline phosphatase facilitates occupation of P-depleted environments by marine picocyanobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2312892121 | PMCID: PMC11098088 | PMID: 38713622
- Version used: **1.6.3**
- Evidence: The final alignment was used to build the phylogenetic tree using IQTREE v 1.6.3 ( 87 ), using ModelFinder ( 88 ) to select the best phylogenetic model for these data.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.3, MUSCLE v3.8.31] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, HMMER, SciPy v1.10.1]

### Frequent nonhomologous replacement of replicative helicase loaders by viruses in <i>Vibrionaceae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2317954121 | PMCID: PMC11087808 | PMID: 38683976
- Evidence: The alignments were curated using trimAl version 1.2 ( 80 ) with the option “-gappyout.” The maximum-likelihood trees were inferred using IQ-TREE with option -m MFP and -bb 1000 ( 81 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.212] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, eggNOG]

### What one genus of showy moths can say about migration, adaptation, and wing pattern. (PNAS 2024)

- DOI: 10.1073/pnas.2319726121 | PMCID: PMC11047066 | PMID: 38630713
- Version used: **1.6.12**
- Evidence: Sequences of the identified FMOs were aligned with MAFFT ( 56 ) and provided to IQ-TREE (v1.6.12) ( 57 ) for phylogeny inference.
- Full pipeline: alignment/mapping [AlphaFold, BUSCO, HMMER, IQ-TREE v1.6.12, MAFFT] -> stage not stated [scikit-learn]

### Subgenome-aware analyses reveal the genomic consequences of ancient allopolyploid hybridizations throughout the cotton family. (PNAS 2024)

- DOI: 10.1073/pnas.2313921121 | PMCID: PMC11009661 | PMID: 38568968
- Evidence: Then, the hierarchical gene lists were used to infer maximum likelihood (ML) trees using IQ-TREE ( 43 ) through WGDI with the parameter “-at.” Finally, we used ASTRAL-III v.5.7.8 ( 44 ) with the parameter “-t 16” and ASTRAL-Pro 2 ( 45 ) with the parameter “-u 3” to construct the coalescent tree and estimate branch support.
- Full pipeline: stage not stated [BUSCO, IQ-TREE]

### Fluorescent proteins generate a genetic color polymorphism and counteract oxidative stress in intertidal sea anemones. (PNAS 2024)

- DOI: 10.1073/pnas.2317017121 | PMCID: PMC10945830 | PMID: 38457522
- Version used: **1.6.1**
- Evidence: Maximum likelihood trees were inferred using IQ-TREE version 1.6.1 ( 83 ): We first used ModelFinder ( 84 ) for model selection, and resulting IQ-TREE tree outputs were then bootstrapped with 1,000 replicates using UFBoot2 ( 85 ).
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [MUSCLE] -> quantification [ImageJ] -> stage not stated [AlphaFold, IQ-TREE v1.6.1, PyMOL v2.4.0]

### The structure of PSI-LHCI from <i>Cyanidium caldarium</i> provides evolutionary insights into conservation and diversity of red-lineage LHCs. (PNAS 2024)

- DOI: 10.1073/pnas.2319658121 | PMCID: PMC10945839 | PMID: 38442179
- Evidence: S12 were inferred using IQ-TREE 2 ( 37 ) with the model selected by ModelFinder ( 38 ).
- Full pipeline: stage not stated [IQ-TREE, Topaz v0.2.4, UCSF Chimera]

### Rubisco is evolving for improved catalytic efficiency and CO<sub>2</sub> assimilation in plants. (PNAS 2024)

- DOI: 10.1073/pnas.2321050121 | PMCID: PMC10945770 | PMID: 38442173
- Evidence: Maximum-likelihood rbcL /RbcL and rbcS /RbcS phylogenetic gene trees were inferred across all sequences within a taxonomic group by IQ-TREE ( 127 ) using the ultrafast bootstrapping method with 1,000 replicates and the Shimodaira–Hasegawa approximate–likelihood ratio branch test.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE, OrthoFinder]

### Global diversity of enterococci and description of 18 previously unknown species. (PNAS 2024)

- DOI: 10.1073/pnas.2310852121 | PMCID: PMC10927581 | PMID: 38416678
- Version used: **1.7**
- Evidence: ... ), converted this alignment to a codon-based alignment using PAL2NAL v14 ( 70 ), and then used this alignment to construct a phylogenetic tree using IQ-TREE (v1.7-beta9) ( 71 ) with 1,000 bootstrap replicates, an edge-proportional partition model, and using ModelFinder Plus to find the best codon model for each gene.
- Full pipeline: alignment/mapping [IQ-TREE v1.7, MAFFT, Pilon v1.23] -> dimensionality reduction/clustering [HMMER, OrthoFinder v2.3.3]

### Pyrenoid proteomics reveals independent evolution of the CO<sub>2</sub>-concentrating organelle in chlorarachniophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2318542121 | PMCID: PMC10927497 | PMID: 38408230
- Version used: **2.2.0**
- Evidence: The tree was generated under the LG+R5 model implemented in IQ-TREE version 2.2.0.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Evidence: We inferred maximum-likelihood phylogenies for plastomes, each nuclear locus, and concatenated nuclear genes using IQ-TREE ( 92 ) with 100 bootstrap replicates, implemented with ModelFinder ( 93 ) to select appropriate models of nucleotide substitution.
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Evidence: Left : Phylogenomic tree of Psilocybe estimated from a gene-partitioned concatenated supermatrix of 2,983 single-copy gene families estimated in IQ-TREE.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### Estimates of early outbreak-specific SARS-CoV-2 epidemiological parameters from genomic data. (PNAS 2024)

- DOI: 10.1073/pnas.2308125121 | PMCID: PMC10786264 | PMID: 38175864
- Evidence: We built a maximum-likelihood phylogenetic tree with IQ-TREE ( 35 ) using this alignment.
- Full pipeline: quality control [Nextstrain] -> alignment/mapping [BEAST, IQ-TREE, Nextstrain] -> differential/statistical testing [BEAST]

### Versatile NTP recognition and domain fusions expand the functional repertoire of the ParB-CTPase fold beyond chromosome segregation. (PNAS 2025)

- DOI: 10.1073/pnas.2527592122 | PMCID: PMC12704722 | PMID: 41343662
- Evidence: ParB homologs -TIGR00180- tree was built using IQ-TREE multicore version 2.2.5 (-alrt 1,000-nt AUTO -mem 32G -m TEST -s).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [AlphaFold, AutoDock Vina, Docker, HMMER v3.4, IQ-TREE]

### Genome of venomous caterpillar &lt;i&gt;Doratifera vulnerans&lt;/i&gt; reveals recruitment of immune peptides and their adaptation as pain-inducing toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2513640122 | PMCID: PMC12704794 | PMID: 41325521
- Evidence: D. vulnerans cecropin nucleotide and amino acid sequences were analyzed phylogenetically using the IQ-TREE 2 and PAML software packages ( 100 , 101 ).
- Full pipeline: stage not stated [IQ-TREE]

### A 120-y time series of genomes reveals the consequences of closed breeding in German Shepherd Dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421755122 | PMCID: PMC12684887 | PMID: 41284896
- Version used: **2.1.4**
- Evidence: We also constructed a maximum-likelihood phylogeny in IQ-TREE v.2.1.4 ( 64 ) using all Dog10K samples to determine the maternal affinities of historical GSDs ( SI Appendix , Fig.
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.5.3, SAMtools v1.9] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.1.4, PLINK v1.90b]

### The impacts of European arrival on Australian dingoes. (PNAS 2025)

- DOI: 10.1073/pnas.2421749122 | PMCID: PMC12684890 | PMID: 41284893
- Version used: **2.1.4**
- Evidence: We also constructed a maximum-likelihood phylogeny in IQ-TREE v.2.1.4 ( 77 ) using 33 modern and 18 high-coverage (7.7 to 276.2x) nonmodern mitochondrial genomes, alongside 165 publicly available sequences spanning the last ~13,000 y ( SI Appendix , Table S1 D ).
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [SAMtools v1.9] -> differential/statistical testing [ADMIXTURE v1.3.0] -> stage not stated [BCFtools v1.9, BEDTools, IQ-TREE v2.1.4, PLINK v1.90b, R, VCFtools]

### A legacy of genetic entanglement with wolves shapes modern dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421768122 | PMCID: PMC12684911 | PMID: 41284883
- Evidence: ( A ) Cartoon depictions of a mitochondrial phylogeny ( Left , n = 1,011) and a Y-chromosome phylogeny ( Right , n = 428 males) generated by IQ-TREE.
- Full pipeline: stage not stated [IQ-TREE]

### Structure and encapsulation of carbonic anhydrase within the α-carboxysome. (PNAS 2025)

- DOI: 10.1073/pnas.2523723122 | PMCID: PMC12646314 | PMID: 41223214
- Evidence: The resulting alignment file was submitted to W-IQ-TREE for inference of a phylogenetic tree by maximum likelihood ( 71 ).
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, Clustal Omega]

### When islands collide: Divergence predicts outcomes of secondary contact during the fusion of Sulawesi's paleo-archipelago. (PNAS 2025)

- DOI: 10.1073/pnas.2514344122 | PMCID: PMC12625910 | PMID: 41144686
- Version used: **2.1.1**
- Evidence: We estimated a maximum likelihood tree using IQTREE v2.1.1 ( 56 ) with automatic model selection and partition merging for each of the three codon positions ( 57 ).
- Full pipeline: stage not stated [IQ-TREE v2.1.1, RAxML v8.2.12, phytools v2.3]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Version used: **2.3.6**
- Evidence: We combined the final set of the B. franklini barcodes with a set of Bombus (subgenus Bombus ) barcodes downloaded from BOLD, aligned the sequences with MAFFT, and inferred a phylogenetic tree using IQTREE v2.3.6 ( 86 ), with a general time reversible model (GTR + G) and 1,000 ultrafast bootstrap replicates ( 87 ).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Apusomonad rhodopsins: A new family of ultraviolet to blue light-absorbing rhodopsin channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510619122 | PMCID: PMC12557545 | PMID: 41082663
- Version used: **1.6.11**
- Evidence: The trimmed alignment was taken to maximum likelihood phylogenetic reconstruction with IQ-TREE v.1.6.11 ( 94 ) under the LG+C60+F+R9 model as chosen per Bayesian information criterion.
- Full pipeline: read trimming [IQ-TREE v1.6.11, MAFFT] -> alignment/mapping [IQ-TREE v1.6.11, MAFFT] -> differential/statistical testing [IQ-TREE v1.6.11] -> structure determination [IQ-TREE v1.6.11] -> stage not stated [AlphaFold, BLAST, GROMACS v4.5.7]

### A nonenzymatic effector disrupts &lt;i&gt;Bacteroides&lt;/i&gt; cell wall homeostasis via OmpA targeting to mediate interbacterial competition. (PNAS 2025)

- DOI: 10.1073/pnas.2513207122 | PMCID: PMC12541434 | PMID: 41055976
- Evidence: A maximum-likelihood phylogenetic tree was constructed using IQTREE (Version 2.1.4_beta) with automatic model selection (1,000 bootstrap).
- Full pipeline: alignment/mapping [AlphaFold, BLAST, MAFFT] -> structure determination [AlphaFold] -> stage not stated [IQ-TREE]

### Phylogenomics redefines the evolutionary history of mosquitoes. (PNAS 2025)

- DOI: 10.1073/pnas.2519291122 | PMCID: PMC12557814 | PMID: 41052354
- Version used: **2.2**
- Evidence: ML phylogenetic inference was done with IQ-TREE v2.2 ( 69 ).
- Full pipeline: alignment/mapping [BUSCO] -> differential/statistical testing [R, ggplot2] -> stage not stated [BEAST, IQ-TREE v2.2, TreeTime]

### Transcriptional regulation of thorn tip sclerification in plants. (PNAS 2025)

- DOI: 10.1073/pnas.2510775122 | PMCID: PMC12501164 | PMID: 40986360
- Evidence: For phylogenetic analysis, we aligned MYB protein sequences using MAFFT, constructed a phylogenetic tree with IQTREE, and visualized it on the ITOL platform.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT] -> visualisation [IQ-TREE, MAFFT]

### Language models reveal a complex sequence basis for adaptive convergent evolution of protein functions. (PNAS 2025)

- DOI: 10.1073/pnas.2418254122 | PMCID: PMC12501123 | PMID: 40986350
- Version used: **2.2.5**
- Evidence: Phylogeny reconstructions in the three cases of individual genes and thermophilic prokaryotes were conducted by IQ-TREE 2.2.5 ( 78 ) under default settings and validated by Bayesian inference in the hemoglobin case.
- Full pipeline: alignment/mapping [MAFFT v7.505] -> differential/statistical testing [IQ-TREE v2.2.5] -> structure determination [IQ-TREE v2.2.5] -> stage not stated [BLAST, OrthoFinder v2.5.5, R]

### A widespread family of molecular chaperones promotes the intracellular stability of type VIIb secretion system-exported toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2503581122 | PMCID: PMC12478183 | PMID: 40953262
- Evidence: A maximum likelihood tree of amino acid sequences was constructed using IQTREE V2.1.4 ( 67 ), with 1,000 ultrafast bootstraps and visualized using FigTree V1.4.4 ( http://tree.bio.ed.ac.uk/software/figtree/ ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [IQ-TREE] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Nano-biochar regulates phage-host interactions, reducing antibiotic resistance genes in vermicomposting systems. (PNAS 2025)

- DOI: 10.1073/pnas.2511986122 | PMCID: PMC12403132 | PMID: 40838886
- Evidence: A maximum likelihood phylogeny of MAGs was inferred using IQ-TREE from bacterial marker genes generated from GTDB TK ( 59 ).
- Full pipeline: read trimming [QUAST] -> dimensionality reduction/clustering [BLAST] -> stage not stated [IQ-TREE, R, eggNOG]

### Evolution of developmental bias explains divergent patterns of phenotypic evolution in two nematode clades. (PNAS 2025)

- DOI: 10.1073/pnas.2507529122 | PMCID: PMC12403097 | PMID: 40828025
- Version used: **2.2.0.3**
- Evidence: We aligned the protein sequences using MAFFT v7.49 ( 63 ) and used IQ-TREE 2.2.0.3 ( 64 ) to infer a gene tree for each BUSCO gene, allowing the best-fitting substitution model to be automatically selected ( 65 ).
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MAFFT v7.49] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.2.2, emmeans v1.10.3, ggplot2 v3.5.1]

### Repeated polyploidization shapes divergence in floral morphology in &lt;i&gt;Lithophragma bolanderi&lt;/i&gt; (Saxifragaceae). (PNAS 2025)

- DOI: 10.1073/pnas.2505119122 | PMCID: PMC12377753 | PMID: 40802687
- Evidence: Based on these, a cpDNA tree was built using IQ-TREE 2 ( 85 ) with GTR+G model and 1,000 bootstraps, and a median joining haplotype network was built using POPART ( 86 ) ( SI Appendix , Supporting Text S3.8 ).
- Full pipeline: read trimming [GATK v4.1.4.1, fastp] -> alignment/mapping [GATK v4.1.4.1, fastp] -> variant calling [GATK v4.1.4.1, IQ-TREE, VCFtools, fastp] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4] -> stage not stated [BUSCO, WhatsHap]

### Tracing SARS-CoV-2 clusters across local scales using genomic data. (PNAS 2025)

- DOI: 10.1073/pnas.2501435122 | PMCID: PMC12358902 | PMID: 40773234
- Version used: **2.3.2**
- Evidence: First, a maximum-likelihood phylogeny was estimated using IQ-TREE v2.3.2 ( 43 ), applying the HKY85 nucleotide substitution model with empirical base frequencies.
- Full pipeline: alignment/mapping [minimap2 v2.24] -> stage not stated [IQ-TREE v2.3.2, R, TreeTime v0.11.2]

### Evolutionarily divergent nidovirus with an exceptionally large genome identified in Pacific oysters undergoing mass mortality. (PNAS 2025)

- DOI: 10.1073/pnas.2426923122 | PMCID: PMC12377751 | PMID: 40758866
- Version used: **2.2.0.3**
- Evidence: ML phylogenies were conducted using IQ-TREE v.2.2.0.3 ( 105 ) employing the best-fit model and 1000 bootstrap replicates.
- Full pipeline: read trimming [MAFFT, SPAdes v3.15.2, Trimmomatic v0.38] -> alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2.1] -> structure determination [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0.3, InterProScan v5.59]

### A trans-species cytoplasmic polymorphism is associated with seed shape and aridity across multiple species of sunflowers. (PNAS 2025)

- DOI: 10.1073/pnas.2410943122 | PMCID: PMC12337292 | PMID: 40720659
- Evidence: We used IQ-TREE with the model finder and 1,000 ultrafast bootstraps to generate separate chloroplast and mitochondrial maximum likelihood phylogenies ( 88 – 90 ).
- Full pipeline: read trimming [Trimmomatic v0.22] -> alignment/mapping [Trimmomatic v0.22] -> variant calling [GATK] -> stage not stated [BCFtools v1.10.2, IQ-TREE, SAMtools v1.10]

### A preclinical pig model of Angelman syndrome mirrors the early developmental trajectory of the human condition. (PNAS 2025)

- DOI: 10.1073/pnas.2505152122 | PMCID: PMC12318228 | PMID: 40690672
- Evidence: A maximum-likelihood phylogenetic tree was constructed from the cDNA sequences using IQ-TREE, with ultrafast bootstrap approximation for branch support ( 63 ).
- Full pipeline: read trimming [GATK, Trimmomatic v0.39] -> alignment/mapping [GATK, Trimmomatic v0.39] -> stage not stated [IQ-TREE]

### Paleobiome dynamics shaped a large Gondwanan plant radiation. (PNAS 2025)

- DOI: 10.1073/pnas.2502129122 | PMCID: PMC12304948 | PMID: 40663609
- Evidence: We estimated separate unrooted gene trees using a maximum-likelihood approach in the software IQ-TREE [v.
- Full pipeline: alignment/mapping [MAFFT v7.023b, R] -> dimensionality reduction/clustering [MAFFT v7.023b, R] -> stage not stated [IQ-TREE]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Version used: **2.2**
- Evidence: Reconstruction of a maximum likelihood phylogenetic tree used IQ-TREE (version 2.2) ( 58 ), and model selection used ModelFinder ( 59 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Identification of a VPS29 isoform with restricted association to Retriever and Retromer accessory proteins through autoinhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2501111122 | PMCID: PMC12260524 | PMID: 40587794
- Version used: **2.2.5**
- Evidence: Multiple rounds of maximum likelihood tree inference were used to identify homologous sequences using IQTREE v2.2.5 ( 79 ), with the best fitting substitution model (-m MFP) and 10,000 ultrafast bootstraps (-B 10,000).
- Full pipeline: alignment/mapping [ChimeraX v1.6.1, PyMOL] -> differential/statistical testing [R] -> machine learning [AlphaFold, ColabFold] -> visualisation [ChimeraX v1.6.1, Cytoscape v3.3, Metascape v3.5, PyMOL] -> stage not stated [IQ-TREE v2.2.5]

### Homoploid hybridization adds clarity to the origins of octoploid strawberries. (PNAS 2025)

- DOI: 10.1073/pnas.2502814122 | PMCID: PMC12207424 | PMID: 40531871
- Evidence: A maximum likelihood (ML) tree was constructed for each window using IQ-TREE V2.3 ( 57 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [GATK, IQ-TREE, OrthoFinder, SAMtools]

### An endosymbiotic origin of the crimson pigment from the lac insect. (PNAS 2025)

- DOI: 10.1073/pnas.2501623122 | PMCID: PMC12207437 | PMID: 40523179
- Evidence: 4 A ) but not with any known PKSs (maximum-likelihood tree constructed with IQTREE using LG+I+G4 substitution model based on BIC scores).
- Full pipeline: stage not stated [BLAST, BUSCO, IQ-TREE, InterProScan]

### Enzymatic carbon-fluorine bond cleavage by human gut microbes. (PNAS 2025)

- DOI: 10.1073/pnas.2504122122 | PMCID: PMC12184663 | PMID: 40512801
- Evidence: S20 and S21 ) was generated using the IQ-TREE algorithm ( 82 , 83 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R] -> simulation/modelling [AlphaFold, GROMACS] -> visualisation [Cytoscape] -> stage not stated [ColabFold, IQ-TREE]

### Structural basis of the catalytic and allosteric mechanism of bacterial acetyltransferase PatZ. (PNAS 2025)

- DOI: 10.1073/pnas.2419096122 | PMCID: PMC12184503 | PMID: 40498448
- Evidence: A maximum likelihood tree was inferred from the concatenation of amino acid alignments of 81 bacterial core genes extracted from the assemblies using UBCG ( 79 ) (version 2.0), with the JTT+F+I+G evolutionary model in IQ-TREE ( 80 ) (version 2.2.2.7).
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, Kraken2] -> structure determination [ChimeraX, PHENIX] -> visualisation [Kraken2] -> stage not stated [AlphaFold]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **1.6.12**
- Evidence: The phylogeny was reconstructed using IQ-TREE v1.6.12 http://iqtree.cibiv.univie.ac.at/ with the VT+F+I+G4 model and support was provided with 1,000 ultrafast bootstrap replicates ( 67 – 69 ).
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Parallel sensory compensation following independent subterranean colonization by groundwater salamanders (&lt;i&gt;Eurycea&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2504850122 | PMCID: PMC12168003 | PMID: 40460121
- Version used: **2.3.4**
- Evidence: We performed a maximum likelihood phylogenetic analysis using IQ-TREE 2.3.4 ( 98 ) with 10 replicates under the edge-proportional partition model ( 99 ) with 100,000 ultrafast bootstrap replicates ( 100 , 101 ) to assess support ( SI Appendix , Tables S9 and S10 ).
- Full pipeline: read trimming [MAFFT v4.475] -> alignment/mapping [MAFFT v4.475] -> differential/statistical testing [R] -> structure determination [phytools v2.3] -> stage not stated [IQ-TREE v2.3.4]

### Convergent expansions of keystone gene families drive metabolic innovation in Saccharomycotina yeasts. (PNAS 2025)

- DOI: 10.1073/pnas.2500165122 | PMCID: PMC12167968 | PMID: 40460114
- Evidence: After aligning, a species phylogeny was inferred with IQ-TREE ( 48 ) v2.0.7 using the general amino acid substitution matrix ( 49 ) with four gamma discretized rate categories.
- Full pipeline: alignment/mapping [IQ-TREE] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [InterProScan, OrthoFinder]

### Rhomboid-mediated cleavage of the immune receptor XA21 protects grain set and male fertility in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2502025122 | PMCID: PMC12146745 | PMID: 40445755
- Evidence: Phylogenetic analysis of the OsRBL3b homologs across multiple representative plant species was performed using the maximum likelihood (ML) algorithm implemented in IQ-TREE ( 63 ) as described in SI Appendix .
- Full pipeline: quantification [ImageJ] -> stage not stated [BLAST, IQ-TREE]

### Phylogenomics reveals the slow-burning fuse of diatom evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2500153122 | PMCID: PMC12146733 | PMID: 40440071
- Evidence: Species trees were inferred using gene tree summary methods with ASTRAL ( 61 ) or ASTRAL-Pro ( 62 ) and maximum likelihood analysis of concatenated ortholog matrices with IQ-TREE ( 63 ).
- Full pipeline: stage not stated [BUSCO, IQ-TREE]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Version used: **1.6.12**
- Evidence: Based on the unmodified alignment, a maximum likelihood phylogenetic tree was computed in IQ-TREE 1.6.12 ( 79 ).
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### Structure and evolution of photosystem I in the early-branching cyanobacterium &lt;i&gt;Anthocerotibacter panamensis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2427090122 | PMCID: PMC12107172 | PMID: 40366692
- Version used: **2.2**
- Evidence: Maximum Likelihood tree inference was performed for each individual subunit with IQ-TREE 2.2 ( 67 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [IQ-TREE v2.2, RELION v3.1, UCSF Chimera]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: A phylogenetic tree was constructed in IQ-TREE with the VT amino acid substitution model, as determined by ProtTest ( 48 , 49 ), and branch support was assessed using 1,000 bootstrap replicates.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Phylogenomics of the tetraploid Hawaiian lobeliads: Implications for their origin, dispersal history, and adaptive radiation. (PNAS 2025)

- DOI: 10.1073/pnas.2421004122 | PMCID: PMC12088406 | PMID: 40324077
- Version used: **2.2.2.6**
- Evidence: We selected the best nucleotide substitution model for each nuclear locus using IQ-TREE v.2.2.2.6 ( 89 ).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [BEAST v2.7.5, IQ-TREE v2.2.2.6, R]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Version used: **2.06**
- Evidence: The resulting sequences were aligned using MAFFT v7.490 and used to produce a phylogenetic tree via IQ-TREE v2.06, run with 1000 ultrafast bootstrap and Shimodaira–Hasegawa approximate likelihood ratio test replicates ( 31 , 64 , 66 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### Horizontal transfer of nuclear DNA in transmissible cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2424634122 | PMCID: PMC12067285 | PMID: 40261943
- Version used: **2.2.5**
- Evidence: Otherwise, single base substitutions present with a variant allele read depth of 3 or higher and a VAF greater than 0.5 were used to construct a phylogenetic tree using the software IQ-TREE v2.2.5 ( 59 ), with substitution model GTR+G{4} ( 60 ).
- Full pipeline: variant calling [DESeq2] -> quantification [R] -> normalisation [DESeq2] -> differential/statistical testing [R] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.2.5]

### Diet-regulated transcriptional plasticity of plant parasites in plant-mutualist environments. (PNAS 2025)

- DOI: 10.1073/pnas.2421367122 | PMCID: PMC12037023 | PMID: 40244681
- Evidence: Phylogenetic trees were generated by IQ-TREE ( 56 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, HTSeq, ImageJ] -> differential/statistical testing [DESeq2, HTSeq] -> stage not stated [IQ-TREE]

### Genomic signatures associated with the evolutionary loss of egg yolk in parasitoid wasps. (PNAS 2025)

- DOI: 10.1073/pnas.2422292122 | PMCID: PMC12036997 | PMID: 40232796
- Evidence: Orthology and species trees were reconstructed with OrthoFinder ( 120 ), STAG ( 121 ), and IQ-TREE ( 122 ), with divergence times estimated using r8s-v1.81 ( 123 ) and fossil-calibrated nodes ( 124 ).
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> quantification [RSEM] -> structure determination [IQ-TREE, OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, HMMER]

### Discovery and functional characterization of a bombesin-type neuropeptide signaling system in an invertebrate. (PNAS 2025)

- DOI: 10.1073/pnas.2420966122 | PMCID: PMC12002301 | PMID: 40153458
- Evidence: Therefore, to further investigate relationships between putative BN-type peptide precursors in echinoderms and BN/ET/CCHa/EP-type precursors in other taxa, a maximum-likelihood phylogenetic tree was generated using W-IQ-TREE ( http://iqtree.cibiv.univie.ac.at/ ) ( 55 ) (JTT+I+G4 model, 1,000 bootstrap replicates).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **2.3.0**
- Evidence: Maximum likelihood phylogenetic trees were constructed for each alignment using IQ-TREE v2.3.0 ( 83 ), and the best substitution model was predicted for each tree using ModelFinder ( 84 ).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### &lt;i&gt;Enterobacter hormaechei&lt;/i&gt; replaces virulence with carbapenem resistance via porin loss. (PNAS 2025)

- DOI: 10.1073/pnas.2414315122 | PMCID: PMC11874173 | PMID: 39977318
- Version used: **1.6.10**
- Evidence: Core genomes were computed for 18 ST78 isolates (4,439,247 alignment positions of which 1,158 were variable) and a subset of six closely related ST78 clade D isolates (the same for which hybrid assemblies were generated; 4,876,976 alignment positions of which 85 were variable) and used to obtain two maximum likelihood phylogenies computed with IQ-TREE v.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.10] -> stage not stated [BLAST v2.11.0, Medaka]

### Subfunctionalization and epigenetic regulation of a biosynthetic gene cluster in &lt;i&gt;Solanaceae&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2420164122 | PMCID: PMC11874288 | PMID: 39977312
- Version used: **2.1.4**
- Evidence: IQTREE (v2.1.4-beta) ( 64 ) was used to infer the maximum likelihood tree with the best-fit model selected by ModelFinder ( 65 ) with 1,000 replicates of ultrafast bootstrapping ( 66 ).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> quantification [DESeq2] -> normalisation [DESeq2] -> visualisation [Python v3.9] -> stage not stated [IQ-TREE v2.1.4, OrthoFinder v2.5.4]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Evidence: The phylogenetic tree was constructed using IQ-TREE, employing the LG+F+I+G4 model.
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Natural variations in <i>TT8</i> and its neighboring <i>STK</i> confer yellow seed with elevated oil content in <i>Brassica juncea</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2417264122 | PMCID: PMC11804580 | PMID: 39883846
- Version used: **1.6.12**
- Evidence: A maximum likelihood phylogeny was inferred by IQ-TREE (v 1.6.12) ( 92 ) with concatenated alignments and the best-fitting model, and with 1,000 bootstrap replicates.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12] -> differential/statistical testing [GEMMA] -> visualisation [Cytoscape] -> stage not stated [BUSCO, R, VCFtools, WGCNA, minimap2 v2.17]

### Emergence and evolution of heterocyte glycolipid biosynthesis enabled specialized nitrogen fixation in cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2413972122 | PMCID: PMC11804610 | PMID: 39869795
- Version used: **2.1.2**
- Evidence: A phylogenetic tree was constructed with IQ-TREE (v2.1.2) ( 65 ) (further details in SI Appendix ), and visualized and decorated in Interactive Tree of Life (iTOL) ( 66 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> visualisation [IQ-TREE v2.1.2]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Version used: **2.2.2.3**
- Evidence: The phylogeny was reconstructed using IQ-TREE v2.2.2.3 with the model LG + C20 + F + G and support was provided with 1,000 ultrafast bootstrap replicates ( 42 – 44 ).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **1.6.1035**
- Evidence: The phylogenetic tree based on these supergenes was constructed with IQ-TREE v1.6.1035, using the JTT + F + I + G4 method with 1,000 bootstrap replicates.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Metabolic enhancement contributed by horizontal gene transfer is essential for dietary specialization in leaf beetles. (PNAS 2025)

- DOI: 10.1073/pnas.2415717122 | PMCID: PMC11725898 | PMID: 39793087
- Version used: **2.2.2.6**
- Evidence: The phylogenetic tree was then constructed using IQTREE v2.2.2.6, incorporating 1,000 boot-strap replicates and the Q.insect model ( 55 ).
- Full pipeline: alignment/mapping [Clustal Omega, SAMtools v1.17] -> stage not stated [IQ-TREE v2.2.2.6, OrthoFinder v2.5.4, RepeatMasker v2.0.4, eggNOG, fastp v0.23.4]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Evidence: High-quality 4DTv SNPs (36,028) were used for maximum-likelihood phylogenetic tree construction (IQ-TREE) (v1.6.12) ( 69 ), PCA (PLINK, v1.9), and population structure analysis (ADMIXTURE, K = 2–10, v1.23) ( 70 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Persistent trade-offs balance competition and colonization across centuries. (PNAS 2026)

- DOI: 10.1073/pnas.2534310123 | PMCID: PMC13250502 | PMID: 42228529
- Version used: **2.1.4**
- Evidence: A maximum-likelihood tree was constructed from 3,095 biallelic SNPs detected in at least 95% of isolates using IQ-TREE v2.1.4 ( 60 ) applying TVM+F+ASC+R3 as the best substitution model ( 61 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [lme4] -> stage not stated [DESeq2, IQ-TREE v2.1.4, R, emmeans]

### Ancient DNA from shells reveals delayed genomic erosion and rapid immune adaptation in the critically endangered black abalone. (PNAS 2026)

- DOI: 10.1073/pnas.2600483123 | PMCID: PMC13229213 | PMID: 42207912
- Evidence: Finally, we constructed gene trees for individual outlier windows by first converting the VCF region to a phylip file ( https://github.com/edgardomortiz/vcf2phylip ) and performing phylogenetic inference with IQ-TREE 2 ( 105 ) using the GTR+I + G substitution model and default parameters.
- Full pipeline: read trimming [fastp] -> variant calling [SAMtools] -> stage not stated [GATK, IQ-TREE, R]

### Distinct evolutionary patterns of endemic and emerging parvoviruses and the origin of a new pandemic virus. (PNAS 2026)

- DOI: 10.1073/pnas.2515274123 | PMCID: PMC13099694 | PMID: 41980105
- Evidence: Maximum likelihood (ML) phylogenetic analysis was performed using PhyML ( 65 ) or IQ-TREE ( 66 ), employing a general time-reversible (GTR) substitution model, gamma-distributed (Γ) rate variation among sites, and bootstrap resampling (1,000 replications).
- Full pipeline: differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [AlphaFold, ChimeraX, IQ-TREE]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **2.4.0**
- Evidence: A maximum likelihood phylogenetic tree of the 47 mitogenomes was constructed in IQ-TREE v2.4.0 ( 61 ) with standard model selection (-m TEST), ultrafast bootstrapping with 1000 replicates (-B 1000) ( 62 ), and applying a SH-like approximate likelihood ratio test with 1000 replicates (-alrt 1000) ( 63 ).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### Mycoviruses confer hypovirulence but enhance antifungal volatile organic compound production in a phytopathogenic fungus. (PNAS 2026)

- DOI: 10.1073/pnas.2526822123 | PMCID: PMC13080020 | PMID: 41941638
- Version used: **2.2.6**
- Evidence: Maximum likelihood phylogenetic trees were constructed using IQ-TREE 2.2.6 ( 53 ), with branch support values calculated based on 1,000 bootstrap replicates.
- Full pipeline: alignment/mapping [ChimeraX, MAFFT v7.0] -> normalisation [ComplexHeatmap] -> dimensionality reduction/clustering [ComplexHeatmap, HMMER v3.3.2] -> visualisation [ChimeraX, ComplexHeatmap, ImageJ] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.2.6]

### Photoreceptor control of &lt;i&gt;Platynereis&lt;/i&gt; growth and lifespan via evolutionarily conserved molecular pathways. (PNAS 2026)

- DOI: 10.1073/pnas.2514719123 | PMCID: PMC13012086 | PMID: 41855267
- Evidence: Maximum likelihood phylogenies were generated using the IQ-TREE ( 91 ) web server, with default settings.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [IQ-TREE, ImageJ]

### Decoding antibody response to MERS-CoV in wild dromedary camels. (PNAS 2026)

- DOI: 10.1073/pnas.2513716123 | PMCID: PMC12913009 | PMID: 41662528
- Version used: **2.1.4**
- Evidence: Amino acid sequences were aligned using MUSCLE v3.8.1551, and a phylogenetic tree was constructed with IQ-TREE v2.1.4-beta using 1,000 bootstrap replicates ( http://www.iqtree.org/ ).
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.310, MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, PyMOL] -> stage not stated [CCP4]

### Biological causes and impacts of rugged tree landscapes in phylodynamic inference. (PNAS 2026)

- DOI: 10.1073/pnas.2510938123 | PMCID: PMC12799104 | PMID: 41512041
- Version used: **2.3.2**
- Evidence: To perform RTT regression ( 50 ), we first conducted maximum-likelihood (ML) phylogenetic inference of each dataset using IQ-TREE v2.3.2 ( 84 ).
- Full pipeline: differential/statistical testing [IQ-TREE v2.3.2]

### Deep evolutionary conservation of a sex-determining locus without sequence homology. (PNAS 2026)

- DOI: 10.1073/pnas.2522417123 | PMCID: PMC12799146 | PMID: 41490485
- Version used: **2.3.6**
- Evidence: To assess haplotype diversity at the multiallelic sex-determining region of the ANTSR locus in B. terrestris and V. velutina nigrithorax , VCFs were converted to FASTA with vcf-kit v0.2.6 ( 58 ), and maximum-likelihood phylogenies were reconstructed in IQ-TREE v2.3.6 with ascertainment bias correction and SH-aLRT support (“ –st DNA –m GTR+ASC –bb 1000 –alrt 1000 ”) ( 59 ).
- Full pipeline: alignment/mapping [BWA v0.7.18, freebayes v1.0.2] -> variant calling [BWA v0.7.18, IQ-TREE v2.3.6, SPAdes v3.15.2, freebayes v1.0.2] -> dimensionality reduction/clustering [BWA v0.7.18, freebayes v1.0.2] -> structure determination [IQ-TREE v2.3.6] -> stage not stated [BCFtools v1.21, PLINK v1.9, R v4.4, VCFtools v0.1.16]

### SARS-CoV-2 within-host diversity and transmission. (Science 2021)

- DOI: 10.1126/science.abg0821 | PMCID: PMC8128293 | PMID: 33688063
- Evidence: The recommendations of Morel et al . do not easily lend themselves to fast bootstrapping, so to explore phylogenetic uncertainty, we performed an additional phylogenetic reconstruction on the same alignment using the ultrafast bootstrap procedure in IQ-TREE ( 68 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT] -> structure determination [IQ-TREE, RAxML] -> stage not stated [Docker, Pangolin]

### The molecular epidemiology of multiple zoonotic origins of SARS-CoV-2. (Science 2022)

- DOI: 10.1126/science.abp8337 | PMCID: PMC9348752 | PMID: 35881005
- Version used: **2.0.7**
- Evidence: We (i) inferred a maximum likelihood tree of 31 sarbecovirus genomes (SARS-CoV-2 and 30 closely related sarbecoviruses sampled from bats and pangolins) across 15 predefined non-recombinant regions ( 13 ) with IQ-TREE v2.0.7 ( 60 ), (ii) inferred the sequence of the ancestor of SARS-CoV-2 in each tree with TreeTime v0.8.1 ( 61 ), and (iii) concatenated the resulting sequences.
- Full pipeline: alignment/mapping [MAFFT v7.453] -> stage not stated [IQ-TREE v2.0.7, TreeTime v0.8.1]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Evidence: A MAFFT multiple sequence alignment was performed using the FFT-NS-i (standard) strategy with a maximum of two iterations ( 104 ) and then used for phylogenetic tree construction implementing IQ-TREE software ( 105 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Ancient &lt;i&gt;Borrelia&lt;/i&gt; genomes document the evolutionary history of louse-borne relapsing fever. (Science 2025)

- DOI: 10.1126/science.adr2147 | PMCID: PMC7617810 | PMID: 40403067
- Version used: **1.6.12**
- Evidence: We then reconstructed relatedness using a maximum likelihood approach in IQ-TREE v.1.6.12.
- Full pipeline: differential/statistical testing [BEAST] -> structure determination [IQ-TREE v1.6.12]

