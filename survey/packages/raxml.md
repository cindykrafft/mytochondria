# RAxML

- **Category:** phylogenetics
- **Papers in survey:** 167
- **Journals:** PNAS (122), Nature (36), Cell (7), Science (2)
- **Years:** 2021 (30), 2022 (38), 2023 (26), 2024 (40), 2025 (30), 2026 (3)
- **Versions named:** 8.2.12 (25), 8.2.11 (8), 8.2.10 (8), 8.2.4 (6), 1.1.0 (4), 0.9.0 (3), 8.2.9 (3), 1.0.3 (2), 8.1.16 (1), 4.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (47), structure determination (14), read trimming (8), differential/statistical testing (7), visualisation (6), dimensionality reduction/clustering (2), machine learning (1), simulation/modelling (1), variant calling (1)

## Papers

### The genomic history of the Middle East. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.013 | PMCID: PMC8445022 | PMID: 34352227
- Version used: **8.2.10**
- Evidence: ... 2014 https://crossmap.readthedocs.io/en/latest/ BEAST v1.8.4 Drummond and Rambaut 2007 https://beast.community/2016-06-17_BEAST_v1.8.4_released.html RAxML v8.2.10 Stamatakis 2014 https://cme.h-its.org/exelixis/web/software/raxml/ FigTree v1.4.4 N/A http://tree.bio.ed.ac.uk/software/figtree/ Chromopainter/FineSTRUCTURE pipeline v4.1.1 Lawson et al., 2012 http://paintmychromosomes.com/ (fast)GLOBET...
- Full pipeline: stage not stated [ADMIXTURE, BCFtools v1.9, GATK v3.7, RAxML v8.2.10, SAMtools]

### Identification of novel bat coronaviruses sheds light on the evolutionary origins of SARS-CoV-2 and related viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.008 | PMCID: PMC8188299 | PMID: 34147139
- Evidence: Phylogenetic analysis was performed using RAxML( Stamatakis 2014 ) with 1,000 bootstrap replicates, employing the GTR nucleotide substitution model.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.450] -> stage not stated [BLAST, Bowtie2 v2.4.1, PyMOL v2.4.0a, RAxML, SAMtools v1.10]

### In vivo structural characterization of the SARS-CoV-2 RNA genome identifies host proteins vulnerable to repurposed drugs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.008 | PMCID: PMC7871767 | PMID: 33636127
- Version used: **8.2.12**
- Evidence: To visualize phylogenetic relationships among major coronaviral clades, one hundred representative viral sequences were selected to generate evolutionary tree by RAxML v.8.2.12 ( Kozlov et al., 2019 ) with GTR+G substitution model and 1,000 bootstrap replicates.
- Full pipeline: read trimming [Bowtie2, SAMtools, Trimmomatic] -> alignment/mapping [MAFFT v7.313] -> differential/statistical testing [SciPy] -> simulation/modelling [UCSF Chimera] -> structure determination [UCSF Chimera] -> visualisation [RAxML v8.2.12] -> stage not stated [AutoDock Vina]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Version used: **8.2.12**
- Evidence: .../roblanf/sarscov2phylo Minimap2 v2.17 Li, 2018 https://github.com/lh3/minimap2 trimAl v1.2 Capella-Gutiérrez et al., 2009 http://trimal.cgenomics.org RAxML v8.2.12 Stamatakis, 2014 https://cme.h-its.org/exelixis/web/software/raxml CmdStan v2.28.1 The Stan Development Team https://mc-stan.org CmdStanr v0.4.0 The Stan Development Team https://mc-stan.org/cmdstanr/ R v4.1.3 The R Foundation https://w...
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Version used: **8.2.12**
- Evidence: .../sarscov2phylo Minimap2 v2.17 ( Li, 2018 ) https://github.com/lh3/minimap2 trimAl v1.2 ( Capella-Gutiérrez et al., 2009 ) http://trimal.cgenomics.org RAxML v8.2.12 ( Stamatakis, 2014 ) https://cme.h-its.org/exelixis/web/software/raxml BEAST2 v2.6.6 ( Bouckaert et al., 2014 ) https://www.beast2.org CmdStan v2.28.1 The Stan Development Team https://mc-stan.org CmdStanr v0.4.0 The Stan Development Te...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Evidence: The multiple sequence alignment (MSA) of these Pfam domains were used for phylogenetic analysis by RAxML (-m PROTGAMMAAUTO).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Evidence: For each gene of interest, MUSCLE v5.1 108 was used for multiple sequence alignment of representative orthologs, ModelTest-NG 109 was used to select the optimal substitution model, and RAxML-NG 110 used for tree construction employed via raxmlGUI 2.0 111 to map their phylogenetic relationships.
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### A chickpea genetic variation map based on the sequencing of 3,366 genomes. (Nature 2021)

- DOI: 10.1038/s41586-021-04066-1 | PMCID: PMC8612933 | PMID: 34759320
- Evidence: The maximum likelihood tree was constructed using RAxML 50 v.8.2.12 with parameters “-f a -x 12345 -p 12345 -# 1000 -m GTRCATX”.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BUSCO, PLINK, RAxML, VCFtools]

### The origins and spread of domestic horses from the Western Eurasian steppes. (Nature 2021)

- DOI: 10.1038/s41586-021-04018-9 | PMCID: PMC8550961 | PMID: 34671162
- Evidence: Maximum-likelihood phylogenetic reconstruction was performed using RAxML 65 (version 8.2.11) with default parameters, and assessing node support from a total of 100 bootstrap pseudo-replicates.
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [Rcpp] -> structure determination [RAxML] -> stage not stated [ANGSD, R]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **8.1.15**
- Evidence: To assess the certainty of core genome phylogeny of the 30 M. smithii genomes, we used RAxML (v.8.1.15) 92 under a GTR model of substitution with 4 gamma categories and 100 bootstrap pseudo replicates.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: A maximum-likelihood phylogenetic tree of 16S rRNA gene sequences was calculated using RAxML 78 v.8.2.8 integrated in ARB with the GAMMA model of rate heterogeneity and the GTR substitution model with 100 bootstraps.
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Version used: **8.2.4**
- Evidence: The final dataset (99,601 aligned nucleotides) was used to reconstruct the phylogeny with RAxML v.8.2.4 under the GTRGAMMA model and 1,000 bootstrap replicates.
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### GTSF1 accelerates target RNA cleavage by PIWI-clade Argonaute proteins. (Nature 2022)

- DOI: 10.1038/s41586-022-05009-0 | PMCID: PMC9385479 | PMID: 35772669
- Version used: **1.0.0**
- Evidence: Protein sequences were aligned using Clustal Omega (1.2.4); unrooted tree was constructed using randomized axelerated maximum likelihood (RAxML 1.0.0) with default parameters 84 and visualized in Interactive Tree of Life 85 .
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4, HTSeq v0.9.1, RAxML v1.0.0, SAMtools v1.8, STAR v2.3] -> quantification [HTSeq v0.9.1] -> visualisation [Clustal Omega v1.2.4, RAxML v1.0.0] -> stage not stated [Bowtie2 v2.5]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Evidence: We performed phylogenetic analysis with RAxML 81 v.8.2.9 using the generalized time-reversible (GTR) substitution model with 4 gamma rate categories.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Island-specific evolution of a sex-primed autosome in a sexual planarian. (Nature 2022)

- DOI: 10.1038/s41586-022-04757-3 | PMCID: PMC9177419 | PMID: 35650439
- Version used: **0.9.0**
- Evidence: Phylogenetic trees were built by maximum likelihood using RAxML-NG version 0.9.0 (ref.
- Full pipeline: variant calling [GATK v4.1.4.1] -> quantification [kallisto v0.44.0] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [ImageJ, RAxML v0.9.0, VCFtools v0.1.14]

### ACE2 binding is an ancestral and evolvable trait of sarbecoviruses. (Nature 2022)

- DOI: 10.1038/s41586-022-04464-z | PMCID: PMC8967715 | PMID: 35114688
- Version used: **8.2.12**
- Evidence: Phylogenies were inferred with RAxML (v.8.2.12) 54 using the LG+Γ substitution model for amino acid sequence alignments or GTR+Γ with separate data partitions applied to the first, second and third codon positions for nucleotide sequence alignments.
- Full pipeline: alignment/mapping [RAxML v8.2.12] -> stage not stated [Pangolin]

### From primordial clocks to circadian oscillators. (Nature 2023)

- DOI: 10.1038/s41586-023-05836-9 | PMCID: PMC10076222 | PMID: 36949197
- Version used: **8.2.9**
- Evidence: This alignment was used as input to generate an initial phylogenetic tree for KaiC with RAxML (v.8.2.9) 42 using the PROTGAMMALG model.
- Full pipeline: alignment/mapping [IQ-TREE v1.6, MAFFT, RAxML v8.2.9] -> simulation/modelling [UCSF Chimera v1.15] -> structure determination [Coot v0.9.81, PHENIX v1.20.1] -> visualisation [PyMOL v2.6.0]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **8.2.11.9**
- Evidence: Maximum likelihood trees were constructed using RAxML (v.8.2.11.9) 113 with an LG substitution matrix 114 and 1,000 ultrafast bootstraps.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Cas12a2 elicits abortive infection through RNA-triggered destruction of dsDNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05559-3 | PMCID: PMC9811890 | PMID: 36599979
- Evidence: The resulting alignment was trimmed using ClipKIT 54 and used to create a maximum-likelihood phylogeny using RAxML-NG 55 with the following parameters: --model JTT+G --bs-metric fbp, tbe --tree pars{60}, rand{60} --seed 12345 --bs-trees autoMRE.
- Full pipeline: read trimming [RAxML] -> alignment/mapping [Bowtie2, MAFFT v7.490, RAxML] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST, Python]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Version used: **0.9.0**
- Evidence: We used RAxML-NG (v.0.9.0) 60 to generate the phylogenetic tree, applying the GTR + G model and using the Y. pseudotuberculosis reference genome (GCF_000834295.1) as an outgroup.
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Geographical migration and fitness dynamics of Streptococcus pneumoniae. (Nature 2024)

