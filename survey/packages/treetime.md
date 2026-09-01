# TreeTime

- **Category:** phylogenetics
- **Papers in survey:** 20
- **Journals:** PNAS (9), Nature (6), Cell (3), Science (2)
- **Years:** 2021 (3), 2022 (6), 2023 (4), 2024 (2), 2025 (4), 2026 (1)
- **Versions named:** 0.7.6 (2), 0.7.4 (1), 0.9.4 (1), 0.8.4 (1), 0.8.1 (1), 0.11.2 (1), 0.7.1 (1), 0.8.0 (1)
- **Pipeline stages it appears in:** structure determination (4), normalisation (4), alignment/mapping (1), dimensionality reduction/clustering (1), differential/statistical testing (1), simulation/modelling (1)

## Papers

### Generation and transmission of interlineage recombinants in the SARS-CoV-2 pandemic. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.014 | PMCID: PMC8367733 | PMID: 34499854
- Evidence: (2020) http://www.iqtree.org/ TreeTime Sagulenko et al.
- Full pipeline: alignment/mapping [Pangolin, minimap2] -> variant calling [Python] -> structure determination [IQ-TREE v2.1] -> stage not stated [SAMtools, TreeTime]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Version used: **0.8.0**
- Evidence: ...ning assay N/A Vogels et al., 2021 Software and algorithms R CRAN https://cran.r-project.org/ IQ-Tree 1.6.12 http://www.iqtree.org/ Minh et al., 2020 TreeTime 0.8.0 https://github.com/neherlab/treetime Sagulenko et al., 2018 TempEst http://tree.bio.ed.ac.uk/software/tempest/ Rambaut et al., 2016 TreeAnnotator https://beast.community/treeannotator Rambaut et al., 2018 BEAST v1.10 http://beast.commu...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### Dispersal patterns and influence of air travel during the global expansion of SARS-CoV-2 variants of concern. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.001 | PMCID: PMC10247138 | PMID: 37413988
- Evidence: 41 N/A TreeTime Sagulenko et al.
- Full pipeline: stage not stated [R, TreeTime, ggplot2]

### Emergence and expansion of SARS-CoV-2 B.1.526 after identification in New York. (Nature 2021)

- DOI: 10.1038/s41586-021-03908-2 | PMCID: PMC8481122 | PMID: 34428777
- Evidence: ...://github.com/nextstrain/nextclade ), constructs a maximum-likelihood phylogenetic tree via IQ-TREE 33 , estimates molecular clock branch lengths via TreeTime 34 and reconstructs nucleotide and amino acid changes (also via TreeTime).
- Full pipeline: alignment/mapping [Nextstrain] -> structure determination [IQ-TREE, Nextstrain, TreeTime] -> stage not stated [Pangolin]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Version used: **0.8.4**
- Evidence: Because most Bayesian phylogenetic frameworks (such as BEAST2) are based on bifurcating trees and hence are poor at resolving multifurcating nodes, we complemented our approach by using TreeTime v.0.8.4 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Evidence: The resulting maximum-likelihood tree topology was transformed into a time-calibrated phylogeny in which branches along the tree were scaled in calendar time using TreeTime 68 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### A molnupiravir-associated mutational signature in global SARS-CoV-2 genomes. (Nature 2023)

