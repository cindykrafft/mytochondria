# BEAST

- **Category:** phylogenetics
- **Papers in survey:** 67
- **Journals:** PNAS (41), Nature (20), Cell (4), Science (2)
- **Years:** 2021 (15), 2022 (9), 2023 (8), 2024 (10), 2025 (17), 2026 (8)
- **Versions named:** 1.10.4 (7), 2.6.6 (7), 2.6.7 (3), 2.6 (3), 6.6 (3), 1.10.5 (2), 2.6.0 (2), 1.10 (2), 2.5.2 (2), 2.6.3 (2)
- **Pipeline stages it appears in:** differential/statistical testing (25), structure determination (9), simulation/modelling (5), alignment/mapping (4), normalisation (2), machine learning (1)

## Papers

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Version used: **1.10**
- Evidence: Finally, using the time-scaled maximum-likelihood tree as a fixed topology, we performed Bayesian inference of ancestral states (discrete phylogeographic reconstruction) using BEAST v.1.10 ( Suchard et al., 2018 ), for 15x10 6 generations, sampling every 1,000 generations, which led to MCMC convergence and good mixing, with all parameters showing ESS > 200 when assessed using Tracer 1.7 ( Rambaut ...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### Evaluating the Effects of SARS-CoV-2 Spike Mutation D614G on Transmissibility and Pathogenicity. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.020 | PMCID: PMC7674007 | PMID: 33275900
- Evidence: ...ng http://www.R-project.org BEAST1 v1.10.5 ( Suchard et al., 2018 ) https://beast.community/ Tracer ( Rambaut et al., 2018 ) https://beast.community/ BEAST2 PhyDyn ( Bouckaert et al., 2019 ; Volz and Siveroni, 2018 ) https://github.com/mrc-ide/PhyDyn ARTIC network protocol ARTIC network https://artic.network/ncov-2019 R packages ( treedater 0.5.1, ape package v.
- Full pipeline: differential/statistical testing [R v3.6] -> stage not stated [BEAST, IQ-TREE, Nextflow, brms v2.13.5]

### Genome-wide data from medieval German Jews show that the Ashkenazi founder event pre-dated the 14<sup>th</sup> century. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.002 | PMCID: PMC9793425 | PMID: 36455558
- Version used: **2.6.6**
- Evidence: Estimating the time to the most recent common ancestor (TMRCA) of the K1a1ba1 carriers To estimate the TMRCA of the K1a1ba1 lineage, we used a Bayesian coalescent analysis, as implemented in BEAST 2 (v2.6.6) ( Bouckaert et al., 2019 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BCFtools, BWA v0.7.15] -> quantification [SAMtools] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [BEAST v2.6.6] -> visualisation [ggplot2] -> stage not stated [ADMIXTURE, R]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Version used: **2.6.6**
- Evidence: ...2 ( Capella-Gutiérrez et al., 2009 ) http://trimal.cgenomics.org RAxML v8.2.12 ( Stamatakis, 2014 ) https://cme.h-its.org/exelixis/web/software/raxml BEAST2 v2.6.6 ( Bouckaert et al., 2014 ) https://www.beast2.org CmdStan v2.28.1 The Stan Development Team https://mc-stan.org CmdStanr v0.4.0 The Stan Development Team https://mc-stan.org/cmdstanr/ R v4.1.2 The R Foundation https://www.r-project.org/...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Triangulation supports agricultural spread of the Transeurasian languages. (Nature 2021)

- DOI: 10.1038/s41586-021-04108-8 | PMCID: PMC8612925 | PMID: 34759322
- Version used: **2.6**
- Evidence: All posterior estimates were performed using BEAST v.2.6 52 using adaptive coupled Markov chain Monte Carlo (MCMC) 53 .
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12, SAMtools v1.3] -> simulation/modelling [BEAST v2.6]

### Leprosy in wild chimpanzees. (Nature 2021)

