# phytools

- **Category:** phylogenetics
- **Papers in survey:** 91
- **Journals:** PNAS (80), Nature (11)
- **Years:** 2021 (7), 2022 (23), 2023 (11), 2024 (16), 2025 (28), 2026 (6)
- **Versions named:** 0.7 (4), 2.3 (2), 2.4 (1), 1.5 (1), 1.9.1 (1), 1.9 (1), 1.9.16 (1), 2.1.1 (1), 1.0 (1), 1.2 (1)
- **Pipeline stages it appears in:** structure determination (22), visualisation (9), alignment/mapping (8), differential/statistical testing (6), simulation/modelling (4), dimensionality reduction/clustering (3)

## Papers

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Evidence: Genome size evolution Genome size evolution was modelled by maximum likelihood using the ‘fastAnc’ function in the phytools R package 78 .
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Evidence: In the genic phylogenetic signal analysis, Pagel’s λ was calculated for group 1–3 genes ( n = 8,368) using ‘phylosig’ from the phytools R package v.1.0-1 (ref.
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### Pterosaur melanosomes support signalling functions for early feathers. (Nature 2022)

- DOI: 10.1038/s41586-022-04622-3 | PMCID: PMC9046085 | PMID: 35444275
- Evidence: As such, we used the ‘make.simmap’ function of the phytools package 54 .
- Full pipeline: stage not stated [ImageJ, R, phytools]

### Cancer risk across mammals. (Nature 2022)

- DOI: 10.1038/s41586-021-04224-5 | PMCID: PMC8755536 | PMID: 34937938
- Evidence: Phylogenetic signal of cancer risk was assessed using the function phylosig from the R package phytools 22 .
- Full pipeline: stage not stated [R, emmeans, phytools]

### Global hotspots of traded phylogenetic and functional diversity. (Nature 2023)

- DOI: 10.1038/s41586-023-06371-3 | PMCID: PMC10412452 | PMID: 37495700
- Evidence: For the two continuous traits (body mass and proportion of diet) we calculated Pagels lambda using the R package phytools 58 and tested whether this was significantly different from the scenario in which the trait had evolved randomly.
- Full pipeline: stage not stated [R, brms, phytools]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Version used: **1.5**
- Evidence: Phylogenetic trees were annotated using the R packages ape (v5.6.2) 83 , phytools (v1.5-1) 84 , and ggtree (v3.3.0.9) 85 and further edited in Adobe Illustrator.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Growth of complete ammonia oxidizers on guanidine. (Nature 2024)

- DOI: 10.1038/s41586-024-07832-z | PMCID: PMC11410670 | PMID: 39143220
- Evidence: Trees were visualized in R using a combination of the cophylo function from the phytools package and the ggtree package.
- Full pipeline: alignment/mapping [ImageJ v1.54f] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ImageJ v1.54f, PyMOL, phytools] -> stage not stated [AlphaFold, BEDTools, HMMER]

### Drivers of avian genomic change revealed by evolutionary rate decomposition. (Nature 2025)

