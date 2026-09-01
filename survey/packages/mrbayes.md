# MrBayes

- **Category:** phylogenetics
- **Papers in survey:** 40
- **Journals:** PNAS (25), Nature (15)
- **Years:** 2021 (6), 2022 (8), 2023 (10), 2024 (8), 2025 (7), 2026 (1)
- **Versions named:** 3.2.7 (11), 3.2.7a (9), 3.2.6 (6), 3.1.2 (1), 3.2.5 (1), 3.2 (1)
- **Pipeline stages it appears in:** differential/statistical testing (27), simulation/modelling (3), alignment/mapping (3), structure determination (2), visualisation (1), dimensionality reduction/clustering (1)

## Papers

### Fossil evidence unveils an early Cambrian origin for Bryozoa. (Nature 2021)

- DOI: 10.1038/s41586-021-04033-w | PMCID: PMC8580826 | PMID: 34707285
- Version used: **3.2.7**
- Evidence: Bayesian analyses were run using MrBayes (v.3.2.7) 33 and the Mkv model 34 , with gamma-distributed rate variation and variable coding.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7]

### A new elpistostegalian from the Late Devonian of the Canadian Arctic. (Nature 2022)

- DOI: 10.1038/s41586-022-04990-w | PMCID: PMC9385497 | PMID: 35859171
- Version used: **3.2.7a**
- Evidence: Undated Bayesian analyses were performed using MrBayes (v.3.2.7a) 41 .
- Full pipeline: differential/statistical testing [MrBayes v3.2.7a]

### The oldest three-dimensionally preserved vertebrate neurocranium. (Nature 2023)