- DOI: 10.1038/s41586-021-03968-4 | PMCID: PMC8550970 | PMID: 34646009
- Version used: **2.5.2**
- Evidence: Dating analysis Dating analyses were performed using BEAST2 (v.2.5.2) 67 as described previously 24 with 278 genomes and an increased chain length from 50 to 100 million.
- Full pipeline: stage not stated [BEAST v2.5.2]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **2.5.1**
- Evidence: BEAST2 (v.2.5.1) 93 was used to infer the divergence times between genomes using a GTR model of substitution with 4 gamma categories.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Context-specific emergence and growth of the SARS-CoV-2 Delta variant. (Nature 2022)

- DOI: 10.1038/s41586-022-05200-3 | PMCID: PMC9534748 | PMID: 35952712
- Version used: **1.10**
- Evidence: We then reconstructed the geographic movement of nodes on a fixed tree (pruned from the overall maximum clade credibility (MCC) tree) in BEAST v.1.10 46 , using a relaxed random walk model 53 , and a Cauchy distribution to account for among-branch heterogeneity in dispersal velocity.
- Full pipeline: alignment/mapping [minimap2] -> structure determination [BEAST v1.10] -> visualisation [Python] -> stage not stated [Pangolin]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Version used: **6.6**
- Evidence: For the molecular dating analysis, we used the Bayesian statistical framework BEAST2 v.6.6 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Version used: **1.10.4**
- Evidence: Time-calibrated BEAST analysis To estimate a time-scale and growth rate from the genome sequencing data, BEAST (v.1.10.4) 70 , 71 was used to sample phylogenetic trees under an exponential growth coalescent model using a strict molecular clock.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### Indigenous Australian genomes show deep structure and rich novel variation. (Nature 2023)

- DOI: 10.1038/s41586-023-06831-w | PMCID: PMC10733150 | PMID: 38093005
- Version used: **2.6.0**
- Evidence: Mitochondrial phylogenies were inferred using BEAST (v.2.6.0) 79 , and maximum clade credibility trees were produced with TreeAnnotator 79 .
- Full pipeline: variant calling [GATK v3.8] -> normalisation [R v5.1] -> dimensionality reduction/clustering [R v5.1, UMAP v0.2.7.0] -> stage not stated [ADMIXTURE v1.3, BCFtools, BEAST v2.6.0, PLINK, ggplot2]

### Ancient human DNA recovered from a Palaeolithic pendant. (Nature 2023)

- DOI: 10.1038/s41586-023-06035-2 | PMCID: PMC10247382 | PMID: 37138083
- Version used: **2.6.6**
- Evidence: Tree building and genetic dating were performed using BEAST2 (version 2.6.6) 54 .
- Full pipeline: differential/statistical testing [R] -> stage not stated [BEAST v2.6.6]

### Geographical migration and fitness dynamics of Streptococcus pneumoniae. (Nature 2024)

- DOI: 10.1038/s41586-024-07626-3 | PMCID: PMC11236706 | PMID: 38961295
- Version used: **1.10.4**
- Evidence: We compared concordance between BEAST (v.1.10.4) 63 with both strict and relaxed clocks, and a Bayesian skyline prior.
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SAMtools] -> registration [SAMtools] -> differential/statistical testing [BEAST v1.10.4, R v3.6.2] -> stage not stated [RAxML]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Maximum clade credibility tree produced using BEAST2 with the optimized relaxed clock and Bayesian coalescent skyline models.
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Homo sapiens reached the higher latitudes of Europe by 45,000 years ago. (Nature 2024)