- DOI: 10.1038/s41586-025-08777-7 | PMCID: PMC12119353 | PMID: 40108459
- Evidence: The distribution of trait data was visualized across branches in the avian phylogeny using fast maximum-likelihood ancestral state reconstruction as implemented in phytools 73 .
- Full pipeline: dimensionality reduction/clustering [BLAST, clusterProfiler] -> differential/statistical testing [brms] -> structure determination [phytools] -> visualisation [phytools] -> stage not stated [IQ-TREE v2.1.2, R]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **2.4**
- Evidence: The tree was midpoint rooted using phytools v.2.4-4 (ref.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Limited thermal tolerance in tropical insects and its genomic signature. (Nature 2026)

- DOI: 10.1038/s41586-026-10155-w | PMCID: PMC12999521 | PMID: 41781608
- Evidence: We reconstructed ancestral trait values of thermal tolerances using the fastAnc function from phytools 59 , plotted them on the phylogenetic tree with ggtree 60 , and calculated a phylogenetic correlogram using phylosignal to test for significance of the phylogenetic signal—that is, if trait values of related OTU are more similar (or dissimilar) than expected by chance 21 .
- Full pipeline: structure determination [phytools] -> visualisation [phytools] -> stage not stated [AlphaFold, BUSCO, Conda]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Evidence: First, we generated an ultrametric phylogenetic tree with ape, TreeTools and phytools packages in R, based on phylogenetic tree built using IQ-TREE.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### A conserved genetic architecture among populations of the maize progenitor, teosinte, was radically altered by domestication. (PNAS 2021)

- DOI: 10.1073/pnas.2112970118 | PMCID: PMC8639367 | PMID: 34686607
- Evidence: This test is performed by using the skewers function with 1,000 simulations implemented in the phytools package ( 40 ) in R.
- Full pipeline: simulation/modelling [phytools]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Version used: **0.7**
- Evidence: Then, the make.simmap function in phytools (v0.7–70, R package) ( 44 ) was used to perform stochastic source mapping based on ARD model and the tip states on the tree, with 10,000 generations of MCMC sampling every 100 generations. pPCP1 and pla Analysis Samtools depth command was used to count the depth of whole pPCP1 plasmid and pla gene for each sample from bam files.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Global abundance estimates for 9,700 bird species. (PNAS 2021)

- DOI: 10.1073/pnas.2023170118 | PMCID: PMC8166167 | PMID: 34001610
- Evidence: Using the function phylosig from the R package, phytools ( 94 ), we calculated Blomberg’s K as our measure of phylogenetic signal.
- Full pipeline: differential/statistical testing [R, brms] -> stage not stated [phytools]

### Phylogenomic and ecological analyses reveal the spatiotemporal evolution of global pines. (PNAS 2021)

- DOI: 10.1073/pnas.2022302118 | PMCID: PMC8157994 | PMID: 33941644
- Version used: **0.7**
- Evidence: To estimate evolutionary rates of niche and phenotypic traits in Pinus , we firstly ordinated all environmental variables and phenotypic data using phylogenetic principal component analysis (PCA) implemented in phytools (v.0.7-70) package ( 93 ) with the “phyl.pca” function.
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> dimensionality reduction/clustering [phytools v0.7] -> stage not stated [IQ-TREE v2.0, R v3.6.2, ggplot2]

### Evolutionary relationships between drought-related traits and climate shape large hydraulic safety margins in western North American oaks. (PNAS 2021)

- DOI: 10.1073/pnas.2008987118 | PMCID: PMC7958251 | PMID: 33649205
- Evidence: This was achieved using the phylosig function in the phytools package in R.
- Full pipeline: stage not stated [ImageJ, phytools]

### The evolution of siphonophore tentilla for specialized prey capture in the open ocean. (PNAS 2021)

- DOI: 10.1073/pnas.2005063118 | PMCID: PMC7923536 | PMID: 33593896
- Evidence: We reconstructed ancestral states using ML [R phytools::anc.ML ( 52 )], and stochastic character mapping (R phytools::make.simmap) for categorical characters.
- Full pipeline: alignment/mapping [phytools] -> structure determination [phytools] -> stage not stated [R]

### Multiclonal human origin and global expansion of an endemic bacterial pathogen of livestock. (PNAS 2022)

- DOI: 10.1073/pnas.2211217119 | PMCID: PMC9897428 | PMID: 36469788
- Evidence: Discrete trait reconstruction analyses aimed to infer ancestral states, and state changes across the branches of the phylogeny for host and location were performed using 100 simulations of stochastic character mapping (SIMMAP) ( 43 ) as implemented in the R package phytools ( 44 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36] -> alignment/mapping [phytools] -> differential/statistical testing [BEAST, R] -> simulation/modelling [phytools] -> structure determination [phytools] -> stage not stated [InterProScan v5.52, Prokka v1.13]

### Transposable elements drive intron gain in diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2209766119 | PMCID: PMC9860276 | PMID: 36417430
- Evidence: To evaluate a correlation between aquatic lifestyle and the presence of Introners, we used Pagel's test through the R package phytools ( 57 , 61 ) using the aforementioned global phylogeny as an input ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MAFFT, SAMtools] -> differential/statistical testing [R, lme4] -> stage not stated [Python, RepeatMasker, phytools]

### Ancestral sex-role plasticity facilitates the evolution of same-sex sexual behavior. (PNAS 2022)

- DOI: 10.1073/pnas.2212401119 | PMCID: PMC9674213 | PMID: 36346843
- Evidence: We carried out separate ancestral-state reconstructions for tandem running, female leadership, and male leadership, respectively, using the function ace() in the R package “phytools” ( 75 ).
- Full pipeline: structure determination [phytools] -> stage not stated [R v4.0]

### Alternating regimes of shallow and deep-sea diversification explain a species-richness paradox in marine fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2123544119 | PMCID: PMC9618140 | PMID: 36252009
- Evidence: We performed a maximum-likelihood ancestral state reconstruction of the eight size-adjusted variables individually using the “fastAnc” function in phytools.
- Full pipeline: structure determination [phytools] -> stage not stated [R]

### Factors influencing terrestriality in primates of the Americas and Madagascar. (PNAS 2022)

- DOI: 10.1073/pnas.2121105119 | PMCID: PMC9586308 | PMID: 36215474
- Evidence: We fitted the models in R v3.6.3 ( 118 ) using the ‘brms’ package ( 126 ), for model fitting, ‘bayestestR’ ( 125 ) for Bayesian summary statistics, and ‘ape’ ( 127 ) and ‘phytools’ ( 128 ) for handling the phylogenetic data.
- Full pipeline: differential/statistical testing [brms, phytools] -> stage not stated [R v3.6]

### The evolution of insular woodiness. (PNAS 2022)

- DOI: 10.1073/pnas.2208629119 | PMCID: PMC9478640 | PMID: 36067289
- Evidence: To test if IW was phylogenetically clustered on the nonmonocot angiosperm tree of life, we calculated the phylogenetic signal in the proportion of IWS per taxon using Blomberg’s K ( 65 ) and Pagel’s λ ( 66 ) as implemented in phytools ( 63 ).
- Full pipeline: dimensionality reduction/clustering [phytools] -> stage not stated [R, lavaan v0.6.8]

### Diploid-dominant life cycles characterize the early evolution of Fungi. (PNAS 2022)

- DOI: 10.1073/pnas.2116841119 | PMCID: PMC9457484 | PMID: 36037379
- Evidence: Marginal and stochastic ancestral state reconstructions of ploidy were conducted with phytools ( 73 ) in R.
- Full pipeline: variant calling [GATK, SAMtools v1.5] -> structure determination [phytools] -> stage not stated [BUSCO]

### Wildlife susceptibility to infectious diseases at global scales. (PNAS 2022)

- DOI: 10.1073/pnas.2122851119 | PMCID: PMC9436312 | PMID: 35994656
- Evidence: The predicted susceptibility of each host–pathogen assemblage was used as a trait to map it onto a phylogeny that was constructed using contmap and fastAnc functions from phytools R package ( 107 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [ape (R), ggplot2, phytools]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Evidence: Tree topology exploration from the Twisst analyses, including identification of sister clades, was conducted using the R packages ape and phytools ( 89 , 90 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### The rise of biting during the Cenozoic fueled reef fish body shape diversification. (PNAS 2022)

- DOI: 10.1073/pnas.2119828119 | PMCID: PMC9351382 | PMID: 35881791
- Evidence: To reconstruct the history of feeding modes along the phylogeny, we used “phytools” version 0.7–80 to generate a distribution of 100 stochastic character maps ( 103 , 104 ) (further details are in SI Appendix ).
- Full pipeline: structure determination [phytools] -> stage not stated [R]

### The impact of paleoclimatic changes on body size evolution in marine fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2122486119 | PMCID: PMC9308125 | PMID: 35858316
- Evidence: We performed ancestral state reconstructions of body sizes for all nodes and mapped these onto the MCC tree using the “contMap” function in the R package “phytools” ( 36 ).
- Full pipeline: alignment/mapping [phytools] -> structure determination [phytools] -> stage not stated [IQ-TREE v1.6.12, MrBayes v3.2.7a, R v4.0.2]

### Adaptive variation in the upper limits of avian body temperature. (PNAS 2022)

- DOI: 10.1073/pnas.2116645119 | PMCID: PMC9245658 | PMID: 35727970
- Evidence: We subsequently conducted a post hoc multiple comparison taking into account phylogenetic relationships using the PhylANOVA function in the R package “ phytools ” ( 85 ) to obtain pairwise differences in T b max as well as predictor variables between study localities.
- Full pipeline: stage not stated [R v4.0, phytools]

### High exposure of global tree diversity to human pressure. (PNAS 2022)

- DOI: 10.1073/pnas.2026733119 | PMCID: PMC9231180 | PMID: 35709320
- Evidence: We further tested the phylogenetic signal for each imputed trait with the function phylosig in the phytools package ( 125 ), and found four of the eight traits showed significant phylogenetic signals ( SI Appendix , Table S1 ).
- Full pipeline: stage not stated [phytools]

### Ancient proteins resolve controversy over the identity of <i>Genyornis</i> eggshell. (PNAS 2022)

- DOI: 10.1073/pnas.2109326119 | PMCID: PMC9995833 | PMID: 35609205
- Evidence: ( 82 ) and generated a consensus calibrated tree using “consensus.edges” in phytools ( 83 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, MUSCLE v3.8.31] -> stage not stated [AlphaFold, ColabFold, R v4.1, RAxML v1.0.3, phytools]

### Identifying engaging bird species and traits with community science observations. (PNAS 2022)

- DOI: 10.1073/pnas.2110156119 | PMCID: PMC9169790 | PMID: 35412904
- Evidence: We then obtained a consensus tree including branch edges using the R package phytools ( 48 ).
- Full pipeline: stage not stated [R, phytools]

### Physical constraints on thermoregulation and flight drive morphological evolution in bats. (PNAS 2022)

- DOI: 10.1073/pnas.2103745119 | PMCID: PMC9169619 | PMID: 35377801
- Evidence: Seven species missing in the phylogeny were randomly inserted in their genus using functions implemented in the phytools R package ( 63 ).
- Full pipeline: stage not stated [R, phytools]

### Early evolution of diurnal habits in owls (Aves, Strigiformes) documented by a new and exquisitely preserved Miocene owl fossil from China. (PNAS 2022)

- DOI: 10.1073/pnas.2119217119 | PMCID: PMC9169863 | PMID: 35344399
- Evidence: The fossil taxon M. diurna was added to the tree as a sister to the clade S. ulula + Glaucidium using the bind. tip function in phytools ( 61 ), with it added to with the edge length and position set arbitrarily as 0.001 and 0.0005 ( SI Appendix ).
- Full pipeline: structure determination [R, ggplot2] -> stage not stated [MrBayes, phytools]

### The evolution of brain neuron numbers in amniotes. (PNAS 2022)

- DOI: 10.1073/pnas.2121624119 | PMCID: PMC8931369 | PMID: 35254911
- Version used: **0.7**
- Evidence: Ancestral reconstructions of continuous traits were performed using the function fastAnc in the package phytools v0.7 ( 75 ) and the function mvBM in the package evomap ( 76 ).
- Full pipeline: structure determination [phytools v0.7] -> stage not stated [R v4.0.3]

### A milk-sharing economy allows placental mammals to overcome their metabolic limits. (PNAS 2022)

- DOI: 10.1073/pnas.2114674119 | PMCID: PMC8915790 | PMID: 35238685
- Evidence: K was calculated and significance determined using the phylosig function in the “phytools” package ( 97 ) in R.
- Full pipeline: differential/statistical testing [R v4.0.1] -> stage not stated [phytools]

### No link between population isolation and speciation rate in squamate reptiles. (PNAS 2022)

- DOI: 10.1073/pnas.2113388119 | PMCID: PMC8795558 | PMID: 35058358
- Evidence: We determined whether β IBD shows evidence for phylogenetic signal using Pagel’s lambda ( λ ) ( 110 ) as implemented in the R package phytools ( 111 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [GATK v4.1.8, RAxML v8.2.11, SAMtools v1.5] -> stage not stated [R, phytools]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **1.0**
- Evidence: Phylogenetic analyses were performed with ape v5.6-2, phytools v1.0-3, and phylolm v2.6.4 packages.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Bacterial tolerance to host-exuded specialized metabolites structures the maize root microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2310134120 | PMCID: PMC10622871 | PMID: 37878725
- Evidence: The following further R packages were used: Tidyverse ( 80 ), Broom ( 81 ), DECIPHER ( 82 ), DESeq2 ( 83 ), emmeans ( 84 ), ggthemes ( 85 ), multcomp ( 86 ), phyloseq ( 87 ), phytools ( 88 ), and vegan ( 89 ) in combination with some custom functions.
- Full pipeline: alignment/mapping [MAFFT v7.475] -> stage not stated [DESeq2, R, RAxML v8.2.12, emmeans, phyloseq, phytools]

### Development shapes the evolutionary diversification of rodent stripe patterns. (PNAS 2023)

- DOI: 10.1073/pnas.2312077120 | PMCID: PMC10636316 | PMID: 37871159
- Version used: **1.2**
- Evidence: We used a Bayesian method [implemented in phytools version 1.2 ( 61 )] to estimate the value of r , using a gamma prior with β = 1 centered at the maximum likelihood estimate for r .
- Full pipeline: differential/statistical testing [phytools v1.2] -> stage not stated [R]

### The reconstructed cranium of &lt;i&gt;Pierolapithecus&lt;/i&gt; and the evolution of the great ape face. (PNAS 2023)

- DOI: 10.1073/pnas.2218778120 | PMCID: PMC10622906 | PMID: 37844214
- Evidence: 3D geometric morphometric analyses and modeling of these data were carried out in “geomorph” (v.4.0.2; 81 , 82 ) “phytools” (v.1.0-3; 83 ) in R (v.4.1.2; 84 ); the PGLS regression was carried out in “caper” (v.1.0.1; 85 ).
- Full pipeline: differential/statistical testing [R v4.1.2, phytools]

### Clade-specific forebrain cytoarchitectures of the extinct Tasmanian tiger. (PNAS 2023)

- DOI: 10.1073/pnas.2306516120 | PMCID: PMC10410726 | PMID: 37523567
- Evidence: A PGLSs regression was performed using the phytools package ( 60 ), with the Brownian motion correlation structure and branch lengths from the consensus trees of each figure.
- Full pipeline: differential/statistical testing [phytools] -> stage not stated [R]

### Demographic consequences of phenological asynchrony for North American songbirds. (PNAS 2023)

- DOI: 10.1073/pnas.2221961120 | PMCID: PMC10334763 | PMID: 37399376
- Evidence: This matrix was calculated using a consensus phylogenetic tree calculated using the “phytools” package ( 97 ) in R, based on 100 phylogenetic trees obtained from BirdTree ( 98 ) ( www.birdtree.org ).
- Full pipeline: differential/statistical testing [R, tidyverse] -> visualisation [tidyverse] -> stage not stated [Stan, phytools]

### Phylogenomic comparative methods: Accurate evolutionary inferences in the presence of gene tree discordance. (PNAS 2023)

- DOI: 10.1073/pnas.2220389120 | PMCID: PMC10235958 | PMID: 37216509
- Evidence: However, many popular packages for implementing comparative methods—such as phytools ( 59 ), ape ( 60 ), and Geiger ( 61 )—do not take a matrix directly, instead turning an input species tree into a matrix.
- Full pipeline: stage not stated [R, phytools]

### Lizards exploit the changing optics of developing chromatophore cells to switch defensive colors during ontogeny. (PNAS 2023)

- DOI: 10.1073/pnas.2215193120 | PMCID: PMC10161005 | PMID: 37104475
- Evidence: Ancestral states were reconstructed using stochastic character mapping ( 71 ), implemented in the function make.simmap in the phytools package in R ( 72 ).
- Full pipeline: alignment/mapping [R, phytools] -> structure determination [R, phytools]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: The midpoint-rooted sample tree was visualized in R with “phytools” ( 101 ) and “phangorn” ( 102 ).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### The tempo and mode of character evolution in the assembly of mimetic communities. (PNAS 2023)

- DOI: 10.1073/pnas.2203724120 | PMCID: PMC9910590 | PMID: 36577073
- Evidence: We fit four evolutionary models to each PC axis using R package phytools : Brownian motion, early burst, Ornstein–Uhlenbeck, and lambda.
- Full pipeline: quantification [R] -> stage not stated [ImageJ, phytools]

### Order of amino acid recruitment into the genetic code resolved by last universal common ancestor's protein domains. (PNAS 2024)

- DOI: 10.1073/pnas.2410311121 | PMCID: PMC11670089 | PMID: 39665745
- Evidence: We re-estimated the branch lengths of the reconciled Pfam trees in IQ-Tree using the NQ.PFAM substitution model with no rate heterogeneity, then performed midpoint rooting using the phytools R package ( 93 ) on these re-estimated branch lengths.
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [MAFFT] -> stage not stated [InterProScan, R, phytools]

### Emergent collective behavior evolves more rapidly than individual behavior among acorn ant species. (PNAS 2024)

- DOI: 10.1073/pnas.2420078121 | PMCID: PMC11621464 | PMID: 39576350
- Evidence: Phylomorphospace plots were generated with the phytools package in R.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R] -> stage not stated [IQ-TREE v2.1.2, phytools]

### A global assessment of plant-mite mutualism and its ecological drivers. (PNAS 2024)

- DOI: 10.1073/pnas.2309475121 | PMCID: PMC11621742 | PMID: 39560650
- Evidence: We used corHMM to simulate stochastic character maps (“simmaps”) and infer ancestral states under each model as well as phytools to calculate the simulated number of transitions between states and visualized the inferred phylogenetic distribution of lineages with the precursor state (estimated to have evolved 160 to 210 times) using shiftPlot .
- Full pipeline: simulation/modelling [phytools] -> visualisation [phytools] -> stage not stated [R]

### Ecology and life history predict avian nest success in the global tropics. (PNAS 2024)

- DOI: 10.1073/pnas.2402652121 | PMCID: PMC11621757 | PMID: 39556725
- Evidence: 2 A ), we estimated ancestral states using maximum likelihood in the phytools R package ( 98 ).
- Full pipeline: stage not stated [R, metafor, phytools]

### Homeotic and nonhomeotic patterns in the tetrapod vertebral formula. (PNAS 2024)

- DOI: 10.1073/pnas.2411421121 | PMCID: PMC11588047 | PMID: 39527744
- Evidence: We confirmed our calculations with the widely used ape ( 83 ) and phytools ( 84 ) R libraries and include the scripts in an electronic repository ( 42 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [BLAST, BUSCO, SciPy, phytools]

### Asymmetric winter warming reduces microbial carbon use efficiency and growth more than symmetric year-round warming in alpine soils. (PNAS 2024)

- DOI: 10.1073/pnas.2401523121 | PMCID: PMC11513915 | PMID: 39401358
- Evidence: We assessed phylogenetic clustering to examine variations in growing absolute growth rate among microbial species and phylogenetic groups, using Pagel’s λ ( 83 ) and Blomberg’s K ( 84 ) phylogenetic signal tests (using the “ phytools ” and “ picante ” packages).
- Full pipeline: dimensionality reduction/clustering [phytools] -> stage not stated [R, lme4]

### Phylogenetic evidence clarifies the history of the extrusion of Indochina. (PNAS 2024)

- DOI: 10.1073/pnas.2322527121 | PMCID: PMC11363272 | PMID: 39159371
- Version used: **0.7**
- Evidence: Ancestral climatic niches were reconstructed for each of the 24 clades using the ML method in phytools v0.7-80, which can analyze continuous characters with missing data ( 59 ).
- Full pipeline: differential/statistical testing [RAxML v8.2.10] -> structure determination [phytools v0.7]

### Flexible oviposition behavior enabled the evolution of terrestrial reproduction. (PNAS 2024)

- DOI: 10.1073/pnas.2312371121 | PMCID: PMC11295038 | PMID: 39042675
- Evidence: The phylogeny of Dendropsophus and its outgroup was used to estimate ancestral states of reproduction as both a categorical variable (aquatic, terrestrial, or flexible) using the ace function in the ape package ( 41 ) and as a continuous variable ranging from 0 (completely aquatic oviposition) to 1 (completely terrestrial reproduction) using the anc.ML function in the phytools package ( 42 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2] -> stage not stated [ImageJ, RAxML v1.0.3, emmeans, lme4, phytools]

### Multiple evolutionary pressures shape identical consonant avoidance in the world's languages. (PNAS 2024)

- DOI: 10.1073/pnas.2316677121 | PMCID: PMC11228491 | PMID: 38917001
- Evidence: Data were processed using Python 3 as well as version 0.6-99 of the R package phytools ( 99 ).
- Full pipeline: stage not stated [Python, R, Stan v2.26.13, phytools]

### Bacterial lifestyle shapes pangenomes. (PNAS 2024)

- DOI: 10.1073/pnas.2320170121 | PMCID: PMC11126918 | PMID: 38743630
- Evidence: In cases where we had multiple species within a single genus, we used the R package “phytools” to add these species as additional branches in the tree ( 51 ).
- Full pipeline: stage not stated [R, phytools]

### Linking fine root lifespan to root chemical and morphological traits-A global analysis. (PNAS 2024)

- DOI: 10.1073/pnas.2320623121 | PMCID: PMC11032481 | PMID: 38607930
- Evidence: To evaluate the phylogenetic influence on plant traits and their correlations, we tested Blomberg’s K using the phytools R package.
- Full pipeline: stage not stated [R, phytools]

### Significant shifts in latitudinal optima of North American birds. (PNAS 2024)

- DOI: 10.1073/pnas.2307525121 | PMCID: PMC11009622 | PMID: 38557189
- Evidence: To create a phylogenetic correlation matrix among species, we first obtained 999 ultrametric phylogenetic trees from the BirdTree project ( http://birdtree.org ) ( 102 ) and computed a consensus majority rule phylogenetic tree ( 103 ) using the consensus.edges function of the phytools R package ( 104 ).
- Full pipeline: stage not stated [R, ape (R), metafor, phytools]

### Functional constraints on the number and shape of flight feathers. (PNAS 2024)

- DOI: 10.1073/pnas.2306639121 | PMCID: PMC10895369 | PMID: 38346196
- Evidence: In order to study the evolution of remex and rectrix number and primary vane asymmetry, as well as to estimate and visualize the ancestral state of these traits, we used an ancestral trait reconstruction analysis under a continuous-time Markov chain model in the R package “phytools” (version 0.6-99; Phylogenetic Tools for Comparative Biology) ( 85 ).
- Full pipeline: normalisation [R] -> structure determination [phytools] -> visualisation [phytools]

### Pollen nutrition structures bee and plant community interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2317228120 | PMCID: PMC10801918 | PMID: 38190523
- Evidence: We tested for phylogenetic signal (Pagel’s λ and Blomberg’s K) in pollen nutrition using the R packages “ ape” ( 90 ) , “pez” ( 91 ), and “phytools” ( 92 ).
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [Stan] -> stage not stated [phytools]

### The olfactory bulb endocast as a proxy for mammalian olfaction. (PNAS 2025)

- DOI: 10.1073/pnas.2510575122 | PMCID: PMC12718348 | PMID: 41359846
- Evidence: All the analyses and plots were performed with R ( 62 ) and the following packages: APE ( 63 ), phytools ( 64 ), and ggplot2 ( 65 ).
- Full pipeline: stage not stated [BUSCO, ggplot2, phytools]

### Nitrogen-fixing microbes gain genes in diverse types of living environments. (PNAS 2025)

- DOI: 10.1073/pnas.2523106122 | PMCID: PMC12685144 | PMID: 41296715
- Evidence: To account for the nonindependence of species due to shared evolutionary history, we conducted a PGLS ( 44 ) analysis using the R packages ape ( 104 ), caper ( 105 ), and phytools ( 45 ).
- Full pipeline: stage not stated [phytools]

### Biodiversity conservation requires consideration of different life history stages. (PNAS 2025)

- DOI: 10.1073/pnas.2507870122 | PMCID: PMC12663988 | PMID: 41264235
- Evidence: For species not in the tree but the phylogenetic position is clear, we used the bind.tip function of the phytools package ( 46 ) to insert them at the corresponding positions according to the relevant literature.
- Full pipeline: stage not stated [ImageJ, R, phytools]

### When islands collide: Divergence predicts outcomes of secondary contact during the fusion of Sulawesi's paleo-archipelago. (PNAS 2025)

- DOI: 10.1073/pnas.2514344122 | PMCID: PMC12625910 | PMID: 41144686
- Version used: **2.3**
- Evidence: We ran two separate ancestral character estimation analyses on these data modeling state changes using Brownian motion, one on the bifurcating topology using phytools v.2.3 ( 83 ) and one on the network topology using PhyloTraits ( 84 ) by manually joining the two nonghost hybrid edges.
- Full pipeline: stage not stated [IQ-TREE v2.1.1, RAxML v8.2.12, phytools v2.3]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Evidence: To infer body size across the Gobioidei phylogeny, we used a maximum likelihood ancestral character state reconstruction for TL using the “fastAnc” function in the phytools package ( 77 ) in R v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Heterochronic shifts in a timing-keeping microRNA are associated with multiple instances of neoteny in plants. (PNAS 2025)

- DOI: 10.1073/pnas.2510697122 | PMCID: PMC12541458 | PMID: 41060751
- Version used: **1.9.1**
- Evidence: Ancestral character reconstruction was implemented using phytools v1.9.1 ( 51 , 52 ).
- Full pipeline: differential/statistical testing [ggplot2] -> structure determination [phytools v1.9.1] -> stage not stated [RAxML v8.2]

### Duplication of a conserved mitochondrial enzyme gene arms parasitoid wasps with venom cytotoxicity and oogenesis regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2512820122 | PMCID: PMC12501140 | PMID: 40996803
- Evidence: The maximum-likelihood ancestral state reconstruction was performed using the R packages ape (Paradis et al., ( 70 )) v5.8, geiger ( 71 ) v2.0.11, and phytools (Revell, ( 72 )) v2.3-0.
- Full pipeline: quality control [fastp] -> alignment/mapping [MAFFT] -> quantification [fastp] -> structure determination [phytools] -> stage not stated [AlphaFold, BLAST, HMMER]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: 27 using the function fitMk in R package phytools ( 65 ).
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### Keys to the global treeline formation: Thermal limit for its position and moisture for the taxon-specific variation. (PNAS 2025)

- DOI: 10.1073/pnas.2504685122 | PMCID: PMC12377724 | PMID: 40794829
- Evidence: We used the “phylosig” function in the “phytools” R package ( 88 ) to calculate λ.
- Full pipeline: stage not stated [R, phytools]

### Prevalence of monogamy at the level of flowers in plants. (PNAS 2025)

- DOI: 10.1073/pnas.2506724122 | PMCID: PMC12358840 | PMID: 40758893
- Evidence: These analyses were conducted using the R package phytools ( 31 ).
- Full pipeline: stage not stated [R, phytools]

### Six million years of vole dental evolution shaped by tooth development. (PNAS 2025)

- DOI: 10.1073/pnas.2505624122 | PMCID: PMC12337299 | PMID: 40743389
- Version used: **1.9**
- Evidence: We used Maximum Likelihood (ML) ancestral character state reconstruction under a time-reversible continuous discrete Markov process—the extended M k model for discrete character evolution ( 93 – 95 )—implemented in phytools 1.9-16 ( 96 ) to estimate the evolution of the number of cusps of the first lower molar for 15 nested character transition models ( SI Appendix , Fig.
- Full pipeline: structure determination [phytools v1.9] -> stage not stated [ImageJ v1.53c]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Evidence: S5 B ) did not converge, also not using an “optimized relaxed molecular clock.” Phylogenies were visualized using the packages “ape” (v5.7-1) and “phytools” (v2.1-1) in R ( 106 , 107 ) and FigTree (v1.1.4) ( http://tree.bio.ed.ac.uk/software/figtree/ ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Mutualisms within light microhabitats are associated with sensory convergence in a mimetic butterfly community. (PNAS 2025)

- DOI: 10.1073/pnas.2422397122 | PMCID: PMC12305024 | PMID: 40663600
- Evidence: ( 19 ) (packages phytools and ape ) ( 62 , 63 ).
- Full pipeline: stage not stated [ImageJ, Python, R, lme4, phytools]

### Climate-linked biogeography of mycorrhizal fungal spore traits. (PNAS 2025)

- DOI: 10.1073/pnas.2505059122 | PMCID: PMC12304957 | PMID: 40663605
- Evidence: To visualize trait variation across the phylogeny, we standardized traits to z-scores and constructed a phylogenetic heatmap using the “phytools” package in R ( 91 ).
- Full pipeline: visualisation [phytools] -> stage not stated [R v4.4.3]

### The evolution of male-female dominance relations in primate societies. (PNAS 2025)

- DOI: 10.1073/pnas.2500405122 | PMCID: PMC12280975 | PMID: 40623178
- Evidence: We estimated the strength of the phylogenetic signal for both the quantitative and the qualitative measure of intersexual dominance using the function phylosig in the package “phytools” ( 74 ) in R to calculate the K -statistic ( 75 ), assessing their significance by comparison to 10,000 simulations.
- Full pipeline: differential/statistical testing [R v4.2.2, phytools] -> simulation/modelling [Stan, phytools]

### Herbarium specimens reveal a constrained seasonal climate niche despite diverged annual climates across a wildflower clade. (PNAS 2025)

- DOI: 10.1073/pnas.2503670122 | PMCID: PMC12280893 | PMID: 40591614
- Version used: **1.9.16**
- Evidence: To test whether species retained traits of their ancestral niches as they diverged, we evaluated which model(s) of evolution provided the best fit for the evolution of climate niche traits ( 35 ) using the functions bounded_bm() from phytools v.1.9.16 ( 37 ) and fitContinuous() from geiger v.2.0.11 ( 75 ).
- Full pipeline: stage not stated [R, phytools v1.9.16]

### Parallel sensory compensation following independent subterranean colonization by groundwater salamanders (&lt;i&gt;Eurycea&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2504850122 | PMCID: PMC12168003 | PMID: 40460121
- Version used: **2.3**
- Evidence: Ancestral state reconstruction on both continuous and discrete traits was performed using the R packages ape version 5.8 ( 102 ) and phytools version 2.3-0 ( 103 ).
- Full pipeline: read trimming [MAFFT v4.475] -> alignment/mapping [MAFFT v4.475] -> differential/statistical testing [R] -> structure determination [phytools v2.3] -> stage not stated [IQ-TREE v2.3.4]

### Independent transitions to fully planktonic life cycles shaped the global distribution of medusozoans in the epipelagic zone. (PNAS 2025)

- DOI: 10.1073/pnas.2415979122 | PMCID: PMC12146771 | PMID: 40440075
- Evidence: The evolution of the colonized bathymetric depth and the acCDOM was estimated by mapping their median values onto the OTUs phylogenetic tree using the anc.ML function from the phytools [v.
- Full pipeline: alignment/mapping [BLAST, phytools] -> differential/statistical testing [tidyverse, vegan] -> stage not stated [R, igraph]

### Distinct latitudinal patterns of molecular rates across vertebrates. (PNAS 2025)

- DOI: 10.1073/pnas.2423386122 | PMCID: PMC12088427 | PMID: 40339119
- Evidence: Phylogenetic signals were computed using Pagel’s λ in the phytools ( 53 ).
- Full pipeline: stage not stated [R, RAxML v8.2.4, phytools]

### Lateral jaw motion in fish expands the functional repertoire of vertebrates and underpins the success of a dominant herbivore lineage. (PNAS 2025)

- DOI: 10.1073/pnas.2418982122 | PMCID: PMC12088409 | PMID: 40324084
- Evidence: To assess the phylogenetic history of lateral jaw rotation (presence/absence), we carried out an ancestral reconstruction using stochastic character mapping ( simmap ) in the phytools R package ( 77 ).
- Full pipeline: alignment/mapping [phytools] -> structure determination [phytools] -> stage not stated [ImageJ, R, ggplot2]

### Dynamic interplay between niche variation and flight adaptability drove a hundred million years' dispersion in iconic lacewings. (PNAS 2025)

- DOI: 10.1073/pnas.2414549122 | PMCID: PMC12087969 | PMID: 40314968
- Evidence: Based on the time-calibrated phylogeny, LTT plot was obtained utilizing the R package “phytools” ( 83 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7, ggplot2] -> stage not stated [NCO, R, phytools]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Evidence: We generated 100 stochastic maps of ancestral character reconstruction using the R package phytools ( 85 ) with the same transition matrix.
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### A selfish supergene causes meiotic drive through both sexes in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421185122 | PMCID: PMC12054836 | PMID: 40267129
- Evidence: We used phytools in R ( 62 ) to root each tree with D. putrida as the outgroup and inferred the topology of the X, X D , and D. neotestacea copies.
- Full pipeline: alignment/mapping [BEDTools, MAFFT] -> stage not stated [Flye v2.9, Pilon v1.24, R v4.3.0, phytools]

### Nonnative tree invaders lead to declines in native tree species richness. (PNAS 2025)

- DOI: 10.1073/pnas.2424908122 | PMCID: PMC12054818 | PMID: 40258149
- Version used: **2.1.1**
- Evidence: Comparison of this phylogenetic tree with the FIA plot data identified 35 species that were missing from the phylogeny; we added each missing species to its respective genus in the phylogeny as part of a polytomy, using add.species.to.genus in phytools version 2.1.1 ( 81 ).
- Full pipeline: stage not stated [phytools v2.1.1]

### &lt;i&gt;Sinorhizobium meliloti&lt;/i&gt; FcrX coordinates cell cycle and division during free-living growth and symbiosis by a ClpXP-dependent mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2412367122 | PMCID: PMC11929396 | PMID: 40073061
- Evidence: Ancestral state reconstruction of distances was performed and mapped on trees with function contMap from the R package phytools ( 58 ).
- Full pipeline: alignment/mapping [R, phytools] -> structure determination [R, phytools] -> stage not stated [ImageJ]

### Innovation in ant larval feeding facilitated queen-worker divergence and social complexity. (PNAS 2025)

- DOI: 10.1073/pnas.2413742122 | PMCID: PMC11892636 | PMID: 39999174
- Evidence: For each trait (i.e., body volume of queens and workers and queen–worker dimorphism), we assessed their phylogenetic signal in the data by calculating Pagel’s lambda and Blomberg’s K with the R package phytools ( 99 ) (v.1.9.16).
- Full pipeline: stage not stated [ImageJ, R, phytools]

### Divergence time and environmental similarity predict the strength of morphological convergence in stick and leaf insects. (PNAS 2025)

- DOI: 10.1073/pnas.2319485121 | PMCID: PMC11725862 | PMID: 39715436
- Evidence: We substituted original measurement values with the residuals calculated from a phylogenetically corrected linear regression against body volume (R package “phytools”) ( 50 , 70 ), after log 10 -transformation.
- Full pipeline: alignment/mapping [BEAST v2.6.3] -> differential/statistical testing [BEAST v2.6.3, R, phytools] -> structure determination [BEAST v2.6.3]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Evidence: Ancestral state reconstruction was conducted using the “phytools” package (v2.4.4) ( 93 ) in R.
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

### DNA methylation in invertebrate genomes and cell lineage plasticity. (PNAS 2026)

- DOI: 10.1073/pnas.2510416123 | PMCID: PMC13012060 | PMID: 41790947
- Evidence: The tree was processed using the R packages ape ( 92 ) and phytools ( 93 ) and ultrametricized by non-negative least squares (NNLS).
- Full pipeline: quality control [Bismark v0.24.0, Trim Galore v0.6.10] -> read trimming [Bismark v0.24.0, Trim Galore v0.6.10] -> alignment/mapping [Bismark v0.24.0, Trim Galore v0.6.10] -> stage not stated [R v4.5, emmeans, phytools]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Evidence: We visualized the sum of genes for each of naphthalene degradation, catechol meta- and ortho-cleavage, protocatechuate ortho- and meta-cleavage, and N-acquisition pathways alongside the species tree generated with Orthofinder using the plotTree.barplot function of Phytools ( https://cran.r-project.org/web/packages/phytools/index.html ) in R v.4.3.2 ( 78 ).
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