- DOI: 10.1038/s41586-024-07626-3 | PMCID: PMC11236706 | PMID: 38961295
- Evidence: We built trees masking recombination regions using Gubbins (v.2.4.1) 60 with the hybrid model that uses FastTree for the first iteration and RAxML subsequently 61 and a GTR model.
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SAMtools] -> registration [SAMtools] -> differential/statistical testing [BEAST v1.10.4, R v3.6.2] -> stage not stated [RAxML]

### Middle and Late Pleistocene Denisovan subsistence at Baishiya Karst Cave. (Nature 2024)

- DOI: 10.1038/s41586-024-07612-9 | PMCID: PMC11291277 | PMID: 38961285
- Version used: **4.0**
- Evidence: RAxML v.4.0 (ref.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [RAxML v4.0]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Maximum likelihood phylogeny produced with RAxML-NG using a complete deletion alignment including 17,100 SNP positions.
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Evidence: Coalescence gene trees were constructed with each gene applied using RAxML-8.2.11.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **8.2.12**
- Evidence: We then used RAxML (v.8.2.12) 61 (parameters: -f a -x 50217 -p 50217 -# 1000 -o Pcine,Vursi -m GTRGAMMA) and Phylofit (RPHAST suite v.1.6.9) 62 to produce a guide species tree and mod file, respectively (Fig.
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Complexity of avian evolution revealed by family-level genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07323-1 | PMCID: PMC11111414 | PMID: 38560995
- Evidence: All analyses are coalescent-based species trees obtained from ASTRAL with support being local posterior probabilities, with the exception of the values on the panel showing the topology obtained from concatenated analysis using RAxML-NG with support values resulting from bootstrapping.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE, RAxML]

### Compensatory evolution in NusG improves fitness of drug-resistant M. tuberculosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07206-5 | PMCID: PMC10990936 | PMID: 38509362
- Version used: **8.2.11**
- Evidence: We performed Maximum Likelihood Inference using RAxML (v8.2.11) to construct the ancestral sequence and determine the derived state of each allele.
- Full pipeline: variant calling [GATK v3.5, SAMtools v1.7] -> quantification [ImageJ] -> differential/statistical testing [Stan] -> stage not stated [RAxML v8.2.11, freebayes v1.3.1]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **8.2.12**
- Evidence: Next, for each of these 1,247 families, we built gene trees using RAxML (v.8.2.12) 100 , with 10 distinct starting trees and the PROTGAMMAJTT model, for: the unconstrained maximum likelihood (ML) tree; the constrained ancestral rediploidization topologies; and the constrained lineage-specific rediploidization topology.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Evidence: We built a reference phylogenetic tree of 1,244 male individuals from the 1000 Genomes project with RAxML-NG (ref.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### A lethal mitonuclear incompatibility in complex I of natural hybrids. (Nature 2024)

- DOI: 10.1038/s41586-023-06895-8 | PMCID: PMC10830419 | PMID: 38200310
- Evidence: We used a combination of PacBio amplicon sequencing of 10 individuals (2 or more per species, Supplementary Information 1.5.3 ) and newly available whole-genome resequencing data to confirm this result and polarize the direction of the discordance by constructing maximum likelihood mitochondrial phylogenies with the program RAxML 63 .
- Full pipeline: stage not stated [ImageJ, RAxML]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Evidence: Phylogenetic tree construction For the F. prausnitzii strains with SVs containing the GalNAc utilization gene cluster, we first constructed a phylogenetic tree using the RAxML approach based on 81 accurately selected single-copy marker genes 77 .
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Version used: **8.2.9**
- Evidence: The alignment was used to generate an untrimmed phylogenetic tree in RAxML (v.8.2.9) 64 .
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Assessing phylogenetic confidence at pandemic scales. (Nature 2025)

- DOI: 10.1038/s41586-025-09567-x | PMCID: PMC12611777 | PMID: 41193798
- Evidence: ...oddsidemargin}{-69pt} \begin{document}$${n}^{^{\prime} }$$\end{document} n ′ (length l 3 ), similarly to the ‘lazy subtree rearrangement’ approach of RAxML 37 (see Extended Data Fig.
- Full pipeline: stage not stated [IQ-TREE v2.1.3, Pangolin, RAxML]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Evidence: Maximum-likelihood trees were constructed using RAxML 57 (v.8.2.12) PROTGAMMALGF model with 100 bootstraps replicates and visualized in iTOL 58 .
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### Microbial iron oxide respiration coupled to sulfide oxidation. (Nature 2025)

- DOI: 10.1038/s41586-025-09467-0 | PMCID: PMC12545173 | PMID: 40866705
- Version used: **8.2.12**
- Evidence: The resulting sequence alignment was used to reconstruct the maximum-likelihood tree using RAxML v8.2.12.
- Full pipeline: alignment/mapping [MAFFT v7.407, RAxML v8.2.12] -> structure determination [RAxML v8.2.12] -> visualisation [R v4.1] -> stage not stated [AlphaFold v2.3.2, AutoDock Vina v1.1.2, DESeq2 v3.19, HMMER, ImageJ, featureCounts]

### Complete biosynthesis of salicylic acid from phenylalanine in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09175-9 | PMCID: PMC12408352 | PMID: 40702181
- Version used: **8.2.12**
- Evidence: The retained protein sequences with at least one conserved domain (Supplementary Table 10 ) were then used for multiple sequence alignment with MAFFT v7.526 69 and construction of maximum-likelihood gene trees with 500 bootstrap replicates and optimal model using RAxML (v.8.2.12) 70 .
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.526, Picard, RAxML v8.2.12] -> stage not stated [InterProScan v5.69]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **8.2.12**
- Evidence: The chromosome phylogenies were constructed from multiple alignments using RAxML (v.8.2.12) 96 with the GTRGAMMAI model.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: RAxML 106 (v.8.2.10) with the GTRGAMMA substitution model was used to construct a starting maximum-likelihood phylogenetic tree for BEAST.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: Phylogenetic analysis and metabolic reconstruction The phylogenetic profile of recovered MAGs was reconstructed using UBCG 54 v.3.0, involving marker gene identification, multiple sequence alignment refinement and concatenation, and phylogeny reconstruction using Mafft 55 v.7.487 and RAxML 56 v.8.2.12.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **8.1.16**
- Evidence: For the ASTRAL analysis, input trees were estimated in RAxML v.8.1.16 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Evidence: Maximum likelihood trees were generated in RAxML-ng 36 with 1,000 bootstrap replicates and 25% permission of missing data (Fig.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Evidence: ProtPipeliner runs as follows: (1) alignments are curated with minimal editing by GBLOCKS 92 ; (2) model selection is conducted via ProtTest 93 ; and (3) maximum-likelihood phylogeny for alignments are conducted using RAxML 94 v.8.3.1 with 100 bootstrap replicates.
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Evidence: A phylogenetic tree was inferred from the full alignment file including all reference sequences and the three high-coverage samples from this study using RAxML-NG 91 with the GTR + G substitution model and using the Y. similis reference genome (SAMEA5779183) as an outgroup (see Extended Data Fig.
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Version used: **8.2.10**
- Evidence: For both the autosome and Z-chromosome datasets, we concatenated all SNPs and constructed ML phylogenies using RAxML version 8.2.10 ( 65 ) with 100 bootstrap replicates under the ASC_GTRGAMMA model.
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: The ML tree was constructed using RAxML ( 89 ) with the PROTGAMMAJTT model and estimated clade support with 100 rapid bootstrap replicates.
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Version used: **8.2.11**
- Evidence: A maximum likelihood tree for 47 ancient genomes during the second pandemic was rebuilt using RAxML (v8.2.11) ( 43 ) with 100 replicates and GTRGAMMA model.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### A squalene-hopene cyclase in <i>Schizosaccharomyces japonicus</i> represents a eukaryotic adaptation to sterol-limited anaerobic environments. (PNAS 2021)

- DOI: 10.1073/pnas.2105225118 | PMCID: PMC8364164 | PMID: 34353908
- Version used: **0.8.1**
- Evidence: Alignments were trimmed using trimAl version 1.2 ( 92 ) in “gappyout” mode and used to build a phylogenetic tree with RAxML-NG version 0.8.1 ( 93 ) using 10 random and 10 parsimony starting trees, 100 Felsestein Bootstrap replicates, and PROTGTR + FO model.
- Full pipeline: read trimming [RAxML v0.8.1] -> alignment/mapping [HMMER, MAFFT v7.402, RAxML v0.8.1] -> stage not stated [Flye v2.7.1, Pilon v1.18]

### Evolution of a σ-(c-di-GMP)-anti-σ switch. (PNAS 2021)

- DOI: 10.1073/pnas.2105447118 | PMCID: PMC8325347 | PMID: 34290147
- Version used: **8.2.10**
- Evidence: Phylogenetic reconstruction was performed by RAxML version 8.2.10 ( 54 ) with 100 rapid bootstraps replicates to assess node support.
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX, RAxML v8.2.10]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Version used: **8.2.10**
- Evidence: RAxML v8.2.10 ( 83 ) was used to build a phylogenetic tree from this new alignment as described in ref.
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### GRINS: Genetic elements that recode assembly-line polyketide synthases and accelerate their diversification. (PNAS 2021)

- DOI: 10.1073/pnas.2100751118 | PMCID: PMC8256042 | PMID: 34162709
- Evidence: We then performed phylogenetic reconstruction via RAxML ( 30 ) and removed paralogues by eliminating the multicopy genes that had the most substitutions within each genome.
- Full pipeline: structure determination [RAxML] -> stage not stated [eggNOG v4.5]

### Fifty million years of beetle evolution along the Antarctic Polar Front. (PNAS 2021)

- DOI: 10.1073/pnas.2017384118 | PMCID: PMC8214695 | PMID: 34108239
- Evidence: The dataset was partitioned using PartitionFinder and analyzed under the GTR+G+I model using maximum likelihood (ML) phylogenetic inference conducted in RAxML (Randomized Axelerated Maximum Likelihood) v.8 ( 88 ) on the University of Memphis high-performance computing (HPC) cluster.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Clustal Omega, MAFFT] -> dimensionality reduction/clustering [R, RAxML] -> differential/statistical testing [MrBayes v3.2.6] -> structure determination [MAFFT] -> stage not stated [BEAST v2.5]

### Evolutionary and phylogenetic insights from a nuclear genome sequence of the extinct, giant, "subfossil" koala lemur <i>Megaladapis edwardsi</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2022117118 | PMCID: PMC8255780 | PMID: 34162703
- Evidence: Using RAxML (Randomized Axelerated Maximum Likelihood) ( 26 ), we estimated a single unrooted phylogeny from the concatenated alignment without partitioning under the GTR (General Time Reversible) GAMMA model (assuming variable nt frequency changes that are independent for each type of nt) ( 100 ).
- Full pipeline: alignment/mapping [RAxML, SAMtools]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Version used: **8.0.0**
- Evidence: A phylogenetic tree was built with RAxML version 8.0.0 ( 98 ) (see details in SI Appendix , SI Methods S3 ).
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Evolution of bacterial steroid biosynthesis and its impact on eukaryogenesis. (PNAS 2021)

- DOI: 10.1073/pnas.2101276118 | PMCID: PMC8237579 | PMID: 34131078
- Evidence: Phylogenetic trees were constructed by maximum likelihood inference using Randomized Axelerated Maximum Likelihood (RAxML) version 8.2.11 and IQ-TREE version 2.1.06 ( 48 ) and by Bayesian inference using MrBayes version 3.2.6 ( 49 ) and PhyloBayes version 4.1c ( 50 ) (see SI Appendix , Methods for details).
- Full pipeline: differential/statistical testing [IQ-TREE v2.1.06, MrBayes v3.2.6, RAxML]

### HBD1 protein with a tandem repeat of two HMG-box domains is a DNA clip to organize chloroplast nucleoids in <i>Chlamydomonas reinhardtii</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2021053118 | PMCID: PMC8157925 | PMID: 33975946
- Evidence: RAxML was used for phylogenetic tree search and bootstrap value calculation by the maximum likelihood method.
- Full pipeline: differential/statistical testing [MrBayes, R, RAxML] -> stage not stated [HMMER, ImageJ]

### Anaerobic gut fungi are an untapped reservoir of natural products. (PNAS 2021)

- DOI: 10.1073/pnas.2019855118 | PMCID: PMC8106346 | PMID: 33906945
- Evidence: Phylogenetic trees were constructed using FastTree ( 72 ) and RAxML ( 73 ).
- Full pipeline: alignment/mapping [AUGUSTUS, MAFFT] -> dimensionality reduction/clustering [BLAST] -> visualisation [Cytoscape] -> stage not stated [OrthoFinder, RAxML]

### Host barriers to SARS-CoV-2 demonstrated by ferrets in a high-exposure domestic setting. (PNAS 2021)

- DOI: 10.1073/pnas.2025601118 | PMCID: PMC8106344 | PMID: 33858941
- Evidence: M. p. furo (ferret) orthologs were inconsistent with related species by preliminary RAxML ortholog analysis ( 50 ).
- Full pipeline: stage not stated [RAxML, SAMtools]

### Multiple independent recombinations led to hermaphroditism in grapevine. (PNAS 2021)

- DOI: 10.1073/pnas.2023548118 | PMCID: PMC8053984 | PMID: 33837155
- Version used: **8.2.4**
- Evidence: The maximum likelihood (ML) phylogeny of these haplotypes was further calculated using RAxML v8.2.4 with a GTRCTA site rate substitution model ( 40 ).
- Full pipeline: variant calling [RAxML v8.2.4] -> differential/statistical testing [BEAST v2.5.2] -> stage not stated [RepeatMasker]

### The diversity of stomatal development regulation in <i>Callitriche</i> is related to the intrageneric diversity in lifestyles. (PNAS 2021)

- DOI: 10.1073/pnas.2026351118 | PMCID: PMC8040647 | PMID: 33782136
- Version used: **8.2.12**
- Evidence: After trimming nonhomologous regions using trimAL v1.4 ( 56 ), we constructed a maximum likelihood tree using RAxML v8.2.12 ( 57 ) with 1,000 bootstraps ( Fig.
- Full pipeline: read trimming [RAxML v8.2.12] -> alignment/mapping [MAFFT v7.453] -> stage not stated [BLAST]

### An introgressed gene causes meiotic drive in <i>Neurospora sitophila</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2026605118 | PMCID: PMC8092558 | PMID: 33875604
- Evidence: We tested the hypothesis of introgression by extracting the fragment of NCU09865 found in Spk-1 from 177 Neurospora assemblies, as well as the two neighboring genes NCU09864 and NCU09866 , and generating phylogenies using RAxML ( 51 ).
- Full pipeline: alignment/mapping [Cufflinks] -> differential/statistical testing [RAxML] -> stage not stated [ADMIXTURE, BLAST, IQ-TREE]

### Isolation and characterization of <i>Helicobacter suis</i> from human stomach. (PNAS 2021)

- DOI: 10.1073/pnas.2026337118 | PMCID: PMC8020762 | PMID: 33753513
- Evidence: Phylogenetic analysis based on the core genome alignments of H. suis from the Roary pipeline was performed using Randomized Axelerated Maximum Likelihood version 1.0.0 ( https://github.com/stamatak/standard-RAxML ) with 1,000 bootstraps and visualized using FigTree version 1.4.4 ( http://tree.bio.ed.ac.uk/software/figtree/ ).
- Full pipeline: alignment/mapping [RAxML] -> visualisation [RAxML]

### Estimating maximal microbial growth rates from cultures, metagenomes, and single cells via codon usage patterns. (PNAS 2021)

- DOI: 10.1073/pnas.2016810118 | PMCID: PMC8000110 | PMID: 33723043
- Evidence: To assess sensitivity to phylogeny, we built a maximum likelihood tree with 10 bootstrap replicates from the GTDB-Tk alignment using RAxML [v8.2.11, with -k -f a -m PROTGAMMAGTR options ( 98 )].
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [RAxML] -> visualisation [ggplot2, ggpubr] -> stage not stated [R, ape (R)]

### Diel transcriptional oscillations of light-sensitive regulatory elements in open-ocean eukaryotic plankton communities. (PNAS 2021)

- DOI: 10.1073/pnas.2011038118 | PMCID: PMC8017926 | PMID: 33547239
- Version used: **8.2.8**
- Evidence: A maximum-likelihood (ML) phylogenetic 18S rDNA tree representing 117 marine relevant eukaryotic order levels was built using RAxML version 8.2.8 ( 119 ) (parameters: -f a -m GTRGAMMA -p 12345 -x 12345 -# 100).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R] -> stage not stated [HMMER v3.1b, RAxML v8.2.8]

### A modern scleractinian coral with a two-component calcite-aragonite skeleton. (PNAS 2021)

- DOI: 10.1073/pnas.2013316117 | PMCID: PMC7826372 | PMID: 33323482
- Evidence: Mitophylogenomic Maximum Likelihood (ML) analyses were based on approximate likelihood ratio test using PhyML 3.0 ( 59 ) and 100 bootstrap replicates using RAxML ( 60 ) implemented at CIPRES ( 61 ) under the General Time Reversible (GTR) + G + I model of nucleotide substitution.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [BEAST, RAxML]

### Earliest evidence of primate captivity and translocation supports gift diplomacy between Teotihuacan and the Maya. (PNAS 2022)

- DOI: 10.1073/pnas.2212431119 | PMCID: PMC9704712 | PMID: 36399550
- Evidence: Maximum likelihood gene trees with 100 bootstrap replicates were made with both RAxML and in MEGA with partial deletion ( 98 , 99 ).
- Full pipeline: stage not stated [RAxML]

### Tissue-specific regulation of lipid polyester synthesis genes controlling oxygen permeation into <i>Lotus japonicus</i> nodules. (PNAS 2022)

- DOI: 10.1073/pnas.2206291119 | PMCID: PMC9704718 | PMID: 36375074
- Evidence: Maximum-likelihood phylogeny trees were constructed in CIPRES ( http://www.phylo.org/ ) using default parameters of the RAxML-HPC BlackBox tool version 8.2.12 ( 64 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [ImageJ] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, R] -> stage not stated [RAxML, ggpubr v0.4.0.999, pheatmap]

### Phylodynamic signatures in the emergence of community-associated MRSA. (PNAS 2022)

- DOI: 10.1073/pnas.2204993119 | PMCID: PMC9659408 | PMID: 36322765
- Evidence: As input, we used the phylogenetic tree inferred using ML in RAxML-NG after removing recombination with Gubbins.
- Full pipeline: quality control [Nextflow] -> variant calling [Nextflow] -> normalisation [TreeTime v0.7.1] -> differential/statistical testing [Nextflow] -> structure determination [Nextflow] -> stage not stated [RAxML]

### Coevolution of tandemly repeated <i>hlips</i> and RpaB-like transcriptional factor confers desiccation tolerance to subaerial <i>Nostoc</i> species. (PNAS 2022)

- DOI: 10.1073/pnas.2211244119 | PMCID: PMC9586280 | PMID: 36215485
- Version used: **8.1.20**
- Evidence: For the phylogenetic analysis, the Hrf1 sequences from representative species were aligned using the MAFFT multiple alignment program and the maximum-likelihood phylogenetic tree was generated by RAxML v8.1.20 under the PROTGAMMA model with 1,000 bootstrap replicates ( 71 , 72 ).
- Full pipeline: alignment/mapping [MAFFT, RAxML v8.1.20]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Evidence: Then, RAxML was applied to these sequence sets to build phylogenetic trees ( 84 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **8.0.19**
- Evidence: RAxML (v8.0.19) was used to build a phylogenetic tree with the parameters: “-n cds -m GTRGAMMA -p 12345 -x 12345 -# 1000 -f ad”.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Green diatom mutants reveal an intricate biosynthetic pathway of fucoxanthin. (PNAS 2022)

- DOI: 10.1073/pnas.2203708119 | PMCID: PMC9499517 | PMID: 36095219
- Version used: **8.0.14**
- Evidence: Maximum likelihood (ML) trees were inferred from the protein alignments using PThreads in RAxML 8.0.14 ( 58 ) and the WAG substitution model ( 59 ) with gamma rate distribution (“PROTGAMMAWAG,” four discrete rate categories).
- Full pipeline: alignment/mapping [RAxML v8.0.14]

### Convergent evolution of a genotoxic stress response in a parasite-specific p53 homolog. (PNAS 2022)

- DOI: 10.1073/pnas.2205201119 | PMCID: PMC9478680 | PMID: 36067283
- Evidence: BMGE trimmed sequences were next filtered for identical sequences (i.e., p53 homologs from closely related animals) and were then analyzed using Randomized Axelerated Maximum Likelihood (RAxML) version 8.2.12 ( 39 ) via raxmlGUI version 2.0.6 ( 40 ) with the following parameters: -f a -x 256425 -p 256425 -N 1000 -m PROTGAMMAPMB -k -O.
- Full pipeline: read trimming [MAFFT, RAxML] -> alignment/mapping [MAFFT]

### Biotic colonization of subtropical East Asian caves through time. (PNAS 2022)

- DOI: 10.1073/pnas.2207199119 | PMCID: PMC9407641 | PMID: 35969742
- Version used: **8.2.10**
- Evidence: For each clade, we first performed maximum-likelihood (ML) searches using RAxML v8.2.10 ( 37 ) for each locus and deleted those species that were a source of significant incongruence between different locus trees based on a threshold bootstrap value >70% ( 38 ).
- Full pipeline: differential/statistical testing [R, RAxML v8.2.10]

### Divergent evolution of extreme production of variant plant monounsaturated fatty acids. (PNAS 2022)

- DOI: 10.1073/pnas.2201160119 | PMCID: PMC9335243 | PMID: 35867834
- Version used: **8.2.4**
- Evidence: Both alignments were analyzed by maximum likelihood using RAxML v8.2.4 ( 62 ) with the PROTGAMMAAUTO model and 1,000 bootstrap replicates.
- Full pipeline: alignment/mapping [RAxML v8.2.4] -> normalisation [CCP4] -> structure determination [PHENIX] -> visualisation [PyMOL]

### Uncovering the enigmatic evolution of bears in greater depth: The hybrid origin of the Asiatic black bear. (PNAS 2022)

- DOI: 10.1073/pnas.2120307119 | PMCID: PMC9351369 | PMID: 35858381
- Version used: **8.2.11**
- Evidence: 22,105 genomic windowed trees (100 kb) and 13,529 protein-coding gene trees were first reconstructed using RAxML version 8.2.11 ( 52 ) with the GTRGAMMAI model and 100 bootstrap replicates, and then the species trees were estimated using MP-EST.
- Full pipeline: read trimming [BWA v0.78] -> alignment/mapping [BWA v0.78, MAFFT v7.486, SAMtools v0.1.18] -> registration [GATK v3.7] -> structure determination [RAxML v8.2.11] -> stage not stated [Picard v1.87, VCFtools v0.1.14]

### The durability of natural infection and vaccine-induced immunity against future infection by SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2204336119 | PMCID: PMC9351502 | PMID: 35858382
- Version used: **7.2.8**
- Evidence: We analyzed the concatenated alignment of the S , M , and ORF1b genes to reconstruct maximum-likelihood molecular phylogenies using IQ-TREE v2.0.6 ( 24 ) and RAxML v7.2.8 ( 25 ), with 1,000 nonparametric bootstrap replicates to assess node support.
- Full pipeline: alignment/mapping [IQ-TREE v2.0.6, RAxML v7.2.8] -> normalisation [TreeTime v0.7.6] -> structure determination [IQ-TREE v2.0.6, RAxML v7.2.8]

### The evolution of synaptic and cognitive capacity: Insights from the nervous system transcriptome of &lt;i&gt;Aplysia&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122301119 | PMCID: PMC9282427 | PMID: 35867761
- Evidence: A dendrogram from a RAxML analysis (see Methods and SI Appendix , Table S2 ) with bootstrap values shown for values ≥50%.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> differential/statistical testing [RAxML] -> stage not stated [BUSCO]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **8.2.12**
- Evidence: To specify a starting tree constraint (-s), we ran RAxML v.8.2.12 ( 86 ) with ascertainment bias correction (–asc-corr = lewis) on a reduced dataset containing the highest-coverage representative of each subspecies to obtain a maximum likelihood phylogeny.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Insights into bear evolution from a Pleistocene polar bear genome. (PNAS 2022)

- DOI: 10.1073/pnas.2200016119 | PMCID: PMC9214488 | PMID: 35666863
- Evidence: Although the initial tree with no migration edges largely recapitulated the splits already seen in the RAxML autosomal SNP analysis ( SI Appendix , Fig.
- Full pipeline: stage not stated [ADMIXTURE, RAxML]

### Repeated translocation of a supergene underlying rapid sex chromosome turnover in <i>Takifugu</i> pufferfish. (PNAS 2022)

- DOI: 10.1073/pnas.2121469119 | PMCID: PMC9191631 | PMID: 35658077
- Version used: **0.8**
- Evidence: To determine the phylogenetic relationships of the male-specific genes and their autosomal paralog(s), we used RAxML (version 0.8) ( SI Appendix , Methods ).
- Full pipeline: alignment/mapping [BWA, minimap2] -> stage not stated [BUSCO, RAxML v0.8]

### Ancient proteins resolve controversy over the identity of <i>Genyornis</i> eggshell. (PNAS 2022)

- DOI: 10.1073/pnas.2109326119 | PMCID: PMC9995833 | PMID: 35609205
- Version used: **1.0.3**
- Evidence: Maximum likelihood trees were inferred using RAxML-NG v.1.0.3 ( 114 ) using 10 parsimony and 10 random starting trees, and the number of bootstrap replicates were determined using bootstopping ( 115 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, MUSCLE v3.8.31] -> stage not stated [AlphaFold, ColabFold, R v4.1, RAxML v1.0.3, phytools]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: Maximum likelihood analyses and bootstrapping (1,000 replicates) were performed using RAxML v7 ( 65 ).
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Genomic insights into zokors' phylogeny and speciation in China. (PNAS 2022)

- DOI: 10.1073/pnas.2121819119 | PMCID: PMC9171634 | PMID: 35512099
- Evidence: Discordant tree analysis was performed with RAxML, ASTRAL, and DiscoVista.
- Full pipeline: alignment/mapping [GATK] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BUSCO, RAxML, VCFtools]

### Stone Age <i>Yersinia pestis</i> genomes shed light on the early evolution, diversity, and ecology of plague. (PNAS 2022)

- DOI: 10.1073/pnas.2116722119 | PMCID: PMC9169917 | PMID: 35412864
- Version used: **0.9.0**
- Evidence: The resulting snpAlignment was used to compute a ML tree with RAxML-NG (v0.9.0, https://github.com/amkozlov/raxml-ng ) Molecular Dating Analyses.
- Full pipeline: variant calling [GATK, Picard] -> differential/statistical testing [GATK, Picard] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.25.0, RAxML v0.9.0, ggpubr]

### Origin and early evolution of the plant terpene synthase family. (PNAS 2022)

- DOI: 10.1073/pnas.2100361119 | PMCID: PMC9169658 | PMID: 35394876
- Evidence: For the maximum likelihood analyses, RAxML ( 53 ) was used with 1,000 bootstrap replicates under the best substitution model (JTT+G+F).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [HMMER v3.0, RAxML]

### Layered evolution of gene expression in "superfast" muscles for courtship. (PNAS 2022)

- DOI: 10.1073/pnas.2119671119 | PMCID: PMC9168950 | PMID: 35363565
- Evidence: We used MVFtools “InferTrees” method to construct a RAxML-NG maximum-likelihood phylogeny of a single concatenated alignment using the GTR+Γ model ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [BCFtools, BWA, RAxML, STAR v2.7.3a] -> differential/statistical testing [limma] -> stage not stated [featureCounts v2.0.1]

### Leg length and bristle density, both necessary for water surface locomotion, are genetically correlated in water striders. (PNAS 2022)

- DOI: 10.1073/pnas.2119210119 | PMCID: PMC8892508 | PMID: 35193982
- Evidence: Maximum-likelihood searches were performed using RAxML ( 56 ) under the LG+Γ+I model.
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [DESeq2, RSEM] -> differential/statistical testing [DESeq2] -> structure determination [MUSCLE] -> stage not stated [RAxML]

### Multiple spillovers from humans and onward transmission of SARS-CoV-2 in white-tailed deer. (PNAS 2022)

- DOI: 10.1073/pnas.2121644119 | PMCID: PMC8833191 | PMID: 35078920
- Evidence: The genome sequences were screened for quality, SNP positions called against the SARS-CoV-2 reference genome ( NC_045512 ), and SNP alignments used to generate a maximum-likelihood phylogenetic tree using RAxML.
- Full pipeline: read trimming [SAMtools v1.11] -> alignment/mapping [QGIS, RAxML] -> variant calling [SAMtools v1.11] -> stage not stated [Pangolin v3.1.11]

### Discovery of ultrafast myosin, its amino acid sequence, and structural features. (PNAS 2022)

- DOI: 10.1073/pnas.2120962119 | PMCID: PMC8872768 | PMID: 35173046
- Evidence: The phylogenetic tree was constructed using RAxML with -m PROTGAMMALGF option.
- Full pipeline: stage not stated [RAxML]

### Occasional paternal inheritance of the germline-restricted chromosome in songbirds. (PNAS 2022)

- DOI: 10.1073/pnas.2103960119 | PMCID: PMC8794876 | PMID: 35058355
- Version used: **1.0.2**
- Evidence: All phylogenetic trees were built using RAxML-NG v1.0.2 ( 46 ) assuming a general time-reversible model and a discrete gamma model of rate heterogeneity with 100 randomized parsimony starting trees and 1,000 bootstrap replicates (for details, see Data Accessibility ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard] -> quantification [Picard] -> differential/statistical testing [R v4.0, lme4] -> stage not stated [BCFtools v1.9, GATK, RAxML v1.0.2, SAMtools v1.6]

### Acquisition of the arginine deiminase system benefits epiparasitic Saccharibacteria and their host bacteria in a mammalian niche environment. (PNAS 2022)

- DOI: 10.1073/pnas.2114909119 | PMCID: PMC8764695 | PMID: 34992141
- Version used: **8.2.11**
- Evidence: Concatenated and aligned trees were inferred using RAxML (version 8.2.11) with the following commands: best tree and perform “fast bootstrapping”. raxmlHPC-PTHREADS-SSE3 -s 96_genomes.phy -n 96_genomes -m GTRCAT -q 96_genomes.partitions -p 12345 -T 12 -f a -x 12345 -N 100.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE, RAxML v8.2.11] -> visualisation [MUSCLE] -> stage not stated [Python, eggNOG]

### Convergent evolution of venom gland transcriptomes across Metazoa. (PNAS 2022)

- DOI: 10.1073/pnas.2111392119 | PMCID: PMC8740685 | PMID: 34983844
- Evidence: The expression tree (Neighbor-Joining) was constructed using two distance metrics, 1-Spearman coefficient and Euclidean distances, and the species tree was based on multisequence alignments of 1:1 orthogroups using RAxML ( 18 ).
- Full pipeline: quality control [kallisto] -> read trimming [kallisto] -> alignment/mapping [RAxML] -> quantification [kallisto] -> normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [Bioconductor, InterProScan]

### No link between population isolation and speciation rate in squamate reptiles. (PNAS 2022)

- DOI: 10.1073/pnas.2113388119 | PMCID: PMC8795558 | PMID: 35058358
- Version used: **8.2.11**
- Evidence: We then concatenated these alignments and used RAxML v8.2.11 ( 103 ) to infer a phylogeny across all individuals.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [GATK v4.1.8, RAxML v8.2.11, SAMtools v1.5] -> stage not stated [R, phytools]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: Region-specific phylogenies were then inferred at the level of individual samples with RAxML-NG ( 101 ) based on the GTR + G model, 10 each of random and parsimony starting trees, and 100 bootstrap replicates (git 14.5 to 14.6).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Insight into the symbiotic lifestyle of DPANN archaea revealed by cultivation and genome analyses. (PNAS 2022)

- DOI: 10.1073/pnas.2115449119 | PMCID: PMC8784108 | PMID: 35022241
- Evidence: An MLtree was constructed using RAxML ( 21 ) with the GTRGAMMA model.
- Full pipeline: stage not stated [HMMER, Prokka v1.13, RAxML, eggNOG v4.5.1]

### Longitudinal clonal dynamics of HIV-1 latent reservoirs measured by combination quadruplex polymerase chain reaction and sequencing. (PNAS 2022)

- DOI: 10.1073/pnas.2117630119 | PMCID: PMC8794825 | PMID: 35042816
- Version used: **8.2.11**
- Evidence: Sequence alignments, phylogenetic trees, and calculation of patristic distance to measure both the genetic distance and topology of the phylogenetic trees were performed by using Geneious Pro software, version 2020.0.3 and RAxML 8.2.11.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [RAxML v8.2.11] -> structure determination [SPAdes v3.13.1]

### Integrated genomic and functional analyses of human skin-associated &lt;i&gt;Staphylococcus&lt;/i&gt; reveal extensive inter- and intra-species diversity. (PNAS 2023)

- DOI: 10.1073/pnas.2310585120 | PMCID: PMC10666031 | PMID: 37956283
- Version used: **1.1.0**
- Evidence: Maximum likelihood (ML) phylogenetic trees were constructed using RAxML-NG v1.1.0 ( 55 ), based on the core-gene alignment generated by panaroo. iTOL v6 ( 56 ) was used for tree display and annotation.
- Full pipeline: alignment/mapping [RAxML v1.1.0] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [DADA2, R v4.2, eggNOG, phyloseq]

### Male-killing virus in a noctuid moth &lt;i&gt;Spodoptera litura&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312124120 | PMCID: PMC10655585 | PMID: 37931114
- Evidence: The RdRP sequences were aligned using MAFFT, trimmed manually, as well as using TrimAl, and then used for maximum likelihood tree reconstruction using RAxML, by applying the best evolutionary model found by ModelTest-NG.
- Full pipeline: read trimming [MAFFT, RAxML] -> alignment/mapping [MAFFT, RAxML] -> structure determination [MAFFT, RAxML] -> stage not stated [BLAST]

### Bacterial tolerance to host-exuded specialized metabolites structures the maize root microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2310134120 | PMCID: PMC10622871 | PMID: 37878725
- Version used: **8.2.12**
- Evidence: 7.475 ( 74 ) with default options, and analyzed with RAxML v.
- Full pipeline: alignment/mapping [MAFFT v7.475] -> stage not stated [DESeq2, R, RAxML v8.2.12, emmeans, phyloseq, phytools]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Evidence: The phylogenetic tree was constructed using RAxML ( 82 ).
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### Cooperation and cheating orchestrate Vibrio assemblages and polymicrobial synergy in oysters infected with OsHV-1 virus. (PNAS 2023)

- DOI: 10.1073/pnas.2305195120 | PMCID: PMC10556616 | PMID: 37751557
- Evidence: Phylogenetic trees for each marker were reconstructed with RAxML using a GTR model of evolution and Gamma law of rate heterogeneity.
- Full pipeline: quantification [DESeq2 v1.36.0] -> differential/statistical testing [phyloseq] -> structure determination [RAxML] -> stage not stated [DADA2 v1.14, QIIME 2]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Evidence: Maximum likelihood analyses were conducted using IQ-Tree 2 and RAxML ( 88 ).
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### Reactive oxygen species are regulated by immune deficiency and Toll pathways in determining the host specificity of honeybee gut bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2219634120 | PMCID: PMC10438842 | PMID: 37556501
- Evidence: The phylogenetic tree including B19101 and W8127 was built with RAxML ( 63 ).
- Full pipeline: stage not stated [RAxML]

### The genomic landscape of swine influenza A viruses in Southeast Asia. (PNAS 2023)

- DOI: 10.1073/pnas.2301926120 | PMCID: PMC10438389 | PMID: 37552753
- Version used: **1.1.0**
- Evidence: Maximum likelihood (ML) phylogenies for H1, H3, N1, N2, and six internal genes (PB2, PB1, PA, NP, MP, and NS) were individually reconstructed using RAxML-NG v1.1.0 ( 55 ) with the following number of sequences H1-HA (n = 1,009), N1-NA (n = 986), H3-HA (n = 766), N2-NA (n = 773), PB2 (n = 924), PB1 (n = 923), PA (n = 915), NP (n = 927), MP (n = 927) and NS (n = 927).
- Full pipeline: quality control [FastQC, Trimmomatic v0.39] -> read trimming [FastQC, Trimmomatic v0.39] -> structure determination [BEAST v10.4, RAxML v1.1.0] -> stage not stated [BLAST v2.2.18, SPAdes v3.15.3]

### Speciation across the Earth driven by global cooling in terrestrial orchids. (PNAS 2023)

- DOI: 10.1073/pnas.2102408120 | PMCID: PMC10629580 | PMID: 37428929
- Evidence: After an initial ML search with 1,000 BS replicates using RAxML V8 ( 101 ), we identified and removed taxa exhibiting rogue behavior in the BS replicates using RogueNaRok ( 102 ).
- Full pipeline: stage not stated [R, RAxML]

### Echoes of ancient introgression punctuate stable genomic lineages in the evolution of figs. (PNAS 2023)

- DOI: 10.1073/pnas.2222035120 | PMCID: PMC10334730 | PMID: 37399402
- Evidence: A maximum-likelihood tree based on the unpartitioned alignment was inferred with RAxML-ng under the “GTRCAT” model, with 1,000 bootstrap replicates.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.450, RAxML] -> stage not stated [SAMtools]

### <i>oskar</i> acts with the transcription factor Creb to regulate long-term memory in crickets. (PNAS 2023)

- DOI: 10.1073/pnas.2218506120 | PMCID: PMC10214185 | PMID: 37192168
- Evidence: A maximum likelihood tree was created in RAxML using the PROTGAMMAWAG model ( 62 ) and plotted with the FigTree package v1.4.4 ( http://tree.bio.ed.ac.uk/software/figtree ) ( Fig.
- Full pipeline: read trimming [Cutadapt v3.4, RSEM v1.2.29, STAR v2.7.0e] -> alignment/mapping [MAFFT v7.510] -> quantification [Cutadapt v3.4, ImageJ, RSEM v1.2.29, STAR v2.7.0e] -> visualisation [RAxML]

### Evolution of coronavirus frameshifting elements: Competing stem networks explain conservation and variability. (PNAS 2023)

- DOI: 10.1073/pnas.2221324120 | PMCID: PMC10193956 | PMID: 37155888
- Version used: **8.2.12**
- Evidence: A phylogenetic tree is built upon the whole genome MSA using RAxML v8.2.12 ( 58 ).
- Full pipeline: stage not stated [Pangolin, RAxML v8.2.12]

### Evolution and diversification of the ACT-like domain associated with plant basic helix-loop-helix transcription factors. (PNAS 2023)

- DOI: 10.1073/pnas.2219469120 | PMCID: PMC10175843 | PMID: 37126718
- Version used: **1.1.0**
- Evidence: ML trees of the ACT-like and bHLH domains derived from Chloroplastida were constructed by best-fit substitution models chosen by ProtTest v3.4.2 ( 58 ) with 1,000 or 2,000 iterations using the Transfer Bootstrap method ( 59 ), or using the SH-aLRT implemented in RAxML-NG v1.1.0 ( 43 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [AlphaFold, ColabFold, RAxML v1.1.0]

### Identification of hidden associations among eukaryotic genes through statistical analysis of coevolutionary transitions. (PNAS 2023)

- DOI: 10.1073/pnas.2218329120 | PMCID: PMC10120013 | PMID: 37043529
- Version used: **8.2.12**
- Evidence: 2022), or to a fully resolved tree (1263 internal node) obtained with RAxML (v.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Python, RAxML v8.2.12]

### The <i>Holothuria leucospilota</i> genome elucidates sacrificial organ expulsion and bioadhesive trap enriched with amyloid-patterned proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2213512120 | PMCID: PMC10120082 | PMID: 37036994
- Evidence: Multiple sequence alignments for all gene families mentioned above were built with the Multiple Alignment using Fast Fourier Transform (MAFFT) aligner, while their corresponding phylogeny was inferred with RAxML, followed by visualization with Evolview.
- Full pipeline: alignment/mapping [BUSCO, BWA, MAFFT, RAxML] -> normalisation [DESeq2] -> visualisation [MAFFT, RAxML] -> stage not stated [AlphaFold, InterProScan]

### Bacterial origin of a key innovation in the evolution of the vertebrate eye. (PNAS 2023)

- DOI: 10.1073/pnas.2214815120 | PMCID: PMC10120077 | PMID: 37036996
- Evidence: Maximum likelihood phylogenetic analyses were performed using IQ-TREE ( 40 ) or RAxML ( 41 ) as indicated in Table 1 and Dataset S5 .
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, BLAST, IQ-TREE, RAxML]

### Aneuploidy and gene dosage regulate filamentation and host colonization by &lt;i&gt;Candida albicans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2218163120 | PMCID: PMC10089209 | PMID: 36893271
- Version used: **8.2.12**
- Evidence: RAxML version 8.2.12 ( 63 ) with the GTRCAT model of substitution and 1,000 bootstraps was used to infer phylogenetic relationships between the SC5314 isolates using the dataset of 8,264 confident SNPs.
- Full pipeline: alignment/mapping [Picard, SAMtools, minimap2 v2.17] -> variant calling [VCFtools, minimap2 v2.17] -> differential/statistical testing [R] -> visualisation [Cutadapt] -> stage not stated [GATK, ImageJ, RAxML v8.2.12]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Evidence: Unpartitioned phylogenetic analyses were performed using IQTree (all datasets), and partitioned analyses were performed with RAxML (extended dataset only).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Edaphic specialization onto bare, rocky outcrops as a factor in the evolution of desert angiosperms. (PNAS 2023)

- DOI: 10.1073/pnas.2214729120 | PMCID: PMC9963280 | PMID: 36716359
- Evidence: ML and BI trees were generated using RAxML-NG ( 51 ) and ExaBayes ( 52 ) on the CIPRES science supercomputing portal ( 53 ) and a pseudocoalescent tree from gene trees while accounting for ILS was produced using ASTRAL-III ( 54 ) ( SI Appendix , Figs.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [RAxML]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Evidence: Illumina reads for the VNII strains shown were aligned to the Cryptococcus neoformans H99 reference genome to identify SNPs across the genome, which were used to infer a phylogeny with RAxML.
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Landscape dynamics and diversification of the megadiverse South American freshwater fish fauna. (PNAS 2023)

- DOI: 10.1073/pnas.2211974120 | PMCID: PMC9926176 | PMID: 36595684
- Evidence: We performed tree searches in RAxML assuming independent GTR + G models for partitions and a start tree with a few justifiable node constraints.
- Full pipeline: stage not stated [RAxML]

### Two-speed genome evolution drives pathogenicity in fungal pathogens of animals. (PNAS 2023)

- DOI: 10.1073/pnas.2212633120 | PMCID: PMC9926174 | PMID: 36595674
- Evidence: ( A ) a phylogenetic tree of Bsal and its three closest relatives: Bd , Hp , and Eh constructed using a core ortholog multiple alignment and RAxML.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, RAxML] -> stage not stated [BUSCO, Canu v1.8, GATK, HMMER, RepeatMasker v4.0.5]

### Photosynthetic demands on translational machinery drive retention of redundant tRNA metabolism in plant organelles. (PNAS 2024)

- DOI: 10.1073/pnas.2421485121 | PMCID: PMC11670086 | PMID: 39693336
- Version used: **8.2.12**
- Evidence: S8–S10 ). using RAxML v 8.2.12 ( 103 ) after aligning sequences using MAFFT v7.525 ( 104 ) trimming with trimAl v1.5 ( 105 ).
- Full pipeline: read trimming [MAFFT v7.525, RAxML v8.2.12, SPAdes v3.15.4] -> alignment/mapping [MAFFT v7.525, RAxML v8.2.12] -> visualisation [Python]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Evidence: The phylogeny tree was built using RAxML with 1,000 bootstraps.
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### Electrochemical cofactor recycling of bacterial microcompartments. (PNAS 2024)

- DOI: 10.1073/pnas.2414220121 | PMCID: PMC11626177 | PMID: 39585991
- Version used: **0.6.0**
- Evidence: The sequence alignment was then used to construct a maximum likelihood tree using RAxML-NG (v0.6.0) ( 64 ).
- Full pipeline: read trimming [Clustal Omega] -> alignment/mapping [Clustal Omega, RAxML v0.6.0] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### &lt;i&gt;Prevotella&lt;/i&gt; are major contributors of sialidases in the human vaginal microbiome. (PNAS 2024)

- DOI: 10.1073/pnas.2400341121 | PMCID: PMC11388281 | PMID: 39186657
- Version used: **8.2.10**
- Evidence: We used HMMER (v3.3.2) to find ribosomal proteins, aligned the sequences with MAFFT (v7.508) and used RAxML (v.8.2.10) to create the phylogenetic trees.
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508, RAxML v8.2.10] -> stage not stated [AlphaFold, InterProScan, Python]

### Climate, demography, immunology, and virology combine to drive two decades of dengue virus dynamics in Cambodia. (PNAS 2024)

- DOI: 10.1073/pnas.2318704121 | PMCID: PMC11388344 | PMID: 39190356
- Evidence: Serotype-specific maximum likelihood phylogenetic trees were constructed in RAxML ( 77 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [BEAST] -> stage not stated [R, RAxML]

### Phylogenetic evidence clarifies the history of the extrusion of Indochina. (PNAS 2024)

- DOI: 10.1073/pnas.2322527121 | PMCID: PMC11363272 | PMID: 39159371
- Version used: **8.2.10**
- Evidence: For each clade, we first used maximum likelihood (ML) to conduct nonparametric bootstrap analyses for each locus in RAxML v8.2.10 ( 49 ) and then removed those species that occurred in different locus trees with significant conflict based on the threshold of bootstrap value >70% ( 50 ).
- Full pipeline: differential/statistical testing [RAxML v8.2.10] -> structure determination [phytools v0.7]

### Computational detection of antigen-specific B cell receptors following immunization. (PNAS 2024)

- DOI: 10.1073/pnas.2401058121 | PMCID: PMC11363332 | PMID: 39163333
- Evidence: The lineages are inferred using HILARy software ( 15 ), and the corresponding trees are reconstructed with RAxML ( 59 ) and represented with iTOL ( 70 ).
- Full pipeline: structure determination [RAxML]

### Flexible oviposition behavior enabled the evolution of terrestrial reproduction. (PNAS 2024)

- DOI: 10.1073/pnas.2312371121 | PMCID: PMC11295038 | PMID: 39042675
- Version used: **1.0.3**
- Evidence: A maximum likelihood (ML) tree of concatenated sequences, with the appropriate model applied to each gene partition, was estimated with RAxML-NG v1.0.3 ( 38 ) implemented in raxmlGUI v2.0 ( 37 ) using 1,000 bootstrap iterations to estimate node support.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2] -> stage not stated [ImageJ, RAxML v1.0.3, emmeans, lme4, phytools]

### Amoebozoan testate amoebae illuminate the diversity of heterotrophs and the complexity of ecosystems throughout geological time. (PNAS 2024)

- DOI: 10.1073/pnas.2319628121 | PMCID: PMC11287125 | PMID: 39012821
- Version used: **8.2.12**
- Evidence: The topological support values inferred from MLRB were mapped onto the ML tree using RAxML v.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RAxML v8.2.12] -> stage not stated [BUSCO v5.3.2, IQ-TREE]

### A wound-induced differentiation trajectory for neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2322864121 | PMCID: PMC11260127 | PMID: 38976727
- Version used: **8.2.4**
- Evidence: Alignments were trimmed using Gblocks ( 118 , 119 ) with the least stringent parameters Phylogenetic trees were inferred using Maximum Likelihood analysis with 1,000 bootstrap replicates, implemented in RAxML (v8.2.4) ( 120 ) using the WAG+G model of protein evolution.
- Full pipeline: read trimming [RAxML v8.2.4] -> alignment/mapping [MUSCLE v3.8.31, RAxML v8.2.4] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [BUSCO v3.0.2, Pilon v1.23]

### Multisubstrate specificity shaped the complex evolution of the aminotransferase family across the tree of life. (PNAS 2024)

- DOI: 10.1073/pnas.2405524121 | PMCID: PMC11214133 | PMID: 38885378
- Version used: **1.2.0**
- Evidence: To avoid a potential issue of a local optima described in the previous study ( 66 ), we generated 40 FastTree trees using 20 random and 20 parsimony starting trees prepared by RAxML-NG (v1.2.0) with a JTT+G model, and then selected the most likelihood trees.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [seaborn] -> simulation/modelling [AutoDock Vina v4.2.6] -> stage not stated [AlphaFold v2.1.0, HMMER v3.3.1, RAxML v1.2.0]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: ModelTest-NG ( 99 ) was used to identify the best-fitting model and 100 bootstrap replicates were performed for each LCN OG tree using RAxML-NG ( 100 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Version used: **8.2.4**
- Evidence: ND2 phylogenies were estimated using maximum likelihood (ML) in RAxML v8.2.4 ( 92 ) and Markov chain Monte Carlo (MCMC) in Beast2 2.6.7 ( 93 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### Evolution of homologous recombination rates across bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316302121 | PMCID: PMC11067023 | PMID: 38657048
- Evidence: A strain phylogeny was then generated from the core genome nucleotide concatenate of each species using RAxML v8 with a GTR+gamma model ( 58 ).
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> differential/statistical testing [R] -> simulation/modelling [R] -> stage not stated [HMMER, RAxML]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Evidence: A phylogenetic tree was constructed using RAxML ( 92 ) and data for 215794 high-confidence SNPs available for all 296 strains.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### Intergenerational protective anti-gut commensal immunoglobulin G originates in early life. (PNAS 2024)

- DOI: 10.1073/pnas.2309994121 | PMCID: PMC10990157 | PMID: 38517976
- Evidence: The GTR+I + G4 model was used with the –all options in RAxML-ng v.
- Full pipeline: read trimming [Bowtie2 v2.4.1, MAFFT v7.475] -> alignment/mapping [Bowtie2 v2.4.1, MAFFT v7.475] -> dimensionality reduction/clustering [Docker] -> visualisation [R v4.0, phyloseq] -> stage not stated [BLAST, RAxML]

### The evolutionary genomics of adaptation to stress in wild rhizobium bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2311127121 | PMCID: PMC10990125 | PMID: 38507447
- Evidence: We then constructed a ML tree using RAxML ( 80 ) with rapid bootstrapping.
- Full pipeline: quality control [Prokka v1.13.3] -> read trimming [MUSCLE] -> alignment/mapping [MAFFT v7.475, MUSCLE] -> differential/statistical testing [lme4 v1.1] -> visualisation [R] -> stage not stated [RAxML, SPAdes v3.14.1]

### The extent of introgression between incipient <i>Clarkia</i> species is determined by temporal environmental variation and mating system. (PNAS 2024)

- DOI: 10.1073/pnas.2316008121 | PMCID: PMC10963018 | PMID: 38466849
- Version used: **8.2.11**
- Evidence: We converted our filtered VCF to a fasta (vcf2phylip.py script from https://github.com/edgardomortiz/vcf2phylip ) and inferred the phylogenetic relationships among taxa with RAxML version 8.2.11 ( 98 ) using the GTR model and rapid bootstrapping.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, Picard, SAMtools] -> variant calling [GATK v3.8.0] -> stage not stated [BCFtools, Canu v2.1, RAxML v8.2.11]

### The metabolic domestication syndrome of budding yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2313354121 | PMCID: PMC10945815 | PMID: 38457520
- Evidence: We built a concatenated maximum likelihood tree with RAxML (AVX version, 8.2.12) ( 73 ) using the LG amino acid substitution matrix with the GAMMA model and using one partition for each orthogroup.
- Full pipeline: alignment/mapping [MAFFT v7.471] -> dimensionality reduction/clustering [OrthoFinder v2.4.0] -> stage not stated [RAxML]

### Genome copy number predicts extreme evolutionary rate variation in plant mitochondrial DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2317240121 | PMCID: PMC10927533 | PMID: 38427600
- Evidence: Then, absolute time since divergence events was estimated from a chronogram made using a phylogeny based on matK plastid sequences constructed in RAxML-NG (using default settings) and then using r8s to time calibrate the tree ( 83 – 85 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.5, SAMtools] -> differential/statistical testing [R v4.2.2] -> visualisation [ggplot2] -> stage not stated [RAxML, SPAdes]

### Dual membrane-spanning anti-sigma factors regulate vesiculation in <i>Bacteroides thetaiotaomicron</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2321910121 | PMCID: PMC10927553 | PMID: 38422018
- Version used: **8.2.12**
- Evidence: The core genome alignment from panaroo was constructed into a maximum likelihood phylogenetic tree using RAxML v8.2.12 with the command “raxmlHPC -s core_gene_alignment.aln -n EP_raxml -m GTRGAMMA -f a -T 4 -N 100 -p 12345 -x 54321” {24451623}.
- Full pipeline: alignment/mapping [RAxML v8.2.12] -> stage not stated [AlphaFold]

### Genomes, fossils, and the concurrent rise of modern birds and flowering plants in the Late Cretaceous. (PNAS 2024)

- DOI: 10.1073/pnas.2319696121 | PMCID: PMC10895254 | PMID: 38346181
- Evidence: Moreover, we applied concatenation methods rooted in maximum likelihood (ML) approaches as implemented in RAxML ( 13 ).
- Full pipeline: stage not stated [BLAST, OrthoFinder v2.3.12, R, RAxML]

### A recent gibbon ape leukemia virus germline integration in a rodent from New Guinea. (PNAS 2024)

- DOI: 10.1073/pnas.2220392121 | PMCID: PMC10861895 | PMID: 38305758
- Version used: **8.2.11**
- Evidence: A Maximum likelihood (ML) tree was constructed with rapid bootstrapping (1,000 replicates) and GTRGAMMA substitution rate in Randomized Axelerated ML (RAxML v8.2.11) ( 52 ).
- Full pipeline: read trimming [Cutadapt v1.15, Picard v1.4, Trimmomatic v0.27] -> alignment/mapping [PyMOL v2.4] -> differential/statistical testing [MrBayes v3.2.7] -> simulation/modelling [MrBayes v3.2.7] -> stage not stated [QGIS v3.16.10, RAxML v8.2.11]

### Extraordinary preservation of gene collinearity over three hundred million years revealed in homosporous lycophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2312607121 | PMCID: PMC10823260 | PMID: 38236735
- Version used: **8.2.12**
- Evidence: Phylogenetic trees were constructed using low-copy orthologous genes with RAxML v8.2.12 ( 61 ) and ASTRAL v5.7.1 ( 62 ), respectively.
- Full pipeline: stage not stated [ANGSD v0.935, BUSCO, DESeq2 v3.17, RAxML v8.2.12]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **8.2.12**
- Evidence: The genome-wide alignment sequences constructed above were cut into different window sizes, and a maximum likelihood method was used to construct a phylogenetic tree (RAxML v8.2.12) ( https://github.com/stamatak/standard-RAxML ).
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Microbial necromass carbon enhances arsenic methylation in paddy soils. (PNAS 2025)

- DOI: 10.1073/pnas.2527462122 | PMCID: PMC12685052 | PMID: 41289391
- Evidence: These placements were conducted using RAxML with the parameters “-f v -G 0.2 -m PROTGAMMALGX”.
- Full pipeline: differential/statistical testing [DESeq2 v1.44.0] -> stage not stated [BLAST, R v4.2, RAxML]

### Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage. (PNAS 2025)

- DOI: 10.1073/pnas.2517473122 | PMCID: PMC12626013 | PMID: 41196353
- Evidence: Gene trees were generated using the Geneious RAxML plug-in 8.2.11 and GAMMA BLOSUM62 substitution matrix with n_bootstraps=100.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [Cufflinks v2.2.1, DESeq2 v1.20.0, HISAT2 v2.1.0, MAFFT] -> stage not stated [Prokka, RAxML, SciPy]

### Symbiotic solutions for colony nutrition: Conserved nitrogen recycling within the bacterial pouch of &lt;i&gt;Tetraponera&lt;/i&gt; ants. (PNAS 2025)

- DOI: 10.1073/pnas.2514882122 | PMCID: PMC12595465 | PMID: 41150726
- Version used: **8.2.12**
- Evidence: Both analyses utilized maximum likelihood approach using RAxML v8.2.12 ( 81 ) with 1,000 bootstraps.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic] -> read trimming [FastQC v0.11.9, Trimmomatic] -> differential/statistical testing [QUAST] -> stage not stated [BLAST, Flye v2.9, RAxML v8.2.12]

### When islands collide: Divergence predicts outcomes of secondary contact during the fusion of Sulawesi's paleo-archipelago. (PNAS 2025)

- DOI: 10.1073/pnas.2514344122 | PMCID: PMC12625910 | PMID: 41144686
- Version used: **8.2.12**
- Evidence: We estimated gene trees using RAxML v8.2.12 ( 63 ) under the GTRGAMMA model with 100 bootstrap replicates each.
- Full pipeline: stage not stated [IQ-TREE v2.1.1, RAxML v8.2.12, phytools v2.3]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Version used: **1.1.0**
- Evidence: We estimated the final Gobioidei phylogeny using RAxML-NG v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Heterochronic shifts in a timing-keeping microRNA are associated with multiple instances of neoteny in plants. (PNAS 2025)

- DOI: 10.1073/pnas.2510697122 | PMCID: PMC12541458 | PMID: 41060751
- Version used: **8.2**
- Evidence: For each supermatrix, maximum likelihood trees were generated using RAxML v8.2 ( 46 ) with the GTRGAMMA model of rate heterogeneity using the rapid bootstrapping mode with 100 searches.
- Full pipeline: differential/statistical testing [ggplot2] -> structure determination [phytools v1.9.1] -> stage not stated [RAxML v8.2]

### Convergent evolution of &lt;i&gt;NFP&lt;/i&gt;-facilitated root nodule symbiosis. (PNAS 2025)

- DOI: 10.1073/pnas.2424902122 | PMCID: PMC12452920 | PMID: 40924454
- Evidence: We estimated branch lengths for this tree with the RAxML-NG-estimate option ( 53 ) on a subset of eight nuclear housekeeping loci from ref.
- Full pipeline: stage not stated [BEDTools, BLAST, MAFFT, RAxML]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Version used: **8.2.12**
- Evidence: ProteinModelSelection.pl provided by RAxML (v.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Cenozoic geoclimatic changes drove the evolutionary dynamics of floristic endemism on the Qinghai-Tibet Plateau. (PNAS 2025)

- DOI: 10.1073/pnas.2426017122 | PMCID: PMC12232610 | PMID: 40549922
- Version used: **8.2.10**
- Evidence: ( 37 ), we first conducted maximum likelihood analyses in RAxML v.8.2.10 ( 61 ) and deleted the strongly conflicting taxa between the plastid and nuclear trees based on a threshold bootstrap value >70% ( 62 ).
- Full pipeline: differential/statistical testing [RAxML v8.2.10] -> stage not stated [BEAST v1.8.4, R]

### Deep origins, distinct adaptations, and species-level status indicated for a glacial relict seal. (PNAS 2025)

- DOI: 10.1073/pnas.2503368122 | PMCID: PMC12207470 | PMID: 40493204
- Version used: **8.2.12**
- Evidence: The phylogenetic tree was inferred with RAxML v.8.2.12 ( 90 ) using the model ASC_GTRGAMMA and correcting for the invariable sites (totaling 9,945) missing from the VCF file with the option --asc-corr=felsenstein.
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, RAxML v8.2.12, VCFtools]

### Anthropogenic iron alters the spring phytoplankton bloom in the North Pacific transition zone. (PNAS 2025)

- DOI: 10.1073/pnas.2418201122 | PMCID: PMC12168011 | PMID: 40455985
- Evidence: Environmental hits were further selected by RAxML Evolutionary Placement Algorithm (-m PROTGAMMAILG) ( 65 ) analysis onto their respective RAxML-generated reference trees ( 66 ).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [kallisto] -> stage not stated [HMMER v3.1b, RAxML]

### Identification of the lydiamycin biosynthetic gene cluster in a plant pathogen guides structural revision and identification of molecular target. (PNAS 2025)

- DOI: 10.1073/pnas.2424388122 | PMCID: PMC12130866 | PMID: 40388608
- Evidence: Sequences were aligned using ClustalW ( 74 ) and a phylogenetic tree was inferred using RAxML ( 75 ) at the CIPRES science gateway ( 76 ).
- Full pipeline: alignment/mapping [ChimeraX v1.5, Clustal Omega, RAxML] -> visualisation [Cytoscape v3.8.2] -> stage not stated [ColabFold v1.2]

### Distinct latitudinal patterns of molecular rates across vertebrates. (PNAS 2025)

- DOI: 10.1073/pnas.2423386122 | PMCID: PMC12088427 | PMID: 40339119
- Version used: **8.2.4**
- Evidence: We inferred the maximum likelihood (ML) topologies from nucleotide sequences using RAxML 8.2.4 ( 42 ), which constrains deep nodes at the order or family level with established backbone trees of birds ( 43 , 44 ), mammals ( 45 ), amphibians ( 46 ), reptiles ( 47 , 48 ), and fishes ( 24 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [R, RAxML v8.2.4, phytools]

### Distinguishing species boundaries from geographic variation. (PNAS 2025)

- DOI: 10.1073/pnas.2423688122 | PMCID: PMC12088384 | PMID: 40324080
- Evidence: We inferred a phylogenetic tree for the filtered concatenated SNP dataset under maximum likelihood using RAxML-ng v.0.8.0 ( 35 , 36 ) with the general time-reversible substitution model with a Γ correction, 10 random starting trees, and with 200 nonparametric bootstrap replicates.
- Full pipeline: visualisation [ggplot2] -> stage not stated [ADMIXTURE v1.3.0, R, RAxML, VCFtools v0.1.13, tidyverse, vegan]

### Accurate, scalable, and fully automated inference of species trees from raw genome assemblies using ROADIES. (PNAS 2025)

- DOI: 10.1073/pnas.2500553122 | PMCID: PMC12088440 | PMID: 40314967
- Evidence: ( 40 ), was generated using 250 single-copy BUSCO genes (using Amino acid sequences) and running MAFFT, RAxML-NG, and ASTRAL-MP (in summary mode) sequentially.
- Full pipeline: stage not stated [BUSCO, MAFFT, RAxML, Snakemake]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Evidence: We aligned the gene sequences of all clownfish species and P. moluccensis with MAFFT [strategy L-INS-I; v.7.841; ( 68 )], and we reconstructed the gene trees with RAxML [GTR+G model, 100 bootstrap replicates; v.8.2.12; ( 69 )].
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### Archaeogenomic insights into commensalism and regional variation in pig management in Neolithic northwest Europe. (PNAS 2025)

- DOI: 10.1073/pnas.2410235122 | PMCID: PMC11962444 | PMID: 40096601
- Evidence: The mitochondrial phylogeny was constructed with RAxML ( 110 ).
- Full pipeline: variant calling [ADMIXTURE] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ANGSD] -> structure determination [ADMIXTURE, ANGSD] -> stage not stated [RAxML]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Evidence: Gene trees for summary MSC methods were estimated in RAxML v8 ( 122 ) using a GTRCAT model and 100 bootstrap replicates.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### Characterization of diverse Cas9 orthologs for genome and epigenome editing. (PNAS 2025)

- DOI: 10.1073/pnas.2417674122 | PMCID: PMC11929499 | PMID: 40073054
- Evidence: A tree was generated with Geneious by using the RAxML plugin with a GTR GAMMA nucleotide model, a rapid hill-climbing algorithm, and 20 replicates ( 58 ).
- Full pipeline: alignment/mapping [AlphaFold, MUSCLE v3.8.425] -> stage not stated [BLAST, RAxML]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Evidence: We then constructed a phylogenetic tree comprising the isolated bacterium and 20 other Serratia species using RAxML (randomized accelerated maximum likelihood) ( 24 ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Evidence: This alignment was used as input for RAxML (v8) ( 95 ) to construct a SNP phylogeny.
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

### Incomplete lineage sorting shaped mixed traits during a colobine primate radiation. (PNAS 2026)

- DOI: 10.1073/pnas.2524833123 | PMCID: PMC12867756 | PMID: 41576102
- Version used: **8.2.9**
- Evidence: For each dataset, maximum likelihood phylogenetic trees were constructed using RAxML v.8.2.9 ( 79 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold v2.3.1] -> stage not stated [BUSCO, RAxML v8.2.9]

### SARS-CoV-2 within-host diversity and transmission. (Science 2021)

- DOI: 10.1126/science.abg0821 | PMCID: PMC8128293 | PMID: 33688063
- Evidence: ( 42 ), in which 100 separate maximum likelihood phylogenies were generated using RAxML-NG ( 66 ) and the GTR+G substitution model, such that each reconstruction used a different random starting parsimony tree.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT] -> structure determination [IQ-TREE, RAxML] -> stage not stated [Docker, Pangolin]

### Evolution and host-specific adaptation of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (Science 2024)

- DOI: 10.1126/science.adi0908 | PMCID: PMC7618370 | PMID: 38963857
- Version used: **8.2.12**
- Evidence: The temporal signal was assessed with TempEst ( 68 ) by comparing collection dates with root-to-tip distances using non-dated phylogenetic tress inferred with RAxML 8.2.12 ( 69 ).
- Full pipeline: quality control [BWA] -> alignment/mapping [BWA, kallisto] -> quantification [DESeq2, kallisto] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEAST v6.6, RAxML v8.2.12, STRING db]