- DOI: 10.1038/s41586-023-06923-7 | PMCID: PMC10849966 | PMID: 38297117
- Version used: **2.6.6**
- Evidence: A phylogenetic tree relating these mtDNA genomes was generated using BEAST2 v2.6.6 (ref.
- Full pipeline: alignment/mapping [BWA] -> registration [MAFFT v7.453] -> structure determination [MAFFT v7.453] -> stage not stated [BEAST v2.6.6, QGIS, R v4.1, SAMtools]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Version used: **2.6.7**
- Evidence: Molecular clock dating We used the Bayesian phylogenetics package BEAST2 v2.6.7 119 to estimate a time-calibrated phylogeny of the context dataset of 98 T. pallidum genomes along with our new ancient genome, ZH1540.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Picuris Pueblo oral history and genomics reveal continuity in US Southwest. (Nature 2025)

- DOI: 10.1038/s41586-025-08791-9 | PMCID: PMC12137115 | PMID: 40307544
- Version used: **2.6**
- Evidence: 108 ) and BEAST v.2.6 (ref.
- Full pipeline: quality control [ANGSD v0.931] -> variant calling [BCFtools v1.17] -> stage not stated [ADMIXTURE, BEAST v2.6, Picard v2.25.0, SAMtools v1.3.1]

### Fine-scale patterns of SARS-CoV-2 spread from identical pathogen sequences. (Nature 2025)

- DOI: 10.1038/s41586-025-08637-4 | PMCID: PMC11964829 | PMID: 40044856
- Version used: **1.10.4**
- Evidence: DTA We conduct phylogeographical inference using symmetric DTA 14 using the Bayesian stochastic search variable selection (BSSVS) model implemented in BEAST (v.1.10.4) 61 applied to the synthetic data simulated in our two sequencing scenarios.
- Full pipeline: dimensionality reduction/clustering [vegan] -> differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [Nextstrain, R, ape (R), igraph]

### Learning the fitness dynamics of pathogens from phylogenies. (Nature 2025)

- DOI: 10.1038/s41586-024-08309-9 | PMCID: PMC11735385 | PMID: 39743587
- Version used: **1.10.4**
- Evidence: For B. pertussis , the time tree was reconstructed using BEAST v.1.10.4 52 , under a GTR substitution model 18 accounting for the number of constant sites, a relaxed lognormal clock model 53 and a skygrid population size model 54 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BWA, GATK, MAFFT] -> structure determination [BEAST v1.10.4] -> stage not stated [Stan]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Evidence: In a second step, we compared the fit of a strict clock and an uncorrelated log-normal relaxed clock using path sampling 41 , as implemented in the BEAST 2 model selection package 38 .
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Version used: **1.10.5**
- Evidence: Phylogenetic reconstruction Alphacoronavirus spike gene sequences of the 40 selected strains, in addition to those representing the local phylogeny of CcCoV-KY43, were aligned using MAFFT (v.7.526) 49 and molecular clock calibration was performed in BEAST (v.1.10.5) 74 .
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### Dogs were widely distributed across western Eurasia during the Palaeolithic. (Nature 2026)

- DOI: 10.1038/s41586-026-10170-x | PMCID: PMC13017512 | PMID: 41882128
- Version used: **2.6.7**
- Evidence: 82 ) (HKY + F + I + G4; 1,000 bootstrap replicates) rooted against a coyote, and a time-calibrated Bayesian tree in BEAST2 v.2.6.7 (ref.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.505] -> differential/statistical testing [BEAST v2.6.7] -> stage not stated [ADMIXTURE v1.3.0]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **1.10.5**
- Evidence: We used this reduced dataset for further analyses with BEAST v.1.10.5, under strict and uncorrelated log-normal relaxed clock models 55 .
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### Ecology and spread of the North American H5N1 epizootic. (Nature 2026)

- DOI: 10.1038/s41586-025-09737-x | PMCID: PMC12779553 | PMID: 41225000
- Version used: **1.10.4**
- Evidence: Phylodynamic analysis The following Bayesian phylogenetic reconstructions and analyses were performed using BEAST (v.1.10.4) 75 .
- Full pipeline: alignment/mapping [MAFFT v7.5.20] -> differential/statistical testing [BEAST v1.10.4] -> structure determination [BEAST v1.10.4] -> stage not stated [Nextstrain]

### Accounting for spatial sampling patterns in Bayesian phylogeography. (PNAS 2021)

- DOI: 10.1073/pnas.2105273118 | PMCID: PMC8719894 | PMID: 34930835
- Evidence: 22 and implemented in the popular Bayesian samplers BEAST ( 17 ) and BEAST2 ( 18 ).
- Full pipeline: differential/statistical testing [BEAST]