- DOI: 10.1038/s41586-023-06538-y | PMCID: PMC10533405 | PMID: 37730987
- Version used: **3.2.7**
- Evidence: Bayesian analysis was carried out in MrBayes v.3.2.7, a flat (uniform) prior was used with an Mkv model and a gamma-distributed rate parameter.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Version used: **3.2.7a**
- Evidence: We modelled fusion-with-mixing events in the animal genomes as state transitions, and used RevBayes (v.1.1.1) 106 and MrBayes (v.3.2.7a) 52 to estimate the likelihood of the ctenophore-sister hypothesis, and we used FigTree (v.1.4.4; https://github.com/rambaut/figtree ) to visualize the trees.
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### Triassic stem caecilian supports dissorophoid origin of living amphibians. (Nature 2023)

- DOI: 10.1038/s41586-022-05646-5 | PMCID: PMC9892002 | PMID: 36697827
- Version used: **3.2.6**
- Evidence: A Bayesian inference analysis of the character–taxon matrix was conducted in the phylogenetic software package MrBayes v.3.2.6 (ref.
- Full pipeline: differential/statistical testing [MrBayes v3.2.6]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **3.2.7a**
- Evidence: Bayesian reconstructions in MrBayes (v.3.2.7a) 97 were also performed using the same WAG matrix but substituting the R4 model for the discrete gamma model 98 , with 4 rate categories (G4).
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Brazilian fossils reveal homoplasy in the oldest mammalian jaw joint. (Nature 2024)

- DOI: 10.1038/s41586-024-07971-3 | PMCID: PMC11464377 | PMID: 39322670
- Version used: **3.2.7**
- Evidence: Moreover, a Bayesian phylogenetic analysis was performed in MrBayes (v.3.2.7) 92 with four Markov chain Monte Carlo chains, using a discrete morphological character model.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> simulation/modelling [MrBayes v3.2.7]

### Organ systems of a Cambrian euarthropod larva. (Nature 2024)

- DOI: 10.1038/s41586-024-07756-8 | PMCID: PMC11374701 | PMID: 39085610
- Version used: **3.2.7a**
- Evidence: We ran four runs of eight chains in MrBayes 3.2.7a 76 , discarding the first 100,000 generations as burn-in before sampling every 500th generation for 900,000 generations.
- Full pipeline: stage not stated [MrBayes v3.2.7a]

### Middle and Late Pleistocene Denisovan subsistence at Baishiya Karst Cave. (Nature 2024)

- DOI: 10.1038/s41586-024-07612-9 | PMCID: PMC11291277 | PMID: 38961285
- Version used: **3.2.7**
- Evidence: A Bayesian tree was generated using MrBayes v.3.2.7 (ref.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [RAxML v4.0]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **3.1.2**
- Evidence: The secondary nucleotides of each codon with phasing alignment were extracted and used for constructing the phylogenetic tree using MrBayes (v.3.1.2) 86 under the GTR model.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### Mosaic anatomy in an early fossil squamate. (Nature 2025)

- DOI: 10.1038/s41586-025-09566-y | PMCID: PMC12629976 | PMID: 41034584
- Version used: **3.2.7a**
- Evidence: Phylogenetic inference was carried out using Bayesian inference in MrBayes 3.2.7a 57 , using a fossilized birth–death tree prior 58 , 59 with a proportion of extant species sampled of 0.038 under diversified sampling, and default priors for speciation rate, extinction rate and fossil sampling rate.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7a]

### The oldest known lepidosaur and origins of lepidosaur feeding adaptations. (Nature 2025)

- DOI: 10.1038/s41586-025-09496-9 | PMCID: PMC12629995 | PMID: 40931068
- Version used: **3.2.7**
- Evidence: Bayesian inference The modified 127 taxon matrix was subjected to Bayesian inference in MrBayes (v.3.2.7) 74 under the fossilized birth–death and relaxed clock transition model (outlined in a previous study 5 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7]

### Triassic diapsid shows early diversification of skin appendages in reptiles. (Nature 2025)

- DOI: 10.1038/s41586-025-09167-9 | PMCID: PMC12310547 | PMID: 40702174
- Version used: **3.2.7**
- Evidence: Bayesian inference analyses were executed in MrBayes v.3.2.7 (ref.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [ImageJ]

### New Silurian aculiferan fossils reveal complex early history of Mollusca. (Nature 2025)

- DOI: 10.1038/s41586-024-08312-0 | PMCID: PMC11735398 | PMID: 39779843
- Evidence: Bayesian analyses were conducted using MrBayes 50 , 51 v.3.2.7 via the CIPRES Science Gateway 52 with two parallel runs on four chains in a temperature of 0.1, running indefinitely (100 million generations) but stopping automatically when the analysis reached posterior probability values below 0.01.
- Full pipeline: differential/statistical testing [MrBayes]

### Enamel proteins from six Homo erectus specimens across China. (Nature 2026)

- DOI: 10.1038/s41586-026-10478-8 | PMCID: PMC13322979 | PMID: 42129550
- Version used: **3.2.6**
- Evidence: Then, we built a consensus Bayesian phylogenetic tree using the software MrBayes (v3.2.6) 65 , running 8 Markov Chain Monte Carlo (MCMC) chains for 1 million iterations in 2 independent runs.
- Full pipeline: differential/statistical testing [MrBayes v3.2.6] -> simulation/modelling [MrBayes v3.2.6]

### Fifty million years of beetle evolution along the Antarctic Polar Front. (PNAS 2021)

- DOI: 10.1073/pnas.2017384118 | PMCID: PMC8214695 | PMID: 34108239
- Version used: **3.2.6**
- Evidence: To further test statistical support for the nearest relatives of the Ectemnorhinini, we conducted marginal likelihood estimation (via stepping stone sampling in MrBayes v.3.2.6).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Clustal Omega, MAFFT] -> dimensionality reduction/clustering [R, RAxML] -> differential/statistical testing [MrBayes v3.2.6] -> structure determination [MAFFT] -> stage not stated [BEAST v2.5]

### Evolution of bacterial steroid biosynthesis and its impact on eukaryogenesis. (PNAS 2021)

- DOI: 10.1073/pnas.2101276118 | PMCID: PMC8237579 | PMID: 34131078
- Version used: **3.2.6**
- Evidence: Phylogenetic trees were constructed by maximum likelihood inference using Randomized Axelerated Maximum Likelihood (RAxML) version 8.2.11 and IQ-TREE version 2.1.06 ( 48 ) and by Bayesian inference using MrBayes version 3.2.6 ( 49 ) and PhyloBayes version 4.1c ( 50 ) (see SI Appendix , Methods for details).
- Full pipeline: differential/statistical testing [IQ-TREE v2.1.06, MrBayes v3.2.6, RAxML]

### HBD1 protein with a tandem repeat of two HMG-box domains is a DNA clip to organize chloroplast nucleoids in <i>Chlamydomonas reinhardtii</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2021053118 | PMCID: PMC8157925 | PMID: 33975946
- Evidence: A Bayesian inference analysis was performed using MrBayes with 1,000,000 generations.
- Full pipeline: differential/statistical testing [MrBayes, R, RAxML] -> stage not stated [HMMER, ImageJ]

### Endoplasmic reticulum membrane receptors of the GET pathway are conserved throughout eukaryotes. (PNAS 2021)

- DOI: 10.1073/pnas.2017636118 | PMCID: PMC7817167 | PMID: 33443185
- Version used: **3.2.7a**
- Evidence: Phylogenetic analyses were performed with MrBayes 3.2.7a, with 500,000 generations ( 46 ).
- Full pipeline: variant calling [ImageJ] -> stage not stated [MrBayes v3.2.7a]

### A modern scleractinian coral with a two-component calcite-aragonite skeleton. (PNAS 2021)

- DOI: 10.1073/pnas.2013316117 | PMCID: PMC7826372 | PMID: 33323482
- Evidence: Bayesian inference was performed on MrBayes also implemented at CIPRES with two runs each containing 100,000 generations saved at every 1,000, with a burn-in factor of 0.25.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [BEAST, RAxML]

### Bioremediation of mercury-polluted soil and water by the plant symbiotic fungus <i>Metarhizium robertsii</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214513119 | PMCID: PMC9704736 | PMID: 36375055
- Version used: **3.2.5**
- Evidence: We also constructed a Bayesian inference tree with MrBayes v3.2.5 as described ( 11 , 36 ); the models of evolution for MMD and MIR were the same as those used for ML tree construction.
- Full pipeline: alignment/mapping [MUSCLE v3.7] -> differential/statistical testing [MrBayes v3.2.5]

### Experimental evolution reveals the synergistic genomic mechanisms of adaptation to ocean warming and acidification in a marine copepod. (PNAS 2022)

- DOI: 10.1073/pnas.2201521119 | PMCID: PMC9499500 | PMID: 36095205
- Evidence: We generated consensus sequences for the major and minor variant for each sample and generated phylogenetic trees using MrBayes ( 83 ), including samples from Figueroa et al.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [VarScan] -> stage not stated [MrBayes]

### Middle Jurassic fossils document an early stage in salamander evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2114100119 | PMCID: PMC9335269 | PMID: 35858401
- Version used: **3.2**
- Evidence: Phylogenetic analyses were conducted in MrBayes 3.2 ( 96 ) under a relaxed MkV model of character state transitions with independent gamma branch rates and a fossilized-birth-death tree prior ( 97 ) [analytical script available on the Open Science Framework (OSF) ( 98 )].
- Full pipeline: stage not stated [MrBayes v3.2]

### The impact of paleoclimatic changes on body size evolution in marine fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2122486119 | PMCID: PMC9308125 | PMID: 35858316
- Version used: **3.2.7a**
- Evidence: In addition to the phylogenomic analyses described above, we conducted divergence time estimations under a total-evidence, or tip-dating, framework using the FBD model in MrBayes v 3.2.7a ( 73 ).
- Full pipeline: alignment/mapping [phytools] -> structure determination [phytools] -> stage not stated [IQ-TREE v1.6.12, MrBayes v3.2.7a, R v4.0.2]

### The Long chain Diol Index: A marine palaeotemperature proxy based on eustigmatophyte lipids that records the warmest seasons. (PNAS 2022)

- DOI: 10.1073/pnas.2116812119 | PMCID: PMC9169758 | PMID: 35412908
- Version used: **3.2.7**
- Evidence: In order to verify sequence identifications, phylogenetic analyses were performed by Bayesian Inference algorithms, using the program MrBayes 3.2.7-WIN ( 76 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [Cutadapt, DADA2]

### Early evolution of diurnal habits in owls (Aves, Strigiformes) documented by a new and exquisitely preserved Miocene owl fossil from China. (PNAS 2022)

- DOI: 10.1073/pnas.2119217119 | PMCID: PMC9169863 | PMID: 35344399
- Evidence: MBASR is an R language toolkit that highly automates the ASR workflow and uses the machinery of the popular phylogenetics software MrBayes ( 60 ).
- Full pipeline: structure determination [R, ggplot2] -> stage not stated [MrBayes, phytools]

### Amino acid sensor conserved from bacteria to humans. (PNAS 2022)

- DOI: 10.1073/pnas.2110415119 | PMCID: PMC8915833 | PMID: 35238638
- Evidence: Phylogenetic inference was performed using RaXML ( 41 ) and MrBayes ( 42 ).
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina, HMMER, MAFFT, MrBayes]

### Amine-recognizing domain in diverse receptors from bacteria and archaea evolved from the universal amino acid sensor. (PNAS 2023)

- DOI: 10.1073/pnas.2305837120 | PMCID: PMC10589655 | PMID: 37819981
- Evidence: Using the determined amino acid replacement model, a phylogenetic tree was inferred using a Bayesian inference algorithm implemented in MrBayes ( 67 ).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [AlphaFold, AutoDock Vina, Open Babel, PyMOL]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Evidence: Bayesian inference analyses were performed using MrBayes ( 90 ) v3.2.0 and PhyloBayes MPI v1.6 ( 91 ).
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### Cambrian lobopodians shed light on the origin of the tardigrade body plan. (PNAS 2023)

- DOI: 10.1073/pnas.2211251120 | PMCID: PMC10334802 | PMID: 37399417
- Version used: **3.2.6**
- Evidence: Bayesian inference was performed by MrBayes 3.2.6.
- Full pipeline: differential/statistical testing [MrBayes v3.2.6] -> stage not stated [IQ-TREE]

### An eosimiid primate of South Asian affinities in the Paleogene of Western Amazonia and the origin of New World monkeys. (PNAS 2023)

- DOI: 10.1073/pnas.2301338120 | PMCID: PMC10334725 | PMID: 37399374
- Version used: **3.2.7a**
- Evidence: The BTD analyses were performed with MrBayes 3.2.7a ( 78 ), using the computer cluster CIPRES Science Gateway 3.3 ( 79 ).
- Full pipeline: dimensionality reduction/clustering [MrBayes v3.2.7a] -> stage not stated [R v4.2]

### Evolution and diversification of the ACT-like domain associated with plant basic helix-loop-helix transcription factors. (PNAS 2023)

- DOI: 10.1073/pnas.2219469120 | PMCID: PMC10175843 | PMID: 37126718
- Version used: **3.2.7**
- Evidence: Bayesian trees were estimated using MrBayes v3.2.7 ( 60 ) by summarizing 25,000 trees generated from two independent runs that converged after 7.5 million generations with the SD of split frequencies <0.02.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [AlphaFold, ColabFold, RAxML v1.1.0]

### <i>Starships</i> are active eukaryotic transposable elements mobilized by a new family of tyrosine recombinases. (PNAS 2023)

- DOI: 10.1073/pnas.2214521120 | PMCID: PMC10104507 | PMID: 37023132
- Evidence: Sequences were aligned using Clustal Omega ( 58 ) and a phylogeny was inferred using a Bayesian approach implemented in MrBayes using the HKY85 substitution model ( 42 ).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega, MAFFT, MrBayes] -> differential/statistical testing [Clustal Omega, MrBayes] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.0.3]