- DOI: 10.1038/s41586-023-06649-6 | PMCID: PMC10651478 | PMID: 37748513
- Evidence: We took the 20 sequences in the cluster, and the three closest outgroup sequences, we aligned using Nextclade 52 , calculated a tree using IQ-TREE 54 and reconstructed the mutation-annotated tree using TreeTime 55 .
- Full pipeline: alignment/mapping [IQ-TREE, TreeTime, minimap2] -> dimensionality reduction/clustering [IQ-TREE, TreeTime] -> structure determination [IQ-TREE, TreeTime] -> stage not stated [Nextstrain]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Version used: **0.9.4**
- Evidence: Discrete trait analysis was performed using TreeTime (v0.9.4) 65 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **0.7.4**
- Evidence: TreeTime v.0.7.4 (ref.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Phylodynamic signatures in the emergence of community-associated MRSA. (PNAS 2022)

- DOI: 10.1073/pnas.2204993119 | PMCID: PMC9659408 | PMID: 36322765
- Version used: **0.7.1**
- Evidence: We used an ML approach with TreeTime v0.7.1 ( 67 ) to obtain a time-scaled phylogenetic tree by fitting a strict molecular clock to the data (using sampling dates in years throughout).
- Full pipeline: quality control [Nextflow] -> variant calling [Nextflow] -> normalisation [TreeTime v0.7.1] -> differential/statistical testing [Nextflow] -> structure determination [Nextflow] -> stage not stated [RAxML]

### The durability of natural infection and vaccine-induced immunity against future infection by SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2204336119 | PMCID: PMC9351502 | PMID: 35858382
- Version used: **0.7.6**
- Evidence: Topologies were time calibrated using least-squares dating ( 26 ) in IQ-TREE v2.0.6 ( 24 ), RelTime ( 27 ) in MEGA X v10.1.9 ( 28 ), and TreeTime v0.7.6, enabling us to assess consistency across divergence times that were scaled proportionally to the most recent common ancestor.
- Full pipeline: alignment/mapping [IQ-TREE v2.0.6, RAxML v7.2.8] -> normalisation [TreeTime v0.7.6] -> structure determination [IQ-TREE v2.0.6, RAxML v7.2.8]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Evidence: Briefly, SNPPar uses TreeTime to perform an ancestral sequence reconstruction at each node, then infers mutation events arising on each branch of the tree.
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Correlated substitutions reveal SARS-like coronaviruses recombine frequently with a diverse set of structured gene pools. (PNAS 2023)

- DOI: 10.1073/pnas.2206945119 | PMCID: PMC9945976 | PMID: 36693089
- Evidence: We use a standard maximum likelihood phylodynamic approach ( TreeTime ; ( 54 )) to estimate the mutation rate as μ ≈ 9.8 × 10 - 4 b p - 1 · y e a r - 1 for SARS-CoV-2 (see Methods for details); for the SL-CoVs, previous studies have inferred μ ≈ 5.0 × 10 - 4 b p - 1 · y e a r - 1 ( 20 , 21 ).
- Full pipeline: alignment/mapping [Nextstrain, minimap2] -> stage not stated [TreeTime]

### Incipient functional SARS-CoV-2 diversification identified through neural network haplotype maps. (PNAS 2024)

- DOI: 10.1073/pnas.2317851121 | PMCID: PMC10927536 | PMID: 38416684
- Version used: **0.7.6**
- Evidence: TreeTime v0.7.6 ( 62 ) was used for the ancestral reconstruction of most likely sequences of internal nodes of the tree and their clades.
- Full pipeline: alignment/mapping [MAFFT v7.453] -> structure determination [TreeTime v0.7.6] -> stage not stated [Nextstrain]

### Phylogenomics redefines the evolutionary history of mosquitoes. (PNAS 2025)

- DOI: 10.1073/pnas.2519291122 | PMCID: PMC12557814 | PMID: 41052354
- Evidence: Ancestral sequences, GC content, and substitutions were estimated for the basal nodes of subfamily Anophelinae and tribes Aedini and Culicini using the program TreeTime ( 83 ).
- Full pipeline: alignment/mapping [BUSCO] -> differential/statistical testing [R, ggplot2] -> stage not stated [BEAST, IQ-TREE v2.2, TreeTime]

### Tracing SARS-CoV-2 clusters across local scales using genomic data. (PNAS 2025)

- DOI: 10.1073/pnas.2501435122 | PMCID: PMC12358902 | PMID: 40773234
- Version used: **0.11.2**
- Evidence: Next, time calibration was performed using TreeTime v0.11.2 ( 44 ), which estimated an evolutionary rate of 0.0007 substitutions per site per year with r^2 = 0.35.
- Full pipeline: alignment/mapping [minimap2 v2.24] -> stage not stated [IQ-TREE v2.3.2, R, TreeTime v0.11.2]

### Horizontal transmission of functionally diverse transposons is a major source of new introns. (PNAS 2025)

- DOI: 10.1073/pnas.2414761122 | PMCID: PMC12130899 | PMID: 40402243
- Evidence: We estimated time-scaled phylogenies with TreeTime ( 93 ), specifying sampling dates from NCBI and substitution rates from the literature.
- Full pipeline: alignment/mapping [BLAST, MAFFT] -> normalisation [TreeTime] -> structure determination [RepeatMasker]

### Bayesian phylodynamic inference of population dynamics with dormancy. (PNAS 2025)

- DOI: 10.1073/pnas.2501394122 | PMCID: PMC12067208 | PMID: 40314983
- Evidence: Next, given the simulated seedbank genealogy and the specified mutation model parameters, we generated molecular sequences using a modified implementation of the TreeTime package ( 89 ).
- Full pipeline: simulation/modelling [TreeTime] -> stage not stated [BEAST]

### The evolving SARS-CoV-2 epidemic in Africa: Insights from rapidly expanding genomic surveillance. (Science 2022)

- DOI: 10.1126/science.abq5358 | PMCID: PMC9529057 | PMID: 36108049
- Evidence: Following the removal of potential outliers in R with the ape package ( 70 ), the resulting ML-trees were then transformed into time calibrated phylogenies in TreeTime ( 71 ) by applying a rate of 8x10e-4 substitution per site per year ( 72 ) in order to transform the branches into units of calendar time.
- Full pipeline: stage not stated [Pangolin, TreeTime]

### The molecular epidemiology of multiple zoonotic origins of SARS-CoV-2. (Science 2022)

- DOI: 10.1126/science.abp8337 | PMCID: PMC9348752 | PMID: 35881005
- Version used: **0.8.1**
- Evidence: We (i) inferred a maximum likelihood tree of 31 sarbecovirus genomes (SARS-CoV-2 and 30 closely related sarbecoviruses sampled from bats and pangolins) across 15 predefined non-recombinant regions ( 13 ) with IQ-TREE v2.0.7 ( 60 ), (ii) inferred the sequence of the ancestor of SARS-CoV-2 in each tree with TreeTime v0.8.1 ( 61 ), and (iii) concatenated the resulting sequences.
- Full pipeline: alignment/mapping [MAFFT v7.453] -> stage not stated [IQ-TREE v2.0.7, TreeTime v0.8.1]