### Anatomy of an extensively drug-resistant <i>Klebsiella pneumoniae</i> outbreak in Tuscany, Italy. (PNAS 2021)

- DOI: 10.1073/pnas.2110227118 | PMCID: PMC8640832 | PMID: 34819373
- Version used: **2.6.5**
- Evidence: To date, internal nodes of interest on the phylogeny and Bayesian phylogenetic inference were performed using BEAST 2 v2.6.5 ( 46 ) under a coalescent constant population model using tip dates and a mean clock rate constrained to 1.45 × 10 −6 substitutions per site per year, based on a previously reported evolution rate for the ST-147 lineage ( 47 ).
- Full pipeline: differential/statistical testing [BEAST v2.6.5] -> machine learning [BEAST v2.6.5] -> stage not stated [BLAST]

### Relict inland mangrove ecosystem reveals Last Interglacial sea levels. (PNAS 2021)

- DOI: 10.1073/pnas.2024518118 | PMCID: PMC8522267 | PMID: 34607943
- Evidence: For this analysis, we used the Bayesian Markov Chain Monte Carlo (MCMC) sampler SNAPP ( 37 ), which we ran through the BEAST2 package ( 38 ).
- Full pipeline: differential/statistical testing [BEAST] -> simulation/modelling [BEAST] -> stage not stated [Python, VCFtools v0.1.14]

### Fifty million years of beetle evolution along the Antarctic Polar Front. (PNAS 2021)

- DOI: 10.1073/pnas.2017384118 | PMCID: PMC8214695 | PMID: 34108239
- Version used: **2.5**
- Evidence: Divergence dates among Ectemnorhinini were estimated from our five-gene dataset by linking gene trees, as implemented in BEAST v.2.5 ( 94 ), and by coestimating gene trees embedded in a shared species tree, as implemented in starBEAST ( 95 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Clustal Omega, MAFFT] -> dimensionality reduction/clustering [R, RAxML] -> differential/statistical testing [MrBayes v3.2.6] -> structure determination [MAFFT] -> stage not stated [BEAST v2.5]

### Herded and hunted goat genomes from the dawn of domestication in the Zagros Mountains. (PNAS 2021)

- DOI: 10.1073/pnas.2100901118 | PMCID: PMC8237664 | PMID: 34099576
- Evidence: Uniparental trees were built with phyML3.0 ( 78 ) and BEAST2 ( 79 ).
- Full pipeline: alignment/mapping [MUSCLE] -> registration [MUSCLE] -> differential/statistical testing [ANGSD] -> stage not stated [BCFtools v1.5, BEAST]

### The evolution and changing ecology of the African hominid oral microbiome. (PNAS 2021)

- DOI: 10.1073/pnas.2021655118 | PMCID: PMC8157933 | PMID: 33972424
- Evidence: An input file of the consensus sequences and references was generated in BEAUTi and used to run BEAST2 ( 104 ) for Bayesian skyline plot analysis.
- Full pipeline: alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [BEAST, R] -> stage not stated [BEDTools]

### Multiple independent recombinations led to hermaphroditism in grapevine. (PNAS 2021)

- DOI: 10.1073/pnas.2023548118 | PMCID: PMC8053984 | PMID: 33837155
- Version used: **2.5.2**
- Evidence: Genetic divergence for the ML phylogeny was estimated by Bayesian analysis with the software BEAST v.2.5.2 with a relaxed molecular clock for 80 × 10 6 Markov chain Monte–Carlo cycles ( 41 ).
- Full pipeline: variant calling [RAxML v8.2.4] -> differential/statistical testing [BEAST v2.5.2] -> stage not stated [RepeatMasker]

### Predicting transcriptional responses to cold stress across plant species. (PNAS 2021)