### <i>Rickettsia</i> symbionts spread via mixed mode transmission, increasing female fecundity and sex ratio shift by host hormone modulating. (PNAS 2024)

- DOI: 10.1073/pnas.2406788121 | PMCID: PMC11194588 | PMID: 38865267
- Version used: **3.2.7**
- Evidence: The best-fit model was identified by jModelTest v2.1.10 (with parameters -i -g 4 -AICc -uLnL), and the trees were reconstructed using MrBayes v3.2.7 for gltA and 16S rRNA gene tree with GTR+G model and SYM+I+G model respectively.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, MAFFT v7.520] -> differential/statistical testing [edgeR] -> structure determination [MrBayes v3.2.7]

### Identification and epidemiological study of an uncultured flavivirus from ticks using viral metagenomics and pseudoinfectious viral particles. (PNAS 2024)

- DOI: 10.1073/pnas.2319400121 | PMCID: PMC11087778 | PMID: 38687787
- Version used: **3.2.7a**
- Evidence: The BI dendrogram and posterior probabilities were estimated using MrBayes version 3.2.7a ( 74 ) using the WAG + G + F model.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [MrBayes v3.2.7a]

### The 10,000-year biocultural history of fallow deer and its implications for conservation policy. (PNAS 2024)

- DOI: 10.1073/pnas.2310051121 | PMCID: PMC10895352 | PMID: 38346198
- Version used: **3.2.6**
- Evidence: 3.1.1.1 ( www.fluxus-engineering.com ) and a Bayesian phylogeny within MrBayes v.
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [MrBayes v3.2.6]