- DOI: 10.1073/pnas.2026330118 | PMCID: PMC7958178 | PMID: 33658387
- Version used: **5.1**
- Evidence: StarBEAST2 (v0.15.5) ( 61 ) implemented in BEAST 2.5.1 ( 62 ) employing a Bayesian Markov chain Monte Carlo (MCMC) framework was used to estimate both species trees and divergence dates.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [HTSeq v0.6.1, MAFFT v7.149, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [BEAST v5.1, DESeq2] -> simulation/modelling [BEAST v5.1] -> stage not stated [R]

### The origin and early spread of SARS-CoV-2 in Europe. (PNAS 2021)

- DOI: 10.1073/pnas.2012008118 | PMCID: PMC7936359 | PMID: 33571105
- Evidence: For inferences, we used the implementation of the multitype birth–death model in the bdmm package ( 39 , 42 ) in the BEAST2 software ( 43 ).
- Full pipeline: alignment/mapping [Nextstrain] -> stage not stated [BEAST]

### A modern scleractinian coral with a two-component calcite-aragonite skeleton. (PNAS 2021)

- DOI: 10.1073/pnas.2013316117 | PMCID: PMC7826372 | PMID: 33323482
- Evidence: Uncorrelated relaxed molecular clock with a log-normal distribution was run on BEAST2 ( 62 ) under the Yule speciation process ( 63 ) and calibrated using the following time points: Acropora , 55 My; Dendrophylliidae, 127 My; Poritidae/Dendrophylliidae, 130 My; Agariciidae, 220 My; and Pocilloporidae, 70 My.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [BEAST, RAxML]

### Multiclonal human origin and global expansion of an endemic bacterial pathogen of livestock. (PNAS 2022)

- DOI: 10.1073/pnas.2211217119 | PMCID: PMC9897428 | PMID: 36469788
- Evidence: Finally, we also performed tip permutation to assess the effects of uneven numbers of sequences in categories in BEAST2 and BaTS ( 33 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36] -> alignment/mapping [phytools] -> differential/statistical testing [BEAST, R] -> simulation/modelling [phytools] -> structure determination [phytools] -> stage not stated [InterProScan v5.52, Prokka v1.13]

### Phylogeographic analysis of the Bantu language expansion supports a rainforest route. (PNAS 2022)

- DOI: 10.1073/pnas.2112853119 | PMCID: PMC9372543 | PMID: 35914165
- Evidence: We ran each analysis for 400,000,000 generations in BEAST 2 ( 76 ).
- Full pipeline: stage not stated [BEAST, R]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **2.6.0**
- Evidence: To estimate the relationships among the sampled subspecies, we constructed a population-level tree using the BEAST2 v.2.6.0 application SNAPP, a multispecies coalescent-based tool that uses biallelic markers as input ( 83 – 85 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### The enigmatic tropical alpine flora on the African sky islands is young, disturbed, and unsaturated. (PNAS 2022)

- DOI: 10.1073/pnas.2112737119 | PMCID: PMC9295768 | PMID: 35617436
- Evidence: We estimated ages of afroalpine species and clades based on the seed-plant-wide and individual seed-plant clade datasets using two different molecular dating methods: penalized likelihood as implemented in treePL ( 48 ) and Bayesian statistics under an uncorrelated lognormal relaxed clock model as implemented in BEAST2 ( 49 ).
- Full pipeline: differential/statistical testing [BEAST]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Version used: **2.6.6**
- Evidence: The SNAPP (v.1.5.2) analyses were implemented in BEAST2 v.2.6.6 ( 77 ) and were run in parallel for one million generations, sampling every 1,000 steps with two independent replicates.
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### The genomic landscape of swine influenza A viruses in Southeast Asia. (PNAS 2023)

- DOI: 10.1073/pnas.2301926120 | PMCID: PMC10438389 | PMID: 37552753
- Version used: **10.4**
- Evidence: To examine the spatial patterns of EA-swine H1 viruses, we reconstructed the spatiotemporal pathways between locations using discrete phylogeographic analyses in BEAST v.10.4.
- Full pipeline: quality control [FastQC, Trimmomatic v0.39] -> read trimming [FastQC, Trimmomatic v0.39] -> structure determination [BEAST v10.4, RAxML v1.1.0] -> stage not stated [BLAST v2.2.18, SPAdes v3.15.3]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Version used: **2.6**
- Evidence: The phylogenetic history of DWV isolates was reconstructed jointly with their geographic movement using a discrete-trait continuous-time Markov chain phylogeographic model in BEAST v.
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Complex evolutionary processes maintain an ancient chromosomal inversion. (PNAS 2023)

- DOI: 10.1073/pnas.2300673120 | PMCID: PMC10288594 | PMID: 37311002
- Version used: **2.6.6**
- Evidence: We then used BEAST2 (version 2.6.6) ( 78 ) to estimate the divergence times between the Perform chromosomal variants in T. knulli .
- Full pipeline: alignment/mapping [RepeatMasker v4.0.7, SAMtools v1.5] -> variant calling [BCFtools v1.6] -> stage not stated [BEAST v2.6.6, BUSCO v4.0.5, R v4.0.2]

### Bayesian phylodynamics reveals the transmission dynamics of avian influenza A(H7N9) virus at the human-live bird market interface in China. (PNAS 2023)

- DOI: 10.1073/pnas.2215610120 | PMCID: PMC10151560 | PMID: 37068240
- Evidence: The BEAST 2 XML file used to perform the phylodynamic analysis together with the accession numbers of the H7N9 genome sequences, and the R scripts are available at https://github.com/ClaireGuinat/h7n9_bdmm-prime ( 99 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BEAST, R v4.0]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Version used: **2.6.3**
- Evidence: STACEY v.1.2.5, implemented in BEAST v.2.6.3, was used to assess species limits under the MSC model ( 37 , 38 , 69 ).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Climate, demography, immunology, and virology combine to drive two decades of dengue virus dynamics in Cambodia. (PNAS 2024)

- DOI: 10.1073/pnas.2318704121 | PMCID: PMC11388344 | PMID: 39190356
- Evidence: Using the best-fit model (GTR+I + G4 in all cases), we built a Bayesian phylogenetic tree for each serotype in BEAST 2 ( 58 ), incorporating the date of sample collection for each sequence (or the midpoint of the collection year if date was not reported), and specifying a strict molecular clock rate of 7.9 × 10 −4 s/s/y ( 8 ) and a Coalescent Bayesian skyline prior.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [BEAST] -> stage not stated [R, RAxML]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Evidence: We used BEAST2 ( 91 ) v2.7.3 to generate a time-scaled phylogeny from our mitochondrial sequence alignment.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### Illuminating the coevolution of photosynthesis and Bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322120121 | PMCID: PMC11194577 | PMID: 38875151
- Version used: **2.6.6**
- Evidence: Molecular clock analysis was performed using BEAST v.2.6.6 ( 111 – 113 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE v2.1.3, MAFFT] -> stage not stated [AlphaFold, BEAST v2.6.6, Prokka v1.14]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Version used: **6.6**
- Evidence: We used BEAST 2.6.6 ( 97 ) to calibrate the ASTRAL-III phylogeny against time employing five plastid genes ( atpB , psaA , psbD , rbcL , rps4 s) extracted from assembled plastomes using custom BLAST ( 98 ).
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### Estimates of early outbreak-specific SARS-CoV-2 epidemiological parameters from genomic data. (PNAS 2024)

- DOI: 10.1073/pnas.2308125121 | PMCID: PMC10786264 | PMID: 38175864
- Evidence: We use the BDSKY package ( 19 ) of BEAST 2 ( 36 ) to perform Bayesian phylodynamic inference of outbreak-specific basic reproductive numbers and sampling proportions from the sequence alignments.
- Full pipeline: quality control [Nextstrain] -> alignment/mapping [BEAST, IQ-TREE, Nextstrain] -> differential/statistical testing [BEAST]

### Phylogenomics redefines the evolutionary history of mosquitoes. (PNAS 2025)

- DOI: 10.1073/pnas.2519291122 | PMCID: PMC12557814 | PMID: 41052354
- Evidence: We estimated divergence times using BEAST2 by performing independent runs with different sets of UCE loci, prior distributions, and constraint trees based on the TSH and ACS topologies ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [BUSCO] -> differential/statistical testing [R, ggplot2] -> stage not stated [BEAST, IQ-TREE v2.2, TreeTime]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Evidence: We inferred divergence times between taxa under the multispecies coalescent model using the SNAPP add-on package for BEAST2 ( 26 ) with reduced sets of 5,000 randomly selected genome-wide SNPs.
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### The radiation and geographic expansion of primates through diverse climates. (PNAS 2025)

- DOI: 10.1073/pnas.2423833122 | PMCID: PMC12358913 | PMID: 40763018
- Evidence: ( 28 ), using a slightly modified version of their tip-dating procedure ( 28 ) and implemented in BEAST2 ( 66 ).
- Full pipeline: structure determination [R] -> stage not stated [BEAST]

### A 75,000-y-old Scandinavian Arctic cave deposit reveals past faunal diversity and paleoenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2415008122 | PMCID: PMC12358836 | PMID: 40758875
- Version used: **1.10.4**
- Evidence: Phylogenetic dating of V. lagopus , D. torquatus, and U. maritimus was done using Bayesian reconstruction of phylogenetic trees with BEAST v.1.10.4 [( 112 ); SI Appendix , Text S4 ; see phylogenetic analyses below].
- Full pipeline: differential/statistical testing [BEAST v1.10.4] -> structure determination [BEAST v1.10.4]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Evidence: 11 was produced using BEAST2 ( 105 ) ( https://beast2-dev.github.io/beast-docs/beast2/DivergenceDating/DivergenceDatingTutorial.html ) with the nuclear phylogenetic dataset thinned to 1 in 5,000 sites and with each lineage represented by the individual with highest coverage.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Phylogenetic networks empower biodiversity research. (PNAS 2025)

- DOI: 10.1073/pnas.2410934122 | PMCID: PMC12337313 | PMID: 40720655
- Evidence: Refer to SI Appendix for details on the Bayesian approaches implemented in PHYLONET , as well as other methods available in BEAST2 and BPP .
- Full pipeline: differential/statistical testing [BEAST]

### Cenozoic geoclimatic changes drove the evolutionary dynamics of floristic endemism on the Qinghai-Tibet Plateau. (PNAS 2025)

- DOI: 10.1073/pnas.2426017122 | PMCID: PMC12232610 | PMID: 40549922
- Version used: **1.8.4**
- Evidence: For the final concatenated datasets, we used BEAST v.1.8.4 ( 63 ) to generate time-calibrated phylogenies under an uncorrelated relaxed molecular clock model, a Yule tree prior, and the GTR + I + Γ model for each locus separately.
- Full pipeline: differential/statistical testing [RAxML v8.2.10] -> stage not stated [BEAST v1.8.4, R]

### Phylogenomics of the tetraploid Hawaiian lobeliads: Implications for their origin, dispersal history, and adaptive radiation. (PNAS 2025)

- DOI: 10.1073/pnas.2421004122 | PMCID: PMC12088406 | PMID: 40324077
- Version used: **2.7.5**
- Evidence: We calibrated the nuclear tree using BEAST2 v.2.7.5 ( 99 ) with a single partition and the GTR+I+Γ model with branch rates estimated under the optimized relaxed clock ( 100 ) and birth–death tree prior.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [BEAST v2.7.5, IQ-TREE v2.2.2.6, R]

### Bayesian phylodynamic inference of population dynamics with dormancy. (PNAS 2025)

- DOI: 10.1073/pnas.2501394122 | PMCID: PMC12067208 | PMID: 40314983
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Our open-source software as a BEAST2 package is available on GitHub at BEAST-seedbank/SeedbankTree ( 96 ).
- Full pipeline: simulation/modelling [TreeTime] -> stage not stated [BEAST]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Evidence: We inferred the calibrated phylogenetic tree with BEAST2 [v.2.6.3; ( 73 )].
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Evidence: Concatenated divergence time analyses were performed in BEAST2 for all datasets using the optimized relaxed clock model ( 123 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### Divergence time and environmental similarity predict the strength of morphological convergence in stick and leaf insects. (PNAS 2025)

- DOI: 10.1073/pnas.2319485121 | PMCID: PMC11725862 | PMID: 39715436
- Version used: **2.6.3**
- Evidence: Regions of three nuclear [18S rRNA (18S), 28S rRNA (28S), and histone subunit 3 (H3)] and four mitochondrial genes [12S rRNA (12S), 16S rRNA (16S), cytochrome-c oxidase subunit I (COI) and COII] were extracted from Genbank, aligned and concatenated (6,778 bp total) to reconstruct a MCC tree for phasmids using Bayesian inferences in BEAST 2 (v.
- Full pipeline: alignment/mapping [BEAST v2.6.3] -> differential/statistical testing [BEAST v2.6.3, R, phytools] -> structure determination [BEAST v2.6.3]

### Parallel algorithms for phylogenetic inference under a structured coalescent approximation. (PNAS 2026)

- DOI: 10.1073/pnas.2602412123 | PMCID: PMC13143046 | PMID: 42048453
- Version used: **7.7**
- Evidence: 2 , Upper panel), our parallel BEAGLE implementation achieves maximum speedups of approximately 15 × for EBLV, 26 × for PEDV, and 22 × for ZIKV compared to the BASTA package in BEAST 2.7.7 ( 13 ).
- Full pipeline: stage not stated [BEAST v7.7]

### Distinct evolutionary patterns of endemic and emerging parvoviruses and the origin of a new pandemic virus. (PNAS 2026)

- DOI: 10.1073/pnas.2515274123 | PMCID: PMC13099694 | PMID: 41980105
- Version used: **1.10.4**
- Evidence: The rates of evolution of natural FPV ( n = 40) and CPV ( n = 212) genomes were determined using root-to-tip genetic distance by regression of each ML tree by date (year) in the TempEst v.1.5.3 software ( 67 ), and by the Bayesian Markov chain Monte Carlo (MCMC) approach run in BEAST v.1.10.4 ( 68 ).
- Full pipeline: differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [AlphaFold, ChimeraX, IQ-TREE]

### A high-coverage Neandertal genome from the Altai Mountains reveals population structure among Neandertals. (PNAS 2026)

- DOI: 10.1073/pnas.2534576123 | PMCID: PMC13037865 | PMID: 41871248
- Evidence: Relationship among ancient human genomes mt DNA and Y chromosome were inferred using comparative datasets through phylogenetic analyses under a Bayesian framework implemented in BEAST2 ( 53 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [BEAST]

### Archaeogenetic insights into the demographic history of Late Neanderthals. (PNAS 2026)

- DOI: 10.1073/pnas.2520565123 | PMCID: PMC13037871 | PMID: 41871253
- Version used: **2.6.7**
- Evidence: The software package BEAST2 v.
- Full pipeline: stage not stated [BEAST v2.6.7, BLAST]

### Evolution and host-specific adaptation of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (Science 2024)

- DOI: 10.1126/science.adi0908 | PMCID: PMC7618370 | PMID: 38963857
- Version used: **6.6**
- Evidence: Clones with a significant temporal signal in this test (P < 0.05) were taken forward for molecular dating with BEAST 2.6.6 ( 29 ).
- Full pipeline: quality control [BWA] -> alignment/mapping [BWA, kallisto] -> quantification [DESeq2, kallisto] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEAST v6.6, RAxML v8.2.12, STRING db]

### Ancient &lt;i&gt;Borrelia&lt;/i&gt; genomes document the evolutionary history of louse-borne relapsing fever. (Science 2025)

- DOI: 10.1126/science.adr2147 | PMCID: PMC7617810 | PMID: 40403067
- Evidence: Given strong temporality in our dataset, we implemented formal Bayesian tip-dating calibration via BEAST2 ( 31 ) to provide a probabilistic assessment of the divergence of sampled B. recurrentis from the closest sequenced relative B. duttonii Ly and simultaneously estimated the mutation rate across the recombination pruned core genome.
- Full pipeline: differential/statistical testing [BEAST] -> structure determination [IQ-TREE v1.6.12]