### A recent gibbon ape leukemia virus germline integration in a rodent from New Guinea. (PNAS 2024)

- DOI: 10.1073/pnas.2220392121 | PMCID: PMC10861895 | PMID: 38305758
- Version used: **3.2.7**
- Evidence: Bayesian phylogenetic inference was produced using Markov Chain Monte Carlo for 1,000,000 iterations in MrBayes v3.2.7 ( 51 ).
- Full pipeline: read trimming [Cutadapt v1.15, Picard v1.4, Trimmomatic v0.27] -> alignment/mapping [PyMOL v2.4] -> differential/statistical testing [MrBayes v3.2.7] -> simulation/modelling [MrBayes v3.2.7] -> stage not stated [QGIS v3.16.10, RAxML v8.2.11]

### Specificities of chemosensory receptors in the human gut microbiota. (PNAS 2025)

- DOI: 10.1073/pnas.2508950122 | PMCID: PMC12415202 | PMID: 40857311
- Evidence: Multiple sequence alignments were built using MAFFT ( 72 ), computational docking was carried out using DiffDock ( 73 ), and phylogenetic tree analysis was performed using MrBayes ( 74 ).
- Full pipeline: alignment/mapping [MAFFT, MrBayes] -> stage not stated [AlphaFold]

### Cryptic isoprene emission of soybeans. (PNAS 2025)

- DOI: 10.1073/pnas.2502360122 | PMCID: PMC12184331 | PMID: 40504154
- Evidence: A phylogenetic tree of isoprene and ocimene synthases was generated with amino acid sequences using MrBayes (version ver.
- Full pipeline: visualisation [AlphaFold] -> stage not stated [MrBayes, PyMOL v4.6.0]

### Dynamic interplay between niche variation and flight adaptability drove a hundred million years' dispersion in iconic lacewings. (PNAS 2025)

- DOI: 10.1073/pnas.2414549122 | PMCID: PMC12087969 | PMID: 40314968
- Version used: **3.2.7**
- Evidence: Bayesian tip-dating analyses were performed to assess the phylogenetic relationships among genera of Berothidae by MrBayes 3.2.7 ( 78 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7, ggplot2] -> stage not stated [NCO, R, phytools]

